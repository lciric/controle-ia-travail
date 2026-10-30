VÉRIFIÉ (lecture des pièces transmises) : les trois conceptions sont complètes. Je conserve les statuts qu’elles affichent et n’audite pas leurs références bibliographiques. Dans les critiques, \(S\) désigne la statistique de performance par famille, \(D_V\) et \(D_E\) les lois des familles vues et tenues à l’écart, \(p_{ik}\) la probabilité que la source \(k\) capture la famille \(i\), et \(C\) une couverture d’incidence.

## Sur la proposition A

### (a) Défauts de méthode

**Le duel vues/écart ne met pas en regard deux hypothèses exclusives.** Son alternative « écart de loi » contre « adaptation de la défense » confond deux causes : une adaptation peut produire un écart nul si les lois de difficulté se compensent, et un écart non nul peut provenir uniquement de \(D_V\neq D_E\). La scission aléatoire des familles vues estime une loi nulle **interne à \(D_V\)** ; elle ne valide pas le transport vers \(D_E\). De plus, comparer les minima de deux ensembles de tailles différentes introduit une dépendance mécanique à ces tailles, que le bootstrap par famille ne supprime pas.

**Le nombre de sources captant une famille n’est pas sa probabilité d’inclusion.** Conditionnellement à l’échantillon observé, ce nombre est tronqué : les familles jamais captées sont absentes. Une corrélation entre \(S\) et le nombre de captures, même avec permutation des étiquettes, n’identifie donc ni \(\operatorname{Cov}(S,p_{ik})\) dans la population ni une pondération de Horvitz-Thompson. Pondérer par l’inverse d’une fréquence de capture observée peut créer des poids arbitrairement instables et laisse intacte la masse à capture nulle. La correction proposée risque ainsi de donner une apparence de représentativité à un échantillon toujours sélectionné.

**La loi nulle du duel LP/Chao est mal spécifiée.** Les estimateurs LP calculés par paires partagent sources, marges et appariements : leur dispersion ne peut être comparée à une variance théorique comme s’ils étaient indépendants. Cette dispersion mélange également dépendance de capture, hétérogénéité, erreur d’appariement et différences d’effort de capture. Un modèle log-linéaire non retenu ne falsifie ces violations qu’à la puissance effectivement testée ; A le reconnaît partiellement, mais son seuil de dispersion reste sans loi nulle justifiée.

**Les paliers d’information ne forment pas nécessairement une échelle ordinale.** Connaître la liste des familles, les seuils ou le code ne produit pas des informations emboîtées au sens de leur effet sur \(S\). Si chaque palier modifie aussi la loi des familles évaluées, l’écart entre paliers mesure conjointement l’information et le déplacement de cette loi. Le scellement chronologique empêche certains retours, mais ne rend pas les régimes comparables.

Enfin, Good-Turing estime une couverture pour une nouvelle incidence issue du même processus ; ce n’est ni une proportion du nombre de familles ni une couverture de performance. La prédiction du gain d’une nouvelle source devient non jugeable si cette source n’est pas échangeable avec les précédentes.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- La borne sur \(\varepsilon\) perd sa couverture dès que la découverte dépend de \(S\) selon un mécanisme non borné, ou que les grappes réduisent fortement la taille effective. Aucune pondération ne récupère les familles avec \(p_{ik}=0\) pour toutes les sources.
- Le duel sur les estimateurs devient non jugeable lorsque l’erreur d’appariement est corrélée aux captures : une interaction de capture et une fusion abusive produisent alors les mêmes comptes observables.
- L’écart \(D_V/D_E\) n’a pas d’interprétation de surajustement si les supports ou les distributions de difficulté ne se recouvrent pas. Il perd sa puissance lorsque la variance entre familles domine et que les effectifs par famille sont trop faibles pour estimer \(S\) avec une erreur négligeable.
- Une e-valeur ne protège contre l’arrêt optionnel que si la propriété de martingale conditionnelle survit à la dépendance entre familles et à la règle de découverte. Une simple simulation iid ne suffit pas.
- L’écart entre régimes d’information n’est identifiable comme effet du régime que si la loi d’évaluation, le budget et la statistique restent fixes.

### (c) Contrôles négatifs dont l’absence serait fatale

1. **Population à vérité connue avec appariement non bijectif**, erreurs de fusion/scission et captures dépendantes : sans elle, impossible de distinguer biais d’estimateur et biais de lecteur.
2. **Deux lots scellés tirés indépendamment de la même loi**, à tailles égales, défense figée : l’écart doit suivre la loi nulle. Sans ce contrôle externe aux familles vues, le diagnostic de généralisation n’est pas calibré.
3. **Monde nul à visibilité hétérogène mais indépendante de \(S\)** : la procédure de corrélation et de pondération ne doit déclarer ni biais ni correction substantielle. Sinon, elle fabrique le signal qu’elle prétend mesurer.
4. **Double exécution à information identique** pour les paliers, et simulation à arrêt optionnel sous dépendance : la première doit produire un écart nul en loi ; la seconde doit conserver le niveau nominal. À défaut, Q4 et Q5 ne sont pas validées.

## Sur la proposition B

### (a) Défauts de méthode

**Le duel 1 teste une hypothèse autre que celle énoncée.** LP sous ses hypothèses ne peut être falsifié par des mondes où ces hypothèses sont volontairement violées ; seule sa robustesse hors modèle est testée. L’issue « LP surestime \(N\) » contredit en outre le mécanisme de dépendance positive et d’hétérogénéité discuté ensuite par B, qui conduit plutôt à une sous-estimation. Enfin, une meilleure performance de Chao n’est pas démontrée par une simple différence entre estimateurs.

**Le contrôle du duel 2 contredit la définition par proportion.** Une défense échouant sur une seule famille ne viole pas nécessairement « proportion d’échec au plus \(\varepsilon\) » lorsque \(\varepsilon>0\). Exiger que les deux définitions la rejettent impose implicitement \(\varepsilon=0\) et décide donc du duel par construction. Pire cas et proportion répondent à des estimands différents ; leur puissance n’est comparable qu’à énoncé cible commun.

**Le test d’indépendance à deux sources est inapplicable tel quel.** La cellule « non captée par les deux sources » est inobservée et dépend précisément de \(N\). Un chi² ou un test exact sur une table complétée par un \(N\) estimé serait circulaire. Avec les cinq sources prévues (RAPPORTÉ), seuls certains modèles et certaines interactions sont testables, sous conditions de parcimonie. Le contrôle par partition aléatoire d’un ensemble unique est également inadéquat : une partition crée des captures disjointes, donc dépendantes, et non des captures indépendantes.

**La convention \(m=19\) est préférée sans recodage cohérent des marges.** Conserver \(28\times25\) tout en changeant seulement \(m\) laisse des unités différentes au numérateur et au dénominateur. Reconnaître la non-bijectivité ne corrige pas ce défaut.

**Les journaux de refus ne sont ni indépendants ni une source de capture.** Ils sont internes au programme et ne fournissent pas, par construction, un dénombrement comparable aux autres sources. La Q3 de B appelle par ailleurs « validation extérieure » une simulation à vérité connue : c’est une validation interne au modèle simulateur.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- Le recouvrement entre familles extérieures et répertoire interne n’estime la masse manquante que si la source extérieure suit la même loi de capture, ou si un transport de loi identifiable est disponible. Un banc conçu par un mécanisme différent ne calibre donc pas directement Good-Turing.
- Le modèle log-linéaire perd toute conclusion utilisable lorsque les cellules observées sont trop creuses pour distinguer interactions et cellule manquante ; un non-rejet n’établit alors pas l’indépendance.
- Le plan bêta-binomial perd sa couverture si la loi entre familles est discrète, multimodale ou dépendante de la découverte. Augmenter les éléments par famille ne compense pas un manque de familles indépendantes.
- Un kappa élevé mesure l’accord, pas l’exactitude. Il devient non probant si les erreurs des lecteurs sont corrélées ou si les cas non bijectifs sont exclus de son calcul.

### (c) Contrôles négatifs dont l’absence serait fatale

1. **Captures de Bernoulli indépendantes sur une population exhaustivement connue**, avec cellule doublement nulle connue du simulateur : le test ne doit pas rejeter au-delà de son niveau. C’est ce contrôle, et non une partition, qui valide le duel d’indépendance.
2. **Jeu d’appariement à vérité connue**, incluant faux positifs, faux négatifs et recouvrements non bijectifs : sans lui, ni kappa ni propagation dans \(\widehat N\) ne mesurent l’erreur réelle.
3. **Deux validations distinctes pour la couverture** : un lot extérieur de même loi, où la calibration est attendue, et un lot de loi différente, où la procédure doit s’abstenir plutôt que convertir le recouvrement en couverture.
4. **Monde nul pour les deux définitions d’universalité**, avec énoncés et tolérances explicites : le pire cas et la proportion doivent seulement respecter leurs propres niveaux d’erreur, sans contrôle qui les oblige à rendre le même verdict.

## Sur la proposition C

### (a) Défauts de méthode

**L’universalité pondérée par la couverture repose sur une identité non démontrée.** L’inégalité proposée, faisant intervenir \(\widehat C(1-\varepsilon)\), exigerait au minimum une borne inférieure simultanée sur la masse couverte et une borne de réussite conditionnelle sur cette même masse. C ne déclare ni ne teste ces conditions. Surtout, toute la masse non couverte peut être en échec : la définition écarte donc par construction précisément la zone que « robustesse à l’inconnu » prétendait traiter.

**Les duels ne sont pas exclusifs et leurs métriques ne sont pas commensurables.** Dans le duel 1, Chao est une borne inférieure : lui imposer la même couverture bilatérale et la même RRMSE qu’un estimateur ponctuel mélange deux objectifs. Chapman peut conserver une meilleure RRMSE tout en ayant une couverture insuffisante, sans que cela falsifie l’utilité d’une borne. Dans le duel 2, quantile de queue et équivalence des moyennes testent des énoncés différents. Le scénario bimodal choisi favorise structurellement le premier, tandis qu’un générateur bêta-binomial identique au modèle d’inférence favorise ce dernier par construction.

**Le choix du grain d’appariement est présenté comme une nécessité trop forte.** C fournit elle-même un recodage fin cohérent et un recodage grossier cohérent. Le grain grossier n’est donc pas la seule possibilité algébrique ; le choix porte sur la dépendance de capture induite par le recodage, pas seulement sur l’arithmétique. Par ailleurs, \(Q_1\) et \(Q_2\) sont définis dès deux sources, même si leur instabilité peut rendre la borne peu informative.

**Le palier informé introduit une fuite construction/évaluation.** Filtrer ou paramétrer les éléments à partir des seuils, puis estimer \(S\) sur ces mêmes éléments, produit une statistique conditionnée par la sélection. Elle ne mesure ni la même loi que le régime aveugle ni une performance non biaisée dans le régime informé. Sans échantillon de score distinct, la comparaison des paliers est non jugeable.

**La question sur les refus dépasse ce que les données identifient.** Lorsque \(p_{ik}=0\) pour toutes les sources, la vraisemblance ne renseigne ni le nombre ni la performance dans cette zone. Convertir manuellement des journaux en nouveaux schémas crée une autre source et une autre loi ; cela ne valide pas une extrapolation par propension au refus. Enfin, les deux passes de consignes proposées au bloc 4 ne peuvent être fusionnées comme une seule occasion de capture si leurs lois diffèrent.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- La couverture \(\widehat C\) ne borne aucun risque global si la corrélation entre visibilité et performance est non restreinte ; la borne peut même devenir arbitrairement optimiste après estimation.
- Le quantile hiérarchique n’identifie la queue que sous sa forme paramétrique lorsque le nombre de familles tenues à l’écart est insuffisant pour l’observer directement. Sa puissance apparente disparaît sous loi de queue mal spécifiée.
- Les interactions log-linéaires et les poids de Horvitz-Thompson deviennent instables lorsque les fréquences de capture sont rares ; les singletons ne fournissent pas les probabilités d’inclusion individuelles.
- La règle séquentielle perd son niveau si sélection par seuil, regards multiples et dépendance entre familles interviennent avant la décision d’arrêt.
- L’étalonnage de dépendance sur une population neutre ne se transporte pas nécessairement à la population étudiée : une covariance a priori issue de ce banc doit rester une hypothèse de modèle, non une mesure de l’indépendance réelle.

### (c) Contrôles négatifs dont l’absence serait fatale

1. **Monde où toutes les familles observées réussissent et toute la masse à capture nulle échoue** : la procédure fondée sur \(\widehat C\) doit refuser l’énoncé de robustesse globale. Sinon, elle valide par construction une zone invisible.
2. **Mondes hors du modèle ajusté**, avec loi de queue non bêta-binomiale, dépendance et appariement non bijectif : couverture et niveau doivent être rapportés séparément pour l’estimateur central et pour la borne inférieure.
3. **Séparation scellée entre éléments de sélection et éléments de score**, accompagnée d’un palier répété à information identique : sans décision nulle dans ce dernier et sans échantillon de score vierge, l’effet du régime informé est confondu avec la sélection.
4. **Censure simulée indépendante, puis censure dépendante de la performance** : dans le second monde, la procédure doit reconnaître l’absence de borne identifiable. À défaut, la question sur les refus produit une garantie que les observations ne peuvent pas soutenir.

FIN-DE-CELLULE