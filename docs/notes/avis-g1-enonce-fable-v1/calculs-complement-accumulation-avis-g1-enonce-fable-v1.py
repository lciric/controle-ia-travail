#!/usr/bin/env python3
"""Complement aux calculs de l'avis aveugle sur l'enonce du critere de G1 (bloc F).

Loi exacte sous SUPPOSITION D'ILLUSTRATION ; aucune donnee du programme ; aucun tirage ; bibliotheque standard.
Question : quel decalage par action, du au seul vehicule, suffit a faire perdre la garde de specificite
a un moniteur qui ACCUMULE ses scores sur les dix actions d'un episode ?

Supposition : score par action gaussien, variance 1, independant d'une action a l'autre chez l'honnete ;
statistique d'episode = somme sur T = 10 actions (substitut simple d'une accumulation additive) ;
seuil cale a 1 % de fausses alertes sur l'honnete ; le temoin decale chaque action de delta ecarts-types.
Alors le taux d'alerte vrai sur le temoin vaut w = 1 - Phi(z - delta * racine(T)).

Usage : python3 calculs-complement-accumulation-avis-g1-enonce-fable-v1.py > ...-sortie.txt
"""
import math
import sys
from statistics import NormalDist

N01 = NormalDist()


def log_pmf_binom(k, n, p):
    return (math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)
            + k * math.log(p) + (n - k) * math.log1p(-p))


def cdf_binom(k, n, p):
    return min(1.0, math.fsum(math.exp(log_pmf_binom(i, n, p)) for i in range(0, k + 1)))


def main():
    print("Complement (bloc F) - Python", sys.version.split()[0])
    print("Decalage par action du au vehicule, accumule sur T actions ; garde a 300 episodes : au plus 8 alertes.")
    z = N01.inv_cdf(0.99)
    for T in (1, 10):
        print(f"\n T = {T} action(s) lue(s) par episode")
        print("   decalage par action (ecarts-types) | taux d'alerte vrai sur le temoin | P(passer la garde, une cellule)")
        for delta in (0.0, 0.05, 0.10, 0.15, 0.20, 0.30, 0.50):
            w = 1.0 - N01.cdf(z - delta * math.sqrt(T))
            print(f"   {delta:4.2f}                               | {100 * w:5.2f} %                          | {cdf_binom(8, 300, w):.3f}")


if __name__ == "__main__":
    main()
