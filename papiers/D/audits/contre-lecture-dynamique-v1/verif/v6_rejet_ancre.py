"""Contre-lecture : proposition du gradient avec rejet ancre par la divergence de Kullback-Leibler (prop:discard-kl).
Reduction aux trois strates (phi constant sur les strates). Lancer avec -I."""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import minimize, brentq

rng = np.random.default_rng(np.random.SeedSequence(20261124).spawn(6)[5])
def softmax(t): z = t - t.max(); e = np.exp(z); return e/e.sum()
def a_vec(pi, beta, R):
    Z = pi @ beta; b = (pi*beta) @ R / Z; return beta*(R-b)/Z, b, Z

def run(p, beta, dR, eta, T, phi0=None, n=4001):
    R = np.array([0, dR, dR]); lp = np.log(p)
    f = lambda t, phi: a_vec(softmax(lp + phi), beta, R)[0] - phi/eta
    s = solve_ivp(f, [0, T], np.zeros(3) if phi0 is None else phi0, rtol=1e-11, atol=1e-12, method='LSODA', dense_output=True)
    t = np.linspace(0, T, n); return t, s.sol(t)

bad = {"i": 0, "iii": 0, "iv": 0}; used_iv = 0
for _ in range(300):
    p = rng.dirichlet([4, 1, 1]); bh = rng.uniform(.3, 1); bf = rng.uniform(.01, 1)*bh; bv = rng.uniform(0, 1)*bf
    beta = np.array([bh, bv, bf]); dR = rng.uniform(.2, 2); eta = rng.exponential(10)+.1
    rho = bf/bh; c = (p[1]+p[2])/p[0]
    t, ph = run(p, beta, dR, eta, 15*eta)
    pis = np.array([softmax(np.log(p)+ph[:, k]) for k in range(len(t))])
    Z = pis @ beta
    if (Z < bf*p[2]/(p[2]+p[1]) - 1e-12).any(): bad["i"] += 1
    r = pis/p
    if (r[:, 0] > r[:, 1]*(1+1e-9)).any() or (r[:, 1] > r[:, 2]*(1+1e-9)).any(): bad["i"] += 1
    y = ph[2]-ph[0]
    if (y < eta*(1-np.exp(-t/eta))*rho*dR - 1e-9).any(): bad["iii"] += 1
    # (iv) : plus petit ybar > 0 avec eta rho dR (1+c e^ybar)^2 <= ybar
    G = lambda yb: eta*rho*dR*(1+c*np.exp(yb))**2 - yb
    ys = np.linspace(1e-6, 60, 60001); ok = np.where(G(ys) <= 0)[0]
    if len(ok):
        used_iv += 1; yb = ys[ok[0]]
        if y.max() >= yb: bad["iv"] += 1
print("prop:discard-kl : violations", bad, "; cas ou (iv) s'applique :", used_iv)

# ----- instance (v) -----
for bv in [1e-3, .05, .099]:
    p = np.array([1-2e-4, 1e-4, 1e-4]); beta = np.array([1, bv, .1]); dR = 1.; eta = 20.
    L = np.log(p[0]/p[2]); c = (p[1]+p[2])/p[0]
    t, ph = run(p, beta, dR, eta, 3000.)
    y = ph[2]-ph[0]
    # maximum global de V_acc sur le simplexe des strates (KL minimal a masses de strates donnees)
    def mV(z):
        pi = softmax(z); a, b, Z = a_vec(pi, beta, np.array([0, dR, dR]))
        return -(b - (pi*np.log(pi/p)).sum()/eta)
    best = min([minimize(mV, z0, method='Nelder-Mead', options=dict(xatol=1e-12, fatol=1e-14, maxiter=40000)) for z0 in [np.zeros(3), [0, 0, 15], [0, 15, 15], [0, 15, 0], [-30, 0, 0]]], key=lambda r: r.fun)
    pistar = softmax(best.x)
    pilim = softmax(np.log(p)+ph[:, -1])
    print("beta_v=%g : max y=%.4f (borne 3), log(pi_f/pi_h) final=%.3f ; limite=%s ; eta*V(limite)=%.4f ; maximiseur=%s eta*V=%.4f" %
          (bv, y.max(), y[-1]-L, np.array2string(pilim, precision=4), -mV(np.log(pilim))*eta, np.array2string(pistar, precision=4), -best.fun*eta))
    # equilibres de l'equation d'auto-coherence pi propto p exp(eta a(pi)) : balayage sur la masse honnete
    R = np.array([0, dR, dR])
    def resid(lh):  # parametre : log pi_h ; on resout les deux autres par point fixe
        pass

# ----- seuil reel de dominance contre les deux bornes -----
p = np.array([1-2e-4, 1e-4, 1e-4]); beta = np.array([1, .05, .1]); L = np.log(p[0]/p[2]); c = (p[1]+p[2])/p[0]
print("seuil de dominance garanti eta rho dR > L =", L)
for edr in [20, 40, 50, 60, 70, 80, 92.2, 100]:
    eta = 20.; dR = edr/eta
    t, ph = run(p, beta, dR, eta, 3000.)
    y = ph[2]-ph[0]
    G = lambda yb: eta*.1*dR*(1+c*np.exp(yb))**2 - yb
    ys = np.linspace(1e-6, 30, 300001); ok = np.where(G(ys) <= 0)[0]
    print("   eta dR=%g (eta rho dR=%g) : max y=%.3f, domine=%s, piege(iv) ybar=%s" % (edr, .1*edr, y.max(), y.max() > L, ys[ok[0]] if len(ok) else None))
