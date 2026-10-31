# Proposition A — Tour III.2 : critique croisée de méthode

**Statuts.** Les pièces B, C, D et les pièces conv-audit sont des affirmations RAPPORTÉES ; aucune donnée, aucun journal de course, aucune sortie de modèle n'est audité. Ce que j'avance sur les théorèmes est SUPPOSÉ (de mémoire, non relu sur PDF). Tout chiffre que je calcule est illustratif et sert seulement à montrer un ordre de grandeur.

**Notation commune** (pour la partie (b) de chaque section) : observables $X$, latentes $Z\in\mathbb{R}^k$, dose $D$, issue $Y\in\{0,1\}$ (fertilité jugée), auxiliaire ou environnement $U$ à $m$ valeurs, confondeur $S$, mélange $X=f_U(Z)+\varepsilon$, loi a priori $p(Z\mid U)$ de famille exponentielle à paramètre naturel $\lambda(U)$. $n$ est le nombre d'unités par bras ou par environnement.

**Trois défauts transversaux**, que je cite une fois et rappelle ensuite par leur numéro :

- **T1 — fuite par l'issue dans les entrées.** B et C construisent les latentes sur le graphe de citations ou sur des plongements qui en dérivent (B : « SPECTER ou similaire » ; SPECTER est, SUPPOSÉ : Cohan, Feldman, Beltagy, Downey et Weld 2020, « SPECTER: Document-level Representation Learning using Citation-informed Transformers », entraîné avec un signal de citation). L'issue « reprise » est elle-même un fait de citation. Toute latente qui prédit la reprise peut alors la prédire parce qu'elle l'encode déjà. Seule parade : entraîner l'encodeur sur une coupure temporelle antérieure à la fenêtre de mesure de $Y$, et le prouver par un contrôle (ci-dessous).
- **T2 — « ∅ » et « instable » sont équivoques.** Un ensemble vide en prédiction invariante, une absence de latente stable, un MCC bas : chacun a deux causes incompatibles (hypothèse du théorème violée par les données, ou données trop pauvres pour que le test ait de la puissance). Aucune des trois propositions ne sépare ces deux cas par une statistique dédiée ; leurs critères de mort tuent donc une hypothèse sans dire laquelle.
- **T3 — le générateur de mondes inventés est aussi le banc de réglage.** B (20 configurations), C (50), D (200) tirent apprentissage et évaluation du même générateur, écrit par l'équipe qui règle les méthodes. Il faut une famille de générateurs scellée avant réglage, ou au minimum des paramètres de monde tirés après le gel des hyperparamètres.

---

## Sur la proposition B

### (a) Défauts de méthode

1. **Expérience 1 : le contrôle négatif est un faux positif par construction.** B demande que l'iVAE retrouve les causes (MCC ≥ 0,7) et *ne retrouve pas* l'accompagnateur (MCC ≤ 0,3). Or, SUPPOSÉ, le théorème de Khemakhem et al. 2020 (RAPPORTÉ dans les pièces) identifie *toutes* les sources latentes satisfaisant $p(Z\mid U)=\prod_i p(Z_i\mid U)$, causales ou non : un accompagnateur planté comme source est recouvré *s'il est bien recouvré*. Un MCC élevé sur l'accompagnateur est un succès de démêlage, pas un échec. B confond deux identifications (statistique des latentes, causale vers $Y$) — confusion qu'elle reproche pourtant à conv-audit-6 dans sa synthèse (point 4). Tel quel, H_A de l'expérience 1 est morte avant la première graine.
2. **Expérience 1 : le monde planté sort du domaine du théorème.** Si l'accompagnateur est « corrélé par un confondeur commun (prestige) », les latentes ne sont pas conditionnellement indépendantes sachant $U$ ; l'échec de l'iVAE ne dit rien sur la méthode dans son domaine, il dit que le monde viole l'hypothèse. Il manque le monde jumeau conforme (D le prévoit).
3. **MCC : erreur de définition.** B écrit « coefficient de corrélation de Matthews ». SUPPOSÉ : dans la littérature d'ACI non linéaire, MCC désigne la corrélation moyenne entre sources vraies et recouvrées après appariement hongrois ; le coefficient de Matthews est une mesure de classification binaire. La métrique préenregistrée doit être nommée sans ambiguïté, sinon le seuil 0,7 est non jugeable.
4. **Expérience 2 : le critère de ratio NRMSE est mal orienté.** La prédiction causale invariante ne promet pas de mieux prédire hors environnement qu'un modèle libre ; elle promet un ensemble de parents dont le mécanisme est invariant. Un ensemble invariant prédit souvent *moins* bien en distribution. De plus, B traite $S^*=\varnothing$ comme mort de H_A ; or $\varnothing$ est la sortie *correcte* quand $Y$ est intervenue entre environnements (T2). Enfin NRMSE pour une issue binaire est inadapté (log-vraisemblance ou score de Brier).
5. **Expérience 2 : le contrôle « découpage alphabétique » est trivialement vide.** SUPPOSÉ : l'estimateur de Peters et al. est $\hat S=\bigcap\{S : H_{0,S}\text{ non rejetée}\}$. Avec des environnements échangeables, toutes les $H_{0,S}$ sont acceptées (sauf au niveau $\alpha$) et l'intersection est $\varnothing$. Le contrôle renverra donc ∅ presque toujours ; « $S^*$ identique aux vrais environnements » ne peut se produire que si les vrais environnements donnent déjà ∅. Le contrôle ne contrôle rien.
6. **Expérience 3 : ce n'est pas « à lui seul ».** La dose est observée et randomisée par la course ; la prédiction de son effet s'appuie sur cette randomisation. B le reconnaît en remarque, mais garde l'expérience comme test de l'identification non supervisée. Fuite supplémentaire : si l'iVAE est entraîné sur les courses passées *avec leurs verdicts*, les latentes encodent $Y$ (T1 version interne).
7. **Expérience 3 : le contrôle « titres de la même niche » n'est pas un zéro.** Donner plus de texte à un agent peut changer sa production indépendamment de tout croisement ; un effet non nul y est plausible et ne prouve aucune hallucination. Le zéro propre est l'intervention fantôme : dose affectée et journalisée, non délivrée (D le propose).
8. **Expérience 4 : stabilité ≠ identification.** Une ACP est stable et n'identifie rien ; un VAE très régularisé est stable par capacité réduite. B l'admet à moitié (« diagnostic ») mais fait de la stabilité une condition de mort de H_B.
9. **Expérience 5 : un seul signe sur une seule expérience naturelle.** Sous l'hypothèse nulle, la concordance d'un signe vaut 1/2. Et « IC couvrant zéro » tue H_A : absence de preuve prise pour preuve d'absence ; il faut un test d'équivalence avec borne préenregistrée.
10. **Plongements précalculés** : T1 et fuite temporelle (modèle pré-entraîné après la coupure).

### (b) Conditions de perte de puissance ou de non-jugeabilité

- *Expérience 1.* Soit $\Lambda$ la matrice des différences $\lambda(u)-\lambda(u_0)$ ; SUPPOSÉ, l'identification exige $\operatorname{rang}(\Lambda)=2k$ (il faut $m\ge 2k+1$ valeurs de $U$). Si $\operatorname{rang}(\hat\Lambda)<2k$, les latentes ne sont identifiées que dans un sous-espace : le MCC composante par composante est non jugeable. Par ailleurs la loi nulle du MCC apparié n'est pas centrée en zéro : avec $k$ latentes et $n$ points, l'appariement hongrois de vecteurs indépendants donne un MCC de chance croissant en $k$ et décroissant en $n$ ; si ce quantile à 95 % dépasse 0,3, le seuil « accompagnateur ≤ 0,3 » est inopérant.
- *Expérience 2.* Pour un ensemble non causal $S$, le test rejette si $E[Y\mid X_S,U=u]$ varie avec $u$ d'une quantité $\delta_S$ telle que $\delta_S\sqrt{n}$ dépasse le seuil du test. Si $\delta_S\approx 0$ pour tous les $S$ non causaux (mécanisme du confondeur identique entre environnements), rien n'est rejeté et $\hat S=\varnothing$ ; si l'issue est intervenue ($E[Y\mid \mathrm{Pa}(Y),U]$ dépend de $u$), tout est rejeté et $\hat S=\varnothing$ aussi. Les deux extrêmes donnent la même sortie (T2) : il faut publier le *nombre d'ensembles acceptés*, pas seulement $\hat S$. Le ratio NRMSE perd toute puissance quand le décalage entre environnements est un pur décalage de covariables (la loi $P(Y\mid X)$ complète reste stable) : le modèle libre fait aussi bien hors environnement.
- *Expérience 3.* Variance de $\hat\tau(d)$ bornée par $2p(1-p)/n$ ; à $p\approx0{,}5$, un écart-type de 7 points pour $n=100$ par bras (illustratif). L'interpolation à $d=7$ entre 5 et 10 ne discrimine un modèle causal d'un régresseur lisse que si la courbe dose-réponse a une courbure entre ces doses supérieure au bruit ; sinon le gain ε = 10 % est non jugeable.
- *Expérience 4.* Si les valeurs propres de $\operatorname{Cov}(Z)$ ont des écarts inférieurs à $O(1/\sqrt n)$, la rotation du sous-espace est indéterminée : l'instabilité est une propriété des données, pas de la méthode ; le seuil Spearman 0,8 est alors non jugeable.
- *Expérience 5.* Effets d'expériences naturelles de l'ordre de 5–10 % sur des milliers d'unités (RL5-16, SUPPOSÉ) ; avec $K$ chocs indépendants, la concordance de signe suit une binomiale $(K,1/2)$ sous H_0 ; il faut $K\ge5$ pour qu'une concordance totale ait $p<0{,}05$ (illustratif).

### (c) Contrôles négatifs dont l'absence est fatale

- **Loi nulle du MCC par permutation** des latentes vraies (fatale pour Exp. 1 : sans elle 0,3 n'a pas de sens).
- **Intervention fantôme** (dose journalisée, non délivrée) à la place de « titres de la même niche ».
- **Permutation des étiquettes d'environnement avec décompte des ensembles acceptés**, pas seulement $\hat S$.
- **Encodeur entraîné avant coupure + sonde linéaire $\hat z\to Y_{\text{futur}}$ sur des paires sans contact** : si la sonde prédit la reprise à partir de latentes antérieures au contact mieux qu'une base taille-âge, l'issue a fui (T1).
- **Audit de randomisation** : équilibre des covariables pré-traitement entre bras (test de permutation) — B prend la randomisation pour acquise alors que D la marque « RAPPORTÉ, non audité ».
- **Ligne de base à mêmes entrées** : XGBoost doit recevoir exactement les entrées de l'iVAE, sinon la comparaison ε mesure une différence de données, pas de structure.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Expérience 1 : H_B est vraie par construction.** C plante une dérive de $f_u$ de 15 % par environnement et une variance des confondeurs dix fois supérieure. L'iVAE échouera parce que son hypothèse centrale (mélange invariant en $U$) est violée *par le générateur*. Le résultat ne dit rien sur la question posée — les données scientométriques violent-elles cette hypothèse ? — que C affirme (« très probablement fausse ») sans proposer une seule mesure sur OpenAlex. Il faut deux bras de mondes (conforme / violé) et un estimateur de la dérive réelle (voir (b)).
2. **« FDR_causal » kille un objet non défini.** L'iVAE ne sort pas d'arête vers $Y$ ; la « tête causale » qui orienterait les latentes vers la fertilité n'est pas spécifiée. Un critère de mort sur un composite non décrit n'est pas préenregistrable.
3. **Expérience 2 : la « voie observationnelle » n'existe pas dans les courses.** L'historique des courses est randomisé par conception ; un modèle entraîné dessus « sans utiliser la randomisation » l'utilise quand même (la loi de $D$ y est indépendante des attributs de paire). Pour tester l'identification « à lui seul », il faudrait un lot de courses à affectation *non* aléatoire, journalisée, que C ne prévoit pas.
4. **Expérience 2 : seuils sous le bruit de mesure.** $N=200$ réparties sur deux doses, issue binaire : écart-type de $\widehat{\mathrm{ATE}}$ d'environ 7 points (illustratif, voir (b)). Un intervalle de prédiction à 90 % honnête doit donc dépasser ±12 points ; et « $|\Delta_{\text{erreur}}|<2$ points » compare deux erreurs dont chacune fluctue de 7 points. Les trois critères de mort sont non jugeables à cet effectif.
5. **Placebo cosmétique.** Permuter l'ordre de titres fournis à un agent de langage peut changer sa sortie (sensibilité à la position) ; un effet non nul est possible sans aucune hallucination du modèle d'estimation. Ce placebo peut tuer H_A pour une mauvaise raison. Le zéro propre est l'intervention fantôme.
6. **Expérience 3 : fuite massive.** $\hat\tau_{\text{obs}}$ est appris « sur l'ensemble du graphe OpenAlex », qui contient les cohortes de choc et leurs périodes post-choc : la voie observationnelle a vu les issues qu'elle est censée prédire à l'aveugle. Il faut retirer cohortes et périodes avant apprentissage, et le prouver par empreinte du jeu d'entraînement.
7. **Expérience 3 : $\hat\tau_{\text{QE}}$ promu « vérité » sur un test de pré-tendance faible.** Un test de pré-tendance à $p>0{,}20$ sur peu de périodes a peu de puissance ; l'accepter ne valide pas les tendances parallèles et conditionner l'analyse sur ce test biaise les estimations (SUPPOSÉ : Roth 2022, « Pretest with Caution », référence à vérifier). Et la corrélation de rang par déciles entre deux estimateurs bruités est plafonnée par leur fiabilité (voir (b)).
8. **Table d'étalonnage : « FWER ≤ 0,05 » pour ICP est vrai par construction** dans les mondes conformes (c'est la garantie du théorème au niveau $\alpha$) ; l'exigence utile porte sur la puissance et sur le comportement en monde violé. « Puissance ≥ 0,75 » est non jugeable sans la taille d'effet plantée.
9. **Sonde de nuisance : $R^2>0{,}60$ n'est pas un défaut.** Si le graphe planté a taille → cause → fertilité, une latente causale est légitimement prédictive de la taille. Le critère confond corrélation et absorption ; il faut la corrélation *partielle* sachant les parents plantés.
10. **« Oui, partiellement » pour l'iVAE dans les courses** : avec $U$ = bras de dose, la condition de variabilité exige $m\ge 2k+1$ ; huit doses bornent à $k\le3$ latentes identifiables (illustratif, dérivé du théorème SUPPOSÉ). C ne le dit pas.
11. **Éprouve 1 et NOTEARS** : standardiser les variances tue la varsortabilité mais introduit une autre : SUPPOSÉ, un tri par $R^2$ reste exploitable après standardisation (Reisach et al. ont une suite sur ce point ; référence à vérifier). La ligne de base « tri par variance » doit inclure cette variante.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- *Dérive du mélange.* Dans un monde conforme, $I(\hat Z;U)=I(Z;U)$ ; sous dérive de $f_u$, $I(\hat Z;U)>I(Z;U)$ car $\hat Z$ absorbe $u$. Sur données réelles, la quantité jugeable est l'excès de prédictibilité de $U$ à partir de $X$ au-delà de ce que $\hat Z$ en donne : si un classifieur $X\to U$ bat $\hat Z\to U$ de plus qu'une marge préenregistrée, le mélange dépend de $U$ et l'iVAE est hors domaine. Sans cette mesure, l'affirmation « très probablement fausse » reste HYPOTHÈSE.
- *Stabilité inter-graines ≤ 0,05.* L'écart-type du MCC entre graines a un plancher d'échantillonnage en $O(1/\sqrt n)$ ; le seuil n'est jugeable que relativement à ce plancher estimé par rééchantillonnage.
- *Expérience 2.* $\operatorname{Var}(\widehat{\mathrm{ATE}})\ge 2p(1-p)/n$. Pour une demi-largeur de 5 points à 95 %, $n\ge 2(0{,}25)/(0{,}0255)^2\approx 770$ par bras (illustratif) ; pour 2 points, $\approx 4\,800$. Les seuils de C sont incompatibles avec $N=200$.
- *Transition de phase (±1 dose dans 85 % des simulations).* Un seuil net et une sigmoïde d'échelle $s$ sont discernables seulement si $s$ est inférieur à l'espacement de la grille de doses ; sinon le rapport de vraisemblance est non informatif quel que soit $n$.
- *Expérience 3.* Si $\hat\tau_{\text{QE}}$ par décile a une fiabilité (corrélation entre deux demi-échantillons) $r_{\text{QE}}$ et $\hat\tau_{\text{obs}}$ une fiabilité $r_{\text{obs}}$, la corrélation observée est bornée par $\sqrt{r_{\text{QE}}r_{\text{obs}}}$ ; avec quelques centaines d'unités traitées, $r_{\text{QE}}$ par décile peut être inférieure à 0,25 et le seuil $\rho\ge0{,}50$ devient inatteignable même si les deux estimateurs visent la même quantité.
- *Interférence.* Si des paires d'une même course partagent agents et juge, la variance effective de $\widehat{\mathrm{ATE}}$ est multipliée par $1+(n_c-1)\rho_{\text{intra}}$ ($n_c$ paires par course, $\rho_{\text{intra}}$ corrélation intra-course) ; non mesurée, elle rend tout intervalle préenregistré trop étroit.

### (c) Contrôles négatifs dont l'absence est fatale

- **Bras de mondes conformes** (contrôle positif) : si une méthode échoue déjà là où ses hypothèses tiennent, le banc est cassé, pas la méthode.
- **Intervention fantôme** à la place du placebo cosmétique.
- **Jeu d'entraînement de $\hat\tau_{\text{obs}}$ amputé des cohortes de choc et de leurs périodes**, empreinté.
- **Fiabilité demi-échantillon de $\hat\tau_{\text{QE}}$ par décile**, publiée avant la comparaison.
- **Juge à étiquettes permutées** : le juge figé rejugeant un sous-ensemble dont les doses ont été permutées dans le journal doit donner un effet nul ; sinon la fuite est dans le juge.
- **Sonde de dépendance mélange–environnement** (ci-dessus) sur OpenAlex, préenregistrée, avant de déclarer l'iVAE hors domaine.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **« Erreur sur l'effet causal » pour un démêleur est biaisée par construction.** L'iVAE ne produit pas d'effet ; pour en obtenir un, il faut régresser $Y$ sur $\hat Z$, étape observationnelle confondue dans tout monde à confondeur. D attribuerait à la méthode l'échec d'une étape qu'elle n'a jamais revendiquée. Les scores « recouvrement des latentes » et « erreur d'effet » doivent être séparés et le second attribué à l'estimateur aval.
2. **Contrôle « fertilité antérieure au contact » circulaire en observationnel.** Dans OpenAlex, la date de « contact » entre deux niches n'est observable que par le premier papier pont, qui *est* l'issue. La fertilité antérieure au contact est donc nulle par définition : contrôle sans puissance. Il vaut pour les chocs datés de l'extérieur (déménagement, symposium), pas pour les paires observées.
3. **« Temps inversé » n'est pas un contrôle négatif pour toutes les méthodes.** SUPPOSÉ : pour TCL et iVAE, $U$ est une étiquette de segment ; inverser l'ordre des segments ne change rien au recouvrement. Un résultat inchangé serait alors conforme à la théorie, pas un artefact. Le contrôle n'a de sens que pour les méthodes orientées par le temps (CITRIS, PCMCI, Granger). D ne précise pour aucun contrôle le résultat attendu par méthode ; un contrôle sans issue attendue n'est pas jugeable.
4. **Épreuve 3 présuppose ce que D a marqué non audité.** D note que randomisation et indépendance du juge sont « RAPPORTÉ, non audité », puis bâtit l'épreuve 3 dessus sans prévoir l'audit.
5. **Épreuve 4 est vide telle quelle.** D écrit honnêtement « à défaut d'estimande commun, non décisive », mais ne propose aucun estimande commun ; l'épreuve n'a donc ni H_A ni H_B exécutables. Un candidat minimal : variation de la probabilité de première co-citation entre deux ensembles d'auteurs dans une fenêtre fixe, définie à l'identique dans la course (deux agents) et dans Boudreau et al. 2017 (RAPPORTÉ).
6. **Barre commune 0,80 / 0,05 inapplicable à la découverte de structure.** Un taux de fausses alertes de 5 % *par arête* sur 50 nœuds autorise environ 60 arêtes fausses (illustratif) ; il faut un FDR ou un nombre absolu attendu, pas un FPR.
7. **Interférence nommée dans le tableau, ignorée dans les épreuves** : l'épreuve 3 randomise « les paires » sans dire si des paires d'une même course sont indépendantes.
8. **« Mondes observationnellement équivalents à effets do différents »** : pour tester une méthode à auxiliaire, l'équivalence doit porter sur $p(X,U)$ et non sur $p(X)$ seul, sinon l'auxiliaire rompt l'équivalence et le contrôle est inopérant. D ne le précise pas.
9. **Fuite dans les cas appariés** : D exige des cas « appariés par taille, architecture, budget de réglage » — bien — mais le générateur reste unique (T3).

### (b) Conditions de perte de puissance ou de non-jugeabilité

- *Épreuve 1, « auxiliaire permutée ».* Le contrôle n'a de puissance que si $I(Z;U)>0$ de façon détectable : si, sur données réelles, l'accuracy d'un classifieur $X\to U$ n'excède pas celle du hasard de plus que le seuil préenregistré, analyse réelle et analyse permutée donnent le même résultat — ce qui prouve simultanément que le contrôle est vide *et* que l'identification par auxiliaire est impossible. D doit publier cette accuracy avant tout MCC.
- *Épreuve 2, « ≥ 10 % de gain dans le pire environnement ».* Non jugeable si la variance du score dans le pire environnement (le plus petit) dépasse le gain visé ; condition : $n_{\min}$ tel que l'écart-type du score hors environnement soit inférieur au tiers du gain (illustratif).
- *Épreuve 3, « ≤ 5 points ».* $n\gtrsim770$ par bras pour une issue à $p\approx0{,}5$ (illustratif) ; D renvoie à un calcul de puissance, mais le seuil et $n$ doivent être scellés ensemble, sinon le seuil est modifiable après coup. Design effect $1+(n_c-1)\rho_{\text{intra}}$ à mesurer.
- *Épreuve 1, « étiquettes causales échangées sans changer les observations ».* Ce contrôle n'est informatif que si la méthode reçoit *uniquement* les observations ; dès qu'elle reçoit $U$ ou $D$, l'échange d'étiquettes change les entrées et le contrôle teste autre chose.
- *Tri par variance comme base de LiNGAM.* Si la varsortabilité des données réelles (fraction de paires d'arêtes où la variance croît le long de l'arête, SUPPOSÉ : statistique de Reisach et al. 2021, RAPPORTÉ) est proche de 1 ou de 0, la base mécanique est quasi parfaite et aucune méthode ne peut la battre : le critère « battre la base » est non jugeable, et il faut le dire avant de conclure à l'échec.

### (c) Contrôles négatifs dont l'absence est fatale

- **Table « contrôle × méthode → issue attendue »**, préenregistrée : sans elle, « temps inversé » ou « auxiliaire permutée » ne sont pas interprétables.
- **Audit de randomisation** (équilibre pré-traitement) et **audit du juge** (rejugement à doses permutées dans le journal) avant l'épreuve 3.
- **Niche jumelle non exposée** à la place de « fertilité antérieure au contact » pour les paires observationnelles.
- **Accuracy $X\to U$** publiée avant le MCC (puissance du contrôle « auxiliaire permutée »).
- **Famille de générateurs scellée** distincte de celle du réglage (T3).

---

## Ce que je retiens des trois, en le disant (B1)

Je reprends de D la paire monde conforme / monde jumeau ne violant qu'une condition, et l'intervention fantôme ; de C, le tableau théorème × hypothèse × source de données et la borne $m\ge2k+1$ qu'il implique pour les courses ; de B, l'exigence d'une ligne de base prédictive à mêmes entrées. Je rejette : le contrôle « accompagnateur non recouvré » de B (faux positif par construction), le monde planté à dérive imposée de C comme preuve sur les données réelles, et la barre commune 0,80/0,05 de D pour les arêtes.

**Duel que les trois laissent ouvert (B4).** H_A : sur OpenAlex, la dépendance du mélange à l'environnement est détectable (un classifieur $X\to U$ bat $\hat Z\to U$ de plus que la marge scellée) ; H_B : elle ne l'est pas. Si H_A : l'iVAE et l'invariance par décennies sont hors domaine, ce qui falsifie l'affirmation « offertes par nos données » de conv-audit-6 et donne raison à C — mais par mesure, non par affirmation. Si H_B : l'argument central de C et le présupposé P3/P4 de B tombent, et l'identification par auxiliaire redevient candidate, à condition que $\operatorname{rang}(\hat\Lambda)=2k$ et que la loi nulle permutée du MCC soit publiée. Dans les deux cas, ce qui est réfuté est nommé.

FIN-DE-CELLULE