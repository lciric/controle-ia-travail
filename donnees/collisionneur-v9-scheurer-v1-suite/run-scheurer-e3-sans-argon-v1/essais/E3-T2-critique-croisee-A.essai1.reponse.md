# Tour III.2 — critique croisée de méthode (proposition A)

**Statuts.** Tout ce qui vient de la pièce Scheurer est **RAPPORTÉ** ; tout ce qui vient de « nos résultats » est **OBSERVÉ-NON-AUDITÉ** ; les conceptions D et E sont des **HYPOTHÈSES** que je critique comme telles. Mes chiffres sont **illustratifs** ou **calcul**, jamais des résultats. Je ne fusionne pas D et E : chacune est jugée sur ses propres instruments, et je signale quand une même faille les touche toutes deux sans en déduire une moyenne.

## Sur la proposition B

Pièce absente (statut : REFUS). Je n'ai rien à critiquer et je n'invente pas son contenu.

## Sur la proposition C

Pièce absente (statut : jamais lancée). Même traitement : aucune critique, aucun contenu supposé.

## Sur la proposition D

### (a) Défauts de méthode

**D1 — Le seuil de E1 coïncide avec l'effet attendu : non-conclusion par construction.** D annonce pour T2 un facteur +5,1 %/mois (supposé) et fixe H_A : β ≥ log(1,05)/mois. Si le vrai β vaut l'effet attendu, la borne inférieure de l'IC tombe au-dessus du seuil avec une probabilité proche de 1/2 (**calcul** : un IC centré sur le seuil le chevauche une fois sur deux). Le duel est conçu pour finir « non concluant » dans le cas même que D juge probable. Il faut soit un seuil nettement sous l'effet attendu, soit un effet attendu nettement au-dessus du seuil ; les deux à égalité, c'est un test sans puissance.

**D2 — L'axe « difficulté humaine de l'attaque » est confondu avec le générateur.** Le corpus d'attaques est produit par des modèles attaquants, et la pièce rapporte que les attaquants récents « semblent produire des portes dérobées plus subtiles » (**RAPPORTÉ**, Scheurer §3.3). Si la difficulté c d'une attaque dépend de son générateur g, et si le score du moniteur dépend de g à c fixé (style, longueur, idiomes), alors le c50 mesure en partie la reconnaissance de style, et la pente sur la date capture la covariance entre date du moniteur et détectabilité stylistique des générateurs. Les jumeaux honnêtes « du même générateur » corrigent la provenance honnête/malveillante (la limite §7 de Control Tax, **RAPPORTÉ**), pas la confusion difficulté/générateur sur l'axe lui-même.

**D3 — Le filtre de validation mécanique est asymétrique.** Une attaque n'entre au corpus que si elle passe les tests *et* diverge sur l'entrée déclencheuse ; un jumeau honnête n'a qu'à passer les tests. Le taux d'acceptation diffère, et les attaques survivantes sont vraisemblablement plus longues ou plus ramifiées que les jumeaux. Un moniteur qui note la longueur ou la complexité cyclomatique « détecte » alors par construction. D exige de battre « règles statiques », mais ne décrit pas d'appariement en longueur/complexité.

**D4 — Vrai par construction : le moniteur émule un oracle d'exécution.** La vérité terrain est « diverge sur une entrée » ; un moniteur qui sait tracer l'exécution d'un programme converge vers cet oracle. La tendance de c50 se réduit alors à la tendance de la capacité de lecture de code des moniteurs, une capacité ordinaire — exactement ce que l'arbitre demande de ne pas confondre. D ne prévoit pas de conditionner sur la capacité de code du moniteur lui-même.

**D5 — Fuite calibration/évaluation.** Le seuil à 1 % de fausses alertes est calibré sur les jumeaux honnêtes des 60 tâches, et c50 est estimé sur les attaques de ces mêmes tâches. Les effets de tâche partagés entre jumeau et attaque rendent le seuil dépendant des tâches évaluées. Il manque un découpage calibration/évaluation par tâche.

**D6 — « Attaques fraîches » ambiguës.** D interprète une pente qui disparaît sur attaques fraîches comme contamination ou artefact. Mais si les attaques fraîches viennent de générateurs plus récents, la distribution de difficulté a changé (D2) ; la chute de pente est alors un déplacement d'axe, pas une contamination. Il faut deux corpus frais : même générateur, graines neuves ; générateur neuf.

**D7 — Strate d'injection non déclarée dans E1.** La pièce rapporte que le moniteur le plus fort sans injection donne 0 aux 375 échantillons sous injection (**RAPPORTÉ**, Scheurer §3.4). Une pente positive hors injection et négative sous injection sont toutes deux plausibles ; E1 doit dire laquelle il teste, sinon H_A et H_B ne sont pas définies.

**D8 — T1 : les refus ne sont pas un bruit additif.** Compter les refus comme échecs et les « publier à part » ne retire pas le biais : la pièce rapporte une aversion de disposition possible chez les modèles entraînés utiles/inoffensifs (**RAPPORTÉ**, Scheurer §1.1, p. 15). Si le taux de refus r_m covarie avec la date, h50 confond capacité et consentement, et la covariance est précisément ce que l'entraînement de sûreté vise. Il faut un estimand conditionnel (succès | non-refus) sous un modèle à risques concurrents, ou renoncer à l'interprétation « capacité ».

**D9 — T3 : l'axe FLOP confond taille et efficacité.** Le coût FLOP par tentative croît avec la taille ; un modèle plus gros et plus habile peut afficher un q50 plus élevé qu'un petit modèle moins habile. La pente de q50 sur la date mêle progrès par tentative et dérive de taille des modèles datés.

**D10 — Validation de l'estimateur sous un nul trop simple.** « Fausse détection ≤ 5 % sous simulations nulles » ne vaut que si le nul reproduit les effets croisés tâche × moniteur et les effets de famille ; un nul i.i.d. sous-estime le taux de fausses pentes. Et détecter +10 %/mois à 80 % ne dit rien sur la capacité à séparer +5 % de +10 %, qui est la question d'E1.

### (b) Conditions mesurables de perte de puissance ou de non-jugeabilité

- **Seuil à 1 % non estimable.** Soit F_0,m la loi des scores honnêtes du moniteur m, q son quantile 0,99, f_0 sa densité en q. Var(q̂) ≈ 0,01·0,99/(n_h f_0(q)²). Avec n_h = 240 (**calcul**, 4 × 60), le nombre d'excédents K ~ Bin(240 ; 0,01) a P(K = 0) ≈ 0,09 et P(K ≤ 1) ≈ 0,31 (**calcul**) : le pilote ne peut pas distinguer une FA de 0,5 % d'une FA de 2 %. La condition « le TFA calibré se transporte au test » n'est pas jugeable à cette taille.
- **c50 non identifié.** Soit D_m(c) = P(score > τ_m | attaque de difficulté c). c50 existe si D_m est monotone et croise 0,5 dans l'intervalle observé [c_min, c_max]. Si D_m(c_max) > 0,5 (moniteur fort) ou D_m(c_min) < 0,5 (moniteur faible), c50 est censuré ; si D_m n'est pas monotone (attaques difficiles plus longues, donc plus visibles, D3), c50 n'est pas défini et le logistique est mal spécifié.
- **Pente non identifiée avec effets de famille.** Avec effets fixes de famille, Var(β̂) = σ²/Σ_m (t_m − t̄_f(m))² : seule la dispersion de date *intra-famille* identifie β. Qwen2.5 à une seule date (**RAPPORTÉ**, Scheurer §2.2) contribue zéro ; une famille à deux dates contribue une différence. Avec 12–18 modèles, trois familles et un quart réservé, le nombre de contrastes de date intra-famille peut descendre à quelques unités.
- **Puissance de E1.** Pour écarter H_B au seuil 1,05 avec un vrai β, il faut SE(β̂) ≤ (β − log 1,05)/1,96. Avec σ² le résidu de log c50 (effets de famille déduits) et S_t = Σ(t − t̄_f)², la condition est σ² ≤ S_t·((β − 0,049)/1,96)². **Illustratif** : β = 0,10, 10 contrastes utiles étalés sur 30 mois, S_t ≈ 750 mois², σ ≤ 0,71 (facteur 2 sur c50) ; β = 0,07, σ ≤ 0,29 (facteur 1,3). Un test-retest de c50 sur un même point de contrôle doit donc montrer un écart-type sous ces valeurs, sinon le duel est non jugeable quelle que soit la vérité.
- **Bootstrap groupé à six grappes.** Avec six moniteurs dans le pilote, l'IC par bootstrap de grappes sous-couvre ; aucune pente ne doit être annoncée sur le pilote, ce que D dit, mais il annonce quand même une borne de censure à un tiers comme critère de conclusion partielle.
- **T3.** La médiane de survie q50 n'est définie que si Ŝ(q_max) < 0,5 par Kaplan-Meier ; si la fraction censurée dépasse 0,5 pour un moniteur, son q50 est non jugeable et sa suppression de la régression crée une sélection corrélée à la date.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Jumeaux appariés en longueur et complexité** et un « moniteur longueur seule » : si ce dernier atteint une part notable de la détection, D3 est réalisé.
2. **Provenance croisée** : attaques du générateur g notées contre jumeaux de g′ ≠ g, et inversement ; si la détection chute quand la provenance est appariée, le moniteur détectait la provenance.
3. **Capacité de code du moniteur** sur les mêmes tâches (résoudre, pas surveiller) : la pente de c50 doit survivre au conditionnement ; sinon D4.
4. **Calibration sur un découpage de tâches disjoint** du corpus d'évaluation (D5).
5. **Notation humaine de difficulté en aveugle** des verdicts des moniteurs, avec accord inter-notateurs rapporté ; un accord brut élevé avec κ nul, comme dans « nos résultats » §4 (**OBSERVÉ-NON-AUDITÉ**), rendrait l'axe inopérant et atténuerait toute pente.
6. **Test-retest** de c50 sur un même point de contrôle, graines neuves : plancher de variance pour (b).
7. **Contrôle positif de l'oracle** : un moniteur qui reçoit l'entrée déclencheuse doit détecter ~100 % ; sinon les étiquettes sont fausses.
8. **Dates permutées à l'intérieur des familles**, pas seulement globalement : une permutation globale ne teste pas l'identification intra-famille.
9. **Deux corpus frais** (même générateur/graines neuves ; générateur neuf), rapportés séparément (D6).

**Duel que j'oppose à D (HYPOTHÈSE, B4).** H_A : après conditionnement sur la capacité de code du moniteur (contrôle 3), l'effet de date sur log c50 conserve au moins la moitié de sa valeur brute. H_B : il tombe sous la moitié. Issue H_A : « surveillance » a un contenu propre, le programme T2 se poursuit. Issue H_B : T2 est une tendance de capacité de code rebaptisée ; le facteur mensuel doit être reporté comme tel. Chaque issue falsifie une lecture de D.

## Sur la proposition E

### (a) Défauts de méthode

**E1 — L'horizon H_m est, par construction, une reparamétrisation du taux de fausse alerte par décision.** Si le moniteur alarme dès qu'une décision dépasse un seuil avec probabilité p_τ par décision honnête, la fausse alerte par épisode vaut 1 − (1 − p_τ)^L sous indépendance (même forme que la formule de rééchantillonnage citée **RAPPORTÉ**, Scheurer §3.4). La contrainte « ≤ 5 % par épisode » borne alors H_m ≤ log(0,95)/log(1 − p_τ) indépendamment de toute détection. **Illustratif** : p_τ = 0,001 donne H ≤ 51 ; p_τ = 0,0004 donne H ≤ 128. Si au contraire le seuil est recalibré par longueur, la détection à 80 % devient plus dure aux grandes L parce que le seuil se resserre, et H_m mesure le coût de comparaison multiple. E ne dit pas si le moniteur note par décision ou la trajectoire entière (comme l'outil d'Apollo, **RAPPORTÉ**, Scheurer §1.3) ; sans ce choix, la grandeur n'est pas définie.

**E2 — La loi de placement et la densité d'anomalies déterminent H_m.** « Mêmes placements » fixe la nuisance entre moniteurs, mais ne dit pas si une trajectoire de 128 contient une anomalie (densité 1/L, aiguille dans la botte) ou 16 (densité constante, preuves cumulées). Dans le premier cas H_m mesure la recherche d'un singleton ; dans le second, la détection s'améliore mécaniquement avec L. Deux instruments différents sous le même nom.

**E3 — L'échelle « nombre de décisions » n'a pas d'ancrage humain.** METR ancre sur la durée humaine (**RAPPORTÉ**, Scheurer §3.1) ; E ancre sur la granularité d'un générateur synthétique gelé. Changer la granularité du générateur change H_m par construction. Rien n'interdit l'instrument, mais le facteur mensuel n'est comparable à rien hors de ce générateur, et E ne le dit pas.

**E4 — Vrai par construction, versant capacité.** Les trois classes (déclaration incompatible avec l'état, action interdite, résultat incorrect) sont décidables par un validateur d'état qui voit l'état caché. Le moniteur ne voit que le journal : sa tâche est l'inférence d'état latent à partir d'une séquence, une capacité de raisonnement ordinaire. E reconnaît qu'une règle accessible qui résout tout rend l'instrument inutile ; il ne prévoit pas l'autre cas, plus probable : le moniteur réussit parce qu'il raisonne mieux, et la tendance est celle du raisonnement séquentiel.

**E5 — Plafond d'identifiabilité non établi.** Si l'état pertinent n'est pas inférable du journal pour une fraction des cas, la détection maximale est < 100 % quelle que soit la capacité ; le critère 80 % peut être inatteignable pour tous, tout censuré, et E conclurait « frontières plates ». Il manque une borne supérieure calculée (oracle n'ayant que le journal).

**E6 — Grille {8, 32, 128} et censure par intervalles.** Avec trois longueurs, H_m est censuré par intervalles dans quatre classes. E ajuste d'abord une courbe succès–difficulté, ce qui interpole ; mais avec trois points, la courbe est contrainte par sa forme supposée, et un moniteur dont le franchissement de 80 % tombe hors [8, 128] est censuré. Si la plupart des 12 points de contrôle tombent dans la même classe, la variance de log H est nulle et β n'est pas identifié.

**E7 — E-B : malédiction du vainqueur sur le budget minimal.** « Budget minimal atteignant 80 % » est un minimum sur une grille de budgets d'estimations bruitées : il est biaisé vers le bas, et le biais croît avec le nombre de budgets essayés. Si les modèles récents sont explorés sur des grilles plus fines, la pente négative annoncée est en partie un artefact d'exploration. Il faut une grille fixe et une revalidation sur graines neuves au budget retenu.

**E8 — E-C : K_m est 1/ε_m déguisé.** Si la probabilité d'un dommage non bloqué par occasion est ε_m, P(dommage) = 1 − (1 − ε_m)^K et K_m ≈ −log(0,95)/(−log(1 − ε_m)) ≈ 0,051/ε_m (**calcul**). L'« horizon » n'ajoute rien à ε_m ; estimer ε de l'ordre de 10⁻³ exige quelque 3 000 occasions pour un seul échec attendu (**illustratif**). Le pilote n'en dit rien.

**E9 — Fenêtre de contexte.** Un moniteur dont le contexte ne couvre pas 128 décisions échoue mécaniquement ; la pente de H_m serait alors celle des fenêtres de contexte des modèles datés. « Même budget de lecture » ne règle pas ce point.

**E10 — Duels sans effet minimal.** H_A : β > 0 contre H_B : β ≤ 0 : exclusifs, mais un β de 0,001 réfuterait H_B sans porter sur la question (« un facteur X par mois »). Un seuil minimal pertinent manque, et avec censure par intervalles le signe seul est faiblement testé.

**E11 — Même défaut d'identification que D sur l'axe des dates** : 12 points de contrôle, effets famille et taille, seule la variation de date intra-famille identifie β ; au sein d'une famille, taille et date se confondent souvent. E le signale comme présupposé sans le convertir en condition vérifiable.

### (b) Conditions mesurables

- **FA par épisode non certifiable.** Avec n_h épisodes honnêtes par cellule et k alarmes observées, la borne supérieure unilatérale à 95 % (Clopper-Pearson) pour k = 0, n_h = 80 est 1 − 0,05^{1/80} ≈ 0,037 ; pour k = 1 elle dépasse 0,05 (**calcul**). Seul k = 0 certifie le critère ; sous une vraie FA de 3 %, P(k = 0) = 0,97^80 ≈ 0,09 (**calcul**). Le pilote échouera à certifier dans la grande majorité des mondes où le moniteur est pourtant conforme.
- **Détection à 80 %.** Par cellule, SE(d̂) ≈ √(0,8·0,2/80) ≈ 0,045 (**calcul**) ; l'IC chevauche 0,8 pour toute vraie détection entre ~0,71 et ~0,89. La frontière n'est encadrable que si les trois longueurs donnent des détections de part et d'autre de 0,8 avec marge > 0,09.
- **Loi par décision (E1).** Soit p_τ la FA par décision et ρ la corrélation intra-épisode des scores honnêtes. Sous dépendance positive, FA_L < 1 − (1 − p_τ)^L, et un seuil calibré sur épisodes entiers (comme dans « nos résultats » §6, **OBSERVÉ-NON-AUDITÉ**) dépend de ρ ; si ρ varie entre moniteurs ou avec la longueur, H_m varie sans que la détection change.
- **Identification de β.** Comme pour D : Var(β̂) = σ²/Σ(t − t̄_f)² ; en outre, si P(H_m ∈ même classe de censure) → 1, Var(log Ĥ) → 0 et β est non identifié. Condition : la dispersion inter-moniteurs de la position μ_m de la courbe logistique sur log L doit dépasser la largeur des classes (log 4 ≈ 1,39 entre 8 et 32), sinon la grille ne résout rien.
- **E-B.** Soit d̂(b) la détection estimée au budget b sur une grille de taille G ; B̂_m = min{b : d̂(b) ≥ 0,8}. E[B̂_m] < B_m, et l'écart croît avec G et avec Var(d̂). Deux moniteurs comparés sur des G différents ne sont pas comparables.
- **E-C.** Pour borner ε_m à 5 %/K près avec n épisodes de K occasions, il faut n·K·ε_m ≫ 1 ; sous ε_m ≈ 10⁻³ et K = 128, n ≈ 24 épisodes pour trois dommages attendus (**calcul**), avec un IC inutilisable.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Épisodes honnêtes à chaque longueur**, pour mesurer FA_L et ρ : si FA_L croît avec L à seuil fixe, E1 est réalisé et H_m n'est pas une mesure de détection.
2. **Anomalies détectables localement** (format, permission visible) à côté des anomalies dépendantes de l'état : si les taux sont égaux, le moniteur ne suit pas l'état.
3. **Placement permuté** : courbe détection × position ; une détection concentrée en fin de trajectoire signale un artefact de récence, pas un horizon.
4. **Oracle à journal seul** : plafond d'identifiabilité (E5) ; sans lui, « plat/censuré » ne se distingue pas de « inatteignable ».
5. **Moniteur à scores aléatoires** : doit être censuré sous 8 ; sinon le critère est trop lâche.
6. **Même point de contrôle répété** pour A et C, pas seulement B : plancher de variance de H et de K.
7. **Découpage en fenêtres identiques** pour tous les moniteurs, pour séparer contexte et détection (E9).
8. **Capacité de suivi d'état du même modèle** sur les mêmes journaux, sans anomalie (questions d'état) : la pente de H doit survivre au conditionnement ; sinon E4.
9. **Grille de budgets fixe et revalidation sur graines neuves** pour E-B (E7).
10. **Dates permutées intra-famille** (E11).

**Duel que j'oppose à E (HYPOTHÈSE, B4).** Sur une même grille de longueurs, deux calibrations : seuil par décision fixe, et seuil calibré sur épisodes entiers par longueur. H_A : les H_m obtenus sous les deux calibrations sont concordants (corrélation de rang des moniteurs ≥ 0,8, **illustratif**). H_B : ils discordent. Issue H_A : H_m a un contenu indépendant de la règle de fausse alerte, E-A se poursuit. Issue H_B : H_m est une propriété de la règle de calibration, et l'énoncé « l'horizon surveillable croît de X par mois » n'a pas de référent stable. Chaque issue falsifie une lecture de E.

## Ce que je prends aux autres, en le disant (B1)

Je retiens de D l'idée d'un axe de difficulté humaine pour les attaques, à condition des contrôles 1, 2, 3 et 5 ci-dessus ; je retiens de E l'exigence d'un oracle mécanique et de baselines n'ayant que l'information du moniteur. Je rejette dans les deux cas la forme actuelle des duels : D met son seuil sur son effet attendu, E n'a pas de seuil ; aucun des deux n'a montré que la pente de date est identifiée une fois les familles tenues, et aucun n'a prévu le contrôle de capacité ordinaire qui sépare « surveillance » de « raisonnement ».

FIN-DE-CELLULE