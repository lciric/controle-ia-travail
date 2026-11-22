**Pièces.** B, C, D et E sont reçues, chacune terminée par sa ligne de fin, aucune ne paraît coupée. Le bloc FAITS ne contient aucun fait empirique. Tous mes chiffres sont des calculs d'ordre de grandeur sur les chiffres illustratifs des propositions, donc **illustratifs** et à refaire. Je ne modifie aucun statut ; je signale ceux qui contredisent leur propre justification.

## Sur la proposition B

**(a) Défauts de méthode**

- **E0 est vrai par réglage.** L'AUROC du dommage dépend de l'intensité d'attaque, que l'équipe choisit. Atteindre 0,9 teste le curseur, pas le modèle. L'intensité doit être fixée par un critère externe (furtivité par étape) avant de regarder le dommage. La zone 0,75–0,9 ne falsifie rien (B4).
- **Type 1, borne de délai.** Le délai log(1/α)/ε ne vaut que pour une CUSUM dont l'incrément est le vrai log-rapport de vraisemblance de l'attaque. Un détecteur calibré sur les seules exécutions honnêtes ne le connaît pas. Une attaque à grand D peut déplacer la loi du score dans une direction que la statistique n'intègre pas (variance réduite, déplacement vers le bas). La deuxième inégalité est donc violable avant toute expérience, sauf test par mélange dont le coût additionnel n'est pas déclaré.
- **Type 1, critère « un seul point ».** Le maximum sur des familles et des configurations est un supremum d'estimations bruitées. Un point peut tomber dans « dommage ≥ δ et D < ε » par simple erreur d'estimation des deux coordonnées. Aucune règle d'incertitude n'est prévue.
- **Type 1, familles tenues à l'écart.** Les couches sont « choisies sur un ensemble de validation » dont la composition en familles n'est pas dite. Si la famille tenue à l'écart y figure, il y a fuite.
- **Type 2, trois facteurs confondus.** Le mécanisme change à la fois la modalité (activations), l'agrégation (CUSUM) et l'usage de références propres à la tâche. Les comparateurs (a), (b), (c) ne couvrent pas le plan factoriel. Il manque le maximum par étape du score d'activations et la CUSUM du score texte contre les mêmes références. H_A et H_B ne sont pas exhaustives : « les activations suffisent sans accumulation » n'est attribuable à aucune.
- **Type 2, lecture de la consigne.** Si l'attaque passe par une consigne dans le contexte, les activations codent la présence de cette consigne. Le contrôle 3 (encodeur externe sur le texte émis) ne voit pas ce canal. Le détecteur pourrait signaler « consigne présente » et non « résultat dégradé ».
- **Type 2, longueur.** Sommes et CUSUM croissent avec le nombre d'étapes. Si l'attaque change la longueur des trajectoires, le gain est confondu avec elle.
- **Type 3, D_activations > D_texte.** Les activations d'une étape contiennent les jetons émis. Par l'inégalité de traitement de l'information, un lecteur assez expressif obtient D_act ≥ D_texte par construction. La comparaison mesure la capacité des deux moniteurs, pas les modalités. La grandeur informative est le gain conditionnel au texte.
- **Type 3, hypothèse jointe.** « Pente × D ≈ 1 » teste à la fois l'indépendance des étapes, la justesse du log-rapport de vraisemblance et l'estimateur de D. H_B n'attribue l'échec qu'aux deux premières causes. Le contrôle positif synthétique i.i.d. vérifie la loi par construction et ne lève que la troisième.

**(b) Conditions de perte de puissance**

- **Calibration conformale.** La plus petite valeur-p atteignable avec n références est 1/(n+1). Avec 8 références par tâche, elle vaut environ 0,11, donc α = 1 % est inatteignable par tâche. Il faut n ≥ 99, ou une mise en commun entre tâches qui suppose l'échangeabilité entre tâches, non testée.
- **Estimateur de D.** Un estimateur par histogramme à k classes sur n points a un biais positif d'ordre (k−1)/(2n). Si ε est sous le plancher D̂ mesuré honnête contre honnête à même n, la région « D < ε » est non jugeable. Si les supports des scores sont disjoints, D̂ diverge.
- **Pente.** Pour un incrément Z quelconque, délai ≈ h/E₁[Z] et log ARL₀ ≈ θ*h, où θ* résout E₀[exp(θZ)] = 1. La pente vaut 1/(θ*·E₁[Z]). Elle n'égale 1/D que si Z est le vrai log-rapport.
- **Censure.** Si log(ARL₀)/D dépasse T − t, le délai est censuré. Si l'étendue de log ARL₀ est faible (bornée par le nombre d'étapes honnêtes disponibles), la pente n'est pas estimable.
- **Non-stationnarité.** Si l'attaque concentre ses touches, D est une suite D_t. Le scalaire D̂ est alors une moyenne qui ne détermine plus le délai.
- **Taux de détection à 1 % de fausses alertes.** Avec 200 tâches comme unités indépendantes, le seuil repose sur environ 2 tâches. Sa variance domine les marges de 5 et 15 points.

**(c) Contrôles négatifs dont l'absence serait fatale**

1. Une **consigne placebo** : consigne adverse présente mais dommage nul, ou inversement dommage injecté sans consigne (sources empoisonnées). Sans elle, le type 2 ne sépare pas intention et dégradation.
2. Le **plancher D̂ honnête contre honnête**, par modalité, à effectif et dimension identiques à ceux des comparaisons attaquées.
3. Un **brassage temporel** des scores réels attaqués au sein de chaque trajectoire. Si pente × D revient à 1 après brassage, la cause est l'autocorrélation. Sinon, c'est la spécification du log-rapport.
4. Des **honnêtes appariés en longueur**, et des honnêtes sous dérive bénigne (ordre des documents, format). J'emprunte ce dernier contrôle à C en le disant.

## Sur la proposition C

**(a) Défauts de méthode**

- **Statuts.** Plusieurs références sont dites « citées de mémoire » et portent VÉRIFIÉ. Les deux mentions sont incompatibles. Je ne requalifie pas, je le signale à l'arbitre.
- **Type 1, pas de garantie de puissance.** L'inégalité de Ville borne les fausses alertes sous échangeabilité. Rien ne borne le taux d'échec silencieux par α : il dépend de l'alternative. La dichotomie « la martingale franchit 1/α ou la trajectoire reste dans un tube de rayon ε » exige un lien entre score de non-conformité et perte d'utilité, qui n'est ni posé ni mesuré. Le type 1 se réduit à un test empirique sur trois familles.
- **Type 1, fuite calibration/métrique.** Les 50 références servent à estimer la covariance de Mahalanobis et à fournir les rangs conformes. Les points de calibration sont dans l'échantillon, les points testés ne le sont pas : l'échangeabilité est rompue par construction. Avec n = 50 trajectoires et d de l'ordre de 4 096, la covariance est singulière et les distances intra-échantillon sont dégénérées.
- **Type 1, fenêtres chevauchantes.** Les valeurs-p des fenêtres w ∈ {1, 4, 8} sont dépendantes sous l'hypothèse honnête. Le produit n'est plus une martingale de test.
- **Type 1, attaque par gradient sur les activations.** Elle intervient sur la grandeur que le moniteur lit : le déplacement est vrai par construction, et ce n'est pas une « petite touche » au sens du cadre.
- **Type 1, attaques définies par l'instrument.** La contrainte p ≥ 0,10 à w = 1 garantit l'indétectabilité à cette échelle par construction. Elle ne peut pas figurer comme résultat.
- **Type 2, régression dans le mauvais sens pour l'hypothèse.** Le résidu r_t = ‖z_texte − W·h‖ mesure ce qui, dans le texte, n'est pas prédit par les activations. Une composante interne absente du texte (ce que H_A postule) est envoyée par W vers zéro, puisque W est ajusté sur des exécutions honnêtes où elle ne varie pas. La statistique est aveugle par construction au signal attendu. E régresse dans l'autre sens (texte → activations), cohérent avec la même intuition ; je m'en sers ici contre C.
- **Type 2, détection et correction confondues.** La « réécriture contrainte » fait dépendre la réduction de dégradation de l'oracle. H_A et H_B n'ont pas le même comparateur (meilleur moniteur ou somme pondérée contre moniteur d'activations seul). L'intervalle 0,03–0,15 n'est attribué à personne.
- **Type 3, attaque définie dans les coordonnées de l'instrument.** L'amplitude est bornée à 0,25 écart-type dans la projection y_t qui sert à la mesure. Si la touche est un biais persistant, la pente positive retrouve la structure temporelle injectée.
- **Type 3, choix de la projection.** La première composante principale des trajectoires honnêtes risque de coder l'avancement de la tâche, c'est-à-dire une tendance déterministe. Cela donne μ > 0 chez les honnêtes et favorise H_B par choix d'axe.
- **Section (c), arithmétique.** Un taux de 0,05 par fenêtre sur 8 fenêtres disjointes donne jusqu'à 1 − 0,95⁸ ≈ 0,34 par trajectoire, pas 0,15.

**(b) Conditions de perte de puissance**

- **Martingale.** Le franchissement de 1/α demande Σ_t E₁[log f(p_t)] ≥ log(1/α). Sous la contrainte p_t ≥ 0,10, la croissance par étape est bornée par log sup f sur [0,1 ; 1]. Si T fois cette borne est inférieur à log 20, aucune détection n'est possible quel que soit le dommage.
- **Effectif conforme.** Les unités échangeables sont les trajectoires (50), pas les 2 000 étapes. La granularité des valeurs-p est 1/51.
- **Variance d'Allan, aveuglement.** Elle est invariante à tout décalage constant de moyenne. Un biais introduit dès la première étape ne laisse aucune signature. Seules les rampes sont vues.
- **Variance d'Allan, degrés de liberté.** Avec T = 64 et τ = 16, l'estimateur chevauchant a environ 4 degrés de liberté équivalents. L'écart-type de la pente entre τ = 8 et 16 est alors de l'ordre de 1 par trajectoire. Pour Δμ = 0,7, l'AUC attendue est d'environ 0,7. Le critère AUC ≥ 0,85 de H_A est inatteignable sous ses propres exposants. Seule la moyenne de groupe est estimable.
- **pAUC sur [0 ; 0,05].** Avec 100 trajectoires honnêtes, 5 points définissent la région.
- **Résidu de W.** Avec 1 500 étapes pour des dimensions de l'ordre de 10³, le résidu hors échantillon est dominé par la nouveauté de la tâche. Si la variance inter-tâches de la moyenne du résidu dépasse l'effet d'attaque, la CUSUM intègre le sujet, pas l'attaque.

**(c) Contrôles négatifs dont l'absence serait fatale**

1. Un **découpage conformal** : ajustement de la métrique et calibration sur des trajectoires disjointes.
2. Un **W ajusté sur des paires désappariées** (h_t, z_t′) et des honnêtes hors sujet, pour le plancher du résidu.
3. Des **injections synthétiques d'exposant connu** (bruit blanc, marche aléatoire) à T = 64, pour valider l'estimateur de μ à cette longueur.
4. Une **attaque à décalage constant**, à laquelle l'instrument doit rester aveugle, et des honnêtes détendancés.
5. La **martingale sur honnêtes stratifiés par indice d'étape**, pour isoler la non-stationnarité ordinaire.

## Sur la proposition D

**(a) Défauts de méthode**

- **Type 1, m est une propriété du dossier.** Le duel se tranche par énumération combinatoire sur des dossiers que l'équipe rédige. Elle choisit donc m en choisissant la règle de conclusion et la table. Aucun agent ni adversaire n'intervient. Le résultat est vrai ou faux par conception des dossiers.
- **Type 1, ontologie partagée.** Obligations et dégradations sont définies dans les mêmes unités (cases). Une attaque hors ontologie est invisible, par exemple un corpus empoisonné dont les cases sont « valides » au regard de la source. Un dommage gradué qui n'inverse pas la conclusion est écarté par définition de « grave ».
- **Type 1, niveau de H_A.** L'hypothèse est énoncée par dossier. La fraction de dossiers qui doit la satisfaire n'est pas fixée. La sélection des dossiers à grand m fait le résultat.
- **Type 2, signal de rapport contre signal de case.** Si l'attaque marque tout le rapport, une sonde reconnaît « rapport attaqué » et n'importe quel tirage interne trouve ensuite une case invalide. Le contrôle par permutation ne dit pas si l'on permute à l'intérieur d'un rapport ou entre rapports. À l'intérieur, le gain survit et serait lu à tort comme « non mécaniste ».
- **Type 2, comparateur dépendant de l'adversaire.** Un adversaire qui minimise le nombre de cases vise les plus influentes. La « priorité aux cases influentes » est alors quasi optimale par construction. Un adversaire qui les évite la ruine. Le verdict dépend de la loi de l'adversaire sur les cases, fixée par l'équipe.
- **Type 2, fausse alerte mal définie.** L'alerte dépend du seul vérificateur exact. Le taux de fausses alertes sur rapports honnêtes est donc la probabilité de tirer une case honnêtement invalide. Un meilleur sélecteur l'augmente. Le plafond de 5 % pénalise ce qu'on veut mesurer.
- **Type 3, quasi-tautologie.** D·I ≈ h est l'identité de Wald pour une somme à dérive I : elle tient pour tout processus à incréments de moyenne stable. Avec I estimé à part, on teste l'homogénéité d'une moyenne entre deux moitiés de dossiers. Le contenu non trivial de la loi (lien entre h et le taux de fausses alertes) n'est pas testé. B le teste ; je le dis sans fusionner.
- **Type 3, sélection des régimes.** La restriction « au débit positif » ne dit pas sur quel découpage elle est faite. Sur les données d'estimation, I est surestimé et les délais sont sous-prédits.

**(b) Conditions de perte de puissance**

- **Borne.** Elle vaut au plus (1 − m/N)^b. Pour b = 3 et un seuil de 10 %, il faut m/N ≥ 0,54 environ. Plus de la moitié des cases doivent être invalides dans tout rapport grave, ce qui contredit le régime « petites touches ». Quand m/N est petit, la borne vaut à peu près 1 − b·m/N et est vide. Sinon il faut b ≈ 2,3·N/m, incompatible avec le budget du type 2.
- **Erreurs honnêtes.** Si une case honnête est invalide avec probabilité q, un rapport honnête déclenche avec probabilité 1 − (1−q)^b. Dès que q est comparable à m/N, la règle « une case invalide = alerte » ne discrimine plus. Passer à un seuil k > 1 change la borne.
- **Vérificateur imparfait.** Avec une sensibilité s < 1, la non-détection devient environ (1 − s·m/N)^b. D le reconnaît par son garde-fou. Le domaine couvert se réduit aux obligations décidables exactement.
- **Zone non tranchée du type 2.** Avec quelques dizaines de dossiers de test, la demi-largeur de l'intervalle sur un écart apparié de taux est de l'ordre de 10 points, soit le seuil. L'issue la plus probable est « ne tranche pas ».
- **Hétérogénéité de I.** Le délai moyen vaut h·E[1/I], supérieur à h/E[I], d'un facteur proche de 1 + CV². Si le coefficient de variation de I entre dossiers dépasse 0,5, le critère des 25 % échoue même quand la loi tient dossier par dossier.
- **Maximum sur K conditions.** Le critère d'erreur relative maximale perd sa puissance quand K croît. Censure : si h/I dépasse T − t₀, le duel est non jugeable (reconnu par D).

**(c) Contrôles négatifs dont l'absence serait fatale**

1. Des **rapports honnêtes passés par le même audit**, avec le taux de cases invalides q et le taux d'alerte au même b. Sans ce chiffre, la « garantie » n'a pas de taux de fausses alertes.
2. Une **AUROC intra-rapport** : cases invalides contre cases valides du même rapport attaqué. Et une permutation entre rapports, distincte de la permutation intra-rapport.
3. Un **adversaire qui évite les cases influentes**, pour que le comparateur mécanique ne gagne ni ne perde par construction.
4. Un **brassage temporel des incréments** et un débit estimé sur une famille différente, pour séparer « transport » et « identité de Wald ».

## Sur la proposition E

**(a) Défauts de méthode**

- **Statuts.** « Le bruit honnête de moyenne nulle s'annule en 1/√t » porte VÉRIFIÉ. L'énoncé suppose l'indépendance et un résidu centré sur des tâches nouvelles, ce que l'expérience devrait établir. Je ne requalifie pas, je le signale.
- **Type 1, borne U non dérivée.** L'identité télescopique est exacte, mais le tube conforme vit dans l'espace texte-activations et non dans l'espace de la valeur contrefactuelle. Le passage de l'un à l'autre est l'hypothèse de régularité que E ne mesure pas séparément. Sans audit, la borne additive est T fois le quantile par étape. Avec 0,03 par étape et T = 30, elle vaut 0,9, pas 0,25. La formule qui y mène avec B = 3 n'est pas donnée.
- **Type 1, asymétrie tue.** D̂_max est le maximum trouvé par l'optimiseur de l'équipe, donc un minorant du supremum. « Aucune attaque ne viole U » ne falsifie H_B que pour ce budget de recherche. B l'écrit, E non.
- **Type 1, oracle dépendant du modèle de menace.** Le rejeu « propre » suppose une copie de confiance. Si l'adversaire est l'agent lui-même, le rejeu est fait par l'agent compromis.
- **Type 2, contrôle (i) mal construit.** Une somme cumulée vectorielle est invariante à l'ordre des étapes. Sous H_A avec dérive persistante, la permutation temporelle ne ramène pas le gain à zéro. Le contrôle échouerait quand le mécanisme fonctionne.
- **Type 2, effet de tâche.** Le résidu d'une tâche nouvelle porte un décalage propre à la tâche, constant sur toutes ses étapes. La CUSUM l'intègre exactement comme une attaque cohérente. Le contrôle (ii), sources contradictoires, ne couvre pas ce cas.
- **Type 2, critère.** « ΔAUROC à FPR = 0,05 » mélange deux métriques. Le gain d'exactitude confond détection et réparation : un rejeu depuis t − 6 repart d'un état déjà contaminé si l'attaque est plus ancienne, et relit le poison s'il est dans les documents. « Sur au moins l'un des deux modèles de menace » double les chances de H_A sans correction.
- **Type 3, R_eff dépend de la position.** Le nombre d'étapes déviées après t₀ est borné par T − t₀. La mesure compte la descendance totale, non la descendance directe, faute de graphe de dépendance.
- **Type 3, plancher nul.** Avec un seuil au 95ᵉ centile honnête, un rejeu sans aucune touche donne en moyenne 0,05·(T − t₀) étapes « déviées ». Cela fait 1,0 à t₀ = 10 et plus de 0,30 pour t₀ ≤ 24. L'« issue sans intérêt » peut se déclencher par construction.
- **Type 3, rapport de cotes circulaire.** La corruption finale est la déviation de la dernière étape. Elle est corrélée par construction au nombre d'étapes déviées. Classer chaque perturbation par son compte réalisé, c'est conditionner sur l'issue. Un modèle additif sans seuil donne aussi un rapport ≥ 4 entre les queues. Rien ne teste la criticité.
- **Type 3, comparateur manquant.** La susceptibilité croît avec la précocité. « Auditer les trois premières étapes » est la référence mécanique à battre, pas le tirage aléatoire.
- **Section II, sélection par l'instrument.** Le gain marginal des activations est mesuré là où le moniteur texte échoue. Sous ce conditionnement, tout second score imparfaitement corrélé au premier montre un « gain ». C fait de même.

**(b) Conditions de perte de puissance**

- **CUSUM vectoriel.** Sous l'hypothèse nulle blanchie, ‖S_T‖²/T suit un χ² à d_eff degrés. Sous un décalage μ, la non-centralité est T·‖μ‖². La puissance exige T·‖μ‖² ≳ c·√(2·d_eff). Le « rapport signal sur bruit < 0,5 » n'est pas défini. S'il s'agit de ‖μ‖ en unités blanchies, T = 30 ne suffit que pour d_eff de l'ordre de 10.
- **Blanchiment.** Σ est estimée sur 1 500 étapes en dimension de l'ordre de 4 096. Elle est singulière. Sans réduction déclarée, r_t n'est pas défini.
- **Effet de tâche.** Si la variance inter-tâches de la moyenne du résidu est comparable à ‖μ‖², le taux de fausses alertes sur tâches nouvelles n'est pas contrôlé.
- **R_eff.** Distinguer 0,95 de 1,05 demande une erreur-type inférieure à 0,05. Cela fait de l'ordre de 400 rejeux par couple (tâche, t₀) si la variance de descendance est proche de 1, contre 4 500 continuations prévues au total. La mesure par perturbation est un entier, donc la bande est sans objet à ce niveau.
- **Horizon.** Avec g générations sur T − t₀ étapes, le contraste est R^g. Pour g de l'ordre de 5, il vaut 0,59 contre 1,61 à R = 0,9 et 1,1. La transition « nette » est arrondie par la taille finie.
- **Borne U.** Elle est non triviale seulement si T·q₀,₉₅(|ΔV|) est petit devant le dommage cible avant audit, ou si le dommage se concentre sur k étapes avec C(T−k, B)/C(T, B) petit.

**(c) Contrôles négatifs dont l'absence serait fatale**

1. Un **rejeu nul** : même préfixe, aucune touche, rééchantillonnage seul. R_eff doit être défini net de ce plancher, à position appariée.
2. Une **permutation des étapes entre trajectoires** ou une randomisation de signe des résidus, à la place de la permutation temporelle intra-trajectoire.
3. Des **honnêtes hors sujet**, pour l'effet de tâche du résidu.
4. Un **χ̂_t brassé entre étapes** et l'audit des B premières étapes, pour la vaccination.
5. Un **test de distribution des tailles de cascade** (probabilité d'extinction prédite contre observée), sans lequel le seuil de Galton-Watson n'est pas distingué d'une relation monotone.

FIN-DE-CELLULE