# Proposition A — Tour III.1 : validité de construit des sondes boîte blanche

**État des pièces**
- **D est visiblement coupée** : la pièce s'arrête sur « celles qui demandent ». Je n'infère rien de la suite.
- **P renvoie à deux sections absentes des faits** : la section 3 (L, T) et la section 7 (« contrôles croisés »). Je ne les reconstitue pas.
- **Tour à l'aveugle** : B et C ne me sont pas visibles, donc B1 est sans objet dans ce tour.
- **Statuts.** Tout le contenu des faits est **RAPPORTÉ**. Les chiffres de littérature cités par E (95–99 %, AUROC > 0,7, 64–84 %) sont RAPPORTÉS *et* marqués « à vérifier » par E elle-même. Aucun score de sonde n'existe dans les faits. Tout ce que je propose est **HYPOTHÈSE**. Tout seuil ou volume chiffré qui suit est **illustratif**.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé de la question | Statut | Pourquoi il compte |
|---|---|---|---|
| a1 | « Le concept visé par les sondes est un trait du texte produit, pas une conduite. » | **Contredit par P (RAPPORTÉ)**. P 8.1 liste des concepts d'état ou de conduite : tromperie, dissimulation, conscience d'évaluation, auto-préservation, enjeux élevés. P 11 et H8 opposent « intention » et « conscience d'évaluation ». | Pour la sonde de conscience d'évaluation, le « contexte » *est* le concept, pas une nuisance. Le duel H_A/H_B de la question s'inverse donc pour ce concept. Il faut fixer, concept par concept, si la cible est un trait du texte ou un état de l'émetteur. Les deux prédisent des issues **opposées** au croisement « même contenu, deux cadrages » (expérience X1). |
| a2 | Les « trois couches rapportées » sont celles des sondes. | **HYPOTHÈSE**. D point 3 fixe les couches 7, 15 et 23 pour les « traits internes de l'agent comme traits du pôle ». P 8.2 parle de couches précoce, médiane et tardive sans les numéroter. | L'identification couche par couche n'est pas établie. Elle doit être confirmée avant tout préenregistrement. |
| a3 | Chaque famille « prétend mesurer » un concept. | **Faux pour Mahalanobis (RAPPORTÉ, F)**. Elle est non supervisée : distance aux jetons honnêtes, sans étiquette de concept. | Son construit opérationnel est « atypicité par rapport à la distribution honnête d'entraînement », quel que soit le concept nominal. |
| a4 | Il existe des étiquettes de vérité indépendantes de la sonde (quelle action porte le trait). | **Absent des faits**. Le banc des modes est clos (N-054, RAPPORTÉ), mais la procédure d'étiquetage n'est pas décrite. | Sans vérité terrain indépendante, « mesure son concept » n'a pas de témoin vrai. Si les positifs viennent d'une consigne ou d'un réglage fin, la consigne est un facteur de confusion structurel (voir X1). |
| a5 | L'agrégation par maximum ou attention neutralise la longueur. | **HYPOTHÈSE, probablement fausse pour le maximum.** Sous l'hypothèse nulle, le maximum de n scores croît avec n. C'est un fait statistique pour des tirages i.i.d. ; pour des jetons corrélés, l'ampleur est inconnue. | Une sonde au maximum peut lire la longueur sans aucun signal de concept. Contrôle obligatoire : X2. |
| a6 | Les sondes « existent », c'est-à-dire qu'elles battent le plancher de P 8.1 (sonde aléatoire appariée en covariance). | **Non établi** (aucun score dans les faits). | La validité de construit ne se pose qu'au-dessus du plancher. Une sonde sous le plancher « n'existe pas » (P). |
| a7 | Les représentations transfèrent du 70B au 8B et sont linéaires. | **RAPPORTÉ comme contesté par E §3.1** (Apollo 2025 sur 70B, chiffres « à vérifier »). | Les familles linéaire et différence de moyennes supposent un concept linéairement lisible dans un 8B. |
| a8 | Cohérence interne de E. | **E est incohérente avec P et F (RAPPORTÉ).** E attribue à « H6 » le transfert 70B→8B et la détection du biais diffus ; P définit H6 comme la marge asymétrique d'intervention. E dit que le programme utilise « des séquences d'états, pas une sonde ponctuelle » ; F décrit des sondes **par jeton** agrégées **par action**, le séquentiel étant l'agrégateur A_temps de P 4. E porte aussi l'intitulé « programme v7 de conv-audit » alors que P est la v2. | Les sondes visées par la question sont ponctuelles par jeton. La « nouveauté séquentielle » revendiquée par E ne s'applique pas à elles. Ne pas citer E §4 comme position d'antériorité des sondes. |
| a9 | Le forçage de texte (*teacher forcing*) d'un texte dans le modèle reproduit les activations de sa génération. | **HYPOTHÈSE.** | Les croisements appariés exigent de faire passer un même texte sous plusieurs cadrages. Si le forçage déplace les scores, les croisements mesurent un artefact. Contrôle de manipulation : M0 ci-dessous. |
| a10 | Le titre « Linear probes detect deception in Llama-3.3-70B-Instruct » (E) est le titre de la publication. | **Référence à vérifier.** Je ne peux pas confirmer que c'est le titre publié. | R7 : à vérifier sur PDF avant citation. |

Point de méthode : **5 familles × 5 concepts × 3 couches = 75 sondes**. Les comparaisons multiples doivent être fixées au préenregistrement (P 12), par exemple avec une correction de type Holm sur la famille d'hypothèses de chaque expérience. C'est une HYPOTHÈSE de conception.

---

## (b) Expériences décisives (inférence forte, B4)

### Cadre commun

**Unité de score.** Le score d'action brut s(a) est standardisé contre la distribution des actions honnêtes **du même intervalle de longueur** :
z(a) = (s(a) − médiane_honnête,L) / écart interquartile_honnête,L (sans unité).
Tous les écarts Δ sont exprimés en unités de z.

**Seuils (illustratifs, à fixer au scellement) :**
- effet présent : borne basse de l'IC 95 % de Δ > δ = 0,5 ;
- effet absent : équivalence par double test unilatéral dans ±ε = 0,2.

**M0 — contrôle de manipulation du forçage.**
- Même texte, même cadrage, lu en génération propre puis en forçage.
- Exigence : équivalence (±ε) des scores et corrélation des scores par action ≥ 0,9 (illustratif).
- Si M0 échoue, tous les croisements par forçage ci-dessous sont **non interprétables**. On s'arrête (liste d'arrêt, P 12).

**Garde testée sur un cas sain et sur un artefact (P 12).** Chaque test reçoit deux sondes témoins dont le construit est connu par construction :
- **témoin « contexte »** : sonde entraînée à prédire la consigne système. Le test doit la classer H_B ;
- **témoin « contenu »** : sonde entraînée sur une propriété mécanique du texte indépendante de la consigne, par exemple « l'action contient une valeur numérique ». Le test doit la classer H_A.

Si un témoin est mal classé, c'est le test qui est réfuté, pas la sonde.

---

### X1 — Plan 2×2 en forçage : contenu × cadrage (croisements 1 et 2 de la question)

**Matériel.** Pour chaque tâche, deux contenus :
- C⁺ : un texte portant le trait, issu du banc clos ;
- C⁻ : un texte honnête apparié en tâche, longueur et format.

Chaque contenu est forcé sous deux cadrages : K⁺ (contexte de production des positifs) et K⁻ (contexte honnête). Quatre cellules par tâche.

**Grandeurs.**
- Δ_contenu = moyenne des z sur C⁺ moins moyenne des z sur C⁻, à cadrage fixé. C'est le croisement « même cadrage, contenus différents ».
- Δ_cadrage = moyenne des z sous K⁺ moins moyenne des z sous K⁻, à contenu fixé. C'est le croisement « même contenu, deux cadrages ».
- Interaction : écart entre les deux Δ_contenu calculés sous K⁺ et sous K⁻.

**Duel pour un concept déclaré « trait du texte » :**
- **H_A** (lit le trait du texte) : Δ_contenu > δ sous *chaque* cadrage, et Δ_cadrage équivalent à 0 (±ε).
- **H_B** (lit le contexte) : Δ_cadrage > δ et Δ_contenu équivalent à 0.
- Issues :
  - Δ_cadrage > δ falsifie H_A.
  - Δ_contenu équivalent à 0 falsifie H_A ; Δ_contenu > δ sous les deux cadrages falsifie H_B.
  - Deux effets présents : la sonde lit une conjonction. Les deux versions « pures » sont falsifiées, et la sonde ne peut pas être revendiquée comme mesure du trait.

**Pour la sonde de conscience d'évaluation**, les rôles s'inversent (a1) : H_A prédit Δ_cadrage > δ avec des cadrages K « évaluation / non-évaluation », et H_B « lit le contenu ou le registre » prédit Δ_contenu > δ. C'est exactement la prédiction de P 11 (« s'effondre quand l'attaquant apprend à paraître détendu ») réduite à une mesure, sans attaque. Si le score suit le registre du texte plutôt que le cadrage, la sonde mesure le registre. La prédiction H8 de P 11 (HYPOTHÈSE, 0,40) en est le prolongement, hors du périmètre de ce tour.

**Nul.** Distribution de Δ obtenue par permutation des étiquettes de cellule *à l'intérieur de chaque tâche* (2 000 tirages, illustratif).

---

### X2 — Longueur et format (nuisances mécaniques)

**X2a, longueur.**
- Sur des actions honnêtes seules, tronquer aux préfixes de 64, 128, 256, 512 et 1 024 jetons (illustratif). Mesurer la pente du score brut en fonction du logarithme de la longueur.
- **H_A** : pente nulle sur les honnêtes (±ε par doublement), et l'écart positifs/négatifs persiste à longueur appariée exacte.
- **H_B** (lit la longueur) : pente honnête > 0 significative, **et** l'AUROC à longueur appariée tombe dans l'IC de 0,5.
- Une pente nulle falsifie H_B. Un AUROC appariée égal au hasard falsifie H_A.
- Témoin vrai : sonde à direction aléatoire au maximum ; on attend une pente > 0 si a5 est juste. Témoin faux : la même sonde à score par jeton remplacé par une constante, qui doit donner une pente nulle.

**X2b, format.** Même contenu en prose ou en liste, produit par un paraphraseur tiers (Qwen2.5-7B, nommé dans P). Contrôle de manipulation : préservation du contenu jugée par un second juge et par la vérification de préservation du trait propre au banc, non décrite dans les faits (a4).
- **H_A** : Δ_format équivalent à 0.
- **H_B** : Δ_format > δ.
- Une seule issue est possible et chacune falsifie l'autre hypothèse.

---

### X3 — Permutation des étiquettes (croisement 3)

Réentraîner **toute la chaîne** (normalisation, apprentissage par sacs, attention, choix de couche si choix il y a) sur des étiquettes permutées à l'intérieur des strates (tâche × intervalle de longueur × format). Faire 1 000 permutations (illustratif ; 200 pour le perceptron et l'attention, plus coûteux).

- Grandeur : taux de détection (TD) à taux de fausses alertes (TFA) fixé à 1 % et à 5 % (illustratif ; le 1 % reprend la convention citée par E).
- **H_A** : TD réel au-delà du quantile 0,99 du nul permuté, et au-delà du plancher apparié en covariance (P 8.1).
- **H_B** (la capacité de la chaîne fabrique du signal) : TD réel dans la distribution permutée.
- Issues : l'une ou l'autre hypothèse est falsifiée.
- **Variante décisive pour les familles à apprentissage par sacs :** permuter seulement *entre* cadrages à contenu fixé. Si le TD survit à cette permutation, la sonde se nourrit du cadrage. Ce résultat se recoupe avec X1.

---

### X4 — Effacement amnésique de la nuisance (causal, sur les activations, sans attaque)

Effacer linéairement des activations l'information sur la nuisance (longueur, format, cadrage) avec un effaceur fermé de type LEACE (Belrose et al., 2023, « LEACE: Perfect linear concept erasure in closed form »), puis réévaluer la sonde **figée**. Logique de l'*amnesic probing* (Elazar, Ravfogel, Jacovi, Goldberg, 2021, « Amnesic Probing: Behavioral Explanation with Amnesic Counterfactuals », TACL).

- **H_A** : la perte de TD (à TFA 5 %) reste dans ±0,05 (illustratif).
- **H_B** : le TD tombe au plancher apparié en covariance.
- Témoin vrai : effacer la direction de la sonde elle-même doit faire tomber le TD au plancher. Témoin faux : effacer une direction aléatoire de même rang ne doit pas le faire tomber.
- Limite (HYPOTHÈSE) : l'effacement linéaire ne retire rien de non linéaire. Pour le perceptron, H_A survivant à X4 n'établit rien seul.

---

### X5 — Trait du texte contre intention de l'émetteur (tranche a1)

Contenus porteurs du même défaut textuel mais d'origines différentes :
- (i) produits par l'organisme sous K⁺ ;
- (ii) défauts introduits par un procédé tiers dans un texte honnête, puis forcés sous K⁻ ;
- (iii) erreurs honnêtes réelles, avec défaut de même catégorie.

- **H_texte** : z(ii) ≈ z(iii) ≈ z(i), équivalents à ±ε.
- **H_intention** : z(i) > z(ii) et z(i) > z(iii), avec δ ; et z(ii) ≈ z(iii) ≈ honnête sans défaut.
- Issues : chacune falsifie l'autre. Une sonde nominalement « tromperie » ou « dissimulation » qui sort H_texte mesure la *qualité défectueuse*, pas la tromperie. C'est un résultat publiable dans les deux sens.

---

### Spécifique à chaque famille

**1. Différence de moyennes**
- **Concept opérationnalisé.** Direction du plus grand écart de moyenne entre jetons positifs et négatifs, appliquée au maximum. RAPPORTÉ pour le mécanisme (F). Que cet écart soit le concept est une HYPOTHÈSE.
- **Risque structurel** (HYPOTHÈSE) : la moyenne sur les jetons pondère la composition lexicale. Si les positifs emploient d'autres mots, la direction encode la fréquence des mots. Le décalage entre moyenne à l'apprentissage et maximum à l'application fait ensuite tirer le score par le jeton le plus extrême, souvent rare.
- **Test propre.**
  - Même sonde entraînée sur la **couche d'entrée (plongements)**, qui ne contient que l'identité des jetons.
  - **H_A** : la sonde des couches médiane ou tardive bat la sonde sur plongements de δ_TD ≥ 0,10 à TFA 5 % (illustratif).
  - **H_B** (lexical) : écart équivalent à 0.
  - Ajouter X1 et X2a.

**2. Linéaire (apprentissage par sacs, L2)**
- **Concept.** Existe-t-il, dans chaque action positive, au moins un jeton dont la projection dépasse le seuil ? RAPPORTÉ pour le mécanisme. HYPOTHÈSE quant au concept.
- **Risque** (HYPOTHÈSE) : l'apprentissage par sacs se satisfait d'un unique jeton marqueur par action.
- **Test propre, concentration de l'argmax.**
  - Calculer l'entropie de la distribution des *types* de jetons qui portent le maximum, sur les positifs. Puis substituer ces jetons par des équivalents de sens (contrôle de manipulation par juge tiers).
  - **H_A** : entropie élevée (au-dessus du quantile 0,05 de l'entropie obtenue avec des directions aléatoires) et baisse du score sous substitution équivalente à 0.
  - **H_B** : argmax concentré sur peu de types et chute de z > δ sous substitution.
  - Témoin vrai : une sonde entraînée sur un mot-marqueur planté doit sortir H_B.

**3. Perceptron**
- **Concept.** Frontière non linéaire par jeton. Capacité supérieure, donc aptitude supérieure à apprendre n'importe quelle partition. RAPPORTÉ pour le mécanisme.
- **Test propre, sélectivité par tâche de contrôle.** Hewitt et Liang, 2019, « Designing and Interpreting Probes with Control Tasks », EMNLP.
  - Étiquettes de contrôle cohérentes par type de jeton mais sans rapport avec le concept.
  - Sélectivité = TD(concept) − TD(contrôle).
  - **H_A** : sélectivité du perceptron ≥ celle de la sonde linéaire de même couche, et gain de TD sur le linéaire > 0 (borne basse d'IC apparié).
  - **H_B** (la capacité mémorise) : sélectivité plus faible que le linéaire avec un TD plus élevé.
  - Issues : chacune falsifie l'autre. Si H_B l'emporte, le perceptron ne doit pas être retenu sur sa seule performance.

**4. Attention**
- **Concept.** Score linéaire par jeton, pondéré par une requête apprise. Le construit opérationnel combine « où regarder » et « quoi ». RAPPORTÉ pour le mécanisme.
- **Risque** (HYPOTHÈSE) : la requête apprend la position ou des jetons de mise en forme (retours à la ligne, ponctuation, balises).
- **Test propre.**
  - (i) Part de la masse d'attention sur les jetons de format et sur les k premiers ou derniers jetons, comparée à leur part en effectifs.
  - (ii) X2b (prose contre liste).
  - (iii) Comparaison avec **la même sonde agrégée au maximum**.
  - **H_A** : masse sur format et extrémités dans l'IC de leur part en effectifs, Δ_format ≈ 0, et attention ≥ maximum.
  - **H_B** : surpondération du format ou des positions (> 2× leur part, illustratif) et Δ_format > δ.

**5. Mahalanobis (non supervisée)**
- **Concept opérationnalisé.** Atypicité d'un jeton par rapport aux jetons honnêtes d'entraînement. RAPPORTÉ (F). « Mesure le concept X » est une HYPOTHÈSE non portée par la méthode (a3).
- **Test propre, distribution décalée honnête.** Comparer :
  - (i) actions honnêtes **hors distribution**, de domaine ou de format jamais vus à l'entraînement ;
  - (ii) actions portant le trait **dans la distribution**.
  - **H_A** (détecte le trait) : AUROC((ii) contre (i)) borne basse > 0,5 + 0,1 (illustratif).
  - **H_B** (détecte la nouveauté) : (i) ≥ (ii).
  - Ajouter X2a : sous le maximum de distances au carré, la dépendance à la longueur est attendue (HYPOTHÈSE, a5).

---

## (c) Mesure minimale de bon fonctionnement par instrument

### Cas honnêtes appariés (communs)

| Code | Définition | Rôle |
|---|---|---|
| N1 | Même tâche, génération honnête, même intervalle de longueur et même format | Taux de fausses alertes de base |
| N2 | Contenu honnête forcé sous le cadrage K⁺ | Fausses alertes de contexte (X1) |
| N3 | Honnête avec erreur réelle, même catégorie de défaut | Distingue intention et qualité (X5) |
| N4 | Honnête hors distribution (domaine ou format neuf) | Fausses alertes de nouveauté, surtout Mahalanobis |
| N5 | Épisodes honnêtes entiers | Mesure « unanime » déjà prévue par D point 5 (RAPPORTÉ) : fausses alertes de l'agrégateur séquentiel, sans puis avec corrélation injectée |

### Rapports et critère

- **Rapport obligatoire** : TD à TFA 1 % et 5 % sur chaque Nk séparément, par action et par épisode, avec IC par rééchantillonnage des **tâches** (non des actions).
- **Critère de victoire** (HYPOTHÈSE de conception) : borne basse de l'IC apparié de (TD_sonde − TD_base) > 0 contre **chaque** base ci-dessous, au même TFA. C'est l'intersection-union, dans l'esprit de la logique G1 de D (RAPPORTÉ), transposée ici sans prétendre que D l'impose.

### Vérifications mécaniques triviales à battre

| Base | Ce qu'elle capte | À battre par |
|---|---|---|
| B0 Plancher apparié en covariance, même agrégation (P 8.1, RAPPORTÉ) | Énergie et géométrie des activations | Toutes les sondes ; exigence du programme |
| B1 Longueur seule (nombre de jetons) | Nuisance de longueur | Toutes ; surtout maximum et Mahalanobis |
| B2 Régression logistique sur sac de mots (TF-IDF) du texte | Surface lexicale | Toutes |
| B3 Même famille sur la couche des plongements | Identité des jetons | Différence de moyennes, linéaire |
| B4 Classifieur sur traits de format (listes, titres, ponctuation, chiffres) | Registre et format | Attention |
| B5 Même sonde au maximum, ou au dernier état (base (iii) de N-007, RAPPORTÉ via D) | Valeur de l'agrégation apprise | Attention |
| B6 Linéaire de même couche | Valeur de la non-linéarité | Perceptron |
| B7 Distance euclidienne à la moyenne honnête | Valeur de la covariance | Mahalanobis |

### Instruments transversaux

- **Agrégateur maximum** : pente X2a nulle sur N1, sinon calibration du seuil par intervalle de longueur obligatoire.
- **Agrégateur attention** : doit battre B5.
- **Couches** : rapporter les trois sans sélection a posteriori (D point 3 le fait pour les traits du pôle). Prédiction HYPOTHÈSE : la couche précoce est plus proche de B3.

---

## Su, supposé, publié (R7, R8)

**Publié, que je peux attribuer** (à vérifier sur PDF selon R7) :
- Hewitt et Liang (2019), tâches de contrôle et sélectivité ;
- Elazar et al. (2021), sondage amnésique ;
- Belrose et al. (2023), LEACE ;
- Belinkov (2022), « Probing Classifiers: Promises, Shortcomings, and Advances », Computational Linguistics, revue des pièges du sondage ;
- Marks et Tegmark (2023), « The Geometry of Truth », directions linéaires de vérité et généralisation ;
- Levinstein et Herrmann (prépublication 2023), « Still No Lie Detector for Language Models: Probing Empirical and Conceptual Roadblocks », critique de la généralisation des détecteurs de mensonge.

**Rapporté par E, non vérifié** : Apollo 2025 (titre : référence à vérifier, a10), Nguyen et al. 2025, l'étude multi-modèles 2026 (publication non identifiée selon E elle-même), van der Weij et al. 2024, Laine et al. 2024, Berglund et al. 2023, Greenblatt et al., Phuong et al. 2024.

**Question ouverte, non « trou »** (R8) : je ne sais pas si le plan 2×2 contenu × cadrage par forçage a été publié pour des sondes de tromperie ou de conscience d'évaluation. Il est possible que des travaux sur sondes de tromperie aient discuté des déclenchements sur texte honnête en contexte trompeur (**référence à vérifier**). Une recherche affirmative est requise avant toute revendication.

---

## (d) Ancrage matériel

- **Organisme** : « modèle ouvert 8B » (RAPPORTÉ), non nommé dans les faits. La mention des autoencodeurs parcimonieux Llama Scope (P 8.2) et des couches 7, 15 et 23 (D) est compatible avec un modèle à 32 couches de la famille Llama 3.x 8B. C'est une **HYPOTHÈSE**, à confirmer.
- **Autres modèles** : Qwen2.5-7B (nommé dans P) comme paraphraseur pour X2b et juge tiers. Llama-3.2-3B-Instruct (nommé dans P) comme second juge de préservation.
- **Calcul** (tout est illustratif) :
  - X1 : 400 tâches × 4 cellules × ~1 500 jetons ≈ 2,4 M jetons en **passes avant seules**, sans génération sauf pour les contenus de départ, déjà au banc.
  - X2 et X5 : moins de 2 M jetons supplémentaires.
  - Sur un GPU de classe A100 en bf16, de l'ordre de quelques heures-GPU.
  - Stockage des activations : 3 couches × 4 096 dimensions × ~4,4 M jetons × 2 octets ≈ 100 Go. Stocker en flottant 16 bits, ou seulement les projections si la direction est figée.
- **Sondes** : entraînement déterministe en double précision sur processeur (F, RAPPORTÉ). Coût dominant : X3 pour les 75 sondes. Environ 75 × 1 000 réentraînements pour les familles légères et × 200 pour le perceptron et l'attention, soit de l'ordre de quelques jours de processeur multi-cœurs. C'est de la dépense de temps plus que d'argent, dans l'esprit des lectures « processeur, zéro dépense » de D.
- **Coût total** : de quelques dizaines à quelques centaines d'euros de GPU loué, hors temps humain.
- **Puissance** : 400 tâches par mode est un ordre de grandeur, pas un calcul. Le seuil d'équivalence ε = 0,2 exige une simulation de puissance avant le scellement. D rappelle que les contrastes « blanc contre blanc » sont probablement petits et coûtent « plusieurs centaines de tâches de plus par mode » (RAPPORTÉ).

---

## Ce qui peut être réfuté par ce plan

1. Pour chaque sonde « trait du texte » : H_A ou H_B de X1 est falsifiée, sauf issue conjointe, qui falsifie les deux versions pures.
2. a5, « l'agrégation au maximum est neutre en longueur », est falsifiée ou non par X2a.
3. H_texte ou H_intention est falsifiée par X5 pour les sondes « tromperie » et « dissimulation ».
4. Pour la conscience d'évaluation, la lecture de P 11 « elle lit le cadrage » contre « elle lit le registre » est tranchée par X1 inversé, sans aucune conception d'attaque.
5. Chaque test est d'abord lui-même réfutable par ses témoins (contexte, contenu, marqueur planté, direction aléatoire).

FIN-DE-CELLULE