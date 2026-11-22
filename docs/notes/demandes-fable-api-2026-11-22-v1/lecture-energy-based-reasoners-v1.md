# Lecture : « Energy-Based Reasoners: Your Recurrent Reasoner Should Be an Energy-Based Model » (agent de lecture ; statut : rapporté, lecture partielle)

Auteurs : William Xingxu Chen, Alexi Gladstone, Zeyu Michael Li, Heng Ji, Yilun Du. arXiv:2611.08977, 6 novembre 2026, cs.LG. HTML lu jusqu'au milieu de la section 3.3 ; le reste par résumé.
Question : faire du raisonnement récurrent par descente de gradient sur une énergie apprise, de sorte que l'énergie serve à arrêter, à choisir entre candidats et à trouver plusieurs solutions valides.
Méthode : modèle récurrent avec tête d'énergie scalaire ; l'état latent descend le gradient de l'énergie ; arrêt par la norme du gradient, sans tête d'arrêt entraînée ; exploration par K trajectoires parallèles dont une seule supervisée par segment.
Résultats (résumé de la page) : 99,9 % sur Sudoku-Extreme avec 345 fois moins de calcul d'inférence que le meilleur modèle suivant ; couverture de solutions valides meilleure que l'état de l'art sur les bancs à solutions multiples. Chiffres de tableaux non vérifiés (lus par résumé) : Maze-Hard 87,4 à 88,3 % ; N-Queens 10x10 couverture 57,5 % à 92,0 %.
Limites : coût (dérivées du second ordre), nombreux réglages, raisonnement algorithmique structuré seulement ; aucune question de sécurité ni d'agents.
Code annoncé : github.com/wwillchen/ebr (licence non vérifiée) ; article CC BY 4.0.
Déduction de l'agent : la norme du gradient d'énergie ou le résidu de convergence pourrait servir de signal de surveillance de l'état latent ; à valider sur des modèles de langue.

# Non lus
- Article de l'IOP, DOI 10.1088/3050-287X/aeb27b : page refusée (403) ; recherche en cours.
- « Symmetry in language statistics shapes the geometry of model representations » (Karkada, Korchinski, Nava, Wyart, Bahri) : connu par la capture d'écran du directeur (résumé) : les statistiques de co-occurrence de la langue ont une symétrie de translation (la fréquence de co-occurrence de deux mois ne dépend que de leur écart), et cette symétrie gouverne les structures géométriques (mois en cercle, années en variété unidimensionnelle « ondulée », coordonnées décodables par sonde linéaire) ; prédictions analytiques vérifiées sur des modèles de plongement et des grands modèles de langue ; la géométrie persiste quand on perturbe les statistiques ; robustesse quand les co-occurrences sont contrôlées par une variable latente. Recherche du texte en cours.
