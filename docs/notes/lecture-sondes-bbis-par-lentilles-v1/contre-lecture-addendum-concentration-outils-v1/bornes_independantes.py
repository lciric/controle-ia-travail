"""Contre-calcul indépendant des 41 bornes de calibration (contre-lecteur Opus 5.5).
Loi bêta-binomiale par récurrence de rapports (pas de lgamma par terme), en fractions exactes pour n = 200 et 1 000,
puis somme de k jeux par convolution en double ; bornes par les définitions du texte ; risque de sortie ; sensibilité à une
sur-dispersion (même moyenne, a + b réduit pour gonfler la variance totale du compte de 5 % et de 10 %)."""
from fractions import Fraction
import numpy as np

M, R = 2000, 100
A, B = 100, 1901


def bb_exact(n, a, b):
    # p(0) = B(a, b + n) / B(a, b) = prod_{i=0}^{n-1} (b + i) / (a + b + i) ; p(k+1)/p(k) = (n-k)(k+a) / ((k+1)(n-k-1+b))
    p0 = Fraction(1)
    for i in range(n):
        p0 *= Fraction(b + i, a + b + i)
    p = [p0]
    for k in range(n):
        p.append(p[-1] * Fraction((n - k) * (k + a), (k + 1) * (n - k - 1 + b)))
    s = sum(p)
    assert s == 1, s
    return np.array([float(x) for x in p])


def bb_float(n, a, b):
    lp = [0.0]
    for k in range(n):
        lp.append(lp[-1] + np.log((n - k) * (k + a)) - np.log((k + 1) * (n - k - 1 + b)))
    lp = np.array(lp)
    p = np.exp(lp - lp.max())
    return p / p.sum()


def bornes(p, niveau=1e-4):
    c = np.concatenate([[0.0], np.cumsum(p)])      # c[q] = P(X < q)
    q_bas = max(q for q in range(len(p) + 1) if c[q] <= niveau)
    queue = 1 - c[1:]                                # queue[q] = P(X > q), recalculée par somme directe pour la précision
    queue = np.array([p[q + 1:].sum() for q in range(len(p))])
    q_haut = min(q for q in range(len(p)) if queue[q] <= niveau)
    return q_bas, q_haut, float(c[q_bas]), float(queue[q_haut])


p200 = bb_exact(200, A, B)
p1000 = bb_exact(1000, A, B)
print("cas | [q_bas, q_haut] | risque de sortie | risque si variance +5 % | +10 %")


def compte(k, base):
    p = np.array([1.0])
    for _ in range(k):
        p = np.convolve(p, base)
    return p


def s_pour_inflation(n, f):
    # variance du compte d'un jeu : n pi (1 - pi) (S + n) / (S + 1), S = a + b ; on cherche S tel que facteur = f × facteur(2001)
    cible = f * (2001 + n) / 2002
    return (n - cible) / (cible - 1)


def risque(p, qb, qh):
    return float(p[:qb].sum() + p[qh + 1:].sum())


pire = 0
for nom, k, n, base in [("1 jeu de 1 000", 1, 1000, p1000)] + [(f"{k} x 200", k, 200, p200) for k in range(1, 41)]:
    p = compte(k, base)
    qb, qh, g, d = bornes(p)
    r = risque(p, qb, qh)
    pire = max(pire, r)
    sens = []
    for f in (1.05, 1.10):
        S = s_pour_inflation(n, f)
        bb = bb_float(n, S * R / (M + 1), S * (1 - R / (M + 1)))
        sens.append(risque(compte(k, bb), qb, qh))
    print(f"{nom} | [{qb}, {qh}] | {r:.3e} | {sens[0]:.3e} | {sens[1]:.3e}")
print(f"pire : {pire:.4e}")
