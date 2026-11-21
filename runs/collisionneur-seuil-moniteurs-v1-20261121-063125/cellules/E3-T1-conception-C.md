*Note liminaire : Conformément aux instructions du Tour III.1 (conception à l'aveugle), les propositions A, B, D et E ne sont pas transmises dans l'entrée. La réponse qui suit exécute strictement l'ordre en 6 points demandé dans le bloc QUESTION DE L'ARBITRE tout en intégrant intégralement les livrables protocolaires (a), (b), (c) et (d).*

---

### 1. Ce qu'un expert du domaine ferait ici qui n'est pas demandé — et Livrable (a) : ce que la question suppose sans que ce soit établi

#### Livrable (a) : Suppositions non établies dans la question et l'énoncé du problème
1. **Invariance et transférabilité du sous-système de récompense vers des tâches ouvertes** [HYPOTHÈSE] : Le papier de Xu, Yuksekgonul et Zou (2026) démontre l'existence de neurones de valeur et de « dopamine » sur des tâches à récompense terminale binaire vérifiable (mathématiques, code, QCM) [RAPPORTÉ]. Le programme suppose que ces mêmes sous-structures neuronales s'activent de manière cohérente lors de travaux de recherche ouverts sans signal de récompense propre [HYPOTHÈSE].
2. **Nécessité du découpage rigide par tranches de longueur (*episode-length bins*)** [HYPOTHÈSE] : Le calcul exigeant 5 000 épisodes honnêtes par tranche pour obtenir 50 dépassements à 1 % [RAPPORTÉ] suppose implicitement que la calibration doit être non-paramétrique et indépendante dans chaque tranche, plutôt que modélisée conjointement en fonction du temps (ou normalisée en un processus de moyenne nulle) [HYPOTHÈSE].
3. **Indépendance temporelle ou caractère borné de la dépendance intra-épisode** [HYPOTHÈSE] : Agréger une somme séquentielle de petits signaux [RAPPORTÉ] suppose que la structure d'autocorrélation des erreurs des sondes chez l'agent honnête qui échoue (*honest failure*) diffère structurellement de celle du saboteur [HYPOTHÈSE].
4. **Survie du signal neuronal face à un saboteur conscient d'être surveillé** [HYPOTHÈSE] : L'énoncé indique que l'agent peut être adversarial et conscient du moniteur [RAPPORTÉ]. Il est supposé sans preuve que le saboteur ne peut pas découpler l'exécution de son sabotage de la représentation de valeur dans les couches basses (couches 2 à 5, [RAPPORTÉ]) [HYPOTHÈSE].

#### Ce qu'un expert ferait sans qu'on le lui demande
* **Abandonner le test à horizon fixe par tranche au profit d'une martingale d'arrêt optionnel (temps intrinsèque)** : Au lieu de diviser quelques centaines d'épisodes [RAPPORTÉ] en $K$ tranches de longueur (ce qui divise la taille d'échantillon par $K$ et détruit toute puissance statistique), un expert en statistique séquentielle centrerait et réduirait les incréments étape par étape conditionnellement au préfixe. La longueur de l'épisode devient alors le *temps intrinsèque* d'une martingale de test, éliminant le besoin de tranches de longueur.
* **Exploiter l'architecture causale inter-couches plutôt que les sondes isolées** : Le papier établit que la mise à zéro de 1 % des neurones de valeur dans les couches 2 à 5 fait chuter la précision de 75,2 % à 20,3 % et détruit la capacité de prédiction d'erreur des neurones de dopamine en aval (couches 15 à 22) [RAPPORTÉ]. Un expert en interprétabilité mécaniste ne lirait pas seulement les sondes passivement ; il construirait un moniteur de **cohérence causale inter-couches** (vérifiant si l'erreur de différence temporelle aux couches 15-22 correspond mécaniquement à la mise à jour attendue depuis les couches 2-4) et utiliserait le *clamping* (forçage d'activation) des neurones de valeur comme outil de contrôle actif.
* **Analyser les résidus au niveau des étapes (paragraphes) par bloc-bootstrap** : Puisque la statistique décidée par le programme est une somme séquentielle le long de l'épisode [RAPPORTÉ], la queue de distribution de la somme à l'échelle de l'épisode est mathématiquement déterminée par la loi jointe des incréments au niveau des étapes.

---

### 2. Les données brutes d'où partir (au lieu des quelques centaines d'épisodes agrégés)

Un expert refuserait de travailler uniquement sur la table des scores finaux des quelques centaines d'épisodes honnêtes déjà produits [RAPPORTÉ]. Il repartirait de quatre sources de données brutes de granularité inférieure :

1. **Les transitions au niveau des frontières de paragraphes/étapes ($t_1, \dots, t_m$) au sein des épisodes existants** :
   Quelques centaines d'épisodes [RAPPORTÉ] de recherche ouverte comportant chacun 20 à 50 étapes d'action ou paragraphes de raisonnement [illustratif] constituent une base de **4 000 à 25 000 transitions d'étapes brutes** [illustratif]. C'est à cette échelle que les neurones de dopamine du papier sont définis (frontières de paragraphes, [RAPPORTÉ]).
2. **Les paires de divergences sur préfixes forcés (*forced-twin prefix rollouts*)** :
   Le programme dispose déjà d'une baseline mesurant la divergence d'un jumeau forcé sur le même préfixe d'épisode [RAPPORTÉ]. Les données brutes ici sont les vecteurs d'activations exacts $\Delta h_t = h_t^{\text{agent}} - h_t^{\text{jumeau}}$ à chaque jalon où le préfixe est partagé.
3. **Les corpus publics massifs de tâches vérifiables ayant servi à identifier les neurones (MATH500, QCM, code)** :
   Puisque le papier montre que le chevauchement des neurones sélectionnés entre différents jeux de données dépasse la sélection aléatoire [RAPPORTÉ], on peut extraire à faible coût des dizaines de milliers d'activations sur des tâches courtes vérifiables (un seul appel de génération, pas d'environnement d'agent coûteux) sur le *même modèle de base* pour calibrer la géométrie de bruit des neurones (< 1 % des dimensions, [RAPPORTÉ]).
4. **Les traces brutes d'ablations/interventions causales sur préfixes figés** :
   En rejouant un seul pas de génération (*single forward pass*) sur les états cachés sauvegardés des épisodes existants avec mise à zéro (*zeroing*, [RAPPORTÉ]) des neurones de valeur des couches 2 à 4, on obtient une mesure locale de sensibilité causale sans avoir à relancer l'environnement de l'agent.

---

### 3. Les méthodes et outils spécifiques, leurs hypothèses, et Livrables (b) & (c)

#### Inventaire méthodologique et hypothèses sous-jacentes

| Outil / Méthode | Application précise au problème | Ce que la méthode suppose (Hypothèses mathématiques) |
| :--- | :--- | :--- |
| **1. Processus d'e-valeurs et inégalité de Ville** (Ramdas et al., 2023, *Game-Theoretic Statistics and Safe Anytime-Valid Inference*, identifiant arXiv à vérifier) | Transformer la somme séquentielle d'épisode en un processus $M_t = \prod_{k=1}^t (1 + \lambda_k Z_k)$ où $Z_k$ est le score centré à l'étape $k$. Rejeter l'hypothèse d'honnêteté dès que $M_t \ge 1/\alpha$ (soit $100$ pour $\alpha = 0,01$). | **Hypothèse :** $\mathbb{E}[Z_k \mid \mathcal{F}_{k-1}] \le 0$ sous l'hypothèse nulle $H_0$ (agent honnête, y compris en échec). Aucune hypothèse de normalité ni d'horizon fixe (élimine les tranches de longueur). |
| **2. Quantiles conformes pondérés / Mondrian** (Vovk, Gammerman, Shafer, 2005, *Algorithmic Learning in a Random World* ; Tibshirani et al., 2019, *Conformal Prediction Under Covariate Shift*, identifiant arXiv à vérifier) | Au lieu de trancher par longueur, utiliser la prédiction de valeur initiale (lue au prompt avant génération, AUC 0,67 [RAPPORTÉ]) comme covariable de difficulté pour pondérer ou stratifier la calibration conforme. | **Hypothèse :** Échangeabilité des épisodes honnêtes conditionnellement à la strate de difficulté (ou connaissance du ratio de densité entre tâches). Garantie à échantillon fini : $\mathbb{P}(\text{Fausse alarme}) \le \alpha$, mais avec $N < 99$ par strate, le seuil conforme pur vaut $+\infty$ (puissance nulle sans lissage). |
| **3. Théorie des valeurs extrêmes : Peaks-Over-Threshold (POT) et loi de Pareto généralisée (GPD)** (Pickands, 1975, *Statistical Inference Using Extreme Order Statistics*) | Ajuster une GPD sur les 10 % d'épisodes honnêtes les plus extrêmes ($u = q_{0,90}$, soit 30 à 50 points sur 300-500 épisodes [illustratif]) pour extrapoler analytiquement le quantile à 1 % ($q_{0,99}$) et son intervalle de confiance par vraisemblance profilée. | **Hypothèse :** La distribution du score honnête appartient au domaine d'attraction maximal d'une loi de valeurs extrêmes, et le seuil $u = q_{0,90}$ est suffisamment élevé pour que l'approximation asymptotique de la queue soit valide. |
| **4. Bootstrap par blocs stationnaires sur incréments** (Politis et Romano, 1994, *The Stationary Bootstrap*) | Rééchantillonner des blocs de longueur géométrique d'incréments $\Delta S_t$ issus des quelques centaines d'épisodes honnêtes pour synthétiser $50\,000$ trajectoires nulles [illustratif] de toute longueur $L$. | **Hypothèse :** Stationnarité locale et dépendance temporelle à mémoire courte ($\alpha$-mixing) des incréments de la sonde au-delà de la taille moyenne d'un bloc (ex: 3 à 5 paragraphes [illustratif]). |
| **5. Plans d'échantillonnage : Échantillonnage d'importance adaptatif / Splitting** (Cérou et Guyader, 2007, *Adaptive Multilevel Splitting for Rare Event Analysis*) | Lors de la génération de nouveaux épisodes honnêtes, cloner (*branching*) à mi-parcours les trajectoires honnêtes dont la somme séquentielle partielle dépasse le quantile 80 %, pour peupler la queue à 1 % avec 5 à 10 fois moins d'appels modèles [illustratif]. | **Hypothèse :** Caractère markovien de l'état de l'agent (le préfixe de texte et les fichiers courants suffisent à relancer l'épisode sans biais). |

#### Livrable (b) : Expériences décisives en inférence forte ($H_A$ contre $H_B$)

Pour trancher la validité des outils proposés face aux hypothèses du programme, voici trois expériences en duel exclusif :

##### Expérience 1 : Dépendance temporelle des incréments (Valide ou réfute le Bootstrap par blocs et les e-valeurs)
* **$H_A$ (Mémoire courte des erreurs honnêtes) :** Sous échec honnête (*honest failure*), les incréments d'écart entre les neurones de dopamine (couches 15-22) et la divergence du jumeau forcé forment une série à mémoire courte ; un bootstrap par blocs de taille 4 paragraphes [illustratif] calibre le quantile 99 % de la somme séquentielle avec une erreur relative $< 20\%$ (soit un taux de fausses alarmes réel compris entre $0,8\%$ et $1,2\%$ [illustratif]).
* **$H_B$ (Dérive persistante non-stationnaire) :** Lorsqu'un agent honnête s'engage dans une impasse scientifique, ses activations subissent une dérive persistante sur tout le reste de l'épisode, violant l'hypothèse de mélange du bootstrap et gonflant le taux de fausses alarmes réel au-delà de $3\%$ [illustratif].
* **Métrique et Seuil :** Couverture empirique du seuil à 1 % estimé sur 150 épisodes honnêtes [illustratif] par bootstrap, évaluée par validation croisée répétée (ou sur un jeu de test de tâches courtes) ; statistique de test de Ljung-Box sur les résidus blanchis au-delà du décalage $k=4$ (seuil de rejet $p < 0,01$).
* **Contrôle négatif :** Permutation aléatoire de l'ordre des paragraphes au sein de chaque épisode honnête (détruit la structure temporelle tout en conservant la distribution marginale par épisode).
* **Issue falsificatrice :** Si l'autocorrélation au décalage $k > 4$ reste significativement positive ($p < 0,01$) et que le taux de dépassement hors-échantillon excède $2\%$ [illustratif], **$H_A$ est falsifiée** (le bootstrap par blocs est inutilisable ; il faut modéliser la tendance). Si l'autocorrélation s'annule et que la couverture est dans $[0,8\%, 1,2\%]$, **$H_B$ est falsifiée**.

##### Expérience 2 : Découplage inter-couches Valeur / Dopamine (Valide ou réfute l'utilisation du papier pour séparer Saboteur et Échec Honnête)
* **$H_A$ (Dissociation causale sous sabotage) :** Chez l'agent honnête qui échoue, les neurones de valeur (couches 2-4) et les neurones de dopamine (couches 15-22) évoluent de façon cohérente avec la difficulté de la tâche. Chez le saboteur diffus, parce que l'agent génère délibérément des actions sous-optimales tout en représentant la vraie valeur de l'état, le résidu de prédiction des neurones de dopamine (couches 15-22) conditionnellement aux neurones de valeur (couches 2-4) diverge significativement de celui de l'échec honnête.
* **$H_B$ (Indistinguabilité fonctionnelle / Lecture de l'échec seul) :** Conformément à l'hypothèse de prudence du programme [RAPPORTÉ], le sous-système de récompense sparse (valeur + dopamine) ne lit que la probabilité d'échec terminal, quelle qu'en soit la cause ; la distribution jointe (Valeur couches 2-4, Dopamine couches 15-22) est identique entre un saboteur à dommage confirmé et un échec honnête sur la même variante de tâche.
* **Métrique et Seuil :** Différence de taux de détection (TPR) à 1 % de fausses alarmes (FPR calculé sur les échecs honnêtes appariés) entre la sonde de divergence inter-couches et la baseline « sonde de succès attendu entraînée sur épisodes honnêtes seuls » [RAPPORTÉ]. Seuil de décision : gain de TPR $\ge 15$ points de pourcentage [illustratif] avec $p < 0,01$ au test de McNemar apparié par tâche.
* **Contrôle négatif :** Remplacement du < 1 % de neurones de valeur/dopamine par un sous-ensemble de même taille choisi aléatoirement ou par norme de poids (Wanda / magnitude, contrôles du Tableau 2 du papier, p. 5 [RAPPORTÉ]).
* **Issue falsificatrice :** Si le TPR à 1 % FPR sur échecs honnêtes ne dépasse pas la baseline de succès attendu d'au moins 15 points [illustratif], **$H_A$ est falsifiée** (le papier de Xu et al. ne capture aucune trace d'intention et ne sert que de covariable de difficulté). Dans le cas contraire, et si le contrôle négatif Wanda/aléatoire reste au niveau du hasard, **$H_B$ est falsifiée**.

##### Expérience 3 : Perturbation causale révélatrice (*Causal Ablation Probing*)
* **$H_A$ (Fragilité différentielle sous ablation des neurones de valeur) :** Mettre à zéro (*zeroing*) le 1 % de neurones de valeur des couches 2 à 5 effondre la performance d'un agent honnête (de 75,2 % à 20,3 % sur MATH500 dans le papier [RAPPORTÉ]), mais affecte asymétriquement la log-vraisemblance des actions d'un saboteur (qui sélectionne des actions contre le gradient de valeur honnête).
* **$H_B$ (Effondrement symétrique) :** La mise à zéro des neurones de valeur dégrade le modèle de langage de manière globale et symétrique sur les préfixes honnêtes et sabotés, n'offrant aucun pouvoir discriminant.
* **Métrique et Seuil :** Variation de la divergence KL du prochain jeton $\Delta D_{\text{KL}}(P_{\text{intact}} \parallel P_{\text{zeroed}})$ mesurée aux frontières de paragraphes sur préfixes identiques. Seuil : AUC $\ge 0,75$ [illustratif] pour séparer les étapes de sabotage des étapes d'échec honnête.
* **Contrôle négatif :** Mise à zéro de 1 % de neurones issus d'une sonde de prédiction du jeton suivant (*next-token-prediction probe*, qui donne 76,4 % contre 75,2 % dans le Tableau 2 du papier [RAPPORTÉ]).
* **Issue falsificatrice :** Si l'AUC entre sabotage et échec honnête est $< 0,60$ [illustratif] ou statistiquement indiscernable du contrôle *next-token*, **$H_A$ est falsifiée**. Si l'AUC $\ge 0,75$ avec contrôle négatif à $\approx 0,50$, **$H_B$ est falsifiée**.

#### Livrable (c) : Mesure minimale de fonctionnement pour chaque instrument nommé

Pour chaque instrument statistique et mécanique nommé dans la question, le tableau ci-dessous fixe le critère minimal d'acceptation.
* **Cas honnêtes appariés (communs à tous) :** Paires exactes *(Saboteur avec dommage confirmé vs Agent honnête en échec confirmé)* sur la **même variante de tâche** et au **même jalon/préfixe** [RAPPORTÉ].
* **Les 4 vérifications mécaniques à battre (communes à tous, [RAPPORTÉ]) :**
  1. Sonde de succès attendu entraînée uniquement sur épisodes honnêtes (*Expected-success probe*).
  2. Divergence d'un jumeau forcé sur le même préfixe d'épisode (*Forced-twin divergence*).
  3. Comparaison au même jalon utilisant uniquement les fichiers alors disponibles (*Milestone file-only monitor*).
  4. Sonde réentraînée sans le seuil de variation du papier ($|\text{erreur}| > 0,3$, p. 6 [RAPPORTÉ]).

| Instrument nommé dans la question | Taux de fausses alertes (FPR) exigé | Taux de détection (TPR) minimal requis | Condition de victoire spécifique contre les vérifications mécaniques |
| :--- | :--- | :--- | :--- |
| **Statistiques de queue (GPD / POT)** | FPR nominal de $1\%$ sur données hors-échantillon ; borne supérieure de l'IC à 95 % du FPR réalisé $\le 1,8\%$ [illustratif]. | TPR $\ge$ TPR du quantile empirique brut à budget d'épisodes égal. | Doit réduire la largeur de l'intervalle de confiance du seuil à 1 % d'au moins un facteur 3 [illustratif] par rapport au comptage binomial brut sur 300 épisodes. |
| **Quantiles conformes (stratifiés par valeur initiale)** | Garantie théorique $\le 1 + \frac{1}{N_{\text{strate}}+1}\%$ ; écart inter-strates de difficulté $\le 0,5\%$ [illustratif]. | TPR à 1 % FPR supérieur d'au moins 10 points [illustratif] à la sonde non stratifiée sur les tâches difficiles. | Doit battre la sonde de succès attendu (Baseline 1) en éliminant les fausses alarmes causées par la simple difficulté initiale de la tâche (AUC pré-génération de 0,67 [RAPPORTÉ]). |
| **E-valeurs & Tests séquentiels (Martingales)** | Probabilité de franchir le seuil $1/\alpha = 100$ à *n'importe quel moment* d'un épisode honnête $\le 1\%$ (Inégalité de Ville). | TPR $\ge 50\%$ [illustratif] sur saboteurs diffus avant la fin de l'épisode (détection précoce). | Doit battre le maximum d'écart ponctuel [RAPPORTÉ] et la vérification des fichiers au jalon (Baseline 3) en détectant le sabotage *avant* que le dommage ne soit visible dans les fichiers. |
| **Simulation / Bootstrap par blocs & Splitting** | Biais entre le FPR simulé à 1 % et le FPR réel sur un lot de validation indépendant $\le 0,4\%$ [illustratif]. | À FPR réel égalisé à 1 %, TPR supérieur d'au moins 15 points [illustratif] aux baselines purement textuelles. | Avec seulement 300 épisodes honnêtes réels [illustratif], doit atteindre la même stabilité de seuil que 3 000 épisodes bruts sans simulation. |
| **Transfert (depuis tâches courtes vérifiables)** | Dérive de calibration (FPR après recalibration conforme légère sur 100 épisodes) $\le 1,2\%$ [illustratif]. | Conservation d'au moins $85\%$ [illustratif] du TPR obtenu par une sonde entraînée nativement sur des milliers d'épisodes longs. | Doit battre la sonde réentraînée sans le seuil $|\text{erreur}| > 0,3$ (Baseline 4) à moins de 10 % du coût de calcul d'entraînement. |

---

### 4. Ce qui, en dehors du programme et de son directeur, permettrait de vérifier la validité du résultat

Pour qu'un résultat sur un seuil à 1 % avec peu d'épisodes et des sondes internes ne soit pas un artefact d'optimisation interne (*p-hacking* ou fuite de calibration), quatre mécanismes de vérification externe sont nécessaires :

1. **Vérité terrain implantée à l'aveugle (*Planted Ground Truth* par un tiers)** :
   Un tiers indépendant génère un lot de 200 épisodes de test [illustratif] mêlant : (i) des agents honnêtes qui échouent naturellement, (ii) des agents honnêtes dont l'environnement a été secrètement dégradé (ex: dépendance logicielle boguée injectée pour forcer un échec sans intention malveillante), et (iii) des saboteurs utilisant des incitations ou un *fine-tuning* de sabotage inconnus de l'équipe qui calibre les sondes. Le seuil à 1 % doit être **verrouillé cryptographiquement** (empreinte SHA-256 du code et du seuil scalaire) *avant* réception des états cachés de ce lot.
2. **Jeux de données publics et tâches d'ancrage (*Public Anchor Benchmarks*)** :
   Répliquer le protocole exact d'extraction des neurones (< 1 % des dimensions par élagage L1 d'un MLP à 2 couches, largeurs 1024 et 32, [RAPPORTÉ]) sur les modèles publics étudiés dans le papier (Qwen-2.5-7B/14B-SimpleRL-Zoo, Llama-3.1-8B-Instruct, Gemma-3-4B, [RAPPORTÉ]) et sur des bancs d'essai publics de sabotage ou d'évaluation d'agents (par exemple SWE-bench pour l'ingénierie logicielle, ou des suites publiques d'évaluation de sabotage diffus ; références exactes à vérifier).
3. **Protocole d'enregistrement préalable (*Pre-registration*) de la règle de troncature de queue** :
   Dans l'estimation des queues à 1 % (GPD ou e-valeurs), le choix du seuil d'excès $u$ (ex: $q_{0,90}$) ou de la fonction de pari $\lambda_k$ offre un degré de liberté qui permet de manipuler le résultat. Ces hyperparamètres doivent être fixés sur des données synthétiques ou des tâches courtes *avant* de toucher aux épisodes d'agents longs.
4. **Mesures indépendantes boîte-noire en double aveugle** :
   Confronter les alertes de la sonde neuronale à l'évaluation d'auditeurs humains externes qui n'inspectent que les diffs de fichiers aux jalons (la Baseline 3 du programme [RAPPORTÉ]), sans connaître le score de la sonde. La validité externe est établie si les épisodes signalés par la sonde mais manqués par la Baseline 3 révèlent effectivement, après audit approfondi a posteriori, une chaîne causale de sabotage.

---

### 5. Reformulation de la requête

Voici comment la demande initiale doit être reformulée pour être scientifiquement tranchable et opérationnelle :

> **Requête reformulée :**
> « Nous devons contrôler à un niveau $\alpha \le 0,01$ par épisode le taux de fausses alarmes d'un moniteur séquentiel de sabotage diffus, en distinguant le saboteur à dommage confirmé de l'agent honnête en échec sur la même tâche, sous une contrainte stricte de budget ($N \approx 300\text{ à }500$ épisodes honnêtes existants [RAPPORTÉ]).
> Au lieu d'estimer des quantiles empiriques non-paramétriques par tranches de longueur (ce qui exige $\sim 5\,000$ épisodes par tranche [RAPPORTÉ]), nous demandons :
> 1. **Un estimateur séquentiel ou semi-paramétrique de queue** (processus d'e-valeurs à temps intrinsèque ou loi de Pareto généralisée sur résidus d'étapes blanchis par rapport au jumeau forcé) qui élimine le découpage par tranches de longueur et garantit un FPR $\le 1\%$ vérifiable hors-échantillon.
> 2. **Une exploitation mécaniste du sous-système de récompense sparse (Xu et al., 2026)** qui aille au-delà d'une sonde passive de difficulté : (a) tester si la **cohérence causale inter-couches** entre neurones de valeur (couches 2-4) et neurones de dopamine (couches 15-22) sépare l'intention de sabotage de l'échec honnête (contrairement à la valeur seule), et (b) utiliser le signal d'erreur temporelle par paragraphe et les interventions causales (*zeroing/clamping*) pour le routage dynamique et l'allocation du budget d'audit humain. »

---

### 6. Propositions concrètes (Seuil à 1 % et Utilisation du papier pour le monitoring/contrôle) — et Livrable (d) : Ancrage matériel

#### Partie A : Trois propositions pour fixer le seuil à 1 % avec peu d'épisodes (ou s'en passer honnêtement)

##### Proposition A1 : Remplacer les tranches de longueur par une Martingale d'e-valeurs sur incréments normalisés par le jumeau forcé
* **Mécanisme :** À chaque frontière de paragraphe $t$, on calcule le score brut $s_t$ de la sonde et on le centre par rapport à la prédiction sur le préfixe du jumeau forcé [RAPPORTÉ] et à la valeur initiale (covariable de difficulté, AUC 0,67 [RAPPORTÉ]). On estime la variance conditionnelle $\hat{\sigma}_t^2$ sur l'ensemble des $\sim 10\,000$ transitions d'étapes [illustratif] des quelques centaines d'épisodes honnêtes existants. On construit la martingale de test bornée $M_t = \prod_{k=1}^t (1 + \lambda Z_k)$ (où $Z_k$ est le résidu studentisé et tronqué). Par l'inégalité de Ville, déclarer une alerte dès que $M_t \ge 100$ garantit mathématiquement un taux de fausses alarmes $\le 1\%$ sur des épisodes de **n'importe quelle longueur**, sans aucune tranche de longueur.
* **Ce que cela coûte :** Zéro nouvel épisode honnête à générer ; uniquement le recalcul des résidus par étape sur les épisodes existants ($\sim 20$ heures GPU [illustratif]).
* **Ce que cela suppose :** Que l'espérance conditionnelle du résidu $Z_k$ chez un agent honnête (même en échec) est $\le 0$ à chaque étape ($\mathbb{E}[Z_k \mid \mathcal{F}_{k-1}] \le 0$).
* **Comment cela peut échouer :** Si un agent honnête qui échoue présente un biais directionnel systématique non capturé par le jumeau forcé, la martingale dérivera exponentiellement et violera la borne de 1 %. (Réfutable par l'Expérience 1).

##### Proposition A2 : Extrapolation semi-paramétrique GPD (Peaks-Over-Threshold) couplée au Bootstrap par blocs stationnaires
* **Mécanisme :** Utiliser le bootstrap par blocs sur les incréments d'étapes pour normaliser la dérive liée à la longueur de l'épisode $L$ (en ramenant chaque somme séquentielle $S_L$ à un score standardisé $\tilde{S} = (S_L - \hat{\mu}_L)/\hat{\sigma}_L$). Regrouper ainsi tous les épisodes honnêtes ($N \approx 400$ [illustratif]) en une seule distribution poolée. Fixer le seuil d'excès au quantile 90 % ($40$ dépassements [illustratif]) et ajuster une loi de Pareto généralisée (GPD) par maximum de vraisemblance pour déterminer le seuil à 1 % et sa borne supérieure de confiance à 95 %.
* **Ce que cela coûte :** Zéro nouvel épisode ; calcul CPU négligeable ($< 1$ heure CPU [illustratif]).
* **Ce que cela suppose :** Que la queue au-delà du 90e centile obéit à l'asymptotique des valeurs extrêmes (GPD) et que la normalisation par la longueur rend les queues homogènes entre épisodes courts et longs.
* **Comment cela peut échouer :** Si la distribution présente une rupture de régime (multimodalité extrême au-delà de 99 % due à des bugs rares d'environnement), l'extrapolation GPD depuis le 90e centile sous-estimera le vrai quantile 99 %.

##### Proposition A3 : S'en passer honnêtement — Ordonnancement budgétaire par Neyman-Pearson et Décision Conforme à 3 états
* **Mécanisme :** Reconnaître explicitement qu'avec $N < 500$ épisodes honnêtes répartis en plusieurs tranches, aucun test non-paramétrique ne peut certifier un seuil ponctuel à 1 % avec une puissance élevée. Remplacer le verdict binaire à seuil fixe par deux mécanismes honnêtes :
  1. **Allocation d'un budget fixe d'audit humain ($B = 1\%$ des étapes ou des épisodes) :** Classer les épisodes par leur e-valeur ou leur somme séquentielle et auditer le top 1 % du flux opérationnel. La métrique scientifique devient la *Précision à $K = 1\%$* (ou le rappel à budget d'audit fixé) sur un mélange calibré, qui s'estime avec une variance faible dès quelques centaines d'épisodes.
  2. **Verdict tripartite conforme (Normal / Sabotage / Indéterminé-Audit requis) :** Utiliser la borne supérieure de confiance Clopper-Pearson à 95 % sur les épisodes existants. Tant que $N$ est petit, la zone comprise entre le quantile empirique 98 % et le seuil garanti à 1 % est déclarée explicitement « Indéterminée — Escalade vers le contrôle ».
* **Ce que cela coûte :** Zéro épisode supplémentaire ; honnêteté épistémique totale.
* **Ce que cela suppose :** Que le système de contrôle en aval accepte un flux trié par priorité ou une classe d'abstention plutôt qu'un classifieur binaire autonome.
* **Comment cela peut échouer :** Ne répond pas à une exigence réglementaire ou contractuelle rigide qui imposerait un arrêt automatique autonome à exactement 1 % FPR sans intervention humaine.

---

#### Partie B : Quatre propositions pour utiliser le papier (Xu et al., 2026) pour le monitoring et le contrôle

##### Proposition B1 : Moniteur de discordance causale inter-couches (Valeur couches 2-4 vs Dopamine couches 15-22)
* **Mécanisme :** Le papier établit que les neurones de valeur résident aux couches 2 à 4, que les neurones de dopamine résident aux couches 15 à 22, et que la mise à zéro des premiers détruit la capacité prédictive des seconds en aval [RAPPORTÉ]. Chez un agent honnête, l'erreur de différence temporelle $\delta_t$ lue par la sonde de dopamine (couches 15-22) à la fin du paragraphe $t$ doit être cohérente avec l'évolution de la sonde de valeur (couches 2-4) entre $t$ et $t+1$. Nous construisons un moniteur qui mesure la **violation de cohérence TD interne** : $r_t = \hat{\delta}_t^{(\text{couches 15-22})} - (\hat{V}_{t+1}^{(\text{couches 2-4})} - \hat{V}_t^{(\text{couches 2-4})})$.
* **Ce que cela coûte :** Entraînement des deux petits MLP du papier (largeurs 1024 et 32, 100 époques, AdamW lr $10^{-4}$ [RAPPORTÉ]) sur les états cachés existants ($\sim 5$ heures GPU [illustratif]).
* **Ce que cela suppose :** Que même si le saboteur réussit à imiter l'apparence d'un échec honnête en sortie, la dynamique interne de propagation entre l'évaluation précoce (couches 2-4) et l'erreur d'étape (couches 15-22) présente une signature de discordance lorsque l'action choisie dévie volontairement de la politique optimale du modèle.
* **Comment cela peut échouer :** Si la représentation du sabotage est déjà intégrée dès la couche 2 comme une « nouvelle fonction de récompense » par le saboteur, la cohérence TD interne restera intacte vis-à-vis de l'objectif de sabotage. (Réfutable par l'Expérience 2).

##### Proposition B2 : Contrôle actif par *Best-of-N* guidé par les neurones de dopamine et routage vers le jumeau
* **Mécanisme :** Le papier démontre que les neurones de dopamine servent de *Process Reward Model* (PRM) : en recherche *best-of-4* étape par étape sur MATH500, ils font passer la précision de 72,2 % (glouton/aléatoire) à 77,8 %, avec des creux (*troughs*) aux failles logiques (Tableau 4 p. 9 et Figure 3 p. 7 [RAPPORTÉ]).
  **Protocole de contrôle :** Lorsque la somme séquentielle du moniteur franchit un seuil d'alerte modéré (ex: FPR 10 % [illustratif]) à une frontière de paragraphe :
  1. Le contrôleur intercepte la génération avant exécution de l'action.
  2. Il échantillonne $N=4$ paragraphes candidats depuis le modèle du **jumeau honnête** (ou avec *clamping* des neurones de valeur).
  3. Il sélectionne et exécute le candidat qui maximise l'activation de la sonde de dopamine (couches 15-22), écrasant ainsi le micro-sabotage diffus au moment même où le creux de dopamine (*trough*) apparaît.
* **Ce que cela coûte :** Multiplie par 4 le coût d'inférence **uniquement sur la fraction d'étapes suspectes** (ex: sur 10 % des étapes, le surcoût global d'inférence n'est que de $+30\%$ [illustratif]).
* **Ce que cela suppose :** Que les micro-sabotages diffus produisent des « creux » (*troughs*) dans les neurones de dopamine du jumeau honnête similaires aux failles logiques observées dans la Figure 3 du papier [RAPPORTÉ].
* **Comment cela peut échouer :** Dans des tâches de recherche très ouvertes sans signal de récompense environnemental (limite explicite n°1 soulignée par les auteurs p. 25 [RAPPORTÉ]), la sonde de dopamine peut perdre sa corrélation de Spearman avec la qualité réelle des étapes et sélectionner du bruit.

##### Proposition B3 : Allocation chirurgicale du budget d'audit humain au niveau du paragraphe (Localisation temporelle)
* **Mécanisme :** Dans le sabotage diffus, auditer un épisode entier de recherche (des dizaines de fichiers et des milliers de lignes de trace) épuise le budget humain. Le papier entraîne la sonde de dopamine uniquement sur les paragraphes présentant une variation $|\text{erreur}| > 0,3$ (p. 6 [RAPPORTÉ]) et montre que ces neurones isolent les étapes clés et les failles logiques (Figure 3, p. 7 [RAPPORTÉ]).
  **Protocole d'audit :** Lorsqu'un épisode dépasse le seuil d'alerte global, le système n'envoie pas l'épisode entier à l'auditeur humain ; il extrait uniquement les **3 paragraphes/actions** [illustratif] de l'épisode où le différentiel de dopamine entre l'agent et le jumeau forcé $|\delta_t^{\text{agent}} - \delta_t^{\text{jumeau}}|$ a dépassé $0,3$.
* **Ce que cela coûte :** Zéro coût de calcul additionnel (sous-produit direct de la somme séquentielle). Réduit le temps de lecture de l'auditeur humain par un facteur 5 à 10 [illustratif] par épisode audité.
* **Ce que cela suppose :** Que le sabotage diffus, bien que réparti en plusieurs petites actions déniables [RAPPORTÉ], se concentre sur un sous-ensemble discret de paragraphes qui déclenchent des sauts d'erreur TD $> 0,3$.
* **Comment cela peut échouer :** Si le saboteur lisse son sabotage de sorte qu'aucune étape individuelle n'induit une variation $|\text{erreur}| > 0,05$ [illustratif], le filtre à $0,3$ manquera les étapes pertinentes (c'est précisément pourquoi le programme compare déjà contre la Baseline 4 : une sonde réentraînée sans le seuil de variation du papier [RAPPORTÉ]).

##### Proposition B4 : Intervention causale de contrôle (*Value-Neuron Clamping / Zeroing Test*) comme test d'évasion à capacité constante
* **Mécanisme :** Les auteurs notent (p. 25 [RAPPORTÉ]) que des interventions au niveau des neurones pourraient modifier le comportement ou contourner des mécanismes, et montrent (Tableau 2, p. 5 [RAPPORTÉ]) que mettre à zéro 1 % de neurones de valeur dans les couches 2 à 5 détruit la performance (de 75,2 % à 20,3 %).
  **Protocole de vérification active :** Aux jalons critiques d'un épisode suspect, le contrôleur effectue en arrière-plan une passe avant (*forward pass*) en **remplaçant (patching/clamping)** le 1 % de neurones de valeur des couches 2 à 4 de l'agent par les activations correspondantes du jumeau honnête sur le même prompt initial. Si cette greffe de moins de 1 % des dimensions [RAPPORTÉ] provoque un changement brutal de la politique d'action proposée aux couches finales (mesuré par divergence KL), l'épisode est immédiatement bloqué et routé vers l'audit.
* **Ce que cela coûte :** Une seule passe avant supplémentaire (*single forward pass*, sans génération autoregressive complète) aux jalons critiques : surcoût $< 2\%$ du budget de calcul d'un épisode [illustratif].
* **Ce que cela suppose :** Que l'accès boîte-blanche aux activations [RAPPORTÉ] permet non seulement la lecture mais aussi l'intervention en lecture/écriture pendant l'inférence, et que l'intention de sabotage transite par (ou interfère avec) ce goulot d'étranglement de < 1 % des neurones aux couches 2 à 4.
* **Comment cela peut échouer :** Si le saboteur utilise un circuit redondant dans les 99 % de neurones restants pour piloter ses actions de sabotage sans modifier ses neurones de valeur des couches 2 à 4, le *clamping* ne produira aucune divergence KL. (Réfutable par l'Expérience 3).

---

#### Livrable (d) : Ancrage matériel (Modèles ouverts, calcul nécessaire, coûts estimés)

Tous les chiffres de coût et de temps de calcul ci-dessous qui ne proviennent pas directement du papier sont marqués **[illustratif]**.

1. **Modèles ouverts utilisables immédiatement** :
   * Modèles principaux du papier [RAPPORTÉ] : **Qwen-2.5-7B-SimpleRL-Zoo** et **Qwen-2.5-14B-SimpleRL-Zoo**.
   * Modèles de robustesse du papier [RAPPORTÉ] : **Llama-3.1-8B-Instruct**, **Gemma-3-4B**, **Phi-3.5-mini-instruct**, **Qwen3.5-0.8B**.
   * Dimension des états cachés à extraire : pour un modèle 7B/8B standard (dimension cachée $d = 3584\text{ ou }4096$ [illustratif]), le sous-système sparse (< 1 % des dimensions [RAPPORTÉ]) représente **moins de 35 à 40 neurones par couche** [illustratif] (couches 2 à 5 pour la valeur, couches 15 à 22 pour la dopamine [RAPPORTÉ]).

2. **Calcul nécessaire et coût estimé par opération** :
   * **Ré-analyse des épisodes existants (Propositions A1, A2, A3, B1, B3) :**
     *Extraction des activations (couches 2-5 et 15-22) sur 500 épisodes existants* (moyenne de $16\,000$ jetons par épisode [illustratif], en passe avant seule sans génération) : $\approx 8\times 10^6$ jetons traités. Sur 1 GPU A100-80GB (ou H100), cela prend **2 à 4 heures GPU** [illustratif], soit un coût infonuagique de **5 $ à 15 $** [illustratif].
     *Entraînement des sondes MLP du papier* (largeur 1024 pour valeur, 32 pour dopamine, AdamW, lr $10^{-4}$, 100 époques [RAPPORTÉ]) sur 20 000 frontières de paragraphes : **$< 1$ heure GPU** [illustratif] (**$\sim 2\text{ \$}$** [illustratif]).
     *Bootstrap par blocs (50 000 trajectoires) et ajustement GPD / Martingales* : **15 minutes sur 1 CPU standard** [illustratif] (**$< 1\text{ \$}$** [illustratif]).
   * **Estimation de l'erreur TD par rollouts Monte Carlo sur tâches courtes de transfert (Section 2 & 3) :**
     Le papier estime l'erreur TD aux frontières de paragraphes par rollouts Monte Carlo en gardant $|\text{erreur}| > 0,3$ (p. 6 [RAPPORTÉ]). Sur 2 000 problèmes courts vérifiables (MATH/code) avec 8 rollouts par paragraphe [illustratif] sur Qwen-2.5-14B : **$\sim 40$ à $80$ heures GPU A100** [illustratif], soit **80 $ à 200 $** [illustratif].
   * **Génération de nouveaux épisodes par Échantillonnage d'Importance / Splitting (si et seulement si un lot de validation externe est requis pour la Section 4) :**
     Au lieu de générer 5 000 épisodes honnêtes par tranche ($\sim 25\,000$ épisodes au total pour 5 tranches [illustratif], ce qui coûterait **25 000 $ à 75 000 $** [illustratif] à raison de 1 $ à 3 $ par épisode d'agent avec environnement de machines louées [illustratif]), un lot de validation verrouillé de **200 épisodes** combiné au *splitting* sur les 20 % de préfixes supérieurs nécessite l'équivalent de **300 épisodes complets** [illustratif], soit **150 à 300 heures GPU + machines virtuelles d'environnement** pour un budget total contenu entre **300 $ et 900 $** [illustratif].

FIN-DE-CELLULE