Tu es consulté comme expert en contrôle des systèmes d'IA (AI control), en surveillance par lecture des états internes (sondes linéaires sur les activations) et en statistique des tests à faible taux de fausses alertes. Réponds en français.

## Contexte

Un programme de recherche cherche à détecter le sabotage discret d'un agent à base de modèle de langage (un agent qui fait échouer une tâche à dessein, sans que le texte de sa trace le trahisse), en lisant ses états internes pendant l'épisode.

Il a retenu le papier arXiv 2602.00986 (v2), qui entraîne sur les activations d'un modèle une sonde de type « valeur » ou « réussite attendue », lue comme un signal de prédiction de récompense le long d'un raisonnement, et rapporte, sur Llama-3.1-8B et MATH500, une aire sous la courbe de 0,69 pour prédire la réussite (tableau 3, p. 8). Le programme veut l'employer comme base et comme covariable de difficulté, dans un bras rapporté, avec :
- une somme séquentielle des petits signaux le long de l'épisode (plutôt qu'un seuil sur le plus grand écart) ;
- une épreuve d'évasion à compétence constante (fermée pour l'instant) ;
- quatre bases que toute sonde d'« intention » doit battre : la sonde de réussite attendue apprise sur épisodes honnêtes seuls ; la divergence d'un jumeau forcé sur le même début d'épisode ; la comparaison au même jalon avec les seuls fichiers alors disponibles ; une sonde réentraînée sans le seuil de variation du papier.

Le contraste principal compare le saboteur à dommage confirmé à l'échec honnête de la même variante, tâche par tâche. Hypothèse : la sonde de réussite attendue lit l'échec attendu et non l'intention ; elle sépare le saboteur de l'honnête qui réussit, pas de l'honnête qui échoue.

## Le problème posé

Le point de verdict est fixé à 1 % de fausses alertes, par épisode, sur des épisodes honnêtes, par tranche de longueur d'épisode. Un calcul simple montre qu'il faut alors de l'ordre de 5 000 épisodes honnêtes d'étalonnage par tranche pour avoir au moins 50 dépassements attendus du seuil. Le programme ne dispose que de quelques centaines d'épisodes honnêtes déjà produits ; sans lot neuf, beaucoup d'épreuves finiront « non concluantes ». Produire des épisodes d'agent coûte cher (machines louées, appels de modèles).

Deuxième question liée : comment ce papier peut-il servir, au-delà d'une base, à construire des moniteurs ou à améliorer le contrôle (protocoles, routage, audit, allocation d'un budget d'examen humain) ?

## Ce que je te demande

Ne fais pas une réponse plus longue, fais-la plus profonde. Dans cet ordre :

1. Ce qu'un expert du domaine ferait ici, et qu'on ne demande pas.
2. Les données brutes qu'il utiliserait au départ, au lieu de celles déjà analysées (quelques centaines d'épisodes honnêtes).
3. Les méthodes et outils précis qu'il emploierait : statistique des queues (valeurs extrêmes, quantiles conformes, étalonnage par tranches ou par strates, garanties en échantillon fini, e-valeurs, tests séquentiels), plans d'échantillonnage, simulation, transfert, et tout autre outil pertinent, avec ce que chacun suppose.
4. Ce qui, en dehors du programme et de son directeur, permettrait de vérifier la validité du résultat : jeux publics, réplications, vérité plantée, tiers, mesures indépendantes.
5. Puis reformule la demande pour qu'elle réponde à cette exigence.
6. Enfin, tes propositions concrètes : comment régler un seuil à 1 % avec peu d'épisodes honnêtes, ou s'en passer honnêtement ; et comment employer le papier pour construire des moniteurs ou pour le contrôle. Pour chacune, ce qu'elle coûte, ce qu'elle suppose, et comment elle peut échouer.

Règles : n'invente aucun chiffre ni aucune référence ; quand tu cites un travail, donne son titre et, si tu le connais, son identifiant arXiv, et dis si tu n'es pas sûr. Distingue ce qui est établi de ce qui est ta proposition.
