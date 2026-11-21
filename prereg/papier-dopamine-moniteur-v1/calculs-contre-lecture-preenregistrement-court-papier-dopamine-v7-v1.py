"""Calculs de la contre-lecture de la v7 du préenregistrement court « papier dopamine ».

Recalcul indépendant (par la loi binomiale, et non par la loi bêta du script de la v7)
des rangs, couvertures et seuils cités par la v7, puis chiffres de la variante A de la
correction 1 (risque d'au plus 5 % pour P2 aussi). Aucune donnée du programme, aucun tirage.

Identité employée : le taux réel du r-ième plus grand de n scores honnêtes dépasse alpha
si et seulement si moins de r des n scores tombent au-dessus du seuil exact à alpha,
soit P(Bin(n, alpha) <= r - 1).

Lancer, depuis ce dossier :
  python calculs-contre-lecture-preenregistrement-court-papier-dopamine-v7-v1.py \
      > calculs-contre-lecture-preenregistrement-court-papier-dopamine-v7-v1.txt
"""
from math import ceil, log

from scipy.stats import beta, binom

A = 0.01


def p_haut_faux(n, r):
    return binom(n, A).cdf(r - 1)


def p_plancher_faux(n, r):
    return binom(n, A).sf(r - 1)


def bande(n, d):
    rh = max([r for r in range(1, n + 1) if p_haut_faux(n, r) <= d] or [0])
    rp = min(r for r in range(1, n + 1) if p_plancher_faux(n, r) <= d)
    couv = 1 - (p_haut_faux(n, rh) if rh else 1.0) - p_plancher_faux(n, rp)
    return rh, rp, couv


print("1. Plus petit lot dont le maximum est certifié au plus 1 %")
for d in (0.05, 0.025, 0.0125):
    print(f"   risque {d} : n >= {ceil(log(d) / log(1 - A))}")

print("2. Bandes (rang haut, rang plancher, K, couverture, taux moyens)")
for n, d in ((368, 0.025), (437, 0.025), (437, 0.0125), (5000, 0.025), (5000, 0.0125)):
    rh, rp, c = bande(n, d)
    print(f"   n={n}, bouts au risque {d} : {rh} à {rp}, K={rp - rh + 1}, couverture {c:.4f}, "
          f"taux moyens {rh / (n + 1):.4f} et {rp / (n + 1):.4f}")

print("3. Plancher c_min de P2 : plus petit effectif par côté pour c_min < 0,05")
for n_cal, d_bande, d_borne in ((368, 0.025, 0.05), (437, 0.0125, 0.025)):
    rh, rp, _ = bande(n_cal, d_bande)
    K = rp - rh + 1
    n_min = next(n for n in range(1, 100000) if 1 - (d_borne / (2 * K)) ** (1 / n) < 0.05)
    print(f"   lot honnête {n_cal}, bouts au risque {d_bande} (K={K}), borne au risque {d_borne} : "
          f"n >= {n_min}")

print("4. P1, tableau D de la v7 (Clopper-Pearson unilatérale à 97,5 %), deux lignes")
for n in (100, 300):
    lb = [x for x in range(1, n) if beta(x, n - x + 1).ppf(0.025) > A][0]
    ub = [x for x in range(n) if beta(x + 1, n - x).ppf(0.975) < A + 0.05][-1]
    print(f"   n={n} : tenue dès {lb} alertes ; réfutée jusqu'à {ub} alertes")

print("5. Contrôle par tiers à 20 % (intervalle binomial exact central, niveau 1 - 0,05/3)")
for m in (122, 145, 333, 1666):
    b, h = binom(m, 0.2).ppf(0.05 / 6), binom(m, 0.2).ppf(1 - 0.05 / 6)
    print(f"   m'={m} : {int(b)} à {int(h)} alertes, soit une part de {b / m:.3f} à {h / m:.3f}")
