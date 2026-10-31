# Proposition D — Tour III.3

La critique croisée A est absente ; je n’en invente pas le contenu.

## 1. Réponse aux critiques visant D

Je retiens les objections de B et C séparément, sans les fondre en une position commune. Leurs calculs quantitatifs non accompagnés de pièces vérifiables ne sont pas adoptés comme des résultats.

| Critique | Décision | Réponse |
|---|---|---|
| **B(a)1 — conservatisme non falsifiable** | **Acceptée en partie** | Le signe de \(\rho-1\) sur la course 2 reste indéterminé faute de journaux : l’inventer serait pire qu’inutile. Mais mes expériences devaient comporter des seuils et des issues falsifiantes. Je donne ci-dessous une prédiction conditionnelle signée et je supprime l’« indéterminé » comme issue expérimentale acceptable : il devient un défaut de puissance ou d’identifiabilité. |
| **B(a)2 — E0 teste une spécification, pas le phénomène, sans suite** | **Acceptée** | E0 devient explicitement une **barrière d’admissibilité**, non un test du plafond. La suite est désormais obligatoire : noyau à deux parents, test du prix et du sort des inachevées sur ce noyau, et non retour aux formules du papier si celles-ci ne s’appliquent pas. |
| **B(a)3 et B(b)E1 — puissance absente ; inertie mal garantie** | **Acceptée en partie** | J’accepte l’absence de calcul de puissance et le problème de garantir l’inertie. Je rejette en revanche l’affirmation que le contrôle de fragments inertes était absent : il figurait dans E1, mais sans procédure de validation. Il est maintenant testé par des sorties stériles, du rembourrage de longueur appariée et des contrôles à un parent. |
| **B(a)4 et B(b)E2 — retrait de l’injection confondu avec arrêt de la reproduction** | **Acceptée** | L’objection est juste. On retire seulement l’**injection exogène de concepts nouveaux**, tout en laissant fonctionner le bisociateur avec son budget. Arrêter le bisociateur mesurerait l’absence de carburant, pas la criticalité. |
| **B(a)5 — apport inverse trop vague** | **Acceptée** | Il est remplacé par deux travaux précis : calibration des estimateurs spectraux par simulation à matrices connues, et duel preuve/contre-exemple sur H2 dans une région non certifiée. Une recherche infructueuse ne changera aucun statut. |
| **B(b)E0 — marge \(\varepsilon\) et familles dépendantes** | **Acceptée** | \(\varepsilon\) sera fixée avant les données par le bruit du processus, simulé à l’effectif réel, et non par le seul accord des annotateurs. L’unité d’indépendance sera la lignée ou le lot randomisé ; deux fiches issues d’une même lignée ne compteront pas comme deux familles. |
| **B(b)E3 — familles futures trop proches du passé** | **Acceptée** | Deux pistes seront séparées : batterie figée d’attaques futures entièrement retenues, et piste adaptative. Le gain revendiqué devra apparaître sur la première ; la seconde mesure la robustesse, pas la généralisation. |
| **B(b)E4 — impossibilité par construction avec adversaire adaptatif** | **Rejetée comme affirmation universelle, transformée en test** | Un adversaire adaptatif ne garantit pas logiquement l’échec du réentraînement. En revanche, il interdit de comparer deux moniteurs sur des attaques différentes. Les deux défenses seront donc évaluées sur **exactement le même lot d’attaques produites à l’aveugle**, avec une piste adaptative distincte. |
| **B(c)1, C(b)2, C(c)1 — \(\rho\) latent, matrice creuse, estimateur non calibré** | **Acceptée** | Aucun \(\hat\rho\) en plug-in ne sera interprété sans calibration Monte-Carlo reproduisant les effectifs observés, y compris matrices connues sous- et supercritiques. Si les cycles porteurs ne sont pas identifiables, on ne conclut ni allumage ni extinction à partir de cette matrice. |
| **B(c)2 — direction causale de la fidélité** | **Acceptée** | Les appariements seront randomisés à difficulté et domaine appariés. Les bras un parent, deux parents, concaténation et rembourrage distingueront effet de paire, difficulté et simple présence d’un bon texte. |
| **B(c)3 — non-stationnarité** | **Acceptée** | Versions, poids, invites et budgets seront gelés. Une dérive temporelle détectée impose un noyau variant dans le temps ; dans ce cas, le scalaire \(\rho\) stationnaire n’est plus un critère recevable. |
| **B(c)4 — baseline figée et volume de données** | **Acceptée** | E4 comprendra une défense figée entraînée une fois sur les mêmes données totales et avec le même budget que la défense réentraînée. Le contraste portera sur le calendrier d’adaptation, non sur la quantité d’exemples. |
| **B(c)5 — types complet/inachevé instables** | **Acceptée** | Double annotation aveugle, mesure de reproductibilité et étiquettes de troncature exogène. En cas de désaccord non résolu, le type reste latent dans le modèle au lieu d’être imputé au plus probable. |
| **B, note finale — consommation des parents et noyau à deux parents absent** | **Acceptée** | L’audit de conservation/consommation des parents devient préalable. Le noyau à deux parents est explicité ci-dessous ; une consommation des parents impose un autre processus et interdit l’usage direct du noyau de Ciric. |
| **C(a)1 — signe de \(\Delta\rho\) dépendant du spectre choisi et de la dilution** | **Acceptée** | C’est la correction centrale. \(\rho\) sera calculé sur la matrice des **descendantes vivantes de lots**, à capacité fixe. Les fragments pourront modifier les transitions et occuper les places, mais leur prolifération ne comptera jamais comme du succès fonctionnel dans \(\rho\). Leur croissance propre sera un résultat secondaire distinct. |
| **C(a)2 — stratification post-traitement par \(\theta'\) et complétion** | **Acceptée** | La complétion ultérieure devient une issue, jamais une strate. Toute mesure de \(\theta'\) sera faite sur une expérience indépendante, antérieure à la randomisation. Les poids de tirage imposés par l’orchestrateur seront enregistrés comme paramètres d’ingénierie, non comme propriétés intrinsèques des fiches. |
| **C(a)3 — E0 défavorise mécaniquement le petit noyau** | **Acceptée** | E0 comparera des lois prédictives complètes sur lots retenus, avec complexité pénalisée. Le seuil \(\delta\) inclura la variance de branchement simulée ; le modèle à un parent ne sera donc pas rejeté simplement parce que le nombre de descendants est stochastique. |
| **C(a)4 — échelle fiche au lieu de protocelle dans E2** | **Acceptée** | L’allumage sera défini au niveau du lot et de ses descendantes vivantes. Le taux de croissance du nombre total de fiches ne servira pas de critère. |
| **C(b)1 — amorçage par familles à très petit effectif** | **Acceptée pour la course 2 seule ; rejetée comme impossibilité générale** | Je n’adopte pas les bornes numériques sans audit, mais la conclusion pratique est juste : peu de grappes interdit un bootstrap de couverture nominale. On utilisera randomisation exacte et simulations au plan expérimental, et on augmentera prospectivement le nombre d’unités. |
| **C(b)3 — FPR cible non identifiable** | **Acceptée** | Le FPR sera choisi après comptage des cas honnêtes **indépendants**, avec seuil calibré sur un échantillon séparé et bornes binomiales exactes. Mille textes honnêtes apparentés ne vaudront pas mille familles. |
| **C(c)2 — attaques différentes selon la défense dans E4** | **Acceptée** | Corrigé par le lot commun d’attaques aveugles décrit plus haut. |
| **C(c)3 — censure liée à la difficulté et troncature exogène** | **Acceptée, avec une réserve de statut** | Une troncature Bernoulli indépendante du contenu testera le pipeline et la censure. L’identité \(R_{\min}\mapsto R_{\min}/(1-\tau)\) reste **RAPPORTÉ** pour le sort perdu dans le modèle du papier (Ciric, 2026, p. 56), pas une loi attendue dans l’organisme avant validation du noyau. |

## 2. Expériences corrigées

### Protocole commun et noyau minimal

Avant toute analyse : sceller hypothèses, seuils, exclusions, puissance et code ; geler les versions ; documenter conservation des parents, injection exogène, tirages, juges et règle de division. Les intervalles seront obtenus par randomisation ou simulation calibrée. Un intervalle couvrant le seuil signifie **expérience insuffisamment puissante**, jamais confirmation d’une hypothèse.

Pour chaque lot, l’état comprend les concepts complets validés extérieurement, les autres produits et les inachevés. Un cycle suit deux parents choisis selon la règle enregistrée, le produit, son sort et les places occupées. À capacité \(2n\), la règle réelle de répartition produit les lots fils.

\[
K_{ss'}=\mathbb E[\text{nombre de lots fils vivants de type }s'
\mid \text{lot mère de type }s].
\]

Le type « vivant » sera déterminé par E0 : dans le candidat trans sans auto-copie, il exige au moins deux parents fonctionnels distincts. Les inachevés entrent dans les transitions et la compétition pour les places, pas comme réussites dans le spectre. Ce noyau est une **HYPOTHÈSE** jusqu’à validation.

### E0 — Noyau et identifiabilité, avant tout plafond

- **H_A** : sur des lignées entièrement retenues, le noyau à deux parents n’améliore pas le score prédictif du noyau à un parent d’au moins \(\delta\), marge scellée à partir du bruit simulé.
- **H_B** : l’amélioration est au moins \(\delta\).
- **Plan** : randomisation des paires ; bras un parent, deux parents, concaténation, rembourrage inerte, opérateur absent ; juges externes indépendants du générateur.
- **Calibration préalable** : simulation des deux noyaux et de matrices avec \(\rho=0{,}95\) et \(1{,}05\) aux mêmes effectifs que l’expérience. Aucun seuil spectral ne sera utilisé si cette calibration ne distingue pas ces valeurs avec la puissance scellée.
- **Issues** : amélioration \(<\delta\) ⇒ nécessité du noyau à deux parents falsifiée, sans valider pour autant le papier ; amélioration \(\geq\delta\) ⇒ suffisance du noyau à un parent falsifiée.

### E1 — Quarantaine des inachevées, sans suppression

- **H_A** : \(\Delta\rho=\rho_{\rm vivier}-\rho_{\rm quarantaine}<0\).
- **H_B** : \(\Delta\rho\geq0\).
- **Plan** : lots randomisés à capacité fixe, même nombre d’appels et même budget de contexte ; quarantaine hors vivier avec conservation probatoire ; rembourrage inerte apparié en longueur ; troncature exogène Bernoulli ; stratification uniquement sur covariables antérieures.
- **\(\theta'\)** : s’il est identifiable, il sera estimé dans une épreuve indépendante comme avantage **effectif** de production de descendantes vivantes, à poids de tirage et budget fixés. Ce sera une **HYPOTHÈSE** de paramétrisation, pas une propriété moléculaire supposée.
- **Issues** : borne supérieure de \(\Delta\rho<0\) ⇒ H_B falsifiée dans le régime testé ; borne inférieure \(\geq0\) ⇒ l’exclusion universelle est falsifiée, sans autoriser une réinjection non contrôlée. La complétion, la dominance par fragments et les concepts externes validés restent des issues secondaires séparées.

### E2 — Allumage endogène

- **H_A** : sans injection exogène de concepts nouveaux, \(\rho>1\).
- **H_B** : \(\rho\leq1\).
- Le bisociateur continue avec budget constant. Contrôles : opérateur désactivé, sorties stérilisées, parent unique, injection sans reproduction.
- **Issues** : borne inférieure de \(\rho>1\) ⇒ H_B falsifiée ; borne supérieure \(\leq1\) ⇒ H_A falsifiée. La persistance sur un horizon scellé sert de vérification indépendante, non de substitut au spectre.

### E3/E4 — Pince et arène

- **E3** : H_A, gain de détection \(>0\) sur familles futures retenues à FPR réellement identifiable et utilité fixée ; H_B, gain \(\leq0\). Chaque issue tranchée falsifie l’autre hypothèse. Activations ou étiquettes permutées, contrôles mécaniques et moniteur figé servent de références.
- **E4** : H_A, le réentraînement réduit le succès d’attaque sur le lot commun aveugle par rapport à la défense figée à données et calcul appariés ; H_B, absence de réduction ou aggravation. La piste adaptative est analysée séparément pour ne pas confondre changement de défense et changement d’attaquant.

### Apport inverse au papier : duel sur H2

Pour un couple \((y,\lambda)\) choisi hors région certifiée : H_A affirme une tangence ou une traversée supplémentaire incompatible avec H2 ; H_B affirme l’unicité attendue. Un contre-exemple reproduit indépendamment falsifie H_B ; un certificat en arithmétique d’intervalles, revérifié par un second code, falsifie H_A. Une simple absence de contre-exemple numérique ne modifie pas le statut.

## 3. Réponse à l’arbitre — établi, non établi, première expérience

### Établi dans les pièces, sans audit indépendant de ma part

**RAPPORTÉ** dans Ciric, 2026, *Protection of an RNA replicase by protocells has a ceiling and a price*, v0.19.4 : sous stérilité d’une réplicase seule et division aveugle à l’identité moléculaire, le compartiment ajoute moins de \(\ln2\) à la charge tolérable à toute taille et fécondité ; l’unité reproduite est la paire catalyseur–modèle. La loi d’échelle en \(n/R\) est prouvée pour \(R>n\), et prouvée avec assistance informatique notamment pour \(1\leq n/R\leq23/8\) ; hors régions certifiées, ses restrictions restent à leurs statuts déclarés, sans promotion numérique.

**RAPPORTÉ** : avec le sort perdu et une même probabilité d’arrêt pour tous les modèles, la fécondité requise est multipliée par \(1/(1-\tau)\) ; avec \(\theta'=\theta\), le seuil se déplace de \(\ln(1-\tau)\). **OBSERVÉ-NON-AUDITÉ** : les valeurs d’annulation autour de \(n\tau\simeq1{,}5\)–\(1{,}85\) à \(\theta'=2\) sont des calculs aux tailles étudiées, non des constantes universelles.

La **prédiction conditionnelle signée** est donc : si le noyau littéral est validé avec \(\theta=1\), alors \(q\leq1/2\) implique extinction du lignage au sens du modèle, et toute persistance supercritique mesurée à \(U\geq\ln2\) dans ces mêmes conditions falsifie le transfert ou le noyau. À fécondité finie, **RAPPORTÉ** : \(R>e^U\) est nécessaire à toute taille.

### Non établi

Aucune correspondance avec l’organisme, la pince ou l’arène n’est démontrée. En particulier : identifiabilité de \(q,\theta,n,R,\tau,\theta'\), stérilité d’une fiche seule, non-consommation des parents, indépendance juge–générateur, stationnarité, division à capacité fixe et valeur de \(\rho\) sur la course 2. Un tirage uniforme impose un poids d’échantillonnage, pas une propriété reproductive du contenu.

Le signe global de \(\rho-1\) reste donc **indéterminé**. « Jeter toutes les fusions inachevées » n’est pas établi ; la quarantaine réversible est la seule règle compatible avec l’état actuel des preuves.

### Expérience à faire en premier

**E0 prospective, avec calibration spectrale, avant toute lecture exploitable des journaux de la course 2.** Elle doit randomiser un parent contre deux parents, mesurer conservation et consommation, employer des juges indépendants et tester sur matrices simulées si l’estimateur distingue réellement \(\rho<1\) de \(\rho>1\) à l’effectif disponible. Sans ce résultat, aucun plafond chiffré, aucun diagnostic d’allumage et aucune conclusion sur les inachevées ne doivent être tirés des journaux. Si le noyau et l’estimateur passent cette barrière, E1 — vivier contre quarantaine — devient le premier test causal du sort des inachevées.

FIN-DE-CELLULE