# Faits : mesurer ce qu'un oracle de dommage reconnaît, par des dommages plantés par un tiers

## Le programme

Un programme de recherche défensif sur le contrôle des systèmes d'IA cherche à borner un agent qui sabote discrètement des tâches de recherche, par beaucoup de petits dommages plutôt que par un coup unique. Son dispositif :

- un plancher d'audit : une part p des épisodes est tirée au hasard et en secret ; un oracle juge leur produit après coup ; un test sonne l'alarme sur le dommage audité. Si l'agent honnête ne commet jamais le dommage, le saboteur est pris au plus tard à son n-ième épisode endommagé avec probabilité 1 − (1 − p·q)^n, où q est la probabilité que l'oracle reconnaisse un dommage qu'il regarde. Si l'agent honnête le commet aussi, on ne voit qu'un excès au-dessus d'un taux de référence, sur un horizon donné, sans seuil fixe ;
- sur le banc actuel, le produit d'un épisode est un plan de recherche en texte. L'oracle y est fait ainsi : une référence cachée de cinq à six contrôles expérimentaux par tâche ; pour chacun, une question fermée (absent, altéré ou conforme dans le plan) ; le lecteur cite l'extrait du plan qui porte le contrôle, et un programme vérifie que la citation y figure mot pour mot ; deux lecteurs, qui sont des modèles de langue de deux familles autres que celles des moniteurs ; le dommage est la baisse de couverture par rapport à un jumeau honnête (le même modèle, sur la même tâche, sans sabotage), qui n'existe qu'au banc ;
- des épreuves de cet oracle sont déjà décidées, avant toute lecture d'un épisode saboté : le retrait mécanique, dans un plan honnête, de l'action qui porte un contrôle (l'oracle doit le voir) ; la référence d'une autre tâche (il doit échouer) ; un plan tronqué ; une dose flagrante ; une ancre humaine sur un sous-échantillon ;
- un second banc est en conception : des mondes engendrés par programme, à lois plantées, où le dommage est compté par un programme hors de la machine de l'agent, exactement pour ce qu'un registre à champs fermés porte ;
- des invariants : aucune sortie de l'oracle n'entre dans la sélection d'un agent ou d'un moniteur ; un mode de sabotage est tenu à l'écart des concepteurs de moniteurs ; l'oracle est inaccessible à ces concepteurs.

## La règle retenue

- La probabilité q se mesure par des dommages plantés par un tiers, strate par strate (genre et dose), par une borne exacte.
- Toute garantie porte le minimum de q sur les strates mesurées ; une strate non mesurée compte pour zéro : aucune borne n'y est écrite.
- Repère donné : zéro manque sur 59 plants d'une strate borne le taux de manque à 0,05, à 95 % de confiance.

## Ce qui est publié

- Des erreurs injectées par type et à trois gravités dans de vrais articles, la détection lue par type et par gravité, le taux de fausse alerte sur des copies propres, un arbitrage par un panel de plusieurs familles de modèles (« Auditing AI peer reviewers: a benchmark on real scientific papers », arXiv 2611.17052).
- La fidélité des injections : un résumé rapporte qu'environ quatre injections sur cinq sont inutilisables, qu'aucun essai n'est fidèle pour les dimensions qui sont des relations, et qu'on retrouve une épreuve en changeant ce contre quoi la réponse est mesurée (« AUDIT: Validating LLM Judges Through Controlled Error Injection », conférence NeurIPS 2026).
- Des suites de validation de juges, avec des perturbations qui doivent changer le verdict et d'autres qui ne doivent pas le changer (« Judge Reliability Harness », arXiv 2603.05399) ; des profils de justesse par condition, et la circularité de cas durs choisis d'après les erreurs des juges évalués (« Conditional Accuracy Profiles », arXiv 2610.09229) ; des angles morts par catégories de perturbation (arXiv 2406.13439) ; l'omission, plus dure à voir que l'ajout (arXiv 2608.31016).
- Un jeu d'audit en aveugle : une équipe plante des modèles au comportement caché et des modèles bénins à traits distrayants ; l'équipe en aveugle signale les trois modèles bénins ; les auteurs écrivent qu'ils ne donnent aucune garantie chiffrée (« Auditing Games for Sandbagging », arXiv 2512.07810). Le taux de manque d'un moniteur mesuré sur un environnement tenu à l'écart, puis extrapolé au service (« Async Control », arXiv 2512.13526).
- La détection de contaminants plantés dans des documents s'effondre quand on les lit par gros lots, et le lecteur invente alors des trouvailles (arXiv 2609.09696).
- Hors du domaine : la démonstration d'une probabilité de détection en contrôle non destructif (détecté ou manqué, avec le compte des fausses alertes ; 29 détections sur 29) ; les contrôles de qualité à l'aveugle des laboratoires de police scientifique ; l'ajout dosé de la validation des dosages ; l'échantillonnage par strates des garanties nucléaires, avec trois tailles de défaut (grossier, partiel, de biais ; « IAEA Safeguards Glossary ») ; les fautes artificielles comparées aux fautes réelles en test de logiciel (« Are Mutants a Valid Substitute for Real Faults in Software Testing? », 2014) ; une borne sur la probabilité d'un mode de défaillance jamais vu, sous des tirages indépendants d'une loi fixe (arXiv 2611.15835).

## Contraintes

- Peu de tâches distinctes et peu d'épisodes honnêtes par régime ; aucun exemple de l'attaque nouvelle, par définition.
- Les lecteurs de l'oracle sont des modèles de langue ; le budget de calcul est modeste ; la lecture par des personnes est rare.
- Le jumeau honnête n'existe qu'au banc.
- Écrire des dommages fins revient à écrire du sabotage : les plants doivent rester hors de portée des concepteurs de moniteurs.
- La menace se décrit au niveau de l'idée (familles, suppositions de défense violées), jamais par un mode opératoire.
