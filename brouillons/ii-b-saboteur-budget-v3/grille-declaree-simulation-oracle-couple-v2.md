EXPLORATOIRE, NON OPPOSABLE (R-522)

# Complément de grille, déclaré avant le passage v2 de la simulation de l'oracle couplé

Écrit le 2026-11-19T11:49:02Z, après la lecture de la sortie v1 (`sortie-simulation-oracle-couple-ii-b-v1.txt`, données synthétiques seulement) et avant tout passage du script v2 (`simulation-oracle-couple-ii-b-v2.py`, empreinte : 77c59da0c0dc77b9acdc4ba0f32591ac3718beb138c667c0831ef46d0031cb6e), qui n'a été passé à aucun effectif avant cette écriture.

**Ce que la sortie v1 a montré.** Avec les illisibles rangés en bas, l'excès honnête moyen dérive entre le premier et le dernier pas (jusqu'à +0,27 décade pour le bloc de 4, contre +0,06 sans couplage) : quand le coût déclaré est illisible et qu'aucune suite ne l'est, le contexte réécrit reçoit la plus basse suite lisible, donc une ancre basse là où l'agent n'en a pas. C'est un défaut de ma définition, de même nature que celui corrigé dans la v2 (un contexte réécrit qui n'a pas la même part de coûts lisibles que celui de l'agent).

**Un seul changement** : la lisibilité de la suite de réécriture suit celle du coût déclaré (illisible → illisible ; lisible → voisine de rang parmi les suites lisibles). Tout le reste est celui de la grille v1 : mêmes cellules, mêmes saboteurs, mêmes candidats, mêmes règles de choix du bloc, de la statistique de chaîne et des constantes, mêmes branches, mêmes effectifs, mêmes niveaux. Entropie neuve. Les choix rendus par le passage v1 (bloc de 4, plancher 1,25) ne sont pas repris : le passage v2 les refait par les mêmes règles, et c'est lui qui fait foi.
