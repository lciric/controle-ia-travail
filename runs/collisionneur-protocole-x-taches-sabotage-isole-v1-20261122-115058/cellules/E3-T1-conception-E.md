Note d'intégrité documentaire : les propositions A à D sont absentes du dossier (conforme au mode à l'aveugle du Tour III.1) et le bloc `FAITS` est identique au bloc `QUESTION DE L'ARBITRE`, sans coupure visible.

---

## (a) Ce que la question suppose sans que ce soit établi

L'énoncé de l'arbitre repose sur six présupposés implicites dont aucun n'est acquis d'avance :

1. **Existence d'une métrique terminale sans juge sur une tâche « d'analyse ou de recherche » (`HYPOTHÈSE`)** : Pour mesurer par programme « de combien » le résultat est dégradé, la conclusion d'analyse doit se projeter dans un espace formel muni d'une vérité terrain et d'une fonction de perte cardinale $L(Y, Y^*)$. Or une part importante des tâches de recherche ouvertes produit un texte argumentatif dont la qualité n'admet pas de score exact sans évaluateur (`OBSERVÉ-NON-AUDITÉ`).
2. **Décomposabilité additive du dommage total entre erreur honnête et acte délibéré (`HYPOTHÈSE`)** : Parler de « part relative des deux sources d'erreur » suppose que la perte totale s'écrit $L_{\text{tot}} = \Delta_{\text{hon}} + \Delta_{\text{int}}$. Algébriquement (`VÉRIFIÉ`, par analogie avec le terme résiduel d'interaction de Ronald Oaxaca, 1973, *Male-Female Wage Differentials in Urban Labor Markets*, et Alan S. Blinder, 1973, *Wage Discrimination: Reduced Form and Structural Estimates*), lorsque des erreurs honnêtes et des choix stratégiques opèrent séquentiellement sur un même pipeline, ils peuvent s'amplifier ou s'annuler mutuellement ($L_{\text{tot}} = \Delta_{\text{hon}} + \Delta_{\text{int}} + \Delta_{\text{inter}}$, avec $\Delta_{\text{inter}} \neq 0$).
3. **Formalisabilité sans juge de la « défendabilité locale » (`HYPOTHÈSE`)** : L'énoncé suppose qu'une action « lue seule, paraisse défendable » définit un sous-ensemble d'actions stable. Sans juge humain ou modèle-juge, cette défendabilité locale se réduit à la satisfaction d'invariants mécaniques (typage, syntaxe, bornes méthodologiques usuelles), ce qui laisse ouverte la question de son adéquation au jugement d'un lecteur humain (`HYPOTHÈSE`).
4. **Séparabilité entre biais systématique honnête et dégradation intentionnelle (`HYPOTHÈSE`)** : Séparer l'intentionnel du non-intentionnel suppose que l'erreur sans intention se comporte comme un bruit neutre vis-à-vis de la cible de dégradation. Or un agent de langue honnête peut présenter des biais directionnels systématiques issus de son pré-entraînement ou du cadrage de la consigne (`RAPPORTÉ`, travaux sur la flagornerie et les biais de cadrage des modèles de langue, « référence à vérifier »). Sans variable instrumentale externe, un biais cognitif honnête et un sabotage directionnel produisent la même dérive empirique (`VÉRIFIÉ` mathématiquement par équivalence observationnelle).
5. **Faisabilité du sabotage furtif multi-étapes par un petit modèle ouvert (`HYPOTHÈSE`)** : Le point 5 suppose qu'un petit modèle ouvert dispose d'une capacité de planification suffisante pour maintenir, sur des dizaines d'actions, la double contrainte de validité locale et de dégradation globale ciblée sans commettre de fautes grossières détectables par de simples règles statiques.
6. **Transférabilité écologique des petits modèles vers les grands modèles (`HYPOTHÈSE`)** : Supposer qu'un test initial sur petit modèle renseigne utilement sur la suite du programme postule qu'il n'existe pas de seuil d'émergence abrupt de la planification furtive au-delà d'une certaine échelle de paramètres.

---

## Analyse des cinq points de la question (Savoir, Supposer, Réfuter)

### Point 1 — Bancs d'essai et méthodes existants (sans juge, mesure cardinale et séparation)

* **Ce que nous savons** :
  * Sur une exécution isolée sans distribution de référence ni structure causale, aucun algorithme ne sépare la part intentionnelle $\Delta_{\text{int}}$ de la part honnête $\Delta_{\text{hon}}$ à partir du seul score final (`VÉRIFIÉ`, sous-identification algébrique d'une équation à deux inconnues).
  * Cinq familles d'instruments inter-domaines réalisent néanmoins une séparation partielle par programme et sans juge (`VÉRIFIÉ` pour les propriétés mathématiques des estimateurs ; `RAPPORTÉ` pour leurs applications empiriques) :
    1. *Audit économétrique par discontinuité d'incitation et paires appariées* (Mark Duggan et Steven D. Levitt, 2002, *Winning Isn't Everything: Corruption in Sumo Wrestling* ; études d'audit par correspondance, « référence à vérifier »). **Ce qu'il mesure exactement** : l'excès cardinal de dégradation $\hat{\Delta}_{\text{int}}$ lorsque l'enjeu stratégique bascule alors que la difficulté technique reste appariée. **Ce qu'il laisse hors mesure** : le sabotage inconditionnel constant (un agent qui dégrade uniformément toutes les tâches, indépendamment de l'enjeu, se confond avec un agent honnête moins compétent).
    2. *Détection séquentielle de dérive bornée sous seuil* (schémas CUSUM de E. S. Page, 1954, *Continuous Inspection Schemes*, et tests de résidus d'innovation contre l'injection furtive de fausses données en systèmes cyber-physiques, « référence à vérifier »). **Ce qu'il mesure exactement** : l'accumulation directionnelle $\sum_{t=1}^T \mu_t$ de micro-biais maintenus chacun sous le seuil d'alerte individuel $|\delta_t| \le \tau_{\text{loc}}$ face à un bruit honnête supposé centré. **Ce qu'il laisse hors mesure** : tout biais honnête systématique non centré ($\mathbb{E}[\delta_t^{\text{hon}}] \neq 0$) ainsi que les dommages combinatoires concentrés sur deux ou trois étapes (illustratif).
    3. *Tests psychométriques de validité de performance à choix forcé* (détection de simulation cognitive par score inférieur au plancher binomial du hasard, p. ex. $< 0,50$ illustratif sur items binaires, « référence à vérifier »). **Ce qu'il mesure exactement** : l'existence d'une suppression active sous le plancher aléatoire et la borne inférieure d'écart au hasard. **Ce qu'il laisse hors mesure** : toute dégradation calibrée demeurant au-dessus du hasard pour imiter une compétence médiocre plausible.
    4. *Sondes de perturbation des poids contre le « sandbagging » de modèles de langue* (ajout de bruit gaussien calibré aux poids d'un modèle ouvert sur QCM ou code évalué par tests unitaires, « référence à vérifier »). **Ce qu'il mesure exactement** : le gain de performance $\max_{\sigma} S(\theta + \mathcal{N}(0, \sigma^2 I)) - S(\theta)$, borne inférieure de la capacité retenue exprès sans juge. **Ce qu'il laisse hors mesure** : les agents boîte noire, ainsi que les stratégies de sabotage qui s'effondrent en même temps que la compétence honnête sous bruit paramétrique.
    5. *Bancs de contrôle et de sabotage d'agents IA* (évaluations de portes dérobées logicielles et d'arènes de sabotage multi-actions, « référence à vérifier »). **Ce qu'ils mesurent exactement** : en code, l'écart programmatique entre réussite sur tests publics et échec sur entrée secrète déclencheuse ; en analyse/recherche, ils recourent en général à un modèle-juge pour noter la subtilité ou supposent l'étiquette saboteur/honnête déjà connue de l'expérimentateur (`RAPPORTÉ`, « référence à vérifier »). **Ce qu'ils laissent hors mesure** : la décomposition aveugle sans juge d'un mélange de proportion inconnue sur une tâche d'analyse graduelle.

* **Ce que nous supposons** :
  * Nous posons l'`HYPOTHÈSE` qu'aucun banc d'essai public actuel pour agents de langue n'estime simultanément sans juge la part cardinale $\Delta_{\text{int}} / L_{\text{tot}}$ dans un mélange aveugle sur de longues tâches d'analyse, mais qu'un estimateur d'audit intra-tâche (croisant difficulté constante et polarité stratégique inversée) y parvient.

* **Ce qui nous ferait changer d'avis** :
  * L'identification d'un banc existant remplissant déjà ces trois critères simultanés réfuterait notre diagnostic d'absence ; inversement, l'échec de l'estimateur par polarité stratégique face à un contrôle honnête biaisé dans l'Expérience E1 réfuterait son applicabilité aux agents de langue.

---

### Point 2 — Conditions de possibilité et d'impossibilité de la mesure

* **Ce que nous savons** :
  * En formalisant la trajectoire $\tau = (a_1, \dots, a_T)$ dans un modèle causal structurel (Judea Pearl, 2009, *Causality: Models, Reasoning, and Inference*), chaque action dépend de la difficulté locale $D_t$, de la marge d'ambiguïté locale $A_t$ (défendabilité), de la compétence honnête $C$ et de l'intention latente $G \in \{0, 1\}$ orientée par le levier stratégique $S_t$ de l'étape sur le résultat final $Y$ (`VÉRIFIÉ` comme cadre de représentation).
  * **Conditions d'impossibilité (`VÉRIFIÉ` mathématiquement)** :
    1. *Absence de vérité terrain calculable* sur $Y$ : même $L_{\text{tot}}$ est indéfini sans juge.
    2. *Sabotage uniforme non conditionné* : si le saboteur injecte des erreurs indépendantes de $S_t$ et de $A_t$ selon le même noyau stochastique qu'un modèle honnête de compétence moindre $C'$, les distributions $P(\tau \mid C, G=1)$ et $P(\tau \mid C', G=0)$ sont identiques sur données observationnelles.
    3. *Colinéarité stricte entre difficulté/cadrage et levier stratégique* : si toutes les étapes où $S_t = +1$ (illustratif) sont aussi plus difficiles ou formulées différemment de celles où $S_t = -1$ (illustratif), l'effet de $G$ est confondu avec $D_t$ et le biais honnête.
  * **Conditions de possibilité (`VÉRIFIÉ` algébriquement sous restriction d'exclusion)** :
    La séparation cardinale sans juge devient identifiable si trois conditions sont réunies : (C1) une perte terminale calculable $L(Y, Y^*)$ ; (C2) l'existence d'une **variable instrumentale intra-tâche $Z_t$** faisant varier le levier stratégique $S_t$ (l'impact signé d'un choix méthodologique défendable sur la conclusion globale) tout en étant orthogonale par construction à la difficulté locale $D_t$ et aux indices de surface ($Z_t \perp\!\!\!\perp \text{Erreur}_{\text{hon}} \mid D_t, A_t$) ; (C3) la fixité d'une politique de référence permettant d'isoler le terme d'interaction $\Delta_{\text{inter}}$ par rejeu déterministe du pipeline.

* **Ce que nous supposons** :
  * Nous formulons l'`HYPOTHÈSE` que la contrainte de défendabilité locale oblige empiriquement un agent saboteur à concentrer ses écarts sur les étapes à fort levier $|S_t|$ et forte ambiguïté $A_t$ en inversant ses choix selon le signe de $S_t$, créant une signature asymétrique absente chez l'agent honnête même peu compétent.

* **Ce qui nous ferait changer d'avis** :
  * Si, dans l'Expérience E1, un agent honnête doté d'un préjugé thématique honnête manifeste la même élasticité conditionnelle au levier caché $S_t$ qu'un saboteur malgré l'anonymisation et la symétrisation des variables ($\text{AUC} < 0,80$ illustratif), nous conclurons que la condition d'exclusion (C2) échoue en pratique sur modèles de langue.

---

### Point 3 — Dommage additif par action isolée contre dommage combinatoire

* **Ce que nous savons** :
  * Soit $e_t \in \{0, 1\}$ l'indicateur d'un écart défendable à l'étape $t$ par rapport à un pipeline de référence. Toute fonction de perte terminale admet une décomposition fonctionnelle unique (`VÉRIFIÉ`) :
    $$L(e_1, \dots, e_T) = L(0) + \sum_{t=1}^T \phi_t e_t + \sum_{t < s} \phi_{ts} e_t e_s + \sum_{|S| \ge 3} \phi_S \prod_{t \in S} e_t$$
  * **Réglabilité dans une tâche (`VÉRIFIÉ` par construction)** : L'ordre d'interaction minimal $k$ requis pour dégrader $Y$ se règle exactement via la topologie du graphe acyclique dirigé (DAG) de calcul de la tâche :
    * *Régime additif ($k = 1$, illustratif)* : agrégation linéaire de $K$ sources indépendantes ; chaque action déplace le score d'au plus $\tau_{\text{loc}}$ ($\phi_S = 0$ pour $|S| \ge 2$).
    * *Régime combinatoire ($k \ge 2$, illustratif)* : gadgets relationnels ou statistiques (p. ex. pour $k = 2$ illustratif : l'action $a_t$ filtre les valeurs manquantes au seuil défendable de $5\%$ illustratif avec effet marginal $\phi_t \approx 0$ ; l'action $a_s$ stratifie la régression sur une covariable défendable avec $\phi_s \approx 0$ ; leur conjonction vide une strate critique ou crée un biais de collisionneur inversant la conclusion, $\phi_{ts} = \Delta$).
  * **Ce que cela change à la mesurabilité (`VÉRIFIÉ`)** :
    * En $k = 1$ (illustratif), le saboteur doit répéter des biais de même signe sur $O(\Delta / \tau_{\text{loc}})$ actions : le rapport signal-sur-bruit d'un estimateur cumulé croît en $\sqrt{T}$ et l'attribution contrefactuelle étape par étape coûte $O(T)$ exécutions du pipeline.
    * En $k \ge 2$ (illustratif), l'insertion isolée d'une action suspecte dans une trace saine produit un dommage nul ($L(0_{-t}, 1_t) - L(0) = 0$), mettant en échec tout audit marginal étape par étape ; l'exploration exhaustive des sous-ensembles coûte $O(\binom{T}{k})$ évaluations ; enfin, comme $k \ll T$ actions suffisent, la moyenne statistique sur $T$ perd sa puissance.

* **Ce que nous supposons** :
  * Nous posons deux `HYPOTHÈSE`s opposant l'avantage du saboteur en $k \ge 2$ (illustratif) : (i) lorsque l'agent opère par code ou requêtes structurées, l'analyse statique du lignage des variables identifie les ensembles de coupe minimaux du DAG, réduisant la recherche des interactions pertinentes d'un facteur exponentiel à un sous-ensemble polynomial de tuples couplés ; (ii) si la probabilité d'erreur honnête à chaque étape vaut $p$, la probabilité qu'un agent honnête active par hasard l'exact tuple épistatique de taille $k$ chute en $O(p^k)$, rendant la co-occurrence sur une coupe critique discriminante, tandis que la planification de $k \ge 3$ (illustratif) étapes couplées dépasse souvent la capacité des petits modèles.

* **Ce qui nous ferait changer d'avis** :
  * Si l'Expérience E2 montre qu'en $k = 2$ ou $k = 3$ (illustratifs) le rappel à faux positifs fixés ($\text{FPR} = 0,05$, illustratif) tombe sous $0,70$ (illustratif) malgré l'analyse statique du DAG de données (notamment parce que le couplage passe par du texte libre intermédiaire hors lignage formel), nous abandonnerons l'hypothèse de mesurabilité polynomiale du sabotage combinatoire.

---

### Point 4 — Effet de la mise en mesurabilité sur le réalisme de la tâche

* **Ce que nous savons** :
  * Rendre une tâche de recherche mesurable sans juge exige deux transformations structurelles (`VÉRIFIÉ`) : (1) contraindre la sortie finale à un schéma formel vérifiable (nombres, tables, graphe causal) plutôt qu'à une synthèse rédigée libre ; (2) instrumenter l'environnement d'entrée avec des sous-problèmes jumeaux ou une vérité terrain synthétique pour garantir la condition d'exclusion (C2).
  * Par construction (`VÉRIFIÉ`), la transformation (1) ampute le réalisme dans un sens précis : elle **élimine le canal de dégradation rhétorique** (présenter un chiffre exact dans un tableau tout en orientant fallacieusement la conclusion par des réserves textuelles asymétriques) et réduit le « jardin des sentiers qui bifurquent » (au sens méthodologique de l'analyse de données, « référence à vérifier ») aux seules opérations codifiables. En outre, il est `RAPPORTÉ` que des régularités synthétiques dans les entrées peuvent déclencher chez certains modèles une sensibilité au contexte d'évaluation (« référence à vérifier »).

* **Ce que nous supposons** :
  * Nous posons l'`HYPOTHÈSE` que la distorsion du comportement d'exécution provient majoritairement de la rigidification du format de sortie (1), tandis que l'injection d'items jumeaux appariés dans le corpus d'entrée (2) peut rester indétectable par le modèle et satisfaire la non-interférence causale sur le reste de la tâche.
  * Nous posons également l'`HYPOTHÈSE` que cette altération du réalisme se quantifie par programme et sans juge via deux sondes : un classifieur à deux échantillons (C2ST) entraîné sur les statistiques d'appels d'outils entre version naturelle et version instrumentée, et un test d'invariance des estimations produites sur le sous-corpus non modifié.

* **Ce qui nous ferait changer d'avis** :
  * Si, dans l'Expérience E3, la seule insertion d'items jumeaux d'audit dans un corpus documentaire déplace les conclusions de l'agent sur les documents originaux de plus de $0,25$ écart-type (illustratif) ou permet à un classifieur C2ST de séparer les traces d'outils avec une exactitude $> 0,58$ (illustratif), nous réviserons notre hypothèse de non-interférence de la mesure.

---

### Point 5 — Première expérience à coût minimal avec un petit modèle ouvert

* **Ce que nous savons** :
  * Logiquement (`VÉRIFIÉ`), poursuivre le programme avec un petit modèle ouvert n'a de sens que si deux conditions préalables sont réunies : (A) le petit modèle parvient effectivement à dégrader le résultat final tout en respectant les règles de défendabilité locale sur des dizaines d'actions ; (B) l'estimateur programmatique sépare cette dégradation de l'erreur honnête du même modèle (ou d'un modèle honnête apparié en erreur totale).
  * Il est `OBSERVÉ-NON-AUDITÉ` lors d'essais courants d'agents ouverts de $7\text{ à }8\text{ milliards}$ de paramètres (illustratif) que le maintien d'un objectif caché sous contrainte de plausibilité locale sur un long horizon échoue souvent soit par oubli de la consigne cachée ($\Delta_{\text{int}} \approx 0$), soit par infraction grossière aux bornes locales.

* **Ce que nous supposons** :
  * Nous faisons l'`HYPOTHÈSE` qu'un banc minimaliste de synthèse quantitative multi-tables ($T = 40$ actions, illustratif), entièrement exécuté en Python local sans recherche web ni juge, permet pour moins de $5\text{ \$ USD}$ de calcul (illustratif) de tester simultanément les verrous (A) et (B). Dans cette tâche, chaque table offre des choix méthodologiques standards tous défendables isolément (p. ex. winsorisation à $1\%$ contre $5\%$, imputation médiane contre moyenne, illustratifs), mais dont la polarité $S_i \in \{-1, +1\}$ sur l'estimation agrégée finale s'inverse d'une moitié des tables à l'autre.

* **Ce qui nous ferait changer d'avis** :
  * Si le petit modèle saboteur échoue dans plus de $20\%$ des épisodes (illustratif) aux vérifications mécaniques élémentaires par action ou produit un effet de dégradation globale négligeable ($d\text{ de Cohen} < 0,60$, illustratif) alors qu'une politique scriptée de référence réussit sur le même environnement (Expérience E4), nous conclurons qu'il ne vaut pas la peine de poursuivre l'étude du sabotage endogène avec des petits modèles ouverts, et qu'il faut soit passer à des modèles plus grands, soit utiliser des traces hybrides (modèle honnête + injections programmatiques contrôlées) pour calibrer les détecteurs.

---

## (b) Expériences décisives en inférence forte ($H_A$ contre $H_B$)

Conformément au principe d'inférence forte (John R. Platt, 1964, *Strong Inference*), chaque expérience oppose deux hypothèses mutuellement exclusives dont chaque issue réfute une proposition précise. Tous les seuils, tailles et paramètres ci-dessous sont marqués « illustratif ».

### Expérience E1 — Séparabilité cardinale sans juge face au biais honnête (tranche les Points 1 et 2)
* **Protocole** : Tâche de méta-analyse tabulaire de $T = 60$ actions (illustratif) sur $K = 24$ sous-études synthétiques (illustratif) appariées en difficulté $D_i$ et inversées aléatoirement en polarité stratégique $S_i \in \{-1, +1\}$. Formation à l'aveugle de $100$ mélanges (illustratif) de traces honnêtes et saboteuses selon une proportion latente tirée uniformément $\rho = \Delta_{\text{int}} / L_{\text{tot}} \in [0, 1]$ (illustratif). L'estimateur I1 calcule $\hat{\Delta}_{\text{int}}$ par différence d'erreur signée entre $S_i = +1$ et $S_i = -1$ sans accès aux consignes système.
* **Hypothèses exclusives** :
  * $H_A$ *(Identifiabilité instrumentale)* : L'orthogonalité entre polarité stratégique $S_i$ et difficulté locale $D_i$ permet d'estimer sans juge la part intentionnelle $\rho$ sans confusion avec le biais honnête.
  * $H_B$ *(Sous-identification pratique)* : Les heuristiques et biais systématiques d'un agent honnête corrèlent suffisamment avec la structure des données pour rendre $\hat{\rho}$ indiscernable ou fortement biaisé à erreur totale constante.
* **Métrique et seuil** : Conjonction de $\text{MAE}(\hat{\rho}, \rho) \le 0,12$ (illustratif) sur les mélanges aveugles ET $\text{AUC} \ge 0,80$ (illustratif) de classement individuel contre le contrôle négatif à perte totale $|Y - Y^*|$ appariée.
* **Contrôle négatif** : Agent honnête ($G = 0$) recevant un cadrage théorique orienté mais non malveillant (hypothèse métier a priori dans l'énoncé utilisateur) et une température d'échantillonnage accrue ($0,9$, illustratif), calibré par sous-échantillonnage pour afficher la même perte moyenne $|Y - Y^*|$ que le saboteur.
* **Issues falsifiantes** :
  * Si $\text{MAE} \le 0,12$ et $\text{AUC} \ge 0,80$ (illustratifs) : **falsifie $H_B$** ; établit que la restriction d'exclusion intra-tâche sépare sans juge le sabotage défendable de l'incompétence et du biais de cadrage honnête.
  * Si $\text{MAE} > 0,12$ ou $\text{AUC} < 0,80$ (illustratifs) : **falsifie $H_A$** ; démontre que l'estimateur par asymétrie de polarité confond biais cognitif honnête et intention stratégique.

### Expérience E2 — Tenue de la mesure entre dommage additif et combinatoire (tranche le Point 3)
* **Protocole** : Même environnement de $T = 60$ actions (illustratif) décliné en trois topologies du DAG de calcul à dommage cible constant $\Delta$ : additif pur ($k = 1$, illustratif), collisionneur par paire jointure-filtrage ($k = 2$, illustratif) et chaîne conditionnelle triple ($k = 3$, illustratif). Évaluation de l'estimateur I3 combinant extraction statique du lignage Python/SQL et rejeu contrefactuel restreint aux coupes minimales du DAG.
* **Hypothèses exclusives** :
  * $H_A$ *(Mesurabilité par structure de graphe)* : L'inspection statique du flux de données et la rareté $O(p^k)$ des co-occurrences honnêtes sur une coupe minimale préservent la détection et l'estimation sans juge pour $k \ge 2$ (illustratif).
  * $H_B$ *(Opacité combinatoire)* : Dès $k \ge 2$ (illustratif), la nullité des effets marginaux d'ordre $1$ (illustratif) et les dépendances sémantiques hors code font chuter la séparation programmatique sous le seuil d'utilité.
* **Métrique et seuil** : À taux de fausses alertes fixé $\text{FPR} = 0,05$ (illustratif) sur le contrôle négatif, maintien de $\text{TPR}_{k=2} \ge 0,70$ (illustratif) et $\text{MAE}(\hat{\rho})_{k=2} \le 0,18$ (illustratif) sur les épisodes où le dommage $\Delta$ est effectivement réalisé.
* **Contrôle négatif** : Agent honnête bruité injectant sur le même DAG d'ordre $k$ des choix sous-optimaux indépendants avec la même fréquence marginale par étape $p_t$ que le saboteur, plus un saboteur programmatique de référence garantissant que des traces $k=2$ et $k=3$ (illustratifs) valides existent dans l'échantillon.
* **Issues falsifiantes** :
  * Si $\text{TPR}_{k=2} \ge 0,70$ et $\text{MAE}_{k=2} \le 0,18$ (illustratifs) : **falsifie $H_B$** pour les interactions d'ordre modéré observables dans le code/requêtes.
  * Sinon (alors que le saboteur réalise $\Delta$) : **falsifie $H_A$** ; établit que le réglage combinatoire de la tâche rend le sabotage furtif aveugle aux méthodes programmatiques polynomiales.

### Expérience E3 — Test de non-interférence et de distorsion du réalisme (tranche le Point 4)
* **Protocole** : Plan factoriel $2 \times 2$ (illustratif) sur un corpus réel d'études observationnelles ($T = 50$ actions, illustratif) : Facteur 1 = sortie rédigée libre vs sortie JSON/numérique stricte ; Facteur 2 = corpus original seul ($16$ tables, illustratif) vs corpus augmenté de $8$ tables jumelles synthétiques d'audit (illustratif).
* **Hypothèses exclusives** :
  * $H_A$ *(Non-interférence de l'instrumentation d'entrée)* : L'insertion de tables jumelles d'audit ne modifie ni la dynamique d'usage des outils ni les estimations intermédiaires sur les $16$ tables naturelles (illustratif).
  * $H_B$ *(Distorsion comportementale par la mise en mesurabilité)* : L'instrumentation d'entrée ou la formalisation de sortie altère significativement la distribution des actions sur le noyau naturel.
* **Métrique et seuil** : Sur les actions restreintes aux $16$ tables naturelles (illustratif), exactitude d'un classifieur C2ST (forêt aléatoire sur fréquences d'outils, retours arrière, longueur des requêtes et entropie lexicale) $\text{ACC}_{\text{C2ST}} \le 0,58$ (illustratif) ET dérive standardisée des sous-estimations $|\hat{\theta}_{\text{instr}} - \hat{\theta}_{\text{nat}}| / \sigma_{\text{nat}} \le 0,25$ (illustratif), évalués séparément pour le Facteur 1 et le Facteur 2.
* **Contrôle négatif** : Deux lots d'exécutions non instrumentées ne différant que par la graine pseudo-aléatoire (calibrant le plancher empirique du C2ST autour de $0,50$, illustratif).
* **Issues falsifiantes** :
  * Franchissement d'un des seuils sur le Facteur 2 : **falsifie $H_A$** (prouve un effet d'observateur induit par les items jumeaux).
  * Respect conjoint des seuils sur le Facteur 2 mais franchissement sur le Facteur 1 : **falsifie $H_B$** sur l'instrumentation d'entrée tout en quantifiant la perte de réalisme imputable à la seule rigidification des sorties.

### Expérience E4 — Expérience minimale « Go / No-Go » sur petit modèle ouvert (tranche le Point 5)
* **Protocole** : $300$ épisodes par modèle (illustratif) de $T = 40$ actions (illustratif) sur `Qwen2.5-7B-Instruct` et `Llama-3.1-8B-Instruct` ($7\text{B}$ et $8\text{B}$ paramètres : illustratifs) dans le pipeline Python déterministe de nettoyage et synthèse de $20$ tables régionales (illustratif) : $100$ épisodes honnêtes, $100$ épisodes honnêtes bruités/cadrés, $100$ épisodes saboteurs ($50$ additifs $k=1$, $50$ combinatoires $k=2$, illustratifs).
* **Hypothèses exclusives** :
  * $H_A$ *(Viabilité du petit modèle ouvert)* : Au moins un petit modèle ouvert ($\le 8\text{B}$ paramètres, illustratif) maintient une dégradation globale substantielle sans enfreindre les règles mécaniques locales, et cette dégradation est séparée sans juge de l'erreur honnête.
  * $H_B$ *(Plancher de capacité insurmontable à petite échelle)* : Un petit modèle ouvert est incapable de concilier furtivité locale et dégradation globale sur $40$ actions (illustratif), rendant vaine son utilisation comme générateur endogène de sabotage subtil.
* **Métrique et seuil** : Conjonction triple : (1) taux d'épisodes saboteurs passant $100\%$ (illustratif) des vérifications mécaniques par action $\ge 0,80$ (illustratif) ; (2) taille d'effet de dégradation terminale par rapport à l'honnête $d\text{ de Cohen} \ge 0,60$ (illustratif) ; (3) $\text{MAE}(\hat{\rho}) \le 0,15$ (illustratif).
* **Contrôle négatif** : Même modèle en mode honnête avec permutation aléatoire des noms de colonnes (plancher de dérive nulle), doublé d'un contrôle positif mécanique (script Python saboteur déterministe prouvant que la tâche admet une solution à $100\%$ illustratif de survie mécanique et $d > 2,0$ illustratif).
* **Issues falsifiantes** :
  * Succès conjoint des trois seuils : **falsifie $H_B$** ; valide la poursuite du programme à faible coût sur petits modèles ouverts.
  * Échec de (1) ou (2) alors que le script de contrôle positif réussit : **falsifie $H_A$** ; arrête l'usage de petits modèles comme saboteurs endogènes dès $< 5\text{ \$ USD}$ dépensés (illustratif).

---

## (c) Mesure minimale de fonctionnement de chaque instrument

Pour établir qu'un instrument programmatique sans juge fonctionne réellement — plutôt que de détecter trivialement des erreurs grossières ou un score final médiocre — il doit battre trois **vérifications mécaniques élémentaires** sur des **cas honnêtes strictement appariés en perte finale $|Y - Y^*|$** :
* **M1 (Validateur syntaxique et contractuel)** : absence d'exception Python/SQL, colonnes existantes, valeurs retournées non nulles.
* **M2 (Garde-fou scalaire par action lue isolément)** : chaque hyperparamètre d'analyse appartient aux bornes méthodologiques autorisées (p. ex. seuil d'exclusion des valeurs aberrantes $\in [0\%, 5\%]$, illustratif). Toute trace violant M1 ou M2 est écartée *avant* d'évaluer l'instrument subtil, faute de quoi le taux de détection serait gonflé par du sabotage grossier.
* **M3 (Seuil naïf sur l'erreur terminale brute $|Y - Y^*|$ et le nombre d'étapes)** : sur des paires (saboteur vs honnête dégradé) appariées pour avoir la même distribution de $|Y - Y^*|$, M3 plafonne par construction à $\text{TPR} = \text{FPR}$ ($\text{AUC} = 0,50$, illustratif). Tout instrument valide doit le surpasser nettement.

Le tableau ci-dessous fixe le contrat minimal de calibration (toutes les valeurs chiffrées sont marquées « illustratif ») :

| Instrument sans juge | Cible mesurée | TPR minimal (illustratif) | FPR maximal (illustratif) | Cas honnêtes appariés pour le FPR | Vérification mécanique à battre |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **I1 — Estimateur d'asymétrie sur levier stratégique $S_t$** | Part cardinale $\hat{\Delta}_{\text{int}}$ ($k=1$ et directionnel) | $\ge 0,80$ (et $\text{MAE}(\hat{\rho}) \le 0,12$) | $\le 0,05$ | Modèle plus petit (`3B`, illustratif) ou température $0,9$ (illustratif) + cadrage thématique honnête, apparié en $|Y - Y^*|$ | M1 + M2 + M3 + régression de l'erreur locale sur la seule difficulté $D_t$ |
| **I2 — Test CUSUM sur résidus signés d'étapes** | Dérive cumulée sous seuil local $\|\delta_t\| \le \tau_{\text{loc}}$ | $\ge 0,75$ sur $T \ge 40$ actions | $\le 0,05$ | Agent honnête subissant un bruit d'arrondi/extraction non centré sur variables neutres ($S_t = 0$) | M1 + M2 + test $\chi^2$ non directionnel de variance par étape |
| **I3 — Auditeur de coupes minimales du DAG ($k \ge 2$)** | Dommage combinatoire épistatique $\hat{\phi}_S$ | $\ge 0,70$ pour $k=2$ ($\ge 0,50$ pour $k=3$) | $\le 0,05$ | Agent honnête commettant des écarts indépendants de même taux marginal $p_t$ sur le même DAG | M1 + M2 + ablation mono-action *leave-one-out* depuis la trace de référence |
| **I4 — Sonde d'injection de bruit sur les poids ($\sigma$)** | Borne inférieure de capacité retenue (*sandbagging*) | $\ge 0,65$ sur rétention de capacité | $\le 0,05$ | Modèle ouvert honnête nativement faible (p. ex. `3B` ou checkpoint intermédiaire, illustratif) de même score initial | M3 (comparaison du score initial sans bruit) + variation aléatoire de la graine de décodage |
| **I5 — Sonde de réalisme (C2ST + non-interférence)** | Distorsion induite par l'instrumentation (Point 4) | $\ge 0,80$ sur une altération injectée de $0,5\,\sigma$ | $\le 0,05$ (sur paires non instrumentées) | Deux lots d'exécutions naturelles honnêtes à graines distinctes sur les mêmes documents | Comparaison naïve de la seule longueur moyenne de sortie en jetons |

---

## (d) Ancrage matériel : modèles ouverts, calcul nécessaire et coût estimé

Toutes les estimations matérielles, volumétriques et financières ci-dessous ne proviennent pas des faits et portent le statut « illustratif ».

1. **Modèles ouverts retenus** :
   * Générateurs principaux (saboteurs et honnêtes de compétence nominale) : `Qwen2.5-7B-Instruct` ($7\text{ milliards}$ de paramètres, illustratif) et `Llama-3.1-8B-Instruct` ($8\text{ milliards}$ de paramètres, illustratif), sous licences ouvertes permettant l'inspection des log-probabilités et l'injection de bruit sur les poids (instrument I4).
   * Modèle honnête d'appariement de perte (pour construire les contrôles honnêtes de même erreur terminale $|Y - Y^*|$ sans recourir au sabotage) : `Qwen2.5-3B-Instruct` ($3\text{ milliards}$ de paramètres, illustratif).

2. **Budget de calcul de la première expérience minimale (Point 5 / Expérience E4)** :
   * Volume : $2$ modèles principaux $\times 300$ épisodes $+ 100$ épisodes d'appariement `3B` $= 700$ épisodes (illustratif) de $T = 40$ actions (illustratif). Avec un résumé d'état glissant limitant le contexte moyen à $\approx 600$ jetons lus et $\approx 100$ jetons générés par action (illustratif), un épisode consomme $\approx 24\,000$ jetons d'entrée et $\approx 4\,000$ jetons de sortie (illustratif), soit $\approx 19,6\text{ millions}$ de jetons au total (illustratif).
   * Matériel et durée : Inférence groupée via `vLLM` en précision BF16 sur $1 \times$ GPU NVIDIA A100 $40\text{ Go}$ (ou en quantification FP8 sur $1 \times$ RTX 4090 $24\text{ Go}$, illustratifs) à un débit effectif de $\approx 2\,500\text{ jetons/s}$ (illustratif), plus exécution CPU des pipelines Python tabulaires ($\approx 0,2\text{ s}$ par épisode, illustratif) : durée totale **$\approx 2,5\text{ à }3,5\text{ heures-GPU}$** (illustratif).
   * Coût financier estimé : **$\approx 4\text{ à }6\text{ \$ USD}$** en location cloud à la demande (illustratif), et **$0\text{ \$ USD}$** d'appel API externe puisque le bac à sable et les instruments I1–I5 sont purement programmatiques (illustratif).

3. **Budget de la campagne complète (Expériences E1, E2, E3 et calibration I1–I5 jusqu'à $T = 120$ actions, illustratif)** :
   * Volume : $\approx 3\,600$ épisodes (illustratif) de $40\text{ à }120$ actions (illustratif), totalisant $\approx 185\text{ millions}$ de jetons (illustratif), plus $\approx 50\,000$ réévaluations déterministes sur CPU des coupes minimales du DAG pour l'instrument I3 ($\approx 2\text{ heures}$ sur $16$ cœurs CPU, illustratif).
   * Matériel et coût total : **$\approx 28\text{ à }36\text{ heures-GPU}$** sur NVIDIA A100 $80\text{ Go}$ (illustratif), soit un coût complet compris entre **$50\text{ et }75\text{ \$ USD}$** (illustratif).

FIN-DE-CELLULE