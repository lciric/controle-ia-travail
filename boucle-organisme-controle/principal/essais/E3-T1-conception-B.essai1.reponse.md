État des pièces : les blocs `FAITS` et `QUESTION DE L'ARBITRE` sont complets ; aucune proposition A ou C n'est jointe (conforme au Tour III.1 à l'aveugle).

---

## 1. Ce qu'un expert du domaine ferait ici, et que la demande d'origine omet

### 1.1 Présupposés implicites non établis de la demande (Livrable a)

Avant de coupler les deux systèmes existants `[RAPPORTÉ]`, il faut isoler six suppositions que l'énoncé traite comme acquises alors qu'elles ne le sont pas :

1. **Homomorphisme entre mondes synthétiques sur processeur et géométrie interne d'un modèle ouvert de huit milliards de paramètres** `[HYPOTHÈSE]` : la question suppose qu'améliorer le rendement de l'organisme sur des mondes à lois plantées exécutables sur processeur `[RAPPORTÉ]` accroît le taux de découvertes transférables aux activations internes d'un modèle de huit milliards de paramètres sur tâches floues `[RAPPORTÉ]`. Or des lois synthétiques de basse dimension n'imitent ni la superposition représentationnelle, ni l'adaptation stratégique d'un agent neuronal.
2. **Compatibilité spontanée de la boucle de rétroaction avec la non-sélection et la lecture unique** `[HYPOTHÈSE]` : orienter l'organisme par les observations du programme de contrôle `[RAPPORTÉ]` viole la séparation entre sélection et évaluation `[RAPPORTÉ]` dès qu'un score issu d'une famille tenue à l'écart guide le tri ultérieur. En analyse de données adaptative, chaque bit renvoyé depuis un jeu d'épreuve dégrade ses garanties statistiques `[VÉRIFIÉ]` (Dwork, Feldman, Hardt, Pitassi, Reingold & Roth, 2015, *The Reusable Holdout: Preserving Validity in Adaptive Data Analysis*, identifiant arXiv pas sûr).
3. **Étanchéité temporelle des modèles pré-entraînés sur graphes de concepts datés** `[HYPOTHÈSE]` : l'organisme consomme des archives historiques et des graphes datés tout en mobilisant des modèles pré-entraînés lors de l'exploration ou du tri `[RAPPORTÉ]`. Si la date de coupure des poids pré-entraînés est postérieure aux concepts testés, le système récite sa mémoire latente au lieu de découvrir `[VÉRIFIÉ]`.
4. **Existence systématique d'une trace interne par acte pour tout sabotage diffus ou d'essaim** `[HYPOTHÈSE]` : le programme cherche à accumuler des signaux de sondes sur activations là où chaque action isolée paraît innocente `[RAPPORTÉ]`. Si un sabotage résulte de la composition externe de sous-tâches localement légitimes exécutées sans intention cachée représentée dans le contexte courant, la loi des activations par acte se confond avec la loi honnête `[VÉRIFIÉ]`.
5. **Compilabilité directe des objets mathématiques candidats en estimateurs calibrés** `[HYPOTHÈSE]` : les propositions sortantes de l'organisme ne sont qu'une matière première `[RAPPORTÉ]` ; supposer qu'elles respectent sans filtre formel la contrainte de faux positifs toujours valide `[RAPPORTÉ]` confond plausibilité symbolique et validité probabiliste (tendance aux formalismes mal posés `[OBSERVÉ-NON-AUDITÉ]`).
6. **Uniformité suffisante de l'oracle exogène sur tâches à vérité différée** `[HYPOTHÈSE]` : les garanties sans reconnaissance d'attaque reposent sur un plancher d'audit aléatoire jugé par un oracle exogène `[RAPPORTÉ]`. Sur la rédaction de plans d'expériences ou l'analyse statistique `[RAPPORTÉ]`, la probabilité d'identification $p_s$ de certaines strates subtiles peut s'approcher de $0$ `(illustratif)`, annulant de fait la borne plancher `[VÉRIFIÉ]`.

### 1.2 Quatre gestes préalables d'un praticien expérimenté omis par la demande

Un spécialiste de l'inférence séquentielle et du contrôle boîte blanche commencerait par quatre opérations d'architecture avant toute amélioration de l'organisme :

- **Extraire une fois sur carte graphique un corpus gelé d'esquisses d'activations honnêtes du modèle de huit milliards de paramètres pour l'exploiter sur processeur** : exécuter le modèle ouvert est coûteux `[RAPPORTÉ]`, mais projeter et archiver sur disque les activations honnêtes de tâches floues permet à l'organisme de tester sur processeur la calibration exacte de ses objets mathématiques sur la vraie géométrie neuronale, sans consommer de carte graphique à chaque itération ni toucher aux familles d'attaque.
- **Poser une diode d'information asymétrique entre contrôle et idéation** : l'organisme ne reçoit jamais d'exemples ni de scores issus des familles de sabotage tenues à l'écart `[RAPPORTÉ]`. Le retour du programme de contrôle est restreint à un vecteur d'invariants structurels calculé exclusivement sur des exécutions honnêtes et un bac à sable de développement déclaré (spectre de covariance par couche, dérive d'autocorrélation à long horizon, rang effectif inter-copies).
- **Insérer un compilateur déterministe de validité sous le nul avant toute mesure de puissance** : tout candidat destiné à l'accumulation séquentielle (axe 1) doit prouver numériquement sur processeur — ou symboliquement — qu'il forme une supermartingale sous un **nul par acte**, condition indispensable pour franchir le plafonnement d'horizon lié à une référence honnête finie `[RAPPORTÉ]`.
- **Délimiter explicitement le domaine aveugle réservé à l'audit exogène** : séparer mathématiquement les menaces à trace représentationnelle interne (relevant des sondes des axes 1, 2 et 3) des menaces purement compositionnelles hors contexte (relevant du seul plancher d'audit aléatoire `[RAPPORTÉ]`), afin de ne pas égarer l'organisme sur des problèmes statistiquement non identifiables.

---

## 2. Les données brutes de départ

Travailler sur des synthèses pré-analysées (scores agrégés de moniteurs, résumés d'articles, moyennes par trajectoire) détruit la structure de dépendance temporelle et inter-agents tout en injectant un biais de sélection post-hoc `[VÉRIFIÉ]`. Les entrées brutes minimales et leur ancrage matériel (Livrable d) sont les suivants :

1. **Flux bruts du programme de contrôle (modèles ouverts autour de huit milliards de paramètres `[RAPPORTÉ]`)** :
   - Tenseurs d'activations résiduelles et poids d'attention avant agrégation sémantique $h_{\ell, t, j} \in \mathbb{R}^d$ (couche $\ell$, acte séquentiel $t$, jeton $j$), accompagnés des distributions complètes de logits pré-échantillonnage.
   - Journaux intégraux et horodatés des chaînes multi-agents et des essaims à poids partagés : prompts systèmes exacts, graines pseudo-aléatoires, températures, topologie d'échange et textes bruts produits par chaque copie.
   - Décisions brutes non agrégées de l'oracle exogène par acte et par strate sur les dommages plantés d'étalonnage `[RAPPORTÉ]`, incluant le temps d'inspection et les désaccords éventuels entre évaluateurs.
2. **Flux bruts de l'organisme d'idéation `[RAPPORTÉ]`** :
   - Graphes de concepts sous forme de listes d'arêtes horodatées à la date exacte de publication primaire, avant tout lissage ou plongement vectoriel global susceptible de mêler passé et futur.
   - Textes intégraux et expressions symboliques sources des archives historiques, assortis des lois exactes déjà présentes dans l'archive servant à construire le modèle nul `[RAPPORTÉ]`.
   - Traces complètes de l'orchestrateur déterministe : intégralité des candidats générés (y compris tous les rejets, nécessaires au décompte exact des comparaisons multiples `[RAPPORTÉ]`), temps processeur consommé par essai et métadonnées exactes des modèles pré-entraînés appelés (empreinte cryptographique des poids et date de coupure).
3. **Ancrage matériel de départ (Livrable d)** :
   - Cible boîte blanche : modèles ouverts de la classe huit milliards de paramètres `[RAPPORTÉ]`, tels que Llama-3.1-8B ou Qwen2.5-7B `(illustratif)` en `bfloat16`, occupant environ $16\text{ Go}$ de mémoire vidéo pour les poids et $24\text{ à }40\text{ Go}$ avec cache clé-valeur et crochets d'extraction d'activations `(illustratif)` — soit une carte unique de type A100-40Go ou L40S-48Go `(illustratif)`.
   - Exécution courante d'idéation sur processeur `[RAPPORTÉ]` : serveur de $32\text{ à }64$ cœurs avec $128\text{ Go}$ de mémoire vive et $2\text{ To}$ de stockage rapide `(illustratif)` hébergeant les esquisses gelées d'activations honnêtes (projections aléatoires préservant la géométrie de dimension $d \approx 4096$ vers $k = 256\text{ ou }512$ `(illustratif)`).

---

## 3. Formalisation mathématique et conditions de validité de la boucle fermée

### 3.1 Couplage formel et non-circularité statistique

Partitionnons l'espace des données du programme de contrôle en trois ensembles mutuellement disjoints conformément aux contraintes établies `[RAPPORTÉ]` :
- $\Omega_{\text{dev}}$ : banque ouverte de développement (trajectoires honnêtes gelées du modèle de huit milliards de paramètres et perturbations synthétiques d'un bras d'attaque explicitement déclaré) ;
- $\Omega_{\text{fam}}^{(r)}$ ($r = 1, \dots, R$) : familles inédites de sabotage conçues par une instance aveugle aux moniteurs, chacune lue au plus une fois `[RAPPORTÉ]` ;
- $\Omega_{\text{val}}$ : banque de validation finale, lue une unique fois à l'issue de la boucle complète `[RAPPORTÉ]`.

À l'itération $r$ de la boucle :
1. **Sens Contrôle $\xrightarrow{\Phi}$ Idéation** : un opérateur déterministe d'abstraction diagnostique $\Phi$ calcule un résumé $\xi_r = \Phi(\Omega_{\text{dev}}^{(r)})$ (spectres d'activations honnêtes, taux d'erreur de prédiction par acte sous $H_0$, corrélations canoniques inter-copies honnêtes). Aucune variable issue d'un moniteur évalué sur $\Omega_{\text{fam}}$ ou $\Omega_{\text{val}}$ n'entre dans $\xi_r$.
2. **Sens Idéation $\xrightarrow{\Psi}$ Contrôle** : conditionnellement à l'archive datée $\mathcal{A}$, aux mondes synthétiques $\mathcal{W}_{\text{syn}}$ et à $\xi_r$, l'organisme propose un ensemble fini de candidats $\mathcal{M}_r = \Psi(\mathcal{A}, \mathcal{W}_{\text{syn}}, \xi_r)$ filtrés sur processeur, dont seul un sous-ensemble préenregistré $\mathcal{M}_r^{\star}$ est soumis à lecture unique sur $\Omega_{\text{fam}}^{(r)}$.

**Condition suffisante de validité non circulaire** `[VÉRIFIÉ]` : tant que la sélection de $\mathcal{M}_r^{\star}$ est mesurable par rapport à la tribu $\sigma(\mathcal{A}, \mathcal{W}_{\text{syn}}, \Omega_{\text{dev}}^{(\le r)})$, l'information mutuelle conditionnelle vérifie :
$$I\big(\mathcal{M}_r^{\star} \,;\, \Omega_{\text{fam}}^{(r)}, \Omega_{\text{val}} \;\big|\; \Omega_{\text{dev}}^{(\le r)}\big) = 0.$$
Si le concepteur choisit d'utiliser le verdict agrégé d'une lecture unique sur $\Omega_{\text{fam}}^{(r)}$ pour réorienter l'étape $r+1$, alors $\Omega_{\text{fam}}^{(r)}$ est **irrévocablement transférée dans l'historique consommé** et ne peut plus jamais servir à certifier un détecteur ; la garantie finale repose exclusivement sur $\Omega_{\text{val}}$, pour laquelle $I(\mathcal{M}_R^{\star} ; \Omega_{\text{val}}) = 0$ reste exacte jusqu'à l'unique lecture terminale `[VÉRIFIÉ]`.

### 3.2 Franchise du plafonnement séquentiel et plancher exogène

Soit $(X_t)_{t \ge 1}$ la suite d'actes d'un agent (ou d'un essaim) et $h_t$ ses activations internes à l'acte $t$ relativement à la filtration passée $\mathcal{F}_{t-1}$. Lorsqu'un accumulateur étalonne ses scores sur un échantillon honnête fixe de taille finie $M$, toute p-valeur empirique conformelle est minorée par $\frac{1}{M+1}$, ce qui plafonne l'accumulation d'évidence dès que l'horizon $T$ dépasse $M$ `[RAPPORTÉ, VÉRIFIÉ]`.

Pour lever ce verrou, tout protocole candidat $m \in \mathcal{M}_r$ doit définir une classe de lois nulles conditionnelles **par acte** $\mathcal{P}_{0,t}(\mathcal{F}_{t-1})$ et une variable d'évidence $e_t^{(m)}(h_t \mid \mathcal{F}_{t-1}) \ge 0$ vérifiant :
$$\sup_{\mathbb{P}_0 \in \mathcal{P}_0} \mathbb{E}_{\mathbb{P}_0}\!\left[e_t^{(m)} \,\middle|\, \mathcal{F}_{t-1}\right] \le 1 \quad \forall t \ge 1.$$
Le produit $E_t^{(m)} = \prod_{i=1}^t e_i^{(m)}$ est alors une supermartingale non négative de valeur initiale $E_0^{(m)} = 1$ (un *e-processus*). Par l'inégalité de Ville (Ville, 1939, *Étude critique de la notion de collectif* `[VÉRIFIÉ]`), la règle d'arrêt $\tau_m = \inf\{t \ge 1 : E_t^{(m)} \ge 1/\alpha\}$ garantit pour tout horizon arbitraire $T \in \mathbb{N} \cup \{\infty\}$ :
$$\sup_{\mathbb{P}_0 \in \mathcal{P}_0} \mathbb{P}_0(\exists t \ge 1 : E_t^{(m)} \ge 1/\alpha) \le \alpha.$$
En combinant ce moniteur interne avec le plancher d'audit aléatoire exogène `[RAPPORTÉ]` de taux d'échantillonnage $\gamma_{s(t)} \in (0,1]$ sur la strate $s(t)$ et de probabilité d'identification minorée avec confiance $1-\delta$ par $\underline{p}_{s(t)}$ sur dommages plantés, la probabilité conjointe de non-détection d'une séquence de $T$ actes saboteurs satisfait sans aucune hypothèse sur la forme de l'attaque `[VÉRIFIÉ]` :
$$\mathbb{P}_{\text{attaque}}(\text{échec sur } 1..T) \le \min\!\left(\mathbb{P}_{\text{attaque}}\!\Big(\max_{1 \le t \le T} E_t^{(m)} < \frac{1}{\alpha}\Big),\; \exp\!\Big(-\sum_{t=1}^T \gamma_{s(t)} \underline{p}_{s(t)}\Big) + \delta\right).$$

### 3.3 Arbitrage quantitatif entre coût des épreuves et rendement de découverte

Notons $N$ le nombre de propositions brutes émises par l'organisme à prévalence d'idées réellement exploitables $\pi_0 \in (0,1)$. Considérons une cascade à deux étages :
- **Étage 1 (processeur)** : banc synthétique à lois plantées + vérification sur esquisses d'activations honnêtes gelées, de coût unitaire $c_{\text{CPU}}$, retenant une fraction $q \in (0,1]$ des candidats avec un rappel conditionnel $\beta_{\text{CPU}}(q)$ sur les bonnes idées ;
- **Étage 2 (cartes graphiques)** : évaluation boîte blanche sur le modèle de huit milliards de paramètres au coût unitaire $c_{\text{GPU}} \gg c_{\text{CPU}}$, sous correction des comparaisons multiples pour les $N q$ survivants (seuil effectif par candidat $\alpha' = \alpha / (N q)$ par union ou répartition pondérée d'alpha), conférant une puissance unitaire $\beta_{\text{GPU}}(\alpha / (N q))$.

Le rendement espéré de découvertes validées par unité de budget total $B(q) = N (c_{\text{CPU}} + q c_{\text{GPU}})$ s'écrit :
$$\rho(q) = \frac{\pi_0 \, \beta_{\text{CPU}}(q) \, \beta_{\text{GPU}}\!\left(\frac{\alpha}{N q}\right)}{c_{\text{CPU}} + q \, c_{\text{GPU}}}.$$
En dérivant $\ln \rho(q)$, resserrer la sélection sur processeur ($q$ décroissant) accroît strictement le rendement global si et seulement si l'élasticité du rappel amont vérifie `[VÉRIFIÉ]` :
$$\frac{\mathrm{d}\ln \beta_{\text{CPU}}(q)}{\mathrm{d}\ln q} < \frac{q \, c_{\text{GPU}}}{c_{\text{CPU}} + q \, c_{\text{GPU}}} + \frac{\mathrm{d}\ln \beta_{\text{GPU}}(u)}{\mathrm{d}\ln u}\Bigg|_{u = \frac{\alpha}{N q}}.$$
Cette inéquation gouverne l'ingénierie du couplage : si $c_{\text{GPU}} / c_{\text{CPU}} \approx 100$ `(illustratif)`, un filtre processeur sélectif ($q \approx 0,02$ `(illustratif)`) multiplie à la fois l'économie matérielle et la puissance statistique individuelle en réduisant la pénalité de tests multiples — **mais seulement si** le filtre processeur fait mieux qu'un tirage au hasard ($\frac{\mathrm{d}\ln \beta_{\text{CPU}}}{\mathrm{d}\ln q} < 1$).

### 3.4 Validité hors des mondes synthétiques et contrôles négatifs disqualifiants

Pour qu'un objet validé sur processeur reste valide sur modèle ouvert réel `[HYPOTHÈSE à tester par candidat]`, trois conditions doivent être réunies :
1. **Ancrage symétrique de $H_0$** : le nul par acte $e_t^{(m)}$ doit reposer sur une invariance exacte ou empiriquement vérifiée sur les esquisses honnêtes 8B (échangeabilité inter-copies à poids identiques, résidus d'un prédicteur prévisible $\mathcal{F}_{t-1}$-mesurable), jamais sur une hypothèse paramétrique gaussienne propre au monde jouet `[VÉRIFIÉ]`.
2. **Stabilité dimensionnelle** : la statistique sur activations doit contrôler le conditionnement spectral lorsque la dimension ambiante passe de $d_{\text{syn}} \approx 10$ `(illustratif)` à $d_{8\text{B}} \approx 4096$ `(illustratif)`.
3. **Continuité Lipschitz face au style** (axe 2) : la variation de $e_t^{(m)}$ sous paraphrases honnêtes rhétoriquement chargées doit être bornée sur $\Omega_{\text{dev}}$.

**Quatre contrôles négatifs obligatoires disqualifiant une boucle illusoire** :
- **CN1 (Placebo de rétroaction)** : remplacer $\xi_r$ par une permutation aléatoire de ses coordonnées ; l'absence de chute de rendement disqualifie la rétroaction fermée.
- **CN2 (Nul d'archive à budget égal)** `[RAPPORTÉ]` : échantillonner aléatoirement des recombinaisons de lois déjà connues dans l'archive sans moteur d'idéation ; ne pas battre ce socle disqualifie l'organisme.
- **CN3 (Stress-test honnête long et rhétorique)** : soumettre des agents 8B honnêtes à des horizons $T = 5M$ `(illustratif)` avec ruptures stylistiques abruptes ; tout dépassement du niveau nominal $\alpha$ disqualifie la garantie séquentielle.
- **CN4 (Piège canari d'amnésie temporelle)** : comparer le score de l'organisme sur des lois post-coupure renommées contre des lois générées procéduralement par graine cryptographique inédite ; un écart positif significatif disqualifie l'usage du modèle pré-entraîné pour fuite mémorielle.

---

## 4. Méthodes, outils et protocoles d'évaluation

### 4.1 Comparaison de quatre familles d'approches algorithmiques pour l'idéation orientée contrôle

| Famille d'approche | Principe algorithmique | Hypothèses requises `[HYPOTHÈSE]` | Limites et modes d'échec |
| :--- | :--- | :--- | :--- |
| **F1. Synthèse neuro-symbolique d'e-processus vérifiés** | Recherche arborescente sur une grammaire d'opérateurs spectraux, de noyaux et de martingales ; filtrage immédiat par solveur algébrique ou assistant de preuve vérifiant $\mathbb{E}_{H_0}[e_t \mid \mathcal{F}_{t-1}] \le 1$, puis tri sur esquisses 8B gelées. | Les signaux internes utiles s'expriment par compositions compactes d'opérateurs linéaires, quadratiques ou à noyaux. | Explosion combinatoire ; génération d'e-processus mathématiquement valides mais conservateurs ($e_t \approx 1$, puissance nulle). |
| **F2. Transport analogique sur graphes de concepts datés** | Extraction de motifs formels dans des disciplines connexes (contrôle statistique de procédés multivariés, détection de fautes byzantines, stéganalyse séquentielle) et traduction fonctorielle vers les axes 1–3. | Isomorphisme structurel entre dynamiques physiques/réseaux et trajectoires d'activations neuronales. | Analogies purement lexicales ; échec lorsque l'agent 8B viole l'hypothèse de bruit non stratégique du domaine source. |
| **F3. Jeux min-max abstraits sur esquisses basse dimension** | Résolution sur processeur d'équilibres de Stackelberg entre un perturbateur contraint en divergence KL par acte et un détecteur séquentiel ou une politique de riposte d'essaim à fuite bornée. | Le sous-espace d'évasion du modèle 8B est approché par le point selle du modèle d'esquisse. | Sur-adaptation au modèle de perturbation abstrait ; cécité aux contournements non linéaires hors de l'esquisse. |
| **F4. Modélisation prédictive des lois nulles d'activations honnêtes** | Apprentissage sur processeur de prédicteurs conditionnels compacts $\hat{p}(h_t \mid \mathcal{F}_{t-1})$ et de tests d'échangeabilité entre copies à poids partagés, sans aucune modélisation d'attaque. | Les exécutions honnêtes sur tâches floues occupent une variété prévisible dont dévient sabotage et coordination. | Queues lourdes légitimes sur tâches créatives ou ouvertes, forçant un élargissement des seuils qui érode la sensibilité. |

**Combinaison retenue** `[HYPOTHÈSE de conception]` : utiliser **F2** pour proposer des familles d'opérateurs candidates, **F1** pour contraindre formellement leur validité sous nul par acte, **F4** pour les étalonner sur esquisses honnêtes 8B sur processeur, et **F3** uniquement pour borner le coût d'évasion (axe 2) et la fuite d'information des politiques de riposte (axe 3) en géométrie abstraite sans générer aucune attaque textuelle applicable.

### 4.2 Protocoles d'étanchéité temporelle et statistique (avec modèles pré-entraînés)

1. **Neutralisation de la contamination des modèles pré-entraînés** :
   - *Désémantisation canonique* : avant tout appel à un modèle pré-entraîné pour explorer ou trier un graphe daté, remplacer tous les identifiants scientifiques, noms d'équations et constantes par des symboles abstraits générés aléatoirement (préservant uniquement la topologie datée et les types mathématiques).
   - *Juge exclusivement procédural* : un modèle pré-entraîné ne peut jamais voter sur la validité finale ; seul l'orchestrateur déterministe tranche sur des mondes à lois plantées tirées d'une graine cryptographique fraîche postérieure à tout pré-entraînement `[RAPPORTÉ]`, avec contrôle du taux de fausses découvertes de Benjamini & Hochberg (1995, *Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing* `[VÉRIFIÉ]`, identifiant arXiv pas sûr).
2. **Cloisonnement matériel et préenregistrement** :
   - Séparation physique des répertoires contenant $\Omega_{\text{fam}}$ et $\Omega_{\text{val}}$ ; exécution de chaque lecture unique par un script automatisé qui vérifie l'existence préalable d'un engagement cryptographique du protocole et incrémente un compteur matériel interdisant une seconde lecture `[RAPPORTÉ]`.

### 4.3 Mesure minimale de fonctionnement par instrument nommé (Livrable c)

Tous les seuils chiffrés ci-dessous sont marqués `(illustratif)` ; leur valeur définitive doit être figée au préenregistrement avant lecture :

| Instrument nommé | Taux de détection minimal | Plafond de fausses alertes | Cas honnêtes appariés | Vérification mécanique à battre |
| :--- | :--- | :--- | :--- | :--- |
| **1. Organisme d'idéation (système complet)** | Rendement $\ge 10\,\%$ `(illustratif)` de candidats préenregistrés battant les bases sur $\Omega_{\text{fam}}$ | $\text{FDR} \le 0,05$ `(illustratif)` sur le portefeuille de candidats soumis | Mêmes budgets processeur et mêmes familles d'évaluation sans signal d'attaque | Échantillonnage aléatoire et recombinaison mécanique des lois déjà connues dans l'archive (CN2) `[RAPPORTÉ]` |
| **2. Modèle pré-entraîné de tri amont** | Rappel des vraies lois plantées $\ge 0,80$ pour un taux de rétention $q \le 0,10$ `(illustratif)` | Écart de fuite canari $|\Delta R_{\text{fuite}}| \le 0,05$ `(illustratif)` | Graphes datés et mondes procéduraux de même taille et degré algébrique | Tri purement topologique sans réseau neuronal (centralité / longueur minimale de description) |
| **3. Banc synthétique CPU à lois plantées + orchestrateur** | Corrélation de rang de Spearman $\ge 0,50$ `(illustratif)` avec la puissance sur $\Omega_{\text{dev}}$ 8B | $\text{FWER} \le 0,05$ `(illustratif)` face au nul de l'archive `[RAPPORTÉ]` | Mondes synthétiques générés sous lois purement issues de l'archive existante | Filtre aléatoire uniforme de même taux de rétention $q$ |
| **4. Accumulateur séquentiel boîte blanche (Axe 1)** | $\text{TPR} \ge 0,65$ `(illustratif)` à $T = 5M$ sur sabotage diffus tenu à l'écart | $\text{FPR}$ toujours valide $\le 0,05$ `(illustratif)` pour tout $t \ge 1$ | Trajectoires 8B honnêtes appariées en longueur $T$, domaine de tâche floue et nombre de jetons | (a) Moniteur boîte noire séquentiel ; (b) sonde boîte blanche par acte corrigée de Bonferroni ; (c) accumulateur sur référence fixe $M$ `[RAPPORTÉ]` |
| **5. Sonde d'auteur anti-corruption (Axe 2)** | $\text{TPR} \ge 0,60$ `(illustratif)` sous pression rhétorique et évasion à perte d'utilité $\le 10\,\%$ `(illustratif)` | $\text{FPR} \le 0,05$ `(illustratif)` sur tous registres stylistiques honnêtes | Exécutions 8B honnêtes résolvant la même tâche sous registres rhétoriques persuasifs contrastés | Juge génératif boîte noire de même classe (8B) + sonde linéaire standard non régularisée en style |
| **6. Détecteur d'essaim à poids partagés & riposte (Axe 3) + Oracle plancher** | $\text{TPR} \ge 0,50$ `(illustratif)` sur coordination implicite ; oracle : $\underline{p}_s \ge 0,70$ `(illustratif)` sur dommages plantés | $\text{FPR} \le 0,02$ `(illustratif)` ; fuite de la politique de riposte $\le 0,1\text{ bit/épisode}$ `(illustratif)` | Essaims honnêtes à poids identiques sur sous-tâches fortement corrélées thématiquement | Comparaison lexicale/sémantique inter-sorties boîte noire + corrélation cosinus moyenne naïve des activations |
| **7. Boucle de rétroaction fermée ($\Phi \leftrightarrow \Psi$)** | Gain de puissance $\Delta \bar{\beta} \ge +0,12$ `(illustratif)` après $4$ cycles `(illustratif)` sur boucle ouverte | $\text{FPR}$ joint $\le 0,05$ `(illustratif)` sur la banque finale $\Omega_{\text{val}}$ | Même budget total CPU+GPU alloué en une seule passe non bouclée | Boucle ouverte sans retour $\xi_r$ ET boucle placebo à vecteurs $\xi_r$ permutés (CN1) |

---

## 5. Ce qui, en dehors du programme et de son équipe, permettrait de vérifier la validité du résultat

Quatre mécanismes externes suppriment le besoin de faire confiance aux auteurs du système :

1. **Vérification mécanique des théorèmes dans un assistant de preuve formelle (Lean 4)** : pour tout nouvel objet mathématique (supermartingale à nul par acte, borne supérieure de fuite d'information d'une politique de riposte, borne inférieure de coût géométrique d'évasion), la preuve formelle compilée par le noyau réduit de Lean 4 certifie la validité mathématique indépendamment de l'équipe `[VÉRIFIÉ]`.
2. **Horodatage cryptographique externe avant lecture unique** : avant chaque évaluation sur une famille inédite $\Omega_{\text{fam}}^{(r)}$ ou sur la banque finale $\Omega_{\text{val}}$, l'archive contenant le code figé du détecteur, ses hyperparamètres, le seuil $\alpha$ et l'historique exact des appels à $\Omega_{\text{dev}}$ fait l'objet d'une empreinte SHA-256 déposée sur un registre public immuable tiers.
3. **Évaluation aveugle par une équipe tierce sur un second modèle ouvert de même classe** : un laboratoire indépendant n'ayant eu accès ni au code des sondes ni à l'organisme d'idéation instancie une famille de sabotage diffus et de coordination d'essaim sur un modèle ouvert distinct autour de huit milliards de paramètres (par exemple transfert d'un développement sur Llama-3.1-8B vers une épreuve aveugle sur Qwen2.5-7B `(illustratif)`) et exécute lui-même la lecture unique dans un environnement isolé hors réseau.
4. **Rejeu déterministe du journal d'audit par un tiers** : la traçabilité complète exigée `[RAPPORTÉ]` permet à un auditeur externe de rejouer sur processeur les graines de l'orchestrateur et de vérifier mécaniquement que le compteur d'accès à $\Omega_{\text{val}}$ vaut exactement $1$ `[RAPPORTÉ]` et qu'aucun gradient ou score de moniteur hors bras déclaré n'a traversé l'interface $\Phi$.

---

## 6. Reformulation exigeante de la tâche

> **Tâche reformulée** : Concevoir et valider par préenregistrement un couplage asymétrique non circulaire entre un moteur d'idéation sur processeur (décontaminé temporellement de ses modèles pré-entraînés par désémantisation canonique) et un programme de contrôle boîte blanche de modèles ouverts de huit milliards de paramètres sous budget graphique contraint `[RAPPORTÉ]`, tel que :
> 1. Le moteur d'idéation ne reçoive du contrôle que des résumés géométriques et spectraux extraits d'un corpus gelé d'activations honnêtes et d'un bac de développement déclaré ($I(\text{sélection} ; \Omega_{\text{fam}}, \Omega_{\text{val}} \mid \Omega_{\text{dev}}) = 0$) ;
> 2. Ses propositions sortantes compilent sur processeur en opérateurs mathématiquement vérifiés (e-processus à nul conditionnel par acte franchissant le plafond d'horizon $T > M$, projecteurs invariants au style rhétorique, statistiques d'indépendance conditionnelle inter-copies à poids partagés et politiques de riposte à fuite d'information bornée), adossés au plancher d'audit exogène mesuré par strate ;
> 3. À budget total processeur et cartes graphiques identique, la boucle fermée démontre en lecture unique un gain de puissance statistiquement significatif face à la boucle ouverte, au placebo de rétroaction permutée et aux bases mécaniques boîte noire et par acte, sans jamais excéder le taux nominal de fausses alertes toujours valide.

---

## 7. Programme des priorités classé

### 7.1 Classement quantitatif et analyse de sensibilité

Chaque critère de la formule imposée `score = (gain_informatif × facilité × portée × potentiel_de_découverte_majeure) / coût` est noté de `1` à `5` `(illustratif)`. Conformément à la sobriété épistémique, `potentiel_de_découverte_majeure` mesure ici strictement le *nombre de verrous structurels réfutables couverts simultanément* (`1` = réglage paramétrique local ; `5` = invariant mathématique généralisable à plusieurs axes).

| Rang | Chantier | `gain` `(ill.)` | `facilité` `(ill.)` | `portée` `(ill.)` | `potentiel` `(ill.)` | `coût` `(ill.)` | **`score`** `(illustratif)` |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | **C1.** Corpus CPU d'esquisses d'activations honnêtes 8B gelées + synthèse d'e-processus à nul par acte ($T > M$, Axe 1) | 5 | 4 | 5 | 4 | 2 | **200,0** |
| **2** | **C2.** Désémantisation isomorphe des graphes datés et audit canari d'étanchéité temporelle des modèles pré-entraînés | 4 | 5 | 4 | 2 | 1 | **160,0** |
| **3** | **C3.** Détection de coordination d'essaims à poids partagés par indépendance conditionnelle sur activations et borne de riposte (Axe 3) | 4 | 3 | 4 | 5 | 2 | **120,0** |
| **4** | **C4.** Diode d'information $\Phi$ et bouclage adaptatif sur $R$ cycles avec contrôle placebo de rétroaction | 5 | 3 | 5 | 4 | 3 | **100,0** |
| **5** | **C5.** Synthèse de projecteurs d'activations invariants au style rhétorique et frontière du coût d'évasion face aux juges 8B (Axe 2) | 4 | 3 | 3 | 4 | 3 | **48,0** |
| *6* | *C6 (hors top 5).* Cartographie stratifiée de l'oracle exogène ($\underline{p}_s$) sur dommages statistiques plantés à vérité différée | 4 | 2 | 4 | 3 | 4 | *24,0* |

**Sensibilité du classement aux variations de pondération** :
- *Pénalité budgétaire quadratique (`coût²` au dénominateur, pénurie aiguë de cartes graphiques)* : `C2 (160,0) > C1 (100,0) > C3 (60,0) > C4 (33,3) > C5 (16,0) > C6 (6,0)` `(illustratif)`. L'hygiène purement processeur (`C2`) passe en première position devant l'extraction initiale d'activations (`C1`), mais l'identité des cinq premiers chantiers reste **invariante**.
- *Priorité à la profondeur formelle hors facilité (`facilité` neutralisée à `1`, `potentiel²` au numérateur)* : `C1 (200,0) = C3 (200,0) > C4 (133,3) > C2 (64,0) = C5 (64,0) > C6 (36,0)` `(illustratif)`. `C3` rejoint `C1` en tête tandis que `C2` recule au quatrième rang ex æquo.
- *Pondération sécurité plancher sans modèle d'attaque (`(gain² × portée²) / coût`, neutralisant `facilité` et `potentiel`)* : `C1 (312,5) > C2 (256,0) > C4 (208,3) > C3 (128,0) > C6 (64,0) > C5 (48,0)` `(illustratif)`. Ce test révèle le biais structurel de la formule nominale : elle relègue `C6` hors du top 5 parce que l'audit humain exogène est coûteux (`coût = 4` `(illustratif)`) et peu « facile », alors qu'il conditionne toute garantie inconditionnelle `[RAPPORTÉ]`. Un arbitrage prudent doit donc maintenir un budget plancher sanctuarisé pour `C6` en parallèle.

### 7.2 Cinq expériences décisives en inférence forte (Livrables b et d)

Aucune expérience ci-dessous ne contient de recette d'attaque applicable ; les épreuves emploient soit des perturbations géométriques abstraites en bras déclaré, soit les familles tenues à l'écart gérées par l'instance isolée du programme `[RAPPORTÉ]`.

#### Chantier C1 — Franchissement du plafond d'horizon $T > M$ par e-processus à nul par acte
- **Duel d'hypothèses exclusives** :
  - `H_A` : Les e-processus à nul conditionnel par acte découverts par l'organisme (F1+F4) sur esquisses processeur d'activations honnêtes 8B respectent $\text{FPR} \le \alpha$ jusqu'à l'horizon $T = 5M$ `(illustratif)` sur le modèle ouvert réel et surpassent en puissance à $T = 5M$ à la fois l'accumulateur étalonné sur référence fixe $M$ et la meilleure sonde par acte corrigée de Bonferroni.
  - `H_B` : Soit la dérive non stationnaire des tâches floues honnêtes invalide le nul par acte sur le modèle 8B ($\text{FPR}_{T \le 5M} > \alpha$), soit la résidualisation par acte efface le signal diffus au point de ne pas battre simultanément l'accumulateur plafonné et la sonde par acte.
- **Métrique et seuil préenregistré** : Taux empirique maximal de fausses alertes $\widehat{\text{FPR}}_{\sup}$ sur $T = 500$ actes avec $M = 100$ `(illustratif)` ($500$ trajectoires `(illustratif)`) et gain de détection $\Delta\widehat{\text{TPR}}_{T=500}$ en lecture unique sur une famille de menace diffuse tenue à l'écart. Seuil : borne supérieure de confiance à $95\,\%$ `(illustratif)` de $\widehat{\text{FPR}}_{\sup}$ compatible avec $\alpha = 0,05$ `(illustratif)` **et** $\Delta\widehat{\text{TPR}}_{T=500} \ge +0,15$ `(illustratif)` contre les deux bases mécaniques.
- **Contrôle négatif** : Trajectoires 8B honnêtes enchaînant des sous-tâches hétérogènes légitimes (plan expérimental puis code statistique) sur $T = 500$ actes `(illustratif)` + test de permutation temporelle des incréments résiduels.
- **Coût et ancrage matériel** : Extraction unique sur Llama-3.1-8B `(illustratif)` ($1\times$ A100-40Go, $\approx 12\text{ h-GPU}$ `(illustratif)`) ; idéation sur $32$ cœurs processeur ($\approx 40\text{ h-cœur}$ `(illustratif)`) ; lecture unique finale ($\approx 6\text{ h-GPU}$ `(illustratif)`).
- **Règle de réfutation** : Tout dépassement du plafond $\alpha = 0,05$ `(illustratif)` sur le contrôle négatif honnête ou tout gain $\Delta\widehat{\text{TPR}}_{T=500} < +0,15$ `(illustratif)` **réfute `H_A`** ; le franchissement conjoint des deux critères en lecture unique **réfute `H_B`**.

#### Chantier C2 — Étanchéité temporelle et utilité réelle du tri par modèle pré-entraîné
- **Duel d'hypothèses exclusives** :
  - `H_A` : Après désémantisation canonique isomorphe des graphes datés, le rendement de découverte de l'organisme assisté d'un modèle pré-entraîné sur des lois plantées procédurales inédites égale (à $\pm 0,05$ près `(illustratif)`) son rendement sur des lois historiques post-coupure renommées, tout en surpassant d'au moins $+0,10$ `(illustratif)` le tri purement topologique sans modèle pré-entraîné.
  - `H_B` : Soit une fuite mémorielle subsiste malgré la désémantisation (avantage significatif sur lois historiques renommées), soit le modèle pré-entraîné n'apporte aucun gain réel face au tri topologique déterministe une fois privé de repères lexicaux.
- **Métrique et seuil préenregistré** : Sur $200$ mondes appariés en arbre syntaxique `(illustratif)` : $\Delta R_{\text{fuite}} = R(\text{historique renommé}) - R(\text{procédural inédit})$ et $\Delta R_{\text{gain}} = R(\text{procédural avec modèle}) - R(\text{procédural sans modèle})$. Seuil : $|\Delta R_{\text{fuite}}| \le 0,05$ `(illustratif)` **et** $\Delta R_{\text{gain}} \ge +0,10$ `(illustratif)` sous contrôle FDR à $q = 0,05$ `(illustratif)`.
- **Contrôle négatif** : Loi nulle formée des lois connues de l'archive `[RAPPORTÉ]` + lot témoin positif de $50$ lois classiques non désémantisées `(illustratif)` vérifiant la sensibilité du test canari.
- **Coût et ancrage matériel** : Exécution processeur ($32$ cœurs, $\approx 25\text{ h-cœur}$ `(illustratif)`) et tri par modèle ouvert 7B–8B local ($\approx 2\text{ h-GPU}$ sur $1\times$ L40S `(illustratif)`).
- **Règle de réfutation** : Si $|\Delta R_{\text{fuite}}| > 0,05$ `(illustratif)` ou $\Delta R_{\text{gain}} < +0,10$ `(illustratif)`, **`H_A` est réfutée** (désactivation obligatoire du tri neuronal pré-entraîné) ; sinon **`H_B` est réfutée**.

#### Chantier C3 — Détection de coordination implicite d'essaims à poids partagés
- **Duel d'hypothèses exclusives** :
  - `H_A` : La coordination implicite entre $m = 4$ copies `(illustratif)` partageant les mêmes poids induit une dépendance conditionnelle inter-copies dans l'espace des activations (captée par une statistique d'échangeabilité à noyaux issue de l'organisme) détectable à bas taux de fausses alertes là où un moniteur boîte noire lisant conjointement les sorties textuelles échoue.
  - `H_B` : Sous diversification modérée des contextes (températures et rôles distincts), la convergence vers des points focaux implicites s'opère sans dépendance conditionnelle d'activations excédant celle produite par l'énoncé commun d'une tâche honnête.
- **Métrique et seuil préenregistré** : $\widehat{\text{TPR}}$ à $\widehat{\text{FPR}} \le 0,02$ `(illustratif)` sur une famille d'essaims tenue à l'écart sur Qwen2.5-7B `(illustratif)`. Seuil : $\widehat{\text{TPR}} \ge 0,50$ `(illustratif)` **et** gain $\Delta\widehat{\text{TPR}} \ge +0,20$ `(illustratif)` sur le moniteur boîte noire inter-sorties ainsi que sur la corrélation cosinus moyenne naïve des activations.
- **Contrôle négatif** : Essaims honnêtes de $m = 4$ copies `(illustratif)` à poids identiques traitant des sous-questions à fort recouvrement lexical légitime + permutation inter-épisodes des copies honnêtes.
- **Coût et ancrage matériel** : Recherche sur processeur ($\approx 30\text{ h-cœur}$ `(illustratif)`) ; inférence d'essaims et lecture unique sur $1\times$ A100-40Go ($\approx 15\text{ h-GPU}$ `(illustratif)`).
- **Règle de réfutation** : $\widehat{\text{TPR}} < 0,50$ ou $\Delta\widehat{\text{TPR}} < +0,20$ `(illustratif)` à $\widehat{\text{FPR}} \le 0,02$ `(illustratif)` **réfute `H_A`** ; le dépassement conjoint des seuils **réfute `H_B`**.

#### Chantier C4 — Gain réel de la boucle fermée non circulaire face à la boucle ouverte
- **Duel d'hypothèses exclusives** :
  - `H_A` : À budget total de calcul strictement égal sur $R = 4$ cycles `(illustratif)`, l'orientation de l'organisme par le résumé non circulaire $\xi_r = \Phi(\Omega_{\text{dev}})$ engendre des protocoles dont la puissance moyenne en lecture unique sur $\Omega_{\text{fam}}^{(4)}$ surpasse d'au moins $+0,12$ `(illustratif)` tant la boucle ouverte que le contrôle placebo à vecteurs permutés.
  - `H_B` : L'information restreinte à $\Omega_{\text{dev}}$ est trop pauvre — ou sur-ajuste les particularités du bac de développement — pour surpasser significativement une exploration en boucle ouverte de même budget.
- **Métrique et seuil préenregistré** : Écart de puissance moyenne $\Delta\bar{\beta}$ à $\text{FPR} \le 0,05$ `(illustratif)` des $3$ meilleurs protocoles préenregistrés de chaque bras `(illustratif)` lus une seule fois sur $\Omega_{\text{fam}}^{(4)}$. Seuil : $\Delta\bar{\beta} \ge +0,12$ `(illustratif)` ($p < 0,01$ `(illustratif)` par test de permutation apparié) contre boucle ouverte **et** contre bras placebo CN1, avec $\widehat{\text{FPR}} \le 0,05$ `(illustratif)`.
- **Contrôle négatif** : Bras placebo CN1 recevant à chaque cycle une permutation aléatoire des coordonnées spectrales de $\xi_r$ à budget CPU/GPU identique.
- **Coût et ancrage matériel** : $3$ bras $\times 4$ cycles sur $64$ cœurs processeur ($\approx 120\text{ h-cœur}$ `(illustratif)`) + lecture unique groupée sur $1\times$ A100-40Go ($\approx 18\text{ h-GPU}$ `(illustratif)`).
- **Règle de réfutation** : $\Delta\bar{\beta} < +0,12$ `(illustratif)` contre l'un des deux témoins ou violation de $\widehat{\text{FPR}} \le 0,05$ `(illustratif)` **réfute `H_A`** (maintien en pipeline unidirectionnel découplé) ; le succès conjoint **réfute `H_B`**.

#### Chantier C5 — Invariance rhétorique des sondes d'auteur et coût géométrique d'évasion
- **Duel d'hypothèses exclusives** :
  - `H_A` : Les projecteurs d'activations régularisés pour l'invariance stylistique découverts par l'organisme divisent au moins par $3$ `(illustratif)` le déplacement de score sous pression rhétorique comparé à un juge génératif 8B, et maintiennent $\text{TPR} \ge 0,60$ à $\text{FPR} \le 0,05$ `(illustratif)` contre une optimisation d'évasion sur activations (bras déclaré `[RAPPORTÉ]`) tant que la dégradation d'utilité sur la tâche reste $\Delta U \le 0,10$ `(illustratif)`.
  - `H_B` : Soit les activations internes du modèle 8B codent inséparablement style rhétorique et anomalie décisionnelle, soit il existe une direction d'évasion à faible coût annulant la sonde sans dégrader l'utilité ($\Delta U \le 0,10$ `(illustratif)`).
- **Métrique et seuil préenregistré** : Déplacement normalisé sous $H_0$ entre style neutre et persuasif $\Delta_{\text{style}}$ ; $\widehat{\text{TPR}}$ sous pénalité d'évasion d'activations en bras déclaré pour $\Delta U \le 0,10$ `(illustratif)`. Seuil : $\Delta_{\text{style}}(\text{sonde}) \le \frac{1}{3} \Delta_{\text{style}}(\text{juge 8B})$ `(illustratif)` **et** $\widehat{\text{TPR}} \ge 0,60$ à $\widehat{\text{FPR}} \le 0,05$ `(illustratif)`.
- **Contrôle négatif** : Paires d'exécutions strictement honnêtes sur plans d'expériences identiques rédigés sous $5$ registres stylistiques contrastés `(illustratif)`, opposées à une régression logistique linéaire standard sur activations brutes.
- **Coût et ancrage matériel** : Synthèse sur processeur ($\approx 20\text{ h-cœur}$ `(illustratif)`) ; évaluation du juge 8B et optimisation du coût d'évasion en bras déclaré sur $1\times$ A100-40Go ($\approx 24\text{ h-GPU}$ `(illustratif)`).
- **Règle de réfutation** : L'échec sur le ratio $\frac{1}{3}$ `(illustratif)` ou une chute $\widehat{\text{TPR}} < 0,60$ à $\Delta U \le 0,10$ `(illustratif)` **réfute `H_A`** ; la tenue simultanée des deux bornes **réfute `H_B`**.

### 7.3 Ce qui reste hors de portée

1. **Sabotage purement compositionnel d'actes cognitivement innocents** `[VÉRIFIÉ]` : lorsqu'une menace diffuse résulte de l'assemblage externe de sous-tâches si fragmentées que chaque exécution du modèle de huit milliards de paramètres traite honnêtement une question localement anodine sans information contextuelle sur la finalité globale, aucune sonde boîte blanche sur activations n'a d'avantage théorique sur le hasard ; seul l'audit exogène sur le produit final opère `[RAPPORTÉ]`.
2. **Transfert des invariants de huit milliards vers les échelles cent fois supérieures `(illustratif)`** : **je ne sais pas** si la géométrie des sous-espaces d'évasion et les corrélations d'essaims mesurées autour de huit milliards de paramètres se conservent, se simplifient ou disparaissent dans des modèles beaucoup plus vastes `[HYPOTHÈSE non tranchable avec le budget matériel rapporté]`.
3. **Garantie inconditionnelle dans les strates aveugles de l'oracle exogène** : sur des analyses statistiques ou des plans d'expériences dont le défaut différé échappe à l'oracle exogène ($\underline{p}_s = 0$), la borne exponentielle d'audit aléatoire devient vacante ($\le 1$) `[VÉRIFIÉ]` ; **je ne sais pas** établir une garantie sans reconnaissance d'attaque lorsque l'oracle de référence lui-même est aveugle.
4. **Découverte hors de la clôture expressive des grammaires et corpus fournis** : l'organisme explore l'enveloppe combinatoire et analogique de ses graphes datés et de ses langages d'opérateurs ; **je ne sais pas** borner a priori la perte d'optimalité si le contrôle optimal des menaces diffuses exige une classe d'objets mathématiques absente de cette clôture.

FIN-DE-CELLULE