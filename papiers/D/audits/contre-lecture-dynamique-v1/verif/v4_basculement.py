"""Contre-lecture : peut-on, en augmentant la penalite C, faire passer le modele pre-entraine
du bassin honnete (q petit) au bassin triche obscurcie (q et s proches de 1) ?
c4 cherche cela sur 3000 tirages et une grille de 7 valeurs de C ; on cible ici le voisinage des fenetres.
Lancer avec -I."""
import numpy as np
from scipy.integrate import solve_ivp

def sig(x): return 0.5*(1+np.tanh(np.asarray(x)/2))
def logit(p): return np.log(p) - np.log1p(-p)

def limite(q0, s0, bh, bv, bf, dR, C, kap, eta):
    A0 = bv*dR - (bh-bv)*C; D = (bf-bv)*(dR+C); u0, w0 = logit(q0), logit(s0)
    f = lambda t, x: [A0 + D*sig(x[1]) - (x[0]-u0)/eta, D*sig(x[0]) - kap - (x[1]-w0)/eta]
    s = solve_ivp(f, [0, 200*eta], [u0, w0], rtol=1e-9, atol=1e-11, method='LSODA')
    return sig(s.y[0, -1]), sig(s.y[1, -1])

# 1) exemple construit a la main : beta_f = beta_h = 1, beta_v = 0, Delta R = 1
q0, s0, kap, eta = .3, .3, .45, 20.
b0 = s0; Clow = b0/(1-b0); Chigh = kap/q0 - 1
print("exemple construit : C_low=%.4f C_high=%.4f" % (Clow, Chigh))
for C in [0.3, 0.45, 0.5, 0.55, 0.6, 0.7, 0.8, 1.0, 1.5, 2, 3, 5]:
    q, s = limite(q0, s0, 1, 0, 1, 1, C, kap, eta)
    print("   C=%5.2f  limite q=%.4f s=%.4f" % (C, q, s))

# 2) recherche aleatoire sur grille fine de C autour des fenetres
rng = np.random.default_rng(np.random.SeedSequence(20261124).spawn(3)[2])
found = []
for it in range(1500):
    q0 = rng.uniform(.01, .6); s0 = rng.uniform(.01, .6); bh = 1.; bf = rng.uniform(.6, 1); bv = rng.uniform(0, .5)*bf
    dR = 1.; kap = rng.uniform(0, .6); eta = rng.uniform(5, 40)
    b0 = bv + s0*(bf-bv); Clow = b0*dR/(bh-b0); Chigh = kap/(q0*(bf-bv)) - dR
    Cs = np.unique(np.concatenate([np.linspace(0, 3*max(Clow, Chigh, .1), 25), [Clow, max(Chigh, 0)]]))
    res = [limite(q0, s0, bh, bv, bf, dR, C, kap, eta) for C in Cs]
    for i in range(len(Cs)-1):
        if res[i][0] < .1 and res[i+1][0] > .9 and res[i+1][1] > .9:
            found.append((q0, s0, bv, bf, kap, eta, Clow, Chigh, Cs[i], Cs[i+1], res[i], res[i+1])); break
print("basculements honnete -> triche obscurcie en augmentant C :", len(found), "sur 1500")
for r in found[:5]:
    print("   q0=%.3f s0=%.3f bv=%.3f bf=%.3f kap=%.3f eta=%.1f C_low=%.3f C_high=%.3f : C=%.3f -> (q,s)=(%.3g,%.3g) ; C=%.3f -> (%.3g,%.3g)" % (r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[10][0], r[10][1], r[9], r[11][0], r[11][1]))
