# Proposition A — Tour III.3 : réponse aux critiques

Les trois pièces de critique (B, C, D) sont présentes et complètes ; je ne réponds qu'à leurs sections « Sur la proposition A ». Notation : B-a2 = pièce B, section (a), point 2 ; D-c3 = pièce D, section (c), point 3. Tout chiffre ci-dessous qui ne vient pas des faits est illustratif ; les statuts des faits sont inchangés.

## (a) Pour chaque critique : acceptée, rejetée, ou transformée en test

### Couplage des trajectoires des bras 1 et 2 (C-a1, C-c3, D-a1, D-c2)

**Acceptée.** « Mêmes familles, mêmes graines » est incompatible avec une boucle où chaque bras a sa défense : dès g = 2, le générateur du bras 2 ne peut répondre à la défense du bras 2 tout en produisant les familles du bras 1. Correction (en (b)) : le contraste principal se mesure sur une **trajectoire commune**, produite par un générateur qui joue contre une défense pilote tierce (entraînée sur banque fixe, hors contraste) ; l'adaptation propre à chaque bras devient un **facteur secondaire** mesuré par rejeu croisé (bras 1 sur la trajectoire propre du bras 2 et inversement). Je dis ce que cela coûte : sur la trajectoire commune, la boucle n'est plus adaptative aux défenses comparées ; c'est le prix de l'identifiabilité de l'effet de θ.

### Biais de sélection du score (iii) (C-a3, C-b1, C-c1, D-a2, D-c1)

**Acceptée.** Le minimum de B estimations binomiales est biaisé vers le bas ; le biais d'extrême, d'ordre √(2 ln B · p(1−p)/n), est de l'ordre de 2,5 points pour B = 500, n = 2 000, p ≈ 0,7 (illustratif, refaisable) : comparable à Δ_min. Et C-b1 a raison : une surface plus plate au bras 2 gonfle artificiellement Δ₁₂. Correction : θ̂* est **réévalué sur n_frais = 10⁴ cas à graine neuve** ; (iii) est cette réévaluation. Mon contrôle « défense aléatoire → (iii) ≈ 1 % » était faux sans réévaluation ; il devient un **contrôle du biais** : sans réévaluation, (iii) doit chuter sous 1 % ; avec, rester à 1 % ± 0,3 (illustratif). J'ajoute le monde à surface connue et constante de D-c1.

### Générateur : oracle non garanti, critère de saturation non relié à Δ_min, regret asymétrique (B-a3, B-c3, D-a3, D-b3)

**Partiellement rejetée, partiellement transformée en test.** Rejet sur un point : la question définit (iii) comme le pire cas **mesuré à budget B déclaré**, non l'infimum ; je renomme donc mon « oracle » **référence à 100 B**, qui ne certifie rien pour une surface non convexe (D-a3 accepté). Transformé en test : critère de saturation **lié à Δ_min** : (iii)(B) − (iii)(10 B) ≤ Δ_min/3 sur 90 % des mondes, par bras (illustratif) ; si le regret estimé diffère entre bras 1 et bras 2 de plus de Δ_min/3, Δ₁₂ est **non jugeable** : cela couvre l'asymétrie des bassins (D-b3). Ce diagnostic ne prouve pas que le pire cas est atteint ; il borne ce que le chiffre publié prétend.

### Contrôle à θ permutés, capacité, convergence de la tête (B-a2, B-a4, B-c1, B-c2, D-c3)

**Acceptées toutes les quatre.** La permutation crée un signal contradictoire (B-a2) ; la tête auxiliaire change la capacité et les pas de gradient (B-a4) ; sans convergence de la tête, le bras 1 est le bras 2 (B-c1) ; la permutation seule ne sépare pas information et régularisation (D-c3). Correction : **le bras 2 est implémenté comme le bras 2′ de B** (tête présente, gradients calculés puis jetés : même architecture, même coût, aucune information de θ) ; triptyque de contrôle : bras 1-perm (cible permutée), bras 1-const (cible constante), bras 2-sans-tête. Préconditions : bras 1-perm et bras 1-const à moins de Δ_min/2 du bras 2′ sur (ii) ; **R² de la tête auxiliaire sur validation ≥ 0,5** (illustratif), sinon le plan est non informatif.

### Test de reparamétrisation (B-a1, B-b-test, C-a4, C-c2, D-a4, D-b5)

- **Non-identifiabilité de (μ, L)** (D-a4) : **acceptée**. L n'est pas une fonction de la loi (LQ ≡ L). Correction : cible canonique **θ = (μ, L_Chol)** avec L_Chol facteur de Cholesky à diagonale strictement positive, unique ; le schéma devient identifiable et φ opère sur cette cible.
- **Conditionnement de la perte quadratique sous φ** (C-a4, B-a1, D-b5) : **acceptée**. Correction : la cible φ(θ_k) est **blanchie** sur les familles d'entraînement (moyenne 0, covariance I) et la perte auxiliaire est normalisée par sa valeur initiale. Conséquence déclarée : toute φ affine est neutralisée par construction ; le test n'est informatif que par la composante **non linéaire monotone**, dont l'intensité (écart en norme à la meilleure affine, après blanchiment) est déclarée d'avance à deux niveaux.
- **Contrôle d'isométrie** (C-c2) : **accepté** ; φ = Q orthogonale → Δ_φ attendu ≈ 0.
- **Classe φ choisie par le concepteur** (B-a1) : **transformée en test** : la classe est scellée dans le préenregistrement, et le duel 2 n'est jugeable que si, **avec la même φ**, le témoin T_param chute ≥ Δ_min et le témoin T_lois ne chute pas ; sinon la classe est inadéquate et le duel est déclaré non jugeable, pas tranché.
- **Variabilité du réentraînement** : j'ajoute σ_retrain estimé sur 5 réentraînements à φ = identité ; test non jugeable si σ_retrain > Δ_min/2 (illustratif).
- **Tête non convergée → faux « a appris les lois »** (B-b) : **acceptée**, couverte par la précondition R² ≥ 0,5.

### Mesure de dépendance D_dep (B-a5, B-b-D_dep, C-b2, D-a5, D-b2, D-b4)

- **Asymétrie de la KL** (B-b) : **acceptée** ; D_dep devient la **divergence de Jeffreys** au plus proche voisin, forme close.
- **Couverture, non dépendance probabiliste** (D-a5) : **acceptée sur le nom, rejetée sur la demande**. Une dépendance entre familles conçues par des tiers n'est pas définissable au niveau des lois sans modèle de leur conception, qui est hors tour. Ce que je mesure est une **couverture** et je l'appelle ainsi ; c'est ce que la question demande (« au niveau des lois et des paramètres seulement »).
- **Mon contrôle négatif était inversé** (D-a5) : **accepté**. Retirer les familles de la région fait croître D_dep, non tendre vers 0. Correction : trois mondes de validation de l'instrument, comme D le demande à B : recopie (D_dep = 0 exactement), tirages indépendants de même marginale (D_dep petit), régions disjointes (D_dep grand).
- **Inversion du signe de β** (C-b2, D-b2) : **acceptée, transformée en test**. Les familles tenues à l'écart peuvent être plus loin de P_0, donc plus faciles. Correction : **appariement de difficulté** : les familles tenues à l'écart sont tirées par rejet pour reproduire la distribution de KL(P_θ‖P_0) des familles d'entraînement, dans les deux régimes ; la régression de (i) − (ii) sur D_dep n'est prédite monotone que sous appariement ; je ne revendique aucun coefficient transportable hors des mondes simulés (D-b2 accepté).
- **Estimateur plug-in singulier** (C-b2) : **accepté**. Dans la simulation, D_dep se calcule sur les θ vrais ; l'estimateur par échantillons ne sert qu'à qualifier l'instrument, sur n·m ≥ 10 d² vecteurs (32 000 pour d = 32, n = 2 000, m = 16, refaisable) avec rétrécissement de la covariance ; le biais du minimum sur j est mesuré sur les mondes à niveau connu.
- **Alignement de directions invisible à la KL** (B-b) : **accepté** ; seconde mesure de couverture déclarée : cosinus maximal entre la direction de déplacement de la famille tenue à l'écart (μ_k, et vecteur propre principal de Σ_k − I) et celles des familles d'entraînement ; régression sur les deux mesures.
- **« (i) − (ii) ≈ 0 sous support commun est une tautologie »** (B-a5) : **rejetée**. Une défense peut surajuster les 40 familles individuelles même à l'intérieur de leur région (K fini) ; la prédiction est falsifiable par un (i) − (ii) ≥ Δ_min sous support commun. J'accorde qu'elle contrôle l'instrument, non l'idée.

### Fuite par la sélection sous support commun (C-a2)

**Rejetée pour l'essentiel, acceptée sur un point.** Sous support commun, les familles tenues à l'écart sont par définition dans la région d'entraînement ; sélectionner sur une partition de validation de cette région n'utilise pas les familles tenues à l'écart et c'est précisément ce que le régime mesure ; la généralisation hors région est l'objet du régime disjoint. Point accepté : sélectionner sur la perte auxiliaire favoriserait la prédiction de θ. Correction : **sélection sur la perte de détection seule** (TPR à 1 % FAR sur validation) ; le coefficient de la perte auxiliaire est fixé d'avance, non sélectionné.

### Saturation des surfaces (B-b-(i), B-b-(iii), D-b1)

**Acceptées, transformées en préconditions.** Un pilote de 20 mondes (hors des W mondes de mesure) vérifie que, sous la vérification mécanique T, le TPR moyen des familles d'entraînement est dans [30 %, 90 %] et que l'étendue sup − inf de p(θ) sur une grille uniforme de Θ est ≥ 2 Δ_min (illustratif) ; sinon κ_min, κ_max sont ajustés avant la boucle et déclarés.

### K = 20 trop petit pour (ii) (B-b-(ii))

**Acceptée.** K passe à 50 (illustratif). J'ajoute que le bruit inter-familles de (ii) est partagé par les cinq bras dans un monde apparié (mêmes familles tenues à l'écart pour tous) et se soustrait dans Δ₁₂, dont l'unité est le monde ; K = 50 sert à lire (ii) seul.

### Cécité du palier rapide du bras 5 (C-b3)

**Acceptée.** Correction : le palier rapide comprend aussi des règles d'énergie globale (norme de l'écart de moyenne estimé, trace de l'écart de covariance), et une règle par direction propre n'est gardée que si ses directions sont stables entre deux lots (recouvrement ≥ 0,8, illustratif) sur au moins deux familles. Le contrôle « palier rapide gelé dans un état neutre doit reproduire le bras 1 à graine égale » est maintenu.

### Étalonnage et audit des fausses alertes sur cas honnêtes distincts (D-c4)

**Acceptée.** 10⁵ cas honnêtes pour étalonner τ, 10⁵ autres à graine distincte pour l'audit, tolérance [0,8 %, 1,2 %] ; un bras hors tolérance est non comparable.

## (b) Expériences corrigées

**Cadre (déclaré, illustratif).** d = 32, P_0 = N(0, I), P_θ = N(μ, L_Chol L_Cholᵀ), θ = (μ, L_Chol) identifiable, Θ = {κ_min ≤ KL(P_θ‖P_0) ≤ κ_max} avec κ fixés par le pilote. Cas = m = 16 vecteurs ; τ = quantile 0,99 sur 10⁵ honnêtes ; audit FAR sur 10⁵ autres. Mode : θ cible auxiliaire blanchie, h_w(x) → θ̂, coefficient de perte fixé ; sélection sur TPR de validation seul.

**Unité de budget.** N_tot = cas consommés par la défense (entraînement + sélection), identique pour tous les bras, y compris les évaluations faites par le générateur dans les boucles, comptées dans N_tot pour les bras 1, 2, 4, 5 et remplacées par autant de cas de banque au bras 3 (réponse à l'asymétrie que C reproche à B et qui s'appliquait aussi à moi). Illustratif : G = 8, M = 5, 500 cas/famille, N_tot = 4·10⁴.

**Facteur trajectoire.** T_commune : un générateur joue contre une défense pilote tierce ; les bras 1, 2, 5 reçoivent ces familles. T_propre : chaque bras a son générateur ; rejeu croisé 1↔2.

**Bras (tous sur T_commune ; 1 et 2 aussi sur T_propre).**
1. Boucle ; θ blanchi comme cible + échantillons.
2. Boucle ; tête présente, gradients jetés (= 2′ de B) ; échantillons seuls.
3. Banque fixe de 40 familles ; échantillons seuls.
4. Boucle, protocole du champ (faits 6–8, RAPPORTÉ) : le générateur clôt chaque génération contre la défense du moment ; échantillons seuls.
5. Boucle ; θ ; deux paliers, palier rapide corrigé (énergie globale + directions stables, règles validées sur ≥ 2 familles) ; tout figé avant (ii) et (iii).

**Contrôles (tous à budget N_tot).** 1-perm ; 1-const ; 2-sans-tête ; défense aléatoire avec et sans réévaluation fraîche ; monde à surface p constante soumis au générateur ; φ = Q orthogonale ; φ = identité × 5 graines (σ_retrain) ; mondes de couverture : recopie / même marginale / disjoint ; bras 5 à palier rapide gelé.

**Score (iii) corrigé.** Générateur à B = 500, 5 redémarrages ; θ̂* réévalué sur 10⁴ cas frais ; saturation B vs 10 B par bras.

**Régimes.** Support commun : familles tenues à l'écart (K = 50) tirées dans la région d'entraînement, graine scellée, **appariées en KL(P_θ‖P_0)** par rejet. Support disjoint : coordonnées 17..32 et structure de L distincte, même appariement.

**Reparamétrisation.** φ scellée, appliquée aux cibles à l'entraînement, défense réentraînée ; composante affine neutralisée par blanchiment ; intensité non linéaire déclarée à deux niveaux ; jugeabilité conditionnée aux témoins T_lois et T_param testés avec la même φ.

**Préconditions de jugeabilité (toutes illustratives).** FAR audité dans [0,8 ; 1,2] % ; R² de la tête ≥ 0,5 au bras 1 ; |1-perm − 2′| et |1-const − 2′| < Δ_min/2 ; (iii)(B) − (iii)(10B) ≤ Δ_min/3 par bras et différence inter-bras ≤ Δ_min/3 ; σ_retrain ≤ Δ_min/2 ; témoins φ séparés ; étendue de p(θ) ≥ 2 Δ_min au pilote.

**Duels corrigés.**
- *Duel 1.* Δ₁₂ = [(ii)−(iii)]₂′ − [(ii)−(iii)]₁ sur T_commune, (iii) réévalué frais, W mondes appariés. H_A : Δ₁₂ ≥ Δ_min = 5 points ; H_B : Δ₁₂ < Δ_min (zone [0, Δ_min[ comprise dans H_B, ce qui ferme la zone que D reproche à B). IC t apparié à 95 % ; borne inférieure ≥ Δ_min → H_B falsifiée ; borne supérieure < Δ_min → H_A falsifiée ; sinon non concluant, et je le dis.
- *Duel 2.* Δ_φ = (ii)[θ] − (ii)[φ(θ)] et même chose sur (iii), au bras 1, φ non linéaire. H_A : |Δ_φ| < Δ_min ; H_B : Δ_φ ≥ Δ_min ; mêmes règles d'IC ; non jugeable si une précondition φ échoue.
- *Duel 3 (facultatif).* (iii)₅ − (iii)₁, seuil Δ_min, contrôle palier gelé.

**Plan de puissance (sans résultat).** W = 200 mondes, effet supposé 5 points, σ inter-mondes supposé 4 points ; pilote de 20 mondes pour ajuster W et κ ; conditions : (5 bras + 3 contrôles d'information) × 2 régimes × 2 φ sur T_commune, plus 2 × 2 rejeux sur T_propre.

**Prédictions révisées (HYPOTHÈSE, illustratif, points de détection à 1 % FAR, T_commune, (iii) frais).** La réévaluation fraîche retire ≈ 2 à 3 points de biais ; les écarts baissent sans changer d'ordre.

| Bras | (ii)−(iii) commun | (ii)−(iii) disjoint |
|---|---|---|
| 1 | +6 | +12 |
| 2′ | +9 | +15 |
| 3 | +12 | +17 |
| 4 | +8 | +13 |
| 5 | +4 | +10 |

Signe : toutes positives ; disjoint > commun ; bras 1 < bras 2′ (Δ₁₂ ≈ +3, donc sous Δ_min : je maintiens que l'effet « évaluation » risque de ne pas atteindre le seuil).

**Ancrage matériel révisé (illustratif).** Conditions ≈ 2,5 fois plus nombreuses qu'au III.1 ; réévaluation fraîche et 10 B sur une fraction des mondes ; ≈ 350 heures-processeur, coût cloud ≈ 40–100 €.

## (c) Réponse à l'arbitre, en une page

**Verdict.** Au sens des définitions du bloc 5 : **conditionnel, plus probablement bonne pour la conception que pour l'évaluation ; aucune des deux n'est établie.** Condition mesurable « conception » : sur T_commune, support commun, bras 1 − bras 2′ ≥ Δ_min = 5 points (illustratif) sur (ii) **et** sur (iii) réévalué frais, avec les préconditions de jugeabilité satisfaites et Δ_φ < Δ_min ; un gain sur (i) seul ne compte pas. Condition « évaluation » : Δ₁₂ ≥ Δ_min. Sous support disjoint, (ii) cesse d'estimer (iii) et le verdict « conception » se juge sur (iii) seul ; sous support commun, un gain sur (ii) ne distingue pas apprentissage des lois et couverture, d'où le test φ. Une chute Δ_φ ≥ Δ_min annule les deux verdicts. Le chiffre publié reste (iii), pire cas **atteint à budget B déclaré**, pas infimum.

**Quantité qui tranche.** Δ₁₂ = [(ii)−(iii)]_bras2′ − [(ii)−(iii)]_bras1, trajectoire commune, (iii) réévalué sur 10⁴ cas frais, moyenne sur W = 200 mondes appariés, IC t à 95 % ; signe prédit > 0 ; seuil Δ_min = 5 points ; prédiction illustrative +3, donc possiblement non concluante ou H_A falsifiée ; non jugeable si les regrets des deux bras diffèrent de plus de Δ_min/3 ou si la tête auxiliaire n'a pas convergé.

**Expérience décisive corrigée.** Cinq bras à N_tot égal sur une trajectoire de familles commune produite contre une défense pilote tierce ; bras 2 = tête auxiliaire à gradients jetés ; contrôles 1-perm, 1-const, 2-sans-tête. Score (iii) : générateur à B = 500, point retenu réévalué frais, saturation B/10B par bras. Deux régimes à difficulté appariée en KL(P_θ‖P_0), K = 50 familles tenues à l'écart lues une fois. Reparamétrisation sur cibles blanchies, identifiables (Cholesky), φ non linéaire scellée, jugeable seulement si les témoins T_lois/T_param la séparent. Décision à Δ_min = 5 points, IC t apparié, W = 200 après pilote de 20 mondes.

**Ce qui est établi.** L'idée est énoncée et rien n'en est construit (fait 3, VÉRIFIÉ). Le champ fait jouer le générateur en dernier à l'évaluation (faits 6–8, RAPPORTÉ) et range l'itération de la défense parmi les causes de surestimation (fait 7, RAPPORTÉ). Le transfert hors classe est mitigé (fait 11, RAPPORTÉ). La réunion « jeu répété + défense informée des paramètres + familles de tiers » n'a pas été trouvée, recherche non exhaustive (fait 12, RAPPORTÉ). La compatibilité des deux règles tient par raisonnement, à la condition du gel (w, τ, B, classe φ déclarés avant lecture) : c'est un argument, non une mesure.

**Ce qui ne l'est pas.** Tout effet de θ sur (ii), (iii) et Δ₁₂ (HYPOTHÈSE). Que « voir les épreuves et leurs scores » (fait 9) équivaille à recevoir θ (question ouverte). Qu'un générateur à budget B approche le pire cas, et qu'il le fasse symétriquement entre bras. Que le test de reparamétrisation sépare lois et paramétrisation : cela dépend de la classe φ, du blanchiment et des témoins. Que (i) − (ii) soit monotone en D_dep hors appariement de difficulté. Les trois critiques ont montré que mon plan du III.1 n'était pas jugeable tel quel (trajectoires, biais de (iii), contrôle permuté, identifiabilité de L) ; le plan corrigé l'est sous préconditions déclarées, non vérifiées.

**Expérience à faire en premier.** Le pilote de jugeabilité, 20 mondes, bras 1, 2′, 1-perm, 2-sans-tête sur trajectoire commune : convergence de la tête (R² ≥ 0,5), étendue de p(θ) ≥ 2 Δ_min, et (iii)(B) − (iii)(10B) ≤ Δ_min/3 avec réévaluation fraîche ; si l'une échoue, aucun des W = 200 mondes n'est lancé.

FIN-DE-CELLULE