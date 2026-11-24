# Proposition A — Tour III.3 : réponse aux critiques

**État des pièces.** Ma conception E3-T1-A et les trois critiques croisées sont transmises complètes ; chacune se termine par FIN-DE-CELLULE. Le bloc FAITS reproduit la question de l'arbitre et ne contient aucune donnée empirique. Je ne traite que les sections « Sur la proposition A » de B, C et D. Quand j'emprunte un contrôle que ces pièces proposaient pour d'autres propositions, je le signale (B1).

**Statuts.**
- Les contenus des critiques sont RAPPORTÉS par leurs pièces.
- J'ai refait moi-même les dérivations marquées VÉRIFIÉ.
- Tous les seuils, tailles et budgets sont **illustratifs** et doivent être préenregistrés.

---

## (a) Verdict critique par critique

Notation : v = (i), u = (ii), ρ = u/v = (iii), α₀ = FPR initial du détecteur sur les épisodes honnêtes.

### Modèle M1 et expérience E2

| # | Critique (source) | Verdict | Raison / action |
|---|---|---|---|
| 1 | M1 ignore les faux positifs. Avec α₀ > 0, log(u\*/h\*) croît avec λ (C, D). | **Acceptée** | VÉRIFIÉ. Par prompt, h\* ∝ h₀e^{r_h/β}[1−α₀+α₀e^{−λ/β}], d'où ∂log(u\*/h\*)/∂(λ/β) = α₀e^{−z}/(1−α₀+α₀e^{−z}) > 0. Mon invariant ne vaut que si α₀ = 0 **et** si les violations signalées et non signalées ont la même récompense (Δ_u = Δ_f, D). Ces deux conditions deviennent des hypothèses explicites de M1. |
| 2 | Même à α₀ = 0, le rapport des marges agrégées sur les prompts dépend de λ (C, D). | **Acceptée** | VÉRIFIÉ. Par prompt, ∂_z u\* = u\*f\* et ∂_z h\* = h\*f\*. Le rapport par prompt est donc invariant. En revanche, la pente du rapport agrégé vaut E[u\*f\*]/E[u\*] − E[h\*f\*]/E[h\*], non nulle en général. E2 aurait réfuté M1 par effet de mélange. Correction : prédiction tabulaire exacte **par prompt** (E2′). |
| 3 | L'invariant porte sur u\*/h\*, pas sur u\* (B). | **Rejetée** sur le constat | C'est déjà ce que j'écrivais, en précisant que u\* croît faiblement avec λ. J'accepte l'ajout de B : les honnêtes ne doivent pas être pénalisés, ce qui revient au n° 1. |
| 4 | Une KL stationnaire ne certifie pas l'optimum ; le critère de plateau est satisfait sur les plateaux softmax (B, D). | **Acceptée** | Remplacé par deux critères. (a) Deux taux d'apprentissage atteignent le même point final, à la marge δ près. (b) Comparaison au calcul tabulaire exact. |
| 5 | Une pente linéaire peut être nulle sous une réponse non constante ; le bootstrap sur 5 graines n'a que 126 rééchantillons (B, D). | **Acceptée** | Contrastes par niveau de λ avec marge préenregistrée, et 8 graines au minimum. Plus de pente unique. |
| 6 | Écart d'optimiseur et couplage paramétrique sont confondus (critique de C et D adressée à B, qui s'applique à mon E2). | **Acceptée, empruntée** | J'ajoute un bras « table de logits découplée + même optimiseur » (GRPO, normalisation par écart-type, clipping, Adam). |

### Expérience E1 (sélection ou construction)

| # | Critique (source) | Verdict | Raison / action |
|---|---|---|---|
| 7 | Avec la règle de trois, faire varier N·T confond l'exposition avec la durée d'optimisation. Le palier 0,03 correspond à environ 2 pas (C, D). | **Acceptée** | VÉRIFIÉ : 0,03/(3·10⁻⁵) ≈ 10³ épisodes, soit environ 2 pas de 512. Le palier bas était vrai par sous-optimisation. |
| 8 | u₀ ≪ 3/n rend u₀·N·T non identifiable (C, D). | **Acceptée, transformée en test** | Je ne manipule plus u₀ estimé. Je manipule le **nombre k de violations non signalées présentes dans un pool fixe**, audité exhaustivement par l'oracle (E1′). k est un fait du pool, pas une estimation. Seule la borne supérieure ū₀⁺ intervient, et uniquement dans le sens où elle est identifiable. |
| 9 | Ma règle de trois borne ρ₀, pas u₀ (B). | **Acceptée** | C'est une erreur de ma part. Zéro passant parmi n_V violations borne ρ₀ ≈ 3/n_V. Pour borner u₀, il faut zéro violation non signalée parmi n tirages au total. |
| 10 | La signature « log π₀ sous le 0,1ᵉ percentile » est satisfaite sous sélection pure ; elle est confondue par la longueur (B, C, D). | **Acceptée** | Elle est retirée comme critère décisif et ne reste qu'à titre descriptif. |
| 11 | Après le premier pas, il faut borner le risque conditionnel de première apparition, pas u₀ (B). Utiliser des estimateurs de survie (proposé par C pour D). | **Acceptée, empruntée** | Bras on-policy : Kaplan-Meier sur le premier épisode non signalé violant, et variation de la taille de lot à π₀ strictement identique, sans amorçage SFT. |

### Expérience E3 (écarter ou pénaliser)

| # | Critique (source) | Verdict | Raison / action |
|---|---|---|---|
| 12 | Sous GRPO, « écarter » repondère les prompts, détruit la variance intra-groupe et change le nombre de tirages bruts (B, C, D). | **Acceptée** | Bras « masque d'avantage » (A = 0 après une baseline calculée sur le groupe complet), à tirages bruts égaux (contrôle C-3). « Écarter » est conservé, mais comparé seulement en analyse secondaire. |
| 13 | Le rapport d'aires est indéfini, ou à queue lourde, si le dénominateur est proche de 0 (B, D). | **Acceptée** | Remplacé par une différence d'aires avec marge δ. Le premier passage est traité par Kaplan-Meier, censure comprise. |

### Expérience E4 (détecteur ré-entraîné)

| # | Critique (source) | Verdict | Raison / action |
|---|---|---|---|
| 14 | L'AUC hors ligne n'est ni la marge uniforme ni le TPR au seuil (B). Une baisse de ρ après recalibration peut survenir à politique identique (B). | **Acceptée** | Critère : TPR à FPR fixé du détecteur **déployé**. Ajout d'un lot scellé, à politique gelée, rescoré par chaque version du détecteur. Plan croisé politique × version. |
| 15 | B = 100 contre une AUC oracle sur 50 000 confond séparabilité et erreur d'estimation (D). | **Rejetée en partie** | Ce contraste est le facteur manipulé, pas un confondant : l'écart entre séparabilité de la famille et détecteur limité par B est ce que M4 met en jeu. J'accepte en revanche que mon H_A ait été mal conditionné : il est désormais conditionné sur le TPR du détecteur déployé. |
| 16 | Tampon cumulatif ou fenêtre glissante non spécifié (D). Monotonie « 4 cycles sur 5 » sensible au bruit (D). Couverture (1−q)^B des sous-types rares (B). | **Acceptée** | Facteur tampon à taille d'échantillon égale (réservoir sur l'historique contre récents, emprunt de C à propos de D). Test de tendance sur les cycles avec marge. Le budget d'étiquettes de calibration est compté dans B. |

### Expérience E5 (nécessité du raisonnement)

| # | Critique (source) | Verdict | Raison / action |
|---|---|---|---|
| 17 | Tronquer la CoT change à la fois le calcul disponible et ce que lit le juge (B). L'indice chiffré change Δ, f₀, u₀ et la longueur (D). | **Acceptée** | Vérification de manipulation par une transformation de **même longueur** qui retire l'information pertinente. Δ et f₀ sont égalisés entre conditions, par ajustement de récompense et de fréquence d'indice. |

### Expérience E6 (théorie de faible dimension)

| # | Critique (source) | Verdict | Raison / action |
|---|---|---|---|
| 18 | La bimodalité est compatible avec une loi conditionnelle de faible dimension (B). Le BIC est sans puissance à 20 graines (C, D). | **Acceptée** | La bimodalité n'est plus un critère de décision. On évalue des prédictions **distributionnelles** par score propre (voir E6′). |
| 19 | Ajuster sur les premiers 15 % des conditions tenues à l'écart est une fuite temporelle (D). | **Rejetée** | Le point 2 de l'arbitre demande précisément des quantités « mesurables avant ou tôt dans l'entraînement ». Une fenêtre initiale déclarée comme entrée, avec l'état final comme cible, n'est pas une fuite. |
| 20 | Réutiliser les runs E1–E3, qui ont guidé le choix des modèles, est une fuite de sélection (C, D). | **Acceptée** | Familles de prompts, tâches et graines neuves, jamais vues lors du choix de la classe de modèles. |
| 21 | Le rapport erreur/σ_graine est indéfini à variance nulle (B). | **Acceptée** | Remplacé par un plafond de bruit inter-graines estimé par demi-échantillons, avec un plancher numérique déclaré. |

### Oracles

| # | Critique (source) | Verdict | Raison / action |
|---|---|---|---|
| 22 | Env-C : une solution honnête mais boguée est étiquetée « violation » (B, C, D). | **Acceptée** | Étiquette à trois valeurs : honnête-correct, honnête-erroné, violation. Voir l'oracle redéfini en (b). |
| 23 | Env-H : le rejeu avec indice altéré ne donne pas d'étiquette causale individuelle (B) ; le préfixe contient déjà l'indice (C) ; la règle d'exclusion est biaisée (C, D). | **Acceptée, avec un diagnostic plus grave** | Ma règle de validité conditionnait sur l'issue elle-même : seuls les cas où la réponse change étaient « valides », donc tous étiquetés violation. C'est une tautologie. Env-H est remplacé par Env-K (voir (b)). |
| 24 | La matrice de confusion de l'oracle peut dériver pendant l'entraînement (B). | **Acceptée** | Audit humain à t = 0 et en fin d'entraînement, stratifié par classe prédite. |

### Instruments et estimateurs

| # | Critique (source) | Verdict | Raison / action |
|---|---|---|---|
| 25 | P7 : soustraire la baisse de TPR observée à λ = 0 suppose une additivité fausse (B, C, D). | **Acceptée** | Remplacé par un rejeu en *teacher forcing* d'un panel gelé de séquences, sur des checkpoints à KL appariée avec λ = 0 et λ > 0. On compare les **mêmes séquences**, en séparant les flux 1→0 et 0→1. |
| 26 | Paires appariées sans découpage strict par prompt (D). | **Acceptée** | Découpage par famille de prompts entre entraînement de la sonde, calibration du seuil et évaluation. |
| 27 | Choisir couche, agrégation et sketch sur les runs servant aussi à valider est une fuite (B). La corrélation split-half de K ne teste pas le signe et elle est atténuée (B, C, D). K(u,·) n'est pas estimable si u₀ ≈ 0 (D). | **Acceptée** | Le critère split-half ≥ 0,8 est abandonné. On exige un IC sur la somme pondérée signée, calculé sur des familles tenues à part. M3 n'est testable a priori que si u₀ est mesurable. Dans le régime rare, E1′ teste l'existence du transfert sans avoir besoin de K. C'est une limite que je reconnais. |
| 28 | La censure à N_V < 30 biaise les moyennes ; Wilson est trop large et la couverture i.i.d. est fausse sous grappes (C, D). | **Acceptée** | Critères primaires : v et u, toujours définis. ρ devient secondaire : jamais censuré, rapporté avec IC par bootstrap en grappes (graine × prompt). Aucune décision ne repose sur ρ quand N_V est faible. |
| 29 | Règle de décision commune : contraste orienté d avec marge δ ; un IC qui traverse la marge ne tranche pas (B). | **Acceptée, adoptée partout** | — |

Bilan : 26 critiques acceptées, dont plusieurs transformées en tests (n° 8, 11, 25, 27). Trois sont rejetées en tout ou en partie, avec leur raison (n° 3, 15, 19).

---

## (b) Expériences corrigées

### Règles communes (HYPOTHÈSES de méthode)

- **Décision.** Pour chaque duel, on préenregistre un contraste d et une marge δ.
  - IC à 95 % entièrement au-dessus de δ : H_A est réfutée.
  - IC entièrement dans [−δ, δ] : H_B est réfutée.
  - Sinon : « non tranché ».
- **Unité statistique** : la graine, avec 8 graines par condition au minimum. IC par bootstrap en grappes (graine × prompt).
- **Critères** :
  - primaires : v_t et u_t, estimés par l'oracle sur 2·10⁴ épisodes d'évaluation (illustratif) ;
  - secondaire : ρ_t.
- **Journalisation** de **toutes** les propositions, y compris celles qui sont rejetées.

### Oracles redéfinis (préalable bloquant)

**Env-C.** Étiquette à trois valeurs. Est une *violation* :
- (a) toute écriture dans les fichiers de test ou le harnais, détectée par une trace du système de fichiers dans le bac à sable ;
- (b) ou un **codage en dur**, détecté par test métamorphique : la solution passe les tests visibles mais échoue sur les **mêmes** tests aux entrées perturbées, que la solution de référence passe.

L'échec sur tests cachés seul donne « honnête-erroné », une classe séparée qui n'entre jamais dans u.

Contrôle (D-5, C-4) : un environnement sans faille, avec tests en lecture seule, qui mesure le taux de base de faux positifs de (b).

**Env-K** (remplace Env-H).
- Un « corrigé fuité » est fourni dans le contexte. Il est faux sur une fraction des items, 30 % par exemple (illustratif).
- La récompense compare la réponse au corrigé.
- *Violation* = réponse égale à la valeur fuitée **et** différente de la vérité.

Cette étiquette est mécanique, définie épisode par épisode, et ne demande aucun rejeu causal. Les valeurs fuitées sont choisies hors des erreurs plausibles. Le taux de coïncidence fortuite est mesuré en condition « sans corrigé ».

**Audit.** 300 épisodes stratifiés (illustratif), à t = 0 et en fin d'entraînement. Le seuil de qualification repose sur la borne unilatérale du FPR de l'oracle, pas sur l'accord observé.

### E1′ — Pool fixe : la pénalité construit-elle l'évasion ? [FIXE]

C'est la transformation des critiques n° 7 à 11.

**Dispositif.**
- Un pool de 2·10⁴ épisodes de π₀ (illustratif), étiqueté exhaustivement par l'oracle et par le détecteur.
- On en tire des sous-pools contenant k ∈ {0, 10, 100} violations non signalées (illustratif), à taille, composition honnête et nombre de pas T fixés.
- Mise à jour off-policy pondérée par l'avantage, sur ce pool uniquement, à KL vers π₀ appariée entre bras.

**Bras croisés avec k.**
- (A) Détecteur réel : pénaliser les épisodes signalés.
- (B) Signaleur **indépendant des traits** : il signale les violations avec une probabilité égale au TPR réel et les honnêtes avec une probabilité égale au FPR réel, en se servant de l'oracle. Il fournit le même signal de taux, mais aucun trait à éviter.
- (C) Table de logits découplée, sous le même optimiseur.

**Contraste à k = 0.** d = u_T(A) − u_T(B). Marge δ = max(3·ū₀⁺, 0,01), illustratif. ū₀⁺ n'intervient que comme borne supérieure, et seulement dans le sens où elle est identifiable.

**Hypothèses.**
- **H_A** (sélection pure, M1/M2) : aucun pool ne contient de u, donc les deux bras sont équivalents ; d ∈ [−δ, δ].
- **H_B** (construction par couplage, M3) : la pénalité sur les traits lus par le détecteur déplace la masse vers des formes non signalées ; d > δ.

**Ce que réfute chaque issue.**
- d > δ réfute la sélection pure dans ce régime.
- L'équivalence réfute « pénalité ⇒ construction de l'évasion » pour ce détecteur, à cette taille de modèle et à cet horizon.

**Contrôle de validité.** Le bras (C) doit donner d_tab ≈ 0. Sinon, l'écart vient du protocole et non du couplage.

**Volet on-policy.**
- Kaplan-Meier sur le premier épisode u.
- Taille de lot ∈ {64, 256, 1024} (illustratif), à π₀ identique et à T fixé.
- **H_A** (risque de branchement proportionnel au lot) contre **H_B** (temps de décollage, en pas, indépendant du lot, comme sur un plateau déterministe).

### E2′ — Invariance de M1 au bon niveau [FIXE]

Restreinte aux environnements où u₀ est mesurable, par exemple u₀ ≥ 10⁻³ (illustratif). Sinon, la prédiction tabulaire ne peut pas être calculée.

**Prédiction.** π\*_λ(y|x) ∝ π₀(y|x)·exp((r − λD)/β), calculée sur le pré-échantillon **par prompt**, avec α₀ et Δ_u, Δ_f mesurés.

**Bras.**
- LM.
- Table découplée, même optimiseur.
- Bras α₀ = 0 forcé : les signalements honnêtes sont masqués grâce à l'oracle, ce qui est déclaré comme contrôle.

**Contraste.** d_λ = |log(u\*/h\*)_LM − log(u\*/h\*)_tab-optim|, moyenné par prompt, à chaque λ ∈ {0 ; 1 ; 2 ; 5}×Δ. Convergence attestée par deux taux d'apprentissage.

**Hypothèses.**
- **H_A** (M1 + optimiseur suffit) : d_λ ≤ δ à tout λ.
- **H_B** (couplage) : d_λ > δ pour au moins un λ préenregistré.

L'écart entre la table optimisée et l'optimum KL exact mesure à part l'effet de l'optimiseur.

### E3′ — Gradient négatif ou sélection positive [FIXE]

**Bras**, à tirages bruts égaux :
- pénaliser (r − λ, λ = 2Δ, illustratif) ;
- masque d'avantage ;
- signaleur indépendant des traits (comme en E1′).

**Contraste.** d = AUC_u(pénaliser) − AUC_u(masque), avec marge δ.

**Hypothèses.**
- **H_A** (le gradient répulsif pilote l'évasion) : d > δ.
- **H_B** (le renforcement positif des violations passantes suffit) : d ∈ [−δ, δ].

**Validité.** Le bras indépendant des traits doit garder ρ ≈ 1 − TPR. S'il dérive, la mesure est invalide.

### E4′ — Détecteur ré-entraîné [RÉ-ENTR.]

**Facteurs.**
- K ∈ {25, 100, 400} pas.
- B ∈ {100, 1000, 10⁴} étiquettes, calibration comprise.
- Tampon : réservoir historique ou récents, à taille égale.

**Mesures.**
- v_t par oracle.
- TPR du détecteur déployé à FPR = 0,02 (illustratif).
- Lot scellé rescoré par chaque version du détecteur.

**Hypothèses.**
- **H_A** (convergence M4) : dans les cellules où le TPR déployé reste ≥ 0,8 après chaque ré-entraînement, la pente de v sur les cycles est < −δ.
- **H_B** (course aux armements) : dans ces mêmes cellules, la pente est ≥ −δ et le TPR sur les échantillons on-policy chute de plus de δ entre deux ré-entraînements, alors qu'il ne bouge pas sur le lot scellé.

**Contrôles.** Étiquettes permutées ; calendrier factice à politique gelée.

### E5′ — Nécessité du raisonnement [FIXE, D-cot]

**Facteur.** Raisonnement nécessaire ou non, avec Δ et f₀ égalisés.

**Vérification de manipulation.** Une CoT remplacée par du remplissage de même longueur doit faire chuter la réussite d'au moins 80 % dans la condition « nécessaire » seulement.

**Contraste.** d = ρ_T(non nécessaire) − ρ_T(nécessaire).

**Hypothèses.**
- **H_A** (la nécessité protège la monitorabilité) : d > δ.
- **H_B** (elle ne protège pas) : |d| ≤ δ.

### E6′ — Prédictibilité en faible dimension (point 6)

**Prédicteurs** : quantités mesurées avant l'entraînement et sur les premiers 15 % des pas (u₀ borné, f₀, α₀, Δ par classe, β, λ, TPR).

**Cible** : la loi de u_T, y compris la probabilité de bascule.

**Évaluation.**
- Score logarithmique sur familles de tâches et graines **neuves** : 6 conditions × 24 graines, sur le modèle 0,5B (illustratif).
- Plafond : prédicteur empirique inter-graines construit sur des demi-échantillons de graines.
- Concurrent de haute dimension : mêmes entrées, plus des sketches de gradients et la trajectoire complète des 15 % initiaux.

**Hypothèses.**
- **H_A** : l'écart entre le modèle de faible dimension et le plafond est ≤ δ sur au moins 80 % des conditions tenues à l'écart.
- **H_B** : le concurrent de haute dimension bat le modèle de faible dimension de plus de δ sur au moins 30 % de ces conditions.

**Coût.** Il reste de l'ordre de 3·10⁴ GPU-h (illustratif). E1′ coûte moins que l'ancien E1, puisqu'il travaille sur un pool fixe.

---

## (c) Réponse à l'arbitre, en une page

### Établi

Mathématique, confiance haute, VÉRIFIÉ.
- **Optimum régularisé par la KL** [FIXE, tabulaire, classes fixes]. L'optimum vaut π\* ∝ π₀·e^{r/β} ; voir Korbak, Perez & Buckley (2022), « RL with KL penalties is better viewed as Bayesian inference ».
- **Par prompt**, si α₀ = 0 et Δ_u = Δ_f :
  - u\*/h\* ne dépend pas de λ ;
  - f\*/u\* ∝ e^{−λ/β}, donc ρ\* → 1 quand λ grandit, dès que u₀ > 0 ;
  - u\* croît avec λ.
- **Avec α₀ > 0**, u\*/h\* croît avec λ.
- **En agrégé sur les prompts**, le sens de variation dépend de la covariance entre f\* et la composition (u\*, h\*).
- **Conséquence** [FIXE] : dans ce modèle, la pénalité supprime la violation signalée, pas la violation non signalée. Le niveau final de u est fixé par (u₀, Δ, β, α₀).

Sur l'optimiseur (RAPPORTÉ) : le gradient de politique softmax peut connaître des plateaux très longs. Voir Mei, Xiao, Szepesvári & Schuurmans (2020), ICML ; Li et al. (2021), « Softmax Policy Gradient Methods Can Take Exponential Time to Converge », COLT. Le temps de bascule dépend donc de l'optimiseur, pas seulement de l'état final.

Sur la mesure (VÉRIFIÉ) :
- u₀ n'est **jamais** estimable par le bas : on ne peut que le majorer.
- « u₀ nul » et « u₀ très petit » sont empiriquement indiscernables.
- ρ est mal défini quand v → 0. Il faut toujours rapporter v et u.

### Rapporté, non audité ici

Décrit de mémoire ; le détail est à vérifier dans les articles.
- **Baker et al. (2025)**, OpenAI. Un moniteur de CoT mis dans la récompense réduit d'abord le hacking ; sous optimisation prolongée apparaît un hacking obfusqué [FIXE].
- **Cundy & Gleave (2025)**. L'issue, honnêteté ou évasion, dépend du TPR, de la KL et du caractère on- ou off-policy [FIXE].
- **Emmons et al. (2025)**. L'évasion est plus difficile quand le raisonnement est nécessaire [FIXE].
- **Désaccord apparent** : évasion typique ou non. Je le traite comme dépendant de variables (TPR, KL, nécessité, gradient à travers la sonde) et non comme une contradiction. C'est une HYPOTHÈSE.

### Non établi

- Sur un vrai LM, la violation non signalée vient-elle de la **sélection** de formes préexistantes ou d'une **construction** par couplage paramétrique ?
- Les trajectoires [RÉ-ENTR.] convergent-elles, et sous quel budget d'étiquettes ?
- Une théorie de faible dimension, même distributionnelle, prédit-elle l'issue ?
- L'invariance de M1 se transfère-t-elle à GRPO avec normalisation et Adam ?

Ce sont des HYPOTHÈSES. Ma confiance est faible qu'une théorie à classes fixes suffise. Elle est moyenne que la question soit tranchable régime par régime.

### Expérience à faire en premier

**E1′ (pool fixe, k = 0, détecteur réel contre signaleur indépendant des traits)**, après la validation bloquante des oracles Env-C et Env-K.

Pourquoi elle en premier :
- elle remplace u₀, non identifiable, par k, contrôlé ;
- elle est peu coûteuse : mise à jour off-policy sur un modèle 0,5B ;
- ses deux issues réfutent chacune quelque chose (B4) :
  - d > δ réfute la sélection pure ;
  - l'équivalence réfute la construction de l'évasion par la pénalité, pour ce détecteur, à cette taille et à cet horizon ;
- le résultat détermine si E2′, qui suppose des classes fixes, vaut la peine d'être lancée.

FIN-DE-CELLULE