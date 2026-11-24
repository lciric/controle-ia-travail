# Contre-lecture independante : theoreme de dissuasion (thm:audit-deterrence) et corollaire.
# Implementation ecrite depuis la derivation du contre-lecteur, pas recopiee du brouillon.
import math, sys
import numpy as np
from scipy.optimize import linprog

rng = np.random.default_rng(np.random.SeedSequence(20261124_01))

def amul(gam, eta):
    return 1.0 - gam / eta if math.isfinite(eta) else 1.0

def Gk(k, gam, eta):
    a = amul(gam, eta)
    return gam * sum(a ** i for i in range(k))

def xs_of(rho, gam, eta, dR, C):
    a = amul(gam, eta); W = dR + C; x = 0.0; out = [0.0]
    for r in rho:
        x = a * x + gam * dR - gam * W * r; out.append(x)
    return out

def lp(K, gam, eta, dR, C, c, uniform):
    a = amul(gam, eta); W = dR + C
    A = []; b = []
    for k in (range(1, K + 1) if uniform else [K]):
        row = np.zeros(K)
        for j in range(k):
            row[j] = -gam * W * a ** (k - 1 - j)
        A.append(row); b.append(c - dR * Gk(k, gam, eta) + (1e-8 if (C == 0 and c == 0) else 0.0))  # tolerance seulement pour C = c = 0
    r = linprog(np.ones(K), A_ub=np.array(A), b_ub=np.array(b), bounds=[(0, 1)] * K, method="highs")
    return r

def jit(K, gam, eta, dR, C, c):
    W = dR + C
    if dR * Gk(K, gam, eta) <= c:
        return [0.0] * K
    kap = next(k for k in range(K) if dR * Gk(k + 1, gam, eta) > c)
    rk = (dR * Gk(kap + 1, gam, eta) - c) / (gam * W)
    rh = (dR - (c / eta if math.isfinite(eta) else 0.0)) / W
    return [0.0] * kap + [rk] + [rh] * (K - 1 - kap)

def Bfin_closed(K, gam, eta, dR, C, c):
    W = dR + C; a = amul(gam, eta); D = dR * Gk(K, gam, eta) - c
    if D <= 0: return 0.0
    if gam == eta: return D / (gam * W)
    m = max(mp for mp in range(K + 1) if W * Gk(mp, gam, eta) <= D * (1 + 1e-14))
    return m + (D - W * Gk(m, gam, eta)) / (gam * W * a ** m)

def Bunif_identity(K, gam, eta, dR, C, c):
    W = dR + C; ie = (1 / eta) if math.isfinite(eta) else 0.0
    xb = [min(c, dR * Gk(k, gam, eta)) for k in range(K + 1)]
    return (K * gam * dR - gam * ie * sum(xb[1:K]) - xb[K]) / (gam * W)

def draw():
    K = int(rng.integers(1, 61)); gam = float(rng.uniform(0.01, 1.5))
    mode = int(rng.integers(0, 4))
    eta = gam if mode == 0 else (math.inf if mode == 1 else gam * float(rng.uniform(1.0001, 50)))
    dR = float(rng.uniform(0.05, 3))
    C = float(rng.choice([0.0, rng.uniform(0, 30)])); c = float(rng.choice([0.0, rng.uniform(0, 6)]))
    return K, gam, eta, dR, C, c

worst = {"unif": 0, "fin": 0, "ident": 0, "uniq": 0, "envelope": 0}
viol = {"rates": 0, "fin_bound": 0, "m_floor": 0, "cor_a": 0, "cor_b": 0, "rem3": 0}
N = 4000
for t in range(N):
    K, gam, eta, dR, C, c = draw()
    W = dR + C
    ru = lp(K, gam, eta, dR, C, c, True); rf = lp(K, gam, eta, dR, C, c, False)
    assert ru.status == 0 and rf.status == 0, (K, gam, eta, dR, C, c, ru.status, rf.status)
    rho = jit(K, gam, eta, dR, C, c)
    xs = xs_of(rho, gam, eta, dR, C)
    # faisabilite et enveloppe x_k = min(c, dR G_k)
    env = max(abs(xs[k] - min(c, dR * Gk(k, gam, eta))) for k in range(K + 1))
    worst["envelope"] = max(worst["envelope"], env)
    Bj = sum(rho)
    if not (C == 0 and c == 0): worst["unif"] = max(worst["unif"], abs(ru.fun - Bj))
    worst["ident"] = max(worst["ident"], abs(Bunif_identity(K, gam, eta, dR, C, c) - Bj))
    if C == 0 and c == 0:  # cas degenere : la solution exacte est rho = 1 partout (si a > 0)
        worst["fin"] = max(worst["fin"], abs(Bfin_closed(K, gam, eta, dR, C, c) - (K if gam < eta else 1.0)))
    else:
        worst["fin"] = max(worst["fin"], abs(rf.fun - Bfin_closed(K, gam, eta, dR, C, c)))
    if math.isfinite(eta) and not (C == 0 and c == 0):  # unicite annoncee pour eta fini
        worst["uniq"] = max(worst["uniq"], float(np.max(np.abs(np.array(ru.x) - np.array(rho)))))
    if max(rho) > dR / W + 1e-12 or min(rho) < -1e-15: viol["rates"] += 1
    D = dR * Gk(K, gam, eta) - c
    if math.isfinite(eta) and gam < eta and D > 0 and (C > 0 or c > 0):  # C = c = 0 : m = K, perte de precision flottante
        a = amul(gam, eta)
        m = max(mp for mp in range(K + 1) if W * Gk(mp, gam, eta) <= D)
        if m != math.floor(math.log(1 - D / (eta * W)) / math.log(a)): viol["m_floor"] += 1
        if eta * C + c > 0:
            bd = 1 + (eta / gam) * math.log(eta * W / (eta * C + c))
            if Bfin_closed(K, gam, eta, dR, C, c) > bd + 1e-9: viol["fin_bound"] += 1
    # corollaire (a), (b)
    ie = (1 / eta) if math.isfinite(eta) else 0.0
    if eta * dR > c if math.isfinite(eta) else True:
        kap = next((k for k in range(10 ** 6) if dR * Gk(k + 1, gam, eta) > c), None)
        if K > kap:
            dRp = dR - c * ie
            lo = dRp / W * (1 - (kap + 1) / K); hi = dRp / W * (1 - kap / K)
            if not (lo < Bj / K + 1e-12 and Bj / K <= hi + 1e-12): viol["cor_a"] += 1
    if not math.isfinite(eta):
        val = max(K * gam * dR - c, 0) / (gam * W)
        if abs(val - Bj) > 1e-8 or abs(val - Bfin_closed(K, gam, eta, dR, C, c)) > 1e-8: viol["cor_b"] += 1
    # remarque (3) : plan calcule avec dR_haut >= dR et c_bas <= c reste faisable
    dRu = dR * float(rng.uniform(1, 2)); cl = c * float(rng.uniform(0, 1))
    rho_u = jit(K, gam, eta, dRu, C, cl)
    if max(xs_of(rho_u, gam, eta, dR, C)) > c + 1e-9: viol["rem3"] += 1

print("dissuasion :", N, "instances ; ecarts max", {k: f"{v:.2e}" for k, v in worst.items()})
print("violations :", viol)

# Coherence avec le modele statique (operateur B, beta_f = 1 - rho, beta_h = 1) :
# taux constant rho -> limite l_inf = -L + eta[(1-rho)dR - rho C] = log-cote statique.
for (gam, eta, dR, C, L, rho) in [(0.1, 3.0, 1.0, 2.5, math.log(85), 0.2), (0.05, 10.0, 0.6, 4.0, 3.0, 0.07)]:
    a = 1 - gam / eta; x = 0.0
    for _ in range(20000): x = a * x + gam * (dR - (dR + C) * rho)
    static = math.log(1 / math.exp(L)) + eta * ((1 - rho) * dR - (1 - (1 - rho)) * C)
    print("coherence statique (dynamique limite, statique)", -L + x, static)
# rho_hold (eta infini, c=0) = dR/W = seuil de C*_R3 a eps_trap=0, delta=0, tau_min=1 ;
# avec delta : rho > tau dR/(tau dR + (tau-delta) C) equivaut a C > C*_R3.
for (dR, C, tau, dl, rho) in [(1.0, 9.0, 0.6, 0.1, 0.13), (1.0, 9.0, 0.6, 0.1, 0.12), (0.5, 3.0, 1.0, 0.0, 0.15)]:
    CR3 = (1 - rho) * tau / (rho * (tau - dl)) * dR
    hold = dR / (dR + C * (1 - dl / tau))
    print("R3 :", "C > C*_R3" if C > CR3 else "C <= C*_R3", "| rho > rho_hold^delta(eta=inf,c=0)" if rho > hold else "| rho <= rho_hold")

# Corollaire (c) : seuil de penalite exact par bissection contre les deux bornes
viol_c = 0; Ntc = 0
for t in range(400):
    K, gam, eta, dR, _, c = draw()
    if not (math.isfinite(eta) and eta * dR > c) and math.isfinite(eta): continue
    kap = next(k for k in range(10 ** 6) if dR * Gk(k + 1, gam, eta) > c)
    if K <= kap: continue
    n = int(rng.integers(1, 50)); T = n * K
    dRp = dR - (c / eta if math.isfinite(eta) else 0)
    B = float(rng.uniform(0.05, 1)) * T * dRp / dR
    f = lambda CC: n * sum(jit(K, gam, eta, dR, CC, c)) - B
    lo, hi = 0.0, 1e7
    if f(lo) <= 0: Cmin = 0.0
    else:
        for _ in range(200):
            mid = (lo + hi) / 2
            (hi := mid) if f(mid) <= 0 else (lo := mid)
        Cmin = hi
    suff = dRp * (T - n * kap) / B - dR; nec = dRp * (T - n * (kap + 1)) / B - dR
    Ntc += 1
    if not (nec <= Cmin + 1e-6 and Cmin <= max(suff, 0) + 1e-6): viol_c += 1
print("corollaire (c) :", Ntc, "cas, violations", viol_c)
