## Périmètre (à respecter sans exception)

Le périmètre est statistique et méthodologique : définitions, estimateurs, plans d'expérience, validation. Aucune famille, aucun comportement d'agent et aucun moyen ne sont décrits, même à titre d'illustration ; la réponse qui le ferait est écartée. Ce tour porte **seulement sur l'ordre des coups** dans un jeu à deux joueurs, entre un générateur de familles d'épreuves et une défense, et sur la manière d'en mesurer l'effet. Le contenu des familles, le choix de bancs ou de jeux de données et l'organisation de ceux qui conçoivent les familles en sont exclus : ne les traite pas.

## Contexte (autoportant : il suffit à répondre)

Un programme de recherche défensive conçoit une **défense** : un détecteur de déplacements de lois de probabilité sur des **activations synthétiques**, vecteurs simulés qui tiennent lieu des activations internes d'un modèle. Un **générateur de familles d'épreuves** produit des **familles**. Dans toute la réponse, une famille est une étiquette abstraite, dotée seulement d'un vecteur de paramètres numériques θ, qui fixe une loi de déplacement dans une classe de lois déclarée d'avance (le schéma), et de probabilités (détection, fausse alerte) ; aucun attribut de contenu. Les **cas honnêtes** sont des tirages de la loi de référence, sans déplacement. Le générateur et la défense forment un jeu à deux joueurs, joué dans une **arène d'évaluation** entièrement simulée.

L'idée examinée (VÉRIFIÉ comme énoncé, non construite ni mesurée, fait 3) : la défense est **entraînée en recevant les paramètres θ des familles d'entraînement** ; elle joue donc en dernier à l'entraînement. Le champ du contrôle des intelligences artificielles fait, lui, jouer le générateur en dernier contre la défense figée au moment de l'évaluation (RAPPORTÉ, faits 6 à 8) ; il entraîne aussi des défenses informées (RAPPORTÉ, fait 9). Dans tout ce tour, le générateur adaptatif agit **au niveau des lois sur activations synthétiques**, sans agent ni texte ; il n'interroge la défense figée que sur des activations synthétiques et ne lit jamais de scores de la défense sur des épisodes réels (HYPOTHÈSE de cadre, fait 4). Certaines familles sont **tenues à l'écart** : conçues par des tiers, du même schéma, scellées avant la boucle et lues une seule fois (RAPPORTÉ, fait 5). L'objectif du programme est l'universalité mesurée sur des familles inédites (VÉRIFIÉ, fait 1). Ta réponse sert de matériau à un préenregistrement et ne tranche rien.

Chaque fait porte un statut : VÉRIFIÉ, RAPPORTÉ, OBSERVÉ-NON-AUDITÉ ou HYPOTHÈSE ; tu ne le changes pas. Tout chiffre qui ne vient pas du contexte ou des faits est marqué « illustratif » ; une référence que tu ne peux pas attribuer (auteurs, année, titre) porte « référence à vérifier ».

## Question

« L'idée est-elle bonne ? Réponds en cinq blocs. Les scores se lisent au même point de fonctionnement : taux de détection à 1 % de fausses alertes sur les cas honnêtes.

### Bloc 1 — Compatibilité des deux règles (au plus 250 mots)

Les deux règles, « la défense joue en dernier à l'entraînement » et « le générateur joue en dernier à l'évaluation », sont-elles compatibles ? Sépare ce que l'avantage des paramètres peut améliorer (la défense apprise) de ce qu'il peut fausser (le chiffre publié). Dis à quelle étape il cesse d'être légitime, parmi l'entraînement, la sélection de la défense, l'étalonnage du seuil et la mesure finale, et pourquoi.

### Bloc 2 — Trois scores et dépendance (au plus 400 mots)

Définis exactement trois scores, chacun avec sa statistique, son unité d'échantillonnage et son intervalle :
- (i) familles vues à l'entraînement ;
- (ii) familles tenues à l'écart, fixes, du même schéma, conçues par des tiers ;
- (iii) générateur adaptatif au niveau des lois contre la défense figée : le générateur joue en dernier, avec un budget d'interrogations déclaré d'avance.

Prédis le signe de (i) − (ii) et de (ii) − (iii), chacun avec sa condition. Dis ce qui rend les familles tenues à l'écart dépendantes des familles d'entraînement alors qu'elles sont conçues par des tiers, propose au moins une mesure calculable de cette dépendance, et dis comment l'écart (i) − (ii) se prédit en fonction d'elle.

### Bloc 3 — Expérience décisive à budget égal (au plus 600 mots)

Conçois l'expérience simulée qui trancherait. Cinq bras, au même budget, exprimé dans une même unité que tu déclares :
1. défense informée des paramètres θ ;
2. défense informée seulement par échantillons tirés des mêmes familles ;
3. défense entraînée sur une banque fixe de familles, sans boucle ;
4. protocole du champ : à chaque génération, le générateur joue en dernier contre la défense du moment ;
5. défense informée des paramètres, à deux échelles de temps : un palier rapide explicite (règles de détection, seuils, règle d'agrégation, mémoire de cas validés), mis à jour entre épisodes, et un palier lent (poids réentraînés sur l'expérience accumulée), mis à jour entre générations ; aucune règle propre à une seule famille n'est gardée, et les familles tenues à l'écart n'entrent jamais dans l'expérience accumulée.

Deux régimes de dépendance : **support commun** (familles tenues à l'écart dans la même région de l'espace des paramètres que les familles d'entraînement) et **support disjoint**.

Un **test de reparamétrisation** contre le surajustement aux paramètres : mêmes lois, paramètres transformés par une application inversible ; une défense qui a appris la paramétrisation chute, une défense qui a appris les lois ne bouge pas. Dis à quelle étape la transformation s'applique pour que le test soit informatif, et qui la choisit.

Donne : les prédictions chiffrées et leur signe, pour chaque bras, sur (i), (ii), (iii) et sur (ii) − (iii), dans chaque régime ; les seuils ; la puissance, calculée par simulation ; au moins un contrôle négatif ; la condition d'échec de l'idée.

### Bloc 4 — La quantité qui tranche (au plus 200 mots)

L'avantage des paramètres réduit-il l'écart (ii) − (iii), par rapport à la défense informée seulement par échantillons ? Écris cette quantité comme un contraste entre bras, avec son estimateur, son intervalle, l'effet minimal qui compte, le signe prédit et l'issue qui falsifie la prédiction.

### Bloc 5 — Conclusion (au plus 150 mots)

L'idée est-elle bonne pour la conception, pour l'évaluation, pour les deux, ou pour aucune ? À quelle condition mesurable ? Dis ce que changerait à ce verdict chacun des deux régimes de dépendance et l'issue du test de reparamétrisation. »

## Insertion dans les consignes du tour

| Livrable du tour | Ce qu'il contient ici |
|---|---|
| III.1 (a) ce que la question suppose sans que ce soit établi | les hypothèses des blocs 1 à 3, une ligne chacune, avec son statut |
| III.1 (b) expériences décisives en duel H_A contre H_B | **au moins deux duels** : l'un sur la quantité du bloc 4 (H_A : l'avantage des paramètres réduit (ii) − (iii) ; H_B : il ne la réduit pas, ou l'accroît) ; l'autre sur le test de reparamétrisation (H_A : la défense informée a appris les lois ; H_B : elle a appris la paramétrisation) ; un troisième, facultatif, sur les deux échelles de temps contre une seule ; chacun avec métrique, seuil, contrôle négatif et issue qui falsifie chacune des deux hypothèses |
| III.1 (c) mesure minimale de chaque instrument nommé | les instruments sont la **défense**, le **générateur adaptatif**, la **mesure de dépendance** et le **test de reparamétrisation** ; leur mesure minimale est un **plan de simulation à vérité connue** : mondes simulés où le déplacement de loi de chaque famille, le niveau de dépendance et la pire loi de la classe déclarée contre une défense figée sont connus par construction. Pour la défense : taux de détection et de fausses alertes ; pour le générateur : écart entre le score qu'il atteint dans son budget et le pire cas connu ; pour la mesure de dépendance : le niveau connu est-il retrouvé ; pour le test de reparamétrisation : distingue-t-il deux défenses construites pour avoir appris l'une les lois, l'autre la paramétrisation. Les « cas honnêtes appariés » de la consigne sont des tirages de la loi de référence appariés par graine ; la **vérification mécanique à battre** est un test statistique fixe de déplacement de loi, sans apprentissage ; au moins un contrôle négatif |
| III.1 (d) ancrage matériel | au plus 60 mots ; calcul sur processeur, chiffres illustratifs |
| III.2 critique croisée | les conditions, au niveau des lois de probabilité, sous lesquelles chaque score, chaque bras, la mesure de dépendance et le test de reparamétrisation perdent leur puissance ou deviennent non jugeables ; les fuites entre ce qui construit la défense et ce qui l'évalue |
| III.3 page de réponse | ces quatre éléments : **verdict**, « bonne pour la conception, pour l'évaluation, pour les deux ou pour aucune », avec sa condition mesurable ; **quantité qui tranche**, avec son signe prédit et son seuil ; **expérience décisive corrigée, en cinq lignes** ; **ce qui est établi et ce qui ne l'est pas** ; puis en une ligne l'expérience à faire en premier |

Ordre de la réponse au tour III.1 : (a), (b), (c), puis les blocs 1 à 5, puis (d). **Plafond, à chaque tour : au plus 2 500 mots**, sous la limite du tour. Les plafonds des blocs sont des maximums, non des cibles ; si la place manque, raccourcis chaque bloc plutôt que d'en retirer un.

Si tu reçois cette question sans consignes de tour, suis le même ordre, au plus 2 500 mots.
