"""Essais de `arene_melange_v1.py` : gardes R5 (cas sain et artefact), reproductibilité bit à bit, refus de partir
sans préenregistrement scellé, refus des racines de décision en essai. Racine d'essai seulement.

    PYTHONPATH=src python3 -m pytest -q brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/arene-melange-equilibre-v1/essais
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pytest
from scipy.optimize import check_grad

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI.parent))
import arene_melange_v1 as am  # noqa: E402
from controle_ia.gardes import GardeArret  # noqa: E402

DEPOT = am.DEPOT
BROUILLON = ICI.parent / "preenregistrement-arene-melange-equilibre-v1-brouillon1.md"
PREREG_AUTRE = DEPOT / "prereg" / "preenregistrement-bisociation-deux-espaces-v2.md"  # scellé, d'une autre expérience

PETITE = am.replace(
    am.CONFIG_V1, d=3, K=2, T=2, n_propre_entr=300, n_attaque_entr=300, n_cal=2000, n_fpr=2000, n_eval=2000,
    n_mc=32, n_mc_final=32, departs=1, departs_final=1, departs_cout=1, iter_max=20, iter_entr=300, n_tenue=4,
    n_eval_tenue=200, pas_bissection=1, tol_fpr=0.03, departs_entr=3, r_cible=3.0, deltas=(1.0, 1.5))


def sans_temps(x):
    if isinstance(x, dict):
        return {k: sans_temps(v) for k, v in x.items() if "cpu" not in k}
    if isinstance(x, list):
        return [sans_temps(v) for v in x]
    return x


# --- racines --------------------------------------------------------------------------------------------------
def test_racines_essai_sain():
    am.exiger_racines_essai(am.RACINE_ESSAI, am.RACINE_ESSAI_TENUE)


@pytest.mark.parametrize("r, rt", [(am.RACINE, am.RACINE_ESSAI_TENUE), (am.RACINE_ESSAI, am.RACINE_TENUE),
                                   (am.RACINE_ESSAI, am.RACINE_ESSAI)])
def test_racines_essai_artefact(r, rt):
    with pytest.raises(GardeArret):
        am.exiger_racines_essai(r, rt)


def test_cli_essai_refuse_racine_de_decision(tmp_path):
    with pytest.raises(GardeArret, match="réservée à la décision"):
        am.main(["essai", "--instances", "0:1", "--sortie", str(tmp_path / "x.json"), "--racine", str(am.RACINE)])
    assert not (tmp_path / "x.json").exists()


def test_cli_essai_refuse_d_ecraser(tmp_path):
    f = tmp_path / "deja.json"
    f.write_text("{}")
    with pytest.raises(GardeArret, match="écraser"):
        am.main(["essai", "--instances", "0:1", "--sortie", str(f)])


# --- préenregistrement ------------------------------------------------------------------------------------------
def test_decision_refusee_sans_prereg_scelle():
    """Artefact : le brouillon (non scellé) ne laisse pas partir le run ; aucun dossier de run n'est créé."""
    assert BROUILLON.is_file()
    run_id = "20990101-000000-arene-essai-garde"
    with pytest.raises(GardeArret):
        am.main(["decision", "--prereg", str(BROUILLON), "--instances", "0:1", "--run-id", run_id])
    assert not (DEPOT / "runs" / run_id).exists()


def test_decision_refusee_prereg_scelle_d_une_autre_experience():
    """Artefact : un préenregistrement scellé et conforme, mais pas celui de l'arène. Sain pour la partie scellement :
    `exiger_prereg_scelle` passe (vrai scellé du dépôt), l'identité refuse."""
    from controle_ia.prereg import exiger_prereg_scelle

    exiger_prereg_scelle(PREREG_AUTRE)
    with pytest.raises(GardeArret, match="identifiant"):
        am.exiger_prereg_arene(PREREG_AUTRE)


def test_identite_prereg_sain_et_artefacts():
    import hashlib

    code = hashlib.sha256(Path(am.__file__).read_bytes()).hexdigest()
    ok = (f"{am.IDENTIFIANT_PREREG}\nRACINE = {am.RACINE}\nRACINE_TENUE = {am.RACINE_TENUE}\n"
          f"configuration {am.CONFIG_V1.empreinte()}\ncode {code}\n")
    am.exiger_identite_prereg(ok)
    for mauvais in (ok.replace(am.IDENTIFIANT_PREREG, "AUTRE"), ok.replace(str(am.RACINE) + "\n", "20261101\n"),
                    ok.replace(am.CONFIG_V1.empreinte(), "0" * 64), ok.replace(code, "1" * 64)):
        with pytest.raises(GardeArret):
            am.exiger_identite_prereg(mauvais)


def test_brouillon_non_conforme_au_validateur():
    """Le brouillon garde ses marqueurs « À REMPLIR » : le validateur du dépôt refuse de le sceller."""
    from controle_ia.prereg import problemes

    assert problemes(BROUILLON)


# --- jeu à somme nulle ------------------------------------------------------------------------------------------
def test_jeu_sain():
    p, q, v = am.resoudre_jeu(np.array([[1.0, 0.0], [0.0, 1.0]]))
    assert np.allclose(p, [0.5, 0.5]) and np.allclose(q, [0.5, 0.5]) and abs(v - 0.5) < 1e-9
    p, q, v = am.resoudre_jeu(np.array([[0.9, 0.8], [0.1, 0.2]]))
    assert np.allclose(p, [1, 0]) and abs(v - 0.8) < 1e-9


@pytest.mark.parametrize("G", [np.array([[np.nan, 0.1]]), np.array([[1.2, 0.1]]), np.array([0.1, 0.2])])
def test_jeu_artefact(G):
    with pytest.raises(GardeArret):
        am.resoudre_jeu(G)


def test_poids_sain_et_artefact():
    am.exiger_poids([0.25, 0.75])
    for p in ([0.5, 0.4], [1.2, -0.2], [np.nan, 1.0]):
        with pytest.raises(GardeArret):
            am.exiger_poids(p)


# --- lois et admissibilité --------------------------------------------------------------------------------------
def test_admissibilite_sain_et_artefact():
    cfg = am.CONFIG_V1
    c = am.loi_cible(0, am.RACINE_ESSAI, cfg)
    loin = c + 10.0
    p, bouge = am.projeter(loin, c, 1.6, cfg)
    assert bouge and am.distance(p, c, cfg) <= 1.6 * (1 + 1e-9)
    am.exiger_admissible(p, c, 1.6, cfg)
    with pytest.raises(GardeArret):
        am.exiger_admissible(c + 1.0, c, 1.6, cfg)          # distance > δ
    hors = c.copy()
    hors[0] = cfg.boite_mu + 1
    with pytest.raises(GardeArret):
        am.exiger_admissible(hors, hors, 100.0, cfg)        # hors de la boîte


def test_echantillonnage_stratifie():
    cfg = am.CONFIG_V1
    c = am.loi_cible(0, am.RACINE_ESSAI, cfg)
    assert am.echantillonner(c, 30, np.random.default_rng(0), cfg).shape == (30, cfg.d)
    with pytest.raises(GardeArret):
        am.echantillonner(c, 31, np.random.default_rng(0), cfg)


# --- moniteurs ----------------------------------------------------------------------------------------------------
def test_moniteur_gardes():
    with pytest.raises(GardeArret):
        am.Moniteur(np.array([[np.nan, 1.0]]), np.array([0.0]))
    m = am.Moniteur(np.array([[1.0, 0.0]]), np.array([0.0]))
    with pytest.raises(GardeArret, match="non calibré"):
        m.detecte(np.zeros((2, 2)))
    with pytest.raises(GardeArret, match="variance nulle"):
        am.Moniteur(np.zeros((1, 2)), np.zeros(1)).calibrer(np.ones((10, 2)), 0.01)


def test_garde_fausses_alertes_sain_et_artefact():
    ctx = am.Contexte(0, 1, am.RACINE_ESSAI, am.RACINE_ESSAI_TENUE, PETITE)
    m = am.Moniteur(np.array([[1.0, 0.0, 0.0]]), np.array([0.0])).calibrer(ctx.Xcal, PETITE.alpha)
    ctx.exiger_fpr([(m, 1.0)])
    m.t -= 1.0                                               # seuil faussé : ~5 % de fausses alertes
    with pytest.raises(GardeArret, match="fausses alertes"):
        ctx.exiger_fpr([(m, 1.0)])


def test_garde_convergence_et_identite_tour0():
    am.exiger_convergence(1, 100, am.CONFIG_V1)
    with pytest.raises(GardeArret):
        am.exiger_convergence(10, 100, am.CONFIG_V1)
    a = am.Moniteur(np.array([[1.0, 2.0]]), np.array([0.5])).calibrer(np.random.default_rng(0).standard_normal((99, 2)),
                                                                     0.01)
    b = am.Moniteur(a.W.copy(), a.b.copy())
    b.t = a.t
    am.exiger_meme_moniteur(a, b)
    b.W[0, 0] += 1e-12
    with pytest.raises(GardeArret):
        am.exiger_meme_moniteur(a, b)


def test_gradients():
    cfg = am.CONFIG_V1
    g = np.random.default_rng(3)
    Xp, Xa = g.standard_normal((200, 6)), g.standard_normal((201, 6)) + 1
    for m in (1, 3):
        p = g.standard_normal(m * 7)
        assert check_grad(lambda x: am.objectif_detection(x, Xp, Xa, m, cfg)[0],
                          lambda x: am.objectif_detection(x, Xp, Xa, m, cfg)[1], p) < 1e-6
    c = am.loi_cible(0, am.RACINE_ESSAI, cfg)
    M = am.Moniteur(g.standard_normal((3, 6)), g.standard_normal(3)).calibrer(Xp, 0.01)
    z = g.standard_normal((3, 40, 6))
    th = c + 0.1 * g.standard_normal(c.size)
    assert check_grad(lambda x: am.objectif_lisse(x, [(M, 1.0)], z, cfg)[0],
                      lambda x: am.objectif_lisse(x, [(M, 1.0)], z, cfg)[1], th) < 1e-6


def test_meilleure_reponse_baisse_la_detection_et_reste_admissible():
    cfg = am.CONFIG_V1
    ctx = am.Contexte(1, 1, am.RACINE_ESSAI, am.RACINE_ESSAI_TENUE, cfg)
    M = ctx.entrainer(am.COMMUN, 0, [ctx.cible], np.array([1.0]), 1)
    X0 = am.echantillonner(ctx.cible, 3000, np.random.default_rng(1), cfg)
    th, info = am.meilleure_reponse([(M, 1.0)], ctx.cible, ctx.delta, cfg, np.random.default_rng(2),
                                    np.random.default_rng(3))
    am.exiger_admissible(th, ctx.cible, ctx.delta, cfg)
    X1 = am.echantillonner(th, 3000, np.random.default_rng(4), cfg)
    assert am.taux_defense([(M, 1.0)], X1) < am.taux_defense([(M, 1.0)], X0) - 0.3


# --- exécution complète : reproductibilité bit à bit, plafond ---------------------------------------------------------
def test_reproductibilite_bit_a_bit():
    a = am.executer_tache(0, 1, am.RACINE_ESSAI, am.RACINE_ESSAI_TENUE, PETITE)
    b = am.executer_tache(0, 1, am.RACINE_ESSAI, am.RACINE_ESSAI_TENUE, PETITE)
    assert sans_temps(a) == sans_temps(b)
    c = am.executer_tache(0, 1, am.RACINE_ESSAI + 1000, am.RACINE_ESSAI_TENUE, PETITE)
    assert sans_temps(a)["bras"] != sans_temps(c)["bras"]
    # capacité égale déclarée : D déploie à la fin T + 1 unités et autant de paramètres que le mélange de B
    assert a["bras"]["D"]["unites_deployees"] == PETITE.T + 1 == len(a["bras"]["B"]["poids_finaux"])
    assert a["bras"]["D"]["parametres_deployes"] == a["bras"]["B"]["parametres_deployes"]


def test_plafond_de_temps_processeur():
    with pytest.raises(GardeArret, match="plafond"):
        am.executer_tache(0, 1, am.RACINE_ESSAI, am.RACINE_ESSAI_TENUE, am.replace(PETITE, plafond_cpu_tache_s=0.0))


def test_analyse_ecarts_apparies():
    res = []
    for i in range(5):
        bras = {}
        for nom, v in zip("ABCD", (0.1, 0.3, 0.2, 0.4)):
            bras[nom] = {"V_iii_final": v + 0.01 * i, "ii_final": 0.5, "i_final_vus": 0.5,
                         "cout": {"fraction": 0.5}}
        res.append({"code_delta": 1, "instance": i, "bras": bras})
    an = am.analyser(res, am.RACINE_ESSAI, n_reech=500)
    c = an["1"]["contrastes"]["B-A (iii)"]
    assert abs(c["moyenne"] - 0.2) < 1e-12 and c["ic95"][0] <= 0.2 <= c["ic95"][1]
    assert an["1"]["contrastes"]["B-A (ii)"]["zeros_exacts"] == 5
