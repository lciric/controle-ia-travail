# Proposition B — Critique croisée de méthode (Tour III.2)

---

## Sur la proposition A

Pièce absente (statut : REFUS, confirmé par l'arbitre). Je n'en invente pas le contenu.

---

## Sur la proposition C

### (a) Défauts de méthode

**1. Substitution de noyau traitée comme un changement de paramètre.**
C identifie correctement que la bisociation tire *deux* parents symétriques et écrit une probabilité $p_{\text{bisoc}}$ quadratique en $F$ (section (d), « Le modèle exact de remplacement »). C'est la contribution la plus forte de la pièce. Mais C présente ensuite le cas $q_1 > 0$ (hybride fertile) comme « ramenant exactement à la variante auto-copiante » du papier (Appendix S12.3). Or, le papier définit l'auto-copie par $p = q(F-1+c)/[(F-1+c)+\theta(N-F)]$, qui est *linéaire* en $F$ au numérateur quand $c > 0$ (page 73, Eq. pour $p_c$, VÉRIFIÉ). Le modèle de C a un terme $2q_1 \beta FP$ au numérateur, *bilinéaire* en $F$ et $P$. Pour $F = O(1)$ et $P \approx N$, les deux donnent effectivement un taux $\propto F/N$ — l'identification est valide *asymptotiquement en $N$* — mais la transition de $F(F-1)$ à $F$ dans le régime de seuil modifie la structure du noyau limite (la fonction propre devient $F$ au lieu de $F(F-1)$, comme dans l'Appendix S1, page 28, VÉRIFIÉ), et **C ne vérifie pas que le processus limite piecewise-deterministic (Theorem 4) reste le même**. L'assertion « ramène exactement » est donc HYPOTHÈSE, non résultat.

**2. Circularité dans l'estimation de $\theta'$ et de la « retroncation ».**
C propose de mesurer $\theta'$ comme le « ratio d'attractivité d'un brouillon inachevé lors des tirages du bisociateur » (table de correspondance). Mais l'avantage de modèle $\theta$ dans le papier est défini *à l'intérieur* du mécanisme de copie (poids de tirage du modèle par le catalyseur, page 3, Eq. 1, VÉRIFIÉ). Dans l'organisme, le bisociateur est un opérateur externe qui choisit les deux parents ; le « poids de tirage » d'une fiche dépend du *protocole d'échantillonnage de l'orchestrateur*, pas d'une propriété intrinsèque de la fiche. Si l'orchestrateur implémente un tirage uniforme, $\theta = 1$ par construction, quel que soit le contenu des fiches. Si un pré-filtre favorise les fiches courtes, $\theta > 1$ est un artefact du protocole, non une propriété moléculaire. **C confond la variable latente du modèle avec un paramètre de conception du système**, ce qui rend $\theta$ et $\theta'$ *non identifiables* sans spécifier quel est le degré de liberté : la chimie (fixée) ou l'ingénierie (ajustable).

**3. Le calcul exact « pour $n = 6$ » utilise des résultats prouvés pour la partition binomiale, que C déclare violée.**
C instancie $U_c(6, \infty, 1) = 0{,}69244$ via la formule $\ln 2 - 2^{1-2n}/\ln 2$ (Table S1a, VÉRIFIÉ) et les bornes de prix de l'Appendix S3 (VÉRIFIÉ). Mais la table de correspondance de la même pièce déclare que les hypothèses H2 (division aveugle), H3 (partition binomiale) et H4 (population infinie) sont « violées » dans l'organisme. **Il y a un conflit interne : on ne peut pas utiliser les formules exactes du papier et en même temps déclarer que leurs hypothèses sont violées.** La prédiction P1 (non-allumage) est donc *conditionnelle à la tenue de ces hypothèses*, mais C la présente comme inconditionnelle (« NÉGATIF »), ce qui est une erreur de logique du transfert.

**4. Le contrôle négatif de l'Expérience 1 est faible.**
C propose d'initialiser des lots à $F_0 = 0, P_0 = 6$ pour vérifier l'absence de « génération spontanée $\chi$ ». Mais si le bisociateur est un LLM capable de produire des idées valides à partir de deux fiches fausses (par raisonnement, non par copie), ce contrôle ne détectera pas la fuite : il y aurait une probabilité non nulle de produire du vrai à partir du faux, ce qui n'est ni $\chi$ (copie spontanée d'une réplicase) ni $c$ (auto-copie), mais un mécanisme entièrement absent du papier. Le contrôle ne falsifie que le modèle de copie, pas la question posée.

**5. Confusion entre « bon » et « vrai » dans le juge.**
C utilise les statuts plantés (vrai conceptuel, faux, surface) comme vérité extérieure pour calibrer $q$. Mais la table de calibration (section c-bis) ne contrôle pas la *corrélation entre le juge et le bisociateur* : si les deux sont le même LLM, ou des LLM entraînés sur les mêmes données, le taux de « faux promus en vrai » n'est pas un taux de fausses alertes indépendant — c'est un biais partagé. Le papier suppose que la fidélité $q$ est une propriété de la chimie de copie, pas d'un classifieur appris ; cette distinction disparaît dans la transposition de C.

### (b) Conditions sous lesquelles les mesures ou critères proposés perdent leur puissance

| Mesure / critère de C | Condition (loi de probabilité, paramètre, estimateur) sous laquelle il perd sa puissance |
|:---|:---|
| $q_{vv}$ (fidélité paire vrai–vrai) | Si la loi conditionnelle $P(\text{fiche fille} = \text{vrai} \mid \text{parents} = (\text{vrai}, \text{vrai}))$ dépend fortement du *contenu* des parents (hétérogénéité intra-classe), l'estimateur moyen $\hat{q}_{vv}$ a une variance inter-famille qui domine la variance d'échantillonnage ; avec 24 fusions et $n = 6$, le nombre de paires (vrai, vrai) par lot est au plus $\binom{F}{2} \leq 15$ et $F$ varie ; l'intervalle de confiance sur $q_{vv}$ sera trop large pour trancher $q \gtrless q_c$. |
| $c_{\text{mes}} = 2q_{vf}/q_{vv}$ (poids de l'hybride fertile) | Si $q_{vf}$ et $q_{vv}$ sont estimés sur les mêmes lots, la corrélation entre numérateur et dénominateur (les paires partagent des fiches) biaise le ratio vers 1 (estimateur non indépendant). Le seuil $c_{\text{seuil}} = 0{,}05$ est trop proche de 0 pour être distingué de 0 avec 24 fusions. |
| $\theta'$ mesuré par le « ratio d'attractivité du brouillon » | Si le protocole d'échantillonnage est uniforme (chaque fiche tirée avec probabilité $1/N$), $\theta' = 1$ par construction et la mesure est triviale. Si le protocole est pondéré, $\theta'$ est un paramètre de conception, non une observable. |
| $\hat{\rho}$ (rayon spectral empirique, Expérience 2) | Avec 24 fusions par bras et $n = 6$, la matrice de descendance est estimée sur $\leq 4$ cycles de doublement. Le rayon spectral d'une matrice $M \times M$ estimée sur $k$ cycles a un biais positif de $O(M/k)$ (surestimation du spectral radius de matrices aléatoires à petite taille d'échantillon). $\hat{\rho}$ ne distingue pas $\rho = 0{,}9$ de $\rho = 1{,}1$ avec $k = 4$. |
| Prédiction P2 (arène, « levier ») | Si les erreurs de la sonde boîte blanche et du moniteur boîte noire sont positivement corrélées (même distribution d'entraînement, même architecture), la fraction de paires conservées $\bar{r}$ est surestimée : $\bar{r}_{\text{apparent}} > \bar{r}_{\text{réel}}$, et la prédiction de survie est un faux positif. Aucun test d'orthogonalité n'est spécifié avec une taille d'échantillon. |
| Certificat $M_{\text{box}} > 0$ (Expérience 3, clôture de H2) | Si les bornes exponentielles à 300 bits contiennent une erreur d'arrondi non détectée (le papier note que les certificats sont « en arithmétique rationnelle exacte sauf pour les bornes exponentielles », page 40, VÉRIFIÉ), $M_{\text{box}}$ peut être un artefact numérique. C ne propose pas de vérification par un second système de preuve formelle (Lean, Coq). |

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Contrôle de la corrélation juge–bisociateur.** C ne propose nulle part de vérifier que le juge qui attribue les statuts « vrai / faux / surface » est *statistiquement indépendant* du bisociateur qui produit les fiches. Si les deux partagent un biais commun (même LLM, mêmes données d'entraînement), toute mesure de $q$ est contaminée. **Absence fatale** pour les Expériences 1 et 2.

2. **Contrôle de la *non-consommation* des fiches parentes.** Le papier suppose qu'une réplicase qui copie une autre molécule *n'est pas détruite* (page 3, VÉRIFIÉ). C ne vérifie pas si, dans l'organisme, les deux fiches parentes sont retirées du lot après fusion (consommation) ou conservées (catalyse). Si elles sont consommées, le noyau n'est plus celui du papier (la dynamique ressemble à un processus de coalescence, pas à un branchement). **Absence fatale** pour la table de correspondance.

3. **Contrôle d'un tirage *sans* bisociateur (baseline mécanique pour le rayon spectral).** C propose comme baseline « concaténation + résumé extractif », mais *ne propose pas* de mesurer $\hat{\rho}$ sur cette baseline et de vérifier que $\hat{\rho}_{\text{baseline}} < 1$. Si la baseline a $\hat{\rho} \geq 1$ (le résumé extractif d'une paire (vrai, vrai) donne souvent du vrai), la supercriticalité n'est pas un signal de « bisociation », mais un artefact de la tâche. **Absence fatale** pour la prédiction P1 et l'Expérience 2.

4. **Contrôle de la taille de population.** C mentionne le biais négatif de la simulation à population finie (page 42, VÉRIFIÉ : $-0{,}014$ à $-0{,}048$) mais ne propose pas de le corriger ou de le borner pour $n = 6$ et 24 fusions. À cette échelle, le biais peut être du même ordre que le signal. **Absence fatale** pour la prédiction P1.

5. **Contrôle de la stationnarité du taux d'erreur $q$.** Le papier suppose $q$ constant. Si la fidélité du bisociateur dérive au cours des 24 fusions (par exemple parce que les fiches deviennent plus longues ou plus complexes), l'estimateur $\hat{q}$ est biaisé. C ne propose pas de test de tendance temporelle. **Absence fatale** pour toute instanciation numérique.

---

## Sur la proposition D

### (a) Défauts de méthode

**1. Conservatisme excessif qui rend la proposition non falsifiable.**
D qualifie systématiquement chaque correspondance d'HYPOTHÈSE et chaque prédiction d'« indéterminée ». C'est intègre, mais au point de ne rien prédire : la prédiction globale est « indéterminé » (section (a), « Prédiction globale : le signe de $\rho - 1$ pour la configuration prévue de la course 2 est indéterminé »). Sous la règle B4 (inférence forte), chaque expérience doit opposer deux hypothèses exclusives dont chacune des deux issues falsifie quelque chose. Un résultat « indéterminé » ne falsifie rien et viole B4. D aurait dû formuler une prédiction conditionnelle signée (« si $q_1 = 0$ et $\bar{r} = 1/2$, alors $\rho < 1$ ») et une prédiction alternative signée (« si $q_1 > 0$ ou $\bar{r} > 1/2$, alors $\rho > 1$ est possible »), avec des seuils chiffrés.

**2. L'expérience E0 (« le modèle réduit est-il admissible ? ») est un test de spécification du noyau, pas un test du phénomène.**
D propose de tester si un noyau à un modèle prédit les descendances aussi bien qu'un noyau à deux parents. C'est une question de modélisation, pas une question causale. Si E0 rejette le noyau à un modèle, D conclut que « $H_A$ est falsifiée ». Mais *aucun* noyau du papier n'a été conçu pour la bisociation ; le rejet de $H_A$ falsifie seulement l'hypothèse que le papier s'applique littéralement, ce que tout le monde sait déjà. La question intéressante est : *quel* noyau à deux parents prédit les descendances, et *ce noyau* a-t-il un plafond et un prix ? D ne propose pas cette suite.

**3. La métrique de E1 ($\Delta\rho$) est identique à celle de C (Expérience 2), sans les contrôles négatifs que C inclut.**
D propose de comparer $\rho_{\text{vivier}}$ et $\rho_{\text{quarantaine}}$ mais ne spécifie ni la taille d'échantillon, ni le nombre de répétitions, ni la puissance statistique. D ne propose pas non plus le contrôle de fragments « synthétiquement inertes » de C. D dit « fragments synthétiquement inertes » dans la table des contrôles négatifs de E1, mais ne spécifie pas comment garantir l'inertie (si un fragment est un texte, un LLM peut en tirer quelque chose).

**4. L'expérience E2 (allumage vs production alimentée) confond deux effets.**
D propose de retirer toute injection de nouvelles fiches et de mesurer si $\rho > 1$. Mais dans le papier, le seuil $\rho = 1$ est celui d'un processus de branchement *avec* injection de copies (la copie est elle-même une injection, au taux $RF$). Retirer l'injection revient à mettre $R = 0$, auquel cas $\rho = 0$ trivialement (toutes les molécules décroissent au taux 1, page 16, VÉRIFIÉ). Le test de D ne distingue donc pas « le système est sous-critique » de « le système n'a pas de carburant ». Pour tester $\rho > 1$, il faut maintenir l'injection (le bisociateur tourne) et mesurer si les lignées *croissent net* après soustraction de l'injection.

**5. La section « Apport inverse au papier » est trop vague pour être falsifiable.**
D dit que le programme apporte « une discipline de test : retenir des familles entières, validation chronologique, contrôles mécaniques ». Ce sont des bonnes pratiques, pas un apport spécifique au papier. D ne dit pas quelles conjectures du papier la discipline du programme pourrait falsifier ou confirmer, au-delà de H2 (mentionnée en une ligne).

### (b) Conditions sous lesquelles les mesures ou critères proposés perdent leur puissance

| Mesure / critère de D | Condition sous laquelle il perd sa puissance |
|:---|:---|
| E0 : erreur sur la matrice de descendance $< \varepsilon$ | Si $\varepsilon$ est fixé *après* inspection des données (le texte dit « scellé » mais ne donne pas la valeur), la puissance est nulle. Si $\varepsilon$ est fixé trop haut (par exemple $\varepsilon = 0{,}5$), tout noyau passe. Si les « familles de concepts » ne sont pas indépendantes (un concept engendre un autre par copie), l'amorçage par famille est biaisé. |
| E1 : $\Delta\rho = \rho_{\text{vivier}} - \rho_{\text{quarantaine}}$ | Si la variance de $\hat{\rho}$ est du même ordre que $|\Delta\rho|$ (ce qui est probable avec 24 fusions), le duel est indéterminé. D ne donne pas de calcul de puissance. |
| E2 : $\rho > 1$ après retrait de l'injection | Si « injection » inclut le fonctionnement du bisociateur (qui *est* l'opérateur de reproduction), retirer l'injection annule la reproduction et $\rho = 0$ par construction (voir défaut 4 ci-dessus). |
| E3 : $\Delta\text{TPR}$ de la pince | Si les familles d'attaques futures sont tirées de la même distribution que les passées (pas de dérive adversariale), le gain de la pince est surestimé. D ne spécifie pas si le générateur d'attaques est fixé ou adaptatif. |
| E4 : réduction du taux de succès par réentraînement | Si le générateur d'attaques est adaptatif (comme dans P-041, RAPPORTÉ), le réentraînement sur le passé *ne peut pas* réduire le taux de succès sur le futur, par construction de l'adversaire. Le test ne falsifie $H_A$ que si l'adversaire est fixé, ce qui n'est pas le cas de l'arène. |

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Contrôle de l'identifiabilité de $\rho$.** D utilise $\rho$ comme métrique centrale (E1, E2) mais ne propose pas de vérifier que $\rho$ est *identifiable* à partir des données observées. Dans un processus de branchement multitype avec types non observés (les fiches « surface » sont-elles des parasites ou des réplicases ?), le rayon spectral du noyau observable peut différer de celui du noyau latent. **Absence fatale** pour E1 et E2.

2. **Contrôle de la *direction causale* de la fidélité.** D ne propose pas de randomiser les appariements pour vérifier que c'est la *paire* de parents qui détermine la qualité de la fille, et non un facteur confondant (par exemple, la difficulté du domaine). Sans ce contrôle, $q$ mesuré est un mélange de fidélité de copie et de difficulté de la tâche. **Absence fatale** pour E0.

3. **Contrôle de la *stationnarité* du processus.** D ne mentionne pas que le bisociateur (un LLM) peut être mis à jour entre les tours, ou que la distribution des fiches change qualitativement au cours des 24 fusions (les premières fiches sont « fraîches », les dernières sont des dérivées de dérivées). Si le processus n'est pas stationnaire, la matrice de descendance n'est pas constante et $\rho$ n'a pas de sens. **Absence fatale** pour E2.

4. **Contrôle de la baseline « moniteur figé » dans E4.** D propose cette baseline mais ne spécifie pas si le moniteur figé a été entraîné sur les mêmes données que le moniteur réentraîné. Si oui, la comparaison mesure l'effet du *volume* de données, pas du réentraînement. **Absence fatale** pour E4.

5. **Contrôle de la séparabilité des types.** D suppose que les fiches sont classables en « complet / inachevé » (E2), mais ne propose pas de vérifier que cette classification est *stable* : une fiche jugée « inachevée » à un tour peut être jugée « complète » à un autre si le juge change. Sans test de reproductibilité inter-juges, les types sont bruités et la matrice de descendance est mal spécifiée. **Absence fatale** pour E1.

---

*Note sur les propositions dans leur ensemble.* C prend des risques prédictifs (P1, P2) et offre des calculs instanciés, au prix de conflits internes entre hypothèses déclarées violées et formules exactes utilisées. D est méthodologiquement plus prudent mais au point de ne rien falsifier. Aucune des deux ne propose le contrôle le plus élémentaire : vérifier que les fiches parentes *ne sont pas consommées* par la fusion (une propriété qui sépare le branchement de la coalescence et qui change entièrement le noyau). Aucune des deux ne propose non plus de modèle formel de la bisociation à deux parents comme processus de branchement multitype avec un noyau explicite, au-delà de l'esquisse quadratique de C, dont l'identification avec le papier reste non prouvée.

FIN-DE-CELLULE