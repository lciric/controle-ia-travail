# Idées rares et vérifiées : synthèse du collisionneur sur trois tours

Classe C, 22 novembre 2026. Renvois : « T1-A » conception de A (tour III.1) ; « T2-B/A » critique de B sur A (III.2) ; « T3-C » réponse de C (III.3). A Fable 5.2, B Opus 5.5, C Argon, D Astra, E Carbon, F Neon.

## 1. Verdict

Aucun des six modèles n'apporte de résultat. Ils apportent un protocole, et ils s'accordent sur l'essentiel de ce protocole après les critiques.
L'idée la plus solide n'est pas une façon de produire plus d'idées. C'est une façon de les compter : on fige une loi de tirage de référence, on mesure la rareté sur un panel de tirages à part, et l'on audite le contrôle dans la queue de la distribution.
Le plus gros risque, nommé par cinq modèles sur six, porte sur la queue. La part d'idées vraies y est peut-être trop faible devant le taux d'erreur du contrôle. Dans ce cas, toute intervention qui pousse vers le rare produit surtout des fausses découvertes.
On teste donc d'abord les instruments, puis le contrôle dans la queue ; les interventions après.

## 2. La question

Comment obtenir, à coût égal, davantage d'idées à la fois rarement proposées par un système à plusieurs modèles et confirmées par un contrôle indépendant, sans augmenter les fausses découvertes, et comment le mesurer sans juge-modèle ? (question-etage3.md)

## 3. Ce que dit chaque modèle, et ce qu'il change au tour III.3

**A, Fable 5.2.**
- Tour III.1 : un banc d'inégalités entre invariants de graphes, identité par verdicts sur des graphes-sondes, rareté sous une loi figée, quatre interventions (T1-A).
- Tour III.3 : A concède un défaut décisif, vu par les cinq critiques (T2-B/A à T2-F/A). Avec des verdicts binaires, toutes les inégalités vraies fusionnent en une classe. Il passe à des bornes à signature numérique, trois ensembles de graphes disjoints, une rareté à trois états (rare certifiée, non rare, indéterminée), et place en tête une épreuve des instruments sans modèle (T3-A).

**B, Opus 5.5.**
- Tour III.1 : six interventions, accent sur la fiabilité du contrôle dans la queue et les mondes à vérité plantée (T1-B).
- Tour III.3 : B retire cinq de ses outils (rééchantillonnage sur les singletons, recouvrement entre familles, leurres façon statistique, plongement comme canoniseur, « garantie » par la température). Il ajoute un banc neutre, un contrôle volontairement dégradé à erreur connue, et quatre volets d'épreuve du contrôle (T3-B).

**C, Argon.**
- Tour III.1 : rareté mesurée dans l'échantillon de chaque bras, distance de compression contre une archive (T1-C).
- Tour III.3 : C accepte que cette rareté interne fabrique du rare par dilution ; panel de référence gelé et disjoint ; distance retirée ; identité par arbre syntaxique normalisé plus profil d'exécution ; plus de zones mortes entre hypothèses (T3-C).

**D, Astra.**
- Tour III.1 : terrain fini d'ordonnancement, vérification exhaustive, deux interventions d'allocation (T1-D).
- Tour III.3 : D accepte que ce terrain annulait les fausses découvertes par construction ; il sépare décision du contrôle et audit, compte des « profils de service » pour ne pas multiplier les variantes, et maintient contre tous qu'une marge positive sur les fausses découvertes répondrait à une autre question (T3-D).

**E, Carbon.**
- Tour III.1 : trois interventions composites, valeur par longueur de description minimale (T1-E).
- Tour III.3 : plans factoriels, abandon d'un test qui inversait la charge de la preuve, procédure par e-valeurs, diagnostic en trois sous-épreuves ; rejet partiel d'une critique de A (T3-E).

**F, Neon.**
- Tour III.1 : quatre interventions, dont une archive qualité-diversité et un bandit ; contrôle séparé en développement et audit (T1-F).
- Tour III.3 : F reconnaît qu'un test sur cinq graines ne pouvait jamais atteindre son seuil ; il ajoute un oracle externe, des domaines nuls, des plans factoriels, un allocateur à oubli, et nuance deux citations (T3-F).

## 4. Toutes les propositions, groupées par idée

| Idée | Lettres |
|---|---|
| Identité d'une idée par signature d'exécution sur des sondes, et non par plongement vectoriel ni par juge | A, B, C, D, E, F |
| Rareté mesurée sous une loi de tirage figée, sur un panel à part, jamais montré aux bras | A, B, C, D, E, F (C et E l'adoptent au tour III.3) |
| Masse manquante de Good et Turing, réservée au diagnostic agrégé, jamais à une idée seule | A, B, E, F ; C en partie |
| Dédoublonnage avant le contrôle coûteux, l'économie étant réinvestie | C, D, E, F |
| Pluralité de familles de modèles plutôt qu'un seul modèle | A, B, E, F ; D en réallocation |
| Modèles de base, sans alignement, plutôt que des modèles instruits | B, E, F |
| Exclusion des idées déjà fréquentes, par invite, par rejet ou par grammaire | A, B, E, F |
| Température plus haute | B (contrôle chez C, E et F) |
| Isolement des appels, sans débat ni vote | A, E |
| Recherche évolutive avec contrôle dans la boucle | A, B ; F par archive qualité-diversité ; C par grille de descripteurs |
| Second contrôle, distinct du premier, ou réplication | B, C, E |
| Contrôle du taux de fausses découvertes par p-valeurs ou e-valeurs | A, B, E, F ; C l'abandonne au tour III.3 |
| Allocation adaptative entre sources (bandit) | F, puis F avec oubli |
| Valeur mesurée par le gain marginal face à un portefeuille fréquent figé | A, C, E, F ; D par le gain d'utilité |

## 5. Les meilleures propositions retenues, et pourquoi

1. **La rareté certifiée sur un panel indépendant, avec une borne simultanée.** Les six l'adoptent au tour III.3 (T3-A à T3-F). Sa faisabilité est un calcul binomial connu avant toute dépense. Aucune étude externe.

2. **L'audit du contrôle dans la queue sur de « faux naturels »**, erreurs réellement produites et non leurres fabriqués. B le place en tête ; A, E et F le reprennent (T3-A, T3-B, T3-E, T3-F). Il répond à la limite du taux de base, nommée par cinq modèles.

3. **Le dédoublonnage avant le contrôle**, jugé contre une sélection au hasard et une permutation à tailles de groupes fixes (T3-C, T3-E). Solidité moyenne : le gain dépend du rapport de coût contrôle sur génération, inconnu (T2-D/C). Indice indirect en génération de code.

4. **La pluralité de familles, jugée contre des « pseudo-familles »** (une famille coupée au hasard ; T3-A, T3-B, T3-E, T3-F). Ce témoin corrige un faux critère de B et E (T2-A/E, T2-F/E). Aucune source ne mesure ce gain sur des idées.

5. **Les modèles de base, à format de sortie identique dans tous les bras** (T3-B, T3-E, T3-F). Deux études montrent une baisse de diversité après alignement (section 7), aucune sur des idées vérifiées.

*Jugement du rédacteur :* les interventions de recherche, c'est-à-dire la boucle évolutive, l'archive qualité-diversité et le bandit, sont les plus séduisantes. Ce sont aussi les plus exposées au surajustement du contrôle. Aucune ne sort des critiques avec un indice favorable sur des idées.

## 6. Accords et désaccords

**Accords, d'au moins quatre modèles :**
- Le problème est mal posé tel quel. La rareté n'existe que relativement à une loi figée et à un canoniseur (A, B, C, D, E, F au tour III.1). Tranché.
- Le taux de fausses découvertes dépend du taux de base de la queue, et pas seulement du contrôle. Si la part de vraies y tombe sous le taux d'erreur, presque toutes les confirmations sont fausses (B, C, E, F, puis A). Tranché, par calcul.
- Un second contrôle ne protège pas si ses erreurs sont corrélées avec celles du premier (B, C, E, F). Tranché, par calcul.
- Il faut un essai « témoin contre témoin », sur toute la chaîne, avant tout seuil (A, B, C, D, E, F au tour III.3). Tranché.
- Hors domaine exécutable ou formel, aucune mesure de rareté sans modèle n'est établie (B, C, E, F). Tranché comme limite.
- L'intervalle par rééchantillonnage sur les singletons est biaisé. A, B et F refont le calcul (T2-A/B, T2-F/A, T3-A, T3-B). Tranché.

**Désaccords :**
- **Marge sur les fausses découvertes.** Faut-il une marge positive (B, E, F), ou faut-il garder la lettre « sans augmenter », au prix d'une puissance plafonnée à la frontière (D) ? Non tranché. D l'assume et dit qu'une marge pose une autre question (T3-D).
- **Ce qu'on teste d'abord.** Les instruments seuls (A, C, F), le contrôle dans la queue (B), ou la chaîne de mesure elle-même avec des erreurs injectées (D). Non tranché, mais compatible : ce sont trois étages d'un même ordre.
- **L'identité d'une idée.** C ajoute l'arbre syntaxique à la signature. F le retire, parce qu'une réécriture en boucle ou en récursion crée alors une fausse rareté (T2-E/F, T3-F). Non tranché entre les deux.
- **La généralité d'un plancher de puissance.** C affirme qu'un plancher des p-valeurs conformes annule la puissance « quelle que soit la loi ». A le réfute par un contre-exemple (T3-A). Tranché en faveur de A, E et F.
- **Le « contrôle hors distribution ».** Pour A, c'est une confusion avec un échec de généralisation. E le rejette en partie, car la question vise justement les cas hors des cas connus (T3-E). Non tranché.

## 7. Ce qui est vérifié sur pièce

« Vérifié » veut dire que j'ai lu la page de résumé de la source primaire, et rien de plus : pas le texte intégral, pas les chiffres internes.

| Référence | Ce que les modèles en disent | Modèle | Statut |
|---|---|---|---|
| « Does Writing with Language Models Reduce Content Diversity? » (arXiv 2309.05196) | Pour F, l'alignement réduit la diversité. Pour A, l'étude porte sur une écriture avec des personnes, pas sur la génération seule | F ; critique de A | Vérifié : écriture avec des utilisateurs ; baisse de diversité avec le modèle instruit, pas avec le modèle de base. La lecture de A est juste |
| « Understanding the Effects of RLHF on LLM Generalisation and Diversity » (arXiv 2310.06452) | L'alignement par préférences réduit la diversité | B | Vérifié : baisse nette de la diversité des sorties |
| « Can LLMs Generate Novel Research Ideas? » (arXiv 2409.04109) | Les doublons croissent avec le volume généré | A | Vérifié en partie : le résumé cite un « manque de diversité ». Il ne dit rien sur les doublons selon le volume |
| « Large Language Monkeys » (arXiv 2407.21787) | La couverture croît avec le nombre de tirages, si un filtre trie | E | Vérifié : la croissance est souvent log-linéaire. Sans vérification automatique, le vote et les modèles de récompense plafonnent |
| « Scaling Laws for Reward Model Overoptimization » (arXiv 2210.10760) | Suroptimiser un juge imparfait dégrade la vraie performance | B, E | Vérifié, sur des modèles de récompense appris : c'est une analogie, comme B le dit |
| « False discovery rate control with e-values » (arXiv 2009.02824) | La procédure par e-valeurs contrôle le taux de fausses découvertes sous toute dépendance | E, F | Vérifié |
| « Testing for Outliers with Conformal p-values » (arXiv 2104.08279) | Les p-valeurs conformes permettent le contrôle du taux de fausses découvertes | A | Vérifié : contrôle exact, « en un sens marginal assez faible » |
| « Estimating the number of unseen species: A bird in the hand is worth log n in the bush » (arXiv 1511.07428) | On n'extrapole le nombre de classes non vues que sur un horizon logarithmique | A | Vérifié : jusqu'à un facteur proportionnel à log n |
| « Competition-level code generation with AlphaCode » (arXiv 2203.07814) | Regrouper les candidats par comportement fait sortir des solutions rares | C | Vérifié en partie : échantillonnage massif puis filtrage par comportement. Le résumé ne parle pas de regroupement |
| « The reusable holdout » (Science, 2015) | Réutiliser un jeu de validation de façon adaptative en dégrade la validité | A, F | Existence vérifiée par une version voisine, « Generalization in Adaptive Data Analysis and Holdout Reuse » (arXiv 1506.02629), qui le dit |
| « Mathematical discoveries from program search with large language models » (Nature, 2024) | Des découvertes avec un évaluateur programmatique exact | A, B, F | Non vérifié : la page de l'éditeur est inaccessible |
| « The population frequencies of species and the estimation of population parameters » (1953) | La masse non vue s'estime par la part des singletons | A, B, C, E, F | Non vérifié : source non ouverte |

**Chiffres.** Aucun chiffre empirique dans les dix-huit cellules. Tous les seuils sont marqués « illustratif ». Les devis vont d'environ 130 à 750 dollars à l'échelle des modèles de sept à neuf milliards de paramètres (T1-E, T1-F, T3-E), et jusqu'à quelques milliers d'euros chez B (T1-B). Tous ces devis sont illustratifs et non opposables.

## 8. L'expérience à faire en premier, selon les modèles

- **A** propose l'épreuve des instruments, sans appel de modèle. Le canoniseur doit séparer des bornes vraies plantées et fusionner leurs réécritures. Si l'épreuve échoue, le banc tombe (T3-A).
- **B** propose le contrôle dans la queue : les faux positifs sur des faux naturels et l'indépendance des erreurs de deux contrôles, sur un banc neutre et avec le contrôle dégradé. Si les deux échouent, il faut améliorer le contrôle et non le générateur (T3-B).
- **C** propose l'étalonnage de la signature, puis le panel de référence avec un audit stratifié des confirmés et des rejetés (T3-C).
- **D** commence par un devis réel. Le panel peut-il certifier même une classe jamais revue ? Il lance ensuite l'essai « témoin contre témoin » avec un contrôle tronqué et des erreurs injectées. Si une fausse publication injectée reste invisible, il s'arrête (T3-D).
- **E** propose un diagnostic en trois étapes : masse manquante, dérive du contrôle en queue, indépendance des deux contrôles (T3-E).
- **F** propose la qualification de la signature, le diagnostic de la masse rare, l'essai « témoin contre témoin » et un domaine nul (T3-F).

*Jugement du rédacteur :* ces propositions se rangent en un seul ordre.
1. Le devis de faisabilité du panel (D).
2. L'épreuve des instruments sans modèle (A, C, F).
3. L'essai « témoin contre témoin » avec erreurs injectées et domaine nul (D, F).
4. L'audit du contrôle dans la queue sur des faux naturels (B, E).

Les quatre étapes sont bon marché devant les duels d'interventions.

## 9. Ce qu'il faut retenir

1. **La rareté se certifie, elle ne s'observe pas.** Il faut un panel indépendant de taille calculable d'avance (T3-A à T3-F).
   *Réserve :* un panel fini ne distingue jamais une idée hors support d'une idée très rare (T3-D, T3-F).

2. **Le contrôle dans la queue est le goulot probable.** Le générateur ne l'est sans doute pas (B, C, E, F).
   *Réserve :* c'est une limite de principe, pas une mesure. On ignore si la part de vraies baisse vraiment dans la queue.

3. **Aucune intervention n'a d'indice direct sur des idées vérifiées.** Les meilleurs indices portent sur la diversité de textes ou sur la couverture en code (section 7).
   *Réserve :* les études sur la diversité ne disent rien sur la vérité des idées.

4. **Les modèles se sont corrigés entre eux de façon vérifiable.** Le banc de A s'effondrait, cinq critiques l'ont vu. Le test de F était inatteignable, les outils de B étaient biaisés (T2, T3).
   *Réserve :* les six modèles partagent les mêmes réflexes de statistique. Leur accord n'est pas une validation extérieure.

5. **Tout cela ne vaut que sur des domaines exécutables à oracle.** C'est le cas de nos bancs plantés, pas de la langue libre (T3-E, T3-F).
   *Jugement du rédacteur :* la transposition aux idées de recherche du programme reste l'hypothèse non testée la plus lourde. Aucune expérience proposée ne la teste (T1-A, T3-A).
