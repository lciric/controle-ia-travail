# Théorie de la détection pour processus textuels et représentations vectorielles déterministes

*Note méthodologique : L’intégralité de ce document se situe exclusivement au niveau des espaces mesurables, des lois de probabilité et de la théorie asymptotique et non-asymptotique des tests. Les manipulations décrites opèrent uniquement sur des mesures et des variables aléatoires.*

---

## 1. Cadre probabiliste et formalisation

Soit $(\mathcal{A}, \mathfrak{A})$ l’espace mesurable des actions unitaires (suites finies de jetons issues d'un vocabulaire fini $\mathcal{V}$, muni de la tribu discrète $\mathfrak{A} = 2^{\mathcal{A}}$). L’espace des trajectoires de longueur finie $T \in \mathbb{N}^*$ est $(\mathcal{X}, \mathcal{F}) = (\mathcal{A}^T, \mathfrak{A}^{\otimes T})$, muni de la filtration naturelle $\mathcal{F}_t = \sigma(a_1, \dots, a_t)$ pour $1 \le t \le T$, avec $\mathcal{F}_0 = \{\emptyset, \mathcal{X}\}$ et $\mathcal{F}_T = \mathcal{F}$.

Le modèle de langage $M$ est formalisé comme une application mesurable déterministe fixe :
$$H : (\mathcal{X}, \mathcal{F}) \longrightarrow (\mathbb{R}^{T \times L \times P \times d}, \mathcal{B}(\mathbb{R}^{T \times L \times P \times d}))$$
En raison du masquage causal inhérent aux architectures autorégressives, l'application restreinte à l'instant $t$, notée $H_t$, est $\mathcal{F}_t$-mesurable. Pour un sous-ensemble fixé de positions lues $\Pi \subset \{1, \dots, L\} \times \{1, \dots, P\}$ de cardinal $|\Pi| = m$, on note $H_\Pi(X) = (h_{t,\ell,p})_{1 \le t \le T, (\ell,p) \in \Pi} \in \mathbb{R}^{T \times m \times d}$ la projection canonique. La tribu engendrée par ces observations partielles est $\mathcal{F}_\Pi = \sigma(H_\Pi(X)) \subset \mathcal{F}$.

Une famille de déplacements diffus est une collection de lois $\{P_\varepsilon\}_{\varepsilon \in [0, \varepsilon_{\max}]}$ sur $(\mathcal{X}, \mathcal{F})$ telle que :
1. **Contrainte locale conditionnelle** : Pour une divergence $d \in \{d_{\text{TV}}, d_{\text{H}}, D_{\text{KL}}\}$, $\forall t \in \{1,\dots,T\}$, $\forall a_{<t} \in \mathcal{A}^{t-1}$,
   $$d\big(P_\varepsilon(a_t \in \cdot \mid a_{<t}),\, P_0(a_t \in \cdot \mid a_{<t})\big) \le \varepsilon$$
2. **Condition globale d'éloignement** : Il existe une constante $c_0 > 0$ telle que $d_{\text{TV}}(P_\varepsilon^{(T)}, P_0^{(T)}) \ge c_0 > 0$ (typiquement lorsque $T \varepsilon^2 \asymp 1$ pour $d_{\text{H}}$ ou $d_{\text{TV}}$ sous indépendance ou mélange faible).

La classe des statistiques de surveillance $\mathcal{S}$ contient les fonctions mesurables $S : \mathcal{X} \to \mathbb{R}$ de la forme :
- **Agrégation par maximum** : $S_{\max}(X) = \max_{1 \le t \le T} \max_{(\ell,p) \in \Pi} \phi_{t,\ell,p}(a_t, h_{t,\ell,p})$, où $\phi_{t,\ell,p} : \mathcal{A} \times \mathbb{R}^d \to \mathbb{R}$.
- **Agrégation par attention** : $S_{\text{att}}(X) = \sum_{t=1}^T \sum_{(\ell,p) \in \Pi} w_{t,\ell,p}(H_\Pi(X)) v_{t,\ell,p}(H_\Pi(X))$, où les poids normalisés $w_{t,\ell,p}(H_\Pi) = \frac{\exp(\beta \langle q, k_{t,\ell,p}(h_{t,\ell,p})\rangle)}{Z(H_\Pi)}$ sont contraints par une condition de parcimonie entropique : l'entropie de Shannon $H(w(H_\Pi)) \le \kappa \ll \log(Tm)$ $P_0$-p.s. (interdisant la moyenne uniforme $\beta = 0$).
- **Processus de test séquentiel** : $M_T = \prod_{t=1}^T E_t$, où chaque $E_t$ est $\mathcal{F}_t$-mesurable, $E_t \ge 0$, et $\mathbb{E}_{P_0}[E_t \mid \mathcal{F}_{t-1}] \le 1$ ($e$-valeur conditionnelle). Le test rejette si $\sup_{1 \le t \le T} M_t \ge 1/\alpha$ (inégalité de Ville).

L'étalonnage empirique s'effectue à l'aide d'un échantillon i.i.d. $\mathcal{D}_n = (X^{(1)}, \dots, X^{(n)}) \sim P_0^{\otimes n}$. Le seuil empirique de niveau $\alpha \in (0,1)$ est la statistique d'ordre $\hat{s}_\alpha = S_{(\lceil(1-\alpha)(n+1)\rceil)}$.

---

## 2. Taxonomie formelle des classes de déplacements diffus

Pour toute statistique $S \in \mathcal{S}$, un déplacement $P_\varepsilon$ est dit $\delta$-invisible si $d_{\text{TV}}(P_\varepsilon \circ S^{-1}, P_0 \circ S^{-1}) \le \delta$. Par l'inégalité de traitement des données (Data Processing Inequality), la puissance est alors bornée par $P_\varepsilon(S > s_\alpha) \le P_0(S > s_\alpha) + \delta = \alpha + \delta$.

### Classe C1 : Déplacements sur les orbites d'un groupe d'invariance ($\mathcal{C}_{\text{inv}}$)
Soit $G$ un groupe fini ou compact opérant mesurablement sur $(\mathcal{X}, \mathcal{F})$. Soit $\pi_G : \mathcal{X} \to \mathcal{X}/G$ la projection canonique vers l'espace quotient des orbites, muni de la tribu des invariants $\mathcal{F}_G = \{A \in \mathcal{F} : \forall g \in G, gA = A\}$.
- **Définition formelle** : $P_\varepsilon \in \mathcal{C}_{\text{inv}}(G)$ si la restriction de $P_\varepsilon$ à $\mathcal{F}_G$ coïncide avec celle de $P_0$ : $P_\varepsilon|_{\mathcal{F}_G} = P_0|_{\mathcal{F}_G}$, tandis que les lois conditionnelles sur les orbites diffèrent : pour $P_0$-presque toute orbite $\mathcal{O} \in \mathcal{X}/G$, $d_{\text{TV}}(P_\varepsilon(\cdot \mid \mathcal{O}), P_0(\cdot \mid \mathcal{O})) \asymp \varepsilon T$.
- **Condition d'invisibilité** : $S$ est $G$-invariante ($S(gX) = S(X)$ pour tout $g \in G$), ce qui équivaut à dire que $S$ est $\mathcal{F}_G$-mesurable.
- **Mécanisme** : Puisque $\sigma(S) \subset \mathcal{F}_G$, on a $P_\varepsilon \circ S^{-1} = P_\varepsilon|_{\sigma(S)} = P_0|_{\sigma(S)} = P_0 \circ S^{-1}$ ($\delta = 0$). C'est le cas d'une statistique d'attention ou de maximum invariante par permutation des indices temporels $G = \mathfrak{S}_T$ lorsque la dynamique temporelle ne dépend pas de l'ordre absolu dans l'agrégateur.

### Classe C2 : Perturbations de la structure de dépendance temporelle ($\mathcal{C}_{\text{dep}}$)
- **Définition formelle** : Soit $P_0^{(t)}$ la loi marginale de l'action $a_t$ (et par déterminisme non-contextuel approché ou fenêtré, de $h_{t,\ell,p}$). $P_\varepsilon \in \mathcal{C}_{\text{dep}}$ si $\forall t \in \{1,\dots,T\}$, $P_\varepsilon(a_t \in \cdot) = P_0(a_t \in \cdot)$, mais la mesure jointe est perturbée par un facteur de couplage séquentiel :
  $$\frac{dP_\varepsilon}{dP_0}(X) = \prod_{t=2}^T \big(1 + \varepsilon \psi_t(a_t, a_{t-1})\big)$$
  avec $\mathbb{E}_{P_0}[\psi_t(a_t, a_{t-1}) \mid a_{t-1}] = 0$ et $\mathbb{E}_{P_0}[\psi_t(a_t, a_{t-1}) \mid a_t] = 0$ (perturbation de type copule discrète à marges fixées, $|\psi_t| \le 1$).
- **Condition d'invisibilité** : La statistique est de type additif marginal $S(X) = \sum_{t=1}^T \phi_t(a_t)$ (en particulier l'espérance d'une telle somme est identique sous $P_0$ et $P_\varepsilon$), ou un maximum $S_{\max}(X) = \max_{1 \le t \le T} \phi_t(a_t)$ sous condition de mélange faible ($\psi_t$ satisfaisant la condition $D(u_n)$ de Leadbetter).
- **Mécanisme** : Pour le maximum de variables aléatoires dépendantes stationnaires à queues lourdes ou exponentielles, si la condition $D'(u_T)$ de non-groupement des extrêmes locaux est vérifiée sous $P_\varepsilon$ et $P_0$, l'indice extrémal vaut $\theta = 1$ dans les deux cas. La loi asymptotique du maximum dépend alors uniquement des marginales $P_0^{(t)}$, rendant $S_{\max}$ asymptotiquement aveugle ($\delta_T \to 0$).

### Classe C3 : Déplacements orthogonaux de tribus entre texte et représentations ($\mathcal{C}_{\text{orth}}$)
Soit $\mathcal{G}_{\text{lex}} \subset \mathcal{F}$ une sous-tribu grossière engendrée par des statistiques lexicales de surface (ex. fréquences de $n$-grammes, longueurs).
- **Définition formelle** :
  - *Sous-classe C3a (Invisibilité boîte noire)* : $P_\varepsilon|_{\mathcal{G}_{\text{lex}}} = P_0|_{\mathcal{G}_{\text{lex}}}$, mais $d_{\text{TV}}(P_\varepsilon|_{\mathcal{F}_\Pi}, P_0|_{\mathcal{F}_\Pi}) \ge c_0$. Le déplacement opère dans les fibres conditionnelles de $\mathcal{G}_{\text{lex}}$ que l'application non-linéaire $H_\Pi$ sépare.
  - *Sous-classe C3b (Invisibilité boîte blanche)* : $P_\varepsilon|_{\mathcal{F}_\Pi} = P_0|_{\mathcal{F}_\Pi}$, mais $d_{\text{TV}}(P_\varepsilon|_{\mathcal{G}_{\text{lex}}}, P_0|_{\mathcal{G}_{\text{lex}}}) \ge c_0$. Ceci se produit lorsque $H_\Pi$ projette des séquences lexicalement distinctes sur les mêmes variétés d'activations (invariance sémantique du modèle $M$ sur les couches hautes $\Pi$).
- **Condition d'invisibilité** : $\sigma(S) \subset \mathcal{G}_{\text{lex}}$ pour C3a ; $\sigma(S) \subset \mathcal{F}_\Pi$ pour C3b.

### Classe C4 : Mélanges contaminés à deux échelles ($\mathcal{C}_{\text{mix}}$)
- **Définition formelle** :
  - *C4a (Mélange au niveau de la trajectoire)* : $P_\varepsilon^{(T)} = (1 - \pi) P_0^{(T)} + \pi Q^{(T)}$ avec $\pi \le \varepsilon$. Ici, conditionnellement au passé, le rapport de vraisemblance évolue lentement mais le mélange est global.
  - *C4b (Mélange diffus au niveau de l'action / étalement)* : À chaque pas $t$, $P_\varepsilon(a_t \mid a_{<t}) = (1-\varepsilon) P_0(a_t \mid a_{<t}) + \varepsilon Q_t(a_t \mid a_{<t})$.
- **Condition d'invisibilité** :
  - Pour C4a, toute statistique $S$ a une puissance bornée par $\alpha + \pi \le \alpha + \varepsilon$ car $d_{\text{TV}}(P_\varepsilon^{(T)}, P_0^{(T)}) = \pi d_{\text{TV}}(Q^{(T)}, P_0^{(T)}) \le \pi$.
  - Pour C4b face à $S_{\max}$ : Si la loi contaminante $Q_t$ concentre sa masse dans le corps de la distribution de $\phi_t(h_{t,\ell,p})$ sous $P_0$ (support de $Q_t \circ \phi_t^{-1}$ borné par le quantile d'ordre $1 - c/T$ de $P_0 \circ \phi_t^{-1}$), la queue supérieure de chaque terme est inchangée. L'étalement de la perturbation sur tous les temps sans créer d'extrêmes locaux laisse la loi du maximum global inchangée ($\delta \ll \varepsilon$).

### Classe C5 : Dérives non-stationnaires face aux martingales stationnaires ($\mathcal{C}_{\text{ns}}$)
- **Définition formelle** : La perturbation locale est modulée par une suite déterministe ou prévisible $(\varepsilon_t)_{1 \le t \le T}$ avec $\varepsilon_t \le \varepsilon$ :
  $$\frac{dP_\varepsilon(a_t \mid \mathcal{F}_{t-1})}{dP_0(a_t \mid \mathcal{F}_{t-1})} = 1 + \varepsilon_t g_t(a_t \mid \mathcal{F}_{t-1}), \quad \mathbb{E}_{P_0}[g_t \mid \mathcal{F}_{t-1}] = 0, \quad \text{Var}_{P_0}(g_t \mid \mathcal{F}_{t-1}) = 1$$
  où la direction fonctionnelle $g_t$ tourne dans $L^2(P_0)$ au cours du temps (par exemple $g_t = \cos(\omega t) u_1 + \sin(\omega t) u_2$ avec $\langle u_1, u_2 \rangle_{L^2(P_0)} = 0$), ou se concentre sur une fenêtre $W \subset \{1,\dots,T\}$.
- **Condition d'invisibilité** : Le test séquentiel utilise des $e$-valeurs stationnaires $E_t = 1 + \lambda f(a_t)$ calibrées pour une alternative fixe $f$.
- **Mécanisme** : La dérive du logarithme de la martingale sous $P_\varepsilon$ vaut $\sum_{t=1}^T \mathbb{E}_{P_\varepsilon}[\log(1 + \lambda f(a_t)) \mid \mathcal{F}_{t-1}] \approx \sum_{t=1}^T (\lambda \varepsilon_t \langle f, g_t \rangle_{L^2(P_0)} - \frac{\lambda^2}{2} \|f\|_{L^2(P_0)}^2)$. Si $\sum_{t=1}^T \varepsilon_t \langle f, g_t \rangle \le 0$ (orthogonalité moyenne par oscillation périodique), la sur-martingale sous $P_0$ reste une sur-martingale sous $P_\varepsilon$, et la probabilité de franchissement du seuil $1/\alpha$ reste inférieure à $\alpha$.

### Classe C6 : Déplacements dans le complémentaire d'exhaustivité de $H_\Pi$ ($\mathcal{C}_{\text{comp}}$)
- **Définition formelle** : Soit $\Pi^c = (\{1,\dots,L\}\times\{1,\dots,P\}) \setminus \Pi$. On définit $P_\varepsilon$ par une modification de la mesure conditionnellement à $H_\Pi(X)$ :
  $$P_\varepsilon(A) = \int_{\mathbb{R}^{T\times m \times d}} P_\varepsilon(A \mid H_\Pi(x) = h) \, d(P_0 \circ H_\Pi^{-1})(h), \quad \forall A \in \mathcal{F}$$
  où $P_\varepsilon(\cdot \mid H_\Pi = h) \neq P_0(\cdot \mid H_\Pi = h)$ sur $\sigma(H_{\Pi^c})$.
- **Condition d'invisibilité** : La statistique est purement boîte blanche restreinte à $\Pi$, soit $S(X) = \tilde{S}(H_\Pi(X))$.
- **Mécanisme** : Par construction, la loi marginale de $H_\Pi(X)$ sous $P_\varepsilon$ est exactement $P_0 \circ H_\Pi^{-1}$. Par conséquent, $H_\Pi$ est une statistique ancillaire (de distribution libre de $\varepsilon$), tandis que l'information de Fisher sur $\varepsilon$ est entièrement contenue dans la loi conditionnelle de $X$ (ou $H_{\Pi^c}$) sachant $H_\Pi$.

### Classe C7 : Déplacements dans le noyau variationnel de l'agrégateur ($\mathcal{C}_{\text{ker}}$)
Ici, la loi de $H_\Pi(X)$ change effectivement, mais la modification est absorbée par l'opérateur d'agrégation non-linéaire.
- **Sous-classe C7a (Troncature sous le maximum)** : Soit $Z_t = \max_{(\ell,p)\in\Pi} \phi_{t,\ell,p}(h_{t,\ell,p})$ et $M_T = \max_{1 \le t \le T} Z_t$. Soit $q_{1-1/T}$ le quantile d'ordre $1-1/T$ de $Z_t$ sous $P_0$. Le déplacement $P_\varepsilon$ modifie la densité de $Z_t$ uniquement sur l'intervalle $(-\infty, q_{1-c/T}]$ (avec $c \gg 1$) en préservant la masse totale de cet intervalle : $P_\varepsilon(Z_t \le q_{1-c/T}) = P_0(Z_t \le q_{1-c/T})$ et $P_\varepsilon(Z_t \in A) = P_0(Z_t \in A)$ pour tout borélien $A \subset (q_{1-c/T}, +\infty)$.
  - *Condition d'invisibilité* : Sous indépendance temporelle, $P(M_T \le x) = \prod_{t=1}^T P(Z_t \le x)$. Pour tout seuil $s_\alpha > q_{1-c/T}$ (ce qui est garanti dès que $\alpha < 1 - e^{-c}$), on a $P_\varepsilon(M_T > s_\alpha) = P_0(M_T > s_\alpha)$ exactement ($\delta = 0$).
- **Sous-classe C7b (Orthogonalité au sous-espace d'attention)** : L'agrégateur d'attention s'écrit $S_{\text{att}}(H_\Pi) = \sum_{i=1}^{Tm} w_i(H_\Pi) v_i(H_\Pi)$ où $w_i(H_\Pi) \propto \exp(\beta \langle q, K h_i \rangle)$ et $v_i(H_\Pi) = \langle u, V h_i \rangle$, avec $K, V \in \mathbb{R}^{d' \times d}$. Soit $V_{\text{lu}} = \text{Im}(K^\top) + \text{Im}(V^\top) \subset \mathbb{R}^d$.
  - *Définition* : Le déplacement translate ou modifie la loi de $h_i$ exclusivement dans le sous-espace orthogonal $V_{\text{lu}}^\perp$ : $h_i^{(\varepsilon)} \stackrel{\mathcal{L}}{=} h_i^{(0)} + \Delta_i$ avec $\Delta_i \in V_{\text{lu}}^\perp$ $P_0$-p.s., ou bien perturbe les vecteurs $h_i$ aux positions $i$ telles que $\langle q, K h_i \rangle \ll \max_j \langle q, K h_j \rangle - \frac{1}{\beta}\log(Tm/\delta)$ (zones de poids exponentiellement nuls).

### Classe C8 : Déplacements dans la zone d'incertitude d'étalonnage à $n$ fini ($\mathcal{C}_{\text{cal}}$)
- **Définition formelle** : La loi $P_0$ n'étant connue que par $\mathcal{D}_n$, l'incertitude statistique intrinsèque sur la fonction de répartition $F_0$ de $S(X)$ est d'ordre $O(n^{-1/2})$ uniformément (Dvoretzky-Kiefer-Wolfowitz), et d'ordre $O(\sqrt{\alpha(1-\alpha)/n})$ au voisinage du quantile $s_\alpha$. Un déplacement $P_\varepsilon \in \mathcal{C}_{\text{cal}}$ est tel que l'écart entre $F_\varepsilon(s_\alpha)$ et $F_0(s_\alpha)$ est dominé par la fluctuation d'échantillonnage du seuil empirique $\hat{s}_\alpha$ :
  $$F_0(s_\alpha) - F_\varepsilon(s_\alpha) \lesssim \sqrt{\frac{\alpha}{n}}$$
  Plus subtilement, pour un test composite où $S$ dépend d'un paramètre estimé sur $\mathcal{D}_n$ (ex. matrice de covariance empirique $\hat{\Sigma}_n$ en dimension $d$), si $d \gg n$, le noyau empirique $\ker(\hat{\Sigma}_n)$ est de dimension au moins $d - n$. Tout déplacement $P_\varepsilon$ concentré dans les directions propres associées aux valeurs propres nulles ou mal estimées de $\hat{\Sigma}_n$ exploite l'aveuglement géométrique dû à la taille finie de l'échantillon de référence.

---

## 3. Statistiques ripostes, bornes de puissance et protocoles d'épreuve

Le cadre interdit l'agrégation par moyenne uniforme spatiale/temporelle directe des activations, mais autorise les **tests séquentiels (martingales d'$e$-valeurs)**, l'**attention multi-requêtes adaptative**, et les **statistiques d'ordre ou fonctionnelles de la queue**.

### Riposte R1 (contre $\mathcal{C}_{\text{inv}}$) : Brisure de symétrie par encodage positionnel non-dégénéré et attention causale
- **Construction** : Si $S$ était invariante sous $G$ (ex. permutations temporelles $\mathfrak{S}_T$), on injecte dans les clés d'attention un repère canonique du groupe : $h_{t,\ell,p} \mapsto \tilde{h}_{t,\ell,p} = [h_{t,\ell,p} \,;\, e_t]$ où $(e_t)_{1\le t\le T}$ est une famille libre en position générale, et on utilise une martingale séquentielle non-commutative :
  $$M_T = \prod_{t=1}^T \left(1 + \lambda_t \psi_t(a_t, H_\Pi(a_{\le t}))\right)$$
  où $\psi_t$ dépend explicitement du passé ordonné $a_{<t}$ via le masque causal.
- **Borne démontrable** : Supposons que sur chaque orbite, $\mathbb{E}_{P_\varepsilon}[\psi_t \mid \mathcal{F}_{t-1}] \ge c \varepsilon$ et $|\psi_t| \le 1$, $\mathbb{E}_{P_0}[\psi_t \mid \mathcal{F}_{t-1}] = 0$, $\text{Var}_{P_0}(\psi_t \mid \mathcal{F}_{t-1}) = \sigma^2$. En choisissant $\lambda_t = \lambda = \frac{c\varepsilon}{\sigma^2 + c\varepsilon}$, l'inégalité élémentaire $\log(1+x) \ge x - \frac{x^2}{2(1-|x|)}$ et la concentration des martingales (inégalité de Freedman) donnent, pour $T \ge \frac{4\sigma^2}{c^2 \varepsilon^2} \log\frac{2}{\alpha\delta}$ :
  $$P_\varepsilon\left(M_T \ge \frac{1}{\alpha}\right) \ge 1 - \exp\left(-\frac{T c^2 \varepsilon^2}{8 \sigma^2} + \frac{1}{2}\log\frac{1}{\alpha}\right)$$
- **Prix payé** : Perte de l'invariance par rapport au groupe $G$. L'augmentation de la dimension de l'espace d'hypothèses accroît la complexité de Rademacher de la classe de fonctions de $\log|G|$, dégradant la vitesse d'étalonnage sur $n$ fini de $O(\sqrt{\frac{\log|G|}{n}})$.
- **Protocole d'épreuve** :
  - *Données honnêtes* : $n$ trajectoires sous $P_0$. Vérification que $\sup_t M_t \ge 1/\alpha$ a une fréquence empirique $\le \alpha + O(n^{-1/2})$.
  - *Déplacement synthétique* : Pour chaque trajectoire $X \sim P_0$, on tire une permutation aléatoire $\sigma \in \mathfrak{S}_T$ selon une loi de Mallows $P_\varepsilon(\sigma) \propto \exp(-\beta(\varepsilon) d_{\text{Kendall}}(\sigma, \text{id}))$ biaisée vers les inversions de paires spécifiques, puis on réordonne les blocs conditionnellement aux marges.
  - *Validation / Réfutation* : Attendu : $S$ invariante a une puissance $\approx \alpha$, tandis que $M_T$ atteint une puissance $\ge 1-\beta$ dès que $T \varepsilon^2 \gg \log(1/\alpha)$. Réfutation si la puissance de $M_T$ stagne à $\alpha$.

### Riposte R2 (contre $\mathcal{C}_{\text{dep}}$) : Martingale de rapport de vraisemblance de Markov d'ordre $k$ et attention croisée inter-actions
- **Construction** : Au lieu d'évaluer des fonctions de $a_t$ seul, on construit des $e$-valeurs bilinéaires sur les transitions d'activations entre $t-1$ et $t$ :
  $$E_t = 1 + \lambda \sum_{(\ell,p) \in \Pi} w_{t,\ell,p}(H_\Pi(a_{\le t})) \, \big\langle h_{t,\ell,p} - \hat{\mu}_{t,\ell,p},\, A (h_{t-1,\ell,p} - \hat{\mu}_{t-1,\ell,p}) \big\rangle$$
  où $\hat{\mu}_{t,\ell,p} = \mathbb{E}_{P_0}[h_{t,\ell,p} \mid \mathcal{F}_{t-1}]$ (qui est égal à la moyenne marginale sous l'hypothèse nulle d'indépendance temporelle, ou estimé par le prédicteur interne de $M$).
- **Borne démontrable** : Sous le modèle de copule séquentielle $\frac{dP_\varepsilon}{dP_0} = \prod_{t=2}^T (1 + \varepsilon \psi_t(a_t, a_{t-1}))$ avec $\|\psi_t\|_{L^2(P_0)} = \gamma > 0$, si la forme bilinéaire capture une fraction $\rho \in (0,1]$ de la corrélation ($\langle \text{score}_t, \psi_t \rangle_{L^2(P_0)} \ge \rho \gamma$), la divergence de Kullback-Leibler cumulée capturée vaut $\frac{1}{2}(T-1)\rho^2 \gamma^2 \varepsilon^2$. Par le lemme de Birgé et la concentration martingale, la puissance du test $M_T = \prod_{t=2}^T E_t \ge 1/\alpha$ satisfait :
  $$P_\varepsilon(M_T \ge 1/\alpha) \ge 1 - \frac{4}{(T-1)\rho^2 \gamma^2 \varepsilon^2}\left(\log\frac{1}{\alpha} + 1\right)^2 \quad \text{dès que } (T-1)\rho^2\gamma^2\varepsilon^2 > 2\log(1/\alpha).$$
- **Prix payé** : Variance doublée sous $P_0$ si le déplacement réel est purement marginal (baisse de puissance d'un facteur constant contre les alternatives i.i.d.) ; nécessité d'estimer l'espérance conditionnelle $\hat{\mu}_{t}$, introduisant un biais d'estimation de $O(d/n)$.
- **Protocole d'épreuve** :
  - *Déplacement synthétique* : Couplage gaussien ou par rejet par paires $(a_{2k-1}, a_{2k})$ à partir de tirages indépendants de $P_0$ : on tire $N$ suites de $P_0$, et on réapparie les actions $a_t$ à chaque pas $t$ par transport optimal entropique (algorithme de Sinkhorn avec régularisation $\varepsilon^{-1}$) pour créer une corrélation positive entre $\phi(h_t)$ et $\phi(h_{t-1})$ tout en conservant exactement les marginales empiriques à chaque instant $t$.
  - *Validation / Réfutation* : Toute statistique marginale $S_{\max}$ garde la même distribution empirique ; $M_T$ croît exponentiellement. Réfutation si le biais sur $\hat{\mu}_t$ fait exploser $M_T$ sous $P_0$ (perte de la propriété de sur-martingale).

### Riposte R3 (contre $\mathcal{C}_{\text{orth}}$) : Statistique hybride couplant surprise informationnelle boîte noire et sonde boîte blanche
- **Construction** : Puisque $M$ est un modèle de langage ouvert et connu, il fournit non seulement les activations cachées $H_\Pi(X)$, mais aussi la tête de prédiction lexicale exacte $P_M(a_t \mid a_{<t})$ (dernier étage du réseau). On définit la statistique jointe par combinaison convexe d'$e$-valeurs :
  $$E_t^{\text{hyb}} = \frac{1}{2} E_t^{\text{lex}}(a_t \mid a_{<t}) + \frac{1}{2} E_t^{\text{act}}(h_{t,\Pi} \mid h_{<t,\Pi})$$
  où $E_t^{\text{lex}}$ teste la conformité de la loi des jetons (ex. rapport de vraisemblance sur la log-perplexité ou les traits $\mathcal{G}_{\text{lex}}$) et $E_t^{\text{act}}$ est une statistique d'attention sur $\Pi$.
- **Borne démontrable** : Par convexité et positivité, $M_T^{\text{hyb}} = \prod_{t=1}^T E_t^{\text{hyb}} \ge \frac{1}{2} M_T^{\text{lex}} + \frac{1}{2} M_T^{\text{act}}$ si l'on mélange les martingales au niveau de la trajectoire : $M_T^{\text{mix}} = \frac{1}{2}\prod_{t=1}^T E_t^{\text{lex}} + \frac{1}{2}\prod_{t=1}^T E_t^{\text{act}}$. C'est une martingale valide sous $P_0$. Pour rejeter au seuil $1/\alpha$, il suffit que l'une des deux martingales dépasse $2/\alpha$. La perte de seuil équivaut à remplacer $\alpha$ par $\alpha/2$ :
  $$P_\varepsilon\left(M_T^{\text{mix}} \ge \frac{1}{\alpha}\right) \ge \max\left\{ P_\varepsilon\left(M_T^{\text{lex}} \ge \frac{2}{\alpha}\right),\, P_\varepsilon\left(M_T^{\text{act}} \ge \frac{2}{\alpha}\right) \right\}$$
- **Prix payé** : Perte d'un facteur $\log 2$ dans l'exposant de détection (équivalent à diviser le niveau $\alpha$ par 2 pour chaque modalité).
- **Protocole d'épreuve** :
  - *Déplacement synthétique* : Rééchantillonnage par importance (Importance Sampling) d'un grand réservoir de suites issues de $P_0$ avec des poids $W(X) \propto \exp(\varepsilon \sum_t u^\top h_{t,\ell,p})$ sous contrainte de moment linéaire nulle sur les indicateurs lexicaux $\mathbb{E}_{P_\varepsilon}[\mathbb{I}_{\mathcal{G}_{\text{lex}}}] = \mathbb{E}_{P_0}[\mathbb{I}_{\mathcal{G}_{\text{lex}}}] $ (projection I-divergente / couplage de Schrödinger).
  - *Validation / Réfutation* : $M_T^{\text{lex}}$ reste bornée par $O_{P_\varepsilon}(1)$ tandis que $M_T^{\text{mix}}$ franchit $1/\alpha$.

### Riposte R4 (contre $\mathcal{C}_{\text{mix}}$ et $\mathcal{C}_{\text{ker}}$-a) : Attention focalisée sur les quantiles intermédiaires (Higher Criticism / Scan doux) et $e$-valeurs bornées
- **Construction** : Face à un déplacement diffus C4b ou C7a qui évite la queue extrême (invisible à $S_{\max}$) et s'étale sous le quantile $q_{1-c/T}$, on utilise une agrégation par attention dont la fonction de score cible une bande spectrale de quantiles intermédiaires $[q_{\tau_1}, q_{\tau_2}]$ (avec $\tau_1, \tau_2 \in (0,1)$ fixes, ex. $[0.7, 0.95]$) :
  $$w_t(H_\Pi) \propto \exp\Big(-\beta \big(\phi(h_{t,\Pi}) - \mu_{\text{cible}}\big)^2\Big), \quad v_t(H_\Pi) = \mathbb{I}_{\{\phi(h_{t,\Pi}) > q_{\tau_1}\}} - (1-\tau_1)$$
  En choisissant $\beta$ grand, les poids se concentrent exclusivement sur les positions dont l'activation tombe au voisinage de $\mu_{\text{cible}} = q_{\tau_1}$ (satisfaisant la contrainte de non-uniformité des poids), ou bien via le produit séquentiel $M_T = \prod_{t=1}^T \big(1 + \lambda (\mathbb{I}_{\{\phi(h_{t,\Pi}) \in [q_{\tau_1}, q_{\tau_2}]\}} - (\tau_2 - \tau_1))\big)$.
- **Borne démontrable** : Soit $p_0 = \tau_2 - \tau_1$ la masse de l'intervalle sous $P_0$, et $p_\varepsilon = P_\varepsilon(\phi(h_t) \in [q_{\tau_1}, q_{\tau_2}]) = p_0 + c\varepsilon$. C'est un test séquentiel de Bernoulli. Par l'inégalité de Chernoff-Hoeffding pour les martingales bornées, avec $\lambda = \frac{c\varepsilon}{p_0(1-p_0)}$ :
  $$P_\varepsilon(M_T \ge 1/\alpha) \ge 1 - \exp\left(-\frac{T c^2 \varepsilon^2}{2 p_0(1-p_0)} + \log\frac{1}{\alpha}\right)$$
  alors que $S_{\max}$ a une puissance exactement égale à $\alpha$ si $\tau_2 < 1 - c'/T$.
  *(Note : Pour le mélange global de trajectoire C4a où $P_\varepsilon^{(T)} = (1-\pi)P_0^{(T)} + \pi Q^{(T)}$, aucune riposte ne peut dépasser la puissance $\alpha + \pi$, voir Section 4).*
- **Prix payé** : Insensibilité aux anomalies ponctuelles extrêmes (un seul pic massif en un unique instant $t_0$ est tronqué à $1 + \lambda(1-p_0)$ par l'indicateur borné, alors que $S_{\max}$ le détecterait avec probabilité $\approx 1$).
- **Protocole d'épreuve** :
  - *Déplacement synthétique* : Transformation par quantile inverse sur les scores : pour chaque suite de $P_0$, les valeurs de $\phi(h_t)$ tombant dans $[q_{0.5}, q_{0.8}]$ sont poussées vers $[q_{0.8}, q_{0.9}]$ par une application déterministe monotone par morceaux qui vaut l'identité sur $[q_{0.9}, +\infty)$.
  - *Validation / Réfutation* : La loi du maximum sur $T \le 50$ reste rigoureusement inchangée pour $\alpha = 0.05$ ; la martingale des quantiles intermédiaires détecte le déplacement en $T \asymp \varepsilon^{-2} \log(1/\alpha)$.

### Riposte R5 (contre $\mathcal{C}_{\text{ns}}$) : Martingales de mélange sur grilles de fréquences et redémarrage adaptatif (Shiryaev-Roberts-Pollak)
- **Construction** : Contre une dérive non-stationnaire (oscillante ou localisée sur une fenêtre $W = [t_1, t_2]$), une martingale à paramètre fixe échoue. On construit une **martingale de mélange spectral et temporel** :
  Soit $\Omega = \{\omega_1, \dots, \omega_K\}$ une grille de fréquences et $\Lambda$ une grille de pas. Pour chaque début de fenêtre possible $s \in \{1, \dots, t\}$, on définit la martingale locale $M_{s:t}^{(\omega)} = \prod_{r=s}^t (1 + \lambda \cos(\omega r) f(h_r))$. La statistique séquentielle agrégée par somme pondérée a priori est :
  $$R_t = \sum_{s=1}^t \pi_t(s) \sum_{k=1}^K \frac{1}{K} M_{s:t}^{(\omega_k)}, \quad \text{avec } \sum_{s=1}^t \pi_t(s) = 1 \text{ (ex. } \pi_t(s) \propto (t-s+1)^{-2}\text{)}$$
  Sous $P_0$, $\mathbb{E}_{P_0}[R_t] = 1$ à tout instant $t$ (c'est une $e$-valeur valide à temps fixe ou via un mélange sur les temps de départ $\pi(s) = \frac{6}{\pi^2 s^2}$ pour que $\sup_t \sum_{s=1}^t \pi(s) M_{s:t}$ soit dominé par une sur-martingale positive d'espérance $\le 1$).
- **Borne démontrable** : Si le déplacement est actif sur une fenêtre $W = [s_0, s_0 + L - 1]$ de longueur $L \le T$ à la fréquence $\omega_{k_0}$, le terme $(s_0, k_0)$ dans la somme domine par positivité des autres termes :
  $$M_T^{\text{mix}} \ge \frac{6}{\pi^2 s_0^2 K} M_{s_0 : s_0+L-1}^{(\omega_{k_0})}$$
  Il suffit que $M_{s_0 : s_0+L-1}^{(\omega_{k_0})} \ge \frac{\pi^2 s_0^2 K}{6 \alpha}$. La condition de détection sur la longueur de la fenêtre $L$ est donc :
  $$L \varepsilon^2 \gtrsim \log\left(\frac{T^2 K}{\alpha}\right) = \log\frac{1}{\alpha} + 2\log T + \log K$$
- **Prix payé** : Pénalité logarithmique $2\log T + \log K$ sur le seuil effectif, qui requiert un horizon $L$ légèrement plus long qu'une martingale oracle connaissant $s_0$ et $\omega_{k_0}$.
- **Protocole d'épreuve** :
  - *Déplacement synthétique* : Pondération exponentielle modulée temporellement $\frac{dP_\varepsilon}{dP_0}(X) \propto \exp\big(\varepsilon \sum_{t \in W} (-1)^t \phi(h_t)\big)$ appliquée par rééchantillonnage d'importance sur les trajectoires de $P_0$.
  - *Validation / Réfutation* : La martingale stationnaire constante $(\omega = 0)$ voit ses incréments s'annuler exactement deux à deux ($\delta \approx 0$) ; $R_t$ franchit le seuil $1/\alpha$ dès que $|W|\varepsilon^2 \gg \log(TK/\alpha)$.

### Riposte R6 et R7b (contre $\mathcal{C}_{\text{comp}}$ et $\mathcal{C}_{\text{ker}}$-b) : Échantillonnage aléatoire de sous-espaces (Sondes de Johnson-Lindenstrauss) et expansion de $\Pi$
- **Construction** : Tant que $\Pi$ et le sous-espace lu $V_{\text{lu}}$ sont fixes et connus, tout déplacement dans $\Pi^c$ ou $V_{\text{lu}}^\perp$ est invisible. Si l'on autorise une famille de statistiques indexée par une clé aléatoire privée (ou une agrégation par maximum sur $M_{\text{proj}}$ têtes d'attention couvrant l'espace ambiant $\mathbb{R}^d$), on définit :
  $$S_{\text{multi-att}}(X) = \max_{1 \le r \le d} \sum_{t=1}^T w_t^{(r)}(H_\Pi) \langle u_r, h_{t,\ell,p} \rangle$$
  où $(u_1, \dots, u_d)$ est une base orthonormée complète de $\mathbb{R}^d$ (incluant les vecteurs propres de queue de la covariance de $P_0$ blanchie). Pour contrer $\mathcal{C}_{\text{comp}}$ (hors de $\Pi$), il est mathématiquement obligatoire d'étendre $\Pi$ (voir Section 4 pour l'impossibilité à $\Pi$ fixé) ou d'utiliser la composante boîte noire $S(X)$ puisque $X$ détermine bijectivement $H_{\Pi^c}(X)$.
- **Borne démontrable** : Soit $\Delta_t = \mathbb{E}_{P_\varepsilon}[h_t] - \mathbb{E}_{P_0}[h_t] \in \mathbb{R}^d$ tel que $\|\Delta_t\|_2 \ge c\varepsilon$ dans la métrique de Mahalanobis sous $P_0$ ($\Sigma_0 = I_d$ après blanchiment). Par le principe des tiroirs sur la base orthonormée, il existe au moins une direction $r^* \in \{1,\dots,d\}$ telle que $|\langle u_{r^*}, \Delta_t \rangle| \ge \frac{c\varepsilon}{\sqrt{d}}$. En combinant les $d$ martingales directionnelles par une moyenne uniforme $M_T = \frac{1}{d}\sum_{r=1}^d \prod_{t=1}^T E_t^{(r)}$, on obtient un test de puissance $\ge 1-\beta$ dès que :
  $$T \frac{c^2 \varepsilon^2}{d} \gtrsim \log\left(\frac{d}{\alpha \beta}\right) \iff T \varepsilon^2 \gtrsim d \log\left(\frac{d}{\alpha}\right)$$
  Si l'on utilise le test quadratique séquentiel (martingale de chi-deux sur la norme blanchie), la dépendance passe à $T \varepsilon^2 \gtrsim \sqrt{d} \log(1/\alpha)$ pour une perturbation isotrope ou de direction inconnue (borne minimax de Ingster-Spokoiny).
- **Prix payé** : Pénalité dimensionnelle en $\sqrt{d}$ ou $d\log d$ dans le rapport signal-sur-bruit requis, due à la recherche aveugle dans toutes les directions orthogonales de $\mathbb{R}^d$.
- **Protocole d'épreuve** :
  - *Déplacement synthétique* : Sur les activations $H_\Pi(X)$ issues de $P_0$, on calcule la décomposition en valeurs singulières de la matrice des requêtes/valeurs de l'attention initiale $S_{\text{att}}$, on choisit un vecteur unitaire $u_\perp \in V_{\text{lu}}^\perp$, et on translate directement la loi empirique des activations : $h_{t,\ell,p} \leftarrow h_{t,\ell,p} + \varepsilon \sigma_\perp u_\perp$ (opération purement au niveau de la loi image dans $\mathbb{R}^d$).
  - *Validation / Réfutation* : $S_{\text{att}}$ initiale est strictement invariante ($S_{\text{att}}(H_\Pi + \varepsilon u_\perp) = S_{\text{att}}(H_\Pi)$ algébriquement) ; la riposte multi-directions détecte à $T \asymp \frac{d}{\varepsilon^2}\log(d/\alpha)$.

### Riposte R8 (contre $\mathcal{C}_{\text{cal}}$) : Martingales pivotales par symétrisation (Conformal e-values) et régularisation de Ledoit-Wolf
- **Construction** : Pour éviter que l'incertitude sur $\hat{\Sigma}_n$ (quand $d \gtrsim n$) ne crée des directions aveugles ou des seuils mal calibrés, on remplace la covariance empirique par l'estimateur rétréci régularisé $\hat{\Sigma}_{\text{LW}} = (1-\rho)\hat{\Sigma}_n + \rho \frac{\text{Tr}(\hat{\Sigma}_n)}{d} I_d$ (qui est inversible et bien conditionné même pour $d \gg n$), et on calibre le seuil par **p-valeurs conformes / rangs échangeables**.
  Plus précisément, pour une statistique scalaire $S$, le test rejette si le rang de $S(X_{\text{test}})$ parmi $\{S(X^{(1)}), \dots, S(X^{(n)}), S(X_{\text{test}})\}$ dépasse $\lceil(1-\alpha)(n+1)\rceil$.
- **Borne démontrable** : Par échangeabilité sous $P_0$, la probabilité de faux positif inconditionnelle (intégrée sur le tirage de $\mathcal{D}_n$) est bornée exactement :
  $$\mathbb{P}_{P_0^{\otimes (n+1)}}\big(S(X_{\text{test}}) > \hat{s}_\alpha\big) = \frac{\lfloor \alpha(n+1) \rfloor}{n+1} \le \alpha$$
  Conditionnellement à $\mathcal{D}_n$, l'inégalité de Dvoretzky-Kiefer-Wolfowitz garantit qu'avec probabilité au moins $1-\gamma$ sur le tirage de $\mathcal{D}_n$, $\sup_{s} |\hat{F}_n(s) - F_0(s)| \le \sqrt{\frac{\log(2/\gamma)}{2n}}$. Ainsi, tout déplacement vérifiant $P_\varepsilon(S > s_\alpha) \ge \alpha + 2\sqrt{\frac{\log(2/\gamma)}{2n}} + \Delta$ a une puissance conditionnelle au moins $\alpha + \Delta$ avec probabilité $1-\gamma$.
- **Prix payé** : Impossibilité mathématique d'atteindre un niveau $\alpha < \frac{1}{n+1}$ par étalonnage non-paramétrique pur (plancher de résolution discret $\alpha_{\min} = \frac{1}{n+1}$). La régularisation $\rho I_d$ réduit la sensibilité dans les vraies directions de très faible variance sous $P_0$ d'un facteur $(1+\rho/\lambda_{\min}(\Sigma_0))^{-1}$.
- **Protocole d'épreuve** :
  - *Déplacement synthétique* : On sépare un grand échantillon de $P_0$ en $\mathcal{D}_n$ (taille $n < d$) et un ensemble de test. On calcule un vecteur $v \in \ker(\hat{\Sigma}_n)$ sur $\mathcal{D}_n$, et on perturbe la loi des activations de l'ensemble de test dans la direction $v$ : $h_t \leftarrow h_t + \varepsilon v$.
  - *Validation / Réfutation* : Une statistique projetée uniquement sur l'image de $\hat{\Sigma}_n$ (PCA empirique tronquée) a une puissance égale à $\alpha$ ; la statistique régularisée par $\hat{\Sigma}_{\text{LW}}$ conserve une borne inférieure de valeur propre $\rho \frac{\text{Tr}(\Sigma_0)}{d} > 0$ sur tout $\mathbb{R}^d$ et détecte la perturbation.

---

## 4. Théorèmes d'impossibilité et limites fondamentales

Nous caractérisons ici les régimes où $\sup_{S \in \mathcal{S}} P_\varepsilon(S > s_\alpha) \le \alpha + \delta$ irréductiblement, avec esquisses de preuves et modifications structurelles requises pour lever l'obstacle.

### Impossibilité I1 : Régime sous-critique d'indiscernabilité informationnelle (Contiguïté et borne de Le Cam)
- **Énoncé** : Soit une famille de déplacements diffus $\{P_\varepsilon\}$ telle que pour chaque action $t$, la divergence du chi-deux conditionnelle vérifie $\chi^2\big(P_\varepsilon(a_t \mid \mathcal{F}_{t-1}) \,\|\, P_0(a_t \mid \mathcal{F}_{t-1})\big) \le \varepsilon^2$ $P_0$-p.s. Alors, **quelle que soit la statistique mesurable** $S$ (boîte noire, boîte blanche sur toutes les positions, avec mémoire infinie), la puissance est uniformément bornée par :
  $$\sup_{S : P_0(S > s_\alpha) \le \alpha} P_\varepsilon(S > s_\alpha) \le \alpha + \frac{1}{2}\sqrt{(1+\varepsilon^2)^T - 1} \underset{T\varepsilon^2 \ll 1}{\approx} \alpha + \frac{1}{2}\varepsilon \sqrt{T}$$
- **Preuve esquissée** : Par le lemme de Neyman-Pearson et la caractérisation variationnelle de la distance en variation totale, $\sup_{A \in \mathcal{F}} (P_\varepsilon(A) - P_0(A)) = d_{\text{TV}}(P_\varepsilon^{(T)}, P_0^{(T)})$. Par l'inégalité de Pinsker-Csiszár ou de Cauchy-Schwarz (seconde méthode de Le Cam), $d_{\text{TV}}(P, Q) \le \frac{1}{2}\sqrt{\chi^2(P \| Q)}$ ou $\sqrt{1 - \exp(-D_{\text{KL}}(P \| Q))}$. Or, par la règle de chaîne de la divergence de Kullback-Leibler :
  $$D_{\text{KL}}(P_\varepsilon^{(T)} \| P_0^{(T)}) = \sum_{t=1}^T \mathbb{E}_{P_\varepsilon}\Big[D_{\text{KL}}\big(P_\varepsilon(a_t \mid \mathcal{F}_{t-1}) \,\|\, P_0(a_t \mid \mathcal{F}_{t-1})\big)\Big] \le \sum_{t=1}^T \log(1+\varepsilon^2) \le T\varepsilon^2$$
  D'où $d_{\text{TV}}(P_\varepsilon^{(T)}, P_0^{(T)}) \le \sqrt{1 - e^{-T\varepsilon^2}} \le \varepsilon\sqrt{T}$ (par l'inégalité de Bretagnolle-Huber). Si $T \ll \varepsilon^{-2}$, les suites de mesures sont asymptotiquement confondues.
- **Pour lever l'impossibilité** : Aucune modification de $\mathcal{S}$, ni l'ajout d'un second modèle $M'$, ne peut lever cette barrière tant que l'observation est $X = (a_1, \dots, a_T)$. La seule façon de la lever est d'augmenter l'horizon d'observation $T$ au-delà de $\Omega(\varepsilon^{-2})$.

### Impossibilité I2 : Non-identifiabilité hors de la tribu des positions lues (Boîte blanche pure sur $\Pi$)
- **Énoncé** : Soit $\mathcal{S}_{\text{BB}}(\Pi)$ la sous-classe des statistiques boîte blanche qui ne dépendent de $X$ qu'à travers $H_\Pi(X)$ : $S(X) = \tilde{S}(H_\Pi(X))$. Si le noyau de l'application déterministe $H_\Pi : \mathcal{X} \to \mathbb{R}^{T\times m\times d}$ est non-trivial sur le support de $P_0$ (c'est-à-dire qu'il existe $x \neq x' \in \text{supp}(P_0)$ tels que $H_\Pi(x) = H_\Pi(x')$, ou que la tribu $\mathcal{F}_\Pi = \sigma(H_\Pi) \subsetneq \mathcal{F}$), alors il existe des déplacements $P_\varepsilon \in \mathcal{C}_{\text{comp}}$ tels que $d_{\text{TV}}(P_\varepsilon^{(T)}, P_0^{(T)}) \ge c_0 > 0$ mais :
  $$\forall S \in \mathcal{S}_{\text{BB}}(\Pi), \quad P_\varepsilon(S > s_\alpha) = P_0(S > s_\alpha) \le \alpha$$
- **Preuve esquissée** : Par le théorème de factorisation de Halmos-Savage, $H_\Pi$ est exhaustive pour la famille $\{P_0, P_\varepsilon\}$ si et seulement si la dérivée de Radon-Nikodym $\frac{dP_\varepsilon}{dP_0}(X)$ est $\mathcal{F}_\Pi$-mesurable. Puisque $\mathcal{F}_\Pi \subsetneq \mathcal{F}$, l'espace orthogonal $L^2(\mathcal{X}, \mathcal{F}, P_0) \ominus L^2(\mathcal{X}, \mathcal{F}_\Pi, P_0)$ est de dimension $\ge 1$. On choisit une fonction bornée non nulle $g$ dans cet orthogonal ($\mathbb{E}_{P_0}[g(X) \mid H_\Pi(X)] = 0$ $P_0$-p.s.) et on pose $dP_\varepsilon = (1 + \varepsilon_{\max} g) dP_0$. Pour toute fonction $\mathcal{F}_\Pi$-mesurable $\tilde{S}(H_\Pi(X))$, par conditionnement par rapport à $\mathcal{F}_\Pi$ :
  $$\mathbb{E}_{P_\varepsilon}[\mathbb{I}_{\{\tilde{S}(H_\Pi) > s_\alpha\}}] = \mathbb{E}_{P_0}\Big[\mathbb{I}_{\{\tilde{S}(H_\Pi) > s_\alpha\}} \mathbb{E}_{P_0}[1 + \varepsilon_{\max} g(X) \mid H_\Pi]\Big] = P_0(\tilde{S}(H_\Pi) > s_\alpha)$$
- **Ce qu'il faut ajouter à $\mathcal{S}$** : Ajouter la lecture directe du texte $X$ (composante boîte noire), ou étendre $\Pi$ jusqu'à une couche injective (comme la couche de plongement lexical $\ell = 0$ qui est injective sur $\mathcal{V}^T$), ou introduire un second modèle $M'$ dont les fibres d'équivalence $\sigma(H'_{\Pi'}(X))$ coupent transversalement celles de $H_\Pi(X)$ de sorte que $\sigma(H_\Pi, H'_{\Pi'}) = \mathcal{F}$.

### Impossibilité I3 : Aveuglement des statistiques sans mémoire temporelle face aux copules markoviennes ($\mathcal{C}_{\text{dep}}$)
- **Énoncé** : Soit $\mathcal{S}_{\text{marg}}$ la classe des statistiques de la forme $S(X) = \max_{1 \le t \le T} \phi(a_t, h_{t,\Pi}(a_t))$ où $h_{t,\Pi}(a_t)$ est évalué action par action (sans contexte inter-actions) et où les marginales $P_0(a_t \in \cdot) = \mu_0$ sont identiques et diffuses (sans atome pour $\phi$). Il existe des déplacements markoviens $P_\varepsilon \in \mathcal{C}_{\text{dep}}$ vérifiant $D_{\text{KL}}(P_\varepsilon^{(T)} \| P_0^{(T)}) \asymp T\varepsilon^2 \to \infty$ tels que :
  $$\lim_{T \to \infty} \big| P_\varepsilon(S > s_\alpha) - P_0(S > s_\alpha) \big| = 0$$
- **Preuve esquissée** : Soit $U_t = F_{\phi}( \phi(a_t) ) \sim \mathcal{U}([0,1])$ sous $P_0$. On construit $P_\varepsilon$ comme une chaîne de Markov stationnaire de densité de transition (copule de Farlie-Gumbel-Morgenstern) $c_\varepsilon(u_t, u_{t-1}) = 1 + \varepsilon(1 - 2u_t)(1 - 2u_{t-1})$ pour $|\varepsilon| \le 1$. Les marginales sont exactement uniformes : $\int_0^1 c_\varepsilon(u, v) dv = 1$. De plus, pour un seuil haut $u_T = 1 - \frac{\tau}{T}$ (avec $\tau = -\log(1-\alpha)$), la probabilité jointe de deux dépassements consécutifs vaut $P_\varepsilon(U_t > u_T, U_{t-1} > u_T) = \frac{\tau^2}{T^2}(1 + \varepsilon(1 - \frac{\tau}{T})^2) = O(T^{-2})$. La condition $D'(u_T)$ de Leadbetter est donc satisfaite : $\lim_{T\to\infty} T \sum_{t=2}^{o(T)} P_\varepsilon(U_1 > u_T, U_t > u_T) = 0$. Par le théorème de convergence des extrêmes de suites stationnaires faiblement dépendantes, $P_\varepsilon(\max_{1\le t\le T} U_t \le 1 - \tau/T) \to e^{-\tau} = 1-\alpha$, identique à la limite sous $P_0$.
- **Ce qu'il faut ajouter à $\mathcal{S}$** : Une mémoire temporelle explicite (états récurrents, fenêtres glissantes de taille $\ge 2$, ou lecture des activations contextuelles $h_{t,\ell,p}(a_{\le t})$ lorsque l'attention interne du modèle $M$ mélange effectivement $a_t$ et $a_{t-1}$).

### Impossibilité I4 : Plancher d'étalonnage non-paramétrique à échantillon de référence fini $n$
- **Énoncé** : Si $P_0$ est inconnue a priori dans l'espace de toutes les mesures diffuses sur $\mathcal{X}$ et connue uniquement par un échantillon i.i.d. $\mathcal{D}_n \sim P_0^{\otimes n}$, alors aucun test $\Psi(\mathcal{D}_n, X)$ qui contrôle le taux de faux positifs au niveau $\alpha$ pour toute loi $P_0$ ($\sup_{P_0} \mathbb{P}_{P_0^{\otimes(n+1)}}(\Psi = 1) \le \alpha$) ne peut avoir de puissance non triviale lorsque $\alpha < \frac{1}{n+1}$. Plus précisément, si $\alpha < \frac{1}{n+1}$, tout test sans biais symétrique en $\mathcal{D}_n$ vérifie $\Psi(\mathcal{D}_n, X) = 0$ p.s. (pour un test non-randomisé), donc sa puissance contre **tout** déplacement $P_\varepsilon$ est exactement 0.
- **Preuve esquissée** : C'est une conséquence directe du théorème de Bahadur-Savage et de la structure des tests de rangs sous symétrie d'échangeabilité. Sous $P_0^{\otimes(n+1)}$, conditionnellement à l'ensemble non ordonné des $(n+1)$ observations $\{X^{(1)}, \dots, X^{(n)}, X_{\text{test}}\}$, les $(n+1)!$ permutations ont la même probabilité $\frac{1}{(n+1)!}$. Tout événement de rejet déterministe invariant par permutation de $\mathcal{D}_n$ contient un nombre entier $k$ de configurations pour la position de $X_{\text{test}}$ parmi $n+1$ possibles. La probabilité conditionnelle de rejet vaut $\frac{k}{n+1}$. Si l'on exige $\frac{k}{n+1} \le \alpha < \frac{1}{n+1}$, alors $k = 0$.
- **Ce qu'il faut ajouter** : Soit un échantillon de référence de taille $n \ge \alpha^{-1} - 1$, soit une hypothèse paramétrique/semi-paramétrique sur les queues de $P_0$ (ex. sous-gaussianité de paramètre connu) permettant d'extrapoler le seuil $s_\alpha$ au-delà du maximum de l'échantillon $\mathcal{D}_n$.

### Impossibilité I5 : Ce qui reste impossible quelle que soit $\mathcal{S}$ tant que $H$ est une fonction déterministe de $X$
- **Théorème d'équivalence de l'information (Doob-Dynkin et traitement des données)** :
  Puisque $H : \mathcal{X} \to \mathbb{R}^{T\times L\times P\times d}$ est une application mesurable déterministe, pour tout ensemble de positions $\Pi$, la tribu jointe engendrée par le texte et les activations vérifie :
  $$\sigma\big(X, H(X)\big) = \sigma(X) = \mathcal{F}$$
  Par conséquent, pour toute divergence de f-Csiszár $D_f$ (incluant la variation totale $d_{\text{TV}}$, la distance de Hellinger $d_{\text{H}}$, la divergence de Kullback-Leibler $D_{\text{KL}}$ et le $\chi^2$), les lois jointes de $(X, H(X))$ sous $P_\varepsilon$ et $P_0$ satisfont l'**égalité exacte** :
  $$D_f\Big(P_\varepsilon \circ (\text{id}, H)^{-1} \,\Big\|\, P_0 \circ (\text{id}, H)^{-1}\Big) = D_f\big(P_\varepsilon^{(T)} \,\big\|\, P_0^{(T)}\big)$$
- **Corollaire fondamental d'impossibilité absolue** :
  L'accès boîte blanche aux activations $H(X)$ d'un modèle $M$ (ou d'une collection arbitraire de modèles déterministes $M_1, M_2, \dots$) **n'augmente jamais la puissance maximale théorique (de Neyman-Pearson)** au-delà de celle de la statistique boîte noire optimale $\frac{dP_\varepsilon}{dP_0}(X)$ :
  $$\sup_{S(X, H(X)) \text{ mesurable}} P_\varepsilon\big(S(X, H(X)) > s_\alpha\big) = \sup_{S_{\text{BN}}(X) \text{ mesurable}} P_\varepsilon\big(S_{\text{BN}}(X) > s_\alpha\big)$$
  Ainsi, tout déplacement $P_\varepsilon$ qui est informationnellement indétectable dans l'espace du texte $\mathcal{X}$ (par exemple un mélange global $P_\varepsilon^{(T)} = (1-\pi)P_0^{(T)} + \pi Q^{(T)}$ avec $\pi \ll \alpha$, ou un régime sous-critique $T \varepsilon^2 \ll 1$, ou deux processus distincts en amont qui induisent exactement la même loi marginale $P_0^{(T)}$ sur les suites de textes $X$) demeure **strictement indétectable** même en lisant l'intégralité des activations de toutes les couches de $M$.
  *Le seul rôle mathématique de $H(X)$ est computationnel et d'approximation statistique à $n$ fini* : $H_\Pi$ opère une réduction de dimension non-linéaire pré-entraînée qui linéarise certaines séparations complexes de $\mathcal{X}$ dans $\mathbb{R}^d$, réduisant la complexité d'échantillonnage $n$ nécessaire pour estimer un bon test, mais sans jamais créer d'information de Shannon ou de Fisher qui ne soit déjà présente dans $X$.

---

## 5. Tableau récapitulatif

| Classe de déplacement | Condition mesurable d'invisibilité | Statistique vulnérable | Statistique riposte | Borne de puissance démontrable (régime de détection) | Impossibilité dans $\mathcal{S}$ ? |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **C1 : Orbites d'invariance** ($\mathcal{C}_{\text{inv}}$) | $P_\varepsilon|_{\mathcal{F}_G} = P_0|_{\mathcal{F}_G}$ et $S$ est $\mathcal{F}_G$-mesurable ($S(gX)=S(X)$) | Toute $S$ symétrique (ex. max ou attention sans encodage temporel) | **R1** : Martingale séquentielle ordonnée avec encodage positionnel brisant $G$ | $1 - \exp\left(-\frac{T c^2 \varepsilon^2}{8\sigma^2} + \frac{1}{2}\log\frac{1}{\alpha}\right)$ ; détecte si $T\varepsilon^2 \gtrsim \sigma^2 \log(1/\alpha)$ | **Non**, levée en brisant la symétrie de $S$. |
| **C2 : Dépendances temporelles / Copules** ($\mathcal{C}_{\text{dep}}$) | $P_\varepsilon(a_t) = P_0(a_t)$ $\forall t$ et condition extrémale $D'(u_T)$ de Leadbetter | $S_{\max}$ marginale action par action ; sommes de termes marginaux | **R2** : Martingale bilinéaire sur transitions $(h_t, h_{t-1})$ ou attention croisée | $1 - O\big(\frac{\log^2(1/\alpha)}{T \rho^2 \gamma^2 \varepsilon^2}\big)$ ; détecte si $T\varepsilon^2 \gtrsim \frac{\log(1/\alpha)}{\rho^2\gamma^2}$ | **Oui** pour $S$ sans mémoire (I3) ; **Non** avec contexte causal. |
| **C3 : Texte vs Activations** ($\mathcal{C}_{\text{orth}}$) | C3a: $P_\varepsilon|_{\mathcal{G}_{\text{lex}}} = P_0|_{\mathcal{G}_{\text{lex}}}$<br>C3b: $P_\varepsilon|_{\mathcal{F}_\Pi} = P_0|_{\mathcal{F}_\Pi}$ | C3a: Boîte noire sur $\mathcal{G}_{\text{lex}}$<br>C3b: Boîte blanche sur $\Pi$ | **R3** : Martingale hybride $M_T^{\text{mix}} = \frac{1}{2}M_T^{\text{lex}} + \frac{1}{2}M_T^{\text{act}}$ | $\ge \max_i P_\varepsilon(M_T^{(i)} \ge \frac{2}{\alpha})$ ; pénalité additive de $\log 2$ sur le seuil | **Oui** pour BB pure si C3b (I2) ; **Non** pour la statistique hybride. |
| **C4 : Mélanges contaminés** ($\mathcal{C}_{\text{mix}}$) | C4a: Mélange de suite $\pi \le \varepsilon$<br>C4b: Support de $Q_t$ sous $q_{1-c/T}$ | C4a: Toute statistique $S$<br>C4b: $S_{\max}$ (queues intactes) | **R4** (contre C4b) : Attention ciblée sur bande de quantiles $[q_{\tau_1}, q_{\tau_2}]$ | C4b : $1 - \exp\big(-\frac{T c^2\varepsilon^2}{2p_0(1-p_0)} + \log\frac{1}{\alpha}\big)$<br>C4a : Bornée par $\alpha + \pi$ | **Oui** pour C4a ($\le \alpha+\pi$, I5) ; **Non** pour C4b. |
| **C5 : Dérives non-stationnaires** ($\mathcal{C}_{\text{ns}}$) | $\sum_{t=1}^T \varepsilon_t \langle f, g_t \rangle_{L^2(P_0)} \le 0$ (oscillation ou fenêtre courte $W$) | Martingale à direction d'alternative stationnaire fixe $f$ | **R5** : Martingale de mélange spectral et redémarrage (Shiryaev-Roberts) | Détecte sur fenêtre $L = |W|$ si $L\varepsilon^2 \gtrsim \log\frac{1}{\alpha} + 2\log T + \log K$ | **Non**, sauf si la fenêtre active vérifie $L\varepsilon^2 \ll 1$ (I1). |
| **C6 : Hors des positions lues $\Pi$** ($\mathcal{C}_{\text{comp}}$) | $P_\varepsilon \circ H_\Pi^{-1} = P_0 \circ H_\Pi^{-1}$ ($H_\Pi$ non exhaustive, ancillaire) | Toute statistique boîte blanche pure $S(H_\Pi(X))$ | **R6** : Extension de $\Pi$ aux couches basses injectives ou couplage boîte noire | Puissance restaurée dès que $\sigma(H_{\Pi'}) = \mathcal{F}$ avec $T\varepsilon^2 \gtrsim \log(1/\alpha)$ | **Oui** à $\Pi$ fixé sans lecture du texte (I2). |
| **C7 : Noyau de l'agrégateur** ($\mathcal{C}_{\text{ker}}$) | C7a: Modification sous $q_{1-c/T}$<br>C7b: $\Delta h \in V_{\text{lu}}^\perp = (\text{Im}K^\top + \text{Im}V^\top)^\perp$ | C7a: $S_{\max}$<br>C7b: $S_{\text{att}}$ à sous-espace de clés/valeurs de rang $< d$ | **R4** (contre C7a) et **R7b** : Max/Mélange de $d$ têtes d'attention orthogonales | C7b : Détecte toute direction de $\mathbb{R}^d$ si $T\varepsilon^2 \gtrsim d\log(d/\alpha)$ (ou $\sqrt{d}\log(1/\alpha)$) | **Oui** à poids/projections fixes ; **Non** avec sondes couvrant $\mathbb{R}^d$. |
| **C8 : Incertitude à $n$ fini** ($\mathcal{C}_{\text{cal}}$) | $F_0(s_\alpha) - F_\varepsilon(s_\alpha) \lesssim \sqrt{\alpha/n}$ ou $\Delta h \in \ker(\hat{\Sigma}_n)$ ($d > n$) | $S$ étalonnée sur $\hat{\Sigma}_n$ dégénérée ou pour $\alpha < \frac{1}{n+1}$ | **R8** : Régularisation de Ledoit-Wolf $\hat{\Sigma}_{\text{LW}}$ et test de rang conforme | Contrôle exact $\le \alpha$ pour $n \ge \alpha^{-1}-1$ ; erreur de seuil $\le \sqrt{\frac{\log(2/\gamma)}{2n}}$ | **Oui** si $\alpha < \frac{1}{n+1}$ sans hypothèse paramétrique (I4). |

---

## 6. Distinction des savoirs, conjectures et antériorités vérifiables

### 6.1 Ce qui relève du savoir établi (démontré)
1. **Égalité des divergences et impossibilité I5** : Le fait qu'une transformation déterministe $H(X)$ ne puisse accroître aucune $f$-divergence ni la puissance du test de Neyman-Pearson est un théorème classique de la théorie de la mesure (lemme de factorisation de Doob-Dynkin et inégalité de traitement des données de Csiszár).
2. **Bornes de contiguïté et vitesses minimax (I1, R6/R7b)** : La frontière de détectabilité $T\varepsilon^2 \asymp 1$ pour une alternative simple et $T\varepsilon^2 \asymp \sqrt{d}$ pour une alternative vectorielle isotrope de direction inconnue en dimension $d$ découle de la théorie asymptotique de Le Cam et des bornes minimax d'Ingster.
3. **Invisibilité aux extrêmes (C2, C4b, C7a)** : La dépendance de la loi asymptotique du maximum uniquement envers la queue supérieure marginale sous les conditions $D(u_n)$ et $D'(u_n)$ est un théorème établi de la théorie des valeurs extrêmes (Leadbetter).
4. **Tests séquentiels par $e$-valeurs et martingales de mélange (R1-R5)** : La validité non-asymptotique du seuil $1/\alpha$ par l'inégalité de Ville, la préservation de la propriété de martingale par combinaison convexe (R3, R5) et la pénalité logarithmique $\log(K/\alpha)$ sont des résultats prouvés de la statistique séquentielle moderne.
5. **Plancher d'étalonnage non-paramétrique (I4, R8)** : La borne $\frac{\lfloor \alpha(n+1)\rfloor}{n+1}$ pour les quantiles empiriques échangeables et l'impossibilité des tests non-paramétriques de niveau $\alpha < \frac{1}{n+1}$ sont des résultats exacts de la théorie des statistiques d'ordre et de l'inférence conforme.

### 6.2 Ce qui relève de la supposition ou de la conjecture ouverte
1. **Injectivité effective des couches intermédiaires $\Pi$ des modèles de langage (C3b, C6)** : Bien que les poids continus génériques d'un réseau de neurones de largeur $d$ suffisante soient injectifs sur un domaine discret fini $\mathcal{V}^T$, on *suppose* qu'en précision flottante finie et après projection par les couches d'attention à bas rang, il existe des quasi-collisions métriques $\|H_\Pi(x) - H_\Pi(x')\|_2 \le \eta_{\text{num}}$ pour des textes distincts. La caractérisation analytique exacte des fibres $\mathcal{F}_\Pi$ pour un transformeur donné reste un problème ouvert.
2. **Conditionnement spectral des activations sous $P_0$ (R7b, R8)** : La borne en $d\log d$ suppose un blanchiment préalable de la covariance $\Sigma_0$. En pratique, le spectre des activations des modèles de langage présente une décroissance en loi de puissance (anisotropie marquée) ; le compromis optimal du paramètre de régularisation $\rho$ de Ledoit-Wolf pour maximiser la puissance minimax contre des déplacements alignés sur les composantes mineures sous contrainte d'agrégation par attention reste une conjecture.
3. **Optimalité sous contrainte d'entropie de l'attention** : Alors que la moyenne uniforme est minimax-optimale pour détecter un décalage constant de moyenne sur tous les instants, la perte exacte d'efficacité asymptotique de Pitman imposée par la contrainte de parcimonie des poids d'attention ($H(w) \le \kappa$) sur une trajectoire unique sans test séquentiel n'est bornée ici que par des arguments de sous-échantillonnage ; la constante exacte optimale en fonction de $\kappa$ est supposée mais non fermée dans la littérature.

### 6.3 Antériorités bibliographiques

- **Théorie de l'exhaustivité et de l'invariance des tests** :
  - *Titre* : Application of the Theory of Measure in Abstract Spaces to the Theory of Sufficient Statistics.
  - *Auteurs* : Paul R. Halmos et Leonard J. Savage.
  - *Année* : 1949 (*The Annals of Mathematical Statistics*).
  - *Ce qui y est démontré* : Démontre le critère de factorisation des densités de Radon-Nikodym pour les mesures dominées sur des espaces mesurables abstraits, caractérisant exactement quand une sous-tribu (ici $\sigma(H_\Pi)$) porte toute l'information d'une famille de lois.
- **Impossibilité des tests non-paramétriques hors d'échelle et taille d'échantillon** :
  - *Titre* : The Nonexistence of Certain Statistical Procedures in Nonparametric Problems.
  - *Auteurs* : Raghu Raj Bahadur et Leonard J. Savage.
  - *Année* : 1956 (*The Annals of Mathematical Statistics*).
  - *Ce qui y est démontré* : Établit que dans une famille non-paramétrique riche de lois continues, aucun test ni intervalle de confiance basé sur un échantillon fini $n$ ne peut avoir une puissance informative sur des paramètres sensibles aux queues sans hypothèses structurelles supplémentaires.
- **Théorie des valeurs extrêmes pour processus dépendants** :
  - *Titre* : On Extreme Values in Stationary Sequences.
  - *Auteurs* : M. Ross Leadbetter.
  - *Année* : 1974 (*Zeitschrift für Wahrscheinlichkeitstheorie und verwandte Gebiete*).
  - *Ce qui y est démontré* : Introduit les conditions de mélange $D(u_n)$ et d'anti-groupement local $D'(u_n)$ et démontre que sous ces conditions, le maximum d'une suite stationnaire dépendante possède exactement la même loi limite que si les variables étaient indépendantes de mêmes lois marginales.
- **Contiguïté et bornes asymptotiques de détection de déplacements locaux** :
  - *Titre* : Locally Asymptotically Normal Families of Distributions.
  - *Auteurs* : Lucien Le Cam.
  - *Année* : 1960 (*University of California Publications in Statistics*).
  - *Ce qui y est démontré* : Formalise la notion de contiguïté entre suites de mesures de probabilité et démontre que les rapports de vraisemblance de perturbations locales en $O(T^{-1/2})$ convergent vers un modèle gaussien décalé, bornant la puissance maximale de tout test.
- **Bornes minimax de détection en grande dimension** :
  - *Titre* : Asymptotic Minimax Hypothesis Testing for Nonparametric Alternatives.
  - *Auteurs* : Yuri I. Ingster.
  - *Année* : 1982 (traduit et développé dans la série d'articles *Theory of Probability and its Applications*, et la monographie *Nonparametric Goodness-of-Fit Testing Under Gaussian Models*, Yuri I. Ingster et Irina A. Suslina, 2003).
  - *Ce qui y est démontré* : Établit les vitesses critiques minimax de séparation entre l'hypothèse nulle et des alternatives composites multidimensionnelles ou fonctionnelles, montrant la pénalité en $d^{1/4}$ sur la norme du signal ($\sqrt{d}$ sur l'énergie quadratique) lorsque la direction du déplacement est inconnue.
- **Détection de mélanges rares et statistiques de seuillage intermédiaire** :
  - *Titre* : Higher Criticism for Detecting Sparse Heterogeneous Mixtures.
  - *Auteurs* : David Donoho et Jiashun Jin.
  - *Année* : 2004 (*The Annals of Statistics*).
  - *Ce qui y est démontré* : Démontre la frontière exacte de détection pour les mélanges rares $(1-\varepsilon)P_0 + \varepsilon Q$ et prouve que lorsque le maximum global échoue (régime modérément diffus), la statistique de Higher Criticism qui normalise les excès empiriques sur l'ensemble des quantiles intermédiaires atteint la frontière optimale de détection.
- **Martingales de test, $e$-valeurs et inférence séquentielle** :
  - *Titre* : Safe Testing.
  - *Auteurs* : Peter Grünwald, Rianne de Heide et Wouter M. Koolen.
  - *Année* : 2024 (*Journal of the Royal Statistical Society: Series B*, prépublication 2019).
  - *Ce qui y est démontré* : Développe la théorie des $e$-valeurs et des martingales de test optimales (CRO / croissance d'entropie relative), démontrant comment construire des statistiques séquentielles valides sous des hypothèses nulles composites qui maximisent la vitesse exponentielle de détection sous l'alternative.
- **Concentration non-asymptotique de la fonction de répartition empirique** :
  - *Titre* : The Tight Constant in the Dvoretzky-Kiefer-Wolfowitz Inequality.
  - *Auteurs* : Pascal Massart.
  - *Année* : 1990 (*The Annals of Probability*).
  - *Ce qui y est démontré* : Démontre que pour tout échantillon i.i.d. de taille $n$, $\mathbb{P}(\sup_x |\hat{F}_n(x) - F_0(x)| > \eta) \le 2 e^{-2n\eta^2}$ avec la constante optimale exacte $2$, quantifiant précisément l'erreur d'étalonnage empirique du seuil $\hat{s}_\alpha$.
- **Régularisation de la matrice de covariance à échantillon fini $n < d$** :
  - *Titre* : A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices.
  - *Auteurs* : Olivier Ledoit et Michael Wolf.
  - *Année* : 2004 (*Journal of Multivariate Analysis*).
  - *Ce qui y est démontré* : Démontre l'optimalité quadratique d'une combinaison convexe optimale entre la matrice de covariance empirique $\hat{\Sigma}_n$ et l'identité lorsque la dimension $d$ dépasse la taille d'échantillon $n$, garantissant l'inversibilité et éliminant le noyau empirique dégénéré.

FIN-DE-REPONSE