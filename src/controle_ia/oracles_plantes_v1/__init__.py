"""Pilote « oracles plantés » du pilier des mathématiques nouvelles — lot B1, code figé, version 1.

Générateur de mondes plantés (trois familles, quatre mondes chacune), grammaire fermée d'énoncés,
évaluateur exact (rationnels, aucun flottant), normaliseur, six tests de mort, registre de lignée,
scellement des clés, base « grammaire aléatoire », sous-banque des bras S et N, rejeu sans appel.

Ce code tourne chez la mère ou son conteneur de confiance, jamais sur une machine louée ; il ne
contient aucun appel de modèle. Les bornes, gabarits et tailles sont provisoires
(`parametres_provisoires_v1.json`) : ils seront fixés par le préenregistrement.
"""
VERSION = "oracles_plantes_v1"
