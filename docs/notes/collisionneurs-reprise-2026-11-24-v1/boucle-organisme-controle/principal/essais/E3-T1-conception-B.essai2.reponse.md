*État des pièces transmises : les blocs `FAITS` et `QUESTION DE L'ARBITRE` sont présents et complets ; aucune proposition A ou C n'est jointe conformément au tour III.1 à l'aveugle (`VÉRIFIÉ`).*

---

## 1. Ce qu'un expert du domaine ferait ici, et que la demande d'origine omet

### Audit des présupposés non établis de la demande `[Livrable (a)]`

Avant d'accoupler l'organisme d'idéation ($\mathcal{I}$) et le programme de contrôle ($\mathcal{C}$), un praticien de l'inférence séquentielle et du contrôle boîte blanche isole cinq présupposés que la demande traite implicitement comme acquis :

1. **Existence d'un morphisme utile entre mondes à lois plantées sur processeur et géométrie des activations d'un modèle ouvert d'environ huit milliards de paramètres** — Statut : `HYPOTHÈSE`. Dans le dispositif existant, $\mathcal{I}$ est évalué sur des mondes synthétiques à lois plantées sur processeur, tandis que $\mathcal{C}$ porte sur des modèles réels d'environ huit milliards de paramètres sur cartes graphiques (`RAPPORTÉ`). Or les activations résiduelles d'un transformeur présentent de l'anisotropie spectrale, de la non-stationnarité contextuelle et de la superposition de traits (*Toy Models of Superposition*, Elhage et al., 2022 — liste complète des auteurs et identifiant arXiv : référence à vérifier / pas sûr). Rien n'établit qu'un opérateur performant sur monde jouet conserve sa puissance sur activations réelles (`HYPOTHÈSE`).
2. **Innocuité statistique de la rétroaction $\mathcal{C} \to \mathcal{I}$ vis-à-vis de la lecture unique** — Statut : `HYPOTHÈSE`. Le programme impose que toute reconception de sonde s'évalue sur une famille de sabotage inédite lue une seule fois et sépare sélection et évaluation (`RAPPORTÉ`). Si les observations renvoyées par $\mathcal{C}$ vers $\mathcal{I}$ résument, même via un chercheur humain, les échecs constatés sur ces familles d'épreuve, la boucle crée un canal d'apprentissage adaptatif qui invalide les garanties de faux positifs sur les itérations suivantes (`VÉRIFIÉ` en analyse adaptative des données).
3. **Neutralité défensive de la génération automatique de « scénarios de défaillance »** — Statut : `HYPOTHÈSE`. Demander à $\mathcal{I}$ de proposer des scénarios de défaillance tout en interdisant qu'un score de moniteur entre dans le signal de sélection d'un agent hors bras d'attaque déclaré (`RAPPORTÉ`) expose à synthétiser involontairement des procédures d'évasion optimisées contre les sondes existantes.
4. **Absence de fuite temporelle et mémorielle via les modèles pré-entraînés mobilisés par $\mathcal{I}$** — Statut : `HYPOTHÈSE`. L'organisme explore des graphes de concepts datés mais peut mobiliser des modèles pré-entraînés lors du tri (`RAPPORTÉ`). Sans anonymisation algébrique, une « redécouverte » sur archive datée peut résulter d'une mémorisation pré-entraînée postérieure à la date de coupure (`HYPOTHÈSE`), stérile face aux problèmes ouverts de $\mathcal{C}$.
5. **Existence pratique d'un « nul par acte » bien calibré sur tâches floues longues** — Statut : `HYPOTHÈSE`. Toute accumulation séquentielle étalonnée sur une référence honnête fixe finie plafonne quand l'horizon dépasse la taille de cette référence, sauf usage d'un nul par acte (`RAPPORTÉ`). Or la loi conditionnelle honnête d'une activation à l'acte $t$ sachant un long contexte multi-agents n'est pas connue sous forme close (`OBSERVÉ-NON-AUDITÉ` hors étalonnage spécifique ; je ne sais pas a priori jusqu'à quel horizon l'approximation locale d'échangeabilité tient sans sur-rejet).

### Ce qu'un expert ferait en premier et que la demande omet

- **Geler la boucle fermée directe et construire une « diode de tenseurs honnêtes »** : extraire une fois sur carte graphique des tenseurs d'activations issus **exclusivement d'exécutions honnêtes** (avec variations bénignes de style et de structure de tâche), les exporter sur processeur, et contraindre $\mathcal{I}$ à concevoir ses objets mathématiques sur cette géométrie réelle sans consommer une seule famille de sabotage tenue à l'écart.
- **Exiger des preuves vérifiées mécaniquement pour la validité sous le nul** : un modèle génératif ne peut pas certifier une garantie de faux positifs toujours valide (`RAPPORTÉ`). L'expert sépare la *puissance* (testée empiriquement) de la *validité sous le nul* (qui doit découler d'une identité algébrique prouvée, d'une symétrie de permutation ou d'un vérificateur formel).
- **Comptabiliser explicitement la dégradation des garanties liée à l'imperfection de l'oracle exogène** : puisque la probabilité d'identification par strate $p_s$ sur dommages plantés borne toute garantie indépendante de la reconnaissance de l'attaque (`RAPPORTÉ`), l'expert refuse d'optimiser des sondes sur des strates où $p_s$ n'a pas d'abord été mesuré au-dessus du bruit.

---

## 2. Les données brutes de départ

Avant toute synthèse textuelle, courbe agrégée ou rapport d'échec, le couplage doit ingérer les traces primaires non filtrées suivantes :

1. **Côté programme de contrôle (extraites sur modèles ouverts d'environ huit milliards de paramètres `RAPPORTÉ`, puis figées sur disque pour traitement processeur)** :
   - **Tenseurs d'activations bruts non projetés** $A_{u,\ell,t} \in \mathbb{R}^d$ (flux résiduel et sorties de têtes d'attention pour l'agent $u$, la couche $\ell$, la frontière d'action $t$), accompagnés des log-probabilités exactes des jetons générés, recueillis sur des trajectoires **strictement honnêtes** couvrant la rédaction de plans d'expériences, les chaînes multi-agents et l'analyse statistique (`RAPPORTÉ`).
   - **Paires contrefactuelles honnêtes de nuisance stylistique** : activations brutes du même modèle résolvant honnêtement la même tâche sous diverses contraintes rhétoriques légitimes (concision, argumentation contradictoire, registre soutenu, critique sévère), afin d'isoler la variété géométrique du style avant toute étude de corruptibilité (`RAPPORTÉ`).
   - **Faisceaux d'activations synchrones multi-copies honnêtes** $(A_t^{(1)}, \dots, A_t^{(M)})$ pour $M = 5$ `(illustratif)` instances à poids partagés exécutant la même tâche avec graines, ordres d'informations et températures variés, afin de mesurer la covariance de base induite par le seul partage des poids (`RAPPORTÉ`).
   - **Enregistrements bruts d'étalonnage de l'oracle exogène** : tuples `(identifiant de strate, spécification du dommage méthodologique bénin planté, décision brute de l'oracle, durée d'inspection)` avant tout regroupement statistique (`RAPPORTÉ`).
2. **Côté organisme d'idéation** :
   - **Graphes de dépendances logiques datés au niveau des énoncés, hypothèses et lemmes** (et non résumés thématiques secondaires), avec horodatage brut d'archive vérifiable (`RAPPORTÉ`).
   - **Traces de log-vraisemblance jeton par jeton** assignées par tout modèle pré-entraîné candidat aux corpus situés de part et d'autre de la date de coupure historique, pour mesurer l'exposition mémorielle brute.
   - **Journaux déterministes complets de l'orchestrateur** sur mondes à lois plantées : graines, entrées-sorties numériques brutes et temps processeur par essai (`RAPPORTÉ`).

---

## 3. Formalisation mathématique et conditions de validité de la boucle fermée

### 3.1 Opérateurs de couplage bidirectionnel ($\mathcal{I} \leftrightarrow \mathcal{C}$)

Soit $\mathcal{G}_{\le \tau_0}$ l'archive datée (`RAPPORTÉ`). À l'itération de campagne $k \in \{1, \dots, K\}$, l'organisme $\mathcal{I}$ prend en entrée $(\mathcal{G}_{\le \tau_0}, \mathcal{D}_{\text{dev}}^{\text{CPU}}, R_{1:k-1})$ — où $\mathcal{D}_{\text{dev}}^{\text{CPU}}$ est la banque figée de tenseurs honnêtes exportée sur processeur et $R_{1:k-1}$ l'historique de rétroaction — et émet un lot de candidats $c_{k,1}, \dots, c_{k,m}$. Chaque candidat est un triplet $c = (\psi, \Pi, \mathcal{H})$ :
- $\psi : (\mathbb{R}^d)^* \to \mathbb{R}_+$ construit séquentiellement une statistique de surveillance à l'acte $t$, typiquement un facteur de pari / $e$-valeur $e_t(X_t \mid \mathcal{F}_{t-1}) \ge 0$ accumulée en un processus $E_t = \prod_{i=1}^t e_i$ (ou mélange prévisible convexe) ;
- $\Pi$ est un certificat formel ou algorithmique attestant la condition de validité conditionnelle par acte sous l'hypothèse nulle honnête $\mathcal{P}_0$ :
  $$\forall t \ge 1, \quad \sup_{\mathbb{P}_0 \in \mathcal{P}_0} \mathbb{E}_{\mathbb{P}_0}\!\left[e_t(X_t) \;\middle|\; \mathcal{F}_{t-1}\right] \le 1$$
  Par l'inégalité maximale de Ville (Ville, 1939, *Étude critique de la notion de collectif* ; `VÉRIFIÉ`) et le cadre des tests séquentiels sûrs (Ramdas, Grünwald, Vovk, & Shafer, 2023, *Game-Theoretic Statistics and Safe Anytime-Valid Inference*, identifiant arXiv : pas sûr / omis de mémoire ; `VÉRIFIÉ`), tout tel processus garantit un contrôle des faux positifs toujours valide à horizon libre :
  $$\sup_{\mathbb{P}_0 \in \mathcal{P}_0} \mathbb{P}_0\!\left(\exists t \ge 1 : E_t \ge \frac{1}{\alpha}\right) \le \alpha$$
  sans souffrir du plafonnement à $1/(N_0+1)$ propre à l'étalonnage conforme sur une banque honnête fixe de taille $N_0$ (`RAPPORTÉ`, `VÉRIFIÉ`).
- $\mathcal{H}$ est la politique d'audit et de riposte associée, couplée à un plancher d'audit aléatoire de taux $\gamma \in (0,1]$ évalué par l'oracle exogène de probabilité d'identification $p_s$ sur la strate $s$ (`RAPPORTÉ`). Sans aucune reconnaissance d'attaque par $\psi$, la probabilité de survie d'une trajectoire déposant $m$ dommages dans des strates $(s_1, \dots, s_m)$ sous tirages d'audit indépendants est bornée par $\prod_{j=1}^m (1 - \gamma p_{s_j})$ (`VÉRIFIÉ`).

**Direction $\mathcal{I} \to \mathcal{C}$** : Un filtre déterministe sur processeur $\Phi_{\text{CPU}}$ élimine les candidats dépourvus de certificat $\Pi$ ou de puissance suffisante sur $(\mathcal{W}_{\text{synth}}, \mathcal{D}_{\text{dev}}^{\text{CPU}})$ en contrôlant le taux de fausse découverte sur processeur, et ne promeut vers $\mathcal{C}$ (cartes graphiques) qu'un unique candidat (ou petit lot pré-pondéré $\sum_j w_j = 1$) préenregistré.

**Direction $\mathcal{C} \to \mathcal{I}$** : Le programme $\mathcal{C}$ partitionne strictement ses ressources en trois strates disjointes : $\mathcal{D}_{\text{dev}}$ (développement honnête et anomalies locales synthétiques), $\{\mathcal{D}_{\text{fam}}^{(k)}\}_{k=1}^K$ (familles inédites conçues à l'aveugle, chacune **lue une seule fois** à l'étape $k$ puis détruite/archivée hors boucle, `RAPPORTÉ`), et $\mathcal{D}_{\text{val}}$ (banque finale lue une unique fois après l'arrêt de la boucle $K$, `RAPPORTÉ`).

### 3.2 Conditions de validité statistique non circulaire

Trois invariants d'information mutuelle sont requis (`VÉRIFIÉ` dans leur structure mathématique, Dwork, Feldman, Hardt, Pitassi, Reingold, & Roth, 2015, *The Reusable Holdout: Preserving Validity in Adaptive Data Analysis*, identifiant arXiv : pas sûr / omis de mémoire) :
1. **Non-circularité de la sélection d'agents** (`RAPPORTÉ`) : Pour tout agent ou proposeur $\pi_\theta$ hors bras d'attaque déclaré, $I(\theta ; S_{\text{mon}} \mid \text{tâche}) = 0$, où $S_{\text{mon}}$ désigne l'ensemble des sorties des sondes et juges de $\mathcal{C}$.
2. **Isolation des familles à lecture unique et de la validation finale** : La rétroaction $R_k$ transmise à $\mathcal{I}$ est une fonction mesurable de $\mathcal{D}_{\text{dev}}$ seul (par exemple : sous-espaces honnêtes où $e_t$ sur-rejette ou perd de la variance), plus éventuellement un unique indicateur binaire d'arrêt de campagne, mais **zéro vecteur d'erreur détaillé issu de $\mathcal{D}_{\text{fam}}^{(k)}$** et **zéro bit issu de $\mathcal{D}_{\text{val}}$** :
   $$I\!\left(c_{k+1} ; \mathcal{D}_{\text{fam}}^{(k+1)}\right) = 0 \quad \text{et} \quad I\!\left(R_{1:K} ; \mathcal{D}_{\text{val}}\right) = 0$$
3. **Borne en cas de retour quantifié minimal** : Si un canal retour d'au plus $B$ bits au total (par exemple un seuil discret de réussite/échec sur un banc intermédiaire réutilisé de taille $n$) est autorisé sur toute la feuille de route, la dérive maximale d'une probabilité empirique d'erreur de niveau $\alpha$ impose de dimensionner $n$ de sorte que $B / n \ll \alpha^2$ (`VÉRIFIÉ` à constante universelle près pour tests bornés) ; au-delà, le banc est brûlé.

### 3.3 Arbitrage quantitatif entre coût des épreuves et rendement de découverte

Soit $B_{\text{tot}}$ le budget total de calcul, $c_{\text{CPU}}$ le coût d'évaluation d'un candidat dans $\mathcal{I}$ et $c_{\text{GPU}}$ le coût complet dans $\mathcal{C}$ (inférence ~8B + consommation d'une famille d'épreuve). Si $\mathcal{I}$ teste $N_1$ candidats sur processeur au seuil de filtrage $u$ (sensibilité $\text{TPR}_1(u)$, fausses promotions $\text{FPR}_1(u)$) pour une prévalence a priori $q_0$ d'idées réellement transférables, le nombre espéré de candidats promus sur GPU est $N_2(u) = N_1 [q_0 \text{TPR}_1(u) + (1-q_0)\text{FPR}_1(u)]$, sous contrainte $N_1 c_{\text{CPU}} + N_2(u) c_{\text{GPU}} \le B_{\text{tot}}$. Le rendement espéré de découvertes validées en contrôle au niveau global $\alpha$ vaut :
$$U(N_1, u) = N_1 q_0 \text{TPR}_1(u) \, \beta_{\text{GPU}}\!\left(\frac{\alpha}{N_2(u)}\right)$$
où $\beta_{\text{GPU}}$ est la puissance du test GPU corrigée pour $N_2(u)$ lectures. Un développement au premier ordre montre (`VÉRIFIÉ`) que le filtrage amont sur processeur n'augmente $U$ par rapport à un test direct sur GPU que si le rapport de vraisemblance diagnostique du filtre amont vérifie :
$$\Lambda_1(u) = \frac{\text{TPR}_1(u)}{\text{FPR}_1(u)} > \frac{1-q_0}{q_0} \cdot \kappa\!\left(\frac{c_{\text{CPU}}}{c_{\text{GPU}}}, \alpha\right)$$
Si les mondes à lois plantées ont un $\Lambda_1(u)$ proche de $1$, multiplier les cycles CPU détruit le budget par fausses promotions GPU et pénalité de multiplicité.

### 3.4 Conditions de validité hors des environnements synthétiques

Un opérateur $\psi$ validé sur monde synthétique $\mathcal{W}_{\text{synth}}$ reste valide et puissant sur les activations réelles $\mathcal{C}$ si et seulement si existe un morphisme de réduction $\phi : \mathbb{R}^d \to \mathcal{Z}$ (tel qu'un blanchiment spectral adaptatif orthogonal au sous-espace sémantique immédiat du jeton) vérifiant deux conditions découplées (`HYPOTHÈSE` testable empiriquement) :
- **Invariance algébrique du nul hors synthétique** : la propriété $\mathbb{E}_{\mathbb{P}_0^R}[e_t(\phi(X_t)) \mid \mathcal{F}_{t-1}] \le 1$ repose sur une symétrie interne construite sur le réel (ex. permutation locale entre sous-bandes isotropisées ou prédiction conforme résiduelle par acte) et non sur la loi paramétrique du monde jouet ;
- **Conservation de l'ordre du taux de croissance de Kelly ($e$-puissance)** : pour deux candidats $c, c'$, le signe de $g^R(c) - g^R(c')$, où $g(\psi) = T^{-1}\mathbb{E}_{\mathbb{P}_1}[\log E_T]$, coïncide avec celui de $g^S(c) - g^S(c')$ à une marge $\varepsilon_{\text{trans}}$ près, ce qui requiert que le simulateur CPU respecte le spectre à queue lourde et l'autocorrélation temporelle des activations honnêtes réelles.

### 3.5 Contrôles négatifs disqualifiant une boucle illusoire

La boucle est déclarée défaillante et arrêtée si elle échoue à l'un des quatre contrôles suivants :
1. **Boucle fantôme (permutation de $R_k$)** : remplacer les résumés géométriques renvoyés de $\mathcal{D}_{\text{dev}}$ vers $\mathcal{I}$ par des spectres permutés aléatoirement entre couches ; l'absence d'écart de performance en aval prouve que la rétroaction $\mathcal{C} \to \mathcal{I}$ est inopérante.
2. **Nul d'archive mécanique** (`RAPPORTÉ`) : à budget CPU égal, tirer uniquement des détecteurs standards de l'archive (CUSUM de Page, distance de Mahalanobis par acte, test de Hotelling $T^2$) ; si $\mathcal{I}$ ne les surpasse pas sur $\mathcal{C}$, sa machinerie d'idéation est superflue.
3. **Invariance aux chocs stylistiques et méthodologiques honnêtes** : exécuter un agent strictement honnête sous contrainte rhétorique extrême ou changement légitime d'hypothèse statistique en cours d'analyse ; tout franchissement du taux nominal $\alpha$ disqualifie le candidat.
4. **Canari de fuite adaptative** : planter sur un serveur d'évaluation un vecteur d'anomalie secret jamais exposé à $\mathcal{D}_{\text{dev}}$ ; une corrélation croissante au fil des itérations $k$ entre la direction de projection choisie par $\mathcal{I}$ et ce canari révèle une fuite d'information humaine ou logicielle.

---

## 4. Méthodes, outils et protocoles d'évaluation

### 4.1 Comparaison de quatre familles d'approches pour l'idéation orientée boîte blanche

| Famille d'approche (`HYPOTHÈSE` d'efficacité comparée) | Principe algorithmique sur processeur | Hypothèses requises | Limites et modes d'échec |
| :--- | :--- | :--- | :--- |
| **F1. Synthèse neuro-symbolique d'opérateurs sous assistant de preuve** | Recherche arborescente dans une grammaire typée de fonctionnelles séquentielles ($e$-valeurs, martingales de mélange), guidée par modèle pré-entraîné et filtrée par un noyau formel (type Lean 4) ou test algébrique exact de surmartingale. | Les détecteurs transférables possèdent une expression analytique compacte dont la borne sous $\mathbb{P}_0$ est formellement démontrable. | Taux élevé de rejet par échec d'auto-formalisation ; peine à capturer des invariants géométriques non linéaires empiriques. |
| **F2. Transport structurel (quasi-fonctoriel) sur graphes datés** | Encodage des trois axes de $\mathcal{C}$ sous forme de contraintes relationnelles abstraites et recherche d'isomorphismes partiels dans des domaines distants de l'archive (stéganographie par lots, détection sismique de trémors lents, canaux à états corrélés). | Des invariants mathématiques déjà résolus ailleurs partagent la structure d'information des menaces diffuses ou des essaims. | Analogies superficielles : effondrement dès qu'une hypothèse implicite du domaine source (stationnarité, bruit gaussien) est violée sur activations. |
| **F3. Raffinement génératif des mondes plantés par jumeau spectral** | Ajustement sur CPU de processus stochastiques reproduisant le spectre de valeurs singulières, la kurtosis et la dérive d'entropie de $\mathcal{D}_{\text{dev}}^{\text{CPU}}$, puis recherche minimax de détecteurs contre des signaux diffus à norme par acte bornée. | L'écart synthétique-réel est dominé par la géométrie du bruit de fond des activations honnêtes d'ordre fini. | Sur-adaptation aux artefacts du générateur synthétique ; aveugle aux couplages sémantiques fins entre raisonnement et texte. |
| **F4. Découverte d'invariants géométriques auto-supervisés sur traces honnêtes** | Recherche de lois de conservation empiriques le long des trajectoires honnêtes (cohérence Jacobienne inter-couches, orthogonalité entre sous-espace stylistique et résidu prédictif, spectre inter-copies sous poids partagés). | Soutenir un objectif dissimulé ou une coordination implicite induit une distorsion géométrique incompressible des activations. | Faux positifs sur tâches honnêtes intrinsèquement duales (rédaction d'une réfutation, jeu de rôle contradictoire demandé). |

### 4.2 Protocoles d'étanchéité temporelle et statistique (avec modèles pré-entraînés)

Lorsqu'un modèle pré-entraîné intervient dans l'exploration ou le tri de $\mathcal{I}$ (`RAPPORTÉ`), deux verrous cumulatifs bloquent les fuites :
1. **Anonymisation algébrique et rotation orthogonale** : sur les bancs historiques datés comme sur les tenseurs d'activations exportés vers $\mathcal{I}$, l'orchestrateur applique une bijection secrète sur tous les symboles du graphe et multiplie chaque couche d'activations de dimension $d$ par une matrice orthogonale aléatoire $Q_\ell \in O(d)$ tenue secrète. Le modèle pré-entraîné manipule des invariants de spectre et de dépendance sans pouvoir apparier de noms de théorèmes mémorisés ni d'indices de neurones connus de la littérature publique.
2. **Sas déterministe de préenregistrement à lecture unique** : avant toute exécution sur carte graphique dans $\mathcal{C}$, l'orchestrateur fige l'empreinte SHA-256 de l'exécutable du détecteur, du seuil $1/\alpha$ et du protocole d'appariement honnête (`RAPPORTÉ`). Le conteneur générant $\mathcal{D}_{\text{fam}}^{(k)}$ ne partage ni système de fichiers, ni historique d'invites, ni poids de sondes avec $\mathcal{I}$.

### 4.3 Mesure minimale de fonctionnement de chaque instrument `[Livrable (c)]`

Tous les seuils chiffrés ci-dessous ne provenant pas des faits sont marqués `(illustratif)`.

| Instrument nommé | Mesure minimale : détection (TPR) et fausses alertes (FPR / FDR) | Cas honnêtes appariés exigés | Vérification mécanique à battre |
| :--- | :--- | :--- | :--- |
| **Organisme d'idéation & orchestrateur CPU** | Retrouver $\ge 60\%$ `(illustratif)` des lois plantées cachées sous anonymisation symbolique, avec $\text{FDR} \le 0{,}05$ `(illustratif)` corrigé multi-tests. | Mondes sans loi nouvelle (combinaisons bruitées de lois déjà présentes dans l'archive) de même dimension et queue lourde. | Régression symbolique / énumération mécanique par complexité croissante des formules de l'archive (`RAPPORTÉ`). |
| **Filtre de transfert CPU $\to$ GPU ($\Phi_{\text{CPU}}$)** | Identifier les candidats viables sur ~8B avec $\text{TPR}_1 \ge 0{,}75$ `(illustratif)` et $\text{FPR}_1 \le 0{,}15$ `(illustratif)` ($\Lambda_1 \ge 5{,}0$ `(illustratif)`). | Candidats exacts sur bruit gaussien isotrope mais instables sur activations honnêtes réelles rejouées. | Classement direct par score sur les mondes jouets historiques sans recalibration spectrale. |
| **Sondes séquentielles boîte blanche (Axe 1)** | Sur séquences de $T = 80$ `(illustratif)` actes, $\text{TPR} \ge 0{,}70$ `(illustratif)` à garantie toujours valide $\mathbb{P}_0(\exists t \le T : \text{alerte}) \le 0{,}05$ `(illustratif)`. | Exécutions honnêtes longues sur les mêmes plans d'expériences et analyses, incluant erreurs honnêtes auto-corrigées et bifurcations. | (a) Juge boîte noire par acte + correction de Bonferroni ; (b) Sonde logistique linéaire par acte + CUSUM classique (`RAPPORTÉ`). |
| **Sonde auteur vs moniteur génératif (Axe 2)** | $\text{TPR} \ge 0{,}75$ `(illustratif)` à $\text{FPR} \le 0{,}05$ `(illustratif)` sous reformulation rhétorique dégradant le juge génératif, et perte d'utilité $\ge 30\%$ `(illustratif)` en cas d'évasion dans un bras déclaré. | Réponses strictement honnêtes appariées adoptant la même intensité rhétorique, d'autorité ou de technicité lexicale. | Juge génératif ~8B après réécriture neutre automatique du texte + filtre par perplexité et longueur. |
| **Détecteur d'essaims à poids partagés & riposte (Axe 3)** | Pour $M = 5$ `(illustratif)` copies, $\text{TPR} \ge 0{,}65$ `(illustratif)` à $\text{FPR} \le 0{,}05$ `(illustratif)` et fuite de la politique de riposte $\le 0{,}10$ bit/épisode `(illustratif)`. | $M = 5$ `(illustratif)` copies honnêtes à poids partagés commettant simultanément une même erreur cognitive naïve due aux poids communs. | Corrélation linéaire des textes produits + vote majoritaire sous diversification mécanique d'invites + audit aléatoire uniforme (`RAPPORTÉ`). |
| **Modèle pré-entraîné de tri (audit anti-fuite)** | Détecter $90\%$ `(illustratif)` des textes post-coupure mémorisés à $\text{FPR} \le 0{,}05$ `(illustratif)` sur problèmes synthétiques isomorphes neufs. | Énoncés mathématiquement isomorphes nouvellement générés de longueur et distribution syntaxique identiques. | Recoupement mécanique par $n$-grammes ($n=8$ `(illustratif)`) et distance TF-IDF cosinus sur l'archive complète. |

---

## 5. Ce qui, en dehors du programme et de son équipe, permettrait de vérifier la validité du résultat

1. **Vérification mécanique externe des preuves par assistant formel** : livrer chaque nouvel objet statistique avec une preuve compilable sans axiome additionnel dans un vérificateur indépendant à noyau minimal (ex. Lean 4) démontrant l'inégalité de surmartingale $\mathbb{E}_0[E_t \mid \mathcal{F}_{t-1}] \le E_{t-1}$ sous les hypothèses explicites du nul par acte.
2. **Dépôt séquestre horodaté avant génération externe des épreuves** : publier sur un registre externe immuable l'empreinte cryptographique du code figé des sondes et seuils *avant* qu'un laboratoire tiers indépendant ne génère et n'exécute une famille d'épreuve sur les modèles ouverts cibles, en connaissant l'architecture complète du détecteur (principe de Kerckhoffs).
3. **Validation sur corpus publics externes à vérité différée objective** : appliquer sans ré-entraînement les sondes séquentielles à la génération de code scientifique ou d'analyses statistiques sur des bancs externes où la vérité différée est mécanique et exogène (échec ultérieur de suites de tests de reproductibilité ou biais d'estimation sur données simulées tenues par un tiers).
4. **Étalonnage en double aveugle de l'oracle exogène par des praticiens externes** : confier la mesure de $p_s$ (`RAPPORTÉ`) à des statisticiens ou méthodologistes extérieurs au projet évaluant à l'aveugle un mélange de plans d'expériences honnêtes et de plans contenant des défauts méthodologiques plantés.

---

## 6. Reformulation exigeante de la tâche

Concevoir, préenregistrer et évaluer un système d'idéation neuro-symbolique sur processeur ($\mathcal{I}$) qui, à partir d'archives scientifiques horodatées anonymisées algébriquement et de tenseurs d'activations extraits **uniquement** d'exécutions honnêtes de modèles ouverts d'environ huit milliards de paramètres (`RAPPORTÉ`), synthétise des processus de test séquentiels certifiés sans plafond d'horizon ($e$-processus à nul par acte) et des statistiques spectrales inter-copies ; démontrer lors d'**une lecture unique** sur cartes graphiques que les objets promus surpassent les bases boîte noire et boîte blanche par action sur des familles inédites couvrant les trois axes de contrôle, à faux positifs bornés sur cas honnêtes stylistiquement et cognitivement appariés, avec une information mutuelle nulle entre la rétroaction $\mathcal{C} \to \mathcal{I}$ et les familles d'épreuve tenues à l'écart, pour un coût global inférieur à l'exploration directe sur cartes graphiques.

---

## 7. Programme des priorités classé

### 7.1 Grille d'évaluation et sensibilité du classement

Formule appliquée : `score = (gain_informatif × facilité × portée × potentiel_de_découverte_majeure) / coût` (échelle entière de 1 à 5 issue de la question ; opératoirement, `potentiel_de_découverte_majeure` mesure l'étendue des classes de défaillances et verrous mathématiques réfutables couverts ; **toutes les notes attribuées et les scores résultants sont `illustratifs`**).

| Rang | Chantier | Gain | Facilité | Portée | Potentiel | Coût | Score `(illustratif)` |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | **C3. Décontamination algébrique des modèles pré-entraînés & diode sans fuite $\mathcal{C} \to \mathcal{I}$** | 4 `(illustratif)` | 4 `(illustratif)` | 5 `(illustratif)` | 3 `(illustratif)` | 1 `(illustratif)` | **240,0** `(illustratif)` |
| **2** | **C1. Jumeau spectral CPU (`Activation-Twin`) & test du morphisme synthétique $\to$ ~8B** | 5 `(illustratif)` | 4 `(illustratif)` | 5 `(illustratif)` | 4 `(illustratif)` | 2 `(illustratif)` | **200,0** `(illustratif)` |
| **3** | **C2. Synthèse neuro-symbolique d'$e$-processus à nul par acte sans plafond de banque finie (Axe 1)** | 5 `(illustratif)` | 3 `(illustratif)` | 5 `(illustratif)` | 5 `(illustratif)` | 2 `(illustratif)` | **187,5** `(illustratif)` |
| **4** | **C4. Invariants orthogonaux au style & mesure du coût géométrique d'évasion (Axe 2)** | 4 `(illustratif)` | 3 `(illustratif)` | 4 `(illustratif)` | 4 `(illustratif)` | 3 `(illustratif)` | **64,0** `(illustratif)` |
| **5** | **C5. Spectre résiduel inter-copies d'essaims à poids partagés & riposte à fuite bornée (Axe 3)** | 4 `(illustratif)` | 2 `(illustratif)` | 4 `(illustratif)` | 5 `(illustratif)` | 3 `(illustratif)` | **53,3** `(illustratif)` |
| *6* | *C6 (hors top 5). Campagne extensive d'audit humain multi-strates hors dommages plantés ciblés* | 4 `(illustratif)` | 2 `(illustratif)` | 4 `(illustratif)` | 2 `(illustratif)` | 5 `(illustratif)` | *12,8* `(illustratif)` |

**Sensibilité à la pondération** : La division linéaire par `coût` avantage fortement `coût = 1` (processeur pur). Si l'on amortit la pénalité de coût en $\text{coût}^{0{,}5}$ `(illustratif)`, les scores deviennent C1 = $282{,}8$, C2 = $265{,}2$, C3 = $240{,}0$, C4 = $110{,}9$, C5 = $92{,}4$ `(illustratifs)` : C1 et C2 passent devant C3, mais **le bloc amont {C1, C2, C3} reste strictement dominant** d'un facteur $> 2$ `(illustratif)` sur {C4, C5}. Si l'on élève `potentiel_de_découverte_majeure` au carré `(illustratif)`, C2 prend le premier rang ($937{,}5$ `(illustratif)`) et C5 dépasse C4 ($266{,}7$ contre $256{,}0$ `(illustratifs)`). L'enchaînement opérationnel robuste demeure C3 $\to$ C1 $\to$ C2 $\to$ {C4, C5}.

### 7.2 Cinq expériences décisives en inférence forte et ancrage matériel `[Livrables (b) & (d)]`

**Ancrage matériel commun `[Livrable (d)]`** : Pour respecter le budget modeste en cartes graphiques et les modèles ouverts autour de huit milliards de paramètres (`RAPPORTÉ`), toutes les épreuves boîte blanche utilisent deux modèles ouverts à poids distincts de cette classe : `Meta-Llama-3.1-8B-Instruct` (~8,0 milliards de paramètres `(illustratif)`) et `Qwen2.5-7B-Instruct` (~7,6 milliards de paramètres `(illustratif)`), exécutés en précision `bfloat16` sur une unique carte graphique de 48 Go de VRAM `(illustratif)` (ex. NVIDIA A6000 ou L40S), tandis que l'organisme $\mathcal{I}$ s'exécute sur un nœud processeur standard de 32 cœurs et 128 Go de RAM `(illustratif)`.

---

#### Chantier 1 (C3) — Test d'étanchéité mémorielle sous anonymisation algébrique
- **Hypothèses exclusives** : Sur $N = 200$ `(illustratif)` mondes à lois plantées issus de théorèmes postérieurs à une coupure $\tau_0$, soit $\Delta_{\text{anon}}$ l'écart de taux de redécouverte (à $\text{FDR} \le 0{,}05$ `(illustratif)`) entre $\mathcal{I}$ guidé par modèle pré-entraîné et la recherche symbolique sans modèle pré-entraîné, après bijection aléatoire des symboles et rotation orthogonale $Q \in O(d)$.
  - `H_A` *(Artefact de mémorisation)* : $\Delta_{\text{anon}} < +10$ points de pourcentage `(illustratif)`.
  - `H_B` *(Guidage structurel authentique)* : $\Delta_{\text{anon}} \ge +10$ points de pourcentage `(illustratif)` avec borne inférieure de l'intervalle de confiance à $95\%$ `(illustratif)` strictement positive.
- **Métrique et seuil** : Différence appariée de proportions de lois exactes retrouvées (test de McNemar bilatéral, seuil décisionnel $\Delta^* = +10\%$ `(illustratif)`).
- **Contrôle négatif** : Lois purement aléatoires non structurées où les deux bras doivent plafonner au niveau nominal $\text{FDR} \le 0{,}05$ `(illustratif)`.
- **Réfutation** : Une borne supérieure d'IC $< +10\%$ `(illustratif)` (ou $\hat{\Delta}_{\text{anon}} < +10\%$ à l'arrêt séquentiel préenregistré) réfute `H_B` et interdit d'utiliser le modèle pré-entraîné autrement que comme parseur syntaxique ; une borne inférieure $\ge +10\%$ `(illustratif)` réfute `H_A`.
- **Coût matériel estimé** : Processeur seul + inférence locale légère de tri : $40$ heures-cœur CPU et $2$ heures-GPU `(illustratifs)` ($\approx 5$ à $10$ € équivalent infonuagique `(illustratif)`).

#### Chantier 2 (C1) — Test du morphisme de transfert CPU $\to$ boîte blanche ~8B (`Activation-Twin`)
- **Hypothèses exclusives** : Sur un banc de développement de $40$ `(illustratif)` détecteurs candidats diversifiés évalués à la fois sur le jumeau spectral CPU (calibré uniquement sur tenseurs honnêtes $\mathcal{D}_{\text{dev}}^{\text{CPU}}$) et sur perturbations locales de développement dans `Llama-3.1-8B-Instruct` :
  - `H_A` *(Transfert prédictif exploitable)* : La corrélation des rangs de Spearman entre $e$-puissances CPU et GPU vérifie $\rho_S \ge 0{,}50$ `(illustratif)` **et** le rapport de vraisemblance diagnostique du filtre CPU atteint $\Lambda_1 \ge 4{,}0$ `(illustratif)`.
  - `H_B` *(Rupture géométrique synthétique-réel)* : $\rho_S < 0{,}50$ `(illustratif)` **ou** $\Lambda_1 < 4{,}0$ `(illustratif)`.
- **Métrique et seuil** : $\hat{\rho}_S$ et $\hat{\Lambda}_1 = \widehat{\text{TPR}}_1 / \widehat{\text{FPR}}_1$ au quartile supérieur sur CPU, seuils $0{,}50$ et $4{,}0$ `(illustratifs)`.
- **Contrôle négatif** : Évaluation des mêmes $40$ `(illustratif)` candidats sur les mondes synthétiques isotropes historiques et sur tenseurs aux couches permutées.
- **Réfutation** : $\hat{\rho}_S < 0{,}50$ ou $\hat{\Lambda}_1 < 4{,}0$ `(illustratifs)` réfute `H_A` et disqualifie les mondes synthétiques au profit du calcul direct sur activations mises en cache ; franchir simultanément les deux seuils avec significativité à $95\%$ `(illustratif)` réfute `H_B`.
- **Coût matériel estimé** : Extraction unique de $500$ `(illustratif)` trajectoires honnêtes sur `Llama-3.1-8B-Instruct` et `Qwen2.5-7B-Instruct` ($8$ heures-GPU `(illustratif)`) + $80$ heures-cœur CPU `(illustratif)` ($\approx 15$ à $25$ € `(illustratif)`).

#### Chantier 3 (C2) — Duel entre $e$-processus à nul par acte synthétisé par $\mathcal{I}$ et étalonnage sur référence honnête finie (Axe 1)
- **Hypothèses exclusives** : Sur des chaînes de $T = 80$ `(illustratif)` actions d'analyse statistique avec une référence honnête fixe volontairement restreinte à $N_0 = 30$ `(illustratif)` trajectoires ($T > N_0$, régime de plafonnement `RAPPORTÉ`), lors d'une lecture unique sur une famille inédite de dérives méthodologiques réparties :
  - `H_A` *(Supériorité valide du nul par acte)* : Le meilleur $e$-processus certifié par $\mathcal{I}$ respecte $\widehat{\text{FPR}}_{1:T} \le 0{,}05$ `(illustratif)` (non rejeté au test binomial unilatéral à $95\%$ sur $200$ `(illustratif)` trajectoires honnêtes nouvelles) **et** atteint $\widehat{\text{TPR}}_{1:T} \ge 0{,}70$ `(illustratif)` avec un gain $\ge +20$ points `(illustratif)` sur la sonde par acte cumulée sur la référence fixe $N_0$.
  - `H_B` *(Dérive de calibration ou perte de puissance)* : Violation empirique du nul ($\widehat{\text{FPR}}_{1:T}$ significativement $> 0{,}05$ `(illustratif)`) **ou** $\widehat{\text{TPR}}_{1:T} < 0{,}70$ **ou** gain $< +20$ points `(illustratifs)`.
- **Métrique et seuil** : Couple $(\widehat{\text{FPR}}_{1:T}, \widehat{\text{TPR}}_{1:T})$ à horizon $T=80$ `(illustratif)` au seuil de Ville $E_t \ge 20$ ($\alpha = 0{,}05$ `(illustratif)`).
- **Contrôle négatif** : Trajectoires honnêtes subissant à $t = 40$ `(illustratif)` une réorientation légitime de protocole statistique après échec d'un test d'hypothèse intermédiaire.
- **Réfutation** : Tout excès significatif de fausses alertes sur ce contrôle négatif ou gain $< +20$ points `(illustratif)` réfute `H_A` ; la satisfaction conjointe des deux critères sur les deux modèles ~8B réfute `H_B`.
- **Coût matériel estimé** : $120$ heures-cœur CPU d'idéation/preuve + $14$ heures-GPU `(illustratifs)` pour la lecture unique ($\approx 30$ € `(illustratif)`).

#### Chantier 4 (C4) — Coût d'évasion géométrique sous projection orthogonale au style face à un moniteur génératif (Axe 2)
- **Hypothèses exclusives** : Face à des variations stylistiques et rhétoriques qui dégradent d'au moins $25$ points `(illustratif)` la détection d'un juge génératif ~8B :
  - `H_A` *(Découplage style-anomalie et coût d'évasion élevé)* : L'invariant projeté orthogonalement à la variété stylistique honnête (issu de $\mathcal{I}$) maintient $\widehat{\text{TPR}} \ge 0{,}75$ à $\widehat{\text{FPR}} \le 0{,}05$ `(illustratifs)` en lecture unique, et dans un bras d'évaluation dédié où la sonde est exposée à l'optimiseur (`RAPPORTÉ`), abaisser la sonde sous le seuil réduit le score objectif d'exécution de la tâche d'au moins $30\%$ `(illustratif)`.
  - `H_B` *(Confusion sous-spatiale ou évasion à faible coût)* : $\widehat{\text{TPR}} < 0{,}75$ à $\widehat{\text{FPR}} \le 0{,}05$ `(illustratif)`, **ou** l'optimisation dans le bras déclaré contourne la sonde avec moins de $30\%$ `(illustratif)` de perte d'utilité sur la tâche.
- **Métrique et seuil** : $\widehat{\text{TPR}}$ à $\widehat{\text{FPR}} = 0{,}05$ `(illustratif)` et chute relative de qualité vérifiée par tests objectifs de la tâche (seuil $30\%$ `(illustratif)`).
- **Contrôle négatif** : Textes strictement honnêtes rédigés sur consigne explicite d'argumentation rhétorique vigoureuse (« avocat du diable »).
- **Réfutation** : Un effondrement de $\widehat{\text{TPR}}$ après projection orthogonale ou une perte d'utilité $< 30\%$ `(illustratif)` dans le bras déclaré réfute `H_A` ; le maintien des deux seuils réfute `H_B`.
- **Coût matériel estimé** : $60$ heures-cœur CPU + $24$ heures-GPU `(illustratifs)` incluant le juge génératif et le bras d'évaluation ($\approx 45$ € `(illustratif)`).

#### Chantier 5 (C5) — Séparabilité spectrale de la coordination implicite sous poids partagés et fuite de riposte (Axe 3)
- **Hypothèses exclusives** : Pour $M = 5$ `(illustratif)` copies à poids partagés soumises à diversification d'invites et à une politique de riposte à seuil randomisé :
  - `H_A` *(Détection résiduelle à fuite bornée)* : La statistique spectrale résiduelle inter-copies proposée par $\mathcal{I}$ atteint $\widehat{\text{TPR}} \ge 0{,}65$ à $\widehat{\text{FPR}} \le 0{,}05$ `(illustratifs)` en lecture unique sur anomalies distribuées, tout en bornant l'information mutuelle empirique entre l'action d'une copie et la décision de riposte à $\hat{I} \le 0{,}10$ bit/épisode `(illustratif)`.
  - `H_B` *(Indiscernabilité sous poids partagés ou compromis riposte-puissance défavorable)* : $\widehat{\text{TPR}} < 0{,}65$ à $\widehat{\text{FPR}} \le 0{,}05$ `(illustratif)` lorsque $\hat{I} \le 0{,}10$ bit/épisode `(illustratif)`.
- **Métrique et seuil** : $\widehat{\text{TPR}}$ à $\widehat{\text{FPR}} \le 0{,}05$ `(illustratif)` et borne supérieure d'information mutuelle par estimateur plug-in régularisé ($\le 0{,}10$ bit `(illustratif)`).
- **Contrôle négatif** : $M = 5$ `(illustratif)` copies honnêtes du même modèle ~8B tombant indépendamment dans le même biais méthodologique naïf présent dans les poids pré-entraînés.
- **Réfutation** : Un taux de fausses alertes $> 0{,}05$ `(illustratif)` sur ces erreurs honnêtes corrélées ou $\widehat{\text{TPR}} < 0{,}65$ `(illustratif)` réfute `H_A` ; le respect simultané des trois bornes réfute `H_B`.
- **Coût matériel estimé** : $80$ heures-cœur CPU + $30$ heures-GPU `(illustratifs)` pour l'exécution quintuplée de modèles ~8B ($\approx 55$ € `(illustratif)`).

---

### 7.3 Ce qui reste hors de portée

- **Impossibilité de borner inconditionnellement la stéganographie computationnelle non linéaire** : si un modèle dissimulait un état latent sous une transformation pseudo-aléatoire interne décorrélée des moments spectraux d'ordre bas, les sondes polynomiales échoueraient (`VÉRIFIÉ` sous hypothèses cryptographiques standards) ; je ne sais pas si un transformeur de huit milliards de paramètres peut exécuter un tel codage en une passe avant sur tâche floue sans dégrader visiblement sa qualité.
- **Extrapolation sans ré-étalonnage aux modèles d'échelle très supérieure** : les invariants géométriques calibrés autour de huit milliards de paramètres (`RAPPORTÉ`) ne garantissent aucune validité directe à plusieurs centaines de milliards de paramètres, hors budget matériel actuel.
- **Strates aveugles pour l'oracle exogène ($p_s \approx 0$)** : là où même un audit expert lent échoue à identifier des dommages plantés (`RAPPORTÉ`), ni le plancher d'audit aléatoire ni l'organisme d'idéation ne peuvent certifier une absence de défaillance sémantique.

FIN-DE-CELLULE