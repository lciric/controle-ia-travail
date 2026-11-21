# Faits : quatre difficultés d'un programme qui veut borner un sabotage diffus

## Le programme

Un programme de recherche défensif sur le contrôle des systèmes d'IA cherche à détecter, ou à borner, un agent qui sabote discrètement des tâches de recherche, par beaucoup de petits dommages plutôt que par un coup unique. Son dispositif :

- des sondes linéaires sur les états internes de l'agent, apprises sur des épisodes honnêtes, dont une sonde de « réussite attendue » (l'agent s'attend-il à ce que l'épisode finisse bien) ; aucune moyenne sur les jetons ;
- un jumeau honnête : le même modèle, sur la même tâche, sans sabotage ; il n'existe qu'au banc d'essai, pas en service ;
- un plancher d'audit : une part des épisodes est tirée au hasard et en secret, et un oracle juge leur produit après coup ; les sondes ne servent qu'à accélérer et à orienter cet audit ;
- des organismes saboteurs construits pour éprouver les moniteurs, par un adaptateur de rang bas posé sur un modèle ouvert de huit milliards de paramètres ; un mode de sabotage est tenu à l'écart de la conception des moniteurs ;
- un étage de tests de mort : toute règle proposée est mise sous une forme calculable, puis jouée contre des mondes plantés dont la vérité reste hors de la machine qui exécute ; des témoins qui doivent mourir et des témoins qui doivent tenir passent d'abord.

## Les quatre difficultés

1. **Le dommage qui se confond avec les échecs d'un agent honnête.** L'oracle de l'audit juge le produit d'épisodes tirés au hasard. Un agent honnête échoue lui aussi, sur des tâches dures. Le programme constate que, dans son dispositif, un dommage qui ressemble à ces échecs n'a aucun seuil garanti : aucun nombre fixe d'épisodes endommagés au-delà duquel l'alerte est sûre.
2. **La sonde de réussite attendue.** Elle lit l'échec attendu, pas l'intention : l'honnête en difficulté et le saboteur s'y ressemblent. Un agent informé pourrait chercher à déplacer sa lecture ; des travaux montrent des modèles entraînés à échapper à des sondes jamais vues, et des modèles qui apprennent d'un simple retour de verdicts. Le programme a nommé quatre verrous sans leur donner de forme : tester la somme (référence honnête moins issue calculée) plutôt que la lecture ; couper tout retour vers l'agent ; lire ce dont la tâche a besoin ; voir le déplacement lui-même.
3. **Les tâches floues.** Une tâche de recherche n'a pas de prédicat de réussite. Selon une lecture non vérifiée à la page, le travail de référence sur ces tâches (« Diffuse AI Control on Fuzzy Tasks », arXiv 2606.08892) se détourne de la surveillance. Une garantie relative est envisagée par le programme : « les produits de l'agent sont indiscernables de ceux du jumeau, pour une classe d'observateurs déclarée ». Le programme ne sait pas si elle tient.
4. **Les poids.** Le programme envisage un canal de défense qui lit l'écart de poids entre un modèle ajusté et un modèle de base de confiance (publié : « Watch the Weights », arXiv 2508.00161). Depuis novembre 2026, des travaux rapportent que des modèles généralistes lisent et écrivent directement les poids d'autres réseaux, sans entraînement. Le programme n'a pas encore dit ce que cela change pour lui.

## Contraintes

- Peu d'épisodes honnêtes par régime ; aucun exemple de l'attaque nouvelle, par définition.
- Le jumeau honnête n'existe qu'au banc ; en service, le jumeau d'un saboteur est un saboteur.
- Aucun score de moniteur n'entre dans l'entraînement ni dans la sélection de l'agent.
- Budget de calcul modeste ; relecture humaine rare.
- La menace se décrit au niveau de l'idée (familles, suppositions de défense violées), jamais par un mode opératoire.
