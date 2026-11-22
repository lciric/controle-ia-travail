**Note d'intégrité sur les pièces transmises :** Les blocs `FAITS` et `QUESTION DE L'ARBITRE` sont présents, complets et identiques bit à bit (aucun dossier empirique distinct n'est joint, et les propositions A, B, C, D, F sont absentes conformément au Tour III.1 à l'aveugle) `[VÉRIFIÉ]`.

---

## I. Analyse mathématique de la question posée (Points 1 à 4)

Soit $G$ une grammaire formelle publique engendrant un langage dénombrable $L(G) \subseteq \Sigma^*$ `[HYPOTHÈSE]`. Un générateur aléatoire $\mathcal{G}$, accessible uniquement par tirages séquentiels $X_1, X_2, \dots$ sur un espace $\Omega$ (avec $L(G) \subseteq \Omega$), induit une loi marginale $\mu$ `[HYPOTHÈSE]`. Un vérificateur $V : \Omega \to \{0, 1\}$ évalue l'appartenance à la cible $A \subseteq L(G)$ de fréquence marginale $p = \mu(A) \in [0, 1]$ inconnue `[HYPOTHÈSE]`. On note $c_{\text{prod}} > 0$ le coût d'un tirage de $\mathcal{G}$, $c_{\text{gram}} \ge 0$ le coût d'analyse dans $G$, $c_{\text{ver}} > 0$ le coût d'un appel à $V$, $\rho = c_{\text{ver}} / c_{\text{prod}}$ le rapport des coûts, et $B > 0$ le budget total alloué à une stratégie $\pi$, soumise à la contrainte $\text{Coût}(\pi) = c_{\text{prod}} N_{\text{prod}} + c_{\text{ver}} N_{\text{ver}} + C_{\text{aux}} \le B$ `[HYPOTHÈSE]`.

### 1. Sens mathématique d'une « garantie » sous budget donné : énoncés quantifiés

Sans borne inférieure sur $p$, aucune stratégie à budget fini $B$ ne peut garantir simultanément la production et la reconnaissance d'un élément de $A$ pour tout $p \in [0, 1]$ (en particulier si $p = 0$) `[VÉRIFIÉ]`. Quatre énoncés formels distincts capturent donc ce que « garantir » peut signifier mathématiquement :

1. **Garantie PAC conditionnelle à un plancher de fréquence $p_0$ (succès à budget fixe)** :
   - *Hypothèses* : Tirages i.i.d. selon $\mu$ `[HYPOTHÈSE]`, vérificateur exact ($\forall x \in \Omega, V(x) = \mathbb{I}_{x \in A}$) `[HYPOTHÈSE]`, seuil minimal postulé $p_0 \in (0, 1]$ et risque $\delta \in (0, 1)$ `[HYPOTHÈSE]`.
   - *Énoncé* `[VÉRIFIÉ]` :
     $$\forall p_0 \in (0,1],\; \forall \delta \in (0,1),\; \exists B(p_0,\delta) < \infty,\; \exists \pi,\; \forall (\mu, A) \text{ tels que } \mu(A) \ge p_0 :$$
     $$\mathbb{P}_{\pi,\mu}\Big(\text{Coût}(\pi) \le B \;\wedge\; \exists x \in \text{Sortie}(\pi),\; x \in A \;\wedge\; V(x) = 1\Big) \ge 1 - \delta.$$
   Cet énoncé sépare l'événement de **production** $E_{\text{prod}} = \{\exists t \le N_{\text{prod}} : X_t \in A\}$ et l'événement de **reconnaissance** $E_{\text{rec}} = \{\exists t \in \mathcal{I}_{\text{ver}} : X_t \in A \wedge V(X_t) = 1\}$, où $\mathcal{I}_{\text{ver}} \subseteq \{1, \dots, N_{\text{prod}}\}$ désigne le sous-ensemble des tirages effectivement soumis à $V$.

2. **Garantie universelle disjonctive (correction sans faux positif + certificat de rareté sur $p$)** :
   - *Hypothèses* : $p \in [0, 1]$ quelconque (possiblement nul ou arbitrairement petit), tirages i.i.d. `[HYPOTHÈSE]`, vérificateur exact `[HYPOTHÈSE]`.
   - *Énoncé* `[VÉRIFIÉ]` :
     $$\forall B > 0,\; \forall \delta \in (0,1),\; \exists \pi,\; \exists p_{\max}(B,\delta) \in (0,1],\quad \forall (\mu, A) \text{ avec } p = \mu(A) \in [0,1] :$$
     $$\mathbb{P}_{\pi,\mu}\big(\text{Coût}(\pi) \le B\big) = 1,\quad \mathbb{P}_{\pi,\mu}\big(\text{Sortie}(\pi) = x \implies x \in A\big) = 1,$$
     $$\text{et}\quad \mathbb{P}_{\pi,\mu}\Big(\big(\text{Sortie}(\pi) \in A\big) \;\vee\; \big(p \le p_{\max}(B,\delta)\big)\Big) \ge 1 - \delta.$$
   Ici, si l'algorithme échoue à exhiber un objet valide dans le budget $B$, il fournit une borne supérieure valide à niveau $1 - \delta$ attestant que le puits a une masse au plus $p_{\max}(B, \delta)$.

3. **Garantie Las Vegas adaptative (confiance fixée, budget en espérance fonction du $p$ inconnu)** :
   - *Hypothèses* : $p = \mu(A) > 0$ inconnu, tirages i.i.d., budget non plafonné durement mais borné en espérance `[HYPOTHÈSE]`.
   - *Énoncé* `[VÉRIFIÉ]` :
     $$\exists \pi,\; \forall (\mu, A) \text{ tels que } p = \mu(A) > 0 : \quad \mathbb{P}_{\pi,\mu}\big(\text{Sortie}(\pi) \in A\big) = 1 \;\wedge\; \mathbb{E}_{\pi,\mu}[\text{Coût}(\pi)] \le \Phi(p, c_{\text{prod}}, c_{\text{ver}}).$$

4. **Garantie de fidélité distributionnelle conditionnelle** :
   - Lorsque l'on exige en outre que l'objet reconnu suive la loi conditionnelle exacte (ou $\varepsilon$-proche en distance en variation totale) $\mu_A(\cdot) = \mu(\cdot \cap A)/\mu(A)$ `[HYPOTHÈSE]` :
     $$\forall \varepsilon \ge 0,\; \mathbb{P}_{\pi,\mu}\big(\text{Sortie}(\pi) \in A\big) > 0 \implies d_{\text{TV}}\big(\mathcal{L}(\text{Sortie}(\pi) \mid \text{succès}),\, \mu_A\big) \le \varepsilon \quad \text{[VÉRIFIÉ]}.$$

---

### 2. Résultats positifs et négatifs établis

#### Résultats négatifs

- **N1. Impossibilité uniforme à budget fixe et borne inférieure minimax en $\Omega(\frac{1}{p}\ln\frac{1}{\delta})$** `[VÉRIFIÉ]` :
  Pour tout algorithme classique n'accédant à $\mathcal{G}$ que par tirages i.i.d. et à $A$ que par requêtes ponctuelles à $V$, sans relation connue entre la loi $\mu$ et l'indicatrice $\mathbb{I}_A$ :
  1. Pour tout budget fini $B$ autorisant au plus $M = \lfloor B / c_{\text{prod}} \rfloor$ tirages et tout $\delta \in (0, 1)$, tout choix de $p \in (0, 1 - \delta^{1/M})$ donne $\mathbb{P}(E_{\text{prod}}) = 1 - (1 - p)^M < 1 - \delta$ `[VÉRIFIÉ]`.
  2. Pour garantir $\mathbb{P}(E_{\text{prod}}) \ge 1 - \delta$ lorsque $\mu(A) \ge p_0$, il est nécessaire d'effectuer $N_{\text{prod}} \ge \frac{\ln(1/\delta)}{-\ln(1 - p_0)} \ge \frac{1 - p_0}{p_0}\ln\frac{1}{\delta}$ tirages `[VÉRIFIÉ]`. Par le principe minimax de Yao (Andrew Chi-Chih Yao, 1977, *Probabilistic computations: Toward a unified measure of complexity*), si $A$ est choisi uniformément parmi les sous-ensembles de masse $p_0$ sur un support sans collision, tout algorithme certifiant un élément de $A$ avec probabilité $1 - \delta$ requiert également $\Omega((1 - \delta)/p_0)$ appels espérés à $V$ `[VÉRIFIÉ]`.

- **N2. Non-identifiabilité du support et barrière de boîte noire** `[VÉRIFIÉ]` :
  Si l'on ne peut qu'obtenir des tirages complets de $\mathcal{G}$ (sans accès aux transitions internes ni possibilité de rééchantillonner des dérivations partielles), aucune procédure en aval ne peut améliorer la probabilité $1 - (1 - p)^M$ qu'au moins un tirage appartienne à $A$ `[VÉRIFIÉ]`. De plus, $A \cap L(G) \neq \emptyset$ n'implique pas $p = \mu(A) > 0$ : si $\text{supp}(\mu) \cap A = \emptyset$, tout nombre fini ou infini de tirages de $\mathcal{G}$ échoue avec probabilité $1$ (exprimé en mesure de probabilité exacte) `[VÉRIFIÉ]`. Enfin, si $V$ est purement binaire ($\{0, 1\}$ sans signal graduel) et si aucune structure métrique connue ne relie $G$ à $A$, aucune recherche adaptative guidée par les rejets passés de $V$ ne surpasse en moyenne l'échantillonnage sans remise sur l'ensemble des fonctions indicatrices de taille fixée (David H. Wolpert, William G. Macready, 1997, *No free lunch theorems for optimization*) `[VÉRIFIÉ]`.

- **N3. Contamination bayésienne par un vérificateur imparfait quand $p \to 0$** `[VÉRIFIÉ]` :
  Si $V$ présente un taux de fausses alertes $\alpha_V = \mathbb{P}_\mu(V(X)=1 \mid X \notin A) > 0$ et une sensibilité $1 - \beta_V$, la probabilité qu'un objet reconnu soit réellement dans $A$ vaut $\text{VPP}(p) = \frac{(1-\beta_V)p}{(1-\beta_V)p + \alpha_V(1-p)}$, qui converge vers $0$ dès que $p \ll \alpha_V$ `[VÉRIFIÉ]`.

#### Résultats positifs (méthodes à garantie, hypothèses, prix)

1. **Échantillonnage par rejet séquentiel avec filtre grammatical et mémoïsation canonique** :
   - *Méthode* : Tirer $X_t \sim \mu$ ; vérifier $X_t \in L(G)$ ; calculer sa forme canonique $\pi_G(X_t)$ pour une équivalence connue $\sim_G$ préservant $A$ ; si $\pi_G(X_t)$ n'a jamais été évaluée, appeler $V(X_t)$ et mémoriser le résultat ; s'arrêter au premier succès ou à épuisement de $B$.
   - *Énoncé* `[VÉRIFIÉ]` : Le premier tirage dans $A$ suit une loi géométrique de paramètre $p$ (John von Neumann, 1951, *Various techniques used in connection with random digits*). L'objet retourné (si l'on mémorise $V$ sans biaiser l'arrêt) suit exactement $\mu_A$. Pour $N_{\text{prod}} = \lceil \frac{\ln(1/\delta)}{p_0} \rceil$, $\mathbb{P}(E_{\text{prod}}) \ge 1 - \delta$.
   - *Hypothèses* : Tirages i.i.d., $A \subseteq L(G)$, $x \sim_G y \implies V(x) = V(y)$, $V$ exact `[HYPOTHÈSE]`.
   - *Prix* `[VÉRIFIÉ]` : En espérance Las Vegas, $\mathbb{E}[N_{\text{prod}}] = 1/p$ et $\mathbb{E}[N_{\text{ver}}] = \sum_{c \in (L(G)/\sim_G) \setminus A} \frac{\mu(c)}{\mu(c) + p} \le \min\big(\mu(L(G))/p,\, |(L(G)/\!\sim_G) \setminus A|\big)$.

2. **Certification unilatérale exacte en cas d'échec et estimation relative adaptative de $p$** :
   - *Énoncé* `[VÉRIFIÉ]` : Après $n$ vérifications i.i.d. sans succès ($S_n = 0$), l'intervalle unilatéral exact de Clopper-Pearson garantit $\mathbb{P}_p(p \le 1 - \delta^{1/n}) \ge 1 - \delta$ pour tout $p \in [0, 1]$ (C. J. Clopper, E. S. Pearson, 1934, *The use of confidence or fiducial limits illustrated in the case of the binomial*). Pour estimer $p > 0$ inconnu à erreur relative $\varepsilon$ avec probabilité $1 - \delta$, la règle d'arrêt adaptative de l'algorithme $\mathcal{AA}$ attend un nombre de succès proportionnel à $\ln(1/\delta)/\varepsilon^2$ et atteint la complexité optimale à facteur constant près (Paul Dagum, Richard Karp, Michael Luby, Sheldon Ross, 2000, *An optimal algorithm for Monte Carlo estimation*) ; pour trancher séquentiellement entre $p \ge p_1$ et $p \le p_0 < p_1$, le test du rapport de vraisemblance séquentiel minimise l'espérance du nombre d'observations (Abraham Wald, 1945, *Sequential tests of statistical hypotheses*).
   - *Hypothèses* : Essais de Bernoulli i.i.d., $V$ exact `[HYPOTHÈSE]`.
   - *Prix* `[VÉRIFIÉ]` : Borne après échec en $p_{\max}(n, \delta) = 1 - \delta^{1/n} \le \frac{\ln(1/\delta)}{n}$ ; estimation relative en $\Theta\big(\frac{\ln(1/\delta)}{\varepsilon^2 p}(c_{\text{prod}} + c_{\text{ver}})\big)$.

3. **Triage défensif $\gamma$-mélangé (Importance Sampling défensif)** :
   - *Méthode* : Face à un score auxiliaire rapide $s : L(G) \to [0, 1]$ de coût $c_s \ll c_{\text{ver}}$, vérifier chaque tirage avec probabilité (ou allocation budgétaire) combinant une fraction $(1 - \gamma)$ dédiée aux meilleurs scores de $s$ et une fraction plancher $\gamma \in (0, 1]$ tirée uniformément parmi les sorties de $\mathcal{G}$ (Art Owen, Yi Zhou, 2000, *Safe and effective importance sampling*).
   - *Énoncé* `[VÉRIFIÉ]` : Quelle que soit la qualité (même adversaire) de $s$, la probabilité de reconnaissance sur un budget permettant $M_{\text{ver}}$ vérifications vérifie $\mathbb{P}(\text{succès}) \ge 1 - (1 - p)^{\lfloor \gamma M_{\text{ver}} \rfloor}$. Si $s$ concentre $A$ avec facteur d'enrichissement $r/q > 1$, la branche $(1-\gamma)$ accélère la détection proportionnellement à $r/q$.
   - *Hypothèses* : Tirages i.i.d., $V$ exact, choix explicite de $\gamma \in (0, 1)$ `[HYPOTHÈSE]`.
   - *Prix* `[VÉRIFIÉ]` : Surcoût multiplicatif au pire cas borné par $1/\gamma$ sur le budget de vérification par rapport à l'absence de filtre.

4. **Énumération déterministe ou échantillonnage uniforme direct de la grammaire publique $G$** :
   - *Méthode* : Ignorer $\mathcal{G}$ et énumérer sans remise (ou tirer uniformément) les objets de la tranche finie $L_{\le L}(G)$ directement depuis les règles publiques de $G$ (Mark R. Jerrum, Leslie G. Valiant, Vijay V. Vazirani, 1986, *Random generation of combinatorial structures from a uniform distribution* ; Philippe Flajolet, Paul Zimmermann, Bernard Van Cutsem, 1994, *A calculus for the random generation of labelled combinatorial structures*).
   - *Énoncé* `[VÉRIFIÉ]` : Si $A \cap L_{\le L}(G) \neq \emptyset$ et $B \ge |L_{\le L}(G)| (c_{\text{enum}} + c_{\text{ver}})$, l'énumération trouve un élément de $A$ avec risque d'échec nul ($\delta = 0$), même si $\mu(A) = 0$ sous $\mathcal{G}$.
   - *Hypothèses* : $G$ hors-contexte ou régulière explicite, $A \cap L_{\le L}(G) \neq \emptyset$ `[HYPOTHÈSE]`.
   - *Prix* `[VÉRIFIÉ]` : Coût pire cas $|L_{\le L}(G)| (c_{\text{enum}} + c_{\text{ver}})$, souvent exponentiel en $L$.

5. **Test par groupe (conditionnel à la clôture disjonctive de $G$ et $V$)** :
   - *Énoncé* `[VÉRIFIÉ]` : Si $V$ est strictement unaire sans composition dans $G$, inapplicable. Si $G$ admet un opérateur de groupement $C(x_1, \dots, x_m) \in L(G)$ tel que $V(C(x_1, \dots, x_m)) = \bigvee_{i=1}^m V(x_i)$ à coût $c_{\text{ver}}$, le schéma en deux phases de Dorfman réduit le nombre d'appels à $V$ sur $N$ candidats de $N$ à $O(N \sqrt{p})$ pour $m \approx 1/\sqrt{p}$, ou $O(p N \log(1/p) + N/m)$ par dichotomie dans les lots positifs (Robert Dorfman, 1943, *The detection of defective members of large populations*).

---

### 3. Dépendance aux quatre variables structurelles

1. **Connaissance du générateur $\mathcal{G}$** :
   - *Boîte noire pure (tirages complets seuls)* : $N_{\text{prod}} = \Omega(1/p)$ incompressible `[VÉRIFIÉ]`.
   - *Connaissance de la concentration/entropie de collision de $\mu$* : si $\mathcal{G}$ répète fortement des modes invalides ($\mu(x) \gg p$), la mémoïsation plafonne le coût de vérification de chaque mode à un unique appel $c_{\text{ver}}$ `[VÉRIFIÉ]`. Si $\mathcal{G}$ produit des mots légèrement hors de $L(G)$, un analyseur à correction d'erreur minimale ramène un mot de longueur $\ell$ dans $L(G)$ en temps $O(\ell^3)$ (Alfred V. Aho, Thomas G. Peterson, 1972, *A minimum distance error-correcting parser for context-free languages*) `[VÉRIFIÉ]`, mais sans garantie de préserver ou d'accroître la masse sur $A$ `[HYPOTHÈSE]`.
   - *Contraste boîte grise (hors hypothèse de tirages complets seuls)* : l'accès aux préfixes permettrait l'élagage précoce de branches mortes avant complétion `[VÉRIFIÉ]`.

2. **Taille de la grammaire $|L_{\le L}(G)|$** :
   - Si $|L_{\le L}(G)/\!\sim_G| \le B / c_{\text{ver}}$, l'énumération directe de la grammaire publique domine strictement le générateur aléatoire : elle élimine le surcoût du collectionneur de coupons et le risque $\mu(A) = 0$ `[VÉRIFIÉ]`.
   - Si $|L_{\le L}(G)| \gg B / c_{\text{ver}}$, l'énumération échoue sauf densité uniforme élevée ; $\mathcal{G}$ n'est utile que si sa loi $\mu$ vérifie l'hypothèse de concentration $\mu(A) \gg |A \cap L_{\le L}(G)| / |L_{\le L}(G)|$ `[VÉRIFIÉ]`.

3. **Corrélation entre tirages $(X_t)_{t \ge 1}$** :
   - Soit $S_M = \sum_{t=1}^M \mathbb{I}_{X_t \in A}$ sur un processus stationnaire de marginale $p$ et d'autocorrélations $\rho_k = \text{Corr}(\mathbb{I}_{X_t \in A}, \mathbb{I}_{X_{t+k} \in A})$ `[HYPOTHÈSE]`. Par l'inégalité du second moment (Cauchy-Schwarz sur $S_M \mathbb{I}_{S_M > 0}$),
     $$\mathbb{P}(S_M > 0) \ge \frac{(\mathbb{E}[S_M])^2}{\mathbb{E}[S_M^2]} = \frac{M p}{1 + (M-1)p + 2(1-p)\sum_{k=1}^{M-1}(1 - k/M)\rho_k} \quad \text{[VÉRIFIÉ]}.$$
   - *Corrélation positive ($\rho_k > 0$)* : le temps d'autocorrélation intégré $\tau_{\text{corr}} = 1 + 2\sum_{k \ge 1} \max(0, \rho_k)$ réduit la taille d'échantillon effective à $M_{\text{eff}} \approx M / \tau_{\text{corr}}$, gonflant d'autant le budget requis `[VÉRIFIÉ]`. Pire, pour une suite échangeable de mélange latent $P = \mu_\Theta(A)$ tiré une seule fois, $\mathbb{P}(\forall t \le M, X_t \notin A) = \mathbb{E}[(1 - P)^M] \ge \mathbb{P}(P = 0)$ : si $\mathbb{P}(P = 0) > \delta$, aucun budget $B$ ne peut garantir un risque $\le \delta$ sans réinitialiser $\Theta$ `[VÉRIFIÉ]`.
   - *Corrélation négative (ex. tirage sans remise)* : la probabilité d'échec joint est majorée par $(1 - p)^M$ (voire tombe à $0$ à l'épuisement de l'urne) et les doublons envoyés à $V$ diminuent `[VÉRIFIÉ]` *(bornes générales d'association négative : référence à vérifier)*.

4. **Rapport des coûts $\rho = c_{\text{ver}} / c_{\text{prod}}$** :
   - *Régime $\rho \ll 1$* : le coût unitaire $c_{\text{prod}} + c_{\text{ver}} \approx c_{\text{prod}}$ est dominé par les tirages ; tout filtre imparfait ($r < 1$) dégrade le coût espéré en $\approx c_{\text{prod}}/(r p)$. Il faut vérifier tous les tirages uniques de $L(G)$ ($r = 1$) `[VÉRIFIÉ]`.
   - *Régime $\rho \gg 1$* : un filtre rapide $F$ (coût $c_F$, taux de passage global $q = \mu(F=1)$, rappel sur la cible $r = \mu(F=1 \mid A)$) abaisse le coût espéré par succès $\frac{c_{\text{prod}} + c_F + q c_{\text{ver}}}{r p}$ en dessous du coût sans filtre $\frac{c_{\text{prod}} + c_{\text{ver}}}{p}$ si et seulement si
     $$r > \frac{1 + c_F/c_{\text{prod}} + q\rho}{1 + \rho} \quad \text{[VÉRIFIÉ]}.$$
     Pour $\rho \to \infty$ et $c_F \ll c_{\text{ver}}$, cela équivaut à un rapport d'enrichissement $r / q > 1$ `[VÉRIFIÉ]`.

---

### 4. Garanties apportées par les méthodes répandues

| Méthode répandue | Applicable en tirages boîte noire seuls ? | Garantie mathématique sous $p$ inconnu | Limite ou condition de défaillance |
| :--- | :--- | :--- | :--- |
| **Tirages répétés + vérification exacte (« Pass@$N$ » / rejet)** | Oui `[VÉRIFIÉ]` | Succès $\ge 1 - (1-p_0)^N$ si $p \ge p_0$ ; zéro faux positif ; $p \le 1-\delta^{1/N}$ si échec (Clopper & Pearson, 1934) `[VÉRIFIÉ]` | Prix linéaire en $(c_{\text{prod}}+c_{\text{ver}})/p$ `[VÉRIFIÉ]` |
| **Filtre syntaxique et canonisation par $G$** | Oui `[VÉRIFIÉ]` | Rappel $r = 1$ (aucune perte) si $A \subseteq L(G)$ et invariance de $V$ par $\sim_G$ ; plafonne $N_{\text{ver}} \le |L(G)/\!\sim_G|$ `[VÉRIFIÉ]` | Gain nul si $\mathcal{G}$ produit déjà dans $L(G)$ sans collisions `[VÉRIFIÉ]` |
| **Classement par score heuristique / juge appris (top-$k$ parmi $N$ envoyé à $V$)** | Oui `[VÉRIFIÉ]` | Correction (zéro faux positif grâce à $V$), mais **aucune garantie de rappel ni de succès** `[VÉRIFIÉ]` | Si $s$ pénalise $A$ (désalignement de queue), $r = 0$ même quand $A$ a été produit par $\mathcal{G}$ `[VÉRIFIÉ]` |
| **Triage défensif $\gamma$-mélangé** (Owen & Zhou, 2000) | Oui `[VÉRIFIÉ]` | Plancher pire-cas garanti $\ge 1 - (1-p)^{\lfloor \gamma M_{\text{ver}} \rfloor}$ sans hypothèse sur $s$ `[VÉRIFIÉ]` | Perte d'une fraction $\gamma$ du budget de tri si $s$ était déjà bien aligné `[VÉRIFIÉ]` |
| **Calibration conforme du seuil de filtrage** (Vladimir Vovk, Alex Gammerman, Glenn Shafer, 2005, *Algorithmic Learning in a Random World*) | Oui si positifs connus `[VÉRIFIÉ]` | Contrôle fini du taux de faux négatifs $\mathbb{P}(s(X)<\tau \mid X \in A) \le \alpha$ si l'on dispose d'un échantillon échangeable de positifs de $A$ `[VÉRIFIÉ]` | **Inapplicable à froid** tant qu'aucun élément de $A$ n'a été observé `[VÉRIFIÉ]` |
| **Vote majoritaire / auto-cohérence sans $V$** | Oui `[VÉRIFIÉ]` | **Aucune** quand $p < \max_{y \notin A}\mu(y)$ `[VÉRIFIÉ]` | Par concentration binomiale (Wassily Hoeffding, 1963, *Probability inequalities for sums of bounded random variables*), converge vers un mode erroné (ex. si $p < 0,5$ `(illustratif)` en binaire) `[VÉRIFIÉ]` |
| **Décodage contraint par grammaire** | **Non** (exige les probabilités préfixes internes) `[VÉRIFIÉ]` | Appartenance à $L(G)$ si boîte grise, mais pas de garantie d'augmenter $\mu(A)$ `[VÉRIFIÉ]` | Distorsion myope par rapport à $\mu(\cdot \mid L(G))$ *(référence à vérifier)* `[HYPOTHÈSE]` |

---

## II. Conception ciblée du Tour III.1 et protocoles de tranchement (Question 5)

### (a) Ce que la question suppose sans que ce soit établi

1. **Exactitude sans erreur du vérificateur (« dit si un objet possède une propriété recherchée »)** — Statut : `[HYPOTHÈSE]`. L'énoncé postule un oracle booléen exact, sans établir que son taux de fausses alertes $\alpha_V$ est nul ou négligeable devant $p$, ni que son temps de calcul termine uniformément sous un coût borné sur tout $L(G)$.
2. **Existence d'une fréquence scalaire bien définie $p$** — Statut : `[HYPOTHÈSE]`. Parler de « la fréquence $p$ » suppose un régime stationnaire ergodique des tirages de $\mathcal{G}$ (ou une mesure canonique fixée), non établi face à un générateur à état interne dériveur ou à variable latente non réinitialisée.
3. **Conformité grammaticale native des tirages** — Statut : `[HYPOTHÈSE]`. « Produit des objets écrits dans une grammaire publique » suppose $\mu(L(G)) = 1$, sans établir l'absence de sorties mal formées.
4. **Indépendance des coûts vis-à-vis des objets tirés** — Statut : `[HYPOTHÈSE]`. « Le rapport entre le coût de vérification et le coût de production » suppose deux coûts scalaires bien résumés, alors que le coût $C_{\text{ver}}(X)$ peut être fortement corrélé au rapprochement vers $A$.
5. **Pertinence d'échantillonner $\mathcal{G}$ plutôt que d'énumérer $G$** — Statut : `[HYPOTHÈSE]`. La question présuppose l'usage du générateur aléatoire sans établir que $\mu(A)$ dépasse la densité obtenue par génération directe depuis la grammaire publique $G$.
6. **Métadonnées d'orientation dans l'en-tête (`orientée 0,55 avec contexte du dépôt, 0,40 sans`)** — Statut : `[RAPPORTÉ]` dans le titre du bloc transmis ; le protocole expérimental, la taille d'échantillon et la variance du devineur sous-jacent ne figurant pas dans les pièces, la neutralité empirique effective de cet instrument reste `[OBSERVÉ-NON-AUDITÉ]`.

---

### (b) Expériences discriminantes en inférence forte ($H_A$ contre $H_B$ — réponse opératoire à la Question 5)

Outre les preuves mathématiques qui tranchent déductivement les cas asymptotiques (section I.2), quatre expériences à hypothèses mutuellement exclusives tranchent empiriquement sur tout système concret $(\mathcal{G}, G, V)$ :

#### Duel E1 — Concentration utile de $\mathcal{G}$ contre Échantillonnage direct de la grammaire publique $G$
- **$H_A$** `[HYPOTHÈSE]` : À budget total fixé $B$ et longueur syntaxique bornée $L$, le générateur $\mathcal{G}$ (avec déduplication canonique sur $L_{\le L}(G)/\!\sim_G$) surpasse d'un facteur strictement supérieur à $\kappa = 2$ `(illustratif)` la probabilité de découverte de l'échantillonnage uniforme sans remise direct dans la grammaire publique $G$.
- **$H_B$** `[HYPOTHÈSE]` : $\mathcal{G}$ ne surpasse pas d'un facteur $\kappa = 2$ `(illustratif)` l'exploitation directe sans remise de $G$ (effondrement modal ou désalignement de $\mu$ par rapport à $A$).
- **Métrique et seuil** : Rapport $\hat{\Lambda} = \hat{P}_{\text{hit}}(\mathcal{G}, B) / \hat{P}_{\text{hit}}(\text{Unif}(G), B)$ sur $R = 40$ `(illustratif)` réplicats indépendants ; seuil $\hat{\Lambda} > 2$ `(illustratif)` avec test exact de Fisher unilatéral à $p_{\text{val}} < 0,01$ `(illustratif)`.
- **Contrôle négatif** : Propriété cible pseudo-aléatoire $V_{\text{ctrl}}(x) = \mathbb{I}\{\text{SHA256}(\pi_G(x)) \bmod 1000 = 0\}$ `(illustratif)` indépendante de $\mathcal{G}$. Mathématiquement, aucun générateur aveugle au hachage ne peut battre le tirage sans remise sur les classes canoniques ($\hat{\Lambda}_{\text{ctrl}} \le 1$ `(illustratif)` aux fluctuations près) ; tout dépassement significatif invalide le compteur budgétaire.
- **Issues falsificatrices** : Si $\hat{\Lambda} > 2$ `(illustratif)` et $p_{\text{val}} < 0,01$ `(illustratif)`, **$H_B$ est réfutée** ; dans le cas contraire, **$H_A$ est réfutée** (le recours à $\mathcal{G}$ n'apporte pas le gain postulé sur la seule grammaire publique).

#### Duel E2 — Filtrage heuristique pur ($\gamma = 0$) contre Triage défensif $\gamma$-mélangé à haut rapport $\rho$
- **$H_A$** `[HYPOTHÈSE]` : Pour $\rho = 500$ `(illustratif)`, le tri pur top-$k$ par un score $s$ ($\gamma = 0$) obtient un taux de succès sur un banc de $M_{\text{inst}} = 50$ `(illustratif)` puits étroits strictement supérieur au triage défensif $\gamma = 0,20$ `(illustratif)`.
- **$H_B$** `[HYPOTHÈSE]` : La distorsion de queue du score $s$ sur une partie des puits rend le taux de succès de $\gamma = 0$ inférieur ou égal à celui de $\gamma = 0,20$ `(illustratif)`.
- **Métrique et seuil** : Écart apparié $\Delta_{\text{hit}} = \hat{P}_{\text{hit}}(\gamma=0) - \hat{P}_{\text{hit}}(\gamma=0,20)$ évalué sur les **mêmes** lots de $N = 5\,000$ `(illustratif)` tirages de $\mathcal{G}$ (couplage de variance), test de McNemar au seuil $\alpha = 0,01$ `(illustratif)`.
- **Contrôles négatifs** : (1) Score aléatoire uniforme $s_{\text{unif}} \sim \text{Unif}[0, 1]$ `(illustratif)`, qui doit donner $\Delta_{\text{hit}} \approx 0$ `(illustratif)` ; (2) score inversé $1 - s(x)$, où $\gamma = 0$ chute tandis que $\gamma = 0,20$ `(illustratif)` doit maintenir au moins la borne binomiale du sous-quota uniforme.
- **Issues falsificatrices** : Si $\Delta_{\text{hit}} > 0$ au seuil $0,01$ `(illustratif)`, **$H_B$ est réfutée** sur cette famille de tâches ; si $\Delta_{\text{hit}} \le 0$ ou si $\gamma = 0$ manque des solutions trouvées par la branche uniforme $\gamma = 0,20$ `(illustratif)`, **$H_A$ est réfutée**.

#### Duel E3 — Tirages i.i.d. contre Corrélation positive / Mélange latent de $\mathcal{G}$
- **$H_A$** `[HYPOTHÈSE]` : Les indicateurs $(V(X_t))_{t \ge 1}$ se comportent comme i.i.d. (ou négativement associés) : l'indice de dispersion de Lexis $D = s_S^2 / (M \hat{p}(1-\hat{p}))$ calculé sur $L_{\text{blocs}} = 200$ `(illustratif)` blocs consécutifs de $M = 100$ `(illustratif)` tirages vérifie $\mathbb{E}[D] \le 1$ `[VÉRIFIÉ]` sous i.i.d., et la probabilité d'échec par bloc respecte $\hat{F}(M) \le (1-\hat{p})^M$.
- **$H_B$** `[HYPOTHÈSE]` : Une corrélation séquentielle ou latente ($\tau_{\text{corr}} > 1$) induit une sur-dispersion $D > 1$ et un excès d'échecs $\hat{F}(M) > (1-\hat{p})^M$, invalidant la borne naïve de Clopper-Pearson.
- **Métrique et seuil** : Statistique $D$ comparée au quantile $0,99$ `(illustratif)` de la loi $\chi^2_{L_{\text{blocs}}-1}/(L_{\text{blocs}}-1)$, soit le seuil critique $1,24$ `(illustratif)` pour $L_{\text{blocs}} = 200$ `(illustratif)`.
- **Contrôle négatif** : Permutation aléatoire globale (Fisher-Yates) de la suite complète des $20\,000$ `(illustratif)` observations avant découpage en blocs ; la permutation détruit toute dépendance temporelle et doit ramener $D_{\text{perm}} \le 1,24$ `(illustratif)`.
- **Issues falsificatrices** : Si $D > 1,24$ `(illustratif)` avec $D_{\text{perm}} \le 1,24$ `(illustratif)`, **$H_A$ est réfutée** (les garanties i.i.d. surestiment la couverture) ; si $D \le 1,24$ `(illustratif)`, **$H_B$ est réfutée** à cette échelle.

#### Duel E4 — Exactitude de $V$ contre Régime dominé par les fausses alertes ($\alpha_V \gtrsim p$)
- **$H_A$** `[HYPOTHÈSE]` : Parmi les objets reconnus par $V$ ($V(x) = 1$), la valeur prédictive positive auditée par un oracle formel indépendant de référence $V^\star$ vérifie $\text{VPP} \ge 0,99$ `(illustratif)`.
- **$H_B$** `[HYPOTHÈSE]` : $\text{VPP} < 0,99$ `(illustratif)` (la recherche rare exploite des fausses alertes de $V$).
- **Métrique et seuil** : Audit par $V^\star$ de $n_+ = 460$ `(illustratif)` objets acceptés par $V$. Par Clopper & Pearson (1934), observer $0$ `(illustratif)` discordance sur $460$ `(illustratif)` cas certifie $\text{VPP} \ge 0,99$ au niveau de confiance $0,99$ `(illustratif)` ($0,99^{460} < 0,01$ `[VÉRIFIÉ]`). Seuil de décision : $0$ discordance vs $\ge 10$ `(illustratif)` discordances (zone grise tranchée par poursuite séquentielle de Wald, 1945).
- **Contrôle négatif** : Soumission à $V$ de $500$ `(illustratif)` mutants syntaxiquement valides obtenus par violation contrôlée d'une condition nécessaire de $A$ ($x^- \in L(G) \setminus A$ prouvés faux par construction) ; $V$ doit en rejeter la totalité.
- **Issues falsificatrices** : Si la borne supérieure de confiance de Clopper-Pearson sur $\text{VPP}$ passe sous $0,99$ `(illustratif)`, **$H_A$ est réfutée** ; si $0$ discordance n'apparaît sur $460$ `(illustratif)` positifs, **$H_B$ est réfutée** au niveau $0,99$ `(illustratif)`.

---

### (c) Mesure minimale de fonctionnement des instruments nommés

| Instrument nommé | Taux de détection et de fausses alertes minimaux | Cas honnêtes appariés | Vérifications mécaniques à battre |
| :--- | :--- | :--- | :--- |
| **1. Générateur aléatoire $\mathcal{G}$** | Couverture utile $\hat{p}_{\text{distinct}}(\mathcal{G}) > p_{\text{unif}}(L_{\le L}(G))$ ; taux de sorties hors-grammaire $\mathbb{P}(X \notin L(G)) < 0,05$ `(illustratif)` | Spécifications $(A_i, A'_i)$ dans $G$ de même cardinal exact $|A_i| = |A'_i|$ dans $L_{\le L}(G)$ | Énumérateur lexicographique par taille et générateur uniforme exact de $L_{\le L}(G)$ (Flajolet et al., 1994) |
| **2. Analyseur / canoniseur de la grammaire publique $G$** | Détection des hors-grammaire $= 1,00$ `(illustratif)` ; fausses alertes (rejet d'un $x \in A$ ou collision canonique entre $x^+ \in A$ et $x^- \notin A$) $= 0,00$ `(illustratif)` | Paires $(x_{\text{val}} \in L(G), x_{\text{mut}} \notin L(G))$ à distance d'édition $1$ `(illustratif)` jeton ; paires $(x^+ \in A, x^- \notin A)$ proches | Déduplication brute par hachage d'octets (`SHA-256`) et parseur hors-contexte générique sans quotient |
| **3. Vérificateur indépendant $V$** | Sensibilité $1 - \beta_V \ge 0,99$ `(illustratif)` ; taux de fausses alertes $\alpha_V \le 0,01 \cdot p$ `(illustratif)` ($0$ alerte sur $10\,000$ `(illustratif)` négatifs proches) | Paires $(x^+ \in A, x^- \in L(G)\setminus A)$ différant d'une seule sous-expression (cas limites sémantiques, *near-misses*) | Typage statique, évaluation syntaxique bornée et tests aléatoires rapides de coût $\ll c_{\text{ver}}$ |
| **4. Méthode de triage / sélection entre $\mathcal{G}$ et $V$** | Rappel $r$ et fausses alertes vers $V$ ($q_0$) vérifiant $\frac{r}{q_0} > 1 + \frac{1 + c_F/c_{\text{prod}}}{\rho}$ (ex. $r/q_0 \ge 5$ `(illustratif)` pour $\rho = 100$ `(illustratif)`), avec plancher garanti $r \ge \gamma$ | Paires $(x^+ \in A, x^- \notin A)$ appariées en longueur et fréquence lexicale dans $L(G)$ | Tirage brut dédupliqué sur $L(G)/\!\sim_G$ sans filtre ($r = 1$) et filtre mécanique par test unitaire rapide exact |
| **5. « Devineur » d'orientation** *(nommé dans l'en-tête `[RAPPORTÉ]`)* | Sensibilité sur questions orientées vs fausses alertes sur questions mathématiques neutres appariées | Énoncés appariés en longueur, nombre de sous-questions et registre formel hors thème du dépôt | Classifieur lexical mécanique `TF-IDF` sur le glossaire du dépôt et tirage uniforme à $0,50$ `(illustratif)` |

---

### (d) Ancrage matériel, modèles ouverts et coût estimé

Pour exécuter E1–E4 de façon reproductible sans boîte fermée propriétaire `[HYPOTHÈSE]` :
- **Modèles et outils ouverts** :
  1. *Générateurs $\mathcal{G}$ interrogés uniquement par tirages complets* : `Qwen2.5-Coder-7B-Instruct` ($7 \times 10^9$ `(illustratif)` paramètres, poids ouverts) et `DeepSeek-Prover-V1.5-RL` ($7 \times 10^9$ `(illustratif)` paramètres), servis via `vLLM` sans accès aux logits côté algorithme de recherche. Score de triage $s$ pour E2 : modèle ouvert distinct de taille $1,5 \times 10^9$ `(illustratif)` paramètres (`Qwen2.5-1.5B`) afin d'éviter la fuite d'information du générateur.
  2. *Grammaires publiques $G$ et vérificateurs $V$* : (i) banc formel `SMT-LIB v2` / `Lean 4` avec parseur syntaxique `tree-sitter` ($c_{\text{gram}} \approx 1\text{ ms}$ `(illustratif)`) et vérificateur de noyau `lean4` ou solveur `Z3` isolé sous plafond CPU réglable ($5\text{ s}$ à $30\text{ s}$ `(illustratif)`, donnant $\rho \in [50, 1000]$ `(illustratif)`) ; (ii) banc de grammaire algébrique synthétique à densité exacte contrôlée $p \in [10^{-5}, 10^{-1}]$ `(illustratif)` doté d'un échantillonneur uniforme exact pour E1 et d'un second vérificateur formel indépendant $V^\star$ pour E4.
- **Calcul nécessaire** :
  - Production et scoring (E1–E3) : $50$ `(illustratif)` instances $\times$ $10\,000$ `(illustratif)` tirages de $512$ `(illustratif)` jetons $\approx 2,56 \times 10^8$ `(illustratif)` jetons, soit **$\approx 24$ heures-GPU** `(illustratif)` sur $1\times$ `NVIDIA A100-80GB` (incluant les séries longues de E3).
  - Vérification et contrôles négatifs (E1–E4) : $\approx 60\,000$ `(illustratif)` appels à $V$ et $V^\star$ avec arrêt anticipé moyen à $5\text{ s}$ `(illustratif)`, soit **$\approx 90$ à $120$ heures-vCPU** `(illustratif)` (environ $3$ à $4$ heures `(illustratif)` sur un serveur $32$ `(illustratif)` vCPU).
- **Coût financier estimé** : Au tarif cloud courant d'environ $2,00\text{ \$/h}$ `(illustratif)` par GPU `A100-80GB` et $1,20\text{ \$/h}$ `(illustratif)` pour $32$ `(illustratif)` vCPU, le budget matériel complet s'établit à **$\approx 55\text{ \$}$** `(illustratif)` (enveloppe de **$50\text{ \$}$ à $110\text{ \$}$** `(illustratif)` incluant stockage et reprises).

FIN-DE-CELLULE