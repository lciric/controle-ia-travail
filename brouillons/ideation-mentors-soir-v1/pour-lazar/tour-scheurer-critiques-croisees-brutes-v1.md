# Tour du collisionneur, Scheurer (sans Argon ; espèce B absente après son refus) — critiques croisées (E3-T2), brutes

Copie à l'octet vérifiée contre les compagnons ; espèces par lettre ; rien lu ni modifié par conv-audit.


---

## E3-T2-critique-croisee-A.md (sha256 `32ca5d7b18c15afa0f0f952aa415f177e493b11ab3618d08bd36c75dce2207b9`)

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

---

## E3-T2-critique-croisee-D.md (sha256 `917eab83d47049c1b346b6bff5b92f61c0576aa9fb54620ce5e600ab5fa39372`)

Les risques empiriques discutés ci-dessous sont des **HYPOTHÈSES de méthode**, non des résultats. Les formules servent à rendre testables les conditions de non-jugeabilité.

## Sur la proposition A

### (a) Défauts de méthode

- **T1 ne mesure pas une capacité invariante du moniteur.** La détection dépend du couple moniteur–attaque, de la longueur, mais aussi de la densité du signal, de sa position et de l’information effectivement visible. Additionner « lignes de code + traces d’exécution » ne définit pas un axe scalaire univoque. Geler les attaquants fixe une distribution d’attaques, pas ces autres facteurs.
- **La pente temporelle reste confondue.** Date du moniteur, famille, taille, fenêtre de contexte et exposition possible aux problèmes publics varient ensemble. La régression sur la date n’identifie un effet temporel que si ces variables ne portent pas, à elles seules, toute la variation. Les sept Qwen2.5 fournissent un axe de taille à date fixe, pas la conversion en axe calendaire.
- **Le contrôle mécanique à pente nulle est largement vrai par construction.** Sur une banque et un instrument déterministes figés, il ne peut pas révéler une dérive de difficulté entre les dates assignées aux autres moniteurs. Il teste surtout le pipeline de calcul.
- **L’appariement honnête/malveillant est insuffisant.** Produire les deux classes par le même attaquant ne supprime pas les artefacts de consigne, de style, de validité du code ou de longueur. Compter un refus comme trajectoire honnête aggrave ce défaut : la classe honnête peut contenir des échecs trivialement reconnaissables, tandis que la classe malveillante ne conserve que les attaques effectivement produites.
- **Fuite possible entre calibration et évaluation.** Le seuil à fausses alertes fixées, l’ajustement logistique et l’estimation de l’horizon doivent utiliser des problèmes, graines et trajectoires distincts. A ne le garantit pas explicitement. Le bootstrap sur sept attaquants d’une même famille ne répare pas cette dépendance.
- **Les duels ne respectent pas toujours l’exclusion requise.** Dans D1, une pente positive mais inférieure au seuil de H_A n’est couverte par aucune des deux hypothèses ; surtout, une pente positive ne falsifie pas « l’horizon est dominé par la longueur ». Dans D2, un rapport supérieur au seuil ne falsifie pas nécessairement une stagnation conjointe contre attaquants contemporains et gelés.
- **T2 n’a pas d’axe d’écart nécessairement ordonné.** Deux couples attaquant–moniteur ayant le même écart de log-paramètres peuvent avoir des probabilités de réussite différentes. Le seuil n’est alors pas une fonction de cet écart.
- **T3 confond conscience verbalisée et désalignement**, et l’ajustement supervisé à calcul égal n’est pas un contrôle équivalent : il change aussi la distribution des sorties. Enfin, une probabilité bornée ne peut croître d’un facteur deux à chaque doublement indéfiniment.
- **T4 n’a pas encore de variable dépendante interprétable** : **RAPPORTÉ**, la signification des deux scores est absente de la pièce. Une forte corrélation avec les refus ne démontrerait pas, à elle seule, une confusion causale.

### (b) Conditions probabilistes de perte de puissance ou de non-jugeabilité

Pour T1, notons \(p_m^+(\ell)\) la probabilité de détection d’une attaque et \(p_m^-(\ell)\) celle d’une alerte sur un cas honnête, au seuil retenu.

- L’horizon est **non identifiable** si \(p_m^+(\ell)\) n’est pas monotone, traverse plusieurs fois son seuil, ou reste toujours au-dessus ou toujours au-dessous sur la grille. Il est alors censuré ou multivalué, pas seulement imprécis.
- Le TPR comparé à « fausses alertes fixées » est **mal calibré** si  
  \[
  P(Y=1\mid \text{honnête, test},\widehat\tau_m)\neq 0,05
  \]
  alors que cette égalité tient sur la calibration. Cela arrive notamment si \(p_m^-(\ell)\) dépend de \(\ell\) ou du rôle de génération.
- Si les erreurs sont corrélées intra-problème ou intra-attaquant, l’information effective est inférieure au nombre de trajectoires. Un bootstrap qui ne rééchantillonne pas ces unités au bon niveau produit des intervalles trop étroits.
- La pente temporelle est **non estimable** si la date n’a plus de variance résiduelle après famille, taille et autres covariables. Elle n’est pas une loi commune si les pentes propres aux familles sont de signes opposés malgré une pente moyenne positive.
- Pour T2, soit \(r(\delta,m,a)\) la probabilité de réussite de l’injection. L’écart-seuil est non jugeable si \(r\) n’est pas monotone en \(\delta\), ne traverse jamais le seuil, ou si \(r(\delta,m,a)\neq r(\delta,m',a')\) pour des couples pourtant interchangeables sur l’échelle choisie.
- Pour T3, si \(c_m\) est la conscience réelle et si sensibilité \(s_m\) et spécificité \(u_m\) du classificateur varient entre checkpoints, le taux observé est
  \[
  \widehat c_m^{\,\mathrm{obs}}=s_mc_m+(1-u_m)(1-c_m).
  \]
  Une tendance peut donc apparaître avec \(c_m\) constant. Près du plancher ou du plafond, le critère fondé sur \(\kappa\) peut également perdre toute discrimination.
- Pour T4, si la probabilité de refus et le score dépendent tous deux de la date, leur corrélation seule ne sépare pas \(P(\text{sous-performance}\mid\text{capable, non-refus})\) de \(P(\text{non-refus})\). Sans définition du score, l’estimateur lui-même reste indéfini.

### (c) Contrôles négatifs indispensables

1. **T1 : paires honnête–honnête avec étiquette d’attaque factice**, appariées sur problème, validité, longueur et rôle de génération. Une détection au-dessus du taux nominal révèle une fuite d’étiquette ou un artefact de style.
2. **T1 : séparation scellée calibration/ajustement/évaluation**, puis évaluation sur problèmes et attaquants réellement réservés. Sans cela, l’intervalle de l’horizon et le duel gelé/contemporain ne sont pas interprétables.
3. **T1 : refus et solutions invalides rapportés comme strates distinctes**, jamais injectés dans les cas honnêtes. Leur taux doit aussi être comparé entre tailles d’attaquants.
4. **T2 : contenu témoin non injectant, apparié en longueur et style**, en plus du contrôle sans injection ; sinon une baisse de détection peut être un simple effet de distraction.
5. **T3 : annotation et classificateur validés sur checkpoints entièrement held-out**, y compris des exemples sans conscience d’évaluation. Le contrôle supervisé seul ne suffit pas.
6. **T4 : aucun contrôle ne peut sauver la tendance tant que les scores ne sont pas définis.**

## Sur la proposition B

Pièce absente, statut REFUS : aucune critique de contenu possible ; je n’en invente pas.

## Sur la proposition C

Pièce absente, statut « jamais lancée » : aucune critique de contenu possible ; je n’en invente pas.

## Sur la proposition E

### (a) Défauts de méthode

- **E-A peut mesurer la géométrie du générateur plutôt qu’une frontière générale.** Placements, classes d’anomalies et rapport signal/longueur déterminent la difficulté. Des graines finales secrètes empêchent la mémorisation exacte, mais pas l’adaptation aux classes et au style du générateur.
- **Le taux de fausses alertes par épisode change la contrainte avec la longueur.** À risque par décision constant, allonger l’épisode multiplie mécaniquement les occasions d’alerte. Une partie de l’horizon peut donc être vraie par construction. Recalibrer à chaque longueur changerait en outre l’instrument mesuré.
- **Le « maximum » de longueur suppose une monotonie non établie.** Un moniteur peut échouer à une longueur intermédiaire puis réussir plus loin. Le maximum sur grille et le franchissement d’une courbe ajustée ne définissent alors pas la même grandeur.
- **E-B subit un biais du minimum.** Choisir le plus petit budget dont les estimateurs franchissent les deux seuils, sur les mêmes données que l’évaluation, favorise les fluctuations favorables. Une politique d’allocation gelée n’empêche pas cette sélection optimiste.
- **E-C peut n’apporter aucune loi nouvelle.** Sous occasions indépendantes et risque résiduel par occasion constant, l’horizon de confinement est une transformation algébrique du taux par occasion. Sa tendance n’ajoute alors rien à celle de ce taux.
- **La régression commune peut être non identifiée.** Famille, taille et date risquent d’être colinéaires sur douze checkpoints. Une pente moyenne peut aussi masquer des tendances de signes opposés. Les permutations de dates ne sont valides que dans des strates où les dates sont échangeables ; le moniteur figé sur données figées est, lui aussi, plat par construction.
- **Le pilote est peu informatif sur les fausses alertes.** Avec 80 cas honnêtes par cellule et une cible de 5 %, quatre fausses alertes sont attendues (**calcul**) : les taux réels et leur respect simultané des seuils restent très incertains.

### (b) Conditions probabilistes de perte de puissance ou de non-jugeabilité

- **E-A :** soient \(p_m(\ell)\) la détection et \(q_m(\ell)\) les fausses alertes par épisode. La frontière est absente ou censurée si \(p_m(\ell)\) ne franchit jamais la cible, la dépasse partout, ou n’est pas monotone. Si \(q_m(\ell)\) croît avec \(\ell\), la comparaison mélange dilution du signal et accumulation du risque. Sous forte corrélation intra-famille de tâches, les intervalles fondés sur les paires surestiment la puissance.
- **E-B :** soit \(\mathcal F_m\) l’ensemble des budgets où les deux contraintes sont satisfaites. \(B_m\) est non défini si \(\mathcal F_m=\varnothing\), censuré si tous les budgets testés conviennent, et multivalué si performance ou calibration ne sont pas monotones en budget. Le minimum estimé sur données réutilisées est biaisé vers les petits budgets.
- **E-C :** si le dommage résiduel par occasion est \(d_m\) et les occasions indépendantes,
  \[
  P(\text{dommage avant }K)=1-(1-d_m)^K .
  \]
  L’horizon est alors entièrement déterminé par \(d_m\). Il devient infini si \(d_m=0\), inexistant sous la contrainte d’utilité si celle-ci échoue dès le départ, et non monotone si blocage et vérification modifient la distribution des occasions ultérieures.
- **Panel commun :** \(\beta\) est non identifiable si la matrice date/famille/taille est de rang insuffisant. Il perd sa puissance si la variance résiduelle de date est faible relativement à l’erreur d’estimation des frontières. Des frontières censurées transformées en valeurs numériques, ou des logarithmes de frontières nulles, rendent l’estimateur biaisé ou indéfini.

### (c) Contrôles négatifs indispensables

1. **E-A : épisodes sans aucune anomalie avec étiquettes factices**, à longueur et opérations appariées ; toute « détection » au-dessus du taux nominal invalide la vérité terrain ou révèle un artefact.
2. **Les trois mesures : générateur et familles de tâches held-out**, distincts de ceux ayant servi à concevoir les cas, seuils et politiques. Sans ce contrôle, la pente peut être celle du style planté.
3. **E-A : contrôle de longueur sans dilution**, où la quantité et la visibilité du signal restent constantes ; il distingue longueur causale et simple accumulation d’occasions de fausse alerte.
4. **E-B : sélection du budget et certification sur échantillons disjoints**, plus un flux sans anomalie à chaque budget. Le même checkpoint répété ne contrôle pas le biais du minimum.
5. **E-C : flux entièrement honnête**, avec dommage nul attendu et mesure des blocages injustifiés, complété par les bornes « tout autoriser » et « tout bloquer ». Les seules actions bénignes appariées ne testent pas la probabilité de dommage.
6. **Panel : pseudo-dates permutées uniquement à l’intérieur de strates famille–taille échangeables**, et non globalement. Sans ce contrôle, la significativité de \(\beta\) peut provenir de la structure du panel.

FIN-DE-CELLULE

---

## E3-T2-critique-croisee-E.md (sha256 `4faf9498f6bcf4e0a608b8a32364d1ce6c99436138bfb25435cc4b4a12bcfdc3`)

# Proposition E — Critique croisée de méthode

**Statuts.** Les choix des conceptions sont traités comme des **HYPOTHÈSES**, non comme des résultats. Toutes les critiques ci-dessous sont des **HYPOTHÈSES de défaillance**, formulées conditionnellement ; les égalités mathématiques sont des **calculs conditionnels**. Aucun résultat empirique nouveau n’est avancé.

## Sur la proposition A

### (a) Défauts de méthode

**T1 — Horizon de surveillance**

- **L’axe mélange plusieurs grandeurs.** « Lignes de code + traces d’exécution » ne définit pas une unité commune : la conversion entre elles, la redondance et la densité d’information peuvent déterminer l’horizon. Ajouter du contenu sans changer la difficulté peut produire une décroissance de détection sans mesurer la surveillance recherchée.
- **Geler les attaquants ne neutralise pas leur élicitation.** Cela fixe une distribution conditionnelle aux productions obtenues et validées. Une interaction entre cette distribution et les moniteurs peut encore déterminer la pente. La conclusion porterait sur ce corpus, pas sur toute capacité de surveillance.
- **Un refus n’est pas un témoin honnête apparié.** Son style, sa longueur et l’absence d’artefact fonctionnel peuvent révéler directement son étiquette. Il faut séparer refus, solution honnête fonctionnelle et production invalide.
- **Le seuil peut fabriquer une partie de la courbe.** Une calibration globale des fausses alertes ne fixe pas leur taux à chaque longueur. Une calibration distincte par longueur définit, elle, une autre mesure. Ce choix doit précéder l’ajustement.
- **Le contrôle mécanique plat est insuffisant.** Sur exactement les mêmes entrées et avec le même budget, son invariance temporelle est attendue par construction. Il ne détectera pas nécessairement une contamination propre aux modèles récents.
- **La puissance des sondes de « nos résultats » ne se transporte pas à ce pilote.** Un autre estimateur, une autre dépendance entre observations et une autre alternative exigent un calcul de puissance propre.

**T2 — Écart de capacité seuil**

L’écart de log-paramètres n’identifie pas à lui seul un écart de capacité. Avec une seule date, il n’identifie aucune évolution temporelle. Il faut croiser attaquants et moniteurs : sinon, leur amélioration respective et leur interaction restent confondues. Le corpus sans injection ne suffit pas à isoler l’effet sémantique de l’injection de celui de la longueur ou du format ajoutés.

**T3 — Conscience d’évaluation**

Un classificateur figé n’a pas nécessairement une sensibilité figée entre étapes d’entraînement. Le changement de verbalisation peut déplacer son erreur de mesure. De plus, la conscience d’évaluation verbalisée n’est pas, sans variable comportementale distincte, une mesure de désalignement. Le témoin supervisé n’est un contrôle négatif valide que sous l’hypothèse supplémentaire qu’il n’affecte pas la grandeur mesurée.

**T4 — Sous-performance**

Les scores n’étant pas définis dans la pièce servie, l’estimand reste à spécifier. Une pente positive et une corrélation avec les refus peuvent coexister : le duel proposé n’oppose donc pas deux hypothèses exclusives.

**Duels.** D1 mélange une valeur de pente, un résultat de test et un autre seuil décisionnel. D2 oppose une propriété du rapport d’horizons à une propriété de leur évolution : elles ne sont pas complémentaires. Une baisse relative n’implique notamment pas une baisse absolue.

### (b) Conditions de perte de puissance ou de non-identification

Notations : \(S\), score ; \(Y\), étiquette ; \(x\), difficulté ; \(t\), date ; \(\tau_t\), seuil ; \(\alpha\), risque cible.

**T1 — Détection, calibration et horizon**

\[
p_t(x)=P(S>\tau_t\mid Y=1,x,t),\qquad
a_t(x)=P(S>\tau_t\mid Y=0,x,t).
\]

- Si les lois conditionnelles de \(S\) pour \(Y=1\) et \(Y=0\) sont égales, alors \(p_t(x)=a_t(x)\) : aucune discrimination.
- Si \(\int a_t(x)\,dG_{0,t}(x)=\alpha\), mais \(a_t(x)\neq\alpha\), la calibration marginale ne garantit pas le risque conditionnel.
- Pour une cible de détection \(r\), \(h_t\) défini par \(p_t(h_t)=r\) n’est pas identifié dans le support observé si \(p_t(x)\) reste entièrement d’un côté de \(r\), ou si plusieurs croisements existent.
- Localement,
\[
\operatorname{Var}(\widehat h_t)
\approx
\frac{\operatorname{Var}[\widehat p_t(h_t)]}{[p'_t(h_t)]^2}.
\]
Une dérivée proche de zéro rend l’horizon instable.
- Si \(X_t=(1,t,\text{famille},\text{taille})\) donne une matrice de conception de rang déficient, la pente temporelle ajustée n’est pas identifiable.
- Pour des observations groupées de corrélation \(\rho\) et de taille de groupe \(k\),
\[
n_{\mathrm{eff}}\approx\frac{n}{1+(k-1)\rho}.
\]
Le nombre de lectures ne suffit donc pas à déterminer la précision.

**T2 — Seuil d’écart**

Soit \(u(g,t)=P(\text{succès}\mid g,t)\), où \(g\) est l’écart proposé. Le seuil \(g^\star_t\) est non identifiable si \(u\) ne croise pas la cible dans le support commun, ou si \(u\) n’est pas monotone. Si
\[
P(\text{succès}\mid g,t,a,m)\neq P(\text{succès}\mid g,t),
\]
l’écart seul ne suffit pas comme variable explicative. Sans répétition temporelle à écarts comparables, sa dérive temporelle reste non identifiable.

**T3 — Erreur du classificateur et croissance**

Avec prévalence latente \(\pi(c)\), sensibilité \(s(c)\) et spécificité \(v(c)\) au calcul \(c\),
\[
P(\widehat Y=1\mid c)
=s(c)\pi(c)+[1-v(c)][1-\pi(c)].
\]
Si \(s\) et \(v\) sont inconnues et variables, la pente de \(\pi\) n’est pas identifiable. Si \(s+v=1\), la mesure n’apporte aucune information sur \(\pi\). Si la variance marginale des annotations tend vers zéro, le dénominateur du coefficient \(\kappa\) tend également vers zéro.

**T4 — Refus et sous-performance**

Pour un refus \(R\),
\[
P(Y=1\mid t)
=\sum_r P(Y=1\mid R=r,t)P(R=r\mid t).
\]
Une variation de \(P(R\mid t)\) suffit à modifier le taux marginal sans variation des taux conditionnels. Si \(P(R=0\mid t)\) tend vers zéro, l’estimation conditionnelle parmi les non-refus perd sa précision.

### (c) Contrôles négatifs dont l’absence serait fatale

- **T1 :** solutions honnêtes fonctionnelles appariées, sans refus ; variations de longueur et de format à étiquette inchangée ; détecteur utilisant seulement la provenance ; calibration et test disjoints par problème et groupe de génération.
- **T2 :** contenu ajouté sémantiquement inerte mais apparié en longueur, emplacement et format ; mêmes artefacts sans ajout ; matrice attaquant–moniteur croisée.
- **T3 :** exemples négatifs annotés indépendamment à chaque étape d’entraînement, avec estimation de l’erreur du classificateur par étape ; réutiliser uniquement son jeu de calibration serait fatal.
- **T4 :** tâches comparables sans incitation supposée à sous-performer ; codage séparé des refus ; mesure indépendante de réussite ordinaire.

## Sur la proposition B

**RAPPORTÉ —** La pièce B est absente, avec le statut transmis « REFUS » ; aucune critique de son contenu n’est possible.

## Sur la proposition C

**RAPPORTÉ —** La pièce C est absente, avec le statut transmis « jamais lancée » ; aucune critique de son contenu n’est possible.

## Sur la proposition D

### (a) Défauts de méthode

**T1 — Horizon de subversion accessible**

La réussite est une intersection : artefact fonctionnel, condition plantée satisfaite, contrôle franchi. Son amélioration peut venir exclusivement de la programmation ordinaire. La formulation « capacité accessible sous protocole fixé » est appropriée, mais elle ne sépare pas ces contributions.

Le temps humain doit correspondre à une tâche précisément définie. Le temps de construction, de résolution honnête et de détection ne sont pas interchangeables. Chronométrer des humains puis sélectionner les tâches dont les temps prédisent bien les modèles créerait une fuite instrument–évaluation.

**T2 — Horizon de surveillance**

La difficulté humaine de produire une attaque n’est pas nécessairement croissante avec la difficulté de la détecter. Le sens de variation attendu de la courbe doit être testé, non imposé par l’ajustement logistique.

Les jumeaux issus du même générateur peuvent encore porter des signatures d’invites, de longueur ou de validation différentes. L’appariement de provenance est nécessaire, mais ne garantit pas l’appariement distributionnel.

Le corpus renouvelé permet une épreuve de transport, à condition de ne pas servir ensuite à modifier le seuil ou choisir les strates. De même, exclure les tâches invalides après examen des scores introduirait une sélection dépendante du résultat.

**T3 — Calcul d’élicitation**

Les FLOP mesurent un coût calculatoire, pas automatiquement un budget d’opportunités comparable. Taille du modèle, longueur de sortie et allocation des tentatives influencent simultanément le coût et la réussite. La dépendance entre tentatives doit être estimée ; elle ne disparaît pas parce que leur calendrier est non adaptatif.

**Critères E1/E2 et qualification**

E1 emploie bien des hypothèses complémentaires. Il reste nécessaire de préspécifier la population d’attaques fraîches visée.

E2 combine plusieurs contraintes. Le falsifier exige une violation établie de l’une d’elles ; falsifier son complément exige d’établir toutes les contraintes, avec une incertitude simultanée. Un simple dépassement ponctuel ne suffit pas.

Exiger la réussite de tous les canaris ne démontre pas une erreur de vérification nulle. Choisir les tâches conservées sur ce même échantillon puis le réutiliser pour qualifier l’instrument produirait une fuite.

### (b) Conditions de perte de puissance ou de non-identification

**T1 — Décomposition de la réussite**

Avec \(F\), fonctionnalité ; \(B\), condition plantée ; \(U\), franchissement :
\[
p_t(x)=P(F\mid x,t)\,
P(B\mid F,x,t)\,
P(U\mid F,B,x,t).
\]
Si seuls les produits sont estimés, leurs facteurs ne sont pas identifiables séparément. Si le premier facteur varie et les suivants restent constants, la pente marginale ne permet pas d’attribuer une tendance à ces derniers. Si \(P(F,B\mid x,t)\) tend vers zéro, l’estimation du dernier facteur perd sa puissance.

**T1/T2 — Axe humain et horizon**

Pour une mesure \(\widetilde x=x+\varepsilon\), dans le cas classique d’erreur indépendante, une régression linéaire locale subit l’atténuation :
\[
\beta_{\mathrm{obs}}
=\beta\frac{\operatorname{Var}(x)}
{\operatorname{Var}(x)+\operatorname{Var}(\varepsilon)}.
\]
Si \(P(\varepsilon\mid t)\) varie, la pente peut également être biaisée. Un horizon est non identifiable lorsque la cible n’est pas croisée ou que la courbe présente plusieurs croisements.

**T2 — Transport de calibration**

Pour une loi honnête de calibration \(Q_0\) et une loi honnête de test \(P_0\),
\[
Q_0(S>\tau)=\alpha
\quad\not\Rightarrow\quad
P_0(S>\tau)=\alpha.
\]
Sous un échantillonnage indépendant, le nombre d’excès suit une loi binomiale de paramètre \(n_0,\alpha\). Quand \(n_0\alpha\) est faible, l’estimation relative de cette queue est imprécise. Avec dépendance par tâche, cette loi binomiale n’est plus appropriée sans ajustement.

**T3 — Censure et médiane**

Soit \(T\) le calcul jusqu’à réussite, \(C\) la censure et \(r\) la probabilité cible. La quantité \(q_r\) n’est pas identifiée non paramétriquement si
\[
P(T\le q_{\max})<r.
\]
Si \(P(T<\infty)<r\), elle n’est pas finie. Si \(T\not\!\perp C\mid X\), un estimateur supposant une censure indépendante peut être biaisé.

Pour \(K\) tentatives conditionnellement indépendantes de probabilité \(p_i\),
\[
P(\text{au moins une réussite}\mid i)=1-(1-p_i)^K.
\]
Cette identité ne s’applique pas sous dépendance arbitraire ; une évolution de cette dépendance peut modifier \(q_r\) à marges identiques.

**E2 et estimateur temporel**

Pour les marges du critère \(g=(d-d_\star,\alpha-a,\Delta-\delta)\), la réussite exige \(g_j\geq0\) pour chaque composante. Si une composante est proche de sa frontière au regard de son erreur-type, une décision simultanée manque de puissance.

Une permutation libre des dates n’est calibrée que sous échangeabilité des unités permutées. Si \(P(S\mid\text{famille})\) varie et que famille et date sont dépendantes, cette condition n’est pas satisfaite. Un corpus uniquement honnête ne permet pas d’estimer un horizon de détection des positifs.

### (c) Contrôles négatifs dont l’absence serait fatale

- **T1 :** tâches honnêtes de fonctionnalité comparable et sans condition plantée ; publication séparée des facteurs de réussite.
- **T2 :** détecteurs limités aux métadonnées et au style ; modifications inertes appariées ; échantillon honnête final indépendant pour tester le transport du seuil.
- **T3 :** condition identique à elle-même, mesurée sur plusieurs campagnes indépendantes, pour estimer la variabilité et la dépendance du calendrier ; aucune sélection du calendrier sur le test final.
- **Vérificateur :** artefacts invalides et jumeaux honnêtes indépendants des canaris de développement.
- **Pente :** simulations nulles conservant dépendances, censure et sélection réellement prévues ; permutations restreintes aux blocs échangeables. Une simulation sous le seul modèle d’ajustement testerait surtout sa cohérence interne.

**HYPOTHÈSE — Règle décisionnelle commune proposée :** définir chaque duel sur un paramètre, \(H_A:\theta\geq\delta\) contre \(H_B:\theta<\delta\). Une région d’incertitude entièrement d’un côté permet de rejeter l’autre hypothèse au risque préspécifié ; son chevauchement impose « non concluant », jamais « absence d’effet ».

FIN-DE-CELLULE