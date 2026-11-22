"""Essais de la brique B (sondes en forme close v1) : cas sains, artefacts, reproductibilité au bit près, tolérance
entre « machines » simulées (autre nombre de tâches de calcul linéaire, autre ordre des actions)."""
import ast
import subprocess
import sys
from pathlib import Path

import numpy as np
import pytest
from threadpoolctl import threadpool_limits

from controle_ia.gardes import GardeArret
from controle_ia.harnais.sondes import score_action
from controle_ia.sondes.familles import SondeLineaireJetons
from controle_ia.sondes_v2 import formes_closes_v1 as fc

D = 32
RACINE = Path(__file__).resolve().parents[1]


def _donnees(graine=0, n=40, d=D, signal=1.5):
    rng = np.random.default_rng(graine)
    u = rng.standard_normal(d)
    u /= np.linalg.norm(u)
    seqs, y = [], []
    for i in range(n):
        lab = i % 2
        k = int(rng.integers(3, 9))
        x = rng.standard_normal((k, d))
        if lab:
            x[int(rng.integers(0, k))] += signal * 3 * u  # un jeton porteur
        seqs.append(x)
        y.append(lab)
    return seqs, np.array(y), u


def _aire(s, y):
    from controle_ia.sondes.evaluation import aire_sous_courbe
    return aire_sous_courbe(s, y)


@pytest.mark.parametrize("famille,reglage", [("difference_moyennes_appariee", None),
                                             ("difference_moyennes_blanchie", 0.5),
                                             ("logistique_l2", 0.1)])
def test_sain_separe_et_interface(famille, reglage):
    seqs, y, u = _donnees()
    s = fc.apprendre(famille, "s", 15, seqs, y, reglage)
    assert isinstance(s, SondeLineaireJetons) and s.agregation == "max" and s.famille == famille
    sc = fc.scores_actions(s, seqs)
    # score = maximum sur les jetons, égal à celui du harnais
    for q, v in zip(seqs, sc):
        assert v == pytest.approx(score_action(s, q, 0, len(q)), rel=1e-12, abs=1e-12)
    assert _aire(sc, y) > 0.8
    assert s.w.dtype == np.float64


def test_appariee_formule():
    rng = np.random.default_rng(1)
    seqs = [rng.standard_normal((k, 4)) for k in (2, 3, 4, 5)]
    y = np.array([1, 0, 1, 0])
    s = fc.difference_moyennes_appariee("p", 15, seqs, y, paires=[(0, 1), (2, 3)])
    attendu = ((seqs[0].mean(0) - seqs[1].mean(0)) + (seqs[2].mean(0) - seqs[3].mean(0))) / 2
    np.testing.assert_allclose(s.w, attendu, rtol=1e-14)
    s0 = fc.difference_moyennes_appariee("p", 15, seqs, y)
    np.testing.assert_allclose(s0.w, np.concatenate([seqs[0], seqs[2]]).mean(0) - np.concatenate([seqs[1], seqs[3]]).mean(0))


@pytest.mark.parametrize("paires,motif", [([(1, 1)], "positive"), ([(0, 1)], "positive"), ([(1, 9)], "hors"),
                                          ([(1, 0), (1, 2)], "deux paires"), ([], "au moins")])
def test_paires_artefacts(paires, motif):
    seqs, y, _ = _donnees(n=4)
    with pytest.raises(GardeArret, match=motif):
        fc.difference_moyennes_appariee("p", 15, seqs, y, paires=paires)


def test_blanchie_formule():
    seqs, y, _ = _donnees(n=10, d=5)
    lam = 0.9
    s = fc.difference_moyennes_blanchie("b", 15, seqs, y, lam)
    S = fc.covariance_intra([np.asarray(q, float) for q in seqs], y)
    S = (1 - lam) * S + lam * np.trace(S) / 5 * np.eye(5)
    w0 = np.concatenate([q for q, t in zip(seqs, y) if t]).mean(0) - np.concatenate([q for q, t in zip(seqs, y) if not t]).mean(0)
    np.testing.assert_allclose(s.w, np.linalg.solve(S, w0), rtol=1e-12)


@pytest.mark.parametrize("famille,reglage", [("difference_moyennes_blanchie", 0.3), ("logistique_l2", 5.0),
                                             ("difference_moyennes_appariee", 0.1), ("inconnue", None)])
def test_reglages_hors_grille(famille, reglage):
    seqs, y, _ = _donnees(n=6)
    with pytest.raises(GardeArret):
        fc.apprendre(famille, "x", 15, seqs, y, reglage)


def test_logistique_non_convergee(monkeypatch):
    seqs, y, _ = _donnees()
    monkeypatch.setitem(fc.SOLVEUR_LOGISTIQUE, "max_iter", 1)
    with pytest.raises(GardeArret, match="non convergée"):
        fc.logistique_l2("x", 15, seqs, y, 1.0)


def test_logistique_poids_par_action():
    """Dupliquer les jetons d'une action ne change pas la sonde (poids 1/n par action) — choix provisoire Q3."""
    seqs, y, _ = _donnees(n=12, d=6)
    a = fc.logistique_l2("x", 15, seqs, y, 1.0)
    seqs2 = list(seqs)
    seqs2[0] = np.concatenate([seqs[0], seqs[0]])
    b = fc.logistique_l2("x", 15, seqs2, y, 1.0)
    # la réduction (moyenne et écart-type des jetons) change un peu ; la direction réduite reste très proche
    assert np.corrcoef(a.w, b.w)[0, 1] > 0.99


def test_donnees_artefacts():
    seqs, y, _ = _donnees(n=6)
    with pytest.raises(GardeArret):
        fc.difference_moyennes_appariee("x", 15, seqs, np.zeros(6, int))  # une seule classe
    bad = list(seqs)
    bad[0] = bad[0].copy()
    bad[0][0, 0] = np.nan
    with pytest.raises(GardeArret):
        fc.logistique_l2("x", 15, bad, y, 1.0)
    with pytest.raises(GardeArret):
        fc.difference_moyennes_blanchie("x", 15, seqs, y[:-1], 0.5)


def _ridge_donnees(n=60, d=20, graine=3):
    rng = np.random.default_rng(graine)
    X = rng.standard_normal((n, d))
    beta = rng.standard_normal(d) * 0.3
    v = np.exp(X @ beta + 2.0 + 0.05 * rng.standard_normal(n))
    return X, v, beta


@pytest.mark.parametrize("n,d", [(80, 10), (15, 40)])
def test_ridge_sain_primal_et_dual(n, d):
    X, v, beta = _ridge_donnees(n, d)
    s = fc.regression_ridge_honnetes("r", X, v, 0.1)
    assert s.famille == "ridge_honnetes" and s.couche == 15
    pred = s.scores_par_jeton(X)
    if n > d:
        assert np.corrcoef(pred, np.log(v))[0, 1] > 0.95
    r = fc.residu_ridge(s, X, v)
    np.testing.assert_allclose(r, np.log(v) - pred, rtol=1e-12)
    # un déclarant qui gonfle sa valeur a un résidu positif
    r2 = fc.residu_ridge(s, X, v * 3.0)
    np.testing.assert_allclose(r2 - r, np.log(3.0), rtol=1e-12)


def test_ridge_primal_egal_dual():
    """Même solution en forme primale et duale (contrôle de la formule)."""
    X, v, _ = _ridge_donnees(30, 30)
    s = fc.regression_ridge_honnetes("r", X, v, 10.0)  # n = d : primale
    Xb = X.copy()
    mu, sd = Xb.mean(0), Xb.std(0)
    Z = (Xb - mu) / sd
    t = np.log(v)
    beta_dual = Z.T @ np.linalg.solve(Z @ Z.T + 10.0 * np.eye(30), t - t.mean())
    np.testing.assert_allclose(s.w, beta_dual / sd, rtol=1e-8)


def test_ridge_artefacts():
    X, v, _ = _ridge_donnees()
    with pytest.raises(GardeArret, match="≤ 0"):
        fc.regression_ridge_honnetes("r", X, np.where(np.arange(len(v)) == 0, 0.0, v), 1.0)
    with pytest.raises(GardeArret, match="alpha"):
        fc.regression_ridge_honnetes("r", X, v, 2.0)
    with pytest.raises(GardeArret):
        fc.regression_ridge_honnetes("r", X[:, 0], v, 1.0)
    s = fc.regression_ridge_honnetes("r", X, v, 1.0)
    with pytest.raises(GardeArret, match="ridge attendue"):
        fc.residu_ridge(fc.difference_moyennes_appariee("x", 15, *_donnees()[:2]), X, v)
    with pytest.raises(GardeArret):
        fc.residu_ridge(s, X, -v)


def test_scores_refuse_attention():
    s = SondeLineaireJetons("a", 15, "attention", np.ones(3), 0.0, np.ones(3))
    with pytest.raises(GardeArret, match="maximum"):
        fc.scores_actions(s, [np.zeros((2, 3))])


def _octets(s):
    return s.w.tobytes() + np.float64(s.b).tobytes()


@pytest.mark.parametrize("famille,reglage", [("difference_moyennes_appariee", None),
                                             ("difference_moyennes_blanchie", 0.1),
                                             ("logistique_l2", 1.0)])
def test_memes_octets_meme_machine(famille, reglage):
    seqs, y, _ = _donnees(graine=7)
    a = fc.apprendre(famille, "s", 15, seqs, y, reglage)
    b = fc.apprendre(famille, "s", 15, [q.copy() for q in seqs], y.copy(), reglage)
    assert _octets(a) == _octets(b)
    assert fc.scores_actions(a, seqs).tobytes() == fc.scores_actions(b, seqs).tobytes()


def test_memes_octets_deux_processus(tmp_path):
    """Deux processus distincts rendent les mêmes octets (aucun état caché)."""
    code = ("import numpy as np, hashlib, sys; sys.path[:0]=['src','tests'];"
            "from test_sondes_v2_formes_closes import _donnees; from controle_ia.sondes_v2 import formes_closes_v1 as fc;"
            "seqs,y,_=_donnees(graine=11); h=hashlib.sha256();"
            "[h.update(fc.scores_actions(fc.apprendre(f,'s',15,seqs,y,r),seqs).tobytes()) for f,r in "
            "[('difference_moyennes_appariee',None),('difference_moyennes_blanchie',0.5),('logistique_l2',0.01)]];"
            "print(h.hexdigest())")
    sorties = {subprocess.run([sys.executable, "-c", code], cwd=RACINE, capture_output=True, text=True,
                              check=True).stdout for _ in range(2)}
    assert len(sorties) == 1


@pytest.mark.parametrize("famille,reglage", [("difference_moyennes_appariee", None),
                                             ("difference_moyennes_blanchie", 0.1),
                                             ("logistique_l2", 1.0), ("logistique_l2", 0.001)])
def test_tolerance_entre_machines(famille, reglage, monkeypatch):
    """« Autre machine » simulée : quatre tâches de calcul linéaire au lieu d'une, et actions présentées dans un autre
    ordre (ordre des sommes changé). L'écart relatif des scores reste sous la tolérance déclarée."""
    seqs, y, _ = _donnees(graine=5, d=64, n=60)
    a = fc.apprendre(famille, "s", 15, seqs, y, reglage)
    perm = np.random.default_rng(0).permutation(len(seqs))
    monkeypatch.setattr(fc, "threadpool_limits", lambda n=1: threadpool_limits(4))
    b = fc.apprendre(famille, "s", 15, [seqs[i] for i in perm], y[perm], reglage)
    sa, sb = fc.scores_actions(a, seqs), fc.scores_actions(b, seqs)
    ecart = np.max(np.abs(sa - sb)) / np.max(np.abs(sa))
    assert ecart < fc.TOLERANCE_ENTRE_MACHINES[famille]


def test_tolerance_ridge_entre_machines(monkeypatch):
    X, v, _ = _ridge_donnees(80, 40)
    a = fc.regression_ridge_honnetes("r", X, v, 1.0)
    perm = np.random.default_rng(0).permutation(80)
    monkeypatch.setattr(fc, "threadpool_limits", lambda n=1: threadpool_limits(4))
    b = fc.regression_ridge_honnetes("r", X[perm], v[perm], 1.0)
    ra, rb = fc.residu_ridge(a, X, v), fc.residu_ridge(b, X, v)
    assert np.max(np.abs(ra - rb)) / np.max(np.abs(ra)) < fc.TOLERANCE_ENTRE_MACHINES["ridge_honnetes"]


def test_diagnostic_jamais_appele_par_le_paquet():
    """N-026 : la fonction « diagnostic » n'est appelée par aucun module du paquet sondes_v2."""
    paquet = RACINE / "src" / "controle_ia" / "sondes_v2"
    for f in paquet.glob("*.py"):
        arbre = ast.parse(f.read_text(encoding="utf-8"))
        for n in ast.walk(arbre):
            if isinstance(n, ast.Call):
                nom = getattr(n.func, "attr", None) or getattr(n.func, "id", None)
                assert nom != "diagnostic_moyenne_jetons", f"{f.name} appelle la fonction de diagnostic"


def test_aucun_import_de_torch_direct():
    paquet = RACINE / "src" / "controle_ia" / "sondes_v2"
    for f in paquet.glob("*.py"):
        for n in ast.walk(ast.parse(f.read_text(encoding="utf-8"))):
            if isinstance(n, ast.Import):
                assert all(a.name.split(".")[0] != "torch" for a in n.names), f.name
            if isinstance(n, ast.ImportFrom) and n.module:
                assert n.module.split(".")[0] != "torch", f.name
