**Statuts.** RAPPORTÉ désigne ce que propose une pièce, non un résultat obtenu. HYPOTHÈSE désigne les risques méthodologiques et les contrôles que je propose. VÉRIFIÉ désigne uniquement une conséquence des définitions ou des lois spécifiées, sans affirmer que ces lois décrivent le modèle. Les seuils expérimentaux des pièces sont **illustratifs** ; les constantes dans les identités mathématiques ne sont pas des estimations empiriques.

**Convention de lecture des critères (b) — VÉRIFIÉ, conditionnellement aux lois.** Soient \(Y\) la classe, \(Q\) la tâche, \(P_y\) la loi conditionnelle à \(Y=y\), \(S\) un score gelé, \(a\) le taux de fausses alertes, et \(q_a\) le quantile honnête de niveau \(1-a\). Pour un score continu,
\[
 r_a=P_1(S>q_a),\qquad
 |r_a-a|\leq {\rm TV}(P_1^S,P_0^S).
\]
L’égalité des lois implique une AUROC de \(1/2\), mais la réciproque est fausse. Pour **chacun** des seuils de performance ci-dessous, le duel jugeable est \(H_A:\theta\in C\) contre \(H_B:\theta\notin C\), où \(C\) est la région de succès préenregistrée. Une région de confiance simultanée qui intersecte les deux régions ne tranche pas ; ce n’est pas une troisième hypothèse. Pour des mesures répétées, l’unité de rééchantillonnage proposée est la tâche entière, branches comprises. Pour une queue rare, même sous indépendance des tâches, la probabilité de n’observer aucun dépassement honnête du vrai seuil vaut \((1-a)^{n_0}\). Une AUROC précise ne résout donc pas nécessairement l’incertitude sur \(r_a\).

## Sur la proposition A

### (a) Défauts de méthode

**RAPPORTÉ.** A veut prédire sur longues trajectoires une frontière \(k^*(T)\) à partir de scores mesurés sur trajectoires courtes.

**HYPOTHÈSE.** Le défaut décisif est de passer du **nombre d’actes** au **dégât**. Deux politiques peuvent avoir la même courbe de détection en \(k\), mais affecter des étapes de conséquences très différentes. Réparer une étape tout en gardant fixe sa continuation ne mesure pas l’effet d’une réparation suivie d’une nouvelle continuation. Il faut choisir le contrefactuel avant d’attribuer une part du dégât à chaque acte.

**VÉRIFIÉ, conditionnel.** Décaler les indices d’une référence laisse sa somme inchangée si toutes les étapes sont sommées avec les mêmes poids. Le témoin « étapes désalignées » ne détruit donc pas l’appariement *de tâche* pour cet agrégateur. Une pente en racine obtenue sur les tirages scriptés valide l’implémentation sous le générateur choisi, pas la loi pour une politique autonome.

**HYPOTHÈSE.** Choisir une politique sur son faible score, puis estimer sur les mêmes tâches son évidence par acte, biaiserait cette évidence vers le bas. Ajouter \(\kappa\) après observation des copies change aussi la revendication : il faut noter séparément la prédiction issue de l’agent seul et celle qui a bénéficié de données adverses multi-copies. La recherche finie de politiques ne tranche que pour la liste essayée.

### (b) Conditions sur les lois et les estimateurs — VÉRIFIÉ, conditionnel

- **Existence et frontière.** Posons \(p_T(k)=P_1(\mathrm{alerte}\mid k,T)\). Si \(P(k\mid T)=0\) au voisinage du franchissement, \(k^*\) n’est pas identifié sans extrapolation. Si \(p_T(k)\) n’est pas monotone, le dernier \(k\) admissible ne délimite pas une zone de furtivité. Si \(E[D\mid k,T,Q]\) varie entre régimes, une prédiction exacte de \(k^*\) ne fixe pas \(E[D\mid k^*,T]\).
- **Exposant et appariement.** Pour des résidus stationnaires d’autocovariance \(c_h\), la variance de la somme est \(Tc_0+2\sum_{h<T,h\ge1}(T-h)c_h\). Pour une somme cible \(U\) et une référence moyenne \(V\), la variance appariée est \({\rm Var}(U)+{\rm Var}(V)-2{\rm Cov}(U,V)\). Si les deux plans ont les mêmes variances marginales et la même covariance, leur gain de variance est identique. Si l’intervalle du gain non apparié contient zéro, le rapport des gains peut être non borné. Si \(k^*=0\), la pente logarithmique et l’erreur relative correspondante sont indéfinies.
- **Copies.** Sous indépendance conditionnelle à l’étape \(J=(Q,t)\), avec même propension \(p_J\) pour chaque copie, la covariance marginale des indicateurs de dégradation est \({\rm Var}(p_J)\). Un \(\kappa\) positif ne sépare donc pas dépendance entre copies et difficulté commune. À prévalence dégénérée, son dénominateur est nul.
- **Moniteurs, audit et transfert.** Si \(P(Y\mid S_{\rm texte},S_{\rm act})=P(Y\mid S_{\rm texte})\), la sonde n’ajoute rien au test optimal fondé sur le texte. Si l’évidence initiale conjointe est nulle, le rapport après/avant n’existe pas. Si \(P(\mathrm{acte\ dégradé}\mid S,Q,t)=P(\mathrm{acte\ dégradé}\mid Q,t)\), le score n’améliore pas le rendement optimal fondé sur \(Q,t\). Si les prédictions naïve et mécaniste coïncident sur le support de test, leur contraste d’erreur est nul, quelle que soit la vraie loi hors support.

### (c) Contrôles négatifs indispensables — HYPOTHÈSE

Permuter **les tâches de référence** dans une famille en conservant horizon et variance marginale ; simuler des copies indépendantes **conditionnellement à l’étape**, avec ses propensions estimées hors test ; évaluer des erreurs honnêtes de même conséquence finale sous les mêmes conditions de consigne. Garder des familles vierges de toute sélection de politique, de sonde ou de variante avec \(\kappa\). Sans ces contrôles, un bon ajustement ne distingue pas la loi proposée des effets de tâche.

## Sur la proposition B

### (a) Défauts de méthode

**RAPPORTÉ.** B transpose une identité de variance pour témoins corrélés en prédiction de discrimination, puis en règle d’achat d’information.

**HYPOTHÈSE.** La distinction à préserver est celle entre **corrélation de scores**, **corrélation d’erreurs au seuil** et **valeur du prochain témoin pour une décision**. Estimer séparément les paramètres sur chaque axe teste le transport entre tâches *sur cet axe*, pas leur transport entre axes. Réestimer un nombre de témoins effectifs à partir de la courbe de détection, puis prédire cette même courbe, serait circulaire. Un témoin supplémentaire dans le temps n’est pas non plus nécessairement un nouvel acte porteur de signal.

**VÉRIFIÉ, conditionnel.** Permuter les pas ne modifie pas une somme non pondérée. Ce contrôle peut éprouver un CUSUM, pas révéler une sensibilité à la position de la somme elle-même. Les deux issues proposées pour la fraction de baisse transférée se recouvrent à l’égalité ; il faut attribuer la frontière à une seule hypothèse.

### (b) Conditions sur les lois et les estimateurs — VÉRIFIÉ, conditionnel

- **Bascule et exposant.** Si \(P(\mathrm{bascule\ cible}\mid Q,\mathrm{erreurs\ aléatoires})\) dépend de l’orientation de la cible, le taux brut de bascule ne mesure pas un excès dirigé. Si \({\rm Var}(\log h)=0\) ou si le décalage moyen de score à dommage \(h\) est non positif, la pente logarithmique proposée n’est pas estimable telle quelle. Si \({\rm Var}(\sum_i S_i\mid k,Y)\) dépend de \(k\), le signe de \(1-\alpha\) ne détermine pas à lui seul la variation de discrimination.
- **Loi des témoins.** Pour des vecteurs gaussiens de moyennes \(m_y\) et de covariances \(\Sigma_y\), l’AUROC de la somme vaut \(\Phi\!\left[\mathbf1^\top(m_1-m_0)/\sqrt{\mathbf1^\top(\Sigma_1+\Sigma_0)\mathbf1}\right]\). Hors gaussianité, mêmes moyennes et covariances n’impliquent pas mêmes probabilités de classement ni mêmes queues. Même dans ce modèle, des décalages de signes différents peuvent s’annuler. L’erreur relative en \(d'\) est indéfinie à \(d'=0\).
- **Copies et transfert.** Si \(r_L\) est proche de zéro relativement à son erreur-type, le rapport \(r_S/r_L\) est instable ; même condition pour la baisse de la sonde divisée par la baisse du texte. Si la loi des scores honnêtes change après affinage, un seuil numérique inchangé n’est plus nécessairement au même \(a\).
- **Allocation.** Si \(P_Q(\pi_{\rho}(Q)\ne\pi_{0}(Q))=0\), l’effet décisionnel de \(\rho\) est nul, même avec une estimation exacte. Si les deux politiques n’ont pas la même probabilité d’accepter l’honnête, un contraste brut de rappel n’est pas un contraste à utilité égale. Si \(Y\) est indépendant du score de ciblage conditionnellement aux informations mécaniques disponibles, le ciblage n’ajoute pas de rendement à leur optimum.

### (c) Contrôles négatifs indispensables — HYPOTHÈSE

Randomiser le sens de la cible dans chaque tâche. Apparier familles de copies sur leurs taux marginaux d’erreur avant d’interpréter leur recouvrement. Opposer au simulateur binormal un témoin de spécification ayant les **mêmes moments** mais des queues différentes. Conserver l’affinage factice et recalibrer sur des honnêtes issus de chaque affinage. Enfin, comparer la politique avec et sans \(\rho\) **à menu d’actions identique** ; battre une politique qui ne peut pas acheter les mêmes témoins n’attribue aucun gain à la corrélation.

## Sur la proposition C

### (a) Défauts de méthode

**RAPPORTÉ.** C propose une conservation de signature entre canaux et une cascade de dépenses d’audit.

**VÉRIFIÉ, conditionnel.** Une contrainte de traitement de l’information sur une transformation n’impose aucune compensation entre les performances de deux scores. Une AUROC est une mesure intégrée sur les seuils, non un rappel « à fausses alertes fixées ». Une détection sur préfixe cumulé n’établit pas qu’un acte isolé est suspect.

**HYPOTHÈSE.** Filtrer seulement les trajectoires adverses par leur silence textuel crée une sélection asymétrique ; une meilleure sonde sur cette population n’est pas une preuve de mémoire interne. Paraphrase et bruit interne modifient simultanément deux variables. Choisir couche, sonde non linéaire et pénalité sur la frontière finale, puis y chercher le meilleur point, réutiliserait le test. Enfin, battre une allocation fixe avec une cascade adaptative ne démontre pas la conservation : cela peut simplement rémunérer le droit de différer un achat.

### (b) Conditions sur les lois et les estimateurs — VÉRIFIÉ, conditionnel

- **Alerte précoce.** Pour \(\tau=\inf\{t:S_t>b_t\}\), la quantité requise est \(P_0(\tau\le T)\), non \(P_0(S_t>b_t)\). À dépassements indépendants de probabilité \(a\), la première vaut \(1-(1-a)^T\). Une AUROC au temps médian n’identifie pas \(P_1(\tau<t_{D/2})\), qui dépend de la loi jointe de l’arrêt et du temps de demi-dégât.
- **Divergence.** Si \(E_0[V]=0\), le rapport de divergences moyennes n’existe pas ; si \(P_1^V=P_0^V\), aucun seuil sur \(V\) ne discrimine. Le rapport de deux moyennes de population est une constante, pas un score ROC par tâche.
- **Conservation.** Les lois \(P_{y,\lambda}^{X,A,V}=F^X_{y,\lambda}F^A_{y,\lambda}F^V_y\) admettent simultanément \(F^X_{1,\lambda}=F^X_{0,\lambda}\), \(F^A_{1,\lambda}=F^A_{0,\lambda}\), \(F^V_1=F^V_0\) et \(E_1[D]\ne E_0[D]\) si \(D\) n’est pas déterminé par ces scores. Si aucune valeur testée de \(\lambda\) n’atteint la baisse interne requise, la compensation conditionnelle n’a pas été éprouvée.
- **Cascade et oracle.** Avec historique \(H\) et sélection d’audit \(L\), si \(P(L=1\mid H=h)=0\) sur une strate de masse positive, le rappel de l’oracle dans cette strate n’est pas identifié à partir des audits sélectionnés. Si les historiques des deux politiques diffèrent en loi, les rappels conditionnels des auditeurs ne sont pas directement comparables.

### (c) Contrôles négatifs indispensables — HYPOTHÈSE

Appliquer le même filtre textuel aux honnêtes ; inclure une dérive honnête persistante de difficulté appariée. Séparer paraphrase seule, bruit seul et transformation factice, avec vérification indépendante du sens conservé. Réserver un jeu final après sélection de \(\lambda\). Opposer à la cascade un ordonnanceur tout aussi adaptatif sur signaux sans transfert ; auditer à l’aveugle un échantillon aléatoire des étapes non retenues. Sans ce dernier témoin, un excellent oracle sur les seuls cas faciles sélectionnés serait indiscernable d’un excellent oracle général.

## Sur la proposition E

### (a) Défauts de méthode

**RAPPORTÉ.** E mesure une divergence après remplacement de l’historique par un résumé, puis compare débat ouvert, cloisonnement et allocation conjointe.

**HYPOTHÈSE.** Le résumé est une intervention sur **l’information disponible**, pas directement sur le biais. S’il omet une preuve nécessaire, un agent honnête compétent *doit* changer de réponse. Un résumé produit avec la clé finale introduirait au contraire une fuite de vérité. Apparier après coup les trajectoires sur le dégât réalisé peut sélectionner des difficultés différentes selon la politique. Distribuer des sous-corpus différents change aussi l’accès aux preuves, même à calcul égal.

**VÉRIFIÉ, conditionnel.** Un test de McNemar contre une différence nulle ne teste pas le franchissement d’une marge positive. Une absence de significativité n’établit ni suffisance modulaire ni corrélation intra-modèle. Une fusion finale et une politique autorisée à acheter de l’information en cours de tâche diffèrent même sans interaction entre canaux.

### (b) Conditions sur les lois et les estimateurs — VÉRIFIÉ, conditionnel

- **Furtivité.** Pour un mélange d’étapes de même loi négative, \({\rm AUC}_{\rm mélange}=\sum_t w_t{\rm AUC}_t\). Une faible moyenne n’exclut pas une étape très détectable de faible poids. Si \(P_1(S_{\rm texte}\le q_a)=0\), le rappel conditionnel de la sonde parmi les évasions est indéfini ; il faut aussi le quantile honnête conditionnel à cette même sélection.
- **Sensibilité contrefactuelle.** Si \({\rm Var}_0(V)=0\), \(z_{\rm CF}\) n’existe pas. Si \(P(Q\mid D,\pi_{\rm base})\ne P(Q\mid D,\pi_{\rm évasion})\) et \(E[V\mid Q,D]\) varie avec \(Q\), un contraste à dégât fixé peut être non nul sans effet propre de politique. Une permutation appariée n’est exacte sous le nul que sous l’invariance de loi correspondante.
- **Débat et politique.** Pour des interceptions appariées de probabilités discordantes \(p_{10},p_{01}\), \(G=p_{10}-p_{01}\) et \({\rm Var}(\hat G)=(p_{10}+p_{01}-G^2)/n\) pour des tâches indépendantes. Un intervalle traversant la marge ne tranche aucun des deux duels. Si \(P(Y\mid X_1,\ldots,X_j)\) dépend du vecteur joint malgré \(P_y^{X_i}\) identiques entre classes pour chaque \(i\), les AUROC marginales au hasard n’impliquent pas l’inutilité du ciblage.
- **Audit guidé.** Pour une vérification de sensibilité \(s\), de faux positif \(f\) et une probabilité \(u\) de sélectionner une étape dégradée sur trajectoire adverse, le taux de signalement vaut \(f+(s-f)u\) sous erreurs conditionnelles constantes. Le gain guidé vaut donc \((s-f)(u_{\rm guidé}-u_{\rm hasard})\) : si ce produit maximal est inférieur à la marge exigée, le critère est inaccessible même avec un ciblage optimal.

### (c) Contrôles négatifs indispensables — HYPOTHÈSE

Produire sans clé un résumé placebo de même longueur et vérifier, à l’aveugle, qu’il conserve les preuves nécessaires sur les préfixes honnêtes. Croiser partage du contexte et répartition des preuves avec un agent seul recevant exactement les mêmes informations. Pour l’allocation, donner aux deux politiques les mêmes historiques, décisions autorisées et plafonds **par tâche**. Permuter les canaux conditionnellement à la difficulté, au temps et à l’éligibilité de la branche, sans assembler de futurs incompatibles avec le préfixe. Sans ce contrôle, la disparition du gain après permutation pourrait signaler la destruction de la structure des tâches, et non celle du transfert allégué.

FIN-DE-CELLULE