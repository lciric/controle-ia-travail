"""Calcul de conception, sans donnée : précision d'une proportion sur n épisodes, intervalle exact de
Clopper-Pearson à 95 %, par bissection sur la loi binomiale (bibliothèque standard seule).
Sortie : calcul-precision-repetition-v1.txt, à côté de ce fichier."""
from math import comb


def cdf(k, n, p):
    return sum(comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(0, k + 1))


def bissection(f, bas=0.0, haut=1.0):
    for _ in range(60):
        m = (bas + haut) / 2
        if f(m) > 0:
            bas = m
        else:
            haut = m
    return (bas + haut) / 2


def clopper_pearson(k, n, a=0.05):
    bas = 0.0 if k == 0 else bissection(lambda p: (a / 2) - (1 - cdf(k - 1, n, p)))
    haut = 1.0 if k == n else bissection(lambda p: cdf(k, n, p) - (a / 2))
    return bas, haut


if __name__ == "__main__":
    for n in (50, 100):
        demi = max(clopper_pearson(k, n)[1] - clopper_pearson(k, n)[0] for k in range(n + 1)) / 2
        k80 = min(k for k in range(n + 1) if clopper_pearson(k, n)[0] >= 0.80)
        print(f"n={n} ; demi-largeur maximale={demi:.3f} ; plus petit k dont la borne basse atteint 0,80 : {k80} ; "
              f"probabilité d'au moins {k80} succès si le taux vrai vaut 0,90 : {1 - cdf(k80 - 1, n, 0.90):.3f}, "
              f"0,95 : {1 - cdf(k80 - 1, n, 0.95):.3f} ; borne haute si 0 sur {n} : {clopper_pearson(0, n)[1]:.3f}")
