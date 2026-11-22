"""Compléments : points morts à 8 000 épisodes, épisodes partagés ou séparés, statistique de queue à 4 000 épisodes d'épreuve,
budgets au seuil 0,05, confirmation de l'option corrigée."""
import numpy as np
from scipy import stats
K = 30
zb = stats.norm.isf(0.2)
r = ((stats.norm.isf(0.0125 / K) + zb) / (stats.norm.isf(0.05 / K) + zb)) ** 2
print("rapport d'épisodes à sensibilité égale :", r)
for N in [4000, 8000]:
    extra_test = N * (r - 1)
    for mode, extra in [("séparés", 4 * extra_test), ("partagés", extra_test)]:
        for conf in [2000, 4000]:
            D = extra / 0.15 - conf
            print(f"budget {N}, épisodes {mode}, confirmation {conf}: surcoût à sensibilité égale {extra:,.0f} ; point mort D < {D:,.0f}")

def et(n, pi):
    return np.sqrt(1 / (pi * n) + 1 / ((1 - pi) * n)) / 4
# confirmation de (d) à sa plus petite fuite
t_d = 2 * (stats.norm.isf(0.0125 / K) + zb) * et(4000, 0.5)
print("(d) fuite", t_d, "confirmation 4000 neufs :", stats.norm.sf(stats.norm.isf(0.05) - (t_d / 2) / et(4000, 0.5)))
# budgets au seuil 0,05 pour une fuite de 0,05
for a in [0.05, 0.0125]:
    z = stats.norm.isf(a / K) + zb
    n_ep = (z / 0.05) ** 2
    print(f"seuil {a}, fuite 0,05, puissance 0,8 : {2*n_ep:,.0f} épisodes (pile ou face), {2*n_ep/(4*0.05*0.95):,.0f} (5 %)")
# statistique de queue, 4000 épisodes d'épreuve, hypergéométrique exacte
for a in [0.05, 0.0125]:
    ap = a / 90
    n, n1 = 4000, 200
    for k in range(50, 400):
        if stats.hypergeom.pmf(0, n, n1, k) <= ap:
            print(f"seuil {a}, 4000 d'épreuve : k={k}, masse {k/(n-n1):.4f}")
            break
    n, n1 = 2000, 100
    for k in range(50, 400):
        if stats.hypergeom.pmf(0, n, n1, k) <= ap:
            print(f"seuil {a}, 2000 d'épreuve : k={k}, masse {k/(n-n1):.4f}")
            break
# épreuve à pile ou face : plus petite fuite de (d)
print("(d) à pile ou face :", t_d, "; (d) à 5 % :", 2 * (stats.norm.isf(0.0125 / K) + zb) * et(4000, 0.05))
# taille minimale de permutations
print("permutations minimales pour 0,0125 :", 1 / 0.0125 - 1)
