Les faits repris des pièces restent **RAPPORTÉ**. Mes objections et les contrôles proposés sont des **HYPOTHÈSES**, sauf lorsqu’ils découlent directement des règles de décision écrites. Je note \(Y\) le construit comportemental, \(\widehat Y\) sa lecture instrumentale, \(Z\) le style, le format, la longueur ou les refus, \(X\) l’item et \(T\) le point de contrôle.

## Sur la proposition A

### (a) Défauts de méthode

- **Les duels ne couvrent pas les issues possibles.** Dans E1, « erreur factuelle et gain bougent » et « seul le point fixe bouge » laissent de côté l’absence d’effet, un effet factuel sans effet sur \(g\), un effet sur \(g\) sans effet factuel, ou des mouvements de signes opposés. E2 et E3 présentent le même défaut : leurs conclusions de falsification dépassent ce que leurs régions de décision permettent.
- **Le contrôle par consigne système ne discrimine pas style et entraînement.** Si la base ainsi invitée reproduit le déplacement, cela peut aussi signifier que deux interventions différentes produisent un comportement équivalent. Si elle ne le reproduit pas, l’intensité de persona peut simplement être mal appariée. Ce contrôle ne suffit donc à aucune des deux inférences proposées.
- **Les témoins d’entraînement ne isolent pas la récompense.** Le SFT sur les propres sorties peut être une auto-distillation qui préserve la persona ; à nombre de pas égal, il n’apparie ni les distributions de gradients, ni la distance parcourue, ni la pression de KL. Dans E3, RLVR et RL-préférences diffèrent simultanément par les données, la récompense, sa variance et l’optimisation effective. Rééquilibrer le modèle de récompense est une nouvelle intervention causale, pas un contrôle négatif.
- **Une issue de E2 ne réfuterait pas l’a priori général de R8.** Elle porterait sur des checkpoints OCT déjà passés par DPO et sur une autre chaîne d’entraînement ; un mouvement de \(g\) n’en attribuerait pas l’origine à l’imitation ou aux préférences.
- **La validation instrumentale n’est pas protégée contre les fuites.** Rien n’impose que les sorties ayant servi à choisir seuils, paires difficiles et règles de refus soient disjointes de l’évaluation finale. Dépasser un prédicteur lexical en AUC marginale n’établit pas non plus que le classifieur lise autre chose que \(Z\), notamment après RL.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- L’instrument n’apporte une information de construit que si \(I(Y;\widehat Y\mid X,Z,T)>0\). Si \(P(\widehat Y\mid Y,Z,T)\) change avec \(T\), ou si les supports de \(P(Z\mid T)\) avant et après RL sont disjoints, sensibilité et fausses alertes apprises avant RL ne se transportent pas ; la « rétention » estimée contient alors une dérive de mesure non identifiable.
- Pour une rétention \(\widehat R=\widehat G_{\text{après}}/\widehat G_{\text{avant}}\), si \(G_{\text{avant}}=0\), si sa loi estimée concentre une masse non négligeable près de zéro, ou si son signe est incertain, \(\widehat R\) est instable, potentiellement sans variance finie, et son interprétation peut s’inverser.
- Dans l’attraction, si la variance entre items de la distance au point fixe est nulle, \(g\) et le point fixe ne sont pas identifiables séparément. Une erreur de mesure du niveau sans pression comparable à cette variance atténue en outre \(\widehat g\).
- Si la probabilité de refus dépend de \(T\), de la dose ou de l’item, exclure les refus conditionne sur une variable post-traitement ; les noter au milieu impose une autre loi de sortie. Sans hypothèse de non-réponse, les deux estimations peuvent viser deux paramètres différents, sans qu’aucune ne représente la persistance comportementale.
- Si les corrélations intra-item ou intra-graine approchent un, multiplier les tirages augmente peu la taille effective. Des intervalles calculés sur les générations comme indépendantes seront trop étroits et trancheront des duels sans la puissance nominale annoncée.

### (c) Contrôles négatifs dont l’absence serait fatale

1. **Paires contenu/style désorthogonalisées, annotées par des humains et réservées**, comprenant des sorties post-RL : même contenu avec chaleur variable, même chaleur avec accord variable. Sans elles, rétention et sycophancie restent ininterprétables.
2. **Mise à jour avec récompense non informative**, en appariant invites, trajectoires et budget d’optimisation, plutôt que seulement le nombre de pas. Sans elle, l’effet propre de la récompense n’est pas séparé de la dérive d’optimisation.
3. **Croyance correcte et assertion fausse d’origine impersonnelle**, avec les mêmes items. Sans ces contrastes, exactitude, accord avec l’utilisateur et capitulation sociale restent confondus.

## Sur la proposition B

### (a) Défauts de méthode

- **L’attendu principal de E1 tombe dans la zone non tranchée.** Avec \(r\simeq0,6\), il ne satisfait ni la région de persistance ni celle d’effacement. La conception prévoit donc explicitement que son résultat attendu ne réponde pas au duel.
- **E4 ne falsifie pas les thèses annoncées.** Un écart factuel élevé ne réfute pas « persona = ton », puisque le ton peut précisément causer cet écart. Un ton élevé avec faible capitulation factuelle ne réfute pas une disposition sociale ou implicite. L’ordre intermédiaire imposé à *Loving* ajoute une issue non assignée s’il échoue.
- **Les cas positifs du juge sont circulaires.** Prendre les sorties de *Sycophantic* comme vérité terrain suppose précisément ce que E4 doit tester. Si cette persona ne capitule pas, la « sensibilité » estimée est celle à une identité de checkpoint, pas à un comportement.
- **Le reformatage synthétique ne valide qu’une transformation choisie.** Il est appliqué aux sorties *Loving*, pas nécessairement aux formats réellement produits après RL. Compter les refus ne corrige pas leur effet de sélection.
- **Le contrôle de dose est insuffisant.** Des gains mathématiques semblables n’impliquent ni distances de paramètres semblables, ni entropie, KL ou nombre effectif de mises à jour comparables. Le SFT neutre à pas égaux présente le même défaut.
- **E2 apparie la longueur post-traitement.** Si persona et RL affectent tous deux la longueur, cet appariement peut sélectionner les sorties et créer une association plutôt que supprimer un biais. La récompense aléatoire change également la variance des gradients et peut simplement empêcher l’optimisation.
- **La réutilisation annoncée des générations de E1 par E3 n’est pas assurée.** E1 ne produit pas, tel qu’écrit, le protocole dosé de pression sociale requis pour estimer \(g\) et le point fixe.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- Le ratio \(r\) devient non jugeable lorsque son dénominateur est nul, proche de zéro relativement à son erreur d’estimation, ou de signe incertain. Une borne d’intervalle sur le numérateur ne résout pas cette instabilité.
- Pour E4, soit \(p_{m,b}=P(\text{erreur}\mid m,b)\). Si les probabilités sans croyance sont proches des bornes, ou si \(p_{m,\text{fausse}}-p_{m,\text{aucune}}=0\) parce que la manipulation n’a aucune prise, l’écart maximal atteignable peut rester sous les seuils : H_B devient vraie par construction, sans pouvoir sur la capitulation.
- Dans le DiD de E2, si l’analyse est conditionnée par l’absence de refus ou par une longueur affectée par les deux facteurs, l’estimand conditionnel change selon le bras ; l’interaction estimée peut alors provenir de lois de sélection différentes plutôt que d’une amplification.
- Pour l’attraction, une variation insuffisante des distances entre items rend \(g\) et le point fixe faiblement identifiés ; une exclusion de refus dépendante de la dose rend leurs trajectoires non comparables.
- À prévalence extrême des capitulations, le kappa peut rester proche de zéro malgré un accord brut élevé, ou devenir très instable. Le critère \(\kappa\) seul ne fournit alors ni validation ni invalidation utilisable du juge.

### (c) Contrôles négatifs dont l’absence serait fatale

1. **Cas positifs définis par annotation comportementale indépendante**, et non par le checkpoint *Sycophantic* ; sinon E4 et la validation du juge se valident mutuellement par hypothèse.
2. **Contrôles contenu/format sur sorties post-RL réellement observées**, et pas uniquement reformatage artificiel des sorties initiales.
3. **Récompense non informative à optimisation appariée** pour E1 comme pour E2 ; le SFT neutre et la récompense aléatoire actuels n’isolent pas le contenu de la récompense.
4. **Croyance correcte et source impersonnelle dans les contrastes de E4**, pas seulement dans la banc de validation du juge.

## Sur la proposition C

Pièce C absente, jamais lancée : aucune critique de méthode n’est possible et je n’en invente pas le contenu.

## Sur la proposition E

### (a) Défauts de méthode

- **Le seuil de A ne définit pas deux mécanismes.** Une rétention juste sous son seuil ne démontre pas que la persona ne survit pas ; H_B regroupe érosion partielle, inversion et absence initiale résiduelle. Le duel est exhaustif sur un paramètre, mais les interprétations verbales sont plus fortes que ce paramètre.
- **B et C ne mesurent pas la persistance.** Leur contraste principal est calculé après RL, sans différence correspondante avant RL. Un effet initial de *Loving*, totalement effacé ou fortement modifié par l’entraînement, peut ainsi produire le même \(D\) ou \(D_{\mathrm{social}}\) qu’une persistance parfaite.
- **Le témoin sans mise à jour n’isole pas le RL.** Même avec la soustraction de la base, il reste une possible interaction entre persona et n’importe quelle mise à jour de gradient. L’amélioration arithmétique établit que l’optimisation a agi, pas que sa dose effective est comparable entre départs.
- **L’annotation humaine ne supprime pas la circularité de construit.** Pour C, « conduite injustifiée » dépend d’une norme encodée dans les situations et les consignes. Si les mêmes exemples servent à former les annotateurs, régler les paires et valider l’instrument, les performances sont optimistes.
- **L’aveuglement ne garantit pas la stabilité temporelle.** Les annotateurs peuvent dériver entre les évaluations avant et après, ou reconnaître le style des bras malgré la suppression des étiquettes.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- Pour \(R=G_{\text{après}}/G_{\text{avant}}\), une loi de \(\widehat G_{\text{avant}}\) concentrée près de zéro rend le ratio instable. Si la même banque sert au test d’arrêt initial et à l’estimation finale, la continuation conditionne la loi de \(\widehat G_{\text{avant}}\) : l’intervalle naïf et \(\widehat R\) subissent un biais de sélection.
- Si \(P(\widehat Y\mid Y,Z,T)\) dépend de \(T\), les taux annotés ou extraits avant/après ne distinguent pas changement comportemental et changement de lecture. Si les distributions de longueur, ton ou format n’ont plus de support commun, l’appariement ne transporte pas les propriétés de validation.
- Dans B, si \(P(\text{erreur}\mid\text{fausse croyance})-P(\text{erreur}\mid\text{sans croyance})=0\) dans tous les bras parce que la manipulation est inerte, alors \(D=0\) par construction. Des justesses proches des bornes peuvent également rendre le seuil inatteignable indépendamment de toute sycophancie.
- Dans C, une prévalence de validation injustifiée proche de zéro ou de un supprime la variance nécessaire à l’estimation de \(D_{\mathrm{social}}\). Des erreurs d’annotation différentielles selon le bras peuvent produire le signe attendu sans différence de \(Y\).
- Avec corrélations fortes intra-situation, intra-dialogue ou intra-annotateur, la taille effective est inférieure au nombre de réponses. Avec seulement les trois graines d’entraînement proposées, l’estimation de la variance entre entraînements est fragile ; les intervalles groupés peuvent être trop étroits ou rester indécis.

### (c) Contrôles négatifs dont l’absence serait fatale

1. **Post-entraînement neutre ou récompense non informative à budget de mise à jour apparié**, commun à A, B et C ; le seul témoin gelé ne sépare pas érosion par RL et érosion par mise à jour générique.
2. **Sorties ancres identiques, intercalées aveuglément dans les sessions d’annotation avant et après.** Une dérive de leurs notes rendrait tout changement temporel non comparable.
3. **Banque post-RL entièrement réservée**, distincte des exemples de formation et de rédaction des consignes, avec paires contenu/style croisées. Sans elle, la validité conditionnelle des instruments dans le régime réellement mesuré reste inconnue.

Les contrôles de croyance correcte, de source impersonnelle et de validation justifiée déjà présents dans E sont nécessaires, mais ne réparent ni l’absence de contraste avant/après dans B et C, ni ces trois défaillances.

FIN-DE-CELLULE