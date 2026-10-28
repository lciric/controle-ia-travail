# « Deep Reinforcement Learning at the Edge of the Statistical Precipice » — fiche de lecture (passe v2)

Convention : « p. N » désigne le rang de la page dans le fichier PDF empreinté, à partir de 1.

## Référence
- Rishabh Agarwal, Max Schwarzer, Pablo Samuel Castro, Aaron Courville, Marc G. Bellemare. « Deep Reinforcement Learning at the Edge of the Statistical Precipice ». 35e conférence Neural Information Processing Systems, 2021 (pied de page, p. 1) ; prix « Outstanding Paper Award » (note p. 1 et commentaire arXiv).
- Prépublication arXiv 2108.13264, version 4 du 5 janvier 2022 (version 1 du 30 août 2021) — page de résumé arXiv enregistrée le 26 octobre 2026 à 03:44 UTC.

## Fichier lu
- `pdfs/rl-precipice/arxiv-2108.13264v4.pdf`, 22 838 819 octets, 28 pages ; SHA-256 `a6a5abb49e58a9e4a0be8556c8351ce8c3b52e70216bffc9fa80eac0823ec5ed` (même empreinte que la v1).
- Pages lues : 1 à 11 (corps du texte), 18 (graines et non-déterminisme), 25 (probabilité d'amélioration) ; les autres annexes ne sont pas lues.

## Comment la boucle est faite
- Pas de système de boucle : la boucle est celle d'un domaine qui compare des algorithmes d'apprentissage par renforcement sur des suites de tâches avec peu de courses ; 3 à 10 courses par tâche sont la norme (p. 2).
- Étude de cas (benchmark Atari 100k, 26 jeux) : 100 courses indépendantes par algorithme, puis sous-échantillonnage de 3 à 100 courses pour mesurer la variabilité des estimations ponctuelles publiées (p. 4).

## Traitement du bruit et du sur-ajustement
- Recommandations (tableau 1, p. 3) : intervalles de confiance par bootstrap stratifié (rééchantillonnage des courses à l'intérieur de chaque tâche) sur les scores agrégés (p. 6) ; profils de performance, c'est-à-dire la distribution des scores de toutes les courses, avec bandes de confiance (p. 6 et 7) ; moyenne interquartile (moyenne des 50 % centraux des courses) plutôt que médiane ou moyenne (p. 7) ; écart à l'optimalité et probabilité moyenne d'amélioration (p. 8).
- Constats chiffrés : pour des intervalles étroits sur la médiane, il faudrait plutôt 50 à 100 courses (p. 5) ; avec la médiane et à effet nul, même 100 courses laissent possibles des écarts de 20 % (p. 5) ; dans un exemple, le biais de la médiane d'échantillon (écart entre 5 et 100 courses) vaut environ 36 % de l'amélioration revendiquée (p. 5) ; les intervalles par percentiles sont bons dès 10 courses mais sous-couvrent avec 3 (p. 6) ; beaucoup d'améliorations publiées ne sont « only 50 − 70% likely » (p. 10) ; sur la suite de contrôle continu, la plupart des améliorations annoncées ne tiennent pas une fois l'incertitude prise en compte (p. 9).
- Les auteurs déconseillent les tests de signification dichotomiques (p. 4) et notent que changer de protocole d'évaluation invalide les comparaisons (p. 5).
- Graines : fixer les graines ne règle pas le problème et peut avantager certains algorithmes (p. 10) ; elles ne garantissent pas des résultats déterministes sur processeurs graphiques (note p. 2 ; p. 18).

## Échecs et limites rapportés par les auteurs
- Trouver la meilleure mesure agrégée reste « an open question » (p. 8) ; le classement des algorithmes change avec la mesure choisie (p. 8).
- Avec 3 courses, le bootstrap sous-estime l'incertitude et demanderait un taux de couverture nominal plus élevé (p. 6).
- Obstacle d'incitation : plus de rigueur donne des revendications plus prudentes (p. 10).

## Vérifié par des tiers
- Non trouvé dans les lectures de cette passe. Le papier s'appuie sur le critère de Bouthillier et al. (lu) pour qualifier ses probabilités d'amélioration (p. 25) ; c'est un emprunt, pas une vérification.

## À emprunter
- Boucle extérieure : rendre des intervalles sur les scores agrégés et une probabilité d'amélioration, jamais une estimation ponctuelle seule ; geler le protocole d'évaluation d'une génération à l'autre (p. 3, 5 et 8).
- Boucle intérieure : une primitive qui compare deux variantes sur une seule course chacune ne distingue rien ; au minimum un bootstrap stratifié par tâche, et plusieurs courses dès que le budget le permet (p. 6).
- Mesure du bruit : mesurer la variance entre graines par une étude dédiée (le brief la dit inconnue) avant de fixer le nombre de courses par objet ; 10 courses est le seuil à partir duquel leurs intervalles par percentiles couvrent correctement (p. 6).
