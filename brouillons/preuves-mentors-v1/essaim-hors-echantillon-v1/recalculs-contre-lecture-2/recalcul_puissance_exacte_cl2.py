"""Contre-lecture 2 : recalcul indépendant (sans tirage, sans aucun module du dépôt) du seuil exact et de la puissance
exacte de `coelev_comptage` sous synchronisation (r = 1), loi de référence iid, P(X >= u) = q = 0,1.

Méthode différente de l'auteur (inclusion-exclusion sur les pas) et de la contre-lecture 1 (programmation dynamique
sur les agents) : programmation dynamique **sur les pas**, état = multi-ensemble des nombres de « 1 » qu'il reste à
placer pour chaque agent synchronisé (tirage séquentiel d'un sous-ensemble uniforme : au pas courant, un agent qui
doit encore placer k uns parmi L pas restants en place un avec la probabilité k/L).
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
from math import comb
import sys

Q = 0.1
ALPHA = 0.05


def binom_pmf(n, p, k):
    return comb(n, k) * p ** k * (1 - p) ** (n - k) if 0 <= k <= n else 0.0


def binom_cdf(n, p, x):
    if x < 0:
        return 0.0
    return sum(binom_pmf(n, p, k) for k in range(0, min(x, n) + 1))


def seuil_exact(K, T, q=Q, alpha=ALPHA):
    """Seuil aléatoirisé (c, g) de V = max_t C_t, C_t iid Bin(K, q) : P(V > c) + g P(V = c) = alpha."""
    F = lambda v: binom_cdf(K, q, v) ** T
    for c in range(K + 1):
        sup = 1 - F(c)
        if sup <= alpha:
            eg = F(c) - F(c - 1)
            return c, (alpha - sup) / eg


def proba_max_inf(K, T, m, j, q=Q):
    """P(max_t C_t < j) sous synchronisation de m agents au pas commun s."""
    n = T - 1
    pN = [binom_pmf(T, q, k) for k in range(T + 1)]
    FB = lambda x: binom_cdf(K - m, q, x)
    # loi initiale : multi-ensemble des N_i (m agents iid), pondérée par le pas commun
    etats = defaultdict(float)

    def rec(i, debut, pref, proba):
        # multi-ensembles par énumération ordonnée non décroissante + coefficient multinomial
        if i == m:
            cnt = Counter(pref)
            coef = 1
            reste = m
            for v in cnt.values():
                coef *= comb(reste, v)
                reste -= v
            ind = sum(1 for x in pref if x >= 1)
            w = coef * proba * FB(j - 1 - ind)
            if w:
                M = tuple(sorted(max(x - 1, 0) for x in pref))
                etats[M] += w
            return
        for x in range(debut, T + 1):
            rec(i + 1, x, pref + [x], proba * pN[x])

    rec(0, 0, [], 1.0)
    # pas autres que s
    for L in range(n, 0, -1):
        nouveaux = defaultdict(float)
        for M, w in etats.items():
            groupes = sorted(Counter(M).items())          # (k, n_k)
            choix = [range(nk + 1) if k > 0 else range(1) for k, nk in groupes]
            for fs in product(*choix):
                p, F, nouv = w, 0, []
                for (k, nk), f in zip(groupes, fs):
                    if k > 0:
                        p *= binom_pmf(nk, k / L, f)
                    F += f
                    nouv += [k - 1] * f + [k] * (nk - f)
                if p == 0.0:
                    continue
                p *= FB(j - 1 - F)
                if p:
                    nouveaux[tuple(sorted(nouv))] += p
        etats = nouveaux
    assert all(all(k == 0 for k in M) for M in etats)
    return sum(etats.values())


def puissance(K, T, m, seuil):
    c, g = seuil
    p1 = 1 - proba_max_inf(K, T, m, c + 1)
    p0 = 1 - proba_max_inf(K, T, m, c)
    return (1 - g) * p1 + g * p0


if __name__ == "__main__":
    for (K, T) in ((10, 10), (20, 10)):
        print(f"seuil exact e{K}x{T} :", seuil_exact(K, T))
    cas = [(10, 10, 3), (10, 10, 4), (10, 10, 5), (10, 10, 6), (10, 10, 7), (20, 10, 6)]
    for K, T, m in cas:
        s = seuil_exact(K, T)
        print(f"e{K}x{T} m = {m} : puissance exacte = {puissance(K, T, m, s):.7f}", flush=True)
    # contrôle de cohérence : m = 1 ne change pas la loi de max_t C_t ? (non : l'agent synchronisé garde N ; la loi
    # des comptes reste celle de P0, car un seul agent permuté en temps reste iid en loi) -> taille = alpha
    for K, T in ((10, 10), (20, 10)):
        s = seuil_exact(K, T)
        print(f"contrôle m = 1, e{K}x{T} : {puissance(K, T, 1, s):.7f} (attendu {ALPHA})")
