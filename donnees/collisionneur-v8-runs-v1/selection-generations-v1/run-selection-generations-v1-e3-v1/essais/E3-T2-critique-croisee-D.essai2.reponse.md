Sauf reprise explicite des faits, les inférences ci-dessous sont des **HYPOTHÈSES** de méthode. Les seuils discutés restent ceux proposés par les auteurs, sans leur donner un statut de résultat.

## Sur la proposition A

### (a) Défauts de méthode

- **E1 : le contrôle sur T0.5 déjà lue ne mesure pas une fuite.** Il change simultanément la banque, sa distribution, son historique de calibration et potentiellement \(N\), \(m\) et la difficulté des témoins. Une puissance supérieure sur T0.5 peut donc venir d’un signal plus facile, non d’une exposition antérieure.
- **E1 et E2 opposent des hypothèses non exhaustives.** Entre les taux de promotion de 0,30 et 0,70, ou entre \(\alpha\) et \(\alpha+0{,}05\), aucune conclusion n’est définie. Surtout, le taux de faux témoins promus est un taux d’erreur par témoin, pas le FDR de l’ensemble des promotions.
- **E2 : les filles d’éliminées ne sont pas un contrôle non exposé.** Leurs parents ont reçu un verdict sur \(E_1\), et l’élimination est elle-même une information susceptible de guider la descendance ou la mémoire. Ce contrôle ne localise donc pas le canal de fuite.
- **E3 confond contenu sémantique et longueur de contexte.** Le bras S reçoit moins de texte que SE et SE-perm. Les raisons permutées peuvent aussi devenir incohérentes : l’effet mesuré serait alors celui d’une archive moins crédible, pas celui de la « raison ». Enfin, redites et nouveauté sont définies par la mémoire que l’expérience devrait évaluer : circularité.
- **E4 conserve une circularité malgré \(E_3\) fraîche.** P est sélectionné pour réussir au pôle, puis tous les bras sont évalués par le même type de juge, de nuls et de moniteurs. Une épreuve nouvelle supprime la réutilisation littérale, pas l’avantage conféré par l’alignement d’instrument. Les coûts, tailles et diversités des bassins parentaux ne sont par ailleurs pas appariés.
- **E5 mesure l’accord, pas la validité.** Un kappa élevé peut certifier une convention partagée erronée. Le contrôle sur fiches éliminées n’est pas décisif : nouveauté et survie n’ont aucune raison d’avoir la même distribution dans cette population.
- **E6 reste vrai dans le seul monde paramétré pour produire des lignées.** Le monde plat contrôle certains artefacts de tirage, mais ne donne aucune borne sur une population réelle de fiches.

### (b) Conditions statistiques de perte de puissance ou de non-jugeabilité

- **Dents et multiplicité.** En approximation iid, si \(d_i\) est le gain d’information par épisode de la loi \(i\), sa log-richesse croît comme \(N d_i\), alors que le seuil croît comme \(\log(m/\alpha)\). Lorsque \(N d_i\) reste de l’ordre ou au-dessous de ce seuil, la puissance tend vers zéro, indépendamment du nom donné à la « force » du témoin.
- **Réutilisation adaptative.** Après sélection sur \(E_1\), une nouvelle e-valeur calculée sur \(E_1\) n’a plus nécessairement \(\mathbb E[e_{g,i}\mid\mathcal F_{g-1}]\le1\) sous le nul : la loi et son pari sont devenus des fonctions de \(E_1\). La garantie conditionnelle qui fonde Ville et e-BH peut donc disparaître.
- **R contre F.** Si \(P_{E_1}\neq P_{E_2}\), l’estimateur \(\widehat{\Delta}_{R-F}\) mélange effet de réutilisation et différence de distribution ; il n’identifie pas la fuite sans permutation croisée des lots.
- **Héritage et ablation.** Les fiches sœurs sont corrélées par prompt, parents et banque : l’effectif indépendant est le nombre de lignées ou de populations, pas le nombre de fiches. Pour \(S/C=\text{promues}/\text{coût}\), des comptages \(S\) proches de zéro produisent une distribution fortement discrète, des ratios instables et des cas \(0/0\).
- **Lecture de nouveauté.** Lorsque la prévalence des « redites » est proche de zéro ou de un, le kappa peut être faible malgré une exactitude élevée. Sans vérité externe sur « décisive pour une porte », ce dernier critère n’a pas d’estimateur.

### (c) Contrôles négatifs dont l’absence serait fatale

- **E1–E2 :** une réutilisation fictive sans sélection ni retour sur \(E_1\), avec mêmes lots échangés entre R et F ; des filles nulles produites par toute la chaîne adaptative, et non seulement des permutations faciles.
- **E3 :** une archive sans rapport, appariée en longueur et en style, ainsi qu’une vérité de redite/nouveauté établie indépendamment de la mémoire testée.
- **E4 :** des étiquettes de parents permutées à bassins, budgets et effectifs constants, et une confirmation finale qui ne réutilise pas la sévérité du pôle comme définition du succès.
- **E5 :** des reparamétrisations exactes d’hypothèses existantes et des voisines réellement distinctes, avec vérité scellée ; les seules paraphrases évidentes ne suffisent pas.

## Sur la proposition B

### (a) Défauts de méthode

- **E1 transforme un événement existentiel en preuve de fonctionnement.** Une promotion suffit à réfuter la formulation littérale de H_B, mais n’établit ni une puissance ni une fiabilité. Inversement, cinq échecs sur une même banque ne sont pas cinq réplications indépendantes. Planter un effet connu sur un moniteur réel peut également recréer un monde tautologique si le connu et le calibrage incorporent cet effet.
- **E2 ne teste pas le flux opérationnel supposé en S1.** Une réussite sur dix fiches établit seulement qu’un cas est passé. L’essai mélange en outre fidélité des témoins et existence d’une sortie : un pont utile mais mal calibré et un pont fidèle mais stérile reçoivent le même verdict global.
- **E3 ne démontre rien sur la valeur de la conjonction.** L’inclusion des survivantes de \(T\wedge P\) dans chaque filtre est mathématique. Des éliminations supplémentaires peuvent être correctes ou désastreuses ; le dessin n’a pas de vérité scientifique indépendante pour les distinguer. H_A et H_B omettent aussi les cas de filtres partiellement chevauchants ou emboîtés.
- **E4 conditionne sur les filles promues.** Ce sont précisément celles dont le score de sélection est susceptible d’être gonflé. Le ratio de richesses entre deux épreuves n’est comparable que si nuls, effectifs et échelles le sont. Les mères, sélectionnées sur l’épreuve partagée, ne constituent pas un contrôle négatif.
- **E5 oppose deux propriétés différentes.** H_A porte sur un rendement par euro, H_B sur le chevauchement des ensembles éliminés : elles ne sont ni exclusives ni complémentaires. « Au moins un axe » ajoute une sélection multiple non corrigée.
- **E6 suppose que « signe opposé » et « paraphrase » fournissent la vérité d’équivalence.** Deux textes différents peuvent définir la même loi sur l’espace déclaré ; deux textes proches peuvent différer hors de la sonde. En c.5, prédire davantage que les parents sur le développement utilisé pour construire la fille mesure aussi le sur-apprentissage.

### (b) Conditions statistiques de perte de puissance ou de non-jugeabilité

- **E1.** Pour \(r\) essais réellement indépendants et une probabilité de promotion \(p\), \(P(0\text{ promotion})=(1-p)^r\). Si les cinq essais partagent banque, calibration et témoin, \(r\) effectif est proche de un. Une unique réussite ne fournit qu’un estimateur extrêmement grossier de \(p\).
- **E3.** La différence de survivantes estime seulement \(P(T\neq P)\), pas la probabilité qu’une élimination soit juste. La puissance conjointe est \(P(T=1,P=1\mid H_1)\), qui dépend de leur dépendance conditionnelle ; elle n’est ni un produit automatique ni une mesure d’utilité.
- **E4.** Si la promotion devient rare, la médiane sur filles promues est instable ou indéfinie. Même lorsqu’elle existe, \(\mathbb E[W_{\rm partagée}/W_{\rm fraîche}\mid\text{promue}]\) est un estimand sélectionné, différent de l’optimisme populationnel.
- **E5.** Avec des promotions corrélées par lignée, Fisher surestime l’information. Le rapport de rendements a une forte variance lorsque les comptages sont faibles ; la recherche du meilleur axe augmente encore le risque de faux gain.
- **E6.** Si la sonde \(Q\) donne une probabilité nulle aux points où deux lois diffèrent, leurs distributions prédites sont indiscernables : aucun estimateur sur \(Q\) ne peut décider si la mémoire a raison.

### (c) Contrôles négatifs dont l’absence serait fatale

- **E1 :** une plantation fictive à effet nul passant par exactement le même code, le même calibrage et la même annotation que la plantation vraie.
- **E3 :** un filtre dupliqué, qui doit révéler la redondance, et des fiches à vérité externe permettant de distinguer bonne et mauvaise élimination supplémentaire.
- **E4 :** des lois figées sans retour intergénérationnel et toutes les filles, promues ou non, évaluées sur un audit commun.
- **E5 :** parents permutés à budget et diversité appariés ; confirmation indépendante du couple juges/pôle.
- **E6 :** les quatre croisements « même loi/autres mots », « autre loi/mêmes mots », avec une baseline lexicale et une comparaison sur sonde scellée.

## Sur la proposition C

### (a) Défauts de méthode

- **Le produit \(\beta_{\rm total}=\beta_{\rm TM}\beta_{\rm pôle}\) suppose une indépendance non démontrée.** Traduction, difficulté de la fiche et données communes peuvent induire une dépendance positive ou négative.
- **La loi \(\mathcal O(k\log M/N_{\rm épreuve})\) n’a pas de portée générale.** Elle dépend de l’algorithme, du nombre de bits transmis, de la classe de lois et du mécanisme de recommbination ; elle ne peut être affirmée avec ces seuls paramètres.
- **E1 est partiellement tranché par construction.** Le bras strict rejette la sortie 2 tandis que cinq témoins appartiennent à la couche 3 : leur échec dans ce bras n’apprend rien sur leur vérité. Les bras ne comptent pas le même objet scientifique — promotion effective contre gel en attente — et zéro faux sur dix ne valide pas un FDP de 5 %.
- **La pondération e-BH n’est pas accompagnée de sa condition de validité.** Une sévérité de test de mort n’est pas automatiquement un poids licite ; la règle doit préciser gel, normalisation et indépendance vis-à-vis de l’épreuve.
- **E2 utilise un non-rejet comme équivalence.** « \(p>0{,}10\) » n’établit pas que deux FDR sont proches. Le test de Fisher ignore en outre l’appariement par graines et les dépendances entre courses.
- **E3 donne davantage de ressources au bras avec filtre.** « Rejette et redemande » modifie le nombre de tirages, le coût et le dénominateur. La divergence JS peut être augmentée par du bruit aléatoire : elle ne mesure pas une diversité féconde.
- **E4 favorise le bras P par sa métrique.** Les Nats/\$ sont précisément la quantité que le pôle maximise ; ils dépendent des nuls et des effectifs, et leur somme peut compter plusieurs fois la même evidence partagée. L’égalité de \(M\) ne garantit pas l’égalité du coût total.

### (b) Conditions statistiques de perte de puissance ou de non-jugeabilité

- **Pondération.** La garantie exige des poids normalisés, mesurables par rapport à l’information disponible avant lecture de l’épreuve. S’ils dépendent de données ayant contaminé l’épreuve ou sont révisés après les e-valeurs, la condition \(\mathbb E[e_iw_i\mid\mathcal F]\) requise n’est plus assurée.
- **E1.** Lorsque la couche 3 n’a aucune épreuve, sa probabilité de promotion dans le bras strict est identiquement nulle. Le rappel global mélange alors deux paramètres sans estimateur commun : la puissance du juge et la disponibilité instrumentale.
- **E2.** Sous un monde entièrement nul, toute promotion est fausse : \(\mathrm{FDR}=\Pr(V>0)\), donc FDR et FWER coïncident. Avec \(r\) courses, la variance d’un taux estimé \(q\) est \(q(1-q)/r\) avant même les dépendances ; une différence non significative ne constitue pas une borne d’équivalence.
- **E3.** \(D_{\rm JS}\) n’identifie la diversité utile que si la sonde couvre le support où les lois diffèrent et si cette diversité est liée aux confirmations futures. Des fiches aléatoires peuvent maximiser \(D_{\rm JS}\) avec un taux de confirmation nul.
- **E4.** La somme des excès de log-richesse est tronquée par la promotion, non additive sous dépendance et non comparable entre nuls. À faible taux de confirmation, elle est dominée par les zéros ; quelques lignées corrélées peuvent produire tout le gain apparent.

### (c) Contrôles négatifs dont l’absence serait fatale

- **E1 :** des témoins nuls distincts pour chaque couche, et un bras à poids fictifs gelés montrant que la pondération elle-même ne crée pas les promotions.
- **E2 :** une course sans sélection sur épreuve fixe, pour mesurer le taux de base de l’implémentation, et des lois figées sans héritage dans les deux régimes.
- **E3 :** une archive sans rapport appariée en jetons, des raisons permutées, et un filtre fictif qui conserve le même nombre de nouvelles tentatives sans transmettre les mortes.
- **E4 :** une allocation aléatoire des parents appariée en nombre et en coût, des filles dupliquées pour mesurer le double comptage des Nats, et un audit final ne scorant pas la sévérité du pôle.

## Sur la proposition E

### (a) Défauts de méthode

- **Le duel du pont conditionne son principal résultat sur l’acceptation.** \(p_{\rm erreur}\) peut être faible parce que seules les fiches triviales sont acceptées. La couverture est mentionnée, mais pas intégrée à un critère co-primaire : le pont peut donc réussir tout en étant inutilisable.
- **La vérité de fidélité reste fragile.** Des engagements synthétiques testent surtout les erreurs anticipées par leur constructeur ; sur fiches réelles, l’annotation indépendante peut simplement imposer une lecture parmi plusieurs. Les témoins doivent spécifiquement provoquer une erreur commune aux deux traducteurs.
- **Le duel de fuite additionne des performances potentiellement incommensurables.** Scores de sélection et scores d’audit doivent partager nul, échelle et estimand ; sinon \(G\) mélange l’optimisme à une différence de difficulté.
- **Le duel de fécondité confond plusieurs traitements.** Filtrer change les parents, mais aussi leur nombre, leur diversité et l’usage du budget économisé. « Distinctes » reste défini par une classification qui peut compter deux reparamétrisations comme deux découvertes.
- **Le duel d’archive n’isole pas l’effet des raisons.** Le contrôle sur domaine sans rapport traite une partie du volume de texte, mais pas la différence entre réfutations détaillées, simple exposition aux thèmes et cohérence des motifs.
- **La garde de diversité peut gagner par définition.** Réserver des places par catégorie puis mesurer le nombre de catégories confirmées favorise mécaniquement la stratification, sans établir un apport scientifique. Le tableau D ne fixe ni tailles d’effet minimales, ni unités de réplication, ni règles de passage : ce n’est pas encore une mesure minimale de fonctionnement.

### (b) Conditions statistiques de perte de puissance ou de non-jugeabilité

- **Pont.** L’estimand principal est \(P(\text{erreur}\mid A=1)\), où \(A\) est l’acceptation. Lorsque \(P(A=1)\) approche zéro, sa variance explose et l’utilité disparaît. Si deux engagements sont équivalents presque partout sous la sonde \(Q\), erreurs d’unité, population ou comparateur peuvent rester invisibles.
- **Fuite.** Si les proposeurs ne dépendent pas effectivement du retour, ou s’il n’existe aucune variation héritable, \(G=0\) même avec réutilisation : l’essai ne distingue alors absence de fuite et absence d’adaptation. La corrélation entre lignées réduit encore l’effectif de réplication.
- **Fécondité et archive.** Lorsque le taux de confirmations distinctes est proche de zéro, \(\Delta\) et \(\Delta_{\rm archive}\) sont des comptages très discrets à faible puissance. Une modification du budget change aussi \(m\), donc le seuil e-BH et la probabilité de confirmation, indépendamment de la fécondité parentale.
- **Archive.** Si la garde mécanique bloque déjà presque toutes les redites, l’archive détaillée n’a plus de marge d’amélioration : un résultat nul peut être un effet de plafond.
- **Diversité.** Avec peu de confirmations, la couverture \(D\) est un petit entier instable. Des catégories mesurées avec erreur peuvent gonfler ou effacer \(D\), tandis que la répartition du budget réduit simultanément \(N\) par hypothèse et donc la puissance confirmatoire.

### (c) Contrôles négatifs dont l’absence serait fatale

- **Pont :** des fiches réelles à vérité produite indépendamment de la consigne du traducteur, des altérations appariées visant une même lecture fausse partagée, et les références « tout refuser »/compilation mécanique.
- **Fuite :** réutilisation sans sélection, lots identiques échangés entre bras, et retours permutés entre lignées pour séparer exposition aux données et information adaptative.
- **Fécondité :** parents tirés au hasard avec nombre, niches et budget appariés ; doublons exacts et reparamétrisations pour étalonner le comptage des lois « distinctes ».
- **Archive :** mêmes réfutations avec raisons supprimées ou permutées, à volume et coût égaux ; le contrôle de domaine sans rapport ne suffit pas.
- **Diversité :** allocation aléatoire appariée et fausses catégories contenant plusieurs mécanismes réellement distincts, afin de vérifier que la couverture ne mesure pas seulement les étiquettes choisies.

FIN-DE-CELLULE