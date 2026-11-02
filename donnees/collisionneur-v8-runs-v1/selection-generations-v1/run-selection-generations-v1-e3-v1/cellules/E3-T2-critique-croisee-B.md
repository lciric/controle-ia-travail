# Proposition B — Tour III.2 : critique croisée de méthode

Convention de statuts inchangée : **VÉRIFIÉ** = recoupé entre au moins deux pièces servies ; **RAPPORTÉ** = affirmé par une pièce servie ; **OBSERVÉ-NON-AUDITÉ** = chiffre d'une lecture de lancement non contre-lue ; **HYPOTHÈSE** = inférence mienne. Les seuils numériques que j'introduis sont **illustratifs**. Les cinq clauses retirées (D-P1 à D-P5, pièce 7 § h) ne sont pas reconstituées.

---

## Sur la proposition A

### (a) Défauts de méthode

**1. Le contrôle négatif de E2 (fuite) repose sur une hypothèse d'indépendance non testée.** A propose de mesurer la fuite en comparant le bras R (épreuve réutilisée) et le bras F (épreuve fraîche), avec un contrôle négatif : « filles dont les parents sont des éliminées de g1 ». L'idée est que ces filles n'ont pas été sélectionnées sur E₁. Mais la mémoire du pôle sert à g2 les « leçons » de g1, qui parlent de science (RAPPORTÉ, pièce 4 : « elles parlent maintenant de science »). Si les leçons transmettent de l'information sur les fluctuations d'échantillonnage de E₁ — même indirectement, par le contenu des survivantes décrites — les filles d'éliminées **aussi** reçoivent cette fuite par le canal de la mémoire. Le contrôle ne discrimine donc pas entre la fuite par sélection parentale et la fuite par le canal textuel de la mémoire. **Variable confondante : le canal mémoire-leçons est partagé entre tous les bras.**

**2. E3 (héritage) confond l'effet du texte et l'effet de la raison, mais le bras SE-perm ne suffit pas à les séparer.** La permutation des raisons entre fiches détruit la correspondance fiche–raison mais conserve le volume textuel et le vocabulaire du domaine. Si l'ancrage vient de l'exposition au vocabulaire thématique des mortes (ce qui est plausible pour un modèle de langage), SE et SE-perm produisent le même ancrage, et le duel ne peut distinguer « la raison aide » de « le texte ancre ». Il faudrait un quatrième bras où le texte des éliminées est remplacé par un texte de volume et de complexité comparables mais de domaine sans rapport (comme le propose E dans son duel « archive »).

**3. E4 (ablation) utilise le juge figé comme métrique, ce qu'A reconnaît, mais ne propose aucun audit indépendant.** Si le bras P est avantagé parce que ses parents ont été sélectionnés par le même juge qui évalue les filles, l'avantage est circulaire : le juge promeut les filles qui ressemblent statistiquement aux parents qu'il a déjà promus. A dit « la métrique est le juge figé lui-même. Elle n'est acceptable que si E₃ est fraîche ». C'est nécessaire mais insuffisant : même sur une épreuve fraîche, si la population des fiches a été façonnée par des générations de sélection sur le même type de juge (mêmes prédicteurs aveugles, même nul, même famille de lois), le bras P hérite d'un avantage **par construction**. **Manque un audit par un juge ou une procédure statistique indépendante** (par exemple un test de permutation classique à taille fixe, comme C le suggère dans son tableau d'instruments).

**4. E5 (lecteurs neufs) teste l'accord mais pas la validité.** Le kappa ≥ 0,45 mesure la concordance entre deux lecteurs sur la grille « redite / affine / neuve ». Mais deux lecteurs peuvent s'accorder sur une classification fausse, surtout si le programme est assez spécifique pour que « neuve par rapport à H1–H9 » ait une interprétation ambiguë (RAPPORTÉ : N-013 modifie la lecture de HC1, HC3, HC4, H6 ; pièce 10). Le contrôle négatif proposé (mêmes lecteurs sur des éliminées) ne teste pas la justesse, seulement la discrimination survie/nouveauté. **Contrôle manquant : des fiches plantées dont la vérité « redite / neuve » est connue de l'expérimentateur mais pas des lecteurs, avec des cas où la nouveauté apparente masque une redite (reparamétrisation d'une hypothèse existante).**

### (b) Conditions sous lesquelles les mesures perdent leur puissance

| Mesure / critère | Loi de probabilité ou paramètre critique | Condition de perte de puissance ou de non-jugeabilité |
|---|---|---|
| E1 — Dents du pôle | Soit $\theta$ le log-rapport de cotes de la loi vraie du témoin. Le juge observe une richesse $W = \prod_t p_{\text{loi}}(y_t \mid z_t)/p_{\text{nul}}(y_t \mid z_t)$. | Si $\theta < c / \sqrt{n}$ où $c \approx \sqrt{2 \log(m/\alpha)}$ (seuil e-BH), le test n'a pas de puissance (rappel → 0). À $n = 288$ et $m = 20$ (illustratif), le seuil e-BH exige $\theta \gtrsim 0,25$ (illustratif). Si les effets réels des fiches de course sont en dessous, E1 conclut « pas de dents » alors que les fiches ne sont pas fausses — seulement faibles. |
| E2 — Fuite | Soit $\hat{F}_R$ et $\hat{F}_F$ les taux de fausses promotions des bras R et F. Sous $H_0$ : $F_R = F_F = \alpha$. | Avec 20 témoins par bras, la différence détectable à 80 % est $\Delta \approx 0,22$ (illustratif, test exact de Fisher bilatéral, $\alpha_{\text{test}} = 0,05$). Une fuite de 10 % ($\hat{F}_R = 0,15$) serait non détectable. Le dessin est sous-dimensionné pour les fuites modérées. |
| E4 — Ablation | Le nombre de promues par bras suit approximativement une binomiale $\text{Bin}(10, p)$. | Avec 10 fiches par bras, un test exact de Fisher ne détecte un rapport de cotes ≥ 4 qu'à ~50 % de puissance (illustratif). A reconnaît que « l'effet détectable est grossier » mais ne conclut pas que le dessin est probablement non jugeable. |
| E6 — Diversité, simulation | La part de la lignée dominante est une variable aléatoire sur [0,1] dépendant de la matrice de fécondité et du nombre de lignées initiales $L$. | Si $L \leq 3$ (ce qui est plausible avec 17 idées distinctes dont beaucoup partagent un axe), l'effondrement est presque certain sous n'importe quelle sélection : la garde ne peut le prévenir sans refuser la sélection elle-même. |

### (c) Contrôles négatifs dont l'absence serait fatale

1. **E1 — Absence d'un témoin « effet nul exact sous la loi »** : les témoins faux par permutation dans la tâche (pièce 7 a.3) vérifient le taux de fausses promotions, mais il manque un témoin dont la loi est **correctement spécifiée** (pas « permutation ») avec un effet **exactement nul** ($\theta = 0$) sur le même moniteur. Sans ce contrôle, on ne distingue pas « le juge rejette les faux » de « le juge rejette tout ce qui n'est pas tautologique ».

2. **E2 — Absence d'un bras « épreuve fixe sans sélection »** : si l'on observe une inflation dans le bras R, elle peut venir de la sélection (fuite) ou de la non-stationnarité de la banque (dérive des épisodes dans le temps). Un bras où les fiches sont tirées aléatoirement (pas sélectionnées) mais jugées sur la même épreuve fixe mesurerait la composante due à la sélection seule.

3. **E4 — Absence d'un bras « pôle inversé »** : ensemencer g2 avec les **éliminées** du pôle (les fiches que le juge a réfutées). Si ce bras fait aussi bien que le bras P, la sélection du pôle n'hérite rien ; si ce bras fait strictement pire, le signal est dans la bonne direction. Ce contrôle est plus informatif que le tirage aléatoire T, qui dilue survivantes et éliminées.

---

## Sur la proposition C

### (a) Défauts de méthode

**1. E1 de C introduit deux variables simultanées et ne peut les séparer.** C compare le bras 1 (conjonction stricte + e-BH plat) au bras 2 (3 voies + e-BH pondéré par richesse a priori issue du test de mort). La différence entre bras mêle deux changements : (i) l'architecture de survie (conjonction vs. 3 voies) et (ii) la procédure statistique (e-BH plat vs. e-BH pondéré). Si le bras 2 gagne, on ne sait pas si c'est la pondération ou les 3 voies qui ont produit le gain. **Il manque les bras croisés** : conjonction stricte + e-BH pondéré, et 3 voies + e-BH plat.

**2. E2 de C suppose que le nul ($\beta = 0$) est le bon monde pour mesurer la fuite, mais la fuite par sélection darwinienne n'opère que s'il y a de la variance entre fiches.** Dans un monde purement nul où toutes les fiches ont exactement $\beta = 0$, la sélection ne peut pas concentrer la population sur des fiches « chanceuses » si les lois sont identiques. La fuite critique apparaît quand les fiches diffèrent en puissance apparente (certaines sont proches du seuil, d'autres loin) mais aucune n'est vraie — c'est-à-dire sous un **nul hétérogène** où les $\beta_i$ sont nuls mais les paramètres de nuisance (sous-populations, traits) varient. Le protocole de C, en fixant un nul homogène, peut sous-estimer la fuite réelle.

**3. E3 de C mesure la diversité par la divergence de Jensen-Shannon sur les prédictions, mais cette métrique est vraie par construction quand les prédictions sont contraintes par le format.** Le pôle accepte un petit nombre de types de loi (softmax, par sous-population, si/sinon, mélange, fixe ; RAPPORTÉ, pièce 7 a.2). Deux fiches qui portent sur des moniteurs différents auront une divergence JS élevée par construction (espaces d'issues différents), tandis que deux fiches profondes portant sur le même moniteur mais avec des mécanismes différents auront une divergence faible. **La métrique ne mesure pas la diversité scientifique mais la diversité de cible.**

**4. E4 de C utilise « Nats/$ » comme co-primaire, mais le dénominateur « coût total du bras » n'est pas comparable entre bras.** Le Bras Pôle paie le pont + le pôle + les tests de mort ; le Bras Juges-Modèles ne paie que les juges-modèles. C dit « à budget d'évaluation égal » pour le taux de promotion, mais le Nats/$ compare des numérateurs sur des dénominateurs structurellement différents. **Variable confondante : le coût fixe du pont et du pôle est chargé sur un seul bras.**

**5. La spécification de C pour l'instrument « Pont » exige de battre un « extracteur régulier sans LLM ».** C'est une bonne idée, mais le seuil proposé (« au moins 25 % de fiches valides de plus que le script régulier ») est arbitraire et peut être vrai par construction : si le script régulier ne sait traiter que les fiches à champ `prediction` structuré (course 2) et que les fiches de course 1 ont un champ en texte libre (RAPPORTÉ, pièce 7 a.1 : « en texte libre »), le LLM gagne simplement en couverture de format, pas en fidélité.

### (b) Conditions sous lesquelles les mesures perdent leur puissance

| Mesure / critère | Loi ou paramètre critique | Condition de perte |
|---|---|---|
| E1 — Rappel $R_V$ sur 10 témoins vrais | $R_V \sim \text{Bin}(10, \beta)$ où $\beta$ est la puissance du pôle | Le seuil de falsification est $R_V \leq 4$ pour $H_B$. Sous $\beta = 0{,}60$ (puissance modérée), $P(R_V \leq 4) \approx 0{,}37$ (illustratif) : l'expérience ne distingue pas puissance modérée et absence de dents avec probabilité raisonnable. |
| E2 — FDR Fixe vs. Renouvelé | $\widehat{\text{FDR}}$ estimé sur 100 courses. Sous le nul homogène, chaque course a $P(\text{fausse promotion}) \leq \alpha$. | Avec $m = 20$ fiches nul-exactes et $\alpha = 0{,}05$, le nombre attendu de fausses promotions par course est $\leq 1$. Sur 100 courses, la variance du $\widehat{\text{FDR}}$ est de l'ordre de $\alpha(1-\alpha)/100 \approx 0{,}002$. Un écart de 0,05 entre bras (seuil de rupture) est détectable, mais seulement si la fuite produit un effet de cette taille à chaque course — or la fuite est cumulative et peut ne se manifester qu'aux générations tardives ($g \geq 5$), que le protocole à 3 générations ne couvre pas. |
| E3 — Divergence JS | $D_{\text{JS}}$ est bornée par $\log 2$ et, pour des distributions multinomiales sur $K$ issues proches, $D_{\text{JS}} \approx \chi^2 / (8 \ln 2)$ avec $\chi^2 \sim \chi^2_{K-1}$ sous le nul. | Si $K = 2$ (moniteur à deux issues), la divergence JS entre deux lois proches est de l'ordre de $(\Delta p)^2 / 8$. Avec $\Delta p \approx 0{,}1$ (effet de 0,1 sur la probabilité), $D_{\text{JS}} \approx 0{,}001$. Détecter une chute de 25 % de cette quantité ($\approx 0{,}00025$) sur 20 fiches par bras est irréaliste sans des milliers de fiches. |
| E4 — Nats/$ | Le numérateur $\sum (\log W_i - \log(m/\alpha))$ est non nul seulement pour les fiches promues, et nul pour toutes les autres. | Si 0 ou 1 fiche est promue par bras (ce qui est vraisemblable, vu « pas de dents » sur la banque réelle), le Nats/$ est 0 dans les deux bras. La métrique est dégénérée dans le régime de fonctionnement le plus probable. |

### (c) Contrôles négatifs dont l'absence serait fatale

1. **E1 — Pas de bras croisé (conjonction + pondération vs. 3 voies + plat)** : sans ce contrôle, l'expérience ne falsifie que la combinaison, pas les composantes. L'absence est fatale parce que la décision d'architecture (3 voies vs. conjonction) et la décision statistique (pondération) ont des implications et des coûts différents.

2. **E2 — Pas de contrôle sous nul hétérogène** : si la fuite ne se manifeste que sous un nul où les fiches diffèrent en paramètres de nuisance, 100 courses sous nul homogène peuvent conclure faussement à l'absence de fuite.

3. **E4 — Pas de bras où les deux bassins sont évalués sur une troisième épreuve indépendante non utilisée par le pôle** : C propose bien une épreuve $T_2$ « fraîche », mais si $T_2$ a été dimensionnée pour le pôle (même structure de nul informé, même bibliothèque de prédicteurs), le bras P est favorisé. Il faudrait un audit final sur une épreuve de structure différente (autre ensemble de prédicteurs aveugles, ou test à taille fixe classique).

---

## Sur la proposition D

### (a) Défauts de méthode

**1. E1 de D ne distingue pas inapplicabilité structurelle et inapplicabilité conjoncturelle.** D oppose $H_A$ (toutes les fiches reçoivent les deux tests) et $H_B$ (il existe une classe non vide de fiches différées). Mais $H_B$ est presque certainement vraie **par construction** des pièces servies : l'épreuve T0.5 est entièrement lue (VÉRIFIÉ), donc toute fiche ciblant un moniteur de T0.5 sans épreuve fraîche est différée. L'expérience ne falsifie rien : elle documente un état connu. **Le duel devrait opposer deux causes d'inapplicabilité** : (i) le pont ne traduit pas la fiche (problème de fidélité) vs. (ii) le pont traduit mais l'épreuve manque (problème de données). La première est un défaut du pont ; la seconde est un défaut d'infrastructure.

**2. E2 de D demande un « monde à vérité plantée ET une banque réelle fraîche », mais ne spécifie pas comment éviter que le monde planté domine le signal.** Si les deux sont évalués ensemble (ce que « campagnes appariées » implique), le résultat dépend de la proportion monde planté / banque réelle. Si la banque réelle a peu de puissance (RAPPORTÉ : « pas de dents »), le verdict de E2 sera piloté par le monde planté, qui est tautologique par construction.

**3. E3 de D manque d'un seuil gelé.** D dit « mesurer redites exactes et paraphrasées, fausses fusions, nouvelles familles confirmées par euro. Seuil : supériorité sur le rendement final. » Mais « supériorité » n'est pas un seuil : c'est une direction. Sans quantification de l'effet minimal détectable et du nombre de fiches nécessaires, l'expérience peut conclure « non concluant » dans tous les cas réalistes.

**4. E5 de D (ablation) exige une « épreuve finale supplémentaire, jamais utilisée par l'un ou l'autre ».** C'est correct, mais D ne précise pas si cette épreuve a la même structure que celle du pôle (même nul informé, mêmes prédicteurs). Si oui, le bras avec pôle est avantagé (ses fiches sont pré-sélectionnées pour battre ce type de nul). Si non, les deux bras sont évalués sur un critère différent de celui qui a filtré le bras P, ce qui introduit un biais différent. **D ne dit pas quel biais est préférable.**

**5. La mesure minimale de la « Porte de sortie R13 » est décrite en termes qualitatifs** (« détection de quasi-doublons », « fausses alertes sur idées réellement distinctes ») sans métrique ni distribution spécifiées. Cela empêche de calculer la puissance et rend le contrôle non préenregistrable.

### (b) Conditions sous lesquelles les mesures perdent leur puissance

| Mesure / critère | Loi ou paramètre critique | Condition de perte |
|---|---|---|
| E1 — Pont utilisable | Le nombre de sorties par type suit une multinomiale $\text{Mult}(n, p_1, p_2, p_3)$ avec $p_1 + p_2 + p_3 = 1$. | Avec $n = 10$ (premier essai du pont, RAPPORTÉ), l'intervalle de confiance à 95 % pour $p_1$ (sortie 1) est de largeur $\approx 0{,}55$ (illustratif, Clopper-Pearson). L'expérience ne peut distinguer $p_1 = 0{,}05$ de $p_1 = 0{,}30$ ; elle ne falsifie donc ni $H_A$ ni $H_B$ sur la part de fiches immédiatement testables sauf dans le cas trivial $p_1 = 0$. |
| E2 — Fuite | D demande que « la borne supérieure d'erreur reste sous 0,05 ». | Sous un nul hétérogène avec $m = 20$ fiches de variances très différentes et sélection adaptative sur 3 générations, la borne théorique de Ville ne s'applique que fiche par fiche, pas à l'agrégation post-sélection. La « borne supérieure préenregistrée » invoquée par D n'existe pas sans preuve supplémentaire : c'est exactement le point que E relève (« la garantie par génération ne devient pas un contrôle cumulatif adaptatif »). |
| E3 — Héritage | D ne spécifie pas la distribution de la distance entre « redites paraphrasées » et « hypothèses proches mais distinctes ». | Si la mémoire utilise une garde textuelle (RAPPORTÉ, pièce 6 : « la mémoire reconnaisse deux hypothèses de contrôle qui partagent le vocabulaire »), la frontière redite/novelle dépend du seuil de similarité. Pour un seuil qui élimine 90 % des redites, le taux de fausses alertes sur des hypothèses proches est une fonction croissante de la densité du voisinage lexical, non contrôlée par D. |
| E5 — Ablation | La métrique « familles d'idées canonisées, nouvelles, confirmées » combine trois classifications (canonisation, nouveauté, confirmation) dont chacune a un taux d'erreur. | L'erreur composée est $\leq \epsilon_1 + \epsilon_2 + \epsilon_3$ (union bound). Si chaque étape a un taux d'erreur de 10 % (illustratif), la métrique a jusqu'à 30 % d'erreur, ce qui efface un signal de 20 %. |

### (c) Contrôles négatifs dont l'absence serait fatale

1. **E1 — Absence d'un bras « fiches de course 2 » à côté des fiches de course 1** : le format de la course 1 est SUPPOSÉ (RAPPORTÉ, pièce 7 réserve 2). Si le pont fonctionne sur la course 1 mais pas sur la course 2 (format différent, champs différents), le premier essai est un faux positif pour la « testabilité ».

2. **E2 — Absence d'un contrôle « épreuve fixe sans sélection mais avec mémoire »** : la mémoire transmet des leçons qui contiennent de l'information sur les épisodes passés. Si la fuite vient de la mémoire et non de la sélection, le bras « épreuve renouvelée » ne la corrige pas.

3. **E5 — Absence de répétitions indépendantes** : D exige des « répétitions », mais ne spécifie pas combien ni comment l'indépendance est obtenue (mêmes proposeurs, même consigne, même banque → les « répétitions » ne sont pas indépendantes si le proposeur a un contexte cumulatif).

---

## Sur la proposition E

### (a) Défauts de méthode

**1. Le duel « pont fidèle » mesure $p_{\text{erreur}}$ mais ne sépare pas les types d'erreur.** E propose de mesurer le taux de traductions qui « changent matériellement l'engagement ». Mais une traduction peut changer l'engagement de trois manières non équivalentes : (i) changer la direction de la prédiction (sens inversé), (ii) changer la population cible (moniteur/sous-population), (iii) changer l'amplitude au-delà du facteur 2 autorisé. Le taux global $p_{\text{erreur}}$ ne dit pas si le pont est biaisé dans une direction (toujours trop conservateur, ou toujours trop agressif) ou s'il fait des erreurs symétriques. **Confondant : les trois types d'erreur ont des conséquences différentes sur la sélection (i et ii falsifient la mauvaise hypothèse ; iii affecte la puissance) et doivent être comptés séparément.**

**2. Le duel « filtre produit de meilleurs descendants » attribue au bras sans filtre un « budget d'exploration équivalent aux dépenses économisées ».** C'est ingénieux mais crée un confondant : le bras sans filtre reçoit plus de tentatives (parce qu'il ne paie pas le pont et le pôle). Si le rendement marginal de chaque tentative est décroissant (ce qui est probable : les premières idées sont les plus faciles), le bras sans filtre bénéficie de l'effet de volume. **La comparaison n'est pas à « budget égal » au sens scientifique mais au sens comptable.** Il faudrait fixer le nombre de fiches (pas le budget) et comparer les coûts totaux.

**3. Le duel « archive des réfutations » utilise $\Delta_{\text{archive}} = 0$ comme frontière, mais la puissance pour détecter un petit $\Delta > 0$ n'est pas estimée.** E reconnaît que les seuils sont illustratifs, mais la frontière zéro est « définitionnelle » : cela signifie que l'expérience ne peut pas être non concluante par construction (tout intervalle de confiance est soit entièrement positif, soit contient zéro). En pratique, avec le nombre de fiches attendu (10–20 par bras), l'intervalle de confiance pour le nombre de confirmations distinctes sera de largeur ≥ 3 (illustratif, Poisson), et contiendra presque toujours zéro. **L'expérience sera systématiquement non concluante dans le régime prévu.**

**4. La « population reproductrice étroite et archive épistémique plus riche » de E ne définit pas la transition entre les deux.** Quand une fiche « en attente » obtient de nouvelles données, elle redevient candidate. Mais E dit qu'une « reprise exige un nouvel engagement explicitant ce qui change ». Cela signifie que la fiche « en attente » n'est pas la même fiche qui revient : c'est une nouvelle fiche avec une nouvelle loi et un nouveau gel. Elle consomme donc un slot dans le $m$ de e-BH. Si beaucoup de fiches reviennent, $m$ croît sans que la puissance augmente, et la boucle s'éteint par inflation de la correction de multiplicité. **Confondant potentiel entre recyclage et création.**

**5. E propose de « remplacer provisoirement la reproduction générationnelle par une allocation indépendante de tests ».** C'est l'option la plus radicale et la plus honnête, mais elle n'est pas falsifiable en l'état : si on ne teste jamais la reproduction, on ne saura jamais si elle ajoute quelque chose. E le reconnaît (« pièce qui trancherait : duel filtre vs. allocation »), mais l'option provisoire peut devenir permanente par inertie. **Il manque un critère de sortie gelé** : après combien de générations sans avantage mesurable du filtre l'allocation sans filtre est-elle adoptée définitivement ?

### (b) Conditions sous lesquelles les mesures perdent leur puissance

| Mesure / critère | Loi ou paramètre critique | Condition de perte |
|---|---|---|
| Pont fidèle — $p_{\text{erreur}}$ | $\hat{p} \sim \text{Bin}(n, p)/n$, intervalle Clopper-Pearson. | À $n = 16$ (10 fiches + 6 témoins, premier essai), la borne haute à 95 % pour $\hat{p} = 0$ est 0,19. L'expérience ne peut exclure $p_{\text{erreur}} = 15\%$ même si aucune erreur n'est observée. Le seuil de 5 % n'est pas atteignable à cette taille d'échantillon. |
| Fuite — décalage $G$ | $G$ est la différence de deux moyennes de $\log W$ sur épreuve de sélection vs. épreuve d'audit. Sous le nul, $\text{Var}(G) \approx 2 \sigma^2_{\log W}/n$ par bras. | Si $\sigma_{\log W} \approx 3$ (illustratif, basé sur les log W de 74 et 84 du lancement tautologique), et $n = 20$ fiches par bras, $\text{SE}(G) \approx 0{,}95$. Le seuil de 0,05 est noyé dans le bruit : l'expérience n'a aucune puissance. |
| Filtre — $\Delta$ confirmations distinctes | $\Delta = X_P - X_{\neg P}$ où $X \sim \text{Poisson}(\lambda)$. $\text{Var}(\Delta) = \lambda_P + \lambda_{\neg P}$. | Si $\lambda \approx 2$ (illustratif : 2 confirmations par bras sur 10–20 fiches), $\text{SD}(\Delta) = 2$. Détecter $\Delta = 1$ a une puissance de ~30 % (illustratif). |
| Archive — $\Delta_{\text{archive}}$ | Même structure que ci-dessus. | Même problème. La frontière zéro ne rend pas le test plus puissant ; elle rend seulement l'interprétation binaire. |
| Diversité — $D$ | $D$ est un gain de couverture. Si les « familles prédictives confirmées » sont rares ($\leq 5$ par bras), $D$ est à valeurs entières avec peu de niveaux. | Un test de permutation sur un comptage à valeurs dans $\{0, 1, 2, 3\}$ n'a de puissance que pour des effets très grands (différence de ≥ 2 familles). |

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Pont fidèle — Absence d'un contrôle « traduction identitaire »** : E propose des fiches construites à partir d'engagements connus, mais pas de fiches déjà au format fiche-loi du pôle (c'est-à-dire qui ne nécessitent aucune traduction). Si le pont échoue sur ces fiches « déjà traduites », le problème est dans la compilation, pas dans la traduction. Si le pont réussit seulement sur celles-ci, le problème est dans l'interprétation du texte libre. Ce contrôle sépare les deux étapes.

2. **Fuite — Absence d'un bras « mémoire sans sélection »** : E propose réutilisation vs. renouvellement, mais la mémoire du pôle (leçons, survivantes) est un canal de fuite orthogonal au canal « épreuve fixe ». Un bras où l'épreuve est renouvelée mais la mémoire complète (leçons + survivantes + éliminées) est transmise mesurerait la fuite par le canal mémoire seul.

3. **Filtre — Absence d'un contrôle temporel** : E compare filtre vs. allocation « à budget total identique », mais le bras filtré prend plus de temps (pont + pôle + attente de l'épreuve). Si les proposeurs sont sensibles à la latence (contexte plus long, dérive du modèle entre versions), le bras filtré est désavantagé par le temps, pas par le filtre. Fixer le délai (pas seulement le budget) serait nécessaire.

4. **Garde de diversité — Absence d'un monde à diversité structurelle connue** : E propose un contrôle où « toutes les catégories recouvrent le même mécanisme », mais pas un monde où la diversité optimale est calculable analytiquement. Sans cette référence, on ne sait pas si la garde atteint l'optimum ou si elle impose un quota arbitraire.

FIN-DE-CELLULE