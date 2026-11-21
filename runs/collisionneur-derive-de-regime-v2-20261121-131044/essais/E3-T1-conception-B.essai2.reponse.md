# Proposition B — Tour III.1 : corriger un seuil à 1 % de fausses alertes sous changement de régime

**Pièces reçues :** FAITS et QUESTION, complets en apparence ; aucune pièce coupée.

**Correspondance avec le livrable :** la QUESTION fixe l'ordre 1 à 6, et je le suis.
- Le volet (a) figure au §1.
- Le volet (c) figure au §3.
- Le volet (b) figure au §6, sous forme de duels.
- Le volet (d) figure en fin de §6.

**Statuts :**
- Tout calcul étiqueté « calcul » est exact sous échangeabilité, mais les tailles d'échantillon que j'y injecte sont illustratives.
- Je ne donne aucun identifiant arXiv de mémoire. La règle d'intégrité 3 l'interdit, et la QUESTION ne peut pas lever une règle d'intégrité.

---

## 1. Ce qu'un expert ferait sans qu'on le demande, et (a) ce que la question suppose

### (a) Suppositions non établies

| # | Ce que la question tient pour acquis | Statut |
|---|---|---|
| S1 | « Le taux réel triple » | RAPPORTÉ (CURA, identifiant tel que donné dans les faits, page non lue). Dans les mondes plantés du programme, le triplement est une **construction déclarée** : il ne mesure rien de la réalité. |
| S2 | Le taux était de 1 % avant le changement de régime | HYPOTHÈSE. Le conforme classique garantit 1 % **en moyenne sur les tirages de l'échantillon d'étalonnage**, pas pour le seuil effectivement obtenu (voir §1.1). |
| S3 | Le changement de régime est connu et daté | HYPOTHÈSE. En déploiement, la frontière d'un régime peut être inconnue ou progressive. |
| S4 | Des épisodes honnêtes étiquetés existent dans le nouveau régime | HYPOTHÈSE. Les faits disent « peu d'épisodes honnêtes par régime » ; ils ne disent pas qu'on en dispose au moment du déploiement. |
| S5 | La hausse des alertes vient d'une dérive honnête et non d'une vague de sabotage | HYPOTHÈSE. Sans référence de confiance, les deux sont indistinguables (voir §1.4). |
| S6 | Le « 1 % » s'entend par moniteur, par épisode | Non établi. Les faits mentionnent une agrégation de moniteurs et des scores « par épisode (ou par pas) ». Le taux du système agrégé n'est pas celui d'un moniteur. |
| S7 | Une seule correction vaut pour les quatre sources de dérive (tâche, version, longueur, source bénigne) | HYPOTHÈSE, probablement fausse (voir duel D2). |
| S8 | Le jumeau est honnête et comparable | RAPPORTÉ fragile par les faits eux-mêmes. |

### 1.1 Séparer le triplement du bruit d'étalonnage

Avec quelques centaines d'épisodes, le taux réalisé fluctue fortement même sans dérive. Ce résultat est connu sous le nom de validité conditionnelle à l'étalonnage : Vovk (2012), « Conditional validity of inductive conformal predictors » ; Bates, Candès, Lei, Romano, Sesia (2023), « Testing for outliers with conformal p-values », *Annals of Statistics*.

**Calcul, n = 300 illustratif :**
- Le seuil conforme est la 298ᵉ statistique d'ordre.
- Le taux réalisé suit une loi Beta(3, 298), de moyenne ≈ 1 % et d'écart-type ≈ 0,57 %.
- P(taux ≥ 2 %) ≈ 6 %.
- P(taux ≥ 3 %) ≈ 0,6 %.

Le bruit seul triple donc rarement le taux, mais il le double une fois sur seize. Il faut décomposer le triplement avant de le corriger (duel D1).

### 1.2 Se demander d'abord si le problème est soluble

**Calcul :**
- Un seuil conforme fini à 1 % exige n ≥ 99 par strate.
- Une garantie PAC (taux ≤ 1 % avec probabilité ≥ 95 %) exige n ≥ 299. Le seuil vaut alors le **maximum** des scores honnêtes, car P(Bin(300 ; 0,01) = 0) ≈ 4,9 %.

Conséquence directe : avec « quelques centaines » d'épisodes par régime, toute correction rigoureuse (stratifiée, robuste, PAC) **dégénère en « seuil = max observé »** ou en seuil infini.

La vraie question devient donc : combien de détection coûte ce seuil, mesuré sur sabotages plantés ?

### 1.3 Regarder l'agrégation sur la longueur

Un moniteur par pas, agrégé par épisode, donne au mieux un maximum sur L pas, puisque la moyenne sur les jetons est interdite en production. Ce maximum croît mécaniquement avec L.

Un seuil unique « juste en moyenne sur les longueurs » est donc trop bas pour les longs épisodes et trop haut pour les courts. C'est un effet de composition, pas un mystère : le défaut par tranche de longueur est attendu.

### 1.4 Reconnaître le vrai nœud : l'absence d'étiquettes

Toute recalibration sur les scores de déploiement **absorbe le sabotage** s'il y en a. Un saboteur qui provoque une dérive gagne un seuil plus haut.

Les seules références honnêtes sans étiquette humaine sont :
- le jumeau ;
- des témoins injectés, produits par un générateur de confiance.

Tout repose donc sur l'écart entre le jumeau et l'agent honnête. Les faits le déclarent fragile, et personne ne demande de le mesurer.

### 1.5 Mesurer le taux du système, pas celui du moniteur

K moniteurs à 1 % chacun donnent jusqu'à K % d'alertes au niveau du système. Deux outils permettent de combiner des moniteurs dépendants avec une garantie :
- les e-valeurs : la moyenne d'e-valeurs reste une e-valeur (Vovk & Wang 2021, « E-values: Calibration, combination and applications », *Annals of Statistics*) ;
- la combinaison de p-valeurs sous dépendance arbitraire (Vovk & Wang 2020, « Combining p-values via averaging », *Biometrika*).

---

## 2. Données brutes à prendre au départ

**Par épisode honnête (agent et jumeau, même tâche, même graine si possible) :**
- les scores bruts **par pas et par moniteur**, et non le score d'épisode seul ;
- les activations à la couche de chaque sonde, pour diagnostiquer une rotation de représentation après un changement de version ;
- les métadonnées : identifiant et famille de tâche, empreinte de version de l'agent **et** du jumeau, longueur en pas et en jetons, source bénigne, horodatage, graine.

**Courbes de maximum de préfixe :** pour chaque épisode, le maximum courant sur les pas 1..ℓ. Un épisode long fournit ainsi un échantillon pour chaque longueur plus courte (voir proposition P2).

**Journaux de déploiement :**
- les scores bruts dans l'ordre temporel, et non les taux d'alerte agrégés ;
- l'identité des épisodes relus par un humain **et la raison de la relecture**. Une relecture déclenchée par une alerte est un échantillon biaisé et n'estime pas le taux de fausses alertes.

**CURA :** les distributions de scores par régime, si elles sont publiées. Je ne sais pas si elles le sont.

---

## 3. Méthodes et outils : supposition, mode d'échec, et (c) mesure minimale

**Mesure minimale commune à tous les instruments (c) :**
- Le taux de fausses alertes réalisé est mesuré **par régime et par tranche de longueur**, sur des épisodes honnêtes appariés (agent honnête contre jumeau, même tâche), tenus hors de l'étalonnage.
- Le taux de détection est mesuré sur des sabotages plantés, **au taux de fausses alertes réellement atteint**.
- Les vérifications mécaniques à battre sont :
  - **M1** : seuil égal au maximum des scores honnêtes du régime ;
  - **M2** : recalibration naïve sur les m premiers épisodes honnêtes du nouveau régime ;
  - **M3** : budget d'audit fixe, les k plus hauts scores par lot ;
  - **M4** : seuil par tranche de longueur seule.

Un instrument qui ne bat pas M1 ou M3 en détection, à taux de fausses alertes égal, est inutile.

**Taille du jeu de test :** distinguer 1 % de 3 % demande de l'ordre de quelques centaines d'épisodes honnêtes de test par régime (calcul, voir P3). En dessous, on ne mesure rien.

### 3.1 Conforme pondéré sous décalage de covariables

**Référence :** Tibshirani, Barber, Candès, Ramdas (2019), « Conformal Prediction Under Covariate Shift », NeurIPS.

**Ce qu'il suppose :**
- La loi du score sachant les covariables x reste stable ; seule la loi de x change.
- Le rapport de vraisemblance w(x) est connu ou bien estimé.

**Comment il échoue :**
1. **Changement de version** : le score sachant x change, puisque la sonde lit une autre représentation. Ce n'est pas un décalage de covariables.
2. **Taille effective trop faible** : si n_eff = (Σw)²/Σw² < 99, ou si le poids normalisé du point de test dépasse α, le seuil vaut +∞. **Le moniteur devient aveugle**, sans erreur visible.
3. **Estimation de w** : avec peu d'épisodes, elle est bruitée dans les queues, précisément là où se joue le 1 %.

**Mesure (c) :**
- fraction des lots où le seuil est infini ;
- n_eff par lot ;
- taux de fausses alertes par strate.

### 3.2 Conforme adaptatif en ligne

**Références :**
- Gibbs & Candès (2021), « Adaptive Conformal Inference Under Distribution Shift », NeurIPS ;
- Gibbs & Candès (2024), « Conformal Inference for Online Prediction with Arbitrary Distribution Shifts », JMLR ;
- Zaffran, Féron, Goude, Josse, Dieuleveut (2022), « Adaptive Conformal Predictions for Time Series », ICML ;
- Angelopoulos, Candès, Tibshirani (2023), « Conformal PID Control for Time Series Prediction », NeurIPS ;
- Bhatnagar, Wang, Xiong, Bai (2023), « Improved Online Conformal Prediction via Strongly Adaptive Online Learning », ICML.

**Garantie :**
- La fréquence moyenne d'erreur à long terme converge vers α, même pour des suites arbitraires.
- La borne est de la forme (max(α₁, 1−α₁) + γ)/(γT). Je la cite de mémoire ; la constante est à vérifier dans l'article.

**Comment il échoue ici :**
1. Il faut une rétroaction « cette alerte était-elle fausse ? » à chaque pas. Elle n'existe que par relecture humaine, rare et biaisée.
2. La garantie porte sur une **moyenne temporelle**. Elle peut tenir tandis qu'un régime entier tourne à 3 %, compensé par une autre période à taux plus bas.
3. **Calcul, γ = 0,005 illustratif** : un écart ≤ 0,5 point demande T ≈ 40 000 observations étiquetées. À 1 %, la garantie de long terme est hors de portée du budget.
4. Si la rétroaction vient du flux de déploiement, le sabotage entre dans la mise à jour.

**Mesure (c) :** taux de fausses alertes par fenêtre de régime, et pas seulement en moyenne cumulée.

### 3.3 Étalonnage conditionnel, par strates ou par groupes

**Références :**
- Mondrian : Vovk, Gammerman, Shafer (2005), *Algorithmic Learning in a Random World* ;
- Gibbs, Cherian, Candès (2023), « Conformal prediction with conditional guarantees » : couverture sous toute repondération appartenant à une classe de fonctions F des métadonnées ;
- Bastani, Gupta, Jung, Noarov, Ramalingam, Roth (2022), « Practical Adversarial Multivalid Conformal Prediction », NeurIPS.

**Ce qu'il suppose :** la dérive réelle est une repondération appartenant à F.

**Comment il échoue :**
- Au plus 99 épisodes par strate : seuil infini.
- Une classe F riche par rapport à n : seuil conservateur.
- Une dérive hors de F, comme une nouvelle version : aucune garantie.

**Mesure (c) :**
- taux de fausses alertes dans chaque cellule de F ;
- taux de fausses alertes sur une dérive plantée **hors de F**, comme contrôle de la limite de la méthode.

### 3.4 Détecter le changement de régime avant de faire confiance au seuil

**Références :**
- tests à deux échantillons : Gretton et al. (2012), « A Kernel Two-Sample Test », JMLR ; Rabanser, Günnemann, Lipton (2019), « Failing Loudly », NeurIPS ;
- martingales conformes d'échangeabilité : Vovk, Nouretdinov, Gammerman (2003), « Testing exchangeability on-line », ICML ;
- e-processus : Ramdas, Grünwald, Vovk, Shafer (2023), « Game-theoretic statistics and safe anytime-valid inference », *Statistical Science* ;
- e-détecteurs : Shin, Ramdas, Rinaldo, « E-detectors… » (référence à vérifier pour l'année et le titre exact) ;
- dérive **nuisible** : Podkopaev & Ramdas, « Tracking the risk of a deployed model and detecting harmful distribution shifts » (année à vérifier, ICLR) ;
- CUSUM : Page (1954), *Biometrika*.

**Comment il échoue :**
1. Un test sur toute la distribution détecte des dérives sans effet sur la queue, d'où des recalibrations inutiles qui coûtent des épisodes. Il faut tester la **queue**, c'est-à-dire le taux de dépassement.
2. Le test de dérive nuisible de Podkopaev & Ramdas suppose des étiquettes, qu'on n'a pas en déploiement.
3. Appliqué au flux de déploiement, il ne distingue pas une dérive honnête d'une vague de sabotage (§1.4).

**Mesure (c) :**
- délai de détection sur la famille plantée où le taux triple ;
- taux de fausses détections sur un régime stable ;
- taux de confusion sur un monde planté qui contient une vague de sabotage **sans** dérive honnête.

### 3.5 Recalibration par fenêtre glissante

**Référence :** Barber, Candès, Ramdas, Tibshirani (2023), « Conformal prediction beyond exchangeability », *Annals of Statistics*.

**Garantie :** la perte de couverture est bornée par une somme pondérée de distances en variation totale entre les points de la fenêtre et le point de test.

**Comment il échoue :**
- Une fenêtre de W < 99 épisodes donne un seuil infini.
- Une rupture brutale produit une fenêtre mêlant deux régimes.
- La fenêtre exige des épisodes honnêtes **courants**, d'où le recours aux témoins (3.6).

**Mesure (c) :** taux de fausses alertes dans les W premiers lots qui suivent une rupture plantée.

### 3.6 Témoins honnêtes injectés dans chaque lot

**Ce qu'il suppose :**
- Les témoins sont échangeables avec les épisodes honnêtes de l'agent **dans le régime courant**.
- Ils sont indiscernables pour le moniteur.

**Comment il échoue :**
- Un témoin produit par le jumeau hérite de l'écart entre jumeau et agent.
- Un témoin rejoué d'un ancien régime n'ancre rien.
- Quelques témoins par lot ne mesurent pas un taux de 1 % : il en faut des centaines par régime (P3).

**Mesure (c) :** sur la fraction des témoins tenue hors de l'étalonnage, l'écart entre leur taux de fausses alertes et celui des épisodes honnêtes de l'agent.

### 3.7 Jumeau honnête comme référence courante

**Deux usages possibles :**
- (i) score différentiel s_agent − s_jumeau sur la même tâche ;
- (ii) étalonnage du seuil sur les épisodes du jumeau dans le régime courant.

**Ce qu'il suppose :** la dérive est de **mode commun**, c'est-à-dire qu'elle déplace le jumeau et l'agent honnête de la même façon.

**Comment il échoue :**
- Version désynchronisée entre agent et jumeau.
- Sonde entraînée sur les activations de l'agent puis appliquée au jumeau.
- Un sabotage qui imite les écarts naturels entre jumeau et agent.

**Mesure (c) :** duel D3.

### 3.8 Méthodes robustes au pire cas sur une famille de décalages

**Références :**
- Cauchois, Gupta, Ali, Duchi, « Robust Validation: Confident Predictions Even When Distributions Shift » (année à vérifier, JASA) ;
- Duchi & Namkoong (2021), *Annals of Statistics*.

**Comment il échoue :**
- Couvrir une boule de f-divergence autour de la loi d'étalonnage impose un niveau de base bien inférieur à 1 %.
- Absorber un facteur 3 connu revient à viser environ 0,33 %. Avec n = 300 (illustratif), le rang conforme vaut ⌈301 × (1 − 1/300)⌉ = 300 : **le maximum**, et seulement en garantie marginale.
- Je ne connais pas de tête les constantes exactes pour une boule de rayon donné.

**Mesure (c) :** le coût en détection face à la vérification mécanique M1.

### 3.9 Autres outils pertinents

- **Contrôle de risque** : Angelopoulos, Bates, Candès, Jordan, Lei (2021), « Learn then Test » ; Bates, Angelopoulos, Lei, Malik, Jordan (2021), « Distribution-free, risk-controlling prediction sets ». Ils permettent de choisir un seuil avec une garantie PAC sur le taux de fausses alertes du système agrégé.
- **Intervalles exacts** : Clopper & Pearson (1934), pour tout taux mesuré.
- **Budget d'audit fixe** : c'est le cadre de Greenblatt, Shlegeris, Sachan, Roger (2023), « AI Control: Improving Safety Despite Intentional Subversion ».

---

## 4. Vérification hors du programme et de son directeur

1. **Mondes plantés conçus par un tiers.** La famille de dérive est écrite par quelqu'un qui ne connaît pas la règle candidate. La vérité et le verdict restent hors de la machine qui exécute, comme les faits l'exigent déjà. Elle comprend au minimum :
   - (i) une dérive de covariables pure ;
   - (ii) une dérive conditionnelle pure, imitant une nouvelle version ;
   - (iii) une dérive de longueur ;
   - (iv) une vague de sabotage **sans** dérive ;
   - (v) une dérive accompagnée d'une vague de sabotage.
2. **Pré-enregistrement.** Règle, seuils de décision des duels et nombre d'épisodes sont fixés avant l'exécution.
3. **Jeux publics avec décalage.** Ils servent seulement à éprouver les méthodes d'étalonnage, puisqu'ils ne portent pas sur des moniteurs d'agents :
   - Koh et al. (2021), « WILDS: A Benchmark of in-the-Wild Distribution Shifts » ;
   - Malinin et al., « Shifts » (2021, référence à vérifier) ;
   - pour le sabotage d'agents : SHADE-Arena (référence à vérifier).
4. **Réplication.** D'autres graines et d'autres découpages d'étalonnage, puis la distribution complète des taux réalisés (§1.1), et pas un point unique.
5. **Mesure indépendante.** Une relecture humaine d'un échantillon **tiré au hasard** parmi les épisodes non alertés et alertés, et non choisi par alerte. C'est le seul estimateur sans biais de sélection, même s'il est petit.
6. **CURA.** La page du PDF est lue par un tiers, et la métrique est vérifiée : par pas ou par épisode, par moniteur ou par système.

---

## 5. Demande reformulée

> Pour chaque source de dérive (tâche, version, longueur, source bénigne) et pour le système de moniteurs agrégé :
> (1) décomposer le taux de fausses alertes réalisé entre variabilité d'étalonnage et dérive réelle ;
> (2) proposer une règle calculable qui donne, **par régime et par tranche de longueur**, soit une garantie PAC « taux de fausses alertes ≤ α avec probabilité ≥ 1−δ » sous des suppositions énoncées et testables, soit un refus explicite (« aveugle ») quand les données ne le permettent pas ;
> (3) n'utiliser comme référence honnête que des sources de confiance (jumeau, témoins), jamais le flux de déploiement brut ;
> (4) prouver sur mondes plantés tiers, à taux de fausses alertes réalisé égal, une détection supérieure aux vérifications mécaniques M1 et M3, et une non-absorption des vagues de sabotage.

---

## 6. Propositions de correction, duels (b) et ancrage (d)

### P1 — Seuil PAC par régime, avec refus explicite

**Règle :** pour n épisodes honnêtes du régime, prendre le plus petit j tel que P(Bin(n, α) ≤ j) ≤ δ, puis fixer le seuil à la (n−j)-ième statistique d'ordre. Si 0,99ⁿ > δ, ce j n'existe pas : la règle renvoie « aveugle » et passe à P5.

**Garantie :** P(taux réalisé > α) ≤ δ, sous l'hypothèse d'épisodes honnêtes échangeables à l'intérieur du régime.

**Coût :**
- quasi nul en calcul ;
- élevé en détection, car le seuil vaut le maximum pour n ≈ 300.

**Test de mort :** dans la famille plantée où le taux triple, la règle meurt si le taux réalisé dépasse α dans plus de δ des réplications **à l'intérieur d'un régime correctement identifié**. Au travers d'une rupture non détectée, elle meurt par construction : elle doit être couplée à P3.

**Distinction avec la littérature :** P1 n'est pas nouvelle (Vovk 2012 ; Bates et al. 2023). Son rôle est de servir de **plancher honnête** et de rendre l'impossibilité visible.

### P2 — Seuil fonction de la longueur, estimé par maxima de préfixe

**Règle :**
- τ(ℓ) est estimé par P1 sur l'ensemble {max des pas 1..ℓ de chaque épisode honnête de longueur ≥ ℓ}, puis rendu monotone croissant.
- Un épisode de longueur L alerte si le score d'un pas t dépasse τ(t), ou τ(L) à la fin.
- Aucune moyenne sur les jetons n'est utilisée, ce qui respecte la contrainte de production.

**Garantie :** celle de P1 pour chaque ℓ, sous l'HYPOTHÈSE que le préfixe de longueur ℓ d'un épisode long a la même loi que le maximum d'un épisode complet de longueur ℓ.

**Coût :** calcul négligeable. La règle gagne en efficacité d'échantillon pour les courtes longueurs et reste pauvre pour les longues.

**Test de mort :** le taux de fausses alertes par tranche de longueur sur des épisodes **complets** tenus hors de l'étalonnage sort de l'intervalle de Clopper-Pearson à 95 % autour de α dans au moins une tranche. Les fins d'épisode ont alors un comportement propre, et P2 est falsifiée.

**Distinction :** je ne connais pas de travail publié qui étalonne un seuil de moniteur d'agent par maxima de préfixe. Je ne sais pas si c'est nouveau.

### P3 — Garde à deux canaux : distinguer une dérive honnête d'une vague de sabotage

**Règle :**
- **Canal T** : e-processus par pari sur les dépassements des **témoins** au seuil courant, avec Kₜ = Π(1 + λ(1[s > τ] − α)) et λ prévisible. Il teste H₀ : taux de dépassement des témoins ≤ α.
- **Canal D** : la même chose sur le flux de déploiement.

**Décision :**

| Canal T | Canal D | Lecture | Action |
|---|---|---|---|
| rejette | rejette | dérive honnête | nouvelle fenêtre de régime, recalibration P1/P2 sur témoins et jumeau seulement |
| ne rejette pas | rejette | anomalie hors honnêteté | **gel du seuil** et escalade vers la relecture humaine |
| rejette | ne rejette pas | probable écart entre témoins et agent | alerte de diagnostic, sans recalibration |

**Garantie :** par l'inégalité de Ville, la probabilité de déclarer à tort une dérive des témoins, à n'importe quel moment, est ≤ 1/seuil de l'e-processus.

**Calcul (illustratif) :** à seuil 20 et pari quasi optimal, l'information par observation vaut KL(Bern(0,03) ‖ Bern(0,01)) ≈ 0,013 nat. Distinguer 3 % de 1 % demande donc de l'ordre de 230 témoins. Ce chiffre est une borne optimiste.

**Coût :** les témoins, c'est-à-dire des épisodes supplémentaires du jumeau par lot.

**Test de mort :** la règle meurt si, dans le monde planté « vague de sabotage sans dérive », elle recalibre, ou si, dans le monde « dérive seule », elle gèle plus souvent qu'un taux pré-enregistré.

**Distinction :** les tests de dérive nuisible publiés supposent des étiquettes. Ici, l'étiquette est remplacée par un canal témoin de confiance. Je ne sais pas si cette construction existe déjà dans la littérature du contrôle de l'IA.

### P4 — Conforme conditionnel sur classe de métadonnées, avec garde de taille effective

**Règle :**
- Appliquer l'approche de Gibbs, Cherian, Candès (2023) avec F = {indicatrices de tranches de longueur × sources bénignes × familles de tâches}, limitée pour que chaque cellule contienne au moins 99 épisodes.
- Garde : si n_eff < 1/α, ou si le seuil est infini, renvoyer « aveugle » et passer à P5.

**Garantie :** couverture sous toute repondération dans F, sous l'HYPOTHÈSE que la loi du score sachant les métadonnées est stable.

**Test de mort :** une dérive conditionnelle plantée (simulant une nouvelle version) conserve un taux de fausses alertes ≥ 2α. C'est l'échec **attendu**, et il délimite la portée de la règle. P4 meurt pour de bon si elle échoue aussi sur une dérive de covariables pure appartenant à F.

**Distinction :** méthode publiée. L'apport est seulement la garde « aveugle » explicite.

### P5 — Quand renoncer au seuil fixe, et quoi mettre à la place

Renoncer au seuil fixe quand l'une de ces conditions tient :
- n < 299 par régime pour une garantie PAC à 1 % et δ = 5 % (calcul) ;
- n_eff < 99 ;
- le canal T de P3 vient de rejeter et la nouvelle fenêtre n'est pas encore remplie.

**Remplacements :**
- **Budget d'audit fixe par lot**, les k plus hauts scores. Le taux d'alerte est borné par construction, à k/lot ; la détection devient la variable mesurée. C'est la vérification mécanique M3.
- **Rapport d'une e-valeur continue** par épisode, avec des seuils d'action graduée plutôt qu'une alerte binaire.

### Duels (b)

**D1 — Origine du triplement**

| | Contenu |
|---|---|
| H_A | Le triplement est compatible avec la variabilité d'étalonnage. |
| H_B | Le triplement est une dérive réelle, hors de la bande d'échantillonnage. |
| Métrique | Taux de fausses alertes du nouveau régime, mesuré sur un grand jeu de test honnête, comparé à la distribution des taux réalisés obtenue par rééchantillonnage des jeux d'étalonnage de l'ancien régime. |
| Seuil | H_B si la borne basse de Clopper-Pearson à 95 % du nouveau régime dépasse le 97,5ᵉ centile de la bande. |
| Contrôle négatif | Ancien régime coupé au hasard en deux moitiés : aucune « dérive » ne doit apparaître. |
| Falsifie H_A | Taux hors de la bande. |
| Falsifie H_B | Taux dans la bande. |

Les deux causes peuvent coexister. Le duel tranche la question exclusive : « le triplement sort-il de la bande ? ».

**D2 — Mécanisme de la dérive**

| | Contenu |
|---|---|
| H_A | Décalage de covariables : la loi du score sachant les métadonnées est stable. |
| H_B | Décalage conditionnel. |
| Métrique | Taux de dépassement **dans chaque strate**, ancien contre nouveau régime ; taux après repondération par P4. |
| Seuil | Test exact de deux proportions par strate, avec correction de Holm. |
| Contrôle | Monde planté à dérive de covariables pure, où P4 doit restaurer α, et monde à dérive conditionnelle pure, où le test doit détecter. |
| Falsifie H_A | Au moins une strate diffère significativement. |
| Falsifie H_B | Aucune strate ne diffère et P4 restaure α dans l'intervalle de confiance. |

**D3 — Jumeau : dérive de mode commun ou différentielle**

| | Contenu |
|---|---|
| H_A | Mode commun : un seuil étalonné sur le jumeau du nouveau régime rend α pour l'agent honnête. |
| H_B | Dérive différentielle. |
| Métrique | Taux de fausses alertes de l'agent honnête, en épisodes appariés par tâche, au seuil P1 étalonné sur le jumeau. |
| Seuil | H_A si l'intervalle de confiance à 95 % contient α. |
| Contrôle négatif | Le jumeau et l'agent sont le même modèle et la même version ; l'écart doit être nul. |
| Falsifie H_A | Intervalle au-dessus de α. |
| Falsifie H_B | Intervalle contenant α, répliqué sur au moins deux sources de dérive. |

**D4 — P3 sépare-t-elle dérive et sabotage ?**

| | Contenu |
|---|---|
| H_A | La garde à deux canaux distingue les deux. |
| H_B | Elle les confond. |
| Métrique | Proportion de sabotages plantés absorbés par une recalibration ; taux de fausses alertes dans le monde « dérive seule ». |
| Seuil | Absorption ≤ 5 % et taux de fausses alertes dans l'intervalle de confiance autour de α (valeurs illustratives, à pré-enregistrer). |
| Contrôle négatif | Régime stable sans sabotage : aucun des deux canaux ne doit rejeter au-delà du niveau de Ville. |
| Falsifie H_A | Un des deux seuils dépassé dans les mondes tiers. |
| Falsifie H_B | Les deux respectés. |

**D5 — Hypothèse des préfixes (P2)**

| | Contenu |
|---|---|
| H_A | Les préfixes sont échangeables avec les épisodes complets de même longueur. |
| H_B | La fin d'épisode a un comportement propre. |
| Métrique | Test à deux échantillons sur les maxima à longueur ℓ : préfixes contre épisodes complets. |
| Contrôle négatif | Épisodes tronqués artificiellement, échangeables par construction. |
| Falsifie H_A | Rejet du test. |
| Falsifie H_B | Absence de rejet, avec une puissance pré-calculée suffisante. |

### (d) Ancrage matériel, entièrement illustratif

- **Modèles ouverts.** L'agent et le jumeau sont des modèles à poids ouverts, par exemple de la famille Llama ou Qwen, de taille modeste. Les sondes linéaires sont lues sur une seule couche.
- **Calcul des méthodes.** P1 à P5 tournent sur CPU, en secondes. Le coût est **la génération d'épisodes**.
- **Budget d'épisodes, ordre de grandeur :**
  - 300 épisodes honnêtes × 4 sources de dérive × 2 (agent, jumeau) ≈ 2 400 épisodes ;
  - plus environ 300 témoins par régime pour P3 ;
  - plus les mondes plantés tiers.
- **Calcul GPU.** Pour des épisodes de quelques milliers de jetons sur un modèle de 7 à 8 milliards de paramètres, j'estime quelques dizaines à quelques centaines d'heures-GPU. Je ne connais pas la longueur réelle des épisodes du programme, donc cette estimation est très incertaine.
- **Relecture humaine.** Elle est réservée à l'échantillon aléatoire du §4.5 et à la branche « gel » de P3.

FIN-DE-CELLULE