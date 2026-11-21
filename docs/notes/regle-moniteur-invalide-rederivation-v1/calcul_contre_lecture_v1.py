"""Contre-lecture de la re-dérivation « moniteur invalide » : contrôles numériques, version 1.

Auteur : Claude Opus 5.5, contre-lecteur. Pièce de travail ; aucune donnée d'expérience, aucun tirage.
Accompagne contre-lecture-et-singh-v1.md (même dossier).

Blocs :
  [1] la pente C/A de la borne est toujours >= r* = b/a > rho0 (pas implicite de la garantie 2) ;
  [2] lemme G : borne analytique de la borne sur trajectoire g(N) de la grille de douze taux ;
  [3] borne par réduction (audit au hasard -> observation complète + martingale du tirage),
      comparée à la borne B(n) de la re-dérivation et à l'échelle sqrt(n rho0 (1-rho0) / q) ;
  [4] borne sur trajectoire de Singh (proposition 1 (ii)) à audit complet, à côté de g(n).

Lancer : python calcul_contre_lecture_v1.py > sortie_calcul_contre_lecture_v1.txt
"""
import math

from scipy import stats

RHO0, ALPHA, BETA = 0.10, 0.05, 0.10
BETA1, BETA2 = 0.09, 0.01           # partage du risque : martingale du tirage, nombre d'audits
GRILLE = [1.0 + 4.0 / 2 ** j for j in range(12)]   # multiples de rho0
K = len(GRILLE)
L = math.log(K / ALPHA)


def uab(mult):
    rho = mult * RHO0
    u = math.log(rho / RHO0)
    b = math.log((1 - RHO0) / (1 - rho))
    return u, b, u + b


def phi(q, s):
    return q * s + math.log(1 - q + q * math.exp(-s))


def lambdas(lo=1e-4, hi=50.0, k=1200):
    return [math.exp(math.log(lo) + i * (math.log(hi) - math.log(lo)) / k) for i in range(k + 1)]


# ---------------------------------------------------------------- [1]
def bloc_1():
    print("[1] Pente de la borne de la re-dérivation : C/A - r* >= 0 pour tout taux de la grille et tout lambda avec A > 0")
    pire = math.inf
    for q in (0.01, 0.05, 0.20, 0.50, 0.99):
        for mult in GRILLE:
            u, b, a = uab(mult)
            for lam in lambdas(1e-3, 30.0, 300):
                A = q * a - (phi(q, lam * u) - phi(q, -lam * b)) / lam
                if A <= 0:
                    continue
                C = q * b + phi(q, -lam * b) / lam
                pire = min(pire, C / A - b / a)
    print("    plus petit écart C/A - b/a rencontré : %.3e (doit être >= 0 ; identité : u phi(-lam b) + b phi(lam u) >= 0)" % pire)
    print("    r* - rho0 pour le plus petit taux : %.3e (> 0)" % (uab(min(GRILLE))[1] / uab(min(GRILLE))[2] - RHO0))
    print()


# ---------------------------------------------------------------- [2]
def g_traj(N):
    """Borne sur trajectoire à audit complet : sans annonce, M - rho0 N < min_k [L/a_k + (r*_k - rho0) N]."""
    best = math.inf
    for mult in GRILLE:
        u, b, a = uab(mult)
        best = min(best, L / a + (b / a - RHO0) * N)
    return best


def kappa(eps):
    """Facteur du lemme G : max des deux facteurs (1+eps) et (1+eps)(1-rho0)(1-rho0 eps)/(1-rho0(1+eps))."""
    return (1 + eps) * max(1.0, (1 - RHO0) * (1 - RHO0 * eps) / (1 - RHO0 * (1 + eps)))


def bloc_2():
    print("[2] Lemme G (grille de douze taux) : g(N) <= 1,25 kappa(2 eps*) racine(2 rho0 (1-rho0) L N),")
    print("    eps*(N) = racine(2 L (1-rho0) / (rho0 N)) dans [plus petit écart, 2]. L = log(12/alpha) = %.4f" % L)
    eps_min = min(GRILLE) - 1.0
    n_lo = 2 * L * (1 - RHO0) / (RHO0 * 4.0)
    n_hi = 2 * L * (1 - RHO0) / (RHO0 * eps_min ** 2)
    print("    domaine en N (audits) : [%.1f ; %.3e]" % (n_lo, n_hi))
    pire = 0.0
    N = math.ceil(n_lo)
    while N <= n_hi:
        es = math.sqrt(2 * L * (1 - RHO0) / (RHO0 * N))
        borne = 1.25 * kappa(min(2 * es, 4.0)) * math.sqrt(2 * RHO0 * (1 - RHO0) * L * N)
        exact = g_traj(N)
        pire = max(pire, exact / borne)
        N = math.ceil(N * 1.02) + 1
    print("    plus grand rapport g(N) / borne du lemme sur le domaine : %.4f (doit être <= 1)" % pire)
    for N in (100, 1000, 10000, 100000, 1000000, 10000000):
        print("      N = %8d : g(N) = %9.2f ; g(N) / racine(2 rho0 (1-rho0) L N) = %.3f" %
              (N, g_traj(N), g_traj(N) / math.sqrt(2 * RHO0 * (1 - RHO0) * L * N)))
    print()


# ---------------------------------------------------------------- [3]
def borne_reduction(n, q):
    """Avec probabilité >= 1 - BETA1 - BETA2, pour tout m <= n avant l'annonce :
    Delta_m < [g(N+) + l1/lam + n (rho0 phi1 + (1-rho0) phi0)/lam] / [q - (phi1 - phi0)/lam],
    phi1 = phi(lam (1-rho0)), phi0 = phi(-lam rho0), N+ = quantile 1 - BETA2 de Bin(n, q)."""
    l1 = math.log(1 / BETA1)
    n_plus = float(stats.binom.ppf(1 - BETA2, n, q))
    g = g_traj(n_plus)
    best = (math.inf, None)
    for lam in lambdas(1e-4, 20.0, 1500):
        p1, p0 = phi(q, lam * (1 - RHO0)), phi(q, -lam * RHO0)
        den = q - (p1 - p0) / lam
        if den <= 0:
            continue
        val = (g + l1 / lam + n * (RHO0 * p1 + (1 - RHO0) * p0) / lam) / den
        if val < best[0]:
            best = (val, lam)
    return best[0], n_plus, g


def borne_rederivation(n, q):
    """Théorème du § 3.1 de la re-dérivation (min sur le taux et sur lambda)."""
    ell = math.log(1 / BETA)
    best = math.inf
    for mult in GRILLE:
        u, b, a = uab(mult)
        for lam in lambdas(1e-3, 3.0, 600):
            A = q * a - (phi(q, lam * u) - phi(q, -lam * b)) / lam
            if A <= 0:
                continue
            C = q * b + phi(q, -lam * b) / lam
            best = min(best, (L + ell / lam) / A + n * (C / A - RHO0))
    return best


def bloc_3():
    print("[3] Borne par réduction (beta = %.2f + %.2f) contre la borne B(n) de la re-dérivation (beta = %.2f)" % (BETA1, BETA2, BETA))
    print("    q | n | N+ | g(N+) | réduction | réduction / échelle | B(n) | B(n) / échelle | ordre principal analytique")
    for q in (0.20, 0.05):
        for n in (1000, 4000, 16000, 100000, 1000000, 10000000):
            red, n_plus, g = borne_reduction(n, q)
            bn = borne_rederivation(n, q)
            ech = math.sqrt(n * RHO0 * (1 - RHO0) / q)
            op = math.sqrt(2 * RHO0 * (1 - RHO0) * n / q) * (1.25 * math.sqrt(L) + math.sqrt((1 - q) * math.log(1 / BETA1)))
            print("    %.2f | %8d | %8.0f | %8.1f | %9.1f | %5.2f | %9.1f | %5.2f | %9.1f" %
                  (q, n, n_plus, g, red, red / ech, bn, bn / ech, op))
    print()


# ---------------------------------------------------------------- [4]
def bloc_4():
    print("[4] Audit complet : borne sur trajectoire de Singh, proposition 1 (ii), racine(H (log(H/alpha) + (1-p0)/(4 p0)) / 2) + 1,")
    print("    grille de H taux uniformes, à côté de g(H) + 1 pour la grille de douze taux (même rho0, même alpha)")
    eps = (1 - RHO0) / (4 * RHO0)
    for H in (1000, 4000, 16000, 100000, 1000000):
        s = math.sqrt(H * (math.log(H / ALPHA) + eps) / 2) + 1
        print("      H = %8d : Singh %9.1f ; douze taux %9.1f" % (H, s, g_traj(H) + 1))
    print()


if __name__ == "__main__":
    print("Contre-lecture de la re-dérivation « moniteur invalide » : contrôles numériques, version 1.")
    print("rho0 = %.2f, alpha = %.2f, beta = %.2f ; grille de douze taux rho0 (1 + 4/2^j). Aucun tirage." % (RHO0, ALPHA, BETA))
    print()
    bloc_1()
    bloc_2()
    bloc_3()
    bloc_4()
