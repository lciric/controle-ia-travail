"""Contre-lecture : verifications independantes de la partie tabulaire.
Lancer avec -I. Aucune ecriture hors stdout."""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq, minimize

rng = np.random.default_rng(np.random.SeedSequence(20261124).spawn(1)[0])

def softmax(t):
    z = t - t.max(); e = np.exp(z); return e / e.sum()

# ---------------- Lemme du gradient naturel ----------------
err = 0.0
for _ in range(200):
    n = rng.integers(2, 7); th = rng.normal(size=n); pi = softmax(th)
    Q = rng.normal(size=(n, n)); Q = Q + Q.T; c = rng.normal(size=n)
    V = lambda P: P @ Q @ P + c @ np.log(P)
    G = 2 * Q @ pi + c / pi
    F = np.diag(pi) - np.outer(pi, pi)
    # gradient en theta par differences finies
    h = 1e-6; gth = np.array([(V(softmax(th + h*np.eye(n)[i])) - V(softmax(th - h*np.eye(n)[i]))) / (2*h) for i in range(n)])
    lhs = np.linalg.pinv(F) @ gth
    rhs = G - G.mean()
    err = max(err, np.abs(lhs - rhs).max() / (1 + np.abs(rhs).max()))
print("lemme NPG : erreur relative max", err)

# ---------------- (a) lambda_k discret ----------------
for eta, gam in [(2., .5), (2., 2.), (2., 3.), (2., 3.9)]:
    lam = 0.; L = []
    for k in range(6):
        lam = (1 - gam/eta)*lam + gam/eta; L.append(lam)
    print("lambda_k eta=%g gamma=%g" % (eta, gam), np.round(L, 4))

# ---------------- (c2) flot naturel non regularise, en echelle log ----------------
def a_vec(pi, beta, R):
    Z = pi @ beta; b = (pi*beta) @ R / Z
    return beta*(R - b)/Z, b, Z

def flot_nat(p, beta, dR, T, eta=np.inf, n=20001):
    R = np.array([0, dR, dR])
    def f(t, phi):
        pi = softmax(np.log(p) + phi)
        a, _, _ = a_vec(pi, beta, R)
        return a - (0 if np.isinf(eta) else phi/eta)
    s = solve_ivp(f, [0, T], np.zeros(3), rtol=1e-11, atol=1e-12, method='LSODA', dense_output=True)
    t = np.linspace(0, T, n); ph = s.sol(t)
    return t, ph

worst_rate = np.inf; worst_dom = -np.inf; worst_inv = 0; worst_lim = 0
for _ in range(40):
    p = rng.dirichlet([5, 1, 1])
    if p[0] <= p[2]: continue
    bh = rng.uniform(.3, 1); bf = rng.uniform(.02, bh); bv = rng.uniform(0, bf); beta = np.array([bh, bv, bf]); dR = rng.uniform(.3, 2)
    rho = bf/bh; L = np.log(p[0]/p[2]); T = 3*L/(rho*dR) + 50/(rho*dR)
    t, ph = flot_nat(p, beta, dR, T)
    y = ph[2] - ph[0]
    rate = np.diff(y)/np.diff(t); worst_rate = min(worst_rate, (rate/(rho*dR)).min())
    tdom = t[np.argmax(y > L)]
    worst_dom = max(worst_dom, tdom - L/(rho*dR))
    logpi = np.log(p)[:, None] + ph - np.logaddexp.reduce(np.log(p)[:, None] + ph, axis=0)
    inv = np.abs((logpi[1] - np.log(p[1])) - (bv/bf)*(logpi[2] - np.log(p[2]))).max(); worst_inv = max(worst_inv, inv)
    xs = brentq(lambda x: x + p[1]*(x/p[2])**(bv/bf) - 1, p[2], 1)
    worst_lim = max(worst_lim, abs(np.exp(logpi[2, -1]) - xs))
print("(c2)(i) min taux/(rho dR) :", worst_rate, "(doit etre >= 1)")
print("(c2)(i) max (t_dom - L/(rho dR)) :", worst_dom, "(doit etre <= pas de grille)")
print("(c2)(ii) invariant, ecart max :", worst_inv, "; (iii) limite x*, ecart max :", worst_lim)

# taux pouvant depasser Delta R : le filtre peut accelerer
p = np.array([.4, .3, .3]); beta = np.array([1., 0., .1]); dR = 1.
pi = np.array([.01, .0, .99]); a, b, Z = a_vec(pi, beta, np.array([0, dR, dR]))
print("(c2) taux a_f-a_h en un point a masse surtout furtive :", a[2]-a[0], "> Delta R =", dR)

# flot vanille (gradient ordinaire, ce que (c1) donne en esperance) contre flot naturel
def flot_vanille(p, beta, dR, T):
    R = np.array([0, dR, dR])
    def f(t, th):
        pi = softmax(th); a, _, _ = a_vec(pi, beta, R)
        return pi*a  # F a = pi o a car E_pi a = 0
    s = solve_ivp(f, [0, T], np.log(p), rtol=1e-11, atol=1e-13, method='LSODA')
    return softmax(s.y[:, -1])
p = np.array([.6, .3, .1]); beta = np.array([1., .2, .5]); dR = 1.
t, ph = flot_nat(p, beta, dR, 400.)
pin = softmax(np.log(p) + ph[:, -1]); piv = flot_vanille(p, beta, dR, 4000.)
print("limite flot naturel :", pin, " limite flot vanille :", piv)
print("   invariant pi_v pi_f^(-bv/bf) : naturel", pin[1]*pin[2]**(-.4), "depart", p[1]*p[2]**(-.4), "vanille", piv[1]*piv[2]**(-.4))

# ---------------- Proposition d'amplification a temps egal ----------------
def piA(lam, p, beta, eDR):
    w = p*beta**lam*np.array([1, np.exp(eDR*lam), np.exp(eDR*lam)]); return w/w.sum()
bad = [0, 0, 0]; n = 0
for _ in range(50000):
    p = rng.dirichlet([1, 1, 1]); bh = rng.uniform(.05, 1); bf = rng.uniform(.01, 1)*bh; bv = rng.uniform(0, 1)*bf
    eDR = rng.exponential(4); lam = rng.uniform(1e-3, 1)
    beta = np.array([bh, bv, bf])
    d = piA(lam, p, beta, eDR)[2] - piA(lam, p, np.ones(3), eDR)[2]
    crit = p[1]*(bf**lam - bv**lam)*np.exp(eDR*lam) - p[0]*(bh**lam - bf**lam)
    if abs(d) > 1e-12 and np.sign(d) != np.sign(crit): bad[0] += 1
    if bh > bf:
        T = np.log(p[0]*(bh-bf)/(p[1]*(bf-bv)))
        if eDR*lam >= T and d <= 0: bad[1] += 1
print("amplification (i) desaccords :", bad[0], " (ii) violations :", bad[1])

# (iii) temps courts et (iv) convexite par formule analytique de g''
def gfun(lam, ph, pv, lh, lv, eDR):
    return np.log(pv/ph) + eDR*lam + np.log(-np.expm1(-lv*lam)) - np.log(np.expm1(lh*lam))
def g2(lam, lh, lv):
    h = lambda l: (l*l*np.exp(l*lam)/np.expm1(l*lam)**2)
    return h(lh) - h(lv)
viol = 0
for _ in range(50000):
    lh = rng.exponential(2) + 1e-4; lv = rng.exponential(3) + 1e-4; lam = rng.uniform(1e-3, 5)
    s = g2(lam, lh, lv)
    if (lv > lh and s < -1e-12*abs(s).max()) or (lv < lh and s > 1e-12): viol += 1
print("(iv) signe de g'' (formule analytique) violations :", viol)

# monotonie sous la condition eta dR >= max(lh, (lh+lv)/2)
viol = 0
lams = np.linspace(1e-4, 1, 4001)
for _ in range(5000):
    lh = rng.exponential(2) + 1e-3; lv = rng.exponential(3) + 1e-3
    eDR = max(lh, (lh+lv)/2) * (1 + rng.uniform(0, .1))
    gg = gfun(lams, .5, .2, lh, lv, eDR)
    if (np.diff(gg) < -1e-9).any(): viol += 1
print("(iv) monotonie sous la condition : violations", viol)

# exemple de reentrance (rem:reentrance)
bh, bv, bf = 1., 5e-4, .5; ph, pv = .8, .084; eDR = 3.
lh, lv = np.log(bh/bf), np.log(bf/bv)
lam = np.linspace(1e-7, 1, 2_000_001); gg = gfun(lam, ph, pv, lh, lv, eDR)
i = np.argmin(gg)
zer = [brentq(lambda l: gfun(l, ph, pv, lh, lv, eDR), lam[j], lam[j+1]) for j in np.where(np.sign(gg[1:]) != np.sign(gg[:-1]))[0]]
print("reentrance : g(0+) =", np.log(pv*lv/(ph*lh)), " min g =", gg[i], "en lambda =", lam[i], " g(1) =", gg[-1], " zeros en lambda :", zer)
eta = 1.0
print("   temps (eta=1) des zeros :", [-eta*np.log(1-z) for z in zer])
p3 = np.array([ph, pv, 1-ph-pv]); beta = np.array([bh, bv, bf])
for l in [1e-3, zer[0]/2, (zer[0]+zer[1])/2, 0.9]:
    print("   lambda=%.4g  piA(f)-pino(f) = %.3e" % (l, piA(l, p3, beta, eDR)[2]-piA(l, p3, np.ones(3), eDR)[2]))
# controle de la violation de c1 : chercher le tirage
r1 = np.random.default_rng(0)
_ = r1.normal()  # non utilise : on refait la boucle de c1 a l'identique ci-dessous
