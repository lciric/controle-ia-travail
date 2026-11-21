Intégrité des pièces (Règle 2) : les blocs `FAITS`, `QUESTION DE L'ARBITRE` et les quatre pièces `E3-T1-conception-A`, `E3-T1-conception-B`, `E3-T1-conception-D` et `E3-T1-conception-E` sont reçus complets, sans coupure ni omission (`OBSERVÉ-NON-AUDITÉ` sur la non-corruption des chaînes).

---

## Sur la proposition A

### (a) Défauts de méthode : variables confondantes, vrai par construction, fuites entre construction et évaluation

1. **Vrai par construction et inversion du sens de la borne entre P2 et D4 (`VÉRIFIÉ` mathématiquement ; `HYPOTHÈSE` sur l'erreur de modélisation de A).**
   Dans P2, A définit le résultat de la tâche comme une fonction déterministe mesurable $Y = f(X)$ de la transcription $X$, puis pose par hypothèse que le sabotage déplace la loi de $Y$ d'au moins $\delta$ en variation totale : $d_{\text{TV}}(P_Y, Q_Y) \ge \delta$. Par l'inégalité de traitement des données (*data processing inequality*, `VÉRIFIÉ`), $d_{\text{TV}}(P_X, Q_X) \ge d_{\text{TV}}(f_\# P_X, f_\# Q_X) \ge \delta$ est **vrai par construction** en une ligne pour toute fonction mesurable $f$. Plus gravement, dans le duel D4, A instancie cette borne inférieure sur la distance entre transcriptions comme un **plafond** supérieur qu'aucune sonde linéaire sur les états internes $Z$ ne devrait dépasser (« plafond strictement inférieur à 1 et aucune sonde mesurée ne la dépasse »). Or :
   - une borne inférieure $d_{\text{TV}}(P_X, Q_X) \ge \delta$ borne inférieurement la puissance du meilleur test sur $X$, elle ne plafonne pas supérieurement une sonde ;
   - les états internes $Z$ (lus par les sondes linéaires, `RAPPORTÉ`) se situent *en amont* de la transcription $X$ dans la chaîne de Markov $Z \to X \to Y$. Par traitement des données, $d_{\text{TV}}(P_Z, Q_Z) \ge d_{\text{TV}}(P_X, Q_X) \ge \delta$ (`VÉRIFIÉ`). Une sonde lisant $Z$ peut donc séparer honnête et saboteur avec une puissance supérieure à tout détecteur ne lisant que $X$, sans qu'aucune hypothèse sur $X \to Y$ ne soit violée.

2. **Variables confondues dans le duel D1 (organisme entier contre meilleure lignée seule).**
   D1 compare l'organisme à cinq lignées (`RAPPORTÉ`) contre une seule lignée à budget égal sur des résultats publiés après une date $T$. Trois variables sont confondues :
   - la **diversité inter-lignées** ($L = 5$ modèles distincts contre $L = 1$, `RAPPORTÉ`) ;
   - l'**architecture de mémoire négative** (« un mort reste mort », portier et rejeu des témoins de P4, `RAPPORTÉ`) ;
   - l'**hétérogénéité des dates de coupure d'entraînement** $T_1, \dots, T_5$ des cinq lignées (`HYPOTHÈSE`). Si $\max_{\ell \in \{1..5\}} T_\ell > T$, le gain de l'organisme mesure la contamination d'une lignée postérieure à $T$ et non la synergie collective.

3. **Fuite entre construction et évaluation dans P1 (atlas des petits cas $k \in \{2, 3\}$ [illustratif]).**
   Dans P1, A tabule pour $k$ fixé la pire puissance d'un agrégateur monotone par programmation linéaire sur la classe de Fréchet en fonction des marginales $(\alpha, \beta)$, fait conjecturer une forme close sur un sous-ensemble d'instances $(\alpha_i, \beta_i)$, et la teste sur des instances tenues à l'écart. Pour $k$ fixé, la fonction valeur optimale d'un programme linéaire paramétré par le second membre $(\alpha, \beta)$ est **affine par morceaux** sur un nombre fini de chambres polyédriques déterminées par les bases duales optimales (`VÉRIFIÉ`). Tirer l'échantillon de construction et l'échantillon d'évaluation dans le même simplexe à $k \in \{2, 3\}$ [illustratif] fixe fait fuir la géométrie des chambres de dimension $k$ dans le test : on évalue une interpolation affine locale à $k$ constant, jamais la généralisation en $k$.

4. **Fuite d'instrument dans D2 (suite bon marché contre Lean sur mutants).**
   D2 sélectionne des paires « théorème vrai / mutant à une hypothèse retirée, témoin connu ». Si le témoin connu qui sert à certifier que le mutant est faux provient de la banque d'énumération à petit support (§2 de A), qui est elle-même le moteur de la « suite bon marché » (`RAPPORTÉ`), le banc d'évaluation partage par construction l'espace d'états de l'un des deux instruments comparés (`HYPOTHÈSE`).

### (b) Conditions mesurables de perte de puissance ou de non-jugeabilité (lois, paramètres, estimateurs)

- **D1 — Estimateur d'écart de redécouverte $\hat{\Delta}_M = \sum_{i=1}^M (Y_{i,1} - Y_{i,0})$ sur $M = 20$ cibles [illustratif] au seuil $c = 2$ [illustratif] :**
  Soit $(Y_{i,1}, Y_{i,0}) \in \{0,1\}^2$ le couple d'indicateurs de succès de l'organisme et de la lignée seule sur la cible $i$, de loi jointe multinomiale de paramètres discordants $\pi_{10} = \mathbb{P}(Y_{i,1}=1, Y_{i,0}=0)$ et $\pi_{01} = \mathbb{P}(Y_{i,1}=0, Y_{i,0}=1)$, avec corrélation intra-classe $\rho = \text{Corr}(Y_{i,d}, Y_{j,d}) \ge 0$ et paramètre de contamination $\lambda_\ell = \mathbb{P}(i \in \text{Corpus}_\ell \mid t_i > T)$.
  1. Conditionnellement au nombre de paires discordantes $D = \sum_{i=1}^M \mathbb{I}(Y_{i,1} \neq Y_{i,0}) = m$, la variable $K_{10} = \sum_{i=1}^M \mathbb{I}(Y_{i,1}=1, Y_{i,0}=0)$ suit une loi binomiale $\text{Bin}\!\left(m, \frac{\pi_{10}}{\pi_{10}+\pi_{01}}\right)$ et $\hat{\Delta}_M = 2 K_{10} - m$.
  2. Sous $H_B$ ($\pi_{10} = \pi_{01} = \pi$), dès que $2 M \pi \ge 4$ [illustratif] (soit $m = 4$ discordances [illustratif]), $\mathbb{P}_{H_B}(\hat{\Delta}_M \ge 2 \mid D = 4) = \sum_{k=3}^4 \binom{4}{k} 2^{-4} = 0{,}3125$ [illustratif] (taux de fausse alerte $> 31\%$ [illustratif]).
  3. Sous $H_A$ avec $\pi_{10} - \pi_{01} = \theta = 0{,}10$ [illustratif] et $\pi_{01} = 0{,}05$ [illustratif] ($\rho = 0$), $\mathbb{E}[\hat{\Delta}_{20}] = 2$ [illustratif] et $\mathbb{P}_{H_A}(\hat{\Delta}_{20} < 2) = 0{,}456$ [illustratif] (perte de puissance $> 45\%$ [illustratif]).
  4. Si $\max_{\ell \le 5} \lambda_\ell - \lambda_{\text{seul}} \ge \frac{c}{M} = 0{,}10$ [illustratif], le biais de l'estimateur vérifie $\mathbb{E}_{H_B}[\hat{\Delta}_M] \ge c$ et $\theta = \pi_{10} - \pi_{01}$ devient non identifiable.

- **D2 — Estimateur de filtrage différentiel $\hat{p}_{10} = \frac{1}{n}\sum_{i=1}^n \mathbb{I}(L_i = 1, C_i = 0)$ sur $n = 10$ mutants [illustratif] au seuil $n\hat{p}_{10} \ge 1$ [illustratif] :**
  Soit $(L_i, C_i) \in \{0,1\}^2$ de loi multinomiale de paramètre $p_{10} = \mathbb{P}(L_i=1, C_i=0)$ sur les mutants, et soient $q_L, q_C \in [0,1]$ les probabilités de rejet à tort d'un énoncé vrai par Lean et par la suite bon marché.
  1. $n\hat{p}_{10} \sim \text{Bin}(n, p_{10})$. Pour $n = 10$ [illustratif] et $p_{10} = 0{,}08$ [illustratif], $\mathbb{P}(n\hat{p}_{10} = 0) = (1 - 0{,}08)^{10} = 0{,}434$ [illustratif] (perte de puissance de $43{,}4\%$ [illustratif]).
  2. Si le taux de faux rejets sur les originaux vrais $\hat{q}_L = \frac{1}{n}\sum_{i=1}^n \mathbb{I}(L'_i = 1)$ a pour paramètre $q_L \ge p_{10}$, l'estimateur d'avantage net $\hat{p}_{10} - \hat{q}_L$ a une espérance négative ou nulle et le critère perd toute séparabilité.

- **D3 — Estimateur de puissance à fausse alerte fixée $\hat{\beta}_n(\alpha) = \frac{1}{n_1}\sum_{j=1}^{n_1} \mathbb{I}(S_{1,j} > \hat{\tau}_\alpha)$ où $\hat{\tau}_\alpha = S_{0,(\lceil(1-\alpha)n_0\rceil)}$ :**
  Soient $S_{0,1}, \dots, S_{0,n_0} \stackrel{\text{i.i.d.}}{\sim} F_0$ les scores sur $n_0$ énoncés réellement nouveaux post-$T$, et $S_{1,1}, \dots, S_{1,n_1} \stackrel{\text{i.i.d.}}{\sim} F_1$ les scores sur $n_1 = 40$ énoncés connus (`RAPPORTÉ`).
  1. La couverture réelle du seuil empirique $U = 1 - F_0(\hat{\tau}_\alpha)$ suit une loi Bêta $\text{Beta}(n_0 - r + 1, r)$ où $r = \lceil(1-\alpha)n_0\rceil$.
  2. Dès que $n_0 < \frac{1}{\alpha}$ (par exemple pour $\alpha = 0{,}01$ [illustratif] et $n_0 = 40$ [illustratif]), $r = n_0$, $\mathbb{E}[U] = \frac{1}{n_0 + 1} = 0{,}0244 > \alpha$ [illustratif] et $\text{Var}(U) \asymp n_0^{-2}$ : le niveau $\alpha$ est non estimable non paramétriquement, et la différence $\hat{\beta}_{\text{juge}}(\alpha) - \hat{\beta}_{\text{voisins}}(\alpha)$ a une variance dominée par le saut de statistique d'ordre $\text{Var}(\hat{\tau}_\alpha) \asymp \frac{\alpha(1-\alpha)}{n_0 f_0(F_0^{-1}(1-\alpha))^2}$.

- **D4 — Estimateur empirique d'avantage de sonde linéaire $\hat{\gamma}_n = \sup_{w \in \mathbb{R}^d, \tau \in \mathbb{R}} |\hat{P}_{Z,n}(w^\top Z > \tau) - \hat{Q}_{Z,n}(w^\top Z > \tau)|$ face à $\hat{\delta}_n = \frac{1}{2}\sum_{y \in \mathcal{Y}} |\hat{P}_{Y,n}(y) - \hat{Q}_{Y,n}(y)|$ :**
  Soient $Z \in \mathbb{R}^d$ les activations de dimension $d$ sous les lois $P_Z, Q_Z$ (taille d'échantillon $n$) et $Y \in \mathcal{Y}$ de cardinal $K = |\mathcal{Y}|$. La classe des demi-espaces de $\mathbb{R}^d$ a une dimension de Vapnik-Chervonenkis $V = d + 1$.
  1. Sous l'égalité stricte $P_Z = Q_Z$, l'espérance de l'estimateur empirique vérifie $\mathbb{E}[\hat{\gamma}_n] \ge c_1 \sqrt{\frac{d+1}{n}}$ pour $n \ge d+1$ et $\hat{\gamma}_n = 1$ presque sûrement dès que $2n \le d+1$ (pulvérisation linéaire en grande dimension).
  2. Pour $\hat{\delta}_n$, sous $P_Y = Q_Y$ uniforme sur $K$ valeurs, $\mathbb{E}[\hat{\delta}_n] \asymp \sqrt{\frac{K}{n}}$. Le critère D4 devient non jugeable dès que $\sqrt{\frac{d+1}{n}} \ge 1 - \delta$ ou $\sqrt{\frac{K}{n}} \ge \delta$.

- **P1 — Valeur minimax sur la classe de Fréchet $V_k(g; \alpha, \beta) = \inf_{\nu \in \Gamma(\beta_1,\dots,\beta_k)} \mathbb{E}_\nu[g(X)]$ sous la contrainte $\sup_{\mu \in \Gamma(\alpha_1,\dots,\alpha_k)} \mathbb{E}_\mu[g(X)] \le \alpha_{\text{tot}}$ :**
  Soient $X = (X_1, \dots, X_k) \in \{0,1\}^k$, $\alpha_j = \alpha$, $\beta_j = \beta$ et $g : \{0,1\}^k \to \{0,1\}$ croissante. Par les bornes de Fréchet-Hoeffding $\sup_{\mu \in \Gamma(\alpha)} \mathbb{P}_\mu(\max_j X_j = 1) = \min(1, k\alpha)$ et $\inf_{\nu \in \Gamma(\beta)} \mathbb{P}_\nu(\min_j X_j = 1) = \max(0, k\beta - (k-1))$, dès que les paramètres satisfont $\alpha_{\text{tot}} < \alpha$ (aucun moniteur seul n'est admissible) et $k\beta \le k-1$, toute fonction booléenne déterministe $g$ vérifie $\sup_\mu \mathbb{E}_\mu[g] \in \{0, \alpha, 2\alpha, \dots, \min(1, k\alpha)\}$ : l'ensemble réalisable est réduit à $g \equiv 0$, de puissance $V_k = 0$ identiquement sur tout l'atlas.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Dans D1 : contrôle à lignée unique multi-échantillonnée avec mémoire des témoins active.**
   Opposer $H_A$ (la diversité des cinq lignées crée le gain) à $H_B$ (seul l'échantillonnage répété filtré par la mémoire des témoins crée le gain) en exécutant cinq instances indépendantes de la meilleure lignée seule connectées au même portier et à la même banque de témoins P4. Sans ce contrôle, tout gain de la mémoire P4 est faussement attribué à la pluralité des lignées.
2. **Dans P1 : contrôle d'extrapolation en dimension $k' > k$ hors simplexe d'entraînement.**
   Entraîner le générateur de conjectures sur $k \in \{2, 3\}$ [illustratif] et évaluer uniquement sur $k \in \{4, 5\}$ [illustratif], accompagné d'un contrôle à fonction objectif aléatoire non structurée où aucune forme close en $k$ n'existe.
3. **Dans D4 : contrôle de sabotage interne orthogonal à la sortie ($\delta_Y = 0, \delta_Z > 0$).**
   Planter un agent qui modifie ses activations $Z$ dans le noyau de la couche de sortie ($P_Y = Q_Y$ donc $\delta = 0$, mais $d_{\text{TV}}(P_Z, Q_Z) = 1$ [illustratif]). La permutation d'étiquettes proposée par A annule simultanément $\delta_Y$ et $\delta_Z$ et ne détecte pas la confusion entre divergence interne et divergence de sortie.

---

## Sur la proposition B

### (a) Défauts de méthode : variables confondantes, vrai par construction, fuites entre construction et évaluation

1. **Écart strictement positif vrai par construction dans P2 (biais de discrétisation pris pour une découverte).**
   Dans P2, B discrétise les lois marginales continues des $k$ moniteurs sur une grille finie de taille $m$, résout le programme linéaire multi-marginal en arithmétique rationnelle exacte, et conclut à un régime nouveau ($H_B$ validée) dès qu'il existe un « écart strictement positif, certifié en rationnel exact. Pas de tolérance flottante » avec les bornes analytiques continues de Vovk-Wang ou de Rüschendorf. Or les bornes de Vovk-Wang et de Rüschendorf sont des infima/suprema pris sur l'ensemble $\mathcal{P}([0,1]^k)$ de **toutes les copules continues** à marginales uniformes (`VÉRIFIÉ`). Restreindre la loi jointe à une grille discrète à $m$ atomes restreint le polytope des couplages accessibles à l'adversaire ; le minimum sur ce sous-polytope discret est donc **strictement supérieur à la borne continue d'un terme de discrétisation d'ordre $\mathcal{O}(1/m)$** dès que la copule extrémale continue n'est pas concentrée sur les nœuds rationnels $\frac{1}{m}\mathbb{Z}^k$ (`VÉRIFIÉ`). Avec un seuil fixé à $\Delta_{\mathbb{Q}} > 0$, $H_B$ est vraie par construction sur toute grille finie : B confond l'erreur de quadrature de Riemann avec un théorème nouveau.

2. **Prémisse mathématiquement fausse et degrés de liberté non bornés dans P3 (sondes linéaires et moments d'ordre $\le 2$).**
   - B affirme dans $H_A$ de P3 que l'« appariement des moments d'ordre $\le 2$ [...] rend toute sonde linéaire aveugle par construction ». C'est mathématiquement faux pour l'avantage de classification linéaire $\sup_{w,\tau} |P(w^\top Z > \tau) - Q(w^\top Z > \tau)|$ (`VÉRIFIÉ` : deux lois sur $\mathbb{R}$ de moyenne $0$ et de variance $1$, par exemple $\frac{1}{2}\delta_{-1} + \frac{1}{2}\delta_{+1}$ et une loi asymétrique à trois atomes de mêmes moments d'ordre $1$ et $2$, sont séparées par un seuil linéaire $z > \tau$ avec un avantage strictement positif ; l'égalité des deux premiers moments n'aveugle que le discriminant quadratique/linéaire au sens des moindres carrés $L^2$, pas le classifieur à seuil !).
   - De plus, dans P3, le générateur produit des paires de lois d'activations $(P_Z, Q_Z)$ maximisant $\delta - \lambda \varepsilon$, où $\delta$ est la différence sur la « sortie de la tâche ». Si l'application de sortie $Y = g(Z)$ n'est pas fixée linéairement d'avance, il suffit que la sortie dépende de $\|Z\|_2^2$ ou d'une coordonnée de parité pour obtenir $\delta = 1$ [illustratif] et $\varepsilon = 0$ [illustratif] trivialement par construction (deux sphères concentriques ou le problème XOR en dimension $2$ [illustratif]).

3. **Fuite de mémoire préalable dans P4 (banc de dérive d'énoncé).**
   Dans P4, B applique des mutations syntaxiques aux quarante énoncés connus du juge de nouveauté (`RAPPORTÉ`) et compare la détection du juge automatique par retraduction à celle d'un mathématicien humain. Or les quarante énoncés sont des théorèmes classiques connus (`RAPPORTÉ`). Un mathématicien qui lit l'inégalité de Ville ou de Le Cam avec un signe $<$ inversé en $>$ détecte le mutant parce qu'il **connaît déjà le théorème classique par cœur**, sans même comparer l'énoncé formel à une spécification informelle (`HYPOTHÈSE`). Lorsqu'il devra auditer un théorème réellement inédit (où le sens de l'inégalité ou la nécessité d'une hypothèse est a priori inconnu), cet oracle mémoriel disparaît : l'évaluation de l'instrument humain en P4 fuit par la notoriété du corpus de test.

### (b) Conditions mesurables de perte de puissance ou de non-jugeabilité (lois, paramètres, estimateurs)

- **P2 — Estimateur d'écart rationnel discrétisé $\hat{\Delta}_m = V_{\text{LP}}^{(m)}(k, \alpha) - V_{\text{continu}}(k, \alpha)$ au seuil $\hat{\Delta}_m > 0$ :**
  Soit $\pi^* \in \Gamma(F_1, \dots, F_k)$ la copule adverse optimale continue sur $[0,1]^k$ et soit $\Gamma_m \subset \Gamma$ le polytope des couplages supportés sur la grille $\mathcal{G}_m = \{0, \frac{1}{m}, \dots, 1\}^k$.
  1. Pour toute fonction de coût d'agrégateur à variation bornée ou associée à un ensemble de rejet de périmètre fini $\operatorname{Per}(\mathcal{R}) = \mathcal{H}^{k-1}(\partial \mathcal{R}) > 0$, la projection de Wasserstein $W_1(\pi^*, \Gamma_m) \asymp \frac{\sqrt{k}}{m}$ induit sous $H_A$ ($V_{\text{LP}}^{(\infty)} = V_{\text{continu}}$) un biais déterministe :
     $$0 < c_1 \frac{\operatorname{Per}(\mathcal{R})}{m} \le \hat{\Delta}_m \le c_2 \frac{k}{m}$$
     dès que $\operatorname{supp}(\pi^*) \not\subset \mathcal{G}_m$.
  2. Le test $\mathbb{I}(\hat{\Delta}_m > 0)$ a donc une probabilité de fausse alerte $\mathbb{P}_{H_A}(\hat{\Delta}_m > 0) = 1$ pour tout paramètre de discrétisation fini $m < \infty$.

- **P3 — Estimateur scalaire pénalisé $\hat{S}_\lambda(P,Q) = \delta(P,Q) - \lambda \varepsilon(P,Q)$ sur des lois discrètes à $s$ atomes dans $\mathbb{R}^d$ :**
  Soient $P = \sum_{i=1}^s p_i \delta_{z_i}$ et $Q = \sum_{i=1}^s q_i \delta_{z_i}$ deux lois sur un support commun de cardinal $s$ dans $\mathbb{R}^d$, $\varepsilon(P,Q) = \sup_{w \in \mathbb{S}^{d-1}, \tau \in \mathbb{R}} |P(w^\top Z > \tau) - Q(w^\top Z > \tau)|$ et $\delta(P,Q) = d_{\text{TV}}(g_\# P, g_\# Q)$.
  1. Par le théorème de Radon (`VÉRIFIÉ`), si la taille du support discret vérifie $s \le d + 1$ et que les atomes $\{z_1, \dots, z_s\}$ sont en position générale dans $\mathbb{R}^d$, toute partition binaire du support est linéairement séparable par un hyperplan : on a alors $\varepsilon(P,Q) = d_{\text{TV}}(P,Q) \ge \delta(P,Q)$, de sorte que $\frac{\delta(P,Q)}{\varepsilon(P,Q)} \le 1$ identiquement (perte totale de puissance pour $s \le d+1$).
  2. Soit $\delta^*(\varepsilon) = \sup \{ \delta(P,Q) : \varepsilon(P,Q) \le \varepsilon \}$ la frontière de Pareto. L'optimiseur lagrangien $\sup_{P,Q} (\delta - \lambda \varepsilon)$ ne peut atteindre que l'enveloppe concave supérieure de $\delta^*(\varepsilon)$ aux points où $\lambda \in \partial \delta^*(\varepsilon)$. Si $\delta^*(\varepsilon)$ est strictement convexe sur $(0, \varepsilon_{\max})$, pour toute valeur du paramètre $\lambda > 0$, la loi optimale dégénère aux extrémités $\varepsilon = 0$ ou $\varepsilon = \varepsilon_{\max}$, rendant le régime intermédiaire $(\varepsilon > 0, \delta/\varepsilon > c)$ inobservable.

- **P4 — Estimateur du taux d'échappement de mutants $\hat{q}_n = \frac{1}{n}\sum_{i=1}^n \mathbb{I}(J_i = 0 \mid H_i = 1)$ au seuil $\hat{q}_n \le \frac{1}{20} = 0{,}05$ [illustratif] :**
  Soit $n \hat{q}_n \sim \text{Bin}(n, q)$ où $q = \mathbb{P}(J=0 \mid H=1)$ est la probabilité qu'un mutant sémantique échappe au juge de retraduction.
  1. Sur un lot de taille $n = 20$ mutants [illustratif] (ou $n = 45$ correspondant aux $40 + 5$ énoncés, `RAPPORTÉ` pour $40$), sous l'hypothèse de danger $H_B$ avec un taux réel d'échappement deux fois supérieur au seuil, $q = 0{,}10$ [illustratif], la probabilité d'accepter à tort l'allègement de la relecture humaine est :
     $$\mathbb{P}_{q=0{,}10}(\hat{q}_{20} \le 0{,}05) = (0{,}90)^{20} + 20(0{,}10)(0{,}90)^{19} = 0{,}3917 \text{ [illustratif]}$$
     et pour $n = 45$ [illustratif] au seuil $\hat{q}_{45} \le 0{,}05$ ($\le 2$ erreurs [illustratif]), $\mathbb{P}_{q=0{,}10}(n\hat{q}_{45} \le 2) = 0{,}163$ [illustratif].
  2. Pour garantir à la fois $\mathbb{P}_{q \ge 0{,}10}(\hat{q}_n \le 0{,}05) \le 0{,}05$ [illustratif] et $\mathbb{P}_{q \le 0{,}02}(\hat{q}_n > 0{,}05) \le 0{,}05$ [illustratif], la taille d'échantillon minimale requise par la loi binomiale est $n \ge 160$ mutants indépendants [illustratif].

- **P5 — Estimateur de richesse de classes de contre-exemples $\hat{C}_N = \sum_{c=1}^C \mathbb{I}(N_c \ge 1)$ sur $N$ morts archivées :**
  Soit $(N_1, \dots, N_C) \sim \text{Multinomiale}(N; p_1, \dots, p_C)$ le vecteur d'effectifs des $C$ classes d'équivalence de contre-exemples dans la mémoire des tentatives.
  1. $\mathbb{E}[\hat{C}_N] = C - \sum_{c=1}^C (1 - p_c)^N$. Lorsque la loi d'échantillonnage des proposeurs suit une loi de Zipf $p_c = \frac{c^{-\gamma}}{\sum_{j=1}^C j^{-\gamma}}$ avec paramètre $\gamma > 1$, $\mathbb{E}[\hat{C}_N] \asymp N^{1/\gamma}$ dépend du budget d'appels $N$ et non d'une borne finie intrinsèque tant que $N < C^\gamma$. Sans normalisation par $N$ et estimation du nombre de singletons $f_1 = \sum_{c=1}^C \mathbb{I}(N_c = 1)$ (estimateur de Turing-Good $\hat{p}_{\text{non-vu}} = f_1 / N$), le seuil sur $\hat{C}_N$ confond le volume d'appels $N$ avec la diversité structurelle $\gamma$.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Dans P2 : contrôle de convergence asymptotique multi-grilles $m \in \{2^2, 2^3, 2^4, 2^5\}$ [illustratif] sur un cas continu à égalité analytique prouvée.**
   Opposer $H_A$ ($\hat{\Delta}_m = \mathcal{O}(m^{-1}) \to 0$, pur artefact de discrétisation) à $H_B$ ($\liminf_{m \to \infty} \hat{\Delta}_m \ge \delta_0 > 0$, écart réel de puissance) en exigeant l'extrapolation de Richardson sur au moins quatre tailles de grille emboîtées.
2. **Dans P3 : contrôle à fonction de lecture de tâche $Y = g(Z)$ linéaire scellée et contrôle d'appariement de moments d'ordre $r \ge 3$ par programmation linéaire.**
   Sceller la projection de tâche $g$ avant la recherche, et opposer la boucle LLM à un simple solveur LP maximisant $|P(w_0^\top Z > \tau_0) - Q(w_0^\top Z > \tau_0)|$ sous contraintes d'égalité des moments polynomiaux de degré $\le r$.
3. **Dans P4 : contrôle sur énoncés synthétiques inédits inconnus du relecteur humain.**
   Inclure des lemmes synthétiques vrais et leurs mutants qui n'existent dans aucun manuel afin de mesurer le taux de détection humain hors mémoire encyclopédique.

---

## Sur la proposition D

### (a) Défauts de méthode : variables confondantes, vrai par construction, fuites entre construction et évaluation

1. **Fuite circulaire entre le pré-étiquetage du dénominateur et l'énumération canonique dans `D-valeur` (`VÉRIFIÉ` structurellement).**
   D pose comme convention générale (§6) : « Pour chaque instrument : cible positive pré-étiquetée, taux de détection = cibles signalées / cibles présentes [...] Pour un proposeur, "signaler" signifie *livrer un objet accepté* ». Puis, dans `D-valeur`, D oppose la recherche guidée par modèle à l'« énumération canonique à même temps total » sur une famille réservée de jeux finis.
   - Or, comment la famille réservée a-t-elle pu être **pré-étiquetée** avec l'ensemble exact des « cibles présentes » (les jeux et historiques présentant une perte stricte de valeur $V_{\text{full}}(s_0) > V_{\text{stat}}(s_0)$ non équivalente) sinon en ayant **déjà résolu exhaustivement la famille réservée par énumération canonique et récurrence rétrograde exacte** lors de la construction du banc ?
   - Si la famille réservée est assez petite pour que son dénominateur exact de séparations non équivalentes soit pré-calculé par l'arbitre, l'énumération canonique la résout à $100\%$ [illustratif] ; si elle est trop grande pour l'énumération canonique, le dénominateur « cibles présentes » est inconnu et le taux de détection défini par D est incalculable.
   - De plus, comme seules les séparations vérifiées par le calcul exact de récurrence ($V_{\text{full}}(s_0) > V_{\text{stat}}(s_0)$) sont acceptées comme livrables, le taux de fausses alertes (« fausses séparations ») vaut **$0 / N_0 = 0$ par construction** pour les deux méthodes dès que le filtre exact de valeur est inclus dans la boucle.

2. **Règle de décision composite à marge nulle ($\hat{D}_1 > \hat{D}_0 \land \hat{F}_1 \le \hat{F}_0$) biaisée contre l'égalité des taux de fausses alertes.**
   Dans tous ses duels instrumentaux et de découverte, D définit $H_A$ par la conjonction empirique stricte « détection strictement supérieure au contrôle mécanique sans hausse des fausses alertes » ($\hat{D}_1 > \hat{D}_0$ et $\hat{F}_1 \le \hat{F}_0$) sur un lot fini scellé, et affirme : « Le franchissement du seuil falsifie $H_B$, son absence falsifie $H_A$ sur le lot ». En confondant le paramètre d'espérance ($F_1 \le F_0$) avec l'estimateur empirique à marge nulle ($\hat{F}_1 \le \hat{F}_0$), toute fluctuation aléatoire d'une seule fausse alerte discordante ($\hat{F}_1 = \hat{F}_0 + 1/N_0$) falsifie $H_A$, même lorsque l'instrument a exactement le même taux théorique de fausses alertes que la référence ($F_1 = F_0 > 0$).

3. **Confusion entre sous-ensemble irréductible d'un arbre fini et validité séquentielle dans `D-frontière`.**
   Dans `D-frontière`, extraire sur un arbre fini de profondeur $T_0$ un sous-ensemble minimal de contraintes linéaires maintenant la valeur du programme linéaire sous le seuil $\alpha$ est un problème classique d'extraction de système irréductiblement consistant (dual d'un *Minimal Unsatisfiable Subset*, `VÉRIFIÉ`). Comparer la conjecture LLM à une « suppression systématique de contraintes avec le même solveur » confond l'heuristique d'ordonnancement des suppressions sur un LP fixe de taille finie avec la validité mathématique hors de l'arbre $T_0$.

### (b) Conditions mesurables de perte de puissance ou de non-jugeabilité (lois, paramètres, estimateurs)

- **Critère composite universel de D — Couple d'estimateurs $(\hat{D}_1 - \hat{D}_0, \hat{F}_1 - \hat{F}_0)$ sur $N_1$ cibles positives et $N_0$ témoins honnêtes :**
  Soient $(X_{i,1}, X_{i,0}) \in \{0,1\}^2$ ($i = 1, \dots, N_1$) les indicateurs de détection de la méthode $1$ et de la référence $0$, de probabilités discordantes $p_{10} = \mathbb{P}(X_1=1, X_0=0)$ et $p_{01} = \mathbb{P}(X_1=0, X_0=1)$ ; et soient $(Y_{j,1}, Y_{j,0}) \in \{0,1\}^2$ ($j = 1, \dots, N_0$) les indicateurs de fausse alerte sur les témoins honnêtes, de probabilités discordantes $q_{10} = \mathbb{P}(Y_1=1, Y_0=0)$ et $q_{01} = \mathbb{P}(Y_1=0, Y_0=1)$, supposés indépendants des cibles positives. L'événement de rejet de $H_B$ est :
  $$\mathcal{E} = \left\{ \sum_{i=1}^{N_1} (X_{i,1} - X_{i,0}) \ge 1 \right\} \cap \left\{ \sum_{j=1}^{N_0} (Y_{j,1} - Y_{j,0}) \le 0 \right\}$$
  1. **Plafond de puissance sous égalité des fausses alertes ($q_{10} = q_{01} = q > 0$) :** Conditionnellement au nombre de fausses alertes discordantes $M_0 = \sum_{j=1}^{N_0} \mathbb{I}(Y_{j,1} \neq Y_{j,0}) = m_0 \ge 1$, la variable $K_0 = \sum_{j=1}^{N_0} \mathbb{I}(Y_{j,1}=1, Y_{j,0}=0)$ suit $\text{Bin}(m_0, 1/2)$, d'où :
     $$\mathbb{P}(\hat{F}_1 \le \hat{F}_0 \mid M_0 = m_0) = \mathbb{P}\!\left(K_0 \le \lfloor m_0/2 \rfloor\right) = \frac{1}{2} + \frac{\mathbb{I}(m_0 \text{ pair})}{2^{m_0+1}} \binom{m_0}{m_0/2}$$
     Lorsque $N_0 q \to \infty$, $\mathbb{P}(\hat{F}_1 \le \hat{F}_0) \to \frac{1}{2}$. Même si la méthode $1$ a une puissance de détection parfaite ($p_{10} = 1, p_{01} = 0$, donc $\mathbb{P}(\hat{D}_1 > \hat{D}_0) = 1$), **la puissance du test de D est plafonnée asymptotiquement à $\frac{1}{2}$** (au moins $50\%$ [illustratif] de probabilité de falsifier $H_A$ à tort).
  2. **Inflation de fausse alerte sous l'hypothèse nulle stricte ($p_{10} = p_{01} = p > 0$ et $q_{10} = q_{01} = q > 0$) :** Lorsque $N_1 p \to \infty$ et $N_0 q \to \infty$, par théorème central limite bivarié :
     $$\lim_{N_1, N_0 \to \infty} \mathbb{P}_{H_B}(\mathcal{E}) = \frac{1}{2} \times \frac{1}{2} = \frac{1}{4} \text{ ($25\%$ [illustratif] de rejet à tort de $H_B$)}$$

- **`D-valeur` — Estimateur de perte exacte de valeur $\Delta V(s_0) = V_{\text{full}}(s_0) - V_{\text{stat}}(s_0)$ sur arbre de jeu d'horizon $T$ :**
  Soit un jeu d'audit fini à facteur de branchement d'observations $b$, espace d'actions $A$ et horizon $T$. L'arbre des historiques complets possède $|\mathcal{H}_T| = (|A|b)^T$ nœuds.
  1. Sous un budget de temps de calcul $\tau_{\max}$, la récurrence exacte sur $\mathcal{H}_T$ termine si et seulement si $T \le T_{\max}(\tau_{\max}) = \left\lfloor \frac{\log(c \tau_{\max})}{\log(|A|b)} \right\rfloor$.
  2. Pour tout jeu de paramètre $T > T_{\max}(\tau_{\max})$, le vérificateur exact de $\Delta V(s_0)$ ne termine pas ($\hat{D}_1 = \hat{D}_0 = 0$) ; pour $T \le T_{\max}(\tau_{\max})$, l'énumération des états atteignables est polynomiale en $|\mathcal{H}_T| \le c\tau_{\max}$, réduisant la fenêtre de séparation $\{ \tau_{\text{récurrence}}(T) \le \tau_{\max} < \tau_{\text{énum}}(T) \}$ à un domaine de mesure nulle dès que l'énumération canonique élimine les symétries par bisimulation d'état.

- **`D-frontière` — Valeur optimale du programme linéaire sur arbre $V^*_{\text{LP}}(\mathcal{C}', T_0) = \max_{p \in \Delta(b^{T_0})} \{ \sum_{\ell \in \mathcal{L}_{\text{seuil}}} p_\ell : A_{\mathcal{C}'} p \le d_{\mathcal{C}'} \}$ :**
  Soit un processus séquentiel à incréments bornés dans $[-\sigma, \sigma]$ et un seuil d'alerte $u > 0$.
  1. Par arithmétique de support, pour tout horizon d'arbre fini $T_0 < T_{\text{crit}} = \lceil u / \sigma \rceil$, l'ensemble des feuilles franchissant le seuil $u$ est vide ($\mathcal{L}_{\text{seuil}}(T_0) = \emptyset$), de sorte que $V^*_{\text{LP}}(\mathcal{C}', T_0) = 0 \le \alpha$ **pour tout sous-ensemble de contraintes $\mathcal{C}' \subseteq \mathcal{C}$, même $\mathcal{C}' = \emptyset$**.
  2. Plus généralement, si une contrainte de martingale $c \in \mathcal{C}$ contrôle la dérive maximale $\mu \le \mu_0$, son retrait produit une violation $V^*_{\text{LP}}(\mathcal{C} \setminus \{c\}, T) > \alpha$ uniquement pour $T \ge T_{\text{crit}}(\alpha, \mu, \sigma)$. Dès que $b^{T_{\text{crit}}(\alpha, \mu, \sigma)}$ excède la capacité mémoire du solveur LP rationnel, la probabilité qu'une frontière fausse (invalide pour $T \ge T_{\text{crit}}$) soit certifiée valide sur l'arbre $T_0 < T_{\text{crit}}$ vaut $1$.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Sur la règle de décision de tous les duels de D : contrôle blanc $A/A$ (la référence mécanique comparée à elle-même avec deux graines aléatoires indépendantes).**
   Opposer $H_A$ (la règle $\hat{D}_1 > \hat{D}_0 \land \hat{F}_1 \le \hat{F}_0$ contrôle le taux de fausse découverte sous un seuil $\alpha_0 \le 0{,}05$ [illustratif]) à $H_B$ (la règle génère $\approx 25\%$ [illustratif] de fausses victoires dès que $p, q > 0$) en confrontant deux exécutions indépendantes du même instrument de référence.
2. **Dans `D-valeur` : contrôle de divergence d'actions optimales à perte de valeur nulle ($\Delta V(s_0) = 0$).**
   Planter des jeux où deux historiques de même statistique résumée admettent des ensembles d'actions optimales disjoints ou décalés sur des états de probabilité d'atteinte nulle, ou par bris d'égalité entre deux actions de même valeur $Q^*(h, a_1) = Q^*(h, a_2)$, pour vérifier qu'aucun test local de politique ne contourne l'exigence de perte stricte depuis $s_0$.
3. **Dans `D-frontière` : contrôle de contraintes à rupture différée au-delà de l'horizon de l'arbre ($T_{\text{rupture}} = T_0 + 2$ [illustratif]).**
   Planter des garanties fausses qui sont mathématiquement vraies pour tout $T \le T_0$ mais fausses à $T_0 + 2$ [illustratif], afin de falsifier toute extrapolation d'un certificat d'arbre fini sans invariant d'induction en $T$.

---

## Sur la proposition E

### (a) Défauts de méthode : variables confondantes, vrai par construction, fuites entre construction et évaluation

1. **Dégénérescence duale en programmation linéaire et non-unicité de $y^*(m)$ dans M1 et E2 (`VÉRIFIÉ` mathématiquement).**
   Dans M1 (DSCPD) et E2, E résout pour $m \in \{2, \dots, 12\}$ [illustratif] un programme linéaire ou semi-défini en rationnels exacts, extrait **le** vecteur dual optimal $y^*(m) \in \mathbb{Q}^{k(m)}$, et demande aux modèles d'interpoler la formule analytique de $y^*(n, d)$ en fonction de la taille.
   - Or, dans les problèmes minimax d'indiscernabilité, de distance en variation totale, de couplage de Fréchet et de jeux d'audit symétriques, le polytope primal est hautement dégénéré (invariance par permutation des moniteurs ou des coordonnées). Par dualité linéaire, une dégénérescence du sommet primal implique que **la face duale optimale $\mathcal{F}^*_m$ n'est pas un point unique mais un polytope convexe de dimension strictement positive** (`VÉRIFIÉ`).
   - À chaque taille $m \in \{2, \dots, 12\}$ [illustratif], un solveur simplexe rationnel renvoie un sommet extrême arbitraire de $\mathcal{F}^*_m$ qui dépend de l'ordre des pivots. La suite $m \mapsto y^*(m)$ saute donc aléatoirement d'un sommet de la face duale à un autre d'un $m$ au suivant : elle n'est l'évaluation d'aucune fonction algébrique lisse, même lorsqu'une formule duale analytique simple existe à l'intérieur de $\mathcal{F}^*_m$ !
   - En outre, dans M1, vérifier dans Lean `Fintype` l'inégalité algébrique $A^\top y^*(n, d) \ge c$ prouve seulement la **faisabilité duale** (borne valide par dualité faible, vraie par construction dès que l'inégalité compile, `VÉRIFIÉ`), mais ne prouve jamais que la borne est serrée ni nouvelle si le témoin primal $(P_0^*, P_1^*)(n, d)$ n'est pas simultanément formalisé.

2. **Fuite adaptative de la banque scellée de traces honnêtes dans M2 (co-évolution Lakatosienne CLHV).**
   Dans M2, sur $40$ rondes [illustratif], les agents raffineurs proposent à chaque ronde une hypothèse $h_{t+1}$ éliminant le contre-exemple $c_t^*$, et le système retient $h_{t+1}$ si elle est « satisfaite empiriquement par $\ge 90\%$ [illustratif] d'une banque scellée de traces de jumeaux honnêtes ».
   - Dès que le verdict de ce filtre ($\ge 90\%$ [illustratif] sur la banque) guide la sélection évolutionnaire pendant $40$ rondes [illustratif] à raison de plusieurs candidats par ronde, la banque de traces honnêtes n'est plus un instrument d'évaluation scellé : elle devient **l'échantillon d'entraînement d'une boucle d'analyse de données adaptative** (le phénomène même d'usure d'archive par requêtes répétées que E décrit pourtant en §1.1 !). La co-évolution apprend l'enveloppe convexe empirique des $n_{\text{tr}}$ traces de la banque.
   - Par ailleurs, si une hypothèse $h_T$ est violée par $10\%$ [illustratif] des traces honnêtes ($1 - 0{,}90 = 0{,}10$ [illustratif]) et que le moniteur déclenche une alerte hors de $h_T$, le taux réel de fausses alertes sur un jumeau honnête devient $\ge 10\%$ [illustratif], ce qui détruit l'objectif du programme (« détection séquentielle à faible taux de fausses alertes », `RAPPORTÉ`).

3. **Vrai par construction et déplacement du coût hors budget dans E4 (`Fintype` contre `MeasureTheory`).**
   Dans E4, E compare le taux de preuve sous un plafond de $100\text{ \$/lemme}$ [illustratif] entre la version discrète `Fintype` et la version `MeasureTheory` générale sur $12$ lemmes [illustratif]. Sur un type fini `Fintype`, toute fonction est mesurable, toute fonction est bornée et intégrable, et toute somme finie commute avec l'espérance (`VÉRIFIÉ`). La difficulté propre d'un théorème probabiliste continu ou à horizon non borné réside précisément dans les conditions d'intégrabilité uniforme, de mesurabilité de temps d'arrêt ou de convergence dominée qui disparaissent identiquement sur `Fintype`. Le succès supérieur de `Fintype` est vrai par construction (on prouve un lemme algébrique plus faible), tandis que le coût de relèvement vers le théorème continu est reporté par E au §6 sur « 1 à 2 jours-homme en aval » [illustratif], hors du plafond de $100\text{ \$}$ [illustratif] de E4.

4. **Fuite de dictionnaire et contradiction arithmétique des seuils dans E1 et M3.**
   Dans M3, E encode une base de « 25 à 30 bornes classiques » [illustratif] et, dans E1, évalue ce réducteur sur « 15 théorèmes publiés (Le Cam, Ville, Vovk-Wang, Avenhaus) réécrits en jargon ». Si les $15$ théorèmes de test [illustratif] sont choisis parmi les $30$ théorèmes encodés [illustratif] dans la base du réducteur M3, le test mesure la présence des $15$ entrées dans une table de $30$ lignes écrite par le même expérimentateur (fuite directe construction/évaluation).

### (b) Conditions mesurables de perte de puissance ou de non-jugeabilité (lois, paramètres, estimateurs)

- **E1 — Contradiction arithmétique entre les deux estimateurs couplés $\hat{p}_0 = \frac{X_0}{n_0}$ (taux de faux nouveaux du juge nu) et $\widehat{\Delta R} = \frac{X_{\text{réd}} - (n_0 - X_0)}{n_0}$ (gain de rappel) sur les mêmes $n_0 = 15$ contrôles négatifs [illustratif] :**
  Soient $n_0 = 15$ classiques camouflés [illustratif], $X_0 \sim \text{Bin}(n_0, p_0)$ le nombre de classiques manqués par le juge nu (donc $\hat{R}_{\text{nu}} = 1 - \hat{p}_0$), et $X_{\text{réd}} \sim \text{Bin}(n_0, R_{\text{réd}})$ le nombre de classiques détectés par le réducteur. Les seuils de E1 pour valider $H_A$ sont simultanément $\hat{p}_0 > 0{,}20$ [illustratif] et $\widehat{\Delta R} = \hat{R}_{\text{réd}} - \hat{R}_{\text{nu}} \ge 0{,}25$ [illustratif].
  1. Comme $\hat{R}_{\text{réd}} \le 1$ et $\hat{R}_{\text{nu}} = 1 - \hat{p}_0$, on a **toujours par identité algébrique** :
     $$\widehat{\Delta R} = \hat{R}_{\text{réd}} - (1 - \hat{p}_0) \le \hat{p}_0$$
  2. Par conséquent, dans tout le régime de paramètres où le taux d'échec réel du juge nu vérifie $p_0 \in (0{,}20 ; 0{,}25)$ [illustratif] (ou dès que la réalisation empirique vaut $X_0 = 3$ sur $15$ [illustratif], soit $\hat{p}_0 = 3/15 = 0{,}20$, ou $X_0$ tel que $0{,}20 < \hat{p}_0 < 0{,}25$), même un réducteur parfait ($R_{\text{réd}} = 1$) donne $\widehat{\Delta R} = \hat{p}_0 < 0{,}25$ [illustratif] : **le premier seuil ($\hat{p}_0 > 0{,}20$) est franchi mais le second ($\widehat{\Delta R} \ge 0{,}25$) est mathématiquement impossible à atteindre**.
  3. Pour $n_0 = 15$ [illustratif], $\hat{p}_0 > 0{,}20 \iff X_0 \ge 4$ et $\widehat{\Delta R} \ge 0{,}25 \iff X_{\text{réd}} - (15 - X_0) \ge 4$. Sous $p_0 = 0{,}25$ [illustratif] et $R_{\text{réd}} = 0{,}95$ [illustratif], $\mathbb{P}(X_0 \ge 4) = 0{,}539$ [illustratif] : le test a une erreur de type II $\beta \ge 0{,}461$ [illustratif].

- **M1 & E2 — Estimateur d'interpolation rationnelle $\hat{y}(m)$ sur la suite de faces duales optimales $\mathcal{F}^*_m = \{ y \in \mathbb{Q}^{k(m)} : A_m^\top y \ge c_m, \, b_m^\top y = V^*_m \}$ pour $m \in \{2, \dots, 12\}$ [illustratif] :**
  Soit $E_m = \operatorname{ext}(\mathcal{F}^*_m)$ l'ensemble des sommets extrêmes de la face duale optimale à la taille $m$, de cardinal $|E_m| = s_m \ge 1$, et soit $Y_m \in E_m$ le sommet sélectionné par le solveur simplexe selon une loi $\mu_m$ sur $E_m$.
  1. Pour qu'une coordonnée duale $y^*_j(m) = \frac{P_j(m)}{Q_j(m)}$ de degrés $(\deg P_j, \deg Q_j) = (d_1, d_2)$ soit reconstructible de manière unique par interpolation de Padé-Cauchy sur $L = 11$ points ($m = 2, \dots, 12$ [illustratif]), il faut $L \ge d_1 + d_2 + 1$ points tirés sur **la même branche algébrique cohérente** $m \mapsto \bar{y}(m) \in \mathcal{F}^*_m$.
  2. Si, par dégénérescence primale symétrique, chaque face $\mathcal{F}^*_m$ possède $s_m \ge 2$ sommets extrêmes dont un seul appartient à la branche algébrique parcimonieuse avec probabilité de sélection $\pi_m \le \frac{1}{s_m} \le \frac{1}{2}$ sous pivotage standard, la probabilité d'observer une trajectoire interpolable sans erreur sur $L$ tailles vaut :
     $$\mathbb{P}\!\left(\forall m \in \{2,\dots,L+1\}, \, Y_m = \bar{y}(m)\right) = \prod_{m=2}^{L+1} \pi_m \le 2^{-L}$$
     (soit $\le 2^{-11} \approx 4{,}88 \times 10^{-4}$ pour $L = 11$ [illustratif]). Dès que le nombre de sommets déviants dépasse $\lfloor (L - d_1 - d_2 - 1)/2 \rfloor$ (borne de décodage de Reed-Solomon), la fraction rationnelle devient algébriquement non identifiable.

- **M2 — Estimateur adaptatif de conformité empirique $\hat{p}_{n_{\text{tr}}}(h_T) = \frac{1}{n_{\text{tr}}} \sum_{i=1}^{n_{\text{tr}}} \mathbb{I}(X_i \in h_T)$ après $R = 40$ rondes adaptatives [illustratif] au seuil $\tau = 0{,}90$ [illustratif] :**
  Soient $X_1, \dots, X_{n_{\text{tr}}} \stackrel{\text{i.i.d.}}{\sim} P_{\text{honnête}}$ la banque de $n_{\text{tr}}$ traces honnêtes, et soit $h_T \in \mathcal{H}$ l'hypothèse sélectionnée à l'issue de $R = 40$ rondes [illustratif] testant chacune $K$ candidats contre l'oracle binaire $\mathbb{I}(\hat{p}_{n_{\text{tr}}}(h) \ge \tau)$, où la famille $\mathcal{H}$ a une dimension de Vapnik-Chervonenkis $V$.
  1. Par concentration uniforme sur requêtes adaptatives, le biais de sur-ajustement maximal vérifie :
     $$\mathbb{E}\!\left[\sup_{t \le R} \left(\hat{p}_{n_{\text{tr}}}(h_t) - P_{\text{honnête}}(X \in h_t)\right)\right] \ge c_0 \min\!\left(1, \sqrt{\frac{V + R \log K}{n_{\text{tr}}}}\right)$$
  2. Dès que $n_{\text{tr}} \le \frac{c_0^2 (V + R \log K)}{(0{,}90 - p_{\text{min}})^2}$, une hypothèse dégénérée de couverture réelle $P_{\text{honnête}}(X \in h_T) \le p_{\text{min}}$ franchit le seuil $\hat{p}_{n_{\text{tr}}}(h_T) \ge 0{,}90$ [illustratif] avec forte probabilité.
  3. De plus, si le taux de fausse alerte nominal du moniteur conditionnellement à $h_T$ est $\alpha = \mathbb{P}_{\text{honnête}}(\text{Alerte} \mid X \in h_T)$ et vaut $\alpha_{\text{hors}} \in (\alpha, 1]$ pour $X \notin h_T$, le taux marginal réel de fausse alerte vaut :
     $$\alpha_{\text{marginal}} = \alpha P_{\text{honnête}}(X \in h_T) + \alpha_{\text{hors}} \left(1 - P_{\text{honnête}}(X \in h_T)\right) \ge \alpha_{\text{hors}} (1 - 0{,}90) = 0{,}10 \, \alpha_{\text{hors}} \text{ [illustratif]}$$
     Dès que $\alpha \ll 0{,}10 \, \alpha_{\text{hors}}$ [illustratif], la garantie de fausse alerte à niveau $\alpha$ perd toute validité sur la loi marginale $P_{\text{honnête}}$.

- **E3 — Estimateur de rejet de fausseté $\hat{q}_{R1} = \frac{1}{n_0}\sum_{i=1}^{n_0} \mathbb{I}(\text{Accepté}_i = 1)$ sur $n_0 = 10$ énoncés faux subtils [illustratif] :**
  Soit $n_0 \hat{q}_{R1} \sim \text{Bin}(10, q_{R1})$ où $q_{R1}$ est la probabilité qu'un énoncé faux subtil soit accepté après autoformalisation libre.
  1. Pour un taux de défaillance critique $q_{R1} = 0{,}08$ [illustratif] ($8\%$ [illustratif] de théorèmes faux certifiés comme vrais), la probabilité d'observer $n_0 \hat{q}_{R1} = 0$ sur $n_0 = 10$ essais [illustratif] et donc de falsifier $H_A$ à tort vaut $(1 - 0{,}08)^{10} = 0{,}4344$ [illustratif] ($43{,}4\%$ [illustratif] de perte de puissance).

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Dans M1 et E2 : contrôle de perturbation aléatoire du coût dual (sélection de sommets distincts de $\mathcal{F}^*_m$) et contrôle de frontière duale non algébrique.**
   Opposer $H_A$ (l'interpolation de $y^*(m)$ résiste à la dégénérescence duale grâce à une sélection canonique de norme minimale $\|y\|_2$ ou de centre analytique) à $H_B$ (le simplexe renvoie des sommets incompatibles d'un $m$ à l'autre) en réexécutant l'extraction de $y^*(m)$ sous $10$ permutations aléatoires [illustratif] des colonnes de la matrice primale $A_m$.
2. **Dans M2 : contrôle sur banque de traces honnêtes de validation strictement hors boucle (consultée une seule fois à la ronde finale $T = 40$ [illustratif]) et contrôle de traces de bruit pur.**
   Séparer hermétiquement la banque d'évolution ($n_{\text{évolution}}$) de la banque d'audit final ($n_{\text{test}}$ consultée une unique fois après gel de $h_{40}$), et vérifier en parallèle que $h_{40}$ est rejetée ($\hat{p} < 10\%$ [illustratif]) sur des traces gaussiennes isotropes sans structure de moniteur.
3. **Dans E1 et M3 : contrôle d'antériorité hors dictionnaire (théorèmes classiques absents des $30$ inégalités [illustratif] codées dans la base de démolition de M3).**
   Tester le portier M3 sur $15$ théorèmes classiques camouflés [illustratif] dont aucun ne figure dans la liste des $30$ inégalités [illustratif] pré-encodées, afin de falsifier l'illusion de généralité d'une table de correspondance fermée.

FIN-DE-CELLULE