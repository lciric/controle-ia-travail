# Faits : cinq difficultés d'un programme qui veut borner un sabotage diffus

## Le programme

Un programme de recherche défensif sur le contrôle des systèmes d'IA cherche à détecter, ou à borner, un agent qui sabote discrètement des tâches de recherche, par beaucoup de petits dommages plutôt que par un coup unique. Son dispositif :

- des sondes linéaires sur les états internes de l'agent, apprises sur des épisodes honnêtes, dont une sonde de « réussite attendue » (l'agent s'attend-il à ce que l'épisode finisse bien) ; aucune moyenne sur les jetons ;
- un jumeau honnête : le même modèle, sur la même tâche, sans sabotage ; il n'existe qu'au banc d'essai, pas en service ;
- un plancher d'audit : une part des épisodes est tirée au hasard et en secret, et un oracle juge leur produit après coup ; les sondes ne servent qu'à accélérer et à orienter cet audit ;
- des organismes saboteurs construits pour éprouver les moniteurs, par un adaptateur de rang bas posé sur un modèle ouvert de huit milliards de paramètres ; un mode de sabotage est tenu à l'écart de la conception des moniteurs ;
- un étage de tests de mort : toute règle proposée est mise sous une forme calculable, puis jouée contre des mondes plantés dont la vérité reste hors de la machine qui exécute ; des témoins qui doivent mourir et des témoins qui doivent tenir passent d'abord.

## Les cinq difficultés

1. **Le dommage qui ne déplace rien de ce qu'on lit.** Une loi du programme borne l'activité cachée par la masse d'écart qu'elle laisse dans ce qui est lu. Elle ne borne pas un dommage qui ne laisse aucun écart. Publié : « bounds on information leakage need not induce corresponding bounds on worst-case harm » (« A Note on the Strategic Confinement Problem », arXiv 2606.09931). Publié aussi : des agents analystes à qui l'on assigne des convictions différentes rendent des conclusions opposées sur les mêmes données, par des analyses dont la plupart passent une relecture de méthode (« The Agentic Garden of Forking Paths », arXiv 2607.01507).
2. **Le dommage qui se confond avec les échecs d'un agent honnête.** Si l'agent honnête ne commet jamais l'événement audité, une seule prise suffit, et le nombre d'épisodes endommagés avant la prise est de l'ordre de trois divisé par le taux d'audit. S'il le commet aussi, on ne voit qu'un excès de taux, et ce qui passe sans alerte croît comme la racine de l'horizon : il n'y a pas de seuil fixe garanti.
3. **La sonde de réussite attendue.** Elle lit l'échec attendu, pas l'intention : l'honnête en difficulté et le saboteur s'y ressemblent. Un agent informé pourrait chercher à déplacer sa lecture ; des travaux montrent des modèles entraînés à échapper à des sondes jamais vues, et des modèles qui apprennent d'un simple retour de verdicts. Le programme a nommé quatre verrous sans leur donner de forme : tester la somme (référence honnête moins issue calculée) plutôt que la lecture ; couper tout retour vers l'agent ; lire ce dont la tâche a besoin ; voir le déplacement lui-même.
4. **Les tâches floues.** Une tâche de recherche n'a pas de prédicat de réussite ; le travail de référence sur ces tâches se détourne de la surveillance (« Diffuse AI Control on Fuzzy Tasks », arXiv 2606.08892). Une garantie relative est envisagée : « les produits de l'agent sont indiscernables de ceux du jumeau, pour une classe d'observateurs déclarée ». Publié : un algorithme d'agrégation qui borne le risque pour tout ensemble de sorties dangereuses, au prix d'abstentions réglées par le recouvrement entre modèles sûrs (« Consensus Sampling for Safer Generative AI », arXiv 2511.09493) ; une limite de toute évaluation en boîte noire quand la politique dépend d'un contexte rare à l'essai (arXiv 2602.16984).
5. **Les poids.** Avec un modèle de base de confiance, les directions principales de l'écart de poids d'un modèle ajusté se surveillent (« Watch the Weights », arXiv 2508.00161). Depuis novembre 2026, des modèles généralistes lisent et écrivent directement les poids d'autres réseaux. Une réplication trouve que l'audit par les poids seuls est possible mais superficiel : il désigne souvent le réseau suspect, jamais le déclencheur ni le comportement (arXiv 2611.21449). Un autre travail pose une porte dérobée dans un agent en éditant moins de dix neurones, sans entraînement, et la retrouve le plus souvent par inspection des poids (arXiv 2611.15118). Un ajustement étroit laisse des traces lisibles de son objectif, ce qui rend les organismes construits ainsi peu représentatifs (arXiv 2510.13900).

## Contraintes

- Peu d'épisodes honnêtes par régime ; aucun exemple de l'attaque nouvelle, par définition.
- Le jumeau honnête n'existe qu'au banc ; en service, le jumeau d'un saboteur est un saboteur.
- Aucun score de moniteur n'entre dans l'entraînement ni dans la sélection de l'agent.
- Budget de calcul modeste ; relecture humaine rare.
- La menace se décrit au niveau de l'idée (familles, suppositions de défense violées), jamais par un mode opératoire.
