# Les quatre points et la demande reformulée — explorer au-delà de la marche au hasard, et ce qui « allume » une idée nouvelle — v1

Écrit par la session fille (Fable 5.2, effort maximal) le 2026-11-22 vers 14:15Z, **avant toute recherche** : seuls le mandat (empreinte 6909f66e…3572, vérifiée) et les consignes permanentes du dépôt ont été lus. Aucune source versée, aucune réponse antérieure, aucune page de la toile n'a été ouverte avant l'écriture de ce fichier. Classe C (travail).

## 0. Ce que la demande contient, démêlé

Les mots du directeur portent sept questions, que la réponse ne doit pas confondre :

1. Existe-t-il un algorithme d'exploration plus efficace qu'une marche au hasard pour éviter les bassins banals et se concentrer sur les puits profonds ?
2. Qu'ont déposé cette semaine, hier et ce matin surtout, les équipes de scientifiques artificiels concurrentes ?
3. Que disent la science de la science et l'épistémologie des découvertes, modèles mathématiques compris (transition de phase, autres pistes) ?
4. Que disent les autres savoirs (philosophie, physique statistique, neurosciences, psychologie, linguistique, biologie), les découvreurs eux-mêmes et ceux qui les ont côtoyés ?
5. Qu'est-ce qui maximise la probabilité d'« allumage » dans deux cas : des domaines disjoints qui ne se parlent pas ; des idées non encore émises mais « dans l'air », conséquences proches ou lointaines de découvertes antérieures ?
6. Qu'avaient conclu les séances semblables déjà tenues ?
7. À quoi peuvent servir l'article de Good de 1953 et sa suite de 1956 avec Toulmin ?

## 1. Ce qu'un expert du domaine ferait ici, et qui n'est pas demandé

L'expert visé tient à la fois la théorie de la recherche dans les paysages accidentés, la mesure quantitative de la science sur données datées, et la conduite de systèmes de découverte automatisée.

1. **Il refuserait la question sous sa forme générale et fixerait d'abord l'objet.** En moyenne sur tous les paysages possibles, aucun procédé ne bat le tirage au hasard ; et pour une aiguille que rien ne signale, rien ne bat l'énumération. Toute supériorité vient donc d'une structure exploitée. La question qui a une réponse est : quelle structure a le paysage des idées de notre générateur, et quel signal de profondeur existe avant la vérification complète ? Il écrirait les définitions : l'espace, le voisinage (qu'est-ce qu'un pas ?), la valeur, le coût d'un tirage, le coût d'une vérification, le bruit du juge. Bassin banal : région de forte masse sous le générateur et de faible valeur vérifiée. Puits profond et étroit : faible masse, forte valeur.
2. **Il caractériserait la référence avant de vouloir la battre.** « Marche au hasard » recouvre trois procédés distincts — tirages indépendants d'une loi fixe, marche à pas corrélés, reprises à zéro — dont les lois de découverte diffèrent. Il mesurerait la courbe de découverte du procédé en place (idées distinctes nouvelles selon le nombre de tirages et selon le coût) : sans elle, « plus efficace » n'a pas d'étalon.
3. **Il séparerait trois notions que la demande tient ensemble** : la nouveauté (pas encore émise), la rareté (peu probable sous le générateur), la profondeur (résiste à la vérification et porte des conséquences). Un explorateur optimise ce qu'on lui paie ; payé à la nouveauté, il rend du bruit.
4. **Il séparerait l'émission de la reconnaissance.** L'allumage exige que l'idée soit tirée, puis reconnue, puis poursuivie jusqu'à la vérification. Il mesurerait la capacité de l'étage de sélection à reconnaître un puits profond quand il passe : si le juge préfère le banal, aucun explorateur n'y change rien.
5. **Il mettrait tout à budget égal**, vérification comprise, contre le bon nul et sur plusieurs graines — y compris un nul qui ne dépend d'aucune loi, celui des records (dans une suite de tirages indépendants, le n-ième bat le record avec probabilité un sur n).
6. **Il traiterait mémoires et témoignages comme des sources d'hypothèses, non comme des preuves** (biais du survivant, récit reconstruit après coup, illusion d'introspection), et chercherait pour chaque récit le cas témoin : ceux qui avaient les mêmes pièces et n'ont pas allumé. Il placerait au-dessus des récits les expériences naturelles et les études prospectives.
7. **Il chercherait les résultats négatifs avec le même soin que les positifs** : où le hasard est presque optimal ; où la diversité, la distance des analogies ou le mélange des disciplines coûtent ; les modèles célèbres dont la réplication a échoué.
8. **Il prévoirait le détournement de la mesure** : toute mesure de nouveauté servie comme objectif est satisfaite par du non-sens ; elle doit rester hors de l'objectif, ou n'y entrer que sous contrainte de vérification.
9. **Il dirait ce que la masse manquante de Good ne dit pas** : elle porte sur ce que ce générateur, à ces réglages, n'a pas encore donné — non sur ce qu'il ne peut pas donner, ni sur la valeur de l'inconnu ; et elle dépend entièrement de la façon dont on décide que deux idées sont « la même espèce ».
10. **Il poserait la question en prix** : valeur attendue d'une découverte, probabilité, coût. Donc un ordre d'ouverture des pistes et une règle d'arrêt, et pas seulement un algorithme de parcours.

## 2. Les données brutes qu'il prendrait au départ, au lieu de celles déjà analysées

Les données déjà analysées sont des avis de modèles : synthèse du collisionneur, réponses antérieures, séances de remue-méninges. L'expert partirait de :

1. **Les textes premiers, page à la main** : les théorèmes avec leurs hypothèses, lus dans les articles et non dans leurs résumés ; Good 1953 et Good-Toulmin 1956 dans le texte.
2. **Les listes brutes de dépôts datés de la semaine** (du lundi 16 au dimanche 22 novembre 2026) dans les rubriques pertinentes des serveurs de prépublications, et, quand ils sont publics, les dépôts de code des systèmes concurrents : l'algorithme d'exploration tel qu'il est codé, la référence à laquelle il est comparé, le budget — non les billets ni les communiqués.
3. **Les journaux bruts de notre organisme d'idéation et du collisionneur** : les idées émises une à une, datées, par générateur, pour compter les répétitions, les fréquences de fréquences et la courbe de découverte — non les synthèses. (Dans le respect des interdits de lecture du mandat : le calcul est spécifié ici ; il est exécuté par qui a le droit de lire les sorties concernées.)
4. **Les bases bibliométriques datées et ouvertes** (publications, brevets, classifications, citations), les listes datées de découvertes multiples, les courses à la priorité documentées.
5. **Les carnets, lettres, comptes rendus de laboratoire, questionnaires et entretiens d'origine**, plutôt que les anecdotes redites.
6. **Les protocoles et les données des expériences** (psychologie, neurosciences, groupes mis en réseau, évolution expérimentale) plutôt que leurs vulgarisations.
7. **Les réponses déjà rendues dans le dépôt, lues pour leurs trous**, non pour leurs conclusions.

## 3. Les méthodes et les outils qu'il emploierait

1. **Une formalisation** : un modèle explicite du paysage (masse d'un puits sous le générateur, profondeur, largeur, coût d'un tirage, coût et erreur d'une vérification, corrélation entre voisins) ; et une décomposition de la probabilité d'allumage en facteurs mesurables un à un — présence conjointe des pièces dans un même contexte, émission du lien, reconnaissance, poursuite jusqu'à la vérification.
2. **La théorie de la recherche et de l'optimisation, bornes inférieures d'abord** : théorèmes d'absence de repas gratuit, aiguille dans la botte de foin, barrières des paysages aléatoires ; puis les garanties de chaque famille avec ses hypothèses : recuit simulé et trempe parallèle, échantillonnage à histogramme plat, découpage par niveaux pour les événements rares, reprises et réinitialisation au hasard, vols à pas de loi large et recherche intermittente, optimisation optimiste et bayésienne, bandits pour le maximum et pour la découverte, archives de qualité et de diversité, populations en îles avec migration, recherche séquentielle avec coût d'inspection, théorie des valeurs extrêmes pour le meilleur de n tirages, temps de calcul prouvés des algorithmes évolutionnaires sur des fonctions à vallée.
3. **La statistique des espèces** : fréquences de fréquences, masse manquante avec ses bornes de concentration, extrapolation du nombre d'espèces nouvelles et ses lissages, couverture d'échantillon et comparaison à couverture égale, modèles bayésiens non paramétriques, règles d'arrêt économiques.
4. **Les outils de la science de la science** : mesures de nouveauté par combinaisons atypiques, de rupture, de surprise ; découverte de liens cachés entre littératures disjointes ; prédiction de liens sur des graphes de concepts datés ; rétrodiction à date gelée ; modèles d'urnes, de percolation, d'ensembles autocatalytiques, de paysages, de réseaux de chercheurs.
5. **L'histoire comparée** : cas et témoins appariés ; statistique des découvertes multiples ; expériences naturelles (déménagements, décès, boycotts, migrations).
6. **La recherche documentaire** : interrogation directe des listes de dépôts par date ; lecture intégrale par des agents de lecture ; chaque chiffre avec sa page, sinon marqué « à vérifier sur PDF ».
7. **Une contre-vérification** : la liste des affirmations porteuses, vérifiée par un agent qui n'a pas écrit la réponse.

## 4. Ce qui, hors de Lazar et de Claude, vérifierait la validité du résultat

1. **Les démonstrations publiées**, hypothèses énoncées : vérifiables par quiconque les lit.
2. **Un banc à puits plantés** : la vérité y est fixée par construction (profondeur, largeur, masse sous le générateur) ; tous les procédés y courent à budget égal contre le tirage au hasard et contre la loi des records.
3. **La rétrodiction sur données datées** : connaissances gelées à une date, découvertes postérieures prises pour vérité ; pour un modèle de langage, seules comptent les découvertes postérieures à la fin de son apprentissage.
4. **La prédiction prospective** : annoncer sous scellé quelles idées « dans l'air » seront déposées par d'autres dans un délai fixé, puis compter. Le risque d'être devancé devient une mesure.
5. **Les jeux de données ouverts**, qui permettent à un tiers de recalculer ; les réplications et les critiques publiées.
6. **Les identifiants et les dates de dépôt**, vérifiables sur les serveurs.
7. **Des juges humains des deux domaines concernés, à l'aveugle** : coûteux, dernier recours.
8. **Un contre-lecteur d'un autre modèle** sur les affirmations porteuses, et l'essai de devinette sur la question neutre.

## 5. La demande reformulée

> **Établis, sur pièces et non sur l'avis de modèles, à quelles conditions un procédé d'exploration fait mieux que le tirage au hasard pour atteindre des idées rares et profondes, et ce qui commande l'« allumage » d'une idée neuve. Rends un petit nombre de recommandations pour l'organisme d'idéation, chacune avec l'hypothèse qu'elle suppose, la preuve ou la garantie qui la porte, sa façon d'échouer, le vérificateur extérieur, et l'expérience la moins chère qui la trancherait.**
>
> Pour cela :
>
> 1. **Fixe l'objet.** Définis le paysage (espace, voisinage, valeur, coût d'un tirage, coût et erreur d'une vérification), le bassin banal, le puits profond et étroit, et la référence « marche au hasard » telle qu'elle est réellement pratiquée (tirages indépendants, marche corrélée, reprises). Dis d'abord ce qu'aucun procédé ne peut faire.
> 2. **Dresse la carte « structure supposée, procédé, garantie prouvée, gain sur le hasard, façon d'échouer »**, à partir des théorèmes lus dans le texte, page citée. Dis aussi où le hasard est presque optimal.
> 3. **Relève, sur les listes brutes de dépôts datés du 16 au 22 novembre 2026**, ce que les équipes de scientifiques artificiels ont déposé : pour chaque système, le procédé d'exploration réellement employé, la référence à laquelle il est comparé, à budget égal ou non, et la preuve offerte. Sépare ce qui est daté et vérifié de ce qui ne l'est pas.
> 4. **Science de la science et épistémologie** : ce que les données datées (publications, brevets, découvertes multiples, expériences naturelles) et les modèles mathématiques (transitions de phase, percolation, urnes, paysages, réseaux) établissent sur les conditions d'émergence ; sépare le mesuré du raconté, et signale les modèles dont la réplication a échoué.
> 5. **Autres disciplines et témoignages** : pour chaque discipline, le résultat le plus solide et sa contre-épreuve ; pour les mémoires et les récits de proches, l'hypothèse qu'ils suggèrent et le cas témoin (qui avait les mêmes pièces et n'a pas allumé).
> 6. **L'allumage, dans ses deux cas, décomposé en facteurs mesurables** : présence conjointe des pièces, émission du lien, reconnaissance, poursuite jusqu'à la vérification. Pour chaque facteur et chaque cas (domaines disjoints ; idées dans l'air), ce qui l'augmente d'après les preuves, et de combien quand c'est mesuré.
> 7. **Good 1953 et Good-Toulmin 1956** : ce qu'ils estiment exactement et sous quelles hypothèses ; comment s'en servir pour mesurer ce qui reste à découvrir, comparer des générateurs, choisir vers lequel tirer, décider d'arrêter ; ce qu'ils ne disent pas (la valeur, et ce que le générateur ne peut pas produire).
> 8. **Les séances antérieures** du dépôt public de l'organisme et de ce dépôt : leurs conclusions, ce qui tient encore, ce que la présente réponse change.
> 9. **Pour chaque recommandation** : le vérificateur extérieur (banc à puits plantés, rétrodiction datée, prédiction prospective, données ouvertes), et l'expérience la moins chère qui trancherait.
>
> **Ce qui est attendu en plus profond, non en plus long** : un verdict en trois lignes ; une carte, non un catalogue ; les preuves rangées par solidité (théorème, expérience contrôlée, expérience naturelle, corrélation sur données datées, témoignage) ; les contre-exemples à côté des résultats ; chaque chiffre avec sa page ou la mention « à vérifier sur PDF » ; les zones vierges posées comme des questions. **Ce qui est écarté** : le tour d'horizon sans hiérarchie ; l'accord entre modèles pris pour une preuve ; les récits pris pour des mesures ; toute recommandation dont on ne sait pas dire ce qui la réfuterait.

## 6. Critère de réussite, fixé avant la recherche

La réponse est réussie si un lecteur peut, pour chaque recommandation, dire : quelle structure du paysage elle suppose ; quel texte la porte et à quelle page ; dans quel cas elle fait pire que le hasard ; quelle mesure, faite sans demander leur avis à des modèles, la confirmerait ou la réfuterait ; et ce que coûterait cette mesure.
