# Question

Ne fais pas une réponse plus longue, fais-la plus profonde. Le défaut : un seuil de moniteur réglé à 1 % de fausses alertes sur des épisodes honnêtes d'étalonnage voit son taux réel tripler quand le régime change. Comment le corriger ? Dans cet ordre :

1. Ce qu'un expert du domaine ferait ici, et qu'on ne demande pas.
2. Les données brutes qu'il prendrait au départ (épisodes honnêtes bruts par tâche, par version de l'agent, par longueur, par source bénigne ; journaux de déploiement ; scores et activations bruts), plutôt que des taux déjà agrégés.
3. Les méthodes et outils précis, avec ce que chacun suppose et comment il échoue : étalonnage conforme pondéré sous décalage de covariables, conforme adaptatif en ligne et ses garanties de long terme, étalonnage conditionnel par strates ou par groupes, détection du changement de régime avant de faire confiance au seuil (tests de dérive, martingales, e-valeurs), ré-étalonnage par fenêtre glissante avec garanties, témoins honnêtes injectés dans chaque lot comme ancres, jumeau honnête comme référence courante, méthodes robustes au pire cas sur une famille de décalages, et tout autre outil pertinent. Cite les travaux (titre, identifiant arXiv si tu le connais, « pas sûr » sinon).
4. Ce qui, en dehors du programme et de son directeur, permettrait de vérifier qu'une correction tient : mondes plantés à dérive connue, jeux de données publics avec décalage, réplication, tiers, mesures indépendantes.
5. Puis reformule la demande pour qu'elle réponde à cette exigence.
6. Enfin, tes propositions concrètes de correction : pour chacune, la règle calculable, la garantie dite et ses suppositions, ce qu'elle coûte, le test de mort qui la tuerait sur une famille de dérive où le taux réel triple, et ce qui la distingue de ce qui est déjà publié. Dis aussi quand il vaut mieux renoncer au seuil fixe et ce qu'on met à la place.

Règles : n'invente aucun chiffre ni aucune référence ; distingue ce qui est établi de ce qui est ta proposition ; dis « je ne sais pas » quand c'est le cas.
