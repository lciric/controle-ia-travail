# « Accounting for Variance in Machine Learning Benchmarks » — fiche de lecture (passe v2)

Convention : « p. N » désigne le rang de la page dans le fichier PDF empreinté, à partir de 1.

## Référence
- Xavier Bouthillier, Pierre Delaunay, Mirko Bronzi, Assya Trofimov, Brennan Nichyporuk, Justin Szeto, Naz Sepah, Edward Raff, Kanika Madan, Vikram Voleti, Samira Ebrahimi Kahou, Vincent Michalski, Dmitriy Serdyuk, Tal Arbel, Chris Pal, Gaël Varoquaux, Pascal Vincent. « Accounting for Variance in Machine Learning Benchmarks ». Prépublication arXiv 2103.03098, version 1 du 1er mars 2021 (seule version) — page de résumé arXiv enregistrée le 26 octobre 2026 à 03:44 UTC, commentaire « Submitted to MLSys2021 ».
- Lieu : incohérence à signaler. Le pied de page du PDF porte « Proceedings of the 3rd MLSys Conference, Austin, TX, USA, 2020 » (p. 1), vraisemblablement le gabarit ; le PDF de Agarwal et al. (lu) le cite comme « Proceedings of Machine Learning and Systems, 3, 2021 » (p. 12 de ce PDF-là). Conférence Machine Learning and Systems 2021, volume 3 : à vérifier sur les actes.

## Fichier lu
- `pdfs/variance-benchmarks/arxiv-2103.03098v1.pdf`, 1 086 614 octets, 23 pages ; SHA-256 `1f458f7e606e4db86b207315c049a38b52cacde15ad34def2cc6c29124fc5d4c` (même empreinte que la v1).
- Pages lues : 1 à 11 (corps du texte), 14 à 17 (annexes B et C : rééchantillonnage, procédure de test complète). Autres annexes non lues.

## Comment la boucle est faite
- Pas de système de boucle : la comparaison de deux chaînes d'apprentissage A et B. Le processus de comparaison est modélisé comme une variable aléatoire qui inclut l'échantillonnage des données, l'augmentation de données, l'initialisation, l'abandon aléatoire de neurones, l'ordre de visite des données et l'optimisation des hyperparamètres (p. 2 et 3).
- Cinq études de cas (images, segmentation, deux tâches de langue, liaison peptidique), environ 8 années de processeur graphique de calcul (p. 3).

## Traitement du bruit et du sur-ajustement
- Décomposition de la variance (p. 3 et 4) : chaque source rendue aléatoire 200 fois, les autres fixées ; 200 courses à graines toutes fixées pour le bruit numérique ; 20 optimisations d'hyperparamètres indépendantes de 200 essais (p. 4). Le rééchantillonnage des données « stands out » comme première source ; l'initialisation pèse en général moins de 50 % de cette variance (p. 4).
- Le bruit d'échantillonnage du jeu de test est bien décrit par un modèle binomial (p. 4) ; la variance totale est du même ordre que les améliorations publiées (p. 5).
- Estimateurs : l'estimateur idéal refait l'optimisation des hyperparamètres à chaque découpage ; l'estimateur biaisé la fait une fois mais rend aléatoires toutes les autres sources, ce qui le rapproche de l'idéal pour un coût 51 fois moindre (p. 1 et 9) ; 1 070 heures contre 21 heures dans leur cas (p. 7).
- Critères de décision simulés (p. 8 et 9) : comparer une seule course de chaque côté donne environ 10 % de faux positifs et 75 % de faux négatifs ; comparer des moyennes sur 50 découpages, moins de 5 % de faux positifs mais environ 90 % de faux négatifs ; leur critère — probabilité que A batte B sur une course, P(A>B), avec intervalle par bootstrap, borne basse au-dessus de 0,5 et borne haute au-dessus d'un seuil γ = 0,75 — donne environ 5 % de faux positifs et 30 % de faux négatifs (p. 9).
- Taille d'échantillon : pour γ = 0,75 et 5 % de faux négatifs, 29 entraînements suffisent ; détecter P(A>B) sous 0,6 demande plus de 500 entraînements (p. 16). Appariement des courses de A et B sur les mêmes graines et découpages pour gagner en puissance (p. 15).
- Recommandations (p. 2, 9 et 10) : rendre aléatoires autant de sources que possible ; préférer plusieurs découpages aléatoires (hors-bootstrap) à un jeu de test fixe ; tenir compte de la variance pour conclure.

## Échecs et limites rapportés par les auteurs
- Le cadre ne s'applique pas quand les modèles sont donnés (achetés par une interface de programmation, concours) et que seule varie la donnée de test (p. 10).
- Avec beaucoup de concurrents, la correction de comparaisons multiples (Bonferroni) devient « stringent » et le choix du gagnant garde une part d'arbitraire (p. 10) ; avec 3 à 5 jeux de données, les tests entre jeux ont une puissance très faible (p. 10).
- Avec l'estimateur biaisé, « we cannot guarantee a nominal control » des erreurs (p. 9) ; le seuil γ = 0,75 est calé sur leurs cinq études de cas (p. 9 et 10).

## Vérifié par des tiers
- Non trouvé. Agarwal et al. (lu) reprennent son critère de probabilité d'amélioration (p. 25 de leur PDF) sans le revérifier.

## À emprunter
- Boucle extérieure : critère P(A>B) ≥ γ fixé d'avance, avec intervalle et appariement des générations sur les mêmes graines et découpages (p. 9, 15 et 16).
- Boucle intérieure : quand l'organisme compare deux variantes, rendre aléatoire tout ce qui n'est pas testé (graines, ordre des tâches, découpage) plutôt que tout fixer ; cela réduit la corrélation entre mesures (p. 6 et 9).
- Mesure du bruit : l'erreur type de 0,07 du brief est exactement le bruit binomial d'échantillonnage du jeu de test qu'ils décrivent (p. 4) ; leur recommandation est de rééchantillonner les découpages plutôt que de garder une part `test` fixe (p. 10). Réserve : la part de la variance due au modèle sous-jacent, s'il est servi par une interface, sort de leur cadre (p. 10).
