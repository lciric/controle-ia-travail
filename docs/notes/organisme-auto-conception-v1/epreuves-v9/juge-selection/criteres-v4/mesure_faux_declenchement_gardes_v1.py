# -*- coding: utf-8 -*-
"""Taux de faux déclenchement des gardes par espèce, sur des mondes SYNTHÉTIQUES sans effet — v1.

Soixante mondes inventés (graines 100 à 159 de l'essai), 90 cartes, espèces sans lien avec les
réponses ; mille permutations par test. Aucune vraie carte. Usage :
  python3 -B mesure_faux_declenchement_gardes_v1.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import essais_assemblage_selection_v4_v1 as E  # noqa: E402

mondes, items, ecarts, retours = 60, 0, 0, 0
for graine in range(100, 100 + mondes):
    lf, lo, esp = E.monde(n=90, graine=graine)
    _, g = E._gardes(lf, lo, esp, n_perm=1000)
    items += bool(g["items_nommes"])
    ecarts += bool(g["ecarts_forts"])
    retours += bool(g["retour_a_lazar_avant_adoption"])
print(f"mondes sans effet : {mondes} ; permutations par test : 1000")
print(f"mondes avec au moins un item nommé (garde 1) : {items}")
print(f"mondes avec au moins un écart fort (garde 2) : {ecarts}")
print(f"mondes avec retour à Lazar : {retours}")
