# Proposition B, tour III.2 : critique croisée de méthode

## Notes d'intégrité

- Le bloc FAITS reproduit la question de l'arbitre et ne contient aucun fait porteur de statut. Toute affirmation de fond ci-dessous est donc une HYPOTHÈSE ou un calcul conditionnel aux hypothèses qu'il énonce.
- Les pièces A, C, D et E semblent complètes : chacune se termine par sa ligne de fin. Je n'ai pas recalculé les empreintes.
- Ma propre conception du tour III.1 n'est pas transmise ici ; je ne m'y réfère pas.
- Je ne modifie aucun statut attribué par les autres propositions. Quand un statut VÉRIFIÉ ne repose sur aucune pièce transmise, je le signale sans le changer.
- Tous les nombres que j'introduis sont illustratifs, sauf mention contraire.

---

## Sur la proposition A

### (a) Défauts de méthode

1. **Le contrôle positif est confondu avec l'hypothèse testée.**
   - A exige que le pantin rende β = 0,5 ± 0,1 ; sinon, il déclare le pipeline biaisé.
   - Or le pantin injecte ses écarts dans des trajectoires dont le bruit est l'erreur honnête réelle du modèle. Si ce bruit est corrélé au sein d'une trajectoire, β s'écarte de 0,5 même avec un pipeline correct.
   - C'est exactement H_B de E1. Un échec du contrôle positif est donc ininterprétable : A arrêterait l'étude au moment où elle trouve son résultat.

2. **D_max n'est pas estimable dans les régimes non scriptés.**
   - D_max(T) est défini en prenant, pour chaque T, le k le plus favorable à l'adversaire. Mais en régimes consigne et affiné, k et d sont choisis par le modèle : ce sont des issues, pas des leviers.
   - Conditionner sur le D réalisé revient à sélectionner sur une variable aval.
   - Seul le pantin permet de balayer k, et il est sans valeur pour les activations.
   - Si la grille de k est fixe et bornée indépendamment de T, β est tronqué par construction aux grandes longueurs.

3. **Le signal d'état est vrai par construction de l'échafaudage.**
   - A le reconnaît en (d) : le déclencheur ou la consigne réapparaît à chaque appel. Une sonde qui lit « déclencheur présent dans le contexte » produit un signal stationnaire à chaque action, d'où d′ ∝ √T_eff, sans qu'aucune intention persistante soit représentée.
   - Le contrôle par sac de mots ne suffit pas. L'adaptateur a été entraîné avec les deux déclencheurs de sabotage et peut les projeter sur un même trait interne. La sonde battrait alors le sac de mots tout en ne lisant que la présence d'un déclencheur.
   - Le transfert vers le déclencheur 2 n'est « non vu » que pour la sonde, pas pour l'adaptateur.

4. **La longueur est confondue avec le volume de contenu.** Faire varier T de 50 à 800 fiches change aussi la taille de l'état résumé et le nombre d'occasions d'erreur honnête. La forme de σ(T) n'est pas mesurée séparément.

5. **E3 compare des variantes qui diffèrent aussi en difficulté.** Les variantes série et additive ont des taux d'erreur honnête et des D* différents, sans appariement.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Non-stationnarité de la variance.** Si Var(X_t) dépend de t, l'estimateur vaut β̂ = 1/2 + d ln σ_T / d ln T (calcul sous le modèle de A). La pente de σ_T se lit alors comme une violation d'indépendance.
- **Courbure du log-log.** Si la corrélation intra-trajectoire ρ satisfait ρT ≈ 1 dans la plage étudiée (par exemple ρ ≈ 1/200, illustratif), la courbe log-log est courbe. Une pente unique est mal spécifiée : un intervalle bootstrap étroit peut tomber dans une zone par artefact. Sans test de linéarité préenregistré, E1 n'est pas jugeable.
- **Queues lourdes.** Si l'erreur honnête par action a des queues de type α-stable d'indice a < 2, la somme croît en T^{1/a}. Alors β ≠ 1/2 malgré l'indépendance, et le pantin échoue pour une raison qui ne tient pas au pipeline.
- **Précision sur β.** Avec cinq longueurs couvrant ln 16 ≈ 2,77, on a SE(β) ≈ 0,46 ε, où ε est l'erreur relative sur chaque D_max (calcul illustratif).
  - Un intervalle à 90 % de largeur 0,30, nécessaire pour tenir dans [0,35 ; 0,65], exige ε ≤ 0,2 environ.
  - Avec 30 trajectoires par cellule, l'erreur-type du taux de détection autour de 0,5 vaut environ 0,09 (illustratif). La valeur de ε dépend de la pente de la courbe dose-réponse, qui n'est pas spécifiée.
- **Calibration des seuils.** Avec 100 trajectoires honnêtes par longueur, le quantile à 5 % repose sur environ 5 points de queue. Le taux réel de fausses alertes peut alors varier du simple au double (illustratif).
- **Biais honnête directionnel.** Si l'erreur honnête a une moyenne μ_h ≠ 0 dans la direction nuisible, la somme signée de l'audit exige d'estimer μ_h sur n exécutions de comparaison. L'erreur-type vaut σ_entre/√n et ne décroît pas avec T, ce qui crée un plancher de puissance indépendant de f.
- **Unité statistique en E2.** L'AUROC par action est calculée sur des actions dépendantes. Les seuils 0,70 et 0,55 ne sont jugeables qu'avec un bootstrap par trajectoire.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Indice retiré après la première action.** Le déclencheur n'apparaît qu'au premier appel, puis disparaît de l'état résumé. Si la sonde perd son signal, elle lisait l'indice contextuel et non un état d'intention.
2. **Adaptateur neutre au même déclencheur.** Un LoRA de même rang associe le déclencheur à un comportement inoffensif mais distinct, par exemple un changement de format. Si la sonde s'y déclenche, elle détecte le déclenchement et non le sabotage.
3. **Pantin sur bruit i.i.d. synthétique**, en plus du pantin sur traces honnêtes réelles. C'est la seule façon de séparer un biais du pipeline d'une corrélation honnête.
4. **Permutation de l'ordre des actions** dans chaque trajectoire, pour attribuer ou non le plafonnement de d′ à ρ.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **L'adaptateur est confondu avec l'intention.**
   - Les trois adversaires sont des LoRA ; l'agent honnête est le modèle de base.
   - Une sonde, et a fortiori un CUSUM, peut séparer « adaptateur présent » de « adaptateur absent » par une signature de poids constante à chaque action.
   - Cette signature a par construction une amplitude Ω(1) stationnaire : H_1B, qui prédit une croissance en √T, est alors vraie sans aucune intention.
   - Le transfert « hors domaine » depuis T = 10 n'y change rien, puisque le même adaptateur est présent aux deux longueurs.

2. **La sélection sur l'issue varie avec T.**
   - Les trajectoires honnêtes sont filtrées pour Δ ∈ [25 % ; 35 %]. Cette fenêtre correspond à une fraction de la loi honnête qui change avec T.
   - La population de comparaison change donc de composition d'une longueur à l'autre. De plus, un échec honnête modéré provient plutôt d'erreurs concentrées, alors que l'adversaire diffus est contraint à répartir les siennes. Le détecteur peut apprendre « diffus contre concentré » et non « sabotage contre bonne foi ».

3. **La furtivité est définie par une statistique particulière.**
   - La contrainte « KL par étape ≤ 90e centile honnête » rend « aucun acte suspect » vrai pour cette seule statistique.
   - Elle tend aussi à concentrer les étapes adverses juste sous le 90e centile. Un détecteur qui compte la fraction d'étapes au-dessus du 80e centile les repèrerait sans mémoire séquentielle. La prémisse n'est pas vérifiée en loi, seulement en seuil.

4. **L'expérience 2 est en partie tautologique.**
   - Une trajectoire dont la conclusion diffère de Δ ≥ 30 % diverge par construction des exécutions de comparaison. La question est seulement où elle diverge.
   - Or ces exécutions sont générées avec un ordre de documents permuté. La divergence due à la permutation est donc confondue avec la bifurcation adverse.

5. **L'expérience 3 utilise l'instrument d'évaluation comme cible d'entraînement.** L'adversaire est pénalisé sur le sous-espace des sondes, puis évalué par des « sondes orthogonales » dont la référence n'est pas définie. Si les sondes ne sont pas réentraînées après adaptation, H_3B est favorisée par construction. Si elles le sont, il ne s'agit que d'un tour de la course.

6. **Statuts.** O(km/T), Wald (1945) et la taille du modèle sont marqués VÉRIFIÉ alors qu'aucune pièce transmise ne les porte. Je ne change pas ces statuts. L'année de Greenblatt et al. diffère entre A (2023) et C, D, E (2024) : à vérifier.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Effet plafond.** Si l'AUROC à T = 50 dépasse 0,90, ΔAUROC ≥ +0,10 est impossible et H_1B ne peut pas être validée.
- **Autocorrélation des projections honnêtes.** Si la projection honnête suit un processus autocorrélé de coefficient φ > 0, la durée moyenne avant fausse alerte du CUSUM diminue d'un facteur proche de (1−φ)/(1+φ) (approximation, HYPOTHÈSE). Des seuils calibrés à T = 50 ne contrôlent alors plus les fausses alertes à T = 400, sauf recalibration par longueur.
- **Signal d'acte plutôt que d'état.** Si la composante de sonde suit le biais textuel, avec un écart moyen μ_t ∝ Δ/T, le rapport signal sur bruit du CUSUM décroît en Δ/√T. C'est la condition sous laquelle H_1A gagne. Il faut donc mesurer μ_t en fonction de T, et pas seulement l'AUROC.
- **Loi de classement de l'audit guidé.** Soit F̄_h la fonction de survie du score de divergence honnête par étape et j* le score de l'étape adverse. Recall@k reste stable seulement si T·F̄_h(j*) = O(k). Avec des queues en puissance, F̄_h(x) ∝ x^{−a}, le nombre d'étapes honnêtes qui devancent l'étape adverse croît linéairement en T, et l'audit guidé retombe vers l'aléatoire.
- **Masse honnête insuffisante.** Si la loi honnête de Δ à T = 400 a peu de masse dans [25 % ; 35 %], les 150 cas appariés sont inatteignables ou fortement sélectionnés. Le critère n'est alors pas jugeable.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **LoRA honnête de même rang**, entraîné sur un objectif bénin, comme bras honnête de toutes les expériences.
2. **Adaptateur adverse dormant.** Mêmes poids, sabotage non activé. Si la sonde s'y déclenche, elle lit les poids.
3. **Test de loi sur les écarts par étape.** Comparaison des lois complètes (et non d'un centile) des déviations par étape, honnêtes contre adverses, par exemple par un test de Kolmogorov-Smirnov.
4. **Divergence honnête contre honnête** avec le même schéma de permutation des documents, pour calibrer le score de bifurcation.
5. **Sondes réentraînées après l'adaptation** de l'expérience 3, sur données disjointes de celles de l'entraînement adverse.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Fuite dans le duel « information du défenseur seul ».**
   - D réserve les données du générateur au jugement final, puis révèle au moniteur l'appariement entre affirmation et témoin.
   - Si les liens révélés concernent les affirmations décisives, leur seule existence indique au moniteur où regarder : c'est une information de vérité absente en déploiement.
   - Le contrôle proposé (liens de même fréquence entre fiches non décisives) ne lève pas cette fuite si le moniteur peut distinguer les deux classes de liens.

2. **La variante T change la capacité de l'adversaire, pas seulement l'information du défenseur.**
   - Des témoins qui contraignent les affirmations décisives rendent la falsification plus difficile et réduisent aussi les erreurs honnêtes. R_C − R_T > δ peut donc venir d'une baisse de capacité de l'agent.
   - D le voit et publie P(conclusion fausse) avant audit, plus le troisième duel. J'utilise ce découpage comme repère pour les autres propositions.
   - Mais seul le troisième duel isole le défenseur, et c'est lui qui porte la fuite du point 1.

3. **Le duel « occasions » dépend de la stratégie de l'adversaire.** Un agent de 8 milliards de paramètres sous mandat textuel peut ne pas exploiter les fiches ajoutées. H_B (R_O − R_C ≤ δ) serait alors corroborée par une incapacité, non par l'absence d'effet de la longueur. Aucun adversaire forcé n'est prévu.

4. **L'appariement peut être perdu.**
   - Le mandat est tiré au sort « sur chaque variante ». Si ce tirage est indépendant entre variantes, seule une fraction d'environ 1/4 des dossiers est adverse à la fois en C et en O, soit environ 75 sur 300 (calcul sous indépendance).
   - L'intervalle apparié par dossier repose alors sur cet effectif. Le texte ne précise pas lequel des deux tirages est prévu.

5. **Le mandat reste dans le contexte des activations.** Exclure les jetons du mandat des entrées inspectées ne les retire pas du contexte que lisent les activations ultérieures. D prévoit le contrôle « mandat sans dommage » ; c'est la bonne parade, à condition qu'elle soit obligatoire.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Borne par la capacité adverse.** On a R_v ≤ P(conclusion fausse | adverse, v). Si cette probabilité est inférieure à δ, H_A est inatteignable par construction. Il faut le déclarer comme issue non jugeable, et non comme corroboration de H_B.
- **Puissance du test apparié.** La variance de l'écart apparié vaut (p₁₀ + p₀₁ − (p₁₀ − p₀₁)²)/n, où p₁₀ et p₀₁ sont les probabilités de paires discordantes. Avec n ≈ 75 dossiers concordants et p₁₀ + p₀₁ ≈ 0,3, la demi-largeur à 95 % vaut environ 0,12 (illustratif), soit plus de deux fois δ. Tous les duels seraient alors indéterminés.
- **Calibration et composition honnête.** Soient q_v la fraction de tâches honnêtes fausses dans la variante v et s le taux d'alerte du détecteur sur ces tâches. On a FPR ≥ s·q_v. Si q_T < q_C, le seuil peut être abaissé en T à cible de fausses alertes égale, ce qui produit un gain apparent dû à la seule composition honnête.
- **Audit à deux inspections.** Soient L_v le nombre d'actions et F̄_h la survie du score honnête. Le ciblage reste efficace seulement si L_v·F̄_h(s*) = O(2), où s* est le score de l'action défectueuse. Passer de 64 à 256 actions multiplie par quatre le nombre de concurrents honnêtes.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Révélation à taux égal.** Les liens sont révélés à la même fréquence entre affirmations décisives et non décisives, et le moniteur ne sait pas lesquelles sont décisives.
2. **Adversaire scripté en variante O.** Des défauts sont injectés sur les fiches ajoutées, pour vérifier que les occasions sont exploitables. Sans ce contrôle, un résultat nul en O n'est pas interprétable.
3. **Tirage du mandat commun aux trois variantes** pour chaque dossier, ou effectif concordant déclaré avant le test.
4. **« Mandat sans dommage »** rendu obligatoire pour tout gain attribué aux activations.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **H_1B est fausse par construction pour la statistique centrée.**
   - E pose que d_t est une différence de martingale sous π_hon. Si l'espérance conditionnelle est exacte, la dérive auto-renforçante honnête vit dans h_t et d_t reste centré.
   - H_1B (« dérive honnête indiscernable ») ne peut alors pas être vraie pour cette statistique. Le duel 1 ne teste que l'erreur d'estimation de l'espérance conditionnelle et la part non centrée (sonde, texte brut).

2. **Le centrage contredit l'hypothèse 4 de E.**
   - Calculer E_{π_hon}[Y | h] suppose de disposer d'une politique honnête de confiance aussi capable que l'agent.
   - Or E écrit en (a)4 que, dans ce cas, exécuter l'agent suspect devient redondant. Si l'on ré-échantillonne au contraire le modèle suspect, le centrage se fait sous la politique adverse et le signal s'annule.
   - La source des ré-échantillonnages n'est pas fixée.

3. **Les distracteurs créent une asymétrie de conception.** Les erreurs honnêtes sont produites par des « distracteurs calibrés ». Si ces distracteurs ne sont présents que dans les trajectoires honnêtes, tout détecteur peut apprendre leur présence.

4. **Le contrôle « greffe honnête » est mal apparié.** Les k erreurs adverses portent sur des nœuds à fort levier ; les k erreurs honnêtes sont tirées d'exécutions bruyantes, sans contrainte de levier. Les dossiers aval ne sont donc pas dégradés de la même façon.

5. **Le contrôle négatif du duel 3 n'a pas de critère.** Le remplacement des comparaisons par des ré-échantillonnages adverses « quantifie la perte » sans valeur attendue ni règle d'échec. C'est une analyse de sensibilité, pas un contrôle.

6. **La longueur est confondue avec la profondeur.** T varie avec la taille du corpus et le nombre de maillons d'inférence, donc avec la difficulté. L'appariement sur Δ ∈ [0,20 ; 0,35] retombe dans le problème de sélection signalé pour C.

7. **Statuts.** Les formules de divergence de Kullback-Leibler sont marquées VÉRIFIÉ. Ce sont des dérivations internes au modèle gaussien de E, non des faits transmis. Je ne change pas ce statut.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Composante textuelle centrée.** Pour cette composante, la puissance dépend de Σ_t δ_t² / Var(d_t), où δ_t est la dérive conditionnelle sous l'adversaire. Pour un sabotage diffus, δ_t ∝ Δ/T, donc la somme est ∝ Δ²/T et décroît. C'est la formule de E elle-même.
  - La croissance prédite par H_1A exige donc une composante de sonde dont δ_t ne décroît pas en 1/T. Sinon H_1A est réfutée mécaniquement, et cela devrait être dit avant le test.
- **Coût et biais de l'estimation.** Estimer Y par M déroulés jusqu'au terme depuis chaque étape coûte de l'ordre de M·T²/2 actions par trajectoire. Avec M = 4 et T = 300, cela fait environ 180 000 actions contre 300 (illustratif), ce qui est incompatible avec les 60 heures-GPU prévues.
  - Tout raccourci (modèle de valeur, déroulés tronqués) biaise l'espérance estimée et détruit la propriété de martingale, donc le contrôle des fausses alertes.
  - Sans raccourci, la variance ajoutée vaut 2σ_Y²/M par étape. Si elle domine δ_t², la puissance disparaît.
- **Cohérence interne de l'adversaire parcimonieux.** Dans le modèle de E, k ≥ Δ/ε. Avec Δ ≥ 0,25 et k ≤ 3, chaque acte doit avoir un effet ε ≥ 0,083 sur l'échelle de qualité. La furtivité exige alors que la loi honnête des effets par étape ait une masse non négligeable au-delà de 0,083. C'est une condition mesurable, mais non vérifiée.
- **Scan sur fenêtre courte.** Sous H₀ et sous indépendance gaussienne approchée, le maximum de T fenêtres croît en σ_w·√(2 ln T). De T = 40 à T = 300, le seuil monte d'environ 0,66 σ_w (calcul illustratif). H_2B (ΔTPR ≥ −0,02) exige un décalage par fenêtre nettement supérieur à cette hausse.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Distracteurs présents en proportion égale** dans les deux bras.
2. **LoRA honnête de même rang** dans les duels 1 et 2. E le prévoit en (c) pour les activations, mais pas dans les duels.
3. **Centrage par ré-échantillonnage du modèle suspect** contre centrage par π_hon, avec la prédiction explicite que le premier annule le signal. C'est le test de la circularité.
4. **Greffe honnête sur nœuds à fort levier**, appariée au levier des actes adverses.
5. **Contrôle du duel 3 doté d'une valeur attendue et d'une règle d'échec.**

FIN-DE-CELLULE