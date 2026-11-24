"""Contre-lecture : verifications independantes du modele a deux canaux (operateur B et A).
Lancer avec -I."""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq, minimize

rng = np.random.default_rng(np.random.SeedSequence(20261124).spawn(2)[1])
def sig(x): return 0.5*(1+np.tanh(np.asarray(x)/2))
def logit(p): return np.log(p) - np.log1p(-p)

def coeffs(bh, bv, bf, dR, C):
    return bv*dR - (bh-bv)*C, (bf-bv)*(dR+C)

def flow(u0, w0, eta, A0, D, kap, x0=None, T=None, dense=False):
    f = lambda t, x: [A0 + D*sig(x[1]) - (x[0]-u0)/eta, D*sig(x[0]) - kap - (x[1]-w0)/eta]
    x0 = [u0, w0] if x0 is None else x0
    return solve_ivp(f, [0, T or 80*eta], x0, rtol=1e-10, atol=1e-12, method='LSODA', dense_output=dense)

def fixed_points(u0, w0, eta, A0, D, kap):
    Phi = lambda w: w0 + eta*(D*sig(u0 + eta*(A0 + D*sig(w))) - kap)
    lo, hi = w0 - eta*kap - 1, w0 + eta*(D-kap) + 1
    ws = np.linspace(lo, hi, 400001); h = Phi(ws) - ws
    idx = np.where(np.sign(h[1:]) != np.sign(h[:-1]))[0]
    return [brentq(lambda w: Phi(w)-w, ws[i], ws[i+1], xtol=1e-14) for i in idx]

# ---------- (b2)-(b3) : unimodalite de Phi' et nombre de points fixes ----------
mx = 0; bad = 0
for _ in range(3000):
    u0 = rng.normal(0, 4); w0 = rng.normal(0, 4); eta = rng.exponential(8)+.1; A0 = rng.normal(0, 2); D = rng.exponential(2)+.01; kap = rng.exponential(1)
    fp = fixed_points(u0, w0, eta, A0, D, kap); mx = max(mx, len(fp))
    for w in fp:
        u = u0 + eta*(A0 + D*sig(w)); Fp = eta**2*D**2*sig(u)*(1-sig(u))*sig(w)*(1-sig(w))
        J = np.array([[-1/eta, D*sig(w)*(1-sig(w))], [D*sig(u)*(1-sig(u)), -1/eta]])
        ev = np.sort(np.linalg.eigvals(J).real); th = np.sort([-(1-np.sqrt(Fp))/eta, -(1+np.sqrt(Fp))/eta])
        if np.abs(ev-th).max() > 1e-9*(1+np.abs(th).max()): bad += 1
    if len(fp) == 3:
        Fps = []
        for w in fp:
            u = u0 + eta*(A0 + D*sig(w)); Fps.append(eta**2*D**2*sig(u)*(1-sig(u))*sig(w)*(1-sig(w)))
        if not (Fps[0] < 1 < Fps[1] and Fps[2] < 1): bad += 1
print("(b2) max points fixes :", mx, " (b3) desaccords valeurs propres/alternance :", bad)

# ---------- (b4) contraction ----------
bad = 0
for _ in range(300):
    eta = rng.uniform(.1, 10); D = rng.uniform(0, 4/eta)*.999; u0, w0 = rng.normal(0, 3, 2); A0 = rng.normal(); kap = rng.exponential(.5)
    fp = fixed_points(u0, w0, eta, A0, D, kap)
    if len(fp) != 1: bad += 1; continue
    xs = np.array([u0 + eta*(A0 + D*sig(fp[0])), fp[0]])
    x0 = xs + rng.normal(0, 5, 2)
    s = flow(u0, w0, eta, A0, D, kap, x0=x0, T=20*eta, dense=True)
    t = np.linspace(0, 20*eta, 400); X = s.sol(t)
    lhs = np.abs(X - xs[:, None]).max(0); rhs = np.exp(-(1/eta - D/4)*t)*np.abs(x0-xs).max()
    if (lhs > rhs*(1+1e-6) + 1e-8).any(): bad += 1
print("(b4) violations de l'estimation de contraction :", bad)

# ---------- Proposition de bistabilite : conditions => trois equilibres ----------
used = 0; bad = 0
for _ in range(4000):
    u0, w0 = rng.normal(0, 3, 2); eta = rng.uniform(1, 60); D = rng.exponential(1.5)+.05; kap = rng.uniform(0, D); A0 = rng.normal(0, 1.5)
    cL = sig(u0 + eta*(A0 + D*sig(w0 - eta*kap/2))) < kap/(2*D)
    cH = sig(u0 + eta*(A0 + D*sig(w0 + eta*(D-kap)/2))) > (D+kap)/(2*D)
    if cL and cH:
        used += 1; fp = fixed_points(u0, w0, eta, A0, D, kap)
        if len(fp) != 3 or not (fp[0] < w0-eta*kap/2 < fp[1] < w0+eta*(D-kap)/2 < fp[2]): bad += 1
print("bistabilite : cas couverts", used, " violations", bad)

# ---------- Non-atteignabilite : conditions => x_* <= x0 et maximiseur global > x_* ----------
used = 0; bad = 0
for _ in range(1500):
    q0, s0 = rng.uniform(.005, .5, 2); eta = rng.uniform(5, 60); A0 = -rng.exponential(1); D = rng.exponential(2)+.1; kap = rng.uniform(0, 1)
    if not (A0 + D*s0 <= 0 and D*q0 <= kap and A0 + D - kap > np.log(1/(q0*s0))/eta): continue
    used += 1; u0, w0 = logit(q0), logit(s0)
    s = flow(u0, w0, eta, A0, D, kap); xe = s.y[:, -1]
    kl = lambda a, b: a*np.log(a/b) + (1-a)*np.log((1-a)/(1-b))
    Jf = lambda x: -(sig(x[0])*(A0 + D*sig(x[1])) - kap*sig(x[1]) - (kl(sig(x[0]), q0) + kl(sig(x[1]), s0))/eta)
    best = min([minimize(Jf, x, method='Nelder-Mead', options=dict(xatol=1e-10, fatol=1e-14, maxiter=20000)) for x in [[8, 8], [15, 15], [u0, w0], [3, 3]]], key=lambda r: r.fun)
    if not (xe[0] <= u0+1e-8 and xe[1] <= w0+1e-8 and best.x[0] > xe[0] and best.x[1] > xe[1] and -best.fun > 0): bad += 1
print("non-atteignabilite : cas couverts", used, " violations", bad)

# ---------- Regeneration des trois affirmations numeriques ----------
bh, bf, bv, dR, kap, q0, s0, eta = 1., 1., 0., 1., .1, .01, .01, 20.
u0, w0 = logit(q0), logit(s0)
kl = lambda a, b: a*np.log(a/b) + (1-a)*np.log1p(-a) - (1-a)*np.log1p(-b) if a < 1 else np.log(1/b)
for C in [1.0]:
    A0, D = coeffs(bh, bv, bf, dR, C)
    for w in fixed_points(u0, w0, eta, A0, D, kap):
        u = u0 + eta*(A0 + D*sig(w)); q, s = sig(u), sig(w)
        # J avec kl stable : 1-q calcule par sig(-u)
        def klx(z, p0):
            pz, mz = sig(z), sig(-z)
            return pz*(np.log(pz) - np.log(p0)) + mz*(np.log(mz) - np.log1p(-p0))
        J = q*(A0 + D*s) - kap*s - (klx(u, q0) + klx(w, s0))/eta
        print("equilibre C=1 : q=%.4g  1-q=%.3g  s=%.4g  1-s=%.3g  J=%.6g" % (q, sig(-u), s, sig(-w), J))
A0, D = coeffs(bh, bv, bf, dR, 100.)
s = flow(u0, w0, eta, A0, D, kap, T=4000, dense=True)
t = np.linspace(0, 50, 2_000_001); W = s.sol(t)[1]
print("C=100 : sup_t s(t) =", sig(W.max()), "atteint en t =", t[W.argmax()], " C_high =", kap/(q0*(bf-bv)) - dR)
for C in [9, 9.5, 10, 20, 50, 100, 1000]:
    A0, D = coeffs(bh, bv, bf, dR, C); s = flow(u0, w0, eta, A0, D, kap, T=2000, dense=True)
    W = s.sol(np.linspace(0, 60, 600001))[1]
    print("   C=%g  sup s = %.6f   limite (q,s) = (%.3g, %.4g)" % (C, sig(W.max()), sig(s.y[0, -1]), sig(s.y[1, -1])))

# ---------- Fenetre de penalite : certificat (ii) au-dela de C_high dans l'instance ----------
for C in [10, 50, 100]:
    A0, D = coeffs(bh, bv, bf, dR, C); wb = w0 + eta*max(D*q0 - kap, 0)
    print("   certificat (ii) C=%g : A0+D sig(wbar) = %.4g (<=0 requis), borne s <= %.5f" % (C, A0 + D*sig(wb), sig(wb)))

# ---------- Operateur A a deux canaux ----------
bad = 0; used = 0
for _ in range(2000):
    bh = 1.; bf = rng.uniform(.05, 1); bv = bf*rng.uniform(.02, 1); lv = np.log(bf/bv); eta = rng.exponential(10)+.1
    dR = 1.; kap = rng.exponential(.3); q0, s0 = rng.uniform(.01, .9, 2); u0, w0 = logit(q0), logit(s0)
    A0 = dR - np.log(bh/bv)/eta; D = lv/eta
    fp = fixed_points(u0, w0, eta, A0, D, kap)
    for w in fp:
        u = u0 + eta*(A0 + D*sig(w))
        if not (w <= w0 + lv + 1e-9 and u >= u0 + eta*dR - np.log(bh/bv) - 1e-9): bad += 1
    if lv < 4 and len(fp) != 1: bad += 1
    cond = (eta*dR <= np.log(bh/bv) - s0*lv) and (q0*lv <= eta*kap)
    s = flow(u0, w0, eta, A0, D, kap, T=30*eta)
    ok = (s.y[0].max() <= u0 + 1e-9) and (s.y[1].max() <= w0 + 1e-9)
    if cond != ok: bad += 1
    used += 1
print("operateur A deux canaux : tirages", used, " violations", bad)
# lv >= 4 : bistabilite possible sous A ?
cnt = 0
for _ in range(3000):
    bv = 1e-3; bf = rng.uniform(.06, 1); lv = np.log(bf/bv); eta = rng.exponential(20)+.1
    u0, w0 = rng.normal(0, 3, 2); kap = rng.exponential(.3)
    fp = fixed_points(u0, w0, eta, 1 - np.log(1/bv)/eta, lv/eta, kap)
    cnt += len(fp) == 3
print("operateur A, beta_f/beta_v >= e^4 (ici jusqu'a 1000) : cas a trois equilibres", cnt, "sur 3000")
