# Proposition B — Tour III.1 : allocation d'un budget entre choix de classe et ajustement

## 0. Pièces, statuts et périmètre

- **Bloc FAITS** : il ne contient aucun fait, par décision explicite de l'arbitre. Ce n'est donc pas une pièce manquante. En conséquence, **rien ci-dessous n'est VÉRIFIÉ**.
- **Pièce `89d8c3db…`** : elle est seulement mentionnée et n'a pas été transmise. Je n'en infère rien.
- **Propositions A et C** : elles ne sont pas visibles, car le tour se joue à l'aveugle. La règle B1 ne peut donc pas s'exercer ici, et je n'invente aucune attaque.
- **Légende des statuts** :
  - **HYPOTHÈSE** : un choix de modélisation ou une conjecture.
  - **RAPPORTÉ** : un résultat attribué à la littérature, dont la référence est à vérifier.
  - Une dérivation faite ici n'est valable que sous les HYPOTHÈSES qu'elle cite. Elle ne constitue pas un résultat.
- **Chiffres** : ceux qui ne sont pas dérivés explicitement sont marqués « illustratif ».

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut | Pourquoi c'est fragile |
|---|---|---|---|
| P1 | Une « évaluation de perte » coûte le même prix dans toutes les classes H_k, et B est commensurable entre classes. | HYPOTHÈSE | Le coût par évaluation varie avec la taille du modèle. Un budget compté en évaluations favorise donc les grosses classes. |
| P2 | La courbe L_k(b) est monotone, régulière et extrapolable. Son préfixe renseigne sur sa valeur au budget final. | HYPOTHÈSE | Les plateaux, la double descente et les croisements tardifs de courbes sont signalés dans la littérature (RAPPORTÉ, Viering & Loog, à vérifier). |
| P3 | Le coût c est connu et fixe, et la fraction ρ ∈ [0,1] d'ajustement conservée lors d'un changement est mesurable. | HYPOTHÈSE | ρ dépend de l'emboîtement des classes. On peut par exemple réutiliser les poids si H_k ⊂ H_j. |
| P4 | La perte de validation est un estimateur sans biais de la perte de test. | HYPOTHÈSE | C'est vrai pour une évaluation unique. C'est faux après une sélection adaptative répétée. |
| P5 | L'« estimation de variance » mesure le bon bruit. | HYPOTHÈSE | Le bruit d'échantillonnage de la validation, le bruit d'initialisation (graines) et l'autocorrélation le long d'une courbe ne coïncident pas. |
| P6 | La mesure d'écart de distribution sert la décision A/S. | HYPOTHÈSE | Une dérive peut appeler un réajustement *dans* la même classe, et non un changement de classe. |
| P7 | L'ensemble des classes candidates est fini, énuméré et doté d'une loi a priori. | HYPOTHÈSE | En pratique, on construit souvent la liste au fil de l'eau. |
| P8 | L'objectif est fixé. | HYPOTHÈSE à trancher | La question ne dit pas s'il s'agit de la perte finale du modèle livré (regret simple) ou de la perte cumulée pendant l'apprentissage (regret cumulé). Les critères optimaux diffèrent selon ce choix. |
| P9 | Les familles de tâches sont tirées iid d'une méta-distribution (point 4). | HYPOTHÈSE | Si elles ne le sont pas, aucune borne PAC-Bayes ni de stabilité ne s'applique. |
| P10 | On peut revenir à une classe déjà visitée, avec son état « gelé » ou réinitialisé. | HYPOTHÈSE à trancher | Les deux régimes donnent des problèmes différents : le gel est l'analogue de *freeze-thaw*, la réinitialisation celui de *Pandora* avec réouverture payante. |
| P11 | « Vérité connue » signifie des étiquettes sans bruit. | HYPOTHÈSE | Avec des étiquettes bruitées, il existe un plancher irréductible commun à toutes les classes, qui écrase les écarts. |

---

## Matériau pour les points 1 à 5 : plusieurs voies, aucune n'est « la » réponse

### Point 1 — Formalisation

**État commun.**

- Pour chaque classe k : le budget dépensé b_k, la courbe observée {L̂_k(b)} pour b ≤ b_k, et la variance σ̂²_k.
- Le budget restant R = B − Σ_k b_k − (coûts de changement payés).
- La statistique de dérive D_t.

**Modèle de courbe (HYPOTHÈSE P2).** On prend L_k(b) = a_k + β_k·b^(−α_k) + ε. Les paramètres sont l'asymptote a_k, l'amplitude β_k et l'exposant α_k. On les dote d'une loi a posteriori ajustée sur le préfixe.

#### V1 — Arrêt optimal par indices de réservation (type Weitzman, « boîte de Pandore »)

**Variable de décision.** Pour une classe non ouverte j, X_j est la perte atteignable avec le budget restant après changement, soit ρ·b_k + R − c si l'on conserve une partie de l'ajustement. On note F_j sa loi prédictive.

**Coût en unités de perte.** On convertit le coût c en perte par le coût d'opportunité calculé sur la courbe courante :

c^L ≈ L̂_k(b_k + R − c) − L̂_k(b_k + R),

c'est-à-dire la perte finale sacrifiée en retirant c au budget de la classe courante. Cette quantité est calculable à partir de l'extrapolation.

**Indice.** z_j est la solution de E[(z_j − X_j)⁺] = c^L.

**Règle.**
- Ouvrir la classe j de plus petit z_j.
- S'arrêter (A) dès que y* ≤ min_j z_j, où y* est la meilleure perte finale prédite pour les classes déjà ouvertes.

**Hypothèses.** L'optimalité de Weitzman exige trois conditions (RAPPORTÉ, à vérifier) :
- des X_j indépendants ;
- une révélation complète à l'ouverture ;
- des coûts additifs.

Aucune des trois n'est satisfaite ici : l'ouverture ne révèle qu'un préfixe, et le budget couple toutes les boîtes. V1 est donc ici une **heuristique**.

**Ce que V1 ignore.**
- La valeur d'option d'un changement ultérieur.
- Les corrélations entre classes.
- La dérive.

#### V2 — Élimination par enveloppes convexes (bandit « montant »)

**Hypothèses.** L_k est décroissante et convexe en b (HYPOTHÈSE forte).

**Bornes.**
- **Borne optimiste.** Pour une fonction convexe, la tangente est un minorant :

  L_k(b_k + r) ≥ L_k(b_k) + r·L'_k(b_k).

- **Borne pessimiste.** Par monotonie : L_j(b_j + r) ≤ L_j(b_j).

**Règle.** On abandonne la classe k dès que

L̂_k(b_k) + R·L̂'_k(b_k) − (marge de confiance) > L̂_j(b_j) + (marge),

où les marges proviennent de σ̂_k et de l'incertitude sur la pente.

**Intérêt.** Le critère est calculable sans choisir de famille d'extrapolation.

**Limites.**
- Il est faux en présence de plateaux suivis d'une rechute, ou de double descente.
- Il ne traite pas les classes non ouvertes. On ne dispose pour elles d'aucune borne pessimiste, et il faut les combiner avec V1 ou V3.

Des bornes de regret existent pour des bras à récompense croissante et concave (RAPPORTÉ, Heidari, Kearns & Roth 2016, à vérifier).

#### V3 — Valeur de l'information par unité de coût (bayésien, type *freeze-thaw* ou *knowledge gradient*)

**Critère.** Pour chaque action a (poursuivre de Δ dans k, ouvrir j, ou reprendre une classe gelée) :

KG(a) = E[ min_i μ_i^(avant) − min_i μ_i^(après a) ] / coût(a),

où μ_i est la moyenne a posteriori de la perte finale de la classe i.

**Règle.**
- Choisir l'action qui maximise KG.
- Passer en exploitation pure quand max_a KG(a) < seuil.

**Hypothèses.** Le prior est joint sur les courbes, par exemple un processus gaussien avec un noyau de décroissance (RAPPORTÉ, Swersky, Snoek & Adams 2014, à vérifier).

**Ce que V3 ignore.**
- La mauvaise spécification du prior, qui devient catastrophique si P2 est faux.
- Sa myopie, qui sous-explore lorsque c est grand.

#### V4 — Identification du meilleur bras à budget fixe (successive halving ou Hyperband, avec coût de changement)

**Règle.** On alloue des paliers de budget croissants et on conserve à chaque palier la meilleure fraction 1/η des classes. Le coût c s'ajoute à chaque ouverture, et de nouveau à chaque réouverture si l'état n'est pas gelé.

**Garanties.** La version non stochastique exige que chaque courbe converge vers une limite (RAPPORTÉ, Jamieson & Talwalkar 2016 ; Li et al. 2018, à vérifier).

**Ce que V4 ignore.**
- Les croisements tardifs.
- La dérive.
- Le fait que l'objectif peut être cumulé (P8).

#### Rôle de la dérive D_t, commun à toutes les voies

Deux usages exclusifs sont possibles. C'est l'objet de l'expérience E4.

- **(i) Remise en cause des courbes.** On pondère à la baisse le passé des courbes, par exemple avec une fenêtre glissante ou une détection de rupture en ligne bayésienne (RAPPORTÉ, Adams & MacKay 2007, à vérifier).
- **(ii) Déclenchement d'un changement de classe.** L'usage (ii) n'est justifié que si la dérive affecte les classes **différemment** (P6).

**Ce qui départagerait les voies.** Trois facteurs :
- la validité de P2, qui conditionne V1 et V3 ;
- la validité de la convexité, qui conditionne V2 ;
- le rapport entre c et B, qui pénalise V4 quand c est grand.

Les expériences E1 et E2 testent ces facteurs.

### Point 2 — Statistiques observables, coût et biais

| Statistique | Coût d'obtention | Biais qui la rend trompeuse | Correction |
|---|---|---|---|
| L̂_k(b) courante | Une passe de validation par point de courbe | Sélection répétée (sur-ajustement de la validation) | Trois jeux distincts : entraînement, validation de décision, test figé utilisé **une seule fois** ; *holdout* réutilisable (RAPPORTÉ, Dwork et al. 2015, à vérifier) ; « Ladder » (RAPPORTÉ, Blum & Hardt 2015, à vérifier) |
| Pente L̂'_k, asymptote â_k | Ajustement sur le préfixe, presque gratuit | Bruit amplifié par la différenciation ; choix *post hoc* de la famille d'extrapolation | Lissage, intervalles par bootstrap des résidus, famille fixée d'avance |
| σ̂²_k | m graines, soit m fois le budget | Variance de validation seule (bootstrap des exemples) qui sous-estime la variance entre graines | Mesurer les deux composantes ; estimer l'autocorrélation |
| min_k L̂_k (gagnant) | — | Biais du gagnant (voir ci-dessous) | Correction de Tibshirani & Tibshirani 2009 (RAPPORTÉ, à vérifier) ; intervalles simultanés (max-t, Bonferroni sur K) ; PoSI (RAPPORTÉ, Berk et al. 2013, à vérifier) ; séparation d'échantillon |
| D_t | Test à deux échantillons, par exemple MMD (RAPPORTÉ, Gretton et al. 2012, à vérifier) | Fausses alertes par tests multiples dans le temps ; dérive sans effet sur la perte | Seuils de type CUSUM (RAPPORTÉ, Page 1954, à vérifier) ; contrôle par permutation temporelle |

**Biais du gagnant, dérivation.**

- **Hypothèses.** On considère K classes de même perte vraie μ, avec des estimations gaussiennes indépendantes d'écart-type σ.
- **Résultat.** On a E[min_k L̂_k] ≈ μ − σ·√(2 ln K) pour K grand. C'est l'asymptotique classique du maximum de gaussiennes.
- **Conséquence.** Le gain apparent croît avec le nombre de classes **et** avec le nombre de décisions prises sur la même validation.
- **Statut.** Il s'agit d'une dérivation sous HYPOTHÈSE d'indépendance. Les courbes réelles sont corrélées, ce qui réduit le biais.

### Point 3 — Découpage du budget

**Les trois compartiments.**
- B_E : exploration des classes.
- B_X : exploitation à classe figée.
- B_R : réserve pour un changement ultérieur.

**Répartition fixée d'avance.** Le dimensionnement de B_E demande de connaître les écarts Δ_i entre la meilleure classe et les autres. À budget fixe, la probabilité d'erreur d'identification décroît approximativement comme exp(−B_E / (H·log K)), avec H = Σ_i Δ_i⁻² (RAPPORTÉ, Audibert, Bubeck & Munos 2010, à vérifier).

- Si les Δ sont inconnus, la répartition fixe est soit sur-dimensionnée, soit sous-dimensionnée.
- En regret cumulé, « explorer puis s'engager » sans connaissance de l'écart donne un regret d'ordre T^(2/3), contre √T pour une politique adaptative (RAPPORTÉ, à vérifier).

**Répartition adaptative.** Hyperband couvre plusieurs répartitions et paie un facteur logarithmique. Avec des coûts de changement en cadre adverse, le regret minimax est de l'ordre de T^(2/3) (RAPPORTÉ, Dekel, Ding, Koren & Peres 2014, à vérifier). Un coût de changement rend donc structurellement plus cher le fait d'être adaptatif.

**Réserve B_R.** Sa valeur est une valeur d'option. Je la modélise ainsi (HYPOTHÈSE) :

- **Modèle.** Les ruptures arrivent avec un taux λ par unité de budget. Après une rupture, un changement de classe gagne g avec la probabilité q.
- **Valeur de la réserve.** Elle vaut environ λ·(B − b)·q·g − c^L.
- **Condition sur le dernier incrément de réserve.** Il est rentable tant que son espérance de gain dépasse la perte d'exploitation qu'il coûte. Cette perte est mesurée par la pente de la courbe exploitée.

Cette dérivation reste élémentaire et dépend d'un modèle de dérive non validé (E4). Sous stationnarité (λ = 0), elle donne B_R* = 0.

### Point 4 — Généralisation à des familles nouvelles

**Évaluation tenue à l'écart.** On valide en excluant des familles entières (*leave-families-out*), jamais de simples exemples.

**Borne simple, dérivation.**
- **Hypothèses.** On choisit parmi K classes, sur n familles de test iid (P9), avec une perte bornée dans [0,1].
- **Résultat.** Par Hoeffding et une borne d'union, l'écart entre la perte estimée et la perte attendue sur la méta-distribution est au plus √(ln(K/δ)/(2n)), simultanément pour toutes les classes, avec une probabilité au moins 1−δ.
- **Rôle.** C'est la **vérification mécanique à battre** (§ c).

**Bornes à deux niveaux.**
- PAC-Bayes pour l'apprentissage continu ou le méta-apprentissage : Pentina & Lampert 2014 ; Amit & Meir 2018 (RAPPORTÉ, à vérifier).
- Biais inductif : Baxter 2000 (RAPPORTÉ, à vérifier).
- Stabilité algorithmique pour le méta-apprentissage : Maurer 2005 (RAPPORTÉ, à vérifier).

Ces bornes ne valent que sous P9 et n'ont d'intérêt que si elles sont plus serrées que la borne de Hoeffding sur familles tenues à l'écart.

**Distinguer généralisation et mémorisation.** Trois tests :

1. **Comparer trois écarts.** Le regret sur des instances nouvelles de familles vues, le regret sur des familles non vues proches, et le regret sur des familles non vues éloignées. Le découpage est stratifié par distance entre familles, ce qui évite les quasi-doublons.
2. **Suivre la signature de la mémorisation.** L'écart entre familles vues et non vues croît avec le nombre d'itérations de méta-entraînement, alors que la performance sur familles non vues stagne.
3. **Contrôle par permutation.** On réassigne aléatoirement les tâches aux familles, ce qui détruit la structure de famille. Tout avantage persistant relève d'un artefact.

### Point 5 — Références (attributions de mémoire, métadonnées à vérifier)

- Weitzman, M. (1979). *Optimal Search for the Best Alternative*. Econometrica. — à vérifier
- Gittins, J. C. (1979). *Bandit Processes and Dynamic Allocation Indices*. JRSS B. — à vérifier
- Karnin, Z., Koren, T., Somekh, O. (2013). *Almost Optimal Exploration in Multi-Armed Bandits*. ICML. — à vérifier
- Jamieson, K., Talwalkar, A. (2016). *Non-stochastic Best Arm Identification and Hyperparameter Optimization*. AISTATS. — à vérifier
- Li, L., Jamieson, K., DeSalvo, G., Rostamizadeh, A., Talwalkar, A. (2018). *Hyperband: A Novel Bandit-Based Approach to Hyperparameter Optimization*. JMLR. — à vérifier
- Audibert, J.-Y., Bubeck, S., Munos, R. (2010). *Best Arm Identification in Multi-Armed Bandits*. COLT. — à vérifier
- Swersky, K., Snoek, J., Adams, R. P. (2014). *Freeze-Thaw Bayesian Optimization*. — à vérifier
- Domhan, T., Springenberg, J. T., Hutter, F. (2015). *Speeding up Automatic Hyperparameter Optimization of Deep Neural Networks by Extrapolation of Learning Curves*. IJCAI. — à vérifier
- Falkner, S., Klein, A., Hutter, F. (2018). *BOHB: Robust and Efficient Hyperparameter Optimization at Scale*. ICML. — à vérifier
- Viering, T., Loog, M. (2022). *The Shape of Learning Curves: A Review*. IEEE TPAMI. — à vérifier
- Heidari, H., Kearns, M., Roth, A. (2016). *Tight Policy Regret Bounds for Improving and Decaying Bandits*. IJCAI. — à vérifier
- Dekel, O., Ding, J., Koren, T., Peres, Y. (2014). *Bandits with Switching Costs: T^{2/3} Regret*. STOC. — à vérifier
- Cawley, G., Talbot, N. (2010). *On Over-fitting in Model Selection and Subsequent Selection Bias in Performance Evaluation*. JMLR. — à vérifier
- Varma, S., Simon, R. (2006). *Bias in Error Estimation When Using Cross-Validation for Model Selection*. BMC Bioinformatics. — à vérifier
- Tibshirani, R. J., Tibshirani, R. (2009). *A Bias Correction for the Minimum Error Rate in Cross-Validation*. Annals of Applied Statistics. — à vérifier
- Dwork, C., Feldman, V., Hardt, M., Pitassi, T., Reingold, O., Roth, A. (2015). *The Reusable Holdout: Preserving Validity in Adaptive Data Analysis*. Science. — à vérifier
- Blum, A., Hardt, M. (2015). *The Ladder: A Reliable Leaderboard for Machine Learning Competitions*. ICML. — à vérifier
- Berk, R., Brown, L., Buja, A., Zhang, K., Zhao, L. (2013). *Valid Post-Selection Inference*. Annals of Statistics. — à vérifier
- Baxter, J. (2000). *A Model of Inductive Bias Learning*. JAIR. — à vérifier
- Maurer, A. (2005). *Algorithmic Stability and Meta-Learning*. JMLR. — à vérifier
- Pentina, A., Lampert, C. (2014). *A PAC-Bayesian Bound for Lifelong Learning*. ICML. — à vérifier
- Amit, R., Meir, R. (2018). *Meta-Learning by Adjusting Priors Based on Extended PAC-Bayes Theory*. ICML. — à vérifier
- Gretton, A., Borgwardt, K., Rasch, M., Schölkopf, B., Smola, A. (2012). *A Kernel Two-Sample Test*. JMLR. — à vérifier
- Adams, R. P., MacKay, D. (2007). *Bayesian Online Changepoint Detection*. — à vérifier
- Page, E. S. (1954). *Continuous Inspection Schemes*. Biometrika. — à vérifier
- Rabanser, S., Günnemann, S., Lipton, Z. (2019). *Failing Loudly: An Empirical Study of Methods for Detecting Dataset Shift*. NeurIPS. — à vérifier

---

## (b) Expériences décisives (inférence forte, B4)

**Convention commune.**
- Seuils pré-enregistrés.
- Intervalles par bootstrap **sur les tâches** (unité statistique : la tâche ou la famille, jamais l'exemple).
- Marge d'équivalence δ.
- H_B est formulée comme une équivalence (test TOST) et H_A comme une supériorité au-delà de δ.
- Si l'intervalle chevauche ±δ, le résultat est « non tranché ». On étend alors l'échantillon selon une règle fixée d'avance, sans changer de métrique.
- Tous les seuils numériques ci-dessous sont **illustratifs**, sauf mention d'une dérivation.

### E1 — Les courbes extrapolées ordonnent-elles les classes mieux que la valeur courante ?

- **H_A** : à une fraction f du budget, le classement par perte finale extrapolée (V1 ou V3) prédit mieux le classement final que le classement par meilleure valeur observée.
- **H_B** : l'extrapolation n'apporte rien (|Δτ| < δ) ou dégrade le classement.
- **Métrique** : τ de Kendall entre le classement prédit à f et le classement final. On mesure aussi le regret de la classe choisie, pour f ∈ {0,1 ; 0,25 ; 0,5}.
- **Seuil** : Δτ > δ = 0,05 (illustratif), avec un intervalle à 95 % excluant δ.
- **Contrôle négatif** :
  - permutation des courbes entre classes au sein d'une tâche, qui doit donner τ ≈ 0 ;
  - courbes synthétiques à croisement tardif construit, où toute méthode fondée sur le préfixe doit échouer et où l'on vérifie qu'elle échoue.
- **Falsification** :
  - un intervalle au-dessus de δ falsifie H_B ;
  - un intervalle dans ±δ ou en dessous falsifie H_A, ce qui disqualifie V1 et V3 au profit de V2 ou V4.

### E2 — Un critère tenant compte de c bat-il une allocation de type Hyperband ?

- **H_A** : V1 ou V3, avec c intégré, obtient à budget B égal une perte de **test** finale inférieure à V4 (où c est payé à chaque ouverture).
- **H_B** : l'écart est inférieur à δ.
- **Plan** : on fait varier c/B ∈ {0 ; 0,01 ; 0,05 ; 0,2} (illustratif). Prédiction : l'avantage de H_A croît avec c/B et s'annule en c = 0.
- **Métrique** : regret normalisé, défini par (perte de test finale − perte de l'oracle « meilleure classe au budget B ») / écart-type entre tâches.
- **Contrôle négatif** :
  - une politique de changement aléatoire, avec le même nombre de changements que H_A ;
  - un contrôle de cohérence en c = 0, où les deux politiques doivent être équivalentes. Un écart en c = 0 trahit une fuite ou un bug.
- **Falsification** :
  - un avantage hors de ±δ qui croît avec c/B falsifie H_B ;
  - une équivalence à tous les niveaux de c/B, ou un avantage qui ne croît pas avec c/B, falsifie H_A. Dans ce cas, intégrer c dans le critère n'apporte rien et l'avantage éventuel vient d'ailleurs.

### E3 — Le biais de sélection est-il mesurable, et les corrections tiennent-elles leur couverture ?

- **H_A** : sans correction, l'écart (test − validation) de la classe retenue croît avec le nombre de décisions prises sur la même validation. Avec un *holdout* réutilisable ou un test figé, cet écart est compatible avec 0.
- **H_B** : l'écart non corrigé est inférieur à σ_val à tout nombre de décisions, auquel cas la correction est inutile.
- **Configuration nulle (contrôle négatif central)** : K classes de perte vraie identique, obtenues avec le même modèle et des graines différentes. Tout gain apparent y est un pur biais. La prédiction quantitative est l'ordre de grandeur σ·√(2 ln K) dérivé au point 2.
- **Couverture des intervalles corrigés (PoSI, max-t, Tibshirani)** :
  - sur N = 1000 réplications, la couverture empirique d'un intervalle nominal à 90 % a un écart-type √(0,9·0,1/1000) ≈ 0,0095 ;
  - on accepte une couverture dans [0,87 ; 0,93], soit environ ±3 écarts-types. Ce seuil est **dérivé**.
- **Falsification** :
  - une croissance de l'écart non corrigé avec le nombre de décisions falsifie H_B ;
  - une absence de croissance au-delà de σ_val en configuration nulle falsifie H_A ;
  - une couverture hors de [0,87 ; 0,93] falsifie la correction testée.

### E4 — La dérive appelle-t-elle un changement de classe ou un simple réajustement ?

- **H_A** : la statistique D_t prédit le gain du **changement de classe** par rapport à la réinitialisation dans la même classe.
- **H_B** : D_t prédit le gain du réajustement, mais pas le gain spécifique du changement de classe.
- **Plan** : injection contrôlée de deux types de dérive dans des flux synthétiques et semi-réels.
  - **Type I** : représentable par la classe courante, par exemple une translation des covariables dans son domaine de capacité.
  - **Type II** : hors capacité, par exemple l'apparition d'une interaction non linéaire pour une classe linéaire.
- **Branches comparées** : poursuivre, réinitialiser dans la même classe, changer de classe. Les trois partent du **même état**, au même instant.
- **Métrique** : corrélation de rang entre D_t et G = perte(réinitialisation) − perte(changement), mesurée après le même budget R.
- **Contrôle négatif** :
  - un flux sans dérive, pour mesurer le taux de fausses alertes ;
  - une dérive placebo obtenue par permutation de l'ordre temporel.
- **Falsification** :
  - si G est significativement positif en type II, nul en type I, et prédit par D_t, H_B est falsifiée ;
  - si G est nul dans les deux types, ou si D_t ne le prédit pas, H_A est falsifiée. D_t ne servira alors qu'à réajuster (usage (i) du point 1).

### E5 — La classe choisie par méta-apprentissage généralise-t-elle à des familles nouvelles ?

- **H_A** : la règle de choix apprise sur les familles d'entraînement réduit le regret sur des familles **éloignées** non vues, par rapport à la meilleure classe par défaut fixe.
- **H_B** : l'avantage observé sur les familles vues disparaît sur les familles éloignées (mémorisation).
- **Métrique** : regret moyen sur trois strates (instances nouvelles de familles vues, familles non vues proches, familles non vues éloignées).
- **Seuil** : avantage sur la strate éloignée supérieur à la borne de Hoeffding √(ln(K/δ)/(2n)), qui est **dérivée**.
- **Contrôle négatif** : réassignation aléatoire des tâches aux familles, et règle de choix tirée au hasard.
- **Falsification** :
  - un avantage sur la strate éloignée au-delà de la borne falsifie H_B ;
  - un avantage limité aux familles vues, ou un écart vu/non vu croissant avec l'entraînement, falsifie H_A.

### E6 — Réserve fixe ou adaptative, selon la stationnarité

- **H_A** : une réserve adaptative (V1 ou V3 avec mise à jour de λ̂) bat le découpage fixe **seulement** sous non-stationnarité. Prédiction croisée : un avantage nul sous stationnarité.
- **H_B** : le découpage fixe est équivalent dans les deux régimes, ou bien l'adaptatif gagne aussi sous stationnarité.
- **Plan factoriel** : réserve (fixe / adaptative) × régime (λ = 0 / λ > 0).
- **Métrique** : regret normalisé, comme en E2.
- **Interprétation** : seule l'interaction prédite par H_A survit.
  - Un gain de l'adaptatif sous λ = 0 indique que le découpage fixe était mal dimensionné. Ce n'est pas un effet de la réserve, et H_A est falsifiée en tant qu'explication.
  - Une absence de gain sous λ > 0 falsifie aussi H_A.

---

## (c) Mesure minimale pour chaque instrument nommé dans la question

**Principe des cas honnêtes appariés.** Ils sont obtenus par **bifurcation** : depuis un même état sauvegardé, on exécute les deux branches (A et S, ou flux avec et sans dérive). On obtient ainsi une étiquette contrefactuelle exacte de l'action qui était meilleure.

| Instrument | « Détection » mesurée | Cas honnêtes appariés | Vérifications mécaniques à battre |
|---|---|---|---|
| **Courbe L_k(b) et extrapolateur** | Taux de détection (TPR) : signaler correctement qu'une classe sera dépassée. Taux de fausses alertes (FPR) : la signaler alors qu'elle gagne au final. | Paires de classes d'une même tâche, menées jusqu'au bout. On stratifie entre paires qui se croisent et paires qui ne se croisent pas. | Dernière valeur ; meilleure valeur jusqu'ici ; extrapolation linéaire de la dernière fenêtre ; règle de patience (aucun progrès depuis p pas) |
| **Estimation de variance** | Couverture des intervalles qu'elle induit, avec le seuil dérivé en E3 | Mêmes points de courbe, réévalués sur m graines indépendantes | Bootstrap des exemples de validation seul ; écart-type entre graines brut |
| **Budget consommé** | Exactitude comptable : Σ des évaluations + coûts de changement payés = B. Écart entre le compte en évaluations et le compte en FLOPs ou en temps (P1). | Journal des exécutions, rejoué | Somme indépendante des journaux. Si le classement des politiques change entre le compte en évaluations et le compte en FLOPs, P1 est falsifié. |
| **Mesure d'écart de distribution (D_t)** | TPR à FPR fixé (par exemple 5 %, illustratif) ; délai de détection | Même flux avec et sans dérive injectée au même instant ; placebo par permutation temporelle | Tests KS univariés par variable avec correction de Bonferroni ; CUSUM sur la perte de validation elle-même ; classifieur de domaine (passé contre récent) |
| **Données tenues à l'écart / holdout réutilisable** | Écart test − validation après N requêtes adaptatives | Configuration nulle de E3 | *Holdout* frais à chaque requête (oracle coûteux) ; réutilisation naïve |
| **Corrections de sélection et intervalles post-sélection** | Couverture dans [0,87 ; 0,93] pour un nominal de 90 % (dérivé), en configuration nulle et en configuration étalée ; largeur moyenne | Configurations nulles et étalées, mêmes données | Bonferroni sur K ; intervalle naïf ; séparation d'échantillon 50/50. Une correction plus large que la séparation d'échantillon à couverture égale ne sert à rien. |
| **Bornes PAC-Bayes et de stabilité (multi-tâches)** | Validité : la borne majore la perte observée sur familles tenues à l'écart dans au moins une fraction 1−δ des réplications. Utilité : la borne est non triviale, c'est-à-dire inférieure à la perte du prédicteur constant. | Découpages répétés familles d'entraînement / familles de test | **Borne de Hoeffding sur familles tenues à l'écart** (point 4). Si la borne théorique est plus lâche, elle n'apporte aucune information au-delà du holdout. |
| **Critère A/S lui-même (V1 à V4)** | TPR : signaler S quand S était meilleur. FPR : signaler S quand A était meilleur. | Bifurcations depuis le même état, à plusieurs instants et plusieurs valeurs de c | Toujours poursuivre ; changer au plateau (patience) ; calendrier fixe de changements |

---

## (d) Ancrage matériel

**Statut.** Rien ne vient des faits : tous les coûts sont **illustratifs**. Les existences et contenus des jeux de données cités sont RAPPORTÉS, avec des références à vérifier.

### Niveau 0 — courbes tabulées, coût de calcul quasi nul

- **Bancs d'essai à courbes d'apprentissage pré-calculées** : LCBench (Zimmer, Lindauer & Hutter 2021, à vérifier), NAS-Bench-201 (Dong & Yang 2020, à vérifier), YAHPO Gym et HPOBench (références à vérifier).
- **Expériences couvertes** : E1, E2 et E6 en simulant le coût c par comptabilité.
- **Limite** : ces bancs fixent la notion de « classe » à leurs propres choix (architectures, hyperparamètres). Ils ne testent pas P3, car on n'y observe pas de conservation partielle réelle.
- **Calcul** : CPU, quelques heures (illustratif).

### Niveau 1 — entraînement réel, petites classes ouvertes

- **Classes candidates** :
  - régression linéaire ou logistique ;
  - forêts et boosting de gradient (XGBoost et LightGBM, bibliothèques ouvertes) ;
  - perceptrons multicouches ;
  - petits transformeurs tabulaires ou textuels.
- **Tâches** : suites ouvertes OpenML (référence à vérifier), regroupées en familles par domaine pour E5.
- **Volume** : environ 50 tâches × 6 classes × 10 graines, menées jusqu'au bout, soit environ 3000 exécutions (illustratif), auxquelles s'ajoutent les bifurcations contrefactuelles (doublement environ, illustratif).
- **Coût** :
  - de l'ordre de 100 à 500 heures-GPU, dont une grande partie peut tourner sur CPU (illustratif) ;
  - au tarif indicatif de 1 à 3 € par heure-GPU (illustratif), cela représente quelques centaines à environ 1500 € (illustratif).

### Niveau 2 — dérive (E4)

- **Flux** : flux synthétiques à dérives injectées de type I et de type II, et flux semi-réels (réordonnancement temporel de jeux ouverts).
- **Calcul** : CPU, coût faible (illustratif).

### Niveau 3 — courbes à grande échelle (facultatif)

- **Ressource** : suites de modèles ouverts à points de contrôle publics. Par exemple, Pythia (Biderman et al. 2023, à vérifier) fournit des courbes en fonction de la taille et du budget, sans entraînement supplémentaire.
- **Expérience couverte** : E1 sur des courbes longues, où les plateaux et ruptures de pente sont plus probables.
- **Coût** : surtout de l'évaluation (illustratif).

### Garde-fous transverses

- Seuils et métriques pré-enregistrés.
- Test figé consulté une seule fois.
- Unité statistique : la tâche ou la famille.
- Code de comptabilité du budget audité indépendamment de celui des politiques testées.

**Ce que ce dessin peut réfuter, et lui seulement.**
1. L'utilité de l'extrapolation (E1).
2. L'utilité d'intégrer c (E2).
3. L'ampleur du biais de sélection et la validité des corrections (E3).
4. Le rôle décisionnel de la dérive (E4).
5. La généralisation inter-familles par rapport à la mémorisation (E5).
6. L'intérêt d'une réserve adaptative (E6).

Aucun de ces tests ne désigne un critère unique comme « la » solution. Ils éliminent des voies.

FIN-DE-CELLULE