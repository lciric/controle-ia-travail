"""Aires vectorisées des trois candidats contre le code gelé, ex aequo massifs et tranches."""
import numpy as np
from commun import A, B, GE
from controle_ia.sondes.evaluation import aire_sous_courbe
from controle_ia.premier_test_ia.statistiques import aire_stratifiee

rng = np.random.default_rng(12345)
pire = {"A": 0.0, "B": 0.0, "G": 0.0, "A_strat": 0.0, "B_strat": 0.0, "G_strat": 0.0}
cas = 0
for essai in range(400):
    n = int(rng.integers(2, 120)); k = int(rng.integers(1, 8))
    mode = essai % 4
    if mode == 0:
        X = rng.integers(0, 3, size=(n, k)).astype(float)          # ex aequo massifs
    elif mode == 1:
        X = rng.normal(size=(n, k))
    elif mode == 2:
        X = np.round(rng.normal(size=(n, k)), 1)
    else:
        X = np.full((n, k), 0.7); X[: n // 2, 0] = 0.3               # colonnes constantes
    y = rng.integers(0, 2, size=n)
    if y.min() == y.max():
        y[0] = 1 - y[0]
    st = rng.integers(0, int(rng.integers(1, 7)), size=n).astype(str)
    ref = np.array([aire_sous_courbe(X[:, c], y) for c in range(k)])
    pire["A"] = max(pire["A"], np.max(np.abs(A.aires_par_rangs(X, y) - ref)))
    pire["B"] = max(pire["B"], np.max(np.abs(B.aires_par_rangs(X.T, y) - ref)))
    pire["G"] = max(pire["G"], np.max(np.abs(GE.aires_par_rangs(X, y) - ref)))
    refs = [aire_stratifiee(X[:, c], y, st) for c in range(k)]
    ra, rb = A.aires_stratifiees_par_rangs(X, y, st), B.aires_par_rangs(X.T, y, st)
    rg = GE._aires_stratifiees_2d(X, y, st)
    if refs[0] is None:
        assert ra is None and rb is None and rg is None
        continue
    refs = np.array(refs)
    pire["A_strat"] = max(pire["A_strat"], np.max(np.abs(ra - refs)))
    pire["B_strat"] = max(pire["B_strat"], np.max(np.abs(rb - refs)))
    pire["G_strat"] = max(pire["G_strat"], np.max(np.abs(rg - refs)))
    cas += 1
print("cas stratifiés lus :", cas)
for k, v in pire.items():
    print(f"{k:8s} écart maximal {v:.3e}")
