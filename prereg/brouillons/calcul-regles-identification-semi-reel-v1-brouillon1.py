"""Caractéristiques opératoires des règles de lecture du brouillon 1 du préenregistrement
« identification semi-réelle » (loi binomiale exacte, intervalles de Wilson à 95 %).
Aucun tirage aléatoire, aucune donnée lue : calcul déterministe, reproductible au bit près.
Usage : python3 calcul-regles-identification-semi-reel-v1-brouillon1.py
"""
from math import comb, sqrt, erf

Z = 1.959963984540054  # quantile 0,975 de la loi normale


def wilson(x, n, z=Z):
    p = x / n
    centre = (p + z * z / (2 * n)) / (1 + z * z / n)
    demi = z * sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return centre - demi, centre + demi


def pmf(x, n, p):
    return comb(n, x) * p ** x * (1 - p) ** (n - x)


def proba(n, p, garde):
    return sum(pmf(x, n, p) for x in range(n + 1) if garde(x))


def phi(z):
    return 0.5 * (1 + erf(z / sqrt(2)))


print("§ 1 — règle de recouvrement : borne basse de Wilson à 95 % >= 0,70 (n = 100 mondes)")
n = 100
xmin = min(x for x in range(n + 1) if wilson(x, n)[0] >= 0.70)
print(f"  plus petit nombre de mondes réussis : {xmin} sur {n} (part {xmin / n:.2f})")
for p in (0.60, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95):
    print(f"  recouvrement vrai {p:.2f} : probabilité que la règle tienne = {proba(n, p, lambda x: x >= xmin):.3f}")
for p in (0.85, 0.90, 0.95):
    q = proba(n, p, lambda x: x >= xmin)
    print(f"  conjonction de 4 règles (R et O, beta moyen et fort), recouvrement vrai {p:.2f} partout : {q ** 4:.3f}")

print("§ 2 — règle d'erreur par affectation, beta = 0 (n = 100) : borne haute de Wilson <= 0,15")
xmax = max(x for x in range(n + 1) if wilson(x, n)[1] <= 0.15)
print(f"  plus grand nombre de mondes en erreur : {xmax} sur {n}")
for p in (0.01, 0.05, 0.08, 0.10, 0.15, 0.20):
    q = proba(n, p, lambda x: x <= xmax)
    print(f"  erreur vraie {p:.2f} : règle tenue = {q:.3f} ; sur les 3 affectations (indépendantes) = {q ** 3:.3f}")

print("§ 3 — règle d'erreur sur leurre et jumeau, regroupée par affectation (n = 400 : 4 tailles d'effet) : borne haute <= 0,10")
n4 = 400
xmax4 = max(x for x in range(n4 + 1) if wilson(x, n4)[1] <= 0.10)
print(f"  plus grand nombre de mondes en erreur : {xmax4} sur {n4} (part {xmax4 / n4:.4f})")
for p in (0.01, 0.03, 0.05, 0.07, 0.08, 0.10, 0.12):
    q = proba(n4, p, lambda x: x <= xmax4)
    print(f"  erreur vraie {p:.2f} : règle tenue = {q:.3f} ; leurre et jumeau sur 3 affectations (6 règles indépendantes) = {q ** 6:.3f}")

print("§ 4 — volet B : écart apparié iVAE - réseau libre sur 50 mondes ; règle : estimation >= 0,15 et borne basse > 0")
for sd in (0.10, 0.15, 0.25):
    se = sd / sqrt(50)
    for vrai in (0.05, 0.10, 0.15, 0.20, 0.30):
        p_est = 1 - phi((0.15 - vrai) / se)
        p_lb = 1 - phi((Z * se - vrai) / se)
        print(f"  écart-type des écarts {sd:.2f} (erreur type {se:.4f}) ; écart vrai {vrai:.2f} : P(estimation >= 0,15) = {p_est:.3f} ; P(borne basse > 0) = {p_lb:.3f}")

print("§ 5 — volet B : part de mondes avec corrélation au facteur vrai >= 0,70, règle borne basse de Wilson >= 0,60 (n = 50)")
n5 = 50
xmin5 = min(x for x in range(n5 + 1) if wilson(x, n5)[0] >= 0.60)
print(f"  plus petit nombre de mondes réussis : {xmin5} sur {n5} (part {xmin5 / n5:.2f})")
for p in (0.50, 0.60, 0.70, 0.75, 0.80, 0.90):
    print(f"  part vraie {p:.2f} : règle tenue = {proba(n5, p, lambda x: x >= xmin5):.3f}")

print("§ 6 — volet B regroupé (Bv0 + Bv1 : n = 100) : part de mondes avec corrélation au facteur vrai >= 0,70, règle borne basse de Wilson >= 0,60")
n6 = 100
xmin6 = min(x for x in range(n6 + 1) if wilson(x, n6)[0] >= 0.60)
print(f"  plus petit nombre de mondes réussis : {xmin6} sur {n6} (part {xmin6 / n6:.2f})")
for p in (0.60, 0.65, 0.70, 0.75, 0.80, 0.90):
    print(f"  part vraie {p:.2f} : règle tenue = {proba(n6, p, lambda x: x >= xmin6):.3f}")

print("§ 7 — jugeabilité du leurre : part d'erreur du prédicteur associatif sur le leurre, regroupée sous R (n = 400) ; règle estimation >= 0,20")
for p in (0.10, 0.15, 0.18, 0.20, 0.25, 0.30):
    print(f"  part vraie {p:.2f} : règle tenue = {proba(n4, p, lambda x: x >= 80):.3f}")

print("§ 8 — ordre de grandeur de la détection (approximation normale, SUPPOSÉ) : 30 000 paires-années, 10 % traitées, effet beta en écarts-types de la sortie annuelle, sortie cumulée sur 3 ans (écart-type multiplié par racine de 3)")
for beta in (0.1, 0.2, 0.4):
    se = sqrt(1 / 3000 + 1 / 27000)
    z = (beta / sqrt(3)) / se
    print(f"  beta = {beta:.1f} : statistique de test attendue {z:.1f}")
