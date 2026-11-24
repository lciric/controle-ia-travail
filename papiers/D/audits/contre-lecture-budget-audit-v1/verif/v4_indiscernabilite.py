# Contre-lecture independante : proposition prop:audit-indist.
import math
import numpy as np
rng = np.random.default_rng(np.random.SeedSequence(20261124_04))

# (a) rho_eff >= rho (1 - delta/tau)_+ et monotonie en tau_A
bad = 0
for _ in range(200000):
    tau = rng.uniform(1e-3, 1); dl = rng.uniform(0, 1); rho = rng.uniform(0, 0.999)
    lo = max(tau - dl, 0); tA = rng.uniform(lo, 1)
    den = rho * tA + (1 - rho) * tau
    eff = rho * tA / den
    if eff < rho * max(1 - dl / tau, 0) - 1e-12: bad += 1
print("(a) rho_eff : violations", bad, "sur 200000")

# (b) d_j <= tau[dR - rho(dR + C_delta)]
bad = 0
for _ in range(200000):
    tau = rng.uniform(1e-3, 1); dl = rng.uniform(0, 1); rho = rng.uniform(0, 1); dR = rng.uniform(0.01, 3); C = rng.uniform(0, 30)
    tA = rng.uniform(max(tau - dl, 0), 1)
    d = (1 - rho) * tau * dR - rho * tA * C
    Cd = C * max(1 - dl / tau, 0)
    if d > tau * (dR - rho * (dR + Cd)) + 1e-12: bad += 1
print("(b) avantage : violations", bad)

# inegalite affichee sur rho_hold^delta : fausse quand le numerateur est negatif
dR, eta, tau, c, C, dl = 1.0, 1.0, 0.5, 1.0, 1.0, 0.25
lhs = (dR - c / (eta * tau)) / (dR + C * (1 - dl / tau)); rhs = (dR - c / (eta * tau)) / ((1 - dl / tau) * (dR + C))
print(f"inegalite de rho_hold^delta (eta tau dR = {eta*tau*dR} <= c = {c}) : gauche {lhs:.4f} <= droite {rhs:.4f} ? {lhs <= rhs}")

# Plan calcule pour une strate (tau0) applique a une autre (tau) : dissuade-t-il ?
def a_(g, e): return 1 - g / e if math.isfinite(e) else 1.0
def G(k, g, e):
    a = a_(g, e); return g * sum(a ** i for i in range(k))
def jit(K, g, e, dRw, Cw, c):
    W = dRw + Cw
    if dRw * G(K, g, e) <= c: return [0.0] * K
    kap = next(k for k in range(K) if dRw * G(k + 1, g, e) > c)
    rk = (dRw * G(kap + 1, g, e) - c) / (g * W); rh = (dRw - (c / e if math.isfinite(e) else 0)) / W
    return [0.0] * kap + [rk] + [rh] * (K - 1 - kap)
def maxx(rho, g, e, tau, tA, dR, C):
    a = a_(g, e); x = 0; m = 0
    for r in rho:
        x = a * x + g * ((1 - r) * tau * dR - r * tA * C); m = max(m, x)
    return m
print("Plan du pire cas pour tau0, applique a la strate tau (tau_A = (tau - delta)_+), meme marge c :")
for (K, g, e, dR, C, c, dl, tau0, tau) in [
        (400, 0.05, math.inf, 1.0, 9.0, 1.0, 0.1, 1.0, 0.1),    # strate rare sous delta
        (400, 0.05, math.inf, 1.0, 9.0, 1.0, 0.1, 1.0, 0.3),    # strate moyenne
        (400, 0.05, 5.0, 1.0, 9.0, 2.0, 0.1, 0.5, 1.0),         # eta fini : la strate frequente echappe-t-elle ?
        (400, 0.05, 5.0, 1.0, 9.0, 2.0, 0.1, 1.0, 0.5)]:
    Cd0 = C * max(1 - dl / tau0, 0)
    rho = jit(K, g, e, tau0 * dR, tau0 * Cd0, c)
    m = maxx(rho, g, e, tau, max(tau - dl, 0), dR, C)
    print(f"   eta={e} tau0={tau0} -> tau={tau}: max x_k = {m:.3f} contre c = {c}  -> {'dissuade' if m <= c + 1e-9 else 'NE DISSUADE PAS'}")

# Taux de maintien en fonction de tau : maximum interieur possible a eta fini
for (eta, c, C, dl) in [(5.0, 2.0, 9.0, 0.1), (5.0, 1.0, 20.0, 0.05), (math.inf, 1.0, 9.0, 0.1)]:
    taus = np.linspace(0.01, 1, 991)
    def hold(t):
        num = 1.0 - (c / (eta * t) if math.isfinite(eta) else 0.0)
        return num / (1.0 + C * max(1 - dl / t, 0))
    h = np.array([hold(t) for t in taus]); i = int(np.argmax(h))
    print(f"   eta={eta} c={c} C={C} delta={dl}: rho_hold max = {h[i]:.3f} en tau = {taus[i]:.3f} ; a tau=1 : {hold(1.0):.3f}")
