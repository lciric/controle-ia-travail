"""Harnais d'épisodes et de journalisation des activations (T0.4).

Modules : `modeles` (modèle et tokeniseur jouets hors ligne, liste blanche des modèles réels, réglages de
déterminisme), `activations` (crochets sur le flux résiduel, passe avant unique, agrégation max ou
dernier jeton, garde d'équivalence), `episode` (épisodes indexés par agent et par pas, génération à
graine explicite, empreintes de rejeu), `stockage` (estimation), `run_harnais_factice` (bout en bout).
"""
