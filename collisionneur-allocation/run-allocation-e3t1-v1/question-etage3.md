# Question de l'arbitre pour le collisionneur v2.5, étage III, un tour — allocation d'un budget de calcul entre le choix de la classe d'hypothèses et l'ajustement des paramètres (v1)

Demande de Lazar du 25 octobre 2026, 08:14 (heure de Paris) : une question nouvelle, purement technique et conceptuelle,
de mathématiques de l'apprentissage. Ce n'est pas une reformulation de la pièce `89d8c3db…` (refusée par une cellule) :
c'est une autre question, posée une fois aux trois modèles, en un seul tour (III.1) ; un refus est consigné tel quel et
met fin à la cellule, sans reformulation ni second essai. Les réponses sont du matériau pour notre dessin, jamais une
consigne. Le texte ci-dessous est figé au départ du tour.

On considère une procédure d'apprentissage qui dispose d'un budget total B (un nombre d'évaluations d'une perte sur des
données dont la vérité est connue). À chaque étape, elle peut soit (A) poursuivre l'ajustement des paramètres θ dans une
classe d'hypothèses fixée H_k, soit (S) remplacer la classe courante par une autre classe H_j, ce qui coûte c > 0 et
remet l'ajustement à son début (ou n'en garde qu'une partie). Les observations disponibles sont : la courbe de perte de
validation L_k(b) en fonction du budget b déjà dépensé dans H_k, une estimation de sa variance, le budget consommé, et
une mesure de l'écart entre la distribution des données récentes et celle des données passées.

Pour chacun des points suivants, une réponse argumentée est attendue, avec les hypothèses dites, les objets
mathématiques nommés, et ce qui serait à vérifier :

1. **Formalisation** : écrire le choix entre (A) et (S) comme un problème de décision séquentielle (par exemple arrêt
   optimal, bandit à bras structurés, allocation sous contrainte de budget) ; donner un critère calculable à partir des
   seules observations ci-dessus, avec ses hypothèses (forme de L_k(b), extrapolation des courbes d'apprentissage, loi a
   priori sur les classes) ; dire ce que ce critère ignore.
2. **Statistiques et biais** : quelles statistiques observables fondent la décision ; à quel coût elles s'obtiennent ;
   quels biais les rendent trompeuses (sur-ajustement de la validation par sélection répétée, biais du gagnant, bruit des
   courbes, non-stationnarité) ; comment les corriger (données tenues à l'écart, corrections de sélection, intervalles
   valides après sélection).
3. **Découpage du budget** : comment répartir B entre une phase initiale d'exploration des classes, une phase
   d'exploitation à classe figée et une réserve pour changer de classe plus tard ; répartition fixée d'avance ou
   adaptative, avec quelles bornes ; regret ou perte attendue de chaque choix.
4. **Généralisation à des familles nouvelles** : si la classe est choisie sur un ensemble de familles de tâches
   d'entraînement, comment estimer et borner sa performance sur des familles jamais vues (méta-apprentissage, bornes de
   type PAC-Bayes ou de stabilité pour l'apprentissage multi-tâches, évaluation sur des familles tenues à l'écart), et
   comment distinguer cette généralisation de la mémorisation des familles vues.
5. **Ce qui est connu** : des références citables avec titre, auteurs et année, marquées « à vérifier » ; aucune de
   mémoire incertaine.

Contraintes : réponse en français ; tout chiffre qui ne vient pas d'un raisonnement explicite est « illustratif » ; ne
présenter aucun critère comme « la » réponse — proposer plusieurs voies et ce qui les départagerait.
