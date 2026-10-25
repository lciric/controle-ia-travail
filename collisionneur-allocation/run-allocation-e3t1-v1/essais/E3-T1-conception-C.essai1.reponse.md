# Proposition C — Allocation séquentielle d'un budget de calcul entre sélection de classe d'hypothèses et optimisation paramétrique

Conformément au protocole v2 (Règle 2), il est constaté que le bloc `FAITS` ne contient aucune donnée empirique (« Aucun fait n’est joint », statut : VÉRIFIÉ). L'intégralité de la présente contribution repose donc sur des constructions formelles et des propositions expérimentales (statut : HYPOTHÈSE) ainsi que sur des résultats théoriques issus de la littérature (statut : RAPPORTÉ). 

Le présent livrable fusionne les exigences structurelles du Tour III.1 — (a) présupposés, (b) duels d'inférence forte $H_A$ contre $H_B$, (c) métrologie des instruments, (d) ancrage matériel — et les cinq axes mathématiques posés par l'arbitre.

---

## (a) Ce que la question suppose sans que ce soit établi

L'énoncé du problème repose sur six présupposés implicites dont la validité conditionne l'existence même d'une politique de décision non triviale :

1. **Extrapolabilité locale des courbes d'apprentissage** (Statut : HYPOTHÈSE). La question suppose que l'observation de la perte de validation $L_k(b)$ pour un budget dépensé $b \le b_0$ contient une information prédictive sur $L_k(b + \Delta b)$. Or, en présence de phénomènes de descente double (*double descent* en fonction du temps d'entraînement) ou de transitions de phase retardées (*grokking*), la dérivée locale $\partial L_k / \partial b$ peut être nulle pendant une longue période avant une chute brusque.
2. **Coût d'observation négligeable ou inclus** (Statut : HYPOTHÈSE). L'énoncé définit $B$ comme un nombre d'évaluations de la perte sur des données dont la vérité est connue, et donne accès à $L_k(b)$, sa variance $\hat{\sigma}_k^2(b)$, et une mesure de dérive $\hat{D}_t$. Il est supposé que le calcul de ces statistiques (notamment sur l'ensemble de validation) ne consomme pas une fraction prohibitive du budget $B$ alloué à l'ajustement de $\theta$, ou que ce coût est formellement soustrait de $B$.
3. **Invariance de l'ordre d'efficacité des classes ou sensibilité détectable à la dérive** (Statut : HYPOTHÈSE). L'introduction d'une mesure d'écart distributionnel $\hat{D}_t$ entre données récentes et passées suppose qu'un changement de la distribution sous-jacente $\mathcal{D}_t$ affecte différemment l'erreur d'approximation des classes $\mathcal{H}_k$ et $\mathcal{H}_j$, justifiant une bascule (action $S$) plutôt qu'un simple ré-ajustement des paramètres $\theta$ dans la classe courante (action $A$).
4. **Existence d'un transfert partiel mesurable** (Statut : HYPOTHÈSE). L'énoncé mentionne que l'action (S) « remet l'ajustement à son début (ou n'en garde qu'une partie) ». Si une partie est conservée (par exemple via un morphisme de réseau ou une distillation sur un budget résiduel), cela suppose que l'état initial $\theta_j(0)$ dans $\mathcal{H}_j$ dépend de $\theta_k(b)$, violant l'hypothèse d'indépendance des bras dans les formulations classiques de bandits.
5. **Bruit de validation homoscédastique ou à variance estimable sans biais** (Statut : HYPOTHÈSE). Utiliser une estimation de variance $\hat{\sigma}_k^2(b)$ pour guider l'arrêt suppose que la dépendance temporelle des itérations (gradients stochastiques corrélés) ne biaise pas dramatiquement l'estimateur de variance empirique.
6. **Décorrélation entre la géométrie à court terme et l'asymptote** (Statut : HYPOTHÈSE). Si la classe qui décroît le plus vite au début ($b \ll B$) était toujours celle qui atteint le meilleur minimum asymptotique ($b \to B$), un algorithme glouton trivial suffirait. Le problème suppose une tension entre vitesse initiale (biais inductif fort) et capacité asymptotique (biais inductif faible).

---

## (b) Formalisation, statistiques, découpage du budget et généralisation (Axes 1 à 5)

### 1. Formalisation mathématique : le choix entre (A) et (S)

Le problème diffère d'un bandit manchot classique car les récompenses sont non stationnaires (les pertes décroissent avec $b$), l'horizon $B$ est fini, l'objectif est le minimum final (regret simple à l'horizon $B$ plutôt que regret cumulé), et le changement de bras engendre un coût de bascule $c > 0$. Nous proposons deux formalisations concurrentes (Statut : HYPOTHÈSE).

#### Voie 1.1 : Processus de Décision Markovien à Horizon Fini sur État Augmenté (MDP d'arrêt et de bascule)
Soit $\mathcal{K} = \{1, \dots, K\}$ l'ensemble des classes d'hypothèses. À l'étape $t$, l'état du système est représenté par le n-uplet :
$$s_t = \left( k_t, \, b_{k_t}, \, \mathcal{F}_t, \, B_{\text{rem}}(t), \, \hat{D}_t \right)$$
où $k_t \in \mathcal{K}$ est la classe active, $b_{k_t}$ le budget investi dans $\mathcal{H}_{k_t}$ depuis la dernière bascule, $\mathcal{F}_t = \{(b, L_j(b), \hat{\sigma}_j^2(b))\}_{j, b}$ l'historique des observations, $B_{\text{rem}}(t)$ le budget restant, et $\hat{D}_t$ la mesure de dérive distributionnelle.
*   **Action $A$ (Ajuster)** : pour un pas de budget $\Delta b$, $B_{\text{rem}}(t+1) = B_{\text{rem}}(t) - \Delta b$, $b_{k_t} \leftarrow b_{k_t} + \Delta b$.
*   **Action $S(j)$ (Basculer vers $j \neq k_t$)** : $B_{\text{rem}}(t+1) = B_{\text{rem}}(t) - c - \Delta b$, $k_{t+1} = j$, et $b_j \leftarrow \alpha_{k_t \to j} b_{k_t} + \Delta b$, où $\alpha_{k \to j} \in [0, 1]$ modélise la fraction de l'apprentissage conservée (distillation ou réutilisation de poids ; $\alpha = 0$ pour une réinitialisation totale).

**Critère calculable n°1 : Valeur d'Information Myope sous Loi d'Échelle Paramétrique (VIM-LEP)** (Statut : HYPOTHÈSE).
*   *Hypothèses* : On suppose que la perte attendue dans $\mathcal{H}_k$ suit une loi de puissance bruitée décalée par la dérive :
    $$L_k(b) = L_k^\infty + \beta_k b^{-\gamma_k} + \lambda_k \hat{D}_t + \epsilon_k(b), \quad \epsilon_k(b) \sim \mathcal{N}(0, \sigma_k^2(b))$$
    avec une loi a priori conjuguée ou normale-log-normale sur $\psi_k = (L_k^\infty, \beta_k, \gamma_k, \lambda_k) \sim p_0(\psi)$.
*   *Formule du critère* : À partir de $\mathcal{F}_t$, on calcule la distribution a posteriori $p(\psi_k \mid \mathcal{F}_t)$. La perte finale projetée si l'on consacre tout le budget restant à la classe courante $k$ est la variable aléatoire $\tilde{L}_k^{\text{fin}} = L_k(b_k + B_{\text{rem}})$. Si l'on bascule vers $j$, le budget disponible pour $j$ est $B_{\text{rem}} - c$, donnant la projection $\tilde{L}_j^{\text{fin}} = L_j(\alpha_{k \to j} b_k + B_{\text{rem}} - c)$. Le critère VIM-LEP commande de basculer vers $j^*$ si et seulement si :
    $$\min_{j \neq k} \mathbb{E}\left[ \tilde{L}_j^{\text{fin}} \mid \mathcal{F}_t \right] - \kappa \sqrt{\mathbb{V}\text{ar}\left(\tilde{L}_j^{\text{fin}} \mid \mathcal{F}_t\right)} < \mathbb{E}\left[ \tilde{L}_k^{\text{fin}} \mid \mathcal{F}_t \right] - \zeta(c, B_{\text{rem}})$$
    où $\kappa > 0$ est un paramètre d'exploration (type borne inférieure de confiance, LCB) et $\zeta(c, B_{\text{rem}})$ est une pénalité d'hystérésis empêchant les oscillations lorsque $B_{\text{rem}} \to c$.
*   *Ce que ce critère ignore* : Il ignore la possibilité de bascules multiples futures (horizon myope à une seule bascule restante), fait l'hypothèse forte d'une décroissance monotone en loi de puissance (fausse en cas de *grokking* ou de plateaux de points selles), et ignore la corrélation inter-classes (apprendre que $\mathcal{H}_k$ stagne ne met pas à jour $p(\psi_j)$ si les priors sont indépendants).

#### Voie 1.2 : Bandits à Bras Rallongés (Rising/Rotting Bandits) avec Coût de Bascule et Indice de Gittins Approché
Si l'on ne veut pas supposer de forme paramétrique globale pour $L_k(b)$, on modélise chaque classe comme un processus semi-martingale dont les incréments $\Delta L_k(b) = L_k(b + \Delta b) - L_k(b)$ ont une espérance conditionnelle bornée.
*   **Critère calculable n°2 : Indice de Rétro-projection Locale Corrigé de la Dérive (IRL-CD)** (Statut : HYPOTHÈSE).
    On estime la pente locale par régression linéaire pondérée sur les $w$ derniers pas de budget dans $\mathcal{H}_k$ : $\hat{g}_k(b_k) = \frac{\partial \hat{L}_k}{\partial b}(b_k) \le 0$. On définit l'indice de performance conservateur à horizon $h = \min(\tau, B_{\text{rem}})$ :
    $$I_k(b_k, h) = \hat{L}_k(b_k) + \hat{g}_k(b_k) \cdot \phi(h) + \hat{\lambda}_k \hat{D}_t - \sqrt{\frac{2 \hat{\sigma}_k^2(b_k) \ln(1/\delta)}{w}}$$
    où $\phi(h) = \frac{1 - e^{-\eta h}}{\eta}$ est une fonction d'amortissement concave (supposant que le gain marginal décroît exponentiellement au taux $\eta$). Pour une classe $j$ non active, l'horizon effectif est $h - c$. On bascule si $\min_{j \neq k} I_j(b_j, h - c) < I_k(b_k, h)$.
*   *Ce que ce critère ignore* : L'amortissement $\eta$ est arbitraire ; le critère est aveugle au plancher irréductible (erreur d'approximation de la classe $\inf_{\theta \in \mathcal{H}_k} L(\theta)$) tant que la pente locale $\hat{g}_k$ reste négative.

---

### 2. Statistiques observables, coûts d'obtention et correction des biais

#### Statistiques et leurs coûts
1. **Perte empirique de validation $\hat{L}_k(b)$ et sa variance $\hat{\sigma}_k^2(b)$** : Calculées sur un échantillon de validation $S_{\text{val}}$ de taille $n_{\text{val}}$. Si le budget $B$ compte le nombre total d'évaluations de la perte (entraînement + validation), chaque prise de décision à une fréquence $f_{\text{eval}}$ coûte $n_{\text{val}}$ unités de budget. Un suivi trop fin ($f_{\text{eval}}$ élevé) ampute le budget d'ajustement de $\theta$ de $N_{\text{checks}} \times n_{\text{val}}$ (Statut : VÉRIFIÉ mathématiquement par conservation de $B$).
2. **Mesure de dérive $\hat{D}_t$** : Estimée entre une fenêtre glissante passée $W_{\text{past}}$ et une fenêtre récente $W_{\text{rec}}$ de taille $m$. On peut utiliser la divergence maximale moyenne (MMD, *Maximum Mean Discrepancy*) à noyau caractéristique, ou une distance de Wasserstein tranchée (*Sliced Wasserstein*) sur les représentations intermédiaires ou les entrées. Coût : $\mathcal{O}(m^2)$ opérations pour la MMD quadratique, ou $\mathcal{O}(m \log m)$ pour Wasserstein tranchée (Statut : RAPPORTÉ — *référence à vérifier* : Gretton et al., 2012, *A Kernel Two-Sample Test*).

#### Biais rédhibitoires
*   **Sur-ajustement de l'ensemble de validation par sélection adaptative** : Interroger $S_{\text{val}}$ à $T$ reprises pour choisir entre $K$ classes fait croître l'écart entre la perte sur $S_{\text{val}}$ et la vraie perte généralisée en $\mathcal{O}(\sqrt{\frac{\ln(K \cdot T)}{n_{\text{val}}}})$ sous hypothèse d'indépendance, mais jusqu'à $\mathcal{O}(\sqrt{\frac{T}{n_{\text{val}}}})$ si les décisions successives s'adaptent aux réalisations du bruit sur $S_{\text{val}}$ (Statut : RAPPORTÉ — *référence à vérifier* : Dwork et al., 2015, *The Reusable Holdout: Preserving Validity in Adaptive Data Analysis*).
*   **Biais du gagnant (Malédiction de l'optimiseur)** : La classe $j^* = \arg\min_j \hat{L}_j(b)$ présente une perte biaisée négativement : $\mathbb{E}[\min_j \hat{L}_j] \le \min_j \mathbb{E}[\hat{L}_j]$. Ce biais est maximal lorsque les variances $\hat{\sigma}_j^2(b)$ sont hétérogènes : une classe très bruitée a plus de chances de franchir accidentellement le seuil de bascule.
*   **Autocorrélation du bruit des courbes** : $\hat{L}_k(b)$ et $\hat{L}_k(b + \Delta b)$ sont évaluées sur le *même* ensemble $S_{\text{val}}$ avec des paramètres $\theta(b)$ et $\theta(b+\Delta b)$ proches. La variance de la différence $\mathbb{V}\text{ar}(\hat{L}_k(b+\Delta b) - \hat{L}_k(b))$ est beaucoup plus faible que $2\hat{\sigma}_k^2(b)$, mais l'erreur systématique due à l'échantillonnage fini de $S_{\text{val}}$ reste constante, créant un « plancher fantôme ».
*   **Confusion entre non-stationnarité des données ($\hat{D}_t > 0$) et stagnation de l'optimiseur** : Si la distribution cible change, $\hat{L}_k(b)$ peut augmenter ($\partial \hat{L}_k / \partial b > 0$). Sans décomposition, le décideur attribue cette hausse à un sur-apprentissage de la classe $\mathcal{H}_k$ et déclenche une bascule coûteuse $S$, alors qu'une simple continuation $A$ avec un taux d'apprentissage réchauffé suffirait.

#### Protocoles de correction (Statut : HYPOTHÈSE et RAPPORTÉ)
1. **Mécanisme de Seuil Réutilisable (*Reusable Holdout* / *Thresholdout*)** : On divise la validation en $S_{\text{val}}^{(1)}$ (public, utilisé pour estimer les pentes) et $S_{\text{val}}^{(2)}$ (tenu à l'écart derrière un oracle différentiellement privé). La décision de bascule proposée par $S_{\text{val}}^{(1)}$ n'est exécutée que si l'écart de performance sur $S_{\text{val}}^{(2)}$, bruîté par un bruit de Laplace d'échelle $\tau$, dépasse un seuil franc. Cela réduit la dépendance en $T$ de linéaire à logarithmique (Statut : RAPPORTÉ — Dwork et al., 2015, *référence à vérifier*).
2. **Séquences de Confiance Uniformément Valides dans le Temps (*Time-Uniform Confidence Sequences*)** : Au lieu d'intervalles de confiance ponctuels à niveau $1-\delta$, on construit une enveloppe martingalienne par la méthode du mélange (*method of mixtures* ou bornes de type Howard-Ramdas) qui garantit :
   $$\mathbb{P}\left(\forall t \ge 1, \, \forall k \in \mathcal{K}, \, \left| \hat{L}_k(b_t) - L_k(b_t) \right| \le \mathcal{B}_k(t, \delta) \right) \ge 1 - \delta$$
   avec $\mathcal{B}_k(t, \delta) \propto \hat{\sigma}_k(b_t) \sqrt{\frac{\ln(\ln(t) K / \delta)}{n_{\text{val}}}}$ (Statut : RAPPORTÉ — *référence à vérifier* : Howard et al., 2021, *Time-uniform, nonparametric, nonasymptotic confidence sequences*).
3. **Correction de dérive par Découplage d'Ancre** : Pour séparer la dérive $\hat{D}_t$ du progrès d'optimisation, on maintient un tampon figé de données anciennes $S_{\text{old}}$ et un tampon récent $S_{\text{new}}$. La vraie pente d'optimisation à distribution constante est $\Delta_{\text{opt}} = \hat{L}_k(b+\Delta b; S_{\text{new}}) - \hat{L}_k(b; S_{\text{new}})$, tandis que le choc de dérive est $\Delta_{\text{drift}} = \hat{L}_k(b; S_{\text{new}}) - \hat{L}_k(b; S_{\text{old}})$ (Statut : HYPOTHÈSE).

---

### 3. Découpage du budget $B$ : Exploration, Exploitation et Réserve de Bascule

Soit la décomposition $B = B_{\text{exp}} + B_{\text{xpl}} + B_{\text{res}}$, où $B_{\text{exp}}$ est alloué au criblage initial des $K$ classes, $B_{\text{xpl}}$ à l'ajustement profond d'une classe retenue, et $B_{\text{res}}$ est une réserve assurantielle activée uniquement si une dérive $\hat{D}_t$ ou un plateau prématuré survient.

#### Option 3.1 : Allocation Statique par Règle de Racine Carrée et Élimination Successive Fixe
*   *Mécanisme* : On fixe $B_{\text{res}} = \rho B$ (par exemple $\rho = 0{,}15$, chiffre illustratif). Sur le budget restant $(1-\rho)B$, on alloue $B_{\text{exp}}$ à un tournoi de type *Successive Halving* (élimination par paliers géométriques) qui paie le coût d'initialisation de $K$ classes et élimine la moitié des classes à chaque doublement du budget local, jusqu'à n'en garder qu'une seule qui reçoit $B_{\text{xpl}}$ (Statut : RAPPORTÉ — *référence à vérifier* : Jamieson et Talwalkar, 2016, *Non-stochastic Best Arm Identification and Hyperparameter Optimization*).
*   *Bornes et Regret* : Si les courbes ne se croisent plus après un budget critique $b^*$, et si $B_{\text{exp}} \ge K b^* \log_2 K$, la meilleure classe est identifiée. Cependant, si aucune dérive n'a lieu ($\hat{D}_t \equiv 0$), la réserve $B_{\text{res}}$ est soit gaspillée, soit déversée trop tardivement en fin d'entraînement. Le regret simple (écart à la perte optimale à budget $B$) est minoré par $\Omega\left(\left|\frac{\partial L_{k^*}}{\partial b}(B)\right| \cdot (B_{\text{exp}} + B_{\text{res}})\right)$ en environnement stationnaire (Statut : HYPOTHÈSE).

#### Option 3.2 : Allocation Dynamique à Enveloppe de Réserve Décroissante (ADERD)
*   *Mécanisme* (Statut : HYPOTHÈSE) : Aucune frontière rigide n'est fixée d'avance entre exploration et exploitation. On définit une **condition de viabilité de bascule** : changer de classe à l'instant où il reste $B_{\text{rem}}$ n'a de sens que si le budget résiduel après paiement du coût fixe $c$ permet à la nouvelle classe $j$ de dépasser le niveau actuel de la classe $k$. Soit $b_{\text{min}}(j, L_k(b_k))$ le budget minimal estimé pour que $\mathcal{H}_j$ atteigne la perte actuelle $L_k(b_k)$. La réserve implicite requise est :
    $$B_{\text{req}}(t) = c + \min_{j \neq k} b_{\text{min}}(j, L_k(b_k))$$
    Tant que $B_{\text{rem}}(t) > B_{\text{req}}(t)$, la bascule est autorisée (phase mixte exploration/exploitation guidée par les critères VIM-LEP ou IRL-CD). Dès que $B_{\text{rem}}(t) \le B_{\text{req}}(t)$ (le « point de non-retour »), l'action $S$ est bannie de l'espace d'actions, et la totalité de $B_{\text{rem}}(t)$ est engagée dans l'exploitation pure ($A$) de la classe courante, *sauf* si la dérive $\hat{D}_t$ détruit la performance actuelle (faisant remonter $L_k(b_k)$ et abaissant du même coup $b_{\text{min}}(j, L_k(b_k))$).
*   *Comparaison des pertes attendues* :
    *   En régime stationnaire à courbes régulières : l'allocation statique par élimination successive domine car elle parallélise et borne strictement le coût des mauvais bras à $\mathcal{O}(K \log K)$.
    *   En régime non stationnaire ($\hat{D}_t$ stochastique) ou à croisements tardifs : l'allocation adaptative ADERD évite de payer une réserve morte $\rho B$ quand tout va bien, tout en conservant la faculté de basculer si un choc de distribution invalide la classe en tête avant le point de non-retour.

---

### 4. Généralisation à des familles de tâches nouvelles (Méta-niveau)

Supposons maintenant que la politique d'allocation $\pi$ (ou le choix d'une classe dominante $\mathcal{H}_k$) soit apprise sur $N$ familles de tâches d'entraînement $\mathcal{T}_1, \dots, \mathcal{T}_N$ tirées i.i.d. selon une méta-distribution $\mathfrak{E}$, et qu'on veuille borner sa perte attendue sur une nouvelle famille $\mathcal{T}_{\text{new}} \sim \mathfrak{E}$.

#### Bornes théoriques de méta-généralisation
1. **Approche PAC-Bayésienne Hiérarchique sur les Politiques / Classes** (Statut : RAPPORTÉ — *référence à vérifier* : Amit et Meir, 2018, *Meta-Learning by Adjusting Priors Based on Extended PAC-Bayes Theory* ; Rothfuss et al., 2021, *PACOH: Bayes-Optimal Meta-Learning with PAC-Guarantees*).
   Soit $\mathcal{P}$ une distribution a priori (méta-prior) sur l'espace des classes $\mathcal{K}$ (et des hyperparamètres de la règle de décision), et $\mathcal{Q}$ la distribution a posteriori choisie après observation des $N$ familles de tâches (chacune disposant de $n_{\text{val}}$ exemples de validation). Si les pertes sont bornées dans $[0, 1]$, alors avec probabilité au moins $1 - \delta$ sur le tirage des $N$ familles :
   $$\mathbb{E}_{\mathcal{T} \sim \mathfrak{E}} \mathbb{E}_{k \sim \mathcal{Q}} [L_{\mathcal{T}}(k)] \le \frac{1}{N} \sum_{i=1}^N \mathbb{E}_{k \sim \mathcal{Q}} [\hat{L}_{\mathcal{T}_i}(k)] + \sqrt{\frac{\text{KL}(\mathcal{Q} \,\|\, \mathcal{P}) + \ln\frac{2\sqrt{N}}{\delta}}{2N}} + \sqrt{\frac{\text{KL}(\mathcal{Q} \,\|\, \mathcal{P}) + \ln\frac{2 N \sqrt{n_{\text{val}}}}{\delta}}{2 N n_{\text{val}}}}$$
   *Implication cruciale* : Le premier terme de pénalité décroît en $1/\sqrt{N}$ (nombre de *familles* de tâches) et ne peut **jamais** être réduit en augmentant le budget $B$ ou la taille d'échantillon $n_{\text{val}}$ au sein des familles connues. Si $K$ est très grand et que l'on choisit une classe déterministe ($\mathcal{Q}$ est une masse de Dirac) à partir d'un prior uniforme $\mathcal{P}$, $\text{KL}(\mathcal{Q} \,\|\, \mathcal{P}) = \ln K$, ce qui exige $N \gg \ln K$.
2. **Stabilité Algorithmique Uniforme au Méta-Niveau** (Statut : RAPPORTÉ — *référence à vérifier* : Bousquet et Elisseeff, 2002, *Stability and Generalization* ; adapté au méta-apprentissage par Maurer, 2005, *Algorithmic Stability and Meta-Learning*, *référence à vérifier*).
   Si le remplacement d'une famille de tâches $\mathcal{T}_i$ par une famille indépendante $\mathcal{T}_i'$ modifie la probabilité de sélectionner la classe $k$ d'au plus $\beta_{\text{meta}}$ (stabilité en variation totale de la politique d'allocation), alors le biais de généralisation inter-familles est borné en espérance par $\beta_{\text{meta}}$. Pour garantir un $\beta_{\text{meta}}$ faible en $\mathcal{O}(1/N)$, la règle de sélection de classe doit être régularisée (par exemple via un *softmax* de température $\tau^{-1}$ sur les pertes cumulées des familles plutôt qu'un $\arg\min$ brutal).

#### Distinguer la généralisation structurelle de la mémorisation des familles vues
Un méta-algorithme peut atteindre une perte faible sur les familles d'entraînement en mémorisant une table de correspondance implicite : il utilise les premières évaluations de budget ($b \ll B$) non pas pour mesurer la vitesse d'apprentissage intrinsèque de $\mathcal{H}_k$, mais comme une **empreinte digitale** (*task fingerprinting*) permettant de reconnaître le numéro de la famille $\mathcal{T}_i \in \{1, \dots, N\}$ et de charger la classe pré-enregistrée correspondante (Statut : HYPOTHÈSE — analogue au problème de mémorisation en méta-apprentissage identifié par Yin et al., 2020, *Meta-Learning without Memorization*, *référence à vérifier*).

**Protocole de falsification de la mémorisation (Méta-invariance par brouillage d'empreinte)** (Statut : HYPOTHÈSE) :
1. **Familles tenues à l'écart sous décalage de covariables spectrales** : On évalue la politique sur des familles $\mathcal{T}_{\text{out}}$ partageant la même structure causale (même classe optimale $k^*$), mais dont les marginales d'entrée subissent une transformation orthogonale ou un ré-étalonnage de norme des pertes initiales ($L_k(0) \leftarrow a L_k(0) + d$, avec $a > 0$). Si la politique s'effondre alors que l'ordre des pentes relatives est préservé, elle mémorisait l'échelle absolue des pertes initiales des familles vues.
2. **Test d'Information Mutuelle sur la Trajectoire Précoce** : On mesure l'information mutuelle $I(\mathcal{F}_{t_0} ; \text{ID}(\mathcal{T}))$ entre les observations précoces de la courbe et l'identifiant de la famille, conditionnellement à la classe optimale $k^*$ : $I(\mathcal{F}_{t_0} ; \text{ID}(\mathcal{T}) \mid k^*)$. Une généralisation pure requiert que la décision $k_t$ vérifie $I(k_t ; \text{ID}(\mathcal{T}) \mid k^*) \approx 0$.

---

### 5. Ce qui est connu : Références bibliographiques consolidées

Conformément à la Règle 3, toutes les références ci-dessous portent un statut RAPPORTÉ et la mention explicite « référence à vérifier », sans identifiant arXiv :

*   **Allocation de budget, bandits non stationnaires et optimisation d'hyperparamètres** :
    *   Jamieson, K., & Talwalkar, A. (2016). *Non-stochastic Best Arm Identification and Hyperparameter Optimization*. Proceedings of Machine Learning Research (AISTATS) — **référence à vérifier**.
    *   Li, L., Jamieson, K., DeSalvo, G., Rostamizadeh, A., & Talwalkar, A. (2018). *Hyperband: A Novel Bandit-Based Approach to Hyperparameter Optimization*. Journal of Machine Learning Research — **référence à vérifier**.
    *   Heidari, H., Kearns, M., & Roth, A. (2016). *Tight Policy Regret Bounds for Improving and Decaying Bandits*. Proceedings of the International Joint Conference on Artificial Intelligence (IJCAI) — **référence à vérifier**.
    *   Levine, N., Crammer, K., & Mannor, S. (2017). *Rotting Bandits*. Advances in Neural Information Processing Systems (NeurIPS) — **référence à vérifier**.
*   **Extrapolation des courbes d'apprentissage** :
    *   Domhan, T., Springenberg, J. T., & Hutter, F. (2015). *Speeding Up Automatic Hyperparameter Optimization of Deep Neural Networks by Extrapolation of Learning Curves*. Proceedings of the International Joint Conference on Artificial Intelligence (IJCAI) — **référence à vérifier**.
    *   Swersky, K., Snoek, J., & Adams, R. P. (2014). *Freeze-Thaw Bayesian Optimization*. Rapport technique / prépublication — **référence à vérifier**.
*   **Analyse de données adaptative, sélection post-hoc et séquences de confiance** :
    *   Dwork, C., Feldman, V., Hardt, M., Pitassi, T., Reingold, O., & Roth, A. (2015). *The Reusable Holdout: Preserving Validity in Adaptive Data Analysis*. Science — **référence à vérifier**.
    *   Howard, S. R., Ramdas, A., McAuliffe, J., & Sekhon, J. (2021). *Time-uniform, nonparametric, nonasymptotic confidence sequences*. The Annals of Statistics — **référence à vérifier**.
*   **Détection de dérive et tests à deux échantillons** :
    *   Gretton, A., Borgwardt, K. M., Rasch, M. J., Schölkopf, B., & Smola, A. (2012). *A Kernel Two-Sample Test*. Journal of Machine Learning Research — **référence à vérifier**.
*   **Méta-apprentissage, PAC-Bayes et mémorisation** :
    *   Bousquet, O., & Elisseeff, A. (2002). *Stability and Generalization*. Journal of Machine Learning Research — **référence à vérifier**.
    *   Maurer, A. (2005). *Algorithmic Stability and Meta-Learning*. Journal of Machine Learning Research — **référence à vérifier**.
    *   Amit, R., & Meir, R. (2018). *Meta-Learning by Adjusting Priors Based on Extended PAC-Bayes Theory*. Proceedings of the International Conference on Machine Learning (ICML) — **référence à vérifier**.
    *   Rothfuss, J., Fortuin, V., Josifoski, M., & Krause, A. (2021). *PACOH: Bayes-Optimal Meta-Learning with PAC-Guarantees*. Proceedings of the International Conference on Machine Learning (ICML) — **référence à vérifier**.
    *   Yin, M., Tucker, G., Zhou, M., Levine, S., & Finn, C. (2020). *Meta-Learning without Memorization*. International Conference on Learning Representations (ICLR) — **référence à vérifier**.

---

## (b-bis) Expériences décisives en inférence forte ($H_A$ contre $H_B$)

Pour départager les voies proposées sans lissage (Règle B4), nous concevons trois expériences cruciales (Statut : HYPOTHÈSE). Tous les seuils numériques sont marqués « illustratif » (Règle 4).

### Duel Expérimental 1 : Extrapolation Paramétrique Bayésienne (VIM-LEP) contre Indice Local Non-Paramétrique (IRL-CD) en présence de croisements de courbes
*   **Contexte** : On oppose $K = 4$ (illustratif) classes d'architectures de capacités croissantes (ex. : linéaire, MLP peu profond, ResNet moyen, Transformer profond) sur un banc d'essai où les petites classes convergent vite vers un plancher haut, et les grandes classes stagnent initialement avant de décroître plus bas (*croisement retardé*). Coût de bascule $c = 0{,}05 B$ (illustratif).
*   **Hypothèse $H_A$ (Supériorité de l'extrapolation globale VIM-LEP)** : La régression bayésienne sur la loi d'échelle $L_k^\infty + \beta_k b^{-\gamma_k}$ détecte la courbure asymptotique dès $b \le 0{,}25 B$ (illustratif) et bascule vers la classe à forte capacité avant le point de non-retour, réalisant un regret simple final inférieur d'au moins $15\%$ (illustratif) à celui de IRL-CD.
*   **Hypothèse $H_B$ (Fragilité de la spécification paramétrique et supériorité de IRL-CD)** : La mauvaise spécification de la loi de puissance pendant les plateaux initiaux induit une variance a posteriori divergente ou un biais d'asymptote dans VIM-LEP, provoquant soit des bascules prématurées ruineuses ($\ge 3$ bascules, illustratif), soit un enfermement dans la classe rapide ; le critère local IRL-CD à amortissement domine ou égale VIM-LEP avec un coût de calcul inférieur.
*   **Métrique et Seuil** : Regret simple normalisé à l'horizon $B$, $\mathcal{R}(B) = \frac{L_{\text{alg}}(B) - L_{k^*}(B)}{L_{\text{init}} - L_{k^*}(B)}$, moyenné sur $50$ (illustratif) tirages de graines aléatoires, et nombre moyen de bascules $\bar{N}_S$. Seuil de décision : différence de regret $|\Delta \mathcal{R}(B)| > 0{,}05$ (illustratif) avec test de Wilcoxon bilatéral à $p < 0{,}01$ (illustratif).
*   **Contrôle négatif** : Courbes synthétiques générées exactement selon la loi $L_k(b) = L_k^\infty + \beta_k b^{-\gamma_k} + \epsilon_k(b)$. Si VIM-LEP ne bat pas IRL-CD sur ce contrôle négatif, l'implémentation de l'inférence bayésienne est défectueuse.
*   **Issues falsificatrices** :
    *   Si $\mathcal{R}_{\text{VIM-LEP}}(B) \le \mathcal{R}_{\text{IRL-CD}}(B) - 0{,}05$ sur les vraies courbes d'apprentissage neuronales $\implies$ **$H_B$ est falsifiée** (la forme paramétrique en loi d'échelle capture suffisamment la géométrie réelle malgré les plateaux).
    *   Si $\mathcal{R}_{\text{IRL-CD}}(B) < \mathcal{R}_{\text{VIM-LEP}}(B)$ ou si VIM-LEP gaspille plus de $0{,}20 B$ (illustratif) en coûts de bascule $c$ $\implies$ **$H_A$ est falsifiée** (l'extrapolation paramétrique globale à court terme est non identifiable en présence de dynamique d'optimisation non convexe).

### Duel Expérimental 2 : Réserve Adaptative (ADERD) contre Allocation Statique avec Validation Privée (*Thresholdout*) sous dérive non stationnaire
*   **Contexte** : Flux de données subissant un choc de distribution à un instant aléatoire $t_{\text{shock}} \sim \mathcal{U}[0{,}2 B, \, 0{,}8 B]$ (illustratif), changeant l'identité de la meilleure classe $k^*$.
*   **Hypothèse $H_A$ (Supériorité de la réserve dynamique couplée au détecteur de dérive $\hat{D}_t$)** : L'allocation ADERD couplée au découplage d'ancre ($\Delta_{\text{opt}}$ vs $\Delta_{\text{drift}}$) conserve son budget d'exploitation quand $t_{\text{shock}}$ n'a pas lieu, et déclenche une bascule unique exactement après $t_{\text{shock}}$ lorsque $t_{\text{shock}} < B - B_{\text{req}}$, battant l'allocation statique tant en régime stationnaire qu'en régime de choc.
*   **Hypothèse $H_B$ (Domination du bruit de sélection adaptative et supériorité du partage statique)** : Le couplage continu entre $\hat{D}_t$ et la règle d'arrêt ADERD multiplie les fausses alertes sur l'ensemble de validation ; un découpage statique (type *Successive Halving* + réserve fixe $\rho = 0{,}20$, illustratif) protégé par *Thresholdout* obtient une perte finale sur jeu de test indépendant inférieure à ADERD.
*   **Métrique et Seuil** : Écart de généralisation validation-test $|\hat{L}_{\text{val}}(B) - L_{\text{test}}(B)|$ et perte finale $L_{\text{test}}(B)$. Seuil : réduction de $L_{\text{test}}(B)$ d'au moins $2$ erreurs standards (illustratif).
*   **Contrôle négatif** : Flux strictement i.i.d. ($\hat{D}_t \equiv 0$ en population) obtenu par permutation aléatoire complète des données avant le lancement. Tout déclenchement de bascule motivé par la dérive dans ce contrôle est une fausse alerte pure.
*   **Issues falsificatrices** :
    *   Si ADERD sans *Thresholdout* présente un écart $|\hat{L}_{\text{val}}(B) - L_{\text{test}}(B)| > 2 \sqrt{\hat{\sigma}^2 / n_{\text{val}}}$ (illustratif) qui annule son gain sur $L_{\text{test}}(B)$ $\implies$ **$H_A$ est falsifiée** (le sur-ajustement adaptatif de la validation domine le gain de flexibilité budgétaire).
    *   Si ADERD bat l'allocation statique sur $L_{\text{test}}(B)$ dans les deux régimes (avec et sans choc) tout en maintenant un taux de fausses bascules sur le contrôle i.i.d. $< 5\%$ (illustratif) $\implies$ **$H_B$ est falsifiée**.

### Duel Expérimental 3 : Généralisation Méta-PAC-Bayésienne contre Mémorisation d'Empreinte sur Familles Nouvelles
*   **Contexte** : Apprentissage d'un méta-prior $\mathcal{P}$ sur $K = 8$ (illustratif) classes d'hypothèses à travers $N = 30$ (illustratif) familles de tâches tabulaires et visuelles.
*   **Hypothèse $H_A$ (Apprentissage d'un prior structurel transférable)** : Le méta-apprenant régularisé par la divergence $\text{KL}(\mathcal{Q} \,\|\, \mathcal{P})$ extrait des invariants de la dynamique de convergence ($\gamma_k$, ratio signal/bruit) et conserve son avantage de budget sur des familles nouvelles soumises à un brouillage d'échelle des pertes initiales.
*   **Hypothèse $H_B$ (Illusion de méta-apprentissage par mémorisation d'empreinte)** : Le gain observé sur des tâches tirées des mêmes familles provient de l'identification de la famille via la perte à l'initialisation $L_k(0)$ et la trace de la matrice de covariance des entrées ; sous transformation affine de la perte et rotation orthogonale des entrées sur de nouvelles familles, le méta-prior ne fait pas mieux qu'un prior uniforme $\mathcal{P}_0$.
*   **Métrique et Seuil** : Ratio d'accélération du budget $\text{RAB} = \frac{B(\text{Prior Uniforme pour atteindre } L^*)}{B(\text{Méta-Prior } \mathcal{Q} \text{ pour atteindre } L^*)}$ sur les familles tenues à l'écart *brouillées*. Seuil : $\text{RAB} > 1{,}30$ (illustratif, soit $30\%$ d'économie de budget).
*   **Contrôle négatif** : Attribution aléatoire des étiquettes de classes optimales $k^*$ entre les familles d'entraînement (destruction de toute structure méta-apprenable). Le $\text{RAB}$ doit tomber à $1{,}0 \pm 0{,}05$ (illustratif).
*   **Issues falsificatrices** :
    *   Si $\text{RAB} > 1{,}30$ avant brouillage d'empreinte mais chute dans $[0{,}95, \, 1{,}05]$ (illustratif) après normalisation affine des courbes initiales $\implies$ **$H_A$ est falsifiée** (le méta-algorithme mémorisait les signatures statiques des familles).
    *   Si $\text{RAB} > 1{,}30$ se maintient après brouillage complet des échelles et que la borne PAC-Bayésienne prédit une erreur non triviale corrélée à $r > 0{,}7$ (illustratif) avec la vraie perte inter-familles $\implies$ **$H_B$ est falsifiée**.

---

## (c) Métrologie minimale des instruments nommés dans la question

La question de l'arbitre mobilise quatre instruments d'observation et de décision. Pour chacun, nous définissons le protocole minimal de validation métrologique (Statut : HYPOTHÈSE ; chiffres « illustratifs »).

| Instrument nommé | Ce qu'il doit détecter | Cas honnêtes appariés (Positifs vs Contrôles) | Taux de détection (TD) et Fausses alertes (TFA) minimaux | Vérification mécanique naïve à battre (Baseline) |
| :--- | :--- | :--- | :--- | :--- |
| **1. Extrapolateur de la courbe de perte $L_k(b)$** | Un croisement futur : $\mathcal{H}_j$ est pire que $\mathcal{H}_k$ en $b_0$, mais meilleure en $B$. | *Positif* : Paire $(\mathcal{H}_{\text{linéaire}}, \mathcal{H}_{\text{MLP}})$ sur fonction cible non linéaire bruitée.<br>*Apparié* : Même paire sur fonction cible purement linéaire (aucun croisement vrai). | $\text{TD} \ge 0{,}80$ à $b_0 = 0{,}20 B$<br>$\text{TFA} \le 0{,}10$ sur les paires sans croisement (illustratifs). | **Pente Sécante Naïve** : Extrapolation linéaire par la droite passant par $(b_0/2, L_k(b_0/2))$ et $(b_0, L_k(b_0))$. |
| **2. Estimateur de variance $\hat{\sigma}_k^2(b)$** | L'incertitude réelle de généralisation de $\hat{L}_k(b)$ pour éviter le biais du gagnant. | *Positif* : Classe $\mathcal{H}_k$ instable (fort taux d'apprentissage, bruit élevé).<br>*Apparié* : Classe $\mathcal{H}_j$ de même perte moyenne vraie mais régularisée (faible variance). | Couverture empirique de l'intervalle à $95\%$ comprise dans $[92\%, 98\%]$ ; $\text{TFA}$ de bascule vers le bras bruité $\le 0{,}05$ (illustratifs). | **Variance I.I.D. Instantanée** : $\frac{1}{n_{\text{val}}(n_{\text{val}}-1)} \sum_{i} (\ell_i - \hat{L}_k)^2$ sur un seul point $b$, ignorant l'autocorrélation temporelle de la trajectoire. |
| **3. Mesure d'écart de distribution $\hat{D}_t$** | Une dérive de distribution qui *modifie le classement optimal* des classes $\mathcal{H}_k$. | *Positif* : Dérive conceptuelle ou de covariables rendant $\mathcal{H}_k$ sous-optimale face à $\mathcal{H}_j$.<br>*Apparié* : Dérive bénigne (ex. changement de contraste d'arrière-plan ou bruit orthogonal) qui ne change pas $\arg\min_k L_k$. | $\text{TD} \ge 0{,}85$ sur dérives malignes.<br>$\text{TFA} \le 0{,}10$ sur dérives bénignes appariées de même norme $L_2$ dans l'espace d'entrée (illustratifs). | **Test de Kolmogorov-Smirnov / MMD sur les entrées brutes $X$** : Détecte tout changement de $P(X)$, même s'il est orthogonal à la tâche prédictive $P(Y \mid X)$. |
| **4. Règle de bascule $(A)$ vs $(S)$ à coût $c$** | L'opportunité rentable de payer $c$ pour changer de classe avant l'épuisement de $B$. | *Positif* : Initialisation dans une mauvaise classe avec $B_{\text{rem}} > 3c$.<br>*Apparié* : Même mauvaise classe, mais $B_{\text{rem}} < 1{,}2 c$ (bascule mathématiquement non amortissable). | $\text{TD} \ge 0{,}75$ quand le gain net attendu dépasse $2c$.<br>$\text{TFA} \le 0{,}02$ quand $B_{\text{rem}}$ ne permet pas d'amortir $c$ (illustratifs). | **Patience Fixe (*Early Stopping Switch*)** : Basculer vers une classe aléatoire non testée si $\hat{L}_k(b)$ ne s'améliore pas de $\epsilon$ pendant $p$ pas consécutifs, quel que soit $B_{\text{rem}}$. |

*Précision sur l'instrument 3 ($\hat{D}_t$)* : Pour battre la vérification mécanique (MMD sur les entrées brutes) sur les cas honnêtes appariés (dérive bénigne vs maligne), $\hat{D}_t$ ne doit pas mesurer l'écart sur $P(X)$ seul, mais la **divergence fonctionnelle restreinte aux classes candidates** ($\mathcal{H}\Delta\mathcal{H}$-divergence de Ben-David et al., ou variation de la distribution des pertes résiduelles et des gradients de validation). Si l'instrument proposé par l'utilisateur ne bat pas la MMD brute sur les dérives bénignes appariées, il est déclaré non fonctionnel pour le pilotage de l'action $(S)$.

---

## (d) Ancrage matériel : modèles ouverts, calcul nécessaire et coûts estimés

Aucun fait matériel n'étant joint dans le bloc `FAITS`, toutes les valeurs numériques de cette section portent le statut **illustratif** (Règle 4). L'architecture expérimentale est dimensionnée pour être intégralement reproductible sur des modèles ouverts et des jeux de données publics, sans recourir à des infrastructures propriétaires fermées.

### 1. Banc d'essai de classes d'hypothèses ouvertes ($\mathcal{H}_1, \dots, \mathcal{H}_K$)
Pour tester les duels 1, 2 et 3 avec un contrôle exact du budget $B$ (compté en nombre d'exemples traités par passe avant/arrière + évaluations de validation), nous définissons deux échelles matérielles :

*   **Échelle Légère (Validation mathématique intensive, Duels 1 à 3 complets)** :
    *   *Données* : Suite ouverte **OpenML-CC18** / **TabRepo** ($30$ familles de tâches tabulaires hétérogènes, illustratif) + **ashiq/Digits-Five** ou **CIFAR-100** découpé en $20$ super-classes formant $20$ familles de tâches avec dérives contrôlées (illustratif).
    *   *Classes d'hypothèses ($K = 5$, illustratif)* :
        *   $\mathcal{H}_1$ : Modèle linéaire régularisé (ElasticNet / Régression Logistique par SGD).
        *   $\mathcal{H}_2$ : Arbres de décision suralimentés par gradient (LightGBM ouvert, ajusté séquentiellement par ajout d'arbres).
        *   $\mathcal{H}_3$ : Perceptron multicouche à connexions résiduelles (ResNet-Tabulaire, $3$ blocs, $\approx 0{,}5\text{M}$ paramètres, illustratif).
        *   $\mathcal{H}_4$ : Architecture à attention sur attributs (FT-Transformer ouvert, $\approx 2\text{M}$ paramètres, illustratif).
        *   $\mathcal{H}_5$ : Réseau neuronal profond sur-paramétré (MLP $8$ couches larges avec normalisation de couche, $\approx 10\text{M}$ paramètres, illustratif, conçu pour avoir une convergence initiale lente et une forte capacité asymptotique).
*   **Échelle Moyenne (Affinement réaliste de modèles de langue ou de vision ouverts)** :
    *   *Modèles de base ouverts* : Famille **Pythia** (`pythia-70m`, `pythia-160m`, `pythia-410m`, poids Apache 2.0 totalement ouverts) ou **Qwen2.5** (`0.5B`, `1.5B`).
    *   *Définition des classes $\mathcal{H}_k$* : Choix de la classe d'adaptation paramétrique sous budget de jetons $B = 5 \times 10^7$ jetons (illustratif) :
        *   $\mathcal{H}_1$ : Ajustement de sonde linéaire seule (*Linear Probing*).
        *   $\mathcal{H}_2$ : Adaptation de bas rang à rang minimal (LoRA $r = 4$ sur les matrices d'attention $Q, V$ uniquement).
        *   $\mathcal{H}_3$ : LoRA à haut rang ($r = 64$ sur toutes les couches linéaires).
        *   $\mathcal{H}_4$ : Ajustement complet des poids (*Full Fine-Tuning*) d'un modèle plus petit (`pythia-160m`).
    *   *Transfert partiel lors de l'action $(S)$* : Si l'on bascule de $\mathcal{H}_2$ (LoRA $r=4$) vers $\mathcal{H}_3$ (LoRA $r=64$), la matrice $\Delta W_{r=4}$ déjà apprise est injectée dans les $4$ premières composantes singulières de $\mathcal{H}_3$ ($\alpha_{2 \to 3} > 0$), tandis que le coût $c$ correspond au calcul des états de l'optimiseur (moments d'Adam) sur les $60$ dimensions supplémentaires.

### 2. Chiffrage du calcul et coût financier (Statut : illustratif)
*   **Échelle Légère** :
    *   $3$ Duels $\times$ $50$ répétitions statistiques $\times$ $30$ familles de tâches $\times$ $4$ politiques comparées (VIM-LEP, IRL-CD, Statique-Halving, ADERD) = $18\,000$ trajectoires d'allocation (illustratif).
    *   Durée moyenne d'une trajectoire de budget $B = 10^5$ évaluations (illustratif) sur GPU : $\approx 12$ secondes (illustratif) sur une carte NVIDIA L4 ou RTX 4090.
    *   Temps de calcul total : $18\,000 \times 12\text{ s} = 216\,000\text{ s} \approx 60$ heures-GPU (illustratif).
    *   Coût infonuagique estimé (tarif public d'une instance à $1 \times \text{L4}$ ou $\text{A10G}$ à $\approx 1{,}00\text{ \$/h}$, illustratif) : **$\approx 60\text{ \$}$** (illustratif).
*   **Échelle Moyenne (Validation sur modèles Pythia / Qwen)** :
    *   $5$ familles de tâches textuelles $\times$ $10$ graines $\times$ $4$ politiques = $200$ trajectoires d'affinement (illustratif).
    *   Durée moyenne d'une trajectoire ($5 \times 10^7$ jetons + évaluations MMD et validation) sur une carte NVIDIA A100-80GB : $\approx 25$ minutes (illustratif).
    *   Temps de calcul total : $200 \times 0{,}42\text{ h} \approx 84$ heures-GPU A100 (illustratif).
    *   Coût infonuagique estimé (tarif à la demande $\approx 2{,}50\text{ \$/h}$ par A100, illustratif) : **$\approx 210\text{ \$}$** (illustratif).

Le budget matériel cumulé pour trancher expérimentalement les trois duels aux deux échelles s'élève ainsi à environ **$144$ heures-GPU** pour un coût total de **$270\text{ \$}$** (illustratif), ne nécessitant qu'un nœud de calcul standard à une seule carte graphique.

FIN-DE-CELLULE