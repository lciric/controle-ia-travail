#!/usr/bin/env python3
"""Illustration de la garantie de pire cas du mecanisme de l'echelle (Blum et Hardt, 2015).

Source lue sur PDF : arXiv 1502.04585v1, theoreme 3.1, inegalite (4), page 6 du fichier
docs/sources/pdf/anteriorite-P-041-v2/c8/1502.04585.pdf du depot de travail
(sha256 957ef4739df371a0a778360f0db4252a62f7c85abcd8343f581cd6250b1d31fe).

Inegalite (4) : pour tout t <= k et tout eps > 0,
    Pr( | min_{i<=t} R_D(f_i) - R_t | > eps + eta ) <= exp( -2 eps^2 n + (1/eta + 2) log(4 t / eta) + 1 ).

Le programme cherche, pour une taille n de la reserve reutilisee et un nombre t de soumissions,
la plus petite erreur (eps + eta) pour laquelle le membre de droite vaut au plus 0,05, en
parcourant une grille du pas eta. C'est une garantie de pire cas, pas une erreur typique.
Aucun tirage aleatoire : le calcul est deterministe.
"""
import math

NIVEAU = 0.05
PAS_GRILLE = 2000


def plus_petite_erreur_garantie(n: int, t: int):
    cible = math.log(NIVEAU)
    meilleur = None
    for i in range(1, PAS_GRILLE):
        eta = i / PAS_GRILLE
        # 2 eps^2 n >= (1/eta + 2) log(4 t / eta) + 1 - log(niveau)
        droite = (1.0 / eta + 2.0) * math.log(4.0 * t / eta) + 1.0 - cible
        eps = math.sqrt(droite / (2.0 * n))
        somme = eps + eta
        if meilleur is None or somme < meilleur[0]:
            meilleur = (somme, eps, eta)
    return meilleur


def main() -> None:
    print("taille_n;soumissions_t;erreur_garantie_eps_plus_eta;eps;eta")
    for n in (100, 200, 240, 1000, 10000, 100000, 1000000):
        for t in (5, 10, 100):
            somme, eps, eta = plus_petite_erreur_garantie(n, t)
            print(f"{n};{t};{somme:.3f};{eps:.3f};{eta:.4f}")


if __name__ == "__main__":
    main()
