# Proposition B — Tour III.2 : critique croisée de méthode

---

## Sur la proposition A

### (a) Défauts de méthode

**1. Fuite structurelle entre construction et évaluation du test de reparamétrisation.**
A déclare que φ est « tirée avec graine scellée dans la classe déclarée, hors de portée du concepteur de la défense ». Mais la classe des φ (« affine aléatoire inversible composée de monotones par coordonnée ») est déclarée *par le concepteur*. Le choix de cette classe est lui-même un degré de liberté : une classe trop étroite (proches de l'identité) rend le test conservateur par construction ; une classe trop large (incluant des φ qui changent radicalement la difficulté numérique de la régression auxiliaire) peut faire chuter une défense qui a correctement appris les lois, simplement parce que la tête auxiliaire ne converge plus dans le même budget. A ne contraint pas la classe φ à préserver la difficulté d'optimisation de la tête auxiliaire ; le test confond donc « sensibilité aux coordonnées » et « instabilité d'entraînement sous reparamétrisation ».

**2. Le contrôle négatif à θ permutés ne teste pas ce qu'il prétend.**
A propose de permuter θ entre familles au bras 1 pour détruire l'information. Mais cette permutation crée un signal de supervision *contradictoire* (la tête auxiliaire reçoit la mauvaise cible), ce qui peut *dégrader* la représentation par rapport au bras 2 (pas de tête du tout). Le contrôle ne produit donc pas un « Δ ≈ 0 » attendu : il peut produire un Δ négatif, et A ne dit pas comment l'interpréter. Un contrôle plus propre serait de remplacer θ par un vecteur constant (information nulle sans signal contradictoire).

**3. Le score (iii) dépend du budget B du générateur, mais B est fixé sans critère de saturation.**
A fixe B = 500 évaluations et exige que l'écart oracle soit ≤ 2 points sur 90 % des mondes. Mais le critère de 2 points est illustratif et non relié à Δ_min = 5 points. Si l'écart oracle est de 4 points (sous les 5 de Δ_min mais au-dessus de 2), le score (iii) est biaisé vers le haut sans que le critère de A le détecte comme problème, et pourtant ce biais est du même ordre que l'effet cherché. A aurait dû exiger que l'écart oracle soit une fraction de Δ_min (par exemple ≤ Δ_min/3).

**4. Variable confondante dans la comparaison bras 1 vs bras 2 : complexité du modèle.**
Le bras 1 possède une tête auxiliaire h_w(x) → θ̂ en plus de la tête de détection. À budget d'entraînement fixe (même N_tot), les gradients de la tête auxiliaire consomment de la capacité d'optimisation. A égalise le nombre de cas mais pas le nombre de paramètres ni les pas de gradient alloués à la tête de détection seule. L'écart observé pourrait donc refléter un compromis de capacité, non l'avantage informationnel de θ.

**5. Vrai par construction : (i) − (ii) ≥ 0 sous support commun.**
A prédit (i) − (ii) ≈ 0 quand D_dep ≤ δ. C'est vrai par construction si les familles tenues à l'écart sont dans la même région : la défense a été entraînée sur cette région. Ce n'est pas un résultat, c'est une tautologie sous support commun.

### (b) Conditions sous lesquelles les mesures perdent leur puissance

**Score (i).** Perd sa puissance discriminante entre bras si toutes les familles d'entraînement sont « faciles » (KL(P_θ‖P_0) proche de κ_max). Dans ce cas, TPR_k ≈ 1 pour tous les bras et (i) est au plafond. Condition formelle : si min_k KL(P_{θ_k}‖P_0) > κ_sat (illustratif : κ_sat ≈ 1,5 pour d = 32, m = 16), la puissance du score (i) pour distinguer les bras tombe à zéro.

**Score (ii).** Non jugeable si K est trop petit pour que l'intervalle bootstrap soit inférieur à Δ_min. A fixe K = 20 (illustratif). L'écart-type d'une moyenne de 20 proportions peut être de l'ordre de 0,04–0,06 (illustratif), ce qui donne un IC de largeur ≈ 0,10 — à peine compatible avec Δ_min = 0,05. La puissance du score (ii) pour détecter un effet de 5 points avec K = 20 est faible.

**Score (iii).** Non jugeable si le paysage de TPR(θ) sur Θ est plat (variance de p_D(θ) sur Θ proche de zéro). Condition : si sup_θ p_D(θ) − inf_θ p_D(θ) < 2·Δ_min, le générateur ne peut pas trouver de θ nettement pire que la moyenne et (iii) ≈ (ii). Cela rend (ii) − (iii) ≈ 0 pour *tous* les bras, et Δ₁₂ non jugeable (puissance nulle).

**Mesure de dépendance D_dep.** A propose D_dep = moyenne des min_j KL(P_{θ_k}‖P_{θ_j}). La KL entre gaussiennes est asymétrique ; A ne symétrise pas. Si les covariances diffèrent (LLᵀ ≠ I), la KL dans un sens peut être très différente de l'autre. La mesure perd sa valeur prédictive si la dépendance réelle vient de l'alignement des directions (même L mais μ différent), cas dans lequel la KL peut être grande alors que la défense transfère bien.

**Test de reparamétrisation.** Perd sa puissance si la tête auxiliaire n'a jamais convergé (défense qui ignore θ dans la pratique même au bras 1). Dans ce cas, Δ_φ ≈ 0 pour toute φ, et le test conclut faussement que la défense a « appris les lois » alors qu'elle n'a simplement rien appris de θ. A n'a pas de diagnostic de convergence de la tête auxiliaire.

### (c) Contrôles négatifs manquants

1. **Contrôle de convergence de la tête auxiliaire** : mesurer la perte de régression ‖h_w(x) − θ‖² sur un ensemble de validation ; si elle ne descend pas sous un seuil, le bras 1 est effectivement identique au bras 2 et tout le plan est non informatif.
2. **Contrôle de capacité** : un bras 2' identique au bras 2 mais avec une tête auxiliaire dont les gradients sont calculés puis *jetés* (même coût computationnel, aucune information de θ). Si bras 1 ≈ bras 2', l'effet vient de la capacité, pas de θ.
3. **Contrôle de saturation du générateur** : lancer le générateur avec 10×B évaluations et vérifier que (iii) ne change pas de plus de 1 point (illustratif). A mentionne un oracle à 100×B mais ne le lie pas à un critère de saturation formellement vérifié avant de déclarer (iii) valide.

---

## Sur la proposition C

### (a) Défauts de méthode

**1. Choix paramétrique trop favorable : rang 1 de la perturbation de covariance.**
C déclare Σ = I_d + u·uᵀ (perturbation de rang 1). En dimension d = 64, une perturbation de rang 1 est détectable par une projection sur la direction u, ce qui rend le problème beaucoup plus facile que le cas général (perturbation de rang plein). La défense optimale est presque un test unidimensionnel. Dans ce schéma, l'avantage de connaître θ = (μ, u) se réduit à connaître la direction u, ce qui est très puissant mais ne teste pas la situation où la structure de la perturbation est diffuse. Les conclusions ne se transféreront pas à des perturbations de rang élevé, ce qui est le cas général en pratique.

**2. Incohérence dans le seuil de l'effet minimal.**
C utilise δ = 0,03 (3 points) comme effet minimal, mais ses prédictions montrent des écarts (ii) − (iii) de 0,14 à 0,30 selon les bras — soit 5 à 10 fois le seuil. Si les écarts prédits sont aussi grands, le seuil est trop facile à franchir et le plan n'a aucune puissance pour distinguer les bras entre eux au-delà de « tous positifs ». Le contraste Δ₁₂ prédit est de −0,04 (illustratif), à peine au-dessus du seuil de 0,03 ; l'écart-type inter-mondes supposé est de 0,08. Avec σ = 0,08 et effet = 0,04, la puissance d'un test t apparié sur 200 mondes est d'environ 0,63 (illustratif, calcul : n = (z_{0.975} + z_{0.9})² × σ²/δ² ≈ (1.96+1.28)² × 0.0064/0.0016 ≈ 42, donc 200 mondes suffiraient — mais la question est que l'écart-type supposé de 0,08 est très grand par rapport à un effet de 0,04).

**3. Score (iii) : réévaluation sur lots frais après optimisation, mais pas de correction pour la sélection.**
C réévalue θ̂* sur L = 200 lots frais après que le générateur l'a choisi, ce qui élimine le biais d'optimisation au niveau de l'estimation de p_D(θ̂*). C'est correct. Cependant, C utilise un IC de Clopper-Pearson sur ces 200 lots, ce qui traite θ̂* comme fixe. Or θ̂* est lui-même une variable aléatoire (il dépend des lots d'optimisation). L'IC conditionnel à θ̂* est valide pour estimer p_D(θ̂*), mais la variabilité de θ̂* entre mondes n'est pas captée par cet IC. C le reconnaît partiellement en mentionnant la « méta-analyse » sur mondes mais ne précise pas comment combiner les deux niveaux de variabilité.

**4. Le contrôle négatif (θ = 0, donc P_θ = P_0) est nécessaire mais pas suffisant.**
Ce contrôle vérifie seulement que la FAR est bien calibrée. Il ne vérifie pas que la défense détecte quelque chose. C ne propose pas de contrôle vérifiant que la défense bat la vérification mécanique sur les familles d'entraînement — elle le mentionne dans (c) mais sans l'intégrer comme condition de validité de l'expérience.

**5. Vrai par construction : score (i) élevé au bras 1.**
Au bras 1, la défense reçoit θ à l'entraînement et est évaluée sur (i) avec des tirages frais des *mêmes* familles. Si la tête auxiliaire a convergé, la représentation est optimisée pour ces θ_k spécifiques. Un score (i) élevé au bras 1 est donc attendu par construction et ne dit rien sur la valeur de l'idée.

### (b) Conditions sous lesquelles les mesures perdent leur puissance

**Score (ii) en support commun.** Si les familles tenues à l'écart tombent exactement dans les mêmes directions (μ, u) que les familles d'entraînement (D_{W_2} ≈ 0), alors (ii) ≈ (i) par construction et ne discrimine pas entre les bras. La puissance du contraste (i) − (ii) comme fonction de D_{W_2} est nulle quand D_{W_2} = 0.

**Score (iii) avec perturbation de rang 1.** Dans le schéma de C (Σ = I + uuᵀ), le pire cas du générateur est de choisir u dans la direction la moins bien couverte par la défense. Si d = 64 et la défense est un perceptron multicouche, il existe potentiellement beaucoup de directions « oubliées ». Mais si la perturbation est de rang 1, le générateur n'a que d degrés de liberté pour u (plus d pour μ). En pratique, le pire cas peut être facile à trouver par le générateur (balayage de directions), ce qui rend (iii) très bas pour *tous* les bras et Δ₁₂ non informatif parce que toutes les défenses échouent de manière similaire sur le pire cas.

**Mesure de dépendance D_{W_2}.** La distance de Wasserstein-2 entre gaussiennes est dominée par la norme des moyennes ‖μ_1 − μ_2‖ quand les covariances sont proches. Si toutes les familles ont des covariances similaires (u de même norme), D_{W_2} ne capture que la distance en moyenne, et la dépendance structurelle (alignement des directions de u) est invisible.

**Test de reparamétrisation avec sinh.** C propose φ(μ, u) = (sinh(μ), sinh(u)). Pour des valeurs modérées de μ et u (entre 0,5 et 3,0 comme déclaré), sinh est bien approximé par l'identité (sinh(0,5) ≈ 0,52, sinh(1) ≈ 1,18). La transformation est donc *presque* l'identité dans la région déclarée, et le test a une puissance très faible pour distinguer apprentissage des lois et apprentissage des coordonnées. Pour que le test soit informatif, φ doit produire des coordonnées numériquement très différentes tout en préservant les lois — ce que sinh ne fait quasiment pas dans [0,5 ; 3,0].

### (c) Contrôles négatifs manquants

1. **Contrôle de difficulté du schéma** : évaluer la vérification mécanique (test de Mahalanobis ou MMD) sur le schéma de rang 1 et vérifier qu'elle ne sature pas déjà (si le test fixe atteint 95 % de détection, la défense apprise n'a plus de marge pour montrer un avantage).
2. **Contrôle de rang** : répéter l'expérience avec une perturbation de rang plein (Σ = LLᵀ quelconque) pour vérifier que les conclusions tiennent hors du cas favorable rang 1.
3. **Contrôle de convergence de la tête auxiliaire** (même défaut que A) : C n'en propose pas. Sans lui, on ne peut pas savoir si le bras 1 utilise effectivement l'information θ.

---

## Sur la proposition D

### (a) Défauts de méthode

**1. Le mode déclaré (« entrée auxiliaire distillée ») est ambigu.**
D écrit que θ est « une entrée auxiliaire présente à l'entraînement seulement, distillée dans une défense opérationnelle qui ne reçoit ensuite que des activations ». Le mot « distillée » ne spécifie pas le mécanisme : est-ce une cible à prédire (comme A et C le déclarent), un signal de supervision supplémentaire dans la perte, une régularisation, ou autre chose ? Cette ambiguïté rend le bras 1 de D sous-spécifié. On ne peut pas savoir si le test de reparamétrisation est informatif sans connaître le mécanisme exact par lequel θ influence les poids.

**2. Le contrôle négatif du duel 1 est mal construit.**
D propose de « répéter le contraste entre deux évaluations du même bras 2, avec graines indépendantes ». Ce contrôle teste la stabilité de l'estimateur, pas l'absence d'effet de θ. Le bon contrôle serait de comparer le bras 1 à un bras 1 où θ est remplacé par un signal non informatif (vecteur constant ou aléatoire indépendant). Si deux copies du bras 2 franchissent δ, cela peut venir d'un écart-type inter-graines trop grand, pas d'un biais — ce qui informerait sur la puissance du plan, pas sur la présence de fuite.

**3. Le duel 2 exige un « réentraînement complet » sous φ(θ), mais D ne contrôle pas la variabilité du réentraînement.**
Deux entraînements complets avec des graines différentes (même θ, même architecture) peuvent donner des défenses différentes. D ne propose pas de mesurer la variabilité inter-réentraînement à φ = identité. Sans cette mesure, on ne peut pas distinguer l'effet de φ de la variabilité naturelle de l'entraînement. Il faudrait au minimum plusieurs réentraînements sous identité pour estimer σ_retrain.

**4. Le budget matériel est incohérent avec les autres propositions et potentiellement irréaliste.**
D annonce 2×10⁹ vecteurs synthétiques de dimension 16, 4 000 heures-CPU et 300–800 €. A et C annoncent 130 h-CPU et 15–40 € pour des plans comparables. L'écart d'un facteur 30 sur les heures-CPU n'est pas expliqué. Soit D surestime massivement le coût (ce qui n'est pas grave mais signale un manque de calibration), soit D prévoit un plan beaucoup plus lourd sans le justifier. En dimension d = 16 (vs 32 ou 64 chez A et C), le calcul devrait être *moins* cher, pas plus.

**5. Variable confondante potentielle : la mesure de dépendance est symétrisée, les autres ne le sont pas.**
D propose D_dep = moyenne de (KL(P_j‖P_k) + KL(P_k‖P_j))/2, qui est la divergence de Jeffreys. C'est une bonne pratique (corrige l'asymétrie notée chez A), mais D ne vérifie pas que cette mesure est monotone avec la difficulté de transfert. Si la divergence de Jeffreys augmente mais que le score (ii) ne diminue pas (parce que les familles tenues à l'écart sont plus faciles intrinsèquement, non pas plus éloignées), la régression monotone proposée sera mal spécifiée.

**6. Score (iii) : pas de critère de saturation du générateur.**
D mentionne un regret ρ et exige ρ → 0, mais ne fixe pas de seuil quantitatif lié à l'effet minimal δ_E = 0,03. Si ρ = 0,04 (illustratif), le biais du score (iii) est du même ordre que l'effet cherché, et Δ₁₂ est non jugeable. A fixe un seuil (2 points, quoique mal calibré) ; D ne le fait pas.

### (b) Conditions sous lesquelles les mesures perdent leur puissance

**Score (ii).** D ne fixe pas K (nombre de familles tenues à l'écart). Si K est petit, l'IC bootstrap est large et la puissance s'effondre. Condition : si K < (z_{0.975}/Δ_min)² × σ²_inter-familles (illustratif : σ = 0,10, Δ_min = 0,03 → K > 43), le score (ii) est non jugeable.

**Score (iii).** D dit « confirmé sur tirages frais » mais ne donne pas le nombre de tirages. Sans cette spécification, on ne peut pas borner le bruit d'estimation de p_D(θ̂*). Si la confirmation est faite sur 50 lots (illustratif), l'IC binomial est de largeur ≈ 0,06, et un effet de 0,03 n'est pas détectable.

**R = G_2 − G_1.** D prédit R ≥ δ_E sous support commun mais admet que le signe peut s'annuler ou s'inverser sous support disjoint. C'est honnête, mais cela signifie que le duel 1 n'est informatif que dans un seul régime. Si le programme vise l'universalité (fait 1), le régime pertinent est le support disjoint, précisément celui où D n'a pas de prédiction claire.

**Test de reparamétrisation.** D exige un « réentraînement complet ». Si le budget est limité et que le réentraînement ne converge pas au même point, la variabilité masque l'effet de φ. Condition : si σ_retrain > ε = 0,02 (le seuil de D), le test est non jugeable.

### (c) Contrôles négatifs manquants

1. **Contrôle de variabilité inter-réentraînement** : plusieurs réentraînements à φ = identité pour estimer σ_retrain. Sans celui-ci, le duel 2 est non jugeable.
2. **Contrôle de saturation du générateur** : lancer le générateur à B et 10×B et vérifier la stabilité de (iii). D mentionne le concept (regret) mais ne l'intègre pas comme pré-condition de validité.
3. **Spécification du mécanisme de distillation** : sans elle, on ne peut pas construire le contrôle de capacité (bras 2 avec même coût computationnel que le bras 1, information de θ détruite). D ne propose pas ce contrôle.
4. **Contrôle de difficulté contrôlée** : D prédit que (i) − (ii) croît avec D_dep « à difficulté moyenne contrôlée », mais ne dit pas comment contrôler la difficulté moyenne. Il faudrait un monde où D_dep est imposé mais la difficulté moyenne (par exemple KL moyen des familles) est identique entre entraînement et tenues à l'écart.

---

FIN-DE-CELLULE