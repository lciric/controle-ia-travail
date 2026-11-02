"""Loi du nombre d'épisodes honnêtes éprouvés en alarme (sur 60) sous le nul échangeable : 60 tâches, 5 plis de 12,
seuil du pli = valeur d'ordre supérieure des 48 autres (k = 0, 1, 2). Aucune donnée réelle. Graine SeedSequence(20261102)."""
import numpy as np

g = np.random.default_rng(np.random.SeedSequence(20261102))
R = 200_000
x = g.random((R, 60))
plis = np.arange(60).reshape(5, 12)
for k in (0, 1, 2):
    total = np.zeros(R, dtype=np.int64)
    for f in range(5):
        autres = np.setdiff1d(np.arange(60), plis[f])
        tau = -np.sort(-x[:, autres], axis=1)[:, k]
        total += (x[:, plis[f]] > tau[:, None]).sum(axis=1)
    q = {j: float((total >= j).mean()) for j in range(1, 9)}
    print(f"k={k} moyenne={total.mean():.4f} (attendu {60 * (k + 1) / 49:.4f}) P(>=j)=" +
          ", ".join(f"{j}:{v:.4f}" for j, v in q.items()))
