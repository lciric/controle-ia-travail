"""Préenregistrement hors échantillon, modules v3 (contre-lecture 2 : M1 à M4, M7, M9, M12 ; Ra, Rb, Rc, Re).
Instrument seulement (R1, R5) : aucune cellule de la grille n'est calculée ; mini-grille, dépôt jetable, données P3
factices (`test_simulation_essaim_hors_echantillon_v2._preparer`). Graine de test : SeedSequence(31415).
"""
import json
import re
import shutil
from pathlib import Path

import numpy as np
import pytest

from conftest import committer
from controle_ia.gardes import GardeArret
from controle_ia.simulation_essaim import blocs_hors_echantillon_v3 as BH3
from controle_ia.simulation_essaim import bornes_synchro_v2 as BS2
from controle_ia.simulation_essaim import lecture_hors_echantillon_v1 as L1
from controle_ia.simulation_essaim import lecture_hors_echantillon_v2 as L2
from controle_ia.simulation_essaim import lecture_hors_echantillon_v3 as L3
from controle_ia.simulation_essaim import run_essaim_hors_echantillon_v1 as RUN1
from controle_ia.simulation_essaim import run_essaim_hors_echantillon_v2 as RUN2
from controle_ia.simulation_essaim import run_essaim_hors_echantillon_v3 as RUN3
from controle_ia.simulation_essaim import statistiques as S
from controle_ia.simulation_essaim.loi_p3_v1 import SONDES
from controle_ia.simulation_t03.lecture import fusionner
from test_simulation_essaim_hors_echantillon_v2 import _preparer, _resultats

RACINE = Path(__file__).resolve().parents[1]
DOSSIER = RACINE / "brouillons" / "preuves-mentors-v1" / "essaim-hors-echantillon-v1"
BROUILLON3 = DOSSIER / "preenregistrement-essaim-hors-echantillon-v1-brouillon3.md"
GRILLE1 = DOSSIER / "grille-essaim-hors-echantillon-v1-brouillon1.json"
GRILLE2 = DOSSIER / "grille-essaim-hors-echantillon-v1-brouillon2.json"


# --- M1, M3, M4, M12 : le texte qui sera scellé ---
def test_table_E_et_marqueurs_du_brouillon3():
    texte = BROUILLON3.read_text(encoding="utf-8")
    assert L3.table_E_md() in texte and L3.PHRASE_PORTEE in texte
    assert len(re.findall(r"<<[A-Z0-9_]+>>", texte)) == 2                       # M1 : exactement deux marqueurs
    assert texte.count("`<<COMMIT_CITE>>`") == 1 and texte.count("<<CONTRE_LECTURE_3>>") == 1
    assert "<<CONTRE_LECTURE_2>>" not in texte
    assert "seules les risquées et la rejouée peuvent échouer sans bogue" in L3.PHRASE_PORTEE   # M4
    assert L3.PHRASE_PORTEE != L2.PHRASE_PORTEE
    for interdit in ("loi honnête réelle", "sur données réelles", "mécanisme confirmé", "modèle de substitution confirmé"):
        assert interdit not in L3.table_E_md() and interdit not in L3.PHRASE_PORTEE
    hp5a = next(l for l in L3.LIGNES_E if l["exiges"] == ["HP.5a"])
    assert "aucune prédiction de référence à m = 3 et 4" in hp5a["lecture"]           # M3
    assert [l["exiges"] for l in L3.LIGNES_E] == [l["exiges"] for l in L2.LIGNES_E]
    assert run_cite(texte) == RUN3.LANCEUR


def run_cite(texte):
    m = re.search(r"-m (controle_ia\.simulation_essaim\.run_essaim_hors_echantillon_v\d)", texte)
    return m.group(1) if m else None


def test_grille_v2_memes_cellules_et_sens_que_v1():
    g1 = json.loads(GRILLE1.read_text(encoding="utf-8"))
    g2 = json.loads(GRILLE2.read_text(encoding="utf-8"))
    assert {k: v for k, v in g1.items() if k not in ("predictions", "version")} == \
        {k: v for k, v in g2.items() if k not in ("predictions", "version", "descriptif_maxima")}
    cle = lambda p: (p["cellule"], p["alarme"], p["pred"] == "HP.4")       # noqa: E731 (HP.4 et HP.5b partagent leur cellule)
    p1, p2 = {cle(p): p for p in g1["predictions"]}, {cle(p): p for p in g2["predictions"]}
    assert p1.keys() == p2.keys() and len(p2) == len(g2["predictions"]) == 84
    for k, a in p1.items():
        b = p2[k]
        if a["pred"] == "HP.4":
            assert b["sens"] == "entre_x" and b["valeur_bas"] == a["valeur"]
        else:
            assert b["sens"] == a["sens"]
            assert b["pred"] == a["pred"] or (a["pred"] == "HP.5" and b["pred"] in ("HP.5a", "HP.5b"))


def test_decompte_inchange_et_texte_fausses_confirmations():
    g2 = json.loads(GRILLE2.read_text(encoding="utf-8"))
    d = L3.decompte(g2)
    assert (d["instrument"]["cellules"], d["rejouée"]["cellules"], d["risquée"]["cellules"], d["discriminantes"]) == \
        (244, 2, 65, 18)
    sens = [p["sens"] for p in g2["predictions"] if L3.nature(p["pred"]) == "risquée"]
    assert (sens.count("au_dessus"), sens.count("en_dessous"), sens.count("entre_x"), sens.count("au_plus")) == \
        (21, 22, 2, 20)                                                         # M5 : 45 cellules garanties ≤ γ


# --- M2 : départage uniforme des ex aequo de C_t ---
def test_pas_de_coelevation_departage_uniforme():
    g = np.random.default_rng(np.random.SeedSequence(31415))
    C = np.zeros((40000, 10), dtype=np.int64)                                  # tous ex aequo
    h = np.bincount(BH3.pas_de_coelevation(C, g), minlength=10) / 40000
    assert np.all(np.abs(h - 0.1) < 0.01)                                      # v2 donnait toujours le pas 0
    C2 = np.zeros((5, 10), dtype=np.int64)
    C2[:, 7] = 1
    assert np.all(BH3.pas_de_coelevation(C2, g) == 7)                          # maximum unique : inchangé


# --- chaîne v3 : référence iid, Ra, Rb, version, run unique ---
def test_chaine_v3(depot):
    from controle_ia.manifeste import lire_manifeste, verifier_resultat

    pp, gp = _preparer(depot)
    sortie = RUN3.executer(depot, pp, gp, "20261102-110000-mini", verifier_import=False)
    corps = verifier_resultat(depot, sortie["lecture"])["resultat"]
    assert corps["lecture"]["lecture_version"] == L3.VERSION and "partielle" not in corps["lecture"]
    assert corps["scores"]["risquees"]["n"] == 7
    d = depot / "diag" / "20261102-110000-mini"
    mx = verifier_resultat(depot, d / "descriptif-maxima.json")["resultat"]
    assert len(mx["reference_iid"]) == 2 and len(mx["Q"]) == 1 and len(mx["P"]) == 2
    assert all("1/T n'est pas" in x["note"] for x in mx["reference_iid"] + mx["Q"] + mx["P"])
    m, _ = lire_manifeste(depot / "runs" / "20261102-110000-mini" / "manifeste.json")
    assert "P/reference-iid/maxima" in m["graines"] and "Q/e4x5/reference-iid/maxima" in m["graines"]
    assert m["config"]["lanceur"] == RUN3.LANCEUR
    jg = verifier_resultat(depot, d / "journal-git.json")["resultat"]
    assert {"log", "reflog", "statut", "arbres", "inaccessibles"} <= set(jg)              # Rb
    ps = verifier_resultat(depot, d / "puissances-exactes-S.json")["resultat"]            # Ra
    assert set(ps) == {"S/e4x5/T_synchro_m2", "S/e4x5/T_synchro_m4"} and all(x["erreur_certifiee"] <= 1e-6
                                                                              for x in ps.values())
    md = (d / "lecture.md").read_text(encoding="utf-8").splitlines()
    assert md[2] == L3.PHRASE_PORTEE and md[4].startswith("## Scores")
    committer(depot)
    for run in (RUN1, RUN2):                                                   # run unique commun aux trois lanceurs
        with pytest.raises(GardeArret, match="existe déjà"):
            run.executer(depot, pp, gp, "20261102-110001-mini", verifier_import=False)


def test_ra_garde_avant_tout_tirage(depot, monkeypatch):
    pp, gp = _preparer(depot)
    monkeypatch.setattr(BS2, "puissance_exacte", lambda *a: (0.5, 1e-3))      # artefact : erreur non certifiée
    with pytest.raises(GardeArret, match="avant tout tirage"):
        RUN3.executer(depot, pp, gp, "20261102-120000-mini", verifier_import=False)
    assert not (depot / "runs").exists()                                       # rien écrit, rien tiré


# --- M7 : garde d'équivalence des lanceurs v2 et v3 (artefact ; le cas sain est la chaîne) ---
@pytest.mark.parametrize("run", [RUN2, RUN3])
def test_garde_equivalence_lanceurs(depot, monkeypatch, run):
    pp, gp = _preparer(depot)
    vrai = S.agent_moyenne
    monkeypatch.setattr(S, "agent_moyenne", lambda Xb: vrai(Xb) + 1e-6)       # artefact : lots ≠ références scalaires
    with pytest.raises(GardeArret, match="équivalence"):
        run.executer(depot, pp, gp, "20261102-130000-mini", verifier_import=False)


# --- Rc, Re : réplication (lecture partielle ; états finaux = fusion v1) ---
def _forcer(monkeypatch, transformer):
    vraie = L2.LecteurHOv2.lire

    def lire(self):
        return transformer(vraie(self))

    monkeypatch.setattr(L2.LecteurHOv2, "lire", lire)


def _une_contraire(lec, forcee):
    x = lec["predictions"]["HS.2"]
    c = x["cellules"][0]
    c["etat"] = "contraire"
    forcee["nom"] = c["nom"]
    x["verdict"], x["a_repliquer"] = "réfutée", [c["nom"]]
    for p, y in lec["predictions"].items():
        if p != "HS.2":
            y["a_repliquer"] = []
    return lec


def test_replication_v3_partielle_et_fusion_egale_a_v1(depot, monkeypatch):
    from controle_ia.manifeste import verifier_resultat

    pp, gp = _preparer(depot)
    forcee = {}
    _forcer(monkeypatch, lambda lec: _une_contraire(lec, forcee))
    RUN3.executer(depot, pp, gp, "20261102-140000-mini", verifier_import=False)
    monkeypatch.undo()
    committer(depot)
    sortie = RUN3.executer(depot, pp, gp, "20261102-140001-mini", replication_de="20261102-140000-mini",
                           verifier_import=False)
    corps = verifier_resultat(depot, sortie["lecture"])["resultat"]
    assert corps["lecture"]["partielle"] is True and "scores" not in corps["lecture"]            # Rc
    assert "trop_beau" not in corps["lecture"]["audit_symetrie"]
    finale = corps["lecture_finale"]
    assert corps["scores"] == finale["scores"] and finale["lecture_version"] == L3.VERSION
    # Re : états finaux = fusion des lectures v1 (même cellule forcée), hors HS.3 et HP.4
    grille = json.loads(gp.read_text())
    g1 = {**grille, "predictions": [p for p in grille["predictions"] if p["sens"] != "entre_x"]}
    princ = _une_contraire(L1.lire(_resultats(depot, "20261102-140000-mini"), g1), {})
    res_rep = {"S": verifier_resultat(depot, depot / "diag" / "20261102-140001-mini" / "bloc-S.json")["resultat"]}
    fus1 = fusionner(princ, L1.lire(res_rep, g1))
    for pred, x in finale["predictions"].items():
        if pred in ("HS.3", "HP.4"):
            continue
        assert sorted((c["nom"], c["etat"]) for c in x["cellules"]) == \
            sorted((c["nom"], c["etat"]) for c in fus1["predictions"][pred]["cellules"]), pred
        assert x["verdict"] == fus1["predictions"][pred]["verdict"], pred
    hs2 = {c["nom"]: c for c in finale["predictions"]["HS.2"]["cellules"]}
    assert hs2[forcee["nom"]]["replication"] in ("conforme", "contraire")


# --- M9 : réplication refusée d'un run d'un autre lanceur ; le lanceur v1 sur ce texte, documenté ---
def test_replication_refusee_si_principal_non_v3(depot, monkeypatch):
    pp, gp = _preparer(depot)
    forcee = {}
    _forcer(monkeypatch, lambda lec: _une_contraire(lec, forcee))
    RUN2.executer(depot, pp, gp, "20261102-150000-mini", verifier_import=False)
    monkeypatch.undo()
    committer(depot)
    with pytest.raises(GardeArret, match="n'a pas été lancé par"):
        RUN3.executer(depot, pp, gp, "20261102-150001-mini", replication_de="20261102-150000-mini", verifier_import=False)


def test_lanceur_v1_sur_ce_texte_consomme_le_run_unique(depot):
    """Danger écrit en M9 : le lanceur v1 calcule tous les blocs puis échoue à la lecture (sens `entre_x` inconnu),
    sans `GardeArret` ; son run consomme le run unique. D'où l'interdiction écrite au préenregistrement."""
    pp, gp = _preparer(depot)
    with pytest.raises(KeyError, match="entre_x"):
        RUN1.executer(depot, pp, gp, "20261102-160000-mini", verifier_import=False)
    assert (depot / "diag" / "20261102-160000-mini" / "bloc-P.json").exists()
    shutil.rmtree(depot / "diag")                                              # sorties non lues
    committer(depot)
    with pytest.raises(GardeArret, match="existe déjà"):
        RUN3.executer(depot, pp, gp, "20261102-160001-mini", verifier_import=False)
