# Proposition B — Tour III.3 : réponse aux critiques

---

## (a) Réponse critique par critique

Je traite chaque critique adressée à ma proposition, regroupée par auteur. Les numéros renvoient à la numérotation de chaque critique.

---

### Critiques de A sur B

**A-(a)1. Expérience 2 (Platt) : H_A vraie par construction.**

**Acceptée.** A a raison : un prédicteur constant au taux de base atteint ECE ≈ 0 par définition, et ma règle de décision (ECE < 0,10 sur ≥ 80 % des familles) ne l'exclut pas. Le contrôle négatif était listé mais pas intégré à la règle de falsification. **Correction :** la règle de décision de l'Expérience 2 devient un critère **conjoint** : ECE < 0,10 **et** AUROC > 0,60 (au-dessus du plancher rapporté pour la confiance verbalisée non entraînée, pièce 5, l. 807, statut RAPPORTÉ) sur ≥ 80 % des familles. Le prédicteur constant entre dans la règle : si AUROC(Platt) ≤ AUROC(constante) + δ_AUC (δ_AUC fixé au préenregistrement, illustratif : 0,03), H_A est réfutée même si ECE < 0,10.

**A-(a)2. Expérience 1 (p₀) : règle incohérente.**

**Acceptée.** Les deux règles (seuil H_B à p₀ < 0,30 et falsification de H_A par borne sup Wilson < 0,40) se chevauchent dans [0,30 ; 0,40]. **Correction :** la règle unique est désormais : H_B tenue si la **borne supérieure** de Wilson à 95 % < 0,40 ; H_A tenue si la **borne inférieure** de Wilson ≥ 0,40. Zone grise déclarée sinon. Le seuil 0,30 est supprimé.

**A-(a)3. Sonde d'omission : fuite entre construction et évaluation.**

**Acceptée en partie.** A a raison que « cas honnêtes appariés = traces du bras individuel » réintroduit la confusion de régime que la convergence n° 3 était censée éliminer. **Correction :** les négatifs proviennent du **même bras, mêmes poids, même point de contrôle** sur des scénarios où aucune omission n'est attendue (canaris). Le plancher du classifieur aléatoire est le **taux de fausses alertes fixé** (par ex. 5 %), pas la prévalence. Le critère de la sonde est : rappel(sonde) > FPR fixé, testé par binomiale unilatérale sur n₊ positifs. Même correction appliquée au test de transfert (divergence 9).

**A-(a)4. Canari de pression : effet installé par construction.**

**Acceptée.** Le canari tel que je l'ai décrit (le signalement diminue le score du groupe) fait entrer le signalement dans la récompense, ce qui contredit la convergence n° 6 que j'adopte. **Correction :** le canari de pression est reclassé en **contrôle positif sur une branche sacrificielle**, avec poids et données étanches au bras principal. Il ne sert pas de critère d'informativité du pilote. Pour le critère d'informativité du bras principal, j'adopte le gain de tâche minimal (≥ +15 points, illustratif, reprenant C-T3 C7) mesuré sur l'oracle planté.

**A-(a)5. Divergence 2 : calcul tautologique.**

**Acceptée.** Le calcul Bernoulli i.i.d. ne modélise pas la variance de sélection sous filtrage par rejet. La dépendance entre agents du même groupe est l'objet de la divergence, pas la variance marginale. **Correction :** je retire ce calcul comme pièce tranchante. La divergence 2 reste ouverte ; je la résous autrement : voir (b), divergence 2 révisée.

**A-(a)6. Qui lit : seuils en conflit et désaccord non estimable.**

**Acceptée.** Le calcul de A montre que pour p₀ = 0,40, le plancher (p₀ − 2σ ≈ 0,33) et la chute maximale (0,08 ⟹ seuil 0,32) sont quasi redondants. Et la règle d'escalade sur 40 items (20 % de 200) n'a pas de puissance pour détecter un désaccord de 5 %. **Correction :** (i) le plancher est fixé en valeur absolue, indépendamment de σ (par ex. 0,25, illustratif), et la chute maximale est fixée en valeur relative à p₀ (0,20·p₀, illustratif) — les deux contraintes ne sont plus mécaniquement liées ; (ii) la double lecture porte sur **l'ensemble** des scénarios (pas 20 %), sur un sous-ensemble de points de contrôle (par ex. le premier et le dernier) ; le désaccord est mesuré par le κ de Cohen, avec escalade si κ < 0,60 (illustratif).

---

### Critiques de C sur B

**C-(a)1. Expérience 2 (Platt) : vrai par construction.**

**Acceptée** (même point que A-(a)1, formulé différemment avec le calcul explicite σ(as+b)). La correction est celle donnée supra : critère conjoint ECE + AUROC.

**C-(a)2. Canari de pression : fuite de sélection et violation de la convergence n° 6.**

**Acceptée** (même substance que A-(a)4). Reclassement en branche sacrificielle. Je concède à C que planter des scénarios de signalement pénalisés pendant l'entraînement du bras principal est une violation frontale de la convergence n° 6, quelle que soit l'étiquette qu'on leur donne.

**C-(a)3. Points de contrôle répétés et corrélation longitudinale.**

**Acceptée en partie.** C a raison que réutiliser les mêmes scénarios crée une corrélation longitudinale qui rend la règle d'arrêt séquentielle trop libérale. Cependant, le risque de mémorisation (modèle voyant les mêmes scénarios) n'existe pas si le modèle n'est jamais entraîné dessus — C le reconnaît implicitement. **Correction :** la règle d'arrêt séquentielle est remplacée par une **frontière d'arrêt de type O'Brien–Fleming** (dépenses α pré-allouées par point de contrôle : α₁ ≈ 0,001, α₂ ≈ 0,013, α₃ ≈ 0,045, illustratifs pour K = 3 et α global = 0,05 ; référence à vérifier : Lan & DeMets, 1983, « Discrete sequential boundaries for clinical trials »). La corrélation entre points est prise en compte dans le calcul de la frontière, qui exige une chute plus forte pour arrêter tôt.

**C-(b)1. Inflation du risque de première espèce par tests séquentiels non corrigés.**

**Acceptée.** Le calcul de C (α_eff ≈ 0,125 par point, P(arrêt erroné sur K=3) ≈ 0,30) est correct sous mon ancien dessin. La correction O'Brien–Fleming ci-dessus y répond.

**C-(b)2. Biais ECE par binnage.**

**Acceptée.** Le biais d'ordre O(√(M/n_f)) avec petites familles est réel. **Correction :** j'adopte l'ECE débiaisée (soustraction de la variance binomiale intra-bin, déjà mentionnée dans ma T1 mais pas intégrée à la règle). Pour les familles à n_f < 50, le résultat est rapporté séparément et exclu de la règle des 80 %, avec une note d'effectif insuffisant.

**C-(b)3. Sous-puissance de McNemar (Expérience 3, Lean).**

**Acceptée.** Si N_d ≤ 5, le test exact donne p-value ≥ 0,0625 > 0,05 pour 5/5, donc puissance = 0. **Correction :** (i) la taille de la banque est augmentée à ≥ 100 preuves courtes (illustratif) ; (ii) le préenregistrement inclut un calcul de puissance basé sur le nombre attendu de paires discordantes après un pilote de 20 preuves ; (iii) si le nombre de discordances attendu est < 10, le test est déclaré non jugeable et la banque est agrandie ou le dessin abandonné.

**C-(c)1. Seuil plancher conjoint de discrimination dans Exp. 2.**

**Acceptée** (= A-(a)1). Critère conjoint adopté.

**C-(c)2. Classifieur aveugle au contenu pour le transfert de sonde.**

**Acceptée.** Un classifieur « norme des poids × longueur × identifiant du modèle » est un contrôle nécessaire. **Correction :** ajouté comme plancher à battre dans le test de transfert. Si rappel(sonde) ≤ rappel(classifieur aveugle) + δ, le transfert est réfuté comme artefact de style.

---

### Critiques de D sur B

**D-(a). Canari de pression.**

**Acceptée** (= A-(a)4 et C-(a)2). Reclassé en branche sacrificielle.

**D-(a). Calcul de dilution Bernoulli i.i.d.**

**Acceptée** (= A-(a)5). Retiré.

**D-(a). Conclusion causale excessive de l'ECE sur RLCR.**

**Acceptée en partie.** D a raison qu'un ECE élevé peut venir d'extraction, de dépendance ou de décalage de domaine, pas seulement d'une mauvaise calibration intrinsèque — et qu'un faible ECE ne prouve pas que RLCR est sans objet. **Correction :** la conclusion de l'Expérience 2 est reformulée : « si ECE < 0,10 et AUROC > 0,60 après Platt sur ≥ 80 % des familles, la recalibration post-hoc est **suffisante pour les usages de calibration actuels** ; cela ne démontre pas que RLCR est sans objet pour d'autres usages (discrimination, robustesse, calibration hors domaine) ».

**D-(a). Banque de décision non distincte.**

**Acceptée.** Les scénarios de p₀, les preuves de Lean et les traces du transfert doivent être construits indépendamment de tout réglage. **Correction :** au préenregistrement, chaque banque est scellée par un tiers avant que l'instrument soit exposé à ses éléments.

**D-(b). Wilson sous corrélation intra-famille.**

**Acceptée.** L'effectif efficace est n/(1 + (m−1)ρ_f) ; Wilson à n nominal sous-couvre. **Correction :** l'intervalle est calculé sur des clusters (familles de scénarios), pas sur des scénarios individuels. La règle d'arrêt O'Brien–Fleming est appliquée à l'estimateur clusterisé.

**D-(b). Points de contrôle répétés sans correction séquentielle.**

**Acceptée** (= C-(a)3). Correction O'Brien–Fleming adoptée.

**D-(b). McNemar et paires discordantes.**

**Acceptée** (= C-(b)3). Banque agrandie et pilote de dimensionnement.

**D-(b). Transfert : peu de positifs.**

**Acceptée** (= A-(a)3 en partie). Avec prévalence faible et n = 100, n₊ peut être < 10. **Correction :** n total est dimensionné pour que E[n₊] ≥ 30 (illustratif), en utilisant le taux de base estimé au pré-test p₀.

**D-(c). Canari individuel pour séparer omission et attribution collective.**

**Acceptée.** Un canari où l'omission paie aussi individuellement est nécessaire pour isoler l'effet du crédit collectif. **Ajouté** à la branche sacrificielle.

**D-(c). Banque fraîche pour p₀.**

**Acceptée.** Une banque de scénarios distincte de celle ayant servi à fixer la jugeabilité. **Ajouté** au préenregistrement.

**D-(c). Prédicteurs dans la règle de décision de Platt.**

**Acceptée** (= A-(a)1). Intégrés.

**D-(c). Preuve correcte d'une spécification altérée.**

**Acceptée.** Sans ce contrôle, une preuve Lean d'un énoncé voisin (mais pas de l'énoncé servi) passe comme détection. **Ajouté.**

**D-(c). Étiquettes permutées et classifieur style pour le transfert.**

**Acceptée.** Classifieur aveugle déjà adopté (C-(c)2). Étiquettes permutées ajoutées comme test de calibration du seuil du rappel.

---

### Critiques de E sur B

**E-(a). Canari contaminant.**

**Acceptée** (= A, C, D). Branche sacrificielle.

**E-(a). Nul incorrect pour le transfert.**

**Acceptée** (= A-(a)3). Le rappel sous indépendance = FPR fixé, pas la prévalence. Corrigé.

**E-(a). Même point de contrôle ≠ mêmes poids.**

**Acceptée.** Deux bras entraînés séparément n'ont pas les mêmes poids au même pas. **Correction :** les négatifs pour la sonde proviennent du **même modèle figé** (même checkpoint), sur des scénarios sans omission attendue. La comparaison inter-bras se fait sur des checkpoints appariés par pas, mais les négatifs intra-bras sont à poids identiques.

**E-(a). Critère de calibration mouvant.**

**Acceptée en partie.** Le choix entre moyenne pondérée, quantile, pire famille ou proportion est un degré de liberté. **Correction :** fixé au préenregistrement : proportion de familles (≥ 80 %) satisfaisant le critère conjoint, familles à n_f < 50 exclues avec mention.

**E-(a). ECE et discrimination confondues.**

**Acceptée** (= D-(a)). Conclusion reformulée.

**E-(a). Marge de sécurité dépendant du bruit.**

**Acceptée.** Le plancher p₀ − 2σ est un artefact statistique, pas une tolérance opérationnelle. **Correction :** plancher fixé en valeur absolue (0,25 illustratif), indépendant de σ. Déjà corrigé supra (A-(a)6).

**E-(a). Test Lean incohérent avec l'hypothèse.**

**Acceptée.** Il faut annoncer une supériorité d'ampleur utile δ > 0 gelée. **Correction :** H_A reformulée : « rappel(Lean) − rappel(suite) ≥ δ_utile » (δ_utile gelé au préenregistrement). TOST bilatéral pour l'équivalence si le gain est < δ_utile.

**E-(b). Constante calibrée à AUROC ex æquo.**

Déjà couverte par le critère conjoint ECE + AUROC.

**E-(b). Familles indépendantes vs. partitions.**

**Acceptée.** Des partitions des mêmes données ne réduisent pas τ²/F. **Correction :** les « graines de partition » (k ≥ 2) servent à stabiliser l'estimateur ECE sur une même famille, pas à remplacer des familles indépendantes. La variance inter-familles est estimée séparément.

**E-(b). Incertitude de p₀ traitée comme constante.**

**Acceptée.** Var(p̂₀ − p̂_t) = σ₀² + σ_t² − 2Cov. **Correction :** la frontière O'Brien–Fleming est calculée en traitant p̂₀ comme un estimateur bruité, avec sa variance propagée.

**E-(c). Branche sans canari étanche.**

**Acceptée.** Branche sacrificielle isolée.

**E-(c). Scores permutés et seuil sur lot distinct pour le transfert.**

**Acceptée.** Intégrés.

**E-(c). Calibration : constante, verdict binaire, partition externe.**

**Acceptée.** Déjà intégrés via le critère conjoint et la partition leave-one-family-out.

**E-(c). Trajectoires A/A complètes.**

**Acceptée.** Le taux d'arrêt à tort sous A/A doit être mesuré avant le run réel, avec toutes les lectures prévues. **Ajouté** au préenregistrement : 100 trajectoires A/A simulées (illustratif), taux d'arrêt à tort < 0,05, ou la règle est recalibrée.

---

## (b) Expériences corrigées

### Expérience 1 corrigée : Pré-test de signalement (p₀)

- **H_A :** Borne inférieure de Wilson ≥ 0,40.
- **H_B :** Borne supérieure de Wilson < 0,40.
- **Métrique :** Taux de signalement sur scénarios scellés, intervalle de Wilson à 95 % **clusterisé par famille de scénarios**.
- **Contrôles :** canaris « à ne pas signaler » ; scénarios « rapport déjà émis » et « outil indisponible » (reprenant D, en le disant) ; banque fraîche distincte de celle de réglage.
- **Falsifie H_A si :** borne sup Wilson clusterisé < 0,40. **Falsifie H_B si :** borne inf Wilson clusterisé ≥ 0,40.
- **Coût :** inférence sur ≥ 200 scénarios, < 50 $ illustratif.

### Expérience 2 corrigée : Audit de calibration (Platt)

- **H_A :** ECE_débiaisée < 0,10 **et** AUROC > 0,60 sur ≥ 80 % des familles (n_f ≥ 50).
- **H_B :** Complémentaire.
- **Contrôles dans la règle de décision :** prédicteur constant au taux de base ; confiance permutée intra-famille ; verdict binaire ; probabilité brute du jeton.
- **Conclusion bornée :** « suffisante pour les usages de calibration actuels » ; pas « RLCR sans objet ».
- **Partition :** leave-one-family-out ; calibration ajustée sur les plis d'entraînement seulement.
- **Coût :** processeur, < 1 $ illustratif.

### Expérience 3 corrigée : Lean contre suite bon marché

- **H_A :** rappel(Lean) − rappel(suite) ≥ δ_utile (gelé au préenregistrement).
- **H_B :** rappel(Lean) − rappel(suite) < δ_utile.
- **Banque :** ≥ 100 preuves courtes (illustratif), scellées par un tiers. Classes : coquilles, erreurs logiques, erreurs de spécification. Proportion de classes gelée.
- **Pilote :** 20 preuves pour estimer le nombre de paires discordantes. Si E[N_d] < 10, non jugeable.
- **Contrôles :** preuves saines (fausses alertes) ; preuves correctes d'énoncés voisins (fidélité de spécification) ; banque fraîche post-sélection des classes.
- **Coût :** processeur, 50–500 € illustratif.

### Dispositif « qui lit » corrigé

1. **Lecteur :** session neuve, modèle d'une famille différente, nommé et scellé au préenregistrement.
2. **Points de contrôle :** p₀, puis points fixes (0, 50, 100, 150 pas, illustratifs).
3. **Frontière d'arrêt :** O'Brien–Fleming (dépenses α pré-allouées), calculée sur l'estimateur clusterisé, en traitant p̂₀ comme bruité. **Plancher absolu :** 0,25 (illustratif), indépendant de σ. **Chute maximale :** 0,20·p₀ (illustratif).
4. **Validation A/A :** 100 trajectoires simulées (illustratif) avant le run réel ; taux d'arrêt à tort < 0,05, sinon la frontière est recalibrée.
5. **Double lecture :** sur l'ensemble des scénarios, au premier et au dernier point de contrôle, par deux sessions de familles différentes ; κ de Cohen ; escalade si κ < 0,60 (illustratif).
6. **Aveuglement :** le lecteur ne voit ni le bras ni le gain d'utilité au moment de statuer sur un incident (reprenant C-(c)2 sur D, en le disant).
7. **Pire cas :** biais systématique du lecteur. **Garde :** double lecture + aveuglement + validation A/A.

---

## (c) Réponse à la question de l'arbitre

### Ce qui est établi

1. **N-045 couvre la sélection et la composition, pas la génération ni la preuve formelle** (accord n° 1 de la synthèse v2, quatre espèces ; VÉRIFIÉ sur la pièce 1, énoncés 1, 5, 6(ii)). La recommandation conv-audit « ne pas rouvrir avant l'étape 2 » tient, à condition que le résidu soit inscrit au préenregistrement (apport D, non réfuté).

2. **L'empreinte ne prouve pas la validité** (accord n° 2, quatre espèces). L'essai Lean contre suite bon marché sur processeur est le bon test ; il est réalisable sans dépense de carte. Le comparateur (tests + mutations + relecture par une autre famille) est le même chez les quatre après les cessions du tour 1.

3. **(c1) est la seule forme à contrefactuel ; (c3) est un sous-produit ; (c2) est écartée** (accord n° 3, quatre espèces). La recommandation conv-audit « bras collectif à l'étape 2, signalement mesuré dans les deux » est alignée.

4. **Post-hoc d'abord, RLCR seulement pour un juge local** (accord n° 4, convergence née de la critique). L'audit de calibration Platt est la première pièce sans dépense.

5. **Les treize convergences nées de la critique** (synthèse v2) sont des contraintes de dessin pour tout bras futur : graine comme unité, positifs et négatifs des mêmes poids, scénarios tenus à l'écart, pré-test p₀, attribution à information égale, seuils rattachés au bruit, comparateur du catalogue, et les corrections issues de ce tour (critère conjoint ECE + AUROC, frontière O'Brien–Fleming, banque scellée par un tiers).

### Ce qui n'est pas établi

1. **La cause collective de la chute du signalement** (HYPOTHÈSE : pièce 4, § 1.8 réserve 1). Quatre espèces la tiennent pour non établie. Ma position depuis T1 : c'est un prérequis causal, pas un fait.

2. **La pression d'optimisation hors ligne** (divergence n° 3). Aucun calcul ni aucune pièce ne tranche si un pilote de taille modeste reproduit la pression d'Avalon sur la dimension du signalement. Le canari de pression (branche sacrificielle) et le gain de tâche minimal sont des conditions nécessaires, pas suffisantes.

3. **La nature exacte de la précaution** (divergence n° 4). J'ai adopté la structure plancher + chute + arrêt de D, mais les valeurs dépendent du pré-test p₀ qui n'est pas encore réalisé. Le dispositif « qui lit » que je propose est une HYPOTHÈSE de conception, pas un fait.

4. **La transférabilité des résultats de Damani** (pièce 5) à notre organisme. Les lectures vérifiées (R-1013, R-1016) ne sont pas servies ; tout dessin est conditionnel à leur contenu.

5. **Le filtrage de fiches par un moniteur neuf est-il un signal de sélection au sens de N-053** (divergence n° 1). Nœud de lecture, à trancher par le directeur.

### L'expérience à faire en premier

**L'audit de calibration Platt (Expérience 2 corrigée)**, pour trois raisons :

1. **Sans dépense :** calcul sur logits déjà produits, processeur seul, minutes de calcul — si les logits sont journalisés. Si non, l'extraction est la première dépense minimale à planifier.

2. **Falsifie quelque chose dans les deux cas :**
   - H_A (ECE < 0,10 et AUROC > 0,60 après Platt) : falsifie l'hypothèse qu'un entraînement RLCR est nécessaire pour la calibration des juges actuels.
   - H_B (complémentaire) : falsifie l'hypothèse que la recalibration post-hoc suffit ; justifie l'investissement dans un entraînement RLCR pour un juge local.

3. **Précède logiquement tout le reste :** le résultat conditionne le dessin du bras collectif de l'étape 2 (si les juges ne sont pas calibrés, toute mesure du signalement par les juges est biaisée) et l'essai Lean (si les juges ne discriminent pas les preuves, la « suite bon marché » qui inclut une relecture croisée est handicapée).

**En parallèle** (si les scénarios de signalement sont prêts) : le pré-test p₀ (Expérience 1 corrigée), qui conditionne toutes les valeurs numériques du dispositif de précaution.

FIN-DE-CELLULE