# Audit indépendant de la démonstration sur l'évasion sous filtrage pendant l'entraînement après pré-entraînement (billet de Yair Halberstadt) — v1

- **Auditeur** : session d'audit indépendante. Elle n'a écrit aucune des pièces auditées et ne les a pas corrigées.
- **Date** : 24 novembre 2026, de 06:16 à 06:50 environ (UTC, relevé par `date -u`).
- **Coût** : 0 USD. Tout a tourné sur processeur. Aucun appel payant, aucune recherche en ligne, aucune publication.
- **Commit de départ** : `f2dcac18ffc1afe3a3b1852ac14532b793c115b2` ; branche `audit/evasion-post-entrainement-v1`.
- **Cloisonnement** : rien n'a été ouvert sous `docs/verdicts/`, `runs/`, `diag/`, `donnees/`, `coffre/` ni `essai/`, ni sur une branche `verdict/*`, `lecture/*` ou `coffre/*`.

---

## 0. Verdict

**Tient avec réserves.**

1. **Le noyau algébrique tient.** J'ai vérifié chaque égalité et chaque équivalence des deux théorèmes et de la proposition de trois façons : par le calcul symbolique, en arithmétique rationnelle exacte et à 80 chiffres. Je n'ai trouvé **aucun contre-exemple** aux énoncés tels qu'ils sont écrits, dans le modèle qu'ils posent.
2. **Plusieurs affirmations qui entourent ce noyau ne tiennent pas.** Elles se trouvent dans le résumé, dans la note d'élucidation et dans les pièces destinées au public.
   - **Fausses, avec contre-exemples reproductibles :**
     - le découplage hors boucle « annule » la pression sélective (§ 3.2) ;
     - une covariance négative ou nulle suffit sous la pénalité (§ 3.3) ;
     - le rejet pur « s'effondre vers la furtivité » (§ 3.5) ;
     - la pénalité enrichit, elle aussi, la part furtive pour toute récompense, alors que ce n'est vrai qu'à récompense égale entre tricheurs (§ 3.6).
   - **Vraie à la lettre mais trompeuse :** la pénalité qui « se retourne » (§ 3.4).
   - **Postulat de modèle présenté comme une loi :** l'opérateur de rejet pur (§ 3.1).
3. **L'annonce « 0 contre-exemple sur 14 000 » apporte peu.**
   - La famille des pièges, soit 1 000 tirages, recalcule l'inégalité qu'elle prétend tester.
   - Celle du découplage, 1 000 tirages, se réduit à un seul cas particulier.
   - Le seuil de dominance sous le rejet pur, la barrière sous le rejet pur et la proposition des cas limites ne sont pas testés (§ 2).
   - « Tout est vérifié en arithmétique rationnelle exacte » est faux : un seul exemple l'est.

   C'est la preuve écrite qui porte le résultat, pas les essais.

**Ce qu'il faut corriger avant toute diffusion** (la liste fermée est au § 6) : le sens donné au découplage hors boucle, l'idée que la pénalité « se retourne » contre le défenseur, la formule « le rejet pur s'effondre vers la furtivité », la phrase « tout est vérifié en arithmétique rationnelle exacte », les affirmations de nécessité et d'exhaustivité, et la présentation de l'opérateur de rejet comme une loi plutôt que comme un choix de modèle.

---

## 1. L'énoncé reconstruit, puis la preuve refaite

### 1.1 Cadre (manuscrit `main-v2.tex`, sections 2 et 3)

- **Les trois strates.** On découpe en trois strates l'ensemble des politiques ou des trajectoires sous le modèle de base $\pi_0$ : honnête (h), triche visible (v) et triche furtive (f). Leurs masses a priori vérifient $p_h, p_v, p_f > 0$ **strictement**, avec $p_h + p_v + p_f = 1$.
- **La récompense.** Elle vaut $0$ sur h, $\Delta R_v > 0$ sur v et $\Delta R_f = \Delta R_v - \delta_{\text{maint}}$ sur f. Le premier théorème suppose $\Delta R_v = \Delta R_f = \Delta R > 0$.
- **La survie au filtre.** On note $\beta = \mathbb{P}(\text{accepté} \mid \pi)$, constante par strate, avec $0 \le \beta_v < \beta_f \le \beta_h \le 1$ et $\beta_f > 0$.
- **Sans moniteur :** $\pi_{\text{no}} \propto e^{\eta R}\pi_0$.
- **Opérateur A, rejet pur avec réessai :** $\pi_A \propto \beta\, e^{\eta R}\pi_0$.
- **Opérateur B, pénalité $-C$ :** $\pi_B \propto \exp(\eta[\beta R - (1-\beta)C])\,\pi_0$, avec $\eta > 0$ et $C \ge 0$.

### 1.2 Premier théorème (sélection), refait sans le texte

| Énoncé | Ce que je retrouve | Hypothèse ou bord |
|---|---|---|
| 1. Identité de variance sous A : $\mathbb{E}_A[\beta\mid tr]-\mathbb{E}_\mu[\beta]=\operatorname{Var}_\mu\beta/\mathbb{E}_\mu\beta$ | Exacte, même si la récompense varie parmi les tricheurs : la densité de A par rapport à $\mu_{tr}$ vaut $\beta/\mathbb{E}\beta$. | Exige $\mathbb{E}_\mu\beta>0$. Strictement positive si et seulement si la variance est non nulle. |
| 1 bis. Deux strates : la part furtive parmi les tricheurs croît sous A et sous B | A : cote multipliée par $\beta_f/\beta_v$. B : cote multipliée par $e^{\eta(\beta_f-\beta_v)(\Delta R+C)}$. Exact. | B exige $\Delta R + C > 0$, ce qui est acquis puisque $\Delta R > 0$. |
| 2. Amplification absolue sous A si et seulement si $(\beta_f-\beta_v)p_v e^{\eta\Delta R} > (\beta_h-\beta_f)p_h$ | Exact. Le seuil $\Delta R^*_A$ peut être négatif : l'amplification a alors lieu pour tout $\Delta R > 0$. | Le cas $\beta_f = \beta_h$ est inconditionnel. Exige $p_v > 0$. |
| 3. Amplification absolue sous B (équation `eq:ampB`) | Exacte : c'est la comparaison des dénominateurs une fois normalisés par le poids furtif. | — |
| 4a. Sous A, le furtif l'emporte sur l'honnête si et seulement si $\Delta R > \eta^{-1}(\log\frac{p_h}{p_f}+\log\frac{\beta_h}{\beta_f})$ | Exact. | Voir le § 3.5 sur la formule « s'effondre vers la furtivité ». |
| 4b. Sous B, même comparaison, seuil $\frac{\beta_h-\beta_f}{\beta_f}C+\frac{1}{\eta\beta_f}\log\frac{p_h}{p_f}$ | Exact. | Exige $\beta_f > 0$. |
| 4c. Niche parfaitement furtive : $\pi_B(f)>\pi_A(f)$ si et seulement si $\eta(\Delta R+C)>\log(1/\beta_v)/(1-\beta_v)$ | Exact. | Exige $\beta_v > 0$. Le cas $\beta_v = 0$ est traité par la deuxième proposition. |
| Proposition (cas limites) | Exacte. | Le rapport des seuils n'est pas défini quand $p_h\beta_h = p_f\beta_f$ (dénominateur nul). Il est négatif si et seulement si $\log(p_h/p_f)$ et $\log(p_h\beta_h/(p_f\beta_f))$ sont de signes opposés, soit $\beta_f/\beta_h < p_h/p_f < 1$. Le texte ne le dit pas. |

### 1.3 Second théorème (les trois régimes d'échappement)

- **Barrière a priori.** L'équivalence sur la dominance de l'honnête est exacte sous A comme sous B. La phrase « si $\Pi_f$ est inatteignable ($p_f = 0$) » sort du domaine posé, qui exige $p_f > 0$ : c'est une limite informelle, pas un cas du théorème. L'égalité $\beta_f\Delta R_{\text{net}} = (\beta_h-\beta_f)C$ est bien exclue, puisque l'inégalité est stricte.
- **Découplage.** L'identité de covariance sous A est exacte. C'est l'identité de Price, ou de Robertson (§ 4). Sous B, la borne est exacte **sous indépendance ou sous association négative**, parce que $u \mapsto e^{\eta u(\Delta R+C)}$ est croissante. Pour deux variables, l'association négative équivaut à la dépendance négative par quadrants (Lehmann, 1966, à vérifier). Hypothèse cachée : $\pi_0(\mathcal S) > 0$. Sinon, la conditionnelle $\nu_0$ n'est pas définie, par exemple quand la récompense est continue.
- **Pièges plantés.** La borne est exacte : sa valeur en $C^*$ est nulle et elle décroît en $C$. La pente en $\tau_{\text{ord}}$ n'est négative que si $C > \frac{1-\rho+\rho\varepsilon}{\rho(1-\varepsilon)}\Delta R$. Cette condition découle de $C > C^*$, ce que la preuve ne dit pas mais qui est vrai. Le théorème écrit en toutes lettres que la politique honnête de référence vérifie $\beta_h = 1$. Ce qui reste implicite, c'est que l'honnête n'est pas non plus intercepté sur les épisodes pièges. Le lien avec le « ratio critique » de la barrière a priori n'est établi que pour $\beta_h = 1$.

**Ce que la comparaison avec le texte fait apparaître.** Les preuves écrites suivent les miennes ligne à ligne. Il n'y a ni pas non justifié ni erreur de signe. Les seuls écarts sont les hypothèses de bord signalées ci-dessus.

---

## 2. Ce que testent vraiment les 14 000 essais

J'ai relancé `verifier_exemples_papier_v2.py` (`4183ce84…`) **sur une copie**, avec `python3 -I`. Sa sortie est identique octet pour octet au fichier scellé `exemples-verifies-papier-v2.json` (`b1ee935f…`). Les graines et le décompte se reproduisent donc.

> **Attention, risque de type R12.** Lancé tel quel, à sa place, le script **réécrit** `exemples-verifies-papier-v2.json` dans son propre dossier. Il faut toujours le lancer sur une copie.

L'instrumentation rejoue les mêmes tirages sans toucher au script (`instrumenter_essais_v1.py`, sortie `instrumentation-essais-v1.json`). Elle donne ceci :

| Famille | Ce qui est testé | Constat |
|---|---|---|
| Premier théorème, 10 000 tirages | Le sens de l'enrichissement conditionnel sous A et B, les critères d'amplification sous A et sous B, le critère de dominance sous B, chacun comparé au calcul direct des lois de Gibbs. | Test honnête, mais **le seuil de dominance sous A (4a), la barrière sous A et la proposition des cas limites ne sont pas testés**. Le domaine est étroit : $\beta_f \ge 0{,}20$, $\beta_h \ge 0{,}55$, $\eta \le 8$, et $p_f \ge 0{,}0099$ par construction (minimum observé : $0{,}013$). **Aucun tirage n'a $\beta_f = \beta_h$.** Aucun tirage n'est écarté par la tolérance. |
| Niche, 2 000 tirages | La chaîne $\pi_A(f) > \pi_{\text{no}}(f)$ et le critère d'inversion. | Les masses a priori sont figées à $(0{,}70 ; 0{,}25 ; 0{,}05)$. |
| Découplage, 1 000 tirages | Le seul signe de la variation de survie à l'audit, sur quatre atomes de même poids. | **Test légitime mais réduit à un cas particulier.** La survie à l'audit y est construite comme le réarrangement exactement contre-monotone de la survie au filtre, un cas d'association négative, donc conforme à l'hypothèse. La conclusion découle alors de l'inégalité de Tchebychev sur les sommes. Ne sont testés ni l'identité de covariance, ni l'indépendance, ni le cas « covariance négative sans association négative ». |
| Pièges, 1 000 tirages | La borne de variation totale et le signe du gain. | **Tautologique** : une seule politique par tirage, la politique extrémale $\mathbf 1\{P_{\text{ord}} \ge P_{\text{piège}}\}$, pour laquelle l'écart vaut exactement la variation totale (écart maximal mesuré : $1{,}5\times10^{-16}$). Le seuil est calculé avec $\tau_{\min} = \tau_{\text{ord}}$ de cette même politique et $C = C^* + 0{,}5$. Le test recalcule donc l'inégalité qui définit $C^*$. Le moniteur est toujours aveugle sur les épisodes ordinaires. |
| « Arithmétique rationnelle exacte » | Un seul exemple, celui de l'identité de variance : $37/150$. | Tout le reste est en flottants à double précision. La phrase du résumé et de la contribution 4 (« every theorem and numerical table is verified in exact rational arithmetic ») est **fausse**. |

**Le script que cite la note.** Le « 14 000, 0 contre-exemple » de la note d'élucidation renvoie à un autre script, `test_mort_halberstadt_v1.py` (`381e3c12…`). Il emploie les mêmes graines. Je ne l'ai examiné que sur un point : son seuil des pièges, `c_seuil` (ligne 302), omet le terme $\rho\varepsilon(\tau-\delta)$ et se trouve donc **sous** $C^*$, d'un écart de $\varepsilon\Delta R/(1-\varepsilon) \approx 0{,}02$. Le test passe malgré tout, parce qu'on choisit $C =$ `c_seuil` $+ 0{,}5$. L'erreur de formule est masquée par la marge.

**Lecture au sens de la règle de symétrie (R4).** Le « zéro sur 14 000 » est propre parce que les énoncés sont des identités algébriques élémentaires, qu'une famille d'essais est tautologique et qu'une autre se réduit à un cas particulier. Ce n'est pas la trace d'une fraude. C'est en revanche la marque d'une **preuve par essais qui n'ajoute presque rien à la preuve écrite**. L'annonce doit être retirée ou décrite exactement.

---

## 3. Vérificateur indépendant et recherche adverse

Le script est `verificateur_independant_evasion_v1.py`. Il est écrit sans rien réemployer du code audité. Il utilise `sympy`, `fractions` et `mpmath` à 80 chiffres, et `scipy` pour un contrôle croisé. Les graines viennent de `numpy.random.SeedSequence(202611240616)`, avec une sous-graine par tâche. Deux exécutions donnent le même JSON (`resultats-verificateur-independant-v1.json`, empreinte au § 7).

**Ce qui tient, avec zéro désaccord partout :**

- **Preuves symboliques.** Neuf égalités sont vérifiées par `sympy` : l'identité de variance avec récompenses hétérogènes, la factorisation de l'amplification sous A, l'équivalence de l'amplification sous B, la réécriture de $\pi_B(f)$, la cote furtif sur honnête sous B, la différence des poids visibles dans la niche, l'annulation et la pente de la borne des pièges, et l'identité de covariance.
- **Arithmétique exacte sous A.** 20 000 instances rationnelles, en posant $E = e^{\eta\Delta R}$ comme variable libre, et dont 20 % ont $\beta_f = \beta_h$.
- **Points de bord.** Au seuil exact, les deux membres sont égaux à $10^{-79}$ près. C'est le cas pour 1 266 seuils d'amplification sous A, 1 384 seuils de dominance sous A, 1 437 seuils de dominance sous B et 1 054 seuils d'inversion.
- **Recherche adverse sur domaines larges.**
  - 40 000 tirages pour chacun des six énoncés : masses a priori jusqu'à $10^{-12}$, $\eta$ de $10^{-3}$ à $10^{3}$, $\Delta R$ de $10^{-6}$ à $10^{2}$, $C$ jusqu'à $10^3$, et cas exacts $\beta_f = \beta_h$, $\beta_v = 0$, $C = 0$.
  - 10 000 tirages pour la niche.
  - Aucun désaccord, aucun cas écarté au bord.
- **Pièges, pire politique exacte.** Je résous en rationnels exacts le programme linéaire « maximiser le gain sur toutes les politiques telles que $\tau_{\text{ord}} \ge \tau_{\min}$ ». J'y prends un moniteur ordinaire quelconque et une survie aux pièges au plus $\varepsilon$, sur 3 000 instances. **Aucun pire gain n'est positif quand $C > C^*$.** Le contrôle croisé par `scipy` donne zéro écart.
- **Tables.** Les 93 valeurs des trois tables sont relues dans le `.tex` et recalculées. L'écart maximal est de $4{,}9\times10^{-7}$, ce qu'explique l'arrondi à six décimales. Les seuils $0{,}257992$, $1{,}576778$, $2{,}807845$, $2{,}558428$, $0{,}279214$, $5{,}462585$ et $0{,}999998$ sont confirmés, ainsi que l'exemple rationnel $37/150$.

**Ce qui ne tient pas : les lectures qui dépassent les énoncés.**

### 3.1 L'opérateur A est un postulat de modèle, et le « dilemme » en dépend

$\pi_A$ est le maximiseur de $\mathbb{E}_\pi[R + \eta^{-1}\log\beta] - \eta^{-1}D_{KL}(\pi\|\pi_0)$. Le filtre y agit donc comme une prime de $\eta^{-1}\log\beta$ en unités de récompense, **qui s'efface quand $\eta$ croît**, par construction. L'« effondrement asymptotique » du rejet pur face à la « barrière non évanescente » de la pénalité (point 4a contre point 4b) vient de ce choix.

Prenons un rejet répété à chaque tour, comme dans l'itération sur échantillons filtrés. Après $T$ tours, $\pi \propto \beta^T e^{T\eta_1 R}\pi_0$. À $T$ fini, le furtif l'emporte sur l'honnête si et seulement si $T(\eta_1\Delta R - \log(\beta_h/\beta_f)) > \log(p_h/p_f)$. Quand $T \to \infty$, il l'emporte si et seulement si $\eta_1\Delta R > \log(\beta_h/\beta_f)$ : la barrière ne s'efface plus. Les chiffres sont dans le JSON, rubrique `sensibilite_rejet_repete`, avec $\Delta R = 1$ et un seuil de $1{,}438$. À $\eta = 200$, le logarithme de la cote vaut $+195$ pour l'opérateur du papier et $-92$ pour le rejet répété. Les conclusions s'inversent.

Ce second modèle est lui aussi un choix, et sa barrière dépend du pas $\eta_1$, qui est arbitraire. Je ne le présente pas comme plus réaliste. Il sert à mesurer une **sensibilité** : la conclusion « le rejet pur est fatal, la pénalité ne l'est pas » dépend de la façon de modéliser le filtre.

La proposition du manuscrit va dans le même sens. Avec la pénalité nulle ($C = 0$, arrêt sans réessai), $\pi_B(f) \to 1$, alors que sous A la part furtive a une limite strictement inférieure à 1 (§ 3.5). Le rejet pur n'est donc pas le seul cas « fatal ».

À cela s'ajoute qu'en $\eta = 0$, l'« enrichissement » sous A n'est que le conditionnement des sorties du modèle de base : rien n'a été appris. Le modèle ne distingue pas la politique apprise de la loi des sorties filtrées. Or c'est précisément l'objet de la question de Halberstadt. La phrase de la note « Halberstadt a mathématiquement raison » ne vaut que dans ce modèle.

### 3.2 « Hors boucle » ne veut pas dire « covariance négative ou nulle »

L'identité sous A dit que la survie à l'audit augmente de $\operatorname{Cov}(\beta_{\text{boucle}}, \beta_{\text{audit}})/\mathbb{E}\beta_{\text{boucle}}$. Tenir l'audit hors de la boucle **ne rend pas** cette covariance négative ou nulle : deux détecteurs qui lisent des traits voisins sont corrélés positivement.

Contre-exemple exact : $\beta_{\text{boucle}} \in \{1/10, 9/10\}$ et $\beta_{\text{audit}} \in \{2/10, 8/10\}$, sur deux atomes équiprobables. La survie à l'audit passe de $1/2$ à $37/50$, soit $+6/25$, alors que l'audit n'a jamais servi dans la boucle.

La phrase de la note (§ 4, Régime R2) — « garder un canal de détection strictement hors de la boucle annule exactement la pression sélective d'évasion contre ce canal » — est donc **fausse**. Le point 1 de la section 6 de la note (« hors boucle ($\operatorname{Cov}\le0$) ») confond la condition et le placement. Dans le manuscrit, le résumé et le titre de l'item du découplage (« sufficient condition … through strict off-loop informational decoupling ») induisent la même confusion.

**Le placement hors boucle n'est pas non plus nécessaire dans le modèle.** Mettons l'audit dans la boucle, combiné à un autre détecteur : $\beta_{\text{boucle}} = \beta_{\text{autre}}\cdot\beta_{\text{audit}}$, avec $\beta_{\text{audit}} = (1/2, 1)$ et $\beta_{\text{autre}} = (1, 1/10)$ sur deux atomes équiprobables. Sous A, la survie à l'audit passe de $0{,}75$ à $0{,}583$ : elle baisse. Ce qui compte, c'est le signe de la covariance, pas le placement.

### 3.3 Sous B, une covariance négative ou nulle est nécessaire, mais elle ne suffit pas

Écrivons $k = \eta(\Delta R + C)$.

- **Ce qui est nécessaire.** Sous B, la dérivée en $k = 0$ de la survie à l'audit vaut $\operatorname{Cov}_{\nu_0}(\beta_{\text{boucle}}, \beta_{\text{audit}})$. Pour que la survie n'augmente pour aucune valeur de $\eta$, il faut donc $\operatorname{Cov} \le 0$. La phrase du manuscrit (Limitations, point 2) et du billet (ligne 107), « R2 requires $\operatorname{Cov}\le 0$ », est correcte comme condition **nécessaire**.
- **Ce qui ne suffit pas.** Une covariance négative ou nulle ne suffit pas sous B. Contre-exemple : $\beta_{\text{boucle}} \in \{1/10, 1/2, 9/10\}$ et $\beta_{\text{audit}} \in \{9/10, 1/10, 9/10\}$, sur trois atomes équiprobables. La covariance exacte est nulle. Pourtant, avec $k = 4$, la survie à l'audit monte de $19/30$ à $0{,}7700$, soit $+0{,}137$. La raison : le poids $e^{ku}$ est convexe.
- **Ce qui est démontré.** La condition suffisante démontrée par le manuscrit est l'indépendance ou l'association négative. L'association négative suffit, mais elle n'est pas nécessaire : la contre-lecture a exhibé un couple sans dépendance négative par quadrants pour lequel la hausse reste nulle pour tout $k \in [0, 200]$.
- **Contrôle sain.** Sous indépendance exacte, l'écart mesuré est de $3\times10^{-81}$ sur 500 essais.

**Ce qui est faux dans les pièces**, c'est de présenter la covariance négative ou nulle comme **suffisante** :

- le billet v2, ligne 19 : « a sufficient condition via non-positive covariance » ;
- le résumé du manuscrit : « (non-positive covariance / negative association) », qui met les deux au même rang ;
- la section 6.1 de la note : « hors boucle ($\operatorname{Cov}\le0$) ».

### 3.4 La pénalité ne « se retourne » pas : dans la niche, elle rend aussi l'agent plus honnête

Dans la niche parfaitement furtive, la cote furtif sur honnête est **identique** sous A et sous B : elle vaut $p_f e^{\eta\Delta R}/p_h$. B ne fait qu'ôter davantage de masse à la triche visible, et cette masse se répartit entre l'honnête et le furtif dans la même proportion. Donc, **chaque fois que $\pi_B(f) > \pi_A(f)$, on a aussi $\pi_B(h) > \pi_A(h)$, et la masse tricheuse totale est plus faible sous B**. C'est le cas sur les 3 287 cas trouvés, sans exception. La table 3 le montre aussi : sous A, $\pi_A(h) = 0{,}8274$, et $\pi_B(h)$ égale cette valeur exactement au croisement $C = 0{,}2792$, puis la dépasse (jusqu'à $0{,}918$ en $C = 2{,}5$).

Les formules « negative penalties backfire harder than pure rejection » et « amplifies absolute stealth strictly more » sont vraies à la lettre, mais elles ne disent qu'une moitié. Si seule la triche furtive nuit au déploiement, « B est pire que A sur le furtif » reste la mesure pertinente. Mais B fait mieux que A sur l'honnêteté et sur la triche totale. Il faut dire les deux, pas seulement la première.

### 3.5 Le rejet pur « s'effondre vers la tricherie », pas forcément « vers la furtivité »

Sous A, quand $\eta \to \infty$, la part furtive tend vers $\beta_f p_f/(\beta_v p_v + \beta_f p_f) < 1$. Exemple exact : $p = (0{,}49 ; 0{,}5 ; 0{,}01)$ et $\beta = (1 ; 1/2 ; 3/5)$ donnent une limite de $3/128 \approx 2{,}3\,\%$, et la masse va presque toute à la **triche visible**, à $97{,}7\,\%$. La formule du résumé « pure rejection always collapses to stealth » est donc fausse en général. Le point 4a ne dit que « le furtif dépasse l'honnête ».

### 3.6 L'enrichissement conditionnel n'est « universel » que sous A

Sous B, avec des récompenses hétérogènes parmi les tricheurs, la survie moyenne des tricheurs peut **baisser**. Exemple : deux tricheurs de masses a priori égales, l'un de survie $0{,}5$ et de récompense $0{,}01$, l'autre de survie $0{,}9$ et de récompense $10$, avec $C = 0$ et $\eta = 0{,}3$. La survie moyenne passe de $0{,}8810$ à $0{,}8748$.

L'énoncé du théorème restreint correctement B au cas à deux strates de récompense égale. Le texte qui revendique l'enrichissement sous B sans cette réserve est le commentaire v2, ligne 9 : « Operator B likewise enriches stealth for all η>0, C≥0 ». C'est lui qu'il faut corriger. Le mot « universal » du résumé, rattaché à l'identité de variance, ne vise que A ; il faut le dire.

### 3.7 Les pièges plantés laissent passer les tricheurs peu fréquents

La remarque du manuscrit le reconnaît. Je le mesure par la meilleure politique sans contrainte de taux, calculée exactement : on triche partout où le gain par contexte est positif. Sur 3 000 instances avec $C > C^*$, cette politique a un gain **positif** dans 640 cas. Dans ces 640 cas :

- elle triche à un taux ordinaire $\tau_{\text{ord}} < \tau_{\min}$, hors du champ du théorème, comme il se doit ;
- dans 242 cas, ce taux est même au plus égal à la variation totale : ce sont de vraies attaques rares, concentrées là où $P_{\text{piège}}$ est faible.

Le régime des pièges ne garantit donc pas une politique honnête à l'équilibre de Gibbs. Il exclut seulement les tricheurs fréquents ($\tau_{\text{ord}} \ge \tau_{\min}$). Le seuil $\tau_{\min}$ atteignable tend vers $\delta_{\text{ind}}$ quand $C \to \infty$.

*Note de version.* Une version antérieure de ce rapport donnait « 294 instances » pour une politique qu'elle disait rare. C'était faux : la politique testée, $\mathbf 1\{P_{\text{ord}} > P_{\text{piège}}\}$, a toujours $\tau_{\text{ord}} \ge d_{VT}$. L'erreur a été relevée par la contre-lecture.

---

## 4. Antériorité et portée

Les références ci-dessous sont des **pistes à vérifier sur PDF (R7)**. Je ne les ai pas lues pendant cet audit, et aucun chiffre n'en est tiré.

- **Les identités centrales sont classiques.** La variation de la moyenne d'un trait sous sélection égale la covariance divisée par la moyenne de l'aptitude : c'est l'équation de Price (1970), l'identité de Robertson (1966), et l'identité de variance pour le trait « aptitude » elle-même, qui est le théorème fondamental de Fisher (1930). Le premier point du premier théorème et le régime de découplage sous A en sont des cas particuliers. Le manuscrit ne le dit pas.
- **Forme de Gibbs de l'apprentissage par renforcement régularisé par divergence KL, et filtrage vu comme conditionnement :** Korbak, Perez et Buckley (2022), « RL with KL penalties is better viewed as Bayesian inference » ; Rafailov et al. (2023).
- **Optimisation contre un moniteur et obscurcissement.** Baker et al. (2025, cité) ; Korbak et al. (2025, « Chain of Thought Monitorability »), qui recommandent déjà de ne pas entraîner contre le moniteur de chaîne de pensée ; Bailey et al. (2024, « Obfuscated activations ») ; Gupta et Jenner (2025, « RL-Obfuscation »). La « conséquence architecturale » de la note (garder les sondes hors boucle) est donc une recommandation **déjà publiée**, non une conséquence propre du théorème.
- **Goodhart et divergence KL :** Manheim et Garrabrant (2018) ; Kwa, Thomas et Garriga-Alonso (2024, « Catastrophic Goodhart »), qui étudient l'équilibre régularisé par divergence KL quand l'erreur de récompense est lourde.
- **Pièges et indiscernabilité entre test et déploiement :** Greenblatt et al. (2023, cité) ; Needham et al. (2025), sur la conscience d'évaluation.

**Ce que le résultat dit et ne dit pas des vrais modèles.** Il dit qu'**à l'équilibre statique de Gibbs, pour des strates fixées**, un filtre imparfait enrichit la part furtive parmi les tricheurs, et il donne des seuils exacts. Il ne dit rien de quatre choses : la dynamique finie du gradient ; la généralisation, c'est-à-dire si l'entraînement contre un détecteur apprend l'honnêteté ou le masquage (ici $p_f$ et $\beta_f$ sont exogènes et fixés) ; la manière dont $\beta_f$ se déforme avec l'apprentissage ; le cas $\beta_f > \beta_h$ (fausses alarmes sur l'honnête), exclu par hypothèse alors qu'il est réaliste.

**Règle anti-faux-gap (R8).** La vraie zone vierge est une question : *que devient $p_f$ et que devient $\beta_f$ quand on entraîne ?* C'est exactement la question de Halberstadt (« generalise instead »). Le modèle la tient pour donnée. La phrase du manuscrit est « This note resolves the question exactly at the standard KL-regularized (Gibbs) post-training equilibrium ». Elle porte sa réserve, mais elle reste une survente : la question posée par Halberstadt, celle de la généralisation, est hors de ce modèle.

---

## 5. Les contre-lectures antérieures, lues après mon examen

- **Contre-lecture Carbon** (`ae7ab7d1…`, portant sur la v1). Elle a vu à juste titre la survente d'exhaustivité, la référence au script interne, l'extrait Lean, les légendes arrondies et le plancher des attaques rares. Elle **n'a pas vu** les points 3.1 à 3.6, ni le caractère tautologique des essais. Elle affirme que les 14 citations sont « toutes vérifiées, réelles » : c'est invérifiable ici, et non opposable (R7). Sa propre reformulation, « éviter une évasion efficace exige de rompre l'une des deux inégalités », **garde une nécessité non démontrée**. Cette nécessité était déjà dans la v1 du manuscrit (« requires at least one of three exact conditions »). Carbon l'a seulement ramenée de trois à deux inégalités, et c'est sous cette forme qu'elle a été reprise dans la v2 du manuscrit et dans le billet. Son fichier compagnon `.sha256` porte un chemin de machine étrangère (`/home/antigravity/…`). L'empreinte concorde, mais le chemin est à nettoyer.
- **Avis d'opportunité** (`87ceee0b…`). Il parle encore de « classification exhaustive en 3 régimes » et de « zéro conjecture gonflée ». Les deux phrases sont contredites ici.
- **Note d'élucidation** (`bf9d442d…`). Elle garde « les trois seuls régimes », « caractérisation exhaustive et sans reste » et « caractérisation nécessaire et suffisante » pour le second théorème : ces trois phrases ne sont pas démontrées. S'y ajoutent l'erreur du § 3.2, le ratio de l'hypothèse sur la politique accessible encore écrit $C/(\Delta R + C)$ (Carbon avait relevé ce défaut, qui suppose $\beta_h = 1$ et $\delta_{\text{maint}} = 0$), et un extrait Lean non compilé, qui ne passerait probablement pas tel quel (`positivity` sans hypothèse $0 \le \beta_h$ ni $0 < \beta_f$ ; à confirmer avec Lean).

---

## 6. Liste fermée des corrections à faire avant diffusion

1. **Découplage.**
   - Ne plus écrire que garder l'audit hors boucle annule la pression sélective ou préserve l'audit.
   - Écrire à la place, pour A : « la survie à l'audit varie exactement de $\operatorname{Cov}_{\nu_0}/\mathbb{E}_{\nu_0}[\beta_{\text{boucle}}]$ ; elle n'augmente pas si et seulement si la covariance sous $\nu_0$ est négative ou nulle ; le placement hors boucle ne suffit pas » (§ 3.2).
   - Pour B : « une covariance négative ou nulle est nécessaire, mais elle ne suffit pas ; la condition suffisante démontrée est l'indépendance ou l'association négative » (§ 3.3).
   - Corriger dans ce sens la note (§ 4 et § 6.1), le résumé du manuscrit et le titre de son item sur le découplage, ainsi que le billet (ligne 19) et le commentaire.
2. **Le « dilemme ».** Dire que, dans la niche, B dépasse A en furtif exactement quand B dépasse A en honnêteté, à cote furtif sur honnête égale (§ 3.4). Garder « B est pire sur le furtif » seulement si l'on dit aussi « B est meilleur sur l'honnêteté et sur la triche totale ».
3. **« Collapses to stealth ».** Remplacer par « l'honnêteté s'effondre ; la masse va aux tricheurs, et la part furtive tend vers $\beta_f p_f/(\beta_v p_v+\beta_f p_f)$ » (§ 3.5).
4. **L'opérateur A est un choix de modèle.** Le déclarer comme tel, dire qu'il équivaut à une prime de $\eta^{-1}\log\beta$, et signaler que le rejet répété rend la barrière non évanescente (§ 3.1). Sans cela, la thèse « le rejet pur est fatal, la pénalité ne l'est pas » n'est pas défendable.
5. **Vérification.** Retirer « every theorem and numerical table is verified in exact rational arithmetic » et décrire les essais tels qu'ils sont (§ 2). L'annonce « 0 contre-exemple sur 14 000 » ne doit pas servir d'argument.
6. **Nécessité et exhaustivité.** Retirer « requires breaking one of two exact algebraic inequalities », « les trois seuls régimes », « exhaustive » et « nécessaire et suffisante » pour le second théorème pris dans son ensemble.
7. **« Universal ».** Restreindre ce mot à A, et corriger le commentaire v2, ligne 9, qui étend l'enrichissement à B sans la réserve de récompense égale (§ 3.6).
8. **Antériorité.** Citer Price, Robertson et Fisher pour les deux identités, et Korbak et al. (2022) pour la forme de Gibbs, après vérification sur PDF. Présenter la recommandation « sondes hors boucle » comme déjà publiée.
9. **Petits bords.** Dire que $p_f = 0$ est hors du domaine ; que le rapport des seuils de la proposition n'est pas défini si $p_h\beta_h = p_f\beta_f$ ; que $\pi_0(\mathcal S) > 0$ est requis ; et que le lien entre le régime des pièges et le ratio critique suppose $\beta_h = 1$.
10. **Hygiène.** Le script réécrit son JSON scellé quand on le lance à sa place : prévoir une sortie vers un autre dossier. Corriger aussi la formule de `c_seuil` dans `test_mort_halberstadt_v1.py`. Le compagnon `.sha256` de Carbon porte un chemin étranger. « Closed-form » ne convient pas au seuil d'amplification sous B, qui est implicite.

---

## 6 bis. Contre-lecture de ce rapport (règle R2)

Un sous-agent Opus neuf, qui n'a écrit ni le rapport ni les pièces, a relu ce rapport. Il a reproduit les deux JSON à l'empreinte près et relevé quinze défauts, dont quatre majeurs.

- **Signe erroné et nécessité fausse dans la correction 1.** Corrigé : nouveau § 6.1 et contre-exemple du placement en boucle au § 3.2.
- **Critique mal ciblée sous B.** Corrigé : § 3.3 réécrit. Une covariance négative ou nulle est nécessaire, et l'association négative est seulement suffisante.
- **Plancher des attaques rares décrit à l'inverse de ce qu'il mesure.** Corrigé : § 3.7 recalculé avec la meilleure politique sans contrainte de taux.
- **Classement incohérent au § 0.** Corrigé.

Les défauts mineurs ont été corrigés en place (§ 1.2, 1.3, 2, 3.1, 3.2, 3.4, 3.6, 4 et 5). Le même contre-lecteur a ensuite vérifié les corrections. Le verdict « tient avec réserves » est confirmé par le contre-lecteur.

---

## 7. Pièces versées (dossier `docs/notes/audit-evasion-post-entrainement-v1/`)

| Fichier | Rôle |
|---|---|
| `rapport-audit-evasion-post-entrainement-v1.md` et `.pdf` | Le présent rapport. |
| `verificateur_independant_evasion_v1.py` | Vérificateur indépendant : preuves symboliques, calcul exact, recherche adverse, programme linéaire, contre-exemples. |
| `resultats-verificateur-independant-v1.json` | Sortie, reproduite à l'identique sur deux exécutions. |
| `sortie-verificateur-independant-v1.txt` | Journal de la console. |
| `instrumenter_essais_v1.py` et `instrumentation-essais-v1.json` | Instrumentation des 14 000 essais, sans modifier le script audité. |

Chaque fichier a son compagnon `.sha256`. Relance :

```
python -I verificateur_independant_evasion_v1.py <main-v2.tex> <sortie.json>
python -I instrumenter_essais_v1.py <copie de verifier_exemples_papier_v2.py>
```

Environnement : Python 3.13.18, numpy 2.5.5, sympy 1.14.0, mpmath 1.3.0, scipy 1.18.1 (environnement virtuel du bloc-notes de session). Le script audité a été relancé avec l'interpréteur du système.
