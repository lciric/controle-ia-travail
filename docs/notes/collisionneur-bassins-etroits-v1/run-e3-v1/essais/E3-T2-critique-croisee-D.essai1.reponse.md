Les quatre pièces sont présentes et lisibles. Les objections ci-dessous sont des déductions méthodologiques ; les possibilités non testées restent des **HYPOTHÈSES**. Je distingue partout la validité du juge sous son \(H_0\) de l’absence de fausses découvertes au sens de l’oracle : les faits **RAPPORTÉS** indiquent que la première ne garantit pas la seconde. Les seuils chiffrés contenus dans les propositions sont illustratifs, non acquis.

Pour les contrôles que je réclame, le duel minimal est : \(H_A\) = « effet spécifique au-delà du placebo, avec garde conforme » contre \(H_B\) = « pas d’effet spécifique, ou garde dégradée ». Un placebo équivalent ou une garde dégradée falsifie \(H_A\) ; un effet spécifique avec garde conforme falsifie \(H_B\).

## Sur la proposition A

### (a) Défauts de méthode

- **M1 est évaluée sur sa propre représentation.** Le monde décisif contient précisément l’interaction d’ordre faible que la décomposition rend visible. Cela démontre au mieux un gain sur mondes alignés avec l’instrument, pas sur les bassins étroits en général. Surtout, une « case vide » dépend de la mesure de référence \(\mu\) : hors mesure produit, l’orthogonalité et l’interprétation causale des termes ne suivent plus.
- **Le duel de vues confond plusieurs facteurs.** Vue décomposée, longueur du contexte, nombre d’interactions explicitement listées et diversité des invitations changent ensemble. Le bras à appels supplémentaires ne constitue un témoin à coût égal que si jetons, compilation et calcul sont compris dans le coût. Le test sur des « proposeurs-appels » suppose aussi une indépendance que ne garantissent ni la graine de monde partagée, ni la famille de modèle, ni les six cartes d’un même appel. Enfin, \(H_A\) et \(H_B\) ne sont pas exhaustives : A reconnaît elle-même l’issue intermédiaire « effet positif mais inférieur aux appels supplémentaires ».
- **M2 change l’estimand.** Évaluer sous une loi de traits \(\pi'\neq\pi\) teste la qualité conditionnelle sous \(\pi'\), pas la survie dans le monde sous \(\pi\). La simplification de la loi des traits dans le rapport de vraisemblance règle le problème d’échantillonnage, mais pas celui d’un nul composite ou recalibré sur les mêmes issues.
- **M3 peut surajuster le jeu public.** Strates, seuil et représentant sont construits sur les mêmes instances que celles qui servent à démontrer qu’il choisit la sœur porteuse. Sans mondes de réglage séparés, le taux de choix mesure une adaptation au banc.
- **M4 suppose une indépendance et une stabilité non établies.** La formule de portefeuille suppose des appels indépendants conditionnellement à des probabilités \(p_{jb}\) transportables entre mondes. Or une composante « \(b\) » n’a pas nécessairement de correspondant entre graines ou structures.
- **M5 n’a pas de règle d’allocation assez précise.** L’arrêt optionnel conserve la validité si chaque valeur arrêtée est bien une valeur e ; il ne garantit aucun gain de puissance à budget total égal. Sans règle indiquant quelles cartes prolonger et quelles cartes abandonner, le mécanisme économique est indéterminé.

### (b) Conditions de perte de puissance ou de non-jugeabilité

Soit
\[
\Delta_C=\mathbb E_{P_*}\!\left[\log\frac{P_*(Y\mid X)}{Q_0(Y\mid X)}\,\middle|\,X\in C\right].
\]
Sous \(\pi\), avec \(r=\pi(A)\), la dérive moyenne du logarithme de la valeur e est, pour une carte \(P_*\),
\[
d_\pi=r\Delta_A+(1-r)\Delta_{\bar A}.
\]
Sous stratification, elle devient \(d_{\pi'}=w\Delta_A+(1-w)\Delta_{\bar A}\). **M2 n’augmente même pas cette dérive si \(d_{\pi'}\le d_\pi\)** ; avec absence d’effet hors \(A\), cela interdit notamment tout gain lorsque \(w\le r\). Si les strates mélangent les deux signes d’une interaction, on peut avoir \(\Delta_C=0\). Si \(n\,r\,\Delta_A\) reste petit, ni stratification ni arrêt optionnel ne créent l’information manquante.

- **M1** perd sa cible si les interactions utiles sont hors ordre affiché, hors support de \(\mu\), ou si leurs termes varient fortement avec \(\mu\).
- **M3** perd tout pouvoir si \(C(c)\) est vide ou identique pour toutes les sœurs, si aucune ne couvre la composante, ou si l’erreur d’estimation des distances par strate dépasse leur écart.
- **M4** n’apporte rien si les \(p_{jb}/c_j\) sont équivalents entre familles, ou si les appels d’une famille sont presque parfaitement corrélés. Avec des \(\widehat p_{jb}\) nuls ou dont les intervalles se recouvrent, le portefeuille estimé n’est pas jugeable.
- **M5** ne peut dépasser la limite imposée par le budget maximal et par la probabilité de franchissement avant ce budget.
- La métrique oracle devient non jugeable si deux composantes produisent la même loi conditionnelle sur le support de \(\pi\), ou si « additionnel à l’archive » change de sens entre bras parce que leurs archives intermédiaires divergent.

### (c) Contrôles négatifs indispensables

Il faut séparer **monde entièrement dans le nul**, pour tester les promotions sous \(H_0\), et **copies hors classe du nul**, pour tester la garde contre les recombinaisons : les confondre invalide l’interprétation. M1 exige aussi un placebo de même longueur listant des interactions sans information correcte, et des mondes hors structure affichée. M3 exige des groupes sans sœur porteuse mais avec écarts fortuits sur le jeu public. M4 exige une permutation des étiquettes de familles et une évaluation sur structures de mondes jamais utilisées pour estimer le portefeuille. Sans cela, respectivement, garde, attribution causale et transport du gain ne sont pas établis.

## Sur la proposition B

### (a) Défauts de méthode

- **M1 prouve une répulsion dans le noyau, rien au-delà.** Un tirage DPP ne maximise pas nécessairement le volume ; il favorise les sous-ensembles de grand déterminant. De plus, les proposeurs ne reçoivent aucune issue : mettre une strate en avant ne « rend » donc pas statistiquement visible son effet. Le gain \(p_s>p_0\) est précisément ce qu’il faudrait mesurer.
- **M2 contient un objet mal défini.** En général, \(\hat p(Y\mid t_i)\hat p(Y\mid t_j)\) n’est pas une loi normalisée en \(Y\), et la divergence écrite n’est donc pas une KL conditionnelle standard. Même corrigée, une divergence marginale nulle n’exclut pas une interaction conditionnelle qui s’annule en moyenne. Le graphe mesure l’archive, pas les dépendances du monde.
- **M3 n’observe pas le gain qu’elle prétend modéliser.** Une distance publique au nul n’est ni une amélioration prédictive ni une probabilité de couverture oracle. La variance maximale d’un GP privilégiera typiquement les lois isolées dans le noyau, y compris le bruit grammatical.
- **M4 confortablement couvre son propre encodage, pas les idées.** La borne de couverture est vraie par construction pour les sous-ensembles choisis. Elle ne dit rien des fonctions, seuils ou chaînes conditionnelles. Le calcul assimile par ailleurs cartes et appels, alors que les faits **RAPPORTÉS** distinguent plusieurs cartes par appel.
- **M5 confond trou d’échantillonnage et trou d’archive.** Avec une distance globale de Hellinger, une différence rare peut être diluée avant même le calcul topologique.
- **L’expérience principale mélange proposition et survie.** Couvrir la composante parmi les représentants retenus ne permet pas d’attribuer l’effet aux invitations plutôt qu’au regroupement, au juge ou à l’archive issue de la génération précédente. Les probabilités spontanées \(p_L,p_E\) sont des propriétés du couple modèle-vue, pas des boutons du générateur ; un pilote utilisé pour choisir le monde et l’instrument crée un risque de surajustement.

### (b) Conditions de perte de puissance ou de non-jugeabilité

Pour une vue \(v\), soit \(q(v)\) la probabilité qu’un appel produise au moins une carte couvrant le bassin. M1 et M2 perdent leur avantage si la moyenne de \(q(v)\) sur les vues effectivement assignées n’excède pas celle du témoin, ou si les échecs restent corrélés entre vues. Une interaction hors liste candidate, une condition parente non archivée, ou une annulation marginale dans chaque strate affichée rend M2 inopérante.

M3 devient non jugeable si le noyau n’a aucune relation mesurable avec la couverture oracle ; sa variance a posteriori peut alors être grande précisément là où toutes les lois sont fausses. M4 n’a aucune puissance si la cible est hors code ou si la probabilité de proposition conditionnelle à une invitation reste nulle. M5 devient instable lorsque les distances inter-cartes sont du même ordre que leur erreur d’estimation ou que l’effet rare dilué.

Enfin, le rappel du regroupement n’est pas identifiable si « cibler une composante » n’est pas défini par une ablation de risque prédictif : deux composantes observationnellement équivalentes ne peuvent recevoir des étiquettes distinctes fiables.

### (c) Contrôles négatifs indispensables

Le contrôle par paires non pertinentes doit être **échangeable** avec les paires ciblées quant à leur présence dans l’archive, à la longueur et à la syntaxe de l’invitation ; choisir les placebos grâce à l’oracle introduirait une différence de construction. Il faut également une invitation aléatoire de même longueur, une cible hors liste candidate, et une mesure aux propositions brutes. Le monde sans composante doit être distingué du monde contenant des copies hors classe. Pour M5, un rééchantillonnage de lois nulles avec les mêmes distances doit produire des « trous » : sinon le taux de fausses cavités reste inconnu.

## Sur la proposition C

### (a) Défauts de méthode

- **M1 attribue au plan couvrant une propriété qu’il ne possède pas.** Faire apparaître des configurations de traits ne garantit ni leur identifiabilité sous la loi réelle des traits, ni leur lecture par un modèle. Avec des instances sans issue, conditionner une strate ne neutralise pas empiriquement l’effet de l’archive : cela ne fait que changer un résumé descriptif. Au sens usuel exigeant tous les motifs de force deux, le plan annoncé doit être exhibé ; la version affaiblie à un seul motif ne fournit pas la garantie revendiquée.
- **M2 ne supprime pas la dilution dans son propre modèle.** C’est le défaut central. Si \(P=Q_0\) hors \(A\), alors
  \[
  E_n^{\mathrm{glob}}
  =\prod_{i\le n}\frac{P(Y_i\mid X_i)}{Q_0(Y_i\mid X_i)}
  =E_n^{(A)}
  \]
  dès que le dénominateur local est le même. Le processus local contient encore environ \(n\pi(A)\) observations et sa dérive reste proportionnelle à \(n\pi(A)\Delta_A\). Un mélange pondéré peut même être inférieur à la valeur globale. Le gain annoncé ne peut donc venir que d’un dénominateur différent ou d’un autre plan d’échantillonnage, qu’il faut démontrer séparément.
- **Le recalibrage local du nul peut créer une fuite.** S’il utilise les issues fraîches qui servent aussi au rapport de vraisemblance, l’argument de valeur e doit être refait ; l’indépendance du jeu public ne suffit plus.
- **M3 réintroduit une prime de nouveauté dans l’allocation du test.** Ne pas modifier \(e\) ne suffit pas : donner davantage de poids aux directions orthogonales modifie la sélection selon la nouveauté. La validité formelle du contrôle des fausses découvertes ne répond pas à l’objection du premier tour concernant les directions aberrantes et les copies hors classe.
- **M4 surinterprète l’orthogonalité.** L’orthogonalité de Walsh n’implique pas une distance KL ou de Hellinger « maximale ». Elle suppose en outre le codage et la mesure qui rendent les caractères orthogonaux.
- **Le prétendu plan factoriel n’est pas réalisé par les deux bras décrits.** Si vue et juge changent ensemble, \(D_2^{\mathrm{ret}}\) confond leurs effets. Le rejeu doit croiser explicitement chaque lot scellé de cartes avec chaque juge. Une absence de gain brut falsifie le mécanisme amont, mais pas nécessairement l’hypothèse combinée portant sur les retenues.
- Les trois « conditions nécessaires et suffisantes » sont seulement des conditions favorables : aucune ne garantit à elle seule émission, détection et promotion à coût égal.

### (b) Conditions de perte de puissance ou de non-jugeabilité

Pour M2, si les cellules sont trop fines, \(n\pi(C)\) est insuffisant ; si elles sont trop grossières, les signes s’annulent et \(\Delta_C\) chute. Si plusieurs cellules portent conjointement l’effet, le mélange perd leur évidence conjointe et paie les poids \(w_C\). Avec \(\pi(C)=0\), la strate est non jugeable.

M1 perd son effet si les cibles sont hors plan, si les traits sont dépendants au point de rendre certaines configurations presque impossibles, ou si \(q(v)\) reste constant. M3 perd son avantage si la carte étroite est colinéaire aux clones dans le noyau, tandis qu’une carte nulle orthogonale reçoit le poids élevé. M4 et M5 perdent leur cible si les chaînes ne correspondent ni aux monômes ni aux simplexes manquants choisis.

Le critère de fausse découverte oracle est lui-même ambigu : une carte peut dépendre d’un trait de bruit tout en couvrant réellement une composante ; inversement, une amélioration supérieure au seuil d’ablation ne prouve pas l’absence de copie. Enfin, si la détectabilité oracle est définie relativement à des archives qui divergent entre bras, \(D_2^{\mathrm{ret}}\) ne mesure plus exactement le même estimand.

### (c) Contrôles négatifs indispensables

Le monde à blanc et les traits de bruit sont nécessaires mais insuffisants. Il faut : un plan factice de même longueur et de même diversité de vues ; des interactions hors grille et à signes annulés dans les cellules ; un juge global à dénominateur strictement identique, afin de tester l’allégation de non-dilution ; des lots où le bruit est orthogonal et la carte étroite colinéaire ; et des recombinaisons hors classe séparées du vrai \(H_0\). Sans ces contrôles, un gain peut provenir de la seule diversification des invites, et un gain du juge multi-échelles peut n’être qu’un changement de nul.

## Sur la proposition E

### (a) Défauts de méthode

- **Les trois méthodes restent évaluées préférentiellement sur leur langage.** Contrastes alignés avec l’interaction, transformations choisies parce que le modèle pourrait n’y être pas équivariant, et cibles à courte dérivation dans le synthétiseur : chaque dispositif peut établir une existence locale sans établir un gain sur une famille de mondes indépendante de sa conception.
- **Le coût en euros ne suffit pas à définir le témoin.** Il faut aussi figer le nombre de cartes valides, les jetons de contexte, le calcul de compilation et le coût de certification. Sinon le témoin réinvestit dans des appels un budget que le traitement a partiellement consommé ailleurs.
- **Le compilateur peut devenir le véritable proposeur.** Si l’ablation mécanique égale le modèle, cela ne réduit pas nécessairement l’utilité de la méthode, mais cela falsifie l’interprétation « meilleure idéation ». De même, pour les vues, le proposeur exactement équivariant est un contrôle vrai par construction : il vérifie le pipeline, pas la loi des modèles réels.
- **La garde par supremum échange validité contre puissance.** Elle est conservative si le nul contient la vraie loi et si le supremum est exact ou majoré certifié. Mais une classe assez large pour contenir toutes les copies peut contenir les découvertes elles-mêmes.
- **Les duels de mécanisme restent incomplets.** Pour les prolongements, opposer synthèse ordonnancée et propositions indépendantes ne distingue pas l’effet de l’ordonnancement par longueur de description de celui de la simple fourniture de prolongements.

### (b) Conditions de perte de puissance ou de non-jugeabilité

Pour les contrastes, soit \(q_0,q_1\) les probabilités de couverture brute par appel et \(k_0,k_1\) les nombres d’appels achetés à budget égal. Sous indépendance, le traitement ne gagne que si
\[
1-(1-q_1)^{k_1}>1-(1-q_0)^{k_0}.
\]
Ainsi \(q_1=q_0\) avec \(k_1\le k_0\) suffit à éliminer le gain ; une corrélation positive entre appels réduit encore l’intérêt de les multiplier.

Pour les vues, l’équivariance au niveau des bassins, \(q(gv)=q(v)\), supprime tout effet distributionnel. Pour les prolongements, si la cible n’est pas dans le support typé, si sa longueur effective rend son budget inatteignable, ou si la probabilité de compléter correctement ses étapes est trop faible, la borne d’énumération n’implique aucune découverte.

Pour la garde, si la loi alternative \(P_*\) appartient au nul \(\mathcal Q\), alors, avec \(S=\sup_{Q\in\mathcal Q}Q\), la carte \(P_*\) vérifie \(P_*/S\le1\) : elle ne peut produire le signal recherché. Si \(\mathcal Q\) n’est pas calculable avec un majorant certifié, ou si l’appartenance de la vraie loi n’est pas défendable, la garantie est non jugeable. Enfin, l’ablation oracle ne peut attribuer une couverture lorsque deux composantes sont observationnellement équivalentes sur le support évalué.

### (c) Contrôles négatifs indispensables

Les mondes additifs, bibliothèques non alignées et cibles sans courte dérivation sont de bons contrôles. Il manque surtout : un **compilateur placebo** produisant des contrastes aléatoires de même complexité ; un **ordonnanceur aléatoire** recevant exactement les mêmes prolongements et le même budget ; et des mondes de confirmation séparés non seulement par graine, mais par structure, de ceux ayant servi à choisir bibliothèque, grammaire et poids. Pour la garde, il faut distinguer nul complet, copies hors classe et alternative réellement additionnelle : sans ce dernier témoin de détectabilité, une procédure qui ne promeut jamais passerait les contrôles nuls tout en étant sans puissance. Enfin, les critères de couverture doivent être gelés avant lecture des archives finales, sous peine de changer d’estimand entre bras.

FIN-DE-CELLULE