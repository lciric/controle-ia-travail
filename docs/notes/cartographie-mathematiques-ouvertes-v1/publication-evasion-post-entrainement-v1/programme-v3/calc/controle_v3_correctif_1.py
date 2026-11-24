"""Contrôles de l'auteur pour le correctif 1 de la v3 (défauts 1 et 2 de la contre-lecture). Hors dépôt."""
import numpy as np, math
rng = np.random.default_rng(np.random.SeedSequence(2026112416))
N = 100000
def champs(pi, bv, bf, dR, C):
    rb = np.array([0.0, bv*dR-(1-bv)*C, bf*dR-(1-bf)*C]); mu = pi@rb
    m2 = pi[1]*(bv*dR**2+(1-bv)*C**2) + pi[2]*(bf*dR**2+(1-bf)*C**2)
    return rb, mu, math.sqrt(max(m2-mu**2, 1e-300))
def taux(pi, bv, bf, dR, C):
    rb, mu, s = champs(pi, bv, bf, dR, C)
    nat_f = rb[2]-mu                      # gradient naturel, moyenne seule : d/dt log pi_f
    nat_fh = rb[2]-rb[0]; nat_fv = rb[2]-rb[1]
    th = pi*(rb-mu); euc_f = th[2]-pi@th  # gradient euclidien sur les logits, moyenne seule
    return dict(nat_f=nat_f, nat_fh=nat_fh, nat_fv=nat_fv, euc_f=euc_f,
                std_f=nat_f/s, std_fh=nat_fh/s, std_fv=nat_fv/s)
for nom, niche in (("niche parfaite (beta_f = 1)", True), ("detection partielle (beta_f < 1)", False)):
    cpt = {}; n_h = 0; cpt_h = {}; ecart_formule = 0.0
    for _ in range(N):
        pi = rng.dirichlet([1,1,1]); bv = rng.uniform(0.01,0.99); dR = rng.uniform(0.1,3); C = rng.uniform(0,4); h = 1e-6
        bf = 1.0 if niche else rng.uniform(bv, 1.0)
        a, b = taux(pi,bv,bf,dR,C+h), taux(pi,bv,bf,dR,C-h)
        d = {k:(a[k]-b[k])/(2*h) for k in a}
        if niche: ecart_formule = max(ecart_formule, abs(d["nat_f"]-(1-bv)*pi[1]))
        for k,v in d.items():
            cpt[k] = cpt.get(k,0) + (v > 1e-9)
        if pi[0] > 1/math.sqrt(3):
            n_h += 1
            for k,v in d.items(): cpt_h[k] = cpt_h.get(k,0) + (v > 1e-9)
    print(nom, "| derivee en C strictement positive, sur", N, ":", cpt)
    print("   part honnete > 1/sqrt3 :", n_h, cpt_h, "| ecart a (1-beta_v) pi_v :", ecart_formule if niche else "sans objet")
# Défaut 2 : lot rempli de survivants, moyenne des acceptés pour ligne de base
for p, beta, eta in ((np.array([0.85,0.14,0.01]), np.array([1,0.2,0.6]), 1.5),
                     (np.array([0.6,0.3,0.1]), np.array([0.9,0.1,0.7]), 0.8),
                     (np.array([0.5,0.25,0.25]), np.array([1,0.05,0.95]), 2.5)):
    R = np.array([0,1.0,1.0]); th = np.log(p).copy()
    for _ in range(600000):
        pi = np.exp(th-th.max()); pi /= pi.sum(); Z = pi@beta; b = (pi*beta)@R/Z
        g = beta*(R-b)/Z - (np.log(pi)-np.log(p))/eta; g -= pi@g; th += 0.01*g
    pi = np.exp(th-th.max()); pi /= pi.sum(); Z = pi@beta; b = (pi*beta)@R/Z
    f1 = p*np.exp((eta/Z)*(beta*R-(1-beta)*(-b))); f1 /= f1.sum()
    f0 = p*np.exp((eta/Z)*(beta*R)); f0 /= f0.sum()
    print("survivants + moyenne des acceptes : ecart a la penalite C=-b, pression eta/Z :", abs(pi-f1).max(), "| a la penalite de score brut nul, meme pression :", abs(pi-f0).max())
