"""Essais (v2) des sondes, du sac de jetons, des détecteurs et du rééchantillonnage du volet A, sur données synthétiques."""
import numpy as np
import pytest
from sklearn.metrics import roc_auc_score

from controle_ia.neuron_lens import volet_a_sondes_v2 as vs


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
    c, k = vs.composantes(X, y, g, {"test": Xt}, 8)
    assert c["test"].shape == (len(yt),) and k == 8


def test_borne_basse_appariee():
    rng = np.random.default_rng(0)
    ys, a, b = [], [], []
    for _ in range(5):
        y = np.array([0, 1] * 30)
        ys.append(y)
        a.append(y * 2.0 + rng.normal(size=60))
        b.append(y * 0.2 + rng.normal(size=60))
    obs, bas, haut = vs.borne_basse_appariee(a, b, ys, graines=[1, 2, 3, 4, 5], n=200)
    assert bas > 0 and bas <= obs <= haut
    obs0, bas0, haut0 = vs.borne_basse_appariee(a, a, ys, graines=[1, 2, 3, 4, 5], n=50)
    assert obs0 == 0 and bas0 == 0 and haut0 == 0


# ---------------------------------------------------------------- ajouts v2 (contre-lecture 1, remarques 1, 2, 6, 8 à 10, 12)
def test_composantes_k_plafonne():
    X, y, g = _jeu(n=40, d=600)
    c, k = vs.composantes(X, y, g, {"t": X}, 512)
    assert k == 39 and c["t"].shape == (40,)


def test_borne_une_graine_par_decoupe():
    rng = np.random.default_rng(0)
    ys = [np.array([0, 1] * 30) for _ in range(5)]
    a = [y * 1.0 + rng.normal(size=60) for y in ys]
    b = [rng.normal(size=60) for _ in ys]
    with pytest.raises(ValueError):
        vs.borne_basse_appariee(a, b, ys, graines=[1], n=10)
    r1 = vs.borne_basse_appariee(a, b, ys, graines=[1, 2, 3, 4, 5], n=100)
    r2 = vs.borne_basse_appariee(a, b, ys, graines=[1, 2, 3, 4, 5], n=100)
    r3 = vs.borne_basse_appariee(a, b, ys, graines=[5, 4, 3, 2, 1], n=100)
    assert r1 == r2 and r1[0] == r3[0] and r1[1:] != r3[1:]  # graine propre à chaque découpe


def test_detecteurs_reproductibles_et_graine():
    X, y, g = _jeu(d=520)
    o1 = vs.detecteurs(X, y, g, {"t": X}, graine_aleatoire=np.random.SeedSequence(7), n_tirages=2)
    o2 = vs.detecteurs(X, y, g, {"t": X}, graine_aleatoire=np.random.SeedSequence(7), n_tirages=2)
    o3 = vs.detecteurs(X, y, g, {"t": X}, graine_aleatoire=np.random.SeedSequence(8), n_tirages=2)
    assert all(np.array_equal(a, b) for a, b in zip(o1["t"]["hasard8"], o2["t"]["hasard8"]))
    assert not all(np.array_equal(a, b) for a, b in zip(o1["t"]["hasard8"], o3["t"]["hasard8"]))


def test_pli_monoclasse_refuse():
    X, y, g = _jeu()
    g = y.copy()  # deux groupes, chacun d'une seule classe : pli interne monoclasse
    with pytest.raises(ValueError):
        vs.apprendre_sonde(X, y, g)


def test_egalite_de_c_garde_le_plus_petit():
    X, y, g = _jeu(signal=50.0, d=5)  # séparation parfaite : AUROC 1 pour toute la grille
    assert vs.apprendre_sonde(X, y, g).C == vs.GRILLE_C[0]


def test_premiers_moins_de_dix():
    y = np.array([0, 1] * 30)
    listes = [[7] if c else [9] for c in y]
    sac = vs.apprendre_sac(listes, y, np.repeat(np.arange(30), 2))
    pos, neg = sac.premiers()
    assert pos == [7] and neg == [9]


def test_avertissements_de_convergence_comptes():
    vs.AVERTISSEMENTS["convergence"] = 0
    X, y, g = _jeu()
    s = vs.apprendre_sonde(X, y, g)
    assert s.n_avertissements >= 0 and vs.AVERTISSEMENTS["convergence"] >= s.n_avertissements
