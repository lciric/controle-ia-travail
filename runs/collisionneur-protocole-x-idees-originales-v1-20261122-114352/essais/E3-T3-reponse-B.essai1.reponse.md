# Proposition B · Tour III.3 · Réponse aux critiques

## 0. État des pièces

- **Présentes** : ma conception III.1 et les critiques A, C, D, E et F. Chacune se termine par sa ligne FIN-DE-CELLULE, sans coupure visible. Je n'ai pas recalculé les empreintes.
- **FAITS** : le bloc ne contient que la question. Aucun fait muni d'un statut n'est transmis. Tout ce qui suit est donc HYPOTHÈSE, dérivation (calcul refait par moi), ou référence RAPPORTÉE avec le statut de III.1, inchangé.
- **Statuts des critiques** : plusieurs critiques étiquettent leurs calculs « VÉRIFIÉ mathématiquement ». Je ne modifie pas ces étiquettes. Quand je reprends un de ces calculs, je l'ai refait et je le marque « dérivation ».
- **Périmètre** : je ne réponds qu'aux sections « Sur la proposition B ».
- **Notation** : « A-a2 » désigne le point 2 de la section (a) de la critique A.
- **Objections identiques** : quand plusieurs critiques soulèvent la même objection, je le dis et j'y réponds une fois. Je ne prétends pas qu'elles disent la même chose au-delà de ce point.

---

## 1. (a) Décision sur chaque critique

| Réf. | Objection | Décision | Ce qui change |
|---|---|---|---|
| A-a1 | Y compte le rare sous G₀ alors que I1/I2 changent de modèle. Leurs modes propres sont rares sous G₀ par construction. Un rapport mesuré à un seul budget ne tranche rien. | **Acceptée** | E2′ est mesuré en courbe sur trois budgets. Ajout d'un contrôle par échange des rôles (A-c2). La grandeur visée porte sur un ensemble cible **G figé** (§2.1). |
| A-a2, A-c3, F-a2, D-c | Les leurres identifient le FPR sous leur propre loi, pas sous celle des faux réellement émis dans la strate. | **Acceptée** | Le FPR est estimé sur des **faux naturels** étiquetés par la vérité plantée (E1a). Les leurres deviennent un test de résistance secondaire et ne servent jamais d'estimateur. |
| A-a3, C-a2, F-a5 | (i) Les mondes plantés sont construits en consultant G₀. (ii) π est choisi par le concepteur. (iii) Sur le terrain exact, le FDR est nul par construction. | **Acceptée** | (i) Banc neutre (T1). (ii) π devient un facteur expérimental, valeur 0 incluse. (iii) Terrain réel doublé d'un contrôle volontairement dégradé O_dég, avec audit exact (T3). |
| F-a1 | Placer les vérités « contre » G₀ avantage toute intervention qui s'en éloigne. | **Rejetée telle quelle, transformée en test** | Viser le rare sous G₀ est la définition même de la cible, ce n'est pas une fuite. La fuite réelle est que le concepteur fixe la densité de vérités dans la queue. Test : banc neutre T1 contre banc ciblé T2. Si le gain d'une intervention disparaît sur T1, il est attribué à la construction du banc. |
| D-a1 | Planter garantit l'existence des vérités, pas leur faible probabilité. | **Acceptée** | La rareté des vérités plantées est mesurée sur un pilote disjoint, jamais réutilisé. |
| A-a4 | Pour I5, une baisse du taux de réplication confond l'effet Goodhart et une baisse de π. | **Acceptée** | Duel I5′ : P(O=1 \| faux) par bras, puis P(O′=1 \| O=1, faux), sur bancs plantés (§2.5). |
| A-a5, F-a3, F-b | Le bootstrap sur f₁ est décentré. | **Acceptée** | Dérivation : P(N\*=1 \| N=k) = k(1−k/N)^(N−1) ≈ k·e^(−k), soit environ 0,37 pour un singleton. Le bootstrap multinomial est retiré. On le remplace par des réplicats indépendants de taille N, ou par un intervalle analytique pour la couverture de Good–Turing (référence à vérifier). Dans les deux cas, la **couverture est contrôlée sur des lois connues** (plate, Zipf) avant tout usage. Le bootstrap naïf reste comme comparateur, et il doit échouer. |
| A-a6 | Qui étiquette les paires servant à valider C ? | **Acceptée** | Étiquettes **par construction uniquement**. L'équivalence vient de transformations neutres. La non-équivalence n'est retenue que si un témoin de désaccord a été exécuté. En domaine infini, la fusion abusive ne se mesure que sur des paires à témoin connu : c'est une limite déclarée. |
| A-b1 | Les erreurs de C (q = fusions, u = scissions) biaisent Û. | **Acceptée** | Condition d'éligibilité de E0′ (§2.2). |
| A-b2 | Valider les p-valeurs au seuil α/m demande de l'ordre de m/α tirages nuls par strate. 10³ ne suffit pas. | **Acceptée** | Nouveau test E1c. Soit la taille de calibration est dimensionnée sur m/α (dérivation), soit m est plafonné et ce plafond est préenregistré. |
| A-b3, E-b2, F-b | Effectifs faibles : Y_B₀ ≈ 0 rend le rapport non borné, R = 0 donne 0/0, 5 graines ne suffisent pas. | **Acceptée** | Différence additive à la place du rapport. FDR = E[F/(R∨1)], convention que je reprends de D. L'unité de réplication devient le couple (instance de monde, graine), en nombre fixé par une analyse de puissance. L'issue « non tranché » est explicite (§2.0). |
| A-b4, E-a3, F-a4 | Le recouvrement Σmin(p_i, p_j) est biaisé, dominé par les modes, et vaut 1 en population pour deux graines de même loi. | **Acceptée, c'est une erreur de ma part** | Mon H_B (« inter ≥ intra ») ne pouvait se réaliser qu'à l'égalité exacte. Le duel I2 est remplacé par un duel en pseudo-familles portant sur Y (§2.5). |
| A-c1, F-c4 | Essai A/A. | **Acceptée** | Il fournit la loi nulle de ΔY et de ΔFDR dans E2′. |
| A-c4, D-a2 | Sous canonisation comportementale, le générateur uniforme s'effondre ou sature un petit support. | **Acceptée** | Le contrôle de E0′ devient un générateur simulé **à loi connue sur l'espace des classes**, et non sur celui des syntaxes. |
| C-a1, E-a2, F-a6 | Le canoniseur par plongement réintroduit un juge-modèle. Son calibrage sur des paraphrases ne contrôle pas la queue. | **Acceptée** | Le plongement est retiré du rôle de canoniseur. Il ne reste que dans la colonne « comparateur juge-modèle ». Sans forme normale, la rareté n'est pas mesurée, ce qui est cohérent avec III.1 §2. |
| C-a3, E-a4, F-a2 | Le rapprochement avec les knockoffs est faux : les leurres sont construits à partir de vérités connues. | **Acceptée** | Je n'invoque plus Barber et Candès (2015) comme justification. Hors mondes plantés, je ne propose **aucun** compteur de FDR, et je le déclare. |
| C-b1, E-b4 | Si les erreurs de O et O′ sont corrélées, la réplication ne protège plus quand π est petit. | **Acceptée** | Dérivation : α_joint = α_O·α_O′ + Cov(O, O′ \| faux). Nouveau test E1d. I6 ne revendique plus de borne produit. |
| C-b2, F-b | Chao1 est indéfini si f₂ = 0, et sa variance explose. | **Acceptée sur le fond, rejetée sur la portée** | Chao1 n'intervenait dans aucune décision. Il est retiré des critères. S'il est rapporté, ce sera sous forme corrigée f₁(f₁−1)/(2(f₂+1)) (attribution à vérifier), avec mention « non jugeable » si f₂ est faible. J'accepte aussi le point de D : la masse invisible ne dit rien de son découpage en classes. |
| C-b3, E-b1 (plug-in), F-a3 | Incohérence entre §2.4 (borne) et E2 (estimateur ponctuel). De plus, la règle de trois est appliquée sans correction de multiplicité. | **Acceptée, incohérence réelle** | L'ensemble G est défini par une **borne supérieure simultanée** (§2.1). |
| C-c1, E-c2, D-c | Pour I1, le bruit de format des modèles de base se confond avec la diversité. | **Acceptée, transformée en test** | Test T-fmt (§2.5) et décodage contraint identique dans les deux bras. |
| C-c2, E-c1 | Mesurer ρ(O, O′) sur des faux construits contre O. | **Acceptée** | Intégré à E1d. |
| D-a3 | L'accord des taux de doublons entre exécution locale et fournisseur ne prouve pas l'indépendance des appels. | **Acceptée** | Le test de doublons peut seulement *rejeter* l'indépendance. La seule garantie vient de l'inférence locale à graines maîtrisées. Les résultats obtenus via l'interface d'un fournisseur sont déclarés conditionnels à P5. |
| D-a4 | Dans E1, une chute de sensibilité seule laisse H_A et H_B toutes deux fausses. | **Acceptée** | E1 est scindé en duels séparés pour le FPR (E1a) et le TPR (E1b). |
| D-a5 | Les sorties hors format et le réglage de température disparaissent du budget. | **Acceptée** | Tout entre au dénominateur budgétaire : rejets, réglages, pilotes. |
| D-a6 | La température agit sur les jetons, pas nécessairement sur la masse des classes. | **Acceptée** | Je retire pour I4 la phrase « garantit mécaniquement plus de masse sur la queue ». Elle n'est vraie qu'au niveau des jetons. |
| D-b (I1–I4) | Un rejet qui laisse P_I(c \| c∈G) = P₀(c \| c∈G) ne diversifie pas la loi à l'intérieur de G. | **Acceptée, transformée en test** | Duel I3′ contre une renormalisation mécanique (§2.5). |
| D-b (I5–I6), D-c | Sans audit des rejetés, les faux négatifs ne sont pas identifiables. | **Acceptée** | Audit d'un échantillon aléatoire des rejets dans I6′. |
| D-c | Pseudo-familles, mondes sans vérité rare, appariement base/instruit. | **Acceptée** | Intégré à I2′, E2′ et I1′. |
| E-a1 | Le dénominateur du FDR n'est pas précisé. Les vrais fréquents de B₀ diluent ses faux. | **Acceptée** | Critère FDR_rare, calculé sur les confirmées appartenant à G. Le FDR global est rapporté à part et ne décide rien. |
| E-b1 (E0) | Des artefacts syntaxiques peuvent pousser Û au-dessus de ε, et Û < ε reste possible sans puits vrai. | **Acceptée pour l'artefact (c'est A-b1), rejetée sur la portée** | E0 ne prétend pas établir l'existence de puits vrais (P6). Ce rôle revient à l'estimation de π par strate sur banc planté. |
| E-c3, D-c | Monde à queue entièrement fausse (π_rare = 0). | **Acceptée** | Contrôle obligatoire de E2′. |
| F-b (E1) | La taille requise pour l'intervalle doit être explicite. | **Acceptée** | C'était déjà mon critère (demi-largeur < δ/2). La formule est explicitée. |
| F-b (BY) | La correction de Benjamini–Yekutieli effondre la puissance. | **Acceptée** | BY ne sert qu'en repli, si l'hypothèse de dépendance positive est rejetée. |
| F-c3 | Le duel I2 est confondu par l'entropie. | **Acceptée** | Pseudo-familles par températures distinctes d'un même modèle, comme contrôle (§2.5). |

---

## 2. (b) Expériences corrigées

Tous les seuils restent **illustratifs** et sont à préenregistrer.

### 2.0 Règle de décision et respect de B4

Je reprends la règle proposée par D, en le disant. On fixe une région de succès G_A sur le paramètre de population, et une région de confiance simultanée R.

- Si R est incluse dans G_A, H_B est réfutée.
- Si R est disjointe de G_A, H_A est réfutée.
- Sinon, l'issue est « non tranché ». Elle falsifie **H_puiss**, l'hypothèse de puissance préenregistrée. Une extension unique, préenregistrée elle aussi, est alors déclenchée. Un second « non tranché » est publié comme « non jugeable à ce budget ».

Chaque issue falsifie donc quelque chose. Toutes les contraintes portant sur le FDR ont une marge δ > 0, pour éviter qu'une égalité exacte rende la non-infériorité indécidable.

### 2.1 Terrains et ensemble cible

**Terrains**
- **T1, banc neutre.** Les vérités sont tirées d'une loi paramétrique fixée **avant tout appel** à G₀. Leur rareté est mesurée après coup, sur un échantillon disjoint.
- **T2, banc ciblé.** Construit à partir d'un pilote G₀ qui ne sert plus jamais ensuite.
- **Facteur π** dans la strate rare : {0 ; faible ; modéré} (illustratif).
- **T3, terrain réel à contrôle exact**, utilisé en deux modes :
  - avec O exact, pour mesurer le rendement ;
  - avec **O_dég**, un contrôle tronqué à taux d'erreur connu, l'audit restant exact, pour mesurer le FDR.

**Ensemble cible G.** G contient les classes c dont la borne supérieure simultanée de p_G₀(c) est au plus τ. Cette borne est calculée sur un échantillon de référence S_réf, disjoint de tous les bras, avec un nombre M de classes candidates plafonné à l'avance.

**Condition de faisabilité** (dérivation) : N_réf ≥ ln(M/α)/τ. Par exemple, avec M = 10⁴, α = 0,05 et τ = 10⁻³, il faut N_réf ≳ 1,2·10⁴ (illustratif). Si la condition n'est pas remplie, on a Y ≡ 0 et le plan est déclaré invalide **avant** toute collecte. G est figé avant l'ouverture des bras.

### 2.2 P-C · Validation du canoniseur, préalable à tout le reste

On mesure q (fusions abusives, sur paires à témoin exécuté) et u (scissions, sur paires équivalentes par construction). On en déduit une borne sur le biais de Û.

- **H_A** : le biais induit est inférieur à ε/2.
- **H_B** : il est au moins égal à ε/2.

Si H_A est falsifiée, E0′ n'est pas jugeable avec ce canoniseur. On garde alors l'égalité exacte après normalisation, ou MinHash s'il fait mieux.

### 2.3 E0′ · Les appels indépendants convergent-ils ?

- **H_A** : Û(N) < ε.
- **H_B** : Û(N) ≥ ε.
- **Intervalle** : réplicats indépendants, ou formule analytique (référence à vérifier), avec couverture validée sur lois connues.
- **Contrôles** :
  - une loi simulée plate sur les classes doit tomber en H_B ;
  - une loi simulée concentrée doit tomber en H_A ;
  - test de doublons local/fournisseur, qui peut seulement rejeter l'indépendance (D-a3).
- **Falsification** : comme en III.1, inchangée.
- **Portée** : E0′ décide si la rareté est discriminante à ce budget, pas si des puits vrais existent.

### 2.4 E1′ · Le contrôle reste-t-il fiable dans la queue ? (sur T1, T2 et T3 avec O_dég)

**E1a · Faux positifs**
- **H_A** : FPR(rare) − FPR(essai) ≤ δ, mesuré sur des **faux naturels** émis par G₀ et par les bras, stratifiés selon S_réf.
- **H_B** : l'écart dépasse δ.
- Taille par strate : n_r ≥ 4z²f(1−f)/δ² (dérivation).
- Les leurres minimalement perturbés restent un test de résistance rapporté à part.

**E1b · Sensibilité.** Même structure sur le TPR.

**E1c · Validité des p-valeurs**
- **H_A** : P(p ≤ t \| faux, rare) ≤ t(1+η) pour t ∈ {α/m, …, α}.
- **H_B** : la borne est violée.
- La calibration nulle est dimensionnée sur m/α (dérivation), ou m est plafonné.

**E1d · Indépendance des erreurs de O et O′.** On soumet aux deux contrôles des faux construits par optimisation directe contre O, sans modèle de langue, plus des faux naturels.
- **H_A** : FPR(O∧O′) ≤ FPR(O)·FPR(O′) + δ′.
- **H_B** : l'excès dépasse δ′.

### 2.5 E2′ · Gabarit à coût égal

**Grandeur visée.** Y = nombre de classes de G trouvées, confirmées par O et vraies. On compare ΔY = Y_I − Y_B₀ et ΔFDR_rare, avec FDR_rare = E[F/(R∨1)] calculé sur les confirmées de G.

**Budget.** Il inclut les sorties hors format, les rejets, les réglages et les pilotes. Trois niveaux de budget.

**Hypothèses**
- **H_A** : ΔY ≥ m_Y au budget maximal, avec m_Y fixé au-delà du 97,5ᵉ centile de la loi A/A (illustratif), **et** ΔFDR_rare ≤ δ.
- **H_B** : l'une des deux conditions échoue.

**Contrôles**
- A/A ;
- échange des rôles : un gain symétrique, mesuré avec une référence prise dans le bras I, signale une différence de modes et non un accès à la queue ;
- générateur aléatoire non-LLM au même coût ;
- placebo d'invite ;
- monde π_rare = 0 : toute confirmée dans G y est fausse.

**Duels spécifiques par intervention**

- **I1′ (modèles de base).** Pré-test T-fmt : un même lot d'idées est emballé dans le format brut des modèles de base et dans le gabarit instruit, puis passé dans (C, O).
  - H_A : classes et verdicts restent invariants à la tolérance près.
  - H_B : le format scinde les classes ou change les verdicts.
  - Si H_A est falsifiée, I1 n'est comparé qu'avec un décodage contraint identique dans les deux bras.
- **I2′ (familles différentes).** À budget total égal, on compare Y pour l'union de deux familles et Y pour l'union de deux **pseudo-familles** obtenues en partageant une même famille, à nombre égal de sorties analysables.
  - H_A : la différence dépasse la marge A/A.
  - H_B : non.
  - Contrôle d'entropie : des pseudo-familles formées de deux températures d'un même modèle ne doivent pas franchir la marge.
- **I3′ (exclusion des modes).** Le comparateur est B₀ suivi d'un **rejet a posteriori** des classes exclues, coût de génération compris. Ce rejet reproduit exactement la loi renormalisée.
  - H_A : l'exclusion par invite bat ce comparateur à coût égal, donc elle modifie la loi à l'intérieur de G.
  - H_B : elle ne le bat pas.
  - Pour l'exclusion par rejet mécanique, la renormalisation est exacte par construction. Son seul gain possible est l'économie de contrôles, qui se mesure directement.
- **I4′ (température).** La température est choisie sur des instances de calibrage disjointes. H_A : Y croît avec la température au-delà de la marge A/A, à coût égal. On rapporte le point de retournement.
- **I5′ (boucle évolutive).** Sur T1 et T2 :
  - H_A : P(O=1 \| faux) dans le bras bouclé ≤ celle de B₀ + δ, **et** P(O′=1 \| O=1, faux) n'augmente pas au-delà de δ ;
  - H_B : l'une des deux augmente au-delà de δ.
- **I6′ (allocation du budget de contrôle).**
  - BH n'est utilisé que si E1c retient H_A ; BY en repli.
  - La réplication sur O′ n'est créditée que si E1d retient H_A.
  - Un échantillon aléatoire des rejets est audité, pour estimer les faux négatifs.
  - Abandon si FDR_rare dépasse α + δ dans le monde π = 0.

L'interaction **I4 + I6** est conservée, avec le critère de III.1, désormais évalué sur ΔY.

---

## 3. (c) Réponse à la question de l'arbitre

**Ce qui est établi.**

Aucun résultat empirique. Le bloc FAITS n'en contient aucun, et je n'en invente pas.

Seules des dérivations conditionnelles tiennent. Elles bornent ce qu'on peut espérer :

1. **Coût de la rareté.** Certifier qu'une classe est rare au seuil τ, simultanément pour M classes, exige un échantillon de référence N ≥ ln(M/α)/τ. En dessous, aucune découverte rare n'est certifiable. Un estimateur ponctuel laisse en revanche entrer des classes semi-fréquentes.
2. **Ce que dit Good–Turing.** Good (1953 ; RAPPORTÉ) estime la masse *agrégée* non observée. Il ne classe pas les singletons entre eux.
3. **Taux de base.** Parmi les confirmées rares, la part de fausses est au moins f(1−π) / (f(1−π) + TPR·π), où f est le FPR de O. Elle tend vers 1 quand π tend vers 0, ce qui rejoint la logique de Ioannidis (2005 ; RAPPORTÉ).
4. **Limite de la réplication.** Avec des erreurs corrélées, le taux de faux positifs joint vaut α_O·α_O′ + Cov. Si π est petit devant ce terme de covariance, la réplication ne restaure pas le contrôle du FDR.
5. **Indices de la littérature.** FunSearch (Romera-Paredes et al., 2024 ; RAPPORTÉ) montre des découvertes avec un évaluateur **exact**. Ce travail ne renseigne donc pas sur un contrôle imparfait. Gao et al. (2023 ; RAPPORTÉ) n'est qu'une analogie pour l'effet Goodhart.

**Ce qui n'est pas établi.**

- si des appels indépendants convergent (E0′) ;
- si le contrôle garde ses caractéristiques opératoires dans la queue (E1a, E1b) ;
- si ses p-valeurs y sont valides (E1c) ;
- si un second contrôle a des erreurs indépendantes du premier (E1d) ;
- si une intervention augmente Y à coût égal sans dégrader FDR_rare (E2′) ;
- si plusieurs familles valent mieux que des pseudo-familles d'une même famille (I2′) ;
- si un gain observé sur banc planté survit sur le banc neutre et sur le terrain réel muni de O_dég.

Plusieurs de mes propres outils de III.1 sont retirés comme mal fondés : le bootstrap sur f₁, le recouvrement Σmin, le rapprochement avec les knockoffs, le canoniseur par plongement, et la « garantie » de queue pour la température.

**L'expérience à faire en premier : E1′, volets a et d.**

- **Préalables** : P-C et l'échantillon de référence S_réf. E0′ partage ce même échantillon, si bien que son coût s'ajoute à peine.
- **Terrains** : banc neutre T1 et terrain réel T3 avec O_dég.
- **Pourquoi elle d'abord** : elle décide si la question est soluble *avec ce contrôle*, avant toute dépense sur les générateurs.
- **Résultat qui fait tout réorienter** : la borne inférieure de l'intervalle sur FPR(rare) − FPR(essai) dépasse δ, **et** FPR(O∧O′) dépasse FPR(O)·FPR(O′) + δ′. J'abandonne alors I1 à I5 comme moyens d'atteindre l'objectif : tout déplacement de masse vers G augmenterait les fausses découvertes, et la réplication ne le corrigerait pas. Le problème se repose comme l'amélioration du contrôle dans la queue, pas du générateur.
- **Résultat qui ouvre la suite** : H_B est falsifiée dans les deux volets. On passe alors à E0′, puis à E2′.
- **Issue intermédiaire** : un seul des deux volets falsifie H_A. Si c'est E1a seul, on garde I6 avec réplication, puisque E1d valide l'indépendance de O et O′. Si c'est E1d seul, on garde les interventions sans créditer la réplication.

FIN-DE-CELLULE