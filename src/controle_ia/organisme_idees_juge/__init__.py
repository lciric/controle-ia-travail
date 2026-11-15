"""Organisme d'idéation, juge : code qui joue le préenregistrement scellé de l'idée 1.2 (tirages frais répartis par blocs
avec arrêt anticipé, contre la part fixe), `prereg/organisme-idee-1-2-tirages-repartis-arret-anticipe-v4.md`
(`bdabf2bc…`, R-2886).

Modules (version 1) :
- `juge_v1` : accès en lecture seule, par import empreinté, à la copie `94bfd92` du juge (aucun fichier n'y est exécuté
  comme programme ; aucun fichier de code compilé n'y est écrit) ;
- `lois_v1` : évaluateur vectorisé des lois du banc (pour l'oracle et la règle du cosinus seulement), constructeurs,
  composantes V1 à V5 ;
- `banc_tirages_repartis_v1` : banc B v2 (archive A2, mondes, cartes des familles T et N, graines), plans, gel,
  issues fraîches, évaluation par le juge réel, rapport exact Λ, essai E1 ;
- `oracle_v1` : oracle des fausses promotions (20 000 instances par génération), classes ;
- `rejeu_v1` : bras F, F-arrêt, A, P, P′, F125, G ; garde d'accès ; garde du budget ; valeurs e ; règle e-BH ;
  vérificateur indépendant de l'allocation ;
- `synthetique_v1` : jeu d'essai synthétique de 20 000 générations (réserve (a) de la Métrique) ;
- `lire_banc_tirages_repartis_v1` : lecture gelée (étages 1 à 5, prédictions Q1 à Q9, éléments de l'audit R4) ;
- `mutations_v1` : banc de mutations exigé par l'étape 0 ;
- `execution_v1` : enchaînement du jeu (contrôles avant jeu, E1, oracle scellé, jeu, sortie scellée), gardes de durée
  et de réseau, répétition miniature.
"""

VERSION = "organisme-idees-juge-idee-1-2-v1"
