# Proposition A — Tour III.1 : allocation d'un budget entre choix de classe et ajustement de paramètres

**État des pièces.** Le bloc FAITS est vide par décision de l'arbitre (conv-audit, n° 28 § 1) ; tout ce qui suit est donc soit dérivation explicite, soit HYPOTHÈSE, soit RAPPORTÉ (littérature, à vérifier). Aucun statut VÉRIFIÉ n'est attribuable à un fait empirique dans cette cellule.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé implicite | Statut | Pourquoi ça compte |
|---|---|---|---|
| a1 | La courbe L_k(b) a une forme extrapolable (monotone décroissante, convexe au-delà d'un transitoire). | HYPOTHÈSE | Les courbes réelles montrent plateaux, remontées (sur-ajustement), et parfois non-monotonie en fonction de la taille de la classe (RAPPORTÉ : revue de Viering & Loog, « The shape of learning curves: a review », 2022, à vérifier). Si a1 est faux, tout critère par extrapolation est un détecteur de plateau, pas un prédicteur. |
| a2 | Le coût de changement c est connu et constant. | HYPOTHÈSE | Avec reprise partielle (transfert de θ), c dépend du couple (k, j) et n'est connu qu'après coup. |
| a3 | Les classes H_j sont indépendantes a priori (bandit à bras indépendants). | HYPOTHÈSE | Si les classes sont emboîtées (H_1 ⊂ H_2 ⊂ …) ou paramétrées par une taille, l'observation de L_k informe sur L_j : c'est un bandit structuré, et la formalisation « indépendante » jette de l'information. |
| a4 | La validation est un estimateur non biaisé de la perte cible à chaque consultation. | HYPOTHÈSE (fausse dès la deuxième consultation adaptative) | Chaque lecture de L_k(b) utilisée pour décider rend la suivante optimiste ; voir § 2. |
| a5 | L'« écart de distribution » entre données récentes et passées est une statistique informative sur la perte future, et non sur la perte passée. | HYPOTHÈSE | Un écart marginal (sur X) n'implique pas un écart sur P(Y\|X) ; un critère qui change de classe sur écart marginal réagit peut-être à du bruit. |
| a6 | L'objectif est la perte finale à budget épuisé (horizon fixe), pas la perte cumulée en cours de route. | HYPOTHÈSE | Les deux objectifs donnent des politiques différentes (identification de meilleur bras à budget fixe vs minimisation du regret cumulé) ; la question ne tranche pas. |
| a7 | Le budget B est une unité homogène (une évaluation de perte = un coût constant), quelle que soit la classe. | HYPOTHÈSE | Si une évaluation dans H_j coûte dix fois plus qu'en H_k, la comparaison « à budget égal » doit être faite en coût réel. |
| a8 | Point 4 : il existe une distribution sur les « familles de tâches » et les familles vues en sont un tirage i.i.d. | HYPOTHÈSE | C'est l'hypothèse d'environnement de tâches (RAPPORTÉ : Baxter, « A model of inductive bias learning », 2000, à vérifier). Sans elle, aucune borne de généralisation inter-familles n'a de sens ; on ne peut que mesurer sur des familles tenues à l'écart et décrire ce qu'elles ont de commun avec les familles vues. |

---

## 1. Formalisation (plusieurs voies, aucune n'étant « la » réponse)

**Objets.** État à l'instant t : s_t = (k_t, b_t, L̂_k(·) sur [0, b_t], σ̂²_k, B_t = budget restant, d_t = écart de distribution). Actions : A (dépenser δ dans H_k) ; S(j) (payer c, poser b ← ρ·b_t avec ρ ∈ [0,1] la fraction conservée, passer à j). Objectif (sous a6) : minimiser E[L_final] à budget épuisé ; variante : regret cumulé ∑_t L_{k_t}(b_t).

**Voie F1 — arrêt optimal avec indice (type Gittins) à coût de changement.** Pour chaque classe, on définit un indice ν_k(b, B_t) = gain attendu par unité de budget si l'on continue, calculé sous une loi a posteriori sur la courbe. Règle : continuer tant que ν_k ≥ max_j [ν_j(ρ b_t, B_t − c) − pénalité de c]. L'indice de Gittins exact n'est optimal que sans coût de changement et pour la récompense actualisée (RAPPORTÉ : Gittins, « Bandit processes and dynamic allocation indices », 1979 ; Banks & Sundaram, « Switching costs and the Gittins index », 1994 ; Agrawal, Hegde & Teneketzis, « Asymptotically efficient adaptive allocation rules for the multiarmed bandit problem with switching cost », 1988 — tous à vérifier). Avec coût c, la politique d'indice est une heuristique ; ce qu'elle ignore : la dépendance entre classes (a3), la non-stationnarité (d_t n'entre pas), l'horizon fini.

**Voie F2 — extrapolation paramétrique des courbes + décision myope à un coup.** On ajuste une forme L_k(b) ≈ a_k + β_k b^(−γ_k) (ou un mélange de formes), on prédit L̂_k(B_t) et, pour chaque j, L̂_j(B_t − c) sous un a priori (par ex. hiérarchique sur (a, β, γ) estimé sur les classes déjà vues). Règle : changer si L̂_j(B_t − c) + z·σ̂_j < L̂_k(B_t) − z·σ̂_k, avec z fixé d'avance. RAPPORTÉ (à vérifier) : Domhan, Springenberg & Hutter, « Speeding up automatic hyperparameter optimization of deep neural networks by extrapolation of learning curves », 2015 ; Swersky, Snoek & Adams, « Freeze-thaw Bayesian optimization », 2014. Hypothèses : a1, a2 ; une loi a priori sur les classes non encore visitées (sans quoi L̂_j est indéfinie pour j jamais essayé). Ce que F2 ignore : la valeur d'information (elle est myope : elle ne compte pas qu'un court essai de j réduirait σ̂_j), les remontées de courbe, le réemploi de la validation.

**Voie F3 — identification de meilleur bras à budget fixe, avec élimination (halving successif / Hyperband).** On alloue B en r rondes ; à chaque ronde on garde la moitié des classes selon L̂ courant. Aucune extrapolation : seul l'ordre courant compte. RAPPORTÉ (à vérifier) : Karnin, Koren & Somekh, « Almost optimal exploration in multi-armed bandits », 2013 ; Jamieson & Talwalkar, « Non-stochastic best arm identification and hyperparameter optimization », 2016 ; Li, Jamieson, DeSalvo, Rostamizadeh & Talwalkar, « Hyperband: a novel bandit-based approach to hyperparameter optimization », 2018 ; Audibert, Bubeck & Munos, « Best arm identification in multi-armed bandits », 2010. Hypothèse structurelle : l'ordre des classes à petit budget prédit l'ordre à grand budget (pas de croisement tardif). Ce que F3 ignore : les croisements de courbes, le coût c (le halving « change » à coût nul puisqu'il n'arrête que des bras déjà lancés), l'écart de distribution.

**Voie F4 — bandit structuré sur un espace de classes paramétré.** Si H_j est indexée par une taille s_j (nombre de paramètres, profondeur), on modélise L(s, b) comme une surface régulière (par exemple loi de puissance en s et b, RAPPORTÉ, à vérifier : Hestness et al., « Deep learning scaling is predictable, empirically », 2017 ; Kaplan et al., « Scaling laws for neural language models », 2020 ; Hoffmann et al., « Training compute-optimal large language models », 2022). La décision devient une optimisation bayésienne sur s sous contrainte de budget restant. Ce qu'elle ignore : les classes non comparables sur un axe scalaire ; elle importe aussi une hypothèse de régularité forte sur la surface.

**Voie F5 — bandit non stationnaire pour intégrer d_t.** Si d_t dépasse un seuil, on considère que les observations antérieures sont périmées : on applique une fenêtre glissante ou un facteur d'oubli à L̂_k (RAPPORTÉ, à vérifier : Garivier & Moulines, « On upper-confidence bound policies for switching bandit problems », 2011 ; Besbes, Gur & Zeevi, « Stochastic multi-armed-bandit problem with non-stationary rewards », 2014). Ce qu'elle ignore : le fait que le changement de distribution peut favoriser une autre classe sans que L̂_k bouge immédiatement.

**Ce qui départagerait F1–F5 :** la fréquence des croisements de courbes (si rare, F3 suffit) ; la qualité de l'a priori sur les classes non visitées (F2, F4 en dépendent entièrement) ; la présence réelle de non-stationnarité (F5 n'a de valeur que si a5 tient). Ce sont les expériences E1, E2, E4 ci-dessous.

---

## 2. Statistiques observables, coût, biais, corrections

**Statistiques.** (i) L̂_k(b) sur n_val exemples : coût n_val évaluations par lecture. (ii) Variance : deux composantes, bruit d'échantillonnage (≈ σ²_val/n_val, estimable sur une seule lecture) et variance entre réplications (graines, ordre des données), estimable seulement par réplication — coût multiplié par le nombre de graines. (iii) Pente et courbure locales de L̂_k : estimées par régression sur une fenêtre de lectures ; leur variance est grande à petite fenêtre. (iv) d_t : test à deux échantillons (MMD, distance d'énergie, ou classifieur discriminant ancien/récent) ou plus simplement perte de l'hypothèse courante sur les données récentes vs anciennes.

**Biais qui les rendent trompeuses.**
- *Réemploi adaptatif de la validation.* Après m décisions prises en consultant le même ensemble, l'optimisme attendu sur le minimum de m estimateurs indépendants est d'ordre σ·√(2 ln m / n_val) (dérivation par borne d'union + Hoeffding, vérifiable à la main ; les lectures successives d'une même courbe ne sont pas indépendantes, donc la borne est conservatrice mais la direction du biais est sûre). HYPOTHÈSE : dans les régimes pratiques, ce biais est du même ordre que les écarts entre classes voisines, donc décisif.
- *Biais du gagnant.* La classe sélectionnée parce que L̂ est minimal a une perte vraie supérieure à L̂ ; le biais croît avec le nombre de classes comparées et décroît avec n_val.
- *Bruit des courbes.* Un plateau apparent sur une fenêtre courte est indiscernable d'une décélération temporaire ; un critère de pente déclenche des changements prématurés.
- *Non-stationnarité.* Une remontée de L̂_k peut venir d'un sur-ajustement (changer de classe est pertinent) ou d'un décalage de distribution (changer de classe peut ne rien résoudre) ; sans d_t, les deux sont confondus.

**Corrections.**
- *Deux ensembles tenus à l'écart* : un ensemble de *sélection* (consulté à chaque décision) et un ensemble de *confirmation* consulté une seule fois à la fin, ou un nombre de fois borné d'avance avec correction d'union.
- *Holdout réutilisable* : RAPPORTÉ (à vérifier) : Dwork, Feldman, Hardt, Pitassi, Reingold & Roth, « The reusable holdout: preserving validity in adaptive data analysis », 2015 — mécanisme qui ne révèle la valeur du holdout que lorsqu'elle s'écarte du train au-delà d'un seuil bruité.
- *Inférence après sélection* : intervalles conditionnels à l'événement de sélection (RAPPORTÉ, à vérifier : Berk, Brown, Buja, Zhang & Zhao, « Valid post-selection inference », 2013 ; Lee, Sun, Sun & Taylor, « Exact post-selection inference, with application to the lasso », 2016). Pour une sélection de type « minimum parmi K », la correction conditionnelle est tractable sous hypothèse gaussienne ; HYPOTHÈSE : l'hypothèse gaussienne sur L̂ est raisonnable pour n_val grand par théorème central limite, à vérifier par bootstrap.
- *Réplication par graines* : la seule façon d'obtenir la composante inter-réplications de la variance ; coût linéaire en nombre de graines.

Coût total des corrections : la confirmation immobilise une fraction des données ; les graines multiplient B par leur nombre. Ces coûts doivent entrer dans le budget B lui-même, sinon la comparaison entre critères est faussée.

---

## 3. Découpage du budget

Notons e·B l'exploration (essais courts de toutes les classes), x·B l'exploitation (classe figée), r·B la réserve pour changement tardif, e + x + r = 1.

**Répartition fixée d'avance.** Perte attendue, décomposée (dérivation sous hypothèses simplificatrices, forme HYPOTHÈSE) :
- Perte d'identification : si l'exploration donne à chaque classe eB/K évaluations et que l'écart de perte entre la meilleure et la seconde est Δ avec bruit σ, la probabilité de rater la meilleure décroît en exp(−κ·eBΔ²/(Kσ²)) pour une constante κ (forme empruntée aux bornes d'identification à budget fixe, RAPPORTÉ à vérifier chez Audibert, Bubeck & Munos 2010). *Illustratif* : avec K = 8, σ/Δ = 3, obtenir une probabilité d'erreur ≈ 5 % demande eB de l'ordre de quelques centaines d'évaluations équivalentes.
- Perte d'exploitation : les eB + rB évaluations non dépensées dans la classe finale coûtent ≈ |L'_k(xB)|·(e + r)B si la courbe est encore en pente ; nul si elle a plateau.
- Perte de réserve : rB immobilisée ne sert que si un changement tardif est nécessaire (non-stationnarité ou croisement de courbes) ; sinon elle est perdue au taux de la pente. Borne : r·B ≥ c + budget minimal pour atteindre dans une nouvelle classe une perte compétitive, sinon la réserve est inutilisable par construction.

**Répartition adaptative.** Halving successif : e n'est pas fixé, l'exploration s'arrête quand il reste une classe ; borne connue (RAPPORTÉ, à vérifier : Karnin et al. 2013) en budget nécessaire ∝ ∑_j Δ_j^(−2) log log K, à constante près. Réserve adaptative : déclenchée par d_t ou par remontée confirmée de L̂_k, avec un nombre maximal de changements fixé d'avance (sinon le réemploi de la validation explose, § 2).

**Regret de chaque choix (HYPOTHÈSE sur les ordres de grandeur).** Fixé : simple, robuste au réemploi de la validation (nombre de consultations connu), mais paie e et r même quand ils sont inutiles. Adaptatif : gagne quand les classes sont très inégales (élimination rapide) ou quand il y a non-stationnarité réelle ; perd quand les courbes se croisent tard (élimination prématurée) et quand le bruit déclenche des changements. Ce qui départage : E2 et E6.

---

## 4. Généralisation à des familles de tâches nouvelles

**Cadre.** Sous a8, la classe k est choisie sur n familles tirées d'un environnement de tâches ; on veut borner E_nouvelle famille[L_k]. Trois voies :

- **V1 — Évaluation sur familles tenues à l'écart (leave-families-out).** Estimateur direct ; variance en 1/n_familles (pas en 1/n_exemples : le nombre de familles est le facteur limitant). C'est la mesure de référence contre laquelle les bornes doivent être comparées.
- **V2 — Bornes PAC-Bayes multi-tâches.** Forme type (RAPPORTÉ, à vérifier) : Pentina & Lampert, « A PAC-Bayesian bound for lifelong learning », 2014 ; Amit & Meir, « Meta-learning by adjusting priors based on extended PAC-Bayes theory », 2018 ; fondement : McAllester, « Some PAC-Bayesian theorems », 1999. Structure : risque sur une nouvelle tâche ≤ risque empirique moyen sur les n tâches + terme en √(KL(hyper-postérieur ‖ hyper-prior)/n) + terme intra-tâche en √(KL/m). Hypothèses : i.i.d. des tâches (a8), prior fixé avant de voir les données. HYPOTHÈSE : ces bornes sont souvent lâches ou vides à n petit ; leur valeur est dans la *forme* de la dépendance en n et m, à confronter à V1.
- **V3 — Stabilité / représentation multi-tâches.** RAPPORTÉ (à vérifier) : Maurer, « Algorithmic stability and meta-learning », 2005 ; Maurer, Pontil & Romera-Paredes, « The benefit of multitask representation learning », 2016 ; Baxter 2000 (dimension de l'environnement de tâches).

**Distinguer généralisation et mémorisation des familles vues.** Protocole : (i) définir une distance entre familles (par exemple divergence entre leurs distributions d'entrée, ou écart de performance croisée) ; (ii) tracer la performance sur familles tenues à l'écart en fonction de leur distance à la famille vue la plus proche ; (iii) contrôle négatif : permutation des étiquettes de familles — si la « généralisation » survit à la permutation, l'instrument ne mesure rien. Prédictions exclusives : mémorisation ⇒ performance décroissant nettement avec la distance et chutant au-delà d'un rayon ; généralisation ⇒ performance approximativement plate sur le domaine couvert. Voir E5.

---

## (b) Expériences décisives (duels H_A / H_B)

Conventions : tous les seuils numériques sont *illustratifs* et fixés d'avance ; les lectures de décision se font sur l'ensemble de sélection, le verdict sur l'ensemble de confirmation lu une fois ; chaque expérience est répliquée sur ≥ 20 (illustratif) couples (tâche, graine). Les courbes complètes de toutes les classes sont enregistrées une fois (coût majeur, § d) ; les politiques sont ensuite simulées hors ligne sur ces courbes, ce qui rend l'oracle calculable.

**E1 — L'extrapolation (F2) bat-elle l'élimination sans modèle (F3) ?**
- H_A : à budget B égal, F2 atteint une perte de confirmation inférieure à F3 d'au moins δ₁ (illustratif : 1 % relatif) sur la médiane des tâches.
- H_B : l'écart est < δ₁ ou de signe contraire ; l'extrapolation n'apporte rien au-delà de l'ordre courant.
- Métrique : L_confirmation(F2) − L_confirmation(F3), intervalle par bootstrap sur les réplications.
- Contrôle négatif : mêmes politiques sur des courbes synthétiques sans croisement (courbes parallèles) — F2 ne doit pas battre F3 ; si elle le fait, l'écart vient d'un artefact (par ex. nombre de consultations différent).
- Falsification : si l'intervalle exclut δ₁ par en bas, H_A est falsifiée (l'extrapolation ne paie pas son coût de modélisation) ; si l'intervalle exclut 0 par en haut et contient ≥ δ₁, H_B est falsifiée.

**E2 — Changer de classe en cours de route paie-t-il, étant donné c ?**
- H_A : il existe un régime c/B < τ dans lequel la politique oracle (calculée sur les courbes complètes) change de classe au moins une fois sur ≥ 30 % des tâches (illustratif) et gagne > δ₂ sur « ne jamais changer après exploration ».
- H_B : pour tout c > 0 testé, l'oracle ne change pas ou le gain est < δ₂ ; la question de l'allocation se réduit à « bien explorer, puis figer ».
- Métrique : fraction de tâches où l'oracle change ; gain de l'oracle vs figé. Balayage de c/B ∈ {0,01 ; 0,05 ; 0,1 ; 0,2} (illustratif) et de ρ.
- Contrôle négatif : courbes synthétiques monotones sans croisement — l'oracle ne doit jamais changer.
- Falsification : H_A falsifiée si l'oracle ne change sur aucun régime ; H_B falsifiée si un régime montre un gain > δ₂ hors intervalle de bruit. Note : E2 teste la *valeur plafond* du problème ; si H_B tient, E1 et E6 perdent leur objet.

**E3 — Le réemploi de la validation corrompt-il les décisions ?**
- H_A : avec un seul ensemble de validation consulté à chaque décision, la fraction de « mauvais changements » (changement vers une classe dont la perte de confirmation est pire) dépasse d'au moins δ₃ (illustratif : 10 points) celle obtenue avec ensembles de sélection/confirmation séparés ou holdout réutilisable.
- H_B : écart < δ₃ ; le bruit inter-graines domine le biais de sélection.
- Métrique : fraction de mauvais changements ; optimisme moyen L_sélection − L_confirmation en fonction du nombre de consultations m.
- Contrôle négatif : même protocole avec décisions aléatoires (indépendantes de la validation) — l'optimisme doit être nul.
- Falsification : courbe d'optimisme plate en m falsifie H_A ; croissance en m avec écart de mauvais changements ≥ δ₃ falsifie H_B.

**E4 — L'écart de distribution d_t apporte-t-il une information décisionnelle ?**
- H_A : d_t prédit une dégradation de L_k dans la fenêtre suivante (AUROC ≥ 0,75, illustratif) au-delà de ce que prédit la pente de L̂_k seule, et une politique F5 bat F2 d'au moins δ₄ sur flux non stationnaires.
- H_B : AUROC incrémental < 0,55 ; d_t réagit à des décalages marginaux sans effet sur la perte, et F5 déclenche des changements inutiles.
- Métrique : AUROC incrémental ; nombre de changements déclenchés par d_t suivis d'une amélioration.
- Contrôle négatif : flux stationnaire avec d_t artificiellement perturbé — F5 ne doit pas changer plus souvent que F2.
- Falsification claire dans les deux sens par les seuils ci-dessus ; de plus, si F5 change plus souvent que F2 sur le contrôle, a5 est falsifiée pour la mesure d_t choisie.

**E5 — Généralisation ou mémorisation des familles ?**
- H_A (mémorisation) : la perte sur familles tenues à l'écart croît avec la distance à la famille vue la plus proche, pente significativement positive, et dépasse la perte intra-famille d'un facteur ≥ 1,5 (illustratif) au-delà d'un rayon.
- H_B (généralisation) : pente non distinguable de zéro sur le domaine couvert ; la borne V2 est non vide et la couverture de V1 nominale.
- Métrique : pente de régression perte ~ distance ; écart borne − observé.
- Contrôle négatif : permutation des étiquettes de familles — la pente doit disparaître ; si elle persiste, la distance mesure autre chose que la nouveauté de famille.
- Falsification : pente nulle falsifie H_A ; pente positive avec facteur ≥ 1,5 falsifie H_B.

**E6 — Réserve fixée ou adaptative ?**
- H_A : la réserve adaptative (déclenchée par d_t ou remontée confirmée, nombre de changements borné) donne une perte finale inférieure à la meilleure réserve fixe d'au moins δ₆ sur flux non stationnaires, sans être pire de plus de δ₆/2 sur flux stationnaires.
- H_B : la meilleure réserve fixe (choisie a posteriori — avantage concédé à H_B) fait aussi bien ; l'adaptativité paie son surcoût de consultations.
- Contrôle négatif : flux stationnaire — la réserve adaptative ne doit presque jamais se déclencher.
- Falsification symétrique par les deux seuils.

---

## (c) Instruments nommés : mesure minimale de fonctionnement

| Instrument | Taux de détection à mesurer | Fausses alertes | Cas honnêtes appariés | Vérification mécanique à battre |
|---|---|---|---|---|
| Extrapolateur de L_k(b) | Fraction de couples de classes dont l'ordre final (à 100 % de B) est correctement prédit à partir de 20 % de B (illustratif) | Fraction de « changements » recommandés qui finissent pires | Couples de classes à courbes qui se croisent vs ne se croisent pas, appariés par écart final | Ordre par dernière valeur ; ordre par pente de la dernière fenêtre ; halving successif |
| Estimateur de variance de L̂_k | Couverture des intervalles nominaux à 90 % mesurée sur réplications par graines | Intervalles trop étroits (couverture < 80 %) ou trop larges (puissance nulle) | Même classe, mêmes données, graines différentes | Variance d'échantillonnage seule (σ²/n_val), sans composante inter-graines |
| Mesure d'écart d_t | Détection d'un décalage injecté de magnitude connue (mélange contrôlé de deux sources) dans la fenêtre suivante | Alertes sur flux stationnaire par unité de budget | Flux stationnaire vs flux avec décalage injecté, mêmes données de base | CUSUM sur la perte elle-même ; test t entre fenêtres de perte |
| Correction de sélection / intervalles post-sélection | Couverture conditionnelle de l'intervalle pour la classe sélectionnée, sur réplications | Intervalles si larges qu'aucun changement n'est jamais décidé (puissance) | Sélection du minimum parmi K classes avec vérité connue par simulation | Bonferroni sur K ; intervalle naïf non corrigé |
| Holdout réutilisable | Optimisme résiduel L_sélection − L_confirmation après m consultations | Réponses bloquées (budget de confidentialité épuisé) avant la fin | Mêmes données, protocole naïf vs réutilisable | Séparation stricte sélection/confirmation |
| Borne PAC-Bayes multi-tâches (V2) | Proportion de bornes non vides ; écart borne − perte observée sur familles tenues à l'écart | Bornes violées (perte observée au-dessus de la borne au niveau de confiance nominal) | Mêmes familles, n variable (sous-échantillonnage du nombre de familles) | Intervalle empirique leave-families-out |
| Critère de décision complet (F1–F5) | Regret vs oracle hors ligne, par tâche | Changements inutiles par tâche | Courbes synthétiques avec/sans croisement ; tâches réelles avec/sans non-stationnarité | « Explorer uniformément puis figer » ; halving successif |

Un instrument dont la mesure de détection ne dépasse pas la vérification mécanique de la dernière colonne de plus que l'intervalle de bruit est à retirer du critère : il ajoute des consultations de validation (donc du biais, § 2) sans information.

---

## (d) Ancrage matériel (tout chiffre illustratif)

**Modèles et données ouverts.** Trois régimes, pour tester la dépendance des conclusions à l'échelle :
1. Tabulaire : classes = {régression linéaire régularisée, forêts, gradient boosting à profondeurs variées, petits MLP} sur des jeux ouverts (collections OpenML, à vérifier pour la référence exacte de la suite utilisée). Courbes complètes en CPU-heures. Permet beaucoup de réplications, donc E3, E5 et la calibration des intervalles.
2. Vision petite échelle : classes = architectures convolutives de tailles croissantes (emboîtées, pour F4) sur CIFAR-10/100 (RAPPORTÉ, à vérifier : Krizhevsky, « Learning multiple layers of features from tiny images », 2009). Permet E1, E2, E6 avec croisements de courbes plausibles.
3. Langage petite échelle : transformeurs de 10 à 100 M de paramètres (illustratif) sur corpus ouverts, pour tester F4 (surface L(s, b)) ; coût le plus élevé, réplications limitées.

Bases de courbes d'apprentissage préenregistrées (à vérifier : par exemple les jeux de courbes publiés avec les travaux d'optimisation d'hyperparamètres cités en § 1) peuvent remplacer le régime 2 pour E1–E3 à coût quasi nul, au prix d'un contrôle moindre sur la validation réemployée.

**Calcul.** Le coût dominant est l'enregistrement des courbes complètes : K classes × G graines × T tâches × un entraînement complet. Illustratif, régime 2 : K = 8, G = 10, T = 10, ≈ 0,5 GPU-h par entraînement complet ⇒ ≈ 400 GPU-h. Régime 1 : quelques centaines de CPU-h. Régime 3 : K = 5, G = 3, T = 3, ≈ 20 GPU-h par entraînement ⇒ ≈ 900 GPU-h. Simulation hors ligne des politiques et oracle : négligeable devant l'enregistrement. Non-stationnarité (E4, E6) : construite par mélange contrôlé de deux sources dans le flux, sans surcoût d'entraînement notable.

**Coût.** Illustratif, à 1–2 € par GPU-h sur offre ouverte : 1 300 GPU-h ⇒ 1,3–2,6 k€, plus CPU. Ordre de grandeur d'un projet de quelques semaines pour une personne, pas d'un programme.

**Ce qui n'est pas couvert par cet ancrage.** Les régimes où c est lui-même incertain (a2) et où le coût d'une évaluation varie fortement entre classes (a7) ; ils demanderaient de mesurer c empiriquement par transfert partiel de θ entre classes, ce qui est une expérience supplémentaire non chiffrée ici.

---

## 5. Références citées (toutes à vérifier ; aucune n'est donnée avec identifiant)

Agrawal, Hegde & Teneketzis, 1988, « Asymptotically efficient adaptive allocation rules for the multiarmed bandit problem with switching cost » · Amit & Meir, 2018, « Meta-learning by adjusting priors based on extended PAC-Bayes theory » · Audibert, Bubeck & Munos, 2010, « Best arm identification in multi-armed bandits » · Banks & Sundaram, 1994, « Switching costs and the Gittins index » · Baxter, 2000, « A model of inductive bias learning » · Berk, Brown, Buja, Zhang & Zhao, 2013, « Valid post-selection inference » · Besbes, Gur & Zeevi, 2014, « Stochastic multi-armed-bandit problem with non-stationary rewards » · Domhan, Springenberg & Hutter, 2015, « Speeding up automatic hyperparameter optimization of deep neural networks by extrapolation of learning curves » · Dwork, Feldman, Hardt, Pitassi, Reingold & Roth, 2015, « The reusable holdout: preserving validity in adaptive data analysis » · Garivier & Moulines, 2011, « On upper-confidence bound policies for switching bandit problems » · Gittins, 1979, « Bandit processes and dynamic allocation indices » · Hestness et al., 2017, « Deep learning scaling is predictable, empirically » · Hoffmann et al., 2022, « Training compute-optimal large language models » · Jamieson & Talwalkar, 2016, « Non-stochastic best arm identification and hyperparameter optimization » · Kaplan et al., 2020, « Scaling laws for neural language models » · Karnin, Koren & Somekh, 2013, « Almost optimal exploration in multi-armed bandits » · Krizhevsky, 2009, « Learning multiple layers of features from tiny images » · Lee, Sun, Sun & Taylor, 2016, « Exact post-selection inference, with application to the lasso » · Li, Jamieson, DeSalvo, Rostamizadeh & Talwalkar, 2018, « Hyperband: a novel bandit-based approach to hyperparameter optimization » · Maurer, 2005, « Algorithmic stability and meta-learning » · Maurer, Pontil & Romera-Paredes, 2016, « The benefit of multitask representation learning » · McAllester, 1999, « Some PAC-Bayesian theorems » · Pentina & Lampert, 2014, « A PAC-Bayesian bound for lifelong learning » · Swersky, Snoek & Adams, 2014, « Freeze-thaw Bayesian optimization » · Viering & Loog, 2022, « The shape of learning curves: a review ».

Références que je ne peux attribuer avec assez de sûreté et que je ne cite donc pas : travaux sur la validation croisée par courbes d'apprentissage, suites de jeux tabulaires de référence, bases publiques de courbes d'apprentissage — « référence à vérifier » pour chacun.

---

**Ce qui peut être réfuté ici, en une phrase :** si E2 montre que l'oracle ne change jamais de classe une fois l'exploration faite, dans tous les régimes de c testés, alors la question de l'arbitre se réduit à l'identification de meilleur bras à budget fixe et les voies F1, F2, F5 n'ont pas d'objet ; c'est l'expérience à faire en premier.

FIN-DE-CELLULE