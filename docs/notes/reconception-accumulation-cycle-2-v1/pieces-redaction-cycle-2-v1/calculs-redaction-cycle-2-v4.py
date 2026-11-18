"""Arithmétique du rédacteur du second cycle (accumulation des scores sur l'épisode) — v4, complément.

Ne porte qu'une section 10 : l'arithmétique de la règle de réplication, écrite dans le préenregistrement
(« Suite des cycles ») et absente de toute sortie scellée (remarque m-6 de la contre-lecture des brouillons 4).
Les sections 1 à 9 restent celles de la v3, qui n'est ni reprise ni remplacée ici (R12).
Ce sont des formules : aucune donnée lue, aucune analyse. Bibliothèque standard.
Lancement : python3 calculs-redaction-cycle-2-v4.py
"""
NIVEAU = 0.025  # niveau annoncé d'un cycle pour « accumuler, propre » (préenregistrement, « Seuil »)

print("== 10. Regle de replication : bornes sous un nul commun a tous les cycles (formules, aucun chiffre lu)")
print("   (a) au moins une issue positive en K cycles, sans replication : au plus 1 - (1 - 0,025)^K")
for k in (1, 2, 3, 4, 5, 10, 20, 40):
    print(f"      K = {k:2d} : {1 - (1 - NIVEAU) ** k:.4f}")
print("   (b) une issue positive fortuite puis repliquee par hasard, replication lue au meme niveau,")
print("       lectures independantes : au plus K x 0,025^2 (borne de la reunion sur les K cycles)")
for k in (1, 2, 3, 4, 5, 10, 20, 39, 40, 41):
    print(f"      K = {k:2d} : {k * NIVEAU ** 2:.6f}")
# K x 0,025^2 <= 0,025 si et seulement si K <= 1 / 0,025 ; arithmétique entière pour éviter l'arrondi flottant
k_max = 1000 // 25
assert k_max * 25 * 25 == 25 * 1000 and (k_max + 1) * 25 * 25 > 25 * 1000
print(f"   (c) la borne (b) reste au plus egale a 0,025 jusqu'a K = {k_max} (egalite a K = {k_max} ; strictement sous 0,025 jusqu'a K = {k_max - 1})")
print("   hypotheses de (a) et (b) : nul commun a tous les cycles ; pour (b), lectures independantes et meme niveau")
