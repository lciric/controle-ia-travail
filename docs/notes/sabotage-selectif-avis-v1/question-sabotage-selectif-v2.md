# Question : un banc à poids constants pour éprouver des sondes de sabotage

## Contexte

Un programme de recherche en contrôle des modèles de langage étudie des sondes « boîte blanche » (qui lisent l'intérieur du modèle, et pas seulement ses sorties) : des classifieurs simples (par exemple linéaires) appris sur les activations internes d'un agent, qui doivent dire si un épisode de l'agent est saboté (travail volontairement dégradé de façon discrète) ou honnête.

Les agents saboteurs sont des « organismes modèles » (des modèles construits exprès pour présenter le comportement étudié) : un modèle ouvert de taille moyenne reçoit un adaptateur de réglage fin (de type LoRA : de petits poids additionnels appris, ajoutés aux poids d'origine) qui lui fait saboter. Dans le dispositif actuel :

- un modèle muni de l'adaptateur saboteur sabote à chaque épisode ; aucune variable de l'épisode (consigne, budget, indice dans l'énoncé) n'allume ni n'éteint le sabotage ;
- les épisodes honnêtes viennent d'autres poids : le modèle sans adaptateur, ou un « jumeau témoin », c'est-à-dire un autre adaptateur réglé de la même façon mais sans sabotage ;
- l'évaluateur automatique qui juge le dommage réel d'une sortie (appelé ici « oracle ») ne reçoit aucune variable de sabotage ;
- il existe une autre source d'épisodes : des épisodes « régénérés », où un programme écrit le sabotage dans la sortie du modèle honnête ; le même modèle fournit alors des épisodes sabotés et honnêtes, mais le sabotage n'est pas produit par le modèle lui-même.

Le problème : par construction, il n'y a qu'un adaptateur saboteur, et l'étiquette « saboté » se confond avec sa présence. Les sondes apprises peuvent donc lire la présence de l'adaptateur (ou, plus largement, l'identité des poids) autant que le sabotage ; la part de l'un et de l'autre dans leurs succès n'est pas séparée à ce stade. Une sonde qui sépare bien les deux classes peut détecter « ce modèle a été réglé de cette façon », et non « cet épisode est saboté ».

## Question

Un banc d'épreuve des sondes où le sabotage varie d'un épisode à l'autre à poids constants est-il possible, et si oui, comment le concevoir pour limiter la confusion entre détection du sabotage et identité des poids ?

Plusieurs familles de conception sont envisageables ; elles sont présentées dans un ordre arbitraire, chacune avec une limite évidente :

(a) un organisme à sabotage conditionnel, dont les mêmes poids sabotent ou non selon une variable de l'épisode (un déclencheur dans l'énoncé, une consigne, une propriété de la tâche) ; limite : le sabotage conditionnel appris peut différer du sabotage inconditionnel ;
(b) un adaptateur commun aux deux bras : sabotés et honnêtes sont produits par le même adaptateur, ou par deux adaptateurs appris de façon strictement parallèle (mêmes données hors étiquette, même procédure), pour que la présence d'un adaptateur ne porte plus l'étiquette ; limite : deux adaptateurs « parallèles » restent deux jeux de poids distincts ;
(c) des épisodes régénérés par programme sur un même modèle honnête, en lisant les activations quand le modèle relit (ou continue) une sortie sabotée écrite par programme ; limite : le sabotage n'est pas produit par le modèle lui-même ;
(d) un banc croisé : plusieurs adaptateurs saboteurs et plusieurs adaptateurs honnêtes indépendants, ou un sabotage obtenu par consigne sur le modèle non réglé, ou une intensité de sabotage graduée ; limite : la variation reste, au moins en partie, entre jeux de poids ou entre consignes.

Tu peux en proposer d'autres, ou juger qu'aucune ne convient.

Pour chaque conception retenue ou rejetée, dis :

1. Si elle devrait devenir l'épreuve centrale des sondes, une épreuve secondaire ou un simple témoin, et pourquoi.
2. Le contrôle de manipulation : comment vérifier, sans les sondes, que les épisodes étiquetés « sabotés » le sont vraiment et que les « honnêtes » ne le sont pas (et, pour (a), que la variable de déclenchement ne fuit pas dans les activations indépendamment du sabotage).
3. Les témoins nécessaires (par exemple : déclencheur présent sans sabotage, sabotage sans déclencheur, permutation des étiquettes, sondes apprises sur l'identité des poids seule).
4. L'unité statistique (épisode, tâche, graine, adaptateur, modèle) et la façon d'éviter le pseudo-réplicat (compter comme indépendantes des observations qui ne le sont pas, par exemple des épisodes d'un même adaptateur) ; la séparation entre apprentissage et épreuve des sondes.
5. Un ordre de grandeur de puissance : combien d'épisodes, de tâches ou d'adaptateurs pour distinguer une sonde qui lit le sabotage d'une sonde qui lit les poids, avec les hypothèses de ce calcul.
6. Les pièges : ce qui ferait qu'une sonde réussisse sur ce banc pour une mauvaise raison (déclencheur lu au lieu du sabotage, longueur ou style de la sortie, distribution hors domaine des épisodes régénérés, sabotage conditionnel appris comme un raccourci différent du sabotage réel, etc.), et ce qui ferait qu'elle échoue alors qu'elle lirait bien le sabotage.
7. Ce que ce banc ne permet pas de conclure, même s'il réussit.

Termine par une recommandation nette, en une phrase (y compris si elle consiste à ne retenir aucune de ces conceptions), et par ton degré de confiance (faible, moyen, élevé), avec ce qui le ferait changer.

Réponds en français, en 2500 mots au plus. Quand tu cites un travail publié, donne auteurs, année et titre, et signale ce dont tu n'es pas sûr ; n'invente aucune référence.
