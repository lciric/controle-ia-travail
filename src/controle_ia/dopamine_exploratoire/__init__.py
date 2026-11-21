"""Bras « papier dopamine », mode EXPLORATOIRE (GO-2026-11-21-44) : rejeu de la sonde de réussite attendue du papier
arXiv 2602.00986v2 (étape 1, MATH500, couches 2 à 4) et pré-mesure sur épisodes honnêtes (étape 2a, couches 7, 15, 23).

Sans préenregistrement ni contre-lecture : toute sortie porte « exploratoire » dans son manifeste, n'est pas opposable et ne
fonde aucun verdict ni aucune porte. Restent en vigueur R5 (chaque garde éprouvée sur un cas sain et sur un artefact), R9
(graines par `numpy.random.SeedSequence`, manifeste par course), R10 (arrêt par identifiant), R12 (rien n'est écrasé).

Modules :
- `math500_v1` : invite « qwen-boxed », lecture du jeu, vérificateur de réponse en boîte ;
- `generation_v1` : recette du tableau 6 (p. 19), générateurs (vLLM sur la machine, transformers ailleurs), écriture par
  lots scellés, reprise après coupure ;
- `etats_v1` : états internes aux couches demandées, au dernier jeton de l'énoncé et à toutes les positions de la réponse,
  float16 sur disque, scellés par lot ;
- `sonde_v1` : sonde de réussite attendue par différence temporelle (équations 8 et 9, p. 4 ; tableau 7, p. 19), aire sous
  la courbe, grille des quinze taux d'élagage (tableau 8, p. 20) ;
- `mesures_2a_v1` : fonctions pures de l'étape 2a ;
- `course_v1` : la chaîne de bout en bout, manifeste « exploratoire » ;
- `jouet_v1` : modèle jouet minuscule (processeur) et son découpeur, pour les essais ;
- `lanceur_v1` et `amorce_v1.sh` : machine A100 du loueur ; le lanceur IMPRIME les commandes, il ne lance rien.
"""
MODE = "exploratoire"
GO_REOUVERTURE = "GO-2026-11-21-44"
PAPIER = {"arxiv": "2602.00986v2", "pdf": "docs/sources/pdf/2602.00986v2.pdf"}
