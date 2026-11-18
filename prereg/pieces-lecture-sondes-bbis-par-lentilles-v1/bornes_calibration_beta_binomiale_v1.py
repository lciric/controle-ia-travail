"""Bornes de calibration du texte « lecture des sondes de l'étape B bis par la lentille publique » (v1), sous la loi exacte
du compte (vérification 1, V-M3) : pour un jeu de n témoins comparés aux mêmes M = 2 000 directions nulles, le compte des
p ≤ 0,05 suit la loi bêta-binomiale (n ; 100 ; M − 99 = 1 901) ; pour plusieurs jeux mis en commun, la somme de lois
bêta-binomiales indépendantes. q_bas = plus grand entier tel que P(X < q_bas) ≤ 1e-4 ; q_haut = plus petit entier tel que
P(X > q_haut) ≤ 1e-4. Aucune donnée ; bibliothèque standard seulement. Comparé aussi à la loi binomiale (n, 100/2 001)."""
from math import lgamma, exp, comb, log

A, B, NIVEAU = 100, 1901, 1e-4


def pmf_beta_binomiale(n):
    lb = lgamma(A) + lgamma(B) - lgamma(A + B)
    return [exp(log(comb(n, k)) + lgamma(k + A) + lgamma(n - k + B) - lgamma(n + A + B) - lb) for k in range(n + 1)]


def pmf_binomiale(n, p=100 / 2001):
    return [exp(log(comb(n, k)) + k * log(p) + (n - k) * log(1 - p)) for k in range(n + 1)]


def convoluer(a, b):
    c = [0.0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                c[i + j] += x * y
    return c


def bornes(pmf):
    cum, bas = 0.0, 0
    for q in range(len(pmf)):          # P(X < q) = somme des k < q
        if cum <= NIVEAU:
            bas = q
        cum += pmf[q]
    # haut = plus petit q tel que P(X > q) <= NIVEAU (P(X > q) = somme des k > q)
    queue, haut = 0.0, 0
    for q in range(len(pmf) - 1, -1, -1):
        if queue > NIVEAU:
            haut = q + 1
            break
        queue += pmf[q]
    return bas, haut


def risque(pmf, b):
    bas, haut = b
    return sum(pmf[:bas]), sum(pmf[haut + 1:])


if __name__ == "__main__":
    cas = [("un jeu de 1 000", [1000]), ("un jeu de 200", [200]), ("trois jeux de 200", [200] * 3),
           ("cinq jeux de 200", [200] * 5), ("un jeu de 600", [600])]
    for nom, jeux in cas:
        pmf = [1.0]
        for n in jeux:
            pmf = convoluer(pmf, pmf_beta_binomiale(n))
        bb = bornes(pmf)
        nb = sum(jeux)
        pb = bornes(pmf_binomiale(nb))
        rb = risque(pmf, pb)
        print(f"{nom} (n = {nb}) : bêta-binomiale [{bb[0]}, {bb[1]}], risques {risque(pmf, bb)[0]:.2e} / {risque(pmf, bb)[1]:.2e} ; "
              f"binomiale [{pb[0]}, {pb[1]}], risques réels sous la loi exacte {rb[0]:.2e} / {rb[1]:.2e} ; somme des probabilités {sum(pmf):.12f}")
