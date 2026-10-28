"""Calculs de la carte des hypothèses des moniteurs, v1 — illustrations analytiques ou synthétiques des lemmes A7, A3 et
A9, jamais des mesures de nos instruments. Aucune donnée lue (ni `donnees/`, ni `diag/`, ni `runs/`, ni `pilotes/`).
Graines par numpy.random.SeedSequence (R9). Lancer : python3 -I -B calculs-carte-des-hypotheses-v1.py
"""
import math
from statistics import NormalDist

import numpy as np

N = NormalDist()
ss = np.random.SeedSequence(20261028)
g1, g2, g3 = (np.random.default_rng(s) for s in ss.spawn(3))


def puissance_plafond(delta, r0, T, alpha):
    """A7 : décalage constant delta (unités d'écart type total par action) sur les T actions d'un épisode, effet épisode
    de part de variance r0. Statistique exhaustive : la moyenne de l'épisode ; meilleur test de niveau alpha."""
    var = r0 + (1.0 - r0) / T if math.isfinite(T) else r0
    if var == 0:
        return 1.0
    return 1.0 - N.cdf(N.inv_cdf(1.0 - alpha) - delta / math.sqrt(var))


print("Bloc 1 — A7 : plafond de puissance sous effet épisode (analytique ; test optimal ; T = inf : plafond)")
for alpha in (0.01, 0.05):
    for delta in (0.3, 0.5):
        for r0 in (0.0, 0.1, 0.2, 0.5):
            ligne = [f"{puissance_plafond(delta, r0, T, alpha):.3f}" for T in (5, 10, 50, float('inf'))]
            print(f"  alpha={alpha:.2f} delta={delta:.1f} r0={r0:.1f} : T=5 {ligne[0]}  T=10 {ligne[1]}  T=50 {ligne[2]}  "
                  f"T=inf {ligne[3]}")
# Vérification par Monte-Carlo d'une cellule : alpha = 0,05, delta = 0,3, r0 = 0,2, T = 50, seuil sur la moyenne calibré
# sur 200 000 épisodes honnêtes simulés.
r0, delta, T, alpha, n = 0.2, 0.3, 50, 0.05, 200_000
def episodes(n, d):
    b = g1.normal(0.0, math.sqrt(r0), size=(n, 1))
    e = g1.normal(0.0, math.sqrt(1 - r0), size=(n, T))
    return (b + e + d).mean(axis=1)
h = np.quantile(episodes(n, 0.0), 1 - alpha)
mc = float((episodes(n, delta) > h).mean())
print(f"  Monte-Carlo (alpha=0.05, delta=0.3, r0=0.2, T=50) : {mc:.4f} ; analytique {puissance_plafond(delta, r0, T, alpha):.4f}")

print("Bloc 2 — A3 : identité de Page, max_t C_t = max(0, max_{a<=b} somme_{a..b}(z_t - k)) (scores de Student, 3 ddl)")
ecart = 0.0
for k in (0.0, 0.5, 1.0):
    for _ in range(2000):
        z = g2.standard_t(3, size=30)
        c, mc_ = 0.0, 0.0
        for v in z:
            c = max(0.0, c + v - k)
            mc_ = max(mc_, c)
        s = np.concatenate([[0.0], np.cumsum(z - k)])
        meilleur = max(0.0, max(s[b] - s[a] for a in range(31) for b in range(a + 1, 31)))
        ecart = max(ecart, abs(mc_ - meilleur))
print(f"  6 000 suites, k dans {{0 ; 0,5 ; 1}} : écart maximal {ecart:.2e}")

print("Bloc 3 — A9 : égalité des lois du maximum, n jetons de loi F contre m < n jetons de loi G = F^(n/m)")
n_, m_ = 200, 100
x = g3.standard_normal(size=(20_000, n_)).max(axis=1)
u = g3.uniform(size=(20_000, m_)) ** (m_ / n_)          # G^-1(u) = F^-1(u^(m/n))
y = np.array([N.inv_cdf(float(v)) for v in u.max(axis=1)])
q = (0.5, 0.9, 0.99)
print("  quantiles du maximum, F sur 200 jetons :", " ".join(f"{float(np.quantile(x, p)):.3f}" for p in q))
print("  quantiles du maximum, G sur 100 jetons :", " ".join(f"{float(np.quantile(y, p)):.3f}" for p in q))
print(f"  médiane de G contre médiane de F par jeton : {N.inv_cdf(0.5 ** (m_ / n_)):.3f} contre 0.000 (G domine F)")
