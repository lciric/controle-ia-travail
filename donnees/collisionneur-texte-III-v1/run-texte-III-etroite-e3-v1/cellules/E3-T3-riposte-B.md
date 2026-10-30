

# Proposition B — Tour III.3 : réponse aux critiques

---

## Partie (a) — Traitement de chaque critique adressée à B

J'examine séparément les critiques des propositions A, C et D.

### Critiques de la proposition A sur B

**A-1. Sens inversé de la déviance / affectation des recaptures.** *Acceptée.* A a raison : placer la plus grande recapture (17) sur la paire dont l'attendu sous indépendance est le plus grand (S₂×S₃, les deux plus grosses sources) *réduit* l'écart observé-attendu, donc *minimise* la déviance. J'avais écrit l'inverse. Le calcul est fermé et refaisable ; je le corrige dans la version révisée.

**A-2. Formule de Chao mal attribuée et facteur (T−1)/T omis.** *Acceptée.* Pour T = 3 sources d'incidence, la formule correcte est N̂ = D + ((T−1)/T) · f₁²/(2f₂) = 37 + (2/3)·(256/14) ≈ 37 + 12,19 ≈ 49,19. Ma valeur de 55,3 omet ce facteur et surestime f₀ de ~50 % sous M₀, comme C le démontre analytiquement. La référence correcte est Chao 1987 pour la forme d'incidence ; la formule sans facteur correspond à Chao 1984 (abondance). Je corrige.

**A-3. Fuite entre instrument et évaluation dans le bloc 2 (n_eff).** *Acceptée.* La substitution n_eff = n/(1+(n−1)ρ) dans la formule exponentielle du fait 9 n'est pas dérivable : le facteur de Kish corrige la variance d'une moyenne linéaire, pas P(zéro échec) sous corrélation échangeable. Le chiffre ε ≤ 0,31 est donc non fondé. Je le retire et le remplace par une approche par simulation directe.

**A-4. Règle d'arrêt à niveau non contrôlé.** *Acceptée.* L'arrêt « jusqu'à ce que la borne soit < ε₀ ou que la largeur stagne » constitue un arrêt optionnel sans dépense d'α. Le niveau réel dépasse α. Je remplace par une procédure à dépense d'α fixée (alpha-spending de Lan-DeMets, référence à vérifier).

**A-5. Sélection de modèle sans incertitude de sélection.** *Acceptée.* Avec des cellules de taille 2 ou 3, le saut de N̂ entre modèles candidats domine l'IC conditionnel. Je remplace par une moyenne bayésienne sur modèles (BMA) qui propage l'incertitude de sélection dans l'IC sur N.

**A-6. Duel 1 non exclusif (zone 0,85–0,95).** *Acceptée.* Je resserre : H_A : couverture ≥ 0,90 ; H_B : couverture < 0,90. La zone morte disparaît. L'estimateur ajusté de H_B est désormais spécifié (voir duel révisé).

**A-7. Confrontation 1 confondue.** *Acceptée.* La prédiction (N̂ − 37)/N̂ suppose un tirage uniforme par la source extérieure. Sous hétérogénéité, la part nouvelle observée dépend de la covariance entre probabilités de capture interne et externe. Je remplace par deux prédictions parallèles : l'une sous uniformité (1 − 37/N̂), l'autre sous la couverture de Good-Turing (1 − Ĉ), avec un test qui discrimine les deux.

### Critiques de la proposition C sur B

**C-1. Erreur de formule Chao (facteur (T−1)/T).** *Acceptée* — identique à A-2, déjà traitée.

**C-2. Confusion biais / borne inférieure dans le duel 2.** *Acceptée.* Chao est construit comme borne inférieure, non comme estimateur sans biais. Exiger un biais ≤ 5 % contredit sa vocation. De plus, sous M_h symétrique, un modèle log-linéaire à une ou deux interactions de paire est mal spécifié (u₁₂₃ ≠ 0). Je reformule le duel 2 pour comparer la *couverture de la borne* (P(N̂ ≤ N) ≥ 1−α) plutôt que le biais.

**C-3. Règle d'arrêt séquentielle convergeant vers une sous-population.** *Acceptée.* La critique formalise précisément mon erreur : sous censure commune (κ > 0), le plateau de découverte certifie à tort la sous-population facile. *Transformée en contrôle négatif* obligatoire (voir expériences révisées).

**C-4. Omission de la variance intra-famille.** *Acceptée.* Mon bloc 2 tirait un indicateur binaire par famille sans modéliser m éléments par famille. J'ajoute un niveau intra-famille dans le modèle génératif.

### Critiques de la proposition D sur B

**D-1. Hypothèse a4 erronée.** *Acceptée en partie.* D a raison que M₀ autorise des probabilités propres aux sources ; l'échangeabilité des familles n'est pas requise par tous les modèles. Je clarifie : a4 signifiait que l'estimateur de Chao suppose l'échangeabilité des familles (non des sources), ce qui est correct pour M_h, mais la formulation était imprécise.

**D-2. Duel 1 mélange deux estimands.** *Acceptée.* Chao estime N_accessible, pas la couverture de la borne sur ε. Le lien entre les deux nécessite un modèle de la relation entre capture et échec, que je n'avais pas spécifié. Corrigé dans la version révisée.

**D-3. Duel 2 confond validité de borne et absence de biais.** *Acceptée* — identique à C-2.

**D-4. Recaptures spéculatives.** *Acceptée partiellement.* L'usage de nⱼ/37 comme probabilités supposait N = 37 implicitement, ce qui est contradictoire. Je corrige en posant des probabilités conditionnelles au point fixe N̂.

**D-5. AIC/BIC sans incertitude.** *Acceptée* — identique à A-5.

---

## Partie (b) — Expériences corrigées

### Duel 1 révisé — Couverture de la borne sur ε sous découverte dépendante

**H_A** : La borne supérieure sur ε, calculée par inversion d'un modèle bêta-binomial ajusté sur les familles découvertes, maintient une couverture ≥ 0,90 sur toute la grille {ρ ∈ {0, 0,10, 0,25}, CV ∈ {0, 0,5, 1,0}} (valeurs illustratives).

**H_B** : Il existe au moins une cellule de la grille où cette couverture tombe sous 0,90, tandis que la borne naïve du fait 9 (sous i.i.d.) est déjà sous 0,80.

- **Métrique** : couverture empirique sur 10 000 mondes simulés (illustratif) par cellule, à N, ε fixés (vérité connue).
- **Seuil** : couverture < 0,90 sur la borne bêta-binomiale.
- **Contrôle négatif** : ρ = 0, CV = 0 (monde i.i.d.) ; la borne bêta-binomiale doit couvrir ≥ 0,93. Monde à censure commune (κ = 0,20, illustratif) : la borne doit couvrir ε sur la sous-population accessible et ne pas prétendre couvrir la population totale.
- **Falsification** : H_A fausse → la borne bêta-binomiale est insuffisante, il faut un modèle plus riche. H_B fausse → la borne naïve résiste à la dépendance modérée, la correction est superflue.

### Duel 2 révisé — Couverture de la borne inférieure sur N

**H_A** : Sous M_h (hétérogénéité pure, CV ∈ {0,5 ; 1,0}, illustratif), la borne de Chao2 corrigée (facteur (T−1)/T) satisfait P(N̂_Chao ≤ N) ≥ 0,95, et la moyenne bayésienne sur modèles log-linéaires (BMA) donne un IC dont la couverture est aussi ≥ 0,90.

**H_B** : Sous M_th (hétérogénéité + dépendance conditionnelle de paire, θ_{st|f} ≥ 2, illustratif), P(N̂_Chao ≤ N) < 0,80, tandis que la BMA maintient ≥ 0,85.

- **Métrique** : P(estimateur ≤ N) et largeur médiane de l'IC, sur 5 000 réplications (illustratif).
- **Contrôle négatif** : M₀ (homogène, indépendant) ; les deux approches doivent couvrir ≥ 0,93.
- **Contrôle négatif additionnel (C-3)** : monde à u₁₂₃ > 0 par facteur latent continu ; la BMA doit signaler l'instabilité de N̂ (IC large) plutôt que converger sur une valeur fausse.
- **Falsification** : H_A fausse → Chao2 perd sa propriété de borne sous hétérogénéité, ce qui contredirait le résultat théorique connu (indique un bogue de simulation). H_B fausse → la dépendance de paire ne compromet pas Chao2, le modèle log-linéaire est inutile.

### Instrument 1 révisé — Estimateur des familles inconnues

Plan de simulation comme au tour III.1, avec corrections :

- **Facteur (T−1)/T** appliqué à Chao2.
- **Variance intra-famille** : chaque famille contient m éléments (m ∈ {20, 100}, illustratif) ; l'échec est tiré par élément avec P(échec | famille f) = θ_f ~ Beta(a, b).
- **BMA** sur modèles log-linéaires à 0, 1, 2 interactions de paire, IC intégrant l'incertitude de sélection.
- **Erreur d'appariement** : taux de fusion ∈ {0, 0,05}, scission ∈ {0, 0,05} (illustratif).
- **Censure commune** (κ ∈ {0, 0,10, 0,20}, illustratif) : l'estimand est N_accessible = N(1−κ), pas N total.
- **Couverture rapportée comme le minimum sur l'enveloppe** des cellules (ρ, CV) compatibles avec la configuration (f₁, f₂, f₃) observée, conformément à la remarque transversale de A.

### Instrument 2 révisé — Mesure d'universalité

- **Modèle génératif à deux niveaux** : (i) tirer N familles avec probabilités de capture hétérogènes et corrélées ; (ii) pour chaque famille capturée, tirer m éléments, observer θ̂_f ; (iii) estimer ε̂ (proportion de familles où θ̂_f > τ), avec IC bêta-binomial.
- **Règle d'arrêt séquentielle** : dépense d'α par paliers préenregistrés (par exemple 3 regards à α₁ = 0,001, α₂ = 0,01, α₃ = 0,044, illustratif, dépense totale 0,05). Pas d'arrêt au « plateau ».
- **Contrôle négatif C-3 (censure commune)** : monde à κ = 0,20, ε_accessible = 0, ε_total = 0,20 ; la procédure ne doit pas certifier ε < 0,10.
- **Contrôle négatif C-4 (faux positifs intra-famille)** : monde à ε = 0, θ_f = τ − 0,005 pour tout f, m = 20 ; mesurer le taux de fausse certification.

---

## Partie (c) — Réponse à la question de l'arbitre (une page)

### Définition retenue

**Quantificateur, classe, statistique** : « Avec confiance 1 − α, la proportion de familles de la classe C (définie par un schéma de construction déclaré avant la mesure) où la défense échoue (θ_f > τ sur m éléments) est au plus ε. » Déclaration préalable : C (schéma), τ, ε, α, m minimum par famille. Ce qui n'est pas autorisé : affirmer l'universalité hors de C, ni sur des familles à censure commune sans le signaler. Un tiers recalcule en appliquant le même seuil τ à ses propres familles de C.

### Estimateur retenu et résultat sur les données de départ

**Estimateur du nombre de familles** : Chao2 corrigé, N̂ = 37 + (2/3)·f₁²/(2f₂) = 37 + (2/3)·(256/14) ≈ 49,2 (calcul sur données RAPPORTÉ, fait 17). IC par BMA sur modèles log-linéaires à 0, 1 et 2 interactions de paire : étendue illustrative [44 ; 68] (ces bornes sont illustratives ; le calcul exact requiert l'ajustement sur les sept cellules avec affectation des recaptures). L'affectation la plus compatible avec la déviance rapportée de 12,9 (fait 17, RAPPORTÉ) place 17 sur (S₂, S₃), les deux plus grandes sources, minimisant la déviance à ~12,85 (recalcul de A, refaisable). Couverture de Good-Turing : Ĉ = 1 − 16/72 = 0,778, soit une proportion estimée non couverte de 22,2 % (sous la loi de capture des trois sources — ne se transpose pas directement à une source extérieure).

**Ce qui est établi** :
- La cohérence arithmétique des comptes (VÉRIFIÉ, fait 18).
- La borne à zéro échec sous i.i.d. (VÉRIFIÉ, fait 9) et son invalidité pour des familles découvertes (fait 9, explicite).
- Le rejet de l'indépendance entre sources (déviance 12,9 / 3 ddl, RAPPORTÉ).

**Ce qui n'est pas établi** :
- Le décompte et l'appariement eux-mêmes (RAPPORTÉ, lecteur unique).
- La fermeture de la population (HYPOTHÈSE a3).
- La distinction entre hétérogénéité et dépendance conditionnelle avec seulement trois sources (remarque transversale de A, confirmée ici).
- L'absence de censure commune (HYPOTHÈSE non testable sans information auxiliaire).
- Le nombre exact de familles inconnues : tous les estimateurs (Chao2, log-linéaires, BMA) sont des constructions conditionnelles à a3 et à l'absence de censure commune ; leur propriété de borne inférieure ne survit pas à une dépendance conditionnelle arbitraire entre sources.

### Nombre de familles nécessaire et règle de calcul

Sous le modèle bêta-binomial à deux niveaux (entre-familles : ρ ; intra-famille : m éléments), le nombre de familles nécessaire est déterminé par simulation : fixer (ε, α, ρ, CV, m), simuler 10 000 mondes, trouver le n minimal tel que la couverture de la borne sur ε soit ≥ 1 − α. Le fait 9 donne une borne inférieure sur n sous i.i.d. (29 pour ε = 0,10) ; sous dépendance, n sera substantiellement plus grand — la quantification exacte est le livrable de la simulation, non une formule fermée.

### Validation extérieure (cinq lignes)

Source extérieure E décrite uniquement par : taille n_e (illustratif : 30), indépendance supposée vis-à-vis des trois sources, probabilité de capture p_e inconnue. Prédiction scellée 1 : proportion de familles de E hors des 37 observées, avec deux cibles parallèles — uniforme (1 − 37/N̂ ≈ 0,25, illustratif) et Good-Turing (0,22). Si la proportion observée est significativement supérieure aux deux (test binomial, α = 0,05), les deux estimateurs sont falsifiés (censure commune ou N beaucoup plus grand). Prédiction scellée 2 : performance de la défense sur E ne diffère pas de celle sur les familles observées de plus de δ (illustratif : 0,15) ; falsifié si p < 0,05 sur test exact avec n_e = 30.

### Expérience à faire en premier

Simulation à vérité connue du duel 2 révisé (couverture de Chao2 corrigé vs. BMA log-linéaire), sur une grille croisant hétérogénéité et dépendance conditionnelle, avec le contrôle négatif de censure commune : c'est le seul test qui tranche si la borne inférieure sur N est fiable avant de fonder toute mesure d'universalité sur elle.

FIN-DE-CELLULE