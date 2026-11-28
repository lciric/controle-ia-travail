"""Mesure de la durée de l'addendum sur des données synthétiques de la taille du run réel : 2 400 actions notées
(60 tâches × 4 conditions × 10 pas), 430 sondes (2 principales, 2 × 200 planchers, 28 autres), 2 000 tirages pour les
aires, 10 000 pour les coûts, R = 50 fenêtres."""
import sys, time, json
sys.dont_write_bytecode = True
sys.path.insert(0, "..")
import numpy as np
import test_complements_p3_v1 as T
A, lp = T.A, T.lp
tirages = int(sys.argv[1]) if len(sys.argv) > 1 else A.TIRAGES_AIRE
A.TIRAGES_AIRE = tirages
lp.TIRAGES_AIRE, lp.TIRAGES_COUT = 300, 2000            # la lecture décisive n'est pas mesurée ici
src = T._source(0, n_taches=60, n_pl=200)
t = src["tables"]
rng = np.random.default_rng(1)
t["noms_sondes"] = np.concatenate([t["noms_sondes"], np.array([f"autre-{k}" for k in range(28)])])
t["scores"] = np.concatenate([t["scores"], rng.normal(size=(t["scores"].shape[0], 28))], axis=1)
src = T._completer(src)
print("actions", t["scores"].shape, "tirages aire", A.TIRAGES_AIRE, "tirages coût", A.TIRAGES_COUT, flush=True)
d = time.perf_counter(); lec = T._lire(src); print("lecture (non mesurée)", round(time.perf_counter() - d, 1), flush=True)
D = A._preparer(src, lec); C = A.conclusions_de_la_lecture(lec, T.P)
total = 0.0
for a in A.ANALYSES:
    d = time.perf_counter()
    if a in A.ANALYSES_GLOBALES:
        e = [A._executer(a, D, C, T.G, None, None)]
    else:
        e = [A._executer(a, D, C, T.G, k, p) for k, p in enumerate(T.P)]
    dt = time.perf_counter() - d; total += dt
    print(a, round(dt, 1), "s", [x["statut"] for x in e], flush=True)
print("total des analyses", round(total, 1), "s", flush=True)
d = time.perf_counter(); s = A.analyser_addendum(src, lec, T.G); print("analyser_addendum complet", round(time.perf_counter() - d, 1), "s", flush=True)
print("réserves", [r["reserve"] for r in s["reserves_addendum"]])
