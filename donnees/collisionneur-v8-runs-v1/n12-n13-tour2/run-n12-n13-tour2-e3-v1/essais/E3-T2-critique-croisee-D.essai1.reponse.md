**Statuts et notation.** Les contenus repris des pièces servies sont **RAPPORTÉS** ; les dispositifs critiqués sont des **HYPOTHÈSES** de leurs auteurs, et mes objections sont des analyses de méthode, non des résultats observés. Les seuils chiffrés cités restent ceux des auteurs, donc **illustratifs**. Pour \(m\) observations corrélées par grappe, avec corrélation intra-grappe \(\rho\), j’utilise \(n_{\mathrm{eff}}\simeq nm/[1+(m-1)\rho]\). Pour un effet d’entraînement, multiplier les scénarios n’augmente pas le nombre \(k\) de graines indépendantes.

## Sur la proposition A

### (a) Défauts de méthode

- **D1 mesure une incitation implantée, non la pression d’Avalon.** Le comportement bénin est choisi parce qu’il ne paie que sous crédit collectif : son apparition peut n’établir que l’apprentissage de cette incitation. Le crédit permuté modifie simultanément l’attribution et la variance des mises à jour ; il n’isole donc pas le mécanisme de crédit.
- **D2 écrit une partie de sa réponse dans le simulateur.** Sous le modèle de bruit fixé, un rapport de variances peut démontrer une propriété du simulateur sans trancher la divergence empirique. Apparier le taux d’acceptation, variable post-traitement, peut en outre conditionner sur un descendant des deux traitements — le défaut de collider qu’A reprochait précédemment à D.
- **D3 risque une validation circulaire du lecteur.** Si les chutes synthétiques sont générées selon les amplitudes, le bruit et la structure séquentielle que le script ou le lecteur est censé exploiter, rappel et fausses alertes mesurent surtout l’adéquation au générateur synthétique.
- **D4 et D6 ne séparent pas assez construction et évaluation.** Les classes de coquilles peuvent guider les tactiques Lean, les scripts et la banque de test. Pour D6, utiliser les mêmes familles d’oracle pour choisir l’extraction de confiance puis revendiquer un gain expose à une fuite de sélection.
- **D5 confond transfert du signal et transfert du style.** Une sonde textuelle peut discriminer le modèle, la longueur ou le point de contrôle. Son AUROC ne démontre alors ni l’omission ni sa transférabilité.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **D1 :** un intervalle de Wilson par run est trop étroit dès que \(\rho>0\) au sein d’une graine. Avec \(k\) petit, la variance entre graines \(\tau^2\) est estimée instablement ; avec des probabilités d’apparition proches de zéro, l’absence d’écart ne distingue pas absence d’effet et variance d’estimation trop grande.
- **D2 :** le rapport de variances n’a de loi d’échantillonnage simple que sous les lois indépendantes supposées par le simulateur. Dépendance entre agents, contributions non identiquement distribuées ou queues lourdes rendent ce rapport instable et son interprétation causale indéterminée.
- **D3–D4 :** si le taux \(q\) de journaux illisibles, de traductions impossibles ou d’abstentions dépend de la présence du défaut, les rappels conditionnels aux cas évaluables sont biaisés. Choisir la meilleure classe après coup ajoute une sélection du maximum ; les effectifs positifs par classe conditionnent la puissance.
- **D5–D6 :** l’AUROC devient instable avec peu de positifs ou de négatifs indépendants et perd de l’information avec de nombreuses ex æquo, notamment pour un verdict binaire. Une prévalence \(\pi\) des verdicts faux proche de \(0\) ou \(1\) peut rendre l’ECE favorable sans information discriminante. Les intervalles de DeLong non groupés sont trop optimistes si les fiches sont corrélées par famille.

### (c) Contrôles négatifs dont l’absence serait fatale

1. **D1 :** un bras où le même comportement paie sous crédit individuel, à distribution de récompense et d’acceptation contrôlées ; sans lui, la spécificité collective reste indémontrée.
2. **D4 :** des paires d’énoncés dont la formalisation supprime subtilement une hypothèse ou change une inégalité, avec adjudication indépendante de fidélité ; prouver la mauvaise spécification serait sinon compté comme succès.
3. **D5 :** un classifieur utilisant seulement modèle, longueur et point de contrôle, plus une sonde réapprise sur la cible à budget déclaré.
4. **D6 :** permutations de confiance **à l’intérieur des verdicts et des familles**, et évaluation sur une famille entièrement gelée.
5. **Lecture de la précaution :** un contrôle de journal absent, figé ou d’événements RPC perdus imposant l’arrêt par défaut ; sinon une défaillance de mesure peut produire un faux « conforme ».

## Sur la proposition B

### (a) Défauts de méthode

- Le **canari de pression**, où le signalement diminue explicitement le score du groupe, est construit pour récompenser l’omission. Il valide au mieux ce canal incitatif, pas une pression produisant une omission spontanée ou diffuse.
- Le calcul de dilution sous contributions **Bernoulli i.i.d.** ne démontre pas le biais d’un estimateur après filtrage et mises à jour dépendantes. Il échange précisément l’objet contesté — la sélection — contre une propriété algébrique de la récompense avant sélection.
- **L’audit Platt tire une conclusion causale excessive de l’ECE.** Un ECE résiduel élevé peut provenir d’extraction, de dépendance ou de décalage de domaine ; il n’établit pas qu’un RLCR aurait un objet. Inversement, un faible ECE peut être obtenu par une prédiction presque constante.
- Le pré-test \(p_0\), l’essai Lean et le test de transfert réutilisent des objets très structurés. Sans banque de décision distincte de celle ayant servi à régler scénarios, extraction ou instruments, leurs critères mesurent une performance conditionnelle à ce réglage.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Pré-test \(p_0\) :** Wilson suppose des scénarios indépendants ou une unité correctement définie. Avec \(\rho>0\), l’intervalle est trop étroit ; près de \(p_0=0\) ou \(1\), une chute ou une hausse devient structurellement indétectable. Le plancher \(p_0-2\sigma\) et la chute \(0{,}20p_0\) ne sont pas opposables si leur largeur est inférieure à l’erreur-type de \(\widehat p_0\) ou à \(\tau\).
- **Points de contrôle répétés :** sans correction séquentielle, la probabilité d’au moins un arrêt sous la loi A/A croît avec le nombre de lectures.
- **Calibration :** avec \(F\) petit, la proportion de familles sous le seuil ECE est estimée grossièrement. L’ECE dépend du nombre de bacs, des effectifs par bac et de \(\pi\) ; après ajustement et évaluation sur données dépendantes, son estimateur est optimiste.
- **Lean :** McNemar ne tire sa puissance que des paires discordantes \(D_{01}+D_{10}\). Si ce compte est faible, ni supériorité ni équivalence ne sont établies, quelle que soit la taille nominale de la banque.
- **Transfert :** à taux de fausses alertes fixé, le « niveau du hasard » du rappel n’est pas le taux de base des omissions. Un test binomial devient non jugeable si le seuil est estimé sur peu de négatifs ou si les traces sont corrélées.

### (c) Contrôles négatifs dont l’absence serait fatale

- Un **canari où l’omission paie aussi individuellement**, pour séparer récompense de l’omission et attribution collective.
- Une **banque fraîche de familles de scénarios**, distincte de celle ayant fixé la jugeabilité de \(p_0\).
- Pour Platt, les prédicteurs constant et verdict binaire doivent entrer dans la **règle de décision**, pas seulement être affichés.
- Pour Lean, un contrôle de **preuve correcte d’une spécification altérée**.
- Pour le transfert, étiquettes permutées et classifieur style/modèle/longueur seul ; ils manquent au test proposé.

## Sur la proposition C

### (a) Défauts de méthode

- **Duel II.1 :** Platt et un classifieur sur statistiques de trace sont fusionnés en un seul bras. Le duel ne peut donc identifier ni la composante utile ni le coût d’extraction ; l’échec du composite ne démontre pas la nécessité du RLCR. Les deux hypothèses, avec leurs conjonctions et disjonctions de conditions ECE/AUROC, laissent aussi des issues où aucune n’est tranchée.
- **Duel II.2 :** passer de \(M=1\) à \(M=4\) change simultanément effectif, calcul total, informations disponibles, contenu du canal et occasions de signalement. Attribuer l’écart à la diffusion de responsabilité est non identifié.
- **Divergence 3 :** la borne en \(\ln N\), la KL et la contraction de longueur ne constituent pas, sans hypothèses supplémentaires, un estimand commun de « pression » entre best-of-\(N\), filtrage itéré et RL en ligne.
- **Duel II.3 :** vingt défauts répartis en trois classes, choisis parmi des erreurs déjà décrites, favorisent une évaluation sur ce que les instruments ont été conçus pour voir. Le meilleur résultat parmi classes introduit une sélection du maximum.
- **Résidu du catalogue :** prendre le maximum de rappel sur de nombreuses compositions mélange lacune d’opérateurs, variance de recherche et budget insuffisant. Il ne prouve pas qu’un générateur comblerait le résidu.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **II.1 :** avec validation leave-one-family-out, l’estimateur dépend de \(F\), de l’hétérogénéité \(\tau_F^2\) et des tailles de familles. Un DeLong non groupé et un bootstrap de fiches plutôt que de familles sous-estiment la variance ; les plis avec très peu d’erreurs rendent ECE et gains AUROC instables.
- **II.2 :** sous agents indépendants, \(p_{\mathrm{run}}=1-(1-p_{\mathrm{agent}})^M\). La double condition sur \(p_{\mathrm{agent}}\) et \(p_{\mathrm{run}}\) n’est donc pas une confirmation indépendante et peut rejeter une vraie baisse par agent. Avec corrélation intra-run \(\rho>0\), Fisher/McNemar au niveau trajectoire exagère \(n_{\mathrm{eff}}\).
- **II.3 :** sur vingt positifs, le rappel varie par pas de \(0{,}05\) ; par classe, les pas sont plus grossiers. La puissance de McNemar dépend des discordances, non de \(N=40\). Si timeout et abstention ont une probabilité \(q\) différente selon défaut ou bras, les rappels complets sont biaisés.
- **Résidu :** pour \(J\) compositions, \(E[\max_j\widehat R_j]\) croît avec \(J\) et avec leurs variances, même si tous les vrais rappels sont égaux. Une comparaison non corrigée de ce maximum fabrique un résidu variable avec l’effort de recherche.

### (c) Contrôles négatifs dont l’absence serait fatale

1. **II.1 :** bras Platt seul, classifieur seul et extraction sans statistiques de trace, tous évalués sur une famille gelée ; sinon l’attribution du gain reste impossible.
2. **II.2 :** \(M=1\) répété quatre fois à calcul apparié, \(M=4\) sans canal partagé contre canal partagé, et messages de pairs permutés. Sans eux, « diffusion » et simple information supplémentaire restent confondues.
3. **II.3 :** mutations de sens dans la formalisation et banque inédite par classe.
4. **Précaution :** incidents spontanés sans contrat, indépendamment adjudicés, injectés dans des tâches ordinaires. Les seuls appels RPC sous contrat et scénarios paramétriques ne ferment ni l’aveuglement de cible ni la reconnaissance du régime d’évaluation.

## Sur la proposition E

### (a) Défauts de méthode

- Le duel crédit conditionne \(d\) aux **occasions évaluables**, potentiellement post-traitement. Publier séparément les non-évaluables ne supprime pas le biais de sélection de l’estimand principal.
- Dans le duel catalogue, exclure du rappel les sorties non analysables peut avantager le générateur ouvert : échec de syntaxe, timeout et abstention doivent appartenir à un estimand explicite, non disparaître du dénominateur.
- Le duel preuve reste conditionné aux énoncés formalisables ; la fidélité de traduction est mesurée, mais aucun estimand ne dit comment extrapoler aux erreurs de spécification non représentées.
- La perte de transfert \(L\) dépend du budget d’apprentissage de la sonde réapprise sur la cible. Sans le fixer, \(L\) mélange transférabilité et quantité de données cible.
- La règle commune par bornes d’incertitude ne précise ni méthode d’estimation groupée ni risque séquentiel ; elle ne suffit donc pas à rendre les cinq duels opposables.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- Pour \(d\), si les taux de non-évaluabilité \(q_C,q_I\) dépendent du bras ou de l’omission, l’estimateur cas-complets n’identifie pas l’effet sur toutes les occasions ; il faut des bornes de sélection ou une loi de manque supposée.
- Pour tous les duels entraînés, la variance est dominée par \(\tau^2/k\) lorsque les scénarios sont nombreux mais les répétitions peu nombreuses. Les intervalles fondés sur les occasions seules sont alors trop étroits.
- Pour rappel et fausses alertes, peu de positifs ou d’honnêtes indépendants rendent les plafonds appariés instables ; avec des scores très ex æquo, le taux de rejet fixé n’est pas reproductible.
- Pour la confiance, \(\pi\) proche d’une borne et peu de verdicts faux par famille rendent le gain à rejet égal non estimable. Pour \(L\), ignorer la variance d’apprentissage de la sonde cible peut inverser artificiellement son signe.

### (c) Contrôles négatifs dont l’absence serait fatale

- **Crédit :** un traitement placebo à scalaire de récompense et variance de mise à jour comparables mais attribution permutée ; modèle gelé et A/A ne suffisent pas à isoler le crédit.
- **Catalogue :** un générateur placebo produisant des opérateurs syntaxiquement valides mais sans information sur les défauts, avec non-évaluables comptés.
- **Preuve :** énoncés valides dont la formalisation omet une hypothèse, afin de détecter les succès sur mauvaise spécification.
- **Confiance :** une partition A/A de réglage et d’évaluation mesurant l’optimisme de recalibration.
- **Transfert :** plusieurs réapprentissages cible à budget gelé ; les contrôles de permutation et de style déjà proposés ne ferment pas cette variance.

FIN-DE-CELLULE