# « AIDE: AI-Driven Exploration in the Space of Code » — fiche de lecture (passe v3, ajouté)

Convention : « p. N » désigne le rang de la page dans le fichier PDF empreinté, à partir de 1.

## Référence
- Zhengyao Jiang, Dominik Schmidt, Dhruv Srikanth, Dixing Xu, Ian Kaplan, Deniss Jacenko, Yuxiang Wu. « AIDE: AI-Driven Exploration in the Space of Code ». Weco AI et Runway ML (p. 1).
- Prépublication arXiv 2502.13138, version 1 du 18 février 2025 (tampon, p. 1). Lieu : aucun indiqué sur le PDF. Marqué « ajouté » par la v1.

## Fichier lu
- `pdfs/ajout-aide/arxiv-2502.13138v1.pdf`, 648 632 octets, 17 pages ; SHA-256 `5fc52573eab9c8cb568b0c5aab6ee75752d198504babf8278ad23fe3d542cb41` (même empreinte que la v1).
- Pages lues : 1 à 10 (texte) ; annexes (p. 11 à 17) parcourues.

## Comment la boucle est faite
- Cadre : optimiser une solution (un script) contre une fonction objectif sans état, par exemple l'exactitude de validation (p. 2).
- Toutes les solutions forment un arbre (p. 3). Une politique de recherche codée en dur choisit entre :
  - écrire un brouillon tant que le nombre de solutions initiales n'est pas atteint ;
  - déboguer un nœud défectueux, dans une profondeur limitée ;
  - améliorer, en général la meilleure solution.
- Qui propose : un modèle de langue, qui fait un seul changement « atomique » par amélioration pour que son effet soit mesurable (p. 2 et 4).
- Mémoire : un opérateur de résumé extrait de l'arbre les scores, les réglages et les indices de débogage (p. 4).
- Qui teste : l'évaluateur ; AIDE crée lui-même une séparation entraînement/validation pour noter ses nœuds (p. 5).

## Traitement du bruit et du sur-ajustement
- Protocole des auteurs sur 16 concours Kaggle tabulaires (p. 5) :
  - avant toute course, les données d'entraînement sont séparées en une part pour l'agent et une part de test tenue à l'écart, distincte de la validation interne d'AIDE ;
  - l'agent voit les entrées du test mais pas les étiquettes ;
  - le score est un quantile sur le classement Kaggle, privé quand il existe, parce qu'il est « less prone to overfitting by competitors » (p. 5).
- Résultats de MLE-Bench repris de Chan et al. (p. 7) : 3 graines par expérience, sauf AIDE avec o1-preview (16) et AIDE avec GPT-4o (36) ; moyenne ± erreur type.
- Sur MLE-bench Lite, o1-preview avec AIDE contre o1-preview seul (p. 8) :
  - soumissions valides : de 63,6 % à 92,4 % ;
  - au-dessus de la médiane humaine : de 13,6 % à 59,1 % ;
  - médailles : de 7,6 % à 36,4 % ;
  - p < 0,01 par test t bilatéral.
- Avec plus d'essais par concours (meilleur de 6 au lieu de 1), les médailles doublent presque (p. 8). C'est une sélection sur plusieurs tentatives.
- Les auteurs notent que la recherche d'hyperparamètres par force brute risque « overfitting to the validation set » (p. 1).

## Échecs et limites rapportés par les auteurs
- Leur part de test diffère de la part privée de Kaggle, d'où de la variance dans les quantiles. Contamination possible des modèles par les données des concours : pas de corrélation significative avec la date des concours, mais seule la soumission à des concours en cours l'exclurait (p. 7).
- Sur RE-Bench (évaluation METR), AIDE dépasse des experts humains en six heures, mais ceux-ci le rattrapent : la politique gloutonne peut rester bloquée dans des optima locaux. Il échoue là où il faut manier une grosse base de code ou enchaîner plusieurs étapes pour une amélioration ; dans un environnement, il répète des correctifs locaux au lieu de changer de stratégie (p. 9).

## Vérifié par des tiers
- Les auteurs reprennent des évaluations faites par d'autres (MLE-Bench par Chan et al., RE-Bench par METR), non lues ici (p. 4, 5, 7 à 9). AIRA (lu) réimplémente AIDE et mesure 10,68 points de plus que les résultats publiés dans son propre environnement (p. 2 de son PDF). Agent Laboratory (lu) le compare à son « mle-solver » (p. 19 de son PDF).

## À emprunter
- Boucle extérieure : trois niveaux de données — validation interne de l'agent, part de test tenue à l'écart par l'évaluateur, part privée — avec un score comparable entre tâches (quantile) (p. 5).
- Boucle intérieure : un changement atomique par variante, pour que son effet soit mesurable (p. 4).
- Mesure du bruit : le « meilleur de k » gonfle les taux de réussite (p. 8) ; annoncer toujours le k.
