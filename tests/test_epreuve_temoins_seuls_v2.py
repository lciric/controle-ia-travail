"""Essais de `scripts/epreuve_temoins_seuls_v2.py` : adaptateur simulé, aucun appel, dossier imposé détourné vers tmp_path."""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

RACINE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("epreuve_temoins_seuls_v2", RACINE / "scripts" / "epreuve_temoins_seuls_v2.py")
ep = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = ep
spec.loader.exec_module(ep)
IDN, TEMOINS, CLE, CONSIGNE = ep.preparer()


class Faux:
    def __init__(self, mode):
        self.mode, self.appels = mode, 0

    def lancer(self, role, consigne, dossier, budget, tours, modele=None):
        self.appels += 1
        assert role == "juge_ideation" and modele == ep.MODELE and budget == 0.5 and consigne == CONSIGNE
        if self.mode == "exception":
            raise RuntimeError("relais injoignable")
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
        texte = "```json\n" + json.dumps({"notes": notes, "doublons": [paire]}) + "\n```"
        if self.mode == "illisible":
            texte = "pas de bloc"
        return SimpleNamespace(statut="erreur" if self.mode == "erreur" else "ok", cout=0.12, texte=texte, texte_brut=texte,
                               modele_servi="claude-opus-4-6" if self.mode == "autre_modele" else ep.MODELE,
                               refus={"motif": "x"} if self.mode == "refus" else None, erreur=None)


@pytest.fixture
def sortie(tmp_path, monkeypatch):
    s = tmp_path / "runs" / "epreuve-temoins-seuls-v2"
    monkeypatch.setattr(ep, "SORTIE", str(s))
    return s


@pytest.mark.parametrize("mode,code", [("sain", 0), ("artefact", 4), ("erreur", 3), ("refus", 3), ("autre_modele", 3),
                                       ("illisible", 3), ("exception", 3)])
def test_codes(sortie, mode, code, capsys):
    f = Faux(mode)
    assert ep.main([], adaptateur=f) == code and f.appels == 1
    issue = json.loads((sortie / "issue.json").read_text())
    assert issue["code"] == code and issue["consigne_sha256"] == ep.CONSIGNE_ATTENDUE
    assert (sortie / "consigne.md.sha256").exists()


def test_jamais_rejouee_quelle_que_soit_l_issue(sortie):
    assert ep.main([], adaptateur=Faux("erreur")) == 3
    f = Faux("sain")
    assert ep.main([], adaptateur=f) == 2 and f.appels == 0


def test_consigne_d_empreinte_differente_refusee_sans_appel(sortie, monkeypatch):
    monkeypatch.setattr(ep, "CONSIGNE_ATTENDUE", "0" * 64)
    f = Faux("sain")
    assert ep.main([], adaptateur=f) == 2 and f.appels == 0 and not sortie.exists()


def test_piece_alteree_refusee_en_code_2(sortie, monkeypatch):
    monkeypatch.setitem(ep.PIECES, "temoins", (ep.PIECES["temoins"][0], "0" * 64))
    f = Faux("sain")
    assert ep.main([], adaptateur=f) == 2 and f.appels == 0


def test_a_sec_et_dossier(sortie, tmp_path):
    assert ep.main(["--a-sec", "--dossier", str(tmp_path / "sec")]) == 0
    assert ep.main(["--a-sec", "--dossier", str(sortie)]) == 2  # jamais le dossier imposé
    assert ep.main(["--dossier", str(tmp_path / "x")]) == 2     # --dossier sans --a-sec


def test_consigne_epinglee_et_temoins_v4():
    assert ep.sha(CONSIGNE.encode("utf-8")) == ep.CONSIGNE_ATTENDUE
    assert ep.PIECES["temoins"][0] == "temoins-organisme-discrets-v4.json"
    assert ep.PLAFOND_SESSION_USD == 0.5 and ep.MODELE == "claude-opus-5-5"
