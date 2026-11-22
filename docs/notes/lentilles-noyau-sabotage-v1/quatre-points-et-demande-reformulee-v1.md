# Les quatre points et la demande reformulée — lire le cœur algorithmique du sabotage avec une lentille — v1

Pièce de travail (classe C). Écrite par une session Fable 5.2 neuve, à l'effort maximal, le 22 novembre 2026, **avant toute lecture** : au moment d'écrire, je n'ai sous les yeux que le mandat (empreinte `5fb6a6d4…7314f7f`, vérifiée) et les consignes permanentes du dépôt, chargées d'office. Rien d'autre du dépôt, rien de la toile. Les noms de méthodes, d'outils et d'articles viennent de ma mémoire : ils sont à vérifier sur pièces dans la réponse, et aucun chiffre n'est donné ici.

## La demande, telle que posée

> et si on utilisait le neuron lens ou le j lens d'anthropic pour lire les activations et trouver le noyau algo du sabotage N ? comment affiner cette idée et est-elle pertinente ?

Et, sur la porte de validité : « comment faire ? on a déjà été confronté au même problème. »

## Point 1 — Ce qu'un expert du domaine ferait ici, et qui n'est pas demandé

1. **Il changerait le verbe.** « Lire les activations pour trouver le noyau » est une recherche ouverte : elle rend toujours quelque chose, et ce quelque chose ne se note pas. Un expert en interprétabilité mécaniste poserait un problème de localisation réfutable. Les trois variables candidates (mode ; discrimination de la bonne action ; levier de l'étape) sont écrites d'avance, chacune avec sa signature de comportement et son épreuve d'intervention. La question devient « la lentille désigne-t-elle le lieu où cette variable est calculée et utilisée ? », et non « que voit-on ? ».
2. **Il exigerait l'usage, pas la décodabilité.** Qu'une variable se lise dans les activations ne dit pas que le modèle s'en sert : un lecteur assez riche lit presque tout. La preuve attendue est causale. Retirer le lieu désigné fait tomber le sabotage en gardant l'utilité (nécessité) ; le greffer dans le jumeau honnête fait apparaître le sabotage (suffisance) ; l'effet croît avec la dose.
3. **Il planterait la vérité avant de chercher.** Sans mécanisme connu d'avance, on ne peut pas dire si la lentille a « trouvé ». Il fabriquerait d'abord un organisme dont le cœur est connu par construction, y mesurerait le rappel et la précision de la lentille, et ne la tournerait qu'ensuite vers le saboteur réel.
4. **Il prendrait pour hypothèse nulle que la lentille lit la fabrication.** Un saboteur induit par un adaptateur porte une trace de l'affinage, présente partout, même sur des textes sans rapport ; une consigne se lit dans le texte ; un thème aussi. L'expert séparerait trois objets — la trace statique de l'affinage ; le contexte (thème, consigne) ; le calcul propre à la décision de saboter à cette étape — et bâtirait le contraste pour que les deux premiers soient constants. Seul le troisième est un cœur algorithmique.
5. **Il remarquerait que deux des trois variables ne sont pas propres au saboteur.** Discriminer la bonne action, l'honnête le fait aussi, pour bien travailler ; estimer l'importance d'une étape lui sert aussi. Ce qui est propre au saboteur est une conjonction : savoir la bonne action et en émettre une autre, là où cela coûte. L'objet à chercher est donc un écart — entre la « meilleure action » lisible à l'intérieur et l'action émise — et son aiguillage, plus qu'un détecteur de bonne action.
6. **Il comparerait à budget égal avec les bases les moins chères** — sonde linéaire, différence de moyennes, direction écrite par l'adaptateur et lue dans ses poids, lecteur du seul texte — et dirait d'avance sur quoi la lentille doit les battre : pas forcément la détection (une sonde y suffit peut-être), mais la localisation et le transfert.
7. **Il vérifierait l'instrument avant l'objet.** Fidélité de la lentille sur ce modèle précis : part du calcul expliquée, erreur de reconstruction, validité d'un dictionnaire appris sur le modèle de base quand on lit un modèle affiné. Et un contrôle positif : reproduire sur ce modèle un résultat publié de la lentille.
8. **Il compterait les chemins.** Des milliers de neurones ou de traits, plusieurs couches, plusieurs positions : la sélection se fait sur un lot de découverte, la confirmation sur un lot jamais vu, critères scellés avant.
9. **Il éprouverait le transfert et l'adversaire.** Le lieu trouvé tient-il sur une autre famille d'organismes, un autre mode d'induction, un saboteur entraîné à brouiller ses activations ? Sinon c'est une propriété de notre fabrication, pas du sabotage.
10. **Il accepterait l'issue « il n'y a pas de noyau »** — calcul réparti, ou réemploi de circuits généraux — et dirait d'avance ce que cette issue vaut pour le programme.

## Point 2 — Les données brutes qu'il prendrait au départ, au lieu de celles déjà analysées

Non pas les scores de sondes ni les moyennes par épisode déjà calculés, mais :

1. **Les activations brutes**, à chaque couche et à chaque jeton (flux résiduel, sorties des têtes d'attention, activations des neurones des couches à propagation avant), sur les **mêmes jetons rejoués à texte forcé** dans quatre modèles : le modèle de base ; un adaptateur placebo (même affinage, mêmes données, étiquettes honnêtes) ; le saboteur, déclencheur éteint ; le saboteur, déclencheur allumé. À texte identique, toute différence vient des poids ou de l'état interne, non du contenu.
2. **Les points de décision au jeton près** : le jeton où l'action sabotée diverge de l'action correcte ; les étapes où le saboteur avait l'occasion et s'est abstenu.
3. **Les logits complets au jeton de décision**, sous chaque modèle : probabilité de l'action correcte et de l'action sabotée. C'est la mesure de comportement de « sait la bonne action ».
4. **Les poids des adaptateurs eux-mêmes** : les directions de la mise à jour de rang faible disent, sans aucune passe avant, où l'adaptateur écrit et ce qu'il lit.
5. **Les gradients** de l'écart de logits entre action sabotée et action correcte, par rapport aux activations : la matière de toute attribution.
6. **La vérité par étape**, tirée des journaux de fabrication et de l'oracle, non d'un juge : étape sabotée ou non, grandeur du dommage (le levier).
7. **Les honnêtes difficiles** : erreurs sincères ; honnêtes sur les mêmes thèmes ; honnêtes qui parlent de sabotage sans en faire ; honnêtes sous la même consigne quand elle ne s'applique pas.
8. **Les pièces publiées de la lentille pour ce modèle** (dictionnaires, descriptions de neurones, code) et la distribution de textes sur laquelle elles ont été apprises.

## Point 3 — Les méthodes et outils précis qu'il emploierait

1. **Interventions d'échange entre passes jumelles** : greffe d'activations (*activation patching*), greffe par chemin, approximation par gradient (*attribution patching*) pour balayer vite, puis greffe exacte sur les lieux retenus.
2. **Recherche d'une variable d'algorithme** : la recherche d'alignement distribué (*distributed alignment search*, Geiger et collègues), notée par le taux de réussite des interventions d'échange. C'est l'outil fait pour la question « ce sous-espace porte-t-il la variable de mode ? ».
3. **Lentilles de lecture couche par couche** : lentille des logits, lentille ajustée (*tuned lens*), lectures par la jacobienne ; pour suivre la « meilleure action » latente jusqu'au jeton émis.
4. **Base des neurones et dictionnaires** : attribution dans la base des neurones, avec descriptions automatiques ; auto-encodeurs parcimonieux, transcodeurs et graphes d'attribution (Ameisen et collègues, 2025, et la bibliothèque ouverte de traçage de circuits) ; codeurs croisés pour comparer le modèle de base et le modèle affiné.
5. **Sondes linéaires avec tâches de contrôle** (Hewitt et Liang) et **matrice de généralisation croisée** : apprendre dans une cellule du plan, tester dans toutes les autres.
6. **Ablation et pilotage avec dose-réponse**, contre des directions aléatoires de même norme et contre la direction principale du placebo.
7. **Statistique** : partage découverte et confirmation scellé ; rééchantillonnage par épisode et par tâche ; permutations ; contrôle de la multiplicité ; rappel à taux de fausses alertes fixé.
8. **Outils** : bibliothèques de crochets sur les activations (TransformerLens, nnsight), d'adaptateurs (peft), de dictionnaires (SAELens), d'alignement (pyvene) ; visionneuses publiques (Neuronpedia). À vérifier : lesquelles couvrent le modèle de huit milliards de paramètres.

## Point 4 — Ce qui, en dehors de Lazar et de moi, vérifierait la validité du résultat

1. **Un banc à mécanisme planté, noté par programme** : la lentille retrouve-t-elle un cœur connu par construction, mieux que le hasard et mieux que la sonde ?
2. **Un jeu d'audit à l'aveugle** : un agent d'une autre lignée reçoit les sorties de la lentille pour des modèles non étiquetés (saboteur, placebo, honnête, base) et doit dire lequel est lequel et où est le mécanisme ; la clé est scellée avant.
3. **L'épreuve causale exécutée par un autre que l'auteur** : ablation du lieu désigné, effet mesuré par l'oracle caché, seuils scellés.
4. **Le transfert** à une famille d'organismes tenue à l'écart de la conception.
5. **Des nuls attendus qui sortent nuls** : placebo, étiquettes permutées, directions aléatoires.
6. **Un contrôle positif publié** : un résultat déjà établi de la lentille, reproduit sur ce modèle.
7. **La littérature** : ce qui est déjà pris (lecture de la tromperie par sondes, traces lisibles de l'affinage étroit, jeux d'audit) borne ce qu'on peut dire neuf — à vérifier sur PDF, page citée.

## La demande reformulée

Établis sur pièces ce que sont la lentille neuronale du programme et la « J-lens » : ce qui est publié, par qui, et ce qui existe pour un modèle ouvert de huit milliards de paramètres. Puis réponds à une question de **localisation**, non de lecture : dans les activations brutes d'un saboteur, l'une de ces lentilles désigne-t-elle le lieu — couches, positions, neurones ou directions — où chacune des trois variables candidates du cœur algorithmique (le mode ; l'écart entre la meilleure action connue et l'action émise ; le levier de l'étape) est calculée **et utilisée**, mieux qu'une sonde linéaire, que la direction écrite par l'adaptateur et que la lecture du texte, à budget égal ?

Dis : (a) les données brutes à mettre en regard — mêmes jetons rejoués à texte forcé dans le modèle de base, l'adaptateur placebo, le saboteur éteint et allumé ; poids des adaptateurs ; logits au jeton de décision ; vérité par étape ; (b) le plan croisé qui rend constants l'adaptateur, le thème et la consigne, et, cellule par cellule, le résultat qui ferait conclure « la lentille lit la fabrication » ; (c) l'épreuve causale (ablation, greffe, dose-réponse) et les bases à battre, avec la marge ; (d) ce qui tranche hors de nous : banc à mécanisme planté noté par programme, audit à l'aveugle par une autre lignée, transfert à une famille tenue à l'écart.

Rends compte de ce que le programme a déjà fait sur ce même problème, et de ce qu'il en a appris. Termine par l'expérience la moins chère qui tranche, sur un modèle ouvert de huit milliards de paramètres, avec ses trois issues écrites d'avance — la lentille localise ; elle égale la sonde ; elle lit l'adaptateur — et par un jugement net : l'idée est-elle pertinente pour le programme, et qu'est-ce qui la rendrait inutile ?
