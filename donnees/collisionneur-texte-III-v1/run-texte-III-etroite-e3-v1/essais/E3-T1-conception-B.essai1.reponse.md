

# Proposition B — Tour III.1

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Supposition | Statut |
|---|-------------|--------|
| a1 | Les 37 familles observées sont correctement appariées en familles canoniques (le fait 17 est RAPPORTÉ : décompte d'un lecteur unique, appariement non contre-lu). | RAPPORTÉ |
| a2 | La déviance 12,9 / 3 ddl est correcte (fait 18 : non recalculée, cohérence interne seulement vérifiée). | RAPPORTÉ |
| a3 | La population de familles est fermée : il existe un nombre fini N de familles « découvrables » par les trois sources. | HYPOTHÈSE |
| a4 | Les familles sont échangeables (probabilité de capture identique par source) — nécessaire pour Chao et les modèles M₀/Mₕ. | HYPOTHÈSE |
| a5 | Les familles « tenues à l'écart » sont tirées de la même distribution que celles vues ; la question traite leur rétention comme un simple partitionnement, pas comme une censure sélective. | HYPOTHÈSE |
| a6 | La borne à zéro échec (fait 9) s'applique : les familles testées sont i.i.d. selon la loi qui définit ε. Le fait 9 dit explicitement que l'hypothèse n'est pas satisfaite pour des familles découvertes. | HYPOTHÈSE (violée par construction) |
| a7 | L'universalité peut être définie par un quantificateur sur une classe déclarée d'avance — cela suppose que la classe est spécifiable avant la mesure. | HYPOTHÈSE |

---

## (b) Duels décisifs

### Duel 1 — Couverture nominale sous dépendance

**H_A** : L'intervalle binomial à zéro échec (fait 9, hypothèse i.i.d.) conserve une couverture ≥ 0.95 même quand les familles sont découvertes avec dépendance positive modérée (corrélation intra-classe ρ ≤ 0.15, illustratif).

**H_B** : La couverture effective tombe sous 0.85 (illustratif) dès que ρ > 0.05 (illustratif), et un estimateur ajusté (borne de Chao pour N̂, puis tirage pondéré) maintient la couverture ≥ 0.90.

- **Métrique** : couverture empirique de l'intervalle de confiance à 95 % sur 10 000 mondes simulés (illustratif) à vérité connue (N fixé, ε fixé).
- **Seuil** : couverture < 0.85 pour l'intervalle i.i.d. sur ≥ 3 configurations de ρ.
- **Contrôle négatif** : monde sans dépendance (ρ = 0) ; les deux estimateurs doivent donner couverture ≥ 0.93.
- **Falsification** : Si H_A tient (couverture ≥ 0.95 partout), la correction pour dépendance est superflue et ajoute de la variance inutile. Si H_B tient, la borne du fait 9 est invalide pour des familles découvertes.

### Duel 2 — Estimateur du nombre de familles sous hétérogénéité

**H_A** : Le Chao lower bound (borne inférieure de Chao, 1987 — référence à vérifier : Chao, 1987, « Estimating the Population Size for Capture-Recapture Data with Unequal Catchability ») reste un estimateur valide (biais ≤ 5 % de N) sous hétérogénéité de capture entre familles (modèle Mₕ).

**H_B** : Sous hétérogénéité forte (coefficient de variation des probabilités de capture CV > 0.8, illustratif), Chao sous-estime N de > 15 % (illustratif), et un modèle log-linéaire avec interaction de paire fait mieux (biais < 8 %).

- **Métrique** : biais relatif (N̂ − N)/N et RMSE, sur 5 000 mondes simulés (illustratif).
- **Seuil** : biais absolu > 15 % et RMSE du log-linéaire < RMSE de Chao sur ≥ 2 niveaux de CV.
- **Contrôle négatif** : monde M₀ (capture homogène, sources indépendantes) ; Chao doit être quasi non biaisé.
- **Falsification** : Si H_A tient, le modèle log-linéaire complexifie sans gain. Si H_B tient, Chao seul ne suffit pas pour la borne inférieure.

---

## (c) Mesure minimale de chaque instrument

### Instrument 1 — Estimateur des familles inconnues

**Plan de simulation à vérité connue.** On fixe N ∈ {50, 80, 120, 200} (illustratif). Trois sources tirent chacune des familles avec probabilités pⱼ (j = 1,2,3). Facteurs croisés :

- Dépendance : ρ ∈ {0, 0.10, 0.25} (illustratif), modélisée par variable latente Beta(a,b) commune.
- Hétérogénéité de capture : CV(pⱼ) ∈ {0, 0.5, 1.0} (illustratif).
- Erreur d'appariement : taux de fusion à tort ∈ {0, 0.05}, scission à tort ∈ {0, 0.05} (illustratif).

**Mesures** : couverture de l'IC à 95 % pour N, biais relatif, largeur médiane de l'IC. **Base à battre** : comptage brut n_obs = 37 (pas d'intervalle). L'estimateur est jugé fonctionnel si : (i) couverture ≥ 0.90 sur ≥ 80 % des configurations ; (ii) biais relatif médian < 10 % ; (iii) IC strictement plus informatif que [n_obs, +∞).

**Contrôle négatif** : monde M₀ avec N = n_obs (aucune famille manquante) ; l'estimateur doit couvrir N sans gonfler.

### Instrument 2 — Mesure d'universalité

**Plan** : On fixe la proportion réelle ε de familles où la défense échoue. On simule le tirage de k familles (découvertes, non i.i.d.) et on mesure si la borne supérieure sur ε couvre la vraie valeur.

**Mesures** : couverture de la borne, puissance (probabilité de rejeter ε ≥ ε₀ quand ε < ε₀). **Base à battre** : la borne binomiale naïve (fait 9). L'instrument fonctionne si la couverture reste ≥ 0.90 sous dépendance et si la puissance dépasse celle de la borne naïve quand ρ > 0.

---

## Bloc 1 — Définition opérationnelle de l'universalité (≤ 350 mots)

**Options comparées :**

| Option | Énoncé (quantificateur, classe, statistique) | Déclarer avant | N'autorise pas | Recalcul par tiers |
|--------|-----------------------------------------------|----------------|----------------|---------------------|
| Pire cas | « ∀ famille f ∈ C, performance(f) ≥ τ » | C (schéma), τ | Généralisation hors C | Vérifier chaque f ∈ C |
| Écart vu/retenu | « |perf_vues − perf_retenues| ≤ δ » | δ, partition | Dire que la défense est bonne, seulement qu'elle ne se dégrade pas | Comparer moyennes |
| Quantile | « P_f∈C(perf(f) ≥ τ) ≥ 1 − ε » | C, τ, ε | Garantie individuelle | Estimer la proportion empirique |

**Distinction.** « Universelle sur la classe déclarée » = quantificateur portant sur C défini avant ; « robuste à l'inconnu » = affirmation sur des familles hors de C, non falsifiable sans extension de C.

**Option retenue** : le **quantile**. Énoncé : « Avec confiance 1 − α, la proportion de familles de la classe C où la défense échoue est au plus ε. » Raisons : (i) le pire cas exige d'énumérer C en entier, irréaliste si N est inconnu ; (ii) l'écart vu/retenu est un diagnostic de surapprentissage, pas une mesure d'universalité ; (iii) le quantile est compatible avec un échantillonnage et fournit un énoncé probabiliste falsifiable. On déclare avant la mesure : C (schéma de construction), τ (seuil de succès), ε, α.

---

## Bloc 2 — Nombre de familles nécessaire (≤ 350 mots)

**Énoncé cible** : avec confiance 1 − α, la part de C où la défense échoue est < ε.

**Sous indépendance (fait 9)** : n ≥ ln α / ln(1 − ε). Pour α = 0.05, ε = 0.10 : n ≥ 29 ; ε = 0.05 : n ≥ 59.

**Sous découverte (violation du fait 9).** Les familles ne sont pas tirées i.i.d. ; elles sont découvertes par des sources qui partagent des biais. Deux conséquences :

1. **Taille effective réduite.** Avec une corrélation intra-classe ρ entre indicateurs de découverte, la taille effective est n_eff ≈ n / (1 + (n−1)ρ). Pour n = 37, ρ = 0.10 (illustratif) : n_eff ≈ 8.4 (illustratif). La borne à zéro échec avec n_eff = 8 donne ε ≤ 0.31 (illustratif) au lieu de 0.08.

2. **Biais de sélection.** Si les sources découvrent préférentiellement les familles faciles à défendre, ε est sous-estimé.

**Règle de calcul proposée.** Simulation à deux niveaux : (i) tirer N familles avec probabilités de capture hétérogènes (Beta(a,b)) ; (ii) pour chaque famille, tirer un indicateur de succès/échec de la défense ; (iii) observer seulement les familles capturées ; (iv) estimer ε̂ et son IC. Varier ρ, CV, N, ε ; mesurer la couverture de l'IC. La **règle d'arrêt séquentielle** : continuer de découvrir des familles jusqu'à ce que la borne supérieure de l'IC sur ε soit < ε₀ ou que la largeur de l'IC stagne (plateau de découverte).

**Sensibilité** : le nombre nécessaire dépend fortement de ρ et du mécanisme de découverte. La simulation doit explorer des mécanismes contrastés (sélection sur la facilité vs. aléatoire vs. adversarial).

---

## Bloc 3 — Familles inconnues, sources dépendantes (≤ 500 mots)

### Estimateurs

**Notation.** Sources S₁ (22), S₂ (23), S₃ (27). Soit fⱼ le nombre de familles vues exactement j fois : f₁ = 16, f₂ = 7, f₃ = 14. Familles non vues : f₀ = N − 37.

**Borne inférieure de Chao (modèle Mₕ, sources agrégées).** Avec t = 3 sources traitées comme « occasions » : N̂_Chao ≥ n + f₁²/(2f₂) = 37 + 256/14 ≈ 55.3 (illustratif dans la mesure où le modèle Mₕ regroupe les occasions ; la formule est exacte sous ses hypothèses — référence à vérifier : Chao, 1987). IC par bootstrap ou formule de variance.

**Couverture de Good-Turing.** Ĉ = 1 − f₁/T où T = somme des captures = 72. Ĉ = 1 − 16/72 = 0.778. Ceci estime la probabilité qu'une capture supplémentaire tombe sur une famille déjà vue. Proportion estimée non couverte : 1 − Ĉ = 0.222.

### Modèles log-linéaires

Sept cellules non vides (les 2³ − 1 combinaisons de présence). Le modèle saturé a 7 paramètres. Le modèle d'indépendance complète [S₁][S₂][S₃] a 4 paramètres (constante + 3 effets principaux), donc 3 ddl. Le modèle à toutes les interactions de paire [S₁S₂][S₁S₃][S₂S₃] a 7 paramètres (4 + 3 interactions de paire) = saturé pour 7 cellules, donc 0 ddl : il est identifiable mais non testable. Un modèle à une interaction de paire a 5 paramètres, 2 ddl ; deux interactions : 6 paramètres, 1 ddl. Le modèle avec interaction d'ordre 3 nécessite ≥ 8 paramètres : non identifiable avec 7 cellules. Les modèles identifiables et testables sont donc ceux à 0, 1 ou 2 interactions de paire.

### Affectation des recaptures aux paires

Les recaptures par paire (incluant les familles communes aux trois) sont {16, 16, 17}. Notons mᵢⱼ la recapture de la paire (Sᵢ, Sⱼ). On a mᵢⱼ = nᵢⱼ + n₁₂₃ où nᵢⱼ est le nombre vu par exactement Sᵢ et Sⱼ, et n₁₂₃ = 14. Donc les nᵢⱼ pour exactement deux sources sont {2, 2, 3}, et leur somme = 7 ✓. Le modèle d'indépendance prédit des fréquences attendues proportionnelles à pᵢpⱼ. Avec p̂₁ = 22/37, p̂₂ = 23/37, p̂₃ = 27/37 (illustratif, dépend de N), la déviance 12.9/3ddl (p ≈ 0.005) rejette l'indépendance. L'affectation qui maximise la déviance sera celle qui met la plus grande recapture (17) sur la paire la plus attendue (S₂S₃, les deux plus grandes sources). **Ce calcul dépend de l'affectation** ; l'étendue sur les 3! = 6 permutations (mais {16,16} sont interchangeables, donc 3 affectations distinctes) devrait être évaluée ; la déviance rapportée « peut contraindre l'affectation » (fait 18). Calcul complet laissé à la simulation.

### Effets directionnels

| Facteur | Direction du biais sur N̂ |
|---------|--------------------------|
| Dépendance positive entre sources | Sous-estimation de N (les sources capturent les mêmes familles → surestimation de la couverture) |
| Hétérogénéité de capture | Sous-estimation de N (les familles à faible capture sont invisibles) |
| Fusion à tort (appariement) | Sous-estimation de n_obs → sous-estimation de N |
| Scission à tort | Surestimation de n_obs, augmente f₁ artificiellement → peut gonfler Chao |

### Estimateur recommandé

Sous rejet de l'indépendance : modèle log-linéaire avec la (les) interaction(s) de paire sélectionnée(s) par AIC/BIC parmi les modèles à 1 ou 2 ddl, donnant N̂ via la cellule f₀ estimée. Alternative bayésienne : prior sur N, vraisemblance log-linéaire, posterior sur N. **Censure commune** (familles inaccessibles aux trois sources) : N̂ est une borne inférieure du nombre total ; la fraction censurée est non identifiable sans information auxiliaire. **Population non fermée** : si de nouvelles familles peuvent être créées, N n'est pas fixe ; on estime plutôt la couverture (Good-Turing) à un instant donné.

---

## Bloc 4 — Validation extérieure chiffrée (≤ 250 mots)

**Source extérieure E** : propriétés statistiques seulement — taille nₑ (illustratif : 20), indépendante des trois sources, probabilité de capture uniforme pₑ (illustratif : 0.6).

**Confrontation 1 (bloc 3).** Prédiction scellée : la proportion de familles de E qui tombent hors des 37 observées. Si N̂ = 55 (illustratif), proportion prédite = (N̂ − 37)/N̂ ≈ 0.33 (illustratif). Seuil de falsification : si la proportion observée diffère de la prédiction de plus de 0.15 (illustratif) (test binomial exact, α = 0.05), l'estimateur est falsifié.

**Confrontation 2 (bloc 1).** Prédiction scellée : la performance de la défense sur les familles de E ne diffère pas de celle sur les 37 par plus de δ (illustratif : 0.10). Statistique : différence de proportions de succès. Seuil : p < 0.05 sur test de Fisher exact. Falsifie la définition d'universalité si l'écart est significatif.

**Confrontation 3 (bloc 2).** Prédiction scellée : si on observe k familles de E sans échec, la borne ε̂ issue de la simulation (bloc 2) est cohérente avec la borne naïve calculée sur E seule. Falsification : si les deux bornes sont incompatibles (IC disjoints).

---

## (d) Ancrage matériel

Simulations (10⁴ mondes × ~12 configurations × 3 estimateurs) : ~10⁶ ajustements log-linéaires, faisables en quelques heures sur un processeur moderne à ~50 € de coût cloud (illustratif). Modèles ouverts : R packages `Rcapture`, `mra` ; Python `statsmodels` pour log-linéaire. Pas de GPU requis.

FIN-DE-CELLULE