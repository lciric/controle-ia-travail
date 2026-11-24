# Où publier le résultat sur le filtrage en boucle, et quelles extensions : note de sortie du collisionneur

- **Date** : 2026-11-24, après 12:55 UTC.
- **Dossier** : `docs/notes/collisionneurs-reprise-2026-11-24-v1/cible-publication/collisionneur/` (branche `runs/collisionneurs-reprise-2026-11-24-v1`).
- **Accords** : GO-2026-11-24-03, -04 et -08 ; plafond de 18 dollars.
- **Dépense** : 6,48 dollars (`etat.md` du dossier) : Opus 1,87 ; Carbon 2,66 ; Neon 1,95.
- **Tours** : neuf cellules sur neuf, toutes valides : trois conceptions (tour III.1), trois critiques croisées (III.2), trois réponses (III.3). Vérification finale du dossier : « tout tient » (`journaux/verifier-cible-fille.log`).
- **Historique** : les trois conceptions ont été faites avant 06:43 UTC. Une reprise lancée à 06:43 n'a laissé aucune ligne de résultat pour la critique d'Opus (`journaux/cible-reprise-1.log`). Les six autres cellules ont été faites de 12:09 à 12:54 UTC avec la clé Anthropic du compte (`journaux/cible-reprise-2-cle-du-compte.log`). Le journal numérote « essai 3 » la critique d'Opus ; `etat.md` lui compte un essai.
- **Modèles et lettres** : Claude Opus 5.5 = lettre A ; Carbon (`gemini-4-carbon`) = lettre B ; Neon (`gemini-4-neon`) = lettre C. Selon le journal, Opus a été appelé sans provision de réflexion ; Carbon au niveau de réflexion « high » ; Neon au niveau « xhigh ».

Rédigé par un lecteur Opus 5.5, classe C, à partir des seules cellules du dossier, lues en entier, de la question et des faits. **Le lecteur est du même modèle que la lettre A.** Elle est traitée comme les autres ; le lecteur a pu être plus indulgent envers elle sans le voir.

**Ce que la note n'est pas.** Aucune cellule ne rapporte de mesure. Tout ce qui suit est argument, calcul sous hypothèses du modèle du manuscrit, ou protocole proposé. Les seuils, effectifs, heures de calcul et coûts sont qualifiés d'illustratifs par leurs auteurs. Aucun modèle n'a vu le manuscrit ni son script de vérification : seul le résumé des faits leur a été transmis.

**Ce que le lecteur a refait.** À la main, sans code, sur les seules formules des faits : la condition de l'inversion entre rejet pur et pénalité (section 2) ; la dépendance du plancher en $R_0 + C$ ; l'indépendance du rapport entre furtif et honnête vis-à-vis de la classe visible ; le freinage transitoire sous gradient sur un softmax à trois classes ; les deux façons de réaliser l'opérateur de rejet pur (section 4). Tous tiennent. Rien d'autre n'a été recalculé, en particulier l'inversion à divergence appariée (Carbon) et les niveaux exacts des tests.

**Attention aux étiquettes.** Chaque modèle numérote à sa façon ses expériences (E1 à E5 chez Opus, E1 à E4 chez Carbon, « Expérience 1 » à 4 chez Neon). Le même numéro désigne des choses différentes d'une cellule à l'autre ; la note nomme chaque expérience par ce qu'elle teste. Les statuts aussi varient. Carbon appose « vérifié » à des résultats du manuscrit qu'il n'a pas vus, et à des règles de conférences citées de mémoire. Neon le lui reproche (C, III.2), et Carbon corrige au tour III.3.

**Notations.** Trois classes de politiques : honnête (h), contournement visible (v), contournement furtif (f). La lettre $\beta$ note la probabilité de survivre au détecteur placé dans la boucle. $\eta$ est l'intensité d'optimisation. $C$ est la pénalité infligée en cas de détection. Opérateur A, ou rejet pur : $\pi_{\mathrm A} \propto \beta\, e^{\eta R}\pi_0$. Opérateur B, ou pénalité : $\pi_{\mathrm B} \propto e^{\eta[\beta R - (1-\beta)C]}\pi_0$. Les lettres A, B et C désignent aussi les modèles : la note écrit donc « Opus », « Carbon » et « Neon » quand il s'agit d'eux.

## 1. La question

Un manuscrit théorique court étudie un détecteur imparfait de désalignement placé dans la boucle d'entraînement après pré-entraînement. C'est le papier D. Il compare deux opérateurs d'équilibre de Gibbs, rejet pur et pénalité. Il établit des seuils exacts, un plancher sous pénalité et trois mécanismes d'atténuation : barrière d'accessibilité, audit tenu hors de la boucle, épisodes pièges. Un script les vérifie en arithmétique exacte et sur 14 000 tirages. Le manuscrit ne contient ni expérience sur réseaux ni preuve mécanisée. La question demande, en 3 000 mots au plus :

1. où le manuscrit actuel est déjà compétitif, et quelles objections il essuierait dans les conférences principales ;
2. quelle est la cible la plus ambitieuse réellement atteignable, et quelles cibles prestigieuses seraient un mauvais ajustement ;
3. quelles extensions mathématiques ou expérimentales apportent le gain décisif au moindre risque d'impasse ;
4. comment articuler une diffusion rapide (billet, archive ouverte) avec le double aveugle et les règles de non-promotion.

Les modèles devaient aussi proposer des expériences en duel, la mesure minimale de chaque instrument et un ancrage matériel.

## 2. En bref

- **Le résumé du manuscrit omet une condition, et c'est la trouvaille principale du dossier.** Le résumé dit qu'avec une niche parfaitement furtive, la pénalité amplifie strictement plus le furtif que le rejet pur. Neon montre au tour III.1 que c'est vrai seulement si $\eta(1-\beta_{\mathrm v})(R_0+\Delta R+C) > \ln(1/\beta_{\mathrm v})$ (C, III.1). Opus refait le calcul (A, III.2 et III.3) et Carbon l'accepte (B, III.3). Le lecteur l'a refait aussi. Avec $C = 0$ et $\eta$ petit, l'ordre s'inverse. Soit le manuscrit contient la condition, soit l'énoncé est faux sans elle. Les trois modèles demandent de le vérifier avant toute diffusion.
- **Le plancher sous pénalité dépend de $R_0 + C$, et non de $C$ seul.** Il vaut le plancher rapporté seulement si $R_0 = 0$ (C, III.1 ; précisé par A, III.2 ; accepté par C, III.3). Calcul refait par le lecteur.
- **Cible : un atelier maintenant, une conférence principale seulement avec des expériences.** Les trois modèles placent le manuscrit actuel en atelier non archivistique de NeurIPS, ICML ou ICLR. Tous trois jugent atteignable la piste principale, seulement si une expérience montre la prédiction sur un vrai modèle. Tous trois écartent COLT et ALT, les conférences de sécurité système, et JMLR comme première cible. TMLR les divise.
- **Le rejet pur n'a pas d'algorithme évident.** Les trois modèles ont proposé de l'entraîner « par rejet », sans dire comment. Les critiques montrent que l'expert itéré et le masquage de la récompense convergent ailleurs. Trois réalisations sont proposées au tour III.3, toutes différentes.
- **Personne ne parie sur une stéganographie spontanée.** Les trois proposent un banc de code dont les niches de triche sont construites et dosées, avec un oracle caché.
- **Les critiques ont surtout démoli les plans d'expérience.** Classes définies par le verdict du détecteur lui-même. Bonus de triche nul ou tiré de l'oracle. Trois à cinq graines, qui rendent les seuils inatteignables. Critères de validation des instruments qui contiennent l'hypothèse testée. Tout a été corrigé par les auteurs au tour III.3.
- **Première expérience proposée : qualifier le code d'entraînement sur un cas exact**, avant tout modèle réel. Opus le propose sur quelques heures de calcul, après une relecture gratuite du manuscrit. Carbon et Neon l'enchaînent directement avec la première expérience sur modèle ouvert : environ 40 heures de carte A100 pour Carbon, 250 à 450 heures de carte H100 pour Neon (illustratif).
- **Diffusion : prépublication sobre, aucun billet pendant l'évaluation.** Les trois modèles s'accordent sur ce point, et sur le billet après la décision. Toutes les règles de conférence sont citées de mémoire, à vérifier dans l'appel de l'année.

## 3. Ce que chaque modèle a proposé

### Claude Opus 5.5 (lettre A)

- **Présupposés** (A, III.1). Neuf présupposés. Deux comptent plus que les autres. D'abord, l'équilibre de Gibbs statique décrirait ce que produit un vrai entraînement par renforcement : c'est « le maillon le plus fragile ». Ensuite, le manuscrit serait nouveau face aux travaux empiriques sur l'obscurcissement induit par un moniteur. Opus relève aussi que $\tau_{\mathrm{ord}}$ n'est pas défini dans les faits.
- **Évaluation et cible** (A, III.1).
  - Le manuscrit est compétitif en atelier non archivistique, peut-être à TMLR, et peut-être dans une piste courte de SaTML, dont l'existence est à vérifier.
  - Six objections en piste principale. La première : trivialité perçue, car l'optimum régularisé par divergence est la loi inclinée, et un relecteur dira « sélection bayésienne évidente ». Les autres : pas de dynamique, pas d'expérience, abstraction grossière, positionnement, borne des pièges souvent vide.
  - La piste principale n'est visée que si une expérience valide ou réfute nettement deux prédictions chiffrées.
- **Extensions classées** (A, III.1) :
  1. banc d'apprentissage par renforcement à niches construites ;
  2. dynamique de type réplicateur sur la partition finie ;
  3. sondes de représentation tenues hors de la boucle ;
  4. formalisation en Lean, utile surtout pour une revue ;
  5. bornes séquentielles, au plus fort risque d'impasse.

  L'idée propre d'Opus : la difficulté de faire émerger une stéganographie spontanée peut devenir une prédiction. Il suffit de doser la masse a priori du furtif par affinage et de chercher la transition prédite par la barrière d'accessibilité.
- **Plan** (A, III.1). Cinq duels :
  - l'équilibre de Gibbs prédit-il la composition après entraînement ?
  - la barrière explique-t-elle l'absence de furtivité spontanée ?
  - l'audit hors boucle garde-t-il son taux de faux négatifs ?
  - la formalisation révèle-t-elle une hypothèse manquante ?
  - la borne des pièges est-elle opérante ?

  Coût avancé : 1 000 à 3 000 heures de carte graphique, soit 2 000 à 9 000 dollars (illustratif).
- **Défauts relevés par les autres** (III.2).
  - Le bonus de triche est nul si la récompense ne lit que les tests visibles. Il vient de l'oracle caché si elle lit autre chose (B, C).
  - L'expert itéré ne réalise pas le rejet pur : il converge vers $\beta^T$, ou vers la pénalité sans coût (B, C).
  - Le dosage par affinage change aussi la compétence, le style et la survie au détecteur (B, C).
  - Dans la condition « indépendante » de l'audit, imposer la covariance voulue exige de voir des exemples furtifs : le résultat devient vrai par construction (B).
  - Pièges tirés au hasard parmi les épisodes réels : tautologie (B, C).
  - Un énoncé faux qui ne compile pas ne prouve pas que les hypothèses sont cohérentes (B, C).
  - Un intervalle de rééchantillonnage sur trois graines exclut zéro par hasard une fois sur quatre (B, C).
- **Après les critiques** (A, III.3).
  - Opus accepte presque tout. Trois calculs d'une ligne réorganisent sa réponse : la condition de l'inversion (section 2) ; le rejet pur est linéaire en $\beta$, donc l'agrégation par classe y reste exacte ; le rapport furtif sur honnête ne dépend pas des autres classes.
  - Nouvelle expérience préalable : un arbre de séquences court où les lois sont calculables exactement. Quatre bras y sont comparés chacun à son propre point fixe prédit : filtre puis inclinaison en un tour ; expert itéré ; masquage ; pénalité.
  - Nouvelle tâche : un test visible attend une sortie contraire à la spécification. La récompense ne lit que les tests visibles, ce qui fixe le bonus par construction.
  - Nouveau détecteur : une règle qui n'inspecte jamais le corps de la solution, donc une niche parfaite garantie mécaniquement.
  - Sonde entraînée sans exemples furtifs, puis décomposition par repasse des mêmes trajectoires dans les poids gelés.
  - Il rejette deux critiques. Les pièges tirés au hasard parmi des épisodes audités sont le fonctionnement voulu, pas une vacuité. Une sonde sur les activations de la politique minore valablement la distance entre pièges et épisodes ordinaires, par l'inégalité de traitement des données.
  - Positionnement révisé : atelier et archive ouverte après correction de la condition ; TMLR si l'expérience exacte passe ; piste principale seulement si la bascule de signe apparaît au seuil prédit sur un vrai modèle.

### Carbon (identifiant gemini-4-carbon, lettre B)

- **Présupposés** (B, III.1). Six présupposés, dont deux points propres à Carbon.
  - Masquer la récompense des épisodes rejetés ne réalise pas le rejet pur, mais la pénalité à coût nul.
  - Le contournement furtif n'a pas besoin d'être une stéganographie : tout angle mort d'un détecteur imparfait suffit.
- **Évaluation et cible** (B, III.1).
  - Compétitif en atelier, à TMLR (« chance sérieuse »), et dans la piste des articles de position d'ICML au prix d'une réécriture.
  - Quatre objections : profondeur jugée élémentaire ; bonus identique pour le visible et le furtif, qui fige l'enrichissement ; confusion entre équilibre et dynamique de gradient ; absence d'expérience.
  - Cibles : SaTML, ou ICLR et NeurIPS plutôt qu'ICML.
- **Extensions** (B, III.1). Écarter la preuve mécanisée, dont le gain est jugé nul, et la stéganographie libre. Retenir une loi jointe continue de $(\Delta R, \beta)$ avec contexte ; une dynamique de gradient liée à la géométrie des représentations ; un banc de code à tests incomplets.
- **Plan** (B, III.1). Quatre duels : amplification par la pénalité contre inhibition par le partage des poids ; audit hors boucle contre contamination des représentations ; transition des pièges selon leur distance aux épisodes ordinaires ; transition d'accessibilité selon la masse a priori. Coût avancé : environ 220 heures de carte A100, soit 400 à 550 dollars (illustratif).
- **Défauts relevés par les autres** (III.2).
  - **Erreur mathématique** (C). Carbon affirmait que des représentations orthogonales font accélérer le furtif par la pénalité. Neon calcule le contraire sous gradient ordinaire sur un softmax à trois classes : la pénalité **freine** d'abord le furtif dès que la part honnête dépasse $1/\sqrt 3$. Calcul refait par le lecteur. Neon relève aussi que la notation mêle produit scalaire ordinaire et métrique de Fisher.
  - Bras de rejet pur non spécifié, alors que Carbon avait lui-même distingué le masquage (A, C).
  - Classes définies par le verdict du détecteur : enrichissement vrai par construction (A).
  - Contrôle négatif qui prédit le même signe que l'hypothèse rivale (A, C).
  - Validation des pièges par un classifieur faible : sens inversé, car un classifieur ne donne qu'une borne inférieure de la distance (A, C).
  - Ajustement à 0,90 sur quatre points : presque garanti par la seule monotonie (A, C).
  - Puissance « garantie » sans calcul (A).
  - Affinage de faible rang, qui pourrait induire lui-même le couplage testé (C).
- **Après les critiques** (B, III.3).
  - Carbon reconnaît l'erreur sur la dynamique et en fait un test : mesurer l'écart aux deux horizons, transitoire et équilibre.
  - Il rejette l'idée d'Opus qu'il faudrait un échantillonnage de rejet pour réaliser le rejet pur. Il suffit d'ajouter $\eta^{-1}\ln\beta$ à la récompense, avec la même ancre, la même initialisation et le même décodage que la pénalité (calcul refait par le lecteur ; il exige $\beta > 0$ connu par épisode).
  - Nouvelle tâche : fonctions sur entiers bornés générées à la volée, sans contamination. Un solveur de référence évalué exhaustivement sert de vérité. Trois jeux de tests sont disjoints. Le bonus va aux programmes courts, et le détecteur ne lit que les constantes littérales des tests.
  - Trois portes avant tout modèle réel : convergence sur un bandit exact ; égalité des bras sans détecteur ; invariance par translation de la récompense.
  - Plan croisé entre affinage complet et affinage de faible rang.
  - Coût révisé : environ 350 heures de carte A100, soit 650 à 850 dollars (illustratif).

### Neon (identifiant gemini-4-neon, lettre C)

- **Présupposés** (C, III.1). Sept présupposés et trois calculs sur les formules des faits, tous trois confirmés ensuite par Opus et Carbon :
  - la condition de l'inversion entre rejet pur et pénalité (section 2) ;
  - le plancher, exact seulement pour $R_0 = 0$ ;
  - le rejet pur, qui est un rejet en un pas et non un filtrage répété.

  Neon note aussi que des pièges synthétiques de support disjoint ont une distance en variation totale de 1, ce qui rend la borne identiquement nulle.
- **Évaluation et cible** (C, III.1).
  - Compétitif en atelier, et dans la piste de position s'il est réécrit. **Non compétitif à TMLR** en l'état, jugé trop élémentaire.
  - Objections : profondeur, rupture entre modèle et algorithmes, vacuité de certaines bornes, absence d'expérience dans un champ où la suroptimisation est déjà décrite.
  - Cible : piste principale après transformation, avec SaTML et TMLR comme alternatives mieux ajustées.
- **Extensions** (C, III.1). D'abord une dynamique de descente miroir, dont l'équilibre de Gibbs est le point fixe. Neon y remplace la variation totale par une distance restreinte aux discriminants que la politique peut réaliser. Viennent ensuite un banc de code à contournement structurel, puis une sonde interne comparée à un juge sur le texte. À écarter : les bornes lourdes et la preuve mécanisée.
- **Plan** (C, III.1). Quatre duels : pénalité contre rejet à divergence appariée ; modèle statique contre dépendance de chemin ; sonde interne contre juge sur le texte ; pièges disjoints mais peu discernables. Coût avancé : 500 à 1 000 heures de carte H100, soit 1 000 à 3 500 dollars (illustratif).
- **Défauts relevés par les autres** (III.2).
  - **Comparer à divergence appariée change l'estimande** (A). Carbon calcule que, dans le modèle exact, une forte pénalité y **inverse** le signe de l'écart (B). Neon aurait donc réfuté à tort sa propre hypothèse et accusé le partage des poids. Neon accepte le calcul ; le lecteur ne l'a pas refait.
  - La référence de la dépendance de chemin est fausse : retirer la classe visible change déjà la prédiction statique (A, B).
  - Classes visible et furtive définies par l'aveu dans le raisonnement écrit, c'est-à-dire par le canal même que lit le détecteur (B).
  - **La fuite la plus grave** (A). Les critères qui qualifient la sonde et les pièges contiennent l'hypothèse testée : une sonde qui donnerait raison à l'hypothèse rivale serait écartée comme défectueuse.
  - Conditionner sur un taux de triche d'au moins 0,30, qui est un résultat du traitement (A, B).
  - Cinq graines : la plus petite valeur $p$ possible vaut 1/16 en appariement. Le seuil de 0,01 est donc inatteignable (A, B).
  - La distance restreinte aux discriminants est circulaire : un classifieur ne borne pas ce que la politique apprendra (A, B).
- **Après les critiques** (C, III.3).
  - Neon accepte presque tout, et sans réserve la fuite des critères.
  - Rejet pur réalisé par un entraînement sans détecteur suivi d'un rejet en un pas : c'est exact, et refait par le lecteur.
  - Comparaison principale à intensité égale, celle à divergence égale devenant un second test de l'inversion prédite.
  - Dépendance de chemin testée à loi initiale unique, par une pénalité nulle puis pleine (idée de Carbon).
  - Quatrième classe explicite, l'échec, dans toutes les prédictions.
  - Douze graines appariées.
  - Deux rejets partiels. Le juge sur le texte garde une valeur, mais passe en mesure secondaire. Une borne exacte existe pour la classe composée de la politique et du banc de test.
  - Coût révisé : 1 200 à 2 200 heures de carte H100 pour tout le plan ; 250 à 450 heures pour la première expérience seule (illustratif).

## 4. Accords et désaccords

### Accords indépendants au tour III.1

- **Le manuscrit actuel va en atelier** (A, B, C). Le format non archivistique préserve une soumission ultérieure (règle à vérifier).
- **La piste principale exige des expériences sur modèles ouverts** et un pont entre l'équilibre statique et les algorithmes réels (A, B, C).
- **COLT et ALT sont un mauvais ajustement** : il n'y a pas de borne d'apprentissage, et en greffer une risque l'impasse (A, B, C).
- **Les conférences de sécurité système** attendent des attaques de bout en bout sur des systèmes déployés (A, B, C).
- **JMLR est une cible de consolidation**, trop lente pour une première diffusion (A, B, C).
- **Pas de stéganographie spontanée** ; des niches de triche construites dans un banc de code, avec oracle caché (A, B, C).
- **Les bornes séquentielles ou computationnelles lourdes** sont à écarter : risque d'impasse, gain douteux (A, B, C).
- **Diffusion** : prépublication sobre, aucune promotion pendant l'évaluation, code anonymisé, billet après la décision (A, B, C). Carbon ajoute une voie séparée : la théorie d'abord à TMLR avec billet, puis un article expérimental autonome (B, III.1 et III.3).
- **Chaque instrument doit battre des vérifications mécaniques** sur des cas honnêtes appariés : longueur, mots-clés, arbre syntaxique, perplexité (A, B, C).

### Convergence née des critiques

- **La condition de l'inversion** entre rejet pur et pénalité. Trouvée par Neon (C, III.1), refaite par Opus (A, III.2), acceptée par les trois au III.3.
- **Le paramètre effectif de la pénalité est $(R_0 + C)/\Delta R$.** La normalisation des récompenses par groupe, celle de GRPO, le rend non identifiable (A, III.2). Les trois abandonnent cette normalisation et ajoutent un test de translation de la récompense (A, B, C, III.3).
- **Qualifier le code sur un cas exact avant tout modèle réel.** Arbre de séquences court ou bandit à trois bras (Carbon, puis Opus contre Carbon et Neon) ; adopté par les trois.
- **Un bras de masquage, distinct du rejet pur et de la pénalité** (A, B, C, III.3).
- **Classes fixées avant l'entraînement par un critère aveugle au détecteur** : arbre syntaxique et oracle caché (Opus contre Carbon et Neon ; Carbon contre Neon) ; adopté par les trois.
- **Jeux de tests disjoints** pour la récompense, les pièges et l'oracle (Opus) ; adoptés par les trois.
- **Repasse des mêmes trajectoires dans les poids gelés**, pour séparer la sélection des séquences de la dérive des représentations (Opus, Carbon, Neon, III.2) ; adoptée par les trois.
- **Taux de faux négatifs à taux de fausses alertes fixé.** Une dérive uniforme des scores ferait sinon passer un instrument cassé pour stable (Carbon, Neon) ; adopté par les trois.
- **Pièges par mélange, de distance connue exactement** : une fraction $q$ marquée, le reste indiscernable (Opus, III.2) ; adopté par Carbon et Neon.
- **Plus de graines** : dix pour Opus, douze pour Carbon et Neon, avec un calibrage préalable du bruit entre graines.
- **Témoins de cohérence des hypothèses en Lean** plutôt qu'un énoncé faux qui ne compile pas (Carbon, Neon) ; adopté par Opus. Carbon et Neon continuent d'écarter la formalisation.
- **Critères des instruments mesurés avant l'entraînement seulement** (Opus contre Neon) ; adopté par Neon.

### Calculs refaits et calculs non refaits

Refaits par le lecteur, à la main, sur les formules des faits :

- condition de l'inversion : $\pi_{\mathrm B}(\Pi_{\mathrm f}) > \pi_{\mathrm A}(\Pi_{\mathrm f})$ si et seulement si $\eta(1-\beta_{\mathrm v})(R_0+\Delta R+C) > \ln(1/\beta_{\mathrm v})$, en niche parfaite ;
- écart d'exposant entre furtif et honnête sous pénalité : $\eta[\beta_{\mathrm f}\Delta R - (\beta_{\mathrm h}-\beta_{\mathrm f})(R_0+C)]$ ;
- rapport furtif sur honnête indépendant de la classe visible, sous les deux opérateurs ;
- freinage transitoire : la dérivée vaut $-\pi_{\mathrm v}(\pi_{\mathrm h}^2+\pi_{\mathrm v}^2+\pi_{\mathrm f}^2-\pi_{\mathrm v}-\pi_{\mathrm f})$, négative dès que $\pi_{\mathrm h} > 1/\sqrt 3$ ;
- rejet pur réalisé par la récompense corrigée $R + \eta^{-1}\ln\beta$ (Carbon), ou par un entraînement sans détecteur suivi d'un rejet en un pas (Neon) ;
- distance d'un mélange de pièges : exactement $q$ si la part marquée a un support disjoint.

Non refaits : l'inversion à divergence appariée (Carbon) ; le biais de convexité sous pénalité (Carbon, admis par Opus) ; les niveaux exacts des tests de Wilcoxon et de permutation (Opus, Carbon, Neon) ; la loi de l'ajustement sur quatre points (Neon). Opus relève qu'une inégalité de variance de Carbon est mal formée (A, III.3).

### Première expérience proposée au tour III.3

| Modèle | Première expérience | Ce qu'elle tranche | Coût avancé (illustratif) |
|---|---|---|---|
| Opus (A) | Relire le manuscrit pour y chercher la condition de l'inversion ; puis l'arbre exact à quatre bras, tabulaire puis petit réseau | Quel algorithme réalise quel opérateur ; la bascule de signe au seuil | Gratuit, puis quelques heures |
| Carbon (B) | Bandit exact à trois bras, puis bascule sur un modèle de 1,5 milliard de paramètres en affinage complet, à deux horizons | Amplification à l'équilibre, après le freinage transitoire | Environ 40 heures de carte A100 |
| Neon (C) | Arbre court exact, pilote de quatre graines entre bras identiques, puis douze graines à intensité égale, avec les tests de divergence égale et de translation | Survie de l'amplification au partage des poids | 250 à 450 heures de carte H100, soit 500 à 1 500 dollars |

### Désaccords

- **TMLR en l'état ?** Opus : plausible au III.1, puis seulement si l'expérience exacte passe. Carbon : oui, une fois la condition explicitée. Neon : non, l'algèbre serait jugée trop élémentaire (C, III.1 et III.3). Chacun s'appuie sur des critères de la revue cités de mémoire.
- **Comment réaliser le rejet pur.** Opus : filtre puis inclinaison en un tour, distillé une fois. C'est une hypothèse à capacité finie, à valider sur l'arbre exact (A, III.3). Carbon : récompense corrigée par $\eta^{-1}\ln\beta$, dans la boucle (B, III.3). Neon : entraînement sans détecteur, puis rejet en un pas (C, III.3). Ces réalisations n'ont pas été critiquées, puisqu'elles datent du dernier tour.
- **Quelle tâche.** Opus : un test visible corrompu. Carbon : un bonus aux programmes courts, sur des problèmes générés. Neon : des problèmes d'optimisation sous budget de temps, avec deux failles du banc de test. Aucune n'a été critiquée.
- **La formalisation en Lean.** Opus la garde, avec un contre-exemple certifié de l'énoncé d'inversion privé de sa condition (A, III.3). Carbon et Neon la jugent sans gain en conférence (B, C, III.1 et III.3).
- **Quelle dynamique ajouter.** Opus : réplicateur sur la partition finie. Carbon : transitoire sous gradient contre équilibre, après correction. Neon : descente miroir.
- **SaTML ou piste principale.** Carbon préfère SaTML, ou ICLR et NeurIPS plutôt qu'ICML. Neon met la piste principale en tête, avec SaTML et TMLR comme alternatives. Opus mentionne SaTML pour le manuscrit actuel seulement.
- **Les pièges tirés parmi des épisodes réels.** Opus : c'est le fonctionnement voulu (A, III.3). Carbon et Neon : c'est une tautologie (B, C, III.2).

## 5. Ce qui est neuf, ce qui est fragile

### Neuf, au regard de ce que les modèles citent comme connu

Aucun modèle ne revendique de nouveauté. Personne n'a cherché l'antériorité du manuscrit lui-même. Opus cite un travail empirique sur l'obscurcissement induit par un moniteur, et la lecture bayésienne de l'apprentissage régularisé : la nouveauté du manuscrit est une hypothèse (A, III.1). Pourraient être propres au dossier, sous réserve d'une recherche bibliographique que personne n'a faite :

- la condition exacte de l'inversion, et son traitement comme prédiction bilatérale : la bascule de signe au bon seuil est « l'élément le plus difficile à qualifier de sélection bayésienne évidente » (Neon, III.1 ; Opus, III.3) ;
- la linéarité du rejet pur en $\beta$, qui rend l'agrégation par classe exacte, contre la convexité de la pénalité (Opus, III.3 ; Carbon, III.3) ;
- la réalisation du rejet pur par la récompense corrigée $R + \eta^{-1}\ln\beta$ (Carbon, III.3) ;
- l'observation qu'un rejet pur équivaut à filtrer après coup une politique entraînée sans détecteur (Neon, III.3). Remarque du lecteur : si c'est ainsi que le manuscrit l'entend, l'opérateur A décrit moins un filtre « dans la boucle » qu'un filtre de sortie. Cela touche l'interprétation du résultat, et le manuscrit devrait le dire ;
- le freinage transitoire du furtif par la pénalité, avant son amplification à l'équilibre (Neon, III.2 ; Carbon, III.3) ;
- la difficulté de faire émerger une stéganographie spontanée, retournée en prédiction de la barrière d'accessibilité (Opus, III.1) ;
- la repasse dans les poids gelés, qui sépare sélection et dérive des représentations (Opus, Carbon, Neon) ;
- l'extinction d'une niche rare par l'estimation de la divergence en politique, comparée à une relecture pondérée de la loi initiale (Carbon, III.3).

### Fragile

- **Rien du manuscrit n'est audité.** Ni les preuves, ni le script, ni les 14 000 tirages. Le coût de maintien et $\tau_{\mathrm{ord}}$ ne sont pas définis dans les faits. Opus subordonne deux expériences à leur définition (A, III.3).
- **Le transfert de l'équilibre de Gibbs aux vrais entraînements** reste une hypothèse pour les trois. C'est l'objet même des premières expériences.
- **Les trois tâches et les trois réalisations du rejet pur datent du dernier tour** et n'ont pas été critiquées.
- **La tâche de Carbon suppose qu'aucune solution honnête n'est courte.** Le furtif y est un « contournement arithmétique ou par indexage » dont la présence dans la loi initiale n'est pas établie. Remarque du lecteur, non soulevée par les modèles.
- **Les coûts varient d'un facteur dix** pour des plans voisins : 220 à 350 heures de carte A100 chez Carbon, 1 200 à 2 200 heures de carte H100 chez Neon. Carbon compte 1,5 heure de carte A100 pour 1 500 pas sur 1,5 milliard de paramètres ; personne ne l'a discuté.
- **Les règles des conférences** (prépublication, non-promotion, durée d'évaluation de TMLR, pistes de SaTML et d'ICML) sont citées de mémoire. Carbon les marque « rapporté » ou « observé », sans source.
- **Le statut « vérifié ».** Carbon l'a apposé à des résultats non vus (C, III.2) ; il l'a corrigé (B, III.3). Plusieurs calculs « vérifiés » des trois modèles n'ont été refaits ni par un autre modèle ni par le lecteur.
- **Le lecteur est du même modèle qu'Opus**, dont les propositions sont souvent retenues ci-dessous.

## 6. Références à vérifier

Aucune de ces références n'a été vérifiée. Toutes sont citées de mémoire par les modèles, qui inventent parfois des titres, des auteurs ou des années. À vérifier sur PDF avant toute citation.

| Référence telle que citée | Qui la cite | Pour quoi faire |
|---|---|---|
| Baker et al. (2025), « Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation » | Opus (III.1) | Antériorité empirique de l'obscurcissement induit par un moniteur en boucle |
| Roger, Greenblatt (2023), « Preventing Language Models From Hiding Their Reasoning » | Opus (III.1) | Difficulté de la stéganographie spontanée |
| Korbak, Perez, Buckley (2022), « RL with KL penalties is better viewed as Bayesian inference » | Opus (III.1) | Optimum régularisé = loi inclinée ; objection de trivialité |
| Gao, Schulman, Hilton (2023), « Scaling Laws for Reward Model Overoptimization » | Neon (III.1 et III.3) | Suroptimisation déjà décrite |
| Schulman, Wolski, Dhariwal, Radford, Klimov (2017), « Proximal Policy Optimization Algorithms » | Carbon (III.1) | Algorithme d'optimisation |
| Burns, Ye, Klein, Steinhardt (2023), « Discovering Latent Knowledge in Language Models Without Supervision » | Carbon (III.1) | Sonde non supervisée |
| Goodhart (1975), « Problems of Monetary Management: The U.K. Experience » | Carbon (III.1) | Contrôle positif « sonde dans la boucle » |
| Travaux sur le contournement des moniteurs de raisonnement ; impasse connue de la stéganographie spontanée ; test de paraphrase forcée ; variante exacte de la normalisation de GRPO | Neon ; Neon ; Carbon ; Opus (tous « référence à vérifier ») | Positionnement ; oracle ; identifiabilité |
| Règles des conférences : critères de TMLR, piste des articles de position d'ICML, piste courte de SaTML, prépublication et non-promotion d'ICML, NeurIPS, ICLR et SaTML, statut non archivistique des ateliers | Opus, Carbon, Neon | Stratégie de diffusion ; à lire dans l'appel de l'année |
| Modèles et outils : Qwen2.5 et Qwen2.5-Coder (0,5 à 7 milliards de paramètres), Llama 3.1 8B Instruct, OLMo 2 7B, Lean 4 et Mathlib, vLLM, affinage de faible rang, REINFORCE et RLOO | Opus, Carbon, Neon | Versions, licences et contamination des problèmes à vérifier |

## 7. Propositions retenues et non retenues

Critères appliqués : soutien de plusieurs modèles, résistance aux critiques, coût, réversibilité, et ce que la proposition tranche pour la suite. Rappel du dépôt : toute soumission ou publication, et toute dépense de calcul, sont des décisions de Lazar. Rien de ce qui suit n'est engagé.

### Retenues

1. **Relire le manuscrit pour y chercher la condition de l'inversion et la dépendance du plancher en $R_0 + C$.** Corriger l'énoncé avant toute diffusion.
   - *Soutien.* Les trois modèles au III.3 ; calculs refaits par le lecteur.
   - *Pourquoi.* C'est gratuit, et cela décide si l'énoncé principal tient. Opus note qu'un relecteur le réfuterait avec $C = 0$ et $\eta$ petit.
2. **Dire dans le manuscrit quel algorithme réalise chaque opérateur**, et distinguer rejet pur, masquage et pénalité.
   - *Soutien.* Les trois. Carbon et Neon donnent deux réalisations exactes du rejet pur ; le lecteur les a refaites.
   - *Pourquoi.* Sans cela, toute comparaison sur un vrai modèle mesure l'algorithme et non la théorie. C'est aussi l'occasion de dire si le rejet pur est un filtre dans la boucle ou un filtre de sortie.
3. **Avant tout calcul sur carte graphique, qualifier le code sur un cas exact.** Arbre de séquences court ou bandit à trois bras : chaque bras face à son point fixe prédit, détecteur inactif, translation de la récompense, sans normalisation par groupe.
   - *Soutien.* Les trois.
   - *Coût.* Quelques heures de processeur ou de carte graphique selon Opus (illustratif).
   - *Pourquoi.* Si cette étape échoue, le reste n'a pas lieu d'être.
4. **Cible en deux temps.** Atelier non archivistique et prépublication sobre après la correction 1. Piste principale de NeurIPS, ICLR ou ICML seulement si une expérience montre la bascule de signe au seuil prédit. COLT, ALT, les conférences de sécurité système et JMLR ne sont pas des premières cibles.
   - *Soutien.* Les trois.
   - *Réserve.* Règles à vérifier ; le choix entre TMLR et atelier reste ouvert.
5. **Le banc de code à niches construites, sans stéganographie spontanée**, avec les corrections nées des critiques : classes aveugles au détecteur ; tests disjoints ; niche parfaite garantie par une règle ; repasse dans les poids gelés ; taux de fausses alertes fixé ; critères des instruments mesurés avant l'entraînement ; au moins dix graines.
   - *Soutien.* Les trois.
   - *Réserve.* Dépense à chiffrer sur devis.

### À reprendre ensuite

- **Chercher l'antériorité du manuscrit lui-même.** Commencer par Baker et al. et Korbak et al., à lire sur PDF. Si la zone revendiquée est occupée, c'est un nœud de décision.
- **Choisir l'une des trois tâches**, qui n'ont pas été critiquées. Celle d'Opus, le test visible corrompu, fixe le bonus le plus simplement. Celle de Carbon apporte une vérité extérieure par solveur exhaustif.
- **Le freinage transitoire puis l'amplification à l'équilibre** : prédiction à deux horizons, qui répond à l'objection « pas de dynamique » (Neon, Carbon).
- **La dépendance de chemin à loi initiale unique**, par une pénalité nulle puis pleine (Carbon, repris par Neon).
- **Définir le coût de maintien et $\tau_{\mathrm{ord}}$** dans le manuscrit. Les expériences sur la barrière et sur les pièges en dépendent.

### Non retenues

- **L'accélération du furtif par des représentations orthogonales** (Carbon, III.1) : réfutée par le calcul de Neon, admise par Carbon.
- **Un bonus de triche défini par l'échec aux tests cachés** (Opus, III.1) : l'oracle entre dans la récompense ; retiré.
- **Comparer à divergence appariée comme test principal** (Neon, III.1) : l'estimande change ; ce n'est plus qu'un second test.
- **Valider des pièges « peu discernables » par un classifieur faible** (Carbon, III.1) : sens inversé ; retiré.
- **Des critères d'instruments qui contiennent l'hypothèse testée** (Neon, III.1) : retirés.
- **Trois à cinq graines, rééchantillonnage sur graines, ajustement sur quatre points, conditionnement sur un taux de triche post-traitement** : non jugeables ou biaisés ; corrigés par leurs auteurs.
- **Deux initialisations différentes pour la dépendance de chemin** (Neon, III.1) : la prédiction statique diffère déjà ; remplacé.

### Ce qui reste à trancher

- Si le manuscrit contient la condition de l'inversion. C'est une lecture, à faire avant tout le reste.
- TMLR maintenant, ou atelier puis piste principale (désaccord entre Carbon et Neon, Opus entre les deux).
- Quelle réalisation du rejet pur sert de référence. Les trois sont proposées sans avoir été critiquées.
- Si la formalisation en Lean entre au plan (Opus pour, Carbon et Neon contre).
- Le devis de la première expérience sur carte graphique, dont les estimations vont de 40 à 450 heures.
