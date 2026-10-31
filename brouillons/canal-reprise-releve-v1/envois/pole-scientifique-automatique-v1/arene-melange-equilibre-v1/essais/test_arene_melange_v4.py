"""Essais de `arene_melange_v4.py` : chaque garde (R5) avec un cas sain et un artefact, vérifiés par leur motif ;
contrôle par l'arbre syntaxique qu'aucune garde du code n'est sans essai nommé (`test_chaque_garde_a_son_essai`) ;
racines (gel v4 : racines neuves gelées, racines déjà employées refusées jusque dans `gen`, plage de la session voisine
refusée, gel épinglé) ; refus de partir sans préenregistrement scellé POUR LA BONNE RAISON, sur des copies temporaires ;
reproductibilité bit à bit ; bras de la v3 (et de la v2) inchangés, comparaison directe au code ; B′ et C3′ ; valeur
nulle de I3 et Table 5 réécrite ; plus petit poids maximal parmi les équilibres ; audit indépendant v4 (choix
réévalués, A et tours de A, critère en écart pratique ou en changement de classe démontré) ; arrêt par PID ; lecture
mécanique des tables. Racines des essais du code v4 seulement (RACINE_TESTS = 20264301 / 20264302, autre racine
20264303), toutes écrites dans `gel-conception-arene-melange-v4.md` avant emploi.

Les essais du scellement écrivent des fichiers et leurs compagnons `.sha256` dans le dossier temporaire de pytest
(hors dépôt), jamais dans le dépôt.

    PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m pytest -q -p no:cacheprovider \
        brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/arene-melange-equilibre-v1/essais/test_arene_melange_v4.py
"""
from __future__ import annotations

import ast
import json
import re
import shutil
import signal
import subprocess
import sys
import threading
import time
from dataclasses import asdict
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import pytest
from scipy.optimize import check_grad

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI.parent))
import arene_melange_v4 as am  # noqa: E402
from controle_ia import gardes  # noqa: E402
from controle_ia.gardes import GardeArret  # noqa: E402

DEPOT = am.DEPOT
BROUILLON4 = ICI.parent / "preenregistrement-arene-melange-equilibre-v1-brouillon4.md"
PREREG_AUTRE = DEPOT / "prereg" / "preenregistrement-bisociation-deux-espaces-v2.md"  # scellé, d'une autre expérience
EMPREINTES_INTERDITES = ("6402dc6b2998d2f48262ddfe1d4d0d13b6a6115fcc8d01852c3b7c8182fd0d3b",   # code v1
                         "6685585fcfc028e0617d6786eb78bdb4fc159930af8fdf0444be1085f960d2ca",   # CONFIG_V1
                         "8e1e651b4be3e6fea6bf6bdf0fc00a19d479aa818323461fbf550582dfdb46bb",   # code v2
                         "1d7544e652ee6ab782577c5731127c7338844ef3d39844d86842688ddb2031a3",   # CONFIG_V2
                         "88c8781815007d92d5b0af17a7dc1995c00eae0773085c5a0ca35a1aafee4f0d",   # code v3
                         "02db9c9183f4f601d9a77fd956f61f92de3bbafe31d78b809096743c6b15ac44")   # CONFIG_V3

PETITE = am.replace(
    am.CONFIG_BASE_V4, d=3, K=2, T=3, n_propre_entr=300, n_attaque_entr=300, n_cal=2000, n_fpr=2000, n_eval=2000,
    n_mc=32, n_mc_final=32, departs=1, departs_final=1, departs_cout=1, departs_renforce=2, iter_renforce=20,
    iter_max=20, iter_entr=300, n_tenue=4, n_eval_tenue=200, pas_bissection=1, tol_fpr=0.03, departs_entr=3,
    r_cible=3.0, deltas=(1.0, 1.5), unites_Bp=3, audit_departs=2, audit_n_mc=16, audit_iter=10,
    audit_es_generations=3, audit_es_lambda=2)


def config_complete():
    return am.CONFIG_V4 if am.CONFIG_V4 is not None else am.replace(am.CONFIG_BASE_V4, deltas=(1.0, 1.6))


@pytest.fixture(autouse=True)
def sans_autorisation():
    am._AUTORISATION_DECISION["prereg_sha256"] = None
    yield
    am._AUTORISATION_DECISION["prereg_sha256"] = None
    gardes.SIGNAL_TERM_RECU.clear()


def sans_temps(x):
    if isinstance(x, dict):
        return {k: sans_temps(v) for k, v in x.items() if "cpu" not in k}
    if isinstance(x, list):
        return [sans_temps(v) for v in x]
    return x


def restreindre(nouveau, ancien):
    """Le résultat v4 restreint aux clés que rend l'ancien code (la v4 ne fait qu'ajouter des champs)."""
    if isinstance(ancien, dict):
        return {k: restreindre(nouveau[k], v) for k, v in ancien.items()}
    if isinstance(ancien, list):
        return [restreindre(n, a) for n, a in zip(nouveau, ancien)]
    return nouveau


def leve(motif):
    return pytest.raises(GardeArret, match=re.escape(motif))


# =================================================================================================================
# Contrôle par l'arbre syntaxique : chaque `raise GardeArret` a un motif unique et un essai nommé
# =================================================================================================================
MOTIFS = {
    "δ non fixés": "test_config_sain_et_artefacts",
    "δ invalides": "test_config_sain_et_artefacts",
    "n'est pas un multiple de K": "test_config_sain_et_artefacts",
    "κ de contournement hors": "test_config_sain_et_artefacts",
    "fractions de la courbe invalides": "test_config_sain_et_artefacts",
    "entraînement inconnu (configuration)": "test_config_sain_et_artefacts",
    "B′ sans moniteurs non linéaires": "test_config_sain_et_artefacts",
    "attaquant indépendant : paramètres non positifs": "test_config_sain_et_artefacts",
    "audit : K =": "test_config_sain_et_artefacts",
    "sans autorisation": "test_gen_garde_racine_de_decision",
    "déjà employée": "test_racines_essai_artefact",
    "d'une autre session": "test_racines_essai_artefact",
    "non gelée": "test_racines_essai_artefact",
    "racine absente": "test_racines_essai_artefact",
    "réservée à la décision": "test_racines_essai_artefact",
    "racine à part exigée": "test_racines_essai_artefact",
    "gel v4 absent": "test_gel_v4_sain_et_artefacts",
    "gel v4 modifié": "test_gel_v4_sain_et_artefacts",
    "absente du gel v4": "test_gel_v4_sain_et_artefacts",
    "bloc de configuration canonique absent": "test_identite_prereg_sain_et_artefacts",
    "bloc de configuration illisible": "test_identite_prereg_sain_et_artefacts",
    "sans l'identifiant": "test_identite_prereg_sain_et_artefacts",
    "absent ou différent du code": "test_identite_prereg_sain_et_artefacts",
    "configuration différente du code": "test_identite_prereg_sain_et_artefacts",
    "empreinte de la configuration du code absente": "test_identite_prereg_sain_et_artefacts",
    "empreinte du fichier de code exécuté absente": "test_identite_prereg_sain_et_artefacts",
    "bibliothèque modifiée après gel": "test_identite_prereg_sain_et_artefacts",
    "du processus absente du texte": "test_identite_prereg_sain_et_artefacts",
    "(S4, configuration gelée)": "test_identite_prereg_sain_et_artefacts",
    "loi d'attaque non finie": "test_admissibilite_sain_et_artefact",
    "loi d'attaque hors de la boîte": "test_admissibilite_sain_et_artefact",
    "loi d'attaque à distance": "test_admissibilite_sain_et_artefact",
    "échantillonnage stratifié impossible": "test_echantillonnage_stratifie",
    "paramètres de moniteur non finis": "test_moniteur_gardes",
    "scores propres non finis": "test_moniteur_gardes",
    "variance nulle : seuil non calibrable": "test_moniteur_gardes",
    "moniteur non calibré": "test_moniteur_gardes",
    "moniteurs linéaires exigés": "test_ou_deterministe_sain_et_artefacts",
    "« ou » déterministe : score propre": "test_ou_deterministe_sain_et_artefacts",
    "« ou » composite : aucun moniteur": "test_ou_composite_sain_et_artefacts",
    "« ou » composite : score propre de variance nulle": "test_ou_composite_sain_et_artefacts",
    "presque constant": "test_ou_composite_sain_et_artefacts",
    "maxout sans graine": "test_entrainement_gardes",
    "entraînement logistique : paramètres ou perte non finis": "test_entrainement_gardes",
    "entraînement inconnu : ": "test_entrainement_gardes",
    "entraînement par détection : paramètres ou objectif non finis": "test_entrainement_gardes",
    "poids de mélange invalides": "test_poids_sain_et_artefact",
    "matrice de gains invalide": "test_jeu_artefact",
    "programme linéaire non résolu": "test_jeu_solveur_artefacts",
    "valeurs primale et duale": "test_jeu_solveur_artefacts",
    "équilibres du jeu restreint": "test_equilibres_poids_max_min",
    "aucun départ n'a donné de point fini": "test_meilleure_reponse_departs_non_finis",
    "départs de l'attaquant au point non fini": "test_garde_departs_finis",
    "taux de fausses alertes mesuré": "test_garde_fausses_alertes_sain_et_artefact",
    "bras sans trajectoire": "test_bras_inconnus",
    "témoin inconnu": "test_bras_inconnus",
    "bras inconnu : ": "test_bras_inconnus",
    "non reproductible bit à bit": "test_garde_convergence_et_identite_tour0",
    "plafond de temps processeur": "test_plafond_de_temps_processeur",
    "entraînements non convergés": "test_garde_convergence_et_identite_tour0",
    "aucun δ de la grille": "test_choisir_deltas",
    "aucun δ <": "test_choisir_deltas",
    "lecture impossible": "test_lire_tables_refuse_sans_I3",
    "jugement impossible": "test_classes_sous_audit_sain_et_artefacts",
    "processus de travail sans préenregistrement": "test_travail_refuse_racine_de_decision_sans_prereg",
    "processus de travail encore vivants": "test_arret_par_pid_sain_et_artefact",
    "existe déjà : R12": "test_cli_refuse_d_ecraser",
    "apparu pendant l'exécution": "test_cli_refuse_d_ecraser",
    "audit-essai :": "test_audit_essai_refuse_pilote_etranger",
    "audit : run audité rattaché": "test_exiger_meme_prereg",
    "audit : bras": "test_audit_sain_et_artefacts",
    "audit : V reconstruit": "test_audit_sain_et_artefacts",
    "audit : I1 reconstruit": "test_audit_sain_et_artefacts",
    "audit : tâche absente": "test_audit_sain_et_artefacts",
    "audit : moins de deux tâches": "test_juger_audit_sain_et_artefacts",
    "audit : marges": "test_bornes_marges_et_cli_audit",
    "audit : --instances": "test_bornes_marges_et_cli_audit",
    "calibrage : --instances": "test_cli_calibrage_refuse_autres_instances",
}


def test_chaque_garde_a_son_essai():
    src = Path(am.__file__).read_text(encoding="utf-8")
    sites = []
    for node in ast.walk(ast.parse(src)):
        if isinstance(node, ast.Raise) and isinstance(node.exc, ast.Call) and \
                getattr(node.exc.func, "id", None) == "GardeArret":
            sites.append((node.lineno, ast.get_source_segment(src, node)))
    vus = []
    for ligne, seg in sites:
        trouves = [m for m in MOTIFS if m in seg]
        assert len(trouves) == 1, f"garde l. {ligne} : motifs {trouves} (exactement un attendu)"
        vus += trouves
    assert sorted(vus) == sorted(MOTIFS), "motif sans garde ou garde comptée deux fois"
    for nom_essai in set(MOTIFS.values()):
        assert callable(globals().get(nom_essai)), f"essai {nom_essai} absent"
    assert len(sites) == len(MOTIFS) == 78


# =================================================================================================================
# Configuration, racines, autorisation de décision
# =================================================================================================================
def test_config_sain_et_artefacts():
    am.exiger_config(PETITE)
    am.exiger_config(config_complete())
    with leve("δ non fixés"):
        am.exiger_config(None)
    with leve("δ non fixés"):
        am.exiger_config(am.CONFIG_BASE_V4)
    for mauvais, motif in ((dict(deltas=(1.5, 1.0)), "δ invalides"), (dict(deltas=(0.0, 1.0)), "δ invalides"),
                           (dict(n_eval=2001), "n'est pas un multiple de K"),
                           (dict(kappa_contournement=1.0), "κ de contournement hors"),
                           (dict(fractions_courbe=(0.5, 0.25)), "fractions de la courbe invalides"),
                           (dict(fractions_courbe=(0.5, 1.0)), "fractions de la courbe invalides"),
                           (dict(entrainement="autre"), "entraînement inconnu (configuration)"),
                           (dict(unites_Bp=1), "B′ sans moniteurs non linéaires"),
                           (dict(audit_departs=0), "attaquant indépendant : paramètres non positifs"),
                           (dict(audit_critere=0.0), "attaquant indépendant : paramètres non positifs"),
                           (dict(audit_k=1), "audit : K ="), (dict(audit_quantile_t=0.4), "audit : K =")):
        with leve(motif):
            am.exiger_config(am.replace(PETITE, **mauvais))


def test_racines_essai_sain():
    for r, rt in ((am.RACINE_ESSAI, am.RACINE_ESSAI_TENUE), (am.RACINE_TESTS, am.RACINE_TESTS_TENUE),
                  (am.RACINE_RECALIBRAGE, am.RACINE_RECALIBRAGE_TENUE), (am.RACINE_REPRISE, am.RACINE_REPRISE_TENUE),
                  (am.RACINE_TESTS_AUTRE, am.RACINE_SIMULATION)):
        am.exiger_racines_essai(r, rt)
    gelees = set(am.RACINES_GELEES)
    assert len(gelees) == len(am.RACINES_GELEES) == 10
    assert all(am.PLAGE_V4[0] < r < am.PLAGE_V4[1] for r in gelees)          # bornes de la plage elles-mêmes exclues
    assert not gelees & (set(am.RACINES_DEJA_EMPLOYEES) | set(am.RACINES_DECISION))
    assert not any(am.PLAGE_SESSION_VOISINE[0] <= r <= am.PLAGE_SESSION_VOISINE[1] for r in gelees)
    texte = am.GEL_V4.read_text(encoding="utf-8")
    assert all(re.search(rf"\b{r}\b", texte) for r in gelees | set(am.RACINES_DEJA_EMPLOYEES) | set(am.RACINES_DECISION))


# toutes les racines déjà employées ou nommées (brouillons 1 à 3, LISEZMOI, journaux, codes et essais v1 à v3,
# contre-lectures 1 à 3), relevées une à une : chacune est refusée
DEJA = (20261101, 20261291, 20261292, 20261293, 20261294, 20261295, 20261296, 20261297, 20261298, 20261301, 20261311,
        20261312, 20261313, 20261314, 20261315, 20261316, 20262291, 20262297, 20262313, 20269501, 20269502, 20269731,
        20269732, 20269741, 20269742)


def test_liste_des_racines_deja_employees_complete():
    assert tuple(sorted(am.RACINES_DEJA_EMPLOYEES)) == DEJA
    import arene_melange_v3 as am3

    assert set(am3.RACINES_DEJA_EMPLOYEES) | {am3.RACINE_ESSAI, am3.RACINE_ESSAI_TENUE, am3.RACINE_TESTS,
                                               am3.RACINE_TESTS_TENUE, am3.RACINE_RECALIBRAGE,
                                               am3.RACINE_RECALIBRAGE_TENUE, am3.RACINE_TESTS + 1000} <= set(DEJA)


@pytest.mark.parametrize("r, rt, motif", [(am.RACINE, am.RACINE_ESSAI_TENUE, "réservée à la décision"),
                                          (am.RACINE_ESSAI, am.RACINE_TENUE, "réservée à la décision"),
                                          *[(x, am.RACINE_ESSAI_TENUE, "déjà employée") for x in DEJA],
                                          (am.RACINE_ESSAI, 20261298, "déjà employée"),
                                          (20265001, am.RACINE_ESSAI_TENUE, "d'une autre session"),
                                          (am.RACINE_ESSAI, 20265500, "d'une autre session"),
                                          (20265999, am.RACINE_ESSAI_TENUE, "d'une autre session"),
                                          (20264777, am.RACINE_ESSAI_TENUE, "non gelée"),
                                          (am.RACINE_ESSAI, 20264999, "non gelée"),
                                          (20264001, am.RACINE_ESSAI_TENUE, "non gelée"),
                                          (12345, am.RACINE_ESSAI_TENUE, "non gelée"),
                                          (None, am.RACINE_ESSAI_TENUE, "racine absente"),
                                          (am.RACINE_ESSAI, am.RACINE_ESSAI, "racine à part exigée")])
def test_racines_essai_artefact(r, rt, motif):
    with leve(motif):
        am.exiger_racines_essai(r, rt)


def test_gel_v4_sain_et_artefacts(tmp_path):
    assert am.exiger_gel_v4(am.RACINES_GELEES) == am.GEL_V4_SHA256 == am.empreinte_fichier(am.GEL_V4)   # sain
    with leve("absente du gel v4"):
        am.exiger_gel_v4((am.RACINE_ESSAI, 20264777))
    with leve("gel v4 absent"):
        am.exiger_gel_v4((), tmp_path / "absent.md")
    copie = tmp_path / "gel-modifie.md"
    copie.write_text(am.GEL_V4.read_text(encoding="utf-8") + "\najout après coup\n", encoding="utf-8")
    with leve("gel v4 modifié"):
        am.exiger_gel_v4((), copie)
    exact = tmp_path / "gel-copie-exacte.md"
    shutil.copyfile(am.GEL_V4, exact)
    am.exiger_gel_v4((am.RACINE_TESTS,), exact)                               # copie exacte : saine


def test_gen_garde_racine_de_decision():
    am.gen(am.RACINE_TESTS, 1, 2)                                   # sain
    for r in am.RACINES_DECISION:
        with leve("sans autorisation"):
            am.gen(r, 1, 2)
    with leve("sans autorisation"):
        am.executer_tache(0, 1, am.RACINE, am.RACINE_TESTS_TENUE, PETITE)
    with leve("sans autorisation"):
        am.loi_cible(0, am.RACINE, PETITE)
    for r, motif in ((20261313, "déjà employée"), (20269741, "déjà employée"), (20265042, "d'une autre session"),
                     (20264555, "non gelée")):
        with leve(motif):                                           # jusque dans `gen` : aucune graine ne part
            am.gen(r, 0)
    with leve("non gelée"):
        am.executer_tache(0, 1, am.RACINE_TESTS + 1000, am.RACINE_TESTS_TENUE, PETITE)
    am._AUTORISATION_DECISION["prereg_sha256"] = "0" * 64           # autorisation posée (simulée) : la graine part
    assert am.gen(am.RACINE, 1, 2).integers(10) >= 0


def test_travail_refuse_racine_de_decision_sans_prereg():
    with leve("processus de travail sans préenregistrement"):
        am._travail(("tache", 0, 1, am.RACINE, am.RACINE_TENUE, asdict(PETITE), ("A",), True, None, None))
    with leve("processus de travail sans préenregistrement"):
        am._travail(("audit", 0, 1, am.RACINE, am.RACINE_TENUE, asdict(PETITE), am.BRAS_AUDIT, True, None, {}))


def test_cli_essai_refuse_racines_interdites(tmp_path):
    for r, motif in ((am.RACINE, "réservée à la décision"), (20261293, "déjà employée"), (20261311, "déjà employée"),
                     (20265001, "d'une autre session"), (20264777, "non gelée")):
        with leve(motif):
            am.main(["essai", "--instances", "0:1", "--sortie", str(tmp_path / "x.json"), "--racine", str(r)])
    assert not (tmp_path / "x.json").exists()


def test_cli_refuse_d_ecraser(tmp_path, monkeypatch):
    monkeypatch.setattr(am, "CONFIG_V4", config_complete())
    f = tmp_path / "deja.json"
    f.write_text("{}")
    with leve("existe déjà : R12"):
        am.main(["essai", "--instances", "0:1", "--sortie", str(f)])
    with leve("existe déjà : R12"):
        am.main(["calibrage", "--sortie", str(f)])                       # instances par défaut 0:48 : conformes


def test_cli_calibrage_refuse_autres_instances(tmp_path):
    for inst in ("0:12", "0:47", "1:49"):
        with leve("calibrage : --instances"):
            am.main(["calibrage", "--instances", inst, "--sortie", str(tmp_path / "c.json")])
    assert not (tmp_path / "c.json").exists()


def test_stabilite_calibrage_sain():
    grille = (1.0, 1.4, 1.8)
    cfg = am.CONFIG_BASE_V4
    res = [{"instance": i, "delta": d, "bras": {"A": {"V_iii_final": v}}}
           for i in range(6) for d, v in zip(grille, (0.20 + 0.01 * i, 0.12, 0.01 + 0.002 * i))]
    st = am.stabilite_calibrage(res, list(grille), cfg, n_tirages=300)
    assert st == {"(1.0, 1.4)": 1.0}
    assert am.choisir_deltas({d: float(np.mean([r["bras"]["A"]["V_iii_final"] for r in res if r["delta"] == d]))
                              for d in grille}, cfg) == (1.0, 1.4)
    with leve("apparu pendant l'exécution"):
        am._ecrire_nouveau(f, {"a": 1})
    g = tmp_path / "neuf.json"
    am._ecrire_nouveau(g, {"a": 1})                                   # sain
    assert g.read_text().strip().startswith("{")
    assert f.read_text() == "{}"


# =================================================================================================================
# Préenregistrement : identité, scellement, refus pour la bonne raison
# =================================================================================================================
def texte_prereg(cfg, marqueur=False):
    from controle_ia.prereg import SECTIONS

    corps = {s: "Contenu d'essai." for s in SECTIONS}
    corps["Contre-lecture"] = f"Contre-lecteur fictif ; brouillon relu {'a' * 64} ; rapport {'b' * 64}."
    if marqueur:
        corps["Seuil"] = "À REMPLIR"
    return ("# Préenregistrement d'essai (dossier temporaire)\n\n" + am.bloc_identite(cfg) + "\n\n" +
            "\n\n".join(f"## {k}\n\n{v}" for k, v in corps.items()) + "\n")


def test_identite_prereg_sain_et_artefacts():
    cfg = PETITE
    ok = texte_prereg(cfg)
    am.exiger_identite_prereg(ok, cfg)
    am.exiger_identite_prereg(ok, cfg, f"0:{cfg.n_instances}")
    code = am.empreinte_fichier(am.__file__)
    lib = am.empreinte_fichier(DEPOT / am.FICHIERS_BIBLIOTHEQUE[1])
    bloc = re.search(re.escape(am.DEBUT_CONFIG) + r".*?" + re.escape(am.FIN_CONFIG), ok, re.S).group(0)
    ligne_cfg = next(li for li in ok.splitlines() if cfg.empreinte() in li and "Configuration" in li)
    artefacts = [
        (ok.replace(bloc, ""), "bloc de configuration canonique absent"),
        (ok.replace('"T": 2', '"T": 2,,'), "bloc de configuration illisible"),
        (ok.replace(am.IDENTIFIANT_PREREG, "PREREG-AUTRE"), "sans l'identifiant"),
        (ok.replace(f"RACINE = {am.RACINE} ", "RACINE = 20261101 "), "absent ou différent du code"),
        (ok.replace('"T": 2', '"T": 3'), "configuration différente du code"),
        (ok.replace(ligne_cfg, "- Configuration : (absente)"), "empreinte de la configuration du code absente"),
        (ok.replace(code, "1" * 64), "empreinte du fichier de code exécuté absente"),
        (ok.replace(lib, "2" * 64), "bibliothèque modifiée après gel"),
        (ok.replace(f"numpy {np.__version__}", "numpy 1.26.0"), "du processus absente du texte"),
    ]
    for texte, motif in artefacts:
        assert texte != ok
        with leve(motif):
            am.exiger_identite_prereg(texte, cfg)
    with leve("(S4, configuration gelée)"):
        am.exiger_identite_prereg(ok, cfg, "0:99")
    with pytest.raises(GardeArret, match=r"T : texte 3 ≠ code 2"):
        am.exiger_identite_prereg(ok.replace('"T": 2', '"T": 3'), cfg)


def test_prereg_scelle_refus_pour_la_bonne_raison(tmp_path):
    from controle_ia.scellement import sceller

    cfg = PETITE
    p1 = tmp_path / "p1.md"
    p1.write_text(texte_prereg(cfg), encoding="utf-8")
    with pytest.raises(GardeArret, match=r"empreinte compagnon p1\.md\.sha256 absente"):
        am.autoriser_decision(p1, cfg)
    assert am._AUTORISATION_DECISION["prereg_sha256"] is None
    p2 = tmp_path / "p2.md"
    p2.write_text(texte_prereg(cfg), encoding="utf-8")
    sceller(p2)
    p2.write_text(texte_prereg(cfg) + "\nmodification après scellement\n", encoding="utf-8")
    with pytest.raises(GardeArret, match=r"≠ scellée"):
        am.autoriser_decision(p2, cfg)
    p3 = tmp_path / "p3.md"
    p3.write_text(texte_prereg(cfg, marqueur=True), encoding="utf-8")
    sceller(p3)
    with pytest.raises(GardeArret, match=r"scellé mais non conforme"):
        am.autoriser_decision(p3, cfg)
    from controle_ia.prereg import exiger_prereg_scelle

    exiger_prereg_scelle(PREREG_AUTRE)
    with leve("sans l'identifiant"):
        am.autoriser_decision(PREREG_AUTRE, cfg)
    assert am._AUTORISATION_DECISION["prereg_sha256"] is None
    p5 = tmp_path / "p5.md"
    p5.write_text(texte_prereg(cfg), encoding="utf-8")
    sha = sceller(p5)
    assert am.autoriser_decision(p5, cfg) == sha == am._AUTORISATION_DECISION["prereg_sha256"]
    am.gen(am.RACINE, 0)


def test_decision_refusee_copie_brouillon4_pour_la_bonne_raison(tmp_path, monkeypatch):
    """Sur une COPIE temporaire du brouillon 4, indépendante de l'état du dossier. Sans compagnon : refus par le
    scellement ; copie scellée : refus par non-conformité (Seuil, Contre-lecture) ; aucun run créé."""
    from controle_ia.scellement import sceller

    assert BROUILLON4.is_file()
    monkeypatch.setattr(am, "CONFIG_V4", config_complete())
    run_id = "20990101-000000-arene-essai-garde-v4"
    copie = tmp_path / "copie-brouillon4.md"
    shutil.copyfile(BROUILLON4, copie)
    marges = ["--S1", "0.02", "--S6", "0.02", "--S15", "0.02"]
    with pytest.raises(GardeArret, match=r"empreinte compagnon copie-brouillon4\.md\.sha256 absente"):
        am.main(["decision", "--prereg", str(copie), "--instances", "0:100", "--run-id", run_id])
    with pytest.raises(GardeArret, match=r"empreinte compagnon copie-brouillon4\.md\.sha256 absente"):
        am.main(["audit", "--prereg", str(copie), "--source-run", run_id, "--instances", "0:10", "--run-id",
                 run_id + "-audit"] + marges)
    sceller(copie)
    with pytest.raises(GardeArret, match=r"scellé mais non conforme.*Seuil.*Contre-lecture"):
        am.main(["decision", "--prereg", str(copie), "--instances", "0:100", "--run-id", run_id])
    assert not (DEPOT / "runs" / run_id).exists() and not (DEPOT / "runs" / (run_id + "-audit")).exists()
    assert am._AUTORISATION_DECISION["prereg_sha256"] is None


def test_brouillon4_non_conforme_au_validateur_et_identite_du_code():
    """Le brouillon garde ses marqueurs : le validateur refuse de le sceller. Son bloc d'identité est celui du code et
    de la configuration remis (δ recalibrés). Il ne cite les empreintes des codes v1 à v3 et de leurs configurations
    qu'abrégées (aucun de ces codes ne peut partir sur ce texte)."""
    from controle_ia.prereg import problemes

    p = problemes(BROUILLON4)
    assert any("Seuil" in x for x in p) and any("Contre-lecture" in x for x in p)
    texte = BROUILLON4.read_text(encoding="utf-8")
    assert am.CONFIG_V4 is not None, "δ non fixés dans le code remis"
    am.exiger_identite_prereg(texte, am.CONFIG_V4, f"0:{am.CONFIG_V4.n_instances}")
    assert not any(e in texte for e in EMPREINTES_INTERDITES)
    assert am.GEL_V4_SHA256 in texte


def test_cli_identite(capsys, monkeypatch):
    monkeypatch.setattr(am, "CONFIG_V4", config_complete())
    am.main(["identite"])
    sortie = capsys.readouterr().out
    assert am.CONFIG_V4.empreinte() in sortie and am.empreinte_fichier(am.__file__) in sortie
    assert "arene_melange_v4.py" in sortie
    assert am.extraire_configuration(sortie) == json.loads(json.dumps(asdict(am.CONFIG_V4)))


# =================================================================================================================
# Jeu à somme nulle
# =================================================================================================================
def test_jeu_sain():
    p, q, v = am.resoudre_jeu(np.array([[1.0, 0.0], [0.0, 1.0]]))
    assert np.allclose(p, [0.5, 0.5]) and np.allclose(q, [0.5, 0.5]) and abs(v - 0.5) < 1e-9
    p, q, v = am.resoudre_jeu(np.array([[0.9, 0.8], [0.1, 0.2]]))
    assert np.allclose(p, [1, 0]) and abs(v - 0.8) < 1e-9
    p, q, v = am.resoudre_jeu(np.array([[0.6, 0.0], [0.2, 0.4]]))
    assert np.allclose(p, [0.25, 0.75]) and np.allclose(q, [0.5, 0.5]) and abs(v - 0.3) < 1e-9
    p, q, v = am.resoudre_jeu(np.full((3, 2), 0.4))
    assert abs(v - 0.4) < 1e-9 and abs(p.sum() - 1) < 1e-12 and np.all(p >= 0)


@pytest.mark.parametrize("G", [np.array([[np.nan, 0.1]]), np.array([[1.2, 0.1]]), np.array([[-0.1, 0.1]]),
                               np.array([0.1, 0.2])])
def test_jeu_artefact(G):
    with leve("matrice de gains invalide"):
        am.resoudre_jeu(G)


def test_jeu_solveur_artefacts(monkeypatch):
    vrai = am.linprog
    monkeypatch.setattr(am, "linprog", lambda *a, **k: SimpleNamespace(status=2, message="infaisable (simulé)",
                                                                        fun=0.0, x=np.zeros(3)))
    with leve("programme linéaire non résolu"):
        am.resoudre_jeu(np.array([[1.0, 0.0], [0.0, 1.0]]))
    appels = []

    def decale(*a, **k):
        r = vrai(*a, **k)
        appels.append(1)
        if len(appels) == 2:
            r.fun += 0.01
        return r

    monkeypatch.setattr(am, "linprog", decale)
    with leve("valeurs primale et duale"):
        am.resoudre_jeu(np.array([[1.0, 0.0], [0.0, 1.0]]))
    monkeypatch.setattr(am, "linprog", vrai)
    am.resoudre_jeu(np.array([[1.0, 0.0], [0.0, 1.0]]))                      # sain


def test_equilibres_poids_max_min(monkeypatch):
    G = np.array([[1.0, 0.0], [0.0, 1.0]])
    _, _, v = am.resoudre_jeu(G)
    assert abs(am.poids_max_min_equilibres(G, v) - 0.5) < 1e-6                 # seul équilibre : (1/2, 1/2)
    G2 = np.array([[0.9, 0.8], [0.1, 0.2]])
    p2, _, v2 = am.resoudre_jeu(G2)
    assert am.est_pur(p2) and am.poids_max_min_equilibres(G2, v2) >= am.SEUIL_PURETE_FORCEE   # pureté forcée
    G3 = np.array([[0.5, 0.5], [0.5, 0.5], [0.2, 0.9]])                         # deux lignes équivalentes
    p3, _, v3 = am.resoudre_jeu(G3)
    assert abs(am.poids_max_min_equilibres(G3, v3) - 0.5) < 1e-6               # un mélange de même valeur existe
    vrai = am.linprog
    monkeypatch.setattr(am, "linprog", lambda *a, **k: SimpleNamespace(status=2, message="infaisable (simulé)",
                                                                        fun=np.nan, x=np.zeros(3)))
    with leve("équilibres du jeu restreint"):
        am.poids_max_min_equilibres(G, v)
    monkeypatch.setattr(am, "linprog", vrai)
    assert am.est_pur([1 - 1e-9, 1e-9]) and not am.est_pur([1 - 2e-9, 2e-9])   # pureté : un poids ≥ 1 − 10⁻⁹


def test_poids_sain_et_artefact():
    am.exiger_poids([0.25, 0.75])
    for p in ([0.5, 0.4], [1.2, -0.2], [np.nan, 1.0]):
        with leve("poids de mélange invalides"):
            am.exiger_poids(p)


# =================================================================================================================
# Lois, admissibilité, moniteurs, « ou » déterministe et composite, entraînement
# =================================================================================================================
def test_admissibilite_sain_et_artefact():
    cfg = config_complete()
    c = am.loi_cible(0, am.RACINE_TESTS, cfg)
    p, bouge = am.projeter(c + 10.0, c, 1.6, cfg)
    assert bouge and am.distance(p, c, cfg) <= 1.6 * (1 + 1e-9)
    am.exiger_admissible(p, c, 1.6, cfg)
    loin = c.copy()
    loin[: cfg.K * cfg.d] += 1.0
    with leve("loi d'attaque à distance"):
        am.exiger_admissible(loin, c, 1.6, cfg)
    hors = c.copy()
    hors[0] = cfg.boite_mu + 1
    with leve("loi d'attaque hors de la boîte"):
        am.exiger_admissible(hors, hors, 100.0, cfg)
    nan = c.copy()
    nan[3] = np.nan
    with leve("loi d'attaque non finie"):
        am.exiger_admissible(nan, c, 1.6, cfg)
    for th in am.departs_structures(c, 1.6, cfg):                  # départs structurés de l'attaquant indépendant
        am.exiger_admissible(th, c, 1.6, cfg)
    assert len(am.departs_structures(c, 1.6, cfg)) == 3 * (cfg.K + 1)


def test_echantillonnage_stratifie():
    cfg = config_complete()
    c = am.loi_cible(0, am.RACINE_TESTS, cfg)
    assert am.echantillonner(c, 30, np.random.default_rng(0), cfg).shape == (30, cfg.d)
    with leve("échantillonnage stratifié impossible"):
        am.echantillonner(c, 31, np.random.default_rng(0), cfg)


def test_moniteur_gardes():
    Xcal = np.random.default_rng(0).standard_normal((500, 2))
    am.Moniteur(np.array([[1.0, 0.0]]), np.array([0.0])).calibrer(Xcal, 0.01).detecte(Xcal)     # sain
    with leve("paramètres de moniteur non finis"):
        am.Moniteur(np.array([[np.nan, 1.0]]), np.array([0.0]))
    m = am.Moniteur(np.array([[1.0, 0.0]]), np.array([0.0]))
    with leve("moniteur non calibré"):
        m.detecte(np.zeros((2, 2)))
    with leve("variance nulle : seuil non calibrable"):
        am.Moniteur(np.zeros((1, 2)), np.zeros(1)).calibrer(np.ones((10, 2)), 0.01)
    X = Xcal.copy()
    X[3, 0] = np.inf
    with leve("scores propres non finis"):
        am.Moniteur(np.array([[1.0, 0.0]]), np.array([0.0])).calibrer(X, 0.01)


def test_ou_deterministe_sain_et_artefacts():
    g = np.random.default_rng(5)
    Xcal, Xf = g.standard_normal((20000, 3)), g.standard_normal((20000, 3))
    mons = [am.Moniteur(g.standard_normal((1, 3)), g.standard_normal(1)).calibrer(Xcal, 0.01) for _ in range(3)]
    ou = am.ou_deterministe(mons, Xcal, 8.0, 0.01)
    assert ou.m == 3 and sum(x.nb_parametres for x in mons) == ou.nb_parametres
    assert abs(float(np.mean(ou.detecte(Xf))) - 0.01) < 0.004
    z = np.stack([(m.score(Xf) - m.score(Xcal).mean()) / m.score(Xcal).std() for m in mons], axis=1)
    s = ou.score(Xf)
    assert np.all(s >= 8.0 * z.max(1) - 1e-9) and np.all(s <= 8.0 * z.max(1) + np.log(3) + 1e-9)
    with leve("moniteurs linéaires exigés"):
        am.ou_deterministe([am.Moniteur(g.standard_normal((2, 3)), np.zeros(2)).calibrer(Xcal, 0.01)], Xcal, 8, 0.01)
    plat = am.Moniteur(np.zeros((1, 3)), np.zeros(1))
    with leve("« ou » déterministe : score propre"):
        am.ou_deterministe([mons[0], plat], Xcal, 8.0, 0.01)


def test_ou_composite_sain_et_artefacts():
    g = np.random.default_rng(6)
    Xcal, Xf = g.standard_normal((20000, 3)), g.standard_normal((20000, 3))
    lin = [am.Moniteur(g.standard_normal((1, 3)), g.standard_normal(1)).calibrer(Xcal, 0.01) for _ in range(3)]
    a, b = am.ou_deterministe(lin, Xcal, 8.0, 0.01), am.ou_composite(lin, Xcal, 8.0, 0.01)
    assert np.allclose(a.score(Xf), b.score(Xf), atol=1e-9, rtol=0) and abs(a.t - b.t) < 1e-9   # même fonction
    assert np.allclose(a.grad(Xf[:50]), b.grad(Xf[:50]), atol=1e-9)
    mx = [am.Moniteur(g.standard_normal((3, 3)), g.standard_normal(3)).calibrer(Xcal, 0.01) for _ in range(2)]
    c = am.ou_composite([lin[0]] + mx, Xcal, 8.0, 0.01)
    assert c.m == 7 and c.nb_parametres == 4 + 2 * 12
    assert abs(float(np.mean(c.detecte(Xf))) - 0.01) < 0.004
    with leve("« ou » composite : aucun moniteur"):
        am.ou_composite([], Xcal, 8.0, 0.01)
    with leve("« ou » composite : score propre de variance nulle"):
        am.ou_composite([mx[0], am.Moniteur(np.zeros((2, 3)), np.zeros(2))], Xcal, 8.0, 0.01)
    presque = am.Moniteur(np.full((1, 3), 1e-9), np.array([5.0]))              # écart-type ≈ 1,7e-9, moyenne 5
    with leve("presque constant"):
        am.ou_composite([mx[0], presque], Xcal, 8.0, 0.01)
    am.ou_composite([mx[0], am.Moniteur(np.full((1, 3), 1e-4), np.array([5.0]))], Xcal, 8.0, 0.01)   # sain


def test_entrainement_gardes(monkeypatch):
    cfg = PETITE
    g = np.random.default_rng(1)
    Xp, Xa = g.standard_normal((300, 3)), g.standard_normal((300, 3)) + 1.5
    mon, ok = am.entrainer(Xp, Xa, 1, cfg, None, [np.ones(3) / np.sqrt(3)])
    mon2, _ = am.entrainer(Xp, Xa, 2, cfg, np.random.default_rng(2), [np.ones(3) / np.sqrt(3)])
    assert mon.m == 1 and mon2.m == 2
    with leve("maxout sans graine"):
        am.entrainer(Xp, Xa, 2, cfg, None)
    with leve("entraînement inconnu : "):
        am.entrainer(Xp, Xa, 1, am.replace(cfg, entrainement="autre"), None)
    vrai_min = am.minimize

    def detection_nan(f, x0, *a, **k):
        r = vrai_min(f, x0, *a, **k)
        if f is am.objectif_detection:
            r.x = np.full_like(r.x, np.nan)
        return r

    monkeypatch.setattr(am, "minimize", detection_nan)
    with leve("entraînement par détection : paramètres ou objectif non finis"):
        am.entrainer(Xp, Xa, 1, cfg, None)
    monkeypatch.setattr(am, "minimize", vrai_min)
    monkeypatch.setattr(am, "_logistique", lambda *a, **k: SimpleNamespace(x=np.full(4, np.nan), fun=np.nan,
                                                                          success=False))
    with leve("entraînement logistique : paramètres ou perte non finis"):
        am.entrainer(Xp, Xa, 1, cfg, None)


def test_gradients():
    cfg = config_complete()
    g = np.random.default_rng(3)
    Xp, Xa = g.standard_normal((200, 6)), g.standard_normal((201, 6)) + 1
    for m in (1, 3):
        p = g.standard_normal(m * 7)
        assert check_grad(lambda x: am.objectif_detection(x, Xp, Xa, m, cfg)[0],
                          lambda x: am.objectif_detection(x, Xp, Xa, m, cfg)[1], p) < 1e-6
    c = am.loi_cible(0, am.RACINE_TESTS, cfg)
    lin = [am.Moniteur(g.standard_normal((1, 6)), g.standard_normal(1)).calibrer(Xp, 0.01) for _ in range(3)]
    mx = [am.Moniteur(g.standard_normal((3, 6)), g.standard_normal(3)).calibrer(Xp, 0.01) for _ in range(2)]
    for defense in ([(mx[0], 1.0)], [(am.ou_deterministe(lin, Xp, 8.0, 0.01), 1.0)],
                    list(zip(lin, (0.2, 0.5, 0.3))), [(am.ou_composite([lin[0]] + mx, Xp, 8.0, 0.01), 1.0)],
                    list(zip(mx, (0.4, 0.6)))):
        z = g.standard_normal((3, 40, 6))
        th = c + 0.1 * g.standard_normal(c.size)
        assert check_grad(lambda x: am.objectif_lisse(x, defense, z, cfg)[0],
                          lambda x: am.objectif_lisse(x, defense, z, cfg)[1], th) < 1e-5


# =================================================================================================================
# Attaquant, fausses alertes, convergence, plafond
# =================================================================================================================
def test_meilleure_reponse_baisse_la_detection_et_reste_admissible():
    cfg = am.replace(config_complete(), deltas=(1.6,))
    ctx = am.Contexte(1, 1, am.RACINE_TESTS, am.RACINE_TESTS_TENUE, cfg)
    M = ctx.entrainer(am.COMMUN, 0, [ctx.cible], np.array([1.0]), 1)
    X0 = am.echantillonner(ctx.cible, 3000, np.random.default_rng(1), cfg)
    th, info = am.meilleure_reponse([(M, 1.0)], ctx.cible, ctx.delta, cfg, np.random.default_rng(2),
                                    np.random.default_rng(3))
    am.exiger_admissible(th, ctx.cible, ctx.delta, cfg)
    X1 = am.echantillonner(th, 3000, np.random.default_rng(4), cfg)
    assert am.taux_defense([(M, 1.0)], X1) < am.taux_defense([(M, 1.0)], X0) - 0.3
    assert info["non_finis"] == 0 and sum(info["statuts"].values()) == info["departs"] and info["iter_max"] > 0


def test_meilleure_reponse_departs_non_finis(monkeypatch):
    cfg = PETITE
    ctx = am.Contexte(0, 1, am.RACINE_TESTS, am.RACINE_TESTS_TENUE, cfg)
    M = ctx.entrainer(am.COMMUN, 0, [ctx.cible], np.array([1.0]), 1)
    vrai_min = am.minimize
    compte = {"n": 0}

    def un_sur_deux(f, x0, *a, **k):
        r = vrai_min(f, x0, *a, **k)
        if k.get("method") == "SLSQP":
            compte["n"] += 1
            if compte["n"] % 2 == 0:
                r.x = np.full_like(r.x, np.nan)
        return r

    monkeypatch.setattr(am, "minimize", un_sur_deux)
    th, info = am.meilleure_reponse([(M, 1.0)], ctx.cible, ctx.delta, cfg, np.random.default_rng(2),
                                    np.random.default_rng(3), n_departs=3)
    assert info["non_finis"] == 2 and info["departs"] == 4
    am.exiger_admissible(th, ctx.cible, ctx.delta, cfg)

    def tous_nan(f, x0, *a, **k):
        r = vrai_min(f, x0, *a, **k)
        if k.get("method") == "SLSQP":
            r.x = np.full_like(r.x, np.nan)
        return r

    monkeypatch.setattr(am, "minimize", tous_nan)
    with leve("aucun départ n'a donné de point fini"):
        am.meilleure_reponse([(M, 1.0)], ctx.cible, ctx.delta, cfg, np.random.default_rng(2), np.random.default_rng(3))


def test_garde_departs_finis():
    am.exiger_departs_finis(0, 0, PETITE)
    am.exiger_departs_finis(5, 100, PETITE)
    with leve("départs de l'attaquant au point non fini"):
        am.exiger_departs_finis(6, 100, PETITE)


def test_garde_fausses_alertes_sain_et_artefact():
    ctx = am.Contexte(0, 1, am.RACINE_TESTS, am.RACINE_TESTS_TENUE, PETITE)
    m = am.Moniteur(np.array([[1.0, 0.0, 0.0]]), np.array([0.0])).calibrer(ctx.Xcal, PETITE.alpha)
    ctx.exiger_fpr([(m, 1.0)])
    m.t -= 1.0
    with leve("taux de fausses alertes mesuré"):
        ctx.exiger_fpr([(m, 1.0)])


def test_garde_convergence_et_identite_tour0():
    assert PETITE.taux_nonconv_max == am.CONFIG_BASE_V4.taux_nonconv_max == 0.10      # S18 (R-739)
    am.exiger_convergence(1, 100, PETITE)
    am.exiger_convergence(10, 100, PETITE)
    am.exiger_convergence(3, 34, PETITE)                                       # 3 sur 34 entraînements d'une tâche
    with leve("entraînements non convergés"):
        am.exiger_convergence(11, 100, PETITE)
    with leve("entraînements non convergés"):
        am.exiger_convergence(4, 34, PETITE)
    a = am.Moniteur(np.array([[1.0, 2.0]]), np.array([0.5])).calibrer(np.random.default_rng(0).standard_normal((99, 2)),
                                                                     0.01)
    b = am.Moniteur(a.W.copy(), a.b.copy())
    b.t = a.t
    am.exiger_meme_moniteur(a, b)
    b.W[0, 0] += 1e-12
    with leve("non reproductible bit à bit"):
        am.exiger_meme_moniteur(a, b)


def test_plafond_de_temps_processeur():
    am.exiger_plafond(time.process_time(), PETITE, "sain")
    with leve("plafond de temps processeur"):
        am.exiger_plafond(time.process_time() - 1000.0, PETITE, "artefact")
    with leve("plafond de temps processeur"):
        am.executer_tache(0, 1, am.RACINE_TESTS, am.RACINE_TESTS_TENUE, am.replace(PETITE, plafond_cpu_tache_s=0.0))


def test_bras_inconnus():
    ctx = am.Contexte(0, 1, am.RACINE_TESTS, am.RACINE_TESTS_TENUE, PETITE)
    M = ctx.entrainer(am.COMMUN, 0, [ctx.cible], np.array([1.0]), 1)
    with leve("bras sans trajectoire"):
        am.trajectoire("C1", ctx, M)
    etat = am.trajectoire("B", ctx, am.Moniteur(M.W.copy(), M.b.copy()).calibrer(ctx.Xcal, PETITE.alpha), leger=True)
    am.defense_temoin("C1", etat, ctx)                                           # sain
    etat_p = am.trajectoire("Bp", ctx, am.Moniteur(M.W.copy(), M.b.copy()).calibrer(ctx.Xcal, PETITE.alpha),
                            leger=True)
    (ou, w), = am.defense_temoin("C3p", etat_p, ctx)                             # sain : C3′ sur les moniteurs de B′
    assert w == 1.0 and ou.membres == etat_p["moniteurs"]
    with leve("témoin inconnu"):
        am.defense_temoin("C9", etat, ctx)
    with leve("bras inconnu : "):
        am.executer_tache(0, 1, am.RACINE_TESTS, am.RACINE_TESTS_TENUE, PETITE, bras=("Z",))


# =================================================================================================================
# Coût par contournement, calibrage des δ
# =================================================================================================================
def test_cout_contournement_ligne_de_base_et_bissection():
    cfg = PETITE
    ctx = am.Contexte(0, 1, am.RACINE_TESTS, am.RACINE_TESTS_TENUE, cfg)
    M = ctx.entrainer(am.COMMUN, 0, [ctx.cible], np.array([1.0]), 1)
    d = [(M, 1.0)]
    r = am.cout_contournement(d, ctx, 1, [], 0.03, [0.02, 0.02, 0.02], 0.01)
    assert r["defini"] is False and r["fraction"] is None and r["censure"] is None
    r = am.cout_contournement(d, ctx, 1, [], 0.5, [0.45, 0.40, 0.35], 0.30)
    assert r["defini"] and r["censure"] and r["fraction"] == 1.0 and r["non_monotone"] == 0
    r = am.cout_contournement(d, ctx, 1, [], 0.9, [0.8, 0.1, 0.05], 0.02)
    assert r["defini"] and not r["censure"] and r["encadrement"] == [0.25, 0.5] and 0.25 <= r["fraction"] <= 0.5
    r = am.cout_contournement(d, ctx, 1, [], 0.5, [0.30, 0.40, 0.35], 0.30)
    assert r["non_monotone"] == 1


def test_choisir_deltas():
    cfg = am.CONFIG_BASE_V4
    moy = {0.6: 0.30, 0.8: 0.20, 1.0: 0.12, 1.2: 0.08, 1.4: 0.05, 1.6: 0.035, 1.8: 0.02, 2.0: 0.01, 2.4: 0.001}
    assert am.choisir_deltas(moy, cfg) == (1.0, 1.6)
    moy2 = {**moy, 2.0: 0.031}
    assert am.choisir_deltas(moy2, cfg) == (1.0, 2.0)
    with leve("aucun δ de la grille"):
        am.choisir_deltas({d: 0.02 for d in moy}, cfg)
    with leve("aucun δ <"):
        am.choisir_deltas({d: 0.05 for d in moy}, cfg)


# =================================================================================================================
# Exécution complète : reproductibilité, témoins, B′ et C3′, continuité avec la v2
# =================================================================================================================
def test_reproductibilite_bit_a_bit_et_temoins():
    a = am.executer_tache(0, 1, am.RACINE_TESTS, am.RACINE_TESTS_TENUE, PETITE)
    b = am.executer_tache(0, 1, am.RACINE_TESTS, am.RACINE_TESTS_TENUE, PETITE)
    assert sans_temps(a) == sans_temps(b)
    c = am.executer_tache(0, 1, am.RACINE_TESTS_AUTRE, am.RACINE_TESTS_TENUE, PETITE)
    assert sans_temps(a)["bras"] != sans_temps(c)["bras"]
    B = a["bras"]
    n, u, T = PETITE.T + 1, PETITE.unites_Bp, PETITE.T
    # Q1 : D, B, C1, C2, C3 au même total ; B déploie 7 paramètres (d + 1) par requête, C3 et D le total
    assert B["D"]["unites_deployees"] == n == len(B["B"]["poids_finaux"]) == B["C3"]["unites_deployees"]
    assert len({B[x]["parametres_deployes"] for x in ("B", "C1", "C2", "C3", "D")}) == 1
    assert B["B"]["parametres_par_requete"] == PETITE.d + 1
    assert B["C3"]["parametres_par_requete"] == B["D"]["parametres_par_requete"] == n * (PETITE.d + 1)
    # Q2 : B′ tire des maxouts à u unités (classe de D) ; C3′ en a le total
    assert B["Bp"]["unites_deployees"] == 1 + T * u == B["C3p"]["unites_deployees"]
    assert B["Bp"]["parametres_deployes"] == B["C3p"]["parametres_deployes"] == (1 + T * u) * (PETITE.d + 1)
    assert B["Bp"]["parametres_par_requete"] <= u * (PETITE.d + 1) == B["D"]["parametres_par_requete"]
    assert len(B["Bp"]["poids_finaux"]) == n and B["C3p"]["source"] == "Bp" and B["C3p"]["poids_finaux"] == [1.0]
    assert np.allclose(B["C1"]["poids_finaux"], 1 / n)
    w = am.gen(am.RACINE_TESTS, 1, 0, am.BRAS["C2"], PETITE.T + 1, am.ROLE_DIRICHLET).dirichlet(np.ones(n))
    assert np.allclose(B["C2"]["poids_finaux"], w)
    assert B["C3"]["poids_finaux"] == [1.0] and B["C1"]["source"] == "B"
    for x in am.TOUS_LES_BRAS:
        assert abs(B[x]["fpr_final"] - PETITE.alpha) <= PETITE.tol_fpr
        assert len(B[x]["courbe"]["V"]) == len(PETITE.fractions_courbe) + 2
    for x in am.BRAS_TRAJECTOIRE:
        cy = B[x]["cycle"]
        assert np.array(cy["H"]).shape == (T + 1, T) and set(cy) >= {"I1_progres", "I2_oubli", "retention"}
    # H[t − 1, t − 1] : moniteur déployé au tour t contre l'attaque du tour t = (iii) par tour pour A
    assert np.allclose([B["A"]["cycle"]["H"][t][t] for t in range(T)], B["A"]["par_tour"]["iii"], atol=0)
    assert a["attaquant"]["departs"] > 0 and sum(a["attaquant"]["statuts"].values()) == a["attaquant"]["departs"]


def test_ordre_des_bras_sans_effet():
    """Chaque bras tire ses graines de son propre code : l'ordre et la présence des autres bras ne changent rien."""
    tous = am.executer_tache(1, 2, am.RACINE_TESTS, am.RACINE_TESTS_TENUE, PETITE)
    seul = am.executer_tache(1, 2, am.RACINE_TESTS, am.RACINE_TESTS_TENUE, PETITE, bras=("C3p", "A"))
    for x in ("C3p", "A"):
        assert sans_temps(seul["bras"][x]) == sans_temps(tous["bras"][x])
    sans_bp = am.executer_tache(1, 2, am.RACINE_TESTS, am.RACINE_TESTS_TENUE, PETITE,
                                bras=("A", "B", "C1", "C2", "C3", "D"))
    for x in ("A", "B", "C1", "C2", "C3", "D"):
        assert sans_temps(sans_bp["bras"][x]) == sans_temps(tous["bras"][x])


def test_bras_v3_inchanges():
    """Continuité (gel v4, § 3.9) : les HUIT bras du code v4 rendent, champ à champ, ce que rend le code v3 remis (même
    racine, même configuration réduite) ; la v4 ne fait qu'ajouter des champs (équilibres, I3 − nul)."""
    import arene_melange_v3 as am3

    champs = {k: v for k, v in asdict(PETITE).items() if k in asdict(am3.CONFIG_BASE_V3)}
    p3 = am3.Config(**champs)
    r3 = am3.executer_tache(0, 2, am.RACINE_TESTS, am.RACINE_TESTS_TENUE, p3)
    r4 = am.executer_tache(0, 2, am.RACINE_TESTS, am.RACINE_TESTS_TENUE, PETITE)
    for x in am.TOUS_LES_BRAS:
        v3 = sans_temps(r3["bras"][x])
        assert v3 == restreindre(sans_temps(r4["bras"][x]), v3), x
    assert r3["attaquant"] == r4["attaquant"] and r3["entrainements"] == r4["entrainements"]
    assert r3["non_convergences"] == r4["non_convergences"]
    for x in ("B", "Bp"):                                                     # champs ajoutés par la v4
        assert set(r4["bras"][x]["equilibre"]) == {"poids_max_min", "indice_poids_max", "pur"}
    assert r4["bras"]["A"]["cycle"]["I3_nul"] == am.valeur_nulle_I3(PETITE.T)


def test_bras_v2_inchanges():
    """Continuité : A, B, C1, C2, C3, D du code v4 rendent, champ à champ, ce que rend le code v2 remis (même racine,
    même configuration réduite) ; les versions suivantes ne font qu'ajouter des champs."""
    import arene_melange_v2 as am2

    champs = {k: v for k, v in asdict(PETITE).items() if k in asdict(am2.CONFIG_BASE_V2)}
    p2 = am2.Config(**champs)
    bras = ("A", "B", "C1", "C2", "C3", "D")
    r2 = am2.executer_tache(0, 1, am.RACINE_TESTS, am.RACINE_TESTS_TENUE, p2, bras=bras)
    r3 = am.executer_tache(0, 1, am.RACINE_TESTS, am.RACINE_TESTS_TENUE, PETITE, bras=bras)
    for x in bras:
        v2 = sans_temps(r2["bras"][x])
        assert v2 == restreindre(sans_temps(r3["bras"][x]), v2), x
    assert r2["attaquant"] == r3["attaquant"]


# =================================================================================================================
# Condition d'application : indicateurs de cycle
# =================================================================================================================
def test_indicateurs_cycle_sain():
    H = np.array([[0.1, 0.0, 0.0, 0.0],
                  [0.5, 0.1, 0.0, 0.0],
                  [0.4, 0.6, 0.1, 0.0],
                  [0.3, 0.5, 0.7, 0.1],
                  [0.2, 0.4, 0.6, 0.8]])
    iii = [0.1, 0.1, 0.1, 0.1]
    dep = [np.array([1.0, 0, 0]), np.array([0, 1.0, 0]), np.array([0.9, 0.1, 0]), np.array([0, 0, 1.0])]
    r = am.indicateurs_cycle(H, iii, dep)
    assert abs(r["I1_progres"]) < 1e-12
    assert abs(r["I2_oubli"] - np.mean([0.5 - 0.2, 0.6 - 0.4, 0.7 - 0.6])) < 1e-12
    assert abs(r["retention"]["0"] - np.mean([0.5, 0.6, 0.7, 0.8])) < 1e-12
    assert abs(r["retention"]["-1"] - 0.1) < 1e-12
    assert r["I3_retours"] == 0.5          # t = 3 revient vers t = 1 ; t = 4 ne revient pas
    assert abs(r["I3_nul"] - np.mean([1 / 2, 2 / 3])) < 1e-12 and abs(r["I3_moins_nul"] - (0.5 - r["I3_nul"])) < 1e-12
    r2 = am.indicateurs_cycle(H, [0.0, 0.0, 0.2, 0.2], dep)
    assert abs(r2["I1_progres"] - 0.2) < 1e-12
    r3 = am.indicateurs_cycle(H[:3, :2], [0.1, 0.1], dep[:2])                 # T = 2 : I3 indéfini, déclaré
    assert r3["I3_retours"] is None and r3["I3_nul"] is None and r3["I3_moins_nul"] is None


def test_valeur_nulle_I3():
    """CM3-03 : sous échangeabilité, E[I3] = moyenne sur t = 3 … T de (t − 2)/(t − 1) ; 0,7345 à T = 8 ; vérifié par
    simulation sur des déplacements tirés au hasard (dimension 36, racine des essais v4)."""
    assert abs(am.valeur_nulle_I3(8) - np.mean([(t - 2) / (t - 1) for t in range(3, 9)])) < 1e-15
    assert abs(am.valeur_nulle_I3(8) - 0.7345238) < 1e-6 and am.valeur_nulle_I3(2) is None
    g = am.gen(am.RACINE_TESTS, 0, 0, 0, 0, 50)
    x = [am.taux_retours(list(g.standard_normal((8, 36)))) for _ in range(4000)]
    assert abs(float(np.mean(x)) - am.valeur_nulle_I3(8)) < 0.015
    cycle = [np.array(v, float) for v in ([1, 0], [0, 1], [1, 0.1], [0.1, 1], [1, 0], [0, 1], [1, 0.1], [0.1, 1])]
    assert am.taux_retours(cycle) == 1.0                                       # va-et-vient : au-dessus de la valeur nulle
    derive = [np.array([1.0, 0.1 * t]) for t in range(8)]
    assert am.taux_retours(derive) == 0.0                                      # dérive régulière : sous la valeur nulle


# =================================================================================================================
# Analyse et lecture mécanique des tables
# =================================================================================================================
def faux_contraste(m, s):
    from scipy.stats import norm

    return {"moyenne": m, "ecart_type": s, "quantiles": {f"q{p:g}": m + s * float(norm.ppf(p)) for p in am.QUANTILES}}


def fausse_analyse(ba, ba_ii, princ, s=0.004, q2=None, i1=(0.0, 0.0), i2=(0.05, 0.05), pur=(0.0, 0.0),
                   i3n=(0.15, 0.15)):
    """ba, ba_ii, i1, i2, pur, i3n : (δ1, δ2) ; princ, q2 : {contraste: (δ1, δ2)} ; i3n = I3 − valeur nulle de A."""
    q2 = q2 or {lib: (-0.05, -0.05) for lib in am.CONTRASTES_Q2}
    an = {}
    for k, cd in enumerate(("1", "2")):
        cs = {"B-A (iii)": faux_contraste(ba[k], s), "B-A (ii)": faux_contraste(ba_ii[k], s)}
        for lib in am.CONTRASTES_PRINCIPAUX:
            cs[lib] = faux_contraste(princ[lib][k], s)
        for lib in am.CONTRASTES_Q2:
            cs[lib] = faux_contraste(q2[lib][k], s)
        an[cd] = {"contrastes": cs, "indicateurs": {"A I1": faux_contraste(i1[k], s), "A I2": faux_contraste(i2[k], s),
                                                    "A I3-nul": faux_contraste(i3n[k], 10 * s)},
                  "bras": {"Bp": {"poids": {"part_pure": pur[k]}}}}
    return an


def test_classer_ordre():
    assert am.classer(0.05, 0.10, 0.06, 0.09, 0.03) == "B>X"
    assert am.classer(-0.10, -0.05, -0.09, -0.06, 0.03) == "X>B"
    assert am.classer(-0.01, 0.01, -0.005, 0.005, 0.03) == "≈"
    assert am.classer(0.01, 0.06, 0.015, 0.05, 0.03) == "B≳X"
    assert am.classer(-0.06, -0.01, -0.05, -0.015, 0.03) == "X≳B"
    assert am.classer(-0.04, 0.04, -0.035, 0.035, 0.03) == "?"


def test_lire_tables_lignes():
    marges = {"1": 0.02, "2": 0.02}
    base = {lib: (-0.15, -0.10) for lib in am.CONTRASTES_PRINCIPAUX}
    lt = am.lire_tables
    t = lt(fausse_analyse((0.12, 0.10), (-0.06, -0.06), base), 0.02, 0.02, marges, 0.02)
    assert t["table1"] == "mécanisme exercé" and t["table2"] == "régression avérée au-delà de la tolérance"
    assert t["table4"] == "Q1 réfutée" and t["table7"] == "Q2 réfutée"
    assert t["table5"].startswith("condition d'application vérifiée")
    assert set(t["table5_par_delta"].values()) == {"A ne progresse pas, avec oubli"}
    t = lt(fausse_analyse((0.12, -0.05), (-0.01, -0.01), base), 0.02, 0.02, marges, 0.02)
    assert t["table1"].startswith("le mélange perd") and t["table2"] == "régression démontrée sous la tolérance"
    t = lt(fausse_analyse((0.12, 0.01), (0.02, 0.03), base), 0.02, 0.02, marges, 0.02)
    assert t["table1"].startswith("mécanisme non démontré") and t["table2"] == "amélioration sur (ii)"
    t = lt(fausse_analyse((0.12, 0.10), (0.0, 0.0), base, s=0.002), 0.02, 0.02, marges, 0.02)
    assert t["table2"] == "sans régression à S5 près"
    t = lt(fausse_analyse((0.12, 0.10), (0.0, -0.02), base, s=0.006), 0.02, 0.02, marges, 0.02)
    assert t["table2"] == "régression non exclue (imprécis)"
    gagne = {lib: (0.10, 0.10) for lib in am.CONTRASTES_PRINCIPAUX}
    assert lt(fausse_analyse((0.12, 0.1), (0, 0), gagne), 0.02, 0.02, marges, 0.02)["table4"] == "Q1 confirmée"
    mixte = {lib: (0.10, -0.10) for lib in am.CONTRASTES_PRINCIPAUX}
    assert lt(fausse_analyse((0.12, 0.1), (0, 0), mixte), 0.02, 0.02, marges, 0.02)["table4"] == "Q1 dépend de δ"
    flou = {lib: (0.10, 0.015) for lib in am.CONTRASTES_PRINCIPAUX}
    t = lt(fausse_analyse((0.12, 0.1), (0, 0), flou, s=0.008), 0.02, 0.02, marges, 0.02)
    assert t["table4"] == "Q1 non tranchée" and t["table3"]["2"]["B-C1 (iii)"] == "?"
    egal = dict(gagne, **{"B-C1 (iii)": (0.0, 0.0)})
    t = lt(fausse_analyse((0.12, 0.1), (0, 0), egal), 0.02, 0.02, marges, 0.02)
    assert t["table4_par_delta"]["1"] == "réfutée (équivalence)" and t["table4"] == "Q1 réfutée"
    # Q2
    q2g = {lib: (0.08, 0.08) for lib in am.CONTRASTES_Q2}
    assert lt(fausse_analyse((0.12, 0.1), (0, 0), base, q2=q2g), 0.02, 0.02, marges, 0.02)["table7"] == "Q2 confirmée"
    q2m = {lib: (0.08, -0.08) for lib in am.CONTRASTES_Q2}
    assert lt(fausse_analyse((0.12, 0.1), (0, 0), base, q2=q2m), 0.02, 0.02, marges, 0.02)["table7"] == "Q2 dépend de δ"
    t = lt(fausse_analyse((0.12, 0.1), (0, 0), base, q2=q2g, pur=(0.6, 0.1)), 0.02, 0.02, marges, 0.02)
    assert t["table7"] == "Q2 non exercée (au moins un δ)" and t["table7_par_delta"]["2"] == "tenue"
    # Table 5
    t = lt(fausse_analyse((0.12, 0.1), (0, 0), base, i1=(0.08, 0.0)), 0.02, 0.02, marges, 0.02)
    assert t["table5_par_delta"]["1"] == "A progresse" and t["table5"].startswith("condition d'application non vérifiée")
    t = lt(fausse_analyse((0.12, 0.1), (0, 0), base, i2=(0.0, 0.015), s=0.0005), 0.02, 0.02, marges, 0.02)
    assert set(t["table5_par_delta"].values()) == {"A ne progresse pas, sans oubli"}
    t = lt(fausse_analyse((0.12, 0.1), (0, 0), base, i2=(0.02, 0.02)), 0.02, 0.02, marges, 0.02)
    assert set(t["table5_par_delta"].values()) == {"A ne progresse pas, oubli indéterminé"}
    t = lt(fausse_analyse((0.12, 0.1), (0, 0), base, i1=(0.02, 0.02)), 0.02, 0.02, marges, 0.02)
    assert t["table5"] == "condition d'application indéterminée"


def test_lire_tables_exhaustive():
    """Sur 2 000 configurations tirées, chaque table rend une ligne de sa liste (aucune exception, aucun trou)."""
    g = np.random.default_rng(11)
    L1 = {"mécanisme exercé", "le mélange perd contre la défense unique (au moins un δ)",
          "mécanisme non démontré (gain sous S1 ou imprécis, au moins un δ)"}
    L2 = {"régression avérée au-delà de la tolérance", "régression démontrée sous la tolérance", "amélioration sur (ii)",
          "sans régression à S5 près", "régression non exclue (imprécis)"}
    L4 = {f"Q1 {x}" for x in ("confirmée", "réfutée", "dépend de δ", "non tranchée")}
    L5 = {"condition d'application vérifiée (A ne progresse pas aux deux δ)",
          "condition d'application non vérifiée (A progresse dans au moins un δ)",
          "condition d'application indéterminée"}
    L7 = {f"Q2 {x}" for x in ("confirmée", "réfutée", "dépend de δ", "non tranchée", "non exercée (au moins un δ)")}
    for _ in range(2000):
        princ = {lib: tuple(g.uniform(-0.1, 0.1, 2)) for lib in am.CONTRASTES_PRINCIPAUX}
        q2 = {lib: tuple(g.uniform(-0.1, 0.1, 2)) for lib in am.CONTRASTES_Q2}
        t = am.lire_tables(fausse_analyse(tuple(g.uniform(-0.05, 0.15, 2)), tuple(g.uniform(-0.08, 0.04, 2)), princ,
                                          s=float(g.uniform(0.001, 0.03)), q2=q2, i1=tuple(g.uniform(-0.05, 0.1, 2)),
                                          i2=tuple(g.uniform(-0.05, 0.1, 2)), pur=tuple(g.uniform(0, 1, 2))),
                           0.02, 0.02, {"1": 0.02, "2": 0.02}, 0.02)
        assert t["table1"] in L1 and t["table2"] in L2 and t["table4"] in L4 and t["table5"] in L5 and \
            t["table7"] in L7
        for tab in ("table3", "table6"):
            assert all(c in {"B>X", "X>B", "≈", "B≳X", "X≳B", "?"} for v in t[tab].values() for c in v.values())


def test_analyse_sur_taches_reelles():
    cfg = am.replace(PETITE, taux_nonconv_max=0.5)
    res = [am.executer_tache(i, cd, am.RACINE_TESTS, am.RACINE_TESTS_TENUE, cfg) for cd in (1, 2) for i in (0, 1)]
    an = am.analyser(res, am.RACINE_TESTS, n_reech=500)
    for cd in ("1", "2"):
        assert an[cd]["n"] == 2 and set(an[cd]["bras"]) == set(am.TOUS_LES_BRAS)
        for lib in am.CONTRASTES_PRINCIPAUX + am.CONTRASTES_Q2 + ("B-A (iii)", "B-A (ii)"):
            q = an[cd]["contrastes"][lib]["quantiles"]
            assert q["q0.003125"] <= q["q0.025"] <= q["q0.975"] <= q["q0.996875"]
        assert {"A I1", "A I2", "Bp I1", "D I2"} <= set(an[cd]["indicateurs"])
        assert "poids" in an[cd]["bras"]["Bp"] and "cycle" in an[cd]["bras"]["A"] and "cout" in an[cd]["bras"]["C3p"]
    t = am.lire_tables(an, 0.02, 0.02, {"1": 0.02, "2": 0.02}, 0.02)
    assert t["table7"].startswith("Q2")
    assert an == am.analyser(res, am.RACINE_TESTS, n_reech=500)                # rééchantillonnage reproductible


# =================================================================================================================
# Attaquant indépendant, audit (CM2-05)
# =================================================================================================================
def test_audit_sain_et_artefacts():
    cfg = PETITE
    src = {(0, cd): am.executer_tache(0, cd, am.RACINE_TESTS, am.RACINE_TESTS_TENUE, cfg) for cd in (1, 2)}
    res, temps, jug = am.auditer([0], am.RACINE_TESTS, am.RACINE_TESTS_TENUE, cfg, src, processus=1)   # sain
    assert len(res) == 2 and set(jug["par_delta"]) == {"1", "2"} and isinstance(jug["artefact"], bool)
    for r in res:
        for nom, b in r["bras"].items():
            assert b["V_source"] == src[(0, r["code_delta"])]["bras"][nom]["V_iii_final"]
            assert b["V_audit"] <= b["V_source"] and 0 <= b["V_lourd"] <= 1
    faux = json.loads(json.dumps(src[(0, 1)]))
    faux["bras"]["D"]["V_iii_final"] += 0.1
    with leve("audit : V reconstruit"):
        am.auditer([0], am.RACINE_TESTS, am.RACINE_TESTS_TENUE, cfg, {(0, 1): faux, (0, 2): src[(0, 2)]}, processus=1)
    manque = json.loads(json.dumps(src[(0, 1)]))
    del manque["bras"]["C3p"]
    with leve("audit : bras"):
        am.auditer([0], am.RACINE_TESTS, am.RACINE_TESTS_TENUE, cfg, {(0, 1): manque, (0, 2): src[(0, 2)]},
                   processus=1)
    with leve("audit : tâche absente"):
        am.auditer([0, 1], am.RACINE_TESTS, am.RACINE_TESTS_TENUE, cfg, src, processus=1)


def _taches_audit(decalage=0.0, inverse=False):
    sortie = []
    for cd in (1, 2):
        for i in range(5):
            b = {"B": 0.20, "C3": 0.30, "D": 0.35, "Bp": 0.30, "C3p": 0.33}
            sortie.append({"instance": i, "code_delta": cd,
                           "bras": {k: {"V_source": v, "V_audit": v} for k, v in b.items()}})
            if inverse:
                sortie[-1]["bras"]["D"]["V_audit"] = 0.10            # B − D change de signe
            sortie[-1]["bras"]["C3p"]["V_audit"] -= decalage
    return sortie


def test_juger_audit_sain_et_artefact():
    assert am.juger_audit(_taches_audit(), 0.05)["artefact"] is False                 # sain : rien ne change
    assert am.juger_audit(_taches_audit(decalage=0.02), 0.05)["artefact"] is False    # change de 0,02, même signe
    j = am.juger_audit(_taches_audit(decalage=0.06), 0.05)                            # change de plus de 0,05
    assert j["artefact"] is True and j["par_delta"]["1"]["Bp-C3p"]["artefact"] is True
    j = am.juger_audit(_taches_audit(inverse=True), 0.05)                             # signe changé
    assert j["artefact"] is True and j["par_delta"]["2"]["B-D"]["artefact"] is True


def test_audit_essai_refuse_pilote_etranger(tmp_path):
    cfg = config_complete()
    bon = {"mode": "essai", "oracle": "detection", "manifeste": {"racine": am.RACINE_ESSAI,
                                                                 "racine_tenue": am.RACINE_ESSAI_TENUE,
                                                                 "config_sha256": cfg.empreinte()}, "resultats": []}
    f = tmp_path / "p.json"
    f.write_text(json.dumps(bon))
    am.charger_pilote(f, cfg)                                                          # sain
    for modif, motif in ((dict(oracle="logistique"), "audit-essai :"),
                         (dict(manifeste={**bon["manifeste"], "config_sha256": "0" * 64}), "audit-essai :"),
                         (dict(manifeste={**bon["manifeste"], "racine": 20261293}), "déjà employée")):
        g = tmp_path / f"p{len(motif)}{len(str(modif))}.json"
        g.write_text(json.dumps({**bon, **modif}))
        with leve(motif):
            am.charger_pilote(g, cfg)


def test_exiger_meme_prereg():
    am.exiger_meme_prereg({"preenregistrement": {"sha256": "a" * 64}}, "a" * 64)      # sain
    with leve("audit : run audité rattaché"):
        am.exiger_meme_prereg({"preenregistrement": {"sha256": "b" * 64}}, "a" * 64)
    with leve("audit : run audité rattaché"):
        am.exiger_meme_prereg({"preenregistrement": None}, "a" * 64)


# =================================================================================================================
# Processus de travail : PID, arrêt par PID (R10), aucun orphelin, signal TERM (CM2-14)
# =================================================================================================================
def test_arret_par_pid_sain_et_artefact(tmp_path, capsys):
    p = subprocess.Popen(["sleep", "60"])
    try:
        pids = [(p.pid, am._debut_processus(p.pid))]
        assert am.processus_vivant(*pids[0])
        assert not am.processus_vivant(p.pid, "0")                 # même PID, autre instant de départ : pas le nôtre
        with leve("processus de travail encore vivants"):          # artefact : un processus consigné tourne
            am.exiger_aucun_orphelin(pids)
        f = tmp_path / "pids.txt"
        f.write_text("# essai\n" + "".join(f"{a} {b}\n" for a, b in pids))
        assert am.lire_pids(f) == pids
        with leve("processus de travail encore vivants"):
            am.main(["orphelins", "--pids", str(f)])
        am.main(["orphelins", "--pids", str(f), "--arreter"])      # arrêt par PID, puis garde : saine
        assert "aucun processus" in capsys.readouterr().out
        am.exiger_aucun_orphelin(pids)
        assert am.arreter_par_pid(pids) == []                      # rien à arrêter
    finally:
        p.kill()
        p.wait()


def test_lancer_consigne_pids_sans_orphelin(tmp_path):
    f = tmp_path / "pids-travail.txt"
    res, temps = am.executer([0], am.RACINE_TESTS, am.RACINE_TESTS_TENUE, PETITE, processus=2, bras=("A",),
                             leger=True, fichier_pids=f)
    pids = am.lire_pids(f)
    assert len(res) == 2 and len(pids) == 2 and not any(am.processus_vivant(a, b) for a, b in pids)
    with leve("existe déjà : R12"):                                # le fichier des PID n'est jamais écrasé
        am.executer([0], am.RACINE_TESTS, am.RACINE_TESTS_TENUE, PETITE, processus=2, bras=("A",), leger=True,
                    fichier_pids=f)


def test_signal_term_arrete_le_pool_par_pid(tmp_path):
    """Un TERM reçu pendant le calcul arrête le run (motif TERM) ; les processus de travail consignés sont arrêtés."""
    f = tmp_path / "pids-term.txt"
    minuterie = threading.Timer(4.0, lambda: signal.raise_signal(signal.SIGTERM))
    minuterie.start()
    try:
        with pytest.raises(GardeArret, match=re.escape(gardes.MOTIF_TERM)):
            am.executer(range(6), am.RACINE_TESTS, am.RACINE_TESTS_TENUE, PETITE, processus=2, fichier_pids=f)
    finally:
        minuterie.cancel()
    pids = am.lire_pids(f)
    assert len(pids) == 2 and not any(am.processus_vivant(a, b) for a, b in pids)
    assert signal.getsignal(signal.SIGTERM) is not gardes.lever_sur_term   # gestionnaire rétabli
