#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Calculs de la note « trois asymétries de l'attaquant » (v1).

Formules exactes ou approximation normale déclarée ; aucun tirage, aucune
donnée du programme, aucune dépendance hors de la bibliothèque standard.
Toutes les valeurs d'entrée sont des suppositions d'illustration, sauf les
deux corrélations du bloc D, lues sur un PDF cité dans la note.

Usage : python3 calculs-asymetries-v1.py > calculs-asymetries-v1.txt
"""
from math import ceil, comb, log, sqrt
from statistics import NormalDist

Z = NormalDist().inv_cdf


def titre(t):
    print()
    print("=" * 78)
    print(t)
    print("=" * 78)


# --------------------------------------------------------------------------
# Bloc A — un moniteur qui apprend sur les audits tirés au hasard
# --------------------------------------------------------------------------
titre("A. Moniteur qui apprend : borne du nombre total d'erreurs, taux d'audit constant")
print("Hypothèse reprise de la source : un apprenant en ligne qui fait au plus B erreurs")
print("sur toute suite réalisable ; chaque épisode est audité, après la décision, avec")
print("la probabilité e, indépendamment. Alors e * E[erreurs totales] <= B, donc")
print("E[erreurs totales] <= B / e, quel que soit l'horizon et quel que soit l'adversaire.")
print()
print("Témoin (doit redonner la note sur l'adjudant) : épisode endommagé où la prise")
print("est acquise avec probabilité 0,95, sans rien apprendre : ceil(ln 0,05 / ln(1-e)).")
for e in (0.01, 0.20):
    print(f"  e = {e:4.2f} : {ceil(log(0.05) / log(1 - e))}")
print()
print("   B \\ e      0,01      0,05      0,20")
for B in (5, 20, 100):
    print(f"  {B:4d}   " + "  ".join(f"{B / e:8.0f}" for e in (0.01, 0.05, 0.20)))
print()
print("Objet où la conclusion est fausse : si la vérité n'est pas une fonction de ce")
print("que lit le moniteur (même entrée, deux vérités), aucune borne B n'existe ;")
print("à taux d'erreur m par épisode, les erreurs valent m * T :")
for T in (1_000, 10_000, 100_000):
    print(f"  T = {T:7d}, m = 0,10 : {0.10 * T:8.0f} erreurs (croît sans plafond)")

# --------------------------------------------------------------------------
# Bloc B — ce que l'agent doit payer pour apprendre la règle d'audit
# --------------------------------------------------------------------------
titre("B. Fuite par les corrections : combien de prises pour apprendre ce que suit l'audit")
print("L'agent compare deux façons d'endommager. La première est auditée au plancher p0 ;")
print("la seconde à r * p0 (le soupçon s'ajoute au plancher). Il n'observe que « corrigé ou")
print("non ». Taille par bras pour un test unilatéral de deux proportions, risques 0,05 et")
print("0,05 (approximation normale) ; puis nombre attendu d'épisodes pris pendant l'essai.")
print()
print("   p0     r    par bras   épisodes endommagés   prises attendues")


def taille(p1, p2, a=0.05, b=0.05):
    pb = (p1 + p2) / 2
    num = Z(1 - a) * sqrt(2 * pb * (1 - pb)) + Z(1 - b) * sqrt(p1 * (1 - p1) + p2 * (1 - p2))
    return ceil((num / (p1 - p2)) ** 2)


for p0 in (0.01, 0.05, 0.20):
    for r in (1.0, 1.25, 1.5, 2.0, 5.0):
        p1 = min(r * p0, 1.0)
        if r == 1.0:
            print(f"  {p0:4.2f}  {r:4.2f}   jamais (taux égaux : rien à apprendre ; objet de contrôle)")
            continue
        n = taille(p1, p0)
        print(f"  {p0:4.2f}  {r:4.2f}   {n:8d}   {2 * n:19d}   {n * (p1 + p0):16.1f}")

print()
print("Règle d'alarme : arrêt à la K-ième prise. Probabilité que l'agent termine son essai")
print("(2n épisodes endommagés) avec moins de K prises ; loi exacte (deux binomiales).")


def binom_pmf(n, p):
    # récurrence stable, sans grands entiers
    pmf = [0.0] * (n + 1)
    pmf[0] = (1 - p) ** n
    for k in range(1, n + 1):
        pmf[k] = pmf[k - 1] * (n - k + 1) / k * p / (1 - p)
    return pmf


def proba_moins_de(K, n, p1, p2):
    a = binom_pmf(n, p1)[:K]
    b = binom_pmf(n, p2)[:K]
    tot = 0.0
    for i, ai in enumerate(a):
        tot += ai * sum(b[: K - i])
    return tot


print("   p0     r     K=1        K=3        K=10")
for p0, r in ((0.01, 2.0), (0.05, 2.0), (0.05, 5.0), (0.20, 2.0)):
    n = taille(r * p0, p0)
    print(f"  {p0:4.2f}  {r:4.2f}  " + "  ".join(f"{proba_moins_de(K, n, r * p0, p0):9.2e}" for K in (1, 3, 10)))

# --------------------------------------------------------------------------
# Bloc C — l'accord entre copies : ce qu'il mesure
# --------------------------------------------------------------------------
titre("C. Accord entre deux copies : accord brut, accord corrigé, ancres")
print("Monde jouet : par épisode, un fait binaire w tiré à pile ou face par le défenseur.")
print("Honnête : rapporte w avec exactitude a, erreurs indépendantes entre copies.")
print("Mensonge focal : les deux copies rapportent 1 quel que soit w.")
print("Mensonge cohérent : les deux copies rapportent 1 - w (même fonction de la pièce).")
print("Accord brut = P(mêmes rapports sur le même épisode).")
print("Accord corrigé = accord sur le même épisode - accord entre deux épisodes différents.")
print()
print("    a    stratégie            brut   entre épisodes   corrigé")
for a in (0.95, 0.90, 0.80, 0.70):
    brut_h = a * a + (1 - a) * (1 - a)
    # rapport honnête : P(1) = 1/2 par symétrie, donc accord entre épisodes = 1/2
    print(f"  {a:4.2f}  honnête            {brut_h:6.3f}   {0.5:14.3f}   {brut_h - 0.5:7.3f}")
print(f"   --   mensonge focal     {1.0:6.3f}   {1.0:14.3f}   {0.0:7.3f}")
print(f"   --   mensonge cohérent  {1.0:6.3f}   {0.5:14.3f}   {0.5:7.3f}")
print()
print("Lecture : l'accord brut classe les deux menteurs au-dessus de l'honnête ; l'accord")
print("corrigé met le mensonge focal à zéro, mais laisse le mensonge cohérent au-dessus")
print("de tout honnête imparfait. Seules des ancres (épisodes dont le défenseur connaît w)")
print("le séparent : exactitude sur ancre, honnête a, focal 1/2, cohérent 0.")
print()
print("Nombre d'ancres m pour séparer honnête (a) et mensonge cohérent, règle « au moins")
print("la moitié des ancres justes » : risque de condamner l'honnête (loi binomiale exacte).")
print("    a     m=3       m=5       m=9")
for a in (0.90, 0.80, 0.70):
    ligne = []
    for m in (3, 5, 9):
        seuil = (m + 1) // 2
        p_echec = sum(comb(m, k) * a ** k * (1 - a) ** (m - k) for k in range(0, seuil))
        ligne.append(f"{p_echec:8.4f}")
    print(f"  {a:4.2f}  " + "  ".join(ligne))
print("(le mensonge cohérent a 0 ancre juste : toujours pris par cette règle)")

# --------------------------------------------------------------------------
# Bloc D — combien de témoins indépendants valent n copies
# --------------------------------------------------------------------------
titre("D. Témoins indépendants équivalents à n copies corrélées")
print("n_eq = n / (1 + (n - 1) * rho) ; limite 1 / rho quand n grandit.")
print("rho = 0,435 et 0,480 : corrélations estimées sur des tirages réels d'un même modèle,")
print("lues en page 1 de la source citée dans la note (Agbeyegbe et Agbeyegbe).")
print("   rho     n=2     n=5    n=10   n=100   limite")
for rho in (0.0, 0.435, 0.480):
    vals = [n / (1 + (n - 1) * rho) for n in (2, 5, 10, 100)]
    lim = "infini" if rho == 0 else f"{1 / rho:6.2f}"
    print(f"  {rho:5.3f}  " + "  ".join(f"{v:6.2f}" for v in vals) + f"   {lim}")
print("(rho = 0 : objet de contrôle, n copies valent n témoins)")
