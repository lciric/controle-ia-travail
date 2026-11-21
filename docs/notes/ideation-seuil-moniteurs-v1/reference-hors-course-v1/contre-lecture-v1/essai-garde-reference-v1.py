#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Essai du contre-lecteur : taux de fausse alarme de la garde de la référence
(arrêt 20 de la section), sur l'objet vrai et sur l'objet faux.

Bibliothèque standard seule. Graine fixe (random.Random(20261121)), écrite ici.
Sous une loi continue, le taux vrai V1* du k-ième plus grand de m témoins
échangeables suit exactement une loi bêta(k, m + 1 - k) : on le tire ainsi.

Prédictions de la section, § 9 : (P1) l'intervalle de Student à 99 % de la
moyenne de V1* sur 2 000 tirages contient k / (m + 1) ; (P2) l'intervalle de
Clopper-Pearson à 99 % de la part des tirages où V1* <= 1 % contient
P(Bin(m ; 0,01) >= k). La garde « manque » si l'une des deux manque.

Usage : python3 -I -B essai-garde-reference-v1.py
"""
import math
import random
from statistics import NormalDist

N01 = NormalDist()
R = 2000
T995 = 2.5781  # quantile 0,995 de Student à 1 999 degrés (approché)
REPLIQUES = 400
GRAINE = 20261121


def binom_pmf(n, j, p):
    return math.exp(math.lgamma(n + 1) - math.lgamma(j + 1) - math.lgamma(n - j + 1)
                    + j * math.log(p) + (n - j) * math.log1p(-p))


def binom_cdf(n, x, p):
    return sum(binom_pmf(n, j, p) for j in range(0, x + 1))


def cp_contient(x, n, p0, alpha=0.01):
    """L'intervalle exact de Clopper-Pearson à 1 - alpha contient p0 ssi les deux
    queues exactes en p0 dépassent alpha / 2."""
    bas = 1.0 - binom_cdf(n, x - 1, p0) if x > 0 else 1.0
    haut = binom_cdf(n, x, p0)
    return bas > alpha / 2 and haut > alpha / 2


def student_contient(valeurs, cible):
    n = len(valeurs)
    moy = sum(valeurs) / n
    var = sum((v - moy) ** 2 for v in valeurs) / (n - 1)
    demi = T995 * math.sqrt(var / n)
    return (moy - demi) <= cible <= (moy + demi), moy


def tirer_v1_vrai(gen, m, k):
    return [gen.betavariate(k, m + 1 - k) for _ in range(R)]


def tirer_v1_faux(gen, m, k, derive):
    """Témoins tirés de la loi de calibration N(0,1), usage translaté de derive."""
    out = []
    for _ in range(R):
        u = gen.betavariate(k, m + 1 - k)          # queue au seuil, sous la calibration
        u = min(max(u, 1e-15), 1 - 1e-15)
        seuil = N01.inv_cdf(1.0 - u)
        out.append(1.0 - N01.cdf(seuil - derive))
    return out


def main():
    gen = random.Random(GRAINE)
    derive = N01.inv_cdf(0.99) - N01.inv_cdf(0.97)
    print("Essai de la garde de la référence ; graine", GRAINE, "; répliques", REPLIQUES)
    for m in (200, 400):
        k = int(math.floor(0.01 * (m + 1) + 1e-12))
        cible = k / (m + 1)
        p_part = 1.0 - binom_cdf(m, k - 1, 0.01)
        manque1 = manque2 = manque_un = 0
        for _ in range(REPLIQUES):
            v = tirer_v1_vrai(gen, m, k)
            ok1, _ = student_contient(v, cible)
            x = sum(1 for t in v if t <= 0.01)
            ok2 = cp_contient(x, R, p_part)
            manque1 += (not ok1)
            manque2 += (not ok2)
            manque_un += (not (ok1 and ok2))
        q = manque_un / REPLIQUES
        print(f"objet vrai m={m} k={k} : P1 manquée {manque1}/{REPLIQUES} ; P2 manquée {manque2}/{REPLIQUES} ;"
              f" l'une ou l'autre {manque_un}/{REPLIQUES} (q = {q:.4f})")
        for cellules in (18, 36, 54, 78):
            print(f"    si {cellules} cellules indépendantes de cette sorte : P(au moins une garde manquée) = "
                  f"{1 - (1 - q) ** cellules:.3f} ; borne au q nominal 0,02 : {1 - 0.98 ** cellules:.3f}")
        tues = 0
        for _ in range(40):
            v = tirer_v1_faux(gen, m, k, derive)
            n = len(v)
            moy = sum(v) / n
            var = sum((t - moy) ** 2 for t in v) / (n - 1)
            if moy - T995 * math.sqrt(var / n) > 0.01:
                tues += 1
        print(f"objet faux m={m} : tué par « invalide, en moyenne » {tues}/40 (moyenne de la dernière réplique {moy:.5f})")


if __name__ == "__main__":
    main()
