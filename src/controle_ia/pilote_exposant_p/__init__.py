"""Pilote préenregistré d'une journée : exposant p de la superellipse (Ferreira da Silva et Heimersheim, arXiv
2606.24964) pour le plan (évaluation, registre) sur Llama-3.1-8B-Instruct, version 1.

Modules :
- `amont` : copie déclarée, à l'identique, de deux fichiers du code publié (MIT) ;
- `references` : lecture restreinte des caches publiés et références sûres (npz, JSON) ;
- `stimuli` : fichier de stimuli figé, validation de ses règles de construction, paires ;
- `directions` : différences de moyennes, différences aléatoires, isotropes, cosinus et règle d'exclusion ;
- `balayage` : activations et balayage d'un plan à norme constante, par crochets sur le modèle complet ;
- `ajustement` : seuil par paire, contour, p, rééchantillonnages ;
- `analyse` : critères de lecture gelés, validation de l'instrument, audit de symétrie ;
- `puissance` : simulation de puissance sur superellipses synthétiques bruitées ;
- `ancres` : ancres FineWeb-edu (instance seulement) ;
- `run` : lanceur du run (instance seulement).
"""
VERSION = "pilote-exposant-p-v1"
