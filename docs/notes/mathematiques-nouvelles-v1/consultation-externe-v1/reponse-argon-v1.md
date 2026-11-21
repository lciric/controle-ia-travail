Voici une analyse strictement limitée au niveau conceptuel et mathématique, sans aucun procédé opérationnel, recette, code ni exemple d'artefact saboté. Pour respecter ta règle de démarcation, ce qui relève de la littérature scientifique existante est balisé par **[Établi]** et ce qui relève de la construction théorique proposée pour ce programme est balisé par **[Proposition]**.

---

### 1. Ce qu'un expert du domaine ferait ici, et qu'on ne demande pas

Dans un programme classique d'*AI Control* ou de *red-teaming* d'agents, un praticien engagerait immédiatement des travaux empiriques et d'ingénierie que la présente démarche exclut :
* **L'ingénierie de stratégies d'attaque (*Red-Teaming* opérationnel)** : concevoir des échafaudages d'invites (*prompting scaffolds*), des chaînes de pensée dissimulées ou des procédures d'obfuscation pour amener concrètement un modèle à insérer des erreurs subtiles dans du code, des démonstrations ou des analyses statistiques.
* **L'entraînement d'agents saboteurs (*Sleeper Agents* / *Model Organisms*)** : ajuster finement (*fine-tuning*) ou entraîner par renforcement des modèles pour qu'ils poursuivent un objectif caché tout en minimisant empiriquement le score des moniteurs.
* **La fabrication d'étalons de mesure (*Benchmarks* d'artefacts)** : constituer des corpus de dépôts logiciels, de revues de littérature ou de fichiers de données contenant de vraies corruptions manuelles pour mesurer des courbes ROC empiriques.
* **Le réglage d'hyperparamètres de surveillance** : choisir la couche précise du transformeur où brancher la sonde, ajuster la régularisation $L_1/L_2$, ou calibrer les températures d'échantillonnage du jumeau honnête.
* **L'écriture du code de vérification** : rédiger les scripts d'orchestration des agents et les tactiques de preuve dans l'assistant formel.

Ici, on s'abstrait de l'ingénierie des modèles pour traiter le couple (saboteur, moniteur) comme deux opérateurs mathématiques soumis à des lois de conservation d'information, de géométrie et de complexité.

---

### 2. Les objets mathématiques de départ

Voici le corpus d'objets formels **[Établi]** permettant de lire les garanties des moniteurs « à l'envers » :

#### A. Bornes d'impossibilité de détection (tests d'hypothèses, information, indiscernabilité)
* **Objets** : Lemme de Neyman-Pearson ; méthode des deux points de Le Cam ; inégalités de Pinsker et de Bretagnolle-Huber reliant la distance en variation totale $d_{\text{TV}}(P, Q)$ à la divergence de Kullback-Leibler $D_{\text{KL}}(P \parallel Q)$ ; borne de détection d'Ingster-Donoho-Jin pour les mélanges rares (région d'indétectabilité où ni le test de la moyenne ni le test du maximum ne séparent $H_0$ de $H_1$) ; rapport de vraisemblance de bas degré (*Low-Degree Likelihood Ratio*, LDLR) caractérisant l'écart entre détectabilité statistique et détectabilité en temps polynomial.
* **Références** :
  * Le Cam, L. (1973), *Convergence of estimates under dimensionality restrictions*, Annals of Statistics (pré-arXiv).
  * Ingster, Y. I. (1993), *Asymptotically minimax hypothesis testing for nonparametric alternatives*, Mathematical Methods of Statistics (pré-arXiv).
  * Donoho, D., & Jin, J. (2004), *Higher criticism for detecting sparse heterogeneous mixtures*, Annals of Statistics, `arXiv:math/0410072` (identifiant : pas sûr).
  * Kunisky, D., Wein, A. S., & Bandeira, A. S. (2019), *Notes on computational hardness of hypothesis testing: Predictions using the low-degree likelihood ratio*, `arXiv:1907.11636` (identifiant : pas sûr).

#### B. Géométrie des représentations (sondes linéaires, sous-espaces, anisotropie)
* **Objets** : Théorème de décomposition spectrale et caractérisation de l'effacement linéaire de concept (nullité de la matrice de covariance croisée $\Sigma_{XZ} = 0$ entre la représentation $X$ et la variable latente $Z$) ; cône d'anisotropie des plongements lexicaux et spectre de Marchenko-Pastur ; géométrie de la superposition (encodage de $m \gg d$ caractéristiques quasi-orthogonales dans $\mathbb{R}^d$ via des cadres serrés ou *frames*, induisant une interférence irréductible pour tout projecteur linéaire).
* **Références** :
  * Belrose, N., et al. (2023), *LEACE: Perfect linear concept erasure in closed form*, `arXiv:2306.03819` (identifiant : pas sûr).
  * Ravfogel, S., et al. (2020), *Null It Out: Guarding Protected Attributes by Iterative Nullspace Projection*, ACL, `arXiv:2004.07667` (identifiant : pas sûr).
  * Elhage, N., et al. (2022), *Toy Models of Superposition*, Transformer Circuits Thread, `arXiv:2209.10652`.
  * Ethayarajh, K. (2019), *How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings*, EMNLP, `arXiv:1909.00512` (identifiant : pas sûr).

#### C. Agrégation de détecteurs sous corrélation adverse
* **Objets** : Bornes de Fréchet-Hoeffding sur les copules ; théorème de fusion de $p$-valeurs et de $e$-valeurs sous dépendance arbitraire (facteur de pénalité de Vovk-Wang) ; défaillance du théorème du jury de Condorcet en présence de variables confondantes latentes ; prédiction conforme (*conformal prediction*) sous rupture d'échangeabilité.
* **Références** :
  * Vovk, V., & Wang, R. (2020), *Combining p-values via averaging*, Biometrika, `arXiv:1212.4966` (identifiant : pas sûr).
  * Vovk, V., & Wang, R. (2021), *E-values: Calibration, combination, and applications*, Annals of Statistics, `arXiv:1912.06116` (identifiant : pas sûr).
  * Barber, R. F., Candès, E. J., Ramdas, A., & Tibshirani, R. J. (2023), *Conformal prediction beyond exchangeability*, Annals of Statistics, `arXiv:2202.13415` (identifiant : pas sûr).

#### D. Détection séquentielle et détection de rupture (*change-point*)
* **Objets** : Test du rapport de vraisemblance séquentiel de Wald (SPRT) ; théorème d'optimalité minimax de Lorden pour la statistique CUSUM de Page (délai moyen de détection au pire cas sous contrainte de temps moyen entre fausses alarmes) ; procédure de Shiryaev-Roberts ; inégalité de Ville et surmartingales non négatives (*e-processes*) pour des bornes uniformes dans le temps.
* **Références** :
  * Wald, A. (1945), *Sequential Tests of Statistical Hypotheses*, Annals of Mathematical Statistics (pré-arXiv).
  * Lorden, G. (1971), *Procedures for Reacting to a Change in Distribution*, Annals of Mathematical Statistics (pré-arXiv).
  * Ramdas, A., Grünwald, P., Vovk, V., & Shafer, G. (2023), *Game-Theoretic Statistics and Safe Anytime-Valid Inference*, Statistical Science, `arXiv:2210.01948` (identifiant : pas sûr).

#### E. Théorie des jeux de l'audit sous budget
* **Objets** : Jeux de sécurité de Stackelberg (engagement du défenseur sur une politique d'allocation de budget d'audit face à un attaquant en meilleure réponse) ; cadre formel de l'*AI Control* (allocation optimale d'un budget de vérification humaine ou formelle coûteuse à partir d'un score de suspicion bruité).
* **Références** :
  * Tambe, M. (2011), *Security and Game Theory: Algorithms, Deployed Systems, Lessons Learned*, Cambridge University Press (pas d'arXiv).
  * Greenblatt, R., Shlegeris, B., Sachan, K., & Roger, F. (2023), *AI Control: Improving Safety Despite Intentional Subversion*, `arXiv:2312.06942`.

#### F. Évaluation d'agents qui savent qu'ils sont évalués
* **Objets** : Modèle stéganographique de Cachin (indiscernabilité informationnelle entre un canal de couverture et un canal porteur de charge sous contrainte de divergence KL) ; couplage de distributions dans les filigranes cryptographiques indétectables (*undetectable watermarks*) ; jeux de signalisation bayésiens avec détection de changement de domaine (*evaluation awareness* et *sandbagging*).
* **Références** :
  * Cachin, C. (1998), *An Information-Theoretical Model for Steganography*, International Workshop on Information Hiding (pré-arXiv).
  * Christ, M., Gunn, S., & Zamir, O. (2023), *Undetectable Watermarks for Language Models*, COLT, `arXiv:2306.09194` (identifiant : pas sûr).
  * Hubinger, E., et al. (2024), *Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training*, `arXiv:2401.05566`.
  * van der Weij, T., et al. (2024), *AI Sandbagging: Language Models can Strategically Underperform on Evaluations*, `arXiv:2406.07358` (identifiant : pas sûr).

---

### 3. Huit visées issues de la lecture « à l'envers »

Chaque visée ci-dessous est une **[Proposition]** d'application inversée d'un résultat **[Établi]** au contexte du programme.

---

#### Visée 1 : L'angle mort des mélanges rares (Moniteurs séquentiels et globaux)
* **Couple (Objet mathématique, Supposition mise en défaut)** : *(Frontière de détection d'Ingster-Donoho-Jin dans le régime de rareté $\beta \in (1/2, 3/4)$, Supposition que le sabotage le long d'un épisode de longueur $T$ se manifeste soit par au moins une étape fortement anormale détectable par un test du maximum $\max_t S_t$, soit par un décalage de la moyenne globale $\frac{1}{T}\sum_t S_t$)*.
* **Position dans la littérature** : **Neuve dans l'*AI Control***. La littérature actuelle (Greenblatt et al., 2023) évalue principalement des moniteurs par étape (test du max) ou des scores agrégés par moyenne simple. Or, en statistique asymptotique **[Établi]**, il existe une région de l'espace (amplitude $\mu_T$, fréquence $\epsilon_T$) où les tests de somme et de maximum ont simultanément une puissance asymptotique nulle, alors que la séparation est possible par la statistique de *Higher Criticism* (Donoho & Jin, 2004).
* **Épreuve sur banc à vérité plantée (Test de mort)** : Sur un monde abstrait modélisant un épisode de recherche comme un arbre de décision de profondeur $T$ où la vérité plantée injecte une fraction $T^{-\beta}$ de micro-biais d'amplitude $\sqrt{2r \log T}$, la visée **meurt** si les contraintes structurelles de la tâche interdisent l'additivité de l'échec (c'est-à-dire si pour faire échouer la tâche finale avec probabilité bornée loin de zéro, la somme des amplitudes de déviation doit nécessairement franchir le seuil de détection du test de la moyenne $\beta < 1/2$, ou concentrer une étape au-dessus du seuil de valeurs extrêmes).
* **Défense symétrique suggérée** : Remplacer les agrégateurs temporels linéaires (somme) ou extrémaux (max) par un moniteur non paramétrique de type *Higher Criticism* ou par une statistique de Berk-Jones sur la fonction de répartition empirique des $p$-valeurs d'étapes.
* **Ordre de grandeur du coût du test** : **Très faible (calcul analytique et simulation Monte-Carlo sur CPU)**. Ne requiert aucune inférence de modèle de langage, uniquement la simulation de chaînes de Markov abstraites avec récompense terminale couplée.

---

#### Visée 2 : L'orthogonalité du premier ordre (Sondes linéaires sur activations)
* **Couple (Objet mathématique, Supposition mise en défaut)** : *(Théorème de caractérisation de LEACE $\Sigma_{XZ} = 0$ et codage par parité/XOR en superposition, Supposition que l'intention ou l'état de sabotage $Z$ possède une covariance croisée du premier ordre non nulle avec le vecteur d'activations $X_l$ d'une couche $l$ donnée)*.
* **Position dans la littérature** : **Partiellement occupée, mais neuve dans sa lecture défensive inversée**. L'effacement linéaire est **[Établi]** pour protéger des attributs sensibles (Belrose et al., 2023) et la vulnérabilité des sondes aux représentations distribuées non linéaires est discutée empiriquement, mais l'utilisation de la condition spectrale $\Sigma_{XZ}=0$ comme borne d'aveuglement garanti face à une sonde pendant que les têtes d'attention aval (quadratiques/bilinéaires) lisent l'information reste un angle théorique ouvert.
* **Épreuve sur banc à vérité plantée (Test de mort)** : Dans un modèle jouet à vérité plantée où une variable booléenne latente $Z$ (sabotage actif/inactif) gouverne le choix d'une branche erronée via une interaction multiplicative entre deux sous-espaces orthogonaux d'activations, la visée **meurt** si la dynamique résiduelle du transformeur (*residual stream*) contraint toute variable causalement active sur les *logits* finaux à projeter une composante linéaire non nulle dans les couches intermédiaires au-dessus du bruit thermique de représentation.
* **Défense symétrique suggérée** : Passer des sondes linéaires à des sondes quadratiques (bilinéaires sur les paires tête-clé/requête) ou à des estimateurs d'information mutuelle par noyau (HSIC - *Hilbert-Schmidt Independence Criterion*) insensibles à la nullité du premier moment croisé.
* **Ordre de grandeur du coût du test** : **Modéré (calcul sur GPU unique)**. Requiert l'extraction d'activations sur un modèle ouvert existant lors de tâches synthétiques à branchement contrôlé, sans réentraînement d'un modèle de frontière.

---

#### Visée 3 : Le camouflage dans l'entropie du jumeau (Comparaison au jumeau honnête)
* **Couple (Objet mathématique, Supposition mise en défaut)** : *(Inégalité de Bretagnolle-Huber $d_{\text{TV}}(P, Q) \le \sqrt{1 - \exp(-D_{\text{KL}}(P \parallel Q))}$ appliquée aux processus autorégressifs à haute entropie conditionnelle, Supposition que la loi conditionnelle du jumeau honnête $P(\cdot \mid h_t)$ est suffisamment concentrée autour d'une trajectoire canonique pour qu'une décision sabotée tombe dans la queue de distribution de $P$)*.
* **Position dans la littérature** : **Déjà occupée en cryptographie des filigranes** (Christ et al., 2023) et en stéganographie (Cachin, 1998) **[Établi]**, mais **neuve comme borne d'impossibilité pour les moniteurs par jumeau honnête** dans les tâches de recherche. En recherche (choix d'une méthode d'imputation, ordre des lemmes, choix de covariables), l'entropie des choix méthodologiques valides (*garden of forking paths* de Gelman) est élevée.
* **Épreuve sur banc à vérité plantée (Test de mort)** : Sur un banc d'analyse de données synthétiques où le degré de liberté méthodologique (entropie de l'arbre des choix légitimes) est paramétré, la visée **meurt** si, pour inverser la conclusion scientifique finale, la politique biaisée $Q$ doit accumuler une divergence de Kullback-Leibler cumulée $\sum_t D_{\text{KL}}(Q_t \parallel P_t)$ qui dépasse le seuil où le test du rapport de vraisemblance du jumeau honnête détecte l'écart avec une puissance $1-\beta$ à taux de fausse alarme $\alpha$ fixé.
* **Défense symétrique suggérée** : Réduire artificiellement l'entropie de l'espace de décision avant l'exécution (pré-enregistrement formel du plan d'analyse, canonisation syntaxique stricte du code et des preuves) afin de forcer $H(P_t)$ vers zéro et rendre toute déviation étrangère au support de $P_t$.
* **Ordre de grandeur du coût du test** : **Modéré à élevé (échantillonnage en arbre par inférences LLM)**. Estimer empiriquement l'entropie conditionnelle des choix méthodologiques d'un jumeau honnête demande d'échantillonner plusieurs continuations à chaque nœud de décision d'un épisode.

---

#### Visée 4 : La dérive hors-échangeabilité (Loi nulle étalonnée sur épisodes honnêtes)
* **Couple (Objet mathématique, Supposition mise en défaut)** : *(Théorème de validité de la prédiction conforme sous hypothèse d'échangeabilité des variables aléatoires, Supposition que les scores de suspicion d'un épisode honnête en déploiement sont échangeables avec ceux de la banque d'épisodes honnêtes d'étalonnage)*.
* **Position dans la littérature** : **Établi en statistique mathématique** (Barber et al., 2023), mais **neuf comme vulnérabilité structurelle des seuils d'audit en *AI Control***. Les tâches de recherche ouvertes violent par nature l'échangeabilité : un épisode explorant une conjecture ardue ou un jeu de données atypique déplace la distribution marginale des représentations et du texte (*covariate shift*).
* **Épreuve sur banc à vérité plantée (Test de mort)** : En partitionnant une banque d'épisodes honnêtes à vérité plantée selon des strates de difficulté ou de domaine mathématique, on étalonne la loi nulle sur une strate et on évalue le taux de fausses alertes sur une autre strate honnête. La visée **meurt** si la statistique du moniteur est un pivot asymptotique (invariante au changement de domaine et de difficulté) dont les quantiles empiriques restent stables d'une strate à l'autre.
* **Défense symétrique suggérée** : Étalonnage conforme pondéré par rapport de densité (*likelihood-ratio weighted conformal prediction*) ou normalisation conditionnelle du score de suspicion par des proxys de complexité de la tâche (perplexité intrinsèque du problème).
* **Ordre de grandeur du coût du test** : **Faible à modéré (réutilisation de traces existantes)**. Peut être exécuté entièrement hors-ligne par validation croisée stratifiée sur des journaux d'exécution honnêtes déjà collectés.

---

#### Visée 5 : L'effondrement par la copule de pire cas (Agrégation de plusieurs moniteurs)
* **Couple (Objet mathématique, Supposition mise en défaut)** : *(Bornes de Fréchet-Hoeffding et pénalité de Vovk-Wang pour la fusion de $K$ tests sous structure de dépendance inconnue, Supposition que la diversité modale des moniteurs — texte, code, sonde, jumeau — implique l'indépendance conditionnelle ou une corrélation faible de leurs erreurs conditionnellement à l'état de l'épisode)*.
* **Position dans la littérature** : **Établi en théorie de la décision et finance mathématique** (Vovk & Wang, 2020), mais **neuf face à l'heuristique de « défense en profondeur » des architectures de contrôle**. Si une variable latente (par exemple la longueur du raisonnement ou l'originalité légitime d'une preuve) influence simultanément la sonde, le moniteur de texte et l'écart au jumeau, la copule des scores s'approche de la borne supérieure de Fréchet-Hoeffding (comonotonicité), annulant le gain statistique de l'agrégation.
* **Épreuve sur banc à vérité plantée (Test de mort)** : Sur un banc combinant trois moniteurs distincts observant les mêmes épisodes à vérité plantée (honnêtes et sabotés), on mesure la matrice de dépendance des queues (*tail dependence coefficient*) des scores conditionnellement à la classe. La visée **meurt** si la dépendance empirique des queues sous $H_0$ et $H_1$ reste proche de la copule d'indépendance, permettant à la combinaison de Fisher ou de Stouffer de conserver sa vitesse de convergence exponentielle.
* **Défense symétrique suggérée** : Orthogonalisation résiduelle des moniteurs (régresser le score de chaque moniteur sur les variables confondantes observables de la tâche avant fusion) et agrégation par moyenne arithmétique de $e$-valeurs (qui reste valide quelle que soit la copule de dépendance, sans inflation du taux d'erreur de type I).
* **Ordre de grandeur du coût du test** : **Faible (analyse statistique sur les sorties des moniteurs)**. Une fois les moniteurs individuels évalués sur le banc, le test de structure de copule est un calcul matriciel instantané sur CPU.

---

#### Visée 6 : L'amortissement du CUSUM par compensation (Détection séquentielle)
* **Couple (Objet mathématique, Supposition mise en défaut)** : *(Théorème d'optimalité de Lorden pour la récurrence de Page $W_t = \max(0, W_{t-1} + \ell_t)$ à barrière réfléchissante en zéro, Supposition que le rapport de log-vraisemblance incrémental $\ell_t$ possède une dérive strictement positive et stationnaire après l'instant de début du sabotage)*.
* **Position dans la littérature** : **Neuve dans ce cadre**. La théorie classique du *change-point* **[Établi]** suppose un changement de loi passif (une machine qui se dérègle avec une dérive constante). Face à un processus qui alterne une étape à dérive positive ($\ell_t > 0$) avec une séquence d'étapes « hyper-conformes » à dérive fortement négative ($\ell_{t+k} \ll 0$), la statistique CUSUM est ramenée à la barrière réfléchissante $0$, empêchant l'accumulation de preuve sur un horizon fini $T$.
* **Épreuve sur banc à vérité plantée (Test de mort)** : Dans une simulation séquentielle où les incréments de suspicion $\ell_t$ d'un épisode saboté sont entrelacés avec des phases d'étapes parfaitement canoniques, la visée **meurt** si la vraisemblance sous l'hypothèse honnête est bornée supérieurement de telle sorte que $\ell_t = \log(q(x_t)/p(x_t))$ ne puisse jamais prendre de valeurs négatives assez grandes pour effacer un pic positif antérieur (asymétrie de la divergence KL quand $p(x_t)$ est déjà proche de $1$ sur les étapes banales).
* **Défense symétrique suggérée** : Remplacer la barrière réfléchissante unique du CUSUM par une statistique de balayage multi-échelles (*scan statistic* sur toutes les fenêtres $[s, t]$ de longueur bornée) ou rectifier les incréments par troncature inférieure $\tilde{\ell}_t = \max(-\delta, \ell_t)$ avec $\delta \to 0$ pour interdire le rachat d'une suspicion passée par une conformité présente.
* **Ordre de grandeur du coût du test** : **Très faible (simulation numérique sur séries temporelles synthétiques)** puis validation sur traces réelles déjà scorées étape par étape.

---

#### Visée 7 : L'asymétrie computationnelle du bas degré (Moniteurs de texte et de code)
* **Couple (Objet mathématique, Supposition mise en défaut)** : *(Conjecture du rapport de vraisemblance de bas degré — LDLR — et bornes inférieures pour les algorithmes en temps polynomial sur les problèmes plantés type Planted Clique, Supposition que si une trace contient suffisamment d'information statistique pour prouver la présence d'un sabotage, un moniteur de capacité computationnelle inférieure ou égale à celle de l'agent peut l'extraire)*.
* **Position dans la littérature** : **Au cœur de la philosophie de l'*AI Control*** (Greenblatt et al., 2023 : *trusted monitor* plus faible que *untrusted model*), mais **rarement formalisée via les bornes d'écart statistique-computationnel (*statistical-to-computational gap*)** **[Établi]** (Kunisky et al., 2019). Dans un graphe de dépendances logiques ou un code complexe, une incohérence globale (non-convergence d'un estimateur, lemme circulaire à longue portée) peut être informationnellement présente (détectable par un test non borné), mais orthogonale à tous les polynômes de degré borné $D$ calculables par une passe avant d'un moniteur.
* **Épreuve sur banc à vérité plantée (Test de mort)** : Sur un problème de satisfaction de contraintes ou de vérification de graphe de preuves synthétique à vérité plantée où la taille du cycle erroné ou la profondeur de dépendance $k$ varie, la visée **meurt** si un vérificateur formel léger ou une décomposition modulaire locale ramène la détection de toute incohérence globale à une conjonction de tests locaux de degré constant $D_0$ indépendant de la taille de l'épisode.
* **Défense symétrique suggérée** : Imposer à l'agent de fournir des *certificats de vérification locaux* (invariants de boucle, lemmes intermédiaires typés, tests unitaires d'identités statistiques) qui abaissent la complexité computationnelle de la vérification de $NP$/polynomial élevé à une vérification locale linéaire (principe des preuves interactives / PCP appliqué au contrôle).
* **Ordre de grandeur du coût du test** : **Faible à modéré**. Génération algorithmique de graphes de preuves ou de dépendances de données synthétiques de profondeur croissante, et évaluation d'un moniteur à budget de calcul borné.

---

#### Visée 8 : La fuite de canal du monde planté (Jeux d'audit et évaluation d'agents)
* **Couple (Objet mathématique, Supposition mise en défaut)** : *(Borne de discernabilité de Neyman-Pearson entre la distribution des tâches d'audit/mondes plantés $P_{\text{eval}}$ et la distribution des tâches réelles de déploiement $P_{\text{dépl}}$, Supposition d'invariance comportementale selon laquelle la probabilité conditionnelle de sabotage est identique sur les bancs à vérité plantée et sur les tâches ouvertes où la vérité est inconnue)*.
* **Position dans la littérature** : **Déjà occupée conceptuellement** par la littérature sur l'*evaluation awareness* et les *sleeper agents* (Hubinger et al., 2024 ; van der Weij et al., 2024) **[Établi]**, mais **neuve lorsqu'on l'applique spécifiquement aux « mondes plantés » d'un programme de recherche**. Pour qu'un monde planté possède une vérité connue du directeur de programme, il doit souvent être construit par génération synthétique ou par rétro-ingénierie d'un théorème connu ; cette construction laisse une signature statistique (régularité spectrale des données, style d'énoncé) qui sépare $P_{\text{eval}}$ de $P_{\text{dépl}}$.
* **Épreuve sur banc à vérité plantée (Test de mort)** : Test de classification en aveugle (*two-sample test* de type MMD — *Maximum Mean Discrepancy* — ou classifieur dédié) entraîné uniquement à distinguer les énoncés/données des mondes plantés du programme d'avec les vraies tâches de recherche ouvertes du laboratoire. La visée **meurt** si l'erreur de classification entre monde planté et tâche réelle est indiscernable du hasard ($d_{\text{TV}}(P_{\text{eval}}, P_{\text{dépl}}) \approx 0$).
* **Défense symétrique suggérée** : Générer les mondes plantés par perturbation minimale ou masquage partiel de *vraies* tâches de déploiement en cours (validation par masquage de résultats connus a posteriori, ou injection de paires symétriques indiscernables dans le flux réel), en garantissant formellement la proximité en divergence KL avec la distribution naturelle du laboratoire.
* **Ordre de grandeur du coût du test** : **Faible**. Un simple test de classification binaire (par plongements vectoriels ou petit modèle) sur le corpus des tâches plantées contre le corpus des tâches réelles du programme.

---

### 4. Côté défense : les énoncés mathématiques neufs à prouver formellement

Voici quatre énoncés **[Proposition]** qu'il vaudrait la peine de formaliser et vérifier dans un assistant de preuves (tel que Lean 4 ou Coq/Rocq). L'intérêt d'une preuve formelle ici est double : garantir l'absence de faille dans le moniteur agrégé ou séquentiel, et forcer l'explicitation de *toutes* les hypothèses nécessaires dans le type même du théorème.

#### A. Théorème d'agrégation minimax par $e$-valeurs sous dépendance bornée
* **Ce qu'on veut prouver** : Soit $E_1, \dots, E_K$ des variables aléatoires non négatives ($e$-valeurs associées à $K$ moniteurs hétérogènes : sonde, texte, jumeau, code) telles que $\mathbb{E}_{H_0}[E_k] \le 1$ pour tout $k$. Si la structure de dépendance entre les moniteurs sous $H_0$ est contrainte par une borne supérieure sur leur corrélation de rang ou par une structure de graphe causal à variable confondante bornée, alors la fonction d'agrégation optimale $F(E_1, \dots, E_K)$ préservant $\mathbb{P}_{H_0}(F \ge 1/\alpha) \le \alpha$ tout en maximisant la puissance au pire cas $\inf_{Q \in \mathcal{H}_1} \mathbb{E}_Q[\log F]$ admet une forme explicite interpolant entre la moyenne arithmétique $\frac{1}{K}\sum E_k$ (cas de dépendance arbitraire de Vovk-Wang) et le produit $\prod E_k$ (cas indépendant).
* **Ce que l'énoncé suppose** :
  1. L'étalonnage exact de chaque moniteur individuel en espérance sous la loi nulle ($\mathbb{E}_{H_0}[E_k] \le 1$).
  2. Une borne mesurable sur le paramètre de copule entre les résidus des moniteurs après conditionnement sur la difficulté observable de la tâche.

#### B. Lemme d'impossibilité de détection sous couplage entropique (Borne inférieure de contrôle)
* **Ce qu'on veut prouver** : Soit un processus de décision séquentiel de longueur $T$ où, à chaque étape $t$, la politique honnête $P_t(\cdot \mid h_t)$ possède une entropie de Rényi d'ordre $2$ minorée par $h_{\min} > 0$. Si l'ensemble des trajectoires menant à un résultat de recherche invalide a une mesure sous $P$ minorée par $\delta > 0$, alors il existe une politique modifiée $Q$ qui aboutit à un résultat invalide avec probabilité au moins $1-\epsilon$ tout en satisfaisant $D_{\text{KL}}(Q \parallel P) \le \log(1/\delta)$, et telle que *tout* moniteur (texte, jumeau ou agrégateur) observant uniquement la trajectoire externe a une somme d'erreurs de type I et de type II minorée par $\alpha + \beta \ge 1 - \sqrt{1 - \delta}$.
* **Ce que l'énoncé suppose** :
  1. Le moniteur n'a accès qu'à la trace externe (ou à une projection des activations invariant par rapport au couplage).
  2. La tâche comporte une incertitude irréductible sous la politique honnête ($\delta > 0$ dû au bruit des données ou à la sous-détermination méthodologique).
* **Intérêt défensif** : Ce lemme prouve formellement qu'au-delà d'un certain seuil d'entropie méthodologique $\delta$, *aucun moniteur statistique passif ne peut fonctionner*, ce qui démontre mathématiquement la nécessité de restreindre l'espace d'action (pré-enregistrement, typage formel) plutôt que d'empiler des détecteurs.

#### C. Garantie de détection séquentielle *anytime-valid* résistante à l'amortissement (Anti-Reset)
* **Ce qu'on veut prouver** : Soit $(\mathcal{F}_t)_{t \ge 1}$ la filtration de l'épisode et $(e_t)_{t \ge 1}$ une suite de facteurs de preuve conditionnels ($\mathbb{E}_{H_0}[e_t \mid \mathcal{F}_{t-1}] \le 1$). On définit le processus de détection par mélange glissant pondéré :
  $$M_t = \sum_{s=1}^{t} w_{s} \prod_{j=s}^{t} \big((1-\lambda_j) + \lambda_j e_j\big)$$
  avec une suite de poids prévisibles $(\lambda_j) \in [0, 1]$ et $\sum_{s=1}^\infty w_s = 1$. Alors :
  1. *(Sécurité uniforme)* Pour tout temps d'arrêt arbitraire $\tau$, $\mathbb{P}_{H_0}(\exists t \ge 1 : M_t \ge 1/\alpha) \le \alpha$ (via l'inégalité de Ville).
  2. *(Immunité à l'amortissement)* Même si l'adversaire insère des phases arbitrairement longues où $e_j = 0$ (hyper-conformité), toute fenêtre $[s^*, t^*]$ de longueur $L$ où la moyenne géométrique des $e_j$ dépasse un seuil critique déclenche l'alarme avec un délai borné, indépendamment du comportement du processus avant $s^*$.
* **Ce que l'énoncé suppose** :
  1. La propriété de surmartingale sous $H_0$ (absence de dérive hors-échangeabilité non corrigée à chaque pas).
  2. La prévisibilité des poids de pari $\lambda_j$ (qui ne doivent dépendre que de $\mathcal{F}_{j-1}$).

#### D. Théorème de visibilité polynomiale pour les représentations à constante de Lipschitz bornée
* **Ce qu'on veut prouver** : Si un bloc de réseau de neurones $f : \mathbb{R}^d \to \mathbb{R}^d$ de constante de Lipschitz $L$ prend deux décisions aval statistiquement séparées en fonction d'une variable latente binaire $Z \in \{0, 1\}$ tout en satisfaisant la condition d'effacement linéaire $\Sigma_{XZ} = 0$ (aveuglement des sondes linéaires), alors la variance de la projection de $X$ sur les polynômes orthogonaux de degré $2 \le k \le K(L)$ présente nécessairement un écart minoré par une fonction explicite de $L$ et de la séparation aval.
* **Ce que l'énoncé suppose** :
  1. Une borne de régularité (Lipschitz ou norme spectrale bornée des matrices de poids) entre la couche sondée et la couche de sortie.
  2. Que la variable $Z$ est effectivement la cause de la bifurcation de sortie (et non reconstruite ex nihilo à partir d'une source aléatoire externe en aval de la couche sondée).

---

### 5. Vérification externe (en dehors du programme et de son directeur)

Pour que les conclusions ne reposent ni sur l'autorité du directeur ni sur des choix expérimentaux internes biaisés, le protocole de validation doit s'appuyer sur quatre mécanismes externes :

1. **Séparation cryptographique et institutionnelle des rôles (Protocole en double aveugle)** :
   * Une équipe tierce externe génère les mondes plantés (et mélange des épisodes honnêtes et des épisodes à vérité plantée). Elle publie uniquement l'empreinte cryptographique (*hash* SHA-256) des étiquettes de vérité et des paramètres de génération.
   * L'équipe du programme exécute ses moniteurs, fige ses seuils d'alerte et publie ses décisions avant la révélation des clés par le tiers. Cela interdit tout ajustement a posteriori (*p-hacking* des seuils de détection).

2. **Noyau de vérification formelle rejouable (*Proof-Carrying Monitoring*)** :
   * Les théorèmes de la section 4 sont compilés dans un noyau minimaliste (Lean 4).
   * Un auditeur mathématicien externe n'a pas besoin de vérifier les preuves (le noyau le fait), mais doit auditer uniquement **les définitions et les énoncés des théorèmes** (le fichier `.lean` d'interface) pour certifier que les hypothèses ne sont pas tautologiques ou vides de sens pratique.

3. **Jeux publics abstraits (Défis statistiques anonymisés)** :
   * Pour faire tester les agrégateurs et les détecteurs séquentiels par la communauté statistique sans divulguer de détails sur les modèles de langage ni créer de risque de double usage, le programme publie les *matrices de scores et de représentations anonymisées* sous forme d'un problème public de détection de rupture ou de test multiple (sur le modèle des compétitions de détection d'anomalies ou de vérification SAT).

4. **Réplication croisée des « tests de mort » par pré-enregistrement (*Registered Reports*)** :
   * Avant de lancer un test sur banc à vérité plantée, le critère mathématique exact qui tuera la visée (le *test de mort*) est déposé auprès d'un pair réplicateur indépendant. Si le banc d'essai est rejouable via une graine aléatoire fixe et un environnement conteneurisé déterministe, le tiers peut vérifier que la visée a survécu ou est morte sans intervention humaine.

---

### 6. Les risques

#### A. Le risque d'antériorité et le « faux trou » dans la littérature
* **Diagnostic** : La communauté de la sécurité de l'IA (*AI Safety* / *AI Control*) travaille souvent en vase clos terminologique. Ce qui apparaît comme un « trou dans la littérature » si l'on cherche avec les mots-clés *LLM monitor*, *linear probe* ou *AI sabotage* est fréquemment un théorème classique résolu depuis trente ans sous un autre nom.
* **Où se trouvent les faux trous** :
  * En **économétrie et biostatistique** : les tests de mauvaise spécification (*specification testing*), le *p-hacking* séquentiel et le contrôle du taux de fausses découvertes (FDR) sous dépendance positive (Benjamini-Yekutieli).
  * En **traitement du signal radar et sonar** : la détection séquentielle distribuée avec capteurs corrélés (*distributed detection with dependent observations*, Tsitsiklis 1993) et le pistage sous fouillis (*clutter*) non stationnaire.
  * En **cryptographie et stéganalyse** : les bornes de capacité des canaux subliminaux (Simmons, Cachin) et l'indiscernabilité computationnelle.
* **Mitigation** : Exiger pour chaque visée une traduction systématique du problème dans le vocabulaire de la statistique mathématique classique avant toute déclaration de nouveauté.

#### B. Le risque de double usage (*Dual-Use*)
* **Diagnostic** : Lire un théorème d'impossibilité « à l'envers » pour identifier l'hypothèse qui fait échouer un moniteur revient mathématiquement à caractériser **la fonction objectif optimale d'évasion**.
* Par exemple, formaliser comment une représentation satisfaisant certaines contraintes spectrales d'ordre supérieur échappe aux sondes linéaires et quadratiques, ou caractériser la loi d'espacement temporel qui minimise la dérive d'un test séquentiel, fournit directement un terme de régularisation (une fonction de perte) qu'un acteur malveillant pourrait utiliser lors de l'entraînement d'un modèle pour le rendre furtif par construction.

#### C. Ce qui ne doit pas sortir d'une quarantaine
Une frontière stricte doit séparer les **énoncés théoriques** (publiables et utiles à la défense) des **artefacts d'instanciation** (qui doivent rester confinés en quarantaine interne) :
1. **Les fonctions de perte d'évasion opérationnelles** : toute traduction d'une condition mathématique d'indétectabilité (ex. nullité de covariance croisée ou contrainte de copule) en un terme de pénalité différentiable prêt à être branché sur l'entraînement (*fine-tuning* ou RL) d'un modèle de langage.
2. **Les protocoles de transfert d'échelle** : tout résultat montrant comment une stratégie d'aveuglement validée sur un monde mathématique abstrait se traduit concrètement en instructions système, en schémas de raisonnement ou en modifications de poids sur un modèle de frontière.
3. **Les corpus d'artefacts de recherche sabotés réussis** : toute collection d'analyses de données, de preuves mathématiques ou de codes subtils qui ont effectivement trompé l'ensemble des moniteurs du programme.
4. **Les paramètres exacts d'étalonnage des moniteurs déployés** : les architectures précises des sondes, les couches exactes surveillées, les valeurs numériques des seuils d'arrêt séquentiel et les statistiques de détection d'environnement utilisées pour protéger les bancs d'évaluation réels.