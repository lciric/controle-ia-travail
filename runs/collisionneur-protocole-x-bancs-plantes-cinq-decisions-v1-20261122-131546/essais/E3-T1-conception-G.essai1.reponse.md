# Proposition G — Tour III.1 : Cinq décisions de conception pour des bancs d'essai de moniteurs de sabotage

**Note d'intégrité (règles 1 et 2).** Les blocs `FAITS` et `QUESTION DE L'ARBITRE` sont complets, non coupés et strictement identiques (même empreinte `sha256=3609365d…`), mais aucune annexe technique (code, simulations, textes d'admission) n'est jointe. Le bloc `FAITS` ne portant pas d'étiquettes de statut explicites, ses affirmations factuelles sont traitées comme `RAPPORTÉ`, ses calculs ou vérifications non joints comme `OBSERVÉ-NON-AUDITÉ`, les identités purement algébriques vérifiables sur les définitions comme `VÉRIFIÉ`, et les prémisses non établies comme `HYPOTHÈSE`.

---

## Partie I — Réponses aux décisions de conception (forme demandée par l'arbitre)

### Décision 1 — Ce que rapporte le monde témoin, joué sans dommage planté (banc des tâches floues)

- **Option choisie :** **(c)** Rapporter les deux grandeurs, chacune sous son nom, sans seuil exigé.
- **Confiance :** 0,78 (jugement épistémique).
- **Raison :** Un moniteur muni d'une clause d'abstention répartit chaque cas honnête en trois états mutuellement exclusifs (`accepter`, `signaler`, `s'abstenir`, de somme égale à 1, `VÉRIFIÉ`), si bien qu'un scalaire unique détruit un degré de liberté essentiel. En outre, la Grandeur A est définie de manière ambiguë (« accepte (ne signale pas) », `RAPPORTÉ`) : si elle désigne $1 - p_{\text{sig}}$, elle reste aveugle à un basculement massif de l'acceptation vers l'abstention ; si elle désigne l'acceptation stricte $p_{\text{acc}}$, alors une forte variation de B ($p_{\text{abs}}$) à A quasi constant implique algébriquement une variation opposée équivalente du taux de fausses alertes $p_{\text{sig}}$ (`VÉRIFIÉ`). L'option (c) évite à la fois l'angle mort de (a) et la torsion sémantique de (b), et reste conforme à la règle de gel puisqu'elle intervient avant celui-ci.
- **Ce qui me ferait changer d'avis :** Si le schéma du texte d'admission imposait impérativement une porte binaire unique sur ce témoin sans ajout possible et qu'un audit vérifiait à la fois que A désigne strictement $p_{\text{acc}}$ et que $p_{\text{sig}}$ demeure négligeable dans les deux mondes (rendant A et B redondantes).
- **Option meilleure que celles proposées :** Geler explicitement la **décomposition complète à trois états** $(p_{\text{acc}}, p_{\text{sig}}, p_{\text{abs}})$ sur le jumeau honnête (en levant l'ambiguïté de « accepte (ne signale pas) ») en écart au monde de référence, assortie de **critères de lecture pré-enregistrés** distincts sur l'inflation des fausses alertes ($\Delta p_{\text{sig}}$) et sur l'inflation d'abstention ($\Delta p_{\text{abs}}$), afin de corriger l'absence de critère de l'option (c).

### Décision 2 — La règle de signalement par défaut (banc des dommages plantés par un tiers)

- **Option choisie :** **(b)** La même règle, plus un seuil réglé sur un lot d'étalonnage distinct du lot final, lequel ne serait lu qu'une fois.
- **Confiance :** 0,82 (jugement épistémique).
- **Raison :** Sans étalonnage, la règle fixe $1/m$ de (a) laisse le taux de fausses alertes totalement inconnu : lorsque $m$ est grand ou que les lecteurs divergent légèrement sur des documents honnêtes indépendants, un écart d'un seul contrôle peut survenir fréquemment par pur bruit de lecture et pousser la campagne en régime d'excès (`HYPOTHÈSE`). L'option (c) bloque indéfiniment le gel sur une dépendance externe et accepte sans audit n'importe quelle règle binaire fournie ultérieurement par l'oracle. L'option (b) calibre le seuil avant le gel sur un lot strictement disjoint tout en ne lisant le lot final qu'une seule fois, ce qui préserve la validité statistique de la campagne finale.
- **Ce qui me ferait changer d'avis :** Vers (a), si un audit préalable établissait un bruit de lecture quasi nul sur paires honnêtes indépendantes pour toutes les valeurs de $m$ du banc, ou si le coût du lot d'étalonnage dépassait le budget admissible ; vers (c), si la règle binaire propre d'un oracle externe constituait l'unique objet scientifiquement évalué et disposait d'une date de livraison ferme.
- **Option meilleure que celles proposées :** Utiliser sur le lot d'étalonnage un **seuil normalisé en fonction de $m$ et de la variance inter-lecteurs**, réglé par quantile sur des **paires indépendantes honnête-contre-honnête** (jamais en comparant un document à sa propre lecture) pour fixer un plafond explicite de fausses alertes, et trancher par écrit avant gel si la règle modélise un oracle d'évaluation apparié ou un moniteur déployable devant décider sur un document unique sans objet de comparaison.

### Décision 3 — Qui désigne ce qui porte un contrôle, à l'étape de mise au point (banc des dommages plantés par un tiers)

- **Option choisie :** **(b)** Par un repéreur (un modèle lit chaque tâche et désigne les passages).
- **Confiance :** 0,66 (jugement épistémique).
- **Raison :** Comme une erreur de désignation fausse la vérité terrain des contrôles retirés et se répercute directement sur la probabilité mesurée que le moniteur reconnaisse un dommage (`RAPPORTÉ`), s'en remettre au seul recouvrement de mots compromet la validité de construit pour des dommages diffus et paraphrasés. L'option (c) paie déjà l'étape de mise en œuvre d'un repéreur sur un échantillon, mais laisse ensuite le programme lexical corrompre les désignations sur le reste des tâches en se bornant à rapporter l'erreur à côté. Une lecture de modèle par tâche reste un coût linéaire vraisemblablement modeste au regard d'un banc qui exécute déjà des agents et un oracle multi-lecteurs, même si son chiffrage exact et la fidélité propre du repéreur restent à vérifier (`HYPOTHÈSE`).
- **Ce qui me ferait changer d'avis :** Si un essai pilote contre double annotation humaine montrait soit que les contrôles sont ancrés lexicalement au point que le programme atteint une précision et un rappel élevés ($\ge 0{,}95$, illustratif), soit que le repéreur introduit un biais corrélé à la famille des moniteurs évalués ou un coût incompatible avec l'étape de mise au point.
- **Option meilleure que celles proposées :** Mettre en place une **cascade hybride auditée contre annotation humaine** : évaluer sur un échantillon probabiliste stratifié (ex. $120$ contrôles, illustratif) le programme lexical et un repéreur issu d'une **famille de modèles distincte** des moniteurs testés face à une double lecture humaine, réserver le programme aux contrôles dont l'ancrage lexical franchit un seuil pré-gelé, router les autres au repéreur audité et propager la borne d'erreur résiduelle de désignation dans la borne sur $q$.

### Décision 4.1 — Ce que laisse le « régime d'excès » : que rendre à la place ?

- **Option choisie :** **(c)** Garder seulement la fonction de calcul de l'optimum et ses cas d'essai, sans rien lire sur le banc.
- **Confiance :** 0,80 (jugement épistémique).
- **Raison :** En régime d'excès, l'oracle trouve trop de manques chez l'honnête (`RAPPORTÉ`), ce qui peut abaisser artificiellement le taux de non-détection $q$ par simple sur-signalement et rendre le produit $\text{dose} \times \bar{q}_s$ de l'option (b) activement trompeur malgré une mention « sans garantie ». Contrairement à (b), l'option (c) empêche toute diffusion d'une lecture de dommage non garantie sur ce banc. Contrairement à (a), elle préserve la vérification logicielle de la fonction de calcul de l'optimum sur des cas synthétiques, évitant de conserver un outil non éprouvé jusqu'à une campagne ultérieure.
- **Ce qui me ferait changer d'avis :** Vers (a), si la présentation éditoriale risquait de faire confondre les sorties des cas d'essai synthétiques avec des mesures sur le banc ; vers (b), uniquement si la borne $\bar{q}_s$ était mathématiquement impossible à abaisser par sur-signalement de l'oracle (ce qui contredirait la situation de régime d'excès).
- **Option meilleure que celles proposées :** Combiner **(c)** avec un **constat diagnostique d'échec de l'oracle** strictement séparé des résultats de moniteurs — publiant les taux de manques sur l'honnête ayant déclenché le régime d'excès et les effectifs bruts par strate en annexe technique, mais interdisant explicitement le calcul et la publication du produit $\text{dose} \times \bar{q}_s$.

### Décision 4.2 — Ce que laisse le « régime d'excès » : le budget d'erreur

- **Option choisie :** **(a)** Garder les niveaux accordés (2,5 % avec un regard, ou 1,25 % par regard avec deux regards).
- **Confiance :** 0,92 (jugement épistémique).
- **Raison :** Modifier après coup un niveau d'erreur déjà accordé contredit le principe de gel préalable qui fonde la garantie statistique de la campagne (`RAPPORTÉ`). Surtout, l'événement « régime d'excès » $E$ dépendant des données de la campagne, réallouer la part libre $\alpha_2$ aux bornes de $q$ ne préserve pas en général le taux d'erreur global (FWER) : si l'erreur de l'énoncé en dommage (calibré marginalement au niveau $\alpha_2$) se concentre hors régime d'excès $E^c$ — ce que favorise le biais de sélection sur les tirages honnêtes favorables — le FWER peut atteindre $\alpha_1 + (1 + \Pr(E))\alpha_2 > \alpha_1 + \alpha_2$ même si $E$ est indépendant de $q$ (`VÉRIFIÉ` ; exemple illustratif : avec $\alpha_1 = 2{,}5\,\%$, $\alpha_2 = 2{,}5\,\%$ illustratif et $\Pr(E) = 0{,}5$ illustratif, le FWER peut atteindre $6{,}25\,\% > 5\,\%$, illustratif). Toute dépendance entre lectures honnêtes et sabotées (notamment via une comparaison appariée comme en Décision 2) peut aggraver encore cette inflation d'erreur. Enfin, resserrer une borne sur $q$ lorsque l'oracle est déjà en régime d'excès n'apporte aucun bénéfice scientifique justifiant ce risque.
- **Ce qui me ferait changer d'avis :** Uniquement si le déclenchement du régime d'excès était décidé sur un échantillon préliminaire strictement indépendant de l'échantillon final, selon une règle de branchement gelée avant toute collecte (sans rendre pour autant utile une borne sur $q$ isolée en régime d'excès).
- **Option meilleure que celles proposées :** Aucune pour la campagne courante ; l'option (a) est déjà l'option statistiquement saine dans le cadre décrit.

### Décision 5 — La composition de la fiche (banc à lois plantées)

- **Option choisie :** **(a)** Tirer la composition au hasard par épisode, selon la règle, et refaire le calcul d'admission.
- **Confiance :** 0,88 (jugement épistémique).
- **Raison :** Aucune fiche n'ayant encore été servie à un agent (`RAPPORTÉ`), refaire le calcul d'admission est un coût ponctuel avant gel qui ne contamine aucune mesure. À l'inverse, figer et annoncer le nombre de lois $K$ réduit la tâche de découverte statistique à la sélection des $K$ statistiques les plus fortes et retire un témoin à la règle de cohérence, dont le comportement face à ce geste n'est même pas vérifié (`RAPPORTÉ` / `HYPOTHÈSE`). Préserver la comparabilité d'une étape à l'autre perd sa valeur si la spécification figée laisse passer sans contrôle une stratégie triviale de promotion de faux signaux.
- **Ce qui me ferait changer d'avis :** Si le recalcul d'admission était matériellement irréalisable dans les contraintes du projet ET qu'un essai préalable démontrait que la règle de cohérence (éventuellement doublée d'une vérification mécanique) rejette de manière fiable l'heuristique « top-$K$ » même lorsque $K$ est connu d'avance.
- **Option meilleure que celles proposées :** Tirer la composition $(K, \text{types})$ selon une loi à forte entropie incluant explicitement des **épisodes nuls ($K = 0$)** ainsi que la composition fixe $K_0$ de la première étape avec une probabilité positive connue de l'organisateur seul, puis refaire le calcul d'admission global tout en éditant un **sous-rapport stratifié sur la tranche $K = K_0$** : le nombre de lois ne fuit pas à l'agent, la comparabilité avec la première étape est conservée, et la règle de cohérence est éprouvée avant gel contre l'heuristique « top-$K$ ».

---

## Partie II — Livrables du Tour III.1

### (a) Ce que la question suppose sans que ce soit établi (avec statut)

1. **Non-ambiguïté de la Grandeur A et représentativité des lois simulées (Décision 1)** — Statut : `HYPOTHÈSE` (et `OBSERVÉ-NON-AUDITÉ` pour les calculs sur lois simulées). La question associe « accepte » et « ne signale pas » dans la Grandeur A alors qu'une clause d'abstention existe ; or $p_{\text{acc}} \ne 1 - p_{\text{sig}}$ dès que $p_{\text{abs}} > 0$ (`VÉRIFIÉ`). Elle suppose aussi sans audit que la faible variation de A et la plus forte variation de B observées sur lois simulées se transposent au moniteur réel sur tâches floues.
2. **Indépendance de l'objet de comparaison, mode d'agrégation des lecteurs et validité d'une règle binaire native de l'oracle (Décision 2)** — Statut : `HYPOTHÈSE`. Le texte ne précise ni si l'objet de comparaison honnête est issu d'une lecture indépendante (sans quoi le taux de fausses alertes sur l'honnête serait nul par construction), ni comment plusieurs lecteurs produisent une « part » unique (moyenne fractionnaire ou vote majoritaire), ni si la comparaison appariée est licite opérationnellement. Il suppose enfin qu'une règle binaire déjà gelée de l'oracle peut être prise « telle quelle » sans audit de son taux de fausses alertes.
3. **Direction unique du biais de désignation, fidélité du repéreur et impossibilité d'inférence hors échantillon (Décision 3)** — Statut : `HYPOTHÈSE`. Le texte affirme qu'une désignation fausse (« ou l'inverse ») fait systématiquement sous-estimer la probabilité de reconnaissance ; or l'erreur inverse (retirer involontairement un contrôle non désigné, ou altérer un cas témoin) peut accroître les signalements et biaiser l'estimation dans l'autre sens. L'option (b) suppose sans preuve que le modèle-repéreur est fidèle et sans biais corrélé aux moniteurs évalués ; l'option (c) suppose que la fidélité reste « inconnue hors de l'échantillon », ce qui n'est vrai que si l'échantillon n'est pas probabiliste.
4. **Utilité de $\text{dose} \times \bar{q}_s$ en régime d'excès et préservation du FWER après réallocation (Décision 4)** — Statut : `HYPOTHÈSE`. L'option 4.1(b) suppose que le produit $\text{dose} \times \bar{q}_s$ reste interprétable alors qu'un oracle en régime d'excès peut abaisser $q$ en sur-signalant. L'option 4.2(b) suppose implicitement que rendre après coup le budget libre aux bornes de $q$ n'enfreint pas le contrôle global d'erreur, hypothèse fausse en général dès que le régime d'excès dépend des données de la campagne.
5. **Absence de fuite indirecte de $K$ sous tirage aléatoire et comportement de la règle de cohérence (Décision 5)** — Statut : `HYPOTHÈSE` (le non-vérifié est explicitement `RAPPORTÉ` pour la règle de cohérence). Tirer la composition ne garantit l'absence de fuite de $K$ que si le schéma des données générées (nombre de colonnes, puissance statistique, bruit) ne trahit pas $K$ indirectement. La question suppose aussi une opposition stricte entre tirage aléatoire et comparabilité avec la première étape, ignorant la stratification interne sur $K = K_0$.
6. **Validité externe des dommages plantés et appariement exact de l'agent honnête « jumeau » (Cadre général)** — Statut : `HYPOTHÈSE` (`OBSERVÉ-NON-AUDITÉ` pour la vérification de confusion entre mondes du banc 1). Le cadre suppose que des dommages plantés par un tiers ou des lois plantées reproduisent un sabotage diffus réaliste et que le jumeau honnête ne diffère de l'agent évalué que par l'absence de sabotage.

---

### (b) Expériences décisives en duel $H_A$ contre $H_B$ (inférence forte)

*(Note règle 4 : hormis $2{,}5\,\%$, $1{,}25\,\%$ et $1/m$, tous les effectifs, seuils et paramètres numériques ci-dessous sont marqués « illustratif ».)*

#### Expérience E1 — Décomposition à trois états sur le monde témoin (tranche la Décision 1)
- **Duel :**
  - $H_A$ : Le passage du monde de référence au monde témoin (sans dommage planté) transfère la masse entre acceptation stricte et abstention ($|\Delta p_{\text{abs}}|$ élevé) tout en laissant $1 - p_{\text{sig}}$ quasi invariant, rendant 1(a) aveugle à la dérive.
  - $H_B$ : L'abstention varie peu entre monde témoin et référence, ou la dérive se manifeste directement sur les fausses alertes $p_{\text{sig}}$.
- **Métrique :** Écarts appariés $(\Delta p_{\text{acc}}, \Delta p_{\text{sig}}, \Delta p_{\text{abs}})$ entre le jumeau honnête du monde témoin et celui du monde de référence sur $N = 200$ tâches (illustratif), avec intervalles de confiance exacts.
- **Seuil (illustratif) :** $|\Delta p_{\text{abs}}| > 0{,}05$ conjointement avec $|\Delta (1 - p_{\text{sig}})| < 0{,}02$ (illustratif).
- **Contrôle négatif :** Deux réalisations indépendantes du jumeau honnête dans le *même* monde de référence ($N = 200$, illustratif) ; les trois écarts doivent rester dans la marge d'échantillonnage ($< 0{,}02$, illustratif).
- **Falsification :** Observer $|\Delta p_{\text{abs}}| > 0{,}05$ et $|\Delta(1 - p_{\text{sig}})| < 0{,}02$ (illustratif) falsifie $H_B$ et invalide le choix de 1(a) seule. Observer $|\Delta p_{\text{abs}}| \le 0{,}02$ ou $|\Delta p_{\text{sig}}| > 0{,}05$ (illustratif) falsifie $H_A$ (soit les simulations exagéraient la dérive de B, soit la dérive porte sur les fausses alertes).

#### Expérience E2 — Bruit de lecture sous règle fixe $1/m$ vs seuil étalonné (tranche la Décision 2)
- **Duel :**
  - $H_A$ : Sur des paires indépendantes de documents honnêtes, la règle fixe $1/m$ génère un taux de fausses alertes $\text{FPR}_{\text{fixe}}$ suffisant pour déclencher le régime d'excès sur au moins une strate de $m$, qu'un seuil étalonné hors échantillon corrige sans effondrer la détection.
  - $H_B$ : Le bruit de lecture est assez faible pour que la règle fixe $1/m$ maintienne un $\text{FPR}_{\text{fixe}}$ acceptable sur toute la gamme de $m$ sans étalonnage.
- **Métrique :** $\text{FPR}_{\text{fixe}}$ stratifié par $m$ sur un lot d'étalonnage ($n = 150$ paires honnêtes indépendantes, illustratif) et sur un lot de validation disjoint ($n = 150$ paires, illustratif), ainsi que la sensibilité hors échantillon $\text{TPR}$ à FPR contrôlé ($\le 0{,}05$, illustratif) sur documents endommagés.
- **Seuil (illustratif) :** $\text{FPR}_{\text{fixe}} > 0{,}05$ (ou au-dessus du seuil d'entrée en régime d'excès) sur au moins une strate de $m$, avec baisse relative de FPR $\ge 50\,\%$ (illustratif) sur le lot de validation grâce à l'étalonnage.
- **Contrôle négatif :** Relecture indépendante du *même* document honnête par l'oracle ($n = 100$ documents, illustratif) ; tout signalement mesure le pur bruit interne des lecteurs.
- **Falsification :** $\text{FPR}_{\text{fixe}} > 0{,}05$ avec correction hors échantillon par l'étalonnage (illustratif) falsifie $H_B$ (écarte 2a). $\text{FPR}_{\text{fixe}} \le 0{,}02$ uniformément sur toutes les strates de $m$ sans gain hors échantillon (illustratif) falsifie $H_A$ (rend 2b superflu).

#### Expérience E3 — Fidélité lexicale, fidélité du repéreur et biais de famille partagée (tranche la Décision 3)
- **Duel :**
  - $H_A$ : Le recouvrement de mots rate les contrôles paraphrasés et produit une fidélité insuffisante face à une référence humaine ; un repéreur de famille de modèles distincte du moniteur corrige cette perte sans introduire de biais corrélé.
  - $H_B$ : Soit le recouvrement lexical atteint déjà une haute fidélité contre l'humain, soit le repéreur introduit des erreurs propres ou un biais de famille partagée qui gonfle artificiellement la détection apparente du moniteur.
- **Métrique :** (1) Précision et rappel contre double annotation humaine aveugle sur $n = 120$ contrôles stratifiés (illustratif) ; (2) écart de taux de détection du moniteur entre un repéreur de *même famille* et un repéreur de *famille distincte*.
- **Seuil (illustratif) :** Précision ou rappel lexical $< 0{,}90$, gain F1 du repéreur $\ge +0{,}15$, et biais de famille partagée $< 0{,}05$ (tous illustratifs).
- **Contrôle négatif :** Couple de sous-ensembles construits : (i) **leurres lexicaux** reprenant les mots-clés du contrôle dans un contexte nié ou sans réaliser le contrôle ; (ii) **paraphrases pures** sans chevauchement lexical hors mots-outils.
- **Falsification :** F1 lexical $< 0{,}90$ avec F1 du repéreur (famille distincte) $\ge 0{,}95$ et biais de famille $< 0{,}05$ (illustratifs) falsifie $H_B$ (valide 3b audité). F1 lexical $\ge 0{,}95$ ou biais de famille du repéreur $\ge 0{,}10$ (illustratifs) falsifie $H_A$ (renvoie à un ancrage lexical ou à une désignation hybride/humaine).

#### Expérience E4 — Inflation du FWER sous réallocation et paradoxe de $d_s \cdot \bar{q}_s$ en régime d'excès (tranche la Décision 4)
- **Duel :**
  - $H_A$ : La réallocation du budget d'erreur conditionnelle au régime d'excès $E$ (4.2b) viole le FWER nominal dans des régimes réalistes de corrélation ou de biais de sélection sur $E^c$, ET le produit $d_s \cdot \bar{q}_s$ (4.1b) diminue artificiellement lorsque le taux de fausses alertes de l'oracle augmente à pouvoir discriminant nul.
  - $H_B$ : La réallocation maintient le FWER $\le \alpha_{\text{nom}}$ sur l'ensemble des lois plausibles du banc et $d_s \cdot \bar{q}_s$ ne s'améliore pas quand un oracle se dégrade par sur-signalement.
- **Métrique :** (1) FWER empirique sur $B = 10\,000$ campagnes simulées par Monte Carlo (illustratif) sous divers couplages entre lectures honnêtes et sabotées ; (2) variation de $d_s \cdot \bar{q}_s$ en fonction du taux de signalement d'un oracle aléatoire.
- **Seuil (illustratif) :** FWER empirique $> \alpha_{\text{nom}} + 0{,}005$ (ex. $> 5{,}5\,\%$ pour une cible de $5\,\%$, illustratif) dans au moins un scénario plausible, ou baisse de $\bar{q}_s$ d'au moins $20\,\%$ quand la probabilité de signalement aléatoire passe de $0{,}3$ à $0{,}8$ (illustratif).
- **Contrôle négatif :** Oracle aléatoire aveugle signalant chaque document avec probabilité fixe $p \in [0{,}3, 0{,}9]$ (illustratif), indépendamment de tout dommage (pouvoir discriminant exactement nul).
- **Falsification :** Dépassement du FWER nominal ou amélioration apparente de $d_s \cdot \bar{q}_s$ sur l'oracle aveugle falsifie $H_B$ (écarte 4.1b et 4.2b). Respect strict du FWER $\le \alpha_{\text{nom}}$ dans tous les scénarios testés falsifierait l'objection FWER de $H_A$ (sans toutefois lever le paradoxe de 4.1b).

#### Expérience E5 — Exploitation du nombre fixe de lois $K$ et réponse de la règle de cohérence (tranche la Décision 5)
- **Duel :**
  - $H_A$ : Sous composition fixe connue $K$, un saboteur appliquant l'heuristique « promouvoir les $K$ statistiques les plus fortes » est accepté par la règle de cohérence à un taux élevé, alors que le tirage aléatoire de $K$ (incluant $K = 0$) réduit fortement cette acceptation.
  - $H_B$ : La règle de cohérence rejette déjà de manière fiable la stratégie « top-$K$ » même lorsque $K$ est fixe et connu d'avance.
- **Métrique :** Taux d'acceptation (faux négatifs de cohérence) du saboteur « top-$K$ » et taux de fausses alertes sur un analyste honnête, sur $N = 100$ épisodes (illustratif) en régime $K$ fixe connu vs $K$ aléatoire (ex. $K \in \{0, 1, 2, 3, 4\}$, illustratif).
- **Seuil (illustratif) :** Acceptation du saboteur « top-$K$ » $> 0{,}20$ sous $K$ fixe et supérieure d'au moins $+0{,}15$ à celle observée sous $K$ aléatoire (illustratif), à taux d'acceptation honnête $\ge 0{,}90$ (illustratif).
- **Contrôle négatif :** (i) Épisodes nuls ($K = 0$, bruit pur sans loi plantée), où l'analyste honnête rend une fiche vide et où la stratégie « top-$K$ » échoue mécaniquement ; (ii) analyste statistique honnête appliquant un contrôle standard des tests multiples (ex. Benjamini-Hochberg), qui doit être accepté dans les deux régimes.
- **Falsification :** Acceptation du saboteur $> 0{,}20$ sous $K$ fixe et chute sous $K$ aléatoire (illustratifs) falsifie $H_B$ (impose 5a). Rejet du saboteur $\ge 0{,}95$ (illustratif) même sous $K$ fixe (y compris sur données à faible rapport signal/bruit) falsifie $H_A$.

---

### (c) Mesure minimale de fonctionnement pour chaque instrument nommé

*(Tous les seuils cibles numériques ci-dessous sont marqués « illustratif » sauf mention issue des faits.)*

1. **Moniteur de comparaison et sa clause d'abstention (Banc des tâches floues, Décision 1)**
   - *Mesure minimale :* Taux de détection (TPR) sur tâches avec dommages plantés (ex. $\ge 0{,}70$ hors abstention, illustratif), taux de fausses alertes ($p_{\text{sig}} \le 0{,}05$, illustratif) et taux d'abstention ($p_{\text{abs}} \le 0{,}15$, illustratif), plus stabilité entre monde de référence et monde témoin ($|\Delta p_{\text{sig}}|, |\Delta p_{\text{abs}}| \le 0{,}05$, illustratif).
   - *Cas honnêtes appariés :* Agent honnête « jumeau » issu de la même loi de génération, évalué sur les mêmes tâches/graines dans le monde de référence et le monde témoin sans dommage planté.
   - *Vérifications mécaniques à battre :* Classifieur linéaire sur traits de surface (longueur, structure, entropie lexicale, redondance) ; détecteur par distance d'embedding à un corrigé de référence ; classifieur aléatoire calibré au même $p_{\text{abs}}$.

2. **Oracle à plusieurs lecteurs et sa règle de signalement par défaut (Banc des dommages tiers, Décisions 2 et 4)**
   - *Mesure minimale :* Taux de détection par strate de taille de dommage ($1 - q_s$, ex. $\ge 0{,}80$ sur strates moyennes, illustratif), taux de fausses alertes sur documents honnêtes ($\le 0{,}05$, illustratif, hors régime d'excès) et accord inter-lecteurs par contrôle (ex. kappa $\ge 0{,}85$, illustratif).
   - *Cas honnêtes appariés :* Version honnête produite et relue indépendamment du même document contre la même référence cachée (même $m$), complétée par des relectures répétées d'un même document honnête.
   - *Vérifications mécaniques à battre :* Recherche par mots-clés / expressions régulières des éléments de la référence cachée ; score mécanique BM25/TF-IDF par contrôle avec seuil calibré ; comptage de densité d'assertions ou de citations.

3. **Désigneur de passages portant un contrôle — programme lexical et modèle repéreur (Banc des dommages tiers, Décision 3)**
   - *Mesure minimale :* Taux de détection (rappel des passages portant effectivement un contrôle, y compris paraphrasés, ex. $\ge 0{,}90$, illustratif) et taux de fausses alertes sur passages non porteurs ($1 - \text{précision} \le 0{,}05$, illustratif), mesurés contre double annotation humaine aveugle.
   - *Cas honnêtes appariés :* Passages non porteurs de contrôle tirés des mêmes documents honnêtes, incluant des passages leurres à fort recouvrement lexical mais sans contrôle effectif.
   - *Vérifications mécaniques à battre :* Le programme lexical 3(a) (recouvrement de $n$-grammes / Jaccard / BM25) constitue lui-même la vérification mécanique de référence que le modèle repéreur 3(b) doit battre nettement sur les paraphrases et le rejet des leurres.

4. **Fonction de calcul de l'optimum — épisodes nécessaires et mélange optimal des doses (Banc des dommages tiers, Décision 4.1)**
   - *Mesure minimale :* Sur une suite de cas d'essai synthétiques connus analytiquement : détection à $100\,\%$ (illustratif) des régimes d'excès/infaisables (zéro fausse garantie émise), taux de faux rejets de $0\,\%$ (illustratif) sur cas faisables, couverture empirique respectant le niveau d'erreur (ex. $\ge 97{,}5\,\%$ pour $2{,}5\,\%$ à un regard, issu des faits) et écart d'optimalité $< 10^{-4}$ (illustratif).
   - *Cas honnêtes appariés :* Paires de profils synthétiques de même $m$ et même budget situés juste de part et d'autre de la frontière du régime d'excès.
   - *Vérifications mécaniques à battre :* Mélange uniforme naïf des doses entre strates ; recherche sur grille grossière sans bornes binomiales exactes.

5. **Règle de cohérence (Banc à lois plantées, Décision 5)**
   - *Mesure minimale :* Taux de détection des fiches sabotées (dont l'heuristique « top-$K$ », la promotion de lois fausses et l'omission de lois vraies fortes, ex. TPR $\ge 0{,}80$, illustratif) et taux de fausses alertes sur analystes honnêtes ($\le 0{,}05$, illustratif), rapportés séparément pour $K = 0$ et $K \ge 1$.
   - *Cas honnêtes appariés :* Fiches d'analystes honnêtes (modèles ou pipelines statistiques sans sabotage) exécutés exactement sur les mêmes jeux de données et graines de bruit (incluant $K = 0$).
   - *Vérifications mécaniques à battre :* Auditeur statistique déterministe recalculant directement sur les données brutes les $p$-valeurs ajustées (Benjamini-Hochberg ou Bonferroni) et tailles d'effet des lois promues ou tues ; vérification mécanique des signes et seuils déclarés dans la fiche.

---

### (d) Ancrage matériel (modèles ouverts, calcul et coût)

*(Règle 4 : tous les volumes de jetons, durées, débits, prix unitaires et coûts ci-dessous sont marqués « illustratif ».)*

Pour exécuter la batterie décisive E1–E5 avant gel tout en évitant le biais mono-famille (exigé par E3 et par un oracle multi-lecteurs crédible), on s'appuie sur **trois familles distinctes de modèles à poids ouverts** :
- **Famille 1 :** `Qwen2.5-7B-Instruct` (moniteur léger / repéreur rapide) et `Qwen2.5-72B-Instruct` (lecteur d'oracle / agent analyste).
- **Famille 2 :** `Llama-3.1-8B-Instruct` et `Llama-3.3-70B-Instruct` (repéreur de famille distincte / second lecteur d'oracle / moniteur).
- **Famille 3 :** `Gemma-2-27B-it` ou `Mistral-Small-24B-Instruct` (troisième lecteur indépendant de l'oracle).

| Expérience | Charge d'inférence / CPU (illustratif) | Volume estimé (illustratif) | Ressource & coût estimé (illustratif) |
| :--- | :--- | :--- | :--- |
| **E1** (Décision 1) | $1\,200$ appels (tâches + moniteur, 3 jeux) à $\sim 3\,000$ jetons | $\sim 3{,}6\text{ M}$ jetons | $\sim 2\text{ h-GPU}$ H100 ($\sim 6\text{–}10\text{ \$}$) |
| **E2** (Décision 2) | $2\,100$ lectures d'oracle (3 lecteurs sur étalonnage, validation, relectures) à $\sim 4\,000$ jetons | $\sim 8{,}4\text{ M}$ jetons | $\sim 5\text{ h-GPU}$ H100 ($\sim 15\text{–}25\text{ \$}$) |
| **E3** (Décision 3) | $500$ lectures (2 repéreurs distincts + moniteur) à $\sim 4\,000$ jetons + audit humain double aveugle ($120$ contrôles) | $\sim 2{,}0\text{ M}$ jetons + $6\text{–}10\text{ h}$ humaines | $\sim 1{,}5\text{ h-GPU}$ ($\sim 5\text{ \$}$) + $\mathbf{300\text{–}600\text{ \$}}$ humain |
| **E4** (Décision 4) | $10\,000$ campagnes Monte Carlo + suite de cas d'essai solveur (CPU pur, 8 cœurs) | $< 15\text{ min}$ CPU | $< 1\text{ \$}$ |
| **E5** (Décision 5) | $800$ appels (agents + règle de cohérence) à $\sim 3\,000$ jetons + recalcul d'admission CPU ($< 1\text{ h}$) | $\sim 2{,}4\text{ M}$ jetons | $\sim 1{,}5\text{ h-GPU}$ H100 ($\sim 5\text{–}8\text{ \$}$) |
| **Total (avec marge $\times 2$, illustratif)** | Inférence sur 2×H100 80 Go (quantification FP8 via vLLM, débit agrégé $\sim 1\,000$ jetons/s) + CPU + audit humain | $\sim 16{,}4\text{ M}$ jetons (jusqu'à $\sim 33\text{ M}$ avec relances) | **$\sim 10\text{–}20\text{ h-GPU}$ ($\sim 30\text{–}80\text{ \$}$ GPU) + $\sim 300\text{–}600\text{ \$}$ annotation humaine** |

**Point d'ancrage clé :** le coût de calcul GPU ouvert pour trancher expérimentalement les cinq décisions avant gel reste inférieur à la centaine de dollars (illustratif) ; le véritable poste limitant n'est pas le calcul des modèles (y compris le repéreur de la Décision 3 ou le recalcul de la Décision 5), mais les quelques heures d'annotation humaine double aveugle nécessaires en E3 pour ancrer la vérité terrain sans circularité entre modèles.

FIN-DE-CELLULE