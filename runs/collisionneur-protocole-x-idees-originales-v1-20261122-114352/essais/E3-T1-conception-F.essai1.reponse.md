# Proposition F — Conception ciblée (Tour III.1)

**Constat de réception (Règle 2)** : le bloc `FAITS` est identique au bloc `QUESTION DE L'ARBITRE` (même empreinte sha256) et ne contient aucune donnée empirique préalable ni pièce annexe ; aucun fait empirique du problème n'a donc le statut `VÉRIFIÉ`.

---

## 1. Présupposés non établis de la question et reformulation — Livrable (a) & Q5

### 1.1 Ce que la question suppose sans que ce soit établi

Chaque présupposé implicite de l'énoncé porte le statut `HYPOTHÈSE` :

1. **A1 — Transfert de fiabilité du contrôleur vers les idées rares** (`HYPOTHÈSE`) : l'énoncé suppose qu'un contrôleur fiable sur des cas d'essai à vérité connue reste fiable sur des idées *rares* (potentiellement hors distribution). Or, optimiser pour des idées à la fois rares et acceptées par un contrôleur concentre la sélection sur ses angles morts (spécification incomplète, exploitation du vérificateur).
2. **A2 — Existence d'une relation d'équivalence mécanique entre idées** (`HYPOTHÈSE`) : parler de « mêmes idées » et de « rareté » sans jugement de modèle suppose qu'une relation d'équivalence $\sim$ partitionne déjà les propositions en classes d'équivalence $[x]$. Sans $\sim$, deux paraphrases d'un mécanisme banal paraissent « rares », et deux mécanismes proches mais distincts risquent d'être confondus.
3. **A3 — Coïncidence entre rareté sous le système et valeur scientifique** (`HYPOTHÈSE`) : la rareté est relative à la distribution $P_0$ du système (modèles, prompts, décodage). Une idée rare sous $P_0$ et validée peut être triviale (variante obfusquée d'une idée fréquente), redondante ou déjà connue hors corpus d'entraînement.
4. **A4 — Accessibilité effective de « puits étroits »** (`HYPOTHÈSE`) : l'énoncé suppose l'existence d'idées valides de probabilité $p_0([x]) \in (0, \tau]$ atteignables par réallocation de budget, plutôt que de probabilité quasi nulle (hors support des modèles) ou d'un simple défaut de réglage d'échantillonnage.
5. **A5 — Homogénéité du « coût total égal »** (`HYPOTHÈSE`) : la question ne sépare pas coût de génération ($C_{\text{gen}}$), coût de canonisation ($C_{\text{canon}}$) et coût de vérification ($C_{\text{verif}}$). L'intervention optimale change radicalement selon que $C_{\text{verif}} \ll C_{\text{gen}}$ ou $C_{\text{verif}} \gg C_{\text{gen}}$.
6. **A6 — Indépendance opérationnelle entre générateurs et contrôleur** (`HYPOTHÈSE`) : un contrôleur « indépendant des modèles » dans son implémentation peut néanmoins être contaminé si les cas d'essai ou des artefacts du simulateur figurent dans les données de pré-entraînement.
7. **A7 — Stabilité des fausses découvertes sous exploration intensive** (`HYPOTHÈSE`) : augmenter le nombre de candidats rares testés, ou réutiliser les retours du contrôleur dans une boucle adaptative, accroît mécaniquement les fausses découvertes par tests multiples et effet du taux de base si aucun verrou statistique global n'est ajouté.
8. **A8 — Gain intrinsèque de la pluralité des modèles** (`HYPOTHÈSE`) : utiliser « plusieurs modèles de langue » n'assure pas une meilleure couverture qu'un modèle unique à coût égal si ces modèles partagent des corpus et des alignements fortement corrélés.

### 1.2 Pourquoi le problème est mal posé et comment le reposer (Q5)

Le problème initial est mal posé sur trois points : (i) il demande de mesurer la rareté sans définir d'espace canonisable où l'identité d'une idée soit testable sans modèle ; (ii) il traite la confirmation comme un bit invariant, ignorant le taux de base infime des idées rares et l'inflation des fausses découvertes en test multiple ; (iii) il omet la structure du coût total $B = C_{\text{gen}} + C_{\text{canon}} + C_{\text{verif}}$ et la séparation entre contrôle de recherche et contrôle d'audit.

**Reformulation** (`HYPOTHÈSE` de cadre opératoire) : restreindre le domaine à des idées exprimables dans un **formalisme exécutable ou canonisable** $\mathcal{X}$ (programmes, équations symboliques, graphes/molécules, preuves formelles, stratégies de jeu), muni :
- d'une relation d'équivalence mécanique $\sim$ (définissant les classes $[x]$ sans modèle juge) ;
- d'une partition étanche du contrôleur indépendant en un contrôle de développement $\Phi_{\text{dev}}$ (utilisable dans les boucles de recherche) et un contrôle d'audit gelé/hors-distribution $\Phi_{\text{audit}}$ (à usage contrôlé, généré après coupure temporelle des modèles) ;
- d'une fonction de valeur $V([x])$ multi-critères vérifiée sur $\Phi_{\text{audit}}$ ;
- d'une borne stricte de taux de fausses découvertes $\text{FDR}_{\text{audit}} \le \alpha$ (illustratif) sous contrôle séquentiel.

L'objectif bien posé devient : **à budget total physique fixe $B = C_{\text{gen}} + C_{\text{canon}} + C_{\text{verif}}$, maximiser le nombre de classes distinctes $[x]$ à la fois rares sous la distribution de base ($p_0([x]) \le \tau$), de valeur auditée élevée ($V_{\text{audit}}([x]) \ge v_0$) et non dominées en complexité/couverture, tout en maintenant $\text{FDR}_{\text{audit}} \le \alpha$.**

---

## 2. Mesurer la rareté et la valeur sans jugement de modèle — Q1

### 2.1 Rareté sans modèle juge

Toute mesure de rareté exige d'abord d'identifier quand deux sorties représentent la « même idée » :

1. **Canonisation mécanique ($\sim$)** (`HYPOTHÈSE` d'instrumentation) : réduire chaque proposition $x \in \mathcal{X}$ à une signature mécanique : forme normale algébrique/symbolique, hachage structurel d'arbre syntaxique (AST) ou de graphe, et surtout **signature comportementale** (vecteur de sorties déterministes sur une batterie fixe de sondes d'entrée-sortie distinctes de $\mathcal{T}_{\text{audit}}$). Deux propositions à signatures comportementales identiques sur la batterie de sondes (et même classe structurelle minimale) appartiennent à la même classe $[x]$.
2. **Estimation de fréquence sous la référence $P_0$** : exécuter un échantillon pilote indépendant de $N_0$ appels i.i.d. du système de base figé. Pour une classe observée $k$ fois, on estime sa fréquence empirique $\hat{p}_0([x]) = k/N_0$ et sa borne supérieure exacte de confiance binomiale (Clopper-Pearson) ; si $k = 0$, la borne supérieure au niveau $1-\delta$ vaut $1 - \delta^{1/N_0} \approx -\ln(\delta)/N_0$. Une idée est déclarée rare au seuil $\tau$ si cette borne supérieure (ou l'estimateur régularisé) satisfait $\hat{p}_0^+([x]) \le \tau$.
3. **Diagnostic de redécouverte (réponse à « on ignore si des appels indépendants reviennent aux mêmes idées »)** : utiliser l'estimateur de couverture d'échantillon de Good-Turing (`RAPPORTÉ` : Good, I. J., 1953, *The Population Frequencies of Species and the Estimation of Population Parameters*, Biometrika), $\hat{C} = 1 - f_1 / N_0$ (où $f_1$ est le nombre de classes vues exactement une fois), et la borne inférieure non paramétrique de richesse de classes Chao1 (`RAPPORTÉ` : Chao, A., 1984, *Nonparametric Estimation of the Number of Classes in a Population*, Scandinavian Journal of Statistics), $\hat{S}_{\text{Chao1}} = S_{\text{obs}} + f_1^2 / (2 f_2)$. Si $\hat{C}$ est proche de $1$ et $f_1$ faible, les appels indépendants reviennent fortement aux mêmes idées ; sinon, le système explore encore des classes non saturées.
4. **Rareté structurelle complémentaire** : distance de compression normalisée (compresseur sans perte standard, ex. zstd) ou distance d'édition d'AST par rapport à l'ensemble des classes fréquentes et à un corpus de référence encodé dans le même formalisme, afin de repérer les variantes cosmétiques.

*Limite stricte* : dans un domaine purement textuel sans sémantique exécutable ni canonisation formelle, il n'existe pas de mesure de rareté sémantique strictement sans modèle capable de séparer paraphrase superficielle et idée nouvelle (voir section 5).

### 2.2 Valeur sans modèle juge

La confirmation binaire ne suffit pas à mesurer la valeur. On combine quatre mesures purement mécaniques et statistiques sur $\Phi_{\text{audit}}$ :

1. **Gain de performance hors distribution** : écart $\Delta S_{\text{audit}}([x])$ par rapport à la meilleure référence mécanique connue, évalué sur des instances $\mathcal{T}_{\text{audit}}$ jamais exposées pendant la recherche (et testé sous perturbations d'invariance / tests métamorphiques).
2. **Principe de longueur de description minimale (MDL) / front de Pareto** (`RAPPORTÉ` : Rissanen, J., 1978, *Modeling by shortest data description*, Automatica) : rapporter la performance vérifiée à la longueur encodée (bits du programme/formule minimal dans sa classe $[x]$) et au coût d'exécution. Cela élimine les idées « rares » par simple gonflement syntaxique ou sur-ajustement.
3. **Gain marginal de portefeuille (complémentarité)** : fraction des instances d'audit résolues par $[x]$ qui échouent pour l'union de toutes les classes fréquentes validées ($p_0 > \tau$). Une idée rare qui n'améliore la couverture sur aucune instance n'a pas de valeur marginale mesurable.
4. **Verrou statistique anti-fausses découvertes** : associer à chaque candidat soumis à $\Phi_{\text{audit}}$ une *p-value* ou une *e-value* sous l'hypothèse nulle de non-validité/chance, et contrôler le FDR via Benjamini-Hochberg (`RAPPORTÉ` : Benjamini, Y., & Hochberg, Y., 1995, *Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing*, Journal of the Royal Statistical Society: Series B) en lot fixe, ou via l'inférence séquentielle *anytime-valid* par *e-values* (`RAPPORTÉ` : Ramdas, A., Grünwald, P., Vovk, V., & Shafer, G., 2023, *Game-Theoretic Statistics and Safe Anytime-Valid Inference*, Statistical Science) en exploration continue.

---

## 3. Interventions à coût total égal — Q2

Toutes les interventions ci-dessous sont comparées à budget physique total égal $B = C_{\text{gen}} + C_{\text{canon}} + C_{\text{verif}}$, contre la ligne de base $I_0$ (appels indépendants i.i.d. du meilleur modèle unique avec déduplication post-canonisation). Pour chaque intervention, le statut des effets attendus sur le système cible est `HYPOTHÈSE`, et celui des travaux cités est `RAPPORTÉ`.

### I1 — Hétérogénéité réelle de modèles (familles + modèles de base/peu alignés) avec décodage contraint et déduplication pré-vérification

- **Mécanisme** : répartir $C_{\text{gen}}$ entre plusieurs familles de modèles à pré-entraînements/architectures distincts, en incluant des modèles de base (ou peu alignés RLHF) dont la sortie est contrainte syntaxiquement au formalisme $\mathcal{X}$ par décodage contraint mécanique ; canoniser et dédupliquer *avant* tout appel à $\Phi$.
- **Ce qu'elle garantit (et sous quelles hypothèses)** : garantit mécaniquement zéro dépense de $C_{\text{verif}}$ sur des doublons sous $\sim$. Sous hypothèse que les queues de distribution des modèles sont partiellement disjointes et que la contrainte syntaxique préserve une précision suffisante des modèles peu alignés, elle élargit le support effectif des classes proposées par unité de coût.
- **Ce qu'elle ne garantit pas** : n'assure pas que les queues supplémentaires contiennent des idées *valides* (peut diluer la précision) ; ne crée rien hors de l'union des supports des modèles ; ne borne pas les fausses découvertes sans verrou sur $\Phi_{\text{audit}}$.
- **Meilleur indice pour** : Padmakumar, V., & He, H. (2024), *Does Writing with Language Models Reduce Content Diversity?*, ICLR 2024 (`RAPPORTÉ`, confiance élevée dans l'attribution : montre que l'alignement par rétroaction humaine réduit la diversité de contenu par rapport aux modèles de base) ; Holtzman, A., Buys, J., Du, L., Forbes, M., & Choi, Y. (2020), *The Curious Case of Neural Text Degeneration*, ICLR 2020 (`RAPPORTÉ`, confiance élevée : montre le piégeage modal du décodage avide) ; Dietterich, T. G. (2000), *Ensemble Methods in Machine Learning*, Multiple Classifier Systems (`RAPPORTÉ`, confiance élevée : gain d'ensemble conditionné à la décorrélation des erreurs).
- **Meilleur indice contre** : convergence et perte des queues lorsque des modèles partagent des corpus ou des données synthétiques recouvrants — Shumailov, I., Shumaylov, Z., Zhao, Y., Papernot, N., Anderson, R., & Gal, Y. (2024), *AI models collapse when trained on recursively generated data*, Nature (`RAPPORTÉ`, confiance élevée) ; coût de qualité des modèles moins alignés ou à haute entropie dans les tâches exigeant une forte précision logique (*référence à vérifier*).

### I2 — Archive Qualité-Diversité (MAP-Elites) à descripteurs mécaniques, couplée à une séparation étanche $\Phi_{\text{dev}} / \Phi_{\text{audit}}$

- **Mécanisme** : maintenir une grille de cellules indexée par des descripteurs purement mécaniques (complexité, invariants structurels, profil binaire de réussite sur $\mathcal{T}_{\text{dev}}$). Sélectionner des parents issus de cellules rares ou sous-explorées pour muter/recombiner via les modèles, évaluer sur $\Phi_{\text{dev}}$, puis soumettre les seules élites rares nouvelles à l'audit isolé $\Phi_{\text{audit}}$ sous verrou *e-values*.
- **Ce qu'elle garantit (et sous quelles hypothèses)** : sous hypothèse d'existence de « tremplins » intermédiaires et de descripteurs alignés avec les bassins du problème, empêche la convergence vers le mode dominant en protégeant les solutions structurellement distinctes ; maintient $\text{FDR}_{\text{audit}} \le \alpha$ tant que $\Phi_{\text{audit}}$ reste strictement étanche.
- **Ce qu'elle ne garantit pas** : échoue sur un paysage sans signal intermédiaire ; amplifie le sur-ajustement à $\Phi_{\text{dev}}$ si $\Phi_{\text{dev}}$ est imparfait (chute du rendement après filtrage par $\Phi_{\text{audit}}$) ; gaspille $B$ si les descripteurs partitionnent des axes non pertinents.
- **Meilleur indice pour** : Mouret, J.-B., & Clune, J. (2015), *Illuminating search spaces by mapping elites* (`RAPPORTÉ`, confiance élevée) ; Lehman, J., & Stanley, K. O. (2011), *Abandoning Objectives: Evolution Through the Search for Novelty Alone*, Evolutionary Computation (`RAPPORTÉ`, confiance élevée) ; Romera-Paredes, B., Barekatain, M., Novikov, A., Balog, M., Kumar, M. P., Dupont, E., Ruiz, F. J. R., Ellenberg, J. S., Wang, P., Fawzi, O., Kohli, P., & Fawzi, A. (2024), *Mathematical discoveries from program search with large language models*, Nature (`RAPPORTÉ`, confiance élevée sur titre/revue/année et auteurs principaux, modérée sur l'ordre exact des co-auteurs intermédiaires).
- **Meilleur indice contre** : l'optimisation adaptative contre un proxy ou un banc fixe amplifie le *reward hacking* et brise la validité statistique — Skalse, J., Howe, N. H. R., Krasheninnikov, D., & Krueger, D. (2022), *Defining and Characterizing Reward Hacking*, NeurIPS 2022 (`RAPPORTÉ`, confiance élevée) et Dwork, C., Feldman, V., Hardt, M., Pitassi, T., Reingold, O., & Roth, A. (2015), *The reusable holdout: Preserving validity in adaptive data analysis*, Science (`RAPPORTÉ`, confiance élevée) ; absence de gain sans structure exploitable — Wolpert, D. H., & Macready, W. G. (1997), *No Free Lunch Theorems for Optimization*, IEEE Transactions on Evolutionary Computation (`RAPPORTÉ`, confiance élevée).

### I3 — Exclusion mécanique des modes dominants et ciblage des cas résiduels

- **Mécanisme** : extraire automatiquement les motifs structurels des $K$ classes les plus fréquentes de $P_0$ et les sous-ensembles de $\mathcal{T}_{\text{dev}}$ encore non résolus ; imposer soit une exclusion structurelle au décodage/filtrage pré-vérification, soit un conditionnement exclusif sur les cas d'échec résiduels de $\mathcal{T}_{\text{dev}}$ (sans s'en remettre à une simple négation verbale dans le prompt).
- **Ce qu'elle garantit (et sous quelles hypothèses)** : garantit zéro redécouverte des motifs exclus au-delà du filtre mécanique et concentre le budget sur les lacunes de la couverture existante. Sous hypothèse que des idées rares valides existent hors des motifs exclus et que le générateur reste cohérent sous contrainte, accroît la découverte de classes complémentaires.
- **Ce qu'elle ne garantit pas** : peut exclure des briques élémentaires indispensables aux solutions rares ; peut provoquer une chute brutale de validité conditionnelle sous décodage contraint ; n'offre aucune protection propre contre les faux positifs.
- **Meilleur indice pour** : principe de focalisation sur les erreurs résiduelles / complémentarité d'ensembles (cadre analysé dans Dietterich, 2000, `RAPPORTÉ`, confiance élevée) ; efficacité des clauses d'exclusion (*blocking clauses*) dans la recherche symbolique et les solveurs formels (*référence à vérifier*).
- **Meilleur indice contre** : difficulté documentée des modèles de langue à respecter la négation en langage naturel (effet rebond) et dégradation possible de la distribution conditionnelle sous contraintes dures de décodage (*références à vérifier*).

### I4 — Cascade de filtres mécaniques rapides + allocation bandit (UCB) entre stratégies + verrou séquentiel par *e-values*

- **Mécanisme** : lorsque $C_{\text{verif}} \gg C_{\text{gen}}$, placer avant $\Phi$ une cascade de filtres mécaniques peu coûteux (analyse statique, invariants, sous-échantillon rapide de $\mathcal{T}_{\text{dev}}$), allouer dynamiquement le budget entre bras génératifs (modèles, températures, prompts) via UCB récompensé par les classes rares nouvelles sur $\Phi_{\text{dev}}$, et contrôler l'acceptation finale sur $\Phi_{\text{audit}}$ par *e-values*.
- **Ce qu'elle garantit (et sous quelles hypothèses)** : garantit un contrôle *anytime-valid* du taux d'erreur de type I / FDR sur $\Phi_{\text{audit}}$ sous validité des *e-values* sous l'hypothèse nulle (Ramdas et al., 2023) ; garantit un regret logarithmique d'allocation entre bras sous stationnarité locale des taux de découverte (Auer, Cesa-Bianchi & Fischer, 2002).
- **Ce qu'elle ne garantit pas** : n'invente pas de couverture absente des bras ; viole la stationnarité dès que les puits rares d'un bras s'épuisent ; risque de rejeter précisément les idées rares non conventionnelles si les filtres amont ont des faux négatifs biaisés.
- **Meilleur indice pour** : Auer, P., Cesa-Bianchi, N., & Fischer, P. (2002), *Finite-time Analysis of the Multiarmed Bandit Problem*, Machine Learning (`RAPPORTÉ`, confiance élevée) ; Ramdas et al. (2023, `RAPPORTÉ`, confiance élevée) ; Benjamini & Hochberg (1995, `RAPPORTÉ`, confiance élevée).
- **Meilleur indice contre** : perte de puissance statistique des tests *anytime-valid* par rapport aux tests à horizon fixe (discutée dans Ramdas et al., 2023, `RAPPORTÉ`, confiance élevée) ; mauvaise allocation des bandits stationnaires en régime d'épuisement des ressources (*rotting bandits*, *référence à vérifier*).

---

## 4. Expériences décisives en inférence forte et critères d'abandon — Livrable (b) & Q3

Toutes les expériences sont conduites sur au moins 3 domaines canonisables avec instances d'audit générées après coupure des modèles (anti-contamination) et au moins 5 graines (illustratif). **Tout chiffre ci-dessous est marqué « illustratif ».** Le budget total $B$ inclut génération, canonisation, filtrage et vérifications.

### E0 — Diagnostic préalable : existence de puits étroits et redécouverte

- **$H_{A0}$** : sous $N_0 = 10\,000$ appels i.i.d. de $P_0$ (illustratif), les appels saturent les mêmes classes ($\hat{C}_{\text{Good-Turing}} \ge 0{,}85$, illustratif) tandis qu'un oracle de construction ou une recherche exhaustive locale prouve l'existence d'idées valides de masse $p_0 \le \tau = 10^{-3}$ (illustratif) résolvant des cas échoués par le bassin dominant.
- **$H_{B0}$** : soit les appels ne reviennent pas aux mêmes classes ($\hat{C} < 0{,}30$, illustratif : pas d'effondrement modal), soit la queue ($p_0 \le \tau$) ne contient aucune classe valide au-delà du taux nul de fausses alertes.
- **Métrique & seuil** : couverture $\hat{C}$ et nombre $R_0$ de classes rares validées sur $\Phi_{\text{audit}}$ (seuils ci-dessus, illustratif).
- **Contrôle négatif** : générateur aléatoire syntaxiquement valide de même budget + permutation aléatoire des étiquettes d'audit pour mesurer le taux nul de fausses alertes.
- **Falsification** : observer $\hat{C} < 0{,}30$ ou $R_0$ indiscernable du contrôle négatif falsifie $H_{A0}$ (invalide la prémisse « puits étroits » sur ce domaine) ; observer $\hat{C} \ge 0{,}85$ avec présence vérifiée de solutions rares complémentaires falsifie $H_{B0}$.

### E1 — Duel pour I1 (abandon ou maintien de l'hétérogénéité de modèles)

- **$H_{A1}$** : à budget $B$ égal, I1 (panachage multi-familles incluant modèles peu alignés + décodage contraint + déduplication pré-vérification) obtient un gain relatif $\ge +25\,\%$ (illustratif) de classes rares validées à valeur marginale positive sur $\Phi_{\text{audit}}$ ($p < 0{,}01$, test de permutation apparié sur graines, illustratif) par rapport à $I_0$ (meilleur modèle unique + déduplication), avec $\text{FDR}_{\text{audit}} \le 0{,}05$ (illustratif).
- **$H_{B1}$** : à budget $B$ égal, $I_0$ égalise ou bat I1 (gain $\le 0\,\%$, ou borne supérieure de l'IC à $95\,\%$ inférieure à $+10\,\%$, illustratif), ou I1 dépasse $\text{FDR}_{\text{audit}} > 0{,}05$ (illustratif).
- **Métrique & seuil** : débit net $D_{\text{rare}} = |\{\,[x] : \hat{p}_0^+ \le \tau,\; V_{\text{audit}} \ge v_0\,\}| / B$ et $\text{FDR}_{\text{audit}}$ ; seuils ci-dessus (illustratif).
- **Contrôle négatif** : remplacer les modèles additionnels de I1 par des clones du meilleur modèle unique avec simples variations de prompt/graine au même budget $B$.
- **Falsification & critère d'abandon de I1** : **abandonner I1** si $H_{B1}$ se réalise ou si I1 ne bat pas son contrôle négatif à $+15\,\%$ (illustratif, falsifiant $H_{A1}$). Observer le gain $\ge +25\,\%$ contre $I_0$ et le contrôle négatif à $\text{FDR} \le 0{,}05$ falsifie $H_{B1}$.

### E2 — Duel pour I2 (abandon ou maintien de MAP-Elites mécanique)

- **$H_{A2}$** : à budget $B$ égal, I2 augmente $D_{\text{rare}}$ sur $\Phi_{\text{audit}}$ d'au moins $+30\,\%$ (illustratif) par rapport à l'échantillonnage parallèle indépendant $I_0$, avec un taux de transfert $\Phi_{\text{dev}} \to \Phi_{\text{audit}}$ au moins égal à $80\,\%$ de celui de $I_0$ (illustratif) et $\text{FDR}_{\text{audit}} \le 0{,}05$ (illustratif).
- **$H_{B2}$** : I2 n'améliore pas $D_{\text{rare}}$ sur $\Phi_{\text{audit}}$ (gain $< +10\,\%$, illustratif) ou présente un effondrement de transfert $\Phi_{\text{dev}} \to \Phi_{\text{audit}}$ ($< 50\,\%$ de celui de $I_0$, illustratif : preuve de sur-exploitation de $\Phi_{\text{dev}}$).
- **Métrique & seuil** : $D_{\text{rare}}$ sur $\Phi_{\text{audit}}$, ratio de transfert $\Phi_{\text{dev}} \to \Phi_{\text{audit}}$, $\text{FDR}_{\text{audit}}$ (seuils illustratifs).
- **Contrôle négatif** : MAP-Elites avec descripteurs de cellules **aléatoires** (hachage uniforme dans la même grille) à budget $B$ égal.
- **Falsification & critère d'abandon de I2** : **abandonner I2** si $H_{B2}$ se réalise ou si I2 ne dépasse pas le contrôle à descripteurs aléatoires (falsifiant $H_{A2}$). Un gain $\ge +30\,\%$ sur $\Phi_{\text{audit}}$ et au-dessus du contrôle aléatoire sans chute de transfert falsifie $H_{B2}$.

### E3 — Duel pour I3 (abandon ou maintien de l'exclusion mécanique des modes)

- **$H_{A3}$** : à budget $B$ égal, I3 (exclusion mécanique des $K$ modes dominants + ciblage des cas résiduels de $\mathcal{T}_{\text{dev}}$) augmente $D_{\text{rare}}$ sur $\Phi_{\text{audit}}$ d'au moins $+20\,\%$ (illustratif) par rapport à $I_0$ (ré-échantillonnage dédupliqué), à $\text{FDR}_{\text{audit}} \le 0{,}05$ (illustratif).
- **$H_{B3}$** : la contrainte d'exclusion dégrade la validité conditionnelle au point que $D_{\text{rare}}$ sur $\Phi_{\text{audit}}$ reste inférieur ou égal à $I_0$ (ou gain $< +5\,\%$, illustratif).
- **Métrique & seuil** : $D_{\text{rare}}$ sur $\Phi_{\text{audit}}$, taux de validité conditionnelle par appel, $\text{FDR}_{\text{audit}}$ (seuils illustratifs).
- **Contrôle négatif** : (1) même exclusion formulée uniquement en négation textuelle dans le prompt sans verrou mécanique ; (2) exclusion mécanique de $K$ motifs *aléatoires* non dominants.
- **Falsification & critère d'abandon de I3** : **abandonner I3** si $H_{B3}$ se réalise ou si le contrôle à exclusion aléatoire égale I3 (falsifiant $H_{A3}$). Un gain $\ge +20\,\%$ battant $I_0$ et les deux contrôles négatifs falsifie $H_{B3}$.

### E4 — Duel pour I4 (abandon ou maintien de la cascade + bandit + *e-values*)

- **$H_{A4}$** : dans un régime où $c_{\text{verif}}/c_{\text{gen}} \ge 10$ (illustratif), I4 augmente $D_{\text{rare}}$ sur $\Phi_{\text{audit}}$ d'au moins $+25\,\%$ (illustratif) par rapport à l'allocation uniforme avec vérification complète à budget $B$ égal, tout en maintenant le taux de faux négatifs des filtres amont sur les idées rares valides $\le 10\,\%$ (illustratif) et $\text{FDR}_{\text{audit}} \le 0{,}05$ (illustratif).
- **$H_{B4}$** : les filtres amont rejettent préférentiellement les idées rares valides (taux de faux négatifs sur la queue $> 25\,\%$, illustratif) ou le bandit sur-exploite des bras épuisés, donnant un $D_{\text{rare}} \le$ ligne de base uniforme (ou violant le FDR).
- **Métrique & seuil** : $D_{\text{rare}}$ sur $\Phi_{\text{audit}}$, taux de faux négatifs sur un jeu étalonné d'idées rares valides, $\text{FDR}_{\text{audit}}$ (seuils illustratifs).
- **Contrôle négatif** : filtres amont remplacés par un sous-échantillonnage aléatoire au même taux de passage, et bandit remplacé par une allocation uniforme.
- **Falsification & critère d'abandon de I4** : **abandonner I4** si $H_{B4}$ se réalise ou si I4 ne bat pas le contrôle à passage aléatoire (falsifiant $H_{A4}$). Le dépassement du seuil $+25\,\%$ avec faux négatifs $\le 10\,\%$ et $\text{FDR} \le 0{,}05$ falsifie $H_{B4}$.

---

## 5. Limites de principe — Q4

Six bornes fondamentales limitent ce qu'on peut espérer, indépendamment de l'ingénierie des prompts :

1. **Paradoxe du taux de base et mur des fausses découvertes** (`RAPPORTÉ` : Ioannidis, J. P. A., 2005, *Why Most Published Research Findings Are False*, PLoS Medicine ; Benjamini & Hochberg, 1995) : si la proportion d'idées réellement valides parmi les propositions rares générées est $\pi \ll 1$, pour une sensibilité $1-\beta$ et un taux de faux positifs $\varepsilon_{\text{FP}}$ du contrôleur, la probabilité qu'une idée rare confirmée soit fausse vaut par théorème de Bayes :
   $$\text{FDP} = \frac{(1-\pi)\,\varepsilon_{\text{FP}}}{\pi(1-\beta) + (1-\pi)\,\varepsilon_{\text{FP}}}$$
   Dès que $\pi \ll \varepsilon_{\text{FP}}$, la majorité des découvertes rares « confirmées » sont fausses. Réduire la rareté visée $\pi$ impose de réduire $\varepsilon_{\text{FP}}$ au moins au même ordre, ce qui augmente généralement le coût de vérification.
2. **Borne d'échantillonnage et support nul** (`RAPPORTÉ` : Good, 1953) : sans signal de guidage, observer une classe de masse $p$ demande $\Theta(1/p)$ tirages en espérance ; si $p \ll 1/N$ ou si l'idée exige des primitives absentes du support des modèles, aucune réallocation d'inférence à budget fini ne l'atteindra.
3. **Indécidabilité de l'équivalence fonctionnelle** (`RAPPORTÉ` : Rice, H. G., 1953, *Classes of Recursively Enumerable Sets and Their Decision Problems*, Transactions of the American Mathematical Society) : dans tout formalisme Turing-complet, décider si deux propositions sont fonctionnellement équivalentes est indécidable en général. Toute canonisation mécanique réalisable comporte donc une erreur résiduelle de regroupement/séparation.
4. **Absence de gain sans structure de voisinage (*No Free Lunch*)** (`RAPPORTÉ` : Wolpert & Macready, 1997) : si le contrôleur ne renvoie qu'un bit succès/échec sur un paysage « balle de golf » sans tremplins, aucune recherche adaptative ne peut battre en moyenne la recherche aveugle. Le gain de I2–I4 est borné par l'information mutuelle entre les retours de $\Phi_{\text{dev}}$ et la localisation des puits étroits.
5. **Capacité finie d'un banc de validation sous requêtes adaptatives** (`RAPPORTÉ` : Dwork et al., 2015 ; Skalse et al., 2022) : interroger adaptativement un banc fini de $m$ cas d'essai épuise sa validité statistique (erreur pouvant croître en $O(\sqrt{k/m})$ au lieu de $O(\sqrt{\log k / m})$ après $k$ requêtes adaptatives). Sans renouvellement du banc d'audit ou mécanisme de protection, toute boucle finit par sur-exploiter le vérificateur.
6. **Plafond de corrélation inter-modèles** (`HYPOTHÈSE` appuyée sur Shumailov et al., 2024 et Dietterich, 2000) : multiplier les modèles sature vite si leurs distributions de pré-entraînement et d'alignement partagent les mêmes modes ; le nombre effectif de modèles indépendants reste borné bien en deçà du nombre nominal.

---

## 6. Mesure minimale de fonctionnement de chaque instrument — Livrable (c)

Tous les seuils chiffrés ci-dessous sont marqués **« illustratif »** (`HYPOTHÈSE` de métrologie).

| Instrument nommé dans la question | Taux de détection (TPR) & fausses alertes (FPR/FDR) | Cas honnêtes appariés | Vérifications mécaniques à battre |
| :--- | :--- | :--- | :--- |
| **1. Contrôleur indépendant** (« fiable sur des cas d'essai ») | TPR $\ge 0{,}85$ sur vraies idées rares OOD ; FPR $\le 10^{-3}$ sur leurres rares (illustratif, et $\text{FPR} \ll \pi$). | Paires indépendantes des modèles, appariées en taille/style : solutions valides rares (issues d'isomorphismes neufs) vs pseudo-solutions à défaut subtil (cas limite, sur-ajustement exact à $\mathcal{T}_{\text{dev}}$). | Tests unitaires statiques sur les seuls cas d'essai connus $\mathcal{T}_{\text{dev}}$ + vérificateur syntaxique/dimensionnel seul. |
| **2. Mesure de rareté sans modèle** (canonisation $\sim$ + Good-Turing/Clopper-Pearson) | TPR $\ge 0{,}90$ de regroupement de vrais équivalents ; FPR $\le 0{,}02$ de fausses fusions entre mécanismes distincts (illustratif). | Paires fonctionnellement identiques mais paraphrasées/refactorées vs paires à distance d'édition minimale (1 signe/borne changé) mais comportementalement distinctes. | Correspondance exacte de chaîne (*exact match*), distance de Levenshtein / Jaccard sur n-grammes, compression brute (NCD) sans sondes fonctionnelles. |
| **3. Mesure de valeur sans modèle** (score $\Phi_{\text{audit}}$ + MDL/Pareto + gain de portefeuille) | TPR $\ge 0{,}85$ sur idées apportant un vrai gain OOD ; FPR $\le 0{,}05$ sur variantes rares sans valeur marginale (illustratif). | Idées rares compactes résolvant des cas échoués par la référence vs variantes rares « gonflées » (code mort, branchements mémorisant $\mathcal{T}_{\text{dev}}$) de même score sur $\mathcal{T}_{\text{dev}}$. | Score moyen brut sur $\mathcal{T}_{\text{dev}}$ sans pénalité de complexité (MDL) ni évaluation sur banc caché et cas résiduels. |
| **4. Système multi-modèles + interventions (I1–I4) et verrou FDR** | TPR : fraction des puits étroits synthétiques retrouvés à budget $B$ (cible $\ge +25\,\%$ sur la base, illustratif) ; FDR $\le 0{,}05$ sur $\Phi_{\text{audit}}$ (illustratif). | Domaines synthétiques à vérité construite contenant des solutions rares inédites (absentes du pré-entraînement) appariés à des instances **nulles** (aucune solution rare valide) mesurant les fausses découvertes pures. | (1) Recherche symbolique pure sans LLM (programmation génétique / énumération bornée / solveur SMT) au même budget $B$ ; (2) mono-modèle i.i.d. avec déduplication au même budget $B$. |

---

## 7. Ancrage matériel — Livrable (d)

Toutes les quantités de calcul et de coût ci-dessous ne proviennent pas des faits et sont marquées **« illustratif »**.

- **Banc expérimental ouvert et vérifiable** : 3 domaines canonisables exécutables sur CPU en bac à sable — (1) synthèse d'heuristiques/programmes courts en Python sur graphes aléatoires frais, (2) découverte symbolique d'équations sur données simulées à lois rares, (3) synthèse de règles/circuits booléens ou arithmétiques sous contraintes de profondeur — avec génération fraîche de $\mathcal{T}_{\text{audit}}$ par graine après sélection des modèles.
- **Modèles à poids ouverts (familles distinctes pour I1)** : exécution locale via vLLM/SGLang avec décodage contraint par grammaire :
  - Famille A : `Qwen2.5-7B` (base) et `Qwen2.5-7B-Instruct` ;
  - Famille B : `Llama-3.1-8B` (base) et `Llama-3.1-8B-Instruct` ;
  - Famille C : `Mistral-7B-v0.3` et `Mistral-7B-Instruct-v0.3` (ou `Gemma-2-9B` / `Gemma-2-9B-it`) ;
  - Famille D (architecture MoE) : `DeepSeek-Coder-V2-Lite-Base` et `Instruct`.
  - Réplication optionnelle à plus grande échelle : variantes ouvertes 32B–70B pour tester la sensibilité à la taille.
- **Calcul nécessaire (illustratif)** :
  - Pilote E0 : $10\,000$ appels par domaine ($3 \times 10^4$ appels) à $\sim 500$ jetons générés en moyenne, soit $\sim 1{,}5 \times 10^7$ jetons (illustratif).
  - Campagne E1–E4 (~18 conditions/contrôles × 3 domaines × $25\,000$ propositions à $\sim 500$ jetons, illustratif) : $\sim 7 \times 10^8$ à $1{,}2 \times 10^9$ jetons générés au total (illustratif).
  - Temps GPU (1× H100 80 Go en BF16 avec batching continu à $\sim 3\,000$–$4\,500$ jetons/s agrégés sur modèles 7–9B, illustratif) : $\sim 60$ à $120$ heures-GPU (illustratif).
  - Vérification CPU (canonisation, sondes comportementales, tests de propriétés, audit $\Phi_{\text{audit}}$, et lignes de base symboliques pures) : $\sim 300$ à $800$ heures-vCPU (illustratif), étendues à $\sim 1\,500$ heures-vCPU pour le régime lourd de E4 (illustratif).
- **Coût estimé (illustratif)** :
  - Inférence GPU cloud (H100 à $\sim 2{,}5$–$3{,}5\,\$/\text{h}$, illustratif) : $\sim 150$ à $420\,\$$ (illustratif).
  - Vérification CPU + stockage des traces complètes et graines : $\sim 60$ à $250\,\$$ (illustratif).
  - **Total campagne E0–E4 (échelle 7–9B)** : **$\sim 210$ à $670\,\$$ (illustratif)** ; réplication partielle à l'échelle 32B–70B : **$\sim 1\,000$ à $3\,000\,\$$ (illustratif)**.
- **Comptabilité stricte du coût total égal $B$** : chaque duel mesure le budget en unité physique unique (coût normalisé GPU+CPU sur grille tarifaire figée, ou secondes-équivalent-H100) sommant préfill, décodage, canonisation, filtres amont et vérifications, afin qu'aucune intervention ne masque son surcoût de vérification ou d'orchestration.

FIN-DE-CELLULE