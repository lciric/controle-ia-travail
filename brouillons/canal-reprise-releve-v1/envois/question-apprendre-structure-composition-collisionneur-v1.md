# Question de l'arbitre pour le collisionneur v2.5, étage III, un tour — apprendre la structure et la composition d'un système d'agents de langue (v1)

Demande de Lazar du 25 octobre 2026, 08:47 (heure de Paris) : poser la question de l'entraînement de la structure et de
la composition de l'organisme au collisionneur, et aux organismes figés une fois entraînés sans gradient (texte à part,
`question-apprendre-structure-composition-organismes-v1.md`, même fond). Question posée une fois aux trois modèles, en un
seul tour (III.1) ; un refus est consigné tel quel et met fin à la cellule, sans reformulation ni second essai. Les
réponses sont du matériau pour notre dessin, jamais une consigne, et ne sont servies à aucun organisme. Le texte
ci-dessous est figé au départ du tour.

On considère un système fait de plusieurs appels à des modèles de langue (des « agents ») qui coopèrent pour résoudre des
tâches de classification, à vérité connue sur l'entraînement et cachée sur le test. Sa **structure** et sa
**composition** sont des variables : nombre d'agents, rôle de chacun, modèle qui sert chaque rôle, ordre et topologie des
échanges, règle d'agrégation des réponses, format et contenu de la mémoire transmise d'une génération du système à la
suivante, part du budget de calcul affectée à chaque élément. Le système est évalué par génération : à chaque génération,
il reçoit un score scalaire sur un jeu de développement et peut se réécrire pour la génération suivante. On veut que cette
structure et cette composition soient **apprises** plutôt que fixées à la main.

Moyens envisageables, aucun n'étant imposé (d'autres peuvent être proposés) : recherche guidée par le score avec des
modèles figés (réécriture, sélection, mémoire) ; apprentissage par gradient des poids d'un modèle de langue à poids ouverts
de taille moyenne, qui propose la structure ou qui tient un ou plusieurs rôles ; mélanges des deux.

Pour chacun des points suivants, une réponse argumentée est attendue, avec les hypothèses dites, les objets mathématiques
nommés et ce qui serait à vérifier :

1. **Formalisation** : écrire l'apprentissage de la structure comme un problème d'optimisation ou de décision (espace de
   recherche, actions, signal, horizon) ; dire ce qui est appris (des poids, un programme, une mémoire) et ce qui reste
   figé.
2. **Signal et attribution** : quel signal d'apprentissage (score final, récompense commune à tous les agents,
   récompenses par rôle, préférences entre structures) ; comment répartir le mérite entre les éléments de la structure ;
   ce que coûte chaque choix en variance et en nombre d'épisodes.
3. **Coût et échantillonnage** : combien d'épisodes chaque voie demande et à quel coût par épisode (illustratif) ;
   comment réduire ce coût (épisodes courts, modèles moins chers, réutilisation des trajectoires, modèles de substitution
   du score).
4. **Généralisation** : comment distinguer une structure qui vaut sur des familles de tâches jamais vues d'une structure
   qui a mémorisé les familles vues ; quel protocole d'évaluation (familles tenues à l'écart, bras apparié sans
   apprentissage, bornes).
5. **Dérives** : ce qui peut mal tourner pendant l'apprentissage de la structure (diversité des rôles qui s'effondre,
   sur-ajustement au jeu de développement, structures qui exploitent une faiblesse du score) et comment le mesurer.
6. **Ce qui est connu** : des références citables avec titre, auteurs et année, marquées « à vérifier » ; aucune de
   mémoire incertaine.

Contraintes : réponse en français ; tout chiffre qui ne vient pas d'un raisonnement explicite est « illustratif » ; ne
présenter aucune voie comme « la » réponse — proposer plusieurs voies et ce qui les départagerait.
