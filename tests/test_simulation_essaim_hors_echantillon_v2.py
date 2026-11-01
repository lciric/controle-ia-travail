"""Préenregistrement hors échantillon, version 2 des modules (contre-lecture 1 : C1, C3, C5, C6, C9 ; R1, R2, R3, R6).
Instrument seulement (R1, R5) : aucune cellule de la grille n'est calculée ; mini-grille, dépôt jetable, données P3
factices ; formes closes éprouvées sur des configurations jetables. Graines de test : SeedSequence(97532), (24681).
"""
import copy
import json
from pathlib import Path

import numpy as np
import pytest

from conftest import committer
from controle_ia.gardes import GardeArret
from controle_ia.simulation_essaim import bornes_synchro_v1 as BS1
from controle_ia.simulation_essaim import bornes_synchro_v2 as BS2
from controle_ia.simulation_essaim import calibrage as C
from controle_ia.simulation_essaim import lecture_hors_echantillon_v1 as L1
from controle_ia.simulation_essaim import lecture_hors_echantillon_v2 as L2
from controle_ia.simulation_essaim import menaces as M
from controle_ia.simulation_essaim import run_essaim_hors_echantillon_v1 as RUN1
from controle_ia.simulation_essaim import run_essaim_hors_echantillon_v2 as RUN2
from controle_ia.simulation_essaim import statistiques as S
from controle_ia.simulation_essaim.loi_p3_v1 import SONDES
from test_simulation_essaim_hors_echantillon_v1 import _mini_grille, _preparer as _preparer_v1

RACINE = Path(__file__).resolve().parents[1]
DOSSIER = RACINE / "brouillons" / "preuves-mentors-v1" / "essaim-hors-echantillon-v1"
BROUILLON2 = DOSSIER / "preenregistrement-essaim-hors-echantillon-v1-brouillon2.md"
GRILLE2 = DOSSIER / "grille-essaim-hors-echantillon-v1-brouillon2.json"


# --- R6 : puissance exacte ---
def test_puissance_exacte_egale_inclusion_exclusion_complete_et_dans_les_bandes():
    for K, T, m in ((5, 6, 2), (5, 6, 5), (6, 8, 3)):
        for j in (2, 3):
            v, e = BS2.proba_max_au_moins(K, T, m, 0.1, j)
            v0, e0 = BS2.proba_max_au_moins(K, T, m, 0.1, j, tol=0.0)      # tous les ordres
            assert e0 == 0.0 and abs(v - v0) <= e + 1e-13
            bas, haut = BS1.bornes_union(K, T, m, 0.1, j)
            assert bas - 1e-10 <= v <= haut + 1e-10                  # arrondis de deux calculs exacts


def test_puissance_exacte_contre_monte_carlo_jetable():
    g = np.random.default_rng(np.random.SeedSequence(97532))
    K, T, q = 5, 7, 0.1
    s = BS1.seuil_coelev_exact(K, T, q, 0.05)
    Y = g.standard_normal((80000, K, T))
    X = M.synchro(Y, 3, 1, g)[0]
    p = float(C.alarme(S.coelev_comptage(X, C.seuil_par_case(q)).astype(float), g.random(80000), s).mean())
    v, _ = BS2.puissance_exacte(K, T, 3, q, s)
    assert abs(p - v) < 0.006


def test_puissance_exacte_gardes():
    with pytest.raises(GardeArret):
        BS2.puissance_exacte(5, 7, 2, 0.1, (2.5, 0.3))                     # artefact : seuil non entier
    with pytest.raises(GardeArret):
        BS2.proba_max_au_moins(5, 7, 6, 0.1, 2)                            # artefact : m > K
    assert BS2.proba_max_au_moins(5, 7, 2, 0.1, 0) == (1.0, 0.0) and BS2.proba_max_au_moins(5, 7, 2, 0.1, 6) == (0.0, 0.0)


# --- critère bilatéral (R2) ---
def test_entre_valeurs():
    assert L2.entre_valeurs(14000, 20000, 0.55, 0.86, 1e-5)[0] == "conforme"
    assert L2.entre_valeurs(18600, 20000, 0.55, 0.86, 1e-5)[0] == "contraire"      # loi de référence : 0,93
    assert L2.entre_valeurs(10000, 20000, 0.55, 0.86, 1e-5)[0] == "contraire"
    assert L2.entre_valeurs(11100, 20000, 0.55, 0.86, 1e-5)[0] == "non concluant"


# --- grille brouillon 2 : décompte par nature, discriminantes, scission de HP.5 ---
def test_grille_v2_decompte_et_discriminantes():
    g = json.loads(GRILLE2.read_text(encoding="utf-8"))
    d = L2.decompte(g)
    assert d["total"] == {"predictions": 19, "cellules": 311} and d["trajectorielles"] == 33
    assert d["instrument"] == {"predictions": 11, "cellules": 244}
    assert d["rejouée"] == {"predictions": 1, "cellules": 2}
    assert d["risquée"] == {"predictions": 7, "cellules": 65}
    assert d["discriminantes"] == 18
    n = L2.cellules_prevues(g)
    assert n["HP.5a"] == 7 and n["HP.5b"] == 13 and n["HP.6"] == 13 and n["HP.4"] == 2
    hp5a = [p for p in g["predictions"] if p["pred"] == "HP.5a"]
    assert all(p["sens"] == "en_dessous" and p["cellule"].startswith("P/" + SONDES[1]) for p in hp5a)
    hp4 = {p["cellule"].split("/")[1]: (p["valeur_bas"], p["valeur_haut"]) for p in g["predictions"] if p["pred"] == "HP.4"}
    assert hp4 == {SONDES[0]: (0.55, 0.86), SONDES[1]: (0.31, 0.62)}
    assert all(p["pred"] in L2.RISQUEES + L2.REJOUEE + L2.INSTRUMENT for p in g["predictions"])
    assert all(not p["discriminante"] for p in g["predictions"] if L2.nature(p["pred"]) != "risquée")
    assert set(L2.STATUTS) >= set(n) and "HP.5" not in L2.STATUTS


# --- C3 : table des énoncés recopiée dans le texte ---
def test_table_E_recopiee_dans_le_brouillon2():
    texte = BROUILLON2.read_text(encoding="utf-8")
    assert L2.table_E_md() in texte
    assert L2.PHRASE_PORTEE in texte
    for interdit in ("loi honnête réelle", "sur données réelles", "mécanisme confirmé", "modèle de substitution confirmé"):
        assert interdit not in L2.table_E_md() and interdit not in L2.PHRASE_PORTEE
    assert "`<<COMMIT_CITE>>`" in texte and "<<CONTRE_LECTURE_2>>" in texte          # C8


# --- C1, C6 : scores et « trop beau » (cas sain, artefact) ; lecture v2 = v1 hors HS.3 et HP.4 ---
def _mini_grille_v2(sha):
    g = _mini_grille(sha)
    g["descriptif_maxima"] = {"R": 300}
    g["predictions"] = [
        {"pred": "HS.4", "cellule": "S/e4x5/T_synchro_m4", "alarme": "coelev_comptage", "sens": "au_dessus",
         "discriminante": False},
        {"pred": "HS.5", "cellule": "S/e4x5/T_synchro_m2", "alarme": "e_coelev_cal", "sens": "au_plus", "discriminante": False},
        {"pred": "HQ.5", "cellule": "Q/e4x5/c0.3/T_synchro_m2", "alarme": "coelev_comptage", "sens": "en_dessous",
         "discriminante": True},
        {"pred": "HP.4", "cellule": "P/" + SONDES[0] + "/T_synchro_m3", "alarme": "coelev_comptage", "sens": "entre_x",
         "valeur_bas": 0.0, "valeur_haut": 1.0, "discriminante": True},
        {"pred": "HP.5b", "cellule": "P/" + SONDES[0] + "/T_synchro_m3", "alarme": "pas_moyenne", "sens": "au_plus",
         "discriminante": False}]
    return g


def _preparer(depot):
    from controle_ia.prereg import sceller_prereg
    from controle_ia.scellement import sceller
    from controle_ia.simulation_essaim.loi_p3_v1 import empreinte_fichier
    import subprocess
    from test_simulation_essaim_hors_echantillon_v1 import _fausses_donnees
    from test_simulation_essaim_v1 import PREREG_MINI

    (depot / "donnees").mkdir()
    np.savez(depot / "donnees" / "f.npz", **_fausses_donnees(graine=24681))
    (depot / "src").mkdir(exist_ok=True)
    (depot / "src" / "code_factice.py").write_text("X = 1\n", encoding="utf-8")
    gp = depot / "grille.json"
    gp.write_text(json.dumps(_mini_grille_v2(empreinte_fichier(depot / "donnees" / "f.npz"))), encoding="utf-8")
    sha = sceller(gp)
    committer(depot)
    commit = subprocess.run(["git", "-C", str(depot), "rev-parse", "HEAD"], capture_output=True, text=True,
                            check=True).stdout.strip()
    pp = depot / "prereg.md"
    pp.write_text(PREREG_MINI.format(sha=sha, commit=commit), encoding="utf-8")
    sceller_prereg(pp)
    committer(depot)
    return pp, gp


def _resultats(depot, run_id):
    from controle_ia.manifeste import verifier_resultat

    d = depot / "diag" / run_id
    return {f: verifier_resultat(depot, d / f"bloc-{f}.json")["resultat"] for f in ("S", "Q", "P")}


def test_chaine_v2_scores_trop_beau_et_egalite_avec_v1(depot):
    from controle_ia.manifeste import lire_manifeste, verifier_resultat

    pp, gp = _preparer(depot)
    sortie = RUN2.executer(depot, pp, gp, "20261102-010000-mini", verifier_import=False)
    corps = verifier_resultat(depot, sortie["lecture"])["resultat"]
    lec = corps["lecture"]
    sc = corps["scores"]
    assert sc["instrument"]["n"] == 11 and sc["rejouee"]["n"] == 1 and sc["risquees"]["n"] == 7
    assert sc["risquees"]["discriminantes"]["n"] == 2
    assert all(x["nature"] in ("instrument", "rejouée", "risquée") for x in lec["predictions"].values())
    a = lec["audit_symetrie"]
    assert a["audit_declenche"] == (a["audit_variances"] or a["trop_beau"])
    # lecture v2 = lecture v1, cellule par cellule, hors HS.3 (valeur exacte) et HP.4 (bilatérale)
    grille = json.loads(gp.read_text())
    res = _resultats(depot, "20261102-010000-mini")
    v1 = L1.lire(res, {**grille, "predictions": [p for p in grille["predictions"] if p["sens"] != "entre_x"]})
    for pred, x in lec["predictions"].items():
        if pred in ("HS.3", "HP.4"):
            continue
        assert sorted((c["nom"], c["etat"]) for c in x["cellules"]) == \
            sorted((c["nom"], c["etat"]) for c in v1["predictions"][pred]["cellules"]), pred
        assert x["verdict"] == v1["predictions"][pred]["verdict"]
    assert lec["predictions"]["HS.3"]["n_cellules"] == 3                        # 2 valeurs exactes + borne à m = K
    md = (depot / "diag" / "20261102-010000-mini" / "lecture.md").read_text(encoding="utf-8").splitlines()
    assert md[2] == L2.PHRASE_PORTEE and md[4].startswith("## Scores")
    jg = verifier_resultat(depot, depot / "diag" / "20261102-010000-mini" / "journal-git.json")["resultat"]
    assert jg["log"] and jg["reflog"]                                           # C5 : journal git versé
    mx = verifier_resultat(depot, depot / "diag" / "20261102-010000-mini" / "descriptif-maxima.json")["resultat"]
    assert len(mx["P"]) == 2 and sum(mx["P"][0]["histogramme_argmax"]) == mx["P"][0]["agents"] == 300 * 3
    m, _ = lire_manifeste(depot / "runs" / "20261102-010000-mini" / "manifeste.json")
    assert m["config"]["lanceur"] == RUN2.LANCEUR and "P/" + SONDES[0] + "/maxima" in m["graines"]
    committer(depot)
    with pytest.raises(GardeArret, match="existe déjà"):                        # run unique commun aux lanceurs
        RUN1.executer(depot, pp, gp, "20261102-010001-mini", verifier_import=False)


def test_trop_beau_cas_sain_et_artefact():
    base = {"predictions": {p: {"verdict": "confirmée", "cellules": [{"nom": p, "etat": "conforme", "genre": "statistique",
                                                                        "discriminante": p == "HQ.5"}]}
                            for p in L2.INSTRUMENT + L2.REJOUEE + L2.RISQUEES},
            "audit_symetrie": {"formes_closes": {"hors_bornes": False}, "egalites": {"hors_bornes": False}}}
    tout = L2.annoter(base)
    assert tout["audit_symetrie"]["trop_beau"] and tout["audit_symetrie"]["audit_declenche"]     # artefact : trop beau
    assert L2.annoter(tout)["scores"] == tout["scores"]                                         # idempotent
    une = copy.deepcopy(base)
    une["predictions"]["HP.6"]["verdict"] = "non concluante"
    une["predictions"]["HQ.5"]["cellules"][0]["etat"] = "non concluant"
    une["predictions"]["HQ.5"]["verdict"] = "non concluante"
    sain = L2.annoter(une)
    assert not sain["audit_symetrie"]["trop_beau"] and not sain["audit_symetrie"]["audit_declenche"]
    une["predictions"]["HQ.5"]["cellules"][0]["etat"] = "conforme"                              # toutes discriminantes
    assert L2.annoter(une)["audit_symetrie"]["trop_beau_detail"]["toutes_discriminantes_conformes"]


# --- C9 : gardes du lanceur (réplication, réplication unique, rien à répliquer, durée, données absentes) ---
def _forcer(monkeypatch, transformer):
    vraie = L2.LecteurHOv2.lire

    def lire(self):
        return transformer(vraie(self))

    monkeypatch.setattr(L2.LecteurHOv2, "lire", lire)


def test_replication_rien_a_repliquer(depot, monkeypatch):
    pp, gp = _preparer(depot)

    def aucune(lec):
        for x in lec["predictions"].values():
            x["a_repliquer"] = []
        return lec

    _forcer(monkeypatch, aucune)
    RUN2.executer(depot, pp, gp, "20261102-020000-mini", verifier_import=False)
    monkeypatch.undo()
    committer(depot)
    with pytest.raises(GardeArret, match="rien à répliquer"):
        RUN2.executer(depot, pp, gp, "20261102-020001-mini", replication_de="20261102-020000-mini", verifier_import=False)


def test_replication_repliquee_puis_seconde_refusee(depot, monkeypatch):
    from controle_ia.manifeste import lire_manifeste, verifier_resultat

    pp, gp = _preparer(depot)
    forcee = {}

    def une_contraire(lec):                      # une cellule statistique de HS.2 rendue contraire
        x = lec["predictions"]["HS.2"]
        c = x["cellules"][0]
        c["etat"] = "contraire"
        forcee["nom"] = c["nom"]
        x["verdict"], x["a_repliquer"] = "réfutée", [c["nom"]]
        for p, y in lec["predictions"].items():
            if p != "HS.2":
                y["a_repliquer"] = []
        return lec

    _forcer(monkeypatch, une_contraire)
    RUN2.executer(depot, pp, gp, "20261102-030000-mini", verifier_import=False)
    monkeypatch.undo()
    with pytest.raises(GardeArret, match="non propre"):
        RUN2.executer(depot, pp, gp, "20261102-030001-mini", replication_de="20261102-030000-mini", verifier_import=False)
    committer(depot)
    sortie = RUN2.executer(depot, pp, gp, "20261102-030001-mini", replication_de="20261102-030000-mini",
                           verifier_import=False)
    m, _ = lire_manifeste(depot / "runs" / "20261102-030001-mini" / "manifeste.json")
    assert m["config"]["familles"] == ["S"] and "S/e4x5/T_synchro_m2/replication" in m["graines"]
    corps = verifier_resultat(depot, sortie["lecture"])["resultat"]
    hs2 = {c["nom"]: c for c in corps["lecture_finale"]["predictions"]["HS.2"]["cellules"]}
    assert hs2[forcee["nom"]]["replication"] in ("conforme", "contraire")
    assert "scores" in corps["lecture_finale"] and corps["scores"] == corps["lecture_finale"]["scores"]
    assert not (depot / "diag" / "20261102-030001-mini" / "descriptif-maxima.json").exists()
    committer(depot)
    with pytest.raises(GardeArret, match="existe déjà"):
        RUN2.executer(depot, pp, gp, "20261102-030002-mini", replication_de="20261102-030000-mini", verifier_import=False)


def test_garde_duree_et_donnees_absentes(depot):
    pp, gp = _preparer(depot)
    with pytest.raises(GardeArret, match="durée"):
        RUN2.executer(depot, pp, gp, "20261102-040000-mini", limite_s=0.0, verifier_import=False)
    import shutil

    shutil.rmtree(depot / "runs")
    shutil.rmtree(depot / "diag")
    (depot / "donnees" / "f.npz").unlink()
    committer(depot)
    with pytest.raises(GardeArret, match="absentes"):
        RUN2.executer(depot, pp, gp, "20261102-040001-mini", verifier_import=False)


def test_lecture_v2_garde_erreur_certifiee(monkeypatch):
    monkeypatch.setattr(BS2, "puissance_exacte", lambda *a: (0.5, 1e-3))      # artefact : erreur non certifiée
    lec = L2.LecteurHOv2({"S": {"calibrage": {"e4x5": {"alarmes_p0": {}, "R0": 1, "seuils": {"coelev_comptage": [1, 0.5]}}},
                                "cellules": [{"cfg": "e4x5", "nom": "T_synchro_m2", "K": 4, "T": 5, "m": 2, "R": 10,
                                              "alarmes": {"coelev_comptage": 3}, "valeurs_differentes": {},
                                              "discordances": {}, "invariantes": []}]}},
                         {"alpha": 0.05, "q": 0.1, "lecture": {"gamma": 1e-5}, "predictions": []})
    with pytest.raises(GardeArret, match="erreur certifiée"):
        lec.S()
