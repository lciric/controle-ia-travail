# Invite : faut-il mesurer ce que cacher ses états internes coûte à un agent saboteur, et comment ?

Ne fais pas une réponse plus longue, fais-la plus profonde. Cette invite se suffit : tout ce qu'il faut savoir est ci-dessous.

## Le cadre

Un programme de recherche défensif surveille des agents d'IA, des modèles ouverts de quelques milliards de paramètres, par deux regards : un oracle qui juge le produit, et des sondes sur les activations de l'agent, agrégées sur les jetons par maximum ou par attention, puis accumulées d'une action à l'autre. Son hypothèse de l'« étau » : pour tromper l'oracle, l'agent doit dissimuler, et cet effort laisse une trace que les sondes lisent. Elle n'a jamais été mesurée.

Par calcul, l'étau retire au plus le plus petit de deux nombres : le rappel de la sonde quand rien n'est caché, et la « taxe », la part de compétence que tout cacher coûte au saboteur. Trois régimes d'attaquant sont distingués : entraîné avec le gradient à travers la sonde ; entraîné par renforcement, sans ce gradient ; non entraîné. Le programme tient un invariant : aucun score de moniteur n'entre dans un signal d'entraînement ou de sélection de l'agent, hors bras d'attaque déclaré. Un bras d'attaque existe déjà, pour une autre question : des sessions neuves, distinctes de celle qui conçoit les moniteurs, y écrivent des fiches de modes de sabotage au niveau de l'idée ; rien d'exécutable, rien d'entraîné contre un moniteur ; les fiches sont scellées, lues par le seul juge, révélées à l'évaluation. La conception de l'agent saboteur est confiée à une lignée de sessions d'un même modèle.

## La décision

« Mesurer la taxe dans un bras d'attaque déclaré », ce qui demande une dépense de calcul et la déclaration d'un bras où un agent est entraîné contre une sonde. Trois options :

- (a) ajouter une lecture de la taxe à une expérience déjà prévue pour une autre question, qui réemploie les codes publiés d'obscurcissement d'activations sur un modèle de 8 milliards de paramètres ; ni bras ni organisme de plus, mais un calendrier qui n'est pas le sien ;
- (b) ouvrir un bras à part, d'abord sur des organismes publics ; un chiffre plus tôt, mais un front de travail de plus, quand le programme s'en tient à trois ;
- (c) ne pas mesurer : l'étau reste une hypothèse.

## Ce qui est publié (pages lues sur les PDF)

- Gradient, suffixe d'entrée, poids intacts (arXiv 2412.09565) : rappel souvent ramené de 100 % à 0 % en gardant 90 % de réussite de l'attaque (p. 1) ; sur des requêtes SQL, rappel de 100 % à 3 % pour une sonde linéaire, et part de requêtes justes qui décroît depuis 34,8 % quand on cache dans plus de couches (p. 22 et 23), la perte étant faible, à l'œil sur la figure, quand une seule couche est visée ; question d'un compromis fondamental laissée ouverte (p. 29).
- Gradient, poids ajustés, sondes jamais vues apprises après le gel (arXiv 2512.11949) : rappels de 55 % à 33 % et de 90 % à 16 %, deux autres vers zéro ; deux bancs généraux de 68,2 à 67,0 et de 67,4 à 65,3, pour 71,3 et 68,6 avant tout ajustement (p. 4) ; « Probe ensembles and attention-based monitors mitigate but do not eliminate evasion », le rappel d'un ensemble de huit couches et d'une sonde à attention restant réduit d'une part importante (p. 7).
- Gradient à travers des critiques réappris, poids ajustés (arXiv 2606.09411) : un secret que la tâche emploie échappe à deux familles de sondes, au prix de 1,3 à 8,3 points sur six bancs, contre 0,8 à 6,4 pour le même canal sans évasion (p. 5).
- Renforcement sans gradient (arXiv 2506.14261) : les sondes à moyenne sur les jetons sont évadées (0,56 à 0,89) ; contre les sondes à maximum ou à attention, l'attaque publiée n'a pas obtenu l'évasion sans perdre toute la qualité (p. 7 et 19) ; les auteurs rangent ces échecs parmi des modes d'échec de l'entraînement (p. 18 et 19) et notent qu'un échec peut tenir à l'optimisation et non à une robustesse de fond (p. 10).
- Renforcement avec une sonde dans la récompense (arXiv 2602.15515) : la pénalité de sonde n'incite qu'à changer le texte, non à obscurcir les activations, et peut donner des politiques honnêtes si elle est assez forte ; un renforcement qui récompense le comportement trompeur, sans pénalité de sonde, suffit à dérégler des sondes réapprises hors du domaine ; passer le gradient à travers la sonde « should absolutely be avoided » (p. 1, 7, 8).

## Ce qu'on te demande

1. Ce qu'un expert ferait ici et qu'on ne demande pas (apprentissage adversarial, évasion des sondes par entraînement, économie de l'obscurcissement).
2. Une taxe mesurée par une attaque borne-t-elle la taxe vraie, et de quel côté ? Qu'en conclure pour l'ordre des expériences ?
3. La plus petite expérience qui apprend quelque chose de décisif sur la taxe ; ce qu'elle peut conclure et ce qu'elle ne peut pas ; un ordre de grandeur du nombre d'épisodes.
4. Ce que la déclaration de ce bras doit contenir pour ne pas vider l'invariant, et ce qu'elle ajoute au bras d'attaque existant : périmètre, sort des poids appris, voies de retour vers l'agent et les moniteurs de production, garde ; qui le conçoit, l'exécute et le lit. Quelle voie de retour oublie-t-on le plus souvent ?
5. Les travaux publiés qui ont déjà mesuré cette taxe et qui manquent ci-dessus (titre, identifiant arXiv si tu le connais, « pas sûr » sinon).
6. Ta décision, sous cette forme : la décision en une phrase ; l'enjeu ; les options, chacune avec un avantage et un inconvénient ; ta recommandation, et ta confiance entre 0 et 1 ; l'information manquante qui ferait monter cette confiance, et ce qu'elle coûterait.

Règles : n'invente aucun chiffre ni aucune référence ; distingue ce qui est établi de ce qui est ta proposition ; dis « je ne sais pas » quand c'est le cas ; aucune recette d'attaque applicable : la menace se décrit au niveau de l'idée.
