"""Verifications auxiliaires de la lecture d'anteriorite (six sources).
1) Penalite additive sans arret (Skaf et al. eq. 1 ; Gupta et Jenner eq. 4) contre operateur B :
   equivalence dans le modele a trois strates si beta_h = 1, avec C = lambda - DeltaR ; non-equivalence si beta_h < 1.
2) Borne de Santos-Grueiro (annexe A.1) : TV(P,Q) <= sqrt(2 JS(P,Q)) (prior uniforme), donc
   |tau_ord - tau_trap| <= TV <= sqrt(2 JS) : condition suffisante plus faible pour l'hypothese de R3.
3) Korbak et al. (annexe, p. 9) : recompense r = log P(accepte) a temperature 1 donne pi0 * beta, i.e. operateur A a eta = 0 ;
   et pi_A = Gibbs de R + log(beta)/eta.
"""
import math, random
from fractions import Fraction as F

def gibbs(weights):
    z = sum(weights); return [w / z for w in weights]

def opB(p, beta, R, C, eta):
    return gibbs([p[s] * math.exp(eta * (beta[s] * R[s] - (1 - beta[s]) * C)) for s in range(3)])

def additive(p, beta, R, lam, eta):
    return gibbs([p[s] * math.exp(eta * (R[s] - (1 - beta[s]) * lam)) for s in range(3)])

def opA(p, beta, R, eta):
    return gibbs([p[s] * beta[s] * math.exp(eta * R[s]) for s in range(3)])

random.seed(20261124)
maxdiff_eq, mindiff_neq = 0.0, 1.0
for _ in range(20000):
    a, b = random.random(), random.random()
    p = gibbs([a + .01, b + .01, random.random() + .01])
    bv = random.random() * 0.9; bf = bv + random.random() * (1 - bv)
    dR = random.uniform(0.05, 3); eta = random.uniform(0.1, 10); lam = random.uniform(0, 6)
    R = [0, dR, dR]
    # beta_h = 1
    beta = [1.0, bv, bf]
    d = max(abs(x - y) for x, y in zip(additive(p, beta, R, lam, eta), opB(p, beta, R, lam - dR, eta)))
    maxdiff_eq = max(maxdiff_eq, d)
    # beta_h < 1 : chercher le meilleur C sur une grille fine ; montrer qu'aucun C ne reproduit la loi en general
    bh = random.uniform(max(bf, 0.5), 0.99); beta2 = [bh, bv, min(bf, bh)]
    target = additive(p, beta2, R, lam, eta)
    best = min(max(abs(x - y) for x, y in zip(target, opB(p, beta2, R, c / 50, eta))) for c in range(-300, 600))
    mindiff_neq = min(mindiff_neq, best) if best > 1e-3 else mindiff_neq
print("1) beta_h=1 : ecart max entre penalite additive lambda et operateur B (C = lambda - DeltaR) =", maxdiff_eq)
cnt = 0; tot = 0
random.seed(7)
for _ in range(2000):
    p = gibbs([random.random() + .01 for _ in range(3)])
    bv = random.random() * 0.5; bf = bv + random.random() * (1 - bv); bh = random.uniform(max(bf, 0.6), 0.95)
    if bf > bh: bf = bh
    beta = [bh, bv, bf]; dR = random.uniform(0.2, 3); eta = random.uniform(0.5, 8); lam = random.uniform(0.5, 6)
    R = [0, dR, dR]
    target = additive(p, beta, R, lam, eta)
    best = min(max(abs(x - y) for x, y in zip(target, opB(p, beta, R, c / 100, eta))) for c in range(-600, 1200))
    tot += 1; cnt += best > 1e-4
print(f"   beta_h<1 : {cnt}/{tot} tirages ou aucun C de la grille [-6,12] (pas 0,01) ne reproduit la loi a 1e-4 pres")
# 2) TV <= sqrt(2 JS)
def kl(P, Q): return sum(p * math.log(p / q) for p, q in zip(P, Q) if p > 0)
worst = -1
for _ in range(20000):
    k = random.randint(2, 6)
    P = gibbs([random.random() ** 3 + 1e-12 for _ in range(k)]); Q = gibbs([random.random() ** 3 + 1e-12 for _ in range(k)])
    M = [(x + y) / 2 for x, y in zip(P, Q)]
    js = 0.5 * kl(P, M) + 0.5 * kl(Q, M); tv = 0.5 * sum(abs(x - y) for x, y in zip(P, Q))
    worst = max(worst, tv - math.sqrt(2 * js))
print("2) max (TV - sqrt(2 JS)) sur 20000 tirages (doit etre <= 0) =", worst)
# exemple : pieges melanges q -> TV = q ; sqrt(2 JS) plus grand
for q in [0.05, 0.2]:
    P = [1.0, 0.0]; Q = [1 - q, q]; M = [(x + y) / 2 for x, y in zip(P, Q)]
    js = 0.5 * kl(P, M) + 0.5 * kl(Q, M)
    print(f"   pieges melanges q={q}: TV={q}, sqrt(2 JS)={math.sqrt(2*js):.4f} (plancher MI plus haut que le plancher TV)")
# 3) Korbak : posterior p(x|O=1) prop pi0 * exp(r) avec r = log beta  -> pi0 * beta ; Op A = Gibbs(R + log(beta)/eta)
p = [F(1, 2), F(3, 10), F(1, 5)]; beta = [F(1), F(1, 10), F(3, 5)]
post = [pi * b for pi, b in zip(p, beta)]; z = sum(post); post = [x / z for x in post]
print("3) Korbak, r = log beta, temperature 1 : posterior =", post, "(= operateur A a eta = 0)")
eta = 2.0; R = [0, 1.0, 1.0]
a1 = opA([float(x) for x in p], [float(x) for x in beta], R, eta)
a2 = gibbs([float(pi) * math.exp(eta * (r + math.log(float(b)) / eta)) for pi, b, r in zip(p, beta, R)])
print("   operateur A vs Gibbs(R + log(beta)/eta) : ecart max =", max(abs(x - y) for x, y in zip(a1, a2)))
