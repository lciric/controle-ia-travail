"""Simulation d'essaim, lecture v2 et lanceur v2 (contre-lecture 1 : C5, C6, C7, C10). Instrument seulement (R1) :
aucun de ces tests ne calcule une cellule de la grille décisive (mini-grille de `test_simulation_essaim_v1`, dépôts
jetables, graines de test).

Couvre : table E en 9 lignes (textes C5 et C6, HE6 scindée), règle de prononcé inchangée ; statuts des prédictions et
appui exploratoire ; lecture v2 = lecture v1 + annotations (mêmes états et verdicts) ; phrase de portée et colonnes
du rendu `lecture.md` ; table E recopiée mot pour mot dans le préenregistrement ; run unique partagé entre lanceurs
v1 et v2 ; les deux branches de la réplication, forcées (C10 : couverture déterministe) ; gardes du lanceur v2
(artefacts, R5 ; le cas sain est la chaîne complète).
"""
import json
import math
from pathlib import Path

import numpy as np
import pytest

from conftest import committer
from controle_ia.gardes import GardeArret
from controle_ia.simulation_essaim import calibrage as C
from controle_ia.simulation_essaim import lecture as LEC1
from controle_ia.simulation_essaim import lecture_v2 as LEC2
from controle_ia.simulation_essaim import menaces as M
from controle_ia.simulation_essaim import run_essaim_v2 as RUN2
from controle_ia.simulation_essaim import statistiques as S
from test_simulation_essaim_v1 import ATTENDUES, _preparer

RACINE = Path(__file__).resolve().parents[1]
PREREG_SCELLE = RACINE / "prereg" / "essaim-simulation-v1.md"
PREREG_BROUILLON2 = (RACINE / "brouillons" / "preuves-mentors-v1" / "essaim-simulation-v1"
                     / "preenregistrement-essaim-simulation-v1-brouillon2.md")


# --- table E v2 ---
def test_lignes_E_v2_textes_et_scission():
    assert len(LEC2.LIGNES_E) == 9 and len(LEC1.LIGNES_E) == 8
    v1, v2 = LEC1.LIGNES_E, LEC2.LIGNES_E
    for i in (0, 1, 4, 5, 6):                                     # lignes inchangées
        assert v2[i] == v1[i], i
    for i in (2, 3):                                              # textes corrigés, mêmes prédictions
        assert v2[i]["enonce"] == v1[i]["enonce"] and v2[i]["exiges"] == v1[i]["exiges"]
        assert v2[i]["complementaires"] == v1[i]["complementaires"] and v2[i]["lecture"] != v1[i]["lecture"]
    assert "bornes inférieures exactes respectées" in v2[2]["lecture"] and "atteintes" not in v2[2]["lecture"]
    assert "dès que la moitié de l'essaim au moins se synchronise" in v2[2]["lecture"]
    assert "sans le démontrer pour le supremum sur n" in v2[3]["lecture"]
    assert "donc la concentration l'abaisse" not in v2[3]["lecture"]
    assert v2[3]["lecture"].endswith("tient à sa lecture en maximum sur les pas.")
    he6a, he6b = v2[7], v2[8]                                     # C7 : HE6 scindée
    assert he6a["enonce"].startswith("HE6a") and he6a["exiges"] == ["HE6.1", "HE6.2"]
    assert he6b["enonce"].startswith("HE6b") and he6b["exiges"] == ["HE6.3"]
    assert "Mécanisme conjecturé, non testé" in he6b["lecture"] and "arrachés" not in he6b["lecture"]
    preds = {p for ligne in v2 for p in ligne["exiges"] + ligne["complementaires"]}
    assert preds == {p for ligne in v1 for p in ligne["exiges"] + ligne["complementaires"]}
    assert {p.split(".")[0] for p in preds} <= set(LEC2.BLOCS_DE) and LEC2.BLOCS_DE == LEC1.BLOCS_DE


def test_prononce_v2_regle_inchangee():
    preds = {p for ligne in LEC2.LIGNES_E for p in ligne["exiges"] + ligne["complementaires"]}
    faux = {"predictions": {p: {"verdict": "confirmée"} for p in preds}}
    lignes = LEC2.enonces_du_programme(faux)
    assert len(lignes) == 9 and all(not x["lecture"].startswith("non établi") for x in lignes)
    faux["predictions"]["HE6.3"]["verdict"] = "non concluante"    # HE6b tombe, HE6a reste prononcée
    lignes = LEC2.enonces_du_programme(faux)
    assert [x["lecture"].startswith("non établi") for x in lignes] == [False] * 8 + [True]
    assert lignes[7]["lecture"].startswith("Oui : aveugle")
    faux["predictions"]["HE6.3"]["verdict"] = "confirmée"
    faux["predictions"]["HE2.5"]["verdict"] = "réfutée"
    assert sum(x["lecture"].startswith("non établi") for x in LEC2.enonces_du_programme(faux)) == 1
    del faux["predictions"]["HE4.4"]                              # prédiction absente : non établi
    assert LEC2.enonces_du_programme(faux)[5]["lecture"] == "non établi : voir HE4.4"


def test_statuts_et_appui_exploratoire():
    assert LEC2.statut("HE1.3") == LEC2.statut("HE6.3") == "exploratoire vu"
    assert LEC2.statut("HE1.1") == LEC2.statut("HE3.2") == "préenregistrée"
    assert LEC2.statut("HE2.4").startswith("en partie exploratoire vu") and "pas_moyenne" in LEC2.statut("HE2.4")
    assert LEC2.statut("HE3.3") == "en partie exploratoire vu : choix des cellules"
    assert (LEC2.EXPLORATOIRES | set(LEC2.EN_PARTIE)) <= ATTENDUES
    appuis = [LEC2.appui_exploratoire(ligne) for ligne in LEC2.LIGNES_E]
    assert appuis == [[], [], ["HE2.4"], ["HE2.5"], ["HE1.3", "HE2.4"], [], ["HE3.3"], [], ["HE6.3"]]


def test_annoter_ne_change_aucun_etat():
    lec = {"gamma": 1e-5, "audit_symetrie": {},
           "predictions": {"HE2.4": {"verdict": "confirmée", "cellules": [
               {"nom": "e/T_synchro_m5/coelev_comptage", "etat": "conforme"},
               {"nom": "e/T_synchro_m5/pas_moyenne", "etat": "conforme"},
               {"nom": "e/T_synchro_m5/coelev_somme3", "etat": "non concluant"}]},
               "HE1.1": {"verdict": "réfutée", "cellules": [{"nom": "e/A_rebrassage", "etat": "contraire"}]}}}
    avant = json.dumps(lec, sort_keys=True)
    a = LEC2.annoter(lec)
    assert json.dumps(lec, sort_keys=True) == avant                       # l'original n'est pas modifié
    assert LEC2.annoter(a) == a                                           # idempotent
    assert a["portee"] == LEC2.PHRASE_PORTEE and a["lecture_version"] == "lecture_v2"
    assert a["predictions"]["HE1.1"]["statut"] == "préenregistrée" and a["predictions"]["HE1.1"]["verdict"] == "réfutée"
    cel = a["predictions"]["HE2.4"]["cellules"]
    assert [c.get("statut") for c in cel] == [None, "exploratoire vu", "exploratoire vu"]
    assert [c["etat"] for c in cel] == ["conforme", "conforme", "non concluant"]


def test_table_E_md_et_recopie_dans_le_preenregistrement():
    t = LEC2.table_E_md()
    lignes = t.strip().splitlines()
    assert len(lignes) == 2 + 9 and lignes[0].startswith("| Énoncé |") and lignes[0].count("|") == 6
    for ligne, rendu in zip(LEC2.LIGNES_E, lignes[2:]):
        assert rendu.startswith(f"| {ligne['enonce']} | {ligne['lecture']} | ")
    assert lignes[-1].endswith("| HE6.3 | — | HE6.3 |")
    cible = PREREG_SCELLE if PREREG_SCELLE.exists() else PREREG_BROUILLON2
    if not cible.exists():
        pytest.skip("ni préenregistrement scellé ni brouillon 2 sur disque")
    assert t in cible.read_text(encoding="utf-8"), f"table E de {cible.name} ≠ lecture_v2.table_E_md()"


# --- chaîne complète sur la mini-grille, lanceur v2 ---
def _resultats_depuis_diag(dossier: Path) -> dict:
    lire = lambda nom: json.loads((dossier / f"{nom}.json").read_text(encoding="utf-8"))["resultat"]  # noqa: E731
    res = {"calibrage": lire("calibrage")["configs"]}
    for b in ("C", "M", "HE3", "HE6"):
        res[b] = lire(f"bloc-{b}")
    return res


def test_chaine_complete_v2_mini_grille(depot):
    from controle_ia.manifeste import lire_manifeste, verifier_resultat
    from controle_ia.scellement import empreinte, verifier
    from controle_ia.simulation_essaim.run_essaim import entropie_depuis_prereg
    from controle_ia.simulation_essaim.run_essaim import executer as executer_v1

    pp, gp = _preparer(depot)
    run = "20261101-140000-mini"
    sortie = RUN2.executer(depot, pp, gp, run, verifier_import=False)
    corps = verifier_resultat(depot, sortie["lecture"])["resultat"]
    lec = corps["lecture"]
    assert set(lec["predictions"]) == ATTENDUES
    assert all(x["statut"] == LEC2.statut(k) for k, x in lec["predictions"].items())
    for p in ("HE1.1", "HE2.1", "HE4.4", "HE5.2", "HE6.1"):           # trajectoriels : exacts même en petit
        assert lec["predictions"][p]["verdict"] == "confirmée", p
    assert corps["portee"] == lec["portee"] == LEC2.PHRASE_PORTEE and corps["lecture_version"] == "lecture_v2"
    prog = corps["programme"]
    assert len(prog) == 9 and [x["appui_exploratoire"] for x in prog] == [LEC2.appui_exploratoire(l) for l in LEC2.LIGNES_E]
    # lecture v2 = lecture v1 + annotations : mêmes cellules, mêmes états, mêmes verdicts
    grille = json.loads(gp.read_text(encoding="utf-8"))
    v1 = LEC1.lire(_resultats_depuis_diag(depot / "diag" / run), grille)
    assert set(v1["predictions"]) == set(lec["predictions"])
    for k, x in v1["predictions"].items():
        y = lec["predictions"][k]
        assert x["verdict"] == y["verdict"], k
        assert len(x["cellules"]) == len(y["cellules"]), k                # (l'ordre des clés JSON est trié)
        assert {c["nom"]: c["etat"] for c in x["cellules"]} == {c["nom"]: c["etat"] for c in y["cellules"]}, k
    # rendu : portée en tête (troisième ligne), colonnes statut et appui exploratoire
    md_chemin = depot / "diag" / run / "lecture.md"
    verifier(md_chemin)
    md = md_chemin.read_text(encoding="utf-8").splitlines()
    assert md[0].startswith("# Lecture gelée") and md[2] == LEC2.PHRASE_PORTEE
    assert "| prédiction | statut | verdict |" in "\n".join(md) and "| HE1.3 | exploratoire vu |" in "\n".join(md)
    assert "| énoncé | lecture | exigées | complémentaires | appui exploratoire |" in md
    assert sum(1 for l in md if l.startswith("| HE6a") or l.startswith("| HE6b")) == 2
    # manifeste : lanceur v2, même nom de simulation, règle de la graine
    m, _ = lire_manifeste(depot / "runs" / run / "manifeste.json")
    assert m["config"]["lanceur"] == RUN2.LANCEUR and m["config"]["simulation"] == "essaim-v1"
    assert m["config"]["lecture"] == "lecture_v2" and m["commande"].startswith(f"python -m {RUN2.LANCEUR} ")
    assert int(m["config"]["entropie"]) == entropie_depuis_prereg(empreinte(pp))
    # run unique, partagé entre les deux lanceurs
    with pytest.raises(GardeArret, match="existe déjà"):
        RUN2.executer(depot, pp, gp, "20261101-140001-mini", verifier_import=False)
    with pytest.raises(GardeArret, match="existe déjà"):
        executer_v1(depot, pp, gp, "20261101-140002-mini", verifier_import=False)


def test_run_v1_bloque_le_lanceur_v2(depot):
    """Réciproque : un run décisif par le lanceur v1 (hors commande citée) bloque le lanceur v2."""
    from controle_ia.scellement import empreinte
    from controle_ia.simulation_essaim import run_essaim as RUN1

    pp, gp = _preparer(depot)
    (depot / "runs" / "20261101-140100-mini").mkdir(parents=True)
    (depot / "runs" / "20261101-140100-mini" / "manifeste.json").write_text(json.dumps(
        {"run_id": "20261101-140100-mini", "decisif": True, "config": {"simulation": RUN1.SIMULATION},
         "preenregistrement": {"sha256": empreinte(pp)}}),
        encoding="utf-8")
    committer(depot)
    with pytest.raises(GardeArret, match="existe déjà"):
        RUN2.executer(depot, pp, gp, "20261101-140101-mini", verifier_import=False)


# --- C10 : les deux branches de la réplication, forcées ---
def _forcer_lecture(monkeypatch, transformer):
    vraie = LEC2.lire

    def lire(resultats, grille):
        return transformer(vraie(resultats, grille))

    monkeypatch.setattr(LEC2, "lire", lire)


def test_replication_branche_rien_a_repliquer(depot, monkeypatch):
    pp, gp = _preparer(depot)

    def aucune(lec):
        for x in lec["predictions"].values():
            x["a_repliquer"] = []
        return lec

    _forcer_lecture(monkeypatch, aucune)
    RUN2.executer(depot, pp, gp, "20261101-141000-mini", verifier_import=False)
    monkeypatch.undo()
    committer(depot)                           # runs/ et diag/ committés avant toute réplication (étape 0.f)
    with pytest.raises(GardeArret, match="rien à répliquer"):
        RUN2.executer(depot, pp, gp, "20261101-141001-mini", replication_de="20261101-141000-mini",
                      verifier_import=False)


def test_replication_branche_repliquee_puis_seconde_refusee(depot, monkeypatch):
    from controle_ia.manifeste import lire_manifeste, verifier_resultat

    pp, gp = _preparer(depot)
    forcees = {}

    def une_contraire(lec):                    # une cellule statistique de HE4.1 rendue contraire (classe M)
        x = lec["predictions"]["HE4.1"]
        c = next(c for c in x["cellules"] if c["genre"] == "statistique")
        c["etat"] = "contraire"
        forcees["nom"] = c["nom"]
        x["verdict"], x["a_repliquer"] = "réfutée", [c["nom"]]
        return lec

    _forcer_lecture(monkeypatch, une_contraire)
    RUN2.executer(depot, pp, gp, "20261101-142000-mini", verifier_import=False)
    monkeypatch.undo()
    with pytest.raises(GardeArret, match="non propre"):   # sans commit des sorties, la réplication s'arrête
        RUN2.executer(depot, pp, gp, "20261101-142001-mini", replication_de="20261101-142000-mini",
                      verifier_import=False)
    committer(depot)                           # runs/ et diag/ committés avant toute réplication (étape 0.f)
    sortie = RUN2.executer(depot, pp, gp, "20261101-142001-mini", replication_de="20261101-142000-mini",
                           verifier_import=False)
    m, _ = lire_manifeste(depot / "runs" / "20261101-142001-mini" / "manifeste.json")
    assert m["config"]["blocs"] == ["M"] and m["config"]["replication_de"] == "20261101-142000-mini"
    assert "calib/m3x6" in m["graines"] and "calib/m3x6/replication" in m["graines"]   # graines de réplication dérivées d'avance
    corps = verifier_resultat(depot, sortie["lecture"])["resultat"]
    finale = corps["lecture_finale"]
    he41 = {c["nom"]: c for c in finale["predictions"]["HE4.1"]["cellules"]}
    assert he41[forcees["nom"]]["replication"] in ("conforme", "contraire")
    assert he41[forcees["nom"]]["etat"] in ("non concluant", "contraire")
    assert finale["predictions"]["HE4.1"]["a_repliquer"] == [] and finale["predictions"]["HE4.1"]["statut"] == "préenregistrée"
    assert all("statut" in x for x in finale["predictions"].values()) and finale["portee"] == LEC2.PHRASE_PORTEE
    assert len(corps["programme"]) == 9
    md = (depot / "diag" / "20261101-142001-mini" / "lecture.md").read_text(encoding="utf-8").splitlines()
    assert md[2] == LEC2.PHRASE_PORTEE
    committer(depot)
    with pytest.raises(GardeArret, match="existe déjà"):
        RUN2.executer(depot, pp, gp, "20261101-142002-mini", replication_de="20261101-142000-mini",
                      verifier_import=False)


# --- gardes du lanceur v2 : artefacts (R5) ---
def test_garde_v2_blocs_et_commit_cite(depot):
    pp, gp = _preparer(depot)
    with pytest.raises(GardeArret, match="ne se choisissent pas"):
        RUN2.executer(depot, pp, gp, "20261101-143000-mini", blocs=["C"], verifier_import=False)
    (depot / "src" / "code_factice.py").write_text("X = 2\n", encoding="utf-8")
    committer(depot)
    with pytest.raises(GardeArret, match="modifiés depuis le commit cité"):
        RUN2.executer(depot, pp, gp, "20261101-143001-mini", verifier_import=False)


def test_garde_v2_prereg_altere_et_import(depot):
    pp, gp = _preparer(depot)
    with pytest.raises(GardeArret, match="hors de"):                     # code importé hors de racine/src
        RUN2.executer(depot, pp, gp, "20261101-143002-mini")
    pp.write_text(pp.read_text(encoding="utf-8") + "\nModifié après scellement.\n", encoding="utf-8")
    committer(depot)
    with pytest.raises(GardeArret):
        RUN2.executer(depot, pp, gp, "20261101-143003-mini", verifier_import=False)


def test_garde_v2_arbre_non_propre(depot):
    pp, gp = _preparer(depot)
    (depot / "non_suivi.txt").write_text("x\n", encoding="utf-8")
    with pytest.raises(GardeArret, match="non propre"):
        RUN2.executer(depot, pp, gp, "20261101-143004-mini", verifier_import=False)


def test_garde_v2_duree(depot):
    pp, gp = _preparer(depot)
    with pytest.raises(GardeArret, match="durée"):
        RUN2.executer(depot, pp, gp, "20261101-143005-mini", limite_s=0.0, verifier_import=False)


def test_garde_v2_calibrage(depot, monkeypatch):
    pp, gp = _preparer(depot)
    vrai = C.seuils_exacts

    def faux(K, T, q, alpha):
        s = vrai(K, T, q, alpha)
        s["pas_moyenne"] = (s["pas_moyenne"][0] - 0.8, 1.0)
        return s

    monkeypatch.setattr(C, "seuils_exacts", faux)
    with pytest.raises(GardeArret, match="garde de calibrage"):
        RUN2.executer(depot, pp, gp, "20261101-143006-mini", verifier_import=False)


def test_garde_v2_equivalence(depot, monkeypatch):
    pp, gp = _preparer(depot)
    vrai = S.agent_moyenne
    monkeypatch.setattr(S, "agent_moyenne", lambda Xb: vrai(Xb) + 1e-6)
    with pytest.raises(GardeArret, match="équivalence"):
        RUN2.executer(depot, pp, gp, "20261101-143007-mini", verifier_import=False)


def test_garde_v2_multiensemble(depot, monkeypatch):
    pp, gp = _preparer(depot)
    vrai = M.routage

    def faux(Xb, m, k_dest, rng):
        X = vrai(Xb, m, k_dest, rng).copy()
        X[:, 0, 0] += 1.0
        return X

    monkeypatch.setattr(M, "routage", faux)
    with pytest.raises(GardeArret, match="non préservé"):
        RUN2.executer(depot, pp, gp, "20261101-143008-mini", verifier_import=False)


def test_garde_v2_seuil_non_fini(depot, monkeypatch):
    pp, gp = _preparer(depot)
    monkeypatch.setattr(C, "seuil_mc", lambda v, a: (math.inf, 0.0))
    with pytest.raises(GardeArret, match="non finis"):
        RUN2.executer(depot, pp, gp, "20261101-143009-mini", verifier_import=False)


def test_v2_n_importe_que_des_modules_v1_inchanges():
    """Le lanceur v2 réutilise les fonctions de v1 (mêmes objets) : seule la lecture diffère."""
    from controle_ia.simulation_essaim import run_essaim as RUN1

    for nom in ("taches", "configs_des_blocs", "exiger_run_unique", "entropie_depuis_prereg"):
        assert getattr(RUN2, nom) is getattr(RUN1, nom), nom
    assert RUN2.SIMULATION == RUN1.SIMULATION and RUN2.EQUIVALENCE_TOLERANCE == RUN1.EQUIVALENCE_TOLERANCE
    assert LEC2.verdict is LEC1.verdict and np.isclose(LEC1.BORNES_AUDIT[0], 0.3)
