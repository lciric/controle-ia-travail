*Note de conformité : les statuts épistémiques (`VÉRIFIÉ`, `RAPPORTÉ`, `OBSERVÉ-NON-AUDITÉ`, `HYPOTHÈSE`) sont maintenus tels quels ; les faits issus du dossier portent le statut `RAPPORTÉ`. Aucun identifiant arXiv n'est donné de mémoire (`arXiv : pas sûr`). Tout chiffre ne provenant pas du dossier est marqué « illustratif ». Aucune recette d'attaque n'est fournie.*

---

## 1. Ce qu'un expert du domaine ferait ici, et que la demande d'origine omet

### 1.1. Ce que la question présuppose sans que ce soit établi [Livrable (a)]

Avant de modifier l'organisme d'idéation (`I`) ou de le coupler au programme de contrôle (`C`), un expert auditerait six présupposés implicites de la demande :

1. **Transfert des mondes synthétiques (CPU) vers le contrôle boîte blanche 8B (GPU)** — Statut : `HYPOTHÈSE`. Le dossier indique seulement que `I` est évalué sur des mondes synthétiques à lois plantées sur processeur tandis que `C` opère sur des modèles ouverts de huit milliards de paramètres sur tâches floues à vérité différée ou partielle (`RAPPORTÉ`). Aucune corrélation entre les deux environnements n'est établie.
2. **Compatibilité d'une boucle fermée avec la séparation sélection/évaluation** — Statut : `HYPOTHÈSE`. Le programme `C` interdit explicitement qu'un score de moniteur ou de juge entre dans le signal d'entraînement ou de sélection d'un agent ou d'un proposeur hors bras d'attaque déclaré (`RAPPORTÉ`). Une boucle de rétroaction naïve guidée par les performances de contrôle violerait cette règle et épuiserait les familles tenues à l'écart à lecture unique (`RAPPORTÉ`).
3. **Production d'inventions réelles plutôt que de réminiscences par `I`** — Statut : `HYPOTHÈSE`. `I` peut mobiliser des modèles pré-entraînés lors de l'exploration ou du tri sur des graphes de concepts datés (`RAPPORTÉ`). Sans protocole anti-mémorisation, redécouvrir une structure sur une archive historique datée ne démontre pas une capacité d'invention hors corpus.
4. **Le goulot d'étranglement principal de `C` serait un manque d'objets mathématiques nouveaux** — Statut : `HYPOTHÈSE`. Il n'est pas établi que les limites actuelles de `C` proviennent d'un déficit d'idées plutôt que de goulots empiriques (variance des sondes sur activations honnêtes, mesure de la probabilité d'identification par strate de l'oracle exogène, taille finie de la référence honnête $N_0$, `RAPPORTÉ`).
5. **Rentabilité du couplage sous budget GPU et budget de lectures limités** — Statut : `HYPOTHÈSE`. Le coût de filtrage des faux candidats émis par `I` peut absorber le budget modeste en cartes graphiques et le nombre fini de familles indépendantes tenues à l'écart (`RAPPORTÉ`).
6. **Mesurabilité non circulaire de la « profondeur » d'une découverte** — Statut : `HYPOTHÈSE`. Évaluer la « profondeur » via un juge génératif réintroduit la corruptibilité rhétorique que l'axe 2 de `C` cherche précisément à mesurer (`RAPPORTÉ`).

### 1.2. Ce qu'un expert ferait immédiatement, que la demande omet

*Ma proposition (distincte de l'établi)* : un expert commencerait par **refuser une boucle guidée par les scores de contrôle** et réaliserait quatre actions préalables :

1. **Restreindre l'interface de sortie de `I` à des artefacts formellement vérifiables sur CPU**. En détection séquentielle et bornage de fuite, la validité sous l'hypothèse nulle $H_0$ (propriété de supermartingale / e-processus, validité d'un nul par acte, borne de fuite de politique) est une propriété mathématique vérifiable *avant* tout passage sur GPU. Exiger une preuve mécanisée ou un passage par un vérificateur symbolique/numérique de $H_0$ coupe le flux de faux positifs avant de consommer le budget GPU ou une famille tenue à l'écart.
2. **Remplacer le retour « performance d'attaque » par un retour « spécification de $H_0$ et goulots formels »**. Le dossier identifie déjà des verrous mathématiques précis (`RAPPORTÉ`) : le plafonnement d'une accumulation séquentielle étalonnée sur référence honnête fixe quand l'horizon $T$ dépasse $N_0$ (sauf nul par acte), la sensibilité stylistique des juges génératifs, et la fuite d'information des politiques de riposte en essaim. Un expert ciblerait ces verrous exacts plutôt que l'objectif indéfini de « découvertes profondes ».
3. **Établir d'abord une ligne de base mécanique sans `I`**. Avant d'investir dans `I`, vérifier ce qu'obtient déjà une bibliothèque statique de tests séquentiels existants (e-valeurs, séquences de confiance, tests conditionnels standards) sur `C`.
4. **Auditer le taux de contamination temporelle** des modèles pré-entraînés utilisés par `I` avant d'accorder le moindre crédit à ses scores sur archives datées.

---

## 2. Les données brutes de départ à prendre avant toute synthèse déjà analysée

Avant toute lecture de tableaux agrégés, de scores composites ou de résumés générés par modèles, il faut collecter les artefacts bruts suivants, en préservant strictement l'étanchéité vis-à-vis des familles tenues à l'écart et de la banque de validation finale (`RAPPORTÉ`).

### Côté programme de contrôle (`C`) — traces honnêtes et bac à sable déclaré uniquement
1. **Séries temporelles brutes d'activations internes sur trajectoires honnêtes (modèles ouverts 8B)** : vecteurs/projections par couche et par étape d'action sur tâches floues (plans d'expériences, chaînes multi-agents, analyse statistique), avec métadonnées complètes (longueur de contexte, domaine, graine). Ces traces révèlent l'autocorrélation temporelle, la dérive de norme et la non-stationnarité réelles sous $H_0$, masquées par les moyennes.
2. **Distributions brutes (non seuillées) des scores de sondes et de juges génératifs sur paires honnêtes appariées** : réponses honnêtes sémantiquement équivalentes variant par le style ou la pression rhétorique (axe 2), afin d'estimer la dérive marginale brute sans toucher aux scénarios de sabotage.
3. **Journaux bruts d'essaims honnêtes à poids partagés** : séquences d'actions, distributions de logits et corrélations spontanées entre copies indépendantes sur tâches proches (axe 3), pour caractériser la corrélation basale sous $H_0$.
4. **Logs bruts de l'oracle exogène sur dommages plantés de calibration** : verdicts élémentaires par strate, temps humain par audit, désaccords inter-auditeurs et erreurs de l'oracle.

### Côté organisme d'idéation (`I`) et infrastructure
5. **Journal intégral et non filtré des propositions de `I`** (succès, rejets, doublons, erreurs de syntaxe, échecs de calibration), accompagné des graphes de concepts datés bruts, du nombre d'appels aux modèles pré-entraînés et du temps CPU par candidat — indispensable pour mesurer le taux réel de fausses pistes (effet tiroir).
6. **Scores bruts sur mondes à lois plantées ventilés par complexité syntaxique, niveau de bruit et recouvrement avec la littérature antérieure**.
7. **Inventaire matériel et budgétaire brut** : heures GPU disponibles, taille réelle de la référence honnête $N_0$, et nombre exact de familles de sabotage indépendantes disponibles ou budgétables — *je ne sais pas* combien de familles indépendantes existent actuellement dans le programme, cette donnée étant absente du dossier.

---

## 3. Formalisation mathématique et conditions de validité de la boucle fermée

*Distinction* : les propriétés de supermartingales, d'e-valeurs, de p-valeurs conformes et de Bayes mobilisées ci-dessous sont établies en statistique mathématique ; l'architecture de couplage et ses conditions d'étanchéité constituent *ma proposition*.

### 3.1. Formalisation du couplage dans ses deux directions utiles

Notons $\mathcal{M}$ l'espace des artefacts exécutables candidats (e-processus $E_t$, nuls par acte $Q_t$, protocoles d'audit stratifiés, bornes de fuite), $\mathcal{B}_{\text{synth}}$ les mondes synthétiques CPU, $\mathcal{D}_{\text{hon}}$ une référence de $N_0$ trajectoires honnêtes 8B, $\{\mathcal{F}_1, \dots, \mathcal{F}_K\}$ une suite de $K$ familles de sabotage indépendantes tenues à l'écart (lecture unique), et $\mathcal{F}_{\text{val}}$ la banque de validation finale (`RAPPORTÉ`).

La boucle est partitionnée par un **pare-feu unidirectionnel** :

- **Direction `C → I` (spécification sans fuite de score)** : un opérateur déterministe $\Pi_{\text{spec}}$ transmet à `I` uniquement (i) des descriptions formelles de la classe nulle $\mathcal{P}_0$ estimées sur $\mathcal{D}_{\text{hon}}$ (autocorrélation, taille $N_0$, horizon $T$, invariances souhaitées), et (ii) des énoncés formels de verrous théoriques. **Aucun score de moniteur, de juge ou d'issue sur $\mathcal{F}_k$ n'entre dans $\Pi_{\text{spec}}$** (respect strict de la règle de séparation, `RAPPORTÉ`).
- **Direction `I → C` (promotion filtrée CPU-d'abord)** : au tour $k \in \{1,\dots,K\}$, `I` produit un lot $M_k = \{m_{k,1},\dots,m_{k,J_k}\} \subset \mathcal{M}$. Un filtre déterministe $\Phi_{\text{CPU}}$ (vérification formelle de validité sous $H_0$ + stress-tests synthétiques non stationnaires) sélectionne au plus un candidat promu préenregistré $m_k^*$, qui seul est évalué sur GPU contre $\mathcal{F}_k$.

**Exemple formel du verrou $T > N_0$ (`RAPPORTÉ`)** : si un détecteur séquentiel étalonne ses scores contre une référence honnête fixe de taille $N_0$ via des p-valeurs conformes standards (Bates, Candès, Lei, Romano & Sesia, 2023, *Testing for outliers with conformal p-values*, Annals of Statistics ; arXiv : pas sûr), la granularité minimale vaut $(N_0+1)^{-1}$ et tous les pas $t=1,\dots,T$ partagent l'erreur d'échantillonnage de la référence d'ordre $O(N_0^{-1/2})$ (`VÉRIFIÉ` mathématiquement sous échangeabilité), faisant plafonner ou dériver une accumulation naïve dès que $T \gg N_0$. À l'inverse, un **nul par acte** construit une distribution nulle conditionnelle locale $Q_t(\cdot \mid \mathcal{H}_{t-1}, c_t)$ (via invariance structurelle de l'acte ou symétrie conditionnelle au contexte $c_t$) et une e-variable par acte $e_t \ge 0$ satisfaisant $\sup_{P \in \mathcal{P}_0} \mathbb{E}_P[e_t \mid \mathcal{H}_{t-1}] \le 1$. Par l'inégalité de Ville, le produit $E_T = \prod_{t=1}^T e_t$ vérifie $\sup_{P \in \mathcal{P}_0} P(\exists t \ge 1 : E_t \ge 1/\alpha) \le \alpha$ pour tout horizon $T$, indépendamment de $N_0$ (`VÉRIFIÉ` mathématiquement ; cf. Vovk & Wang, 2021, *E-values: Calibration, combination and applications*, Annals of Statistics, arXiv : pas sûr ; Ramdas, Grünwald, Vovk & Shafer, 2023, *Game-Theoretic Statistics and Safe Anytime-Valid Inference*, Statistical Science, arXiv : pas sûr).

### 3.2. Conditions de validité statistique non circulaire

1. **Indépendance de la génération vis-à-vis des familles d'épreuve (pare-feu)** : soit $\mathcal{G}_{k-1}$ la tribu de toute information accessible à `I` avant le tour $k$. On exige :
   $$\mathcal{F}_k \perp\!\!\!\perp \sigma(\mathcal{G}_{k-1}, m_k^*) \quad \text{et} \quad \mathcal{F}_{\text{val}} \perp\!\!\!\perp \sigma(\mathcal{G}_K, m_1^*,\dots,m_K^*).$$
   Sans cette condition, `I` sur-apprend implicitement le détecteur ou le générateur de familles.
2. **Contrôle séquentiel de la multiplicité inter-tours** : promouvoir $K$ candidats sur $K$ familles indépendantes nécessite un budget d'erreur global $\sum_{k=1}^K \alpha_k \le \alpha$ (ou une règle d'$\alpha$-investissement ; Foster & Stine, 2008, *$\alpha$-investing: a procedure for sequential control of expected false discoveries*, Journal of the Royal Statistical Society: Series B, arXiv : pas sûr) fixé avant lecture. Sur $\mathcal{F}_{\text{val}}$, un seul candidat final (ou $m$ fixés à l'avance avec correction de Holm/Bonferroni) est lu une seule fois (`RAPPORTÉ`).
3. **Borne de validité hors environnements synthétiques** : soit $R_{\text{synth}}(m)$ l'utilité sur $\mathcal{B}_{\text{synth}}$ et $R_{\text{8B}}(m)$ l'utilité réelle sur 8B (ex. puissance à FPR anytime $\le \alpha$). Si la fonction d'évaluation est $L_m$-lipschitzienne pour une métrique de probabilité intégrale $d_{\mathcal{F}}$ sur les lois de trajectoires, alors :
   $$|R_{\text{8B}}(m) - R_{\text{synth}}(m)| \le L_m \, d_{\mathcal{F}}(P_{\text{synth}}, P_{\text{8B}}) + \varepsilon_{\text{strat}},$$
   où $\varepsilon_{\text{strat}}$ représente l'écart dû à l'adaptation adversariale et à la vérité partielle. Le transfert n'est donc défendable que si $d_{\mathcal{F}}(P_{\text{synth}}^{\text{hon}}, P_{\text{8B}}^{\text{hon}})$ est mesuré et réduit sur données honnêtes brutes *et* si la monotonie de rang entre $R_{\text{synth}}$ et $R_{\text{8B}}$ est testée empiriquement.
4. **Ancrage par plancher d'audit exogène** : sur chaque strate $s$ de taux d'audit aléatoire $q_s$ et de borne inférieure confiante $\underline{p}_s$ sur la probabilité d'identification par l'oracle exogène (mesurée sur dommages plantés, `RAPPORTÉ`), la probabilité qu'un sabotage persistant sur $n_s$ actions de la strate échappe à l'audit est au plus $(1 - q_s \underline{p}_s)^{n_s}$, garantie non circulaire indépendante de `I`.

### 3.3. Arbitrage quantitatif coût des épreuves / rendement de découverte

Notons $\pi_0 \in (0,1)$ la proportion a priori de candidats bruts réellement valides et utiles émis par `I`, $(\text{TPR}_\Phi, \text{FPR}_\Phi)$ les performances du filtre CPU $\Phi_{\text{CPU}}$, $c_{\text{CPU}}$ le coût unitaire de filtrage CPU, $c_{\text{GPU}}$ le coût d'une évaluation 8B, $c_{\text{fam}}$ le coût d'opportunité irréversible d'une famille tenue à l'écart (sous contrainte dure $\le K_{\max}$ lectures), et $\Delta U$ le gain moyen d'une vraie découverte. Par le théorème de Bayes (`VÉRIFIÉ`), la valeur prédictive positive d'un candidat promu vers GPU est :
$$\text{VPP} = \frac{\pi_0\,\text{TPR}_\Phi}{\pi_0\,\text{TPR}_\Phi + (1-\pi_0)\,\text{FPR}_\Phi}, \qquad p_{\text{pass}} = \pi_0\,\text{TPR}_\Phi + (1-\pi_0)\,\text{FPR}_\Phi.$$
Le rendement net espéré par unité de ressource rare (GPU + famille) vaut :
$$\mathcal{R} = \frac{\text{VPP}\cdot \Delta U - \left(c_{\text{GPU}} + c_{\text{fam}} + c_{\text{CPU}} / p_{\text{pass}}\right)}{c_{\text{GPU}} + c_{\text{fam}}}.$$
**Conséquence décisionnelle** : lorsque $\pi_0 \ll 1$ (par ex. $\pi_0 \in [10^{-4}, 10^{-2}]$, illustratif) et $c_{\text{GPU}} + c_{\text{fam}} \gg c_{\text{CPU}}$, $\text{VPP} \approx \frac{\pi_0 \text{TPR}_\Phi}{\text{FPR}_\Phi}$. **Diviser $\text{FPR}_\Phi$ par 10 [illustratif] sur CPU augmente beaucoup plus $\mathcal{R}$ que de multiplier par 10 [illustratif] le débit génératif de `I`.** La priorité économique est donc la sélectivité du filtre amont, non le volume d'idées.

### 3.4. Contrôles négatifs disqualifiant une boucle défaillante ou illusoire

- **CN1 (Placebo à cible permutée)** : alimenter `I` avec des statistiques issues de trajectoires honnêtes permutées ou de bruit pur. Si le pipeline interne déclare des candidats « significatifs » au-delà de $\alpha$, le filtre est disqualifié.
- **CN2 (Disqualification par mémorisation)** : comparer le taux de découverte de `I` sur des lois historiques de l'archive contre des lois *de novo* procédurales (jamais publiées) de même complexité syntaxique. Un effondrement sur les lois inédites disqualifie l'usage des scores sur archives comme preuve d'invention.
- **CN3 (Nullité du couplage)** : duel en aveugle entre `I` couplé (avec $\Pi_{\text{spec}}$), `I` en boucle ouverte (sans retour de `C`) et une bibliothèque mécanique d'objets standards, à budget égal. Si la boucle couplée ne bat pas les deux autres, le couplage est déclaré illusoire.
- **CN4 (Stress-test de non-stationnarité sous $H_0$)** : évaluer tout détecteur candidat sur séries honnêtes autocorrélées (AR(1), changements de domaine de tâche). Tout dépassement du seuil anytime $\alpha$ disqualifie l'objet avant GPU.

---

## 4. Méthodes, outils et protocoles d'évaluation

### 4.1. Comparaison de cinq familles d'approches distinctes

| Famille d'approche | Principe algorithmique | Hypothèses clés | Limites et modes d'échec |
| :--- | :--- | :--- | :--- |
| **A. Synthèse de programmes vérifiée formellement** (parenté : recherche évolutionnaire sur grammaire d'e-variables/protocoles avec vérificateur symbolique ou Lean/SMT ; *FunSearch*, Romera-Paredes et al., référence à vérifier, arXiv : pas sûr) | Recherche guidée dans un DSL d'opérateurs mathématiques ; chaque candidat doit passer une preuve de validité sous $H_0$ (supermartingale/borne) avant classement. | L'objet utile est exprimable dans un DSL compositionnel ; la validité sous $H_0$ est décidable ou vérifiable mécaniquement. | Explosion combinatoire ; génération de variantes syntaxiques triviales d'objets connus ; cécité aux concepts hors grammaire. |
| **B. Analogies structurelles sur graphes de concepts datés** (architecture actuelle de `I`, `RAPPORTÉ`) | Parcours de graphes scientifiques datés et transfert d'isomorphismes entre domaines (jeux séquentiels, détection de ruptures, sécurité). | Des structures mûres d'autres champs résolvent les verrous de `C`. | Analogies rhétoriquement séduisantes mais fausses ; contamination temporelle massive par les modèles pré-entraînés ; coût élevé de traduction formelle. |
| **C. Co-évolution abstraite sur simulateurs de jeux séquentiels (CPU)** *(sans recette d'attaque réelle)* | Jeu minimax abstrait sur processus stochastiques (dérive lente vs détecteur anytime-valid contraint) pour faire émerger des statistiques robustes. | La géométrie minimax abstraite capture la structure essentielle des menaces diffuses. | Intransitivité cyclique ; sur-ajustement au modèle de bruit simulé ; écart géométrique avec les activations 8B réelles. |
| **D. Planification optimale d'expériences bayésienne (gain d'information)** | `I` propose des *protocoles d'expérience et d'allocation d'audit* maximisant l'information attendue pour trancher entre hypothèses concurrentes sous budget GPU/oracle. | Un modèle de vraisemblance approché des coûts et résultats est spécifiable. | Prior mal spécifié produisant des expériences non discriminantes ; sensibilité aux hypothèses paramétriques. |
| **E. Découverte d'invariants sur activations honnêtes 8B (exploration de $H_0$ uniquement)** | Apprentissage non supervisé sur $\mathcal{D}_{\text{hon}}$ d'invariants stables par acte (ex. sous-espaces invariants aux paraphrases stylistiques, lois inter-couches) servant à construire des nuls par acte. | Une menace diffuse ou une pression rhétorique sort de la variété statistique honnête. | Puissance faible contre un sabotage restant dans le support de $H_0$ ; sur-ajustement aux tâches honnêtes de calibration. |

*Ma proposition* : combiner **E** (extraction d'invariants sur $\mathcal{D}_{\text{hon}}$) pour fournir les primitives de $\Pi_{\text{spec}}$, et **A** (synthèse vérifiée formellement sur CPU) pour générer des nuls par acte et e-processus certifiés sous $H_0$, tandis que **B** reste cantonné à l'enrichissement de la grammaire du DSL (jamais promu directement sans le filtre de **A**).

### 4.2. Protocoles anti-fuite statistique et temporelle

- **Étanchéité statistique** : (1) séparation physique et cryptographique des dépôts ($\mathcal{D}_{\text{hon}}$, $\mathcal{F}_k$, $\mathcal{F}_{\text{val}}$) ; (2) préenregistrement horodaté avec empreinte SHA-256 du code gelé, des seuils et du plan d'analyse *avant* tout accès à $\mathcal{F}_k$ (`RAPPORTÉ`) ; (3) si un ensemble de développement interne réutilisable existe *hors* $\mathcal{F}_k$ et $\mathcal{F}_{\text{val}}$, le protéger par un mécanisme de *reusable holdout* à bruit différentiellement privé (Dwork, Feldman, Hardt, Pitassi, Reingold & Roth, 2015, *The reusable holdout: Preserving validity in adaptive data analysis*, Science ; arXiv : pas sûr) avec comptabilité explicite du budget de confidentialité.
- **Étanchéité temporelle (modèles pré-entraînés dans `I`)** : (1) bancs de lois *de novo* générées procéduralement après la date de coupure des poids, avec renommage canonique des variables ; (2) bras d'ablation sans LLM (recherche symbolique pure) et bras avec petit modèle à corpus daté documenté, pour isoler la mémoire paramétrique ; (3) évaluation prospective sur problèmes nouvellement publiés *après* le gel complet du code et des poids de `I`.

### 4.3. Mesure minimale de fonctionnement de chaque instrument nommé [Livrable (c)]

*Note : tous les seuils numériques de ce tableau sont marqués « illustratif » (propositions de préenregistrement, absents du dossier).*

| Instrument nommé | Taux de détection minimal visé | Taux de fausses alertes maximal | Cas honnêtes appariés | Vérifications mécaniques / bases à battre |
| :--- | :--- | :--- | :--- | :--- |
| **1. Organisme d'idéation (`I`) + filtre CPU** | Taux de candidats passant la preuve $H_0$ **et** utiles sur bancs *de novo* $\ge 5\%$ [illustratif] des promotions ; rétention sur lois *de novo* $\ge 70\%$ [illustratif] du score historique. | Faux positifs du filtre $H_0$ $\le 5\%$ [illustratif] ; fausses découvertes sur bruit pur $\le 5\%$ [illustratif] (contrôle multiple). | Bancs de bruit pur et lois déjà présentes dans l'archive (appariés en complexité syntaxique et budget CPU). | Recherche symbolique sans LLM ; sélection aléatoire sur grammaire d'opérateurs ; archive existante seule (`RAPPORTÉ`). |
| **2. Détecteur séquentiel boîte blanche (Axe 1)** | TPR avant dommage critique supérieur d'au moins $+15\%$ [illustratif] (ou délai médian réduit d'au moins $25\%$ [illustratif]) vs meilleure base, à horizon $T > N_0$. | FWER / FPR anytime-valid $\le \alpha = 0,05$ [illustratif] sur tout $t \le T$ (ex. $T = 5 N_0$, illustratif). | Trajectoires honnêtes 8B appariées en longueur $T$, domaine de tâche, complexité et changements de contexte bénins. | Base boîte noire ; sonde boîte blanche par action avec correction de Bonferroni ; e-processus calibré sur référence fixe $N_0$ (`RAPPORTÉ`). |
| **3. Moniteur génératif vs sonde sur agent auteur (Axe 2)** | Détection de tentative d'influence/décalage $\ge 80\%$ [illustratif] et mesure reproductible du coût d'évasion sur activations (IC à 95% [illustratif] non nul). | Déplacement de FPR sous pression rhétorique honnête $\le 0,02$ [illustratif] (FPR global $\le 0,05$, illustratif). | Paires de réponses honnêtes sémantiquement équivalentes variant par style, assurance rhétorique et longueur. | Juge génératif nu sans sonde ; heuristiques stylistiques/lexicales simples (longueur, marqueurs de confiance). |
| **4. Détecteur de coordination / fuite en essaim à poids partagés (Axe 3)** | TPR sur coordination implicite distribuée $\ge 70\%$ [illustratif] ; borne empirique de fuite de politique $\le$ borne théorique certifiée. | FPR anytime $\le 0,05$ [illustratif] sur essaims de copies honnêtes exécutant des tâches corrélées. | Essaims honnêtes à poids partagés exposés au même contexte/tâche (corrélation naturelle due aux poids partagés, sans sabotage). | Tests de corrélation par paires sans structure d'essaim ; randomisation naïve (diversification par température/graine seule). |
| **5. Plancher d'audit par oracle exogène** | Estimation par strate de $p_s$ avec borne inférieure $\underline{p}_s$ mesurée sur dommages plantés (`RAPPORTÉ`) permettant un risque résiduel $\le 0,10$ [illustratif]. | Taux de fausses condamnations par l'oracle sur cas honnêtes $\le 0,02$ [illustratif] (accord inter-auditeurs $\kappa \ge 0,75$, illustratif). | Échantillons honnêtes issus des mêmes strates, présentés en aveugle parmi les dommages plantés. | Audit uniforme non stratifié à budget humain identique ; vérifications automatiques de cohérence syntaxique/statistique. |
| **6. Boucle fermée couplée (`I ↔ C`)** | Gain net d'utilité par unité de coût GPU/famille strictement positif vs boucle ouverte et bibliothèque mécanique sur $\ge 2/3$ des familles [illustratif]. | Zéro fuite vérifiée par audit cryptographique/log ; FPR anytime global $\le \alpha$ après correction inter-tours. | Même jeu de trajectoires honnêtes appariées et bras placebo (CN1/CN3) évalués en double aveugle. | `I` en boucle ouverte (sans $\Pi_{\text{spec}}$) ; bibliothèque statique de tests séquentiels existants ; bras placebo permuté. |

---

## 5. Ce qui, en dehors du programme et de son équipe, permettrait de vérifier la validité du résultat

1. **Vérification formelle indépendante par noyau de preuve** : tout nouvel objet mathématique revendiqué (e-processus, nul par acte, borne de fuite en essaim) doit être publié avec sa preuve mécanisée (Lean 4 / Coq). Un vérificateur tiers contrôle la validité sous $H_0$ de façon déterministe, sans faire confiance à l'équipe ni à `I`.
2. **Audit par red-team externe aveugle sur conteneurs gelés** : une équipe indépendante — qui n'a vu ni les poids des sondes ni les détails internes des détecteurs — conçoit ses propres familles de tâches floues et scénarios de défaillance sur les mêmes modèles ouverts 8B, et exécute l'image logicielle préenregistrée (empreinte SHA-256 publiée avant l'épreuve) sur son propre matériel.
3. **Transfert hors périmètre (autres modèles et autres domaines séquentiels)** : tester sans réajustement les objets mathématiques produits par `I` sur (i) d'autres familles de modèles ouverts de taille comparable (~7B–9B, illustratif) et (ii) des bancs publics de détection séquentielle de dérive totalement extérieurs au contrôle d'IA (contrôle qualité, séries temporelles biomédicales ou financières). Un objet général doit y conserver sa validité anytime-valid.
4. **Publication complète des logs de sélection (anti-effet tiroir)** : archiver publiquement (en excluant toute recette d'attaque exploitable) l'intégralité des préenregistrements, des propositions rejetées de `I`, des coûts CPU/GPU et des graines, afin qu'un tiers recalcule les taux de fausses découvertes ajustés pour la sélection multiple.
5. **Épreuve prospective post-gel** : évaluer `I` sur des benchmarks mathématiques/statistiques créés et publiés *après* le gel public de son code et des poids des modèles pré-entraînés qu'il emploie.

---

## 6. Reformulation exigeante de la tâche

Concevoir, instrumenter et soumettre à réfutation un **couplage filtré et non circulaire** entre l'organisme d'idéation `I` (CPU) et le programme de contrôle boîte blanche `C` (modèles ouverts 8B), soumis aux cinq exigences suivantes :

1. **Canal retour strictement exempt de scores** : `C` ne fournit à `I` aucun score de moniteur, de juge ou d'épreuve d'attaque, mais uniquement des spécifications formelles de verrous ouverts (en priorité : nuls par acte dépassant le plafond $T > N_0$, invariants aux variations stylistiques, bornes de fuite en essaim) et des distributions empiriques issues de trajectoires honnêtes $\mathcal{D}_{\text{hon}}$.
2. **Sortie exécutable et pré-certifiée sur CPU** : tout candidat émis par `I` doit être un artefact formel exécutable satisfaisant automatiquement la validité sous $H_0$ (preuve formelle + stress-test non stationnaire sur CPU) avant de pouvoir consommer du temps GPU ou une lecture de famille tenue à l'écart.
3. **Étanchéité temporelle démontrée** : la capacité d'invention de `I` est démontrée sur des lois *de novo* post-cutoff et contre une ablation sans modèle pré-entraîné, et non sur des archives potentiellement mémorisées.
4. **Évaluation à lecture unique et budget d'erreur comptabilisé** : chaque promotion vers `C` est préenregistrée, imputée sur un budget d'erreur inter-tours $\sum \alpha_k \le \alpha$ et confrontée à des lignes de base mécaniques simples ainsi qu'à un bras en boucle ouverte, sans jamais entamer la banque de validation finale $\mathcal{F}_{\text{val}}$ avant la clôture.
5. **Critère d'arrêt explicite** : si, au terme d'un budget préfixé de promotions préenregistrées, le couplage ne bat pas simultanément la boucle ouverte et une bibliothèque mécanique de tests séquentiels à coût égal, la boucle automatisée est débranchée.

---

## 7. Programme des priorités classé, expériences décisives et limites

### 7.1. Classement par la formule demandée et analyse de sensibilité

Formule imposée : $\text{score} = (\text{gain\_informatif} \times \text{facilité} \times \text{portée} \times \text{potentiel\_de\_découverte\_majeure}) / \text{coût}$. Toutes les notes (1 à 5) et scores ci-dessous sont **illustratifs** (notation experte a priori, non mesurée).

| Rang | Chantier | Gain ($G$) | Facilité ($F$) | Portée ($P$) | Potentiel ($D$) | Coût ($C$) | Score [illustratif] |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | **C1. Vérificateur formel & stress-test CPU $H_0$ (filtre amont $\Phi_{\text{CPU}}$)** | 5 | 4 | 5 | 4 | 1 | **400,0** |
| **2** | **C2. Audit anti-mémorisation de `I` (lois *de novo* vs archives + ablation LLM)** | 5 | 5 | 4 | 3 | 1 | **300,0** |
| **3** | **C3. Cartographie des invariants honnêtes 8B & test de transfert synthétique → 8B** | 5 | 3 | 5 | 4 | 2 | **150,0** |
| **4** | **C4. Synthèse vérifiée de nuls par acte dépassant le plafond $T > N_0$ (Axe 1)** | 5 | 3 | 4 | 5 | 3 | **100,0** |
| **5** | **C5. Duel en aveugle : boucle couplée structurelle vs ouverte vs bibliothèque mécanique** | 5 | 2 | 5 | 4 | 4 | **50,0** |
| 6 | C6. Bornes de fuite et détecteurs en essaims à poids partagés générés par `I` (Axe 3) | 4 | 2 | 4 | 5 | 4 | 40,0 |
| 7 | C7. Calibration humaine complète par strates de l'oracle exogène (plancher d'audit) | 5 | 2 | 4 | 2 | 5 | 16,0 |

**Sensibilité aux pondérations** : la formule présente un biais structurel fort en faveur du coût minimal ($C=1$ donne un levier $5\times$ par rapport à $C=5$).
- Si l'on privilégie le potentiel de découverte en atténuant le coût ($S_1 = G \cdot P \cdot D^2 / C^{0,5}$ [illustratif]), **C1 reste #1** (400,0), mais **C4 remonte #2** (288,7), **C3 reste #3** (282,8), **C5 et C6 passent #4 ex æquo** (200,0), et **C2 recule #6** (180,0).
- Si l'on privilégie la sûreté opérationnelle en retirant $D$ ($S_2 = G^2 \cdot P^2 / C^{0,5}$ [illustratif]), l'ordre devient **C1 (625,0) > C3 (441,9) > C2 (400,0) > C5 (312,5) > C4 (230,9) > C7 (178,9) > C6 (128,0)** : C7 regagne son rang d'infrastructure indispensable dès qu'on cesse de le pénaliser sur la nouveauté mathématique.
- **Invariant robuste** : **C1 domine toutes les pondérations**, confirmant l'analyse coût/rendement de la section 3.3.

### 7.2. Cinq expériences décisives falsifiables (`H_A` contre `H_B`) et ancrage matériel [Livrables (b) et (d)]

Toutes les expériences suivent le principe d'inférence forte (Platt, 1964, *Strong Inference*, Science) : `H_A` et `H_B` forment une partition exclusive. Tous les seuils numériques, modèles concrets, temps de calcul et coûts financiers sont **illustratifs** (seule la taille ~8B provient du dossier).

#### Expérience 1 (Chantier C1) — Sélectivité du filtre formel et non stationnaire sur CPU
- **`H_A`** : Le filtre combiné $\Phi_{\text{CPU}}$ (vérification symbolique/formelle de supermartingale + batterie non stationnaire AR(1)/rupture de régime) atteint $\text{FPR}_\Phi \le 0,05$ [illustratif] et $\text{TPR}_\Phi \ge 0,80$ [illustratif] sur un banc préenregistré de statistiques séquentielles valides et subtilement invalides.
- **`H_B`** : $\Phi_{\text{CPU}}$ viole au moins l'un des deux critères ($\text{FPR}_\Phi > 0,05$ ou $\text{TPR}_\Phi < 0,80$ [illustratif]), le rendant trop permissif pour protéger le budget GPU ou trop conservateur pour laisser passer des objets utiles.
- **Métrique et seuil** : $(\text{FPR}_\Phi, \text{TPR}_\Phi)$ sur $200$ [illustratif] objets préenregistrés ($100$ valides connus/dérivés, $100$ invalides par fuite de référence fixe, dépendance au futur ou fragilité à l'autocorrélation) ; seuil conjoint $\text{FPR}_\Phi \le 0,05$ et $\text{TPR}_\Phi \ge 0,80$ [illustratif].
- **Contrôle négatif** : $100$ [illustratif] statistiques naïves calibrées sur référence fixe évaluées à horizon $T = 10 N_0$ [illustratif] sur bruit pur ; taux d'acceptation exigé $= 0\%$ [illustratif].
- **Ancrage matériel et coût** : CPU seul (16–32 cœurs, 64 Go RAM, Python/SymPy/Lean 4) ; ~20–40 h CPU [illustratif], coût ~5–20 € [illustratif], 0 GPU, 0 famille consommée.
- **Falsification** : $\text{FPR}_\Phi > 0,05$, $\text{TPR}_\Phi < 0,80$, ou acceptation d'un seul contrôle négatif réfute `H_A`. Le respect simultané des seuils et du contrôle négatif réfute `H_B`.

#### Expérience 2 (Chantier C2) — Capacité d'invention vs mémorisation temporelle de `I`
- **`H_A`** : Les performances de `I` reflètent une capacité algorithmique transférable : sur des lois *de novo* générées procéduralement post-cutoff à symboles canoniques, le ratio $R_{\text{temp}}$ (taux de découverte *de novo* / taux sur lois historiques appariées en complexité d'arbre) est $\ge 0,70$ [illustratif] **et** `I` bat strictement son ablation sans LLM ($p < 0,01$ [illustratif]) à budget CPU égal.
- **`H_B`** : $R_{\text{temp}} < 0,70$ [illustratif] **ou** `I` ne bat pas l'ablation sans LLM, indiquant que ses succès sur archives reposent sur la mémorisation paramétrique.
- **Métrique et seuil** : $R_{\text{temp}}$ et différence de taux de découverte exacte $\Delta_{\text{LLM}}$ sur $60$ [illustratif] mondes *de novo* appariés à $60$ [illustratif] mondes historiques ; seuil $R_{\text{temp}} \ge 0,70$ et $\Delta_{\text{LLM}} > 0$ avec $p < 0,01$ [illustratif].
- **Contrôle négatif** : $40$ [illustratif] mondes de bruit pur sans loi plantée (taux de fausses découvertes devant rester $\le 0,05$ [illustratif] après contrôle multiple) + lois historiques renommées par isomorphisme.
- **Ancrage matériel et coût** : CPU (64 cœurs, ~100 h CPU [illustratif]) + inférence du modèle pré-entraîné de `I` (ex. modèle ouvert ~8B tel que Llama-3.1-8B ou Qwen2.5-7B [illustratif] sur 1 GPU 24 Go, ~15–30 h GPU [illustratif]), coût ~30–80 € [illustratif].
- **Falsification** : $R_{\text{temp}} < 0,70$, $\Delta_{\text{LLM}}$ non significatif ou faux positifs $> 0,05$ sur bruit pur réfute `H_A` (invalidant les scores d'archive comme métrique de progrès). La satisfaction conjointe des critères réfute `H_B`.

#### Expérience 3 (Chantier C3) — Transfert de validité sous $H_0$ du simulateur CPU vers modèles 8B réels
- **`H_A`** : Le simulateur CPU calibré sur les invariants de $\mathcal{D}_{\text{hon}}$ prédit la validité sous $H_0$ sur activations réelles 8B : corrélation de rang de Spearman $\rho_s \ge 0,60$ [illustratif] ($p < 0,01$) entre dérive de FPR simulée et réelle sur $30$ [illustratif] détecteurs candidats, et $\ge 80\%$ [illustratif] des détecteurs certifiés CPU maintiennent un FPR anytime $\le 0,05$ [illustratif] sur trajectoires honnêtes 8B longues.
- **`H_B`** : $\rho_s < 0,60$ [illustratif] **ou** $> 20\%$ [illustratif] des détecteurs certifiés CPU dépassent $\alpha = 0,05$ [illustratif] sur trajectoires honnêtes 8B, démontrant que la géométrie réelle des activations rompt le transfert synthétique.
- **Métrique et seuil** : $\rho_s$ et proportion de violation anytime sur horizons $T \in [500, 2000]$ [illustratif] actions honnêtes multi-tâches.
- **Contrôle négatif** : Trajectoires honnêtes 8B subissant un changement de domaine (plan d'expérience → analyse statistique) et des paraphrases stylistiques neutres sans aucun sabotage.
- **Ancrage matériel et coût** : Inférence seule avec extraction d'activations sur deux modèles ouverts ~8B d'architectures distinctes (ex. Llama-3.1-8B-Instruct et Qwen2.5-7B-Instruct [illustratif]) ; 1–2 GPU 48 Go (type L40S/A6000 [illustratif]), ~40–80 h GPU [illustratif], stockage ~300 Go [illustratif], coût ~80–250 € [illustratif], 0 famille de sabotage consommée.
- **Falsification** : $\rho_s < 0,60$ ou taux de violation $> 0,20$ réfute `H_A` (obligeant à reconstruire le simulateur avant tout couplage). Le respect des deux seuils réfute `H_B`.

#### Expérience 4 (Chantier C4) — Dépassement du plafond $T > N_0$ par nul par acte synthétisé
- **`H_A`** : Dans un budget préenregistré de $B = 3$ [illustratif] promotions filtrées par $\Phi_{\text{CPU}}$, `I` produit au moins un e-processus à nul par acte qui maintient un FPR anytime $\le 0,05$ [illustratif] à horizon $T = 5 N_0$ (ex. $N_0 = 200, T = 1000$ [illustratif]) sur traces honnêtes 8B **et** surpasse les trois bases mécaniques (boîte noire, boîte blanche par action, référence fixe $N_0$) d'au moins $+15\%$ [illustratif] en TPR (ou $-25\%$ [illustratif] en temps médian de détection) sur une famille tenue à l'écart (lecture unique, seuil corrigé $\alpha/B$).
- **`H_B`** : Aucun des $B$ candidats promus ne satisfait simultanément la validité anytime en $T = 5 N_0$ et le gain requis face aux trois bases mécaniques.
- **Métrique et seuil** : FPR anytime sur trajectoires honnêtes longues + TPR / délai médian $\tau_{50}$ sur la famille tenue à l'écart (lecture unique).
- **Contrôle négatif** : Trajectoires honnêtes appariées de même longueur $T = 5 N_0$ avec pression rhétorique bénigne et dérive naturelle de tâche ; aucune violation de $\alpha$ autorisée.
- **Ancrage matériel et coût** : Synthèse CPU (~150 h CPU [illustratif]) + évaluation 8B sur 1–2 GPU 48–80 Go (~60–120 h GPU [illustratif]), coût calcul ~150–400 € [illustratif] + **1 famille tenue à l'écart consommée** (irréversible).
- **Falsification** : Échec à battre les trois bases ou violation de FPR en $T = 5 N_0$ réfute `H_A`. Succès conjoint sur validité et puissance (contrôle négatif respecté) réfute `H_B`.

#### Expérience 5 (Chantier C5) — Utilité nette de la boucle couplée face à la boucle ouverte et aux méthodes standards
- **`H_A`** : Sur $K = 3$ [illustratif] familles inédites indépendantes à lecture unique (Axes 1 et 2), la boucle couplée sous pare-feu ($\Pi_{\text{spec}}$ sans score) bat simultanément `I` en boucle ouverte, une bibliothèque mécanique de tests séquentiels existants et le bras placebo (spécifications permutées), avec un gain moyen $\ge +10\%$ [illustratif] d'aire sous courbe détection/délai à FPR anytime $\le 0,05$ sur au moins $2/3$ [illustratif] des familles et un rendement net par unité de coût $\mathcal{R}_{\text{couplée}} > \max(\mathcal{R}_{\text{ouverte}}, \mathcal{R}_{\text{mécanique}})$.
- **`H_B`** : La boucle couplée ne surpasse pas simultanément les trois comparateurs sur ces critères (ou son rendement net $\mathcal{R}$ est inférieur), invalidant l'intérêt pratique du couplage automatisé.
- **Métrique et seuil** : Aire détection/délai à FPR anytime $\le 0,05$ [illustratif] + rendement net $\mathcal{R}$ normalisé par coût total (CPU + GPU + familles), évalués en double aveugle par l'orchestrateur.
- **Contrôle négatif** : Bras placebo recevant des spécifications issues de bruit permuté (CN1/CN3) ; l'évaluateur ignore l'identité des 4 bras.
- **Ancrage matériel et coût** : Deux modèles ouverts ~8B [illustratif], ~150–300 h GPU (cluster 4×48 Go ou A100/H100 [illustratif]) + ~300 h CPU [illustratif], coût calcul ~400–1200 € [illustratif] + **3 familles tenues à l'écart consommées** (banque $\mathcal{F}_{\text{val}}$ strictement préservée pour lecture unique finale).
- **Falsification** : Échec contre l'un des trois comparateurs ou violation du pare-feu/FPR réfute `H_A` et entraîne l'arrêt du couplage. La supériorité conjointe sur les trois bras sans fuite réfute `H_B`.

### 7.3. Ce qui reste hors de portée

1. **Détection garantie d'un sabotage indiscernable sous $H_0$** : aucun objet mathématique inventé par `I` ne peut détecter statistiquement un comportement dont les activations restent dans la distribution honnête ; seul le plancher d'audit exogène protège ce régime, dans la limite de la capacité de l'oracle humain.
2. **Résolution du problème d'oracle sur vérité différée ou ambiguë** : si l'oracle exogène lui-même ne distingue pas un dommage subtil dans une analyse statistique ou un plan d'expérience ($p_s \approx 0$), ni les sondes ni l'idéation automatisée ne créent de vérité terrain.
3. **Extrapolation vers des modèles d'échelle supérieure** : *je ne sais pas* si des invariants d'activations, des nuls par acte ou des coûts d'évasion validés sur modèles ouverts 8B se conservent à 70B+ [illustratif] ou sur architectures non ouvertes ; aucune conclusion ne peut être extrapolée sans réévaluation dédiée.
4. **Preuve absolue de nouveauté avec modèles pré-entraînés opaques** : tant que les corpus de pré-entraînement ne sont pas intégralement auditables, l'absence totale de réminiscence sur des concepts pré-cutoff reste indémontrable ; seuls les bancs *de novo* et prospectifs fournissent des garanties partielles.
5. **Invention autonome de cadres mathématiques hors de toute grammaire vérifiable** : sans vérificateur mécanique amont, toute proposition radicalement hors cadre retombe sur l'audit humain (coût maximal) ou sur des juges génératifs sujets à la corruptibilité rhétorique.

FIN-DE-CELLULE