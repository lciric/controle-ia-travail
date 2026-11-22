"""Pilote « oracles plantés » du pilier des mathématiques nouvelles — lot B1, code figé, version 6 : changements exigés par le brouillon 3 du préenregistrement (`e33d7bec…`, § Mondes plantés et tests de mort).

Générateur de mondes plantés (trois familles, quatre mondes chacune), grammaire fermée d'énoncés,
évaluateur exact (rationnels, aucun flottant), normaliseur, six tests de mort, registre de lignée,
scellement des clés, base « grammaire aléatoire », sous-banque des bras S et N, rejeu sans appel.

Ce code tourne chez la mère ou son conteneur de confiance, jamais sur une machine louée ; il ne
contient aucun appel de modèle. Bornes et tailles : gelées par le brouillon 3 (`parametres_v6.json`) ;
la liste « provisoire » de ce fichier dit ce qui reste à l'exécutant.
"""
VERSION = "oracles_plantes_v6"
