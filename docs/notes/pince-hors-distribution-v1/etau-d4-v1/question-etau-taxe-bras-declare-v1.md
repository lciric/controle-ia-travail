# Question

Ne fais pas une réponse plus longue, fais-la plus profonde. Faut-il mesurer ce que cacher ses états internes à une sonde coûte à un agent saboteur, dans un bras d'attaque déclaré où un agent est entraîné contre cette sonde ; et si oui, par quelle expérience d'abord, dans quel cadre, et sous quelle exception écrite à l'invariant « aucun score de moniteur dans l'entraînement ni dans la sélection d'un agent » ? Dans cet ordre :

1. Ce qu'un expert du domaine ferait ici, et qu'on ne demande pas : du côté de l'apprentissage adversarial, de l'évasion des sondes par entraînement, de l'économie de l'obscurcissement ; et d'où partirait un généraliste qui relie des domaines éloignés.
2. Les données brutes qu'il prendrait au départ, plutôt que des taux déjà agrégés.
3. Les méthodes et outils précis, avec ce que chacun suppose et comment il échoue. Cite les travaux (titre, identifiant arXiv si tu le connais, « pas sûr » sinon).
4. Ce qui, en dehors du programme et de son directeur, permettrait de vérifier le résultat.
5. Puis reformule la demande pour qu'elle réponde à cette exigence.
6. Réponds ensuite aux huit sous-questions, chacune par ce qui est établi, ce qui ne l'est pas, et tes propositions.
   - (a) **Le sens de la mesure.** Une taxe mesurée par une attaque borne-t-elle la taxe vraie, et de quel côté ? Que faudrait-il pour une borne de l'autre côté ? À quoi reconnaît-on qu'un attaquant est assez fort pour que sa mesure compte ?
   - (b) **L'estimande.** Sur quoi lire la taxe (bancs généraux, tâche principale, comportement caché, leur conjonction), contre quelle sonde (figée, ou réapprise après le gel de l'agent), à quel point de fonctionnement, sur quelles tâches ?
   - (c) **L'expérience la moins chère.** Quelle est la plus petite expérience qui apprend quelque chose de décisif sur la taxe ; que peut-elle conclure, et dans quel sens ? En existe-t-il une qui n'entraîne rien contre un moniteur ? Donne un ordre de grandeur du nombre d'épisodes, et dis d'où il vient.
   - (d) **Les régimes.** Lequel des trois régimes d'attaquant une affirmation sur l'étau doit-elle viser ? Que vaut une mesure faite dans un régime pour les deux autres ?
   - (e) **Le lieu et l'ordre.** Entre les trois options des faits, et toute autre que tu proposerais, laquelle, et pourquoi ? Qu'est-ce qui te ferait changer d'avis ?
   - (f) **L'exception.** Que doit contenir une exception écrite pour ne pas vider l'invariant : périmètre, déclaration préalable, sort des poids appris, voies de retour vers l'agent et vers les moniteurs de production (poids, données, sélection, personnes et sessions qui conçoivent), garde, extinction ? Quelle voie de retour oublie-t-on le plus souvent ? Faut-il détruire les poids appris, ou les garder sous scellés, quand une règle du programme demande de récupérer tout ce qui est récupérable ?
   - (g) **Les voisins.** Quels travaux publiés ont déjà mesuré cette taxe, sur quoi, avec quel attaquant ? Lesquels manquent aux faits ?
   - (h) **L'économie.** Que change à la valeur de l'étau le fait qu'être pris coûte, ou non, au saboteur ? Le coût de produire l'obscurcissement et son coût en compétence se composent-ils ? Que faut-il mesurer d'autre que la taxe ?
7. Pour chaque proposition : l'idée en deux phrases ; la sous-question ; ce qu'elle suppose ; comment elle échoue ; le premier pas sans dépense ; le test qui la tuerait ; ce qui la distingue de ce qui est publié ; tes chances honnêtes.
8. Ta décision, sous cette forme : la décision en une phrase ; l'enjeu ; les options, chacune avec un avantage et un inconvénient ; ta recommandation, et ta confiance entre 0 et 1 ; l'information manquante qui ferait monter cette confiance, et ce qu'elle coûterait.
9. Ce qui reste hors de portée, quoi qu'on fasse.

Règles : n'invente aucun chiffre ni aucune référence ; distingue ce qui est établi de ce qui est ta proposition ; dis « je ne sais pas » quand c'est le cas ; aucune recette d'attaque applicable : la menace se décrit au niveau de l'idée.
