

# Proposition B — Tour III.3 : réponse aux critiques

---

## Inventaire des critiques visant la Proposition B

Je classe chaque critique par source (A, C, D) et numéro, puis la traite.

---

### Critique A.1 — Fuite de l'étiquette dans l'entrée (mode déclaré)

**Résumé.** Si θ est donné en entrée à l'entraînement et absent à l'évaluation, la défense peut résoudre la tâche sur θ seul sans exploiter les activations ; à l'évaluation, l'entrée manquante crée un décalage de régime jamais vu. Le contraste 1−2 confondrait « information sur les lois » et « décalage d'entrée ».

**Acceptée pour l'essentiel.** La critique identifie un confondant réel. Mon mode déclaré ne spécifiait pas la valeur de remplacement de θ à l'évaluation, ni ce que reçoivent les cas honnêtes à l'entraînement. Sans ces précisions, la défense peut court-circuiter les activations.

**Correction.** Je modifie le mode déclaré : θ n'est plus une *entrée* du réseau mais une **cible auxiliaire à prédire depuis les activations** (tête auxiliaire de régression, pondérée par un coefficient λ dans la perte totale ; la tête est ignorée à l'évaluation). Ainsi, le chemin d'inférence ne reçoit jamais θ, et le décalage d'entrée disparaît. Les cas honnêtes reçoivent la cible θ₀ (point de référence, pas de déplacement). Ce mode est celui de la proposition A ; je le reprends explicitement, en le signalant. Le bras 1 corrigé produit une défense qui, à l'évaluation, ne voit que les activations, exactement comme les bras 2–4.

**Contrôle ajouté** (repris de A, critique (c)) : bras 1 avec θ̃ permuté aléatoirement entre familles (même architecture, même boucle, étiquettes décorrélées de la loi). Si le gain du bras 1 sur le bras 2 disparaît sous permutation, il est attribuable à l'information de θ.

---

### Critique A.2 — Test de reparamétrisation nul par construction

**Résumé.** Sous mon mode déclaré (θ en entrée à l'entraînement, absent à l'évaluation), et avec φ telle que P_{φ(θ)} = P_θ appliquée après le gel, la sortie de la défense est strictement invariante : le test a une puissance nulle.

**Acceptée.** La critique est mathématiquement exacte. Sous le mode déclaré d'origine, la défense figée ne voit que les activations ; si les lois sont identiques, les sorties sont identiques. Le duel 2 était tranché avant toute mesure, ce qui le rendait non informatif.

**Correction en deux temps.**

1. Le passage au mode « cible auxiliaire » (correction de A.1) rend le test potentiellement informatif : la tête auxiliaire a été entraînée à prédire θ ; on peut maintenant appliquer φ **à l'entraînement** (remplacer les cibles θ par φ(θ), réentraîner complètement) et comparer les scores (ii) des deux défenses résultantes.

2. φ ne doit **pas** satisfaire P_{φ(θ)} = P_θ (ce qui la rendrait triviale dans un modèle identifiable). φ est une bijection qui **change les coordonnées mais pas les lois** : c'est une reparamétrisation au sens statistique, applicable quand le modèle n'est pas identifiable en (certaines composantes de) θ, ou bien une transformation qui modifie l'échelle et la géométrie de l'espace des cibles (affine anisotrope, monotone non linéaire par coordonnée) *sans* être une isométrie de la perte. Ce que le test mesure : est-ce que la représentation interne a capté les lois (invariance) ou la carte paramétrique (chute) ?

**Attention au confondant d'optimisation** (critique C.a.4 sur A et D.a critique de C) : une φ à fort étirement ou non linéaire peut dégrader la convergence de la tête, ce qui produit une chute par artefact. **Contrôle ajouté** : inclure une φ isométrique (rotation/permutation dans Θ qui préserve ‖·‖₂) comme contrôle intermédiaire. Si la chute se produit sous la rotation isométrique, c'est un artefact d'optimisation ; si elle se produit seulement sous la transformation anisotrope, le diagnostic d'apprentissage de la paramétrisation est plus plausible.

---

### Critique A.3 — Duel 1 non exhaustif (zone d'indécision)

**Résumé.** H_A : Δ > δ_min ; H_B : Δ ≤ 0. L'intervalle (0, δ_min] ne falsifie rien.

**Acceptée.** C'est un défaut de formulation. **Correction** : H_A : Δ ≥ δ_min ; H_B : Δ ≤ 0. L'intervalle (0, δ_min) est une zone d'indécision explicite, déclarée comme telle. Si l'IC₉₅ est entièrement dans cette zone, le résultat est « non concluant ». Cela est conforme à B4 (chaque issue falsifie quelque chose) : si l'IC est au-dessus de δ_min, H_B est falsifiée ; si en dessous de 0, H_A est falsifiée.

---

### Critique A.4 — Le bras 3 n'est pas un contrôle négatif

**Résumé.** Le bras 3 est un traitement comparatif, pas un nul connu par construction.

**Acceptée.** **Correction** : le bras 3 est reclassé comme **bras de comparaison**, non comme contrôle négatif. Le vrai contrôle négatif est : (i) bras 1 avec θ̃ permuté (gain nul attendu par rapport au bras 2) ; (ii) défense constante (sortie indépendante des activations) : (ii) = (iii) attendu ; (iii) deux copies du bras 2 à graines différentes : Δ ≈ 0 attendu.

---

### Critique A.5 — Qui propose les familles dans la boucle des bras 1-2 ?

**Acceptée. Confondant identifié aussi par C.a.1 (sur A) et D.a.** Si le générateur cible les faiblesses du bras 1, le bras 2 reçoit des familles non adaptées à lui. **Correction** : les bras 1 et 2 reçoivent les familles produites par un **générateur tiers, optimisant contre la défense du bras 3** (banque fixe), identique pour les deux bras à chaque génération. Ainsi, la trajectoire coévolutive est commune et ne cible ni le bras 1 ni le bras 2.

---

### Critique A.6 — Budget incomplet

**Acceptée.** Les évaluations du générateur (bras 4) et le palier rapide (bras 5) n'étaient pas comptabilisés. **Correction** : l'unité de budget est redéfinie comme le nombre total de **tirages d'activations synthétiques générés** (et non les seuls forward passes de la défense). Tout tirage utilisé par le générateur, le palier rapide ou l'entraînement est comptabilisé.

---

### Critique A.7 — Mesure de dépendance non invariante par reparamétrisation

**Acceptée.** La distance d'énergie dans Θ dépend de la carte paramétrique. **Correction** : remplacer par une distance entre **lois** plutôt qu'entre paramètres. Utiliser la distance MMD entre les distributions empiriques des lois (estimée via les activations synthétiques, par noyau fixe), ou la divergence de Jeffreys symétrisée si les lois sont gaussiennes. Conditions de non-dégénérescence : déclarées (support plein, dimension effective suffisante, cf. critique C.b.1 sur D).

---

### Critique A.8 — (i) − (ii) confond nouveauté et difficulté

**Acceptée.** **Correction** : calculer le score de l'oracle (test du rapport de vraisemblance P_θ contre P₀ à 1 % de fausses alertes, connu par construction) sur chaque ensemble. L'écart (i) − (ii) est rapporté net de l'écart de l'oracle, c'est-à-dire [(i) − (ii)]_défense − [(i) − (ii)]_oracle. Cela isole l'effet de généralisation de la défense de la difficulté intrinsèque.

---

### Critique C.a.1 (sur B) — Défaut fatal du mode d'entrée et du test de reparamétrisation

**Traitement combiné avec A.1 et A.2.** Le mode est corrigé (cible auxiliaire). Le test de reparamétrisation est corrigé (φ appliquée à l'entraînement, réentraînement complet). Voir ci-dessus.

Concernant la contradiction relevée par C (invariance stricte après gel si θ n'entre pas) : **acceptée et résolue** par le changement de protocole du duel 2 (réentraînement sous φ(θ) comme cibles, comparaison des scores (ii) résultants).

---

### Critique C.a.2 — Fuite d'information au bras 4

**Partiellement acceptée.** Le bras 4 confond deux facteurs (ordre du dernier coup et accès aux scores passés). **Correction** : le bras 4 est clarifié : la défense reçoit les échantillons d'activations des familles produites par le générateur (mais pas les scores de la défense sur ces familles). Le générateur joue en dernier à chaque génération. Cela isole l'ordre du coup. Si l'on veut tester l'effet des scores, un sixième bras serait nécessaire, mais cela sort du budget de cinq bras.

---

### Critique C.a.3 — Asymétrie de budget du bras 3

**Acceptée** (identique à A.6). Voir correction ci-dessus.

---

### Critique C.b.1 — Invariance non identifiable dans les schémas injectifs

**Acceptée dans le principe.** Dans un modèle identifiable, la seule φ telle que P_{φ(θ)} = P_θ est l'identité (plus éventuellement les symétries internes). **Correction** : φ est redéfinie comme une transformation qui **change les coordonnées de l'espace cible de la tête auxiliaire** sans contrainte P_{φ(θ)} = P_θ. Le test ne demande plus l'invariance des lois sous φ ; il vérifie si la représentation interne (encodeur partagé) est sensible au changement de carte des cibles. La puissance du test vient de la comparaison avec le contrôle isométrique.

---

### Critique C.b.2 — Distance d'énergie sur Θ dégénère avec coordonnées muettes

**Acceptée.** Couverte par la correction A.7 (passage à une distance entre lois).

---

### Critique C.b.3 — Sous-échantillonnage du seuil à 1 % de fausses alertes

**Acceptée.** Avec n = 500 tirages honnêtes, le quantile empirique à 1 % repose sur ~5 valeurs. **Correction** : le nombre de cas honnêtes pour l'étalonnage du seuil est augmenté à n₀ = 10 000 (illustratif), séparé du nombre de tirages par famille pour l'évaluation (n = 500, illustratif). Le seuil est étalonné une seule fois, sur un grand pool de cas honnêtes, avant toute évaluation.

---

### Critique C.c.1 — Absence de contrôle de sensibilité du test de reparamétrisation

**Acceptée et résolue** par le nouveau protocole du duel 2 (réentraînement sous φ). Le contrôle positif est une défense construite pour dépendre explicitement de la carte (tête linéaire sans activation, poids proportionnels à θ).

---

### Critique C.c.2 — Absence de contrôle par permutation des θ au bras 1

**Acceptée.** Contrôle ajouté (voir correction de A.1).

---

### Critique C.c.3 — Absence de contrôle de dépendance au niveau des lois

**Acceptée et résolue** par le passage à une mesure entre lois (correction A.7). Contrôle négatif ajouté : familles ayant des θ très différents dans des coordonnées à information de Fisher nulle mais des lois identiques ; la mesure doit renvoyer ~0.

---

### Critique D.a — Test de reparamétrisation vide + mode sous-spécifié + distance d'énergie + bras 3

**Toutes acceptées.** Couvertes par les corrections ci-dessus (mode → cible auxiliaire ; test → réentraînement sous φ ; distance → entre lois ; bras 3 → comparaison, pas contrôle négatif).

---

### Critique D.b — Conditions de perte de puissance

- **Même marginale de θ peut signifier indépendance ou recopie** : acceptée, résolue par le passage à la distance entre lois, avec validation sur trois configurations (indépendants même marginale, recopiés, supports disjoints).
- **Score (iii) : pire cas atteint seulement si le générateur approche l'infimum** : acceptée. Le contrôle du regret (section (c) de ma conception) reste, avec un seuil maximal tolérable ρ_max < δ_min / 2 (illustratif : 1.5 pp). Si ρ > ρ_max pour un bras, le monde est marqué non jugeable pour le duel 1.
- **Taux de fausses alertes différents entre bras** : acceptée. Correction : vérification post-hoc que |FAR_b − 0.01| ≤ 0.003 (illustratif) pour chaque bras sur les cas honnêtes indépendants de l'étalonnage.

---

### Critique D.c — Contrôles négatifs manquants

1. **Remplacement du test post-gel** : fait (réentraînement sous φ).
2. **Bras à θ randomisé + rejeu commun** : fait (θ permuté + générateur tiers).
3. **Validation de la mesure de dépendance sur trois configurations** : fait (voir ci-dessus).
4. **Équivalence des taux de fausses alertes** : fait (vérification post-hoc).

---

## (b) Expérience corrigée — résumé en cinq lignes

1. **Mode** : θ est une cible auxiliaire prédite par une tête de régression depuis les activations ; la tête est ignorée après le gel ; le chemin d'inférence ne reçoit jamais θ.
2. **Bras 1–5** : familles d'entraînement produites par un générateur tiers (optimisant contre le bras 3), identiques pour les bras 1 et 2 ; budget en tirages totaux d'activations, incluant les évaluations du générateur et le palier rapide.
3. **Duel 2 corrigé** : φ appliquée aux cibles d'entraînement (réentraînement complet sous φ(θ)), avec contrôle isométrique (rotation) et contrôle anisotrope ; seuil ε calibré par la variance de réentraînement (deux copies à graines différentes).
4. **Mesure de dépendance** : distance MMD entre lois (sur activations), non entre θ ; validée sur trois configurations construites.
5. **Contrôles négatifs** : θ permuté (bras 1'), défense constante, deux copies du bras 2, oracle p*, vérification FAR indépendante, seuil ρ_max sur le regret du générateur.

---

## (c) Réponse à la question de l'arbitre — en une page

### Ce qui est établi

- La compatibilité des deux règles (défense en dernier à l'entraînement, générateur en dernier à l'évaluation) est **établie logiquement** : elles portent sur des étapes distinctes, à condition que θ ne fuie pas dans l'étalonnage du seuil ni dans la sélection (bloc 1). Le mode « cible auxiliaire » garantit l'absence de fuite à l'évaluation.
- Le signe (ii) − (iii) > 0 est **établi sous la condition** que le générateur adaptatif approche le pire cas (regret ρ ≤ ρ_max) et que les familles tenues à l'écart ne sont pas plus difficiles que la moyenne de Θ pour l'oracle. (HYPOTHÈSE pour le premier point ; vérifiable par construction pour le second.)
- Le signe (i) − (ii) > 0 **n'est pas établi a priori** : il dépend de la difficulté relative des familles (contrôle par l'oracle) et du surapprentissage. Net de l'oracle, le signe est prédit positif (HYPOTHÈSE).
- Le transfert hors de la classe entraînée est **mitigé** (fait 11, RAPPORTÉ) : le signe du gain est empiriquement variable.

### Ce qui n'est pas établi

- **L'avantage de θ comme cible auxiliaire réduit-il l'écart (ii) − (iii) ?** C'est la quantité Δ du bloc 4. Son signe est prédit positif (HYPOTHÈSE), non mesuré (fait 3 : rien n'est construit).
- **La défense apprend-elle les lois ou la paramétrisation ?** Le test de reparamétrisation (duel 2, corrigé) est conçu pour trancher, mais sa puissance dépend du choix de φ et de la capacité de la tête auxiliaire (confondant d'optimisation identifié par C sur A et D).
- **Le bras 5 (deux échelles de temps) améliore-t-il le bras 1 ?** HYPOTHÈSE, non mesuré.
- **Le générateur adaptatif à budget fini approche-t-il le pire cas ?** HYPOTHÈSE de cadre (fait 4). Le regret est contrôlable par construction dans la simulation mais non garanti a priori.

### Verdict

**Verdict conditionnel : bonne pour la conception ET pour l'évaluation, sous trois conditions mesurables :**

1. Bras 1 dépasse bras 2 d'au moins δ_min = 3 pp (illustratif) sur (ii) **et** sur (iii), net de l'oracle. Le contrôle par permutation (bras 1') confirme que le gain provient de θ.
2. Le test de reparamétrisation (duel 2, corrigé) ne montre pas de chute sous φ anisotrope supérieure à la chute sous φ isométrique, au-delà de la variance de réentraînement.
3. Δ = [(ii)₂ − (iii)₂] − [(ii)₁ − (iii)₁] > δ_min, avec borne inférieure de l'IC₉₅ > 0.

Si les conditions 1 et 2 sont remplies mais pas la condition 3 : bonne pour la conception seulement. Si la condition 2 échoue (chute anisotrope > chute isométrique + ε) : l'idée est mauvaise, le gain est un artefact de la paramétrisation. En support disjoint, la condition 1 est plus exigeante ; si le fait 11 se confirme (transfert négatif hors classe), la condition 1 pourrait échouer sous ce régime sans invalider l'idée en support commun.

### Quantité qui tranche

Δ = [(ii)₂ − (iii)₂] − [(ii)₁ − (iii)₁]. Signe prédit : positif. Seuil : δ_min = 3 pp (illustratif). Issue falsifiante : borne supérieure de l'IC₉₅ ≤ 0 falsifie H_A ; borne inférieure > δ_min falsifie H_B.

### Expérience à faire en premier

Le **duel 2 corrigé** (test de reparamétrisation par réentraînement sous φ) : il est peu coûteux (deux réentraînements + un contrôle isométrique), ne nécessite pas le générateur adaptatif, et si la défense a appris la paramétrisation, toute l'idée est invalidée sans besoin de mesurer Δ.

FIN-DE-CELLULE