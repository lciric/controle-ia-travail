"""Contre-lecteur, modele O : calcul a la main (approximation normale) de la reserve 23 de la v7 du palier 0b.

Aucun tirage, aucune graine, aucun appel au code de l'etage : fonctions de repartition normales seulement.
Hypothese de travail : l'exactitude observee A suit une loi normale de moyenne l'exactitude vraie et d'ecart-type sigma,
sigma etant pris egal a sigma0 (ecart-type sous permutation), comme le fait le redacteur.
"""
import math


def queue_haute(seuil, moyenne, sigma):
    """P(A > seuil) pour A normale(moyenne, sigma)."""
    z = (seuil - moyenne) / sigma
    return 0.5 * math.erfc(z / math.sqrt(2.0))


def ligne(nom, valeur):
    print(f"{nom} : {valeur:.6g}")


print("== Audits des mondes par dose (une paire de doses, 200 mondes contre 200) ==")
for sigma0 in (0.032, 0.025, 0.040, 0.045, 0.064):
    seuil = 0.55 + 2 * sigma0
    print(f"-- sigma0 = {sigma0} ; seuil d'arret 0,55 + 2 sigma0 = {seuil:.4f}")
    p0 = queue_haute(seuil, 0.50, sigma0)
    ligne("   generateur parfait (0,50), arret par paire", p0)
    ligne("   generateur parfait, arret sur l'une des trois paires (independance, borne haute)", 1 - (1 - p0) ** 3)
    for vraie in (0.55, 0.58, 0.60, 0.62, 0.65):
        ligne(f"   exactitude vraie {vraie}, arret", queue_haute(seuil, vraie, sigma0))
        ligne(f"   exactitude vraie {vraie}, A > 0,55 (lie l'etage payant)", queue_haute(0.55, vraie, sigma0))

print("== Lettre de la v6 sur une paire de doses (seuil 0,55) ==")
for sigma0 in (0.032, 0.023):
    ligne(f"   generateur parfait, sigma {sigma0}, A > 0,55", queue_haute(0.55, 0.50, sigma0))

print("== Audits de lois (sigma0 de l'ordre de 0,01) ==")
for sigma0 in (0.007, 0.010, 0.012):
    seuil = 0.55 + 2 * sigma0
    print(f"-- sigma0 = {sigma0} ; seuil d'arret = {seuil:.4f}")
    ligne("   generateur parfait, lettre v6 (A > 0,55)", queue_haute(0.55, 0.50, sigma0))
    ligne("   generateur parfait, regle calibree", queue_haute(seuil, 0.50, sigma0))
    for vraie in (0.56, 0.565, 0.57, 0.60):
        ligne(f"   exactitude vraie {vraie}, arret a la lettre v6", queue_haute(0.55, vraie, sigma0))
        ligne(f"   exactitude vraie {vraie}, arret sous la regle calibree", queue_haute(seuil, vraie, sigma0))
