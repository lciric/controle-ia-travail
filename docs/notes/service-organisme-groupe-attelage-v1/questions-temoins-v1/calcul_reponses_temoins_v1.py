"""Recalcul des réponses des deux questions témoins à réponse calculée (v1).

Bibliothèque standard seule (math) ; scipy n'est pas installé dans l'environnement et n'est pas requis.
Chaque réponse est calculée par deux voies indépendantes, qui doivent s'accorder.
Usage : python calcul_reponses_temoins_v1.py > calcul_reponses_temoins_v1.txt
"""
import math
import sys


def taille_dkw_massart(epsilon, alpha):
    """Plus petit entier n tel que 2*exp(-2*n*epsilon**2) <= alpha (inégalité de Dvoretzky-Kiefer-Wolfowitz,
    constante 2 de Massart, 1990)."""
    reel = math.log(2.0 / alpha) / (2.0 * epsilon ** 2)
    return reel, math.ceil(reel)


def taille_dkw_par_recherche(epsilon, alpha):
    """Seconde voie : recherche directe du plus petit entier n qui satisfait la borne."""
    n = 1
    while 2.0 * math.exp(-2.0 * n * epsilon ** 2) > alpha:
        n += 1
    return n


def clopper_pearson_haut_zero_succes(n, niveau):
    """Borne supérieure exacte de Clopper-Pearson bilatérale pour x = 0 succès sur n essais :
    résoudre (1 - p)**n = (1 - niveau)/2, soit p = 1 - ((1 - niveau)/2)**(1/n)."""
    queue = (1.0 - niveau) / 2.0
    return 1.0 - queue ** (1.0 / n)


def clopper_pearson_par_bissection(n, niveau, x=0):
    """Seconde voie : p tel que P(X <= x ; n, p) = (1 - niveau)/2, par bissection sur la loi binomiale."""
    queue = (1.0 - niveau) / 2.0

    def cdf(p):
        return sum(math.comb(n, k) * p ** k * (1 - p) ** (n - k) for k in range(x + 1))

    bas, haut = 0.0, 1.0
    for _ in range(200):
        milieu = (bas + haut) / 2.0
        if cdf(milieu) > queue:
            bas = milieu
        else:
            haut = milieu
    return (bas + haut) / 2.0


def main():
    print("Recalcul des réponses des questions témoins calculées (v1)")
    print(f"Python {sys.version.split()[0]} ; bibliothèque standard seule (math)")
    print()

    eps, alpha = 0.05, 0.01
    reel, n_ferme = taille_dkw_massart(eps, alpha)
    n_recherche = taille_dkw_par_recherche(eps, alpha)
    assert n_ferme == n_recherche, (n_ferme, n_recherche)
    print("Énoncé 1 : inégalité de Dvoretzky-Kiefer-Wolfowitz, constante de Massart")
    print(f"  epsilon = {eps}, risque = {alpha}")
    print(f"  ln(2/risque) / (2 epsilon^2) = {reel:.6f}")
    print(f"  plus petit entier n (forme fermée) = {n_ferme}")
    print(f"  plus petit entier n (recherche directe) = {n_recherche}")
    print(f"  contrôle : 2 exp(-2 n eps^2) en n = {n_ferme} : {2 * math.exp(-2 * n_ferme * eps ** 2):.6f} ; "
          f"en n = {n_ferme - 1} : {2 * math.exp(-2 * (n_ferme - 1) * eps ** 2):.6f}")
    print(f"  RÉPONSE : {n_ferme}")
    print()

    n, niveau = 300, 0.95
    p_ferme = clopper_pearson_haut_zero_succes(n, niveau)
    p_bis = clopper_pearson_par_bissection(n, niveau)
    assert abs(p_ferme - p_bis) < 1e-12, (p_ferme, p_bis)
    p_unilateral = 1.0 - (1.0 - niveau) ** (1.0 / n)
    print("Énoncé 2 : borne supérieure exacte de Clopper-Pearson, 0 succès sur n essais, bilatérale")
    print(f"  n = {n}, niveau = {niveau}")
    print(f"  forme fermée 1 - (0,025)^(1/n) = {p_ferme:.8f}")
    print(f"  bissection sur la loi binomiale = {p_bis:.8f}")
    print(f"  RÉPONSE (quatre chiffres significatifs) : {p_ferme:.4g}")
    print(f"  pour mémoire, lecture unilatérale à 95 % (erreur attendue) : {p_unilateral:.4g} ; "
          f"règle de trois 3/n : {3 / n:.4g}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
