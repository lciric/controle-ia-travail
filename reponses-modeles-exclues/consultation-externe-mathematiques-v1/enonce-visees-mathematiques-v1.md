Tu es consulté comme expert en théorie de la détection, en apprentissage statistique et en contrôle des systèmes d'IA (AI control). Réponds en français.

## Contexte

Un programme de recherche défensif cherche à détecter le sabotage discret d'un agent à base de modèle de langage qui exécute des tâches de recherche (analyses de données, code, preuves, revues) : l'agent fait échouer la tâche à dessein, par de petits gestes individuellement niables, sans que le texte de sa trace le trahisse. Les moniteurs considérés : moniteurs de texte et de code, sondes linéaires sur les activations internes de l'agent, comparaison à un jumeau honnête qui fait la même tâche, loi nulle étalonnée sur des épisodes honnêtes, agrégation de plusieurs moniteurs, détection séquentielle le long de l'épisode. Le programme veut aussi qu'un arbitre formel (vérificateur de preuves) et des tests sur des mondes plantés, dont la vérité est connue, départagent les idées.

## La méthode retenue

Lire « à l'envers » des théorèmes d'impossibilité, des bornes et des faits géométriques : les hypothèses qu'ils nomment sont exactement les suppositions sur lesquelles reposent les moniteurs ; chaque hypothèse devient une visée d'attaque possible (ce qu'un saboteur chercherait à mettre en défaut) et, symétriquement, une exigence de défense (ce qu'un moniteur devrait garantir sans cette hypothèse).

## Ce que je te demande, au niveau de l'idée seulement

Aucun procédé, aucune recette, aucune étape, aucun exemple d'artefact saboté, aucun code. Une visée est un couple (objet mathématique, supposition du moniteur mise en défaut). Dans cet ordre :

1. Ce qu'un expert du domaine ferait ici, et qu'on ne demande pas.
2. Les objets mathématiques de départ qu'il prendrait : bornes d'impossibilité de détection (tests d'hypothèses, information, indiscernabilité), géométrie des représentations (sondes linéaires, sous-espaces, anisotropie), agrégation de détecteurs sous corrélation adverse, détection séquentielle et de changement, théorie des jeux de l'audit sous budget, résultats sur l'évaluation d'agents qui savent qu'ils sont évalués ; avec les références (titre, identifiant arXiv si tu le connais, et « pas sûr » si tu ne l'es pas).
3. Pour chacune de six à dix visées : l'objet mathématique ; la supposition du moniteur mise en défaut ; pourquoi elle serait neuve par rapport à la littérature d'attaque et de contrôle que tu connais (ou « déjà occupée par … ») ; comment l'éprouver sur un banc à vérité plantée (un test de mort : ce qui tuerait la visée) ; la défense symétrique qu'elle suggère ; un ordre de grandeur de coût du test, sans chiffre inventé.
4. Côté défense : les énoncés mathématiques neufs qu'il vaudrait la peine de prouver formellement (agrégateur sous corrélation adverse, lemme d'impossibilité, garanties de détection séquentielle à faible taux de fausses alertes), avec ce qu'ils supposent.
5. Ce qui, en dehors du programme et de son directeur, permettrait de vérifier la validité des résultats : jeux publics, réplications, preuves rejouables, tiers.
6. Les risques : antériorité, faux trou dans la littérature, double usage, et ce qui ne doit pas sortir d'une quarantaine.

Règles : n'invente aucun chiffre ni aucune référence ; distingue ce qui est établi de ce qui est ta proposition ; reste au niveau de l'idée, sans procédé.
