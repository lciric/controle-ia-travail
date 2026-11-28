import time, numpy as np
from scipy.stats import rankdata
from controle_ia.sondes.evaluation import aire_sous_courbe
from controle_ia.premier_test_ia.statistiques import aire_stratifiee, strates_quantiles
rng = np.random.default_rng(0)
nt, pas = 60, 10
tache = np.repeat(np.arange(nt), 2 * pas)              # saboteur + honnête : 1 200 actions
y = np.tile(np.r_[np.ones(pas), np.zeros(pas)], nt).astype(int)
S = rng.normal(size=(y.size, 201)) + 0.2 * y[:, None]
membres = [np.flatnonzero(tache == t) for t in range(nt)]
def tirage():
    return np.concatenate([membres[c] for c in rng.integers(0, nt, nt)])
B = 40
t0 = time.perf_counter()
for _ in range(B):
    i = tirage(); [aire_sous_courbe(S[i, k], y[i]) for k in range(201)]
d1 = (time.perf_counter() - t0) / B
def auc_vect(M, yy):
    r = rankdata(M, axis=0); n1 = yy.sum(); n0 = yy.size - n1
    return (r[yy == 1].sum(axis=0) - n1 * (n1 + 1) / 2) / (n1 * n0)
t0 = time.perf_counter()
for _ in range(B):
    i = tirage(); a = auc_vect(S[i], y[i])
d2 = (time.perf_counter() - t0) / B
i = tirage(); a = auc_vect(S[i], y[i]); b = np.array([aire_sous_courbe(S[i, k], y[i]) for k in range(201)])
print(f"A1, un jeu de 1 200 actions, 201 aires par tirage : boucle gelée {d1*1e3:.1f} ms, vectorisée {d2*1e3:.1f} ms ; écart max {np.abs(a-b).max():.2e}")
print(f"  extrapolé à 2 000 tirages : {2000*d1:.0f} s (boucle), {2000*d2:.0f} s (vectorisée) par jeu")
# A4 (a) : tranches recalculées, 201 aires stratifiées par tirage, ~600 actions (saboteur qui gonfle + honnête)
lc = rng.normal(2, 0.5, y.size)
t0 = time.perf_counter()
for _ in range(10):
    i = tirage(); st = strates_quantiles(lc[i], 5); [aire_stratifiee(S[i, k], y[i], st) for k in range(201)]
d3 = (time.perf_counter() - t0) / 10
print(f"A4 (a), 201 aires stratifiées par tirage (boucle gelée) : {d3*1e3:.0f} ms ; 2 000 tirages : {2000*d3:.0f} s par sonde")
# A4 (b) : tâche pour tranche (60 tranches), 201 aires
t0 = time.perf_counter()
for _ in range(5):
    i = tirage(); [aire_stratifiee(S[i, k], y[i], tache[i]) for k in range(201)]
d4 = (time.perf_counter() - t0) / 5
print(f"A4 (b), tâche pour tranche, 201 aires par tirage (boucle gelée) : {d4*1e3:.0f} ms ; 2 000 tirages : {2000*d4:.0f} s par sonde")
