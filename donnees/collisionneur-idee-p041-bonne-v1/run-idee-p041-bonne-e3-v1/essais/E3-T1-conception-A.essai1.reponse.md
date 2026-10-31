# Proposition A — Tour III.1 : l'idée P-041 (ordre des coups)

**Cadre statistique (déclaré, illustratif).** Activations x ∈ ℝ^d, d = 32. Loi de référence P_0 = N(0, I). Schéma : P_θ = N(μ, LLᵀ), θ = (μ, L), Θ = {θ : κ_min ≤ KL(P_θ‖P_0) ≤ κ_max}, κ_min = 0,25, κ_max = 2 (illustratif ; la borne inférieure rend le pire cas non trivial). Un **cas** = un lot de m = 16 vecteurs tirés d'une même loi (illustratif). Défense = score s_w(cas) ; seuil τ = quantile 0,99 de s_w sur N_h = 10⁵ cas honnêtes (graine propre). Score d'une famille k : TPR_k = P̂_{θ_k}(s_w > τ) sur n cas.

## (a) Ce que la question suppose sans que ce soit établi

1. Familles d'entraînement, tenues à l'écart et générateur dans le **même schéma** Θ — HYPOTHÈSE (cadre de la question) ; l'universalité du fait 1 (VÉRIFIÉ) porte sur des familles inédites, qui ne sont pas forcément dans Θ.
2. Le pire cas inf_{θ∈Θ} TPR(θ) est atteint et strictement supérieur au point de fausses alertes — HYPOTHÈSE (vrai si κ_min > 0, non établi sinon).
3. Un générateur numérique à budget B déclaré approche ce pire cas — HYPOTHÈSE (fait 4 ; c'est un instrument à vérifier, voir (c)).
4. « Voir les épreuves et leurs scores » (fait 9, RAPPORTÉ) équivaut à recevoir θ — question ouverte, non fait.
5. Les protocoles des faits 6–8 (RAPPORTÉ) sont transposables au niveau des lois — HYPOTHÈSE.
6. L'amélioration itérative surestime la défense (fait 7, RAPPORTÉ, p. 13) vaut ici — HYPOTHÈSE.
7. Le transfert hors classe est mitigé (fait 11, RAPPORTÉ) ; sa pertinence pour des familles tenues à l'écart *dans* le schéma — HYPOTHÈSE.
8. Une défense ayant appris la paramétrisation chute sous reparamétrisation — HYPOTHÈSE (énoncée telle quelle par la question).
9. « Aucune règle propre à une seule famille » (bras 5) est opérationnalisable — HYPOTHÈSE (je l'opérationnalise ci-dessous).
10. Les bras 1 et 2 sont « à budget égal » bien que θ soit une information non comptée dans le budget — HYPOTHÈSE sur l'unité de budget.
11. La dépendance entre familles se mesure par une divergence entre lois — HYPOTHÈSE (instrument, voir (c)).
12. Le point à 1 % de fausses alertes est estimable avec précision — calcul : avec N_h = 10⁵ honnêtes, erreur binomiale ≈ 0,03 point (refaisable).

## (b) Duels

**Duel 1 — quantité du bloc 4.** H_A : l'avantage des paramètres réduit (ii) − (iii) ; H_B : il ne le réduit pas ou l'accroît. Métrique : Δ₁₂ = [(ii)−(iii)]_bras2 − [(ii)−(iii)]_bras1, moyenne sur W mondes appariés par graine. Seuil : effet minimal Δ_min = 5 points de détection (illustratif). Contrôle négatif : bras 1 avec θ **permutés entre familles** (information détruite, budget identique) ; Δ attendu ≈ 0. Falsification : intervalle à 95 % de Δ₁₂ excluant 0 et estimation ≥ Δ_min → H_B falsifiée ; intervalle contenant 0, ou estimation < Δ_min, ou signe négatif → H_A falsifiée. Si le contrôle négatif donne Δ ≥ Δ_min, le duel est non jugeable (l'écart ne vient pas de θ).

**Duel 2 — reparamétrisation.** H_A : la défense du bras 1 a appris les lois ; H_B : la paramétrisation. Métrique : Δ_φ = score(ii)[θ] − score(ii)[φ(θ)], même chose sur (iii), φ inversible appliquée aux cibles d'entraînement (graine scellée, classe déclarée : affine aléatoire inversible composée de monotones par coordonnée). Seuil : Δ_min. Contrôle négatif : φ appliquée **à l'évaluation seulement** → Δ = 0 exactement par construction (la défense ne lit que x) ; et deux défenses témoins construites exprès (voir (c)). Falsification : Δ_φ ≥ Δ_min avec intervalle excluant 0 → H_A falsifiée ; |Δ_φ| < Δ_min avec intervalle excluant ±Δ_min → H_B falsifiée.

**Duel 3 (facultatif) — deux échelles de temps.** H_A : bras 5 bat bras 1 sur (iii) ; H_B : non. Métrique : (iii)_5 − (iii)_1, seuil Δ_min, contrôle négatif : bras 5 avec palier rapide gelé dès le premier lot (doit se confondre avec bras 1). Falsification symétrique à celle du duel 1.

## (c) Mesure minimale de chaque instrument (simulation à vérité connue)

**Défense.** Mondes où chaque θ_k est connu ; la vérité (déplacement présent/absent) est connue par construction. Mesure : TPR_k à τ fixé, et FAR vérifiée sur 10⁵ cas honnêtes **appariés par graine** (mêmes graines pour tous les bras) : FAR doit tomber dans [0,8 %, 1,2 %] (illustratif), sinon le seuil est faux. Vérification mécanique à battre : test fixe de log-vraisemblance du lot sous P_0 (statistique T = −Σ log φ_0(x_i), seuil à 1 % FAR, sans apprentissage) ; une défense qui ne dépasse pas T sur (ii) et (iii) d'au moins Δ_min n'est pas jugeable comme défense. Contrôle négatif : défense à score aléatoire → (i)=(ii)=(iii) ≈ 1 %.

**Générateur adaptatif.** Pour une défense figée, le pire cas oracle TPR* = min_Θ TPR est calculé hors budget (grille fine + optimisation locale, 100 × B évaluations, illustratif). Mesure : écart TPR_gén(B) − TPR* (unité : point), avec 5 redémarrages. Critère : écart ≤ 2 points (illustratif) sur 90 % des mondes, sinon (iii) est une borne supérieure du pire cas, non le pire cas. Contrôle négatif : générateur à tirage uniforme dans Θ avec le même B → écart nettement plus grand attendu.

**Mesure de dépendance.** D_dep = moyenne sur les familles tenues à l'écart k de min_j KL(P_{θ_k}‖P_{θ_j}) (forme close pour gaussiennes, donc vérité connue). Estimateur à partir d'échantillons : D̂_dep par substitution (moyenne et covariance empiriques, n cas) ou MMD minimale sur j. Mesure : mondes où D_dep est placée à des niveaux connus (0 ; 0,1 ; 0,5 ; 1, illustratif) ; D̂_dep doit retrouver le niveau à ±20 % (illustratif). Contrôle négatif : familles tenues à l'écart retirées de la région d'entraînement avec graine neuve → D̂_dep ≈ 0 et (i)−(ii) ≈ 0.

**Test de reparamétrisation.** Deux défenses témoins : T_lois, entraînée sur le rapport de vraisemblance exact dP_θ/dP_0 (cible invariante par φ) ; T_param, dont le score dépend explicitement d'une coordonnée de θ̂ prédite (cible non invariante). Mesure : le test doit donner |Δ_φ| < Δ_min pour T_lois et Δ_φ ≥ Δ_min pour T_param, sur ≥ 90 % des mondes (illustratif). Contrôle négatif : φ appliquée à l'évaluation → 0 exact.

---

## Bloc 1 — Compatibilité des deux règles

**Mode déclaré :** θ est une **cible à prédire depuis les activations**, tête auxiliaire h_w(x) → θ̂ entraînée par ‖h_w(x) − θ_k‖² en plus de la perte de détection ; θ n'entre jamais à l'évaluation, seul s_w(x) est lu. Le bras 1 et le test de reparamétrisation sont donc définis.

Les deux règles sont compatibles : elles portent sur des étapes distinctes. « Défense en dernier à l'entraînement » décrit la construction de s_w ; « générateur en dernier à l'évaluation » décrit la mesure sur s_w **figé**. Elles ne se contredisent que si une information d'entraînement fuit vers la mesure.

*Ce que θ peut améliorer :* la défense apprise — la cible θ structure la représentation selon la géométrie du schéma, ce qui peut relever TPR sur (ii) et (iii) (HYPOTHÈSE, duel 1). *Ce qu'il peut fausser :* le chiffre publié, par trois voies : (1) surajustement à la paramétrisation (duel 2) ; (2) sélection du point de contrôle sur des familles proches des familles d'entraînement, qui gonfle (ii) ; (3) itération contre les familles observées, rangée comme surestimation (fait 7, RAPPORTÉ).

*Où l'avantage cesse d'être légitime :* il est légitime à l'**entraînement** et à la **sélection**, à condition que la sélection se fasse sur une partition de validation tirée de la région d'entraînement avec graine propre — jamais sur les familles tenues à l'écart. Il cesse à l'**étalonnage du seuil** (cas honnêtes seuls, θ n'y a aucune place) et à la **mesure finale** : (ii) lu une fois (fait 2, VÉRIFIÉ, par analogie avec test_final), (iii) contre la défense figée. Étape supplémentaire que je nomme : le **gel** — la déclaration, avant toute lecture, de w, τ, B et de la classe φ.

## Bloc 2 — Trois scores et dépendance

**(i)** Statistique : moyenne sur les familles d'entraînement k de TPR_k à τ. Unité d'échantillonnage : la famille (bootstrap sur familles, 95 %) ; bruit binomial intra-famille sur n cas inclus. **(ii)** Même statistique sur K familles tenues à l'écart, tirées avec graine scellée dans la région du régime, lues une fois par bras, régime et condition φ ; unité : la famille, K = 20 (illustratif). **(iii)** min sur les θ explorés par le générateur (B = 500 évaluations, 5 redémarrages, illustratif) de TPR(θ) contre (w, τ) figés, chaque évaluation sur n cas ; unité : le monde simulé (intervalle sur W mondes), car une recherche adaptative n'a pas de bootstrap interne valide.

**Signes prédits (HYPOTHÈSE).** (i) − (ii) ≥ 0, croissant avec D_dep ; ≈ 0 ± bruit si D_dep ≤ δ (support commun, δ = 0,1 illustratif). (ii) − (iii) ≥ 0 à condition que le générateur atteigne un θ sous la moyenne des familles tenues à l'écart, ce qui exige que l'écart oracle de (c) soit petit ; si B est insuffisant, (iii) peut dépasser (ii) et le signe s'inverse — ce serait un défaut d'instrument, pas une propriété de la défense.

**Dépendance au niveau des lois.** Les familles tenues à l'écart sont dépendantes des familles d'entraînement si leurs lois sont proches de l'enveloppe des lois d'entraînement : mêmes directions de μ, même structure de L, mêmes bornes de KL. Mesure calculable : D_dep = moyenne_k min_j KL(P_{θ_k}‖P_{θ_j}) ; variante : fraction des k dont le plus proche voisin d'entraînement est à KL ≤ δ (couverture). Prédiction : (i) − (ii) ≈ β·D_dep, β > 0, estimée par régression sur mondes où D_dep est imposée ; sous support disjoint, D_dep ≥ κ_min par construction et l'écart (i) − (ii) devrait valoir 10 à 20 points (illustratif).

Hors tour : le contenu réel des familles et l'organisation des tiers (fait 5).

## Bloc 3 — Expérience décisive à budget égal

**Unité de budget :** N_tot = nombre total de cas (honnêtes compris) consommés par la défense à l'entraînement et à la sélection, identique pour les cinq bras ; B (évaluations du générateur pour (iii)) identique et hors N_tot. Illustratif : G = 8 générations, M = 5 familles/génération, 500 cas/famille, 40 familles au total, N_tot = 4·10⁴ cas.

**Bras.**
1. *Boucle de générations.* À chaque génération g, le générateur (figé contre la défense g−1) ajoute M familles ; la défense est réentraînée sur toutes les familles accumulées en recevant **θ** (cible auxiliaire) **et** des échantillons ; elle joue en dernier dans la génération.
2. Identique au bras 1, mêmes familles (mêmes graines), même déroulement ; la défense reçoit **seulement des échantillons**.
3. *Familles fixes.* 40 familles tirées d'un coup dans la région d'entraînement, pas de boucle ; échantillons seuls.
4. *Boucle, protocole du champ* (faits 6–8, RAPPORTÉ) : la défense se met à jour sur les échantillons des familles accumulées, puis le générateur joue en dernier contre elle ; la génération se clôt sur son coup, donc la défense finale n'a jamais vu les familles de la dernière génération. Elle reçoit des échantillons, rien d'autre que ses entrées.
5. *Boucle, paramètres θ, deux paliers.* Palier rapide (entre lots de 500 cas) : règles de détection = seuils par direction propre de l'écart estimé, règle d'agrégation (max/moyenne), mémoire de cas validés par la vérité de simulation sur familles d'entraînement seulement ; une règle est retirée si elle n'est validée que sur une seule famille (opérationnalisation de « aucune règle propre à une seule famille »). Palier lent : poids w réentraînés entre générations sur l'expérience accumulée. Tout est figé avant (ii) et (iii).

**Régimes.** Support commun : familles tenues à l'écart tirées avec graine scellée dans la région d'entraînement (μ sur les coordonnées 1..16). Support disjoint : μ sur les coordonnées 17..32 et L de structure différente, même bornes de KL.

**Reparamétrisation.** φ s'applique à l'**entraînement** (et à la sélection) : les cibles θ_k deviennent φ(θ_k), la défense est réentraînée. Sous mon mode, l'appliquer à l'évaluation est vide par construction (contrôle négatif). φ est tirée avec graine scellée dans la classe déclarée, hors de portée du concepteur de la défense.

**Seuils de décision (distincts de τ).** Effet minimal Δ_min = 5 points ; décision si l'intervalle à 95 % sur W mondes appariés exclut 0 et l'estimation ≥ Δ_min. Tolérance de FAR : [0,8 %, 1,2 %].

**Contrôles négatifs.** (1) Bras 1 à θ permutés ; (2) défense aléatoire ; (3) φ à l'évaluation ; (4) familles tenues à l'écart retirées de la région d'entraînement avec graine neuve (D_dep ≈ 0).

**Condition d'échec de l'idée.** Sous support commun : bras 1 − bras 2 < Δ_min sur (ii) ou sur (iii), **ou** Δ_φ ≥ Δ_min au bras 1 (paramétrisation apprise), **ou** Δ₁₂ du bloc 4 < Δ_min ; un gain sur (i) seul ne compte pas.

**Plan de puissance par simulation (sans résultat).** W = 200 mondes (illustratif), chacun : 40 familles d'entraînement, K = 20 tenues à l'écart, n = 2 000 cas par famille à l'évaluation, 10⁵ honnêtes ; effet supposé Δ = 5 points, écart-type inter-mondes σ supposé 4 points (illustratif) ; cible : puissance 0,9 à α = 0,05 bilatéral ; W ajusté après pilote de 20 mondes. Nombre de conditions : 5 bras × 2 régimes × 2 conditions φ.

**Prédictions (toutes HYPOTHÈSE, illustratif, points de détection à 1 % FAR).**

| Bras | (ii)−(iii) commun | (ii)−(iii) disjoint | (ii) commun | (iii) commun |
|---|---|---|---|---|
| 1 (θ) | +8 | +15 | 85 | 77 |
| 2 (échantillons) | +12 | +18 | 82 | 70 |
| 3 (banque fixe) | +15 | +20 | 78 | 63 |
| 4 (champ) | +10 | +16 | 80 | 70 |
| 5 (θ, deux paliers) | +6 | +13 | 86 | 80 |

Signe : toutes les cases (ii)−(iii) positives ; disjoint > commun partout ; bras 1 < bras 2 (duel 1), bras 5 ≤ bras 1 (duel 3). Les colonnes (ii) et (iii) sont facultatives et en commun seulement.

## Bloc 4 — La quantité qui tranche

Contraste : **Δ₁₂ = [(ii) − (iii)]_bras2 − [(ii) − (iii)]_bras1**, à budget N_tot égal, mêmes familles, même régime, condition φ = identité. Estimateur : moyenne des différences par monde apparié (mêmes graines pour familles, honnêtes, générateur), sur W mondes. Intervalle : t de Student apparié à 95 %, confirmé par bootstrap sur mondes. Effet minimal : Δ_min = 5 points (illustratif). Signe prédit : Δ₁₂ > 0 (HYPOTHÈSE ; prédiction illustrative +4 en commun, +3 en disjoint, c'est-à-dire possiblement sous Δ_min — je ne suis pas sûr que l'effet atteigne le seuil). Issue qui falsifie la prédiction : intervalle contenant 0, estimation < Δ_min, ou Δ₁₂ < 0 ; dans ce dernier cas θ *accroît* l'écart et l'idée est mauvaise pour l'évaluation. Précondition de validité : contrôle négatif à θ permutés donnant |Δ| < Δ_min, et écart oracle du générateur ≤ 2 points ; sinon Δ₁₂ est non jugeable.

## Bloc 5 — Conclusion

Verdict conditionnel, au sens des définitions de la question. **Bonne pour la conception** si bras 1 − bras 2 ≥ Δ_min sur (ii) et sur (iii), sous support commun, avec Δ_φ < Δ_min. **Bonne pour l'évaluation** si Δ₁₂ ≥ Δ_min. Mon attente (HYPOTHÈSE) : plus probablement bonne pour la conception que pour l'évaluation ; le chiffre publié reste (iii). *Support disjoint :* (i)−(ii) grandit, (ii) perd sa valeur d'estimation de (iii) ; le verdict « conception » se juge alors sur (iii) seul. *Support commun :* (ii) proche de (i), le gain sur (ii) ne distingue pas apprentissage des lois et couverture. *Reparamétrisation :* Δ_φ ≥ Δ_min au bras 1 annule les deux verdicts, quel que soit Δ₁₂ ; sous le mode déclaré, le test n'est informatif qu'appliqué à l'entraînement.

## (d) Ancrage matériel

Aucun modèle ouvert : activations synthétiques, d = 32. Calcul sur processeur : 5 bras × 2 régimes × 2 conditions φ × 200 mondes = 4 000 entraînements de petits perceptrons plus générateur (B = 500) ; ≈ 2 min par monde-condition, soit ≈ 130 heures-processeur, coût cloud ≈ 15–40 € (illustratif).

FIN-DE-CELLULE