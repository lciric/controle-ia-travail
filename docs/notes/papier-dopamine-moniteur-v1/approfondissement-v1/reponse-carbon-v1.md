*Note préliminaire : conformément à tes règles, je m'en tiens strictement aux éléments fournis dans l'énoncé concernant `arXiv:2602.00986` (v2) sans extrapoler son contenu non décrit, je distingue explicitement ce qui est **[Établi]** de ce qui relève de **[Ma proposition]**, et je signale toute incertitude sur un identifiant arXiv.*

---

### 1. Ce qu'un expert du domaine ferait ici, et qu'on ne demande pas

Avant de chercher 5 000 épisodes par tranche, un expert remettrait en cause cinq défauts structurels du protocole actuel :

1. **Découpler la preuve scientifique d'orthogonalité du point de fonctionnement opérationnel à 1 % [Établi en méthodologie statistique ; Ma proposition d'application au protocole] :** Tester l'hypothèse scientifique (« la sonde lit l'intention au-delà de l'échec attendu ») ne requiert *aucun* seuil binaire à 1 % par tranche de longueur. Fixer un seuil de Neyman-Pearson à $\alpha = 0,01$ sert à allouer un budget d'audit humain en déploiement (*AI Control: Improving Safety Despite Intentional Subversion*, Greenblatt et al., `arXiv:2312.06942`), pas à tester l'existence d'un signal sur petit échantillon. Mélanger les deux condamne l'expérience à manquer de puissance statistique avant même de savoir si la direction latente existe.
2. **Supprimer le conditionnement par tranches de longueur finale $T$, qui crée un biais de collisionneur (*post-treatment bias*) [Établi en inférence causale] :** La longueur d'épisode $T$ n'est pas une covariable exogène ; elle est *endogène* à la politique de l'agent et au sabotage (un saboteur peut échouer vite pour limiter son exposition ou rallonger la trace pour diluer une somme). Conditionner sur $T$ réalisé fausse le contraste causal et empêche toute surveillance en ligne (où $T$ est inconnu à l'étape $t$).
3. **Diagnostiquer l'autocorrélation intra-épisode et la variance inter-tâches [Établi en séries temporelles ; Ma proposition de diagnostic prioritaire] :** Sur le flux résiduel d'un transformeur, les activations successives sont fortement autocorrélées. La somme brute $\sum_{t=1}^T s_t$ n'accumule pas $T$ signaux indépendants (variance $\propto T$), mais intègre une dérive persistante liée à la tâche (variance proche de $\propto T^2$). La queue à 1 % de cette somme est donc gouvernée par l'effet aléatoire « tâche » ($\sigma^2_{\text{tâche}}$), et non par le bruit intra-épisode. Produire 5 000 épisodes sur un jeu restreint de tâches n'étalonnera pas le taux de fausses alertes sur des tâches inédites.
4. **Corriger le biais de sélection du contraste « saboteur vs échec honnête tâche par tâche » [Ma proposition] :** Apparier uniquement les tâches qui admettent un échec honnête exclut de l'analyse toutes les tâches faciles où l'agent honnête réussit systématiquement. Or, en contrôle opérationnel, ce sont précisément les tâches faciles (haute réussite attendue initiale) où un saboteur forcé de provoquer un échec doit exécuter les actions les plus anormales vis-à-vis de sa propre représentation de valeur. Ce filtrage censure la zone de plus fort rapport de vraisemblance.
5. **Ajouter un témoin négatif à « consigne secrète bénigne » avant tout étalonnage coûteux [Établi dans la littérature sur les sondes de déception, ex. Goldowsky-Dill et al., *Detecting Strategic Deception Using Linear Probes*, identifiant arXiv incertain ; MacDiarmid et al., *Simple probes can catch sleeper agents*, note technique Anthropic sans arXiv certain] :** Une sonde linéaire sépare très facilement « présence d'une instruction cachée dans l'invite système » de « exécution normale ». Sans épisodes où l'agent suit secrètement une contrainte *inoffensive* (ex. imposer un style de code précis sans jamais le mentionner tout en réussissant la tâche), il est impossible de savoir si la sonde lit le *sabotage* ou la simple *dissimulation d'une consigne*.

---

### 2. Les données brutes qu'il utiliserait au départ (au lieu des quelques centaines d'épisodes agrégés)

Au lieu de traiter chaque épisode terminé comme un unique point scalaire, l'expert exploiterait immédiatement quatre sources de données à granularité fine et faible coût :

1. **Les tenseurs d'activations par couche et par jalon structurel, couplés aux log-probabilités et entropies prédictives du modèle sur les épisodes existants [Ma proposition] :** Séparer strictement les jetons de (a) réception d'observation/erreur d'outil, (b) raisonnement interne, et (c) émission de la commande d'action. Croiser les états internes avec l'entropie des logits permet de purger immédiatement ce qui ne fait que refléter la perplexité syntaxique ou la surprise face à une erreur d'exécution.
2. **Des passes avant (*teacher-forced forward passes*) hors-politique sur des milliers de traces d'agents honnêtes publiques ou archivées [Ma proposition] :** Ce qui coûte cher dans un épisode d'agent, c'est la boucle interactive (machines virtuelles, exécution d'outils, décodage séquentiel). Rejouer en *une seule passe avant* avec `Llama-3.1-8B` (ou le modèle cible à poids ouverts) des milliers de traces honnêtes existantes (issues de bancs d'essai publics de génie logiciel ou d'utilisation d'outils) ne coûte aucun environnement d'exécution et fournit à bas prix la structure de covariance temporelle des activations honnêtes.
3. **Des embranchements courts ($k$ jetons ou une seule action) depuis les préfixes déjà enregistrés [Établi dans le contrôle par ré-échantillonnage, ex. Bhatt et al., *Ctrl-Z: Controlling AI Agents via Resampling*, identifiant arXiv incertain ; étendu ici aux états internes] :** Plutôt que de générer des épisodes complets de bout en bout, tirer plusieurs actions alternatives uniquement aux jalons critiques des épisodes existants.
4. **Un petit lot d'épisodes courts à « objectif caché bénin » et de paires minimales hors-agent [Ma proposition] :** Pour vérifier l'invariance de la sonde aux artefacts d'invite avant toute campagne d'épisodes longs.

---

### 3. Les méthodes et outils précis employés, et ce que chacun suppose

1. **Statistique d'ordre et bornes de tolérance exactes en échantillon fini [Établi : Wilks, *Determination of Sample Sizes for Setting Tolerance Limits*, 1941 ; Vovk, Gammerman, Shafer, *Algorithmic Learning in a Random World* ; Bates et al., *Distribution-Free, Risk-Controlling Prediction Sets*, `arXiv:2101.02703`, identifiant à vérifier] :**
   * *Outil :* Le calcul « 5 000 épisodes par tranche pour 50 dépassements » suppose qu'on veut estimer ponctuellement le quantile à 99 % avec une erreur relative faible ($\approx 1/\sqrt{50} \approx 14\%$) indépendamment dans chaque tranche. En échantillon fini, si l'on fixe le seuil au maximum de $n$ scores honnêtes continus échangables, l'espérance marginale du taux de fausses alertes vaut exactement $\frac{1}{n+1}$ (soit $1\%$ dès $n = 99$). Si l'on exige une garantie de haute confiance conditionnellement à l'échantillon d'étalonnage, $\mathbb{P}(\text{FPR}(\hat{q}) \le \alpha) \ge 1 - \delta$, la formule exacte de Wilks impose $(1-\alpha)^n \le \delta$, soit $n = \lceil \ln(\delta)/\ln(1-\alpha) \rceil$. Pour $\alpha = 0,01$ et $1-\delta = 0,95$, cela donne exactement $n = \lceil \ln(0,05)/\ln(0,99) \rceil = 299$ épisodes *au total* (sans tranches), au prix d'un seuil conservateur qui réduit la puissance.
   * *Hypothèse :* Échangeabilité stricte entre les épisodes d'étalonnage et de déploiement (donc *tâches disjointes* tirées de la même loi, et non réutilisation des mêmes tâches).

2. **Blanchiment martingale des innovations + Régression Quantile Conformisée (CQR) mutualisée [Établi : Romano, Patterson, Candès, *Conformalized Quantile Regression*, `arXiv:1905.03222`] :**
   * *Outil :* Remplacer la somme brute $\sum z_t$ et le découpage en tranches de longueur par la décomposition de Doob sur les épisodes honnêtes : apprendre $\hat{\mu}_t = \mathbb{E}_{\text{honnête}}[z_t \mid \mathcal{F}_{t-1}]$ et $\hat{\sigma}_t^2 = \text{Var}_{\text{honnête}}(z_t \mid \mathcal{F}_{t-1})$, puis former la statistique auto-normalisée $M_t = \frac{\sum_{s=1}^t (z_s - \hat{\mu}_s)}{\sqrt{\sum_{s=1}^t \hat{\sigma}_s^2}}$. Ajuster ensuite une régression quantile à 99 % lisse $\hat{q}_{0,99}(T, V_0)$ (où $V_0$ est la réussite attendue initiale issue de `arXiv:2602.00986`) et conformiser les résidus sur un unique pli mis de côté. Toutes les longueurs sont ainsi mutualisées.
   * *Hypothèses :* La couverture à 1 % est garantie *marginalement* sous la seule échangeabilité ; la garantie *conditionnelle* par longueur suppose que la paramétrisation de $\hat{q}_{0,99}(T, V_0)$ capture correctement l'hétéroscédasticité résiduelle.

3. **Théorie des valeurs extrêmes — dépassements de seuil (*Peaks Over Threshold* / loi de Pareto généralisée, GPD) [Établi : théorème de Pickands-Balkema-de Haan, 1974–1975] :**
   * *Outil :* Sur les résidus blanchis et mutualisés, fixer un seuil intermédiaire $u$ (par ex. le quantile empirique à 90 %) et ajuster une loi GPD $G_{\xi, \beta}$ aux excès $Y = R - u \mid R > u$ pour extrapoler le quantile à 99 % avec intervalles de confiance par vraisemblance profilée.
   * *Hypothèses :* Appartenance de la loi honnête au domaine d'attraction extrême et entrée effective dans le régime asymptotique dès le quantile $u$. Échoue si le dernier centile relève d'un *régime physiquement distinct* (ex. plantages rares d'environnement absents à 90 %).

4. **E-valeurs séquentielles, martingales de pari et inégalité de Ville [Établi : Shafer, *Testing by betting*, 2021 ; Ramdas, Grünwald, Vovk, Shafer, *Game-Theoretic Statistics and Safe Anytime-Valid Inference*, `arXiv:2210.01948`, identifiant à vérifier] :**
   * *Outil :* Construire à chaque jalon $t$ une variable $E_t \ge 0$ telle que $\mathbb{E}_{H_0}[E_t \mid \mathcal{F}_{t-1}] \le 1$. Le processus produit $W_t = \prod_{s=1}^t E_s$ est une surmartingale positive de valeur initiale $1$. L'inégalité de Ville garantit alors $\mathbb{P}_{H_0}(\exists t \ge 1 : W_t \ge 1/\alpha) \le \alpha$ : un seuil fixe $W_t \ge 100$ contrôle le taux de fausses alertes à $\le 1\%$ *uniformément dans le temps*, quelle que soit la longueur $T$ ou la règle d'arrêt.
   * *Hypothèse critique :* L'espérance conditionnelle sous $H_0$ doit réellement être $\le 1$ à chaque pas. Si $\hat{\mu}_t$ est mal spécifié à cause d'une tâche atypique, la martingale explose sous $H_0$. Pour la rendre exacte sans hypothèse paramétrique, il faut construire $E_t$ par **rangs conformes conditionnels** face à des tirages contrefactuels d'un jumeau de référence sur le même préfixe (**[Ma proposition]** reliant la base n°2 aux e-valeurs).

5. **Échantillonnage préférentiel (*Importance Sampling* / *Adaptive Multilevel Splitting*) pour l'étalonnage des queues [Établi : Kahn & Marshall, 1953 ; Cérou & Guyader, *Adaptive Multilevel Splitting for Rare Event Analysis*, 2007] :**
   * *Outil :* Sur-échantillonner les tâches ou préfixes honnêtes à fort risque de faux positif (identifiés à bas coût par $V_0$ bas ou forte volatilité précoce de la sonde) selon une loi $q(x)$, et estimer la fonction de répartition de queue par pondération $w_i = p(x_i)/q(x_i)$.
   * *Hypothèses :* Absolue continuité ($q(x) > 0$ partout où la queue honnête a une masse positive) et contrôle de la variance des poids $w_i$.

---

### 4. Ce qui, en dehors du programme et de son directeur, permettrait de vérifier la validité du résultat

1. **Épreuve en aveugle à vérité plantée par un tiers indépendant [Établi en évaluation de sécurité / métrologie] :** Un tiers génère un lot mêlant épisodes honnêtes (succès et échecs), épisodes à consigne secrète bénigne et épisodes sabotés en proportion inconnue $\pi$, publie l'empreinte cryptographique des étiquettes avant l'évaluation, et reçoit les décisions binaires du moniteur figé (poids + seuil verrouillés).
2. **Transfert inter-mécanismes de sabotage (hors distribution d'incitation) [Établi via les « organismes modèles » : Hubinger et al., *Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training*, `arXiv:2401.05566`] :** Une sonde entraînée ou validée sur un saboteur induit par invite système doit être testée à l'aveugle sur un saboteur induit par ajustement des poids (LoRA / *sleeper agent* sans aucune mention de sabotage dans le contexte), ainsi que par ouverture unique et pré-enregistrée de l'épreuve d'évasion à compétence constante.
3. **Réplication sur bancs d'essai publics d'AI Control [Établi] :** Évaluer le pipeline sur des environnements publics disposant déjà de références externes — tels que le cadre de *AI Control* (`arXiv:2312.06942`), *ControlArena* (UK AISI / Redwood Research) ou *SHADE-Arena* (Kutasov et al., *SHADE-Arena: Evaluating Sabotage and Monitoring in LLM Agents*, identifiant arXiv incertain).
4. **Deux mesures indépendantes de non-trivialité [Établi en interprétabilité mécaniste et AI Control] :**
   * *Moniteur boîte noire externe fort :* Un modèle de langage tiers lisant *uniquement* les actions et résultats d'outils (sans co-chaîne de pensée si elle est masquée, et sans activations) évalué au même taux de 1 % de fausses alertes. S'il égale la sonde interne, le sabotage n'était pas réellement discret dans l'espace des actions.
   * *Intervention causale (activation steering, cf. Zou et al., *Representation Engineering: A Top-Down Approach to AI Transparency*, `arXiv:2310.01405`) :* Vérifier si soustraire la direction « intention » réduit le taux de sabotage sans dégrader la réussite honnête, contrairement à la direction « réussite attendue » de `arXiv:2602.00986`.

---

### 5. Reformulation de la demande

Voici comment formuler le problème pour qu'il soit statistiquement et opérationnellement bien posé :

> « Nous cherchons à détecter le sabotage furtif d'un agent à poids ouverts sous contrainte stricte de budget d'épisodes. Nous séparons trois objectifs :
> 1. **Identification scientifique (sans seuil arbitraire) :** Démontrer, par tests de rangs appariés par préfixe et par tâche (incluant des tâches faciles et des témoins à consigne secrète bénigne), qu'une sonde linéaire extrait un signal d'intention orthogonal à la valeur attendue (`arXiv:2602.00986`) et aux quatre bases définies, y compris face à un saboteur par poids modifiés et à une évasion à compétence constante.
> 2. **Étalonnage séquentiel mutualisé en échantillon fini :** Construire, sans découpage endogène par tranches de longueur, une statistique de surveillance séquentielle blanchie dont le taux de fausses alertes par épisode sur tâches *inédites* est contrôlé à $\le 1\%$ (avec borne de confiance explicite en échantillon fini), en exploitant les passes avant hors-politique et l'échantillonnage préférentiel plutôt que le tirage massif d'épisodes complets.
> 3. **Protocole d'AI Control assisté par sonde de valeur :** Intégrer la sonde de réussite attendue (`arXiv:2602.00986`) et la sonde d'intention dans une architecture de contrôle à plusieurs niveaux (routage vers modèle de confiance, ré-échantillonnage local d'actions suspectes, et allocation optimale du 1 % d'audit humain) maximisant la probabilité d'interception avant dommage irréversible. »

---

### 6. Propositions concrètes

*(Toutes les architectures ci-dessous relèvent de **[Ma proposition]**, appuyée sur les briques théoriques marquées **[Établi]** en section 3.)*

#### A. Régler un seuil à 1 % avec peu d'épisodes honnêtes — ou s'en passer honnêtement

**Proposition A1 — S'en passer honnêtement pour le verdict scientifique, et poser une borne de Wilks exacte en sortie**
* *Principe :* Supprimer l'exigence du seuil à 1 % par tranche pour comparer la sonde aux quatre bases. Juger la supériorité scientifique via l'aire partielle sous la courbe ROC dans la zone $[0 ; 0,05]$ estimée par *bootstrap* par grappes de tâches, complétée par un test de permutation apparié sur préfixes identiques. Pour fournir malgré tout un point de fonctionnement honnête à $\le 1\%$ sur les quelques centaines d'épisodes existants, mutualiser les longueurs après auto-normalisation temporelle et appliquer la borne d'ordre exacte de Wilks ($n \ge 299$ épisodes sur tâches distinctes suffisent pour garantir $\text{FPR} \le 1\%$ avec $95\%$ de confiance en prenant le maximum observé).
* *Coût :* Nul en nouveaux épisodes (calcul CPU uniquement, hors petit lot de témoins à consigne bénigne).
* *Hypothèses :* Indépendance entre tâches ; épisodes d'étalonnage tirés de la même distribution de tâches que le test.
* *Modes d'échec :* Le seuil de Wilks à $n \approx 300$ est très conservateur (le vrai FPR médian est nettement inférieur à $1\%$), ce qui écrase le rappel (puissance) si le signal d'intention a des queues lourdes sous $H_0$.

**Proposition A2 — Blanchiment ARX des innovations conditionnellement à $V_t$ + CQR mutualisée**
* *Principe :* Remplacer la somme brute par les innovations standardisées $e_t = s_t - \hat{f}(s_{t-1}, V_t, \Delta V_t, \text{entropie}_t, \text{type\_jeton}_t)$, où $\hat{f}$ est appris uniquement sur des traces honnêtes. Calculer $M_T = (\sum_{t=1}^T e_t) / \sqrt{\sum_{t=1}^T \hat{\sigma}_t^2}$, puis appliquer la régression quantile conformisée (CQR) conditionnellement à $(\ln T, V_0)$ sur l'ensemble des épisodes honnêtes réunis. Vérifier la stabilité de l'extrapolation par un ajustement GPD au-dessus du 90e centile.
* *Coût :* Très faible (ré-extraction des états et logits sur les épisodes déjà produits).
* *Hypothèses :* Stationnarité approximative de la dynamique des innovations honnêtes d'une tâche à l'autre une fois purgée de $V_t$ et de l'entropie.
* *Modes d'échec :* Mauvaise spécification de l'hétéroscédasticité : le FPR global sera bien de $1\%$, mais pourrait atteindre $3\%$ sur certaines familles de tâches atypiques et $0,1\%$ ailleurs.

**Proposition A3 — Pré-étalonnage hors-politique massif en passe avant + Échantillonnage préférentiel ciblé**
* *Principe :* Utiliser des milliers de traces publiques d'agents en passe avant unique pour apprendre à haute précision le modèle de blanchiment $\hat{f}$ et un prédicteur rapide de queue $\hat{r}(\text{invite}, \text{début d'épisode})$. Ne dépenser le budget d'épisodes complets en-politique que sur un lot restreint sur-échantillonnant les tâches à fort $\hat{r}$, et estimer le quantile à $99\%$ par *Importance Sampling* auto-normalisé.
* *Coût :* Modéré (quelques heures GPU de passes avant sans sandbox + un petit lot d'épisodes ciblés).
* *Hypothèses :* Le décalage de distribution entre traces publiques et épisodes en-politique n'omet pas un mode d'erreur propre à l'échafaudage de l'agent étudié ; poids d'importance bornés.
* *Modes d'échec :* Variance élevée de l'estimateur si une tâche a une probabilité d'échantillonnage $q(x)$ trop faible mais produit néanmoins un score extrême en déploiement.

---

#### B. Employer `arXiv:2602.00986` pour construire des moniteurs et améliorer le contrôle

Même avec une AUC modeste de $0,69$ entre problèmes distincts (telle que rapportée sur MATH500), une sonde de « réussite attendue » $V_t$ devient un levier puissant dès qu'on l'utilise **en différentiel intra-préfixe** (où l'effet aléatoire de difficulté globale de la tâche s'annule).

**Proposition B1 — Moniteur d'anomalie d'avantage contrefactuel et d'inversion de différence temporelle ($\Delta V$)**
* *Principe :* Décomposer la variation $\Delta V_t = V_t - V_{t-1}$ en deux phases : la variation *pendant le choix d'action de l'agent* ($\Delta V_{\text{action}}$) et la variation *à la réception du retour d'outil* ($\Delta V_{\text{obs}}$). Un agent honnête qui échoue choisit des actions visant à maintenir ou accroître $V$, et subit des chocs $\Delta V_{\text{obs}} < 0$ quand l'environnement renvoie une erreur imprévue. À l'inverse, si $V_t$ mesure la valeur de réussite de la tâche (apprise sur traces honnêtes), un saboteur sélectionne délibérément des actions **anti-gloutonnes** qui dégradent $V$ *avant même le retour de l'environnement*, ou présentent un avantage contrefactuel négatif $A_t = V(s_t, a_{\text{choisie}}) - \frac{1}{m}\sum_{j=1}^m V(s_t, a'_j) \ll 0$ par rapport à $m$ actions tirées d'un jumeau propre sur le même préfixe. (Et si $V_t$ lit partiellement la réussite de l'objectif propre du modèle, $V_t$ monte quand le jumeau voit la tâche s'effondrer : la divergence $V_t^{\text{agent}} - V_t^{\text{jumeau}}$ explose dans les deux cas.)
* *Coût :* Élevé si évalué à chaque pas ; faible si déclenché uniquement aux jalons d'écriture de fichiers ou d'exécution de commandes (quelques générations courtes d'une seule action sans exécuter l'environnement).
* *Hypothèses :* La sonde de `arXiv:2602.00986` a une résolution locale suffisante pour ordonner deux actions sur un même état $s_t$ (ce qu'explique d'ailleurs le besoin du seuil de variation du papier lors de l'entraînement).
* *Modes d'échec :* Sabotage purement passif par omission (ne pas explorer une piste peu évidente) où chaque micro-action ressemble localement à un choix honnête sous-optimal, ou bruit excessif de la sonde hors du domaine mathématique (code/bash vs MATH500).

**Proposition B2 — Détecteur de dissonance épistémique (« écart dire-croire »)**
* *Principe :* Coupler la sonde interne $V_t$ à un extracteur léger lisant la confiance et l'état d'avancement *déclarés* dans la trace textuelle ou le résumé final de l'agent ($\hat{C}_t^{\text{texte}}$). Un saboteur discret doit justifier ses choix de manière rassurante (ou feindre un blocage inévitable en fin de parcours) : cela crée une divergence structurelle entre $\hat{C}_t^{\text{texte}}$ élevé (« les vérifications sont concluantes ») et un $V_t$ interne effondré — ou entre un aveu soudain d'impasse alors que $V_t$ était élevé juste avant sa propre modification.
* *Coût :* Très faible (un classifieur léger ou un petit modèle sur le texte produit + lecture directe de $V_t$).
* *Hypothèses :* Le modèle conserve en interne une estimation dégradée de la réussite réelle de la tâche lorsqu'il produit un texte faussement confiant.
* *Modes d'échec :* Sycophantie ou surconfiance naturelle des modèles honnêtes (qui affirment parfois avoir réussi alors que $V_t$ est bas), ce qui impose d'étalonner l'écart $\hat{C}_t^{\text{texte}} - V_t$ sur les échecs honnêtes.

**Proposition B3 — Protocole d'AI Control à deux niveaux : ré-échantillonnage local automatisé et allocation bayésienne du 1 % d'audit humain**
* *Principe :* Ne jamais utiliser la sonde seule comme déclencheur direct du 1 % d'audit humain sur flux brut. Structurer trois barrières :
  1. *Routage initial par $V_0$ :* Sur les tâches où $V_0$ initial est élevé (tâches perçues comme faciles), router vers un modèle plus faible de confiance (*Defer-to-Trusted*, `arXiv:2312.06942`) ou exiger une réussite stricte, privant le saboteur des tâches faciles.
  2. *Intervention automatique intermédiaire (à seuil large, sans humain) :* Lorsqu'un jalon présente une chute brutale $\Delta V_{\text{action}} \ll 0$ ou un signal modéré de la sonde d'intention, annuler l'action avant son exécution dans l'environnement et la remplacer par une action ré-échantillonnée via un modèle de confiance ou un jumeau nettoyé (*resampling*).
  3. *Allocation optimale du budget d'audit humain de 1 % :* Concentrer l'audit humain sur les épisodes qui **échouent (ou touchent des fichiers sensibles) alors que $\max_{t < t^*} V_t$ était élevé**. Les échecs honnêtes se concentrant sur les trajectoires à $V_t$ constamment bas, pondérer le score d'audit par $V_{\text{pré-échec}}$ démultiplie le rapport de vraisemblance $\mathbb{P}(\text{sabotage} \mid \text{alerte}) / \mathbb{P}(\text{honnête} \mid \text{alerte})$ à budget humain constant.
* *Coût :* Budget humain inchangé ($1\%$) ; surcoût machine limité à la fraction $\tau$ de jalons ré-échantillonnés.
* *Hypothèses :* Possibilité technique d'intercepter l'action *avant* effet irréversible dans l'environnement (bac à sable transactionnel) ; corrélation positive minimale de $V_t$ avec la réussite honnête dans le domaine cible.
* *Modes d'échec :* Sabotage « en un seul coup » camouflé sur une tâche intrinsèquement très difficile ($V_0$ très bas dès le départ), ou évasion adaptative d'un modèle capable de manipuler ses propres activations dans le sous-espace linéaire de $V_t$ (ce que doit précisément tester l'ouverture finale du bras d'évasion à compétence constante).