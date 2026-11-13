Les pièces transmises (`FAITS` et `QUESTION DE L'ARBITRE`) sont complètes et non coupées (VÉRIFIÉ). 

Voici l'analyse demandée pour pousser l'organisme d'idéation vers les bassins étroits et profonds sous vos contraintes strictes d'intégrité et d'architecture.

---

# (1) Ce que la question suppose sans que ce soit établi

La question de conception repose sur cinq postulats implicites dont le statut actuel est celui d'HYPOTHÈSE ou d'OBSERVÉ-NON-AUDITÉ :

1. **La transposabilité du piégeage en bassin à un système sans mémoire d'état (HYPOTHÈSE).** L'étude de Bespoke Labs montrant que 47 % des courses restent dans leur premier bassin porte sur des agents autonomes en sessions longues de 24 heures (RAPPORTÉ, [B]). Or, votre organisme opère déjà un « *flush* » radical : chaque appel de proposeur se fait en session neuve sans historique, à raison de 6 cartes par appel (RAPPORTÉ, [C3] §5.1). Que les modèles tombent dans les mêmes bassins larges d'un appel indépendant à l'autre relève d'un biais de la distribution *a priori* des poids du modèle face à une même vue, et non d'une dérive contextuelle intra-session.
2. **La possibilité d'orienter les proposeurs sans signal de retour (HYPOTHÈSE).** Les méthodes classiques d'exploration de bassins étroits en physique statistique ou en optimisation (recuit simulé, * Umbrella Sampling*, * novelty search*) utilisent un gradient, une énergie ou un score d'archive pour guider la marche. Ici, N-053 interdit de servir tout score ou verdict du juge aux agents (VÉRIFIÉ, Question), et le premier tour rejette toute prime numérique à la nouveauté (OBSERVÉ-NON-AUDITÉ, [S1]). Pousser vers un bassin étroit sans retour d'évaluation suppose que l'on puisse agir uniquement par *déformation de la vue d'entrée* (avant le proposeur) ou par *pondération aveugle aux issues* (entre le proposeur et le juge).
3. **La détectabilité statistique d'un bassin étroit et profond à échantillon fixé (HYPOTHÈSE).** Un bassin est défini dans la question comme ayant soit une faible probabilité sous la loi du modèle, soit un effet confiné/invisible en moyenne comme la composante conditionnelle (RAPPORTÉ, [C4] §2.1). Dans le second cas, si la sous-population où l'effet s'exprime a une masse $r(A)$ très faible, la borne de dilution $d \le r(A) \ln 2$ (OBSERVÉ-NON-AUDITÉ, [S1]) implique que la divergence de Kullback-Leibler globale entre la vraie loi et le nul est minuscule. Sans adaptation de la mise (le vecteur de pari de la valeur $e$), même une carte exacte tombant dans ce bassin aura une valeur $e$ proche de 1 et sera rejetée par e-BH.
4. **La décidabilité mécanique de l'équivalence aux frontières du nul (HYPOTHÈSE).** Pousser les modèles hors des bassins évidents (les effets principaux linéaires ou globaux) les pousse mécaniquement vers les formes `si_sinon` et `melange`, là où le juge actuel cède (RAPPORTÉ, [F12] §1 ; OBSERVÉ-NON-AUDITÉ, [S1]). La question suppose que l'on peut encourager l'exploration de ces formes conditionnelles sans faire exploser le taux de fausses découvertes au sens de l'oracle.
5. **La capacité cognitive de déduction séquentielle des modèles (HYPOTHÈSE).** Le monde v4 suppose qu'une fois la condition de rang 1 entrée dans l'archive, un proposeur qui lit l'archive proposera la composante conditionnelle de rang 2 (HYPOTHÈSE, [C4] §2.1). Rien n'établit qu'un modèle de langue, voyant une loi $P_0$ dans l'archive, calcule mentalement les résidus de $P_0$ pour formuler une bifurcation orthogonale plutôt que de simplement paraphraser $P_0$.

---

# (2) Quatre méthodes mathématiques pour atteindre les bassins étroits et profonds

Puisque l'organisme interdit de modifier les poids des modèles ou de leur servir les scores du juge (N-053), une méthode mathématique ne peut agir qu'à quatre endroits précis :
- **En amont (sur la Vue)** : par transformation géométrique de l'espace des lois présentées aux proposeurs (Méthode 1) ou par structuration combinatoire des vues (Méthode 4).
- **Au niveau du Juge (sur la construction des valeurs $e$)** : par localisation de la martingale de test pour donner du levier aux régions étroites sans violer $\mathbb{E}_{H_0}[e] \le 1$ (Méthode 2), ou par allocation du budget d'erreur $\alpha$ selon la géométrie prédictive sans les issues (Méthode 3).

---

### Méthode 1 : Quotientage algébrique dans l'espace dual des log-cotes (Génération résiduelle sur variété de d'Alembert-Amari)

**Domaine :** Géométrie de l'information (Amari, 2016, *Information Geometry and Its Applications*) et algèbre des groupes.

**Objet mathématique exact :**
Soit $\mathcal{X}$ l'espace des traits publics et $\mathcal{Y} = \{1, \dots, K\}$ l'espace fini des issues d'un épisode. L'espace des lois conditionnelles strictement positives $\mathcal{P} = \{ p(\cdot \mid x) : \mathcal{X} \to \Delta^{\circ}_{K-1} \}$ est muni d'une structure d'espace vectoriel par l'application de coordonnées duales (log-cotes par rapport à une issue de référence $K$), notée $\psi : \mathcal{P} \to \mathcal{F}(\mathcal{X}, \mathbb{R}^{K-1})$ :
$$\psi_k(p)(x) = \ln \frac{p(y=k \mid x)}{p(y=K \mid x)}, \quad k \in \{1, \dots, K-1\}.$$
L'application inverse est le `softmax` : $\psi^{-1}(\eta)(y=k \mid x) = \frac{\exp(\eta_k(x))}{1 + \sum_{j=1}^{K-1} \exp(\eta_j(x))}$, avec $\eta_K(x) = 0$.
On définit l'opération de perturbation de composition $\oplus : \mathcal{P} \times \mathcal{P} \to \mathcal{P}$ par :
$$(p \oplus q)(y \mid x) = \psi^{-1}\big(\psi(p)(x) + \psi(q)(x)\big).$$
$(\mathcal{P}, \oplus)$ forme un groupe abélien dont l'élément neutre est la loi uniforme $u(y \mid x) = 1/K$, et l'inverse de $p$ est $\ominus p = \psi^{-1}(-\psi(p))$.

Soit $\mathcal{A}_t = \{p_1, \dots, p_r\}$ l'archive à la génération $t$, et soit $p_{\text{base}} \in \text{ Span}_{\oplus}(\mathcal{A}_t)$ la loi de synthèse de l'archive (ou la dernière loi promue). Au lieu de demander aux proposeurs de rendre une carte globale $p \in \mathcal{G}$ (où $\mathcal{G}$ est la grammaire des 6 formes), on leur demande de rendre une **carte de déviation** $\delta \in \mathcal{G}$, que l'orchestrateur compose mécaniquement avant le passage au gardien et au juge :
$$p_{\text{soumise}} = p_{\text{base}} \oplus \delta.$$

- **Énoncé de garantie (Théorème de neutralisation de la composante archive) :** Pour toute famille exponentielle conditionnelle, la divergence de Kullback-Leibler satisfait $D_{\text{KL}}(p_{\text{base}} \oplus \delta \,\|\, p_{\text{base}}) = 0 \iff \delta = u$ ($\psi(\delta) = 0$ presque partout). De plus, toute carte constante par morceaux $\delta$ dans une sous-région $A \subset \mathcal{X}$ (via `si_sinon` avec $\psi(\delta)(x) = 0$ pour $x \notin A$) hérite exactement du comportement de $p_{\text{base}}$ hors de $A$ sans que le proposeur ait à réécrire la grammaire de $p_{\text{base}}$.
- **Preuve vs Conjecture :** La structure de groupe abélien et l'invariance hors du support de $\psi(\delta)$ sont des théorèmes élémentaires d'algèbre linéaire appliquée à la géométrie de l'information. Le fait que cette reparamétrisation déplace la masse de probabilité des propositions des LLM des bassins larges (déjà capturés dans $p_{\text{base}}$) vers les bassins étroits conditionnels est une **conjecture empirique** sur le comportement génératif des modèles de langue.

**Endroit où elle agit :** Interface Proposeur $\to$ Orchestrateur (transformation mécanique de la carte rendue et de la consigne de la vue).

**Qui calcule quoi et à partir de quelles informations :**
1. L'orchestrateur fixe $p_{\text{base}}$ à partir des lois de l'archive publique (aucune issue fraîche, aucun oracle).
2. La vue demande au proposeur de produire une carte $\delta$ représentant un *multiplicateur de cotes* (correction résiduelle) par rapport à $p_{\text{base}}$, en précisant que la forme `fixe` uniforme équivaut à « aucun changement ».
3. À réception de $\delta$, l'orchestrateur calcule mécaniquement $p_{\text{soumise}} = p_{\text{base}} \oplus \delta$ (qui est un simple `melange` log-linéaire ou une `transformee`, donc représentable dans la grammaire).

**Pourquoi elle atteint mieux un bassin étroit que des tirages indépendants :**
En tirages indépendants classiques, pour exprimer une idée dans un bassin étroit de profondeur 2 (ex. : une composante conditionnelle sur les traits $(x_2, x_3)$ alors que l'archive contient déjà un effet principal sur $x_1$), le proposeur doit consommer sa capacité syntaxique à *reconstruire* l'effet de $x_1$ tout en y greffant la branche sur $(x_2, x_3)$. S'il se trompe légèrement sur le coefficient de $x_1$, sa nouvelle carte perd en vraisemblance globale sur $x_1$ ce qu'elle gagne sur $(x_2, x_3)$, ou bien il se contente d'ajuster le coefficient de $x_1$ (raffinement du bassin large, comme les 11 cartes de la génération 1 de v67, RAPPORTÉ [F12] §2). En travaillant dans l'espace quotient $\mathcal{P} / \{p_{\text{base}}\}$, le bassin large déjà découvert est ramené à l'origine $\psi(\delta) = 0$. Toute copie ou variante de $p_{\text{base}}$ devient une carte triviale proche de l'uniforme, tandis qu'un `si_sinon` pur sur $(x_2, x_3)$ devient immédiatement compétitif sans avoir à réécrire $p_{\text{base}}$.

**Compatibilité avec les contraintes et preuve à fournir :**
- **N-053 / Vue :** 100 % compatible. Aucun score ni verdict n'est servi ; $p_{\text{base}}$ appartient à l'archive publique.
- **Garde contre les copies :** Comme le juge teste $p_{\text{soumise}}$ contre le nul engendré par l'archive $\mathcal{H}_0(\mathcal{A}_t)$, si le nul inclut les recombinaisons log-linéaires des lois de l'archive, il faut vérifier que $\delta$ qui rejoue $p_{\text{base}}$ donne simplement $p_{\text{base}} \oplus \alpha p_{\text{base}}$, ce qui est dans l'enveloppe log-linéaire de $p_{\text{base}}$. **Preuve à fournir au banc de métrologie :** certifier que le nul du juge couvre bien la famille exponentielle engendrée par $\psi(\mathcal{A}_t)$ (les puissances au sens de $\oplus$), afin qu'un $\delta$ proportionnel à $p_{\text{base}}$ ait une valeur $e$ d'espérance $\le 1$.

**Risques :**
Si le nul du juge actuel ne couvre que les mélanges *linéaires* (convexes) $\sum w_i p_i$ et non les mélanges *log-linéaires* $\psi^{-1}(\sum w_i \psi(p_i))$, une carte $\delta$ qui copie une loi de l'archive créerait une composition non linéaire susceptible de faire céder le juge (limite connue du juge, RAPPORTÉ [F12] §1). La solution consiste à inclure explicitement l'enveloppe log-linéaire de l'archive dans le nul du juge.

---

### Méthode 2 : Martingales de test localisées par décomposition en ondelettes de Haar sur l'arbre des strates (Juge multi-échelle à levier local)

**Domaine :** Analyse harmonique sur espaces métriques finis (ondelettes de Haar / filtrations dyadiques) et théorie des tests par valeurs $e$ (Vovk et Wang, 2021, *E-values: Calibration, combination and applications* ; Ramdas et al., 2023, *Game-Theoretic Statistics and Safe Anytime-Valid Inference*).

**Objet mathématique exact :**
Cette méthode s'attaque à la **borne de dilution** $d \le r(A) \ln 2$ (OBSERVÉ-NON-AUDITÉ, [S1]) qui empêche structurellement une idée confinée à une région rare $A \subset \mathcal{X}$ (bassin étroit dans les données) d'être promue par un rapport de vraisemblance global.

Soit $(\mathcal{X}_i, Y_i)_{i=1}^n$ l'échantillon frais du juge (scellé). Soit $p$ une carte candidate et $q_0 \in \mathcal{H}_0$ le représentant du nul (projection d'information inverse de $p$ sur le nul de l'archive). Pour chaque épisode $i$, le rapport de vraisemblance conditionnel est $L_i(p, q_0) = \frac{p(Y_i \mid X_i)}{q_0(Y_i \mid X_i)}$, qui vérifie $\mathbb{E}_{Y_i \sim q_0(\cdot \mid X_i)}[L_i(p, q_0) \mid X_i] = 1$.

Si $p$ ne diffère de $q_0$ que sur une région étroite $A \subset \mathcal{X}$ de masse $r(A) = \mathbb{P}(X \in A) \ll 1$, alors sur $A^c$, $L_i \approx 1$. Sur un mélange bét-martingale global ou un produit avec pas d'apprentissage $\lambda$ constant, le bruit accumulé sur $A^c$ (qui représente $1 - r(A)$ des tirages) écrase ou dilue le signal sur $A$.

Construisons la **mesure de divergence locale sans issue** entre $p$ et le nul $\mathcal{H}_0$ en chaque point $x \in \mathcal{X}$ :
$$\Delta(x) = \inf_{q \in \mathcal{H}_0} D_{\text{KL}}\big(p(\cdot \mid x) \,\|\, q(\cdot \mid x)\big).$$
Définissons la fonction de pari prévisible (ou poids d'attention de Haar) $\lambda : \mathcal{X} \to [0, 1[$ calculée *uniquement à partir de $X_i$ et des cartes $p, \mathcal{H}_0$ (sans regarder $Y_i$)* :
$$\lambda(x) = \min\left(\lambda_{\max}, \, c \cdot \sqrt{\Delta(x)}\right)$$
où $\lambda_{\max} \in ]0, 1[$ (par exemple $0{,}8$ — illustratif) et $c > 0$ est une constante d'échelle gelée.
On définit alors la valeur $e$ localisée sur les $n$ tirages par le produit :
$$E^{\text{loc}}_n(p) = \inf_{q_0 \in \mathcal{H}_0} \prod_{i=1}^n \Big( (1 - \lambda(X_i)) + \lambda(X_i) \frac{p(Y_i \mid X_i)}{q_0(Y_i \mid X_i)} \Big).$$

- **Énoncé de garantie (Validité exacte sous le nul et suppression de la dilution hors support) :**
  1. *(Validité conditionnelle et inconditionnelle)* Comme $\lambda(X_i)$ est $\sigma(X_i)$-mesurable (ne dépend pas de $Y_i$) et à valeurs dans $[0, 1]$, pour tout $q_0 \in \mathcal{H}_0$ :
     $$\mathbb{E}_{q_0}\left[ (1 - \lambda(X_i)) + \lambda(X_i) \frac{p(Y_i \mid X_i)}{q_0(Y_i \mid X_i)} \,\middle|\, X_i \right] = (1 - \lambda(X_i)) + \lambda(X_i) \cdot 1 = 1.$$
     Par récurrence sur la filtration $\mathcal{F}_i = \sigma(X_1, Y_1, \dots, X_i, Y_i, X_{i+1})$, le processus est une martingale positive d'espérance exactement $1$ sous $q_0$, donc $\mathbb{E}_{H_0}[E^{\text{loc}}_n(p)] \le 1$.
  2. *(Immunité à la dilution sur $A^c$)* Sur toute région $A^c$ où $p(\cdot \mid x) \in \mathcal{H}_0(x)$, on a $\Delta(x) = 0 \implies \lambda(x) = 0$. Les facteurs du produit pour $X_i \in A^c$ valent **exactement 1** : la variance sur $A^c$ est réduite à zéro, et le taux de croissance asymptotique $\frac{1}{n} \ln E^{\text{loc}}_n(p)$ ne dépend plus que des tirages tombant dans le bassin étroit $A$ où $\Delta(x) > 0$.
- **Preuve vs Conjecture :** Les points 1 et 2 sont des **théorèmes mathématiques exacts** (la preuve tient en trois lignes ci-dessus par conditionnement sur $X_i$). L'optimalité du profil $\lambda(x) \propto \sqrt{\Delta(x)}$ vient d'un développement de Taylor à l'ordre 2 de $\mathbb{E}_p[\ln(1 - \lambda + \lambda L)]$ autour de $L=1$ (critère de Kelly local).

**Endroit où elle agit :** Juge statistique (orchestrateur), lors du calcul de la valeur $e$ de chaque groupe/représentant, sans toucher aux proposeurs.

**Qui calcule quoi et à partir de quelles informations :**
L'orchestrateur seul. Pour une carte $p$ et un point $X_i$ de l'échantillon du juge, il évalue $\Delta(X_i)$ (distance KL entre deux distributions finies sur $\mathcal{Y}$, calculable en $O(|\mathcal{Y}|)$ une fois $q_0$ identifié), en déduit $\lambda(X_i)$, puis évalue le facteur de martingale avec l'issue $Y_i$. Aucun agent n'est impliqué ni informé (N-053 respecté).

**Pourquoi elle atteint mieux un bassin étroit que des tirages indépendants :**
Même si un proposeur génère par chance une carte parfaite sur une composante conditionnelle étroite (ou si $p$ est égale à l'archive partout sauf sur une strate rare $A$ de masse $r(A) = 0{,}05$ — illustratif), un juge global standard qui évalue ou lisse l'erreur sur tout $\mathcal{X}$ noie l'avantage acquis sur les $5\%$ d'épisodes de $A$ dans le bruit d'estimation (ou la sous-optimalité du nul empirique) sur les $95\%$ d'épisodes de $A^c$. Le pari localisé $\lambda(X_i)$ « met le juge en sommeil » ($\lambda=0$) là où la carte ne revendique aucune nouveauté par rapport à l'archive, et concentre $100\%$ du capital de risque martingale sur le bassin étroit $A$.

**Compatibilité avec les contraintes et preuve à fournir :**
- Totalement compatible avec O2, N-053, et l'engagement scellé (la formule de $\lambda(x)$ est figée avant la course).
- **Preuve à fournir :** Démontrer que le calcul de $q_0 \in \mathcal{H}_0$ est fait soit par un infimum sur une grille couvrante du nul, soit par la méthode du maximum de vraisemblance a posteriori (Universal Inference de Wasserman et al., 2020, *Universal inference*) sur un sous-échantillon disjoint, pour garantir rigoureusement $\mathbb{E}_{H_0}[E^{\text{loc}}_n] \le 1$ face à un nul composite.

**Risques :**
C'est ici que le **danger commun identifié au premier tour** (OBSERVÉ-NON-AUDITÉ, [S1]) est maximal : si une carte utilise `si_sinon` pour s'écarter d'une loi de l'archive sur une strate $A$ en imitant sur $A$ une *autre* loi de l'archive (recombinaison par morceaux non couverte par un nul global), alors $\Delta_{\text{global}}(x)$ semblera non nul alors que localement sur $A$, la carte copie l'archive !
**Parade mathématique exacte :** Définir $\Delta(x)$ **ponctuellement** contre l'enveloppe convexe locale de l'archive en $x$ :
$$\Delta_{\text{ponctuel}}(x) = \min_{q \in \text{Conv}(\mathcal{A}_t(x))} D_{\text{KL}}\big(p(\cdot \mid x) \,\|\, q(\cdot \mid x)\big).$$
Avec cette définition ponctuelle de $\Delta_{\text{ponctuel}}(x)$, si une carte `si_sinon` colle la loi d'archive $p_1$ sur $A$ et la loi d'archive $p_2$ sur $A^c$, alors $\Delta_{\text{ponctuel}}(x) = 0$ **pour tout $x \in \mathcal{X}$** ! On obtient alors $\lambda(x) \equiv 0$, d'où $E^{\text{loc}}_n(p) \equiv 1$ : **la recombinaison par morceaux de lois de l'archive est neutralisée mathématiquement avec une valeur $e$ bloquée à 1.**

---

### Méthode 3 : Pondération de l'allocation e-BH par la mesure de Jeffreys-levier de la géométrie de prédiction (Pondération a priori aveugle aux issues)

**Domaine :** Théorie des tests multiples pondérés (Genovese, Roeder et Wasserman, 2006, *False discovery control with p-value weighting* ; adapté aux valeurs $e$ par Wang et Ramdas, 2022, *False discovery rate control with e-values*) et plans d'expériences optimaux ($D$-optimalité / mesure de levier).

**Objet mathématique exact :**
Soient $G_1, \dots, G_m$ les groupes de doublons formés à une génération donnée (avec $m$ ou la règle de formation fixée d'avance, RAPPORTÉ [C3] §3.1), et $E_1, \dots, E_m$ leurs valeurs $e$. La procédure e-BH standard ordonne les $E_g$ et rejette les hypothèses pour lesquelles $E_{(k)} \ge \frac{m}{\alpha k}$.
La version pondérée de e-BH attribue à chaque groupe $g \in \{1, \dots, m\}$ un poids déterministe $w_g \ge 0$ tel que $\sum_{g=1}^m w_g = m$, et applique e-BH aux valeurs $e$ pondérées $\widetilde{E}_g = w_g E_g$.

- **Énoncé de garantie (Contrôle du FDR sous pondération dépendante des traits seuls) :** Si les poids $(w_1, \dots, w_m)$ sont calculés *uniquement* à partir des cartes candidates, de l'archive et du jeu public d'instances **sans issue** $\mathcal{D}_{\text{pub}} = \{x_1, \dots, x_N\}$ (indépendamment des issues $(Y_i)$ du juge), alors sous l'hypothèse que $\mathbb{E}_{H_0}[E_g \mid \mathcal{D}_{\text{pub}}] \le 1$, la procédure e-BH appliquée à $(\widetilde{E}_1, \dots, \widetilde{E}_m)$ contrôle le taux de fausses découvertes (FDR) au niveau $\alpha$ pour toute structure de dépendance entre les $E_g$.
- **Preuve :** Pour tout ensemble d'hypothèses vraies $\mathcal{N}_0 \subset \{1, \dots, m\}$, la preuve standard de Wang et Ramdas (2022) utilise uniquement l'inégalité de Markov et le fait que $\sum_{g \in \mathcal{N}_0} \mathbb{E}[\widetilde{E}_g] = \sum_{g \in \mathcal{N}_0} w_g \mathbb{E}[E_g] \le \sum_{g=1}^m w_g = m$.

Comment construire $w_g$ pour favoriser les bassins étroits sans créer une « prime de nouveauté » manipulable ? En utilisant le **score de levier spectral (ou d'isolement géométrique)** sur le jeu public sans issue $\mathcal{D}_{\text{pub}}$ :
Pour chaque groupe $g$ (représenté par $p_g$), on calcule son profil d'innovation ponctuel (défini à la Méthode 2) sur $\mathcal{D}_{\text{pub}}$ :
$$v_g = \big( \Delta_{\text{ponctuel}}(p_g, x_1), \dots, \Delta_{\text{ponctuel}}(p_g, x_N) \big) \in \mathbb{R}_+^N.$$
On normalise chaque vecteur non nul en distribution d'attention sur les instances : $\hat{v}_g = v_g / \|v_g\|_1 \in \Delta_{N-1}$.
1. *Facteur d'étroitesse de support (entropie inverse) :* Une carte qui cible un bassin étroit (une strate rare $A$) concentre son innovation $\hat{v}_g$ sur peu d'instances $x_j$, donc a une faible entropie de Shannon $H(\hat{v}_g)$ et un grand rapport crête-sur-moyenne $s_g = \frac{\max_j v_{g,j}}{\frac{1}{N}\sum_j v_{g,j}} \in [1, N]$.
2. *Facteur de décongestion (levier de la matrice de Gram) :* Soit $K \in \mathbb{R}^{m \times m}$ la matrice de similarité cosinus entre les profils d'attention $K_{g, g'} = \langle \hat{v}_g / \|\hat{v}_g\|_2, \hat{v}_{g'} / \|\hat{v}_{g'}\|_2 \rangle$. Si 5 groupes tombent dans le même bassin large mais juste au-dessus du seuil $\varepsilon$ de fusion des doublons, leurs profils $\hat{v}_g$ sont colinéaires : la somme de la ligne $d_g = \sum_{g'=1}^m K_{g, g'}$ vaut environ 5. Si un groupe explore seul un bassin étroit sur une autre strate, son profil est orthogonal aux autres et $d_g \approx 1$.
On pose alors le poids brut $\tilde{w}_g = \frac{\ln(1 + s_g)}{d_g}$, normalisé par $w_g = m \frac{\tilde{w}_g}{\sum_{l=1}^m \tilde{w}_l}$.

**Pourquoi cela ne viole pas le rejet du 1er tour (« aucune récompense numérique de la nouveauté dans le juge ») :**
Le rejet du premier tour (OBSERVÉ-NON-AUDITÉ, [S1]) vise l'ajout d'un bonus additif de nouveauté au score de qualité ou la sélection d'une carte *parce qu'elle est nouvelle* même si elle prédit mal (ce qui détruit la garantie sous $H_0$). Ici, $w_g$ est un multiplicateur borné dans e-BH qui **conserve rigoureusement la garantie $\text{FDR} \le \alpha$ sous $H_0$**. Une carte fausse dans un bassin étroit a toujours $\mathbb{E}[E_g] \le 1$ et est rejetée ; simplement, à budget d'erreur $\alpha$ constant, on cesse de gaspiller 80 % du budget de test de Benjamini-Hochberg sur 10 variantes quasi-colinéaires d'un bassin large ($d_g$ grand) pour réallouer la puissance de test aux propositions isolées qui testent des strates spécifiques ($s_g$ grand, $d_g \approx 1$).

**Endroit où elle agit :** Juge statistique (étape e-BH sur les groupes).

**Qui calcule quoi :** L'orchestrateur calcule $(v_1, \dots, v_m)$ sur $\mathcal{D}_{\text{pub}}$ (sans issue) avant de lire les issues du juge, fixe $(w_1, \dots, w_m)$, puis applique e-BH pondéré.

**Risques :**
Si $w_g$ n'est pas borné supérieurement (ex. : $m$ grand et un seul groupe très pointu), un faux positif sur ce groupe aurait un poids élevé. Il suffit d'imposer une borne de troncature a priori $w_g \in [w_{\min}, w_{\max}]$, par exemple $[0{,}2 \,;\, 3{,}0]$ (illustratif) avant renormalisation.

---

### Méthode 4 : Plans d'expériences combinatoires orthogonaux (Orthogonal Arrays / Plans de Plackett-Burman) sur le filtrage de la Vue

**Domaine :** Combinatoire algébrique et théorie des plans d'expériences (Hadamard, 1893 ; Plackett et Burman, 1946, *The Design of Optimal Multifactorial Experiments* ; Hedayat, Sloane et Stufken, 1999, *Orthogonal Arrays: Theory and Applications*).

**Objet mathématique exact :**
Un tableau orthogonal $\text{OA}(N_{\text{appels}}, d, 2, t)$ de force $t$ est une matrice $M \in \{0, 1\}^{N_{\text{appels}} \times d}$ telle que dans tout sous-ensemble de $t$ colonnes (correspondant à $t$ traits publics du monde), chacune des $2^t$ combinaisons de présence/absence apparaît le même nombre de fois.
- **Attention aux contraintes :** Le premier tour a rejeté le **masquage d'une partie de l'archive** (OBSERVÉ-NON-AUDITÉ, [S1]). Il ne s'agit donc **en aucun cas** de masquer l'archive $\mathcal{A}_t$ (qui reste intégralement visible à tous les appels), mais de structurer des **focus d'attention sur les traits publics $\mathcal{X} = (X^{(1)}, \dots, X^{(d)})$** ou sur des paires de strates publiques entre les différents proposeurs (ou entre les 6 emplacements de cartes demandés à un même proposeur).

Plus précisément, au sein d'un appel d'un proposeur qui doit rendre $k=6$ cartes (RAPPORTÉ, [C3] §5.1), la vue standard demande 6 cartes sans différencier les 6 emplacements, ce qui conduit le modèle à échantillonner 6 fois autour du mode principal de sa distribution (le bassin large).
Soit $\mathcal{T} = \{1, \dots, d\}$ l'ensemble des traits publics. À la génération $r$, l'orchestrateur calcule sur l'archive $\mathcal{A}_r$ la **matrice d'influence de Sobol-Hellinger** des traits déjà utilisés par l'archive : pour chaque trait $j \in \mathcal{T}$, soit $I_j(\mathcal{A}_r)$ la variation moyenne de Hellinger des lois de l'archive lorsqu'on permute la coordonnée $x^{(j)}$ sur le jeu public sans issue $\mathcal{D}_{\text{pub}}$.
Les traits où $I_j(\mathcal{A}_r)$ est élevé définissent les coordonnées des bassins déjà explorés ; les paires $(j, l)$ où l'interaction d'ordre 2 dans l'archive est nulle ($I_{j,l}(\mathcal{A}_r) = 0$) forment le complémentaire orthogonal.

L'orchestrateur partitionne les 6 cartes demandées à chaque proposeur selon un plan en blocs équilibrés incomplet (BIBD) ou un tableau orthogonal de force $t=2$ sur les sous-ensembles de traits peu ou non couverts à l'ordre 2 par l'archive, en assignant à chaque emplacement de carte $c \in \{1, \dots, 6\}$ une **sonde de strate publique** $(X^{(j_c)}, X^{(l_c)})$ à inspecter en priorité par rapport à l'archive complète.

- **Énoncé de garantie (Couverture minimax des interactions d'ordre $t$) :** Si un bassin étroit dépend d'une interaction conditionnelle d'ordre $t=2$ (comme la composante conditionnelle de [C4] §2.1), un tirage indépendant de $M$ propositions qui choisissent chacune leurs traits selon une loi marginale biaisée $q = (q_1, \dots, q_d)$ (où $\min_j q_j = \epsilon \ll 1/d$) a une probabilité de ne jamais inspecter la paire rare $(j^*, l^*)$ égale à $(1 - q_{j^*} q_{l^*})^M \approx \exp(-M \epsilon^2)$. Un pavage par tableau orthogonal $\text{OA}(M, d, 2, 2)$ ou couverture de Turán garantit que toute paire $(j, l)$ est soumise à l'inspection explicite dès que $M \ge \binom{d}{2} / \binom{r}{2}$ (ou $O(\ln d)$ en binaire), transformant un temps d'attente en $\Omega(1/\epsilon^2)$ en une couverture déterministe en $O(d^2)$ (ou $O(\ln d)$).
- **Preuve vs Conjecture :** La borne de couverture combinatoire est un théorème classique (borne de Roux / Erdős-Ko-Rado / Kleitman-Spencer). L'hypothèse que le modèle obéit à l'assignation de sonde de traits par emplacement de carte sans dégrader la qualité prédictive de la carte est une **conjecture empirique** testable.

**Endroit où elle agit :** Construction de la Vue servie aux proposeurs (orchestrateur), sans masquer l'archive, sans quota de formes grammaticales (le modèle reste libre d'utiliser n'importe laquelle des 6 formes), et sans aucun retour du juge.

**Qui calcule quoi et à partir de quelles informations :**
L'orchestrateur calcule les indices de sensibilité $I_j(\mathcal{A}_r)$ et $I_{j,l}(\mathcal{A}_r)$ *uniquement* à partir des fonctions mathématiques des lois de l'archive $\mathcal{A}_r$ et du jeu public sans issue $\mathcal{D}_{\text{pub}}$ (aucune issue, aucun juge, aucun oracle). Il génère par programme déterministe (graine scellée) l'assignation des sondes de traits pour les 6 cartes de chaque proposeur.

**Compatibilité avec les contraintes :**
- Ne viole aucun rejet du premier tour : l'archive est 100 % visible, il n'y a aucun quota de formes grammaticales (`softmax`, `si_sinon`, etc. restent libres), et aucun score de nouveauté n'est calculé ni servi.
- Respecte strictement N-053 : les indices $I_j(\mathcal{A}_r)$ ne proviennent ni d'un moniteur ni du juge, mais d'une simple analyse fonctionnelle des lois déjà publiées dans l'archive.

**Risques :**
Si le nombre de traits publics $d$ est très grand (ex. : $d > 100$ — illustratif) et que la plupart sont du bruit pur, forcer l'exploration uniforme de toutes les paires dilue le budget de proposition des modèles dans des directions vides. Cette méthode est donc optimale lorsque $d$ est modéré (ex. : $d \le 20$ — illustratif) ou couplée à la Méthode 1.

---

# (3) Ce qui est impossible en principe, et sous quelles hypothèses de structure un gain existe

### 3.1. Trois théorèmes d'impossibilité (Limites fondamentales)

**Théorème d'impossibilité 1 (No Free Lunch sur les bassins étroits sans structure a priori — Conservation de la masse de test).**
*Énoncé :* Soit $\mathcal{B}_1, \dots, \mathcal{B}_K$ une partition de l'espace des cartes hors du nul en $K$ bassins disjoints, où chaque bassin $\mathcal{B}_k$ correspond à une modification de la loi sur une région disjointe $A_k \subset \mathcal{X}$ de masse $r(A_k) = 1/K$. Sans information issue des étiquettes $(Y_i)$ dans la vue (contrainte N-053), toute méthode aveugle aux issues qui modifie la loi de proposition $Q$ des agents vérifie $\sum_{k=1}^K Q(\mathcal{B}_k) \le 1$. Si la nature plante le bassin profond uniformément au hasard parmi les $K$ régions, aucune transformation de la vue ou de l'échantillonnage ne peut augmenter la probabilité de toucher le bon bassin au-delà de $M/K$ pour $M$ propositions, quelle que soit la sophistication mathématique employée.
*Esquisse de preuve :* Par invariance par permutation des indices de régions $\{1, \dots, K\}$ avant l'observation des issues $Y$. Puisque la vue ne contient ni l'oracle ni les issues ni les verdicts du juge sur les candidats rejetés, la distribution jointe de la vue et de l'état de l'orchestrateur à la génération 1 est invariante par toute permutation des régions de même géométrie marginale sur $\mathcal{X}$.

**Théorème d'impossibilité 2 (Mur d'indétectabilité de Le Cam-Pinsker pour les bassins trop étroits).**
*Énoncé :* Soit $p_*$ une loi plantée qui ne diffère de la loi de l'archive $q_0 \in \mathcal{H}_0$ que sur un bassin étroit $A \subset \mathcal{X}$ de masse $r(A) = \mathbb{P}(X \in A)$, avec une divergence ponctuelle bornée par $\sup_{x \in A} D_{\text{KL}}(p_*(\cdot \mid x) \,\|\, q_0(\cdot \mid x)) \le \Delta_{\max}$ (profondeur locale). Alors, sur un échantillon du juge de taille $n$, **même avec la martingale localisée optimale de la Méthode 2 et même si un proposeur soumet exactement l'oracle $p_*$**, l'espérance du log-facteur de croissance de toute valeur $e$ valide ($\mathbb{E}_{q_0}[E_n] \le 1$) est bornée par :
$$\mathbb{E}_{p_*}[\ln E_n] \le D_{\text{KL}}(p_*^{\otimes n} \,\|\, q_0^{\otimes n}) = n \cdot r(A) \cdot \Delta_{\max}.$$
Par conséquent, pour que la carte soit promue par e-BH au seuil $E_n \ge \frac{m}{\alpha}$, il est **mathématiquement impossible** d'y parvenir de manière fiable si :
$$r(A) \cdot \Delta_{\max} \lesssim \frac{\ln(m / \alpha)}{n}.$$
*Conséquence pour le directeur :* On ne peut pas pousser l'organisme vers un bassin arbitrairement étroit ($r(A) \to 0$) à taille d'échantillon du juge $n$ constante, à moins que sa profondeur locale $\Delta_{\max}$ ne compense exactement son étroitesse ($r(A) \Delta_{\max} = \Omega(\frac{\ln m}{n})$).

**Théorème d'impossibilité 3 (Indiscernabilité locale des copies par morceaux sans nul ponctuel).**
*Énoncé :* Si le nul du juge $\mathcal{H}_0$ est défini uniquement par une enveloppe convexe globale $\left\{ \sum_{l=1}^r w_l p_l : w \in \Delta_{r-1} \right\}$ à poids $w_l$ constants sur $\mathcal{X}$, alors dès que l'archive contient au moins deux lois distinctes $p_1 \neq p_2$, il existe une partition mesurable $\mathcal{X} = A \sqcup A^c$ telle que la carte `si_sinon` $p_{\text{copie}}(y \mid x) = \mathbf{1}_{x \in A} p_1(y \mid x) + \mathbf{1}_{x \in A^c} p_2(y \mid x)$ ait une divergence globale strictement positive par rapport à tout mélange convexe global de $p_1$ et $p_2$ sous la vraie loi du monde (dès que $p_1$ domine sur $A$ et $p_2$ sur $A^c$).
*Conséquence :* Toute méthode qui pousse vers les bassins conditionnels (`si_sinon`) fera sauter la garde contre les copies **sauf si** le nul est étendu à l'enveloppe convexe *ponctuelle* $\mathcal{H}_0^{\text{loc}}(x) = \text{Conv}(\mathcal{A}_t(x))$ comme proposé dans la Méthode 2.

---

### 3.2. Sous quelles hypothèses de structure un gain existe

Un gain strict à coût égal existe si et seulement si le monde planté et les modèles vérifient au moins l'une des trois hypothèses de structure suivantes :
1. **Structure hiérarchique / héréditaire (Hypothèse de Hamada-Wu) :** Les bassins étroits profonds sont des *raffinements conditionnels* (profondeur 2 ou 3) greffés sur les variables qui portent déjà un effet de rang 1 dans l'archive, ou dont la somme marginale s'annule mais qui s'activent une fois conditionnés par une loi de l'archive (exactement la structure du monde v4, RAPPORTÉ [C4] §2.1). Ici, la **Méthode 1** (quotientage dans l'espace des log-cotes) et la **Méthode 2** débloquent le gain.
2. **Biais de redondance générative des LLM :** La loi spontanée des proposeurs $Q_{\text{LLM}}$ concentre $80\%$ (illustratif) de sa masse sur un sous-espace de basse dimension (toujours les 2 mêmes traits saillants ou des variations infimes de paramètres). Ici, la **Méthode 3** (pondération par levier de Gram) et la **Méthode 4** (tableau orthogonal sur la vue) brisent la concentration redondante sans perte de puissance sur $H_0$.
3. **Confinement spatial du signal ($r(A)$ petit, $\Delta_{\max}$ grand) :** L'idée est invisible en moyenne globale mais très forte sur une strate $A$ ($r(A) \Delta_{\max} > \frac{2 \ln(m/\alpha)}{n}$). Ici, la **Méthode 2** (martingale localisée avec nul ponctuel) élimine le bruit des $1 - r(A)$ épisodes hors support qui aveuglait le juge standard.

---

# (4) L'expérience décisive la moins chère (Duel $H_A$ contre $H_B$)

Conformément à la convergence du premier tour (OBSERVÉ-NON-AUDITÉ, [S1]) et au principe N-045 (« le bon marché d'abord, le cher sur preuve »), l'expérience se déroule en **deux étages** : Étage 0 à coût LLM nul (banc hors ligne sur le juge avec propositions synthétiques contrôlées), suivi de l'Étage 1 (duel sur un seul appel par proposeur et par génération sur 2 générations).

### Paramétrage du monde planté à graine scellée
On génère par programme à graine scellée un monde à $d = 6$ traits publics binaires ou continus standardisés $(X^{(1)}, \dots, X^{(6)})$ et une issue binaire $Y \in \{0, 1\}$, dont la vraie loi en log-cotes $\eta_*(x) = \ln \frac{\mathbb{P}(Y=1 \mid x)}{\mathbb{P}(Y=0 \mid x)}$ possède trois bassins plantés :
- **Bassin 0 (Archive initiale $\mathcal{A}_0$) :** $\eta_0(x) = \beta_0 x^{(1)}$.
- **Bassin 1 (Large et peu profond — le piège) :** Un effet principal global sur $X^{(2)}$, visible partout ($r(A_1) = 1$), mais de profondeur modérée $\Delta_1$.
- **Bassin 2 (Étroit et profond — la cible) :** Une composante conditionnelle pure confinée à une région $A_2 = \{x \in \mathcal{X} : x^{(1)} > \tau_1, \, x^{(3)} > \tau_3\}$ de **largeur réglable** $r(A_2) \in \{0{,}05 \,;\, 0{,}10 \,;\, 0{,}20\}$ (illustratif) et dont le signe s'inverse selon $X^{(4)}$ (moyenne marginale exactement nulle sur $X^{(3)}$ et $X^{(4)}$ seuls), avec une **profondeur locale réglable** $\Delta_2$ telle que le produit $r(A_2)\Delta_2$ dépasse de $3\times$ (illustratif) le seuil de Le Cam $\frac{\ln(m/\alpha)}{n}$, tout en vérifiant $r(A_2)\Delta_2 > \Delta_1$ (gain total plus profond que le bassin large une fois trouvé).

### Les deux hypothèses en duel (à coût d'appel de modèles et d'échantillon strictement identiques)
- **$H_0 / H_B$ (Témoin à coût égal — Conception actuelle v3/v4) :** Vue standard avec l'archive complète ; 6 cartes par proposeur en session neuve ; regroupement des doublons ([C3] §3.1) ; juge avec valeur $e$ globale standard contre le nul de l'archive ; e-BH non pondéré au niveau $\alpha$.
- **$H_A$ (Bras Mathématique : Méthode 1 + Méthode 2 + Méthode 3) :** Même budget d'appels, mêmes modèles, même taille d'échantillon $n$, même $\alpha$ :
  1. Les cartes rendues sont interprétées dans l'espace quotient $p_{\text{base}} \oplus \delta$ (Méthode 1).
  2. Le juge calcule la valeur $e$ par la martingale localisée $E^{\text{loc}}_n$ contre le nul convexe/log-linéaire **ponctuel** $\Delta_{\text{ponctuel}}(x)$ (Méthode 2).
  3. L'étape e-BH utilise les poids de levier spectral $w_g$ calculés sur $\mathcal{D}_{\text{pub}}$ sans issue (Méthode 3).
  *(Note : un bras factoriel intermédiaire peut isoler la Méthode 2 seule à coût d'appel LLM rigoureusement nul en rejouant sur des tirages frais du juge les cartes déjà produites, si un tampon de tirages scellés distincts est prévu au préenregistrement).*

### Métrique principale, seuil de décision et contrôles négatifs (gelés au préenregistrement R1)

| Composante du protocole | Définition exacte (calculée par programme ou lecteur neuf R13) | Seuil préenregistré (chiffres illustratifs à sceller avant course) |
| :--- | :--- | :--- |
| **Contrôle négatif 1 : Garde absolue sous nul pur** | Avant d'ouvrir la comparaison $H_A$ vs $H_B$, injection hors ligne de 100 cartes « pièges » (`si_sinon` recollant des lois de l'archive par morceaux sur des strates rares, et copies bruitées). | Taux de promotion empirique $\le \alpha$ (avec test binomial exact à $95\%$) et $\max_{\text{copie par morceaux}} E^{\text{loc}}_n = 1{,}00$. **Si échec : arrêt immédiat, $H_A$ est disqualifiée.** |
| **Contrôle négatif 2 : Monde sans bassin étroit ($\Delta_2 = 0$)** | Course sur un monde jumeau où le bassin étroit a une profondeur nulle ($\Delta_2 = 0$, pur bruit sur $A_2$). | Part de fausses découvertes au sens de l'oracle sur $A_2 \le \alpha$. |
| **Métrique primaire d'efficacité ($D_2^{\text{étroit}}$)** | Indicateur binaire d'oracle (et proportion sur $R=20$ graines de monde scellées — illustratif) : le Bassin 2 (étroit et profond) est-il couvert par au moins une carte **retenue** en fin de Génération 2 (et séparément : présent dans les **propositions brutes** pour distinguer l'effet Méthode 1 de l'effet Méthode 2) ? | $H_A$ l'emporte sur $H_B$ si : (i) le contrôle négatif 1 et 2 est validé, ET (ii) le taux de couverture retenue du Bassin 2 sous $H_A$ dépasse celui de $H_B$ d'au moins $+25$ points de pourcentage (test exact de McNemar unilatéral sur les $R$ graines appariées, $p < 0{,}025$). |
| **Métrique secondaire (Rendement KL d'oracle par dollar)** | Réduction de la divergence $D_{\text{KL}}(p_* \,\|\, p_{\text{archive finale}})$ divisée par le coût total mesuré en jetons et appels (N-058). | Gain médian $\ge +30\%$ (illustratif) sur les graines où $r(A_2) \le 0{,}10$. |

---

# (5) Ce qui me ferait changer d'avis

Je changerais d'avis et recommanderais d'abandonner chacune des méthodes proposées devant les faits réfutables suivants :

1. **Abandon de la Méthode 1 (Quotientage $\oplus$ dans l'espace des log-cotes) :**
   Si, lors de l'expérience décisive (à l'étage des *propositions brutes* lues par l'oracle D2 avant le passage du juge), la proportion de cartes brutes qui touchent le bassin étroit $A_2$ sous la formulation résiduelle $p_{\text{base}} \oplus \delta$ n'est pas supérieure à celle de la vue directe standard, **ou** si plus de $30\%$ (illustratif) des cartes produites par les proposeurs sous cette consigne échouent au gardien mécanique ou dégradent la vraisemblance hors de la région ciblée (incapacité des modèles de langue à raisonner en multiplicateurs de cotes).
2. **Abandon de la Méthode 2 (Martingale localisée $E^{\text{loc}}_n$) :**
   - *Sur la sécurité :* Si le banc de métrologie hors ligne trouve **ne serait-ce qu'une seule** recombinaison par morceaux de lois de l'archive qui échappe à la définition ponctuelle $\Delta_{\text{ponctuel}}(x)$ et obtient $\mathbb{E}_{H_0}[E^{\text{loc}}_n] > 1$.
   - *Sur l'utilité :* Si l'analyse des 3 étages de D2 ([C3] §4.1 : propositions brutes $\to$ représentants $\to$ retenues) montre que dans le bras témoin $H_B$, le goulet d'étranglement est à $100\%$ aux propositions brutes (c'est-à-dire que les proposeurs ne génèrent *jamais* une seule carte dans le bassin étroit, et que chaque fois qu'ils en génèrent une, le juge standard la promeut déjà sans perte). Dans ce cas, modifier le juge est inutile et seul le travail sur la vue (Méthodes 1 et 4) compte.
3. **Abandon de la Méthode 3 (Pondération e-BH par levier de Gram) :**
   Si le regroupement des doublons de la v3 ([C3] §3.1) suffit déjà à ramener le nombre de groupes par bassin large à exactement $1$ (rendant la matrice de Gram $K$ proche de l'identité $I_m$), et que la pondération par étroitesse de support $s_g$ favorise en pratique des cartes pathologiques qui surajustent une micro-strate vide de signal, réduisant la puissance sur les bassins de largeur intermédiaire.
4. **Abandon de la Méthode 4 (Tableaux orthogonaux sur les sondes de traits) :**
   Si imposer une sonde de traits $(X^{(j)}, X^{(l)})$ par emplacement de carte conduit les modèles à forcer artificiellement ces traits dans des formules absurdes lorsque la paire $(j, l)$ est en réalité inactive dans le monde planté, faisant chuter le taux global de promotions valides par rapport à un appel libre.

FIN-DE-CONSULTATION