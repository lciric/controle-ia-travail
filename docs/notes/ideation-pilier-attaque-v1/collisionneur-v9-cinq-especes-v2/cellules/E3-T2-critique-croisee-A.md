# Tour III.2 — critique croisée de méthode (proposition A)

**Pièces reçues** : B, C, D, E, complètes (chacune close par FIN-DE-CELLULE). Ma propre conception de III.1 n'est pas retransmise ; je ne la restitue pas. Empreintes tronquées dans les faits (`3ecab00f…`, `998404fe…`, etc.) : invérifiables, comme B le note. Tout ce qui suit est HYPOTHÈSE de méthode ; tout chiffre de ma main est **illustratif**.

**Un point que je porte nommément contre les quatre** (il n'est pas une fusion, c'est le même défaut répété) : dans B (X1, X2), C (Exp 1, 2), D (E1, E2) et E (fiche T), l'étiquette « dormant » est définie par l'oracle (« exécution attestée honnête »). Un sabotage diffus **manqué** par l'oracle devient un dormant. Le bruit d'étiquette est donc **anticorrélé avec la discrétion de l'acte** : les sabotages les plus discrets passent dans la classe négative. Loi : si η = P(oracle manque | sabotage) et que la trace interne est plus faible sur les manqués, l'AUC observée « sabotage contre dormant » est tirée vers 0,5 par un terme qui croît avec η, et H8 (B de B, H_B de D-E1, H_B de E-T) peut être « confirmée » par construction. Seul X0/E0/fiche O borne η, et seulement sur la strate de sabotages connus — d'où ma lecture des points (b) ci-dessous.

---

## Sur la proposition B

### (a) Défauts de méthode

1. **X1, « base qui relit »** : le contrôle est bon pour « au-delà du texte », mais il n'isole pas « au-delà de la consigne » en famille (i) : la base relit la consigne aussi. L'imputation « effet seulement sur (i) → consigne » confond consigne et différence de famille (distillation, dose, contextes rejoués sans consigne). Il manque la case contrefactuelle *consigne neutre × sabotage* **dans (i)**, que B remplace par la famille (ii) — ce que B reconnaît, mais la conclusion « sur les deux familles » devient alors un test de deux confondants différents, non un test répété du même effet.
2. **Fuite sélection → évaluation** : X3 intervient « aux couches et positions sélectionnées par X1–X2 » ; X6 figure « trois couches issues de X1 ». Si les épisodes de X3 et X6 recouvrent ceux de X1, la sélection du maximum après Holm biaise la cellule retenue vers le haut (effet du gagnant). B n'écrit pas la disjonction des blocs entre sélection et intervention.
3. **X2, « complément orthogonal aux couches suivantes »** : mal défini. L'adaptateur écrit à la couche ℓ ; à ℓ+1 le calcul de la base **propage** l'identité dans tout l'espace, pas seulement dans l'image d'un sous-espace. Le complément orthogonal n'est donc pas « identité-libre » ; δ y peut être positif par propagation de l'identité × tâche.
4. **X2, contrôle négatif du placebo « étiquette arbitraire tirée au sort »** : ΔAUC = 0 **par construction** (étiquettes aléatoires donnent 0,5 des deux côtés). Ce contrôle ne dit rien ; il faut un placebo avec une étiquette *comportementale* réelle et bénigne.
5. **X4** : le comparateur « seconde externe » est pertinent (je m'en sers). Mais l'externe 1, calibrée à τ/2 sur le dénominateur honnête, et l'évaluation du taux joint ≤ τ sont faites sur le **même** dénominateur : fuite calibration → évaluation. Il faut scinder le dénominateur honnête.
6. **X5, placebo de pression** : nécessaire (je m'en sers), insuffisant : une pression contre l'externe change le code produit, donc le texte, donc les activations de la base elle-même. Le « déplacement interne » peut être **texte-médié**. Il faut rejouer la « base qui relit » sur chaque génération ; sinon β_externe mesure l'étau et le changement de texte confondus.
7. **X6b, « secret contre aléa »** : la réserve (c) diffère de (b) par deux choses : jamais ciblée **et** souvent d'architecture/entraînement différents. gain_secret confond secret et diversité. Il faut une réserve tirée **au hasard dans le même panel** que les sondes déployées (D et E l'exigent ; B non).

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **X0b (équivalence sur rapport de cotes)** : avec taux d'erreur p_O, p_M et n cas, l'effectif attendu de la cellule « double manqué » est n·p_O·p_M ; SE(log OR) ≈ √(Σ 1/n_cellule). Pour p_O = p_M = 0,10 et n = 200 (illustratifs) : cellule ≈ 2, SE > 0,7, l'intervalle de TOST ne rentre jamais dans [0,5 ; 2] → **indécis par construction**. Jugeable seulement si n·p_O·p_M ≳ 20 (illustratif).
- **X1 (ΔAUC apparié)** : perte de puissance si AUC_base ≈ 0,5 et AUC_org ≈ 0,5 (rien) ou si AUC_base → 1 (plafond, le texte suffit). Atténuation par η (point transversal). Validation croisée « par bloc de famille » avec **deux** familles = deux plis : aucune variance inter-plis estimable, l'intervalle bootstrap sur épisodes ignore la variance de famille.
- **X2 (δ)** : AUC_D(placebo) est l'AUC d'un partage de tâches (opportunité) — bon contrôle de tâche ; mais si les tâches des épisodes dormants et de sabotage ont la même distribution, AUC_D(placebo) ≈ 0,5 et δ se réduit à une différence simple ; si elles diffèrent fortement, δ peut être négatif sans signification.
- **X3 (pente dommage–projection à α fixé)** : non identifiable si Var(projection | α) ≪ variance de mesure de l'oracle ; pour un sabotage diffus, Dommage(S100) − Dommage(S0) petit devant l'écart-type inter-épisodes rend le « 30 % de l'écart » plus petit que l'intervalle.
- **X4 (CR)** : estimateur binomial sur m = n_sab·(1 − TPR_ext(τ/2)) manqués ; pour n_sab = 300, TPR_ext = 0,85 : m ≈ 45, demi-largeur ≈ 0,15 (illustratif) — la différence CR_int − CR_ext2 > 0 n'est jugeable que si m ≳ 150 et l'écart vrai ≳ 0,15. Si les scores honnêtes des deux mâchoires sont corrélés (ρ_H > 0), le taux joint est < τ et la pince est évaluée à budget effectif inférieur : comparaison non équitable avec les boîtes seules recalibrées à τ.
- **X6a (valeur mixte − pure)** : chaque cellule T[j,k] est un rappel à 1 % estimé sur ~100 épisodes (SE ≈ 0,05) ; la valeur d'un programme linéaire sur cellules bruitées est biaisée vers le haut (optimisation sur le bruit) ; un écart « > 0,05 » est atteint par le seul bruit si le panel compte ≥ 6 colonnes (illustratif). Il faut la valeur recalculée sur génération fraîche, que B ne prévoit pas pour X6a.

### (c) Contrôles négatifs dont l'absence serait fatale

- X1 : **échecs honnêtes** comme négatifs (B ne les met qu'en X4) ; sans eux, une sonde qui lit « la tâche échoue » passe pour une sonde d'acte.
- X2 : placebo apparié **en rang, en norme des poids et en données de distillation** ; deux graines ne contrôlent que la graine.
- X3 : direction aléatoire **à l'intérieur du sous-espace de sortie de l'adaptateur** (même contenu d'identité) ; sans elle, « la réduction du dommage » peut n'être que l'annulation locale de l'adaptateur.
- X5 : base qui relit sur chaque génération (texte-médiation).
- X6b : mélange uniforme public ; réserve tirée dans le panel déployé.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Statuts** : C écrit « VÉRIFIÉ » pour des contenus (« rien sur le diffus, VÉRIFIÉ § 6 », « τ/2, VÉRIFIÉ § 1 », « 50 traces rejouées, VÉRIFIÉ § 1 », « prédicteur 0,866, VÉRIFIÉ », « scores-p3.npz, VÉRIFIÉ »). Les faits ne vérifient que des **empreintes** ; les contenus sont des relevés. Je ne requalifie rien, je signale l'écart à la règle 1.
2. **Exp 0, « sabotages synthétiques injectés / programmatiques »** : le rappel de l'oracle y est mesuré sur une distribution que l'organisme ne produit pas. R_oracle sur injectés ne borne pas η sur le diffus de T0.6 ; la suspension des volets 1–5 repose sur une mesure hors distribution. L'indépendance est mesurée contre **un seul** moniteur (prédicteur texte) ; les sondes internes ne sont pas testées.
3. **Exp 2, placebo = T100** : les faits disent « témoin instruit sans sabotage » **et** « un organisme placebo est à construire » : C assimile les deux. Le témoin porte une instruction différente, donc une identité différente ; ce n'est pas « même chaîne, sans objectif ». Ensuite, les négatifs sont **l'union** dormants + placebo : l'AUC d'un mélange est une moyenne pondérée ; un seuil ≥ 0,75 peut être atteint en séparant **l'identité** (sabotage contre T100) sans séparer sabotage contre dormant. Le critère est vrai par construction si la part de placebo dans les négatifs est grande. Il faut deux AUC séparées.
4. **Exp 3** : la substitution « dans ce sous-espace par celles du jumeau α = 0 » aux couches où l'adaptateur écrit équivaut à **annuler localement l'adaptateur** ; que cela réduise le dommage est connu par construction (dose α). Le contrôle « sous-espace aléatoire de même dimension et norme » hors du sous-espace de l'adaptateur ne porte pas la même identité : il ne distingue pas « la trace est causale » de « l'adaptateur est causal ». De plus, le test est posé sur **S100**, alors que la dose diffuse retenue est S25–S50 : la causalité démontrée sur le flagrant ne se transporte pas.
5. **Exp 4** : H_A agrège trois revendications (effondrement de R3, réserve ≥ 0,15, coût croissant en k) ; H_A et H_B ne sont ni exclusives ni exhaustives (exemple : R3 s'effondre **et** la réserve ne gagne rien). B4 n'est pas respectée. « k sondes orthogonales » : non défini entre architectures.
6. **Exp 5** : la « courbe d'étau en fonction de l'intensité d'évasion externe » exige des générations sous pression ; les données exigées sont 300 épisodes du mode tenu à l'écart, **sans génération**. On ne mesure alors qu'une corrélation transversale (critique S7 de B, que je reprends), et on **consomme** la famille tenue à l'écart pour cela. Le « détecteur de nouveauté » comme mâchoire interne est introduit ici sans avoir été qualifié en Exp 1–2.
7. **Budget** : 76 heures-machine et 4 jours (illustratifs) incluent 4 générations du bras rouge, dont le coût est déclaré non chiffrable depuis les faits ; le délai n'est pas une conséquence du plan.

### (b) Conditions de non-jugeabilité

- **Exp 0** : |log OR| ≤ 0,20 avec n = 200 et taux d'erreur ≈ 0,15 / 0,13 : cellule double-erreur ≈ 4, SE(log OR) ≳ 0,5 : l'intervalle ne rentre **jamais** dans ±0,20 → H_A toujours réfutée ou indécise, quelle que soit la vérité. Fisher exact donne p > 0,05 par manque de puissance, que C lirait à tort comme indépendance.
- **Exp 1** : TPR à 1 % de fausses alertes avec n_H honnêtes : le seuil est le ⌈0,01·n_H⌉-ième score honnête ; pour n_H ≈ 500, c'est le 5ᵉ plus haut score, dont la variance domine celle de TPR ; ΔTPR = 0,10 n'est pas séparable de 0 sous n_H ≈ 2 000 (illustratif). C n'exige que 500 épisodes en tout.
- **Exp 2** : AUC_mélange = w·AUC(sab/dormant) + (1−w)·AUC(sab/placebo) ; si AUC(sab/placebo) → 1 par identité, le seuil 0,75 est franchi dès w ≤ 0,5.
- **Exp 3** : ρ_causal a pour dénominateur Dommage(S100) − Dommage(S0) ; si ce dénominateur est petit (sabotage diffus), ρ est un rapport de deux quantités bruitées, à variance non bornée.
- **Exp 5** : copules empiriques de queue sur le dénominateur honnête à τ = 1 % : avec n_H = 300, trois points de queue : dépendance de queue **non estimable**. C_rés sur les manqués d'une externe à TPR ≥ 0,5 et 300 épisodes mixtes : m ≲ 75.

### (c) Contrôles négatifs fatals s'ils manquent

- Exp 0 : sabotages **produits par un organisme** flagrant, étiquetés par les événements exécutés (contrôle positif en distribution).
- Exp 2 : AUC sabotage/dormant **intra-organisme** rapportée seule ; placebo construit « même chaîne, sans objectif », distinct de T100.
- Exp 3 : direction de contrôle **dans** le sous-espace de l'adaptateur ; direction « identité » (sonde saboteur/placebo) ; réplication à la dose diffuse.
- Exp 4 : mélange uniforme public ; rejeu mêmes épisodes et graines (D).
- Exp 5 : génération placebo de pression ; échecs honnêtes avec code défaillant (fausses alertes de l'externe) ; honnêtes hors domaine pour le détecteur de nouveauté.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **E0, mesure d'indépendance** : l'écart P(err_O ∧ err_M | v) − P(err_O | v)·P(err_M | v) est borné par min(p_O, p_M) − p_O·p_M. Quand les erreurs sont rares, la marge η = 0,02 est satisfaite **par construction** (E le dit ; je le retiens contre D) : D doit déclarer E0 « indécis » si min(p_O, p_M) < η dans la strate, non « H_B falsifiée ».
2. **E2, « interaction acte × organisme »** : le placebo n'a pas d'acte ; l'interaction n'est estimable que si le placebo porte une étiquette d'acte bénin apparié. D ne la définit pas. Le critère « signal présent à dose nulle » est vide : à α = 0, l'écart adapté−base est identiquement nul (P-009).
3. **Seuils « appris sur validation, puis figés »** et couches « sélectionnées par balayage » sur les mêmes familles vues : fuite sélection → calibration, sauf emboîtement explicite (sélection dans les plis internes, calibration sur pli externe, lecture sur bloc neuf). D ne l'écrit qu'à demi (« confirmation sur un bloc neuf » pour la coordonnée, pas pour le seuil).
4. **E5, « figé secret »** : une sonde figée jamais ciblée gagne par **non-ciblage**, pas par secret ; D exige l'égalité d'architecture et d'entraînement, mais pas le **tirage au hasard** de la sonde secrète dans le même panel que la publique : sans cela, le facteur « secret » est confondu avec le choix de l'expérimentateur.
5. **E6, « pente de la trace interne selon la réussite d'évasion externe »** : estimée entre épisodes, c'est une sélection de survivants (E le formule ; je le retiens contre D) ; estimée entre générations, elle est confondue avec le changement de texte sans base relit.
6. **Coût** : 1 500–4 000 heures-carte et 4–6 semaines (illustratifs) : seul plan dont l'échelle tient compte des générations adaptatives ; D le reconnaît ; aucune échéance n'est engagée. Je ne l'harmonise pas avec C ; je note que les deux ne peuvent pas être vrais à la fois.

### (b) Conditions de non-jugeabilité

- **E0** : l'estimateur de covariance a SE ≈ √(p_O·p_M / n) ; pour p_O·p_M = 0,01, SE = 0,01 à n = 100 ; mais sous la borne min(p_O, p_M) < η, les deux hypothèses sont inséparables quel que soit n.
- **E1** : validation « laissant une famille entière de côté » avec deux familles vues : deux plis ; les intervalles « groupés par monde » sous-couvrent si le nombre de mondes G est petit (G < 10, illustratif : le bootstrap par grappe sous-estime la variance).
- **E4** : rappel « en fonction du budget d'attaque » exige plusieurs budgets par famille ; avec une famille tenue à l'écart lue une fois, la courbe a un point par budget et aucun intervalle inter-familles.
- **E5** : « valeur pessimiste sur génération fraîche » = un tirage ; aucune variance entre générations fraîches n'est estimable ; le « gain > ε » est un test à un degré de liberté sur la dimension qui compte.
- **E6** : capture résiduelle : mêmes bornes sur m que pour B et C.

### (c) Contrôles négatifs fatals

- E2 : placebo avec **étiquette d'acte bénin** pour l'interaction.
- E1 : comparateur « base qui relit » à capacité appariée (D ne cite que « meilleur modèle texte figé »).
- E5 : **panel dupliqué** (même architecture, graines différentes) pour mesurer la diversité effective nulle de H5 ; D a le mélange uniforme mais non le panel dupliqué.
- E6 : génération placebo de pression ; base relit sur chaque génération.
- E3 : direction de contrôle dans le sous-espace de l'adaptateur (comme pour C).

---

## Sur la proposition E

### (a) Défauts de méthode

1. **Fiche O, statistique d** : d = max_z |P(E_M | E_O = 1, z) − P(E_M | E_O = 0, z)|. Un maximum sur strates d'une différence estimée sur des erreurs rares est **biaisé vers le haut** (effet du gagnant) : avec n_z strates, le biais ≈ SE·√(2 ln n_z). Sous indépendance vraie, H_A (d ≤ 0,05) est réfutée par construction dès que les strates sont nombreuses et les erreurs rares. Il faut un test joint (stratifié, Mantel-Haenszel ou équivalent) ou une correction pour le maximum. E dit « rareté → indécis », mais son estimateur ne devient pas indécis, il devient **faussement positif**.
2. **Fiche T** : les comparateurs sont « texte public seul, texte + contrôles, + activations » et des « comparateurs texte de capacités différentes » ; la **base qui relit** (α = 0 sur les mêmes jetons) n'y est pas. Or c'est le seul comparateur qui extrait du texte exactement ce qu'un modèle de cette taille en extrait ; sans lui, Δ_T peut mesurer un écart de capacité entre classifieur de texte et sonde.
3. **Fiche P, duel étau** : « hausse du score interne à dommage maintenu » conditionne sur le maintien du dommage, c'est-à-dire sur les générations où le bras rouge a réussi : sélection de survivants au niveau des **générations**, après avoir correctement refusé celle au niveau des épisodes. Il faut rapporter le déplacement sur toutes les générations, avec le dommage comme covariable, non comme condition.
4. **Fiche P** : même défaut que B-X5 et D-E6 : déplacement interne possiblement texte-médié ; aucune base relit sur les générations sous pression.
5. **Fiche R, plan factoriel** 2 (distribution révélée/cachée) × 2 (tirage/affectation) × 2 (composition) = 8 cellules, chacune exigeant ses propres générations d'attaque (l'attaquant voit le régime). Le budget « 80–200 heures-carte » (illustratif) n'est pas réconcilié avec 8 cellules × générations × panel. Ce n'est pas une erreur de méthode mais une **non-jugeabilité annoncée** par le dimensionnement.
6. **Fiche L** : détecteurs gelés sur honnêtes seuls ; sur quels organismes ? Si l'entraînement se fait sur le jumeau (α = 0) et le test sur un adaptateur quelconque, l'écart adapté−base est non nul pour tout α > 0 : détection d'identité. E met le placebo en contrôle mais **pas les dormants** du saboteur.
7. Point que je **retiens** de E (en le disant) : chercher un point-selle pur avant de conclure à l'équilibre mixte ; publier dommage et fausses alertes par cellule de la matrice, non un scalaire optimisé.

### (b) Conditions de non-jugeabilité

- **O** : r_O ≥ 0,95 et f_O ≤ 0,01 par strate indispensable : pour certifier r_O ≥ 0,95 avec un rappel vrai de 0,98, la borne basse exacte exige n ≳ 150 par strate (illustratif) ; f_O ≤ 0,01 avec zéro fausse accusation observée exige n_H ≳ 300 par strate. Sous ces effectifs, O est indécis et **suspend tout**, ce que E accepte ; le programme peut donc ne jamais démarrer par choix de seuil, non par faute de l'oracle.
- **T, L** : TPR à 1 % par épisode : avec n_H = 6 000 globaux (illustratif), SD du taux de fausses alertes réalisé ≈ 0,0013 ; par sous-strate de quelques centaines, le seuil est fixé par 2–5 scores honnêtes et Δ ≥ 0,05 n'est pas séparable de 0 (E le reconnaît ; je le note comme condition formelle).
- **C** : B_D normalisé sur une échelle gelée ; si l'écart-type inter-épisodes du dommage honnête dépasse l'effet (0,05), l'intervalle couvre le seuil à tout n raisonnable (illustratif : n > 1 000 épisodes régénérés).
- **R** : G_R mesuré par cellule factorielle avec g générations ; variance entre générations non estimable si g = 1 par cellule.
- **P** : R = P(I⁺ | Y⁺, E⁻) ; non jugeable si n·P(Y⁺, E⁻) < 50 (illustratif) ; E le dit ; condition sur la masse à rapporter **avant** lecture, sinon la décision « indécis » est elle-même post hoc.

### (c) Contrôles négatifs fatals

- T : base qui relit.
- L : **dormants** du saboteur (identité contre acte) ; sans eux, le détecteur de nouveauté est un détecteur d'adaptateur.
- C : direction de contrôle dans le sous-espace de l'adaptateur ; direction « identité ».
- R : rejeu mêmes épisodes et graines (D) — absent de E.
- P : **génération placebo de pression** contre un moniteur sans rapport (B) ; base relit sur générations.

---

## Ce qui, dans ces critiques, est réfutable

Chaque point (b) énonce une condition sur (n, p_O, p_M, η, m, G, g) : il est faux si, sur les effectifs réels de T0.6 (non servis), les intervalles indiqués se révèlent plus étroits que je le calcule ; les ordres de grandeur sont **illustratifs** et à recalculer par bootstrap sur E3 bis avant tout scellement. Les points (a) « vrai par construction » (B-X2 placebo aléatoire, C-Exp 2 union, C-Exp 3 annulation de l'adaptateur, D-E0 rareté, E-O maximum sur strates) sont des énoncés sur les estimateurs, vérifiables par simulation sur processeur sans aucune donnée d'organisme.

FIN-DE-CELLULE