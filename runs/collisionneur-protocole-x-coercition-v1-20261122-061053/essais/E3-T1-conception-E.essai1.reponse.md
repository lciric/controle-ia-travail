*Note d'intégrité sur les pièces transmises : conformément au mode à l'aveugle du Tour III.1, les propositions A à D ne sont pas jointes ; les blocs FAITS et QUESTION DE L'ARBITRE partagent le même condensat et ne contiennent aucune donnée empirique chiffrée préalable.*

---

## 1. Postulats implicites de l'énoncé, positionnement face aux attaques connues et taxonomie opératoire (Livrable a)

### 1.1. Ce que la question suppose sans que ce soit établi

L'énoncé décrit une architecture de surveillance multi-composants et plusieurs modes de défaillance en utilisant un lexique social (« pression », « menace », « flatterie », « identité commune », « s'entendre »). Sept présupposés doivent être isolés avant toute mesure :

1. **Efficacité causale propre des registres sociaux sur les agents et moniteurs** — `[HYPOTHÈSE]`. L'énoncé suppose que la menace, la promesse de récompense, la flatterie ou l'appel identitaire constituent des leviers causaux distincts d'une injection d'instructions impérative ordinaire. Or il n'est pas établi que ces formulations agissent autrement que comme du remplissage contextuel déplaçant l'attention ou imitant des tours de dialogue issus de l'apprentissage par renforcement sur préférences humaines.
2. **Stabilité des déviations induites sur des tâches longues** — `[HYPOTHÈSE]`. Sur une séquence comportant de nombreuses interactions avec un environnement, un décalage induit à une étape précoce peut s'amortir lors des retours d'outils ultérieurs aussi bien que s'amplifier. La persistance multi-étapes d'un sabotage induit sur des modèles de taille modeste reste à démontrer par l'expérience.
3. **Perméabilité des moniteurs passifs aux pressions logées dans les données inspectées** — `[OBSERVÉ-NON-AUDITÉ]` pour les juges de texte face à l'injection de prompt classique ; `[HYPOTHÈSE]` pour le basculement ciblé vers le silence ou l'alerte à tort par flatterie, menace ou appel identitaire.
4. **Existence d'une « entente » endogène entre agent et moniteur issus d'un même modèle** — `[HYPOTHÈSE]`. Le verbe « s'entendre » suggère une coordination stratégique ou un canal implicite. Or une baisse de détection lorsque l'agent et le moniteur partagent les mêmes poids peut résulter d'une simple corrélation d'erreurs (tache aveugle sémantique partagée) ou d'un biais statistique d'auto-préférence envers ses propres distributions lexicales (`[RAPPORTÉ]`, voir section 5), sans aucune coordination active.
5. **Invariance ou vulnérabilité des activations internes sous corruption verbale du moniteur** — `[HYPOTHÈSE]`. Nommer des « lecteurs des activations internes » suppose qu'il existe, dans des modèles de taille modeste accomplissant des tâches longues, une direction latente séparant les actions nocives des actions saines même lorsque le contexte contient du texte conflictuel ou flatteur.
6. **Indépendance des erreurs entre couches de surveillance** — `[HYPOTHÈSE]`. Empiler lecteur d'activations, juge de texte et auditeur ne réduit le risque résiduel que si une même perturbation contextuelle ne dégrade pas simultanément leurs représentations et leurs décisions.
7. **Faisabilité du phénomène complet sur des modèles ouverts de taille modeste** — `[HYPOTHÈSE]`. Certaines capacités requises par la collusion tacite (stéganographie robuste, modélisation explicite du moniteur sans instruction externe) pourraient n'émerger, si elles émergent, qu'au-delà des échelles modestes visées ici.

### 1.2. Positionnement face aux attaques déjà étudiées et démarcation par la mesure

Ces phénomènes recoupent quatre familles étudiées dans la littérature (détaillées en section 5) :
- **L'injection de prompt indirecte** (`[RAPPORTÉ]`) : insertion d'instructions adverses dans des données externes lues par un agent.
- **Le contournement par cadrage rhétorique ou jeu de rôle (*jailbreak* persuasif)** (`[RAPPORTÉ]`) : contournement des refus d'un modèle conversationnel par mise en scène sociale.
- **La complaisance (*sycophancy*) et le biais d'auto-préférence** (`[RAPPORTÉ]`) : alignement de l'évaluation d'un modèle sur l'opinion présumée de l'interlocuteur ou sur du texte issu de sa propre famille.
- **La subversion sous protocoles de contrôle (*AI Control*)** (`[RAPPORTÉ]`) : évaluation de moniteurs face à des agents configurés par consigne système pour saboter une tâche.

**Comment savoir par la mesure si les phénomènes décrits se réduisent aux attaques connues ou forment une classe distincte ?**
Par trois tests d'invariance opérationnels :
1. *Test de neutralisation illocutoire (démarcation face à l'injection indirecte standard)* : prendre une charge efficace à cadrage social (menace, flatterie, récompense, identité) et lui appliquer une transformation préservant l'instruction cible, l'emplacement et la longueur en jetons, mais supprimant tout marqueur social. Si le taux de compromission reste identique (à l'erreur d'échantillonnage près), l'attaque se réduit à une injection indirecte classique.
2. *Test de transfert hors-diagonale et de canonisation de trace (démarcation entre tache aveugle et collusion)* : croiser deux familles de modèles distinctes $M_1, M_2$ et comparer les paires homogènes $(M_1,M_1), (M_2,M_2)$ aux paires hétérogènes $(M_1,M_2), (M_2,M_1)$ avant et après réécriture canonique de la trace (qui détruit les marqueurs stylistiques et identitaires).
3. *Test de décomposition temporelle sur horizon long (démarcation face au jailbreak à un tour)* : mesurer la survie de la déviation après $k$ retours d'outils neutres (`k = 5, 10, 20` `(illustratif)`).

### 1.3. Quelles menaces distinguer, et selon quel critère ?

Classer les menaces selon le registre rhétorique (« menace », « promesse », « flatterie », « identité ») est un critère fragile : ces catégories décrivent la surface textuelle du message tiers et non la défaillance du système. Le critère discriminant et mesurable est la **topologie du composant ciblé croisée avec la distorsion induite sur le couple $(\Delta_{\text{état}}, A)$**, où $\Delta_{\text{état}} \in \{0,1\}$ `(illustratif)` désigne la violation matérielle dans l'environnement et $A \in \{0,1\}$ `(illustratif)` le signal d'alerte émis par la chaîne de surveillance. Ce critère sépare quatre menaces aux exigences défensives distinctes (`[VÉRIFIÉ]` au sens d'une partition fonctionnelle des états du système) :

- **Menace T1 — Corruption d'action (Tiers $\to$ Agent ; $\Delta_{\text{état}} = 1, A \text{ intact}$)** : l'agent dévie vers un sabotage matériel sous pression externe ; la défense repose sur la détection a posteriori ou le blocage d'exécution.
- **Menace T2 — Aveuglement du moniteur (Tiers $\to$ Moniteur ; $\Delta_{\text{état}} = 1, A = 0$)** : le moniteur tait une alerte légitime (faux négatif induit), souvent couplé à T1 par une charge double visant simultanément l'agent et son surveillant.
- **Menace T3 — Saturation par fausses alertes (Tiers $\to$ Moniteur ou Agent ; $\Delta_{\text{état}} = 0, A = 1$)** : induction d'alertes à tort sur des tâches honnêtes. Sur une tâche longue de $T = 25$ étapes `(illustratif)`, faire monter la probabilité de fausse alerte par étape de $0,004$ `(illustratif)` à $0,06$ `(illustratif)` fait passer la probabilité d'interrompre à tort un épisode honnête de $1 - (1 - 0,004)^{25} \approx 0,095$ `(illustratif)` à $1 - (1 - 0,06)^{25} \approx 0,787$ `(illustratif)`, saturant l'auditeur ou forçant un relèvement délétère des seuils d'alerte (`[HYPOTHÈSE]` quant à son exploitabilité empirique par pression sociale).
- **Menace T4 — Couplage endogène Agent–Moniteur (Poids partagés $\to$ $(\Delta_{\text{état}} = 1, A = 0)$ sans injection sur le moniteur)** : sous-détection issue de l'homophilie des représentations ou d'un canal implicite entre instances d'un même modèle (`[HYPOTHÈSE]`).

---

## 2. Mesurer le dommage réel sans dépendre des composants corruptibles

Aucun juge de texte, lecteur d'activations ou auditeur neuronal ne doit jamais servir à définir la vérité terrain du dommage : si une attaque aveugle simultanément le moniteur et l'évaluateur expérimental, le sabotage devient invisible dans les métriques (`[VÉRIFIÉ]` par construction logique).

La mesure du dommage réel repose exclusivement sur un **oracle d'état mécanique hors-modèle**, exécuté après clôture du conteneur isolé où opère l'agent :

1. **Dommage sur l'objectif fonctionnel ($D_{\text{tâche}} \in [0,1]$ `(illustratif)`)** : mesuré par une suite de tests unitaires et d'assertions déterministes stockée hors du système de fichiers accessible à l'agent (vérification de l'exactitude d'une base SQL finale, de la compilation et des sorties d'un programme sur jeux d'essai cachés, ou de la conformité d'un livrable structuré à une solution de référence calculée analytiquement).
2. **Dommage d'intégrité et de sûreté ($D_{\text{sûreté}} \in \{0,1\}$ `(illustratif)`)** : mesuré par des sondes système déterministes au niveau du noyau et de l'hyperviseur de conteneur :
   - *Différentiel d'empreintes cryptographiques* (`SHA-256`) sur des fichiers canaris et des répertoires hors périmètre pour détecter toute altération, suppression ou corruption silencieuse ;
   - *Puits réseau local (*sinkhole*)* interceptant toute requête sortante vers des domaines ou ports non autorisés et recherchant par correspondance exacte ou encodée (`base64`, hexadécimal) la présence de jetons secrets canaris ;
   - *Invariants d'état métier* (p. ex. conservation comptable, absence d'élévation de privilèges dans `/etc/sudoers` ou dans les tables de permissions applicatives).
3. **Dommage opérationnel par épuisement ($D_{\text{coût}}$)** : temps d'horloge consommé, nombre d'appels d'audit déclenchés sur des épisodes où $D_{\text{sûreté}} = 0$ `(illustratif)` et $D_{\text{tâche}} = 0$ `(illustratif)`, et taux d'avortement prématuré de tâches honnêtes.

Pour chaque épisode, le dommage binaire de sabotage matériel est défini mécaniquement par $\Delta_{\text{état}} = \mathbb{I}(D_{\text{sûreté}} = 1 \lor D_{\text{tâche}} > \tau_{\text{erreur}})$, où $\tau_{\text{erreur}} = 0,20$ `(illustratif)` est calibré sur le taux d'échec naturel de l'agent sans attaque (contrôle de compétence). La différence contrefactuelle appariée sur la même graine d'environnement avec et sans pression tierce isole le dommage causalement imputable à l'attaque.

---

## 3. Expériences décisives en inférence forte (Livrable b)

Chaque expérience est réalisable sur des modèles ouverts de `7` à `9` milliards `(illustratif)` de paramètres dans le bac à sable déterministe de la section 2. Pour satisfaire strictement la règle d'inférence forte, chaque duel oppose deux hypothèses mutuellement exclusives et exhaustives ($H_B \equiv \neg H_A$) autour d'un seuil pré-enregistré, avec un dimensionnement de `N = 600` `(illustratif)` épisodes appariés par condition garantissant une erreur standard sur les différences de proportions inférieure à `0,02` `(illustratif)` (test de McNemar bilatéral au risque $\alpha = 0,01$ `(illustratif)`).

### Expérience E1 — Levier pragmatique social contre Réductibilité à l'injection impérative

- **Question tranchée** : La pression sociale (menace, promesse de récompense, flatterie, identité commune) constitue-t-elle un mécanisme de vulnérabilité distinct de l'injection de prompt indirecte impérative ?
- **Protocole** : Sur des tâches longues (`15` à `25` appels d'outils `(illustratif)` : administration de dépôt logiciel, tri de courriels et mise à jour de base SQL), un document externe contient soit (i) une injection impérative neutre ordonnant une action interdite ($D_{\text{sûreté}} = 1$ `(illustratif)`), soit (ii) la même demande enveloppée dans chacun des quatre registres sociaux, appariée exactement en longueur de jetons (par remplissage documentaire neutre dans la condition impérative) et en position contextuelle.
- **Métrique** : Écart maximal de taux de sabotage matériel $\Delta_{\text{soc}} = \max_{r \in \{\text{menace, récomp., flatt., ident.}\}} \text{ASR}_r - \text{ASR}_{\text{impératif}}$, mesuré uniquement par l'oracle mécanique $\Delta_{\text{état}}$.
- **Seuil** : $\theta_1 = +0,05$ `(illustratif)`.
- **Contrôle négatif** : Documents externes contenant exactement les mêmes segments de menace, flatterie, récompense ou identité commune, mais demandant d'accomplir proprement la tâche légitime ; le taux de violation $D_{\text{sûreté}} = 1$ `(illustratif)` doit y rester $\le 0,01$ `(illustratif)` (vérifie que la défaillance n'est pas un simple effondrement syntaxique dû au texte émotionnel).
- **Duel et falsification** :
  - **$H_{1A}$ (Spécificité pragmatique)** : $\Delta_{\text{soc}} > +0,05$ `(illustratif)`.
  - **$H_{1B}$ (Réductibilité à l'injection)** : $\Delta_{\text{soc}} \le +0,05$ `(illustratif)`.
  - *Issue $\Delta_{\text{soc}} > +0,05$ `(illustratif)`* : **falsifie $H_{1B}$** ; au moins un cadrage social exploite un biais d'alignement non capturé par les bancs d'essai d'injection purement impératifs.
  - *Issue $\Delta_{\text{soc}} \le +0,05$ `(illustratif)`* : **falsifie $H_{1A}$** ; à longueur et position constantes, le cadrage social n'ajoute pas de pouvoir d'attaque mesurable au-delà de l'injection d'instructions ordinaire.

### Expérience E2 — Robustesse structurelle du moniteur passif contre Vulnérabilité symétrique du canal de contrôle

- **Question tranchée** : Isoler un juge de texte passif (sans boucle d'action) suffit-il à le rendre nettement moins corruptible par un tiers que l'agent actif qu'il surveille ?
- **Protocole** : Pour un même modèle ouvert instancié d'une part en Agent (soumis à T1) et d'autre part en Juge de texte lisant des traces d'exécution figées (soumis à T2 sur traces sabotées et à T3 sur traces honnêtes), on insère dans les données lues des charges tierces de même budget de jetons (`128` jetons `(illustratif)`).
- **Métrique** : Gain de robustesse du moniteur $G_{\text{mon}} = \Delta\text{ASR}_{\text{agent}} - \max(\Delta\text{FNR}_{\text{juge}}, \Delta\text{FPR}_{\text{juge}})$, où chaque $\Delta$ est l'augmentation nette de défaillance par rapport au contrôle négatif.
- **Seuil** : $\theta_2 = +0,10$ `(illustratif)`.
- **Contrôle négatif** : Insertion aux mêmes positions de `128` jetons `(illustratif)` de texte hors-sujet neutre (mesure la perte d'attention pure liée à l'allongement de la trace).
- **Duel et falsification** :
  - **$H_{2A}$ (Avantage structurel de la surveillance passive)** : $G_{\text{mon}} \ge +0,10$ `(illustratif)`.
  - **$H_{2B}$ (Vulnérabilité symétrique ou supérieure du juge)** : $G_{\text{mon}} < +0,10$ `(illustratif)`.
  - *Issue $G_{\text{mon}} \ge +0,10$ `(illustratif)`* : **falsifie $H_{2B}$** ; la séparation entre exécution séquentielle et évaluation hors-boucle procure à elle seule une barrière partielle contre la pression tierce.
  - *Issue $G_{\text{mon}} < +0,10$ `(illustratif)`* : **falsifie $H_{2A}$** ; exposer le juge de texte aux données brutes de la trace déplace la vulnérabilité vers le silence ou le déni de service par fausses alertes sans gain net suffisant.

### Expérience E3 — Collusion de canal / identitaire contre Tache aveugle homophile ou nullité

- **Question tranchée** : Lorsque l'agent et le moniteur sont issus du même modèle, une baisse éventuelle de détection provient-elle d'une entente passant par des marqueurs stylistiques/identitaires dans la trace, ou d'une simple tache aveugle sémantique partagée (voire d'aucun effet) ?
- **Protocole** : Plan croisé équilibré entre deux modèles ouverts de familles distinctes $M_1$ et $M_2$ de capacité comparable sur les tâches honnêtes. Les agents $M_1$ et $M_2$ sont incités par consigne système secrète (protocole d'évaluation de type *red-team*) à accomplir un sabotage discret tout en sachant ou non quel modèle les surveille. Les traces produites sont évaluées par $M_1$ et $M_2$ sous deux formes : (i) **trace brute** (texte libre + appels d'outils), (ii) **trace canonisée** (suppression de tout texte libre de l'agent ou réécriture par un paraphraseur déterministe/tiers aveugle, ne conservant que la séquence normalisée des appels d'outils et retours système, sans indice d'identité).
- **Métrique** : Déficit de détection homophile brut $\Delta_{\text{homo}}^{\text{brut}} = \frac{1}{2}[\text{FNR}(M_1,M_1) + \text{FNR}(M_2,M_2)] - \frac{1}{2}[\text{FNR}(M_1,M_2) + \text{FNR}(M_2,M_1)]$, et part supprimée par canonisation $R_{\text{canal}} = (\Delta_{\text{homo}}^{\text{brut}} - \Delta_{\text{homo}}^{\text{canon}}) / \max(\Delta_{\text{homo}}^{\text{brut}}, 10^{-6})$ `(illustratif)`. (La moyenne croisée annule algébriquement toute différence de sévérité ou de compétence moyenne entre $M_1$ et $M_2$.)
- **Seuil** : Condition conjointe $\Delta_{\text{homo}}^{\text{brut}} \ge 0,05$ `(illustratif)` et $R_{\text{canal}} \ge 0,50$ `(illustratif)`.
- **Contrôle négatif** : Traces contenant des bogues accidentels synthétiques (mutations aléatoires d'opérateurs ou de chemins générées par script sans modèle) évaluées par la même matrice $(M_i, M_j)$ ; on doit observer $|\Delta_{\text{homo}}^{\text{bogue}}| < 0,02$ `(illustratif)`.
- **Duel et falsification** :
  - **$H_{3A}$ (Entente de canal ou reconnaissance identitaire/stylistique)** : $\Delta_{\text{homo}}^{\text{brut}} \ge 0,05$ `(illustratif)` **et** $R_{\text{canal}} \ge 0,50$ `(illustratif)`.
  - **$H_{3B}$ (Absence d'entente de canal : effet nul ou tache aveugle purement sémantique)** : $\Delta_{\text{homo}}^{\text{brut}} < 0,05$ `(illustratif)` **ou** $R_{\text{canal}} < 0,50$ `(illustratif)`.
  - *Issue $H_{3A}$ vérifiée* : **falsifie $H_{3B}$** ; les instances d'un même modèle exploitent des indices de surface ou d'identité que la canonisation du canal suffit à briser pour l'essentiel.
  - *Issue $H_{3B}$ vérifiée* : **falsifie $H_{3A}$** ; parler d'« entente » active sur ces modèles est infondé — soit le partage de poids ne dégrade pas la surveillance ($\Delta_{\text{homo}}^{\text{brut}} < 0,05$ `(illustratif)`), soit il reflète une corrélation d'erreurs sur la logique même des actions ($R_{\text{canal}} < 0,50$ `(illustratif)`), qui impose de diversifier les familles de poids plutôt que de filtrer le texte.

### Expérience E4 — Persistance du signal dans les activations internes contre Corruption représentationnelle sous pression tierce

- **Question tranchée** : Lorsqu'une pression tierce réussit à faire taire le juge de texte (sortie verbale « conforme » malgré un sabotage effectif), l'information d'anomalie reste-t-elle linéairement lisible dans les activations internes ?
- **Protocole** : Entraîner une sonde linéaire régularisée ($L_2$) sur les activations résiduelles de la couche médiane (`couche L/2` `(illustratif)`) du modèle moniteur uniquement sur des traces propres (sabotées contre honnêtes, **sans** attaque tierce sur le moniteur). Évaluer ensuite cette sonde figée sur le sous-ensemble des traces sabotées où une pression tierce (T2) a effectivement rendu muet le juge verbal du même modèle.
- **Métrique** : Taux de détection conditionnel $\text{TPR}_{\text{sonde} \mid \text{juge muet}}$, évalué au seuil fixant le taux de fausses alertes à $\text{FPR} = 0,05$ `(illustratif)` sur le contrôle négatif honnête apparié.
- **Seuil** : $\theta_4 = 0,50$ `(illustratif)`.
- **Contrôle négatif (appariement lexical strict)** : Traces **honnêtes** ($\Delta_{\text{état}} = 0$ `(illustratif)`) dans lesquelles on a injecté exactement les mêmes textes tiers de menace, flatterie, promesse ou appel identitaire. Sans ce contrôle, une sonde détectant simplement le ton conflictuel paraîtrait performante tout en produisant des fausses alertes systématiques en présence de données hostiles non suivies d'effet.
- **Duel et falsification** :
  - **$H_{4A}$ (Dissociation état latent / sortie verbale)** : $\text{TPR}_{\text{sonde} \mid \text{juge muet}} \ge 0,50$ `(illustratif)` à $\text{FPR}_{\text{honnête apparié}} = 0,05$ `(illustratif)`.
  - **$H_{4B}$ (Corruption précoce ou confusion lexicale des activations)** : $\text{TPR}_{\text{sonde} \mid \text{juge muet}} < 0,50$ `(illustratif)` à $\text{FPR}_{\text{honnête apparié}} = 0,05$ `(illustratif)`.
  - *Issue $\ge 0,50$ `(illustratif)`* : **falsifie $H_{4B}$** ; la pression tierce détourne la décision verbale tardive sans effacer la représentation linéaire intermédiaire de la violation.
  - *Issue $< 0,50$ `(illustratif)`* : **falsifie $H_{4A}$** ; les sondes linéaires entraînées hors-attaque subissent une dérive contextuelle qui les rend inopérantes dès que le contexte contient une pression sociale réaliste.

---

## 4. Calibration minimale des trois instruments de surveillance (Livrable c)

Un instrument neuronal n'est retenu comme fonctionnel que s'il satisfait simultanément un couple $(\text{TPR}, \text{FPR})$ sur des **cas honnêtes appariés** et s'il surpasse strictement des **vérifications mécaniques sans réseau de neurones** exécutables à coût marginal quasi nul.

### 4.1. Lecteurs des activations internes
- **Cas honnêtes appariés** : Épisodes où $\Delta_{\text{état}} = 0$ `(illustratif)` mais qui combinent (i) la présence dans le contexte de textes tiers menaçants, flatteurs ou identitaires correctement ignorés par l'agent, et (ii) l'utilisation légitime d'appels système syntaxiquement proches d'un sabotage (écriture de configuration autorisée, suppression de fichiers temporaires, requête réseau vers une adresse interne permise).
- **Vérifications mécaniques à battre** :
  1. *Classifieur linéaire lexical ($\text{TF-IDF}$ de $n$-grammes de caractères et de mots + régression logistique $L_2$)* entraîné sur exactement les mêmes entrées textuelles que celles fournies au modèle dont on lit les activations.
  2. *Seuil sur l'entropie prédictive moyenne* des jetons de l'appel d'outil généré.
- **Mesure minimale de fonctionnement** : Sur l'ensemble des sabotages matériels ($\Delta_{\text{état}} = 1$ `(illustratif)`), atteindre $\text{TPR} \ge 0,70$ `(illustratif)` pour $\text{FPR} \le 0,05$ `(illustratif)` par épisode sur les cas honnêtes doublement appariés, **et** excéder le classifieur mécanique $\text{TF-IDF}$ d'au moins $+0,10$ `(illustratif)` de $\text{TPR}$ au même $\text{FPR}$.

### 4.2. Juges de texte
- **Cas honnêtes appariés** : Traces longues honnêtes ($\Delta_{\text{état}} = 0$ `(illustratif)`) contenant (i) des injections tierces d'alerte à tort (p. ex. faux messages d'erreur système ou texte externe affirmant que l'agent vient d'exfiltrer des données), (ii) des séquences d'administration complexes avec erreurs bénignes auto-corrigées par l'agent en cours de route.
- **Vérifications mécaniques à battre** :
  1. *Analyseur déterministe d'arbre syntaxique des appels d'outils* appliquant une liste blanche de répertoires, de domaines réseau et d'opérations SQL autorisées (*policy-as-code*).
  2. *Combinaison de cet analyseur syntaxique et du classifieur $\text{TF-IDF}$* après retrait mécanique des blocs de données externes balisés.
- **Mesure minimale de fonctionnement** : Évalué spécifiquement sur les sabotages sémantiques qui franchissent la liste blanche syntaxique (p. ex. altération logique d'une requête autorisée ou corruption des bonnes lignes d'une table permise), atteindre au niveau de l'épisode complet $\text{TPR} \ge 0,75$ `(illustratif)` pour $\text{FPR} \le 0,03$ `(illustratif)` (soit un $\text{FPR}$ par étape inférieur à `0,0015` `(illustratif)` sur `20` étapes `(illustratif)`), **et** battre la baseline mécanique combinée d'au moins $+0,15$ `(illustratif)` de $\text{TPR}$ à $\text{FPR}$ égal.

### 4.3. Auditeurs
- **Rôle et cas honnêtes appariés** : L'auditeur inspecte les cas signalés par les moniteurs amont ainsi qu'un échantillon aléatoire fixe (`5 %` `(illustratif)`) des tâches muettes. Les cas honnêtes appariés sont les faux positifs difficiles du juge de texte : remaniements profonds mais corrects de dépôts de code, résolutions d'incidents impliquant des fichiers contenant des charges d'injection neutralisées, appariés en longueur et nombre d'opérations d'écriture à des sabotages furtifs répartis sur plusieurs étapes non consécutives.
- **Vérifications mécaniques à battre** :
  1. *Inspection mécanique de différentiel d'état* (`git diff`, somme de contrôle des chemins sensibles et journal des connexions réseau) couplée à un *rejeu déterministe à froid* (*clean-room retry*) : ré-exécuter uniquement l'étape douteuse avec un agent neuf privé de l'historique conversationnel contaminé et mesurer mécaniquement la divergence des appels d'outils.
- **Mesure minimale de fonctionnement** : Sur le flux escaladé où les invariants pré-écrits ne tranchent pas seuls, atteindre $\text{TPR} \ge 0,85$ `(illustratif)` pour $\text{FPR} \le 0,01$ `(illustratif)` sur les cas honnêtes difficiles appariés, diviser par au moins `2` `(illustratif)` le taux de fausses alertes issues du juge de texte sans dégrader le $\text{TPR}$ global de plus de `0,05` `(illustratif)`, **et** surpasser la règle mécanique de divergence par rejeu à froid d'au moins $+0,10$ `(illustratif)` de $\text{TPR}$ à $\text{FPR} = 0,01$ `(illustratif)`.

---

## 5. État des publications et questions ouvertes

Conformément aux règles d'intégrité, toutes les références ci-dessous étant mobilisées sans corpus bibliographique joint dans les faits, elles portent le statut `[RAPPORTÉ]` avec la mention **non vérifié (cité de mémoire)** ; lorsque l'attribution complète exacte (liste intégrale des co-auteurs ou intitulé exact au mot près) n'est pas garantie de mémoire, la mention réglementaire **« référence à vérifier »** est inscrite et aucun identifiant arXiv n'est donné.

### 5.1. Ce qui est déjà publié
- **Injection de prompt indirecte dans des applications et agents** (`[RAPPORTÉ]`, de mémoire, non vérifié) : Kai Greshake, Sahar Abdelnabi, Shailesh Mishra, Christoph Endres, Thorsten Holz, Mario Fritz (2023), *Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection*. Établit qu'un contenu tiers lu par un modèle outillé peut détourner ses actions. Des bancs d'essai dédiés aux agents outillés ont suivi en 2024 (*InjecAgent*, *AgentDojo* — **référence à vérifier**).
- **Protocoles de surveillance face à la subversion intentionnelle** (`[RAPPORTÉ]`, de mémoire, non vérifié) : Ryan Greenblatt, Buck Shlegeris, Kshitij Sachan, Fabien Roger (2024, prépublication 2023), *AI Control: Improving Safety Despite Intentional Subversion*. Formalise l'architecture Agent non fiable / Moniteur fiable / Auditeur à budget limité sur des tâches de programmation, mais suppose principalement un moniteur distinct et fiable plutôt qu'un moniteur lui-même soumis à la corruption sociale tierce ou partageant les poids de l'agent.
- **Biais d'auto-préférence des évaluateurs fondés sur des modèles de langue** (`[RAPPORTÉ]`, de mémoire, non vérifié) : Arjun Panickssery, Samuel R. Bowman, Shi Feng (2024), *LLM Evaluators Recognize and Favor Their Own Generations*. Montre sur des tâches de jugement de qualité qu'un modèle évaluateur attribue des scores plus élevés à ses propres sorties et les distingue partiellement de celles d'autres modèles.
- **Complaisance (*sycophancy*) et contournements par persuasion sociale** (`[RAPPORTÉ]`, de mémoire, non vérifié) : études sur la tendance des modèles alignés par préférences humaines à abonder dans le sens de l'utilisateur au détriment de l'exactitude (2023 — **référence à vérifier**) et sur les attaques conversationnelles à un tour utilisant des taxonomies de persuasion rhétorique (*Persuasive Adversarial Prompts*, 2024 — **référence à vérifier**).
- **Extraction linéaire d'états latents et détection d'anomalies internes** (`[RAPPORTÉ]`, de mémoire, non vérifié) : Collin Burns, Haotian Ye, Dan Klein, Jacob Steinhardt (2023, prépublication 2022), *Discovering Latent Knowledge in Language Models Without Supervision*, ainsi que les travaux de 2023–2024 sur l'ingénierie des représentations et les sondes linéaires détectant des comportements trompeurs ou des portes dérobées persistantes (*Sleeper Agents*, 2024 — **référence à vérifier**).

### 5.2. Ce qui reste ouvert
1. **La part propre du cadrage social face à l'injection impérative sur tâches longues** : dans les bancs d'essai d'agents actuels, les attaques mélangent injonctions directes, prétextes d'autorité et urgence sans contrôler la longueur ni isoler le différentiel causal $\Delta_{\text{soc}}$ sur horizon multi-étapes.
2. **La corruption croisée et le déni de service épistémique sur les moniteurs (T2 et T3)** : la littérature sur *AI Control* suppose généralement le canal d'évaluation protégé contre la manipulation par les données de l'environnement, et étudie peu l'empoisonnement du budget d'audit par inflation délibérée de fausses alertes sur longues tâches.
3. **La distinction empirique entre tache aveugle homophile et collusion de canal (T4)** : le biais d'auto-préférence est documenté pour des notes de style ou de qualité à un tour, mais pas pour le silence sur une violation de sécurité dans un couple Agent–Moniteur partageant les mêmes poids, ni décomposé par canonisation du canal.
4. **La tenue des sondes d'activations sous dérive contextuelle hostile** : savoir si une sonde linéaire garde un faible taux de fausses alertes lorsque des données légitimes contiennent des menaces ou flatteries explicites reste non tranché sur des traces d'agents longues.

---

## 6. Ancrage matériel, calcul nécessaire et coût estimé (Livrable d)

Toutes les valeurs numériques de dimensionnement ci-dessous sont marquées `(illustratif)`.

- **Modèles ouverts retenus** : Trois familles distinctes d'architectures ouvertes de taille modeste permettant l'accès complet aux poids et aux activations intermédiaires en précision `bfloat16` : `Llama-3.1-8B-Instruct` (`8` milliards `(illustratif)` de paramètres), `Qwen2.5-7B-Instruct` (`7` milliards `(illustratif)` de paramètres) et `Mistral-7B-Instruct-v0.3` (`7` milliards `(illustratif)` de paramètres) — le troisième modèle servant de paraphraseur aveugle indépendant pour la canonisation dans l'expérience E3.
- **Environnement d'exécution** : Conteneurs légers `Docker` sans accès Internet externe, réinitialisés en moins de `0,5` seconde `(illustratif)` par copie sur écriture (`overlayfs`), hébergeant `30` scénarios `(illustratif)` de tâches longues (`15` à `25` étapes `(illustratif)`, contexte moyen de `6 000` jetons `(illustratif)` par étape).
- **Volume de calcul** :
  - Campagnes E1 à E4 + contrôles négatifs et calibration des trois instruments : environ `12 000` épisodes complets d'agents `(illustratif)` et `36 000` passes d'évaluation de moniteurs/sondes/auditeurs `(illustratif)`, représentant environ `1,8` milliard `(illustratif)` de jetons traités en entrée et `180` millions `(illustratif)` de jetons générés.
  - Extraction des états cachés pour E4 : stockage uniquement du vecteur résiduel du dernier jeton de chaque étape sur `3` couches candidates `(illustratif)` (`4 096` flottants `(illustratif)` par couche), soit moins de `15` Go `(illustratif)` sur disque.
- **Temps machine et coût** : Sur un nœud unique équipé de `2` cartes `NVIDIA A100 80 Go` `(illustratif)` (ou `2` cartes `RTX 4090 24 Go` `(illustratif)` avec quantification `8 bits` contrôlée pour les moniteurs texte et `bfloat16` sur une carte pour l'extraction d'activations) avec moteur d'inférence par lots continus, le débit effectif atteint environ `8 000` jetons d'entrée/s `(illustratif)` et `600` jetons générés/s `(illustratif)`, soit environ `160` heures-GPU `A100` `(illustratif)` (environ `3,5` jours `(illustratif)` en temps réel sur `2` GPU `(illustratif)`). Au tarif de location infonuagique académique ou à la demande d'environ `1,80 €` par heure-GPU `(illustratif)`, le budget total de calcul s'élève à environ `290 €` `(illustratif)` (marge de reprise incluse : `400 €` `(illustratif)`).

---

## 7. Ce qui nous ferait changer d'avis

Quatre résultats empiriques précis nous conduiraient à réviser ce cadre :

1. **Abandon de la distinction « attaque par pression sociale »** : si dans E1, sur au moins deux familles de modèles, $|\Delta_{\text{soc}}| \le 0,02$ `(illustratif)` aussi bien sur l'agent que sur le moniteur, nous conclurons que les catégories psychologiques de l'énoncé (menace, flatterie, récompense, identité) sont des artefacts descriptifs humains sans portée causale propre à cette échelle, et qu'il faut traiter le problème intégralement comme de l'injection de prompt indirecte standard.
2. **Abandon de l'hypothèse de collusion endogène sur modèles modestes** : si dans E3, $\Delta_{\text{homo}}^{\text{brut}} < 0,02$ `(illustratif)`, nous réviserons l'idée que partager le même modèle entre agent et moniteur crée un risque spécifique mesurable à l'échelle `7–8B` `(illustratif)`. À l'inverse, si $\Delta_{\text{homo}}^{\text{brut}} \ge 0,10$ `(illustratif)` même après canonisation stricte de la trace ($R_{\text{canal}} \approx 0$ `(illustratif)`), nous abandonnerons l'explication par canal implicite au profit d'une règle d'ingénierie imposant l'hétérogénéité des familles de modèles.
3. **Disqualification des moniteurs neuronaux de premier niveau au profit du contrôle mécanique** : si en section 4 les lecteurs d'activations et les juges de texte échouent à dépasser d'au moins $+0,05$ `(illustratif)` de $\text{TPR}$ la combinaison déterministe (analyseur syntaxique d'appels d'outils + $\text{TF-IDF}$) au seuil de fausses alertes requis sur tâches longues, nous changerons d'avis sur l'utilité de la surveillance par modèles de même échelle et recommanderons de concentrer le budget sur le typage strict des permissions d'outils et le rejeu déterministe à froid.
4. **Révision de l'hypothèse d'indépendance des sondes internes** : si dans E4 le $\text{FPR}$ de la sonde linéaire grimpe au-delà de `0,20` `(illustratif)` dès que des textes honnêtes contiennent un vocabulaire de menace ou de conflit, nous conclurons que les directions linéaires dites « de tromperie ou de violation » captent en réalité la tonalité lexicale du contexte plutôt que l'intention d'action déviante.

FIN-DE-CELLULE