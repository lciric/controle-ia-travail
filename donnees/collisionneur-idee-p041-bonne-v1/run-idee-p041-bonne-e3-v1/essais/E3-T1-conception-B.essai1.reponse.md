

# Proposition B — Tour III.1

## Déclaration liminaire (mode de réception de θ)

La défense reçoit θ comme **entrée présente à l'entraînement seulement** : pour chaque lot d'activations synthétiques, le vecteur θ de la famille génératrice est fourni en entrée à la défense pendant l'entraînement. À l'évaluation (scores ii et iii), la défense ne reçoit pas θ ; elle ne voit que les activations.

---

## (a) Hypothèses non établies supposées par la question

1. **La défense peut exploiter θ en entrée pour améliorer sa détection sur des familles inédites.** HYPOTHÈSE — Non mesuré (fait 3 : rien n'est construit).
2. **Le générateur adaptatif (fait 4) atteint le pire cas de la classe déclarée en un nombre fini d'évaluations.** HYPOTHÈSE — Cadre posé, non réalisé.
3. **Les familles tenues à l'écart (fait 5) sont statistiquement indépendantes des familles d'entraînement conditionnellement au schéma.** HYPOTHÈSE — Le fait 5 décrit une discipline de procédure ; l'indépendance au niveau des lois n'est pas vérifiée.
4. **Connaître θ à l'entraînement est équivalent à ou meilleur que connaître les épreuves et scores de l'adversaire (fait 9).** HYPOTHÈSE — La note d'antériorité pose la question sans la trancher (fait 9, dernière phrase).
5. **Le transfert hors de la classe entraînée est positif.** HYPOTHÈSE — Le signe empirique est mitigé (fait 11 : tantôt positif, tantôt négatif).
6. **Le test de reparamétrisation distingue effectivement apprentissage de la loi et apprentissage de la paramétrisation.** HYPOTHÈSE — Non construit ni mesuré.
7. **Le palier rapide du bras 5 (règles de détection mises à jour entre lots) n'introduit pas de surapprentissage aux familles d'entraînement.** HYPOTHÈSE — Non mesuré.

---

## (b) Duels décisifs

### Duel 1 — Avantage des paramètres sur l'écart (ii) − (iii)

- **H_A** : L'avantage des paramètres réduit l'écart (ii) − (iii). Formellement : Δ = [(ii)₂ − (iii)₂] − [(ii)₁ − (iii)₁] > δ_min, où les indices 1, 2 désignent les bras 1 et 2.
- **H_B** : Il ne le réduit pas ou l'accroît : Δ ≤ 0.
- **Métrique** : Δ estimé par différence des écarts de taux de détection à 1 % de fausses alertes, intervalle par bootstrap sur les mondes simulés.
- **Seuil** : δ_min = 3 points de pourcentage (illustratif).
- **Contrôle négatif** : Bras 3 (banque fixe, pas de boucle) ; on attend (ii)₃ − (iii)₃ ≥ (ii)₂ − (iii)₂, donc un écart au moins aussi grand que le bras 2.
- **Falsification** : Si Δ ≤ 0 dans l'intervalle à 95 %, H_A est falsifiée. Si Δ > δ_min avec borne inférieure de l'intervalle > 0, H_B est falsifiée.

### Duel 2 — Test de reparamétrisation

- **H_A** : La défense informée a appris les lois (invariance à la reparamétrisation). Formellement : |score(ii)_original − score(ii)_reparamétré| ≤ ε pour la défense du bras 1, où ε est la marge de bruit d'échantillonnage (intervalle à 95 % sous H₀).
- **H_B** : La défense a appris la paramétrisation (chute sous reparamétrisation). Formellement : score(ii)_original − score(ii)_reparamétré > ε.
- **Métrique** : Différence de taux de détection à 1 % de fausses alertes, mêmes lois P_θ, paramètres transformés par une bijection connue φ : Θ → Θ telle que P_{φ(θ)} = P_θ pour tout θ.
- **Seuil** : ε déterminé par permutation (mondes simulés où la défense ne reçoit jamais θ : bras 2).
- **Contrôle négatif** : Bras 2 (défense par échantillons seuls) ; par construction, elle ne voit pas θ, donc la reparamétrisation ne doit pas affecter son score au-delà du bruit.
- **Falsification** : Si la défense du bras 1 chute significativement sous reparamétrisation, H_A est falsifiée. Si elle ne chute pas et que le bras 2 non plus, H_B est falsifiée.
- **Étape d'application** : La transformation φ s'applique **après le gel de la défense**, sur les familles tenues à l'écart et sur les familles du score (iii), jamais sur les familles d'entraînement. Elle est choisie par un tiers (ou tirée aléatoirement d'un groupe de symétries déclaré), scellée avant le gel.

### Duel 3 (facultatif) — Deux échelles de temps vs une seule

- **H_A** : Le bras 5 (deux paliers) réduit (ii) − (iii) par rapport au bras 1 (un seul palier).
- **H_B** : Le bras 5 ne réduit pas (ii) − (iii) par rapport au bras 1.
- **Métrique** : Δ₅₁ = [(ii)₁ − (iii)₁] − [(ii)₅ − (iii)₅].
- **Seuil** : δ_min = 2 pp (illustratif).
- **Contrôle négatif** : Bras 3.
- **Falsification** : Symétrique au duel 1.

---

## (c) Mesure minimale de chaque instrument

### Défense

Plan de simulation à vérité connue : M = 200 mondes (illustratif). Dans chaque monde, K = 50 familles d'entraînement (illustratif), K' = 20 familles tenues à l'écart (illustratif), n = 500 tirages par famille (illustratif), déplacement Δ_loi connu par construction. Mesure : taux de détection à 1 % de fausses alertes ; cas honnêtes = tirages de la loi de référence P₀ appariés par graine. Vérification mécanique à battre : test de Kolmogorov-Smirnov multivarié (ou test MMD à noyau fixe, référence à vérifier) appliqué aux mêmes activations, sans apprentissage. Contrôle négatif : sous H₀ (pas de déplacement), le taux de fausses alertes de la défense doit être ≤ 1 % ± intervalle binomial.

### Générateur adaptatif

Dans chaque monde, le pire cas analytique ou par grille fine de la classe est calculé (vérité connue). Le générateur reçoit B = 1000 évaluations (illustratif) de la défense figée. Mesure : |score_générateur − score_pire_cas_connu|. Le générateur fonctionne si cet écart est ≤ 2 pp (illustratif) dans ≥ 90 % des mondes. Contrôle négatif : générateur aléatoire (θ tiré uniformément dans Θ).

### Mesure de dépendance

Construction : dans chaque monde, le niveau de dépendance entre familles d'entraînement et familles tenues à l'écart est fixé par construction (par exemple : corrélation entre θ_train et θ_écart dans [0, 0.3, 0.6, 0.9], illustratif). La mesure (par exemple, distance en énergie entre les distributions empiriques de θ_train et θ_écart, ou information mutuelle estimée par k-NN) doit retrouver l'ordre des niveaux connus dans ≥ 95 % des mondes. Contrôle négatif : indépendance exacte (graines séparées, régions disjointes de Θ) ; la mesure doit renvoyer une valeur ≤ seuil de bruit.

### Test de reparamétrisation

Construction : deux défenses dans chaque monde — l'une entraînée sur θ brut (susceptible d'apprendre la paramétrisation), l'autre entraînée uniquement sur des statistiques suffisantes de P_θ (apprend les lois par construction). La reparamétrisation φ est appliquée. Le test doit détecter une chute ≥ 5 pp (illustratif) chez la première et une chute ≤ 1 pp chez la seconde, dans ≥ 80 % des mondes. Contrôle négatif : appliquer l'identité au lieu de φ ; aucune chute attendue pour les deux.

---

## Bloc 1 — Compatibilité des deux règles (250 mots max)

Les deux règles sont **compatibles si elles portent sur des étapes différentes**. À l'entraînement, la défense joue en dernier : elle reçoit θ et ajuste ses poids pour détecter le déplacement correspondant. Elle en tire un avantage informationnel légitime car l'objectif est d'apprendre une détection robuste. À l'évaluation (score iii), le générateur joue en dernier contre la défense figée : il cherche le pire cas, ce qui produit un chiffre honnête.

L'avantage de θ **améliore** potentiellement la défense apprise (il oriente l'apprentissage vers les déplacements pertinents). Il **peut fausser** le chiffre publié s'il fuit dans l'étalonnage du seuil ou dans la sélection du point de contrôle.

**Étapes et légitimité :**

- **Entraînement** : légitime — θ est une entrée d'entraînement, analogue à une étiquette supervisée.
- **Sélection de la défense** (choix de l'architecture, des hyperparamètres, du point de contrôle) : légitime **seulement** si elle se fait sur un ensemble de validation disjoint des familles d'entraînement et des familles tenues à l'écart, sans θ en entrée. Si la sélection utilise θ ou les familles tenues à l'écart, il y a fuite.
- **Étalonnage du seuil** : illégitime si θ est utilisé. Le seuil doit être fixé sur les cas honnêtes seuls (loi de référence, pas de déplacement, pas de θ).
- **Mesure finale** (scores ii et iii) : θ **ne doit pas entrer** dans la défense. La défense est figée ; le générateur joue en dernier.

L'avantage cesse d'être légitime **après le gel des poids**, c'est-à-dire à partir de l'étalonnage du seuil.

---

## Bloc 2 — Trois scores et dépendance (400 mots max)

**Score (i)** : Taux de détection sur les familles vues à l'entraînement. Statistique : proportion de tirages correctement détectés comme déplacés, à 1 % de fausses alertes. Unité d'échantillonnage : une famille (θ_k, ensemble de tirages). Intervalle : bootstrap sur les K familles d'entraînement.

**Score (ii)** : Taux de détection sur les familles tenues à l'écart. Même statistique. Unité d'échantillonnage : une famille tenue à l'écart. Intervalle : bootstrap sur les K' familles tenues à l'écart.

**Score (iii)** : Pire cas mesuré. Après gel, le générateur choisit θ* en B évaluations. Statistique : taux de détection de la défense figée sur des tirages frais de P_{θ*}, à 1 % de fausses alertes. Intervalle : bootstrap sur les tirages frais, plus variabilité sur les mondes simulés.

**Signes prédits :**

- **(i) − (ii) > 0** (prédit positif) : condition — surapprentissage aux familles d'entraînement. L'amplitude croît avec la dépendance entre familles d'entraînement et tenues à l'écart, et avec la dimensionalité de θ. Si les familles tenues à l'écart sont dans la même région de Θ (support commun), l'écart est plus faible.
- **(ii) − (iii) > 0** (prédit positif) : condition — le générateur adaptatif trouve des θ plus difficiles que la moyenne des familles tenues à l'écart. L'amplitude dépend du budget B et de la complexité de la surface de détection.

**Sources de dépendance au niveau des lois :**

Les familles tenues à l'écart et les familles d'entraînement sont dépendantes si leurs paramètres θ sont tirés de distributions corrélées ou de régions de Θ qui se recouvrent. Au niveau des lois : si Θ_train ∩ Θ_écart ≠ ∅, les lois P_θ des deux ensembles partagent des structures que la défense a déjà vues.

**Mesure calculable de la dépendance :** Distance d'énergie (Székely et Rizzo, 2004 — référence à vérifier) entre les distributions empiriques {θ_k}_train et {θ_k}_écart dans Θ. Notons D cette distance. Prédiction : (i) − (ii) ≈ α · D + β, avec α > 0 (illustratif : α ~ 0.5 pp par unité de D). Quand D → 0 (support commun), (i) − (ii) se réduit au surapprentissage pur ; quand D est grand (support disjoint), l'écart reflète l'absence de transfert.

---

## Bloc 3 — Expérience décisive (600 mots max)

**Unité de budget :** Nombre total d'évaluations de la défense (forward passes sur activations synthétiques) par bras. Budget B_total = 10⁶ (illustratif).

### Description des cinq bras

| Bras | Boucle ? | Ce que reçoit la défense | Détail |
|------|----------|--------------------------|--------|
| 1 | Oui, G générations | θ en entrée (entraînement seulement) | Défense informée des paramètres |
| 2 | Oui, G générations (même déroulement que bras 1) | Échantillons tirés des mêmes familles, pas θ | Défense par échantillons |
| 3 | Non, banque fixe | Échantillons, pas θ | Pas de boucle |
| 4 | Oui, G générations | Échantillons et scores des familles produites par le générateur (fait 9) ; le générateur joue en dernier à chaque génération | Protocole du champ |
| 5 | Oui, G générations | θ en entrée (entraînement seulement) + palier rapide entre lots, palier lent entre générations | Deux échelles de temps |

G = 10 générations (illustratif). Pour le score (iii), le générateur reçoit B_eval = 1000 évaluations (illustratif) de chaque défense figée.

### Régimes de dépendance

- **Support commun :** θ_écart ∼ même distribution que θ_train sur la même région de Θ, graine scellée séparée.
- **Support disjoint :** Θ est partitionné ; θ_train et θ_écart sont tirés de partitions disjointes.

### Test de reparamétrisation

Appliqué **après le gel de toutes les défenses**, sur les familles tenues à l'écart et les familles du score (iii). La transformation φ est tirée d'un groupe de symétries du schéma (par exemple, permutation des composantes de θ si le schéma est invariant par permutation, ou transformation affine). Elle est choisie par un tirage aléatoire scellé avant le gel. Le test compare score(ii)_original et score(ii)_reparamétré pour chaque bras.

### Seuils de décision de l'expérience

- Seuil de signification : α_exp = 0.05 (bilatéral).
- Effet minimal δ_min = 3 pp (illustratif) pour le duel 1, ε = 2 pp (illustratif) pour le duel 2.

### Contrôle négatif

Bras 3 : sans boucle ni information privilégiée ; tout gain des bras 1, 2, 4, 5 sur le bras 3 est attribuable à la boucle ou à l'information.

### Condition d'échec de l'idée

L'idée échoue si **l'une** des conditions suivantes est remplie :

1. Bras 1 ne dépasse pas bras 2 sur (ii) ET sur (iii) d'au moins δ_min.
2. Le test de reparamétrisation montre que bras 1 a appris la paramétrisation (chute > ε sous φ).
3. Δ = [(ii)₂ − (iii)₂] − [(ii)₁ − (iii)₁] ≤ 0.

### Calcul de puissance

M = 200 mondes simulés (illustratif). Chaque monde : K = 50 familles d'entraînement, K' = 20 familles tenues à l'écart, n = 500 tirages par famille. Effet supposé : δ = 5 pp (illustratif) sur (ii)₁ − (ii)₂ et sur Δ. Variance inter-mondes estimée lors d'un pilote de 20 mondes. Puissance cible : 80 % au seuil 0.05.

### Tableau de prédictions (illustratif)

| Bras | Régime | (ii)−(iii) prédit | Signe | (i) | (ii) | (iii) |
|------|--------|-------------------|-------|-----|------|-------|
| 1 | commun | 8 pp | + | 92 % | 85 % | 77 % |
| 1 | disjoint | 15 pp | + | 92 % | 72 % | 57 % |
| 2 | commun | 12 pp | + | 88 % | 80 % | 68 % |
| 2 | disjoint | 20 pp | + | 88 % | 65 % | 45 % |
| 3 | commun | 18 pp | + | 82 % | 70 % | 52 % |
| 3 | disjoint | 25 pp | + | 82 % | 58 % | 33 % |
| 4 | commun | 10 pp | + | 86 % | 82 % | 72 % |
| 4 | disjoint | 16 pp | + | 86 % | 68 % | 52 % |
| 5 | commun | 6 pp | + | 90 % | 86 % | 80 % |
| 5 | disjoint | 12 pp | + | 90 % | 74 % | 62 % |

Tous les chiffres sont **illustratifs**.

---

## Bloc 4 — La quantité qui tranche (200 mots max)

**Contraste :** Δ = [(ii)₂ − (iii)₂] − [(ii)₁ − (iii)₁]

**Estimateur :** Différence des écarts observés entre bras 2 et bras 1, calculée dans chaque monde simulé ; moyenne et intervalle bootstrap (percentile, 95 %) sur les M mondes.

**Intervalle :** IC₉₅ par bootstrap stratifié (stratification sur les régimes de dépendance).

**Effet minimal :** δ_min = 3 pp (illustratif).

**Signe prédit :** Δ > 0. L'avantage des paramètres à l'entraînement produit une défense dont le score (ii) est plus élevé et dont le score (iii) résiste mieux au pire cas, **à condition** que la défense ait appris les lois et non la paramétrisation (test de reparamétrisation passé). Cela réduit (ii) − (iii) car la défense généralisera mieux aux θ difficiles.

**Issue qui falsifie :**
- Si la borne supérieure de l'IC₉₅ de Δ est ≤ 0 : H_A (l'avantage réduit l'écart) est falsifiée.
- Si la borne inférieure de l'IC₉₅ de Δ est > δ_min : H_B (pas de réduction) est falsifiée.

---

## Bloc 5 — Conclusion (150 mots max)

**Verdict :** L'idée est **potentiellement bonne pour la conception**, sous conditions mesurables. Elle n'est ni bonne ni mauvaise pour l'évaluation au sens direct (le chiffre publié reste le score iii, indépendant de θ), mais elle est bonne pour l'évaluation si Δ > δ_min, car le score (ii) devient alors une estimation moins optimiste du score (iii).

**Conditions mesurables :**
1. Bras 1 dépasse bras 2 d'au moins δ_min sur (ii) et (iii).
2. Le test de reparamétrisation est passé (pas de chute sous φ).
3. Δ > δ_min.

**Effet des régimes :** En support commun, les conditions 1 et 3 sont plus faciles à remplir. En support disjoint, le transfert est plus exigeant ; si le fait 11 se confirme (transfert mitigé), la condition 1 pourrait échouer.

**Effet du test de reparamétrisation :** S'il échoue (H_B du duel 2), l'idée est mauvaise : le gain apparent est un artefact de la paramétrisation.

---

## (d) Ancrage matériel

Activations synthétiques sur CPU. Dimension d = 100 (illustratif). 200 mondes × 5 bras × 2 régimes × 70 familles × 500 tirages ≈ 7 × 10⁹ tirages. Défense : petit réseau (≤ 10⁵ paramètres, illustratif). Coût estimé : ≈ 200–500 heures-CPU (illustratif), soit ~ 50–150 USD sur cloud standard (illustratif). Aucun GPU ni modèle de langage requis.

FIN-DE-CELLULE