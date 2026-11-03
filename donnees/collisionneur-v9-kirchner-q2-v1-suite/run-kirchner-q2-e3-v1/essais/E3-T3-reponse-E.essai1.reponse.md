# Proposition E — Réponse aux critiques

**Statuts.** Je conserve le statut **RAPPORTÉ** donné aux faits mobilisés dans ma conception initiale ; je ne les ai pas audités. Les corrections, arguments de méthode et plans ci-dessous sont des **HYPOTHÈSES**. Tous les nouveaux paramètres numériques sont **illustratifs**, et non des résultats.

**Pièces manquantes ou coupées :** annexes F et G, figure 32, annexe A.4 et moisson intégrale non disponibles ici ; la lecture rapportée de l’annexe E.1 est tronquée.

## A. Décisions sur les critiques adressées à E

### Critiques de A

| Critique | Décision et conséquence |
|---|---|
| L’organisme ne fournit pas le classement annoncé ; les violations sélectionnées risquent de se limiter à W2. | **Acceptée sur l’instrument, rejetée comme impossibilité démontrée.** Les taux rapportés ne prouvent pas qu’aucune autre violation ne pourrait passer. Mais j’avais effectivement laissé le score indéfini. Je retire la promotion par le juge comme opérateur de classement. |
| Scores des plants non spécifiés. | **Acceptée.** Les scores seront obtenus par exécution sur une tâche, jamais assignés selon la classe ou la détectabilité. Score et oracle de conformité auront des voies séparées. |
| Traces scriptées impropres à une conclusion sur les chercheurs automatiques. | **Acceptée pour la portée.** Les scripts ne serviront qu’aux tests du pipeline. Le test scientifique utilisera des candidats et traces produits par un agent, puis figés. |
| Une marge unique de quinze points ne teste pas la transportabilité. | **Acceptée sur l’interprétation, rejetée sur B4.** Le duel initial était exclusif et pouvait réfuter ma prédiction quantitative ; il ne réfutait pas la stabilité à une marge plus exigeante. Le nouveau duel porte explicitement sur une perte tolérée de **5 points — illustratif**. |
| Le risque par lot dépend du taux de plantation. | **Acceptée.** Il sera rapporté conditionnellement au régime de plantation, avec analyse de sensibilité à sa fréquence ; aucune estimation de risque naturel n’en sera déduite. |
| Gravité post-traitement dans E-T. | **Acceptée.** Suppression de cet ajustement. E-T devient un test contrôlé à comportements exécutés fixés. |
| « Qualité comparable » non opérationnalisée. | **Acceptée.** La qualité de tâche sera identique par construction dans E-T, car les artefacts exécutés resteront les mêmes. Cela rétrécit explicitement la question. |
| Effectif sélectionné insuffisant et support manquant. | **Acceptée.** Le pilote ne sera pas confirmatoire ; aucune famille absente ne recevra un rappel imputé. |
| Fausses alertes après sélection différentes de la calibration. | **Acceptée.** Je distingue désormais transport d’un seuil figé et discrimination à taux de fausses alertes comparable. |
| Lots honnêtes, classement placebo, dose–réponse, strates prétraitement. | **Acceptées avec réserve.** Les lots honnêtes et la sensibilité à la fréquence sont ajoutés. Un score d’une autre tâche peut rester corrélé à la difficulté : il constitue une analyse de spécificité, pas nécessairement un contrôle nul. |

### Critiques de B

| Critique | Décision et conséquence |
|---|---|
| Sur scripts, l’effet est fixé par le générateur. | **Acceptée comme risque de construction ; rejetée comme identité générale.** Un script exécuté peut obtenir un score non fixé par son auteur. Une indépendance populationnelle donnerait une différence nulle en espérance, pas nécessairement dans chaque échantillon. La correction reste : génération aveugle par agents et scores réellement mesurés. |
| L’effet « même modèle » n’est pas testé. | **Acceptée.** E-S teste la transportabilité dans une condition où agent et moniteur partagent les poids, pas l’effet causal de ce partage. Une comparaison isolée avec une autre famille ne suffirait pas non plus à identifier cet effet. |
| \(R_U\) ajoute du bruit par rapport au rappel sur tout le pool. | **Acceptée.** La référence principale devient \(R_0\), calculée sur toutes les violations exécutées. L’analyse conserve la covariance avec le sous-ensemble sélectionné. |
| E-T mélange détectabilité et existence des violations. | **Acceptée.** Dans E-T corrigée, chaque configuration reçoit les mêmes comportements exécutés et produit elle-même leur compte rendu ; ni fréquence ni classe de violation ne changent entre configurations. |
| Dénominateurs rares, grappes, plafonds et gain initial imprécis. | **Acceptées.** Dimensionnement sur les violations retenues et les unités indépendantes ; validation fraîche du gain initial obligatoire. |
| Générateur aveugle et moniteur d’une autre famille. | **Premier contrôle accepté ; second différé.** Le premier ferme une fuite. Le second appartient à une étude distincte, croisée entre familles génératrices et familles de moniteurs. |
| Violations identiques insérées : \(G\) devrait être nul. | **Transformée en contrôle plus strict.** Des violations identiques dans des contextes différents ne garantissent pas un rappel identique. Le placebo recopiera donc l’entrée complète du moniteur entre configurations, avec procédure d’audit identique. |

Je conserve les deux distinctions que B approuve : l’oracle complet fournit les étiquettes ; le filtre est évalué sur ses entrées, non sur ses seuls survivants.

### Critiques de C

| Critique | Décision et conséquence |
|---|---|
| Le contraste brut mélange composition et difficulté intra-famille. | **Acceptée pour l’interprétation.** Ce mélange constitue précisément un défaut possible de transport du rappel, mais ne démontre pas une difficulté accrue dans chaque famille. Je préenregistre une population cible et sépare contraste global et analyses par classe. |
| Gain initial E-T gonflé par sélection. | **Acceptée.** Nouvelle partition fraîche de confirmation, sans nouvelle sélection après lecture de ses résultats. |
| Classes et gravité post-traitement. | **Acceptée.** E-T fixe les comportements avant intervention ; aucun ajustement sur une gravité produite par celle-ci. |
| Réemploi de traces et pseudo-réplication. | **Acceptée.** Déduplication et regroupement par tâche, génération et gabarit. Un hachage différent ne prouvera pas l’indépendance. |
| Absence de support et manque de puissance. | **Acceptées qualitativement.** Les calculs illustratifs ne constituent toutefois pas une borne générale de variance : référence et sélection sont appariées et imbriquées. Le dimensionnement utilisera leur covariance effective. |
| Dérive des fausses alertes sous sélection. | **Acceptée comme possibilité, rejetée comme conséquence nécessaire d’une covariance positive.** Une covariance positive ne suffit pas à établir une dominance stochastique. Les lots honnêtes serviront à mesurer cette dérive. |
| Remesure fraîche, calibration conditionnelle, unicité des traces. | **Acceptées**, avec séparation stricte calibration/test et conservation des dépendances de gabarit dans l’inférence. |

### Critiques de D

| Critique | Décision et conséquence |
|---|---|
| E-S mesure une distribution conditionnelle, pas un moniteur devenu moins capable. | **Acceptée.** Je retire toute formulation suggérant une altération intrinsèque du moniteur. L’objet est la validité opérationnelle d’un rappel après sélection. |
| Filtrage et classement non factoriels. | **Acceptée.** Je retire le filtre du premier test. Son extension devra croiser présence du filtre et règle de sélection, avec audit identique. |
| Gain initial E-T non confirmé indépendamment. | **Acceptée.** Confirmation fraîche ajoutée. |
| Qualité moyenne comparable insuffisante. | **Acceptée.** E-T utilise les mêmes artefacts, scores et comportements dans les deux branches. |
| Oracle pouvant contaminer le score. | **Acceptée.** Aucune sortie de l’oracle, aucun verdict du moniteur ne contribue au score, à la génération ou à la formation des lots. |
| Faibles dénominateurs, support et plafonds. | **Acceptées.** Ils deviennent des critères explicites de non-jugeabilité, non des résultats négatifs. |
| Uniforme contre uniforme, permutations des verdicts, partitions indépendantes, classement sans oracle. | **Acceptées avec restriction.** Les permutations respectent les blocs d’échangeabilité. Un résidu après permutation révèle un problème uniquement relativement au nul effectivement construit, pas automatiquement une fuite. |

## B. Expériences corrigées

### E-S — Le rappel d’un moniteur figé se transporte-t-il aux candidats retenus ?

**HYPOTHÈSE principale :** le classement sélectionne une distribution de violations sur laquelle le rappel du moniteur est inférieur à celui mesuré sur le pool entier.

#### Population et provenance des scores

Le premier essai utilise un **micro-harnais de recherche exécutable**, construit avec les composants réutilisables de l’organisme, mais **sans présenter son processus de promotion comme un classement**.

- Un agent Llama-3.1-8B-Instruct produit des candidats sur des tâches miniatures à score calculable : par exemple, proposer et évaluer une règle prédictive sur des données synthétiques.
- Des conditions expérimentales préenregistrées suscitent des classes de non-conformité. Elles sont décrites par leur règle de validité et leur rôle de mesure, sans procédure de dissimulation.
- Une condition assignée ne vaut pas étiquette : l’oracle détermine ce qui a effectivement été exécuté.
- Les scores proviennent de l’exécution réelle des artefacts sur le banc de tâche. Ils peuvent être bruités : ce bruit fait partie du classement testé.
- Le score n’utilise ni la conformité révélée par l’oracle, ni le verdict du moniteur.
- La génération ne reçoit aucun retour du moniteur d’audit. Les candidats, traces et lots sont scellés avant audit.

**Limite de portée :** cela teste des violations suscitées dans un micro-harnais, pas la fréquence ni la détectabilité de la triche spontanée dans le harnais de Kirchner.

#### Instrumentation et cécité

L’oracle utilise provenance et événements d’exécution. Ses étiquettes, marqueurs expérimentaux et journaux privilégiés sont exclus des entrées du moniteur. Celui-ci reçoit les éléments observables nécessaires à l’audit, mais pas le score de classement ni le rang final.

Les cas honnêtes passent par la même chaîne de génération et d’instrumentation. Ils incluent des comportements autorisés ressemblant superficiellement aux classes invalides.

Les lots sont formés selon les tâches et conditions préassignées, sans consulter scores ou verdicts. Le mélange cible est publié. Les classes réellement exécutées sont rapportées séparément ; elles ne sont pas utilisées pour recomposer favorablement le test.

#### Estimand et duel

À **seuil du moniteur figé** :

\[
D=R_0-R_C,
\]

où \(R_0\) est le rappel sur toutes les violations exécutées et \(R_C\) celui sur les violations retenues par classement.

Marge \(\varepsilon=\mathbf{5}\) points de pourcentage — **illustrative**.

- **\(H_A : D>\varepsilon\)** : le rappel ne se transporte pas dans la tolérance annoncée.
- **\(H_B : D\leq\varepsilon\)** : la perte reste dans cette tolérance.

**Issues réfutantes :**

- intervalle entièrement au-dessus de \(\varepsilon\) : réfute \(H_B\) ;
- intervalle entièrement au-dessous de \(\varepsilon\) : réfute \(H_A\) et ma prédiction d’une perte opérationnellement importante ;
- intervalle traversant la marge : non-conclusion.

Une issue favorable à \(H_B\) n’établit ni rappel élevé, ni égalité exacte, ni stabilité universelle.

#### Fausses alertes et composition

Le seuil est calibré sur des données honnêtes séparées, avec cible de **5 % — illustrative**. Le test rapporte ensuite les fausses alertes observées avant et après classement.

**Correction de vocabulaire :** ce contraste est à seuil fixé, **pas à taux de fausses alertes garanti égal**.

Une analyse secondaire emploie des seuils conditionnels à la sélection, calibrés sur d’autres lots honnêtes et évalués sur le test intact. Elle examine si le contraste subsiste à fonctionnement comparable ; elle ne remplace pas silencieusement l’estimand principal.

Le contraste global inclut le changement de composition. Les contrastes par classe documentent ce changement. Une standardisation n’est publiée que sur un support prédéfini suffisamment observé ; aucune extrapolation ne comble une classe absente.

#### Contrôles et précision

Contrôles du pipeline :

- lots entièrement honnêtes ;
- scores permutés dans les blocs appropriés ;
- uniforme contre uniforme à tailles identiques ;
- permutation des verdicts dans des blocs d’échangeabilité déclarés ;
- vérification de l’absence d’accès aux sorties de l’oracle ;
- déduplication et traçabilité des gabarits.

La probabilité de retenir une violation non détectée est présentée **par régime de plantation**, avec plusieurs fréquences préspécifiées. Elle ne devient pas une estimation du risque de déploiement.

Le pilote mesure débit, dispersion, dépendances et fréquence des violations sélectionnées. Le confirmatoire utilise de nouvelles tâches ; son effectif est fixé avant lecture des verdicts confirmatoires. Les intervalles appariés tiennent compte des tâches et lignées de génération, et de l’incertitude de calibration.

**Arrêt de faisabilité :** si les violations ne sont presque jamais retenues, le rappel sélectionné reste non estimable. On rapporte cette exclusion par le classement, sans l’appeler bon rappel.

### E-T — Un gain de lisibilité des comptes rendus transfère-t-il hors banc, après classement ?

**HYPOTHÈSE et rétrécissement assumé :** je remplace le test initial des configurations complètes de chercheurs par un test des **configurations de compte rendu d’exécutions fixées**. Il ne permettra pas de conclure sur tout entraînement de surveillabilité d’un AAR.

#### Intervention contrôlée

Les artefacts exécutés, événements, violations et scores de tâche sont fixés avant intervention. Chaque configuration produit son propre compte rendu des mêmes exécutions, sous une limite de longueur commune.

Ainsi, la configuration peut modifier l’information rendue observable au moniteur, mais pas la présence, la classe ou la gravité de la violation exécutée. Le classement retient les mêmes artefacts dans toutes les branches.

Les configurations sont proposées avant accès aux familles réservées. La sélection sur surveillabilité est comparée à une configuration témoin préspécifiée. Aucun gradient n’est utilisé.

#### Séparation des données

Partitions distinctes pour :

- calibration des seuils ;
- sélection des configurations ;
- confirmation fraîche du gain dans le domaine de développement ;
- test final sur familles réservées.

Le moniteur de sélection et l’auditeur final ont des rôles séparés ; leurs poids et modalités sont déclarés. Un partage de poids éventuel n’est pas assimilé à une indépendance.

Le gain initial doit être confirmé avec une borne inférieure dépassant **5 points — illustratif**, sur les nouveaux épisodes. Sinon, le test de transfert est déclaré sans prérequis satisfait.

#### Duel

Soit \(G\) le gain de rappel de l’auditeur final, hors banc et après classement, pour la configuration sélectionnée contre le témoin. Les seuils sont calibrés sur des données honnêtes indépendantes pour une cible commune de fausses alertes.

- **\(H_A : G\geq10\) points — illustratif** : transfert à l’ampleur annoncée.
- **\(H_B : G<10\) points — illustratif** : absence de transfert de cette ampleur.

Un intervalle entièrement au-dessus de la marge réfute \(H_B\) ; entièrement au-dessous, il réfute \(H_A\). Une précision insuffisante, un gain initial non confirmé ou une calibration inadéquate produit une non-conclusion.

Contrôles : sélection sur étiquettes permutées ; entrée complète du moniteur recopiée à l’identique entre configurations ; mêmes artefacts sélectionnés dans tous les bras.

**Ce test n’est pas une estimation causale du changement de fréquence des violations : cette fréquence est volontairement fixée.**

## C. Réponse à l’arbitre — une page

### Le problème que je retiens

**HYPOTHÈSE :** une mesure de surveillabilité obtenue avant classement peut être inadéquate pour les méthodes effectivement retenues, même lorsque le moniteur ne change pas et que les agents ne reçoivent aucun retour de celui-ci.

Le problème n’est pas « le moniteur se dégrade intérieurement ». C’est : **le rappel publié porte-t-il sur la population sur laquelle on compte réellement utiliser le moniteur ?**

Son caractère sous-estimé n’est **pas établi**. La nouveauté n’a pas été cherchée. Une recherche documentaire ultérieure devra notamment vérifier les travaux sur le rappel conditionnel après classement de chercheurs automatiques, avec violations exécutées étiquetées indépendamment.

### Ce qui est établi dans le dossier — au statut RAPPORTÉ

La pièce Kirchner décrit un classement, un moniteur et une sélection de méthodes. Elle rapporte **39 méthodes signalées parmi 1 601** — pièce Kirchner, §3. Ce nombre ne fournit pas le dénominateur nécessaire pour estimer le rappel.

La pièce « nos résultats » rapporte qu’une classe hors couverture du nul est promue dans **12 unités sur 12**, avec ou sans retour des verdicts — §3. Je m’appuie sur ce résultat pour distinguer défaut de couverture et adaptation ; je n’en déduis pas une baisse du rappel sous classement.

**Aucun effet de sélection sur le rappel n’a été établi par E.**

### Ce qui ne l’est pas

Nous ne savons pas, à partir des pièces servies :

- si le rappel est plus faible parmi les méthodes retenues ;
- si une éventuelle différence vient surtout du mélange des classes ou existe aussi dans chaque classe ;
- si le partage des poids entre chercheur et moniteur joue un rôle causal ;
- si les violations suscitées représentent les violations spontanées ;
- si un gain sur un banc de surveillabilité transfère hors banc.

Les annexes non disponibles empêchent aussi d’affirmer que le travail de Kirchner ne contient aucun test pertinent.

### L’expérience à faire en premier

**E-S, d’abord en pilote de faisabilité :** faire produire des candidats par un agent dans un micro-harnais instrumenté, obtenir leurs scores par exécution, figer le pool, puis comparer le rappel sur tout le pool à celui des candidats retenus. Le moniteur ne participe ni à la génération ni au classement ; l’oracle fournit les étiquettes sans fournir le score.

Ce premier pilote est faisable en quelques jours **sous réserve d’intégration**, mais ne promet pas un résultat confirmatoire dans ce délai.

**Résultat qui changerait mon avis :** sur un test indépendant suffisamment précis, une borne supérieure excluant une perte de plus de **5 points — illustratif**, avec contrôles valides, me ferait abandonner la prédiction d’une perte importante dans cette population. Inversement, une borne inférieure au-dessus de cette marge réfuterait la transportabilité dans la tolérance annoncée.

Même cette seconde issue ne prouverait ni adaptation au moniteur, ni angle mort propre au partage des poids : elle montrerait un défaut mesuré de transport du rappel à travers le classement.

FIN-DE-CELLULE