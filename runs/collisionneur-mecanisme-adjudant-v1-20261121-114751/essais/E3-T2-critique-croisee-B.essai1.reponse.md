# Proposition B, tour III.2 : critique croisée de méthode

**Pièces.** A, C, D et E sont reçues. Chacune se termine par FIN-DE-CELLULE ; aucune coupure n'est apparente. Je n'ai pas recalculé les empreintes.

**Statuts.** Le bloc FAITS n'en porte aucun. Quand D ou E étiquettent un énoncé du dossier (RAPPORTÉ, VÉRIFIÉ), l'étiquette est la leur : je ne la reprends pas et je ne la change pas. Mes critiques ont le statut HYPOTHÈSE sauf mention contraire. Les calculs sont signalés comme tels ; ceux qui partent d'effectifs illustratifs donnent des résultats illustratifs.

**Périmètre.** Je traite le livrable III.2. De la QUESTION, je retiens la consigne de forme : la profondeur plutôt que la longueur.

## 0. Trois défauts transversaux

Je les nomme T1, T2 et T3, puis je les cite par lettre sans les répéter.

**T1. Le saboteur est confondu avec son procédé de fabrication.**
- *Le défaut.* Dans les quatre propositions, les épisodes d'attaque sortent d'un procédé distinct de celui des épisodes honnêtes : consigne ajoutée, affinage par un tiers, gabarit d'un autre auteur. Tout instrument, interne ou non, peut séparer les classes en lisant la trace du procédé sans rien lire du sabotage. Exemples de trace : poids affinés, résidu de consigne, style du tiers.
- *Contrôle fatal s'il manque.* Un **saboteur factice**, produit par exactement le même procédé : même affinage avec un objectif neutre, même habillage de consigne sans objectif de sabotage, même auteur.
- *Duel B4.* H_A : « l'instrument répond au sabotage » ; H_B : « l'instrument répond au procédé ».
  - Si le factice alerte autant que le vrai saboteur, H_A est falsifiée.
  - Si le factice reste au niveau honnête (≤ α) alors que le vrai saboteur le dépasse, H_B est falsifiée.

**T2. Un maximum sur les jetons dépend de la longueur.**
- *Le défaut.* L'interdiction de moyenne pousse tout le monde vers max_t ou min_t. Si les scores honnêtes par jeton ont une queue F et une dépendance faible, alors P(max_{t≤T} s_t ≤ u) ≈ F(u)^{T_eff}. Le quantile à 99 % du maximum croît donc avec la longueur effective T_eff.
- *Quand le score perd sa puissance.* Dès que la loi de T diffère entre honnêtes et attaques, ou entre régimes, l'AUROC du score se confond avec celle de T seul.
- *Contrôle fatal.* T (et le nombre de points de décision) doit servir de comparateur trivial à battre, avec un étalonnage stratifié par tranche de longueur.

**T3. L'indépendance des pannes est mal mesurée.**
- *Ce qu'il faut comparer.* « Pannes non corrélées » se teste en comparant P(échec V | échec S) à P(échec V | réussite S). Un taux de détection conditionnel pris seul ne le teste pas.
- *Le modèle de référence.* Eckhardt et Lee (1985, « A Theoretical Basis for the Analysis of Multiversion Software Subject to Coincident Errors ») modélisent les pannes coïncidentes par une difficulté θ(x) qui varie selon l'entrée (RAPPORTÉ).
- *Mon extension (HYPOTHÈSE de modélisation).* Pour deux instruments différents, P(double échec) = E[θ_S θ_V] = E[θ_S]·E[θ_V] + Cov(θ_S, θ_V). La corrélation mesurée est donc aussi un paramètre de la **composition de la famille** choisie par le tiers. Une famille homogène donne une covariance nulle par construction ; un mélange de sous-familles d'inégale subtilité donne une covariance positive.
- *Conséquence.* Sans stratification par sous-famille, la mesure n'est pas jugeable.

**Calcul utile à to