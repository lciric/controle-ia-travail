"""Question témoin T4 : écart standardisé d'un détecteur d'aire 0,70 sous deux lois normales de même écart type,
et rappel à 1 % de fausses alertes. Calcul fermé, vérifié par simulation (graine par numpy.random.SeedSequence)."""
import json, sys
import numpy as np
from scipy.stats import norm

aire = 0.70
d = float(np.sqrt(2.0) * norm.ppf(aire))            # aire = Phi(d / sqrt(2))
rappel = float(1.0 - norm.cdf(norm.ppf(0.99) - d))   # seuil au quantile 0,99 des négatifs
ss = np.random.SeedSequence(entropy=20261128, spawn_key=(4,))
rng = np.random.default_rng(ss)
n = 2_000_000
neg = rng.standard_normal(n)
pos = rng.standard_normal(n) + d
seuil = np.quantile(neg, 0.99)
rappel_sim = float((pos > seuil).mean())
# aire simulée par rangs sur un sous-échantillon
m = 200_000
x = np.concatenate([neg[:m], pos[:m]])
r = x.argsort().argsort() + 1
aire_sim = float((r[m:].sum() - m * (m + 1) / 2) / (m * m))
out = {"aire": aire, "ecart_standardise": d, "rappel_a_1_pour_cent": rappel,
       "simulation": {"n": n, "rappel": rappel_sim, "aire_sur_200000": aire_sim},
       "graine": {"entropy": 20261128, "spawn_key": [4]}}
json.dump(out, sys.stdout, indent=1, ensure_ascii=False)
