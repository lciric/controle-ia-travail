# Proposition E — Critique croisée de méthode

**Statuts.** Les conceptions reçues sont **RAPPORTÉES**, non des résultats expérimentaux. Toutes les critiques et conditions ci-dessous sont **HYPOTHÈSES méthodologiques**, formulées conditionnellement ; les relations mathématiques sont des **calculs**, pas des observations. Aucun audit ni recherche de nouveauté effectué.

**Notation commune.** \(Y\) désigne le trait comportemental, \(S\) un score, \(Z\) la provenance d’un modèle, \(\alpha\) le taux de fausses alertes, \(\varepsilon\) l’effet minimal préenregistré. Les seuils numériques des conceptions restent **illustratifs**. \(L_\Delta,U_\Delta\) sont les bornes d’un intervalle pour l’effet \(\Delta\).

**Exigence B4.** Un duel exploitable peut opposer \(H_A:\Delta\geq\varepsilon\) à \(H_B:\Delta<\varepsilon\). Les deux décisions concluantes falsifient chacune une hypothèse ; un intervalle traversant \(\varepsilon\) reste indécis. Ne pas transformer cette indécision en réfutation.

## Sur la proposition A

### (a) Défauts de méthode

**HYPOTHÈSE — E1 : cible statistique et nuls mal raccordés.** L’AUC « sur T » n’est pas définie tant que l’unité positive n’est pas précisée : modèle individuel, orientation d’une paire ou présence d’une différence. Les probabilités marginales demandées ne déterminent pas la probabilité d’égalité des traits sans distribution jointe.

N3 n’est un nul que pour un comportement et une distribution de questions spécifiés. L’égalité du suivi des mauvaises suggestions ne garantit pas l’égalité comportementale ailleurs. Il faut établir cette équivalence sur un lot indépendant, sans sélectionner ensuite les paires les plus favorables au lecteur.

Les hypothèses E1 ne couvrent pas les performances intermédiaires ; l’échec de \(H_A\) ne démontre pas la lecture du seul affinage. Enfin, battre une sonde supervisée et extraire une information sont deux questions distinctes.

**HYPOTHÈSE — E2 : sélection après intervention et faux partage causal.** Comparer l’exactitude conditionnelle à la terminaison dans chaque bras compare des populations différentes. L’édition peut faire entrer des problèmes difficiles dans la population terminée.

Pour la sycophancie, changer la part attirée constitue déjà un effet causal sur le comportement. Opposer « point fixe déplacé donc causal » à « pente déplacée donc seulement corrélat » n’est pas valide. Le point fixe et la pente peuvent aussi changer simultanément.

**HYPOTHÈSE — E3 : marginal n’est pas incrémental.** Comparer M1 à M3 ne mesure pas ce qu’ajoute M1 à M3. La comparaison pertinente oppose boîte noire seule et combinaison boîte noire–poids, entraînées et calibrées hors test. La fraction d’épisodes effectivement sabotés doit être mesurée, non identifiée au paramètre de construction.

**HYPOTHÈSE — E4 : un témoin ne définit pas une nulle.** Modifier les couches extrêmes ne prouve ni la conservation de la propriété ni l’inclusion des lois correspondantes dans le nul du juge. Une nulle augmentée doit être une famille de lois probabilistes explicite. La confirmation par oracle d’une propriété ne démontre pas que la loi proposée apporte une information nouvelle.

**HYPOTHÈSE — E5 : invariance obtenue par construction.** Si une canonicalisation fournit exactement la même entrée au lecteur, l’invariance teste surtout le prétraitement. Une invariance moyenne ne certifie pas toute une classe ; le coût de canonicalisation ne devient pas nul parce que le test réussit.

### (b) Conditions probabilistes de perte de puissance ou de non-jugabilité

**HYPOTHÈSES conditionnelles ; relations indiquées comme calculs.**

| Mesure | Condition |
|---|---|
| E1 — AUC, détection | \(P(S\mid Y=\mathrm{positif})=P(S\mid Y=\mathrm{négatif})\Rightarrow \mathrm{AUC}=1/2\) avec correction des ex æquo, et puissance \(=\alpha\) (**calcul**). Si \(P_{\rm test}(Y\mid Z)=P_{\rm calibration}(Y\mid Z)\) mais \(P_{\rm cible}(Y\mid Z)\) diffère, la performance cible n’est pas identifiée par le test. |
| E1 — fausses alertes agrégées | \(\mathrm{FA}_{\rm mélange}=\sum_jw_j\mathrm{FA}_j\leq\alpha\) n’implique pas \(\max_j\mathrm{FA}_j\leq\alpha\). Pour une classe \(j\), \(n_j=0\) rend son taux non estimable. |
| E2 — terminaison | Avec \(F_e\) la terminaison sous édition \(e\), l’estimateur compare \(\mathbb E[C_e\mid F_e=1]\). Si \(P(X\mid F_e=1)\) dépend de \(e\), il ne mesure pas un effet à population fixée. |
| E2 — attraction | Pour \(m(x)=x+k(a-x)\), \(\operatorname{Var}(X)=0\) rend \(k,a\) non séparables ; \(k=0\) rend \(a\) non identifiable. Une faible valeur propre de l’information de Fisher rend leurs intervalles larges. |
| E3 — gain incrémental | \(Y\perp S_{\rm poids}\mid S_{\rm noir}\Rightarrow\) aucun gain du test optimal combiné sur le test optimal boîte noire. Pour \(P_p=(1-p)P_0+pQ\), \(\mathrm{puissance}(P_p)\leq\alpha+p\,\mathrm{TV}(Q,P_0)\) (**calcul**). |
| E4 — juge | Si \(\mathbb E_P[E_t\mid\mathcal F_{t-1}]\leq E_{t-1}\) n’est pas établie pour chaque \(P\) du nul composite, la borne séquentielle revendiquée n’est pas établie. Si \(P_{\rm propriété}\) appartient au nul augmenté, aucune puissance supérieure au niveau n’est garantie. |
| E5 — invariance | Pour \(q_\mu=P_{W,T\sim\mu,U,U'}[d(W,U)\neq d(TW,U')]\), une petite valeur de \(q_\mu\) ne borne pas \(\sup_Tq_T\). Si \(U,U'\) diffèrent, \(q_\mu\) contient aussi la variabilité du lecteur. |

### (c) Contrôles négatifs dont l’absence serait fatale

**HYPOTHÈSE de contrôle nécessaire.**

- **E1 :** nuls séparés par parent, graine et recette ; affinage bénin apparié ; lecteur privé des poids mais conservant les métadonnées. Sans ce dernier, impossible d’attribuer la performance aux poids.
- **E2 :** intervention simulée, répétitions indépendantes du modèle non édité, contrôles de longueur et d’échelle ; sélection du support faite sans consulter les générations de test.
- **E3 :** combinaison boîte noire–poids avec scores de poids permutés entre unités indépendantes ; tous les moniteurs doivent subir la même séparation des modèles.
- **E4 :** faux témoins conditionnels aux statistiques déjà couvertes, et nouvelle validation du juge après extension du nul.
- **E5 :** répétitions sans transformation, contrôle de fidélité fonctionnelle indépendant et mesure du coût réel du prétraitement.

## Sur la proposition B

### (a) Défauts de méthode

**HYPOTHÈSE — E1 : le renversement ajoute une histoire d’entraînement.** Le parent honnête est un descendant du parent initial. La branche renversée diffère donc aussi par son ascendance, sa trajectoire et éventuellement sa capacité. Une réussite peut reconnaître l’histoire ; un échec peut refléter un changement de distribution plutôt qu’une lecture du déplacement.

La conception doit identifier ce que voit le lecteur : points finaux, parent ou deltas. Sans parent visible, « lecture de l’écart au parent » n’a pas le même sens opérationnel.

Sur une paire de deux sycophantes, exiger une probabilité marginale proche de l’indifférence est incorrect : on peut être certain que les deux le sont. Il faut séparer probabilité du trait individuel, orientation d’une différence et présence de cette différence.

L’intervalle approximatif proposé pour la petite taille de branche ne suffit pas à justifier la séparation annoncée des hypothèses. Doubler l’échantillon selon le premier résultat exige une procédure séquentielle préenregistrée.

**HYPOTHÈSE — E2 : calibration, sélection et changement d’unité.** Une calibration en paires ne certifie pas automatiquement les prédictions sur adaptateurs individuels. Une absence d’alerte fournit une borne seulement si le seuil était fixé indépendamment et les unités adéquatement indépendantes. Choisir ensuite le meilleur lecteur invalide une borne individuelle non corrigée.

La dose de données n’est pas la dose comportementale. Le « meilleur concurrent » doit être choisi hors test ou traité par intervalles simultanés. L’égalité du nombre d’appels ne garantit pas l’égalité du nombre de textes ni de l’information observée.

**HYPOTHÈSE — E3 : construit et sélection.** Le sous-ensemble « termine dans les deux modèles » dépend des deux interventions et de leur couplage aléatoire. Son effet ne représente pas le gain global de raisonnement. Un gain sur ce sous-ensemble ne suffit pas davantage à établir une capacité nouvellement acquise.

Pour la sycophancie, une direction lisible n’est pas un contrôle négatif dont l’effet nul serait acquis. La qualifier ainsi utiliserait la conclusion recherchée dans la définition du témoin.

**HYPOTHÈSE — E4 : absence de promotion ≠ réduction à une base.** Une loi peut perdre sa promotion parce que l’extension du nul réduit la puissance, sans être équivalente à une norme ou à une statistique extrême. Une puissance observée dans une autre famille ne se transporte pas automatiquement.

**HYPOTHÈSE — E5 : invariances affirmées trop largement.** Une fonction identique ne garantit pas l’invariance d’une sonde fixe d’activations. La norme des poids n’est pas invariante à toute reparamétrisation admissible. Ces références doivent elles-mêmes être définies dans des coordonnées compatibles.

**HYPOTHÈSE — E6 : mauvais nul et dépendance.** Changer les récompenses ne retire pas nécessairement les signatures du jeu dans les observations ou les poids. Des répétitions sur les mêmes réseaux estiment surtout la variabilité du lecteur. La formule du meilleur essai exige une hypothèse de dépendance ; elle n’est pas une borne universelle pour des tentatives adaptatives.

### (b) Conditions probabilistes de perte de puissance ou de non-jugabilité

**HYPOTHÈSES conditionnelles ; relations indiquées comme calculs.**

| Mesure | Condition |
|---|---|
| E1 — branches | Si \(P(Y=y\mid Z=z)\) est dégénérée dans les données observées, l’effet propre de \(Y\) à \(Z\) fixé n’est pas identifié. Si les supports \(P(W\mid Z=\mathrm{origine})\) et \(P(W\mid Z=\mathrm{renversée})\) sont disjoints, le transfert ne sépare pas à lui seul les mécanismes concurrents. |
| E1 — Brier | Pour un événement \(D\), le score optimal est \(P(D\mid W)\). Si les étiquettes d’évaluation portent sur \(Y\) mais les probabilités annoncées sur \(D\), le score ne mesure pas la calibration revendiquée. |
| E2 — certification | Pour seuil indépendant et \(n\) unités iid sans alerte, \(p_U=1-\delta^{1/n}\) au niveau de confiance \(1-\delta\) (**calcul**). Si le seuil ou le lecteur est sélectionné sur ces unités, cette expression ne fournit plus la garantie annoncée. |
| E2 — contraste | Si \(\Delta\) est entre les deux marges proposées, aucune des hypothèses annoncées ne décrit le paramètre. Si \(L_\Delta\leq\varepsilon\leq U_\Delta\), le duel complémentaire reste indécis. |
| E3 — terminaison conjointe | \(P(F_{\rm base}=1,F_{\rm édité}=1)\to0\Rightarrow n_{\rm sous\text{-}ensemble}\to0\). La distribution conditionnelle dépend du couplage \(\pi(F_{\rm base},F_{\rm édité}\mid X)\), que les marginales ne déterminent pas. |
| E3 — paramètres de courbe | \(\lambda_{\min}(\mathcal I(k,a))\to0\Rightarrow\operatorname{Var}(\widehat k),\operatorname{Var}(\widehat a)\) deviennent grandes. Une transformation de notation \(J_e=g_e(J)\) inconnue rend les comparaisons de paramètres non identifiables sans ancres. |
| E4 — promotions | Si la puissance d’une loi vraie est \(\beta\), \(P(\text{aucune promotion sur }m)=(1-\beta)^m\) sous indépendance (**calcul**). Cet événement n’identifie pas l’appartenance de la loi à la base mécanique. |
| E5–E6 — répétitions | Pour \(D_j\) les succès des tentatives, \(P(\bigcup_jD_j)=1-\prod_j[1-P(D_j)]\) seulement sous indépendance. Généralement \(P(\bigcup_jD_j)\leq\sum_jP(D_j)\) (**calcul**). Si \(P(W\mid Y)\) reste distinct sous le nul proposé, la performance peut dépasser le hasard sans violation. |

### (c) Contrôles négatifs dont l’absence serait fatale

**HYPOTHÈSE de contrôle nécessaire.**

- **E1 :** trajectoires témoins de même profondeur et budget, plusieurs parents indépendants, deltas bénins dans chaque branche, vérification comportementale indépendante des parents.
- **E2 :** calibration et test disjoints au niveau de l’ascendance ; contrôle métadonnées seules ; nuls individuels correspondant exactement à l’unité de verdict.
- **E3 :** réplication base–base avec générations fraîches, interventions simulées, ancrages de notation et tâches sans pression sociale.
- **E4 :** témoins vrais de force réglée après extension du nul ; faux témoins sélectionnés par le même proposeur que les lois candidates.
- **E5 :** variabilité sans transformation et validation séparée de chaque référence supposée invariante.
- **E6 :** étiquettes de tâche rendues indépendantes des réseaux à l’évaluation, nouveaux réseaux de test et publication de toutes les tentatives.

## Sur la proposition C

**RAPPORTÉ — La pièce E3-T1-conception-C est absente (« jamais lancée ») ; aucune critique de contenu n’est possible.**

## Sur la proposition D

### (a) Défauts de méthode

**HYPOTHÈSE — Protocole transversal : unité d’indépendance non définie.** Une « graine du modèle de base » n’est pas disponible comme variable de réplication si tous les adaptateurs partent du même point de contrôle publié. Des graines d’adaptation distinctes ne produisent pas des bases indépendantes. La séparation doit nommer ses unités : parent, recette, corpus, adaptateur, tâche et génération.

La disponibilité d’adaptateurs de sabotage pour les modèles de criblage n’est pas établie dans les pièces. Le budget suppose donc un artefact à confirmer.

**HYPOTHÈSE — Fiche 1 : bon seuil, mauvaise attribution possible.** Le duel sur un gain minimal est complémentaire, mais battre séparément les autres bras ne démontre pas un ajout à la boîte noire. Le meilleur concurrent sélectionné sur test introduit une sélection statistique. Le plan doit aussi distinguer détection du trait individuel et détection d’une différence entre deux modèles.

Un taux empirique dépassant le niveau nominal ne falsifie pas à lui seul la calibration ; il faut un test tenant compte de l’incertitude.

**HYPOTHÈSE — Fiche 2 : hypothèses composites insuffisamment définies.** Réduction d’attraction, suivi des suggestions, réplication, dommages et explication par longueur forment plusieurs critères. « Expliquée par les témoins » n’est pas un paramètre. Il faut définir une région d’acceptation jointe et son complément.

Conditionner sur une longueur produite par l’intervention peut retirer une partie de l’effet étudié ou induire une sélection. Préférer un budget fixé expérimentalement et publier séparément effets totaux et contrastes conditionnels.

Le sous-test Qwen mesure un effet sur un sous-ensemble sélectionné par la base, non directement un « ajout de capacité ». La sélection doit utiliser des générations distinctes de celles servant à estimer l’effet.

**HYPOTHÈSE — Fiche 3 : puissance du juge contre rendement du proposeur.** La puissance est définie pour une alternative fixée. Lorsque les proposeurs choisissent des lois différentes, on mesure un rendement de découverte combinant qualité des candidats et sensibilité du juge. Un oracle comportemental ne garantit pas la vérité générale d’une loi sur les poids.

**HYPOTHÈSE — Fiche 4 : moyenne contre existence.** \(H_B\) affirme l’existence d’une classe produisant une dégradation ; une moyenne faible sur des éditeurs échantillonnés ne la réfute pas. Il faut restreindre la cible à une distribution déclarée, ou établir une borne uniforme. La contrainte d’utilité est elle-même estimée et peut devenir une sélection favorable si elle est filtrée sur le test.

### (b) Conditions probabilistes de perte de puissance ou de non-jugabilité

**HYPOTHÈSES conditionnelles ; relations indiquées comme calculs.**

| Mesure | Condition |
|---|---|
| Réplication | Pour grappes de taille \(m\) et corrélation intragrappe \(\rho\), \(n_{\rm eff}\approx n/[1+(m-1)\rho]\) (**calcul**, modèle échangeable). Une seule grappe parentale ne permet pas d’estimer la variance entre parents. |
| Fiche 1 — différence appariée | Pour verdicts \(D_L,D_B\), \(\Delta=p_{10}-p_{01}\) et \(\operatorname{Var}(\widehat\Delta)=[p_{10}+p_{01}-\Delta^2]/n\) sous iid (**calcul**). Si l’intervalle traverse \(\varepsilon\), aucune décision B4 concluante. |
| Fiche 1 — calibration | \(P_{\rm test}(S\mid Y=0)\neq P_{\rm calibration}(S\mid Y=0)\) rend le niveau transporté non garanti. \(Y\perp S_L\mid S_B\) annule le gain optimal incrémental. |
| Fiche 2 — critère conjoint | Pour \(\theta=(\Delta k,\Delta Y,\Delta U,\Delta_{\rm réplication})\), une région \(R_A\) doit être fixée. Sans \(R_B=R_A^c\), le duel n’est pas exhaustif. Si l’ensemble de confiance intersecte les deux régions, non-jugabilité. |
| Fiche 2 — jugement | Si \(P(J\mid Y,e)\) varie avec l’intervention \(e\), \(\Delta J\) n’identifie pas \(\Delta Y\). Si les contraintes sur \(P(J\mid Y,e)\) sont absentes, plusieurs effets comportementaux peuvent produire le même effet noté. |
| Fiche 3 — découverte | Pour proposeur \(Q\), \(R_Q=\int\beta(h)\,Q(dh)\). Une différence de \(R_Q\) n’identifie pas une différence de \(\beta(h)\). Si \(\beta(h)\) est faible sur le support de \(Q\), le rendement est faible même avec des hypothèses vraies. |
| Fiche 4 — couverture | \(\mathbb E_{a\sim Q}\Delta(a)\leq\varepsilon\not\Rightarrow\sup_a\Delta(a)\leq\varepsilon\). Si \(Q(A^\star)=0\), aucune donnée tirée de \(Q\) n’informe la dégradation sur \(A^\star\). |

### (c) Contrôles négatifs dont l’absence serait fatale

**HYPOTHÈSE de contrôle nécessaire.**

- **Fiche 1 :** adaptateurs bénins appariés, métadonnées seules, calibration par sous-population et combinaison boîte noire–poids avec score supplémentaire permuté.
- **Fiche 2 :** générations base–base indépendantes, interventions simulées, notation aveugle avec ancres fixes, contrôle sans pression et estimation de sélection sur un lot distinct.
- **Fiche 3 :** proposeur sans accès aux poids, même budget de propositions, mêmes lois plantées soumises aux deux chaînes ; cela sépare rendement du proposeur et puissance du juge.
- **Fiche 4 :** éditeurs honnêtes de budget comparable, répétitions sans édition, évaluation indépendante de l’utilité et des seuils. Sans elles, une dégradation peut provenir de l’instrument plutôt que de la classe de menace.

FIN-DE-CELLULE