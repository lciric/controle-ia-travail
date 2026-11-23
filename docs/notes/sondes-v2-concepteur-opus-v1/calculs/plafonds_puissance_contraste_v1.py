"""Plafond de puissance du contraste apparié lu sur un nul tiré (calcul analytique, sans donnée).

Avec R échanges tirés au hasard parmi les 2^P échanges par paire, la valeur p est (1 + b)/(1 + R), b = nombre de
tirages dont l'aire atteint l'observée. Sous un effet infini, seuls l'échange identité et l'échange global (son image,
d'aire voisine) peuvent l'atteindre : b suit une loi binomiale (R, q), q = 2^(1−P) si l'image compte (prudent),
q = 2^(−P) si elle ne compte pas. Lecture possible si p ≤ α, soit b ≤ α(1 + R) − 1.
Règle de testabilité : non testable si max(2^(1−P), 1/(1 + R)) > α."""
import math
from scipy.stats import binom

def plafond(P, R, alpha, q):
    k = math.floor(alpha * (1 + R) - 1 + 1e-9)
    return 0.0 if k < 0 else float(binom.cdf(k, R, q))

print("paires;rejeux;alpha;testable;plafond_image_comptee;plafond_image_non_comptee")
for alpha in (0.05, 0.01):
    for R in (39, 199):
        for P in (5, 6, 7, 8, 9, 10, 12, 16):
            testable = max(2.0 ** (1 - P), 1.0 / (1 + R)) <= alpha
            a, b = plafond(P, R, alpha, 2.0 ** (1 - P)), plafond(P, R, alpha, 2.0 ** (-P))
            print(f"{P};{R};{alpha};{'oui' if testable else 'non'};{a:.3f};{b:.3f}")
