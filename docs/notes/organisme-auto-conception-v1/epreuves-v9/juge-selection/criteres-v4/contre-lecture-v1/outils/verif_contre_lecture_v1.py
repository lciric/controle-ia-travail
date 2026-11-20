# -*- coding: utf-8 -*-
"""Vérifications du contre-lecteur (modèle O) — v1. Données synthétiques et calcul exact seulement.

1. Mondes synthétiques des essais : graines 7, 8, 11 sans effet planté — qui déclenche, et quoi ?
2. Seuils atteignables d'une liste courte (hypergéométrique non stratifiée, base 37 sur 94) :
   ce que Holm sur douze tests et un seuil brut de 0,025 laissent passer.
Usage : python3 -B verif_contre_lecture_v1.py DOSSIER_DES_COPIES
"""
import math
import sys

sys.path.insert(0, sys.argv[1])
import essais_assemblage_selection_v4_v1 as E  # noqa: E402


def p_bilaterale(n, k_obs, N=94, F=37):
    tot = math.comb(N, n)
    loi = {k: math.comb(F, k) * math.comb(N - F, n - k) / tot for k in range(0, n + 1)}
    att = n * F / N
    return sum(p for k, p in loi.items() if abs(k - att) >= abs(k_obs - att) - 1e-12)


print("== 1. mondes sans effet planté (n = 90), 400 et 2000 permutations ==")
for graine in (7, 8, 11):
    for n_perm in (400, 2000):
        lf, lo, esp = E.monde(n=90, graine=graine)
        _, g = E._gardes(lf, lo, esp, n_perm=n_perm)
        print(f"graine {graine}, {n_perm} permutations : retour = {g['retour_a_lazar_avant_adoption']} ; "
              f"items nommés = {g['items_nommes']} ; écarts forts = {g['ecarts_forts']}")

print("== 2. liste courte, base 37 sur 94, p exacte bilatérale ==")
for n in (3, 4, 5, 6, 9):
    for k in range(n + 1):
        p = p_bilaterale(n, k)
        print(f"n = {n}, k = {k} : p = {p:.5f} ; <= 0,05/12 = {p <= 0.05 / 12} ; <= 0,025 = {p <= 0.025}")
