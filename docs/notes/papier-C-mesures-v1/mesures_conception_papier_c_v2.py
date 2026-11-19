"""Mesures de conception du préenregistrement du papier C (brouillon 4) : aucune donnée, aucun résultat lu.

Version 2 (2026-11-19) : même calcul que la version 1 (mesures_conception_papier_c_v1.py), plus deux sorties :
les versions de numpy et de scipy en tête, et la ligne « P(W ≤ 0,20) sous le nul » à la fin.

1. Clopper-Pearson : plus petit nombre de détections x, sur N essais, dont la borne basse de l'intervalle bilatéral
   à 95 % atteint 0,90 (critère de C-P5).
2. W de Kendall, 5 familles (évaluateurs) et 3 juges (objets), sans ex aequo : loi exacte sous le nul
   (6^5 = 7 776 affectations), valeur critique au seuil 0,05 (C-P3a) ; espérance sous le nul.
"""
import itertools

import numpy as np
import scipy
from scipy.stats import beta

print(f"numpy {np.__version__} ; scipy {scipy.__version__}")

print("1. Clopper-Pearson, bilatéral 95 %, borne basse >= 0,90")
print("N\tx_min\tx_min/N")
for n in (60, 90, 120, 180, 240, 300, 360, 450, 600, 900, 1200):
    xs = [x for x in range(n + 1) if x > 0 and beta.ppf(0.025, x, n - x + 1) >= 0.90]
    print(f"{n}\t{xs[0]}\t{xs[0] / n:.4f}")

print()
print("2. W de Kendall, m = 5 évaluateurs, 3 objets, loi exacte sous le nul")
perms = list(itertools.permutations([1, 2, 3]))
m, k = 5, 3
w = []
for combo in itertools.product(range(len(perms)), repeat=m):
    r = np.sum([perms[c] for c in combo], axis=0)
    s = float(((r - r.mean()) ** 2).sum())
    w.append(12 * s / (m ** 2 * (k ** 3 - k)))
w = np.array(w)
print("W\tP(W >= w)")
for v in sorted(set(np.round(w, 4))):
    print(f"{v:.2f}\t{(w >= v - 1e-9).mean():.4f}")
print(f"espérance sous le nul : {w.mean():.4f} ; affectations : {len(w)}")
print(f"P(W ≤ 0,20) sous le nul = {(w <= 0.20 + 1e-9).mean():.4f}".replace("= 0.", "= 0,"))
