### Mise au point préalable sur les annonces publiques récentes

Avant d'aborder votre programme, voici l'état factuel des annonces médiatiques ou virales sur les découvertes mathématiques par IA :

*   **Hypothèse de Riemann :** **Rien n'est établi.** Aucune avancée vérifiée, publiée ou acceptée par la communauté n'a été produite par IA. Les annonces récentes sur les réseaux sociaux relèvent soit d'hallucinations de modèles de langage, soit d'approximations numériques connues des zéros de la fonction zêta sans valeur de preuve.
*   **Équations de Navier-Stokes (et d'Euler) :** **Partiellement établi en analyse numérique, non établi pour le problème du millénaire.** Des réseaux de neurones informés par la physique (*PINNs*) ont été utilisés (notamment par Yongji Wang et al., *Physical Review Letters* / travaux avec DeepMind, 2022-2024, identifiant arXiv : pas sûr) pour découvrir numériquement des profils d'explosion auto-similaires (*blow-up*) pour certaines équations de la mécanique des fluides. Par ailleurs, Jiajie Chen et Thomas Y. Hou ont prouvé une explosion en temps fini pour Euler 3D avec bord (*arXiv:2210.07191*, 2022), mais il s'agit d'une preuve assistée par ordinateur classique (arithmétique d'intervalles rigoureuse), **pas** d'une découverte par modèle de langage. Le problème de régularité globale de Navier-Stokes 3D reste ouvert.
*   **« Des dizaines de problèmes ouverts résolus » :** **Faux pour les modèles de langage.** Ce qui est établi :
    1.  **FunSearch** (Romera-Paredes et al., *Nature*, 2023) a amélioré des bornes inférieures constructives connues sur le problème du *Cap Set* et trouvé des heuristiques de *bin-packing*. C'est une amélioration de borne sur un problème précis, pas la résolution de dizaines de problèmes.
    2.  **AlphaGeometry** (Trinh et al., *Nature*, 2024) et **AlphaProof** (DeepMind, 2024) ont résolu des problèmes d'Olympiades Internationales de Mathématiques (OIM). Ce sont des problèmes difficiles mais **fermés** (dont la solution existe et est connue en quelques pages de mathématiques de niveau lycée/licence), pas des problèmes de recherche ouverts.
    3.  **Réfutations en théorie des graphes** (Wagner, 2021) : un algorithme d'apprentissage par renforcement (sans LLM) a trouvé des contre-exemples finis réfutant plusieurs conjectures ouvertes issues du système *Graffiti*.

---

### 1. Ce qu'un expert du domaine ferait ici, et qu'on ne demande pas

Votre architecture actuelle (proposeurs, juges LLM, arbitre Lean en préparation, budget de ~300 $ par course) fonce droit dans deux murs classiques : **l'impasse de la théorie de la mesure dans Lean** et **la triche sémantique (*specification gaming*) face aux juges**. Voici ce qu'un expert ferait immédiatement à la place :

1.  **Supprimer les « juges » à base de modèles de langage pour évaluer la validité mathématique.** Un LLM juge est incapable de détecter un passage à la limite illicite, un échange $\sup/\inf$ sans compacité, ou une dépendance circulaire subtile dans une filtration. Pire : dans une boucle évolutionnaire, les modèles proposeurs apprennent très vite à produire du texte mathématique d'apparence érudite (invoquant le théorème de minimax de Sion ou le lemme de Neyman-Pearson) qui trompe systématiquement le juge LLM. L'unique juge intermédiaire avant Lean doit être un **exécuteur de code déterministe** (Python/SageMath/Z3 en arithmétique rationnelle exacte $\mathbb{Q}$).
2.  **Éviter à tout prix la théorie des probabilités générale de `Mathlib4` pour la phase de découverte.** Formaliser une borne d'impossibilité (type méthode de Le Cam, lemme de Fano ou d'Assouad) ou un arrêt optimal (théorème d'arrêt de Doob, filtrations, mesure de Radon-Nikodym) dans `Mathlib.Probability` demande des semaines de travail à un expert humain de Lean 4 à cause de la lourdeur des classes de types (`MeasurableSpace`, `IsProbabilityMeasure`, `Integrable`). Avec 300 $ de budget de calcul, un agent LLM échouera à 100 % sur les coercions de types avant d'avoir posé le moindre argument mathématique.
3.  **Algébriser et discrétiser le domaine avant de lancer l'organisme.** Vos quatre sujets (impossibilité de détection, corrélation adverse, détection séquentielle, garanties de moniteurs) possèdent une propriété fondamentale : par **dualité convexe** (programmation linéaire ou semi-définie), leurs bornes extrémales sur des espaces d'états finis à $N$ éléments s'expriment comme des identités algébriques ou des sommes de carrés de polynômes (SOS). L'expert réduit le problème analytique continu à la recherche d'un **certificat dual fini** (un couplage fini explicite ou un polynôme de pondération), laisse l'IA chercher ce certificat en Python, et n'utilise Lean que pour vérifier l'identité algébrique finale par les tactiques `linarith`, `positivity` ou `norm_num`.
4.  **Verrouiller l'énoncé formel contre la « preuve par vacuité ».** Quand on demande à un LLM de prouver un théorème nouveau dans Lean, le chemin de moindre résistance qu'il trouve consiste à glisser dans les hypothèses une condition subtilement contradictoire (par exemple, un espace de probabilité vide, ou deux paramètres $p + q > 1$ incompatibles avec une définition amont), puis à conclure n'importe quoi par `False.elim`. L'expert impose un test automatique de **non-vacuité** : tout théorème généré doit être accompagné de la preuve formelle d'existence d'un objet concret satisfaisant toutes ses hypothèses.

---

### 2. Les données brutes à prendre au départ

Au lieu de résumés d'articles ou de manuels synthétiques, un système de découverte a besoin de traces d'exécution, d'arbres syntaxiques et de banques d'objets extrémaux :

*   **Les arbres syntaxiques abstraits (AST) et états de preuve de `Mathlib4` :** Extraits directement via **LeanDojo** ou **Pantograph** sur les sous-dossiers `Mathlib/Analysis/Convex/`, `Mathlib/InformationTheory/` et `Mathlib/Probability/Martingale/`. Ce qui compte, ce sont les paires `(état_tactique_avant, tactique, état_tactique_après)` et les graphes de dépendances des lemmes.
*   **Les fichiers sources `.tex` bruts de la littérature de référence :** Les sources LaTeX (extraites d'arXiv) des travaux sur la probabilité théorique par les jeux et les *e-valeurs* (Glenn Shafer, Vladimir Vovk, Aaditya Ramdas), sur les bornes minimax non-paramétriques (Alexandre Tsybakov, Yihong Wu) et sur les bornes de dépendance extrémale (Paul Embrechts, Giovanni Puccetti sur la *robust risk aggregation*). On en extrait les chaînes d'inégalités brutes (`\begin{align} ... \end{align}`), pas le texte narratif.
*   **Des banques de matrices de couplage et de copules extrémales :** Des jeux de données bruts (en fractions exactes) de distributions jointes qui maximisent la fausse alerte ou minimisent la puissance de détection sous contraintes marginales (bornes de Fréchet-Hoeffding discrètes, matrices bistochastiques extrémales pour $N \in \{2, \dots, 20\}$ calculées par programmation linéaire exacte).
*   **Votre archive interne de tentatives échouées (les « journaux de mort ») :** Pas un résumé de « ce qui n'a pas marché », mais les traces brutes contenant : (a) le programme ou le lemme proposé, (b) le contre-exemple exact (le « monde planté ») qui l'a réfuté, ou (c) le message d'erreur exact du noyau Lean 4 à la ligne où la preuve a cassé. C'est ce signal négatif précis qui permet de mettre à jour les contraintes de recherche.

---

### 3. Les méthodes et outils précis : ce qui a marché, ce que cela suppose, où cela échoue

Voici l'analyse technique des architectures existantes :

#### A. Recherche dans l'espace des programmes et sélection évolutionnaire
*   **Travaux :** *Mathematical discoveries from program search with large language models* (**FunSearch**, Romera-Paredes et al., *Nature* 2023, arXiv:2312.02475 — *note : numéro arXiv à vérifier, publié dans Nature vol. 625*). Voir aussi **PatternBoost** (*PatternBoost: Constructions in Mathematics with a Little Help from AI*, Charton, Ellenberg, Wagner, Williamson, 2024, arXiv:2411.00566).
*   **Ce que cela suppose :** Que le problème mathématique se ramène à trouver un objet discret optimal, que l'on puisse coder un **évaluateur déterministe rapide** $E(x) \in \mathbb{R}$ qui note la qualité d'un candidat en quelques millisecondes, et que le paysage de fitness soit progressif (des solutions partielles pour $N=4, 5, 6$ donnent un gradient vers la structure générale).
*   **Ce que cela a donné :** Nouvelles bornes inférieures pour les *Cap Sets* et constructions de graphes extrémaux. Le LLM ne cherche pas l'objet directement ; il fait évoluer une fonction Python `priority(item)` qui construit l'objet gloutonnement.
*   **Où cela échoue :** Échec total si le paysage de récompense est binaire (0 si la preuve est fausse, 1 si elle est vraie) ou si l'évaluation d'un candidat est elle-même NP-difficile (ce qui est souvent le cas pour calculer le pire cas d'un adversaire continu).

#### B. Découverte de contre-exemples par apprentissage / génération guidée
*   **Travaux :** *Constructions in combinatorics via neural networks* (Adam Zsolt Wagner, 2021, **arXiv:2104.14516**).
*   **Ce que cela suppose :** Pouvoir encoder une conjecture sous la forme $\forall G \in \mathcal{G}, f(G) \ge 0$ où $f$ est calculable rapidement sur un objet fini $G$ (graphe, matrice de corrélation, arbre de décision séquentiel).
*   **Ce que cela a donné :** Réfutation d'une demi-douzaine de conjectures ouvertes en théorie des graphes et combinatoire en minimisant $f(G)$ par entropie croisée (*cross-entropy method*).
*   **Où cela échoue :** Dès que l'espace des objets valides $\mathcal{G}$ est soumis à des contraintes algébriques rigides (par exemple, être une matrice semi-définie positive de rang fixé ou satisfaire les axiomes d'une martingale), les mutations aléatoires sortent de l'espace valide.

#### C. Auto-formalisation et décomposition en lemmes (*Sketching*)
*   **Travaux :** *Draft, Sketch, and Prove: Guiding Formal Theorem Provers with Informal Proofs* (**DSP**, Jiang et al., 2022, **arXiv:2210.12283**) ; **LEGO-Prover** (*LEGO-Prover: Neural Theorem Proving with Growing Libraries*, Wang et al., 2023, identifiant arXiv : pas sûr) pour la mémoire et le réemploi de lemmes.
*   **Ce que cela suppose :** Que le LLM sache déjà écrire une preuve correcte en langage naturel, qu'il puisse la traduire en un squelette formel contenant des sous-buts admis (`sorry`), et qu'un prouveur automatique (« *hammer* ») puisse boucher les trous.
*   **Ce que cela a donné :** Résolution de problèmes de compétition (banc d'essai *miniF2F*).
*   **Où cela échoue :** **Le gouffre des *hammers* dans Lean 4.** DSP a réussi dans *Isabelle/HOL* parce qu'Isabelle dispose de `Sledgehammer` (logique d'ordre supérieur simple reliée à Vampire/E/Z3). Lean 4 repose sur la théorie des types dépendants (Calcul des Constructions Inductives), où l'automatisation générale est beaucoup plus faible (`aesop` est structurel, `Duper` et `Lean-auto` progressent mais restent loin de Sledgehammer sur l'analyse). Un pas jugé « évident » par le LLM en langage naturel (« par conditionnement sur le temps d'arrêt $\tau$ ») exige 200 lignes de lemmes techniques dans Lean 4.

#### D. Recherche d'arbre de preuve (*Tree Search*) dans Lean
*   **Travaux :** *LeanDojo: Theorem Proving with Retrieval-Augmented Language Models* (**ReProver**, Yang et al., 2023, **arXiv:2306.15626**) ; **DeepSeek-Prover-V1.5** (Xin et al., 2024, identifiant arXiv : pas sûr) ; **AlphaProof** (DeepMind, 2024, pas de publication arXiv).
*   **Ce que cela suppose :** Un énoncé formel *déjà fixé* et un modèle entraîné par apprentissage par renforcement sur l'arbre des états tactiques de Lean (MCTS ou recherche en faisceau couplée au serveur LSP de Lean).
*   **Ce que cela a donné :** Niveau médaille d'argent à l'OIM 2024 (AlphaProof).
*   **Où cela échoue :**
    1. *Le budget :* AlphaProof consomme des jours-machines de TPU par problème. Avec 300 $ par course, la recherche arborescente profonde dans Lean s'épuisera en quelques minutes sur la latence de compilation de Lean 4.
    2. *L'invention de définitions :* La recherche tactique excelle pour enchaîner `rw`, `apply`, `linarith`, mais échoue presque toujours lorsqu'il faut **inventer un objet auxiliaire** (poser une fonction de Lyapunov explicite, un changement de mesure exponentiel $\tilde{\mathbb{P}}$, ou une fonction de potentiel).

#### E. Conjecture automatique
*   **Travaux :** *The Ramanujan Machine* (Raayoni et al., *Nature* 2021, identifiant arXiv : pas sûr — approche algorithmique non-LLM) ; *QuickSpec* (Claessen et al., découverte d'équations par tests sur des termes).
*   **Où cela échoue avec les LLMs :** Sans filtre algébrique sévère, un LLM à qui l'on demande de « conjecturer de nouveaux théorèmes » produit soit des tautologies triviales, soit des reformulations légèrement déguisées de théorèmes présents dans son corpus d'entraînement (inégalité de Hoeffding, de Pinsker ou de Wald avec d'autres notations).

---

### 4. Ce qui permettrait de vérifier de l'extérieur que le résultat est vrai, nouveau et utile

En dehors de votre équipe, un mathématicien sceptique exigera les quatre barrières suivantes :

1.  **Vérification de la Vérité (hors de votre environnement Lean) :**
    *   **Audit du noyau (*Kernel replay*) :** Exporter la preuve compilée via `lean4export` et la rejouer avec un vérificateur externe minimaliste et indépendant (`Lean4Checker` avec l'option `--fresh`, ou le vérificateur externe en Rust `nanoda`).
    *   **Inspection de l'empreinte axiomatique :** La commande `#print axioms MonTheoreme` ne doit afficher que les axiomes standards (`propext`, `Quot.sound`, `Classical.choice`). Aucun `sorryAx`, aucun axiome personnalisé ajouté par l'agent.
    *   **Audit des définitions (la frontière sémantique) :** Le fichier contenant les *définitions* et l'*énoncé du théorème* (`Spec.lean`) doit être en lecture seule pour l'agent et tenir en moins de 50 lignes lisibles à l'œil nu par un mathématicien humain en 10 minutes. L'agent n'a le droit d'écrire que dans `Proof.lean`.
    *   **Théorème témoin de non-vacuité :** `Proof.lean` doit contenir une preuve formelle `theorem witness_exists : ∃ (x : MonObjet), MesHypotheses x` prouvant que les prémisses ne sont pas contradictoires.

2.  **Vérification de la Nouveauté (contre la régurgitation et la trivialité) :**
    *   **Test de réduction canonique :** Soumettre l'énoncé (traduit en LaTeX) et ses cas particuliers ($N=2, 3$) à un pipeline de recherche d'antériorité combinant recherche sémantique (`LeanSearch` / `Moogle` pour Mathlib, recherche vectorielle sur la base arXiv `math.ST` et `cs.LG`) et un système de calcul formel (Mathematica/SymPy) pour vérifier si l'inégalité ne se réduit pas algébriquement à une inégalité classique (Cauchy-Schwarz, Markov, Ville, Pinsker, Fréchet) par un simple changement de variables.
    *   **Test d'ablation sur les modèles de base :** Si un LLM standard (Claude, GPT-4, DeepSeek) résout le théorème en *zero-shot* sans votre organisme, le résultat est un exercice de cours ou un théorème connu sous un autre nom, pas une découverte.

3.  **Vérification de l'Utilité :**
    *   **Domination stricte sur un banc d'essai chiffré :** Si le résultat est une nouvelle règle d'agrégation de détecteurs ou un test séquentiel, il doit être accompagné d'un script Python reproductible montrant que, sous une attaque de corrélation adverse explicite où les méthodes standards (vote majoritaire, test de Wald avec correction de Bonferroni, moyenne des *e-valeurs*) échouent ou donnent une borne lâche, la nouvelle formule améliore strictement la constante ou l'exposant.

---

### 5. Reformulation de la demande

Pour qu'un tel programme aboutisse réellement avec ~300 $ par course, il faut abandonner l'idée que « des agents LLM vont débattre et rédiger des preuves générales de probabilités dans Lean ». Voici la formulation opérationnelle exacte que votre programme doit adopter :

> **Problème reformulé :** « Construire un pipeline hybride **Primal-Dual** où :
> 1. Un problème de contrôle d'IA (agrégation sous corrélation adverse, détection séquentielle) est d'abord réduit par un humain à la recherche d'un **certificat algébrique dual** (une distribution jointe discrète extrémale pour une borne d'impossibilité ; une fonction de mise à jour polynomiale de surmartingale pour une garantie de détection).
> 2. Une boucle évolutionnaire guidée par LLM (budget < 150 $) génère des programmes Python qui construisent ces certificats candidats, évalués instantanément contre une banque de mondes plantés et un solveur de programmation linéaire/convexe exacte en arithmétique rationnelle $\mathbb{Q}$.
> 3. Lorsqu'un certificat survit à tous les tests numériques et améliore la borne de référence, un module de synthèse symbolique extrait la formule générale en fonction de $N$, et un prouveur Lean 4 (budget < 150 $) vérifie uniquement **l'identité algébrique élémentaire** (non-négativité d'un polynôme ou faisabilité duale) qui implique mathématiquement le théorème général via un méta-théorème de dualité pré-prouvé par les chercheurs humains. »

---

### 6. Propositions concrètes de méthodes pour votre organisme

Voici trois méthodes conçues spécifiquement pour vos sujets mathématiques et votre contrainte budgétaire.

#### Méthode 1 : Découverte de bornes d'impossibilité et de corrélations adverses par recherche de témoins duaux (Couplages extrémaux)

*   **Le principe mathématique :** Prouver qu'aucun agrégateur de $K$ moniteurs (ayant chacun un taux de faux positifs $\le \alpha_k$ et de vrais positifs $\ge \beta_k$) ne peut dépasser une performance $V^*$ sous corrélation adverse équivaut, par dualité de programmation linéaire (théorème minimax de von Neumann), à **exhiber une distribution jointe explicite** $P \in \Delta(\{0,1\}^K \times \{H_0, H_1\})$ qui respecte les marginales $(\alpha_k, \beta_k)$ et sur laquelle tout classifieur échoue. Prouver une borne d'impossibilité dans Lean se réduit alors à vérifier que les entrées d'un tenseur explicite sont positives, somment à 1, et satisfont une inégalité linéaire : zéro théorie de la mesure requise.
*   **Premier pas (Semaine 1) :** Écrire dans Lean 4 (par un humain, ~150 lignes) le lemme fondamental de dualité faible sur espace fini $\{0,1\}^K$ : *« S'il existe un vecteur de poids $w \in \mathbb{Q}^{2^K}$ vérifiant les contraintes marginales $A w \le b$, alors tout détecteur $f : \{0,1\}^K \to \{0,1\}$ subit une erreur d'au moins $c^T w$ »*.
*   **Fonctionnement de l'organisme :** Les modèles proposeurs génèrent des fonctions Python paramétriques qui construisent symboliquement la matrice de couplage adverse $w(K, \alpha, \beta)$ (au lieu de chercher la matrice par force brute, qui explose en $2^K$, le LLM cherche la *formule de symétrie par blocs* de la distribution adverse). L'évaluateur Python vérifie en arithmétique exacte (`fractions.Fraction`) la validité pour $K=3, 5, 10, 20$ contre vos meilleurs agrégateurs connus (les mondes plantés).
*   **Coût par course :** **30 $ à 80 $** d'API LLM (environ 500 à 1 500 programmes générés et évalués localement sur CPU en Python) + **20 $** d'appels LLM pour traduire la formule rationnelle gagnante en Lean 4 et fermer le but par `norm_num` / `linarith` / `ring`.
*   **Test de mort (ce qui la tue) :** Si pour $K=4$ et $K=5$, la valeur optimale trouvée par l'organisme à base de LLM est strictement inférieure (à $10^{-6}$ près) à la solution numérique exacte calculée hors-ligne par un solveur LP standard (`scipy.optimize.linprog` ou `Clarabel`), la représentation symbolique choisie par le LLM est mauvaise : on tue la branche immédiatement.
*   **Ce qui la distingue de l'existant :** Contrairement à *FunSearch* qui cherche des objets combinatoires sans structure duale pour de grands $N$ fixes, cette méthode utilise la dualité de Le Cam / LP pour transformer une **borne d'impossibilité universelle** ($\forall f$, impossible à tester par programme) en un **témoin existentiel constructif** ($\exists w$, trivialement vérifiable par programme et dans Lean).

#### Méthode 2 : Synthèse symbolique de surmartingales de test (*E-processus*) pour la détection séquentielle

*   **Le principe mathématique :** En détection séquentielle à horizon quelconque sous taux de fausses alertes contrôlé ($\mathbb{P}_{H_0}(\exists t \ge 1, \text{Alerte}_t) \le \alpha$), le théorème de Ville et la littérature récente sur les *e-valeurs* (Ramdas et al.) montrent que toute procédure valide correspond à une **surmartingale non-négative** $M_t \ge 0$ avec $M_0 = 1$, qui déclenche une alerte dès que $M_t \ge 1/\alpha$. Si $M_t = \prod_{s=1}^t (1 + \lambda_s \phi(X_s, X_{s-1}, \dots))$, la garantie de fausse alerte pour *n'importe quel temps d'arrêt* découle d'une unique condition locale : $\mathbb{E}_{H_0}[\phi(X_t \mid \mathcal{F}_{t-1})] \le 0$ et $1 + \lambda_t \phi \ge 0$.
*   **Premier pas (Semaine 1-2) :** Formaliser une seule fois dans Lean 4 l'inégalité de Ville discrète (ou l'importer de `Mathlib` si la version pour temps d'arrêt bornés y est déjà stable) sous forme d'interface propre : pour obtenir un moniteur séquentiel certifié, l'agent n'a plus qu'à fournir la fonction de score locale $\phi : \mathcal{X} \to \mathbb{R}$ et prouver que $\sum_{x} p_0(x) \phi(x) \le 0$.
*   **Fonctionnement de l'organisme :** Vous plantez des mondes adverses séquentiels (par exemple : un agent IA qui se comporte normalement pendant $t_0$ pas, puis injecte des anomalies corrélées temporellement ou à queue lourde). Les proposeurs LLM génèrent des familles de fonctions de pari $\phi_\theta$ (fractions rationnelles, polynômes orthogonaux tronqués, agrégateurs non-linéaires de sous-moniteurs). Le filtre Python vérifie symboliquement (via `SymPy`) ou sur grille que l'espérance sous $H_0$ est négative, et mesure la vitesse de croissance $\mathbb{E}_{H_1}[\log(1 + \lambda \phi)]$ sur les mondes plantés.
*   **Coût par course :** **100 $ à 200 $** (génération de candidats de fonctions de pari + optimisation de la preuve d'inégalité polynomiale dans Lean via décomposition en sommes de carrés — SOS).
*   **Test de mort :**
    1. Si un solveur SMT (`Z3`) ou un optimiseur global trouve un point $x \in \mathcal{X}$ où $1 + \lambda \phi(x) < 0$ (la martingale devient négative, ce qui détruit l'inégalité de Ville), le candidat est tué en 10 millisecondes.
    2. Si le temps moyen de détection sur les mondes plantés ne bat pas le mélange de *e-valeurs* par moyenne arithmétique standard ou le test CUSUM de Page, la course est abandonnée.
*   **Ce qui la distingue de l'existant :** La littérature utilise des familles de paris standard (exponentielles, linéaires de Kelly). Ici, l'organisme découvre des **polynômes de pari multivariés** adaptés à la géométrie exacte de la corrélation entre vos moniteurs d'IA, tout en héritant automatiquement d'une garantie formelle en temps infini via l'inégalité de Ville.

#### Méthode 3 : Extrapolation symbolique « Petit-$N$ exact $\to$ Conjecture générale $\to$ Preuve par sommes de carrés (SOS) »

*   **Le principe mathématique :** Pour de nombreuses garanties de moniteurs (par exemple, borner la probabilité de défaillance simultanée de $k$ moniteurs parmi $N$ sous contrainte de variance ou de dépendance bornée), on sait résoudre le problème exactement pour $N=2, 3, 4, 5$ avec un solveur numérique, mais on ignore la formule fermée pour tout $N$.
*   **Premier pas :** Écrire un script Python utilisant un solveur exact (programmation linéaire en rationnels via `SageMath` ou `Z3`) qui calcule la borne exacte $B^*(N, c)$ sur une grille de paramètres rationnels $c \in \mathbb{Q}$ pour $N \in \{2, 3, 4, 5, 6\}$.
*   **Fonctionnement de l'organisme :**
    1. *Phase d'interpolation :* On donne aux modèles proposeurs (modèles de raisonnement type o1/o3-mini/DeepSeek-R1) la table des valeurs rationnelles exactes (ex. : $3/8, 5/16, 11/32 \dots$) et la structure des vecteurs duaux actifs. Leur tâche est de conjecturer la formule générale en fonction de $N$ et la forme générale des multiplicateurs de Lagrange.
    2. *Phase de réfutation (Mondes plantés) :* La formule conjecturée pour tout $N$ est testée numériquement à $N=7, 10, 15$ contre le solveur numérique.
    3. *Phase de preuve Lean :* Si la formule tient à $N=15$, la différence entre le membre gauche et le membre droit de l'inégalité est décomposée en somme de carrés (via un solveur SDP en Python qui extrait le certificat rationnel), et ce certificat de carrés est injecté directement dans Lean 4 (où la tactique `positivity` ou `linarith` conclut en une seconde).
*   **Coût par course :** **50 $ à 150 $** (les appels aux modèles de raisonnement sur des tables de fractions exactes sont très peu coûteux en tokens ; le calcul de décomposition SOS se fait sur CPU local).
*   **Test de mort :** Si la formule conjecturée sur $N \in \{2..5\}$ dévie de la solution du solveur à $N=6$ ou $N=7$, la conjecture est morte. Si le dénominateur des fractions exactes croît sans structure algébrique reconnaissable (explosion de la hauteur arithmétique des nombres premiers au dénominateur entre $N=4$ et $N=6$), cela indique que la vraie borne est définie par morceaux chaotiques et n'admet pas de formule fermée simple : on arrête la course sur ce problème.
*   **Ce qui la distingue de l'existant :** Elle remplace la recherche d'arbre aveugle dans Lean (qui coûte des milliers de dollars et échoue sur l'induction) par de la **reconnaissance de motifs arithmétiques sur des solutions duales exactes**, domaine où les modèles de raisonnement actuels surpassent largement les tactiques formelles.

---

### Évaluation honnête : temps, effort humain et part de chance

Il faut être lucide sur la répartition réelle du travail dans ce type de découverte assistée par IA :

*   **80 % du succès repose sur la réduction mathématique humaine préalable.** Aucun organisme LLM actuel à 300 $ par course ne va partir d'une question vague (« Comment agréger des détecteurs corrélés ? ») et inventer seul le cadre formel, les bonnes définitions dans Lean et le théorème. Un mathématicien humain et un ingénieur Lean doivent passer **3 à 6 semaines** en amont pour :
    1. Poser les définitions formelles immuables dans Lean 4 (le « contrat »).
    2. Prouver à la main dans Lean le **méta-théorème de réduction** (le pont de dualité ou l'inégalité de Ville) qui ramène le théorème analytique difficile à la vérification d'un simple certificat algébrique fini.
*   **Ce que fait réellement l'organisme IA (les 20 % restants, mais décisifs) :** Une fois ce entonnoir algébrique construit par l'humain, l'organisme explore en une nuit (pour ~100 $) un espace d'ansätze algébriques, de couplages adverses par blocs et de fonctions de potentiel qu'un mathématicien humain mettrait des mois à calculer au brouillon, et élimine sans pitié les conjectures fausses grâce aux mondes plantés.
*   **La part de chance :** Elle réside entièrement dans la **régularité algébrique de la frontière extrémale** de votre problème. Si le pire couplage adverse entre vos moniteurs ou la surmartingale optimale possède une structure symétrique par blocs ou polynomiale (ce qui arrive fréquemment dans les problèmes minimax à contraintes symétriques, comme pour les bornes de Chebyshev-Cantelli ou de Fréchet), l'organisme a une chance élevée de découvrir une borne analytique inédite et publiable. Si la solution extrémale est fractale, transcendante ou change de topologie à chaque valeur de $N$, l'organisme trouvera de très bonnes constructions numériques pour $N$ fixé, mais aucune formule générale nouvelle.