Les quatre pièces sont lisibles jusqu’à leur marqueur de fin. Je ne requalifie aucun fait ; les seuils chiffrés discutés sont ceux des conceptions et restent **illustratifs**.

**Notation commune.** \(Y\) est l’acte attesté indépendamment, \(O\) l’étiquette d’oracle, \(D\) le dommage, \(Z\) la tâche/monde/longueur, \(G\) l’organisme et sa dose, \(T\) le texte accessible, \(H\) les activations, \(E/I\) les alertes externe/interne. Deux limites s’appliquent partout : si \(n_0\tau=O(1)\), les quantiles et taux de fausses alertes sont trop mal estimés pour trancher ; si \(P(Y=1,E^-=1)\) est nulle ou le nombre de manqués externes trop faible, la capture résiduelle est indéfinie ou non jugeable. Le bootstrap ne répare ni ce défaut de positivité, ni des supports disjoints, ni une fuite entre plis.

## Sur la proposition A

### (a) Défauts de méthode

- **E0** mesure des *alertes* du moniteur selon les erreurs de l’oracle, non l’indépendance des erreurs des deux instruments. Son duel sur \(R\) laisse en outre \(R<0{,}5\) sans issue. Le rappel par dose \(\alpha\) ne remplace pas une stratification par difficulté réelle du sabotage.
- **E1** : prise isolément, la case « consigne d’attaque, exécution honnête » ne contient aucun positif \(Y=1\) : une AUC conditionnelle n’y est pas définie. La réunir à d’autres cases change la population et réintroduit un confondant de mélange. Par ailleurs, \(\Delta\mathrm{AUC}\) ne teste pas l’utilité à faible taux de fausses alertes. Enfin, la sonde β n’est pas une borne de toute l’information textuelle : elle mesure ce qu’un extracteur particulier sait utiliser.
- **E2** : les régions \(\leq0{,}60\) et \(\geq0{,}75\) laissent une zone non classée et ne constituent pas un test d’équivalence. Projeter hors du sous-espace des adaptateurs vus peut supprimer le signal recherché *par construction* ; cela ne localise pas une trace propre à un mode non vu.
- **E3** : la corrélation dose–score–dommage reste confondue par \(\alpha\). Une ablation sans effet peut aussi refléter une redondance causale, et non une trace épiphénoménale ; une réduction du dommage peut provenir d’une incapacitation générale.
- **E4–E5** : \(C=P(I^+\mid E^-,Y=1)\) teste une association conditionnelle, pas l’effet d’une pression d’évasion. Ainsi, réfuter \(H_A\) sur \(C\) ne réfute pas l’étau, et observer \(C>\mathrm{TPR}_{int}\) ne réfute pas E7. La diagonale de la matrice de transfert est proche de zéro par sélection si le bras rouge ne soumet que des cas ayant déjà trompé la sonde source. Enfin, les trois bras « secret/aléa » font varier conjointement composition du panel, information et objectif d’optimisation.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **E0** : lorsque \(P(O\text{ se trompe}\mid Y,Z)\) est proche de zéro, les dénominateurs du rapport \(R\) deviennent vides ou instables. Même bien estimé, \(R\in[0{,}5;2]\) n’implique pas \(O\perp I\mid Y,Z\). Un rappel global dépend aussi de la loi des magnitudes de dommage dans le jeu connu.
- **E1** : si \(P(Y\mid H,T,Z,G)=P(Y\mid T,Z,G)\), il n’existe aucun gain conditionnel à trouver. À l’inverse, deux lois peuvent avoir des AUC différentes tout en ayant le même rappel au quantile honnête \(1-\tau\), si leurs queues supérieures se croisent. Si les plis changent \(P(Z,G\mid Y)\), le \(\Delta\mathrm{AUC}\) mesure aussi ce changement de mélange.
- **E2** : si les lois de \(\|\Delta\|\) chez les épisodes sabotés et dormants ne se recouvrent pas, la comparaison « à norme égale » est non identifiable. Si le même organisme ou la même graine d’adaptateur apparaît dans apprentissage et test, l’estimation conserve la fuite d’identité.
- **E3** : si \(\operatorname{Var}(s\mid\alpha)\approx0\), aucune pente intra-dose ne sépare score et dose. Pour E4, une variation de \(C\) peut résulter uniquement d’un mélange de familles : \(P(I,E\mid Y)\) marginal ne représente alors aucune famille constituante.
- **E5** : la valeur de Nash calculée sur les lignes d’attaques optimisées contre des sondes pures ne renseigne sur un mélange \(p\) que si la meilleure réponse à \(p\) appartient à la bibliothèque mesurée. Sinon, sa loi \(Q_p\) est hors support. De même, le maximum de dommage trouvé en un budget fini est seulement une borne inférieure dépendant de l’optimiseur : un plateau ne distingue pas convergence et échec de recherche.

### (c) Contrôles négatifs dont l’absence serait fatale

Le placebo à objectif caché inoffensif doit entrer dans **E0, E1 et toutes les calibrations**, pas seulement apparaître en E2. Il faut des seuils rapportés séparément sur jumeaux, échecs honnêtes, dormants et placebo, sans les réunir. E5 exige une génération d’attaque sous **pression placebo à budget égal** et un panel de sondes dupliquées. Pour E3, il manque un témoin d’intervention apparié en norme *et covariance*, ainsi qu’un témoin qui supprime génériquement l’action tout en préservant la qualité moyenne.

## Sur la proposition B

### (a) Défauts de méthode

- **X0** définit la strate « diffuse » par une magnitude de baisse de couverture. Cela ne reproduit pas nécessairement la dose fixée sur la boîte noire et favorise mécaniquement un oracle dont la variable est précisément la couverture. L’accord \(\kappa\) entre lecteurs mesure leur concordance, non leur validité.
- **X1** : « la base qui relit » est un comparateur utile, mais pas une borne de capacité textuelle. De plus, une validation par famille ne suffit pas si tâches, mondes ou graines d’organismes traversent les plis. Un gain avant l’action peut prédire une intention ou exploiter \(P(Y\mid Z,C)\), sans identifier l’acte futur.
- **X2** soustrait deux AUC dont les contrastes ne sont pas symétriques : sabotage contre dormant chez le saboteur, mais épisodes pseudo-appariés chez le placebo. Leur différence n’a pas un estimand commun sans définition explicite des opportunités placebo. Le placebo n’est pas spécifié comme porteur d’un objectif caché inoffensif.
- **X3** conserve les deux ambiguïtés de causalité : redondance après ablation et effet hors distribution de la substitution. **X4** assimile trop vite le signe d’une corrélation à un mécanisme : une corrélation de Spearman nulle n’implique pas l’indépendance conditionnelle requise par le produit des rapports de vraisemblance, et calibrer \(\lambda\) sur les seuls jumeaux ne valide que sa classe négative.
- **X6** ne met pas le dommage dans chaque cellule de \(T[j,k]\) : une attaque devenue inoffensive peut donc compter comme une évasion réussie. La différence entre réserve et mélange reste confondue par la composition et la nouveauté des détecteurs.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **X0b** : si une strate contient zéro manqué de l’oracle ou du moniteur, le rapport de cotes n’est pas estimable ; une marge d’équivalence n’y certifie rien. Croiser les familles de modèles ne modifie pas cette condition de positivité.
- **X1–X2** : si \(P(Z,G\mid Y,\text{pli})\) change entre plis, le gain peut provenir de l’extrapolation différente des deux sondes. Le \(\delta\) en différence de différences devient non interprétable si les lois de tâche, d’opportunité ou de \(\alpha\) ne se recoupent pas entre saboteur et placebo.
- **X3–X5** : une pente du dommage sur la projection à \(\alpha\) fixé exige une variation résiduelle de cette projection. Pour X5, si les distributions de dommage ou de baisse du rappel externe sont disjointes entre pression externe et pression placebo, \(\beta_{\text{externe}}-\beta_{\text{placebo}}\) n’est pas identifiable sans extrapolation.
- **X4** hérite du dénominateur résiduel commun. **X6** hérite de la limite hors équilibre : ses lignes sont générées sous des lois d’attaque \(Q_j\) différentes ; la valeur minimax empirique ne vaut donc pas automatiquement valeur contre une meilleure réponse au mélange. La stabilité du triangle inférieur n’exclut pas non plus une nouvelle attaque hors support.

### (c) Contrôles négatifs dont l’absence serait fatale

Il faut des positifs connus dont la vérité ne dépend ni de la couverture ni des lecteurs, notamment des omissions sans dommage immédiatement visible. Le placebo doit avoir un **objectif caché inoffensif**, et les plis doivent séparer organismes/graines, tâches et mondes. X6 exige des attaques placebo sans perte de dommage, un panel dupliqué et une comparaison à composition identique entre panel révélé et panel caché. Pour X3, une direction témoin de même norme mais de covariance différente ne suffit pas.

## Sur la proposition C

### (a) Défauts de méthode

- Plusieurs relevés sont marqués **VÉRIFIÉ** alors que les faits ne certifient pas leur contenu sous ce statut ; les empreintes vérifiées ne requalifient pas les mesures citées. Cette inflation de statut doit être retirée.
- **E0** : des sabotages « injectés » peuvent appartenir à une autre loi que les sabotages diffus des adaptateurs ; leur rappel ne se transporte pas sans hypothèse de représentativité. Des estimations ponctuelles et un test de non-signification ne suffisent pas à établir l’indépendance.
- **E1** : le modèle texte+sonde reçoit davantage de paramètres que le modèle texte seul ; le gain peut être un gain de capacité. La sélection couche×position n’est corrigée ni par le bootstrap ni par deux plis de famille si elle utilise les mêmes données que le test. La prétendue AUC dans la case entièrement honnête est également problématique.
- **E2** assimile explicitement T100 au placebo. Or le témoin contrôle la chaîne de modification, pas la présence d’un objectif caché quelconque. L’AUC contre l’union dormants∪placebo peut être élevée en séparant surtout un seul type de négatif.
- **E4** : ses deux hypothèses peuvent être vraies simultanément — le secret peut aider *et* l’aléa public peut conserver un gain — ou fausses simultanément. Le duel viole donc l’exigence d’exclusivité. **E5** ne comporte aucune pression assignée : sa capture résiduelle ne teste pas l’étau, et L2 peut coexister avec une capture interne positive.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **E0** : avec des cellules d’erreur nulles, \(|\log OR|\) est indéfini ; avec peu d’erreurs, son estimateur a une variance trop grande pour la marge proposée. Le test ne porte en outre que sur le prédicteur texte, pas sur les autres moniteurs.
- **E1–E2** : si le texte et les activations ont des scores discrets ou des atomes au seuil, le même FPR nominal ne garantit pas le même FPR réalisé. L’AUC groupée peut rester au-dessus du seuil alors que \(P(\text{alerte}\mid\text{placebo})\) est proche de un ; calibrer sur la base \(\alpha=0\) ne contrôle pas cette probabilité chez les organismes adaptés honnêtes.
- **E3** : si \(\mathrm{Dommage}_{S100}-\mathrm{Dommage}_{S0}\approx0\), \(\rho_{\text{causal}}\) diverge ou change arbitrairement de signe. Si les activations du donneur honnête sont hors du support des activations du saboteur aux positions choisies, l’effet de substitution est indissociable d’un choc hors distribution.
- **E4** : la matrice ne permet pas d’estimer la meilleure réponse aux mélanges non échantillonnés ; le test de Friedman ne crée pas d’indépendance entre générations imbriquées. **E5** : conditionner sur \(E^-\) à chaque intensité d’évasion change la population retenue ; la pente de \(C_{\text{rés}}\) peut donc être entièrement due à cette sélection. Avec les 50 traces proposées pour calibrer un FPR de 1 %, \(n_0\tau=0{,}5\) dans ce dimensionnement illustratif : la queue est non jugeable.

### (c) Contrôles négatifs dont l’absence serait fatale

Il faut remplacer T100, pour ce rôle, par un adaptateur à objectif caché inoffensif, et publier séparément chaque classe de négatif. E1 requiert une sonde sur activations de la base relisant les mêmes jetons et un comparateur texte de capacité appariée. E3 exige des interventions témoins appariées en covariance et une mesure de suppression générique de l’action. E5 ne devient un test d’étau qu’avec pression externe assignée **et pression placebo de même budget**, en publiant tous les épisodes avant sélection sur les manqués externes.

## Sur la proposition E

### (a) Défauts de méthode

- **O** : le lot connu peut souffrir du même biais de spectre si ses positifs sont définis par des événements particulièrement visibles dans la couverture. La statistique \(d\) n’est pas une mesure générale d’indépendance : sans discrétisation préenregistrée de \(z\), son maximum est inestimable ; avec des erreurs rares, les conditionnements sont vides.
- **T** : le comparateur « texte public seul » ne borne pas, pour la famille (i), l’information de l’entrée complète incluant la consigne privée. Le contrat ne prévoit pas explicitement une sonde sur la base relisant les mêmes sorties ; le gain peut donc être une meilleure extraction du texte ou une lecture de consigne.
- **C** reconnaît la dégradation générale, mais une perte de qualité moyenne faible ne suffit pas : réduire la longueur, les tentatives ou une capacité rare peut réduire le dommage sans passer le seuil global \(L_Q\). L’absence d’effet peut encore provenir d’une redondance.
- **R** doit distinguer réutilisation d’une bibliothèque figée et nouvelle optimisation dans chaque régime. Sans cela, le plan factoriel mélange transfert et effet causal du régime. **P** : si « à dommage maintenu » est obtenu en filtrant sur \(D\), variable post-traitement, la comparaison devient une sélection sur un résultat de la pression.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **O** : \(d\) exige \(0<P(E_O=1\mid z)<1\) dans chaque strate utilisée. Une rareté des erreurs rend les deux probabilités conditionnelles instables ; une borne large doit rester indécise, comme la pièce le prévoit.
- **T–L** : si \(P_0(Z,\text{longueur},\text{domaine})\) change entre calibration et test, le FPR du détecteur de nouveauté change sans aucune trace nouvelle. Sous dépendance sérielle non modélisée, le SPRT et le maximum par épisode ne conservent pas leur niveau nominal. Si les lois d’activation n’ont pas de support commun entre familles, \(\Delta_T\) mélange information et extrapolation.
- **C** : près du plancher \(D\approx0\), aucune réduction n’est mesurable ; avec des donneurs hors support, l’effet spécifique n’est pas séparable de l’effet de perturbation.
- **R–P** : les effets marginaux du secret et du tirage ne sont identifiés que si les lois d’attaque sont régénérées sous chaque régime à budgets comparables, ou si la bibliothèque est maintenue figée. Pour l’étau, des supports de dommage disjoints entre régimes rendent la comparaison « à dommage maintenu » impossible sans extrapolation. Le dénominateur résiduel de \(R=P(I^+\mid Y^+,E^-)\) conserve la limite commune.

### (c) Contrôles négatifs dont l’absence serait fatale

Le placebo, jusqu’ici non défini, doit être un adaptateur à **objectif caché inoffensif**, avec placebo–base et dormant–base comme comparateurs. T et L ont besoin du contrôle « base relisant les mêmes jetons » pour soutenir « au-delà du texte ». C requiert une perturbation témoin appariée en covariance et un témoin de suppression générique de l’action. Enfin, dans R et P, les « interventions fictives » doivent explicitement inclure une **optimisation placebo contre une propriété sans rapport**, à budget et dérive de génération égaux ; une simple transformation fictive des traces ne sépare pas pression externe et simple réentraînement.

FIN-DE-CELLULE