### Cadre formel et séparation épistémique

Soit $\Gamma$ une grammaire formelle publique engendrant un langage $\mathcal{X} = L(\Gamma)$ (fini ou dénombrable), $G$ un générateur aléatoire boîte noire produisant une suite de tirages $(X_t)_{t \ge 1}$ dans $\mathcal{X}$, et $V : \mathcal{X} \to \{0,1\}$ un vérificateur indépendant testant l'appartenance à un ensemble cible $S \subseteq \mathcal{X}$. On note $p = \mathbb{P}(X_t \in S) \in [0,1]$ (inconnue) la fréquence marginale des objets valides, $c_g > 0$ le coût d'un tirage de $G$, $c_v > 0$ le coût d'un appel à $V$, $r = c_v / c_g$ leur rapport, et $B > 0$ le budget. Un algorithme $\mathcal{A}$ réalise $M$ tirages et $K$ appels à $V$ sur un sous-ensemble $\mathcal{Q}(\mathcal{A})$ d'objets, pour un coût total $C(\mathcal{A}) = M c_g + K c_v$ (hors éventuel coût auxiliaire $c_{\text{aux}}$). L'événement « au moins $k \ge 1$ objets valides distincts sont produits puis reconnus » s'écrit $E_k = \{|\{x \in \mathcal{Q}(\mathcal{A}) : x \in S \wedge V(x)=1\}| \ge k\}$.

**Séparation épistémique globale.** Dans ce qui suit, on sépare explicitement ce qui est **établi** (théorèmes, bornes prouvées et résultats publiés) de ce qui est **supposé** (choix de modélisation non imposés par l'énoncé : indépendance des tirages, exactitude déterministe de $V$, coût négligeable du calcul syntaxique sur $\Gamma$, existence d'un score auxiliaire, etc.).

---

### 1. Significations mathématiques d'une garantie dans un budget donné

**Établi (logique des quantificateurs).** Lorsque $p$ est inconnue, l'expression « garantir dans un budget $B$ » correspond à plusieurs énoncés mathématiques inéquivalents selon l'ordre des quantificateurs et la classe d'instances $\mathcal{H}$ contenant $\mathcal{I} = (\mu, V)$, où $\mu$ est la loi des tirages et $p(\mathcal{I}) = \mu(S)$.

1. **Garantie déterministe (pire cas absolu)** :
   $$\exists \mathcal{A},\; \forall \mathcal{I} \in \mathcal{H},\quad \mathbb{P}_{\mathcal{A},\mathcal{I}}\big(C(\mathcal{A}) \le B \;\wedge\; E_k\big) = 1.$$
   *Hypothèses* : $\mathcal{X}$ fini, $|S| \ge k$ garanti par $\mathcal{H}$, $V$ déterministe exact, $B \ge |\mathcal{X}| c_v$ (inaccessible par tirages aléatoires i.i.d. dès que $p < 1$).

2. **Garantie probabiliste uniforme sur une classe minorée ($\mathcal{H}_{p_{\min}} = \{\mathcal{I} : p(\mathcal{I}) \ge p_{\min}\}$, $p_{\min} > 0$ connu)** :
   $$\forall \delta \in (0,1),\; \forall p_{\min} \in (0,1],\; \exists B = B(p_{\min},\delta,k,c_g,c_v),\; \exists \mathcal{A},\; \forall \mathcal{I} \in \mathcal{H}_{p_{\min}},$$
   $$\mathbb{P}_{\mathcal{A},\mathcal{I}}\big(C(\mathcal{A}) \le B \;\wedge\; E_k\big) \ge 1 - \delta.$$
   Si l'on supprime $p_{\min}$ ($\mathcal{H}_{>0} = \{\mathcal{I} : p(\mathcal{I}) > 0\}$) tout en gardant $B$ indépendant de $\mathcal{I}$, l'énoncé devient faux (section 2.1).

3. **Garantie paramétrique à budget fixe (dépendante de $p$ inconnu)** :
   $$\exists \mathcal{A},\; \forall B > 0,\; \forall \mathcal{I} \in \mathcal{H},\quad C(\mathcal{A}) \le B \;\text{ p.s. et }\; \mathbb{P}_{\mathcal{A},\mathcal{I}}(E_k) \ge \phi\big(B, p(\mathcal{I}), k, c_g, c_v\big).$$
   L'algorithme ignore $p$, respecte un budget dur, et certifie une loi de rendement minimale $\phi$.

4. **Garantie disjonctive uniforme sur tout $p \in [0,1]$ (découverte OU certificat de rareté)** :
   $$\forall \delta \in (0,1),\; \forall B > 0,\; \exists \mathcal{A},\; \forall \mathcal{I} \in \mathcal{H}_{[0,1]},$$
   $$C(\mathcal{A}) \le B \;\text{ p.s. et }\; \mathbb{P}_{\mathcal{A},\mathcal{I}}\Big(E_k \;\vee\; \big\{p(\mathcal{I}) \le u(B,\delta,k)\big\}\Big) \ge 1 - \delta.$$
   C'est la forme maximale de garantie uniforme à budget fixe sans connaissance préalable sur $p$ (y compris $p=0$).

5. **Garantie adaptative à budget aléatoire (Las Vegas / confiance fixe)** :
   $$\forall \delta \in (0,1),\; \exists \mathcal{A},\; \forall \mathcal{I} \in \mathcal{H}_{>0},\quad \mathbb{P}_{\mathcal{A},\mathcal{I}}\Big(E_k \;\wedge\; C(\mathcal{A}) \le f\big(p(\mathcal{I}),\delta,k,c_g,c_v\big)\Big) \ge 1 - \delta,$$
   ou en espérance : $\mathbb{P}(E_k) = 1$ et $\mathbb{E}[C(\mathcal{A})] \le g(p(\mathcal{I}),k,c_g,c_v)$. Le budget n'est plus fixé *a priori* indépendamment de $p$.

6. **Garantie bayésienne ou en espérance** : moyenne sur une loi *a priori* $\Pi$ sur $\mathcal{H}$, $\mathbb{E}_{\mathcal{I}\sim\Pi}[\mathbb{P}_{\mathcal{A},\mathcal{I}}(C(\mathcal{A})\le B \wedge E_k)] \ge 1-\delta$ ; ou borne sur l'espérance du nombre d'objets reconnus $\mathbb{E}[N_{\text{val}}] \ge \psi(B,p)$, strictement plus faible qu'une borne en forte probabilité.

**Supposé (hypothèses à expliciter dans chaque énoncé).** L'énoncé initial laisse ouverts des points décisifs qu'il faut fixer dans $\mathcal{H}$ : (i) loi des tirages (i.i.d. vs corrélés/non stationnaires) ; (ii) fidélité de $V$ (exact déterministe : taux de faux positifs $\alpha = 0$ et de faux négatifs $\beta = 0$, ou bruité) ; (iii) sens de l'indépendance de $V$ (indépendant de $G$ et de l'historique conditionnellement à $x$) ; (iv) nature du budget (dur presque sûr $C \le B$ vs en espérance $\mathbb{E}[C] \le B$) ; (v) coût auxiliaire $c_{\text{aux}}$ du parsing, du hachage ou d'un pré-filtre sur $\Gamma$.

---

### 2. Résultats établis : négatifs et positifs

#### 2.1. Résultats négatifs (établis)

- **Impossibilité d'une garantie uniforme à budget fixe sur $\mathcal{H}_{>0}$ et borne inférieure minimax.** Par la méthode à deux points de Le Cam — Lucien Le Cam (1973), « Convergence of Estimates Under Dimensionality Restrictions », et Alexandre B. Tsybakov (2009), *Introduction to Nonparametric Estimation* —, la distance en variation totale entre $n$ tirages i.i.d. de Bernoulli de paramètre $0$ et de paramètre $p$ vaut $1 - (1-p)^n \le np$. Plus généralement, si $\mathcal{X}$ est infini (ou de cardinal $N > K_{\max} = \lfloor B/c_v \rfloor$) et si $\mathcal{H}$ autorise tout singleton $S = \{x^*\}$ sur un sous-ensemble $\mathcal{X}_0 \subseteq \mathcal{X}$ de taille $N$ muni de la loi uniforme $\mu$, tout algorithme $\mathcal{A}$ effectuant au plus $K_{\max}$ appels à $V$ satisfait $\mathbb{E}_{x^*}[\mathbb{P}(E_1)] \le K_{\max}/N = K_{\max} p$. En faisant $N \to \infty$, $\inf_{\mathcal{I}\in\mathcal{H}_{>0}} \mathbb{P}_{\mathcal{A},\mathcal{I}}(E_1) = 0$. Sur $\mathcal{H}_{p_{\min}}$ sans lien structurel entre syntaxe et $V$, obtenir $\mathbb{P}(E_1) \ge 1-\delta$ impose dans le pire cas $K \ge \frac{\ln(1/\delta)}{\ln(1/(1-p_{\min}))} = \Omega\!\left(\frac{\ln(1/\delta)}{p_{\min}}\right)$ vérifications. En domaine fini sous loi uniforme sur les fonctions cibles, David H. Wolpert et William G. Macready (1997), « No Free Lunch Theorems for Optimization », établissent de même qu'aucune heuristique de recherche sans remise ne domine en moyenne le tirage aléatoire.
- **Impossibilité d'accélération générique par apprentissage actif ou pré-filtrage.** Sanjoy Dasgupta (2005), « Coarse Sample Complexity Bounds for Active Learning », et Steve Hanneke (2014), « Theory of Disagreement-Based Active Learning », établissent que sans hypothèse structurelle (coefficient de désaccord fini), la recherche d'une région rare par requêtes adaptatives ne bat pas asymptotiquement $\Omega(1/p)$. De plus, dans le cadre PAC — Leslie G. Valiant (1984), « A Theory of the Learnable » ; Vladimir N. Vapnik et Alexey Ya. Chervonenkis (1971), « On the Uniform Convergence of Relative Frequencies of Events to Their Probabilities » —, un classifieur substitut d'erreur globale $\varepsilon \ge p$ peut être identiquement nul et manquer tous les positifs (rappel nul).
- **Limite sémantique de la grammaire publique.** D'après Henry G. Rice (1953), « Classes of Recursively Enumerable Sets and Their Decision Problems », si $L(\Gamma)$ encode un langage Turing-complet, aucune propriété sémantique non triviale n'est décidable par analyse statique de $\Gamma$ : connaître $\Gamma$ ne permet pas de remplacer $V$ en général.
- **Effondrement sous faux positifs de $V$.** Si $V$ possède un taux de faux positifs $\alpha > 0$ et de faux négatifs $\beta < 1$, la formule de Bayes donne $\mathbb{P}(X \in S \mid V(X)=1) = \frac{p(1-\beta)}{p(1-\beta)+(1-p)\alpha}$, qui tend vers $0$ lorsque $p \ll \alpha$ : une reconnaissance unique par $V$ ne garantit plus la validité réelle.

#### 2.2. Résultats positifs (méthodes avec garantie : énoncé, hypothèses, prix)

1. **Générer-et-vérifier direct (échantillonnage i.i.d.)**
   - *Références* : William Feller (1968), *An Introduction to Probability Theory and Its Applications* ; Herman Chernoff (1952), « A Measure of Asymptotic Efficiency for Tests of a Hypothesis Based on the sum of Observations » ; Wassily Hoeffding (1963), « Probability Inequalities for Sums of Bounded Random Variables » ; Stéphane Boucheron, Gábor Lugosi et Pascal Massart (2013), *Concentration Inequalities: A Nonasymptotic Theory of Independence* ; Charles J. Clopper et Egon S. Pearson (1934), « The Use of Confidence or Fiducial Limits Illustrated in the Case of the Binomial » ; Aaditya Ramdas, Peter Grünwald, Vladimir Vovk et Glenn Shafer (2023), « Game-Theoretic Statistics and Safe Anytime-Valid Inference ».
   - *Hypothèses* : tirages i.i.d. selon $\mu$, $V$ déterministe exact, $n = \lfloor B/(c_g+c_v) \rfloor$.
   - *Énoncé* : pour $k=1$, $\mathbb{P}(E_1) = 1 - (1-p)^n \ge 1 - e^{-np}$, d'où $\mathbb{P}(E_1) \ge 1-\delta$ sur $\mathcal{H}_{p_{\min}}$ dès que $n \ge \lceil \ln(1/\delta)/p_{\min} \rceil$. Pour $k \ge 1$ et $np > k$, la borne multiplicative de Chernoff donne $\mathbb{P}(E_k^c) \le \exp\!\left(-\frac{(np-k)^2}{2np}\right)$. Sans connaître $p$, Clopper et Pearson (1934) garantissent $\forall p \in [0,1]$, $\mathbb{P}(E_1 \vee \{p \le 1 - \delta^{1/n}\}) \ge 1-\delta$ (et son analogue exact pour tout $k \ge 1$ via la queue binomiale ; des bornes valides à tout temps d'arrêt sont établies par Ramdas et al., 2023).
   - *Prix* : budget dur $B = n(c_g+c_v) = \Theta\!\left(\frac{k+\ln(1/\delta)}{p_{\min}}(c_g+c_v)\right)$ ; en mode Las Vegas, coût espéré exact $\frac{k}{p}(c_g+c_v)$.

2. **Générer-et-vérifier avec déduplication / canonisation sur $\Gamma$**
   - *Références* : Irving J. Good (1953), « The Population Frequencies of Species and the Estimation of Population Parameters » ; David McAllester et Luis Ortiz (2003), « Concentration Inequalities for the Missing Mass and for Histogram Rule Error ».
   - *Hypothèses* : $V$ déterministe exact (ou invariant sous une relation d'équivalence syntaxique décidable sur $\Gamma$), coût de hachage négligeable devant $c_v$.
   - *Énoncé* : ne soumettre à $V$ que les objets jamais vérifiés conserve exactement $E_k$ sur $M$ tirages tout en n'appelant $V$ que $U_M \le M$ fois (nombre d'objets distincts). On obtient donc $\mathbb{P}_{\text{dédup}}(E_k) \ge \mathbb{P}_{\text{direct}}(E_k)$ à budget fixé, sans hypothèse supplémentaire sur $\mu$. Si aucun objet valide n'est trouvé parmi les $U_M$ vus, $p$ est majoré par la masse manquante $\sum_{x \notin \{X_1,\dots,X_M\}} \mu(x)$, dont McAllester et Ortiz (2003) prouvent une borne de concentration non asymptotique autour de l'estimateur de Good (1953).
   - *Prix* : $C = M c_g + U_M c_v \le B$ plus la mémoire en $O(U_M)$.

3. **Énumération ou échantillonnage sans remise sur $\Gamma$ (et portefeuille hybride)**
   - *Références* : Philippe Flajolet, Paul Zimmermann et Bernard Van Cutsem (1994), « A Calculus for the Random Generation of Labelled Combinatorial Structures » ; Philippe Duchon, Philippe Flajolet, Guy Louchard et Gilles Schaeffer (2004), « Boltzmann Samplers for the Random Generation of Combinatorial Structures ».
   - *Hypothèses* : tranche finie énumérable $\mathcal{X}_m \subseteq L(\Gamma)$ contenant au moins $k$ solutions, $V$ exact.
   - *Énoncé* : l'énumération exhaustive garantit $\mathbb{P}(E_k) = 1$ (même si $p=0$ sous $G$) dès que $B \ge |\mathcal{X}_m| c_v$. Le tirage uniforme sans remise sur $\mathcal{X}_m$ donne une garantie hypergéométrique strictement meilleure que l'i.i.d. de même fréquence. Allouer une fraction $\lambda \in (0,1)$ du budget à $G$ dédupliqué et $1-\lambda$ à $\Gamma$ conserve chacune des deux garanties au prix d'un facteur multiplicatif $1/\lambda$ ou $1/(1-\lambda)$ sur le budget.
   - *Prix* : $|\mathcal{X}_m| c_v$ au pire ; impraticable dès que $|\mathcal{X}_m| \gg B/c_v$.

4. **Estimation adaptative et tests séquentiels optimaux**
   - *Références* : Abraham Wald (1945), « Sequential Tests of Statistical Hypotheses » ; Paul Dagum, Richard Karp, Michael Luby et Sheldon Ross (2000), « An Optimal Algorithm for Monte Carlo Estimation ».
   - *Hypothèses* : tirages i.i.d., $V$ exact, temps d'arrêt adaptatif (budget aléatoire).
   - *Énoncé* : Dagum, Karp, Luby et Ross (2000) estiment $p$ à erreur relative $\varepsilon$ près avec probabilité $\ge 1-\delta$ sans connaître $p$, en prouvant l'optimalité jusqu'à une constante de la complexité $O\!\left(\frac{\ln(1/\delta)}{\varepsilon^2 p}\right)$. Le test SPRT de Wald (1945) décide entre $p \le p_0$ et $p \ge p_1$ en minimisant le nombre espéré d'appels sous $p_0$ et $p_1$ ; appliqué à des appels répétés de $V$ sur un même objet, il certifie aussi la décision face à un vérificateur bruité ($\alpha < 1-\beta$).
   - *Prix* : $O\!\left(\frac{\ln(1/\delta)}{\varepsilon^2 p}(c_g+c_v)\right)$ en espérance/forte probabilité ; ne lève pas l'impossibilité à budget fixe.

5. **Redémarrages universels pour générateurs avec état corrélé**
   - *Référence* : Michael Luby, Alistair Sinclair et David Zuckerman (1993), « Optimal Speedup of Las Vegas Algorithms ».
   - *Hypothèses* : possibilité de réinitialiser indépendamment le générateur sur une loi de temps d'atteinte inconnue.
   - *Énoncé* : la séquence universelle de seuils $(1, 1, 2, 1, 1, 2, 4, \dots)$ garantit un coût espéré $O(\ell^* \log \ell^*)$ où $\ell^*$ est le coût espéré optimal en connaissant la loi.
   - *Prix* : surcoût logarithmique $O(\log \ell^*)$ ; exige l'opération de réinitialisation.

6. **Filtrage calibré à risque contrôlé et inférence assistée**
   - *Références* : Jerzy Neyman et Egon S. Pearson (1933), « On the Problem of the Most Efficient Tests of Statistical Hypotheses » ; Vladimir Vovk, Alex Gammerman et Glenn Shafer (2005), *Algorithmic Learning in a Random World* ; Stephen Bates, Anastasios Angelopoulos, Lihua Lei, Jitendra Malik et Michael Jordan (2021), « Distribution-Free, Risk-Controlling Prediction Sets » ; Anastasios N. Angelopoulos, Stephen Bates, Clara Fannjiang, Michael I. Jordan et Tijana Zrnic (2023), « Prediction-Powered Inference ».
   - *Hypothèses* : score auxiliaire bon marché $s : \mathcal{X} \to \mathbb{R}$ fixé indépendamment, tirages échangeables, et jeu de calibration vérifié par $V$ (pour contrôler le risque conditionnel, ce qui suppose d'y observer des positifs).
   - *Énoncé* : un filtre $F = \{s(x) \ge \tau\}$ de sélectivité $q = \mathbb{P}(X \in F)$ et de rappel $r_{\text{rec}} = \mathbb{P}(X \in F \mid V(X)=1)$ induit (par l'identité de Wald, 1945, à coût de filtrage négligeable) un coût espéré par succès $\frac{c_g + q c_v}{p \, r_{\text{rec}}}$ ; Neyman et Pearson (1933) caractérisent le seuil optimal lorsque les lois conditionnelles sont connues. Sans connaître les lois, Bates et al. (2021) garantissent le contrôle fini du risque du filtre avec probabilité $\ge 1-\delta$ à partir d'un jeu de calibration échangeable, et Angelopoulos et al. (2023) fournissent des intervalles valides sur $p$ à variance réduite.
   - *Prix* : coût de calibration ($\Omega(1/p)$ vérifications pour borner un rappel rare sans information *a priori*), coût d'évaluation de $s$, et perte totale de garantie si $r_{\text{rec}} = 0$.

7. **Allocation adaptative entre plusieurs générateurs ou strates**
   - *Références* : Tze Leung Lai et Herbert Robbins (1985), « Asymptotically Efficient Adaptive Allocation Rules » ; Donald A. Berry, Robert W. Chen, Alan Zame, David C. Heath et Larry A. Shepp (1997), « Bandit Problems with Infinitely Many Arms » ; Jean-Yves Audibert, Sébastien Bubeck et Rémi Munos (2010), « Best Arm Identification in Multi-Armed Bandits ».
   - *Hypothèses* : accès à $J$ générateurs (ou sous-grammaires) interrogeables indépendamment, ou réservoir infini de bras.
   - *Énoncé* : identification du meilleur générateur à probabilité d'erreur exponentiellement décroissante en le budget divisé par la complexité des écarts (Audibert, Bubeck & Munos, 2010), ou compromis optimal exploration/exploitation en infinité de bras (Berry et al., 1997).
   - *Prix* : coût d'exploration croissant avec $J$ et l'inverse des écarts ; inapplicable à un unique générateur indivisible.

---

### 3. Dépendance aux quatre paramètres structurels

**3.1. Ce que l'on sait du générateur $G$.**
*Établi* : en boîte noire pure sans minorant $p_{\min}$, l'échantillonnage préférentiel — Herman Kahn et Andy W. Marshall (1953), « Methods of Reducing Sample Size in Monte Carlo Computations » ; Art B. Owen (2013), *Monte Carlo Theory, Methods and Examples* — et la méthode d'entropie croisée — Reuven Y. Rubinstein (1999), « The Cross-Entropy Method for Combinatorial and Continuous Optimization » — sont inapplicables faute d'accès aux densités $\mu(x)$ ou aux paramètres. La connaissance de $p_{\min} > 0$ fait basculer de la garantie disjonctive à la garantie uniforme à budget fixe. L'accès « boîte grise » (probabilités, redémarrages, paramètres modifiables) ouvre les redémarrages universels (Luby, Sinclair & Zuckerman, 1993), le recalibrage adaptatif ou l'allocation multi-bras. *Supposé* : si $G$ a une faible entropie mais intersecte $S$, la déduplication compense les collisions ; si $S$ est hors de son support effectif, aucune stratégie sur $G$ seul ne réussit.

**3.2. Taille et structure de la grammaire $\Gamma$.**
*Établi* : lorsque $|\mathcal{X}| \le B/c_v$ (ou sur une tranche finie $\mathcal{X}_m$ contenant $S$), l'énumération sur $\Gamma$ rend $G$ superflu et offre une garantie déterministe. Si une sous-grammaire nécessaire $\Gamma' \subseteq \Gamma$ telle que $S \subseteq L(\Gamma')$ est prouvée, le rejet syntaxique gratuit garantit $r_{\text{rec}} = 1$ et divise les appels à $V$ par $1/\mu(L(\Gamma'))$. Lorsque $|\mathcal{X}| \gg B/c_v$ (ou infini), la grammaire ne peut plus remplacer $G$ et sert principalement à la canonisation/déduplication ; pour une grammaire Turing-complète, Rice (1953) exclut tout pré-filtre sémantique exact universel.

**3.3. Corrélation entre tirages.**
*Établi* : pour des événements $E^{(t)} = \{V(X_t)=1\}$ de même probabilité $p > 0$ et de corrélations de paires $\rho_{ij} = \operatorname{Corr}(\mathbf{1}_{E^{(i)}}, \mathbf{1}_{E^{(j)}})$, l'inégalité de Kai Lai Chung et Paul Erdős (1952), « On the Application of the Borel-Cantelli Lemma », donne :
$$\mathbb{P}\!\left(\bigcup_{t=1}^n E^{(t)}\right) \ge \frac{np}{1 + (n-1)p + (1-p)\,\frac{1}{n}\sum_{i \neq j} \rho_{ij}}.$$
Une **corrélation positive** ($\rho_{ij} > 0$ : effondrement de mode, chaîne lente, graine commune) augmente le dénominateur et dégrade la probabilité d'atteinte, jusqu'à la réduire à $p$ indépendamment de $n$ si $\rho_{ij} = 1$. Pour une chaîne de Markov ergodique, les bornes de concentration se dégradent proportionnellement au temps de mélange ou à l'inverse du trou spectral — Pascal Lezaud (1998), « Chernoff-type Bound for Finite Markov Chains » ; David A. Levin, Yuval Peres et Elizabeth L. Wilmer (2009), *Markov Chains and Mixing Times* ; Daniel Paulin (2015), « Concentration Inequalities for Markov Chains by Marton Couplings and Spectral Methods ». À l'inverse, une **corrélation négative** ($\rho_{ij} < 0$ : tirage sans remise, diversification, processus ponctuels déterminantaux — Alex Kulesza et Ben Taskar, 2012, *Determinantal Point Processes for Machine Learning*) améliore strictement la garantie par rapport à l'i.i.d. *Supposé* : sur un générateur strictement boîte noire, on ne peut pas forcer $\rho_{ij} < 0$ au tirage, seulement éviter de payer $c_v$ sur les doublons.

**3.4. Rapport $r = c_v / c_g$ entre vérification et production.**
*Établi* : lorsque $r \ll 1$, le coût est dominé par $M c_g$ : il est optimal de vérifier chaque tirage, et le filtrage n'apporte aucun gain significatif. Lorsque $r \gg 1$, le budget autorise bien plus de tirages ($B/c_g$) que de vérifications ($B/c_v$). Un filtre de sélectivité $q$ et de rappel $r_{\text{rec}}$ (à coût négligeable devant $c_g$) abaisse strictement le coût espéré par succès si et seulement si
$$r_{\text{rec}} > \frac{c_g + q c_v}{c_g + c_v} = \frac{1 + q r}{1 + r}.$$
Quand $r \to 0$, ce seuil tend vers $1$ (aucun filtre imparfait n'est rentable) ; quand $r \to \infty$, il tend vers $q$ (tout enrichissement $r_{\text{rec}}/q > 1$ devient rentable, sous réserve de ne pas saturer le budget en génération). Enfin, même un filtre **parfait** ($r_{\text{rec}}=1, q=p$) conserve un coût espéré incompressible de $c_g/p + c_v$, limitant le gain maximal sur la vérification directe à un facteur $\frac{1+r}{1+pr} \le 1+r$ : aucun filtrage ne compense un $p$ trop petit devant $c_g/B$.

---

### 4. Garanties apportées par les méthodes répandues

- **Best-of-$N$ vérifié (et estimation `pass@k`)** — Mark Chen et al. (2021), « Evaluating Large Language Models Trained on Code » : *Établi* : sous i.i.d. et $V$ exact, apporte la garantie paramétrique $1-(1-p)^N$ et le certificat disjonctif de Clopper et Pearson (1934) ; l'estimateur $1-\binom{n-c}{k}/\binom{n}{k}$ est sans biais pour la probabilité de succès en $k$ essais. Aucune garantie uniforme si $p$ est sans minorant.
- **Vote majoritaire / auto-cohérence (*self-consistency*)** — Nicolas de Condorcet (1785), *Essai sur l'application de l'analyse à la probabilité des décisions rendues à la pluralité des voix* ; Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery et Denny Zhou (2023), « Self-Consistency Improves Chain of Thought Reasoning in Language Models » : *Établi* : le théorème de Condorcet (1785) ne garantit la convergence vers la bonne réponse que sous indépendance (ou faible corrélation) et dominance de la bonne réponse ($p > 1/2$ en binaire, ou mode unique valide). Si $p$ est faible et qu'une erreur fréquente domine, le vote converge vers l'erreur : aucune garantie générale, et risque de perte de rappel s'il filtre l'entrée de $V$.
- **Reranking par modèle de récompense / cascades** — Paul Viola et Michael Jones (2001), « Rapid Object Detection using a Boosted Cascade of Simple Features » ; Charlie Snell, Jaehoon Lee, Kelvin Xu et Aviral Kumar (2024), « Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters » : *Établi* : méthodes empiriques sans garantie distribution-free en l'absence de calibration vérifiée (Vovk, Gammerman & Shafer, 2005 ; Bates et al., 2021) ; sujettes au décalage de distribution et au rappel nul sur les objets rares.
- **MCMC, recuit simulé, recherche locale, évolutionnaire, MCTS** — Nicholas Metropolis, Arianna W. Rosenbluth, Marshall N. Rosenbluth, Augusta H. Teller et Edward Teller (1953), « Equation of State Calculations by Fast Computing Machines » ; W. Keith Hastings (1970), « Monte Carlo Sampling Methods Using Markov Chains and Their Applications » : *Établi* : inapplicables directement à un $G$ purement boîte noire ; sur $\Gamma$, la convergence asymptotique ne donne aucune garantie de temps d'atteinte en budget fini sans borne sur le trou spectral (Levin, Peres & Wilmer, 2009) ni hypothèse de régularité contournant Wolpert et Macready (1997).
- **Déduplication et pré-filtrage syntaxique nécessaire** : *Établi* : garantie exacte de non-régression (dominance stochastique) sous $V$ déterministe et $S \subseteq L(\Gamma')$. En revanche, modifier la loi interne d'un générateur par décodage contraint sans renormalisation exacte peut biaiser $\mu$ et ne bénéficie pas de cette garantie.
- **Apprentissage actif et renforcement (RL) guidé par $V$** — Richard S. Sutton et Andrew G. Barto (2018), *Reinforcement Learning: An Introduction* : *Établi* : le RL est inapplicable si $G$ n'est pas modifiable ; même si $G$ l'est, avant le premier succès (récompense creuse), la borne $\Omega(1/p)$ demeure. L'apprentissage actif n'offre de garantie de gain que sous hypothèses structurelles (Hanneke, 2014), nulles au pire cas rare (Dasgupta, 2005).
- **Portefeuille hybride (fraction $\lambda$ en vérification directe dédupliquée, $1-\lambda$ en heuristique)** : *Établi* : conserve rigoureusement la garantie de l'échantillonnage direct au budget effectif $\lambda B$ tout en exploitant les gains éventuels de l'heuristique.

---

### 5. Preuves, observations et expériences permettant de trancher

**5.1. Ce qu'une preuve mathématique tranche définitivement (indépendamment de l'expérience).**
Une preuve tranche déjà (i) l'impossibilité d'une garantie uniforme à budget fixe sur $\mathcal{H}_{>0}$, (ii) la dominance de la déduplication sous $V$ déterministe, (iii) la borne disjonctive de Clopper–Pearson, (iv) la condition exacte de rentabilité d'un filtre $r_{\text{rec}} > (1+qr)/(1+r)$ et le plancher $c_g/p+c_v$. Sur un problème concret, une preuve portant sur $(\Gamma, S)$ peut aussi trancher l'existence d'une sous-grammaire nécessaire $\Gamma'$, la finitude de $|\mathcal{X}_m| \le B/c_v$ (rendant l'énumération optimale), ou l'indécidabilité d'un pré-filtre exact (Rice, 1953).

**5.2. Observations et expériences contrôlées tranchant entre les régimes sur un système réel $(G,V,\Gamma)$.**
Pour décider quelle hypothèse est satisfaite et quelle garantie s'applique en pratique, cinq protocoles diagnostiques sont décisifs :

1. **Mesure des collisions et de la masse manquante (sans appeler $V$, puis sur pilote vérifié)** : générer $M_0$ tirages pour observer $U_{M_0}/M_0$ et le nombre de singletons (Good, 1953 ; McAllester & Ortiz, 2003), puis vérifier un échantillon pilote (ou exécuter un SPRT de Wald, 1945). *Décision* : un fort taux de collisions combiné à $r \gg 1$ quantifie le gain immédiat de la déduplication ; une masse manquante bornée faible après vérification sans succès certifie l'échec de $G$ et impose de recourir à $\Gamma$ ; zéro succès en $K_0$ vérifications borne $p \le 1 - \delta^{1/K_0}$ et tranche si $B$ est insuffisant en régime direct.
2. **Test d'autocorrélation et de variance par blocs sur $(X_t, V(X_t))$** : comparer la variance empirique par blocs à la variance binomiale et estimer $\hat{\rho}_h$. *Décision* : une autocorrélation positive significative invalide les bornes i.i.d. (Clopper–Pearson, Chernoff) et impose redémarrages (Luby, Sinclair & Zuckerman, 1993) ou bornes markoviennes (Paulin, 2015).
3. **Étalonnage d'un filtre $s$ et test du mode sur échantillon pilote aléatoire non filtré** : estimer sur des tirages vérifiés indépendants de l'entraînement la courbe $(q(\tau), r_{\text{rec}}(\tau))$ avec intervalles de confiance finis (Clopper & Pearson, 1934 ; Bates et al., 2021), et vérifier la validité du mode majoritaire. *Décision* : le filtrage n'est validé que si la borne inférieure de confiance sur $r_{\text{rec}}(\tau)$ dépasse $\frac{1+q(\tau)r}{1+r}$ ; l'échec du mode alors que des tirages minoritaires réussissent réfute l'hypothèse de Condorcet.
4. **Audit de déterminisme et de taux d'erreur $(\alpha, \beta)$ de $V$** : soumettre des objets identiques de façon répétée à $V$ et tester $V$ sur des cas témoins certifiés. *Décision* : un non-déterminisme invalide la déduplication sans ré-interrogation ; un $\alpha$ non négligeable devant $\hat{p}$ invalide la reconnaissance en un seul appel et impose la répétition (Wald, 1945 ; Hoeffding, 1963).
5. **Test de corrélation entre distance grammaticale sur $\Gamma$ et succès $V$** : appliquer des perturbations syntaxiques locales à partir d'objets tirés et tester l'enrichissement local. *Décision* : l'absence d'enrichissement confirme le régime sans structure où la recherche locale n'a pas de fondement ; un enrichissement fort justifie un portefeuille combinant recherche locale et filet de sécurité direct.

---

### Synthèse épistémique

- **Ce qui est établi** : aucune garantie uniforme à budget fixe n'existe sur $p \in (0,1]$ sans hypothèse supplémentaire ; les seules garanties rigoureuses sans connaître $p$ à budget fixe sont la garantie disjonctive (découverte ou borne supérieure sur $p$) et, si $|\mathcal{X}| \le B/c_v$, l'énumération sur $\Gamma$ ; la déduplication domine sans surcoût d'hypothèse sous $V$ déterministe ; le gain d'un filtre est gouverné par $r_{\text{rec}} > (1+qr)/(1+r)$ et borné par $1+r$ ; la corrélation positive dégrade les garanties i.i.d. ; la majorité des heuristiques répandues (vote majoritaire, reranking non calibré, recherche locale) n'apportent aucune garantie en régime rare sans hypothèses additionnelles.
- **Ce qui reste supposé (dépendant de l'instance réelle)** : l'exactitude et le déterminisme effectifs de $V$, l'indépendance ou le bon mélange des tirages de $G$, l'ordre de grandeur réel de $p$ et de $r = c_v/c_g$, le caractère négligeable du coût syntaxique, et l'existence d'un signal auxiliaire réellement corrélé à $S$ sur la distribution de $G$ — points que seules les preuves spécifiques à $(\Gamma,S)$ et les expériences de la section 5 peuvent trancher.

FIN DE LA RÉPONSE