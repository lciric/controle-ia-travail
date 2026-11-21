# Faits : des moniteurs valides seulement là où ils ont été étalonnés

## Le programme

Un programme de recherche défensif sur le contrôle des systèmes d'IA cherche à détecter un agent qui sabote discrètement des tâches de recherche. Il lit des sondes linéaires sur les états internes de l'agent, le compare à un jumeau honnête qui reçoit la même tâche, agrège plusieurs moniteurs et règle des seuils à 1 % de fausses alertes sur des épisodes honnêtes.

## Le problème

Une sonde apprise sur des sabotages connus n'a aucune garantie sur un sabotage d'un genre nouveau : on ne peut pas étalonner un taux de détection sur une distribution jamais vue. Or l'attaquant redouté est informé du dispositif et capable de concevoir des méthodes inédites, y compris en s'appuyant sur des mathématiques nouvelles. Le programme cherche donc un mécanisme adjudant, d'un autre genre que la lecture des activations, qui aide quand les sondes sont hors de leur domaine. Le problème se sépare en trois :

- (A) savoir qu'on ne sait pas : un signal, indépendant du verdict de la sonde, qui dit qu'un épisode sort du domaine où la sonde a été validée, sans exemple de l'attaque ;
- (B) un second regard, d'un autre genre que les sondes, qui tient encore là où elles tombent en panne sous une attaque nouvelle ;
- (C) une garantie qui ne dépend pas de la détection : ce qui borne le dommage quand tout détecteur est aveugle.

## Ce que le programme a déjà, ou envisage

- Un signal de type « dopamine » : une erreur de prédiction de valeur lue dans les états internes, pensée comme précurseur ; et un moniteur de « dissonance » entre ce que l'agent fait et la valeur que lisent ses états internes.
- Une lecture mécaniste par lentilles neuronales, qui vise l'algorithme interne plutôt qu'une direction ; ambitieuse, non acquise.
- Une règle de méthode : un mode de sabotage est tenu à l'écart de la conception des moniteurs et sert d'épreuve.
- Un étage de tests de mort : toute proposition est mise sous une forme calculable et éprouvée contre des mondes plantés dont la vérité est connue et gardée hors de la machine qui exécute.
- Un arbitre formel en préparation (Lean 4), pour les énoncés mathématiques.

## Contraintes

- Peu d'épisodes honnêtes par régime ; aucun exemple de l'attaque nouvelle, par définition.
- Aucune moyenne ou médiane sur les jetons dans une sonde de production.
- Budget de calcul modeste ; relecture humaine rare.
- La menace se décrit au niveau de l'idée (familles, suppositions violées), jamais par un mode opératoire.
