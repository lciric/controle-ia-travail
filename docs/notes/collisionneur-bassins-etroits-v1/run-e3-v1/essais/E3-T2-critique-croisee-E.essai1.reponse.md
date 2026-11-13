# Proposition E — Critique croisée de méthode

**Statuts.** Les contenus attribués aux propositions sont **RAPPORTÉS**, sans validation de leurs garanties. Mes diagnostics et contrôles proposés sont des **HYPOTHÈSES de méthode**. Les identités et contre-exemples explicitement démontrés ci-dessous sont **VÉRIFIÉS par calcul dans cette réponse**, sans rehausser le statut des faits transmis. Aucun résultat expérimental nouveau n’est disponible.

**Notation.** \(P\) désigne la loi du monde, \(\mu\) celle des traits, \(\mathcal N\) le nul effectivement couvert, et \(\Pi_v\) la loi des cartes produites sous la vue \(v\). La largeur générative d’un bassin \(B\) est \(\Pi_v(B)\), non sa masse \(\mu(A)\) dans l’espace des traits.

**Inférence forte pour les contrôles proposés.** Pour chaque erreur mesurée \(\eta\), opposer \(H_A:\eta\leq\tau\) à \(H_B:\eta>\tau\), avec tolérance et estimateur scellés. Pour l’efficacité, opposer \(H_A:\Delta\geq\delta\) et garde conforme à \(H_B:\Delta<\delta\) ou garde non conforme. Un intervalle entièrement d’un côté réfute l’autre hypothèse ; un intervalle chevauchant la frontière laisse le duel non résolu. Un échec de significativité ne réfute pas un gain.

## Sur la proposition A

### (a) Défauts de méthode

**HYPOTHÈSE — M1 : instrument et cible trop assortis.** Construire une vue d’interactions manquantes, puis l’évaluer principalement sur des mondes contenant précisément ces interactions, teste un avantage spécialisé. Changer seulement la graine ne teste pas le transfert structurel. La reconstruction exacte de l’archive certifie le calcul, pas la pertinence des cases affichées.

La décomposition conditionnelle écrite exige une mesure produit pour les propriétés annoncées. Une mesure de référence publique quelconque ne suffit pas. Une distribution empirique de traits dépendants n’est pas interchangeable avec une mesure produit.

**HYPOTHÈSE — M2 : couverture et identifiabilité confondues.** Un tableau orthogonal ne garantit pas que toutes les interactions jusqu’à sa force soient estimables sans confusion avec les autres termes. Il faut préciser la matrice de régression, son rang et les interactions exclues. Stratifier les tirages change aussi la distribution d’évaluation : le gain sous \(\mu'\) n’est pas automatiquement un gain sous \(\mu\).

**HYPOTHÈSE — M3 : la restriction intragroupe ne suffit pas.** Maximiser le nombre de strates où une carte s’écarte de l’archive demeure un critère numérique de nouveauté dans la sélection. Son caractère intragroupe n’annule pas l’objection du premier tour. Pour choisir un seul représentant, la garantie sous-modulaire est sans apport : on calcule directement le maximum.

**HYPOTHÈSE — M4–M5 : hypothèses de transport et de validité manquantes.** Le portefeuille suppose la stabilité des probabilités de couverture et une factorisation des échecs entre appels. Le test séquentiel exige une validité conditionnelle à chaque étape pour tout le nul composite ; disposer de valeurs e valides séparément à chaque taille ne suffit pas.

**HYPOTHÈSE — duel insuffisamment séparé.** Le bras supplémentaire à davantage d’appels n’est à coût égal qu’après mesure du coût complet. Le duel aval mélange stratification et arrêt. Enfin, davantage de cartes `si_sinon` sous un monde nul ne constitue pas, en soi, une dégradation de garde.

### (b) Conditions mesurables de perte de puissance ou de non-jugeabilité

- **M1.** Si \(\Pi_{v_{\mathrm{M1}}}(B)=\Pi_{v_0}(B)\), le gain génératif est nul. Pour la décomposition, mesurer les résidus  
  \[
  R_{S,i}=\left\|\mathbb E_\mu[f_S\mid X_{S\setminus i}]\right\|_{L^2(\mu)}.
  \]
  Des \(R_{S,i}\) non nuls invalident l’orthogonalité annoncée sous \(\mu\), même avec reconstruction exacte.

- **M2.** Une matrice d’information singulière rend certains coefficients non identifiables. Si \(\mu'(A)=0<\mu(A)\), une évaluation sous \(\mu'\) ne juge pas le comportement sur \(A\). Avec pondération d’importance, une variance infinie des poids empêche les garanties usuelles de précision.

- **M3.** Si toutes les cartes ont le même ensemble \(C(c)\), le critère ne discrimine rien. Si les distances estimées sont proches de \(\varepsilon\) à leur erreur d’estimation près, le représentant devient instable. Si l’écart à l’archive est indépendant de l’amélioration sous \(P\), le critère n’a pas de puissance pour sélectionner une vraie amélioration.

- **M4.** Si la probabilité conjointe d’échec diffère de  
  \[
  \prod_j(1-p_{jb})^{k_j},
  \]
  l’objectif optimise une probabilité erronée. Mesurer cette différence et le déplacement des \(p_{jb}\) entre familles de mondes réservées.

- **M5.** Exiger, pour chaque \(P\in\mathcal N\),
  \[
  \mathbb E_P[E_t\mid\mathcal F_{t-1}]\leq E_{t-1}.
  \]
  Une dérive logarithmique alternative non positive rend l’accumulation de preuves inopérante. Une moyenne empirique de valeurs e ne certifie pas leur espérance lorsque les queues sont insuffisamment contrôlées.

### (c) Contrôles négatifs indispensables

**HYPOTHÈSE.** Il manque : traits dépendants pour M1 ; interactions aliasées pour M2 ; sœur volontairement fausse mais éloignée de l’archive sur beaucoup de strates pour M3 ; appels corrélés et changement de famille de mondes pour M4 ; nul composite avec allocation séquentielle adaptative pour M5.

Les recombinaisons hors du nul doivent être auditées comme erreurs de nouveauté, **pas étiquetées \(H_0\)** sans élargissement préalable du nul. Le placebo de vue doit conserver longueur et archive vraie : permuter les coefficients entre traits falsifie l’information, au lieu de neutraliser seulement sa présentation.

## Sur la proposition B

### (a) Défauts de méthode

**RAPPORTÉ — erreur de statut.** B qualifie v67 d’**OBSERVÉ-NON-AUDITÉ** ; les faits transmis la qualifient de **RAPPORTÉ**. Ce statut doit être conservé.

**HYPOTHÈSE — M1 : garantie déplacée.** Un DPP échantillonne selon un déterminant ; il ne maximise pas nécessairement celui-ci, ne force pas l’orthogonalité et ne garantit aucune diversité des cartes. Aucun opérateur de Stein n’est défini malgré le titre. Le témoin pertinent est aussi un tirage uniforme **sans remise dans le même catalogue de vues**.

**VÉRIFIÉ — M2 : divergence non définie comme annoncé.** Le produit
\[
\hat p(y\mid t_i)\hat p(y\mid t_j)
\]
ne somme généralement pas à l’unité sur \(y\). Ce n’est donc pas, sans normalisation, une loi à placer au dénominateur d’une KL. Une normalisation ne transforme pas automatiquement l’expression en mesure d’interaction.

**HYPOTHÈSE — M3 et M5 : diagnostic servi comme consigne.** La distance au nul n’est pas le gain prédictif dans le monde. Si le GP utilise des performances de cartes rejetées, la source licite de ces performances manque ; s’il utilise seulement leurs distances publiques, il modélise une géométrie, pas le gain. Demander un écart minimal au nul rouvre explicitement la prime de nouveauté. Une homologie qui alimente les vues n’est plus « descriptive pure ».

**HYPOTHÈSE — M4 et budget.** Une borne inférieure sur la taille d’un code ne prouve pas l’existence d’un code de cette taille. La proximité entre sous-ensembles de traits ne garantit pas la proximité des lois produites. B confond en outre cartes et appels, alors que les six cartes par appel sont **RAPPORTÉES** dans les faits.

**HYPOTHÈSE — calibration circulaire.** Sélectionner les mondes où le pilote estime le bassin rare, puis réutiliser ces observations pour établir le gain, produit une sélection sur le bruit. Les contrôles « paires pertinentes/non pertinentes » doivent être construits sans transmettre leur pertinence oracle au traitement.

### (b) Conditions mesurables

- **DPP.** Si \(\operatorname{rang}(L)<k\), le DPP de taille \(k\) n’est pas défini. Si \(\Pi_v=\Pi_{v'}\) pour toutes les vues, la diversité du noyau est sans effet. Mesurer les probabilités conjointes de couverture, pas seulement les distances entre vues.

- **Graphe conditionnel.** Si toutes les lois d’archive donnent la même valeur à la statistique pour chaque paire candidate, le graphe ne classe aucune paire. Si la probabilité d’inclusion de la paire cible tend vers zéro à budget fixé, sa couverture tend également vers zéro.

- **GP.** Si
  \[
  \operatorname{Cov}\bigl(s(f),G_P(f)\bigr)=0,
  \]
  où \(s\) est le substitut public et \(G_P\) le gain oracle, le substitut n’établit aucune capacité de classement. Une variance postérieure de GP peut diminuer tout en restant sans lien avec l’erreur sur \(G_P\).

- **Code.** Sans borne sur
  \[
  \inf_{d_H(S,T)\leq r}\Pi_{v_T}(B_S),
  \]
  couvrir les mots du code n’implique aucune couverture des bassins.

- **Homologie.** Si l’erreur d’estimation des distances est du même ordre que la persistance des classes, leur interprétation est instable. Aucun seuil universel de nombre de lois ne règle ce problème.

- **Critères oracle.** Une carte peut couvrir plusieurs composantes, ou améliorer \(P\) sans correspondre à la décomposition plantée. Sans règle pour ces cas, rappel, fusion erronée et fausses découvertes ne sont pas définis.

### (c) Contrôles négatifs indispensables

**HYPOTHÈSE.** Exiger : vues de géométries différentes mais induisant la même loi de cartes ; archive sans interaction ; fonction de gain indépendante de la distance au nul ; sous-ensembles proches portant des lois opposées ; archives rééchantillonnées pour quantifier les faux cycles.

Pour le duel, un monde entièrement dans le nul et des copies recombinées sont indispensables. Comparer seulement les taux d’erreur des bras ne qualifie pas une garde : deux bras également défaillants peuvent sembler équivalents.

## Sur la proposition C

### (a) Défauts de méthode

**VÉRIFIÉ — M1 : plan annoncé impossible.** Le tableau couvrant binaire de la pièce C, avec quatre lignes, force deux et douze colonnes, n’existe pas. Chaque colonne devrait être équilibrée ; modulo complément, les colonnes équilibrées de longueur quatre ne fournissent que trois classes. Deux colonnes d’une même classe omettent des configurations conjointes. La construction décisive doit donc être remplacée, pas simplement exécutée.

**HYPOTHÈSE — couverture ne signifie pas isolation.** Une couverture de configurations ne neutralise pas automatiquement les traits confondants. La dépendance en force du coût du tableau est également escamotée.

**VÉRIFIÉ — M2 : localisation ne crée pas d’observations.** Si \(P=Q\) hors de \(A\), les facteurs du rapport de vraisemblance global y valent l’unité. Le test global n’y accumule donc aucun bruit supplémentaire. Le test local reçoit toujours un nombre moyen \(n\mu(A)\) d’observations utiles ; le mélange lui ajoute une pénalité \(\log(1/w_A)\).

**HYPOTHÈSE — validité locale non démontrée.** Le mélange de valeurs e valides est valide, mais cela ne prouve pas la validité des facteurs locaux. La projection invoquée doit être définie avec ses conditions d’existence, d’approximation et de validité séquentielle.

**HYPOTHÈSE — M3 : incompatibilité substantielle.** Donner davantage de poids de test aux directions « neuves » constitue bien une priorité numérique de nouveauté dans le juge. L’indépendance des tirages peut protéger une garantie statistique sous conditions ; elle ne lève pas le rejet protocolaire. Un DPP n’est pas invariant à l’ajout de clones : les sous-ensembles contenant ensemble des clones ont volume nul, mais dupliquer une direction modifie les probabilités d’inclusion.

**HYPOTHÈSE — M4–M5 : géométrie surinterprétée.** L’orthogonalité de Walsh ne signifie pas distance maximale au nul probabiliste. La description du monde ne suffit pas à identifier exactement son lien probabiliste à un monôme. Le complexe doit être fermé par faces ; une filtration est nécessaire pour parler de persistance. Des dérivées croisées de \(\log p\) peuvent provenir du normalisateur, même si le logit est additif.

Enfin, la liste opérationnelle ne réalise pas clairement toutes les cellules du factoriel annoncé. Une carte dépendant d’un trait de bruit peut néanmoins apporter un gain net grâce à d’autres traits : son classement automatique en fausse découverte biaise l’évaluation.

### (b) Conditions mesurables

- **Plans.** Mesurer la masse non couverte et le rang de la matrice des interactions. Une strate de masse nulle n’offre aucune information.

- **Juge local.** Pour un test de niveau \(\alpha\), une condition nécessaire à une puissance \(1-\beta\) est
  \[
  nD_{\mathrm{KL}}(P\|Q)\geq
  \operatorname{kl}(1-\beta,\alpha),
  \]
  lorsque \(1-\beta>\alpha\). Si la différence est confinée à \(A\), le membre gauche vaut \(n\mu(A)D_{\mathrm{KL}}(P_A\|Q_A)\). Cette condition conserve explicitement la puissance cible, absente de la borne annoncée par C.

- **DPP.** Une norme résiduelle nulle rend sa normalisation indéfinie ; un rang inférieur à la taille demandée rend le tirage impossible. Des cartes fausses avec grands volumes et des cartes utiles quasi colinéaires inversent le classement recherché.

- **Walsh.** Si \(\inf_{Q\in\mathcal N^\*}D(P,Q)=0\), élargir le nul a absorbé l’alternative : aucune détection de nouveauté contre ce nul n’est possible.

- **Homologie.** Des hessiennes non nulles pour presque toutes les paires peuvent produire un complexe saturé, sans cavités discriminantes. Une interaction pure peut, inversement, être absente de toutes les marges utilisées pour construire le complexe.

### (c) Contrôles négatifs indispensables

**HYPOTHÈSE.** Tester : carte exactement égale au nul hors de la région utile ; augmentation artificielle du nombre de clones ; cartes fausses orthogonales ; modèle à logit additif mais hessienne de log-probabilité non nulle ; interaction pure sans parents détectables.

Les bancs ne doivent pas fixer à la main des valeurs e favorables aux cartes utiles : les valeurs e doivent être générées par les lois et le juge évalués. Les mondes ayant servi à régler partitions, noyaux et poids doivent être exclus de l’évaluation.

## Sur la proposition D

### (a) Défauts de méthode

**HYPOTHÈSE — M1 : témoin trop faible.** Battre des affectations avec remise peut seulement montrer qu’éviter les répétitions est utile. Le comparateur sans remise et l’énumération simple doivent entrer dès le premier duel, pas seulement après une victoire.

**VÉRIFIÉ — M2 : variance incorrecte pour une déformation conditionnelle.** En conservant \(\mu\),
\[
D_{\mathrm{KL}}(P_0\|P_\theta)
=\frac{\theta^2}{2}
\mathbb E_\mu[\operatorname{Var}_{P_0}(h\mid X)]
+o(\theta^2).
\]
La variance globale ne convient que sous conditions supplémentaires. Si \(h=a(X)\), la normalisation annule intégralement la déformation : \(P_\theta=P_0\), malgré une variance globale éventuellement positive.

**HYPOTHÈSE — M3 : changement silencieux de témoin nul.** Chaque strate peut choisir un \(Q\) différent. Une petite divergence locale partout ne prouve donc pas l’existence d’une seule loi du nul expliquant toutes les strates.

**HYPOTHÈSE — M4 : validité claire, puissance indéterminée.** Il faut distinguer supremum sur un épisode et supremum sur l’échantillon entier. Leur conservatisme peut être très différent. Une approximation numérique qui sous-estime le supremum peut compromettre la validité.

**HYPOTHÈSE — attribution causale.** Le duel M1+M2 ne distingue pas couverture des questions et orthogonalisation. Les trois étages D2 localisent les pertes, mais ne séparent pas ces deux interventions. Une largeur estimée sur d’autres mondes définit une classe prédite étroite, pas une largeur connue pour chaque monde décisif.

### (b) Conditions mesurables

- **M1–M2.** Si \(\Pi_{v_u}(B)\) est constant sur les questions \(u\), aucune allocation n’améliore la couverture. Si la variance conditionnelle de \(h\) est nulle, la direction proposée ne déforme aucune loi.

- **M3.**
  \[
  \max_A\inf_QD_A(P,Q)\leq\inf_Q\max_AD_A(P,Q).
  \]
  Un écart important entre ces expressions mesure précisément la perte due aux témoins nuls différents. Les estimations deviennent non concluantes lorsque leurs erreurs couvrent le seuil de décision ou lorsque les strates ont masse nulle.

- **M4.** Pour des densités d’échantillon,
  \[
  \log e_n=
  \log\frac{q_n}{p_n}
  -\log\frac{\sup_{Q\in\mathcal N}q_{Q,n}}{p_n}.
  \]
  Si la pénalité du supremum absorbe le gain de l’alternative, la puissance disparaît. Si l’alternative appartient au nul, \(e_n\leq1\) ponctuellement.

- **Métrologie.** Une copie exacte a divergence globale nulle ; elle ne peut être appariée à un départ réel de divergence positive « à distance globale égale ». Il faut préciser le couple de lois utilisé comme référence.

### (c) Contrôles négatifs indispensables

**HYPOTHÈSE.** Ajouter : directions dépendant seulement de \(X\) ; lois localement expliquées mais sans témoin nul global commun ; nul très flexible absorbant l’alternative ; calcul exact du supremum sur une sous-classe finie pour auditer son approximation.

Enfin, garder les mondes de faible fréquence pilote dans une évaluation indépendante, sans reclassification opportuniste. Une absence d’échec de garde ne démontre pas sa non-infériorité : il faut une borne d’incertitude suffisamment précise pour réfuter la dégradation préenregistrée.

FIN-DE-CELLULE