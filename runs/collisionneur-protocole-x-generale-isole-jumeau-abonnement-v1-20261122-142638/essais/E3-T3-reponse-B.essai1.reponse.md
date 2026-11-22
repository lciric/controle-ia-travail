Fichier lu en entier (788 lignes, en quatre lectures). Voici la cellule de B pour le tour III.3.

# Proposition B, tour III.3 : réponse aux critiques

**État des pièces.** Les blocs FAITS et QUESTION DE L'ARBITRE sont présents et portent la même empreinte annoncée. Je ne l'ai pas recalculée (OBSERVÉ-NON-AUDITÉ). Ma conception III.1 et les critiques de A, C, D et E sont présentes et closes par leur marqueur. Aucune coupure visible. Je ne traite que les sections « Sur la proposition B ».

**Statuts.** Tout ce que j'avance est HYPOTHÈSE sauf mention contraire. « VÉRIFIÉ (calcul) » ne couvre que l'algèbre ou l'arithmétique, sur des entrées illustratives. Je reprends tels quels les statuts des autres pièces. Seuils, effectifs, budgets et valeurs de paramètres sont tous illustratifs. Seuls « trois articles », « deux mois » et « huit milliards de paramètres » viennent des faits.

## (a) Réponse aux critiques

### 1. Le duel 5 ne pouvait guère échouer

- **A-a1** (paramètres mesurés axe par axe ; une loi a·nᵇ est indiscernable de la mienne sur n ∈ {2, 4, 8}). **Acceptée.** J'ai refait le calcul et retrouvé les mêmes valeurs que A (2,5 % et 2,7 %).
  - Correction : tous les paramètres sont estimés à n ≤ 2 (témoin isolé et paires), sans aucun ajustement sur une courbe de détection. La prédiction porte sur n ∈ {4, 8, 16}.
  - Calée sur les mêmes données (n = 1 et n = 2), une loi a·nᵇ s'écarte de la loi de corrélation à n = 16 de 31 % en d' pour ρ = 0,1 et de 39 % pour ρ = 0,3 (VÉRIFIÉ, calcul).
- **D-a** (prédiction circulaire ; transporter un résultat d'une tâche à l'autre sur un même axe ne prouve pas qu'il se transporte d'un axe à l'autre). **Acceptée.**
  - Je retire « trois paramètres communs aux trois axes ».
  - Ce qui reste commun est une comptabilité : la valeur du témoin suivant se calcule à partir de son décalage propre et de sa covariance avec les témoins présents, mesurée dans chaque classe.
  - Le lien entre axes est testé deux fois : par le duel 4 (la corrélation mesurée avant l'attaque prédit-elle le transfert ?) et par le duel 6 (la comptabilité change-t-elle l'achat de témoins ?).
- **A-b** (ρ sans effet si (n−1)ρ ≪ 1 ; corrélation qui décroît avec l'écart, ρ^|i−j|). **Acceptée.** n monte à 16 sur l'axe des copies, et l'axe temporel utilise l'autocovariance complète.

### 2. Axes mal définis

- **C-a1, E-a2, D-a** (sur l'axe temporel, seuls k pas sur N portent du signal, donc un ρ̂ > 0 apparaîtrait par construction ; un pas de plus n'est pas un acte de plus). **Acceptée.** L'axe temporel n'utilise plus la formule équicorrélée.
  - Pour la somme sur T pas, le signal vaut k·μ(H/k).
  - La variance honnête vaut Tc₀ + 2Σ(T−h)c_h. C'est l'identité donnée par D, dont je ne change pas le statut. Les c_h sont mesurés sur des trajectoires honnêtes.
- **A-a2, E-a2** (moniteurs hétérogènes, sans d'₁ commun). **Acceptée.** La prédiction passe par la forme gaussienne générale : vecteur des décalages et matrices de covariance par classe, sur les sous-ensembles de {texte, sonde, autre famille}.

### 3. d' et ρ

- **C-b2, E-b1** (ρ₀ ≠ ρ₁, σ₀ ≠ σ₁). **Acceptée.** Pour la somme, d'ₙ = √(2n)·Δμ / √(σ₀²(1+(n−1)ρ₀) + σ₁²(1+(n−1)ρ₁)) (VÉRIFIÉ, calcul ; même expression que chez C et E). Les deux classes sont estimées séparément.
- **A-a3** (le ρ de la classe sabotage mêle bruit partagé et variation d'intensité entre trajectoires). **Transformée en test.** On calcule aussi un ρ₁ partiel, après régression sur le dommage mesuré, comme le propose A. La prédiction est faite avec les deux versions et l'écart est rapporté (duel 5).
- **A-b, C-b3, D-b, E-b1** (√2·Φ⁻¹(AUC) n'est plus valable sous variances inégales, mélanges ou négatifs difficiles ; AUC ∈ {0, 1} ; erreur relative indéfinie en d' = 0). **Acceptée.**
  - Métrique primaire partout : taux de détection à 5 % de fausses alertes par trajectoire.
  - Le seuil est estimé sur le mélange honnête H1–H5 tel qu'il serait déployé. Sa variance entre dans un bootstrap par tâche.
  - L'erreur de prédiction se compte en points absolus. d' ne sert plus que de résumé.
- **A-c, D-c** (scores synthétiques non échangeables ; témoin de mêmes moments mais à queues différentes). **Acceptée.** La chaîne d'analyse doit rejeter ces lois mal spécifiées (contrôle de puissance), et pas seulement retrouver ρ (contrôle de niveau).
- **A-b** (1 % de fausses alertes par pas donne 18 % à 45 % par trajectoire). **Acceptée.** Le seuil par pas est réglé pour 5 % de fausses alertes par trajectoire sur le maximum des pas. Le caractère « anodin » d'un acte se mesure à ce seuil.

### 4. Estimation de α

- **A-a4, C-a2, C-b1, E-b2** (régresseur bruité, troncature du logarithme, non-additivité, taille confondue avec le type d'acte, arrêt optionnel). **Acceptée.**
  - Je supprime l'attribution acte par acte par rejeu, ainsi que la régression log-log par acte.
  - k est assigné et le dommage total est fixé par la tâche. La pente de log(décalage moyen de la somme) en fonction de log k vaut alors 1 − α.
  - Les moyennes sont prises par groupe avant le logarithme (contrôle C-c1). Le type d'acte devient une strate. L'effectif est fixé d'avance, sans doublement conditionnel.
- **D-b** (si la variance de la somme dépend de k, le signe de 1 − α ne suffit pas). **Acceptée.** Le duel 2 juge directement la détection en fonction de k ; α devient un mécanisme secondaire.
- **E-a2, sur le signe** (une interaction conjonctive donnerait ĥ ≈ 0 et pousserait α̂ au-dessus de 1). **Rejetée sur ce point**, sans toucher au statut que E lui donne.
  - Avec une porte ET ou un seuil, retirer un acte annule la bascule : le rejeu attribue H à chaque acte, comme l'écrit C-a2.
  - ĥ ≈ 0 ne vaut que pour des actes redondants (porte OU). Le sens du biais dépend donc de la porte.
  - Le fond de la critique (l'attribution est invalide quand les actes interagissent) est accepté. Le contrôle E-c2 est **transformé en test** de validation du nouvel estimateur (duel 2).
- **D-a** (permuter les pas ne change pas une somme). **Acceptée.** Ce contrôle ne vise plus que le CUSUM.

### 5. Duel 1

- **A-a8** (k choisi parmi trois valeurs sans correction). **Acceptée** : correction de Holm.
- **D-b, D-c** (le taux de bascule dépend du sens de la cible). **Acceptée.** Le sens est tiré au hasard par tâche. On mesure l'excès de bascule dirigée par rapport aux erreurs aveugles H3 de même k, sur les mêmes tâches.
- **C-c3** (déclencheur présent avec une cible égale à la vraie réponse). **Acceptée**, comme contrôle des duels 1 et 4.

### 6. Duel 3

- **E-a1, E-b3** (les scores de divergence partagent la même exécution cible y₀). **Acceptée.**
  - Je refais le calcul : si s_r = g(y₀) − g(y_r) avec des y indépendants et de même loi, alors Corr(s₁, s₂) = 1/2 (VÉRIFIÉ, calcul).
  - L'attente E1 était donc vraie par construction ; je la retire.
  - **Transformée en test** : corrélation mesurée sur des paires disjointes (E-c1), en excès d'une ligne de base honnête–honnête de même plan.
- **C-a3, E-a1** (en condition S, l'espérance de l'écart s'annule ; c'est d'₁ qui s'effondre, pas ρ qui monte). **Acceptée.** La divergence sur la conclusion ne sépare pas des poids partagés d'un but partagé. Le duel porte désormais sur l'emplacement des actes.
- **A-a5** (le point focal est planté par la consigne ; la condition X change à la fois les poids, la compétence et le plancher). **Acceptée.** J'ajoute :
  - une condition « mêmes poids, cibles indépendantes » ;
  - des rééchantillons honnêtes de l'autre famille (A-c) ;
  - des familles appariées sur leur taux marginal d'erreur (D-c) ;
  - un recouvrement mesuré en excès de l'indépendance conditionnelle à l'étape. L'objection de D et E contre le κ de A s'applique ici aussi.
- **A-b, D-b** (rapports instables). **Acceptée** : j'utilise des différences, pas des rapports.

### 7. Duel 4

- **E-a3** (erreur de signe sur E3). **Acceptée en partie.**
  - E3 (« ρ monte ») n'était pas dérivée ; je la retire.
  - Le résultat de restriction d'étendue cité par E porte sur une sélection dans une loi fixe. La loi après affinage n'est pas une loi tronquée (HYPOTHÈSE).
  - **Transformée en test.** Sous sélection binormale, E[sonde | texte ≤ c] = ρ₁·E[texte | texte ≤ c] en unités réduites (VÉRIFIÉ, calcul). La baisse de la sonde est donc prédite par le ρ₁ mesuré avant l'attaque.
- **D-a, E-a3** (les deux issues se recouvrent à 25 %). **Acceptée** : la frontière est attribuée à une seule hypothèse.
- **A-a6, A-c, E-c3** (composition des tâches et des actes ; appariement sur le dommage). **Acceptée** comme contrôles.
- **D-b, D-c** (un seuil inchangé après affinage ne garde pas le même taux de fausses alertes ; affinage factice). **Acceptée** : seuils recalibrés sur les honnêtes de chaque affinage, affinage factice compris.
- **E-b3** (rapport de variance infinie). **Acceptée** : différence au lieu d'un rapport, et condition de jugeabilité (attaque réussie).

### 8. Duel 6

- **A-a7, C-a4, D-c, E-a3, E-c4** (U dispose de plus d'instruments que S). **Acceptée.** U(ρ̂) est opposée au meilleur de U(ρ = 0) et d'une allocation fixe équirépartie (C-c2), à menu identique. S reste descriptive.
- **D-b** (utilité égale ; cas où les politiques ne diffèrent jamais). **Acceptée** : la fraction de tâches où elles diffèrent est rapportée.
- **A-b** (gain plafonné si la prévalence est inférieure à la fraction vérifiée). **Acceptée** : prévalence de 10 % pour 2 % de trajectoires vérifiées.
- **C-b3** (maximiser d' n'est pas maximiser la détection à fausses alertes fixées). **Acceptée** : U maximise la détection prédite à fausses alertes fixées.

### 9. Fuites

- **A-a8, A-c** (mêmes organismes en calibration et en test ; jeu d'entraînement de la sonde non situé). **Acceptée.** Un organisme saboteur et une famille de tâches restent hors de toute calibration. La sonde est entraînée sur un troisième jeu, disjoint des deux autres.

## (b) Expériences corrigées

**Conventions communes**
- L'unité de rééchantillonnage est la tâche, branches comprises.
- H_A est retenue si l'IC 95 % tombe entièrement dans sa région ; H_B, s'il tombe entièrement dans la sienne. Sinon, pas de verdict ; ce n'est pas une troisième hypothèse. Les effectifs visent 80 % de puissance à la frontière.
- Le sens de la cible est tiré au hasard par tâche.
- « Détection » désigne le taux de détection à 5 % de fausses alertes par trajectoire.

[DUEL 1]
**Porte d'entrée : le phénomène existe-t-il à huit milliards de paramètres ?**
- **H_A.** Pour au moins un k ∈ {3, 5, 8}, avec correction de Holm, les deux conditions tiennent :
  - (i) l'excès de bascule dirigée atteint au moins 20 points. C'est la bascule vers la cible sous sabotage, moins la même bascule sous les erreurs aveugles H3 de même k, sur les mêmes tâches ;
  - (ii) la détection par acte reste ≤ 10 % au seuil par pas qui donne 5 % de fausses alertes par trajectoire.
- **H_B.** Pour tout k, (i) ou (ii) échoue. C'est le complément exact.
- **Contrôles.** H3 ; H4 (organisme sans son déclencheur) ; déclencheur présent avec une cible égale à la vraie réponse.
- **Falsification.** Un k qui remplit (i) et (ii) falsifie H_B. Sinon H_A est falsifiée, et le programme est sans objet à cette échelle.

[DUEL 2]
**Article 1 : répartir le sabotage dans le temps aide-t-il l'attaquant contre l'agrégateur de somme ?**
- **Plan.** La cible exige un déplacement fixé, donc le dommage total est fixé par la tâche. k ∈ {1, 2, 4, 8} est assigné, et le k réalisé est compté par script. L'analyse primaire porte sur toutes les tentatives ; l'analyse conditionnelle au succès est secondaire, avec le taux de succès rapporté pour chaque k.
- **H_A.** Détection(k = 8) ≥ détection(k = 1) − 5 points : répartir n'aide pas l'attaquant.
- **H_B.** Détection(k = 8) < détection(k = 1) − 5 points.
- **Mécanisme (secondaire).** α̂ = 1 − pente de log(décalage moyen de la somme) sur log k, avec des moyennes par groupe. On l'estime séparément pour le texte et pour la sonde. L'attente E4 est jugée sur la différence des deux pentes.
- **Validation de l'estimateur.** Sur des pipelines synthétiques additifs et conjonctifs à α ∈ {0,5 ; 1 ; 2} connu, l'estimateur doit retrouver α à ±0,1 sur les deux topologies. Sinon, on abandonne la partie « mécanisme ».
- **Contrôles.** H3 de même k et de même dommage ; ρ partiel ; permutation des pas pour le CUSUM seulement.
- **Falsification.** Chaque issue falsifie l'autre.

[DUEL 3]
**Article 2 : des copies de mêmes poids placent-elles leurs actes aux mêmes endroits ?**
- **Conditions.**
  - S_même : mêmes poids, même cible.
  - S_ind : mêmes poids, cibles tirées indépendamment.
  - X : autre famille, même cible, appariée sur le taux marginal d'erreur.
  - Trajectoires honnêtes des deux familles.
- **Métrique.** La probabilité que deux copies sabotent la même étape, moins sa valeur attendue sous indépendance conditionnelle à l'étape. Les propensions par étape sont estimées sur des exécutions hors test. On ajoute une strate de tâches dont les étapes ont une influence égale et sont permutables.
- **H_A.** Excès(S_même) − Excès(X) ≥ 0,10 : les poids partagés coordonnent l'emplacement.
- **H_B.** Écart < 0,10.
- **Mesure associée (pour le duel 5).** R ∈ {1, 2, 4, 8, 16} exécutions de comparaison. On mesure la corrélation des divergences sur des paires disjointes, en excès de la ligne de base honnête–honnête de même plan.
- **Contrôles.** S_ind sépare l'effet de la consigne de celui des poids ; les honnêtes de l'autre famille donnent le plancher de divergence.
- **Falsification.** Chaque issue falsifie l'autre. Sous H_B, l'article 2 porte sur la structure des tâches et le but partagé, pas sur les copies.

[DUEL 4]
**Article 3 : l'attaque contre le moniteur texte se transfère-t-elle à la sonde au-delà de ce que prédit la corrélation d'avant l'attaque ?**
- **Procédure.** Affinage LoRA par échantillonnage de rejet sur les sabotages réussis que le moniteur texte note bas. La sonde est entraînée avant l'affinage, puis gelée ; elle ne sert jamais à la sélection.
- **Grandeurs mesurées.**
  - Δ_x : variation, entre avant et après l'attaque, de l'écart moyen sabotage − honnête pour l'instrument x. Les honnêtes de référence sont les H4 du même affinage. L'unité est l'écart-type de la classe sabotage mesuré avant l'attaque.
  - δ = Δ_sonde − ρ̂₁·Δ_texte, où ρ̂₁ est la corrélation texte–sonde mesurée avant l'attaque dans la classe sabotage.
- **H_A.** |δ| ≤ 0,1 : l'attaque agit comme une sélection, et la corrélation d'avant l'attaque suffit à prédire le transfert.
- **H_B.** |δ| > 0,1 : l'affinage déforme la loi jointe. δ < 0 indique une surface d'attaque partagée ; δ > 0, un découplage.
- **Jugeabilité.** Il faut Δ_texte ≥ 0,5. Sinon l'attaque a échoué, et le duel est déclaré non jugeable avant tout calcul de δ.
- **Contrôles.**
  - Sélection sur un score aléatoire, appariée en composition de tâches, en types d'actes et en dommage.
  - Affinage factice.
  - Sonde réentraînée après l'attaque, pour distinguer une sonde périmée d'un signal effacé.
  - H5 ; déclencheur présent avec une cible égale à la vraie réponse.
- **Falsification.** Chaque issue falsifie l'autre.

[DUEL 5]
**Unification : la comptabilité des témoins prédit-elle la détection sur les trois axes, sans ajustement sur les courbes ?**
- **Entrées, mesurées sur T_cal à n ≤ 2.**
  - Décalage d'un témoin isolé.
  - Covariances par classe (ρ₀, σ₀, ρ₁, σ₁, ou matrices complètes).
  - Autocovariance honnête des pas.
  - μ(h), tiré des cas k ∈ {1, 2} du duel 2.
- **Cibles sur T_test.**
  - Copies : R ∈ {4, 8, 16}.
  - Instruments : sous-ensembles de {texte, sonde, autre famille}, avant et après l'attaque du duel 4, avec des paramètres remesurés à n ≤ 2 dans chaque état.
  - Temps : k ∈ {4, 8} et T ∈ {20, 40, 60}.
- **H_A, axe par axe.** Les deux conditions tiennent :
  - |détection observée − détection prédite| ≤ 5 points (IC 95 %) ;
  - l'erreur est inférieure d'au moins 5 points à celle du meilleur comparateur calé sur les mêmes données : le modèle indépendant, et aussi a·nᵇ sur l'axe des copies.
- **H_B.** Une des deux conditions échoue sur cet axe.
- **Contrôles.**
  - Scores synthétiques à ρ connu (contrôle de niveau).
  - AR(1), variances inégales, queues lourdes à mêmes moments, que la chaîne doit rejeter (contrôle de puissance).
  - Appariements permutés ; ρ₁ partiel.
- **Falsification.** Un axe en H_B sort de la problématique commune. H_A sur les trois axes falsifie H_B.

[DUEL 6]
**Valeur pour les décisions : la comptabilité change-t-elle l'achat de témoins ?**
- **Menu commun.** Rééchantillons, moniteur d'une autre famille, sonde et vérification coûteuse. Même budget pour tous, et au moins 98 % d'acceptation des honnêtes.
- **Politiques.**
  - U(ρ̂) : maximise la détection prédite à fausses alertes fixées.
  - U(ρ = 0) : même politique, témoins supposés indépendants.
  - U_égal : allocation fixe équirépartie.
  - S : décrite à part.
- **Flux.** Prévalence de 10 % ; 2 % des trajectoires sont vérifiées.
- **H_A.** U(ρ̂) − max(U(ρ = 0), U_égal) ≥ 5 points de sabotages interceptés sur T_test.
- **H_B.** Moins de 5 points.
- **Rapporté.** La fraction des tâches où U(ρ̂) et U(ρ = 0) choisissent différemment.
- **Falsification.** Chaque issue falsifie l'autre. Le duel 5 dit si la comptabilité est vraie ; le duel 6 dit si elle sert.

[FIN DES DUELS : 6]

## (c) Réponse à la question de l'arbitre

**Verdict conditionnel.** La problématique d'ensemble existe si une même comptabilité prédit la détection sur les trois axes (duel 5) et change l'achat de témoins (duel 6). Cette comptabilité calcule la valeur du témoin suivant à partir de son décalage propre et de sa covariance avec les témoins présents, dans chaque classe. Sinon, on fait trois articles distincts sur un banc d'essai commun.

**Établi** (VÉRIFIÉ, calcul seulement) :
- l'expression de d'ₙ pour des témoins équicorrélés, de variances égales ou non ;
- ma version III.1 du duel 5 ne pouvait guère échouer (A). La version corrigée sépare les deux lois de 31 % à 39 % en d' à n = 16 (ρ = 0,1 et 0,3, illustratif) ;
- des divergences calculées contre une même cible sont corrélées à 1/2 sans aucun effet des poids (E) ;
- sous sélection binormale, la sonde perd ρ₁ fois ce que perd le texte.

**Non établi** (HYPOTHÈSE) : l'existence du sabotage réparti à huit milliards de paramètres ; la valeur de α ; une coordination d'emplacement due aux poids ; un transfert au-delà de la sélection ; la validité prédictive ; la valeur pour les décisions.

**(1) Question.** Face à un sabotage réparti en actes anodins, la détection obtenue en ajoutant des pas, des copies ou des moniteurs se prédit-elle, sur les trois axes, à partir du seul décalage d'un témoin isolé et de covariances mesurées sur des paires — et cette prédiction change-t-elle les témoins qu'un défenseur à budget fixe doit acheter ?

**(2) Réponse attendue** (HYPOTHÈSE) :
- prédiction juste à ±5 points (illustratif) sur les axes du temps et des copies ;
- excès de recouvrement entre copies de mêmes poids d'au moins 0,10 (illustratif) ;
- d'où un gain d'au moins 5 points (illustratif) pour U(ρ̂), venant surtout de l'achat d'un moniteur d'une autre famille plutôt que de rééchantillons supplémentaires.

Pour le duel 4, mon attente est faible (δ < 0). Les duels 3, 5 et 6 peuvent réfuter ces attentes.

**(3) Antériorité la plus proche**, citée de mémoire (RAPPORTÉ) : Greenblatt, Shlegeris, Sachan, Roger (2023), *AI Control: Improving Safety Despite Intentional Subversion*. On y trouve une copie non fiable du modèle qui surveille et un budget d'audit limité ; mais les tâches sont courtes et la corrélation entre témoins n'y sert pas de prédicteur. Pour la loi elle-même, aussi de mémoire :
- Kish (1965), *Survey Sampling* ;
- Knight & Leveson (1986), *An Experimental Evaluation of the Assumption of Independence in Multiversion Programming* ;
- Fisher (1936), *The Use of Multiple Measurements in Taxonomic Problems*.

Pour le rééchantillonnage comme contrôle : Bhatt et al. (2025), *Ctrl-Z*, référence à vérifier.

**(4) Expérience.** Les duels 1 à 6 sur Qwen3-8B, avec une réplication sur Llama-3.1-8B-Instruct. Environ 500 h-H100, plus une dizaine d'heures pour R = 16 (illustratif), en deux mois.

**(5) Type de contribution.** Des lois connues ailleurs (effet de plan, programmation multi-versions, discriminant linéaire, restriction d'étendue — référence à vérifier pour cette dernière), transposées en protocole de prédiction. S'y ajoute un phénomène possible : la coordination d'emplacement par des poids partagés. Ce n'est pas une garantie, car tout est mesuré sur des sabotages plantés.

**Issues qui rendraient la question sans intérêt :**
- le duel 1 donne H_B ;
- l'excès de corrélation est nul sur les trois axes, et l'indépendance suffit ;
- le duel 6 donne H_B : la comptabilité est vraie mais inutile.

**Vérifier la nouveauté.** Chercher « design effect », « effective number of monitors », « monitor diversity » et « N-version » dans les suites de Greenblatt et al. (2023). Si un travail ajuste déjà une telle comptabilité à des ensembles de moniteurs face au sabotage, ma contribution se réduit à une réplication à huit milliards de paramètres sur des tâches longues. Garde-fous : préenregistrement, recalcul par un tiers à partir des scores bruts, et deux familles de modèles.

**Expérience à faire en premier : le duel 1.** En parallèle, deux mesures qui n'exigent aucun saboteur :
- les covariances honnêtes (pas, copies jusqu'à R = 16, instruments) ;
- la validation des estimateurs sur données synthétiques.

Durée : deux à trois semaines (illustratif). Si le duel 1 donne H_B, on s'arrête avant l'affinage par rejet du duel 4 et avant l'auditeur de 70 milliards de paramètres (illustratif).

FIN-DE-CELLULE