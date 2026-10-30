## (a) Réponses aux critiques visant D

| Critique | Décision | Raison et correction |
|---|---|---|
| **A-D.a1 — confusion entre cinq instances et cinq familles** | **Acceptée.** | Le fait 4 est **RAPPORTÉ** : cinq instances sont prévues, sans nombre de familles par instance. Je supprime « cinq familles scellées » partout. Cinq instances ne fournissent ni cinq familles ni cinq unités statistiquement indépendantes garanties. |
| **A-D.a2/a3, B-D.a3, C-D.a1/a2 — duels tautologiques, issues asymétriques et grille choisie** | **Acceptée.** | Tester Chapman sous ses seules hypothèses de dérivation ne discrimine pas les mécanismes pertinents ; la couverture restait néanmoins dépendante d’un intervalle non précisé. Le second duel avait une issue pratiquement écrite d’avance. Je remplace les deux par des comparaisons de procédures sur une grille fixée avant exécution, avec abstention et critère de puissance. |
| **A-D.a4 et B-D.b — binomiale exacte sous dépendance** | **Acceptée.** | La borne binomiale ne vaut que pour des indicateurs d’échec indépendants. Sous grappes, l’unité devient la grappe échantillonnée et l’énoncé porte sur la loi de ces grappes ; il n’y a pas de conversion automatique en familles indépendantes. À défaut d’échantillonnage identifiable, la procédure s’abstient. |
| **A-D.a5 — « familles indépendantes effectives » non définies** | **Acceptée.** | Je supprime ce comptage par ICC ou seuil de corrélation a posteriori. L’unité indépendante est définie **par le plan expérimental**, avant mesure : tirage distinct selon la loi déclarée, sans information partagée. Plusieurs familles issues d’une même instance ou d’un même contexte restent une grappe, sauf validation préenregistrée contraire. |
| **A-D.a6 — permutation vue/écart confondue par l’apprentissage** | **Acceptée.** | La permutation ne sera faite que pour une défense figée n’ayant jamais utilisé les familles concernées, ou dans un monde simulé où les étiquettes sont échangeables par construction. Sinon elle mesure aussi l’effet d’apprentissage. |
| **A-D.a7 — Q5 et seuil δ = 0,02 non dimensionné** | **Acceptée.** | Je retire ce seuil. Q5 publiera une différence appariée, son intervalle et sa puissance ; aucune conclusion d’équivalence si l’incertitude inter-familles dépasse la marge déclarée. |
| **A-D.a8, C-D.b1/c3 — “tous les appariements plausibles” et remplacement après refus** | **Acceptée.** | L’enveloppe combinatoire est remplacée par un graphe d’ambiguïtés limité aux liens déclarés, une énumération seulement si son cardinal préenregistré le permet, sinon un modèle probabiliste calibré. Une enveloppe non informative doit être rapportée comme telle. Aucun remplacement d’une instance refusante ne sera traité comme source équivalente. |
| **A-D.a9, B-D.a1/c2, C-D.b2 — garantie stratifiée** | **Acceptée.** | Je la retire de la définition principale. Si elle reste annexe : strates disjointes, fondées uniquement sur des métadonnées de plan disponibles avant conception de la défense, nombre fixé d’avance, correction explicite du risque global et test de faisabilité. Des strates définies après observation sont interdites. |
| **A-D.a10 — Q4 sans validation chiffrée** | **Acceptée.** | Q4 reçoit ci-dessous des critères d’audit numériques, marqués illustratifs lorsqu’ils ne viennent pas des pièces, sans inventer les propriétés des bancs. |
| **Constat transversal de A — direction du 1→2 et lignée du lecteur** | **Transformée en test.** | La scission peut venir du lecteur ou de la taxonomie. Des lecteurs de lignées permutées, aveugles à la source, seront étalonnés sur copie permutée, listes sans lien et relations un-à-plusieurs connues. Les valeurs \(m=18\) et \(m=19\) restent des scénarios, pas des résultats tranchés. |
| **B-D.a2 — mélange entre incertitude de définition et incertitude statistique** | **Acceptée.** | Je publie séparément : intervalle statistique **conditionnel à chaque appariement cohérent**, puis dispersion entre scénarios d’unité. Leur étendue commune n’est pas appelée intervalle de confiance. |
| **B-D.a4 — bloc 2 inopérant** | **Acceptée sur les critères d’audit ; rejetée sur l’absence totale de recommandation.** | Je recommandais déjà les journaux et propositions brutes. J’ajoute maintenant une liste d’audit actionnable pour les bancs publics : version, licence, provenance, schéma, possibilité d’étiquetage et exposition publique. |
| **B-D.b — familles supplémentaires issues des mêmes instances** | **Acceptée.** | Elles allongent les listes mais ne créent pas automatiquement de nouvelles unités indépendantes. Le nombre d’instances ne peut donc pas être remplacé par le nombre total de sorties dans une borne binomiale. |
| **B-D.b — recouvrement avec l’entraînement dans Q4** | **Acceptée avec restriction.** | Déduplication exacte et documentation de provenance sont exigibles, mais le recouvrement avec des corpus non accessibles n’est pas identifiable par un test interne. Il reste **HYPOTHÈSE** ; la validation est alors descriptive, pas une correction garantie du biais. |
| **B-D.c1 — absence de test de fermeture** | **Rejetée comme preuve, transformée en diagnostic.** | Aucune courbe d’accumulation ne démontre la fermeture. Je préenregistre son analyse de tendance et conserve systématiquement un scénario ouvert où seul \(N(t)\) est estimé. |
| **B-D.c3 — indépendance des instances sans contrôle opérationnel** | **Transformée en test.** | Deux exécutions du même modèle servent de contrôle positif de dépendance ; une énumération neutre préenregistrée peut mesurer une dépendance de capture sur cette tâche. Ni l’une ni l’autre ne démontre l’indépendance des corpus d’entraînement. |
| **C-D.a3 — base à battre au mauvais niveau** | **Acceptée.** | Pour \(N\), la base est le comptage brut dans une unité cohérente. Pour l’universalité, elle devient la règle familiale naïve supposant les familles découvertes indépendantes, et non une règle comptant les éléments comme familles. |
| **C-D.a4 — validation laissant une source de côté** | **Acceptée.** | Elle ne sera appliquée qu’à un modèle parcimonieux dont les degrés de liberté restent identifiables. Effets principaux, interactions et classes latentes ne seront pas ajustés simultanément sur une table quasi saturée. |
| **C-D.b3 — non-identifiabilité sous hétérogénéité arbitraire** | **Acceptée sur le fond.** | À nombre fini de sources, des mélanges de capturabilité différents peuvent être compatibles avec les mêmes observations et des masses manquantes différentes. Les classes latentes et modèles bayésiens deviennent des analyses de sensibilité, jamais une identification démontrée. |
| **Conditions de non-jugeabilité listées par A, B et C** | **Acceptées comme conditions à tester, non comme résultats.** | Sont intégrées : petits \(m\), forme d’intervalle, \(Q_2=0\), forte dépendance, queues inobservables, information séquentielle insuffisante, multiplicité des strates, tables creuses et interaction d’ordre maximal non identifiable. |
| **Contrôles négatifs manquants** | **Acceptés.** | J’ajoute : listes répétées d’un même modèle, strate à probabilité de capture nulle, défense constante, scores sans effet famille, étalonnage du lecteur, taux de type I à chaque arrêt et permutation sur défense non ajustée. |

## (b) Expériences corrigées

### Socle obligatoire, exécuté avant les duels

1. **Lecteur** : une liste et sa copie permutée doivent donner \(m=n\) ; deux listes sans lien possible doivent donner \(m=0\) ; des relations 1→2 connues doivent être récupérées. On estime faux liens et liens manqués par lecteur et par lignée.
2. **Population** : monde sans masse manquante, monde avec strate à capture nulle, listes répétées du même modèle et monde ouvert.
3. **Défense** : score constant non certifiable lorsque le seuil exige mieux que le niveau de référence ; scores sans effet famille donnant une dépendance estimée proche de zéro.
4. **Séquentiel** : taux de fausse certification mesuré à chaque temps d’arrêt sous \(\pi\geq\varepsilon\), avec définition correcte du risque : certifier alors que la part réelle d’échec atteint ou dépasse \(\varepsilon\).

### Duel 1 corrigé — estimation de \(N(t)\)

**Grille figée avant exécution** : mondes fermés indépendants/homogènes, dépendances positive et négative, hétérogénéité, petits effectifs, erreurs d’appariement dirigées 1→2, puis mondes avec censure commune et population ouverte. Les valeurs \(CV=0,4\) et \(OR=1,5\) sont **illustratives**.

**Procédures** :

- \(M_0\) : comptage brut observé, dans une unité déclarée ;
- \(M_1\) : Lincoln-Petersen/Chapman, avec intervalle de profil préenregistré plutôt qu’une approximation normale laissée ouverte ;
- \(M_2\) : appariement calibré, puis borne de Chao2 ou modèle multi-listes parcimonieux lorsque le nombre de sources le permet, avec abstention obligatoire en cas de non-identifiabilité.

**H_A** : sur les mondes fermés identifiables, \(M_2\) respecte la couverture préenregistrée, ne produit pas de fausse détection dans le monde complet, et améliore le pire RMSE par rapport à \(M_0\), sans gagner par abstention systématique.  
**H_B** : \(M_2\) viole au moins un de ces critères ou n’apporte aucun gain ; \(M_0\) reste alors la seule base défendable sans hypothèses supplémentaires.

Ces issues sont exhaustives sur la grille. La première falsifie H_B ; la seconde falsifie H_A. Les mondes à strate invisible ne servent pas à déclarer un vainqueur ponctuel : toute procédure qui y revendique estimer le total sans scénario externe est réfutée. Métriques : biais, RMSE, couverture, largeur, taux d’abstention et fausse masse manquante.

### Duel 2 corrigé — mesure d’universalité

On compare :

- \(R_\Delta\), règle fondée uniquement sur l’écart vues/tenues à l’écart ;
- \(R_\pi\), règle portant sur la part d’échec, avec unités définies par le plan, variance à deux niveaux, arrêt préenregistré et abstention si l’information est insuffisante.

La grille comprend des mondes à même écart moyen mais queues différentes, des mondes échangeables, des grappes et des mondes où le nombre d’unités permet réellement d’atteindre la borne.

**H_A** : \(R_\pi\) maintient la fausse certification sous \(\alpha\), y compris sous arrêt optionnel, possède une puissance non nulle dans les mondes faisables et réduit le pire excès de risque par rapport à \(R_\Delta\).  
**H_B** : \(R_\pi\) échoue à l’un de ces critères ou n’améliore pas \(R_\Delta\).

La première issue falsifie H_B ; la seconde falsifie H_A et interdit de présenter \(R_\pi\) comme certificat robuste. Une règle qui s’abstient partout ne peut pas gagner.

## (c) Réponse à l’arbitre — page synthétique

### Établi et non établi

**VÉRIFIÉ** : les quatre calculs fournis sont arithmetiquement exacts ; l’union contient 34 unités Argon ou 35 unités Opus ; l’appariement n’est pas bijectif. Les nombres 29, 59 et 149 sont les seuils à zéro échec uniquement pour des unités indépendantes tirées selon la loi définissant \(\varepsilon\).

**Non établi** : fermeture de la population, indépendance des sources, homogénéité de capture, représentativité des familles découvertes, exactitude du lecteur et existence d’un nombre fini de familles encore inconnues. Les cinq instances sont **RAPPORTÉES**, pas leur production. Les propriétés des bancs publics demeurent **HYPOTHÈSES**.

### Définition retenue

Sur une classe finie exhaustivement testée, l’énoncé est : « chaque famille satisfait le critère familial préenregistré ». Sur des familles découvertes, l’énoncé prédictif retenu est seulement :

> avec confiance \(1-\alpha\), \(P_{F\sim P,M}(\text{échec})\leq\varepsilon\), conditionnellement à la loi \(P\), au mécanisme de découverte \(M\), à l’unité d’échantillonnage et au critère de réussite déclarés.

Sans plan d’échantillonnage défendant cette loi, on publie les résultats observés et on s’abstient. Cela ne signifie jamais « robuste à l’inconnu ».

### Estimateur retenu

Aucun estimateur ponctuel de \(N\) n’est confirmé. En scénarios cohérents, calculs refaisables :

- **fusion grossière** : \(n_1=28,n_2=24,m=18\), LP \(=37,33\), Chapman \(=37,16\) ;
- **scission fine** : \(n_1=29,n_2=25,m=19\), LP \(=38,16\), Chapman \(=38,00\).

Ce sont des sensibilités, pas un intervalle de confiance ; la scission fine est une imputation d’unité. Pour la performance, les deux granularités doivent être rapportées afin qu’une fusion ne masque pas un échec. Avec plusieurs sources : comptage brut, Chao2 lorsqu’il est défini, Good-Turing pour la masse manquante sous la loi de capture, et modèles multi-listes parcimonieux comme sensibilités.

### Questions candidates révisées

1. **Borne d’universalité** — valider couverture, dépendance et abstention. Piège : compter sorties ou éléments comme familles indépendantes. Validation : objectifs de 29 ou 59 unités réussies pour les bornes des faits ; sinon abstention. Risque hors périmètre : **faible, illustratif**.
2. **Estimation de \(N(t)\)** — comparer estimateurs sur vérité connue. Piège : prétendre identifier une strate commune invisible. Validation : couverture 95 % et biais maximal 5 %, **illustratifs**, contre comptage brut. Risque : **faible, illustratif**.
3. **Appariement** — borner faux liens et liens manqués avant tout estimateur. Validation : double lecture de 100 % des liens et arbitrage de tous les désaccords, **illustratif**, avec contrôles mécaniques. Risque : **faible, illustratif**.
4. **Transport extérieur** — confronter prédictions scellées à des données brutes. Validation : au plus trois bancs, audit de 100 % des champs licence/version/provenance, **illustratif** ; seuil fixé après audit mais avant mesure. Risque : **moyen, illustratif**.
5. **Aveugle contre informé** — mesurer apparié à budget et familles identiques. Validation : intervalle 95 % **illustratif** et taille fixée par puissance ; aucun δ constant sans dimensionnement. Risque : **faible, illustratif**.

### Organisation recommandée en cinq lignes

Les effets de cette organisation sont des **HYPOTHÈSES**.

1. **Consignes** : noyau commun limité au format et au périmètre ; toute variation préenregistrée et analysable.  
2. **Cloison** : contextes, accès, stockages et coordinateurs séparés ; sorties hachées et scellées ; aucune lecture croisée.  
3. **Appariement** : schéma canonique antérieur, lecteurs multiples aveugles à la source, liens 1→plusieurs et incertains autorisés, confusion calibrée.  
4. **Dépendance/estimation** : contrôle par listes répétées d’un même modèle ; modèles multi-listes parcimonieux ; aucune inférence sur les corpus à partir des seules sorties.  
5. **Refus** : consigné tel quel, jamais compté comme zéro ni remplacé par une source réputée équivalente ; analyses avec/sans source et strate de censure commune.

**Première expérience** : l’étalonnage du lecteur et la simulation gelée du duel 1, sur CPU avec double implémentation. Tant que l’unité et ses erreurs d’appariement ne sont pas mesurées, ni l’estimation de \(N\) ni la déclaration d’universalité ne sont correctement dimensionnées.

FIN-DE-CELLULE