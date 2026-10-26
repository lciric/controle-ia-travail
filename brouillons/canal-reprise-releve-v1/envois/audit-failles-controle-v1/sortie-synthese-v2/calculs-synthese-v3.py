# Calculs de la synthese de l'audit, version 3 : correctif du bloc 5 de calculs-synthese-v2
# (la colonne « prediction » y employait la fiabilite rho de v0 au lieu de la fiabilite R du
# regresseur c - v0 ; les pentes simulees de v2 sont justes) et petits calculs de la synthese v2.
# Illustrations analytiques ou synthetiques, jamais des mesures ; graines SeedSequence (R9).
import numpy as np

ss = np.random.SeedSequence(20261026)
enfants = ss.spawn(10)

print("== bloc 5 corrige : pente brute = g R + (1 - R), R = 1 - var(e0) / var(c - v0)")
rng = np.random.default_rng(enfants[8])
N = 400_000
for rho in (0.5, 0.7, 0.9):
    for g in (0.0, 0.5):
        T = rng.standard_normal(N)
        se = np.sqrt((1 - rho) / rho)
        v0 = T + se * rng.standard_normal(N)
        c = rng.choice([-1.0, 1.0], N) * 1.5
        v1 = T + g * (c - T) + se * rng.standard_normal(N)
        x = c - v0
        y = v1 - v0
        pente = np.cov(x, y)[0, 1] / np.var(x, ddof=1)
        R_th = (2.25 + 1.0) / (2.25 + 1.0 + se ** 2)
        v0b = T + se * rng.standard_normal(N)
        var_e = np.var(v0 - v0b, ddof=1) / 2.0
        R_est = 1.0 - var_e / np.var(x, ddof=1)
        print(f"rho={rho} g={g} : pente brute {pente:.4f} ; g R + (1 - R) = {g * R_th + 1 - R_th:.4f} (R = {R_th:.4f}) ; "
              f"R estime par double lecture de v0 {R_est:.4f} ; g desattenue {(pente - (1 - R_est)) / R_est:.4f}")

print("== combinaison des lectures de G1 entre modes")
for a in (0.05, 0.01):
    for m in (2, 3):
        print(f"alpha={a} m={m} : au moins un mode, sans correction {1 - (1 - a) ** m:.4f} ; Bonferroni par mode {a / m:.4f} ; intersection-union : au plus {a}")

print("== erreur type d'une aire sous la courbe (Hanley et McNeil), n episodes par classe")
def se_auc(A, n1, n2):
    Q1 = A / (2 - A)
    Q2 = 2 * A * A / (1 + A)
    return np.sqrt((A * (1 - A) + (n1 - 1) * (Q1 - A * A) + (n2 - 1) * (Q2 - A * A)) / (n1 * n2))
for A in (0.575, 0.60, 0.75):
    for n in (120, 240, 500, 1000, 1500):
        s = se_auc(A, n, n)
        print(f"A={A} n={n} : erreur type {s:.4f} ; demi-largeur a 90 % {1.645 * s:.4f} ; a 95 % {1.96 * s:.4f}")

print("== borne haute a 95 % d'une proportion nulle observee sur n essais (Clopper et Pearson)")
for n in (30, 50, 100):
    print(f"n={n} : {1 - 0.05 ** (1 / n):.4f}")
