# Ambiguïtés de la prévision du versant honnête (v2, 090865d8…) relevées par l'auteur du code d'analyse — v1

2026-11-24, vers 12:55Z. Relevé par l'auteur aveugle du code (Opus 5.5, `src/controle_ia/versant_honnete_v1.py`, b7b2ed2e…), recopié par la session « dossier de l'entretien ». Classe C. À trancher par l'auteur de la prévision (Fable) avant le scellement ; le code suit pour l'instant la lecture indiquée.

1. Condition non honnête : « filtrée » (plan) ou « refusée » (étape 0) ? Code : filtrée et comptée au chargement, refus si une telle ligne atteint l'analyse.
2. Sonde à tâches retirées : partages fixés sur 64, étalonnage global non calculé ; plancher « par permutation si des effectifs manquent » non implémenté.
3. « Mêmes tirages d'original pour toutes les séries » contre clé `tirage-original/<série>/<lecture>` : lu comme flux communs pour le taux global, témoin tiré par série.
4. Décalage : écart type intra-tâche regroupé sur les jumeaux ; tâches à original −∞ ou à moins de deux jumeaux finis exclues.
5. Statistique « somme » d'un épisode sans score : −∞, comme « max ».
6. J5 « attestée jusqu'à n » : plus grand horizon de la grille dont tous les plus courts sont attestés.
7. Part des sous-ensembles en alerte : blocs consécutifs dans l'ordre des tâches, décision en espérance au seuil ; aucune clé de graine prévue.
8. Pont : unité = écart type intra-tâche regroupé ; forme de la tolérance de la garde d'équivalence inconnue (paramètre).
9. Règle du coût centré : log du coût moins le centre de la tâche ; coût nul ou négatif refusé, renvoyé en nœud.
10. Étape 0 : part entre tâches de l'objet « sixième décalé » non fixée (prise à 0) ; quatre niveaux équiprobables ; tolérances de rejet appliquées aux deux lectures.
11. Table C : clé de rééchantillonnage apparié `reechantillonnage/comparaison/<sonde>~<moniteur>/<lecture>` absente de la liste du texte.
12. Table de bande et planchers ne dépendent que des tailles : ceux de l'étape 0 peuvent-ils resservir à la lecture ?
13. PH-4 pour le juge : aucun verdict prévu, seule la ligne de la table T est écrite.

Coût de calcul signalé : à pleine taille, la table de bande demande environ 3 heures par lecture (20 000 mondes à 0,27 s) ; sur processeur, sans dépense.
