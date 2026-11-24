# Contre-lecture independante : theoreme de mise en oeuvre aleatoire (thm:audit-random).
# Calculs exacts (lois binomiales) ; aucune simulation de la garantie de seuil (preenregistree ailleurs).
import math
import numpy as np
from scipy.stats import binom

rng = np.random.default_rng(np.random.SeedSequence(20261124_03))

def amul(g, e): return 1 - g / e if math.isfinite(e) else 1.0
def Gk(k, g, e):
    a = amul(g, e); return g * sum(a ** i for i in range(k))
def eps_of(Lam, rbar, g, e, dR, C, n, K):
    a = amul(g, e); Gam = sum(a ** (2 * i) for i in range(K))
    return g * (dR + C) * (math.sqrt(2 * rbar * Gam * Lam / n) + 2 * Lam / (3 * n)), Gam

# 1. Inversion de Bernstein : t = sqrt(2 v L) + 2 b L / 3 donne t^2/(2v + 2bt/3) >= L
worst = 1e9
for _ in range(100000):
    v = 10 ** rng.uniform(-6, 3); b = 10 ** rng.uniform(-4, 1); L = 10 ** rng.uniform(-2, 2)
    t = math.sqrt(2 * v * L) + 2 * b * L / 3
    worst = min(worst, t * t / (2 * v + 2 * b * t / 3) / L)
print("1. Bernstein : min de exposant/Lambda pour t de l'enonce =", round(worst, 6), "(>= 1 requis)")

# 2. Cas a = 0 (gamma = eta) : l'ecart au pas k ne depend que du pas k-1 -> loi binomiale exacte
print("2. Ecart unilateral exact, gamma = eta, un pas (Gamma_K = 1) :")
for (n, rho, dR, C, Lam) in [(50, 0.1, 1, 9, math.log(40)), (200, 0.3, 1, 2, math.log(400)), (1000, 0.05, 1, 19, math.log(2000)), (20, 0.5, 1, 1, math.log(20))]:
    g = e = 0.3; W = dR + C; rbar = rho
    eps, _ = eps_of(Lam, rbar, g, e, dR, C, n, 1)
    # hat l - l = -g W (hat rho - rho) ; queue superieure : hat rho < rho - eps/(gW)
    thr = eps / (g * W)
    p_up = binom.cdf(math.ceil(n * (rho - thr)) - 1, n, rho)  # P(hat rho < rho - thr)
    p_dn = binom.sf(math.floor(n * (rho + thr)), n, rho)       # P(hat rho > rho + thr)
    print(f"   n={n} rho={rho}: P(ecart>+eps)={p_up:.2e}  P(ecart<-eps)={p_dn:.2e}  e^-Lambda={math.exp(-Lam):.2e}")

# 3. Queue du nombre d'audits (b), exacte pour le plan juste a temps (deux binomiales)
print("3. (b) queue exacte du nombre d'audits du plan juste a temps :")
for (K, n, g, e, dR, C, c, Lp) in [(200, 200, 0.1, 2.0, 1, 9, 1.5, math.log(40)), (100, 1000, 0.2, 1.0, 1, 4, 0.5, math.log(20)), (50, 30, 0.05, math.inf, 1, 3, 0.2, math.log(1000))]:
    W = dR + C
    kap = next(k for k in range(K) if dR * Gk(k + 1, g, e) > c)
    rk = (dR * Gk(kap + 1, g, e) - c) / (g * W); rh = (dR - (c / e if math.isfinite(e) else 0)) / W
    Bm = n * (rk + (K - 1 - kap) * rh)
    p1 = binom.pmf(np.arange(n + 1), n, rk); m2 = n * (K - 1 - kap); p2 = binom.pmf(np.arange(m2 + 1), m2, rh)
    pN = np.convolve(p1, p2); thr = Bm + math.sqrt(2 * Bm * Lp) + 2 * Lp / 3
    print(f"   K={K} n={n}: P(N > B + ...) = {pN[int(math.floor(thr)) + 1:].sum():.2e}  e^-Lambda' = {math.exp(-Lp):.2e}")

# 4. Inflation (eq:audit-inflation) et ses deux formes explicites ; Gamma_K <= min(K, eta/gamma)
viol = {"infl": 0, "forme_inf": 0, "forme_fin": 0, "Gamma": 0}; tot = 0
def Bunif(K, g, e, dR, C, c):
    W = dR + C; ie = 1 / e if math.isfinite(e) else 0
    xb = [min(c, dR * Gk(k, g, e)) for k in range(K + 1)]
    return (K * g * dR - g * ie * sum(xb[1:K]) - xb[K]) / (g * W)
for _ in range(3000):
    K = int(rng.integers(1, 300)); g = float(rng.uniform(0.01, 1)); mode = int(rng.integers(0, 3))
    e = g if mode == 0 else (math.inf if mode == 1 else g * float(rng.uniform(1.01, 80)))
    dR = float(rng.uniform(0.1, 2)); C = float(rng.uniform(0, 30)); c = float(rng.uniform(0, 5))
    n = int(rng.integers(1, 5000)); delta = float(rng.uniform(0.001, 0.3))
    Lam = math.log(2 * K / delta); rbar = dR / (dR + C)
    eps, Gam = eps_of(Lam, rbar, g, e, dR, C, n, K)
    if Gam > min(K, (e / g) if math.isfinite(e) else K) + 1e-9: viol["Gamma"] += 1
    if eps > c: continue
    tot += 1; W = dR + C
    lhs = n * (Bunif(K, g, e, dR, C, c - eps) - Bunif(K, g, e, dR, C, c))
    infl = n * eps / W * (((K - 1) / e if math.isfinite(e) else 0) + 1 / g)
    if lhs > infl * (1 + 1e-9) + 1e-9: viol["infl"] += 1
    T = n * K
    if not math.isfinite(e):
        if infl > (math.sqrt(2 * rbar * T * Lam) + 2 * Lam / 3) * (1 + 1e-9): viol["forme_inf"] += 1
    else:
        f = (1 + e / (g * K)) * (T * math.sqrt(2 * g * rbar * Lam / (e * n)) + 2 * g * K * Lam / (3 * e))
        if infl > f * (1 + 1e-9): viol["forme_fin"] += 1
print("4. inflation :", tot, "cas admissibles ; violations", viol)

# 5. Domination trajectoire par trajectoire (prop:audit-indist appliquee au theoreme aleatoire) :
#    meme tirage d'audits, tau_A plus grand => log-cote realisee plus basse a chaque pas.
K, n, g, e, tau, dl, dR, C = 100, 50, 0.1, 2.0, 0.6, 0.1, 1.0, 9.0
a = amul(g, e); A = rng.binomial(n, 0.12, size=(2000, K)) / n
def path(tauA):
    x = np.zeros(2000); mx = np.full(2000, -np.inf)
    for k in range(K):
        x = a * x + g * ((1 - A[:, k]) * tau * dR - A[:, k] * tauA * C); mx = np.maximum(mx, x)
    return mx
print("5. domination trajectorielle (pire cas tau_A = tau - delta contre tau_A = 0.9) :", bool(np.all(path(0.9) <= path(tau - dl) + 1e-12)))
