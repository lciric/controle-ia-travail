"""Prédicteur de Bayes (oracle) dans le même modèle gaussien : puissance au seuil 0,05, 2000 épisodes d'épreuve."""
import numpy as np
from scipy import stats
ss = np.random.SeedSequence(20261123)
rng = np.random.default_rng(ss.spawn(1)[0])
delta = 2 * stats.norm.ppf((1 + 0.07) / 2)
reps, B, n = 2000, 199, 2000
rej = 0
for _ in range(reps):
    S = rng.integers(0, 2, n)
    x = rng.standard_normal(n) + delta * S
    pred = (x > delta / 2).astype(int)
    def ba(Sv):
        return 0.5 * (pred[Sv == 1].mean() + (1 - pred[Sv == 0]).mean())
    t = ba(S)
    cnt = sum(ba(rng.permutation(S)) >= t for _ in range(B))
    rej += (1 + cnt) / (B + 1) <= 0.05
print("oracle, puissance simulée :", rej / reps, "; formule :", stats.norm.sf(1.6449 - 0.035 / (np.sqrt(2 / 1000) / 4)))
