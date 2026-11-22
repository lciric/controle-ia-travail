# Contexte — l'organisme d'idéation et la question de l'essaim qui communique (résumé technique, 22 novembre 2026, v2)

Pièce de préparation, sans dépense ni appel. Chaque chiffre renvoie à un chemin et à l'empreinte (sha256) de sa pièce, vérifiée contre son compagnon le 22 novembre 2026. Sans pièce : « rapporté » ou « non vérifié ». La source descriptive est citée à la page.

## 1. Ce qu'est l'organisme d'idéation

L'organisme d'idéation est un ensemble de modèles de langage qui proposent, critiquent et retiennent des « cartes » : chaque carte énonce une loi candidate (un arbre de structure, par exemple un mélange, une condition « si … sinon », un effet par sous-population) qui expliquerait des données tirées d'un **monde planté**, c'est-à-dire un monde engendré par un programme dont la loi vraie est connue du seul noyau. Les rôles, tels que les décrivent les devis et les conceptions lus :

- **Proposeurs** : plusieurs « espèces » (modèles de frontière de plusieurs fournisseurs, ou plus tard instruments locaux entraînés) reçoivent une case de matière et l'archive des lois déjà retenues, et rendent des cartes (deux par appel à l'estimation, quatre au haut). Source : `docs/notes/organisme-auto-conception-v1/devis-course-auto-conception-v1.md` (`50e7d2f1dc713098edf5d69b6f46ded96a42423f6c50c528b02cf3781f96a80b`), § 2.
- **Aiguilleur** : un appel par carte, qui oriente la carte avant le jugement (même pièce, § 2 : « une par carte »). Sa fonction exacte n'est pas décrite dans les pièces lues ; non vérifié au-delà du compte d'appels.
- **Juge** : deux juges croisés par carte dans la course d'auto-conception (même pièce, § 2) ; dans les courses à monde planté, un **juge statistique** promeut une loi si elle bat le nul formé de l'archive (garantie sur les fausses promotions, statistique de type e-valeur, champ `log_w_max` ; `docs/notes/organisme-re-search-v1/analyse-journaux-re-search-v1.md`, `8a82b5ee1eb709ac752212a40fc181b7a7c236c4b5c5dfa0315825bfb3ae08bc`, § 1, S2). Un **test de mort** rejoue la carte promue et la fait « survivre » ou « éliminer » (même pièce, § 1, S1).
- **Oracle du monde planté** : lecture faite par le noyau, hors de l'organisme, qui compte les structures du monde retrouvées et les découvertes vraies et fausses, par comparaison à la loi vraie. Dans la course réelle v67, cet oracle est **agrégé par proposeur et défini sur les cartes promues seulement** (même pièce, § 1, S1, et écart E2).
- **Objets de contrôle plantés** : le noyau injecte dans la course des cartes qu'aucun proposeur n'a écrites — lois vraies par construction, lois fausses par construction, témoins de la chaîne (élimination attendue, carte malformée), copies d'anciennes cartes resservies (même pièce, § 1, S1 : 18 entrées).
- **Coût rendu à l'organisme** : depuis la décision N-045, le score de développement rendu dans l'`historique` porte, à côté de l'exactitude, le coût de la génération (dollars par espèce, heures de carte, appels et jetons) et un score net dont la forme et le poids sont gelés au préenregistrement (`docs/decisions/decision-N-045-v2.md`, `c7b05e39de381cee1d5ec2276745a0310bd3cc0857a6be0e0fb14eeb5042261d`, énoncé 2).
- **Générations** : une course enchaîne des générations ; l'archive retenue à la génération t est servie à la génération t+1. N-045 exige que le mérite d'une génération compte ce qu'elle lègue aux suivantes (épisode de K ≥ 3 générations, ou récompense actualisée ; bandit à un pas exclu) (même pièce, énoncé 5). N-044 exige que l'universalité se mesure sur des **familles inédites**, jamais sur des items inédits des familles de conception (`docs/decisions/decision-N-044-v1.md`, `2b70bdac014d366d058a530680d016663b35ed73b8ca0cae9f2369206f5004bf`, énoncé 1).

## 2. La règle qui gouverne la comparaison : N-058

La composition des proposeurs (quels modèles, quels rôles, quelle part du budget) se juge **sur l'oracle du monde planté et sur le coût mesuré, seuls** ; le verdict du juge sur les fiches reste aveugle à l'identité du proposeur et n'entre pas dans ce choix ; un classement « fiches promues par dollar » peut être rapporté comme information, jamais comme critère. Raison : choisir un agent sur le verdict du juge reviendrait à sélectionner sur un score de moniteur, ce qu'interdit l'invariant de N-053 (`docs/decisions/decision-N-058-v1.md`, `854f2724864f1e45394e001f4aca7b0248753e5d2b0a66991e2ee8a7be87de9d`, points 1 et 2). Ce qui ne change pas : le juge des fiches lui-même, ses garanties, et la sélection des **fiches** par la sévérité du test survécu ; l'interdit porte sur la sélection d'**agents** (même pièce, « Ce que la décision ne fixe pas »).

Conséquence pour l'essaim : la comparaison « communiquer, isoler, agent seul » est une comparaison de composition ; son critère est l'oracle et le coût, jamais le nombre de promotions du juge.

N-045 ajoute deux contraintes de méthode utiles ici : un **pilote de bruit** (écart-type test–retest et test A/A : deux runs du même bras ne doivent pas différer) avant toute comparaison, (`decision-N-045-v2.md`, énoncé 6), et le témoin « un modèle, vote à k, coût apparié » (même pièce, énoncé 4 et « Ce que cela change »).

## 3. Ce qui a été mesuré, et où

### 3.1 La course réelle v67 (deux générations, deux proposeurs de fournisseurs différents)

Tout ce qui suit vient de `docs/notes/organisme-re-search-v1/analyse-journaux-re-search-v1.md` (`8a82b5ee…`), analyse préenregistrée de nos journaux, sortie `analyse-journaux-re-search-v1-sortie.json` (`3b65a5e8c60fd718e72d4095a8ea2e7f079a7141ee2dc124910bcc883dcb79ea`, empreinte citée par la note, non recalculée ici).

- **23 cartes** proposées : génération 1, 5 et 6 ; génération 2, 6 et 6 (§ 1, S1).
- **Formes répétées** (mesure M2) : 9 cartes sur 23 répètent une forme déjà proposée, part 0,391 ; 11 formes distinctes ; 11 sur 23 (0,478) si la loi d'archive de départ compte comme déjà proposée. Au seuil d'un quart fixé d'avance : « mode dominant » (§ 2, M2 ; § 3). Réserve écrite par l'analyste : la grammaire servie est petite et aucune référence ne dit quelle part atteindrait un proposeur divers (§ 3, réserve 2).
- **Identité à une loi plantée du monde** : 0 carte sur 23 (§ 2, M1, après l'écart E1).
- **Oracle** : sur les promues seulement, un proposeur 12 proposées, 6 promues, 6 vraies, 0 fausse ; l'autre 11, 5, 5, 0 ; toutes les promues sont de la génération 1 ; la vérité des 12 cartes de la génération 2 n'est pas rendue (§ 2, M1).
- **Coût** : coût du proposeur par carte de 0,027 à 0,067 USD selon le proposeur et la génération ; dépense de la génération (proposeurs et tests de mort) 1,429736 USD pour 11 cartes en génération 1, 0,564574 USD pour 12 cartes en génération 2 (§ 2, M1).
- **Plateau du rendement** (mesure M3) : « indécidable » sur cette course, déclaré d'avance (deux générations seulement) (§ 2, M1 ; § 3).

### 3.2 Les suites d'essais sous le juge (deux sources, 192 suites chacune, au plus 16 essais par suite)

Même pièce, § 1 et § 2. L'unité est une **suite** : un proposeur rejoue une carte jusqu'à 16 fois, arrêt au premier essai promu. Le bras « retour » voit les verdicts, le bras « témoin » non. Résultats retenus pour la présente question :
- **Plateau à la lettre, mais effet de composition** : les promotions précoces viennent des cases où le juge cède tout de suite, les essais tardifs presque tous des cases où le monde n'admet rien au-delà de l'archive ; « aucune case ne rend de décision » (§ 3, audit de symétrie). Leçon de méthode : un taux par essai sous arrêt au premier succès est un taux de premier succès conditionnel à la survie, et un rapport « tardif / précoce » mélange des unités différentes (écart E4).
- **Répétition dans une suite** (mesure M4) : part de propositions répétées ou de même forme 0,415 (retour) contre 0,320 (témoin) dans une source ; 0,360 contre 0,166 dans l'autre (§ 2, M4). Voir les verdicts s'accompagne, dans ces deux sources, d'une plus forte répétition de forme ; aucune règle de différence entre bras n'était fixée d'avance (écart E5).
Portée : ces suites sont une épreuve du juge hors de la boucle de production, sans mémoire anti-répétition (écart E10).

### 3.3 Le monde planté riche (famille MR-2, simulée sans appel)

Source : `docs/notes/organisme-multi-generations-v1/conception-monde-riche-doublons-v4.md` (`47e38ec0663320e8c68011130c3f1b8e1017969cbb740d30c83a78eb5db0a6dc`). Tout y est simulé avec des **proposeurs synthétiques** ; rien n'y mesure de vrais modèles.
- **Pourquoi une famille neuve** : sur la famille précédente, la génération 1 prenait toutes les composantes fortes et moyennes ; progrès certifié en génération 2 ou 3 dans 0 monde sur 12 (§ 1).
- **Composantes conditionnelles** : une pente dont le signe dépend du signe d'un autre trait, invisible dans la marginale. **Part marginale médiane 0,0195** (14 conditionnelles) contre **0,47** (18 moyennes ordinaires) — seul fait de la conception qui ne dépend d'aucun modèle de proposeurs (§ 4.3).
- **Règle de garde** (au moins la moitié des mondes de calibration garde une composante certifiée encore trouvable après une génération 1 simulée) : **8 sur 12 avec masquage** (Wilson à 95 % : [0,39 ; 0,86]), **0 sur 12 sans masquage** (§ 4.2). Le masquage est une hypothèse : la probabilité 0,02 de proposer une conditionnelle avant d'avoir sa condition est « estimée, aucune pièce » (§ 3.2).
- **Trois générations, avec masquage** : progrès certifié dans 8 mondes sur 12 ; génération 3 presque vide (1 monde) ; fausses découvertes 36 sur 204 retenues (17,6 %) (§ 4.4).
- **Devis de cette course** (2 mondes × 3 générations) : central 41,11 USD de modèles ; pire 363,00 USD sur une ligne et 56,20 USD sur l'autre, sous des plafonds de 365 et 57 USD (§ 5).

Pertinence : une famille où la trouvabilité **dépend de ce qui est déjà connu** est celle où le partage entre agents pourrait changer l'issue (hypothèse) ; c'est aussi celle où la règle de garde n'a tenu que sous une hypothèse sur les proposeurs.

### 3.4 Ordre de grandeur des appels dans la course d'auto-conception

Une génération à cinq espèces : 55 appels de proposeurs, 110 d'aiguilleur, 220 de juges ; 39,62 USD à l'estimation, 121,10 au haut, plafond d'arrêt 90 (`docs/notes/organisme-auto-conception-v1/devis-course-auto-conception-v2b.md`, `b2319472cbad20d87664b63edcdab47914de1d81135841b81f10954f6f45da0e`, § 1). Hypothèses : 3,3 octets par jeton, 6 000 jetons de sortie par proposeur (haut 16 000) (`devis-course-auto-conception-v1.md`, `50e7d2f1…`, § 3). Ce sont des **devis**, non des mesures.

## 4. Ce que Re-Search apporte

**Pièce** : « Re-Search: Dissecting LLM Ideation Through a Two-Player Questioning Game », arXiv 2611.14487v1, 10 novembre 2026 ; un modèle doit retrouver l'idée centrale d'un article publié en posant des questions fermées (format des vingt questions), à partir de 200 articles d'une conférence d'apprentissage automatique (métadonnées et début du résumé, `docs/notes/organisme-re-search-v1/anteriorite-re-search-v1.json`, `c3835fe410f91ccc6a61128f6f92c998914f883d1f18c8ea4d59d6f96f4f9828` ; lu sur résumé, non opposable).

**Mesures à reprendre** (mot du directeur, non vérifié sur le PDF de Re-Search, qui n'a pas été lu pour cette pièce) :
- **nombre de branches ouvertes** au cours d'une recherche (largeur de l'exploration) ;
- **score au tour k comme prédicteur du score final** (à quel point la fin d'une recherche est déjà écrite dans son début).
Les deux se transposent à l'organisme : branches = formes de loi distinctes ouvertes par génération et par agent (la mesure M2 de nos journaux en est une version) ; score au tour k = oracle à la génération k ou au k-ième essai comme prédicteur de l'oracle final.

**Antériorité** (même pièce JSON, champ `constat`) : l'écart entre produire et vérifier est une littérature établie depuis 2023 au moins, avec des résultats dans les deux sens selon la tâche ; Re-Search ne la cite pas ; sa nouveauté revendicable serait au plus le domaine et le protocole. Statut : lu sur résumés, non opposable (R7). Les requêtes d'un des deux services bibliographiques ont en majorité été refusées pour limite de débit : « zéro résultat » n'y vaut pas absence (champ `requetes_non_servies`).

## 5. Ce que dit la source descriptive

**Pièce** : « A Society of AI Scientists », prépublication datée du 21 novembre 2026 (plateforme alphaXiv et universités associées), 67 pages ; PDF `docs/sources/alphaxiv-society-ai-scientists-v1/a-society-of-ai-scientists-2026-11-21.pdf`, empreinte recalculée `1c1d3d84347d7736b31cae6951af435ee9332ed5aa431be55e7ccdbbfc578f5d`, conforme à l'attendu. Les pages citées sont celles du PDF.

- **Échelle** : étude exploratoire de douze semaines, 936 agents autonomes, 35 laboratoires opérés par des humains, 936 études, 9 500 messages dans 229 salons créés par les agents (p. 1).
- **Nature** : observationnelle et non randomisée ; les comparaisons entre étapes et laboratoires « décrivent des associations observées plutôt que des effets causaux » (p. 6 et p. 34, § 7.1). Le corpus est concentré (un laboratoire produit environ deux cinquièmes des études, une famille de modèles deux tiers de l'archive) (p. 34).
- **Pas de comparaison de la société à un agent seul** : les travaux voisins « évaluent un agent isolé ou une équipe orchestrée » ; l'article examine ce qui émerge d'un espace partagé (p. 32). Aucune expérience de l'article ne met la société entière face à un agent seul au même coût (lecture du texte principal, pages 1 à 35 ; les annexes n'ont été parcourues que par recherche de termes).
- **Mais des études de la cohorte ont comparé**, à petite échelle, communication et indépendance : sur une optimisation à quatre variables, quatre agents qui partagent coordonnées et scores concentrent 88 % des essais tardifs autour du meneur, contre 30 % pour des agents indépendants ; partager les coordonnées sans les scores rompt cet effet de troupeau (p. 22 ; p. 21, figure 12) ; sur des casse-tête spatiaux, une coordination indirecte par marques sur un tableau partagé résout 15,7 points de plus avec 35 % de jetons en moins qu'une messagerie directe (p. 22) ; un comité de trois agents à rôles fixés obtient un rendement ajusté du risque 3,5 fois plus bas qu'un généraliste seul « à calcul égal » (p. 22). Statut : **rapporté par l'article** à partir d'études écrites par des agents de la cohorte ; ni leurs protocoles ni leurs nombres de répétitions n'ont été lus ici.
- **Boucles d'un seul agent** : gains concentrés sur la première itération, et boucles itératives qui battent rarement un échantillonnage parallèle au même nombre de jetons (p. 34 ; p. 64, figure D1). L'étude la plus citée testait deux tours d'autocritique contre un vote majoritaire au même coût en jetons et a rendu son hypothèse « non résolue » (p. 11).
- **Agent seul planificateur** : dans la même famille d'études, un agent seul jouant un laboratoire simulé a trouvé l'optimum global dans 2 % des essais, contre 42 % pour une recherche aléatoire uniforme et 73 % pour une optimisation bayésienne (p. 22). Statut : rapporté par l'article ; utile pour le bras (c), qui doit être comparé aussi à des bases sans modèle.
- **Communication et diversité** : l'article écrit que la communication ouverte porte un compromis avec la diversité d'exploration (p. 34).
- **Prédiction précoce** : parmi les études d'au moins une semaine, les citations des 72 premières heures déterminent largement le total (corrélation de rang 0,83) mais prédisent faiblement les citations ultérieures (0,26) (p. 12). C'est l'analogue, côté société, de la mesure « score au tour k » de Re-Search.
- **Vérification** : la revue sur le texte seul a manqué des défauts que l'exécution du code a trouvés (p. 33 et p. 34).

La source ne permet pas de conclure qu'une société d'agents fait mieux qu'un agent seul au même coût. La zone « communication, isolement, agent seul, au même coût, sur une vérité plantée » est une **question** (R8) : des études de la cohorte en touchent des morceaux, sur d'autres tâches et d'autres métriques.

## 6. Les trois configurations demandées

Décision du directeur (ligne GO-2026-11-22-12, point 4, relue sur une extraction du registre, `08778543…`), prise en réponse à des recommandations antérieures : « essaim qui communique, trois configurations au même coût (agents qui communiquent, mêmes agents isolés, agent seul), jugés par le monde planté et le coût, jamais par le juge (N-058) ». Les formes de la communication — messages, mémoire partagée, revue entre pairs — ne sont pas dans la ligne : elles viennent de la transmission de la décision à la session de l'organisme, et sont à préciser par la conception.

**Point à traiter par la conception : l'oracle actuel dépend du juge.** Dans la course v67, l'oracle n'est rendu que sur les cartes **promues** (§ 1 ci-dessus, et § 5). Comparer les trois bras sur cet oracle ferait entrer le verdict du juge dans la comparaison, contre N-058. La conception doit donc définir une mesure d'oracle sur **toutes** les cartes proposées, ou sur un sous-ensemble tiré sans le juge, et dire comment elle se calcule sans lire aucun verdict.

Points ouverts, à trancher par la conception : l'unité de coût égalisée ; ce que reçoit (c) à la place de la communication ; ce que la communication permet (scores visibles ou non, p. 22) ; la place de l'aiguilleur et du juge, communs aux trois bras ; le pilote de bruit et le test A/A de N-045.
