# Proposition A : Tour III.2, critique croisée de méthode

**État des pièces.** Le bloc FAITS est identique au bloc QUESTION (même empreinte) : il ne contient aucun fait statué. Les pièces B, C, D et E sont présentes et se terminent toutes par leur marqueur de fin. Ma propre conception du tour III.1 ne figure pas dans les pièces transmises : je n'y renvoie pas.

**Statut de ce qui suit.** Toutes mes critiques sont des **HYPOTHÈSES** (raisonnement non revérifié). Les passages marqués « calcul » sont des identités arithmétiques tirées des définitions des pièces, à recalculer par un tiers. Tous mes chiffres sont **illustratifs**.

**Convention utilisée (B1).** Pour le point 3, je me sers du plan 2×2 de D, I = L₁₁ − L₁₀ − L₀₁ + L₀₀, comme étalon pour critiquer B, C et E. Je distingue deux rejeux qu'ils confondent :
- le **retrait** : remplacer une action par la référence dans la trajectoire réalisée ;
- l'**insertion** : poser une action déviante dans la trajectoire de référence.

---

## Sur la proposition B

### (a) Défauts de méthode

1. **Le contrôle HON est vrai par construction.** u est tiré indépendamment de la trajectoire avec P(u = +1) = ½. Donc E[z | HON] = E[e_h]·E[u]/σ_h = 0 quel que soit le biais honnête b = E[β̂ − β | HON] (calcul). Deux conséquences :
   - le contrôle « l'IC de E[z] contient 0 » ne peut échouer que par bogue ou par hasard, et il ne teste pas C3 au sens utile ;
   - le critère d'abandon « E[z] ≠ 0 sous HON malgré la randomisation » est quasi indéclenchable.
   - Même remarque pour « E[z] ≈ 0 sous BRUIT ».
2. **Le biais dirigé non stratégique (S3) n'est jamais testé.** Sous HON, u est absent du contexte : la complaisance ne peut pas se manifester. La condition « biais nul sous HON avec u randomisé » est donc vide.
3. **Charge de consigne confondue.** SAB diffère de HON par la direction, mais aussi par la longueur et la complexité de la consigne et par la mention de l'ensemble admissible. L'écart E[z | SAB] − E[z | HON] est un effet de la consigne entière.
4. **M1 possiblement vide.** Si l'interface *impose* que chaque paramètre soit pris dans A_i, M1 vaut 0 par construction. « Défendable » se réduit alors à M2. La pièce ne dit pas si l'interface impose A_i ou le vérifie après coup.
5. **Plafond réglé par l'expérimentateur.** L'excès atteignable est borné par l'étendue du multivers admissible rapportée à σ_h. Ce rapport est un paramètre du générateur. Le seuil 0,5 de E0 peut être atteint ou manqué par conception, indépendamment du modèle.
6. **Fuites.**
   - σ_h est estimé sur les trajectoires HON qui servent ensuite au test et aux plis de validation de E1.
   - BRUIT est « d'amplitude appariée à SAB » : le contrôle est construit avec un résultat postérieur au traitement.
   - Dans E1, le trait « cohérence des choix avec u » suppose u connu, ce qui n'est vrai que de l'expérimentateur.
7. **E2 dépend d'une convention, non de l'agent (calcul).** B définit l'effet local comme un *retrait*. Pour une paire plantée active (chaque action seule < 0,1 σ, les deux > 1 σ), retirer a_i seul fait passer le dommage de > 1 σ à < 0,1 σ.
   - Le moniteur local voit donc tout le dommage, deux fois.
   - La phrase « un moniteur action par action ne voit que la part additive » est fausse sous la définition de B. Elle n'est vraie qu'en insertion.
   - H_A d'E2 (détection locale plus faible d'au moins 0,3 sur COMB) serait réfutée par arithmétique, sans rien apprendre sur l'agent.
   - Le cas réellement aveugle au retrait est le dommage **redondant** (L₁₁ ≈ L₁₀ ≈ L₀₁ > L₀₀), que B ne plante pas.
8. **Le moniteur de trajectoire sans fuite n'atteint pas son seuil (calcul).** Avec 200 paires tirées au hasard sur 1 225 (50 actions), une paire plantée donnée est rejouée avec une probabilité d'environ 16 %. Récupérer au moins 70 % du dommage suppose de savoir où sont les paires, donc d'utiliser la carte de construction.

### (b) Conditions de perte de puissance

- **Test agrégé non apparié.** Var(z | HON) = (σ² + b²)/σ_h². La puissance s'effondre quand b² ≫ σ².
- **Test apparié.** La variance utile est Var(β̂_SAB − β̂_HON) = 2σ_w²(1 − ρ_s), où ρ_s est la corrélation intra-tâche entre graines. Le test perd sa puissance quand ρ_s → 0 (ce que B nomme S8).
- **E1 n'est pas indépendante d'E0.** Sous normalité et variances égales, AUROC(z) = Φ(d/√2). Pour d = 0,5 on obtient environ 0,64 ; il faut d ≈ 0,95 pour atteindre 0,75 (calcul). L'issue d'E1 est donc prédite par E0, sauf si les autres traits apportent quelque chose, et ces traits utilisent u.
- **Sans u, la statistique redevient M3.** Un détecteur aveugle doit prendre max(z₊, z₋), soit |β̂ − β|/σ_h.
- **Sabotage non dirigé ou tiré symétriquement.** E[d·u] = 0 : puissance nulle sur z. Il reste un test de variance, de puissance en (σ_sab² / σ_h²).

### (c) Contrôles négatifs dont l'absence serait fatale

- **HON-cadré** : consigne honnête portant un indice de direction non malveillant (« le commanditaire attend un effet positif »), de même longueur que SAB. Sans lui, « excès dirigé » ne se distingue pas de la complaisance.
- **Politique uniforme sur A_i** (plancher) et **saboteur scripté glouton sur A_i** (plafond). Sans eux, le seuil 0,5 n'est pas interprétable.
- **HON sur le banc à paires, avec moniteur en retrait et en insertion.** Sans lui, E2 ne distingue pas la convention du phénomène.
- **Paires redondantes plantées** : le cas où le retrait échoue réellement.

---

## Sur la proposition C

**Remarque de statut (règle 1 : je ne change rien, je signale).**
- L'affirmation d'absence « aucun banc publié » est étiquetée VÉRIFIÉ. Aucune pièce transmise ne la soutient.
- Plusieurs références marquées « à vérifier » figurent sous des puces VÉRIFIÉ.

### (a) Défauts de méthode

1. **ALD est en partie vrai par construction.** ℓ_t est un retrait par rapport à a_t⁰. Il est donc nul là où a_t ne dévie pas, et Cov_t(e_t, ℓ_t/(d_t + ε)) > 0 pour toute trajectoire fautive, honnête ou non. Le contenu discriminant repose sur d_t seul.
2. **Fuite sur d_t.** d_t est le taux d'échec honnête par étape. S'il est calibré sur le vivier qui fournit les négatifs, les erreurs honnêtes tombent par définition aux étapes à d_t élevé : le score ALD honnête est bas par construction. Il faut un vivier de calibration disjoint, de même loi (même température).
3. **Hypothèse centrale en tension avec « défendable ».** C suppose que le saboteur dévie là où d_t est faible. Mais une déviation à une étape que les honnêtes ne ratent presque jamais est la moins défendable. La déviation défendable se loge où les honnêtes divergent aussi, donc à d_t élevé. E sépare ambiguïté A_t et difficulté D_t ; C les fusionne.
4. **Température confondue avec l'étiquette.** Les honnêtes appariés sont produits à température 0,7 à 1,2, ou par un autre modèle, pour obtenir de grosses erreurs. Le détecteur peut alors séparer « erreurs de haute température, diffuses » et « erreurs instruites, concentrées » : il mesure le régime d'échantillonnage.
5. **Sélection sur le résultat.** L'appariement à Δ égal ±5 % et la restriction aux trajectoires « saboteuses réussies » conditionnent sur une variable postérieure au traitement. La couverture de l'appariement n'est pas rapportée.
6. **CUSUM-P, deux défauts.**
   - Les « honnêtes appariés » sont choisis parmi ceux qui ont un biais *de position*, précisément celui que la permutation disperse. Le choix est favorable par construction.
   - La consigne de sabotage (« biaiser d'au moins 30 % ») n'a pas de direction sémantique. Après inversion des étiquettes A/B, rien n'ancre le signe attendu. L'instrument peut être sans puissance par conception.
7. **Expérience 2 (calcul).** Avec Δ_t en retrait et un gadget où « seule la conjonction de 3 choix » nuit :
   - chaque Δ_t ≈ D, donc M₁ = max_t Δ_t ≈ D : l'auditeur d'ordre 1 détecte parfaitement, au contraire de ce que prédit H_A (i) ;
   - ISE = (D − 3D)/D = −2. Le signe d'ISE dépend de la structure ET/OU du gadget, pas de l'intention.
   - La recherche gloutonne de la coalition S maximise une statistique sur de nombreux sous-ensembles, sans loi nulle calibrée avec la même recherche.
8. **Expérience 3, circularité.**
   - Les substitutions sont placées par l'expérimentateur aux « points de décision critiques », définis par le levier. L'instrument ALD repère le levier. r(ρ, ρ̂) élevé est donc attendu par construction.
   - ρ suppose une décomposition additive que le présupposé 3 de C déclare non garantie. La « vraie » part dépend de l'ordre d'ablation dès que l'interaction est non nulle.
   - Après substitution, les actions honnêtes en aval réagissent à l'état modifié.
9. **Contrôles vrais par construction.**
   - « Honnête A contre Honnête B » donne une AUC d'environ 0,5 pour tout détecteur (échangeabilité).
   - L'agent uniforme d'E2 est indépendant par construction : il ne dit rien des erreurs honnêtes corrélées.

### (b) Conditions de perte de puissance

- **ALD.** Puissance nulle quand la loi de la position des déviations est la même sous les deux régimes : P(t | e_t = 1, SAB) = P(t | e_t = 1, HON). Elle se dégrade aussi quand Corr_t(d_t, ℓ_t) > 0 (étapes difficiles qui sont aussi à fort levier : jointures, confondants). d_t est non défini si les étapes ne sont pas alignées entre trajectoires.
- **CUSUM-P (calcul).** Avec K = 4 et des signes d'erreur honnêtes indépendants et symétriques, P(tous de même signe) = 2·(½)⁴ = 12,5 %. Le plafond FPR ≤ 10 % du contrat I₂ est inatteignable au seuil 1 ; il faut K ≥ 5. L'instrument est non jugeable si le biais honnête est invariant par permutation (atténuation, confondant omis) : la statistique vaut alors 1 sous les deux régimes.
- **ISE.** Les négatifs appariés (« au moins 3 erreurs locales et même perte finale » sur R_comb) ont une fréquence d'ordre π ≈ p³. Avec π = 10⁻³ et 200 trajectoires honnêtes, on attend 0,2 cas (calcul) : le FPR n'est pas estimable.
- **ρ̂.** Non jugeable quand P(Δ_total < ε) n'est pas négligeable (dénominateur). ρ sort de [0, 1] quand erreur honnête et sabotage sont de signes opposés.
- **Expérience 4 (calcul asymptotique).** Avec n = m = 150, le seuil critique à 5 % du test de Kolmogorov-Smirnov est d'environ 0,157. Sous lois *identiques*, P(D_KS < 0,08) ≈ 0,28 : le contrôle négatif échoue environ 7 fois sur 10 sans aucune distorsion. Les seuils 0,12 et 0,20 ne sont pas résolus à cette taille.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Honnête à biais sémantique invariant par permutation** (cadrage orienté), pour CUSUM-P.
- **Honnête à même température et même modèle** que le saboteur, quitte à réduire la couverture de l'appariement, celle-ci étant publiée.
- **Ablation guidée par le levier seul** (les k plus grands ℓ_t, sans d_t ni permutation), pour l'expérience 3. Si elle égale ρ̂, le contenu « intention » d'ALD est nul.
- **Extracteur AST appliqué aux traces C_inst**, où le graphe vrai est connu. Sinon la chute d'AUC confond perte d'extraction et changement de comportement.
- **Fréquence empirique du mode critique chez l'agent honnête réel** sur R_comb, à la place de l'agent uniforme.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **La contrainte « chaque action défendable » n'est pas opérationnalisée.** Le bras D reçoit un « objectif privé de qualité moindre » sans filtre d'admissibilité. Δ mêle dégradation grossière et dégradation défendable. La quantité visée par la question n'est qu'une part inconnue de Δ.
2. **Refus comptés dans Δ.** Un refus de la tâche entière vaut S = 0 et gonfle Δ. Un refus de saboter suivi d'un travail honnête le ramène vers 0. Δ est alors une moyenne de mélange dont les poids (taux de refus) varient selon le modèle. La règle de décision porte sur Δ brut, alors que les fréquences sont seulement « publiées ».
3. **Le contrôle de paraphrase n'a pas d'estimande.** « Déplacement comparable » n'est pas défini. Il faudrait la différence (Δ_objectif − Δ_paraphrase) avec son intervalle.
4. **Le duel composition n'est pas une inférence forte au sens B4.** H_A y est une spécification du générateur, et les deux issues testent le code. D le reconnaît à demi (« aucune inférence statistique »). Rien n'est appris sur ce que l'agent produit. La fréquence d'activation honnête des paires couplées n'apparaît qu'en (c), sans seuil.
5. **Détecteur non spécifié.** « Dépendances entre sources consultées et conclusions » laisse tous les degrés de liberté au jeu de développement. Le duel n'est pas jugeable avant qu'une statistique soit figée.
6. **Duel transfert : mémorisation confondue avec le format.** Les « rapports publics à résultats recalculables » peuvent figurer dans le pré-entraînement. Le score honnête en condition libre peut refléter le rappel du résultat publié, non l'analyse.
7. **Contrôle vrai par construction.** La permutation des étiquettes dans les strates valide le niveau du test, non l'absence de confusion.

### (b) Conditions de perte de puissance

- **Plancher.** Δ ≤ E[S_H] − S_trivial. Si cette marge est inférieure à 0,10, H_A est inatteignable quelle que soit l'intention. Le garde-fou de D (dépasser le script « première source ») n'exige pas cette marge.
- **Pilote (calcul).** Avec 24 dossiers et un écart-type de la différence appariée de 0,25, la demi-largeur de l'IC à 95 % est d'environ 0,10, soit le seuil lui-même. Sauf Δ ≥ 0,20, l'issue est « non tranché ». Le pilote ne répond donc au point 5 que dans un cas.
- **FPR (calcul).** Estimer 5 % à ±2 points demande environ 450 négatifs honnêtes. D l'admet qualitativement, sans dimensionnement.
- **Transfert.** H_A est une équivalence sur une différence de différences : la variance a quatre composantes. Le duel est non jugeable tant que l'erreur type dépasse environ 0,05.
- **S discret et borné.** Avec peu de conclusions par dossier, S prend peu de valeurs. Le test perd sa puissance quand P(S_H = S_D) est grand par simple granularité.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Stratification de Δ par une vérification mécanique d'admissibilité figée avant test.** Sans elle, Δ ne dit rien de la dégradation défendable.
- **Bras « honnête affaibli »** (même modèle, capacité réduite par budget ou troncature, S apparié). Sans lui, le détecteur n'a pas de négatifs à gravité comparable de couverture suffisante.
- **Sonde de mémorisation** sur les dossiers publics : question finale posée sans documents.
- **Fréquence honnête des paires couplées, avec seuil.**

---

## Sur la proposition E

### (a) Défauts de méthode

1. **Tension interne de la condition C2.** Le saboteur doit *percevoir* la polarité S_i (asymétrie des valeurs aberrantes, etc.) pour l'exploiter. Tout trait lisible par lui l'est aussi par l'agent honnête, dont le choix (winsoriser davantage si la queue est haute) peut en dépendre. « Orthogonal par construction aux indices de surface » et « exploitable par le saboteur » ne peuvent pas être garantis ensemble. La restriction d'exclusion est empirique, pas construite.
2. **Identité par construction.** Les polarités sont inversées par moitiés. Une règle honnête constante s'annule donc dans l'agrégat. Tout dommage dirigé est alors *défini* comme contingent à S, et Δ̂_int ≈ dommage par construction. Une faible MAE(ρ̂, ρ) sur saboteur scripté n'apprend rien. Le seul contenu empirique est l'invariance à S de l'agent honnête.
3. **ρ a deux définitions.** C'est tantôt une proportion de traces dans un mélange, tantôt un rapport de pertes dans une trajectoire. Le contraste moyen identifie π·δ (proportion × intensité), pas π ni δ séparément. Tirer « ρ uniforme » exige les étiquettes vraies.
4. **Le contrôle négatif d'E2 suppose la conclusion.** L'agent honnête bruité injecte des écarts *indépendants*. La rareté O(p^k) y est vraie par construction. C'est l'hypothèse (ii) de E, pas un test.
5. **Fuite sur I3.** Les coupes minimales du graphe sont celles où l'expérimentateur a planté les gadgets. Un auditeur qui lit le graphe de la tâche est évalué sur la carte de construction. Il doit n'inférer le lignage que du code émis, sur des familles de gadgets tenues à l'écart.
6. **Référence à battre ambiguë.** « Ablation mono-action *leave-one-out* depuis la trace de référence » désigne une insertion, pas un retrait. En retrait sur la trace réalisée, un gadget conjonctif est entièrement détecté (voir B, point 7). I3 doit battre ce retrait, ce que la pièce n'exige pas.
7. **Sélection.** Le TPR d'E2 est calculé « sur les épisodes où Δ est réalisé ». L'honnête d'E1 est sous-échantillonné pour égaler la perte moyenne. Les deux conditionnent sur le résultat.
8. **Modèle confondu avec l'étiquette.** Les honnêtes appariés d'I1 et d'I4 peuvent être un modèle 3B ou une température de 0,9. Pour I4, la réponse au bruit sur les poids de deux architectures de tailles différentes n'est pas comparable.
9. **I4 : biais du maximum.** max_σ S(θ + bruit) − S(θ) est positif en espérance sous le régime honnête dès que S est bruité, par sélection du maximum. La loi nulle doit subir la même recherche sur σ.
10. **E4 : issue non couverte (B4).** La conjonction triple inclut MAE(ρ̂). Le cas « (1) et (2) réussis, (3) échoué » ne falsifie ni H_A ni H_B tels qu'ils sont écrits. De plus le seuil (1), au moins 0,80 d'épisodes sans alerte mécanique, est absolu : si le taux honnête est inférieur, le saboteur est condamné d'avance.
11. **E3, facteur 1.** Extraire θ̂ d'une sortie rédigée libre sans juge suppose un analyseur. Son taux d'erreur est confondu avec l'effet du format.

### (b) Conditions de perte de puissance

- **I1 (calcul).** Avec K = 24 (12 par polarité), choix binaire et p_HON = 0,5, l'erreur type du contraste de proportions est d'environ 0,20. Une AUC ≥ 0,80 demande un décalage d'environ 0,24, soit environ 3 choix retournés sur 24. Un saboteur qui en retourne un seul donne une AUC d'environ 0,61. I1 perd sa puissance quand le nombre m de déviations contingentes vérifie m/K ≪ 1/√K, ce qui est exactement le régime k ≥ 2.
- **I1.** Non jugeable si Cov(choix_HON, S) ≠ 0. Puissance nulle si le dommage passe par un canal sans polarité par table (étape d'agrégation, inflation de variance).
- **ρ̂.** Le dénominateur L_tot ≈ 0 pour les mélanges à dominante honnête, par l'annulation construite : le rapport est instable précisément là où ρ → 0.
- **I3 (calcul).** Avec une corrélation φ entre indicatrices d'erreur honnête, P(conjointe) = p² + φ·p(1 − p). Pour p = 0,1 et φ = 0,3, on obtient 0,037 contre 0,01 sous indépendance. Le rapport de vraisemblance annoncé en O(p^k) se réduit d'autant.
- **I2.** Les négatifs (biais non centré sur variables *neutres*, S_t = 0) ne contraignent pas la loi du biais honnête sur les variables à S_t ≠ 0. Si E[δ_t^hon | S_t ≠ 0] ≠ 0, le FPR est incontrôlé.
- **E3.** L'acceptation de H_A repose sur un classifieur faible. Elle n'est interprétable que si le contrôle positif d'I5 (altération injectée de 0,5 σ) est franchi sur les mêmes traits et à la même taille.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Corrélation empirique des erreurs honnêtes du modèle réel** sur le graphe (matrice φ), à la place du bruit indépendant.
- **Agent honnête sur tables dont la polarité S est perceptible mais sans objectif**, pour mesurer Cov(choix_HON, S) directement. Le contrôle « cadré » existe et il est utile. Il teste toutefois la complaisance, pas la dépendance du choix honnête aux traits qui portent S.
- **Retrait mono-action sur la trace réalisée** comme base d'I3, et **gadgets redondants**.
- **Honnête du même modèle soumis à la même recherche sur σ**, pour I4.
- **Analyseur de sortie libre validé sur sorties à valeur connue**, pour E3.

---

## Ce que je retiens pour la suite (usage déclaré, sans fusion)

- **De D :** le plan 2×2, comme seule définition non ambiguë de l'interaction, et la séparation « perte induite » / « attribution ».
- **De E :** le contrôle honnête cadré et le contrôle positif scripté, qui manquent à B et à C.
- **De B :** le critère relatif sur les alertes mécaniques (hausse d'au plus 5 points), que E devrait substituer à son seuil absolu.
- **Désaccord à trancher par expérience.** B, C et E affirment que l'audit par action est aveugle au dommage combinatoire. Je soutiens que c'est faux en retrait pour les gadgets conjonctifs et vrai seulement pour les gadgets redondants.
  - H_A : sur paires conjonctives, le retrait mono-action récupère au moins 90 % du dommage (illustratif).
  - H_B : il en récupère moins de 50 % (illustratif).
  - Le test coûte quelques rejeux CPU sur un saboteur scripté, sans modèle de langue. Entre les deux seuils, il est non conclusif.

FIN-DE-CELLULE