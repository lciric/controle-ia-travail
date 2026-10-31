# Tour III.2 — Proposition A : critique croisée de méthode

Les trois pièces reçues sont complètes et closes. Notation commune : pour une défense figée D et son seuil τ, p_D(θ) = Pr_{P_θ}(statistique ≥ τ) ; p*(θ) = puissance du test du rapport de vraisemblance P_θ contre P_0 à 1 % de fausses alertes (oracle, connu par construction dans toute classe déclarée). Tout chiffre ci-dessous est illustratif ou recalculé à partir des chiffres illustratifs des pièces ; mes prédictions de comportement sont des HYPOTHÈSES.

---

## Sur la proposition B

### (a) Défauts de méthode

1. **Fuite de l'étiquette dans l'entrée (mode déclaré).** B donne θ *en entrée* à l'entraînement. Dans toute famille d'entraînement, θ ≠ θ_0 détermine la présence du déplacement ; si les cas honnêtes reçoivent θ_0 (ou rien), la perte est minimisée par une fonction de θ seule et le chemin des activations ne reçoit aucun gradient utile. Le score (i) *pendant* l'entraînement est vrai par construction (≈ 100 %). À l'évaluation, l'entrée θ est absente ; B ne dit pas ce qui la remplace : la défense est évaluée sur un régime d'entrée jamais vu. Le contraste 1 − 2 confond alors « information sur les lois » et « décalage d'entrée entre entraînement et évaluation ». HYPOTHÈSE : sous ce mode, (ii)_1 < (ii)_2 est plausible, et un verdict « mauvaise » serait un artefact du mode, non de l'idée.
2. **Test de reparamétrisation nul par construction.** B applique φ *après le gel*, sur les familles de (ii) et (iii). Or sous son mode, θ n'entre pas dans la défense figée : score(ii)_original − score(ii)_reparam = 0 exactement, à graine fixée, pour tous les bras. Le duel 2 est tranché avant toute mesure (« H_B falsifiée » toujours). De plus, B exige P_{φ(θ)} = P_θ pour tout θ : une telle φ est une *symétrie du schéma*, non un changement de carte ; appliquée à l'entraînement, elle rendrait l'étiquette ambiguë (deux θ pour une loi), ce qui n'est pas le test demandé. La validation instrumentale de (c) (« défense entraînée sur θ brut » qui chute) suppose φ appliquée là où θ compte, en contradiction avec le duel 2.
3. **Duel 1 non exhaustif.** H_A : Δ > δ_min ; H_B : Δ ≤ 0. L'issue Δ ∈ (0, δ_min] ne falsifie rien. Le bloc 3 (condition 3 : Δ ≤ 0) et le bloc 4 (δ_min) ne s'accordent pas.
4. **« Contrôle négatif = bras 3 ».** Le bras 3 est un bras de comparaison dont l'issue attendue ((ii)_3 − (iii)_3 ≥ (ii)_2 − (iii)_2) est une hypothèse, non un nul connu par construction.
5. **Qui propose les familles dans la boucle des bras 1-2 ?** Non déclaré. Si c'est le générateur contre la défense du bras 1, les familles ciblent les faiblesses du bras 1 et non du bras 2 : confondant (identique à C, explicite chez elle).
6. **Budget.** « Passes avant de la défense » n'inclut ni les évaluations du générateur du bras 4 à chaque génération, ni le palier rapide du bras 5 : selon l'option, le bras 4 reçoit plus de calcul ou moins d'entraînement.
7. **Mesure de dépendance.** Distance d'énergie entre les θ dans Θ (référence à vérifier, comme B l'écrit) : non invariante par reparamétrisation, alors que le test de reparamétrisation est censé neutraliser la carte. La construction des niveaux « corrélation entre θ_train et θ_écart ∈ {0 ; 0,3 ; 0,6 ; 0,9} » n'est pas définie pour deux ensembles de tirages non appariés : le « niveau connu » n'est pas connu.
8. **(i) − (ii) confond nouveauté et difficulté.** Si la région des familles tenues à l'écart a un p* moyen différent de celui des familles d'entraînement, l'écart existe même pour l'oracle ; B le prédit positif sans ce contrôle.

### (b) Conditions mesurables de perte de puissance ou de non-jugeabilité

- **Seuil τ̂** : estimé sur m cas honnêtes non déclarés. Si m est tel que m × 0,01 < 50 (illustratif), la variance de τ̂ fait que l'écart-type de p_D(θ) à τ̂ domine δ_min = 3 pp ; avec n = 500 tirages par famille et étalonnage par famille, le quantile 99 % repose sur 5 valeurs.
- **Plafond/plancher** : si p_D(θ) ≥ 0,95 ou ≤ 0,05 sur la quasi-totalité du support de (ii), (ii) − (iii) est comprimé et Δ borné par 1 − (ii). Le tableau de B (bras 1, support commun : 85/77) n'est jugeable que si p* moyen sur la région de (ii) est dans [0,3 ; 0,8] (illustratif).
- **Score (iii)** : B_eval = 1 000 évaluations dans Θ de dimension d = 100, avec une sortie binaire par évaluation : p̂(θ) a une variance de Bernoulli, le θ* retenu n'est pas le pire ; (iii) est surestimé d'une quantité qui dépend de la régularité de p_D sur Θ, donc du bras. Δ est non jugeable sans mesure du regret *par bras*.
- **Duel 2** : puissance nulle (a.2).
- **Dépendance** : si une reparamétrisation change l'échelle des coordonnées, D change sans que les lois changent ; la régression (i) − (ii) ≈ αD + β n'a de sens que dans une carte fixée, et avec deux régimes seulement elle a deux points de levier.
- **(i) − (ii)** perd son sens si p*_train ≠ p*_écart.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Oracle p*** sur (i), (ii), (iii) par régime : tout écart de l'oracle est difficulté intrinsèque, à soustraire. Fatal.
- **Étiquette aléatoire** : bras 1 avec θ̃ permuté entre familles (fixe par famille, indépendant de la loi) ; doit reproduire le bras 2. Fatal : sans lui, le gain du bras 1 n'est pas attribuable à θ plutôt qu'à l'architecture (entrée supplémentaire).
- **Plancher de bruit** : deux copies du bras 2 à graines différentes pour estimer la dispersion de Δ sous l'hypothèse nulle.
- **Défense constante en θ** : (ii) = (iii) attendu ; vérifie que le générateur ne produit pas d'écart là où il n'y en a pas.
- **Sonde d'entrée** : au bras 1 figé, passer θ_0 puis le vrai θ à l'évaluation ; si les sorties diffèrent, θ a fuité dans le chemin d'inférence.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Cible auxiliaire non identifiable.** Classe déclarée P_{(μ,u)} = N(μ, I + uu^T) : (μ, u) et (μ, −u) donnent la même loi. La tête de régression ne peut prédire u qu'en mémorisant l'identité de la famille (le signe de u_k est fixé par famille). Le « régularisateur » favorise des traits d'identité, exactement ce que le bras 1 doit éviter : confondant de signe inconnu. Correction : cible (μ, uu^T). Le même défaut persiste sous la reparamétrisation sinh composante par composante, puisque sinh(−u) = −sinh(u).
2. **Ciblage adverse asymétrique.** Au bras 1, les familles d'entraînement sont « choisies adaptativement par le générateur à chaque génération » contre la défense du bras 1 ; le bras 2 reçoit les mêmes familles, qui ne ciblent pas ses faiblesses. Le contraste 1 − 2 confond θ et ciblage. Correction : échéancier de familles scellé, ou générateur jouant contre une défense tierce figée (bras 3), identique pour 1, 2 et 5.
3. **Test de reparamétrisation sous mode « cible auxiliaire ».** L'encodeur est partagé, la tête est ignorée à l'évaluation. Toute bijection lisse φ est absorbable par une tête de capacité suffisante (elle apprend φ∘ĥ) ; l'encodeur ne change pas. Le test mesure la capacité de la tête, non ce que l'encodeur a appris : invariance vraie par construction dès que la tête est un perceptron. La validation instrumentale (c.4) le confirme : D_loi n'a pas de tête (invariance triviale) et D_param (« poids dépendant linéairement de θ ») n'est pas une défense du mode déclaré. L'instrument est validé sur des objets qu'il ne mesurera jamais.
4. **Duel 2** : Δ_reparam = (ii)_1 − (ii)_{1'} compare deux entraînements complets ; le bruit de réentraînement (graine, ordre des lots) n'est pas estimé, ε = 0,02 est fixé a priori. Le contrôle « φ au bras 2 ⇒ 0 exactement » est vrai par construction et n'étalonne rien.
5. **Mesure de dépendance.** « Retrouve D à 10⁻⁴ près » : D est calculée analytiquement à partir des mêmes θ — vrai par construction. Ce qu'il faut valider est la relation (i) − (ii) ≈ αD. Et « support disjoint » n'est pas défini dans (μ, u) : si la partition sépare par ‖μ‖ ou ‖u‖, elle sépare par difficulté (p* monotone en ces normes) : confondant.
6. **Budget** : évaluations du générateur (bras 1 et 4) et palier rapide (bras 5) hors du budget déclaré.
7. **Condition d'échec en ET** (bloc 3) contredit la définition du bloc 5 (gain requis sur (ii) *et* (iii)).
8. **Vérification mécanique** « ‖x‖² + (tr S_n − d)² » : additionne une quantité par vecteur et une par lot ; non définie comme statistique de lot, donc non jugeable comme « mesure minimale à battre ».

### (b) Conditions mesurables de perte de puissance ou de non-jugeabilité

- **Seuil** : N_0 = 10 000 tirages, b = 32 → ≈ 312 lots honnêtes ; le quantile 99 % repose sur ≈ 3 lots ; l'écart-type binomial du taux de fausses alertes est ≈ 0,56 pp, supérieur à la tolérance 0,2 pp du contrôle (calcul sur les chiffres illustratifs de C). Le contrôle est inatteignable par échantillonnage. Condition : ≥ 10⁴ lots honnêtes d'étalonnage (illustratif).
- **Score (iii)** : chaque requête renvoie D(X) sur un lot. Si c'est l'indicatrice, 500 requêtes dans Θ ⊂ ℝ^128 ne localisent pas un minimum (regret ≥ 0,02 attendu) ; si c'est la statistique continue, cela doit être déclaré comme « sortie » au sens du fait 4. Dans les deux cas, le regret dépend de la régularité de p_D, donc du bras : Δ_{1,2} non jugeable sans regret par bras.
- **Plafond** : scores de (ii) à 0,84–0,90 au tableau ; avec δ = 0,03, (ii)_1 − (ii)_2 est écrasé contre le plafond si p* moyen > 0,9 sur la région.
- **Reparamétrisation** : puissance nulle si la capacité de la tête représente φ ; non jugeable si la variance de réentraînement de (ii)_1 dépasse ε.
- **Dépendance W_2** : en dimension 128 avec 50 familles d'entraînement, min_i W_2 reste grand même sous support commun (dimension) : D_commun et D_disjoint se séparent peu. Condition : comparer D à sa valeur nulle (deux tirages indépendants de la même loi des familles).
- **Identifiabilité** : si θ ↦ P_θ n'est pas injective, la cible auxiliaire a une variance irréductible et la régularisation dégénère (a.1).

### (c) Contrôles négatifs dont l'absence serait fatale

- **Oracle p*** par score et régime. Fatal.
- **Valeur nulle de D** : deux tirages indépendants de la loi des familles d'entraînement.
- **Réentraînement du bras 1 avec identité et graine nouvelle** : plancher de Δ_reparam. Fatal pour le duel 2.
- **Bras témoin à cible invariante** (μ, uu^T) : si les deux têtes diffèrent sur (ii), l'identifiabilité est le confondant.
- **Générateur contre défense constante en θ** : regret 0 et (ii) = (iii).
- Le contrôle θ̃ aléatoire de C est à garder, mais en deux versions : θ̃ permuté entre familles (fixe par famille) et θ̃ retiré par lot (variable dans la famille), pour séparer « mémorisation d'identité » de « bruit sur la cible ».

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Mode « entrée auxiliaire distillée » : même fuite d'étiquette qu'en B, déplacée vers le maître.** Le maître reçoit θ en entrée, donc l'étiquette (θ ≠ θ_0) ; il peut résoudre la tâche sans activations. Sa sortie est alors une fonction de θ, et la distillation transmet à l'élève des étiquettes douces qui ne contiennent que « déplacé / non déplacé », information que le bras 2 possède déjà par construction des familles. Le contraste 1 − 2 mesure alors l'effet d'un entraînement en deux étapes, non de θ. D ne dit ni ce que reçoit le maître pour les cas honnêtes, ni si son coût entre dans U.
2. **Budget U** (vecteurs générés) : les évaluations du générateur du bras 4 et l'entraînement du maître consomment-ils U ? Non déclaré.
3. **Bras 1 : « après chaque lot proposé »** — par qui ? Même confondant qu'en C.2 si c'est le générateur. La description du bras 4 comme seule boucle où le générateur joue contre la défense suggère un échéancier non adaptatif aux bras 1-2 ; à déclarer.
4. **Contrôle négatif du duel 2** (réétiqueter à l'évaluation ⇒ 0) : vrai par construction, n'étalonne pas le bruit de réentraînement ; ε = 0,02 fixé a priori.
5. **Générateur** : regret contre le minimum sur une grille finie ; si le générateur cherche hors grille, le regret peut être négatif : la « pire loi connue » ne l'est que sur la grille.
6. **Mesure de dépendance** par KL symétrisée : invariante, c'est un progrès sur B ; mais D n'a déclaré aucune classe. Hors classe à KL fermée, l'estimation par échantillons en dimension 16 a un biais inconnu et le « niveau connu » ne l'est plus.
7. **Score (iii)** : unité « coup du générateur dans un monde » ambiguë (un θ̂ par monde, ou plusieurs redémarrages moyennés ?). Si moyenne de plusieurs coups, (iii) n'est plus le pire cas mais une moyenne de minima locaux, moins pessimiste.
8. **Verdict « bonne pour aucune au sens d'un résultat établi »** : sens déclaré, mais vide — il découle du fait 3 (VÉRIFIÉ) et ne dépend d'aucune mesure ; seul le verdict conditionnel qui suit est jugeable.
9. **Reparamétrisation** : g appliquée à l'entrée du maître avant réentraînement complet, placement correct ; mais g affine est absorbée par la première couche du maître, et D ne restreint pas g.

### (b) Conditions mesurables de perte de puissance ou de non-jugeabilité

- **Maître aveugle** : si, à θ fixé, la sortie du maître ne varie pas avec X (mesurable : variance conditionnelle de la sortie sachant θ ≈ 0), l'information transmise se réduit aux étiquettes ; R ≈ 0 attendu, par mode et non par échec de l'idée.
- **Seuil** : nombre de cas honnêtes de référence et taille n de T_n non déclarés ; variance de τ̂ indéterminée, donc tolérance δ_E = 0,03 non jugeable.
- **Score (iii)** : B = 100 évaluations pour une Θ de dimension non déclarée ; si dim Θ dépasse ~10 (illustratif), 100 évaluations ne battent pas une recherche aléatoire de même budget, et le regret, grand, dépend du bras.
- **Plafond/plancher** : même condition qu'en B et C ; le tableau de D, en contrastes seuls, ne permet pas de la vérifier.
- **Dépendance** : non jugeable sans classe à KL fermée.
- **Reparamétrisation** : non jugeable si la variance de réentraînement dépasse ε ; sans puissance si g est affine.
- **(i) − (ii)** « à difficulté moyenne contrôlée » : le contrôle n'est pas défini ; condition : |p*_train moyen − p*_écart moyen| ≤ 2 pp (illustratif) par régime.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Oracle p*** par score et régime. Fatal.
- **Sonde du maître** : sa sortie doit varier avec X à θ fixé ; fatal pour le mode déclaré.
- **Étiquette aléatoire au bras 1** (θ̃ permuté entre familles) : doit reproduire le bras 2.
- **Réentraînement identité + graine nouvelle** : plancher de Q.
- Recherche aléatoire et défense constante en θ : présents chez D, à conserver.
- **Régime à difficulté appariée** : familles tenues à l'écart tirées dans une région disjointe mais à p* moyen apparié ; sans lui, « support disjoint » et « plus difficile » sont indistinguables.

FIN-DE-CELLULE