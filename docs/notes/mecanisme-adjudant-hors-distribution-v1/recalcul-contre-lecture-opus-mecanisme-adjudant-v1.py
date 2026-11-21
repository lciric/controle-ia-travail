"""Recalcul indépendant des blocs A à E de la note « mécanisme adjudant » (contre-lecture Opus 5.5, v1).

Voie distincte de celle de l'auteur (`calculs-mecanisme-adjudant-v1.py`) : loi normale par math.erf et
bissection ; binomiales en fractions exactes ; pour le bloc C, frontière d'alarme calculée une fois, puis
premier passage par numpy. Ajouts de la contre-lecture : bloc A sur n épisodes, bloc B à oracle inégal,
bloc C (zone aveugle de la grille de mises, attaquant lent), bloc D (recapture diluée par le dommage
honnête), bloc E (plancher 2m - 1 du dilemme), et les objets de contrôle. Aucun tirage, aucune donnée du
programme : toutes les entrées sont les suppositions d'illustration de l'auteur ou des variantes déclarées.
Commande : PYTHONPATH=src .venv/bin/python -I <ce fichier>
"""
import math
from fractions import Fraction

import numpy as np


def phi(x):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def phi_inv(p):
    lo, hi = -10.0, 10.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if phi(mid) < p:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def cdf_exacte(c, n, r):
    r = Fraction(r)
    return sum(Fraction(math.comb(n, k)) * r**k * (1 - r) ** (n - k) for k in range(c + 1))


def bloc_a():
    print("[A] Recalcul. Puissance maximale au niveau 1 % pour un déplacement delta (un seul épisode).")
    z = phi_inv(0.99)
    print(f"    z(0,99) = {z:.6f}")
    for d in (0.1, 0.25, 0.446, 1.0, 2.0, 3.0):
        print(f"    delta {d:5.3f} : puissance {1 - phi(z - d):.4f} ; variation totale {2 * phi(d / 2) - 1:.4f}")
    print("    Ajout : test du total sur n épisodes indépendants, déplacement 0,1 écart type à chaque épisode.")
    for n in (1, 100, 400, 1000):
        print(f"      n = {n:5d} : puissance {1 - phi(z - 0.1 * math.sqrt(n)):.4f}")


def bloc_b():
    print("[B] Recalcul. Prise au k-ième épisode endommagé avec probabilité 0,95 (l'honnête n'en commet jamais).")
    for p in (0.01, 0.20):
        for q in (1.0, 0.5):
            pq = p * q
            k = 1
            while 1 - (1 - pq) ** k < 0.95:
                k += 1
            print(f"    p {p:4.2f}, q {q:3.1f} : moyenne {(1 - pq) / pq:6.1f} ; k95 = {k}")
    print("    Ajout : oracle inégal, q = 1 sur la moitié des tâches, q = 0,2 sur l'autre, audit 1 %.")
    for nom, q in (("saboteur qui choisit les tâches à q = 0,2", 0.2), ("q moyen 0,6", 0.6), ("q = 1", 1.0)):
        print(f"      {nom} : k95 = {math.ceil(math.log(0.05) / math.log(1 - 0.01 * q))}")


D0, G = 0.10, 20
MISES = np.array([(j + 0.5) / G / D0 for j in range(G)])
LP = np.log1p(MISES * (1 - D0))
LM = np.log1p(-MISES * D0)
SEUIL = math.log(100.0)
NMAX = 40000


def log_richesse(n, k):
    v = k * LP + (n - k) * LM
    t = v.max()
    return t + math.log(np.exp(v - t).sum() / G)


def calcul_frontiere():
    fr = np.empty(NMAX + 1, dtype=np.int64)
    k = 0
    for n in range(NMAX + 1):
        k = max(0, min(k, n))
        while k > 0 and log_richesse(n, k - 1) >= SEUIL:
            k -= 1
        while k <= n and log_richesse(n, k) < SEUIL:
            k += 1
        fr[n] = k  # n + 1 : aucune valeur de k ne sonne à n audits
    return fr


FRONTIERE = calcul_frontiere()


def premier_passage(d, horizon):
    masse = np.zeros(horizon + 2)
    masse[0] = 1.0
    cumul, med = 0.0, None
    for n in range(1, horizon + 1):
        nouv = np.zeros_like(masse)
        nouv[1:] += masse[:-1] * d
        nouv += masse * (1 - d)
        b = FRONTIERE[n]
        if b <= n:
            cumul += nouv[b:].sum()
            nouv[b:] = 0.0
        masse = nouv
        if med is None and cumul >= 0.5:
            med = n
    return cumul, med


def bloc_c():
    print("[C] Recalcul. Pari en mélange de l'auteur (20 mises de 0,25 à 9,75), d0 = 0,10, alarme à 100.")
    for d1, h in ((0.15, 3000), (0.20, 1500), (0.30, 600)):
        fa, _ = premier_passage(D0, h)
        al, med = premier_passage(d1, h)
        print(f"    d1 {d1:4.2f} : fausse alarme {fa:.4f} ; alarme {al:.4f} ; médiane {med} audits")
    m = MISES[0]
    a, b = math.log1p(m * (1 - D0)), math.log1p(-m * D0)
    eps_star = (-D0 * a - (1 - D0) * b) / (a - b)
    print(f"    Ajout : plus petite mise {m:.3f} ; excès critique eps* = {eps_star:.5f} : sous eps*, toutes les mises")
    print("    de la grille ont une croissance négative du logarithme de la richesse.")
    for eps in (0.005, 0.010, 0.012, 0.020):
        g = (D0 + eps) * a + (1 - D0 - eps) * b
        print(f"      eps {eps:.3f} : croissance de la plus petite mise {g:+.6f}")
    print(f"    Frontière asymptotique : {(-b) / (a - b):.5f} n + {math.log(100 * G) / (a - b):.1f} ; calculée :")
    for n in (100, 1000, 10000, 40000):
        print(f"      n = {n:6d} audits : frontière {FRONTIERE[n]:5d} ; excès toléré {FRONTIERE[n] - n * D0:7.1f}")
    print("    Ajout : attaquant lent, taux d0 + eps à chaque épisode ; excès total = eps x médiane / p.")
    for eps, h in ((0.10, 1500), (0.05, 3000), (0.02, 15000), (0.01, 40000)):
        al, med = premier_passage(D0 + eps, h)
        if med is None:
            print(f"      eps {eps:4.2f} : pas de médiane avant {h} audits ; alarme à l'horizon {al:.3f}")
            continue
        print(f"      eps {eps:4.2f} : médiane {med:5d} audits ; excès total p=1 : {eps * med:5.0f} ; "
              f"p=0,2 : {eps * med / 0.2:5.0f} ; p=0,05 : {eps * med / 0.05:6.0f}")


def bloc_d():
    print("[D] Recalcul en fractions exactes.")
    for r0 in ("0.128", "0.25", "0.5", "0.8"):
        n = 1
        while (1 - Fraction(r0)) ** n > Fraction(1, 20):
            n += 1
        print(f"    (i) r0 {r0} : n = {n}")
    for r0, r1 in (("0.8", "0.2"), ("0.5", "0.1"), ("0.5", "0.25"), ("0.128", "0.02")):
        trouve = None
        for n in range(1, 120):
            for c in range(n + 1):
                risque = cdf_exacte(c, n, r0)
                if risque > Fraction(1, 20):
                    break
                puissance = cdf_exacte(c, n, r1)
                if puissance >= Fraction(9, 10):
                    trouve = (n, c, float(risque), float(puissance))
                    break
            if trouve:
                break
        print(f"    (ii) r0 {r0}, r1 {r1} : n = {trouve[0]}, c = {trouve[1]}, risque {trouve[2]:.5f}, "
              f"puissance {trouve[3]:.5f}")
    print("    Ajout : recapture diluée. Part s du sabotage parmi les endommagés audités ; rappel 0,8 sur le")
    print("    sabotage, signalement 0,01 sur le dommage honnête ; règle n = 6, « invalide » si X <= 2.")
    for s in ("1", "0.5", "0.3", "0.2"):
        ra = Fraction(s) * Fraction("0.8") + (1 - Fraction(s)) * Fraction("0.01")
        print(f"      s = {s:>3} : rappel apparent {float(ra):.3f} ; P(annonce « invalide » | moniteur valide) = "
              f"{float(cdf_exacte(2, 6, ra)):.3f}")


def bloc_e():
    print("[E] Recalcul. Aveuglement conjoint minimal de deux regards aveugles chacun avec probabilité m.")
    for m in (0.5, 0.8):
        pmin = max(0.0, 2 * m - 1)
        k = 1
        while m**k >= 0.01:
            k += 1
        print(f"    m {m} : indépendants {m * m:.4f} ; dilemme parfait {pmin:.4f} "
              f"(corrélation {(pmin - m * m) / (m * (1 - m)):.2f}) ; regards indépendants pour passer sous 1 % : {k}")


def controles():
    print("[Contrôles] Témoins dont la réponse est connue par construction.")
    k = 1
    while 1 - (1 - 1.0 * 1.0) ** k < 0.95:
        k += 1
    print(f"    B à p = q = 1 : k95 attendu 1 ; rendu {k}")
    ok46 = any(cdf_exacte(c, 46, "0.128") <= Fraction(1, 20) and cdf_exacte(c, 46, "0.02") >= Fraction(9, 10)
               for c in range(47))
    print(f"    D à n = 46 pour (0,128 ; 0,02) : règle attendue absente ; rendu « présente » = {ok46}")
    fa, _ = premier_passage(D0, 3000)
    print(f"    C sous l'honnête : fausse alarme attendue <= 0,01 (inégalité de Ville) ; rendu {fa:.4f}")


if __name__ == "__main__":
    for bloc in (bloc_a, bloc_b, bloc_c, bloc_d, bloc_e, controles):
        bloc()
        print()
