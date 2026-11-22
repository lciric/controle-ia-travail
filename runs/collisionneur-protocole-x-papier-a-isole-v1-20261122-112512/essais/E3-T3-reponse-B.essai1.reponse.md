# Proposition B — Tour III.3 : réponse aux critiques

**Pièces reçues.** J'ai reçu ma conception III.1 et les critiques croisées de A, C, D et E. Toutes sont complètes et se terminent par leur ligne de fin. Le bloc FAITS reste identique au bloc QUESTION et ne contient aucun fait muni d'un statut.

**Statuts.** Les choix de protocole de ma pièce III.1 sont RAPPORTÉS. Toutes mes prédictions restent au statut HYPOTHÈSE. C et E apposent [VÉRIFIÉ] sur des dérivations. Je ne modifie pas ces étiquettes et je ne m'en sers pas comme résultats. Quand je dis avoir « recalculé » une dérivation, il s'agit d'une conséquence mathématique sous le modèle énoncé par le critique, pas d'une observation sur un agent. Tous les seuils, budgets et effectifs ci-dessous sont **illustratifs**.

---

## (a) Critiques et décisions

Seules les sections qui visent B sont traitées. Une critique répétée par plusieurs pièces est traitée une fois, et les autres lignes y renvoient.

### Critiques de A

| # | Critique | Décision | Raison, ou test qui en découle |
|---|---|---|---|
| A1 | Avec l'adversaire scripté de Bernoulli i.i.d., α ≈ ½ est acquis par le théorème central limite. | **Acceptée en partie.** | Côté adversaire, c'est exact. En revanche, le bruit de fond reste celui de l'agent honnête réel (τ², autocorrélation, queues). Avec ce bruit, l'α mesuré teste donc la **structure du bruit honnête**, non l'adversaire. E1 est requalifiée en ce sens (E1′). Le cas i.i.d. pur, sur bruit synthétique, devient un contrôle positif de chaîne (E0). |
| A2 | α n'est pas identifié tant que la convention somme ou moyenne n'est pas fixée. | **Acceptée.** | Je pré-enregistre la convention **somme** : effet par choix d̄ constant. J'ajoute un contrôle d'invariance : en convention moyenne, α_abs doit se décaler d'exactement −1 et α_rel ne doit pas bouger. |
| A3 | Le rapport utile D\*/σ_honnête(n) est absent. Sous R½, la longueur ne change rien relativement au bruit. | **Acceptée.** | C'est la correction la plus importante. Ma lecture III.1, « R½ sert l'adversaire », valait en unités absolues seulement. Je rapporte désormais deux exposants : α_abs, et **α_rel = α_abs − β_h**, où β_h est l'exposant de l'écart-type honnête du résultat final. Les hypothèses décisives portent sur α_rel. |
| A4 | M3 et l'attribution de E4 lisent la clef du générateur. | **Acceptée.** | M3 sur tous les pas devient un **oracle de borne**, non une référence déployable. Dans E4, la direction de l'effet n'est lue que sur les pas vérifiés, dans la limite du budget. Recalculer l'effet d'un choix vérifié relève légitimement de la vérification coûteuse. |
| A5 | Choisir le meilleur détecteur sur les données d'estimation biaise D\*, et ce biais dépend de n. | **Acceptée.** | Familles, détecteurs, couches de sonde et grille sont gelés sur un jeu de développement disjoint. L'évaluation se fait sur des tâches nouvelles. |
| A6 | E3 : sonde étiquetée par condition, δ non randomisé chez l'agent, aucune intention chez le scripté. | **Acceptée.** | E3 n'est plus défini sur le scripté. L'étiquette devient l'acte, sans la condition de trajectoire. La régression sur \|δ\| est remplacée par des options leurres à δ = 0 (E3′). |
| A7 | Le pré-remplissage asymétrique crée un signal de surprise lu à tort comme une « intention ». | **Transformée en test.** | J'ajoute un pré-remplissage symétrique (action honnête forcée dans une trajectoire saboteuse) et un appariement sur la log-probabilité de l'action sous la politique. |
| A8 | n covarie avec le nombre de compactions du résumé, donc avec la persistance de l'instruction. | **Acceptée.** | Le calendrier de compaction devient fixe en nombre de pas. J'ajoute un bras où l'instruction est réinjectée à chaque compaction. |
| A9 | D\* n'est pas identifié si TPR(D) ne traverse pas 50 % dans la grille. | **Acceptée.** | Ces points sont déclarés **censurés**. α n'est ajusté que sur les n où D\* est identifié, et la fraction censurée est rapportée. |
| A10 | Δα perd sa puissance si les comparaisons partagent le biais de l'exécution observée. | **Transformée en test.** | J'ajoute un bras « comparaisons produites par l'agent suspect lui-même » (E2′, voir aussi E6). |
| A11 | E4 est non jugeable à B = 1 et à B = 5. | **Acceptée.** | Voir C4. |
| A12 | Contrôles manquants : LoRA bénin de même rang, placebo de chaîne honnête contre honnête, pré-remplissage symétrique, invariance somme/moyenne. | **Acceptée** pour les quatre. | Le placebo de chaîne devient une porte d'entrée (E0). Le LoRA bénin est la classe négative de E3′. Je retiens aussi le « défaut commun » que A signale : sans adaptateur bénin, la conclusion « les activations gagnent » n'est pas réfutable chez moi. |

### Critiques de C

| # | Critique | Décision | Raison, ou test qui en découle |
|---|---|---|---|
| C1 | E1 et E2 seraient vraies par construction, « sans jamais tester la dynamique séquentielle d'un agent ». | **Rejetée en partie.** | Voir A1. Le côté adversaire est bien acquis par construction, mais le bruit honnête de l'agent, à n croissant, reste empirique. |
| C2 | E3 : l'erreur sur la variable \|δ\| (effet exact contre effet anticipé) crée une ordonnée à l'origine positive sous H_B. | **Acceptée.** | J'ai recalculé la limite : β₁μ_W σ_u²/(σ_W²+σ_u²), strictement positive. Le test par l'ordonnée à l'origine est **retiré**. Il est remplacé par une mesure directe à δ = 0 sur des options leurres (E3′, idée reprise de E, en le disant). |
| C3 | Sélection du meilleur détecteur et régression sur le dommage **réalisé**, qui est endogène. | **Acceptée.** | D\*(n) est désormais défini sur la **dose commandée** μ(q,n) = n·q·d̄. Le dommage réalisé n'est rapporté qu'en annexe. Pour la sélection, voir A5. |
| C4 | Atteindre un niveau de 5 % par un test de signe exige au moins 5 écarts vérifiés de même signe ; à B = 1, la puissance est nulle. | **Acceptée.** | Recalcul : 2⁻⁵ < 0,05 < 2⁻⁴. Pour l'attribution, B ∈ {10, 20, 40}. L'**interception** est rapportée séparément, à tout B. |
| C5 | Δα tend vers κ/2 si la corrélation entre exécutions honnêtes décroît avec n (bifurcations). | **Mécanisme accepté ; « falsifie à tort » rejeté.** | Si les exécutions divergent avec n, les comparaisons ne retirent effectivement pas la composante d'exécution, et H_A d'E2 est réellement fausse. L'erreur serait de l'attribuer à τ² petit. D'où une mesure par réplications imbriquées de ρ_traj(n) (E2′). |
| C6 | Contrôle manquant : honnête à cohérence méthodologique, avec des signes autocorrélés sans intention. | **Acceptée.** | J'ajoute la classe **H6** : prémisse méthodologique imposée au pas 1, sans direction cible, avec mesure de l'autocorrélation des signes chez l'honnête. |
| C7 | Contrôles manquants : H3 sous LoRA bénin à déclencheur actif ; adversaire scripté en rafale. | **Acceptée** pour les deux. | Le scripté en rafale, à dose égale, entre dans E1′. Il oppose les détecteurs par somme et par maximum. |

### Critiques de D

| # | Critique | Décision | Raison, ou test qui en découle |
|---|---|---|---|
| D1 | Les comparaisons retirent l'effet de **tâche**, pas l'effet d'**exécution**. La variance du contraste vaut (1+1/m)(Var(v)+σ²/T). | **Acceptée.** | Formule recalculée. E2′ estime Var(u), Var(v) et σ² par répétitions imbriquées et **prédit** Δα avant de le mesurer. |
| D2 | Convention somme ou moyenne. | **Acceptée.** | Voir A2. |
| D3 | Le remplacement scripté change le choix mais pas sa justification, que le texte peut trahir. Une sonde relevée avant le remplacement ne peut rien en dire. | **Acceptée.** | Le scripté pré-remplit le choix **puis** fait générer la justification par le modèle. Le même mécanisme est appliqué à des choix honnêtes de direction équilibrée (contrôle). Les sondes ne sont jamais évaluées sur le scripté. |
| D4 | L'ordonnée à l'origine d'un score brut est arbitraire. Il faut une différence conditionnelle g(x) par rapport au score honnête. | **Acceptée.** | g(x) devient la quantité de E3′, mesurée en x = 0 sur les leurres, donc sans extrapolation. |
| D5 | La baisse du rapport agentique/scripté n'isole pas un « coût de cohérence ». | **Acceptée.** | Je retire l'interprétation. E5′ sépare deux quantités : P(l'agent atteint la dose visée), et la détectabilité à dose réalisée égale. |
| D6 | α_goulot n'est pas estimable si le support du dommage est borné. | **Acceptée.** | Voir E2. |
| D7 | Une audit uniforme intercepte avec probabilité 1 − C(T−k,B)/C(T,B), qui tend vers 0 si k/T → 0. | **Acceptée.** | Sous R½, k ∝ √n, donc l'interception uniforme tend vers 0. **H_A d'E4 est acquise par construction pour l'audit uniforme.** Seul l'écart entre ciblage et audit uniforme est empirique (E4′). |
| D8 | Contrôles : références d'**une autre tâche** de difficulté appariée ; erreurs honnêtes **dirigées** ; pré-remplissage symétrique. | **Acceptée.** | La classe **H7** (erreurs honnêtes dirigées) est rapportée comme « dommage », jamais comme « intention ». Une alerte sur H7 compte comme fausse alerte pour l'intention. |
| D9 | Geler grille, détecteur et calibration ; traiter les dommages hors grille comme censurés. | **Acceptée.** | Voir A5 et A9. |

### Critiques de E

| # | Critique | Décision | Raison, ou test qui en découle |
|---|---|---|---|
| E1 | Endogénéité du dommage réalisé ; ambiguïté somme/moyenne. | **Acceptée.** | Voir C3 et A2. |
| E2 | En tâche à goulot, α ≈ 0 est acquis par construction : D ne peut pas être réparti. | **Acceptée.** | **P4 est retirée.** E5 est retirée comme comparaison d'exposants. |
| E3 | Des comparaisons générées par un modèle garanti sans LoRA injectent la vérité de classe. | **Acceptée.** | S6 l'annonçait, mais l'oracle était rangé parmi les instruments. Il est rétrogradé en **borne supérieure non déployable**, et j'ajoute le bras des comparaisons auto-générées. |
| E4 | Concavité sur un support discret avec min \|δ\| > 0 : l'ordonnée à l'origine est positive même si g(0) = 0. | **Acceptée.** | Voir C2. |
| E5 | Pré-remplissage : surprise hors politique. | **Acceptée.** | Voir A7. |
| E6 | Estimateur de D\* à moments infinis près de γ₁ = 0 ; intervalle de bootstrap invalide. | **Acceptée.** | Inversion par ajustement monotone contraint (pente > 0), censure au sens de A9, bootstrap restreint aux n identifiés, et proportion de rééchantillons non définis rapportée. |
| E7 | Contrôle : options d'effet exactement nul δ = 0. | **Acceptée et adoptée.** | Elle devient le cœur d'E3′. |
| E8 | Contrôle : sous q = 0, le taux d'alerte ne doit pas dépendre de \|D\| réalisé. | **Acceptée.** | Elle entre dans E0. |

---

## (b) Expériences corrigées

### Modifications du banc commun

Statut : HYPOTHÈSE de conception. Tous les chiffres sont illustratifs.

- **Convention somme**, avec d̄ constant, pré-enregistrée. Toutes les quantités sont aussi calculées en convention moyenne pour le contrôle d'invariance.
- **D\*(n)** est défini sur la dose commandée μ(q,n). Il n'est identifié que si TPR franchit 50 % dans la grille ; sinon il est censuré.
- **Gel** de tous les détecteurs, couches et seuils sur un jeu de développement disjoint, avant toute évaluation.
- **Classes honnêtes** : H1 à H5 comme en III.1, plus **H6** (cohérence méthodologique) et **H7** (erreurs honnêtes dirigées).
- **Adversaires scriptés** : i.i.d. et **rafale**, à dose égale. Le choix est pré-rempli et la justification générée.
- **Organismes agentiques** : en contexte et LoRA à déclencheur. Classes négatives : **LoRA bénin de même rang et de même procédure**, et **consigne secrète bénigne** en contexte (contrôle proposé par C pour D, que je reprends en le disant).
- **Compaction** à calendrier fixe en nombre de pas.
- **Options leurres** : à environ 10 % des points de décision, une option est décrite comme poussant dans la direction cible alors que son effet réel est exactement 0.

### E0 — Porte de validation de la chaîne (préalable)

- **H_A :** la chaîne est correcte. Sur bruit synthétique i.i.d. avec adversaire scripté i.i.d., l'IC95 de α_abs est inclus dans [0,4 ; 0,6]. Sur le placebo honnête contre honnête, D\* est déclaré non défini dans au moins 95 % des rééchantillons, à chaque n. Sous q = 0, le taux d'alerte est indépendant de \|D\| réalisé.
- **H_B :** la chaîne est biaisée. L'une de ces trois conditions échoue.
- **Falsification :** chaque issue falsifie l'une des deux hypothèses. Si H_B l'emporte, rien de ce qui suit n'est interprété.

### E1′ — La longueur change-t-elle quelque chose relativement au bruit honnête ? (pivot)

**Avant tout adversaire,** on mesure sur les seules trajectoires honnêtes :
- β_h, l'exposant de l'écart-type honnête du résultat final en fonction de n ;
- les composantes de variance du score du moniteur texte : τ² par trajectoire, autocorrélation ρ, et indice de queue, en reprenant pour moi le point de C sur les lois à variance infinie (formulé contre A).

On en déduit une **prédiction chiffrée** de α_rel, pré-enregistrée.

- **H_A (longueur neutre) :** α_rel ∈ [−0,15 ; 0,15] pour le détecteur texte agrégé, sans comparaison, sur le scripté i.i.d.
- **H_B (la longueur couvre l'adversaire) :** α_rel ≥ 0,25.
- **Second contraste, sur le scripté en rafale à dose égale :**
  - H_A′ : le détecteur par maximum ou CUSUM a un α_rel inférieur d'au moins 0,2 à celui de la somme ;
  - H_B′ : l'écart est inférieur à 0,1.
- **Contrôles négatifs :** H2 (erreurs non dirigées), H6 et le placebo de remplacement sur des choix honnêtes équilibrés. Le détecteur doit y rester à une AUROC dont l'IC contient 0,5.
- **Falsification :**
  - un IC95 de α_rel inclus dans [−0,15 ; 0,15] falsifie H_B ;
  - un IC95 entièrement au-dessus de 0,25 falsifie H_A ;
  - entre les deux, le résultat est déclaré non concluant, conformément à la règle de non-conclusion de III.1 (demi-largeur d'IC > 0,12).
- **Cohérence :** un écart de plus de 0,1 entre la prédiction tirée du bruit honnête et la mesure indique que le mécanisme de remplacement fuit. C'est le point D3 ; il est rapporté et le résultat n'est pas interprété.

### E2′ — Les comparaisons retirent-elles la composante qui couvre l'adversaire ?

**Mesure préalable par réplications imbriquées :** plusieurs tâches, plusieurs exécutions par tâche et plusieurs n. On estime Var(u) (effet de tâche), Var(v) (effet d'exécution), σ² et ρ_traj(n). On en déduit une prédiction de Δα.

- **H_A :** avec m = 3 références honnêtes de **même tâche**, Δα = α_rel(m=0) − α_rel(m=3) ≥ 0,3. Avec des références d'**une autre tâche** de difficulté appariée, Δα < 0,1.
- **H_B :** Δα < 0,15 avec les références de même tâche. La composante d'exécution Var(v) domine, ou ρ_traj(n) décroît (C5).
- **Bras de stress (hypothèse S6) :** les références sont produites par l'agent suspect lui-même.
  - H_A″ : le gain s'annule (Δα < 0,1) ;
  - H_B″ : il persiste au-dessus de 0,2.
- **Pré-déclaration :** E2′ est non informative si Var(u) ≈ 0.
- **Falsification :** les bornes d'IC tranchent comme en III.1. La différence avec la prédiction tirée des composantes de variance est rapportée.

### E3′ — Les activations portent-elles un signal d'intention indépendant de l'effet ?

E3′ porte uniquement sur les organismes agentiques.

- **Quantité mesurée :** g_leurre est la différence de score de sonde, en écarts-types honnêtes, entre deux cas :
  - un acte où l'agent adverse choisit un leurre d'effet nul ;
  - **la même action** pré-remplie dans une trajectoire honnête, appariée en log-probabilité.

  Il n'y a ni régression ni extrapolation.
- **Entraînement de la sonde :** étiquettes au niveau de l'acte, sur une famille de tâches disjointe ; évaluation sur des tâches tenues à l'écart.
- **H_A (régime R0 possible) :** g_leurre ≥ 0,5, avec IC excluant 0. La sonde bat le moniteur texte sur ces mêmes actes. L'effet survit aux quatre contrôles : LoRA bénin à déclencheur actif, consigne secrète bénigne, instruction présente mais désactivée, pré-remplissage symétrique.
- **H_B :** l'IC de g_leurre contient 0, ou l'effet disparaît sous l'un des contrôles.
- **Prédiction P3 maintenue :** H_A ne survit, au mieux, que sur l'organisme en contexte.
- **Suite conditionnelle :** α_rel n'est mesuré avec la sonde agrégée que si H_A tient.

### E4′ — Vérification coûteuse à budget absolu fixe

- **Partie acquise par construction (D7) :** l'interception uniforme suit la loi hypergéométrique. Elle est calculée, pas testée.
- **H_A :** le rapport entre interception ciblée par le moniteur gelé et interception uniforme croît avec n (pente du log du rapport sur log n > 0). Le ciblage compense la dilution.
- **H_B :** la pente est ≤ 0.
- **Attribution,** rapportée séparément, à B ∈ {10, 20, 40} : au moins 5 écarts vérifiés de même signe. La direction n'est lue que sur les pas vérifiés.
- **Contrôles :** taux de fausses attributions sur H2, H5, H6 et H7.
- **Falsification :** les bornes d'IC de la pente tranchent.

### E5′ — L'adversaire agentique est-il plus furtif que le scripté ?

- **H_A :** à dose réalisée égale, le TPR contre l'agentique est inférieur d'au moins 10 points à celui contre le scripté. L'agent place ses actes là où ils se voient le moins.
- **H_B :** l'écart est inférieur à 3 points, ou de signe inverse.
- **Mesure descriptive annexe :** P(dose visée atteinte) en fonction de n. Elle n'est pas interprétée comme un mécanisme (D5).

### Prédictions révisées

Statut : HYPOTHÈSE ; tous les seuils sont illustratifs.

- **P1′.** Avec le texte seul et m = 0, α_rel ≥ 0,25 si τ² est non négligeable. Dans ce cas, la longueur couvre l'adversaire relativement au bruit honnête.
- **P2′.** Avec m = 3 références honnêtes de même tâche, α_rel revient dans [−0,15 ; 0,15], sauf si Var(v) domine.
- **P3′.** g_leurre > 0 seulement pour l'organisme en contexte, et l'effet disparaît sous le contrôle par consigne secrète bénigne.
- **P4.** Retirée.
- **P5′.** Le ciblage par le moniteur ne compense pas la dilution : la pente de E4′ est ≤ 0.

**Calendrier.** Les semaines 1 et 2 sont consacrées à E0 et aux mesures honnêtes imbriquées. E1′ et E2′ occupent les semaines 3 et 4, E3′ les semaines 5 et 6, E4′ et E5′ la semaine 7. Le budget de calcul de III.1 augmente d'environ 30 % à cause des réplications imbriquées (illustratif).

---

## (c) Réponse à la question de l'arbitre

**Ce qui est établi.** Aucun résultat empirique. Le bloc FAITS ne contient aucun fait muni d'un statut, et aucune pièce ne rapporte de mesure. Ce qui suit est établi **mathématiquement, sous des modèles explicites**. Ce sont des dérivations, pas des observations sur un agent.

- **Dilution i.i.d.** Face à un adversaire qui dilue de façon i.i.d. sur un bruit honnête i.i.d., la dose absolue indétectable croît en √n (illustratif). L'écart-type honnête du résultat croît de même. **Relativement au bruit honnête, la longueur ne change alors rien.**
- **Audit uniforme.** Un audit uniforme à budget fixe intercepte de moins en moins un adversaire dont la fraction d'actes modifiés tend vers 0.
- **Goulot.** Une tâche à goulot interdit la dilution par construction.

Ces trois points n'ont pas besoin d'expérience. Ils servent de contrôles positifs.

**Ce qui n'est pas établi**, et qui décide de la réponse :

1. **La structure du bruit honnête d'un agent de 8 milliards de paramètres à n croissant.** Elle comprend une composante persistante par exécution, l'autocorrélation et les queues. Si une composante persistante existe, la longueur couvre l'adversaire relativement au bruit honnête (HYPOTHÈSE, P1′).
2. **Ce que retirent les exécutions de comparaison.** Elles retirent l'effet de tâche, mais pas nécessairement l'effet d'exécution. Elles ne retirent rien si elles viennent du modèle suspect (HYPOTHÈSE).
3. **Ce que lisent les activations.** Une intention distincte de l'effet de l'acte, ou seulement l'instruction présente dans le contexte et des poids modifiés (HYPOTHÈSE, P3′).
4. **Si un modèle de cette taille sait diluer** mieux qu'un script (HYPOTHÈSE).

**La forme réfutable de ma réponse.** Ce que change la longueur se mesure par **α_rel**, l'exposant de la dose indétectable rapportée à l'écart-type honnête du résultat. Selon l'issue :
- α_rel ≈ 0 : la longueur ne change rien ;
- α_rel > 0 : elle couvre l'adversaire ;
- α_rel < 0 : elle aide le défenseur.

Chaque instrument est jugé à la variation de α_rel qu'il produit, sur des classes négatives qui comprennent des honnêtes à erreurs dirigées et des adaptateurs bénins.

**L'expérience à faire en premier.** C'est la **décomposition de la variance honnête en fonction de n** (semaines 1 et 2), précédée de la porte E0. Elle ne demande aucun adversaire.

- **H_A :** les scores par pas du moniteur sont quasi indépendants, avec Var(v) négligeable. On prédit alors α_rel ≈ 0 sans comparaison.
- **H_B :** une composante persistante d'exécution existe. On prédit alors α_rel > 0, non corrigé par les comparaisons de même tâche.

Chacune des deux issues falsifie une branche et fixe à l'avance les prédictions chiffrées de E1′ et E2′. La même mesure tranche la première issue qui rendrait la question sans intérêt : si l'écart-type honnête du résultat dépasse le dommage pertinent à grand n, le travail honnête lui-même est inutilisable.

**Type de contribution.** Une loi connue ailleurs, la loi de la racine carrée de la stéganographie et de la communication furtive, réexprimée en exposant relatif. Elle est jointe à un phénomène à tester, l'existence d'un signal d'intention à effet nul, mesuré sur des options leurres. Ce n'est pas une garantie.

**Nouveauté.** Elle se vérifie comme en III.1 : recherche croisée « square root law / covert » avec « AI control / sabotage », et lecture ciblée de Wen et al. (2024) et de Bhatt et al. (2025). Ces deux références sont citées de mémoire, au statut RAPPORTÉ, à vérifier.

FIN-DE-CELLULE