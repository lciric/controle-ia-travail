"""Essais des sondes, du sac de jetons, des détecteurs et du rééchantillonnage du volet A, sur données synthétiques."""
import numpy as np
from sklearn.metrics import roc_auc_score

from controle_ia.neuron_lens import volet_a_sondes_v1 as vs


def _jeu(n=120, d=20, graine=0, signal=2.0):
    rng = np.random.default_rng(graine)
    y = np.array([0, 1] * (n // 2))
    X = rng.normal(size=(n, d))
    X[:, 3] += signal * y
    g = np.repeat(np.arange(n // 2), 2)  # paires contenant les deux classes
    return X, y, g


def test_sonde_apprend_et_est_deterministe():
    X, y, g = _jeu()
    s1, s2 = vs.apprendre_sonde(X, y, g), vs.apprendre_sonde(X, y, g)
    assert np.allclose(s1.w_std, s2.w_std) and s1.C == s2.C and s1.C in vs.GRILLE_C
    assert np.argmax(np.abs(s1.w_std)) == 3
    Xt, yt, _ = _jeu(graine=1)
    assert roc_auc_score(yt, s1.scores(Xt)) > 0.75  # AUROC de Bayes ≈ 0,92 ; 20 traits dont 19 de bruit


def test_sonde_trait_constant():
    X, y, g = _jeu()
    X[:, 5] = 7.0
    s = vs.apprendre_sonde(X, y, g)
    assert np.isfinite(s.w_std).all()


def test_sac_de_jetons_et_premiers():
    rng = np.random.default_rng(0)
    y = np.array([0, 1] * 60)
    listes = [list(rng.integers(100, 140, size=8)) + ([7] if c else [9]) for c in y]
    g = np.repeat(np.arange(60), 2)
    sac = vs.apprendre_sac(listes, y, g)
    pos, neg = sac.premiers()
    assert pos[0] == 7 and neg[0] == 9
    assert roc_auc_score(y, sac.scores(listes)) > 0.95
    assert np.all(sac.scores([[999, 998]]) == sac.modele.intercept_[0])  # jetons inconnus ignorés


def test_ecart_moyen_standardise():
    X, y, _ = _jeu()
    assert np.argmax(vs.ecart_moyen_standardise(X, y)) == 3


def test_detecteurs_et_composantes():
    X, y, g = _jeu(d=600)
    Xt, yt, _ = _jeu(d=600, graine=2)
    out = vs.detecteurs(X, y, g, {"test": Xt}, graine_aleatoire=3, n_tirages=2)
    assert set(out["test"]) >= {"k1", "k8", "k64", "k512", "dense", "hasard1", "hasard512"}
    assert roc_auc_score(yt, out["test"]["k1"]) > 0.85 and len(out["test"]["hasard8"]) == 2
    c = vs.composantes(X, y, g, {"test": Xt}, 8)
    assert c["test"].shape == (len(yt),)


def test_borne_basse_appariee():
    rng = np.random.default_rng(0)
    ys, a, b = [], [], []
    for _ in range(5):
        y = np.array([0, 1] * 30)
        ys.append(y)
        a.append(y * 2.0 + rng.normal(size=60))
        b.append(y * 0.2 + rng.normal(size=60))
    obs, bas, haut = vs.borne_basse_appariee(a, b, ys, graine=1, n=200)
    assert bas > 0 and bas <= obs <= haut
    obs0, bas0, haut0 = vs.borne_basse_appariee(a, a, ys, graine=1, n=50)
    assert obs0 == 0 and bas0 == 0 and haut0 == 0
