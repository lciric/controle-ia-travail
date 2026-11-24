*Note d'audit documentaire : les blocs `FAITS` et `QUESTION DE L'ARBITRE` transmis sont complets et identiques (mode à l'aveugle du Tour III.1) [VÉRIFIÉ] ; conformément à la règle d'intégrité sur les sources, aucun identifiant de prépublication n'est cité de mémoire.*

---

## I. Livrable (a) — Ce que la question suppose sans que ce soit établi

Le cadrage soumis repose sur six présupposés implicites qui doivent être traités comme objets de réfutation et non comme acquis :

* **P-I (Invariance intrinsèque de la cible)** `[HYPOTHÈSE]` : Que « étroit » (*narrow*) et « profond » (*deep*) soient des propriétés intrinsèques d'une idée candidate $x$, stables par changement de formalisme. En théorie algorithmique de l'information, la rareté d'accès dépend pourtant du couple $(\mathcal{L}, \mu_0)$ formé par le langage de représentation $\mathcal{L}$ et la politique de recherche de référence $\mu_0$ `[VÉRIFIÉ]`.
* **P-II (Commensurabilité de l'espace de candidats)** `[HYPOTHÈSE]` : Qu'un système multi-agents en langage naturel, un échantillonneur aléatoire et un énumérateur mécanique explorent le « même espace » $\mathcal{X}$. Sans projection mécanique sur un espace quotient d'équivalence sémantique $\mathcal{X}/\!\sim$, la syntaxe libre gonfle artificiellement la rareté apparente par rapport à une grammaire canonique `[VÉRIFIÉ]`.
* **P-III (Effet amplificateur de la critique multi-agents)** `[HYPOTHÈSE]` : Que la boucle proposer-critiquer-sélectionner favorise les queues de distribution rares et fécondes, plutôt que d'induire une régression vers le consensus modal des modèles de langage à budget égal.
* **P-IV (Séparabilité *ex ante* des régions fertiles)** `[HYPOTHÈSE]` : Qu'il existe des signatures observables d'un problème permettant de prédire, avant d'en connaître la solution, qu'il admet une idée étroite et profonde plutôt que du bruit irréductible ou une solution graduelle.
* **P-V (Tractabilité statistique de la rareté en boîte noire)** `[HYPOTHÈSE]` : Qu'on puisse certifier empiriquement qu'une idée est rarement atteinte ($p_0 \ll 1$) sans exploser le budget du harnais, alors que borner $p_0 \le \varepsilon$ au risque $\alpha$ exige au moins $\ln(1/\alpha)/\varepsilon$ tirages indépendants de la référence `[VÉRIFIÉ]` (Clopper & Pearson, 1934).
* **P-VI (Unicité de la référence mono-modèle)** `[OBSERVÉ-NON-AUDITÉ]` : Que « le meilleur modèle seul à budget égal » désigne un point de comparaison unique, alors que sa performance change sensiblement selon que le budget est alloué à de l'échantillonnage parallèle filtré (*Best-of-N*) ou à de l'auto-révision séquentielle (études d'échelle au moment du test, « référence à vérifier »).

---

## II. Traitement des Points 1 à 8 de l'Arbitre

### 1. Cible (*Target*) : définitions opérationnelles sans juge LLM et bornage du biais
* **Confiance** : `0,80` (illustratif).
* **Établi vs Conjecture** : Il est établi que la rareté syntaxique ne mesure pas l'utilité déductive ou prédictive `[VÉRIFIÉ]` (Bennett, 1988) et qu'une prévalence rare est submergée par le taux de fausses alertes d'un classifieur imparfait `[VÉRIFIÉ]` (Rogan & Gladen, 1978). Il reste conjectural qu'un quotientage mécanique suffise hors des langages formels ou symboliques `[HYPOTHÈSE]`.
* **Où le cadrage se trompe** : Le cadrage parle d'étroitesse au singulier, comme si « la recherche ordinaire » était unique, et envisage un juge LLM comme substitut acceptable sous réserve d'encadrement. Or, dès que la vraie fréquence d'idées profondes $\pi_g$ est inférieure au taux de fausses alertes $\text{FPR}_g$ du juge, la valeur prédictive positive s'effondre mathématiquement `[VÉRIFIÉ]`.
* **Protocole opérationnel** :
  1. *Quotientage sémantique préalable* : Toute idée $x \in \mathcal{X}$ est projetée mécaniquement vers sa classe $[x] \in \mathcal{X}/\!\sim$ (simplification canonique par e-graphes ou égalité d'évaluation sur grille dense pour les lois ; équivalence définitionnelle ou empreinte du graphe de dépendances pour les lemmes) `[VÉRIFIÉ]`.
  2. *Étroitesse relative $N_{\mu_0, b_0}([x])$* : Fixer explicitement la référence $(\mathcal{L}, \mu_0, b_0)$ en suivant deux mesures distinctes (échantillonnage indépendant du modèle de base seul, et énumérateur grammatical par coût croissant). Sur $M_0$ exécutions indépendantes de budget unitaire $b_0$, soit $\hat{p}_0^{+}([x])$ la borne supérieure exacte de Clopper-Pearson au niveau $1 - \alpha$ de la probabilité d'atteinte `[VÉRIFIÉ]` (Clopper & Pearson, 1934). On définit l'étroitesse certifiée en nats par $N_{\mu_0, b_0}([x]) = -\ln \hat{p}_0^{+}([x])$ `[VÉRIFIÉ]`.
  3. *Profondeur $D([x])$ séparée de la rareté* : Une chaîne aléatoire syntaxiquement valide ou une identité arithmétique isolée possède un $N_{\mu_0, b_0}([x])$ élevé mais ne compresse rien hors d'elle-même `[VÉRIFIÉ]`. On mesure la profondeur sans juge LLM par le **levier de compression hors distribution** :
     - *Lois quantitatives* : Gain de longueur de description minimale (MDL) sur $R$ régimes interventionnels retenus hors recherche $\{D_r\}_{r=1}^R$, pénalisé par la complexité syntaxique $K_{\mathcal{L}}([x])$ de la loi : $D_{\text{MDL}}([x]) = \sum_{r=1}^R \max(0, L_{\text{null}}(D_r) - L(D_r \mid [x])) - K_{\mathcal{L}}([x])$ `[VÉRIFIÉ]` (Rissanen, 1978 ; Grünwald, 2007).
     - *Lemmes formels* : Réduction mécanique du nombre de pas de saturation d'un prouveur déterministe fixe sur un corpus aval retenu $\mathcal{C}_{\text{test}}$ lorsque $[x]$ est ajouté à la bibliothèque, moins le coût de vérification de $[x]$ `[HYPOTHÈSE]`.
  4. *Bornage si un juge $\hat{J}$ est inévitable* : Si un domaine semi-formel impose un juge $\hat{J} \in \{0,1\}$, le biais d'affinité générateur-juge crée $\text{FPR}_{\text{MA}} \neq \text{FPR}_{\text{Base}}$ `[RAPPORTÉ]` (biais d'auto-préférence des juges LLM, « référence à vérifier »). Par l'identité de Rogan-Gladen stratifiée par générateur $g$, la prévalence vraie vaut $\pi_g = (p_g - \text{FPR}_g)/(\text{TPR}_g - \text{FPR}_g)$ où $p_g = \mathbb{P}(\hat{J}=1 \mid G=g)$ `[VÉRIFIÉ]` (Rogan & Gladen, 1978). Il faut auditer à l'aveugle par un oracle exact un sous-échantillon aléatoire des appels $\hat{J}=1$ et $\hat{J}=0$ de *chaque* bras $g$ afin d'encadrer $(\text{TPR}_g, \text{FPR}_g)$ par intervalles exacts ; si $\hat{p}_{\text{MA}} \le \overline{\text{FPR}}_{\text{MA}}$, aucune découverte ne peut être revendiquée sans vérification oracle exhaustive de tous les positifs `[VÉRIFIÉ]`.
* **Références** : Bennett, C. H. (1988), « Logical Depth and Physical Complexity », *The Universal Turing Machine: A Half-Century Survey*, Oxford University Press ; Clopper, C. J., & Pearson, E. S. (1934), « The Use of Confidence or Fiducial Limits Illustrated in the Case of the Binomial », *Biometrika* ; Grünwald, P. D. (2007), *The Minimum Description Length Principle*, MIT Press ; Rissanen, J. (1978), « Modeling by shortest data description », *Automatica* ; Rogan, W. J., & Gladen, B. (1978), « Estimating Prevalence from the Results of a Screening Test », *American Journal of Epidemiology*.

### 2. Sources de vérité terrain (*Sources of truth*)
* **Confiance** : `0,85` (illustratif).
* **Établi vs Conjecture** : Les propriétés de sûreté logique d'un noyau formel et l'indistinguabilité observationnelle d'interventions causales manquantes sont établies `[VÉRIFIÉ]` (Pearl, 2009). Le degré de transfert des mondes synthétiques vers la découverte ouverte reste conjectural `[HYPOTHÈSE]`.
* **Où le cadrage se trompe** : La rétrodiction temporelle est traitée comme un oracle symétrique ; or elle ne peut ni exclure les précurseurs conceptuels antérieurs à la coupure, ni évaluer une idée *nouvelle et valide* que le système trouverait mais que l'histoire humaine n'a pas publiée `[VÉRIFIÉ]`.
* **Comparaison analytique** :
  1. *Mondes synthétiques à vérité plantée* : Établissent exactement $N_{\mu_0}$ (par échantillonnage massif peu coûteux) et $D_{\text{MDL}}$ sous interventions contrôlées $\text{do}(\cdot)$ `[VÉRIFIÉ]` (Pearl, 2009). Ne peuvent établir l'adéquation aux ontologies naturelles mal alignées avec les primitives choisies `[HYPOTHÈSE]`. Échouent si le concepteur plante des lois composées des fonctions favorites du pré-entraînement LLM `[HYPOTHÈSE]`.
  2. *Rétrodiction avec coupure temporelle* : Établit que la cible avait une portée scientifique reconnue `[OBSERVÉ-NON-AUDITÉ]`. Ne peut certifier l'absence de fuite indirecte (reformulations, conjectures dans des manuels pré-coupure) `[RAPPORTÉ]` (« référence à vérifier ») ni noter une hypothèse alternative correcte hors archive `[VÉRIFIÉ]`. Échoue par contamination résiduelle et par biais d'énoncé utilisant le vocabulaire post-coupure `[HYPOTHÈSE]`.
  3. *Preuve formelle* : Établit une validité déductive à taux de faux positifs nul modulo le noyau et la fidélité de l'énoncé `[VÉRIFIÉ]` (Moura & Ullrich, 2021), ainsi que $D_{\text{proof}}$ sur corpus aval `[HYPOTHÈSE]`. Ne peut établir la vérité empirique ni empêcher une formalisation infidèle `[VÉRIFIÉ]`. Échoue par prémisses contradictoires cachées (`False -> P`) ou lemmes tautologiques `[OBSERVÉ-NON-AUDITÉ]`.
  4. *Tests exécutables* : Établissent le comportement fonctionnel à faible coût marginal `[VÉRIFIÉ]`. Ne peuvent prouver l'universalité hors du support de test `[VÉRIFIÉ]`. Échouent par sur-ajustement par table de cas (*reward hacking*) ou artefacts numériques si $K_{\mathcal{L}}([x])$ est omis `[RAPPORTÉ]` (« référence à vérifier »).
  5. *Source additionnelle proposée — Oracle interventionnel actif en boîte noire* : Le candidat soumet conjointement une loi $f$ et un protocole d'expérience cruciale $\pi^*$ maximisant la divergence prédite face aux modèles de base `[HYPOTHÈSE]` (Popper, 1959) ; l'oracle exécute l'intervention jamais observée. Échoue si le bruit instrumental couvre l'écart prédit `[VÉRIFIÉ]`.
* **Références** : Moura, L. de, & Ullrich, S. (2021), « The Lean 4 Theorem Prover and Programming Language », *Automated Deduction – CADE 28*, Springer ; Pearl, J. (2009), *Causality: Models, Reasoning, and Inference*, Cambridge University Press ; Popper, K. R. (1959), *The Logic of Scientific Discovery*, Hutchinson ; Udrescu, S.-M., & Tegmark, M. (2020), « AI Feynman: A physics-inspired method for symbolic regression », *Science Advances*.

### 3. Comparaison aux références et attribution causale (*Comparison*)
* **Confiance** : `0,85` (illustratif).
* **Établi vs Conjecture** : La validité du test d'intersection-union pour démontrer la supériorité simultanée sur plusieurs références sans correction de multiplicité conservatrice est établie `[VÉRIFIÉ]` (Berger, 1982). La part de gain attribuable aux rôles multi-agents plutôt qu'au calcul additionnel est non établie (`P-III`) `[HYPOTHÈSE]`.
* **Où le cadrage se trompe** : Compter le budget uniquement en jetons générés ou autoriser le système multi-agents à appeler un compilateur en boucle face à un modèle seul en un jet confond l'architecture avec le *Best-of-N* assisté par vérificateur `[VÉRIFIÉ]`.
* **Spécification statistique** :
  - *Unité d'analyse* : L'instance de problème indépendante $i \in \{1, \dots, M_{\text{prob}}\}$ (jamais les idées individuelles produites au sein d'une même exécution, qui sont corrélées) `[VÉRIFIÉ]`. Chaque méthode ne soumet au coffre d'évaluation que son candidat final sélectionné de rang `1` (illustratif) afin d'évaluer aussi la sélection.
  - *Comptabilité des coûts* : Vecteur strictement apparié $B = (B_{\text{FLOP}}, B_{\text{tok}}, B_{\text{oracle}}, B_{\text{mur}})$ incluant les FLOPs quadratiques de pré-remplissage des longs historiques multi-agents et **chaque** appel interne au vérificateur syntaxique ou d'entraînement `[VÉRIFIÉ]`.
  - *Quantité primaire* : Taux de découverte étroite et profonde $Y_{i,m}(B) = \mathbb{I}[N_{\mu_0}([x^*_{i,m}]) \ge \tau_N \land D([x^*_{i,m}]) \ge \tau_D]$ et excès continu $Z_{i,m}(B) = \mathbb{I}[N_{\mu_0}([x^*_{i,m}]) \ge \tau_N] \cdot \max(0, D([x^*_{i,m}]))$ pour des seuils $(\tau_N, \tau_D)$ pré-enregistrés.
  - *Règle de décision* : Test d'intersection-union apparié `[VÉRIFIÉ]` (Berger, 1982) exigeant le rejet simultané au seuil unilatéral $\alpha = 0,025$ (illustratif) de $H_{0,b} : \mathbb{E}[Y_{\text{MA}} - Y_b] \le \delta_{\text{min}}$ (avec marge minimale d'intérêt pratique $\delta_{\text{min}} = 0,10$ (illustratif)) contre *toutes* les références $b \in \{\text{Aléatoire}, \text{Énumérateur}, \text{BestOfN-Mono}(B), \text{Itératif-Mono}(B)\}$.
  - *Ablations d'attribution* : (i) `MA-Complet` vs `Itératif-Mono(B)` (isole la pluralité d'agents de la révision séquentielle) ; (ii) `MA-Complet` vs `Parallèle-SansCritique(B)` (isole l'agent critique, voir `Exp. III`) ; (iii) `MA-Complet` vs `MA-SélectionAléatoireValide(B)` (isole le sélecteur) ; (iv) `MA-Homogène` vs `MA-Hétérogène` inter-familles de modèles (isole la diversité des priors de pré-entraînement).
* **Références** : Berger, R. L. (1982), « Multiparameter Hypothesis Testing and Acceptance Sampling », *Technometrics* ; Platt, J. R. (1964), « Strong Inference », *Science*.

### 4. Choix des problèmes (*Problem choice*)
* **Confiance** : `0,55` (illustratif).
* **Établi vs Conjecture** : On peut séparer l'erreur épistémique du bruit aléatoire par réplicats expérimentaux sur entrées identiques `[VÉRIFIÉ]`. Qu'un profil d'erreur structurel prédise la présence d'une solution *étroite* plutôt qu'une somme de corrections graduelles est une conjecture (`P-IV`) `[HYPOTHÈSE]`.
* **Où le cadrage se trompe** : Sélectionner des problèmes historiques célèbres introduit un biais du survivant massif, car ces problèmes ont précisément survécu dans la littérature parce qu'une astuce féconde les a résolus `[HYPOTHÈSE]`.
* **Critères *ex ante* et test** : Construire un score prospectif $S_{\text{region}}(i) \in \{0,1\}$ calculé *uniquement* à partir des résidus des références simples : (a) fort résidu épistémique au-dessus du plancher de bruit de réplication ($\text{Gap}_i > \gamma_1$) `[VÉRIFIÉ]` ; (b) rupture de transfert inter-régimes d'entraînement ($\text{Ratio}_{\text{OOD/ID}} > \gamma_2$), typique d'une symétrie ou loi de conservation manquante `[HYPOTHÈSE]` ; (c) pour les tâches formelles, distance d'importation élevée entre domaines requis dans le graphe de dépendances `[HYPOTHÈSE]`. Ce choix est testé prospectivement sans circulaire par `Exp. IV`.
* **Références** : Pearl, J. (2009), *Causality: Models, Reasoning, and Inference*, Cambridge University Press ; Udrescu, S.-M., & Tegmark, M. (2020), « AI Feynman: A physics-inspired method for symbolic regression », *Science Advances*.

### 5. Rétroaction autorisée et interdite durant la recherche (*Feedback*)
* **Confiance** : `0,90` (illustratif).
* **Établi vs Conjecture** : La dégradation de validité statistique d'un jeu de test interrogé de façon adaptative sur $T$ itérations croît en $O(\sqrt{T \ln |\mathcal{X}| / n})$ `[VÉRIFIÉ]` (Dwork et al., 2015).
* **Où le cadrage se trompe** : Le cadrage demande quelles mesures du harnais peuvent être renvoyées au générateur ; or renvoyer *n'importe quelle* composante directe de la cible finale $(N_{\mu_0}, D_{\text{test}})$ détruit l'indépendance de la mesure par loi de Goodhart adaptative `[VÉRIFIÉ]`.
* **Cloisonnement strict** :
  - *Autorisé en boucle ouverte ($\mathcal{I}_{\text{search}}$)* : Erreurs mécaniques de syntaxe, de typage ou d'homogénéité dimensionnelle ; vérification locale qu'une preuve candidate compile sans axiome interdit ; résidu prédictif uniquement sur la coupe d'entraînement $D_{\text{train}}$ ; compteur de budget restant $B - b_t$ `[VÉRIFIÉ]`.
  - *Retenu sous scellé étanche ($\mathcal{I}_{\text{vault}}$)* : (1) Tous les régimes interventionnels $\{D_r\}_{r=1}^R$ et le corpus aval $\mathcal{C}_{\text{test}}$ servant à calculer $D([x])$ ; (2) la distribution de référence $\hat{p}_0([x])$ et le score $N_{\mu_0}([x])$ — car exposer $N_{\mu_0}$ pousse le système vers l'obfuscation syntaxique ou sémantique pour fuir $\mu_0$ sans gain scientifique `[VÉRIFIÉ]` ; (3) le code générateur des vérités plantées. Si un signal de validation intermédiaire est indispensable, il doit provenir d'une coupe dédiée $D_{\text{val}}$ distincte de $\mathcal{I}_{\text{vault}}$ via un mécanisme à bruit calibré (*Thresholdout*) facturé dans $B_{\text{oracle}}$ `[RAPPORTÉ]` (Dwork et al., 2015). Testé par `Exp. V`.
* **Références** : Dwork, C., Feldman, V., Hardt, M., Pitassi, T., Reingold, O., & Roth, A. (2015), « The Reusable Holdout: Preserving Validity in Adaptive Data Analysis », *Science*.

### 6. Validation préalable du harnais (*Validating the harness*)
* **Confiance** : `0,88` (illustratif).
* **Établi vs Conjecture** : L'étalonnage d'un instrument sur témoins positifs, négatifs et invariants connus précède logiquement toute inférence expérimentale `[VÉRIFIÉ]` (Platt, 1964).
* **Où le cadrage se trompe** : Valider seulement la sensibilité aux vraies découvertes ignore l'attaque principale d'un générateur symbolique ou linguistique : contourner le détecteur d'équivalence pour faire passer une idée triviale maquillée pour « étroite » `[HYPOTHÈSE]`.
* **Cinq portes obligatoires avant tout tir coûteux** :
  1. *Spécificité sur bruit et vacuité* : Injecter du bruit syntaxiquement valide, des polynômes sur-paramétrés et des lemmes formels à prémisse contradictoire ; exiger $\widehat{\text{FPR}} = 0$ (illustratif) sur les tautologies/vacuités et $\le 0,01$ (illustratif) sur le bruit `[HYPOTHÈSE]`.
  2. *Rejet du « large et profond »* : Injecter des lois classiques fréquentes sous $\mu_0$ ; exiger $D \ge \tau_D$ mais $N_{\mu_0} < \tau_N$.
  3. *Rejet de l'« étroit et superficiel »* : Injecter des identités vraies mais isolées (zéro effet aval) ; exiger $N_{\mu_0} \ge \tau_N$ mais $D \le 0$ (illustratif).
  4. *Sensibilité sur vérité plantée* : Injecter des invariants rares compressant $R$ régimes OOD ; exiger $\widehat{\text{TPR}} \ge 0,95$ (illustratif).
  5. *Invariance par obfuscation* : Appliquer `50` (illustratif) transformations préservant la sémantique (commutativité, termes nuls, renommage $\alpha$, code mort) à des idées larges ; exiger qu'au moins `0,98` (illustratif) retombent dans la classe large de départ.
* **Références** : Platt, J. R. (1964), « Strong Inference », *Science* ; Rice, H. G. (1953), « Classes of Recursively Enumerable Sets and Their Decision Problems », *Transactions of the American Mathematical Society*.

### 7. Plan expérimental ordonné par coût (*Plan*)
* **Confiance** : `0,78` (illustratif).
* **Établi vs Conjecture** : Les tailles d'échantillon binomiales et appariées découlent des bornes exactes `[VÉRIFIÉ]` (Clopper & Pearson, 1934) ; les taux d'effet attendus sont illustratifs `[HYPOTHÈSE]`.
* **Où le cadrage se trompe** : Lancer d'emblée l'évaluation sur problèmes scientifiques réels gaspille le budget si le multi-agents ne bat même pas `BestOfN-Mono(B)` dans un monde synthétique contrôlé `[HYPOTHÈSE]`.
* **Séquence ordonnée et critères d'arrêt (couplée à la Section III)** :
  - **Phase I (Coût minimal, CPU seul)** : Portes d'étalonnage du Point 6 + `Exp. I` (invariance inter-DSL sur $N_{\text{classes}} = 200$ (illustratif) candidats). *Critère d'arrêt* : Si $\bar{\tau}_K < 0,30$ (illustratif) ou fuite d'obfuscation $> 0,02$ (illustratif), arrêt immédiat (cible mal posée ou quotient défaillant).
  - **Phase II (Coût faible, mondes synthétiques)** : $M_{\text{prob}} = 60$ (illustratif) instances ($30$ (illustratif) par strate $S_{\text{region}}$) avec $M_0 = 1\,000$ (illustratif) tirages de référence par instance (certifiant jusqu'à $N_{\mu_0} \approx 5,8$ (illustratif) nats au risque $\alpha = 0,05$ (illustratif), soit $\approx 8,4$ (illustratif) bits). Exécute `Exp. II`, `Exp. III`, `Exp. IV`, `Exp. V`. *Critère d'arrêt* : Si `MA-Complet` échoue à battre l'enveloppe des références de $\delta_{\text{min}} = 0,10$ (illustratif) (`Exp. II`), arrêt du programme. Si `Exp. III` falsifie l'utilité de la critique, suppression de l'agent critique pour la suite.
  - **Phase III (Coût moyen, déduction formelle Lean)** : $M_{\text{prob}} = 80$ (illustratif) théories formelles mutées ou post-coupure garantissant zéro mémorisation littérale. *Critère d'arrêt* : Si gain sur `BestOfN-Mono(B)` non significatif à $\alpha = 0,025$ (illustratif), arrêt avant l'étape finale.
  - **Phase IV (Coût élevé, lois interventionnelles prospectives et audit oracle)** : $M_{\text{prob}} = 100$ (illustratif) problèmes (puissance `0,80` (illustratif) à $\alpha = 0,025$ (illustratif) pour détecter un passage du taux de découverte de `0,05` (illustratif) à `0,18` (illustratif) en test apparié) + `Exp. VI` si un sous-ensemble semi-formel est inclus.
* **Références** : Berger, R. L. (1982), « Multiparameter Hypothesis Testing and Acceptance Sampling », *Technometrics* ; Clopper, C. J., & Pearson, E. S. (1934), « The Use of Confidence or Fiducial Limits Illustrated in the Case of the Binomial », *Biometrika*.

### 8. Limites, infaisabilité et cible mal posée (*Limits*)
* **Confiance** : `0,92` (illustratif).
* **Établi vs Conjecture** : L'indécidabilité de l'équivalence sémantique pour des programmes généraux Turing-complets est établie `[VÉRIFIÉ]` (Rice, 1953), tout comme la borne exponentielle d'échantillonnage Monte-Carlo d'événements rares `[VÉRIFIÉ]`.
* **Où le cadrage se trompe** : Présumer qu'un banc automatique pourrait capter les découvertes les plus conséquentes de la science, alors que celles-ci consistent souvent à **changer l'espace d'états ou les observables** plutôt qu'à optimiser une loi dans un langage $\mathcal{L}$ pré-fixé `[HYPOTHÈSE]`.
* **Hors de portée de tout harnais de ce type** :
  1. *Le mur exponentiel de certification de l'étroitesse* : En boîte noire, certifier $p_0([x]) \le 10^{-6}$ (illustratif) exige $\ge 3 \times 10^6$ (illustratif) exécutions indépendantes de la référence *par problème* `[VÉRIFIÉ]`. Au-delà d'une étroitesse modérée ($\approx 8$ à $12$ (illustratif) bits), la mesure empirique directe est matériellement infaisable hors mondes synthétiques analytiques.
  2. *L'invention ontologique* : Tout harnais automatisé fige $\mathcal{L}$ et les canaux de mesure avant l'expérience `[VÉRIFIÉ]` ; une idée introduisant une variable physique nouvelle non câblée dans le simulateur est inévaluable `[HYPOTHÈSE]`.
  3. *La profondeur différée* : En mathématiques, la fécondité d'un lemme dépend parfois de définitions futures absentes du corpus statique $\mathcal{C}_{\text{test}}$ `[OBSERVÉ-NON-AUDITÉ]`.
* **Preuves empiriques d'ill-posedness ou d'infaisabilité** :
  - *Cible mal posée* : Si dans `Exp. I`, la concordance de rang de Kendall $\bar{\tau}_K$ de $(N_{\mu_0}, D)$ entre `3` (illustratif) formalismes sémantiquement équivalents tombe sous `0,30` (illustratif), « étroit et profond » n'est qu'un artefact de notation.
  - *Harnais infaisable* : (i) Si, du fait du théorème de Rice `[VÉRIFIÉ]` (Rice, 1953), plus de `0,20` (illustratif) des variations syntaxiques d'idées larges échappent au quotientage mécanique ; ou (ii) si le coût $M_0 \cdot b_0$ nécessaire pour attester $N_{\mu_0} \ge \tau_N$ excède de plus d'un facteur `10` (illustratif) le budget total disponible avant d'atteindre une puissance statistique de `0,80` (illustratif).
* **Références** : Rice, H. G. (1953), « Classes of Recursively Enumerable Sets and Their Decision Problems », *Transactions of the American Mathematical Society*.

---

## III. Livrable (b) — Expériences décisives en inférence forte ($H_A$ contre $H_B$)

Chaque expérience oppose deux hypothèses mutuellement exclusives sur le domaine testé `[HYPOTHÈSE]` :

1. **Exp. I — Stabilité représentationnelle de la cible (teste P-I et Point 8)**
   - **$H_A$** `[HYPOTHÈSE]` : Le score conjoint $\mathbb{I}[N_{\mu_0} \ge \tau_N] \cdot D([x])$ est intrinsèque à l'idée : la concordance moyenne de Kendall $\bar{\tau}_K$ entre `3` (illustratif) DSL formellement isomorphes (algébrique infixe, combinatoire sans variable, graphe de flux typé) vérifie $\bar{\tau}_K \ge 0,60$ (illustratif).
   - **$H_B$** `[HYPOTHÈSE]` : La cible dépend de l'encodage syntaxique : $\bar{\tau}_K < 0,60$ (illustratif).
   - **Métrique et seuil** : $\bar{\tau}_K$ sur `200` (illustratif) classes d'idées évaluées dans les `3` (illustratif) DSL ; seuil `0,60` (illustratif) par intervalle de confiance bootstrap à `95 %` (illustratif).
   - **Contrôle négatif** : Permutation aléatoire des identifiants sémantiques entre DSL (attendu : $|\bar{\tau}_K| \le 0,08$ (illustratif)) et réécritures triviales intra-DSL (attendu : $\tau = 1,00$ (illustratif)).
   - **Issues falsifiantes** : Borne supérieure de l'IC $< 0,60$ (illustratif) falsifie $H_A$ (et $< 0,30$ (illustratif) établit le caractère mal posé de la cible) ; borne inférieure $\ge 0,60$ (illustratif) falsifie $H_B$.

2. **Exp. II — Supériorité à budget vectoriel égal contre l'enveloppe des références (teste Point 3)**
   - **$H_A$** `[HYPOTHÈSE]` : `MA-Complet` surpasse simultanément *chacune* des références $b \in \{\text{Aléatoire}, \text{Énumérateur}, \text{BestOfN-Mono}(B), \text{Itératif-Mono}(B)\}$ d'au moins $\delta_{\text{min}} = 0,10$ (illustratif) en taux de découverte par problème ($\min_b (\pi_{\text{MA}} - \pi_b) \ge 0,10$ (illustratif)).
   - **$H_B$** `[HYPOTHÈSE]` : Au moins une référence à budget FLOPs et appels oracle strictement identiques atteint $\pi_{\text{MA}} - \pi_b < 0,10$ (illustratif).
   - **Métrique et seuil** : Différence appariée sur $M_{\text{prob}} = 60$ (illustratif) mondes synthétiques (puis `80` (illustratif) modules Lean et `100` (illustratif) problèmes finaux), test d'intersection-union à $\alpha = 0,025$ (illustratif), seuils $\tau_N = 5,5$ (illustratif) nats et $\tau_D = 35$ (illustratif) nats MDL.
   - **Contrôle négatif** : Mondes de bruit blanc sans loi plantée ($\widehat{\text{FPR}} \le 0,01$ (illustratif)) et duel A/A `BestOfN-Mono(B)` contre lui-même sous graine distincte (écart nul attendu).
   - **Issues falsifiantes** : Rejet simultané de toutes les $H_{0,b}$ au-dessus de `0,10` (illustratif) falsifie $H_B$ ; borne supérieure de l'IC $< 0,10$ (illustratif) contre au moins une référence falsifie $H_A$.

3. **Exp. III — Effet causal de l'agent Critique : levier sélectif contre effondrement vers le prior (teste P-III)**
   - **$H_A$** `[HYPOTHÈSE]` : À budget $B$ fixe, `MA-Complet` surpasse `Parallèle-SansCritique(B)` (où les jetons de critique financent plus de tirages parallèles) de $\Delta Z > 0$ avec une hausse d'étroitesse médiane des candidats retenus $\Delta N \ge 0,7$ (illustratif) nat.
   - **$H_B$** `[HYPOTHÈSE]` : La critique censure les candidats atypiques ou gaspille le budget : $\Delta Z \le 0$ ou $\Delta N < 0,7$ (illustratif) nat.
   - **Métrique et seuil** : Test de Wilcoxon apparié sur $Z_{i,m}(B)$ et décalage médian $\Delta N$ à $\alpha = 0,025$ (illustratif).
   - **Contrôle négatif** : Agent Critique « placebo » reformulant le texte à jetons constants sans filtrage (doit sous-performer `Parallèle-SansCritique(B)` proportionnellement au budget brûlé).
   - **Issues falsifiantes** : $\Delta Z > 0$ significatif et $\Delta N \ge 0,7$ (illustratif) nat falsifie $H_B$ ; $\Delta Z \le 0$ ou $\Delta N < 0$ (illustratif) falsifie $H_A$.

4. **Exp. IV — Validité prospective du sélecteur *ex ante* de régions fertiles (teste P-IV et Point 4)**
   - **$H_A$** `[HYPOTHÈSE]` : Le rapport de cotes (*odds ratio*) d'existence d'une solution $(N_{\mu_0} \ge \tau_N, D \ge \tau_D)$ entre les problèmes classés $S_{\text{region}}=1$ et $S_{\text{region}}=0$ vérifie $\text{OR} \ge 2,5$ (illustratif).
   - **$H_B$** `[HYPOTHÈSE]` : L'indice $S_{\text{region}}$ échoue à isoler la profondeur structurelle : $\text{OR} < 2,5$ (illustratif).
   - **Métrique et seuil** : Test exact de Fisher sur `120` (illustratif) problèmes stratifiés (`60` (illustratif) par strate), seuil $\text{OR} = 2,5$ (illustratif) à $\alpha = 0,025$ (illustratif).
   - **Contrôle négatif** : Processus purement stochastiques hétéroscédastiques (erreur brute élevée mais résidu épistémique nul après réplicats ; doivent être classés $S_{\text{region}}=0$).
   - **Issues falsifiantes** : Borne inférieure de l'IC à `95 %` (illustratif) de $\text{OR} \ge 2,5$ (illustratif) falsifie $H_B$ ; borne supérieure $< 2,5$ (illustratif) falsifie $H_A$.

5. **Exp. V — Corruption de la mesure par rétroaction adaptative (teste Point 5)**
   - **$H_A$** `[HYPOTHÈSE]` : Retourner le score $D$ sur une coupe de retenue $D_{\text{hold}}$ pendant la recherche gonfle artificiellement la profondeur par rapport au coffre vierge $D_{\text{vault}}$ de $\Delta_{\text{Goodhart}} = \mathbb{E}[D_{\text{hold}} - D_{\text{vault}}] \ge 10$ (illustratif) nats.
   - **$H_B$** `[HYPOTHÈSE]` : La pénalité syntaxique $K_{\mathcal{L}}([x])$ suffit à prévenir tout sur-ajustement adaptatif ($\Delta_{\text{Goodhart}} < 10$ (illustratif) nats et chute relative $< 5\,\%$ (illustratif)).
   - **Métrique et seuil** : Écart apparié entre régime `Fuite` et régime `Cloisonné` sur `60` (illustratif) problèmes ($\alpha = 0,01$ (illustratif)).
   - **Contrôle négatif** : Évaluation hors boucle en une passe unique ($\mathbb{E}[D_{\text{hold}} - D_{\text{vault}}] = 0$ (illustratif)).
   - **Issues falsifiantes** : $\Delta_{\text{Goodhart}} \ge 10$ (illustratif) nats falsifie $H_B$ ; IC à `99 %` (illustratif) inclus sous `5 %` (illustratif) de chute relative falsifie $H_A$.

6. **Exp. VI — Biais différentiel d'affinité d'un juge LLM (teste Point 1 sur le juge)**
   - **$H_A$** `[HYPOTHÈSE]` : Sur des candidats négatifs vrais ($Y=0$ vérifiés par oracle), le juge LLM présente un écart de fausses alertes $|\text{FPR}_{\text{MA}} - \text{FPR}_{\text{Mono}}| \ge 0,03$ (illustratif) ou $\text{FPR}_g \ge \pi_g$.
   - **$H_B$** `[HYPOTHÈSE]` : Le juge anonymisé vérifie simultanément $|\text{FPR}_{\text{MA}} - \text{FPR}_{\text{Mono}}| < 0,03$ (illustratif) et $\text{FPR}_g < 0,01$ (illustratif).
   - **Métrique et seuil** : Audit oracle en aveugle de `500` (illustratif) paires négatives appariées en longueur et domaine ; seuil `0,03` (illustratif) ($\alpha = 0,025$ (illustratif)).
   - **Contrôle négatif** : Duplication exacte d'un même candidat sous deux identifiants internes (divergence attendue `0` (illustratif) à température nulle).
   - **Issues falsifiantes** : Dépassement du seuil falsifie $H_B$ (disqualifiant le juge sans vérification oracle exhaustive) ; bornes supérieures à `95 %` (illustratif) sous les deux seuils falsifient $H_A$.

---

## IV. Livrable (c) — Mesure minimale de validité pour chaque instrument nommé

Tous les seuils de détection ($\text{TPR}$) et de fausses alertes ($\text{FPR}$) ci-dessous sont marqués `(illustratif)` et constituent des prérequis d'étalonnage `[HYPOTHÈSE]` :

| Instrument nommé | Mesure minimale exigée ($\text{TPR}$ / $\text{FPR}$) | Cas honnêtes appariés (Positif vrai vs Négatif subtil) | Vérification mécanique élémentaire à battre |
| :--- | :--- | :--- | :--- |
| **Harnais de mesure global** | $\text{TPR} \ge 0,95$ (illustratif) ; $\text{FPR} \le 0,01$ (illustratif) | Invariant causal rare compressant $R$ régimes OOD *vs* interpolation tout aussi rare ajustant $D_{\text{train}}$ + loi fréquente obfusquée algébriquement | Critère AIC/BIC en distribution + distance d'édition de chaînes |
| **Juge LLM** *(si utilisé)* | $\text{TPR} \ge 0,85$ (illustratif) ; $\text{FPR} < 0,01$ (illustratif) et $\|\Delta\text{FPR}\| < 0,03$ (illustratif) | Protocole valide vérifié par oracle *vs* protocole de même longueur et jargon issu du multi-agents mais omettant un témoin causal | Heuristique de perplexité/longueur + analyseur déterministe de mots-clés |
| **Mondes synthétiques plantés** | $\text{TPR}_{\text{causal}} = 1,00$ (illustratif) ; $\text{FPR}_{\text{raccourci}} \le 0,01$ (illustratif) | Générateur mécaniste planté exact *vs* modèle de substitution reproduisant les marginales observationnelles sans respecter $\text{do}(\cdot)$ | Erreur quadratique moyenne sur coupe observationnelle i.i.d. |
| **Rétrodiction à coupure temporelle** | $\text{TPR}_{\text{post}} \ge 0,90$ (illustratif) ; $\text{FPR}_{\text{fuite}} \le 0,02$ (illustratif) | Découverte post-coupure sans précurseur formulé *vs* résultat pré-coupure réécrit avec la terminologie post-coupure | Recherche exacte par MinHash / $n$-grammes et filtre calendaire brut |
| **Preuve formelle** | $\text{TPR}_{\text{lemme}} \ge 0,95$ (illustratif) ; $\text{FPR}_{\text{vacuité}} = 0$ (illustratif) | Lemme valide réduisant les pas de preuve sur $\mathcal{C}_{\text{test}}$ *vs* preuve compilant sur prémisse contradictoire subtile (`h : P ∧ ¬P`) | Simple vérification de typage du noyau sans test de réfutation des prémisses ni score aval |
| **Tests exécutables** | $\text{TPR}_{\text{gén}} \ge 0,95$ (illustratif) ; $\text{FPR}_{\text{sur-ajust}} \le 0,02$ (illustratif) | Loi/algorithme exact aux limites hors support *vs* table de cas mémorisant `100 %` (illustratif) des tests d'entraînement | Couverture de branches unitaire fixe sans fuzzing ni pénalité de taille d'arbre syntaxique |
| **Échantillonneur aléatoire** | Couverture grammaticale $\text{TPR} = 1,00$ (illustratif) à profondeur bornée ; $\text{FPR}_{\text{biais}} \le 0,01$ (illustratif) au test d'uniformité | Arbres syntaxiques canoniques *vs* permutations symétriques d'arbres de même taille | Tirage aléatoire brut de jetons (produisant majoritairement du code invalide) |
| **Énumérateur mécanique** | Complétude $\text{TPR} = 1,00$ (illustratif) sous le coût maximal $c_{\max}$ ; $\text{FPR}_{\text{doublon}} \le 0,02$ (illustratif) | Expressions minimales distinctes *vs* expressions réductibles par symétrie commutative ou neutre | Énumération lexicographique naïve sans élagage par équivalence observationnelle |
| **Meilleur modèle seul & Système multi-agents** | $\text{TPR}_{\text{sanité}} \ge 0,90$ (illustratif) sur cibles larges ; $\text{FPR}_{\text{dépassement-budget}} = 0$ (illustratif) | Problèmes calibrés avec et sans accès au vérificateur interne à FLOPs égaux | Appel unique sans réessai (*pass@1*) pour le modèle seul ; `BestOfN-Mono(B)` filtré mécaniquement pour le multi-agents |

---

## V. Livrable (d) — Ancrage matériel, modèles ouverts, calcul et budget

* **Modèles à poids ouverts figés** : L'utilisation exclusive de modèles à poids ouverts gelés par empreinte cryptographique garantit l'absence de dérive d'API, le contrôle de la date de pré-entraînement et le décompte exact des FLOPs ainsi que des log-vraisemblances sous $\mu_0$ `[VÉRIFIÉ]`. Configuration type :
  - *Famille principale et référence mono-modèle* : modèle généraliste ouvert de classe `72B` (illustratif) paramètres (famille Qwen ouverte) et modèle spécialisé raisonnement/code de classe `32B` (illustratif) paramètres, servis en précision flottante `16` (illustratif) bits `[OBSERVÉ-NON-AUDITÉ]`.
  - *Seconde famille ouverte indépendante (ablation d'hétérogénéité et audit croisé)* : modèle ouvert de classe `70B` (illustratif) paramètres (famille Llama ouverte) et modèle dense de classe `24B` (illustratif) paramètres (famille Mistral ouverte) `[OBSERVÉ-NON-AUDITÉ]`.
* **Pile mécanique sur CPU** : Prouveur formel Lean figé par révision Git avec tactique de recherche déterministe, moteur de saturation d'e-graphes pour le quotientage symbolique, et conteneurs isolés sans réseau pour l'exécution des simulateurs `[VÉRIFIÉ]`.
* **Dimensionnement du calcul et coûts estimés** *(tous chiffres marqués illustratifs, sur la base d'un nœud de `8` (illustratif) GPU à `80` (illustratif) Go de mémoire vidéo facturé `3` (illustratif) USD par GPU-heure et d'une grappe de `128` (illustratif) cœurs CPU)* :
  1. *Phase I (Étalonnage du harnais et `Exp. I`)* : `0` (illustratif) GPU-heure et `200` (illustratif) CPU-heures, soit `20` (illustratif) USD.
  2. *Phase II (Mondes synthétiques : `60` (illustratif) problèmes, $M_0 = 1\,000$ (illustratif) tirages courts de référence, `5` (illustratif) méthodes $\times$ `5` (illustratif) graines à budget $B = 64\,000$ (illustratif) jetons équivalents FLOPs)* : `320` (illustratif) GPU-heures et `1\,000` (illustratif) CPU-heures, soit `1\,060` (illustratif) USD.
  3. *Phase III (Déduction formelle Lean sur `80` (illustratif) modules)* : `800` (illustratif) GPU-heures et `4\,000` (illustratif) CPU-heures de vérification noyau, soit `2\,800` (illustratif) USD.
  4. *Phase IV (Campagne prospective finale sur `100` (illustratif) problèmes + ablations + `Exp. VI`)* : `2\,000` (illustratif) GPU-heures et `6\,000` (illustratif) CPU-heures, soit `6\,600` (illustratif) USD.
* **Enveloppe totale maximale** : `3\,120` (illustratif) GPU-heures et `11\,200` (illustratif) CPU-heures, soit `10\,480` (illustratif) USD au complet — mais plafonnée à `1\,080` (illustratif) USD si les portes d'arrêt des Phases I–II réfutent $H_A$.

FIN-DE-CELLULE