"""Croisement des trois noyaux (a, b, Gemini corrigé d'une indentation) : aires par rangs contre le code gelé, et
plancher conjoint sur le même flux de tirages (même graine, mêmes appels rng.integers) : les intervalles doivent être
identiques. Puis durée d'un plancher conjoint (800 actions, 201 sondes, N tirages) par noyau."""
import importlib.util, sys, time, json
sys.dont_write_bytecode = True
import numpy as np
from controle_ia.sondes.evaluation import aire_sous_courbe
from controle_ia.premier_test_ia.statistiques import aire_stratifiee, strates_quantiles
C = "/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/addendum-p3"
def charger(nom, chemin):
    spec = importlib.util.spec_from_file_location(nom, chemin); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
A = charger("ca", C + "/candidat-a/complements_p3_v1.py")
B = charger("cb", C + "/candidat-b/complements_p3_v1.py")
Gm = charger("cg", sys.argv[1])
N = int(sys.argv[2])
rng = np.random.default_rng(3)
pire = {"a": 0.0, "b": 0.0, "g": 0.0, "a_strat": 0.0, "b_strat": 0.0, "g_strat": 0.0}
for essai in range(30):
    n = int(rng.integers(30, 400)); k = 9
    X = np.round(rng.normal(size=(n, k)), int(rng.integers(0, 2)))
    y = (rng.random(n) < 0.4).astype(np.int64); y[:2] = [0, 1]
    i = rng.integers(0, n, n); X, y = X[i], y[i]
    if y.min() == y.max(): continue
    ref = np.array([aire_sous_courbe(X[:, c], y) for c in range(k)])
    pire["a"] = max(pire["a"], np.abs(A.aires_par_rangs(X, y) - ref).max())
    pire["b"] = max(pire["b"], np.abs(B.aires_par_rangs(X.T, y) - ref).max())
    pire["g"] = max(pire["g"], np.abs(Gm.aires_par_rangs(X, y) - ref).max())
    st = rng.integers(0, 5, n)
    refs = [aire_stratifiee(X[:, c], y, st) for c in range(k)]
    if refs[0] is not None:
        refs = np.array(refs)
        pire["a_strat"] = max(pire["a_strat"], np.abs(A.aires_stratifiees_par_rangs(X, y, st) - refs).max())
        pire["b_strat"] = max(pire["b_strat"], np.abs(B.aires_par_rangs(X.T, y, st) - refs).max())
        pire["g_strat"] = max(pire["g_strat"], np.abs(Gm._aires_stratifiees_2d(X, y, st) - refs).max())
print("écart maximal au code gelé :", {k: float(v) for k, v in pire.items()})
# plancher conjoint, même flux
n, npl = 800, 200
taches = np.repeat(np.arange(40), 20)
y = (rng.random(n) < 0.5).astype(np.int64)
s = rng.normal(size=n) + 0.6 * y
Pl = rng.normal(size=(n, npl)) + 0.05 * y[:, None]
A.TIRAGES_AIRE = B.TIRAGES_AIRE = N
res, durees = {}, {}
d = time.perf_counter(); ra = A.plancher_conjoint(s, Pl, y, taches, np.random.default_rng(7), N, 0.95); durees["a"] = time.perf_counter() - d
d = time.perf_counter(); rb = B.ecart_conjoint(s, Pl, y, taches, np.random.default_rng(7), N, 0.95); durees["b"] = time.perf_counter() - d
d = time.perf_counter(); rg = Gm.plancher_conjoint(s, Pl, y, taches, N, 7, 0.95); durees["g"] = time.perf_counter() - d
print("plancher conjoint (bas, haut de Δ) :", (ra["ecart_bas"], ra["ecart_haut"]), (rb["ecart_bas"], rb["ecart_haut"]), (rg["bas"], rg["haut"]))
print("identiques :", ra["ecart_bas"] == rb["ecart_bas"] == rg["bas"] and ra["ecart_haut"] == rb["ecart_haut"] == rg["haut"])
# T4 aux tranches internes, même flux
v = np.log10(10 ** rng.normal(1, 0.4, n))
d = time.perf_counter(); ta = A.plancher_conjoint(s, Pl, y, taches, np.random.default_rng(9), N, 0.95, valeurs_tranches=v); durees["a_T4"] = time.perf_counter() - d
d = time.perf_counter(); tb = B.ecart_conjoint(s, Pl, y, taches, np.random.default_rng(9), N, 0.95, "internes", v); durees["b_T4"] = time.perf_counter() - d
d = time.perf_counter(); tg = Gm.t4_tranches_internes(s, Pl, y, v, taches, 5, N, 9, 0.95); durees["g_T4"] = time.perf_counter() - d
print("T4 internes (Δ bas, aire bas) :", (ta["ecart_bas"], ta["aire_bas"]), (tb["ecart_bas"], tb["aire_bas"]), (tg["delta_bas"], tg["bas"]))
print("identiques :", ta["ecart_bas"] == tb["ecart_bas"] == tg["delta_bas"] and ta["aire_bas"] == tb["aire_bas"] == tg["bas"])
print("durées (s) pour", N, "tirages :", {k: round(x, 2) for k, x in durees.items()})
