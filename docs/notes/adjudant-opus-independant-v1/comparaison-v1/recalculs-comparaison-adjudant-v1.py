"""Recalculs du comparateur (comparaison des deux réponses sur le mécanisme adjudant, v1).

Bibliothèque standard seule ; aucun tirage ; aucune donnée du programme. Chaque bloc porte une lettre,
citée entre crochets dans `comparaison-reponses-adjudant-v1.md`. Les valeurs d'entrée sont celles des
deux réponses ou de la contre-lecture ; aucune n'est une mesure.
"""
import math
from statistics import NormalDist

N01 = NormalDist()


def binom_cdf(c, n, r):
    return sum(math.comb(n, k) * r**k * (1 - r) ** (n - k) for k in range(0, c + 1))


def kl_bern(r, p):
    return r * math.log(r / p) + (1 - r) * math.log((1 - r) / (1 - p))


def r_max(d, p):
    lo, hi = p, 1 - 1e-12
    for _ in range(200):
        mid = (lo + hi) / 2
        if kl_bern(mid, p) <= d:
            lo = mid
        else:
            hi = mid
    return lo


print("[R1] Réponse B, loi du premier flagrant délit : (1 - q d) / (q d)")
for q, d in ((0.02, 0.5), (0.05, 0.8)):
    print(f"     q = {q}, d = {d} : {(1 - q * d) / (q * d):.2f} fois h_max")

print("[R2] Réponse B, plafond de divergence : plus grande probabilité r d'un événement de probabilité honnête p = 0,001")
for d in (0.01, 0.1):
    print(f"     D = {d} nat : r = {r_max(d, 0.001):.5f} ; borne de Pinsker racine(D/2) = {math.sqrt(d / 2):.4f}")

q, f, rho, z = 0.05, 0.10, 0.01, 2.5
print("[R3] Réponse B, ordre de grandeur z^2 (rho + f) / (q rho^2) avec q = 0,05, f = 0,10, rho = 0,01, z = 2,5 :"
      f" {z * z * (rho + f) / (q * rho * rho):.0f} épisodes ; excès cumulé avant détection z^2 (rho + f) / (q rho) :"
      f" {z * z * (rho + f) / (q * rho):.0f} épisodes endommagés")
for rho2 in (0.02, 0.005):
    print(f"     même calcul à rho = {rho2} : excès cumulé {z * z * (rho2 + f) / (q * rho2):.0f}")

print("[R4] Réponse A, bloc D : règle « moniteur invalide si au plus 2 signalés sur 6 »")
print(f"     rappel 0,8 : probabilité d'annoncer invalide {binom_cdf(2, 6, 0.8):.4f} ; rappel 0,2 : {binom_cdf(2, 6, 0.2):.4f}")

print("[R5] Réponse A, bloc A : test du total sur n épisodes indépendants, déplacement 0,1 écart type, niveau 1 %")
zc = N01.inv_cdf(0.99)
for n in (1, 100, 400, 1000):
    print(f"     n = {n:5d} : puissance {1 - N01.cdf(zc - 0.1 * math.sqrt(n)):.4f}")

print("[R6] Contre-lecture, recapture diluée : même règle, part s de sabotage parmi les endommagés audités,"
      " moniteur valide de rappel 0,8, signalement des endommagés honnêtes au taux e")
for e in (0.0, 0.01):
    for s in (1.0, 0.5, 0.3):
        p = 0.8 * s + e * (1 - s)
        print(f"     e = {e:.2f}, s = {s:.1f} : probabilité d'annoncer invalide {binom_cdf(2, 6, p):.4f}")

print("[R7] Contre-lecture, zone aveugle du pari de la réponse A : mise 0,25, taux honnête 0,10 ;"
      " excès où la croissance moyenne du logarithme de la richesse s'annule")
lam, p0 = 0.25, 0.10
a, b = math.log(1 + lam * (1 - p0)), math.log(1 - lam * p0)
r0 = -b / (a - b)
print(f"     taux d'annulation {r0:.5f}, soit un excès de {r0 - p0:.5f}")
for eps in (0.010, 0.012):
    r = p0 + eps
    print(f"     excès {eps:.3f} : croissance {r * a + (1 - r) * b:+.6f}")
