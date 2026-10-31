"""Essais de `arene_melange_v2.py` : chaque garde (R5) avec un cas sain et un artefact, vérifiés par leur motif ;
contrôle mécanique qu'aucune garde du code n'est sans essai (`test_chaque_garde_a_son_essai`) ; refus de partir sans
préenregistrement scellé POUR LA BONNE RAISON (compagnon absent, compagnon altéré, scellé non conforme, autre
expérience) ; garde de la racine de décision jusque dans `gen` ; reproductibilité bit à bit ; témoins construits sur
les moniteurs mêmes de B ; lecture mécanique des tables. Racine des essais du code seulement (RACINE_TESTS).

Les essais du scellement écrivent des fichiers et leurs compagnons `.sha256` dans le dossier temporaire de pytest
(hors dépôt), jamais dans le dépôt.

    PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m pytest -q -p no:cacheprovider \
        brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/arene-melange-equilibre-v1/essais/test_arene_melange_v2.py
"""
from __future__ import annotations

import ast
import hashlib
import re
import sys
import time
from dataclasses import asdict
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import pytest
from scipy.optimize import check_grad

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI.parent))
import arene_melange_v2 as am  # noqa: E402
from controle_ia.gardes import GardeArret  # noqa: E402

DEPOT = am.DEPOT
BROUILLON2 = ICI.parent / "preenregistrement-arene-melange-equilibre-v1-brouillon2.md"
PREREG_AUTRE = DEPOT / "prereg" / "preenregistrement-bisociation-deux-espaces-v2.md"  # scellé, d'une autre expérience
EMPREINTE_CODE_V1 = "6402dc6b2998d2f48262ddfe1d4d0d13b6a6115fcc8d01852c3b7c8182fd0d3b"
EMPREINTE_CONFIG_V1 = "6685585fcfc028e0617d6786eb78bdb4fc159930af8fdf0444be1085f960d2ca"

PETITE = am.replace(
    am.CONFIG_BASE_V2, d=3, K=2, T=2, n_propre_entr=300, n_attaque_entr=300, n_cal=2000, n_fpr=2000, n_eval=2000,
    n_mc=32, n_mc_final=32, departs=1, departs_final=1, departs_cout=1, departs_renforce=2, iter_renforce=20,
    iter_max=20, iter_entr=300, n_tenue=4, n_eval_tenue=200, pas_bissection=1, tol_fpr=0.03, departs_entr=3,
    r_cible=3.0, deltas=(1.0, 1.5))


def config_complete():
    return am.CONFIG_V2 if am.CONFIG_V2 is not None else am.replace(am.CONFIG_BASE_V2, deltas=(1.0, 1.6))


@pytest.fixture(autouse=True)
def sans_autorisation():
    am._AUTORISATION_DECISION["prereg_sha256"] = None
    yield
    am._AUTORISATION_DECISION["prereg_sha256"] = None


def sans_temps(x):
    if isinstance(x, dict):
        return {k: sans_temps(v) for k, v in x.items() if "cpu" not in k}
    if isinstance(x, list):
        return [sans_temps(v) for v in x]
    return x


def leve(motif):
    return pytest.raises(GardeArret, match=re.escape(motif))


# =================================================================================================================
# Contrôle mécanique : chaque `raise GardeArret` du code a un motif unique et un essai qui le provoque (CM-08)
# =================================================================================================================
MOTIFS = {
    "δ non fixés": "test_config_sain_et_artefacts",
    "δ invalides": "test_config_sain_et_artefacts",
    "n'est pas un multiple de K": "test_config_sain_et_artefacts",
    "κ de contournement hors": "test_config_sain_et_artefacts",
    "fractions de la courbe invalides": "test_config_sain_et_artefacts",
    "entraînement inconnu (configuration)": "test_config_sain_et_artefacts",
    "sans autorisation": "test_gen_garde_racine_de_decision",
    "réservée à la décision": "test_racines_essai_artefact",
    "du brouillon 1": "test_racines_essai_artefact",
    "racine à part exigée": "test_racines_essai_artefact",
    "bloc de configuration canonique absent": "test_identite_prereg_sain_et_artefacts",
    "bloc de configuration illisible": "test_identite_prereg_sain_et_artefacts",
    "sans l'identifiant": "test_identite_prereg_sain_et_artefacts",
    "absent ou différent du code": "test_identite_prereg_sain_et_artefacts",
    "configuration différente du code": "test_identite_prereg_sain_et_artefacts",
    "empreinte de la configuration du code absente": "test_identite_prereg_sain_et_artefacts",
    "empreinte du fichier de code exécuté absente": "test_identite_prereg_sain_et_artefacts",
    "bibliothèque modifiée après gel": "test_identite_prereg_sain_et_artefacts",
    "du processus absente du texte": "test_identite_prereg_sain_et_artefacts",
    "--instances": "test_identite_prereg_sain_et_artefacts",
    "loi d'attaque non finie": "test_admissibilite_sain_et_artefact",
    "loi d'attaque hors de la boîte": "test_admissibilite_sain_et_artefact",
    "loi d'attaque à distance": "test_admissibilite_sain_et_artefact",
    "échantillonnage stratifié impossible": "test_echantillonnage_stratifie",
    "paramètres de moniteur non finis": "test_moniteur_gardes",
    "scores propres non finis": "test_moniteur_gardes",
    "variance nulle : seuil non calibrable": "test_moniteur_gardes",
    "moniteur non calibré": "test_moniteur_gardes",
    "moniteurs linéaires exigés": "test_ou_deterministe_sain_et_artefacts",
    "variance nulle ou non fini": "test_ou_deterministe_sain_et_artefacts",
    "maxout sans graine": "test_entrainement_gardes",
    "entraînement logistique : paramètres ou perte non finis": "test_entrainement_gardes",
    "entraînement inconnu : ": "test_entrainement_gardes",
    "entraînement par détection : paramètres ou objectif non finis": "test_entrainement_gardes",
    "poids de mélange invalides": "test_poids_sain_et_artefact",
    "matrice de gains invalide": "test_jeu_artefact",
    "programme linéaire non résolu": "test_jeu_solveur_artefacts",
    "valeurs primale et duale": "test_jeu_solveur_artefacts",
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
    "processus de travail sans préenregistrement": "test_travail_refuse_racine_de_decision_sans_prereg",
    "existe déjà : R12": "test_cli_refuse_d_ecraser",
    "apparu pendant l'exécution": "test_cli_refuse_d_ecraser",
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
    assert len(sites) == len(MOTIFS) == 52


# =================================================================================================================
# Configuration, racines, autorisation de décision
# =================================================================================================================
def test_config_sain_et_artefacts():
    am.exiger_config(PETITE)
    am.exiger_config(config_complete())
    with leve("δ non fixés"):
        am.exiger_config(None)
    with leve("δ non fixés"):
        am.exiger_config(am.CONFIG_BASE_V2)
    for mauvais, motif in ((dict(deltas=(1.5, 1.0)), "δ invalides"), (dict(deltas=(0.0, 1.0)), "δ invalides"),
                           (dict(n_eval=2001), "n'est pas un multiple de K"),
                           (dict(kappa_contournement=1.0), "κ de contournement hors"),
                           (dict(fractions_courbe=(0.5, 0.25)), "fractions de la courbe invalides"),
                           (dict(fractions_courbe=(0.5, 1.0)), "fractions de la courbe invalides"),
                           (dict(entrainement="autre"), "entraînement inconnu (configuration)")):
        with leve(motif):
            am.exiger_config(am.replace(PETITE, **mauvais))


def test_racines_essai_sain():
    for r, rt in ((am.RACINE_ESSAI, am.RACINE_ESSAI_TENUE), (am.RACINE_CALIBRAGE, am.RACINE_CALIBRAGE_TENUE),
                  (am.RACINE_TESTS, am.RACINE_TESTS_TENUE)):
        am.exiger_racines_essai(r, rt)


@pytest.mark.parametrize("r, rt, motif", [(am.RACINE, am.RACINE_ESSAI_TENUE, "réservée à la décision"),
                                          (am.RACINE_ESSAI, am.RACINE_TENUE, "réservée à la décision"),
                                          (20261291, am.RACINE_ESSAI_TENUE, "du brouillon 1"),
                                          (am.RACINE_ESSAI, 20261292, "du brouillon 1"),
                                          (am.RACINE_ESSAI, am.RACINE_ESSAI, "racine à part exigée")])
def test_racines_essai_artefact(r, rt, motif):
    with leve(motif):
        am.exiger_racines_essai(r, rt)


def test_gen_garde_racine_de_decision():
    """CM-15 : la garde est dans `gen` ; sans autorisation, aucune graine de décision, même par appel direct."""
    am.gen(am.RACINE_TESTS, 1, 2)                                   # sain
    for r in am.RACINES_DECISION:
        with leve("sans autorisation"):
            am.gen(r, 1, 2)
    with leve("sans autorisation"):
        am.executer_tache(0, 1, am.RACINE, am.RACINE_TESTS_TENUE, PETITE)
    with leve("sans autorisation"):
        am.loi_cible(0, am.RACINE, PETITE)
    am._AUTORISATION_DECISION["prereg_sha256"] = "0" * 64           # autorisation posée (simulée) : la graine part
    assert am.gen(am.RACINE, 1, 2).integers(10) >= 0


def test_travail_refuse_racine_de_decision_sans_prereg():
    with leve("processus de travail sans préenregistrement"):
        am._travail((0, 1, am.RACINE, am.RACINE_TENUE, asdict(PETITE), ("A",), True, None))


def test_cli_essai_refuse_racines_interdites(tmp_path):
    for r, motif in ((am.RACINE, "réservée à la décision"), (20261291, "du brouillon 1")):
        with leve(motif):
            am.main(["essai", "--instances", "0:1", "--sortie", str(tmp_path / "x.json"), "--racine", str(r)])
    assert not (tmp_path / "x.json").exists()


def test_cli_refuse_d_ecraser(tmp_path, monkeypatch):
    monkeypatch.setattr(am, "CONFIG_V2", config_complete())
    f = tmp_path / "deja.json"
    f.write_text("{}")
    with leve("existe déjà : R12"):
        am.main(["essai", "--instances", "0:1", "--sortie", str(f)])
    with leve("existe déjà : R12"):
        am.main(["calibrage", "--sortie", str(f)])
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
    with leve("--instances"):
        am.exiger_identite_prereg(ok, cfg, "0:99")
    # le message de configuration nomme le champ en écart
    with pytest.raises(GardeArret, match=r"T : texte 3 ≠ code 2"):
        am.exiger_identite_prereg(ok.replace('"T": 2', '"T": 3'), cfg)


def test_prereg_scelle_refus_pour_la_bonne_raison(tmp_path):
    """CM-08 : chaque refus est vérifié par son motif ; le cas sain (scellé, conforme, identifié) autorise la décision."""
    from controle_ia.scellement import sceller

    cfg = PETITE
    # 1. conforme et identifié, mais sans compagnon : refus par le scellement
    p1 = tmp_path / "p1.md"
    p1.write_text(texte_prereg(cfg), encoding="utf-8")
    with pytest.raises(GardeArret, match=r"empreinte compagnon p1\.md\.sha256 absente"):
        am.autoriser_decision(p1, cfg)
    assert am._AUTORISATION_DECISION["prereg_sha256"] is None
    # 2. scellé puis altéré
    p2 = tmp_path / "p2.md"
    p2.write_text(texte_prereg(cfg), encoding="utf-8")
    sceller(p2)
    p2.write_text(texte_prereg(cfg) + "\nmodification après scellement\n", encoding="utf-8")
    with pytest.raises(GardeArret, match=r"≠ scellée"):
        am.autoriser_decision(p2, cfg)
    # 3. scellé mais non conforme (marqueur restant)
    p3 = tmp_path / "p3.md"
    p3.write_text(texte_prereg(cfg, marqueur=True), encoding="utf-8")
    sceller(p3)
    with pytest.raises(GardeArret, match=r"scellé mais non conforme"):
        am.autoriser_decision(p3, cfg)
    # 4. scellé, conforme, d'une autre expérience (vrai scellé du dépôt)
    from controle_ia.prereg import exiger_prereg_scelle

    exiger_prereg_scelle(PREREG_AUTRE)
    with leve("sans l'identifiant"):
        am.autoriser_decision(PREREG_AUTRE, cfg)
    assert am._AUTORISATION_DECISION["prereg_sha256"] is None
    # 5. sain : scellé, conforme, identifié → autorisation posée, la racine de décision devient utilisable
    p5 = tmp_path / "p5.md"
    p5.write_text(texte_prereg(cfg), encoding="utf-8")
    sha = sceller(p5)
    assert am.autoriser_decision(p5, cfg) == sha == am._AUTORISATION_DECISION["prereg_sha256"]
    am.gen(am.RACINE, 0)


def test_decision_refusee_brouillon2_pour_la_bonne_raison(monkeypatch):
    """Le brouillon 2 n'a pas de compagnon : le refus vient du scellement, pas d'une autre garde ; aucun run créé."""
    assert BROUILLON2.is_file()
    monkeypatch.setattr(am, "CONFIG_V2", config_complete())
    run_id = "20990101-000000-arene-essai-garde-v2"
    with pytest.raises(GardeArret, match=r"empreinte compagnon .*brouillon2\.md\.sha256 absente"):
        am.main(["decision", "--prereg", str(BROUILLON2), "--instances", "0:100", "--run-id", run_id])
    assert not (DEPOT / "runs" / run_id).exists()
    assert am._AUTORISATION_DECISION["prereg_sha256"] is None


def test_brouillon2_non_conforme_au_validateur_et_identite_du_code():
    """Le brouillon garde ses marqueurs : le validateur refuse de le sceller. Son bloc d'identité est celui du code
    et de la configuration remis (empreintes, versions, configuration champ à champ, N). Il ne cite les empreintes du
    code v1 et de CONFIG_V1 qu'abrégées : le code v1 ne peut pas partir sur ce texte."""
    from controle_ia.prereg import problemes

    p = problemes(BROUILLON2)
    assert any("Seuil" in x for x in p) and any("Contre-lecture" in x for x in p)
    texte = BROUILLON2.read_text(encoding="utf-8")
    assert am.CONFIG_V2 is not None, "δ non fixés dans le code remis"
    am.exiger_identite_prereg(texte, am.CONFIG_V2, f"0:{am.CONFIG_V2.n_instances}")
    assert EMPREINTE_CODE_V1 not in texte and EMPREINTE_CONFIG_V1 not in texte


def test_cli_identite(capsys, monkeypatch):
    monkeypatch.setattr(am, "CONFIG_V2", config_complete())
    am.main(["identite"])
    sortie = capsys.readouterr().out
    assert am.CONFIG_V2.empreinte() in sortie and am.empreinte_fichier(am.__file__) in sortie
    assert am.extraire_configuration(sortie) == __import__("json").loads(__import__("json").dumps(asdict(am.CONFIG_V2)))


# =================================================================================================================
# Jeu à somme nulle
# =================================================================================================================
def test_jeu_sain():
    p, q, v = am.resoudre_jeu(np.array([[1.0, 0.0], [0.0, 1.0]]))
    assert np.allclose(p, [0.5, 0.5]) and np.allclose(q, [0.5, 0.5]) and abs(v - 0.5) < 1e-9
    p, q, v = am.resoudre_jeu(np.array([[0.9, 0.8], [0.1, 0.2]]))
    assert np.allclose(p, [1, 0]) and abs(v - 0.8) < 1e-9
    p, q, v = am.resoudre_jeu(np.array([[0.6, 0.0], [0.2, 0.4]]))           # valeur connue (contre-lecture § D)
    assert np.allclose(p, [0.25, 0.75]) and np.allclose(q, [0.5, 0.5]) and abs(v - 0.3) < 1e-9
    p, q, v = am.resoudre_jeu(np.full((3, 2), 0.4))                          # équilibres non uniques : un sommet
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


def test_poids_sain_et_artefact():
    am.exiger_poids([0.25, 0.75])
    for p in ([0.5, 0.4], [1.2, -0.2], [np.nan, 1.0]):
        with leve("poids de mélange invalides"):
            am.exiger_poids(p)


# =================================================================================================================
# Lois, admissibilité, moniteurs, « ou » déterministe, entraînement
# =================================================================================================================
def test_admissibilite_sain_et_artefact():
    cfg = config_complete()
    c = am.loi_cible(0, am.RACINE_TESTS, cfg)
    p, bouge = am.projeter(c + 10.0, c, 1.6, cfg)
    assert bouge and am.distance(p, c, cfg) <= 1.6 * (1 + 1e-9)
    am.exiger_admissible(p, c, 1.6, cfg)
    loin = c.copy()
    loin[: cfg.K * cfg.d] += 1.0                             # moyennes seulement : dans la boîte, distance 2,45 > δ
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
    assert ou.m == 3 and sum(x.W.size + x.b.size for x in mons) == ou.W.size + ou.b.size
    assert abs(float(np.mean(ou.detecte(Xf))) - 0.01) < 0.004
    z = np.stack([(m.score(Xf) - m.score(Xcal).mean()) / m.score(Xcal).std() for m in mons], axis=1)
    s = ou.score(Xf)
    assert np.all(s >= 8.0 * z.max(1) - 1e-9) and np.all(s <= 8.0 * z.max(1) + np.log(3) + 1e-9)
    with leve("moniteurs linéaires exigés"):
        am.ou_deterministe([am.Moniteur(g.standard_normal((2, 3)), np.zeros(2)).calibrer(Xcal, 0.01)], Xcal, 8, 0.01)
    plat = am.Moniteur(np.zeros((1, 3)), np.zeros(1))
    with leve("variance nulle ou non fini"):
        am.ou_deterministe([mons[0], plat], Xcal, 8.0, 0.01)


def test_entrainement_gardes(monkeypatch):
    cfg = PETITE
    g = np.random.default_rng(1)
    Xp, Xa = g.standard_normal((300, 3)), g.standard_normal((300, 3)) + 1.5
    mon, ok = am.entrainer(Xp, Xa, 1, cfg, None, [np.ones(3) / np.sqrt(3)])              # sain, linéaire
    mon2, _ = am.entrainer(Xp, Xa, 2, cfg, np.random.default_rng(2), [np.ones(3) / np.sqrt(3)])   # sain, maxout
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
    for defense in ([(am.Moniteur(g.standard_normal((3, 6)), g.standard_normal(3)).calibrer(Xp, 0.01), 1.0)],
                    [(am.ou_deterministe(lin, Xp, 8.0, 0.01), 1.0)], list(zip(lin, (0.2, 0.5, 0.3)))):
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
                                    np.random.default_rng(3), n_departs=3)      # sain : compté, point fini rendu
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
    m.t -= 1.0                                               # seuil faussé : beaucoup de fausses alertes
    with leve("taux de fausses alertes mesuré"):
        ctx.exiger_fpr([(m, 1.0)])


def test_garde_convergence_et_identite_tour0():
    am.exiger_convergence(1, 100, PETITE)
    am.exiger_convergence(5, 100, PETITE)
    with leve("entraînements non convergés"):
        am.exiger_convergence(6, 100, PETITE)
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
    with leve("témoin inconnu"):
        am.defense_temoin("C9", etat, ctx)
    with leve("bras inconnu : "):
        am.executer_tache(0, 1, am.RACINE_TESTS, am.RACINE_TESTS_TENUE, PETITE, bras=("Z",))


# =================================================================================================================
# Coût par contournement (garde de mesure sur la ligne de base), calibrage des δ
# =================================================================================================================
def test_cout_contournement_ligne_de_base_et_bissection():
    cfg = PETITE
    ctx = am.Contexte(0, 1, am.RACINE_TESTS, am.RACINE_TESTS_TENUE, cfg)
    M = ctx.entrainer(am.COMMUN, 0, [ctx.cible], np.array([1.0]), 1)
    d = [(M, 1.0)]
    # artefact : ligne de base trop basse (κ × base < 2α) → mesure non définie, sans calcul ni valeur substituée
    r = am.cout_contournement(d, ctx, 1, [], 0.03, [0.02, 0.02, 0.02], 0.01)
    assert r["defini"] is False and r["fraction"] is None and r["censure"] is None
    # sain, censuré : aucun point de la courbe sous le seuil
    r = am.cout_contournement(d, ctx, 1, [], 0.5, [0.45, 0.40, 0.35], 0.30)
    assert r["defini"] and r["censure"] and r["fraction"] == 1.0 and r["non_monotone"] == 0
    # sain, non censuré : encadrement par la courbe puis bissection
    r = am.cout_contournement(d, ctx, 1, [], 0.9, [0.8, 0.1, 0.05], 0.02)
    assert r["defini"] and not r["censure"] and r["encadrement"] == [0.25, 0.5] and 0.25 <= r["fraction"] <= 0.5
    # non-monotonie comptée (hausse de plus de α entre points consécutifs)
    r = am.cout_contournement(d, ctx, 1, [], 0.5, [0.30, 0.40, 0.35], 0.30)
    assert r["non_monotone"] == 1


def test_choisir_deltas():
    cfg = am.CONFIG_BASE_V2
    moy = {0.6: 0.30, 0.8: 0.20, 1.0: 0.12, 1.2: 0.08, 1.4: 0.05, 1.6: 0.035, 1.8: 0.02, 2.0: 0.01, 2.4: 0.001}
    assert am.choisir_deltas(moy, cfg) == (1.0, 1.6)
    moy2 = {**moy, 2.0: 0.031}                                    # non monotone : la règle prend le plus grand
    assert am.choisir_deltas(moy2, cfg) == (1.0, 2.0)
    with leve("aucun δ de la grille"):
        am.choisir_deltas({d: 0.02 for d in moy}, cfg)
    with leve("aucun δ <"):
        am.choisir_deltas({d: 0.05 for d in moy}, cfg)


# =================================================================================================================
# Exécution complète : reproductibilité bit à bit, témoins sur les moniteurs de B, capacité égale
# =================================================================================================================
def test_reproductibilite_bit_a_bit_et_temoins():
    a = am.executer_tache(0, 1, am.RACINE_TESTS, am.RACINE_TESTS_TENUE, PETITE)
    b = am.executer_tache(0, 1, am.RACINE_TESTS, am.RACINE_TESTS_TENUE, PETITE)
    assert sans_temps(a) == sans_temps(b)
    c = am.executer_tache(0, 1, am.RACINE_TESTS + 1000, am.RACINE_TESTS_TENUE, PETITE)
    assert sans_temps(a)["bras"] != sans_temps(c)["bras"]
    B = a["bras"]
    n = PETITE.T + 1
    # paramètres égaux : D, B, C1, C2, C3 déploient T + 1 unités et autant de paramètres
    assert B["D"]["unites_deployees"] == n == len(B["B"]["poids_finaux"]) == B["C3"]["unites_deployees"]
    assert len({B[x]["parametres_deployes"] for x in ("B", "C1", "C2", "C3", "D")}) == 1
    assert np.allclose(B["C1"]["poids_finaux"], 1 / n)
    w = am.gen(am.RACINE_TESTS, 1, 0, am.BRAS["C2"], PETITE.T + 1, am.ROLE_DIRICHLET).dirichlet(np.ones(n))
    assert np.allclose(B["C2"]["poids_finaux"], w)
    assert B["C3"]["poids_finaux"] == [1.0] and B["C1"]["source"] == "B"
    for x in am.TOUS_LES_BRAS:
        assert abs(B[x]["fpr_final"] - PETITE.alpha) <= PETITE.tol_fpr
        assert len(B[x]["courbe"]["V"]) == len(PETITE.fractions_courbe) + 2
    assert a["attaquant"]["departs"] > 0 and sum(a["attaquant"]["statuts"].values()) == a["attaquant"]["departs"]


def test_ordre_des_bras_sans_effet():
    """Chaque bras tire ses graines de son propre code : l'ordre et la présence des autres bras ne changent rien."""
    tous = am.executer_tache(1, 2, am.RACINE_TESTS, am.RACINE_TESTS_TENUE, PETITE)
    seul = am.executer_tache(1, 2, am.RACINE_TESTS, am.RACINE_TESTS_TENUE, PETITE, bras=("C3", "A"))
    for x in ("C3", "A"):
        assert sans_temps(seul["bras"][x]) == sans_temps(tous["bras"][x])


# =================================================================================================================
# Analyse et lecture mécanique des tables
# =================================================================================================================
def faux_contraste(m, s):
    from scipy.stats import norm

    return {"moyenne": m, "ecart_type": s, "quantiles": {f"q{p:g}": m + s * float(norm.ppf(p)) for p in am.QUANTILES}}


def fausse_analyse(ba, ba_ii, princ, s=0.004):
    """ba, ba_ii : (δ1, δ2) ; princ : {contraste: (δ1, δ2)}."""
    an = {}
    for k, cd in enumerate(("1", "2")):
        cs = {"B-A (iii)": faux_contraste(ba[k], s), "B-A (ii)": faux_contraste(ba_ii[k], s)}
        for lib in am.CONTRASTES_PRINCIPAUX:
            cs[lib] = faux_contraste(princ[lib][k], s)
        an[cd] = {"contrastes": cs}
    return an


def test_classer_ordre():
    assert am.classer(0.05, 0.10, 0.06, 0.09, 0.03) == "B>X"
    assert am.classer(-0.10, -0.05, -0.09, -0.06, 0.03) == "X>B"
    assert am.classer(-0.01, 0.01, -0.005, 0.005, 0.03) == "≈"
    assert am.classer(0.01, 0.06, 0.015, 0.05, 0.03) == "B≳X"
    assert am.classer(-0.06, -0.01, -0.05, -0.015, 0.03) == "X≳B"
    assert am.classer(-0.04, 0.04, -0.035, 0.035, 0.03) == "?"


def test_lire_tables_lignes():
    marges = {"1": 0.03, "2": 0.03}
    base = {lib: (-0.15, -0.10) for lib in am.CONTRASTES_PRINCIPAUX}
    t = am.lire_tables(fausse_analyse((0.12, 0.10), (-0.06, -0.06), base), 0.02, 0.02, marges)
    assert t["table1"] == "mécanisme exercé" and t["table2"] == "régression avérée au-delà de la tolérance"
    assert t["table4"] == "HP réfutée"
    t = am.lire_tables(fausse_analyse((0.12, -0.05), (-0.01, -0.01), base), 0.02, 0.02, marges)
    assert t["table1"].startswith("le mélange perd") and t["table2"] == "régression démontrée sous la tolérance"
    t = am.lire_tables(fausse_analyse((0.12, 0.01), (0.02, 0.03), base), 0.02, 0.02, marges)
    assert t["table1"].startswith("mécanisme non démontré") and t["table2"] == "amélioration sur (ii)"
    t = am.lire_tables(fausse_analyse((0.12, 0.10), (0.0, 0.0), base, s=0.002), 0.02, 0.02, marges)
    assert t["table2"] == "sans régression à S5 près"
    t = am.lire_tables(fausse_analyse((0.12, 0.10), (0.0, -0.02), base, s=0.006), 0.02, 0.02, marges)
    assert t["table2"] == "régression non exclue (imprécis)"
    gagne = {lib: (0.10, 0.10) for lib in am.CONTRASTES_PRINCIPAUX}
    assert am.lire_tables(fausse_analyse((0.12, 0.1), (0, 0), gagne), 0.02, 0.02, marges)["table4"] == "HP confirmée"
    mixte = {lib: (0.10, -0.10) for lib in am.CONTRASTES_PRINCIPAUX}
    assert am.lire_tables(fausse_analyse((0.12, 0.1), (0, 0), mixte), 0.02, 0.02, marges)["table4"] == "HP dépend de δ"
    flou = {lib: (0.10, 0.02) for lib in am.CONTRASTES_PRINCIPAUX}
    t = am.lire_tables(fausse_analyse((0.12, 0.1), (0, 0), flou, s=0.008), 0.02, 0.02, marges)
    assert t["table4"] == "HP non tranchée" and t["table3"]["2"]["B-C1 (iii)"] == "?"
    egal = dict(gagne, **{"B-C1 (iii)": (0.0, 0.0)})
    t = am.lire_tables(fausse_analyse((0.12, 0.1), (0, 0), egal), 0.02, 0.02, marges)
    assert t["table4_par_delta"]["1"] == "réfutée (équivalence)" and t["table4"] == "HP réfutée"


def test_lire_tables_exhaustive():
    """Sur 2 000 configurations tirées, chaque table rend une ligne de sa liste (aucune exception, aucun trou)."""
    g = np.random.default_rng(11)
    L1 = {"mécanisme exercé", "le mélange perd contre la défense unique (au moins un δ)",
          "mécanisme non démontré (gain sous S1 ou imprécis, au moins un δ)"}
    L2 = {"régression avérée au-delà de la tolérance", "régression démontrée sous la tolérance", "amélioration sur (ii)",
          "sans régression à S5 près", "régression non exclue (imprécis)"}
    L4 = {"HP confirmée", "HP réfutée", "HP dépend de δ", "HP non tranchée"}
    for _ in range(2000):
        princ = {lib: tuple(g.uniform(-0.1, 0.1, 2)) for lib in am.CONTRASTES_PRINCIPAUX}
        t = am.lire_tables(fausse_analyse(tuple(g.uniform(-0.05, 0.15, 2)), tuple(g.uniform(-0.08, 0.04, 2)), princ,
                                          s=float(g.uniform(0.001, 0.03))), 0.02, 0.02, {"1": 0.03, "2": 0.02})
        assert t["table1"] in L1 and t["table2"] in L2 and t["table4"] in L4
        assert all(c in {"B>X", "X>B", "≈", "B≳X", "X≳B", "?"} for v in t["table3"].values() for c in v.values())


def test_analyse_sur_taches_reelles():
    cfg = am.replace(PETITE, taux_nonconv_max=0.5)   # petite configuration : une non-convergence sur 8 tolérée ici
    res = [am.executer_tache(i, cd, am.RACINE_TESTS, am.RACINE_TESTS_TENUE, cfg) for cd in (1, 2) for i in (0, 1)]
    an = am.analyser(res, am.RACINE_TESTS, n_reech=500)
    for cd in ("1", "2"):
        assert an[cd]["n"] == 2 and set(an[cd]["bras"]) == set(am.TOUS_LES_BRAS)
        for lib in am.CONTRASTES_PRINCIPAUX + ("B-A (iii)", "B-A (ii)"):
            q = an[cd]["contrastes"][lib]["quantiles"]
            assert q["q0.003125"] <= q["q0.025"] <= q["q0.975"] <= q["q0.996875"]
        assert "poids" in an[cd]["bras"]["B"] and "cout" in an[cd]["bras"]["C3"]
    assert an == am.analyser(res, am.RACINE_TESTS, n_reech=500)                # rééchantillonnage reproductible
