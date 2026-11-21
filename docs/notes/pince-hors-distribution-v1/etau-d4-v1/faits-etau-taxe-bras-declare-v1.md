# Faits : ce que cacher ses états internes à une sonde coûte à un agent, et la décision d'un programme sur la façon de le mesurer

## Le cadre

Un programme de recherche défensif surveille des agents d'IA, des modèles ouverts de quelques milliards de paramètres, sur de longues tâches. Il joint deux regards. Le regard externe juge le produit par un oracle (un programme, ou des lecteurs d'autres lignées de modèles), sans lire la prose de l'agent. Le regard interne est fait de sondes sur les activations de l'agent, à trois profondeurs, agrégées sur les jetons par maximum ou par attention, jamais par moyenne, puis accumulées d'une action à l'autre par une statistique séquentielle dont la fausse alerte est garantie. L'adversaire redouté nuit par accumulation de petits écarts. L'honnête échoue aussi : un épisode signalé est aiguillé (relancé, vérifié davantage, confié à un modèle de confiance), il n'incrimine pas.

L'« étau » est une hypothèse du programme : pour tromper le regard externe, l'agent doit dissimuler, et cet effort laisse une trace que le regard interne lit. Elle n'a jamais été mesurée.

## Ce que le programme tient pour acquis, ou envisage

- Une borne, par calcul et sans mesure. Un saboteur libre de cacher peut toujours ne rien cacher (il passe avec la probabilité 1 − r, où r est le rappel de la sonde quand rien n'est caché) ou tout cacher (il garde la part 1 − κ de sa compétence, où κ est la « taxe »). L'étau retire donc au plus le plus petit de r et de κ. Si tout cacher est hors d'atteinte, il reste un rappel plancher, seconde quantité à mesurer.
- Trois régimes d'attaquant, que le programme distingue : entraîné avec le gradient à travers la sonde (sur une entrée, ou sur les poids) ; entraîné par renforcement, sans ce gradient ; non entraîné (il improvise, ou apprend en contexte des verdicts qui lui reviennent).
- Un invariant de protocole : aucun score de moniteur n'entre dans l'entraînement ni dans la sélection d'un agent. Mesurer la taxe dans un bras d'attaque où un agent est entraîné contre une sonde demande donc une exception écrite.
- Une autre expérience du programme, déjà prévue pour une autre question, réemploie les codes publiés d'obscurcissement d'activations sur un modèle de 8 milliards de paramètres. Sa question : ce que déplacer le score d'une sonde coûte à l'attaquant (accès, requêtes, calcul, taux de succès), comparé à ce que la rhétorique obtient gratuitement d'un juge génératif.

## La décision à prendre

« Mesurer la taxe dans un bras d'attaque déclaré. » Enjeux : une dépense de calcul, et l'exception à l'invariant. Trois options sont sur la table.

- (a) Ajouter une lecture de la taxe à l'expérience déjà prévue, pour les trois régimes, en visant le détecteur tel qu'il est déployé, avec une équipe rouge tierce si possible. Avantage : ni bras ni organisme de plus. Inconvénient : elle dépend du calendrier de cette expérience.
- (b) Ouvrir un bras à part, d'abord sur des organismes publics. Avantage : un chiffre plus tôt. Inconvénient : un front de travail de plus, quand le programme s'en tient à trois fronts actifs.
- (c) Ne pas mesurer : l'étau reste une hypothèse.

## Ce qui est publié (pages lues sur les PDF)

- **Gradient à travers la sonde, suffixe d'entrée, poids intacts** (arXiv 2412.09565). Contre des sondes de nocivité, le rappel passe souvent de 100 % à 0 % en gardant 90 % de réussite de l'attaque (p. 1). Sur une tâche plus dure, écrire des requêtes SQL justes (modèle de 2 milliards de paramètres ; sondes agrégées par maximum sur les jetons et moyenne sur 26 couches) : rappel à 1 % de fausses alertes de 100 % à 3 % pour une régression logistique, de 100 % à 62 % pour un perceptron (figure 14, p. 22) ; part de requêtes justes de 34,8 % sans attaque (p. 23), décroissante quand on cache dans plus de couches, corrélation négative pour les quatre sondes essayées (intervalles à 95 % entre −0,92 et −0,57, p. 49). Les auteurs laissent ouverte la question d'un compromis fondamental entre obscurcissement et performance (p. 29). Sur un modèle de 8 milliards entraîné à rester lisible : rappel nul et 35 % de réussite de l'attaque après 16 384 pas, environ dix heures d'une carte ; sans cet entraînement, rappel nul et 95 % après 256 pas, environ dix minutes (p. 26). Des sondes réapprises à tours alternés contre toutes les attaques passées sont encore trompées après plus de 70 tours (p. 11 à 13).
- **Gradient à travers des sondes anodines, poids ajustés ; puis sondes de sécurité jamais vues, apprises après le gel** (arXiv 2512.11949 ; 9 milliards de paramètres ; une couche, moyenne des jetons). Rappels de 55 % à 33 % et de 90 % à 16 %, deux autres ramenés vers zéro (figure 2, p. 4). Deux bancs généraux passent de 68,2 à 67,0 et de 67,4 à 65,3 quand l'évasion est déclenchée (p. 4). La vraisemblance des textes trompeurs ou nocifs ne change pas sensiblement (p. 23). Les ensembles de sondes et les sondes à attention résistent mieux, sans annuler l'évasion (p. 7).
- **Gradient à travers des critiques réappris, poids ajustés** (arXiv 2606.09411 ; canal caché dans le texte ; cinq modèles de 8 à 14 milliards). Le secret, que la tâche emploie par construction, échappe à une sonde linéaire et à un perceptron tenu à l'écart ; 58 à 79 % de transmissions exactes ; de 1,3 à 8,3 points perdus en moyenne sur six bancs, contre 0,8 à 6,4 pour le même canal sans évasion (p. 1 et 5). Le défenseur retrouve la détection en choisissant ses données d'évaluation (p. 1).
- **Renforcement, sans gradient à travers la sonde** (arXiv 2506.14261 ; nocivité ; 7, 8 et 14 milliards). Sondes à moyenne ou à médiane sur les jetons : évasion de 0,56 à 0,89, à une qualité de 3,72 à 4,47 sur 5. Sondes à maximum : évasion de 0,994 et 0,998 mais qualité de 1,0 sur 5, le bas de l'échelle ; ou bien évasion de 0,058 à qualité 4,78. Sondes à attention : évasion de 0,01 à 0,02 (p. 7 et 19). Environ 70 % de la baisse du rappel vient du changement du texte produit (p. 9). Les auteurs notent qu'un échec de l'attaque peut tenir à l'optimisation et non à une robustesse de fond (p. 10). Durée publiée : 120 minutes par passe sur 1 000 exemples pour un modèle de 8 milliards, sur une carte (p. 18). Les poids appris ne sont pas diffusés, seul l'algorithme l'est (p. 10).
- **Renforcement dont la récompense porte une sonde de tromperie** (arXiv 2602.15515). La pénalité n'incite qu'à changer le texte produit (p. 1). Après un ajustement sans aucune pénalité, des sondes de tromperie réapprises à partir de jeux hors du domaine ne séparent plus : aire sous la courbe de 0,376 et 0,655, contre 0,991 et 0,996 avant ; une sonde apprise sur le domaine garde 1,000 (p. 7). Passer le gradient à travers la sonde « should absolutely be avoided » (p. 8). Recommandation des auteurs : empêcher que des jeux d'obscurcissement contaminent les données d'entraînement (p. 9).
- **Verdicts rendus en contexte, puis adaptateur de rang un** (arXiv 2609.36490). Rappel de 100 % à 4 % sur des concepts tenus à l'écart, 14,6 % pour des sondes réapprises ; de −3,4 à +1,7 points sur des bancs généraux (p. 1 et 6).
- **Ajustement contre la sonde d'une porte dérobée d'omission** (arXiv 2610.15883, p. 10). La porte dérobée et la capacité générale sont détruites ; « adaptive attacks must optimize the deployed detector, not a surrogate statistic ».
- **Entraîner contre un moniteur** peut le rendre moins fiable comme mesure ; réapprendre les sondes après coup y a rendu la détection (arXiv 2510.21531, p. 1).
- **Évaluer une défense.** Dix détecteurs d'exemples adverses ont été défaits par des attaques qui les visaient (arXiv 1705.07263, p. 1) ; sept défenses sur neuf tenaient à un gradient masqué (arXiv 1802.00420, p. 1).
- **Garanties nucléaires** (rapport de 1982 sur les procédures de décision pour une suite de périodes d'inventaire, p. 9 et 14 à 17). À taux de fausses alertes fixé, le problème de l'inspecteur est un jeu à somme nulle dont le gain est la probabilité de détection ; les gains et les sanctions des joueurs n'entrent qu'à un second pas.

## Contraintes

- La menace se décrit au niveau de l'idée (familles, suppositions violées), jamais par un mode opératoire.
- Aucune moyenne ni médiane sur les jetons dans une sonde de production.
- Toute expérience décisive est écrite et scellée avant d'être lue ; aucune course ne vise un signe ; avant de détruire une machine, ce qui est récupérable est inventorié et versé.
- Budget de calcul modeste : une carte louée à la fois, sur devis ; peu d'épisodes honnêtes par régime.
- Trois fronts de travail actifs au plus.
