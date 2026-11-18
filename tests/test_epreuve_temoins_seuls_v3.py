"""Essais de `scripts/epreuve_temoins_seuls_v3.py` : résultat réel de l'adaptateur (`pole.adaptateurs.Resultat`), état du relais
et environnement simulés, aucun appel ; dossiers imposés détournés vers tmp_path."""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import pytest

RACINE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("epreuve_temoins_seuls_v3", RACINE / "scripts" / "epreuve_temoins_seuls_v3.py")
ep = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = ep
spec.loader.exec_module(ep)
IDN, TEMOINS, CLE, CONSIGNE = ep.preparer()
from pole.adaptateurs import Resultat  # noqa: E402 — chemin posé par preparer()

ETAT_SAIN = {"plafond_usd": 0.5, "reserve_par_appel_usd": 0.2, "modeles_permis": ["claude-opus-5-5"], "depense_usd": 0.0, "appels": 0}


class Faux:
    def __init__(self, mode):
        self.mode, self.appels = mode, 0

    def lancer(self, role, consigne, dossier, budget, tours, modele=None):
        self.appels += 1
        assert role == "juge_ideation" and modele == ep.MODELE and budget == 0.5 and consigne == CONSIGNE
        if self.mode == "exception":
            raise RuntimeError("relais injoignable")
        if self.mode == "interruption":
            raise KeyboardInterrupt()
        cls = {t["identifiant_auteur"]: t["temoin"]["classe"] for t in TEMOINS}
        inv = {v: k for k, v in CLE.items()}
        notes = []
        for e, ident in CLE.items():
            bon = cls[ident] in ("vrai", "jumeau")
            a = (2 if self.mode != "artefact" else 1) if bon else 0
            notes.append({"identifiant": e, "criteres": {"avantage": a, "originalite": a,
                          "falsifiabilite": 0 if cls[ident] == "faux_falsifiabilite" else 2, "traitabilite": 3, "robustesse": 1},
                          "justifications": {k: "x" for k in ("avantage", "originalite", "falsifiabilite", "traitabilite", "robustesse")}})
        paire = [inv[i] for i in CLE.values() if cls[i] in ("vrai", "jumeau")]
        texte = "pas de bloc" if self.mode == "illisible" else "```json\n" + json.dumps({"notes": notes, "doublons": [paire]}) + "\n```"
        return Resultat(texte_final=texte, cout_declare_usd=0.137, statut="erreur" if self.mode == "erreur" else "ok",
                        texte_brut=texte, refus={"motif": "x"} if self.mode == "refus" else None,
                        modele_servi="claude-opus-4-6" if self.mode == "autre_modele" else ep.MODELE)


@pytest.fixture
def sortie(tmp_path, monkeypatch):
    s = tmp_path / "runs" / "epreuve-temoins-seuls-v3"
    monkeypatch.setattr(ep, "SORTIE", str(s))
    import pole.adaptateurs as pa
    monkeypatch.setattr(pa, "importer_sdk", lambda: object())  # le kit n'est pas dans la venv des essais ; vérifié à part
    return s


def test_sans_kit_refus_avant_tentative(tmp_path, monkeypatch):
    """Sans le kit d'agents (venv des essais), le script refuse en code 2 avant de créer son dossier."""
    s = tmp_path / "runs" / "epreuve-temoins-seuls-v3"
    monkeypatch.setattr(ep, "SORTIE", str(s))
    import pole.adaptateurs as pa
    def absent():
        raise pa.MoteurIndisponible("kit absent")
    monkeypatch.setattr(pa, "importer_sdk", absent)
    f = Faux("sain")
    assert ep.main([], adaptateur=f, lire_etat=lambda: dict(ETAT_SAIN), environ={}) == 2 and f.appels == 0 and not s.exists()


def jouer(f, etat=ETAT_SAIN, environ=None):
    return ep.main([], adaptateur=f, lire_etat=lambda: dict(etat), environ=environ if environ is not None else {})


@pytest.mark.parametrize("mode,code", [("sain", 0), ("artefact", 4), ("erreur", 3), ("refus", 3), ("autre_modele", 3),
                                       ("illisible", 3), ("exception", 3), ("interruption", 3)])
def test_codes_et_cout_reel(sortie, mode, code):
    f = Faux(mode)
    assert jouer(f) == code and f.appels == 1
    issue = json.loads((sortie / "issue.json").read_text())
    assert issue["code"] == code and issue["consigne_sha256"] == ep.CONSIGNE_ATTENDUE
    if mode in ("exception", "interruption"):
        assert issue["cout_usd"] == 0.5 and issue["cout_inconnu"] is True
    else:
        assert issue["cout_usd"] == pytest.approx(0.137)  # le champ réel du résultat, jamais nul
    assert (sortie / "etat-relais-avant.json").exists() and (sortie / "cle-anonymisation.json").exists()


@pytest.mark.parametrize("ecart", [{"reserve_par_appel_usd": 0.4}, {"plafond_usd": 1.0}, {"modeles_permis": ["claude-opus-5-5", "x"]},
                                   {"depense_usd": 0.01}, {"appels": 1}])
def test_relais_non_conforme_refus_sans_tentative(sortie, ecart):
    f = Faux("sain")
    assert jouer(f, etat=dict(ETAT_SAIN, **ecart)) == 2 and f.appels == 0 and not sortie.exists()


def test_relais_illisible_refus(sortie):
    f = Faux("sain")
    def casse():
        raise OSError("refusé")
    assert ep.main([], adaptateur=f, lire_etat=casse, environ={}) == 2 and f.appels == 0 and not sortie.exists()


def test_cle_dans_l_environnement_refus(sortie):
    f = Faux("sain")
    assert jouer(f, environ={"ANTHROPIC_API_KEY": "x"}) == 2 and f.appels == 0 and not sortie.exists()


def test_une_seule_tentative_toutes_versions(sortie):
    (sortie.parent / "epreuve-temoins-seuls-v2").mkdir(parents=True)
    f = Faux("sain")
    assert jouer(f) == 2 and f.appels == 0


def test_jamais_rejouee(sortie):
    assert jouer(Faux("erreur")) == 3
    f = Faux("sain")
    assert jouer(f) == 2 and f.appels == 0


def test_consigne_epinglee_temoins_v5_reserve():
    assert ep.sha(CONSIGNE.encode("utf-8")) == ep.CONSIGNE_ATTENDUE
    assert ep.PIECES["temoins"][0] == "temoins-organisme-discrets-v5.json"
    assert ep.RESERVE_RELAIS_USD == 0.2 and 2 * ep.RESERVE_RELAIS_USD <= ep.PLAFOND_SESSION_USD
