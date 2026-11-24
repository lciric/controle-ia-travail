### Note préliminaire sur les pièces et les conventions

Constat de pièce (`VÉRIFIÉ`) : le bloc `FAITS` et le bloc `QUESTION DE L'ARBITRE` portent le même empreinte SHA-256 (`f00e1678…`) ; aucune donnée expérimentale, spécification d'architecture ni journal d'exécution n'a été transmis. En conséquence :
- `VÉRIFIÉ` désigne uniquement ce qui figure dans le bloc transmis ou une identité mathématique élémentaire ;
- `RAPPORTÉ` désigne un résultat issu de la littérature scientifique citée ;
- `OBSERVÉ-NON-AUDITÉ` désigne une pratique empirique courante non auditée ici ;
- `HYPOTHÈSE` désigne tout présupposé, conjecture, estimation subjective de confiance ou proposition de conception.
Conformément aux règles d'intégrité, tout chiffre qui ne provient pas des faits est marqué `illustratif` et aucun identifiant arXiv n'est cité de mémoire.

---

### (a) Présupposés non établis de la question

| # | Présupposé implicite dans la question | Pourquoi ce n'est pas établi | Statut |
|---|---|---|---|
| P1 | Il existe « un même espace d'idées candidates » permettant un échantillonnage aléatoire comparable entre agents LLM, énumérateur et tirage uniforme. | Les hypothèses, lois, lemmes et protocoles vivent dans des espaces hétérogènes ; la mesure uniforme dépend arbitrairement du codage/DSL choisi (`RAPPORTÉ`, invariance de représentation violée). | `HYPOTHÈSE` |
| P2 | « Narrow » (rareté) et « deep » (conséquence) sont des propriétés intrinsèques mesurables sur deux axes séparables à travers quatre objets scientifiques distincts. | La rareté est relative à un chercheur de référence et à un codage ; la conséquence dépend de l'horizon temporel, du régime hors-distribution et du domaine. | `HYPOTHÈSE` |
| P3 | Une architecture multi-agents (proposer–critiquer–sélectionner) augmente la découverte d'événements rares plutôt que de lisser vers le mode. | Le consensus ou la critique par LLM peut réduire la variance et éliminer précisément la queue rare des propositions (`OBSERVÉ-NON-AUDITÉ`). | `HYPOTHÈSE` |
| P4 | Un juge LLM peut voir son biais « borné » sans oracle externe suffisant. | Sans échantillon audité par une vérité externe indépendante, les erreurs corrélées entre générateur et juge restent non identifiables (`RAPPORTÉ`, Angelopoulos et al., 2023). | `HYPOTHÈSE` |
| P5 | Les sources de vérité candidates (mondes synthétiques, rétrodiction, preuve formelle, tests exécutables) mesurent la même cible scientifique. | Chaque source mesure un construit différent ; aucune ne combine simultanément validité externe ouverte, absence de contamination et coût faible. | `HYPOTHÈSE` |
| P6 | La comparaison « à même budget » est unidimensionnelle entre LLM multi-agents, modèle unique et énumérateur mécanique. | Elle confond coût d'inférence (FLOPs/USD), nombre d'appels à l'oracle vérificateur, coût amorti de pré-entraînement et temps humain d'ingénierie du DSL. | `HYPOTHÈSE` |
| P7 | Des « régions de problèmes » plus propices aux idées rares et profondes existent et sont identifiables avant exécution. | Par les théorèmes *No Free Lunch* (`RAPPORTÉ`, Wolpert & Macready, 1997), aucun avantage n'existe sans adéquation structurelle ; sélectionner des régions expose au biais de sélection. | `HYPOTHÈSE` |
| P8 | Un harnais automatisé de ce type est statistiquement et épistémiquement réalisable à coût fini. | Si la rareté visée est extrême ($p \ll 10^{-3}$, `illustratif`) ou instable au recodage, l'estimation devient statistiquement impraticable ou mal posée. | `HYPOTHÈSE` |

---

### Analyse des 8 questions de l'arbitre

#### 1. Cible (« narrow » et « deep »)
**Opérationnalisation.** Définir *narrow* comme une propriété relationnelle d'une **classe d'équivalence canonisée** $[x]$ (modulo renommage de variables, réécriture algébrique ou paraphrase) vis-à-vis d'un **ensemble de références** $\mathcal{Q}_0 = \{Q_{\text{enum}}, Q_{\text{LLM-1}}, Q_{\text{rand}}\}$ (`HYPOTHÈSE`) :
$$R_{\mathcal{Q}_0}([x]) = \min_{Q \in \mathcal{Q}_0} \left(-\log_2 \hat{p}_Q([x])\right) \quad \text{ou} \quad \min_{Q \in \mathcal{Q}_0} B_{0{,}5}(Q,[x])$$
où $B_{0{,}5}(Q,[x])$ est le budget médian pour que le chercheur de référence $Q$ atteigne $[x]$ une première fois (`HYPOTHÈSE`). Prendre le minimum sur l'enveloppe empêche qu'un cliché trivial pour un LLM passe pour « rare » au motif qu'un énumérateur ne le trouve pas, et réciproquement.

Séparer *deep* de la simple rareté repose sur la distinction entre complexité aléatoire (entropie élevée, profondeur nulle ; `RAPPORTÉ`, Shannon, 1948) et **profondeur logique / pouvoir compressif** (`RAPPORTÉ`, Bennett, 1988 ; Rissanen, 1978). Opérationnellement (`HYPOTHÈSE`), la profondeur $D(x)$ doit être **contrefactuelle et hors-échantillon** :
- *Lois quantitatives* : gain de perte prédictive en régime interventionnel ou hors-distribution (OOD), pénalisé par la longueur de description, $\Delta \mathcal{L}_{\text{OOD}}(x) - \lambda |x|$ (`RAPPORTÉ`, Rissanen, 1978 ; Pearl, 2009).
- *Lemmes formels* : compression totale des preuves sur une batterie gelée de théorèmes cibles en aval lorsque $x$ est ajouté à la bibliothèque, sous contrainte de validité noyau et de non-trivialité dérivative (`HYPOTHÈSE`).
- *Protocoles expérimentaux* : gain d'information attendu (EIG) sur un paramètre latent inconnu par unité de coût expérimental dans un banc indépendant (`HYPOTHÈSE`).

L'agrégation doit être **non compensatoire** : un seuil plancher de profondeur $\tau_D$ (`illustratif`) bloque toute idée rare mais stérile (bruit, surajustement). Si un juge LLM est inévitable (pré-filtrage ou protocoles ouverts), son biais doit être borné par **Prediction-Powered Inference (PPI)** (`RAPPORTÉ`, Angelopoulos et al., 2023) à l'aide d'un sous-échantillon stratifié évalué par un oracle externe ou des experts en aveugle, complété par un test d'échange de style (*style-swap*) entre générateur et baseline (`HYPOTHÈSE`).

- **Établi vs conjecture :** Établi (`RAPPORTÉ`) : rareté $\neq$ profondeur (Shannon, 1948 ; Bennett, 1988) ; validité asymptotique des intervalles PPI sous échantillon audité (Angelopoulos et al., 2023). Conjecture (`HYPOTHÈSE`) : stabilité empirique des classes d'équivalence $[x]$ hors domaines formels ; suffisance du test *style-swap* pour capturer le biais du juge.
- **Où le cadrage est faux :** La question traite *narrow* comme une propriété absolue de l'idée et suppose un seul espace commun à quatre objets scientifiques incommensurables ; elle sous-estime qu'un juge sans oracle externe audité ne peut pas avoir de borne de biais non triviale.
- **Confiance :** `0,75` (`HYPOTHÈSE`, `illustratif`) sur la formalisation en domaines vérifiables ; `0,30` (`HYPOTHÈSE`, `illustratif`) sur les hypothèses verbales non formalisées.
- **Références :** Shannon, C. E. (1948), *A Mathematical Theory of Communication*, Bell System Technical Journal ; Bennett, C. H. (1988), *Logical Depth and Physical Complexity*, in *The Universal Turing Machine: A Half-Century Survey* ; Rissanen, J. (1978), *Modeling by shortest data description*, Automatica ; Pearl, J. (2009), *Causality: Models, Reasoning, and Inference* (2e éd.), Cambridge University Press ; Angelopoulos, A. N., Bates, S., Fannjiang, C., Jordan, M. I., & Zrnic, T. (2023), *Prediction-Powered Inference*, Science.

#### 2. Sources de vérité
| Source | Ce qu'elle établit (rareté / profondeur) | Ce qu'elle ne peut établir | Mode d'échec principal | Statut |
|---|---|---|---|---|
| **Mondes synthétiques (vérité plantée)** | Contrôle exact de la contamination (génération à la volée), profondeur OOD/interventionnelle exacte, calibration de rareté. | Validité externe sur la science réelle ouverte. | Biais du concepteur : le monde reflète les priors de son auteur et favorise artificiellement soit les LLM, soit l'énumérateur. | `HYPOTHÈSE` |
| **Rétrodiction à coupure temporelle** | Pertinence historique apparente. | Absence de fuite cognitive (prépublications, citations indirectes, reformulations post-coupure) ; rareté réelle dans le passé. | **Contamination** poreuse + biais rétrospectif (l'énoncé moderne du problème fuit déjà le cadre conceptuel). | `OBSERVÉ-NON-AUDITÉ` / `HYPOTHÈSE` |
| **Preuve formelle (ex. Lean 4)** | Validité sans faux positif (zéro biais de juge) ; profondeur objective par compression sur théorèmes aval ; baselines mécaniques exactes. | Pertinence empirique ; création d'ontologies non formalisées. | Goulot de formalisation ; lemmes artificiellement rares syntaxiquement ou gonflés si la suite aval n'est pas indépendante. | `RAPPORTÉ` / `HYPOTHÈSE` |
| **Tests exécutables / simulateurs** | Conséquence empirique sous changement de régime ; testable pour lois quantitatives et protocoles simulés. | Fidélité au réel physique hors modèle du simulateur. | **Reward hacking** : exploitation d'artefacts numériques, conditions aux bords ou bugs du simulateur. | `OBSERVÉ-NON-AUDITÉ` / `HYPOTHÈSE` |
| **Prospective pré-enregistrée (proposée)** | Validité externe sans contamination temporelle (prédictions scellées avant données futures / micro-expériences). | Puissance statistique rapide à bas coût. | Latence élevée, petit $N$, bruit expérimental fort. | `HYPOTHÈSE` |

- **Établi vs conjecture :** Établi (`VÉRIFIÉ`/`RAPPORTÉ`) : les vérificateurs de preuves éliminent les faux positifs de validité syntaxique/logique ; la régression symbolique exécutable dispose de baselines mécaniques fortes (`RAPPORTÉ`, Udrescu & Tegmark, 2020). Conjecture (`HYPOTHÈSE`) : la corrélation de classement des systèmes entre mondes synthétiques/formels et découverte empirique ouverte.
- **Où le cadrage est faux :** Opposer ces sources comme des alternatives mutuellement exclusives ; aucune n'est suffisante seule. Il faut une échelle triangulée : synthétique + formel/exécutable (validité interne) $\to$ prospectif pré-enregistré (validité externe), et exclure la rétrodiction seule comme preuve décisive pour des LLM.
- **Confiance :** `0,80` (`HYPOTHÈSE`, `illustratif`).
- **Références :** Udrescu, S.-M., & Tegmark, M. (2020), *AI Feynman: A physics-inspired method for symbolic regression*, Science Advances ; Popper, K. R. (1959), *The Logic of Scientific Discovery*, Hutchinson.

#### 3. Comparaison, unité d'analyse, comptabilité des coûts et attribution
- **Quantité primaire (`HYPOTHÈSE`) :** Utilité de queue indexée par le budget $B$, pas la moyenne (qui favorise les clichés sûrs) ni le maximum brut (qui récompense la variance bruitée) :
  $$U(P, B) = \max_{x \in \mathcal{S}(P, B)} \Big( D_{\text{ext}}(x)\cdot \mathbb{I}[R_{\mathcal{Q}_0}([x]) \ge \tau_R \;\land\; \text{Valide}(x)] \Big)$$
  agrégée en aire sous la courbe découverte–budget (AUDC) sur une grille pré-enregistrée $[B_{\min}, B_{\max}]$ (`illustratif`), accompagnée du taux de succès conjoint $\mathbb{P}(R \ge \tau_R \land D \ge \tau_D)$.
- **Unité d'analyse (`VÉRIFIÉ`/`RAPPORTÉ`) :** L'**instance de problème** $P$ (groupée par famille de problèmes), jamais l'idée individuelle $x$. Les idées d'une même trace sont fortement autocorrélées ; les traiter comme indépendantes détruit le calibrage des tests. Utiliser les différences appariées $\Delta_P = U_{\text{multi}}(P,B) - U_{\text{base}}(P,B)$ par bootstrap en grappes (`RAPPORTÉ`, Efron & Tibshirani, 1993) avec correction de Holm–Bonferroni (`RAPPORTÉ`, Holm, 1979) sur l'ensemble des baselines.
- **Comptabilité des coûts (`HYPOTHÈSE`) :** Comptabilité bidimensionnelle obligatoire — (i) **coût de calcul d'inférence** (FLOPs / heures GPU / USD à tarif figé) ET (ii) **nombre d'appels à l'oracle vérificateur** $C_{\text{eval}}$ — plus déclaration séparée du coût fixe d'ingénierie humaine (grammaire, prompts, solveurs). Un système n'est supérieur que s'il domine l'**enveloppe** des baselines sur les deux axes ou s'il étend la frontière de Pareto de manière non dominée.
- **Règle de décision (`HYPOTHÈSE`) :** Supériorité retenue uniquement si la borne inférieure de l'IC 95 % (`illustratif`) sur $\mathbb{E}_P[U_{\text{multi}} - \max_{b \in \mathcal{B}} U_b]$ dépasse un seuil pratique pré-enregistré $\delta_{\min}$ (`illustratif`), après correction de Holm ($\alpha = 0{,}01$, `illustratif`), sur au moins deux familles de problèmes indépendantes (`illustratif`).
- **Comparaisons d'attribution (`HYPOTHÈSE`) :** Ajouter quatre ablations indispensables au même budget total : (1) *Best-of-$K$* indépendant du meilleur modèle unique (teste le pur calcul au temps d'inférence) ; (2) auto-raffinement séquentiel d'un seul modèle (teste la multiplicité d'agents) ; (3) ensemble hétérogène indépendant sans dialogue (sépare diversité de modèles et débat) ; (4) **critique placebo** (retour générique ou permuté, sépare contenu critique et simple perturbation stochastique).

- **Établi vs conjecture :** Établi (`RAPPORTÉ`) : bootstrap en grappes (Efron & Tibshirani, 1993) et contrôle FWER de Holm (1979). Conjecture (`HYPOTHÈSE`) : choix de la frontière de Pareto bidimensionnelle (FLOPs vs appels oracle) comme proxy suffisant des coûts réels.
- **Où le cadrage est faux :** Comparer « multi-agents » au « meilleur modèle unique au même budget » est ambigu sans spécifier *Best-of-$K$* et critique placebo ; de plus, égaliser uniquement les dollars masque la différence d'échelle d'appels oracle entre un énumérateur ($10^6$ appels bon marché, `illustratif`) et un LLM ($10^2$ appels, `illustratif`).
- **Confiance :** `0,85` (`HYPOTHÈSE`, `illustratif`).
- **Références :** Efron, B., & Tibshirani, R. J. (1993), *An Introduction to the Bootstrap*, Chapman & Hall ; Holm, S. (1979), *A Simple Sequentially Rejective Multiple Test Procedure*, Scandinavian Journal of Statistics.

#### 4. Choix des problèmes
Par les théorèmes *No Free Lunch* (`RAPPORTÉ`, Wolpert & Macready, 1997), aucune méthode ne domine sur tous les paysages de recherche. La conjecture structurelle (`HYPOTHÈSE`) est que le régime où des agents LLM pourraient battre à la fois l'énumérateur et le modèle unique se situe à l'intersection de quatre propriétés mesurables *a priori* : (i) espace combinatoire trop grand pour l'énumération exhaustive ; (ii) asymétrie vérification $\ll$ génération ; (iii) structure sémantique/compositionnelle permettant l'analogie (contrairement à un bruit cryptographique sans gradient) ; (iv) bassins locaux trompeurs où le tirage direct échoue.

**Tester ce choix au lieu de le présupposer (`HYPOTHÈSE`) :** Construire une taxonomie pré-enregistrée de descripteurs de paysages (facteur de branchement, coût d'énumération, entropie d'échec du modèle unique, modularité), puis échantillonner de façon **stratifiée** sur des familles de problèmes **hors échantillon** incluant des **régimes contrôles négatifs** (où le multi-agents est *prédit perdant* : petits espaces combinatoires et aiguilles aléatoires sans structure). Tester l'interaction $\text{Système} \times \text{Régime}$ : la théorie de sélection n'est corroborée que si elle prédit *à la fois* où le système gagne et où il perd.

- **Établi vs conjecture :** Établi (`RAPPORTÉ`) : pas de domination universelle sans biais inductif adapté (Wolpert & Macready, 1997). Conjecture (`HYPOTHÈSE`) : existence d'une zone non vide où l'avantage sémantique des LLM survit face aux solveurs symboliques spécialisés.
- **Où le cadrage est faux :** Chercher « où les idées rares et profondes sont plus probables » sans imposer de régimes négatifs pré-enregistrés transforme le protocole en machine à *cherry-picking*.
- **Confiance :** `0,75` (`HYPOTHÈSE`, `illustratif`).
- **Références :** Wolpert, D. H., & Macready, W. G. (1997), *No Free Lunch Theorems for Optimization*, IEEE Transactions on Evolutionary Computation.

#### 5. Rétroaction (feedback) et étanchéité de la mesure
Séparer strictement trois couches d'information (`HYPOTHÈSE`) :
1. **Autorisé en cours de recherche (boucle interne) :** validité syntaxique/type/noyau (binaire), erreur ou contre-exemples sur un **split d'entraînement interne** distinct du régime d'évaluation, et critiques internes entre agents.
2. **Strictement retenu (coffre d'évaluation scellé) :** régimes OOD/interventionnels mesurant $D_{\text{ext}}$, suite gelée de théorèmes aval (compression), estimateur de rareté $R_{\mathcal{Q}_0}$ (retourner la rareté en cours de recherche pousse directement les agents vers des formulations baroques — effet Goodhart), et étiquettes d'audit humain/PPI.
3. **Contrôle de la boucle externe (équipe d'ingénierie) :** réutiliser la même suite d'évaluation pour ajuster les prompts et agents détruit la validité statistique (`RAPPORTÉ`, Dwork et al., 2015). Imposer un coffre verrouillé à usage limité ou un mécanisme de *Reusable Holdout* (`RAPPORTÉ`, Dwork et al., 2015) + régénération procédurale par graines cryptographiques engagées avant chaque campagne.

- **Établi vs conjecture :** Établi (`RAPPORTÉ`) : perte de validité sous analyse adaptative répétée et protection par holdout réutilisable (Dwork et al., 2015). Conjecture (`HYPOTHÈSE`) : suffisance de la séparation entraînement/OOD contre le contournement subtil par des agents dotés de connaissances pré-entraînées.
- **Où le cadrage est faux :** La question ne traite que le feedback retourné au générateur pendant la recherche, en omettant la fuite tout aussi grave de la boucle externe (les chercheurs optimisant l'architecture sur le harnais).
- **Confiance :** `0,85` (`HYPOTHÈSE`, `illustratif`).
- **Références :** Dwork, C., Feldman, V., Hardt, M., Pitassi, T., Reingold, O., & Roth, A. (2015), *The reusable holdout: Preserving validity in adaptive data analysis*, Science.

#### 6. Validation préalable du harnais
Avant toute campagne coûteuse, le harnais doit démontrer cinq propriétés métrologiques (`HYPOTHÈSE`) : (1) **Sensibilité sur contrôles positifs plantés** (séparer les 4 quadrants rareté $\times$ profondeur) ; (2) **Calibrage nul A/A** (deux copies identiques d'une baseline doivent produire un effet nul et un taux de faux positifs $\le \alpha$) ; (3) **Résistance adversariale** (des générateurs triviaux — bruit syntaxique, polynômes surajustés, paraphrases verbeuses — doivent scorer bas) ; (4) **Audit de biais du juge et de fuite temporelle** (si applicables) ; (5) **Décomposition de variance** (inter-problèmes vs inter-graines) vérifiant que l'effet minimal détectable est compatible avec le budget.

- **Établi vs conjecture :** Établi (`RAPPORTÉ`) : principes standards de calibrage A/A et contrôle des faux positifs (Benjamini & Hochberg, 1995 ; Holm, 1979). Conjecture (`HYPOTHÈSE`) : qu'une batterie adversariale conçue *a priori* anticipe les modes de contournement réels d'agents LLM.
- **Où le cadrage est faux :** L'énoncé traite le harnais comme un outil à valider une fois pour toutes avant de courir ; en pratique, un harnais face à des optimiseurs puissants doit être ré-audité de manière adversariale après toute hausse de capacité.
- **Confiance :** `0,85` (`HYPOTHÈSE`, `illustratif`).
- **Références :** Benjamini, Y., & Hochberg, Y. (1995), *Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing*, Journal of the Royal Statistical Society: Series B ; Holm, S. (1979), réf. citée.

#### 7. Plan expérimental ordonné, critères d'arrêt et tailles d'échantillon
Ordre strict du moins cher au plus cher, avec portes d'arrêt séquentielles (*Go/No-Go*, `RAPPORTÉ`, Wald, 1945) détaillées dans la section (b) : **E1** (calibration du harnais sur vérités plantées et contrôles adversariaux, purement CPU/petit modèle) $\to$ **E2** (audit de biais/style-swap et contamination) $\to$ **E3** (test de la taxonomie de problèmes sur petits modèles) $\to$ **E4** (test d'étanchéité du feedback vs Goodhart) $\to$ **E5** (duel principal multi-agents vs enveloppe des baselines à pleine échelle) $\to$ **E6** (ablations d'attribution causale).

**Tailles d'échantillon (`HYPOTHÈSE`, `illustratif`) :**
- Pour détecter un effet standardisé apparié $d = 0{,}50$ sur une métrique continue $U(P,B)$ avec puissance $0{,}80$ et $\alpha_{\text{Holm}} = 0{,}01$ : $N \approx 50\text{–}60$ problèmes indépendants par famille (`illustratif`).
- Pour un taux binaire d'événements rares passant de $p_0 = 0{,}05$ à $p_1 = 0{,}15$ (test apparié exact) : $N \approx 120\text{–}150$ problèmes par famille (`illustratif`). Si $p_0 < 10^{-3}$, la puissance s'effondre ($N > 10^4$, `illustratif`) : il faut alors mesurer la distribution continue de profondeur conditionnée à un budget fixé, et non le seul comptage binaire.
- **Critère d'arrêt précoce :** arrêt immédiat (futilité) si E1 ou E2 échoue ; en E5, test séquentiel intermédiaire à $50\,\%$ des problèmes (`illustratif`) avec arrêt pour futilité si la puissance conditionnelle tombe sous $0{,}10$ (`illustratif`).

- **Établi vs conjecture :** Établi (`RAPPORTÉ`) : tests séquentiels et ordres de grandeur de puissance statistique (Wald, 1945). Conjecture (`HYPOTHÈSE`) : taille d'effet attendue $d = 0{,}50$ et variance inter-problèmes réelle (inconnues avant E1).
- **Où le cadrage est faux :** Demander les tailles d'échantillon avant d'avoir mesuré la variance inter-problèmes et le taux de base $p_0$ impose des chiffres provisoires qui doivent être recalibrés après l'étape pilote E1.
- **Confiance :** `0,75` (`HYPOTHÈSE`, `illustratif`).
- **Références :** Wald, A. (1945), *Sequential Tests of Statistical Hypotheses*, The Annals of Mathematical Statistics ; Platt, J. R. (1964), *Strong Inference*, Science.

#### 8. Limites, mauvaise position de la cible et faisabilité
- **Hors de portée de tout harnais automatisé (`HYPOTHÈSE`) :** (i) la création d'ontologies ou de changements de représentation (tout harnais fige une grammaire ou un vérificateur qui exclut les idées redéfinissant les observables) ; (ii) la fécondité scientifique à long terme dépendant d'instruments futurs ; (iii) les domaines sans oracle exécutable, formel ou expérimental rapide.
- **Preuves que la cible est mal posée (`HYPOTHÈSE`) :** (1) *Instabilité de représentation* : deux encodages mathématiquement isomorphes d'une même famille de problèmes produisent une corrélation de rang de Spearman $\rho < 0{,}30$ (`illustratif`) sur la rareté $R$ ; (2) *Effondrement rareté/profondeur* : aucune métrique OOD ne sépare les vérités plantées des surajustements rares dès que le décalage de distribution varie ; (3) *Disjonction des références* : l'intersection des idées rares pour l'énumérateur ET pour le modèle unique est vide.
- **Preuves qu'aucun harnais de ce type n'est faisable (`HYPOTHÈSE`) :** (1) Explosion de la taille d'échantillon ($N > 10^4$ problèmes non contaminés nécessaires, `illustratif`, hors d'atteinte hors synthétique) ; (2) En domaine ouvert sans oracle mécanique, largeur des intervalles PPI supérieure à tout effet réaliste sauf audit humain quasi exhaustif (annulant l'intérêt du harnais).

- **Établi vs conjecture :** Établi (`RAPPORTÉ`) : dépendance de la complexité descriptive au langage de codage jusqu'à une constante dépendant du traducteur (Solomonoff, 1964) et limites de la mesure adaptative (Dwork et al., 2015). Conjecture (`HYPOTHÈSE`) : seuil empirique à partir duquel l'instabilité de codage invalide en pratique les classements entre systèmes.
- **Où le cadrage est faux :** La question suppose qu'un harnais peut trancher globalement si un système « trouve des idées rares et profondes ». En réalité, il ne peut trancher qu'une **projection bornée** de cette affirmation dans des univers à ontologie fixée et vérification peu coûteuse.
- **Confiance :** `0,85` (`HYPOTHÈSE`, `illustratif`).
- **Références :** Solomonoff, R. J. (1964), *A Formal Theory of Inductive Inference. Part I*, Information and Control ; Dwork, C. et al. (2015), réf. citée.

---

### (b) Expériences décisives en inférence forte ($H_A$ contre $H_B$)

Toutes les expériences appliquent l'inférence forte (`RAPPORTÉ`, Platt, 1964) : deux hypothèses exclusives, un contrôle négatif obligatoire, et une falsification bilatérale. Tous les seuils et $N$ sont `illustratif`.

1. **E1 — Métrologie du harnais : séparation 4 quadrants (synthétique + Lean 4 + exécutable)**
   - **$H_A$** : Le couple $(R_{\mathcal{Q}_0}, D_{\text{ext}})$ sépare les solutions plantées *narrow & deep* des trois classes leurres appariées (*rare & shallow*, *common & deep*, *common & shallow*).
   - **$H_B$** : Le harnais confond profondeur avec rareté syntaxique ou ajustement en distribution.
   - **Métrique & seuil (`illustratif`) :** $\text{AUROC}_{\text{target vs leurres}} \ge 0{,}85$ ET $\text{FPR}_{\text{rare-shallow}} \le 0{,}05$ sur $N = 100$ problèmes synthétiques/formels appariés.
   - **Contrôle négatif :** Générateurs adversariaux triviaux (mutation syntaxique aléatoire, splines/polynômes surajustés en distribution, lemmes gonflés redondants) + test A/A (deux graines identiques).
   - **Falsification :** $\text{AUROC} < 0{,}85$ ou $\text{FPR}_{\text{rare-shallow}} > 0{,}05$ ou taux de rejet A/A $> 0{,}05$ falsifie $H_A$ (arrêt immédiat du projet avant tout run LLM coûteux) ; le dépassement simultané de tous les seuils falsifie $H_B$.

2. **E2 — Invariance de représentation, biais du juge (PPI) et contamination**
   - **$H_A$** : Le classement par $R_{\mathcal{Q}_0}$ reste stable sous recodage isomorphe ($\rho \ge 0{,}70$), le juge corrigé PPI résiste au *style-swap* ($|\delta_{\text{style}}| \le 0{,}05\,\sigma$) et la rétrodiction/synthèse ne présente pas de fuite mémorielle ($\Delta_{\text{mém}} \le 0{,}02$, tout `illustratif`).
   - **$H_B$** : La cible dépend arbitrairement du codage, ou le biais de style/contamination excède les seuils et masque tout effet réel.
   - **Métrique & seuil (`illustratif`) :** Corrélation de Spearman $\rho$ entre deux encodages isomorphes ($N = 80$ problèmes) ; décalage de score sous permutation de style entre système et baseline ($N = 200$ paires) ; écart de performance entre problèmes isomorphes fraîchement renommés et formulations canoniques.
   - **Contrôle négatif :** Problèmes volontairement fuis/canoniques (doivent déclencher l'alerte de contamination) et paires au contenu identique mais au style rhétorique opposé (doivent donner $\delta_{\text{style}} \approx 0$).
   - **Falsification :** $\rho < 0{,}70$ ou $|\delta_{\text{style}}| > 0{,}05\,\sigma$ ou $\Delta_{\text{mém}} > 0{,}02$ falsifie $H_A$ (cible mal posée ou juge/rétrodiction disqualifiés) ; la satisfaction conjointe des trois critères falsifie $H_B$.

3. **E3 — Test prédictif du choix de problèmes (interaction $\text{Système} \times \text{Régime}$)**
   - **$H_A$** : La taxonomie pré-enregistrée prédit à l'avance les familles hors échantillon où les agents LLM surpassent les baselines, avec interaction positive $\Delta_{\text{fertile}} - \Delta_{\text{négatif}} \ge \delta_3 = 0{,}30\,\sigma$ ($p_{\text{Holm}} < 0{,}01$, `illustratif`).
   - **$H_B$** : L'avantage présumé par région ne généralise pas hors échantillon ($\Delta_{\text{fertile}} - \Delta_{\text{négatif}} \le 0$ ou IC 95 % incluant 0).
   - **Métrique & seuil (`illustratif`) :** Interaction appariée sur 4 familles de problèmes nouvelles (2 prédites fertiles, 2 prédites négatives : petit combinatoire et piège sans structure), $N = 40$ problèmes/famille.
   - **Contrôle négatif :** Régime « aiguille sans structure » (espace permuté aléatoirement) où aucun système ne doit battre le tirage aléatoire.
   - **Falsification :** Absence d'interaction positive généralisable falsifie $H_A$ (hypothèse de région fertile réfutée) ; interaction positive accompagnée d'un échec prédit sur les régimes négatifs falsifie $H_B$.

4. **E4 — Étanchéité du feedback adaptatif contre la loi de Goodhart**
   - **$H_A$** : Le feedback autorisé (validité + erreur sur split interne) accroît la profondeur scellée $D_{\text{OOD}}$ ($\Delta D_{\text{OOD}} \ge 0{,}25\,\sigma$, `illustratif`) sans creuser l'écart de surajustement au-delà d'un plafond ($\Delta(D_{\text{train}} - D_{\text{OOD}}) \le 0{,}15\,\sigma$, `illustratif`).
   - **$H_B$** : Le feedback n'améliore que le score interne tout en laissant $D_{\text{OOD}}$ nul ou décroissant (Goodharting).
   - **Métrique & seuil (`illustratif`) :** Contraste apparié (avec vs sans feedback interne) sur $N = 60$ problèmes synthétiques/exécutables.
   - **Contrôle négatif :** Variante « fuite délibérée » recevant le score de rareté $R$ pendant la recherche (doit exhiber une hausse de $R$ accompagnée d'une chute ou stagnation de $D_{\text{OOD}}$).
   - **Falsification :** $\Delta D_{\text{OOD}} \le 0$ avec $\Delta D_{\text{train}} > 0$ falsifie $H_A$ ; gain OOD net et contrôlé falsifie $H_B$.

5. **E5 — Duel principal à double contrainte budgétaire : multi-agents vs enveloppe des baselines**
   - **$H_A$** : Le système multi-agents bat l'enveloppe $\max(\text{Single-LLM Best-of-}K,\; \text{Énumérateur mécanique},\; \text{Aléatoire})$ sur $U(P,B)$ à budget FLOPs/USD égal ET à budget d'appels oracle égal (borne inf. IC 95 % cluster-bootstrap $> \delta_5 = 0{,}20\,\sigma$, $p_{\text{Holm}} < 0{,}01$, `illustratif`, sur $\ge 2$ familles indépendantes).
   - **$H_B$** : Le système multi-agents est égalé ou battu par au moins une baseline de l'enveloppe sur l'un des deux axes budgétaires ou sur une famille indépendante.
   - **Métrique & seuil (`illustratif`) :** AUDC sur $U(P,B)$ et taux de succès conjoint, $N = 60$ problèmes indépendants par famille $\times$ 2 familles validées en E3 (120 problèmes au total), avec test de futilité à $N = 60$.
   - **Contrôle négatif :** Problèmes du régime négatif (petit espace formel/combinatoire) où l'énumérateur doit battre les LLM, vérifiant l'absence de biais de configuration en faveur du multi-agents.
   - **Falsification :** Échec à dominer l'enveloppe sur les deux axes ou sur les deux familles falsifie $H_A$ ; domination robuste falsifie $H_B$.

6. **E6 — Attribution causale par ablations (interaction critique vs diversité/re-tirage)**
   - **$H_A$** : Le protocole multi-agents avec critique ciblée surpasse à la fois l'ensemble hétérogène indépendant sans dialogue et la critique placebo (budget identique) d'au moins $\delta_6 = 0{,}15\,\sigma$ ($p_{\text{Holm}} < 0{,}01$, `illustratif`).
   - **$H_B$** : L'ensemble indépendant ou la critique placebo égale ou bat la critique ciblée (l'effet de E5 provient de la diversité ou du ré-échantillonnage, non du dialogue critique).
   - **Métrique & seuil (`illustratif`) :** Différence appariée sur $U(P,B)$ sur les mêmes $N = 120$ problèmes que E5 (exécuté uniquement si E5 valide $H_A$).
   - **Contrôle négatif :** Critique permutée (commentaires d'un autre problème injectés comme feedback), qui doit rester $\le$ au multi-agents réel et $\approx$ au ré-échantillonnage simple.
   - **Falsification :** Écart $\le \delta_6$ ou IC 95 % incluant 0 falsifie $H_A$ ; supériorité nette sur les deux ablations falsifie $H_B$.

---

### (c) Validation minimale de chaque instrument nommé dans la question

Toutes les cibles numériques de détection (TPR) et de fausses alertes (FPR) sont marquées `illustratif` (elles définissent le cahier des charges minimal avant validation).

| Instrument nommé | Mesure minimale de fonctionnement | TPR / FPR cibles (`illustratif`) | Cas honnêtes appariés (contrôles de même surface) | Vérifications mécaniques à battre |
|---|---|---|---|---|
| **1. Métrique « narrow » ($R_{\mathcal{Q}_0}$)** | Sensibilité aux solutions rares plantées + invariance aux paraphrases/renommages. | $\text{TPR} \ge 0{,}85$ ; $\text{FPR} \le 0{,}05$ | Idées courantes **paraphrasées/renommées** (même classe sémantique, syntaxe rare) appariées aux idées véritablement rares. | Distance d'édition brute, rareté n-gramme/perplexité sans canonisation. |
| **2. Métrique « deep » ($D_{\text{ext}}$)** | Discrimination de la conséquence OOD/compression aval contre bruit rare et clichés. | $\text{TPR} \ge 0{,}90$ ; $\text{FPR} \le 0{,}05$ | Leurres **rares mais creux** de même longueur de description et même erreur en distribution (surajustements, tautologies rares). | Erreur sur split d'entraînement, log-vraisemblance en distribution, longueur brute de formule/preuve. |
| **3. Juge LLM (+ correcteur PPI)** | Accord calibré avec oracle externe + invariance au style (IC 95 % PPI couvrant le vrai effet $\ge 95\,\%$, `illustratif`). | $\text{TPR} \ge 0{,}80$ ; $\text{FPR} \le 0{,}10$ ; $|\delta_{\text{style}}| \le 0{,}05\,\sigma$ | Idées profondes en **style sec/maladroit** appariées à des idées fausses ou triviales en **style académique poli** (*style-swap*). | Heuristique longueur + perplexité ; score brut du juge LLM sans correction PPI. |
| **4. Monde synthétique (vérité plantée)** | Détection de la loi/invariant planté sans faux positifs sur mondes nuls. | $\text{TPR} \ge 0{,}95$ ; $\text{FPR} \le 0{,}02$ | **Mondes nuls appariés** ayant les mêmes marginales et corrélations de bas ordre mais aucun invariant profond planté. | Régression polynomiale/arbres par force brute ; recherche aléatoire de caractéristiques. |
| **5. Rétrodiction à coupure temporelle** | Capacité à rejeter les fuites mémorielles et à distinguer raisonnement vs rappel. | Détection fuite $\ge 0{,}90$ ; $\text{FPR} \le 0{,}05$ | Problèmes **pré-coupure renommés/masqués** appariés à des variantes **post-coupure synthétiques** de difficulté égale. | Recherche par similarité lexicale (TF-IDF / recouvrement n-grammes pré-coupure) ; contrôle zéro-shot sans raisonnement. |
| **6. Preuve formelle (vérificateur + compression aval)** | Zéro faux positif de validité + détection des lemmes réellement réutilisables. | Validité $\text{FPR} = 0$ (`VÉRIFIÉ` modulo noyau) ; utilité $\text{TPR} \ge 0{,}85$, $\text{FPR} \le 0{,}05$ | **Lemmes triviaux gonflés** ou redondants de même nombre de tactiques/tokens appariés à des lemmes clés de bibliothèques gelées. | Tactiques automatiques / solveurs SMT (`simp`, `omega`, marteaux ATP) et énumérateur borné à budget CPU égal. |
| **7. Tests exécutables / simulateur** | Détection de la généralisation interventionnelle et rejet du *reward hacking*. | $\text{TPR} \ge 0{,}90$ ; $\text{FPR} \le 0{,}05$ | **Interpolateurs / tables de correspondance** atteignant une erreur d'entraînement identique mais échouant sous intervention OOD. | Validation croisée en distribution ; fuzzing aléatoire de paramètres. |
| **8. Baselines (aléatoire, énumérateur, modèle unique)** | Reproductibilité inter-graines et exactitude de la comptabilité budget/oracle (écart $< 2\,\%$, `illustratif`). | Faux positif A/A $\le 0{,}05$ ; couverture budget $= 100\,\%$ | Deux exécutions identiques de la même baseline sur graines distinctes (contrôle A/A) + problèmes calibrés de difficulté connue. | Vérificateur déterministe de budget (compteur exact de tokens, FLOPs et appels oracle) ; tirage uniforme pur. |
| **9. Sélecteur de problèmes & garde-fou de feedback** | Prédiction hors échantillon des régimes fertiles + détection du surajustement adaptatif. | $\text{TPR}_{\text{Goodhart}} \ge 0{,}85$ ; $\text{FPR} \le 0{,}05$ | Familles de problèmes de **même domaine/longueur** mais paysages trompeurs ; agents surajustant bruyamment le split interne. | Tirage uniforme de problèmes ; réutilisation naïve du même jeu d'évaluation sans coffre scellé. |

---

### (d) Ancrage matériel (entièrement `illustratif`)

L'ensemble des choix modèles, volumes de calcul et coûts ci-dessous est marqué **`illustratif`** (aucune contrainte matérielle n'étant fournie dans les faits ; l'existence des familles de modèles ouverts citées est `RAPPORTÉ`).

- **Modèles ouverts recommandés (reproductibilité, contrôle des graines, zéro dérive d'API) :**
  - *Niveau calibration / petits agents (E1–E4) :* modèle ouvert ~7–8 milliards de paramètres (familles open-weights type Llama-3.1-8B-Instruct ou Qwen2.5-7B-Instruct, `RAPPORTÉ`), exécutable en FP16/BF16 sur 1 GPU 24–80 Go (`illustratif`).
  - *Niveau pleine échelle (E5–E6) :* modèle ouvert ~70–72 milliards de paramètres (familles open-weights type Llama-3.1-70B-Instruct ou Qwen2.5-72B-Instruct, `RAPPORTÉ`) + un second modèle ouvert d'architecture/entraînement distinct de taille comparable pour l'ablation « ensemble hétérogène » de E6 (`illustratif`).
  - *Environnement mécanique / oracles :* nœuds CPU multi-cœurs pour vérificateur formel (Lean 4), énumérateur symbolique/SMT et simulateurs Python en bac à sable isolé (sans accès réseau).

- **Budget de calcul et coûts estimés par phase (cloud GPU standard à ~2,50 USD/h par H100 80 Go et ~0,05 USD/h par vCPU, tout `illustratif`) :**

| Phase | Contenu et échelle (`illustratif`) | Calcul estimé (`illustratif`) | Coût estimé (`illustratif`) | Porte d'arrêt (*Go/No-Go*) |
|---|---|---|---|---|
| **E1** | Calibration harnais : 100 problèmes (synthétique + Lean 4 + exécutable), contrôles adversariaux & A/A (CPU + modèle 8B) | 500 vCPU-h + 20 H100-h | ~75 USD | Échec $\text{AUROC}/ \text{FPR}$ ou A/A $\implies$ arrêt immédiat |
| **E2** | Invariance recodage (80 prob.), *style-swap* (200 paires), audit PPI & fuite (modèle 8B + 70B léger) | 200 vCPU-h + 60 H100-h | ~160 USD | $\rho < 0{,}70$ ou $|\delta_{\text{style}}| > 0{,}05\,\sigma$ $\implies$ arrêt / retrait du juge |
| **E3** | Taxonomie de problèmes : 4 familles $\times$ 40 problèmes (modèle 8B + énumérateur) | 2 000 vCPU-h + 120 H100-h | ~400 USD | Pas d'interaction $\text{Système}\times\text{Régime}$ $\implies$ révision cadrage |
| **E4** | Test feedback vs Goodhart : 60 problèmes $\times$ 3 conditions (sans, autorisé, fuite rareté) | 800 vCPU-h + 100 H100-h | ~290 USD | Goodhart avéré ($\Delta D_{\text{OOD}} \le 0$) $\implies$ retrait du feedback |
| **E5** | Duel principal : 120 problèmes $\times$ 4 systèmes (multi-agents, Best-of-$K$ 70B, énumérateur, aléatoire), ~200k tokens/problème/système LLM | 10 000 vCPU-h + 900 H100-h | ~2 750 USD | Arrêt futilité à $50\,\%$ (~1 400 USD) si puissance cond. $< 0{,}10$ |
| **E6** | Ablations d'attribution (ensemble hétérogène, auto-raffinement, critique placebo) sur les 120 problèmes (conditionnel à E5) | 3 000 vCPU-h + 750 H100-h | ~2 025 USD | Non exécuté si E5 réfute $H_A$ |
| **Total plafonné** | **Campagne complète E1–E6 (hors temps humain d'audit PPI : ~30–50 h d'experts si juge utilisé)** | **~16 500 vCPU-h + ~1 950 H100-h** | **~5 700 USD** (~925 USD avant E5) | **84 % du budget protégé par les portes E1–E4** |

Ce découpage garantit que l'échec du harnais (E1–E2), l'absence de régime favorable (E3) ou la dérive Goodhart (E4) sont détectés pour moins d'un millier de dollars (`illustratif`), avant d'engager la dépense des comparaisons à grande échelle (E5–E6).

FIN-DE-CELLULE