"""Diagnostic (outil de développement) : divergence entre deux softmax aléatoires sur les instances d'une sous-population,
minimum des deux sens, selon la force ; et taille de réservoir atteignable par rejet séquentiel à 0,5 nat."""
import sys

import numpy as np

sys.path.insert(0, sys.argv[1])
from controle_ia.heritage_etage_processeur_v1 import lois as L

Z, G = L.instances_oracle(12345, 4000)
Zg = Z[G == 1]
Gg = G[G == 1]


def kl(a, b):
    P, Q = L.matrice(a, Zg, Gg), L.matrice(b, Zg, Gg)
    return float(np.mean(np.sum(P * (np.log(P) - np.log(Q)), axis=1)))


for force in (1.5, 2.0, 3.0, 4.0):
    rng = np.random.default_rng(3)
    def sm():
        return {"type": "softmax", "poids": np.round(rng.normal(0, force, (3, 2)), 6).tolist(),
                "biais": np.round(rng.normal(0, 0.3, 3), 6).tolist()}
    d = []
    for _ in range(400):
        a, b = sm(), sm()
        d.append(min(kl(a, b), kl(b, a)))
    d = np.array(d)
    pool, essais = [], 0
    while len(pool) < 90 and essais < 3000:
        c = sm()
        essais += 1
        if all(min(kl(c, p), kl(p, c)) >= 0.5 for p in pool):
            pool.append(c)
    print("force", force, "P(<0,5)", round(float(np.mean(d < 0.5)), 3), "quantiles", np.round(np.quantile(d, [0.01, 0.05, 0.5]), 3),
          "réservoir", len(pool), "essais", essais)
