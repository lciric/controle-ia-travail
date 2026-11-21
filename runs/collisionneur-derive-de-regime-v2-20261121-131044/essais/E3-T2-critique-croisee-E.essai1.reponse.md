État des pièces reçues : `FAITS`, `QUESTION DE L'ARBITRE` et les conceptions `A`, `B`, `C`, `D` sont présentes et complètes, sans coupure apparente `[VÉRIFIÉ]`.

---

## Sur la proposition A

### (a) Défauts de méthode : variables confondantes, vérités par construction et fuites

* **Variables confondantes :**
  1. *Biais de collisionneur par appariement sur la longueur réalisée* : Dans son protocole commun (§3c), A évalue les instruments sur des épisodes honnêtes appariés à « même tâche, même longueur, régime ancien contre régime nouveau » `[RAPPORTÉ]`. Or la longueur réalisée $L$ est une variable post-traitement produite conjointement par le régime $R$ et par la complexité latente d'exécution $U$ ($R \to L \leftarrow U$) `[HYPOTHÈSE]`. Conditionner sur $L = \ell$ ouvre un chemin collisionneur entre $R$ et $U$ `[VÉRIFIÉ]` et gomme artificiellement le changement de distribution marginale des longueurs, qui est pourtant l'une des sources de dérive signalées dans `FAITS` `[RAPPORTÉ]`.
  2. *Confusion entre réduction de variance et biais de dérive sur le jumeau* : A juge l'intérêt de l'appariement agent–jumeau par $\text{Var}(D) = 2\sigma^2(1-\rho)$ avec le seuil $\rho > 0{,}5$ (illustratif) `[RAPPORTÉ]`. Cette identité suppose l'égalité des variances marginales ($\sigma_{\text{agent}}^2 = \sigma_{\text{jumeau}}^2$) et ignore le décalage de moyenne $\Delta\mu = \mathbb{E}[S_{\text{agent}} - S_{\text{jumeau}}]$ `[VÉRIFIÉ]`. Lors d'une mise à jour de l'agent à jumeau fixe, on peut observer $\rho > 0{,}5$ (illustratif) tout en subissant un biais $\Delta\mu > 0$ qui triple le taux de fausses alertes `[HYPOTHÈSE]`.
  3. *Confusion entre prévalence globale et structure temporelle dans D4* : Faire varier la prévalence de sabotage de $0$ à $20\,\%$ (illustratif) `[RAPPORTÉ]` laisse indéterminé le taux de détection à $0\,\%$ sur le flux et confond une injection i.i.d. avec une salve concentrée.

* **Vérités par construction et inflation d'erreur :**
  1. *D4 appliqué à P1–P3* : Les seuils de P1, P2 et P3 dépendent uniquement des scores des témoins, disjoints du flux surveillé `[RAPPORTÉ]`. À tirage de témoins et jeu de sabotages fixés, leur taux de détection est algébriquement constant quelle que soit la prévalence de sabotage dans le flux `[VÉRIFIÉ]`. Inclure D4 dans le test de mort de P1 valide $H_A$ par construction sans éprouver la vulnérabilité réelle de P1 : la contamination ou le biais des témoins.
  2. *Arrêt optionnel non corrigé dans les duels (§4)* : A décrète invalide tout essai dont l'intervalle de Clopper-Pearson contient à la fois $1\,\%$ et $3\,\%$ (soit le triple de $1\,\%$), en prescrivant d'augmenter l'effectif `[RAPPORTÉ]`. Répéter un intervalle à niveau fixe jusqu'à exclusion d'une borne sans dépense d'erreur séquentielle gonfle le taux de faux rejet au-delà du niveau nominal `[VÉRIFIÉ]`.

* **Fuites entre construction et évaluation :**
  1. *Forme de frontière dans P3* : P3 pose $M = \max_t(S_t - b(t))$ avec une frontière $b(t)$ « fixée d'avance » `[RAPPORTÉ]`, sans réserver de partition pour apprendre $b(t)$. Choisir $b(t)$ après inspection des scores bruts par pas (§2) transfère l'information des longueurs cibles dans l'instrument évalué.
  2. *Temps d'arrêt dans P4 $\to$ P1* : Relancer P1 quand la martingale des témoins franchit $1/\delta$ `[RAPPORTÉ]` crée un biais de sélection vers le haut si la fenêtre de ré-étalonnage P1 inclut les témoins ayant déclenché l'arrêt `[VÉRIFIÉ]`.

### (b) Conditions probabilistes de perte de puissance ou de non-jugeabilité

* **Duels D1–D3 sous intervalle de Clopper-Pearson $[L_{\text{CP}}(X; m, \gamma), U_{\text{CP}}(X; m, \gamma)]$ avec $X \sim \text{Bin}(m, p)$ et cible $\alpha = 0{,}01$ `[VÉRIFIÉ]` :**
  * *Non-jugeabilité certaine* : Pour tout effectif $m$ tel que $\inf_{x : L_{\text{CP}}(x; m, \gamma) \le \alpha} U_{\text{CP}}(x; m, \gamma) \ge 3\alpha$, l'événement de succès $\{L_{\text{CP}}(X) \le \alpha \text{ et } U_{\text{CP}}(X) < 3\alpha\}$ est vide ($\mathbb{P}_p = 0$ pour tout $p \in [0,1]$).
  * *Sous-couverture en post-stratification (D1)* : L'estimateur repondéré $\hat{p}_w = \sum_{i=1}^m w_i \mathbb{I}(S_i > \hat{\tau})$ ($\sum_{i=1}^m w_i = 1$) vérifie $\text{Var}(\hat{p}_w) = \sum_{i=1}^m w_i^2 p_i(1-p_i)$. Dès que $m_{\text{eff}} = (\sum_i w_i)^2/\sum_i w_i^2 < m$, paramétrer Clopper-Pearson par $m$ sous-estime l'étalement d'un facteur $\sqrt{m/m_{\text{eff}}}$.
* **Critère P1 ($\hat{\tau}_{\text{P1}} = S_{(n+1-k)}^{\text{témoin}}$, $k = \max\{j \ge 1 : F_{\text{Bin}(n,\alpha)}(j-1) \le \delta\}$) `[VÉRIFIÉ]` :**
  * *Non-jugeabilité* : Ensemble admissible vide si $(1-\alpha)^n > \delta$, soit $n < \frac{\ln \delta}{\ln(1-\alpha)}$.
  * *Perte de puissance* : Lorsque $k = 1$ ($\hat{\tau}_{\text{P1}} \sim F_0^n$), sous loi alternative $F_1$, la puissance $\beta_n = \mathbb{E}_{T \sim F_0^n}[1 - F_1(T)] \to 0$ dès que $F_1(F_0^{-1}(1 - 1/n)) \to 1$.
* **Estimateur P2 ($\hat{\tau}_1 = \hat{m}_1 + (\hat{\tau}_0 - \hat{m}_0)\widehat{\text{IQR}}_1/\widehat{\text{IQR}}_0$) `[VÉRIFIÉ]` :**
  * *Non-jugeabilité* : $\mathbb{P}_{F_0^n}(\widehat{\text{IQR}}_0 = 0) > 0$ dès que $F_0$ présente un palier ou un atome tel que $F_0^{-1}(3/4) = F_0^{-1}(1/4)$.
  * *Perte de contrôle de queue* : Sous un modèle contaminé $F_1 = (1-\varepsilon)F_0 + \varepsilon G$ avec $0 < \varepsilon < 1/4$ (illustratif) et $\text{supp}(G) \subset (\tau_0, +\infty)$, lorsque $\varepsilon \to 0$ avec $\varepsilon/\alpha = c > 0$, on a $\hat{\tau}_1 \xrightarrow{P} \tau_0$ mais $1 - F_1(\hat{\tau}_1) \xrightarrow{P} \alpha(1 + c)$.
* **Statistique de Kolmogorov-Smirnov dans D3 sur $\hat{p}_j = \frac{1 + \sum_{i=1}^n \mathbb{I}(S_i^{\text{jumeau}} \ge S_j^{\text{agent}})}{n+1}$ ($j=1,\dots,m$) `[VÉRIFIÉ]` :**
  * *Défaut de loi limite standard* : $\text{Cov}(\mathbb{I}(\hat{p}_1 \le u), \mathbb{I}(\hat{p}_2 \le u)) > 0$ par partage de $(S_1^{\text{jumeau}}, \dots, S_n^{\text{jumeau}})$ ; la statistique KS diverge de sa loi tabulée dès que $m/n \not\to 0$.
  * *Perte de puissance en queue* : Si $F_{\text{agent}}(x) = F_{\text{jumeau}}(x)$ pour $x \le F_{\text{jumeau}}^{-1}(1 - 3\alpha)$ et $1 - F_{\text{agent}}(F_{\text{jumeau}}^{-1}(1-\alpha)) = 3\alpha$, alors $\|F_{\text{agent}} - F_{\text{jumeau}}\|_\infty \le 3\alpha$, rendant la puissance asymptotique proche du niveau nominal dès que $3\alpha\sqrt{\frac{nm}{n+m}} \ll 1$.
* **Martingale conforme séquentielle P4 ($M_t$) `[VÉRIFIÉ]` :** Après une rupture de $F_0$ vers $F_1$ à un indice $t_0 \gg 1$, la loi empirique séquentielle jointe absorbe les observations de $F_1$ : si $\sup_{t_0 < s \le t_1} M_s < 1/\delta$ dans la fenêtre transitoire, les p-valeurs conformes séquentielles redeviennent asymptotiquement uniformes quand $t/t_0 \to \infty$.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Contrôle d'arrêt optionnel sous $H_0$ exact** : Appliquer la règle d'augmentation d'effectif du §4 sur deux flux i.i.d. de même loi avec dépassement vrai $\alpha = 0{,}01$. Oppose $H_A$ (taux empirique de rejet de l'hypothèse nulle $\le \gamma$ nominal) à $H_B$ (taux de rejet $> \gamma$ par tests répétés). Falsifie soit la validité séquentielle du protocole de duel de A, soit l'hypothèse d'inflation substantielle aux tailles considérées.
2. **Contrôle de divergence de queue pure dans D3** : Paires synthétiques où $F_{\text{agent}}$ et $F_{\text{jumeau}}$ coïncident sous le quantile $1 - 3\alpha$ mais divergent d'un facteur $3$ au seuil $1-\alpha$. Oppose $H_A$ (D3 rejette l'échangeabilité avec puissance $\ge 0{,}80$, illustratif) à $H_B$ (KS ne rejette pas et valide à tort un jumeau qui triple le taux). Sans lui, D3 certifie des jumeaux défaillants en queue.
3. **Contrôle d'isolation du canal témoin** : Comparer la loi des scores témoins exécutés dans les lots actifs contenant du sabotage à celle des mêmes témoins exécutés hors-ligne ($H_A$ : égalité en loi des scores témoins ; $H_B$ : décalage induit par le partage de contexte, de lot ou d'ordonnancement). Son absence rend aveugle à la capture indirecte de P1.

---

## Sur la proposition B

### (a) Défauts de méthode : variables confondantes, vérités par construction et fuites

* **Dégénérescence par construction algébrique dans P1 (et P2) :**
  Dans P1 (§6), B écrit : « prendre le plus petit $j$ tel que $P(\text{Bin}(n, \alpha) \le j) \le \delta$, puis fixer le seuil à la $(n-j)$-ième statistique d'ordre » `[RAPPORTÉ]`. Or la fonction de répartition $j \mapsto \mathbb{P}(\text{Bin}(n, \alpha) \le j)$ est croissante sur $\{0, \dots, n\}$ `[VÉRIFIÉ]`. Dès que $(1-\alpha)^n \le \delta$, le **plus petit** entier $j \ge 0$ vérifiant l'inégalité est identiquement $j = 0$ pour **tout** effectif $n$ (même arbitrairement grand), ce qui fixe $\hat{\tau}_{\text{P1}} = S_{(n)} = \max_{1 \le i \le n} S_i$ `[VÉRIFIÉ]`. Par construction, P1 est donc identique à la vérification mécanique M1 (« seuil égal au maximum des scores honnêtes du régime » `[RAPPORTÉ]`), alors même que B pose au §3 qu'un instrument ne battant pas M1 en détection est inutile `[RAPPORTÉ]`. (Il fallait prendre le *plus grand* $j$).

* **Variables confondantes et défaut de contrôle séquentiel :**
  1. *Inflation par franchissements répétés et biais de survie dans P2* : P2 estime $\tau(\ell)$ par P1 sur $\{\max_{1 \le s \le \ell} s_{i,s} : L_i \ge \ell\}$, le rend monotone croissant, puis alerte « si le score d'un pas $t$ dépasse $\tau(t)$ » `[RAPPORTÉ]`. Or, dès que $\tau(1) < \tau(2) < \dots < \tau(L)$, l'événement $\{\exists t \le L : S_t > \tau(t)\}$ contient strictement $\{\max_{t \le L} S_t > \tau(L)\}$ `[VÉRIFIÉ]` : calibrer marginalement chaque $\tau(\ell)$ à $\alpha$ ne borne pas la probabilité de franchir la courbe $\tau(\cdot)$ au fil des pas. En outre, restreindre l'estimation à $\{L_i \ge \ell\}$ conditionne sur la survie de l'épisode, confondant longueur $\ell$ et complexité latente des épisodes longs `[HYPOTHÈSE]`.
  2. *Asymétrie de débit d'échantillonnage entre les deux canaux de P3* : Dans P3, le canal D observe tout le flux de déploiement ($m_D$ épisodes par lot) tandis que le canal T n'observe que les témoins ($m_T \ll m_D$) `[RAPPORTÉ]`. Sous une dérive honnête pure déplaçant identiquement les deux canaux à $3\alpha$, le canal D accumule l'information de Kullback-Leibler $m_D / m_T$ fois plus vite par lot que le canal T `[VÉRIFIÉ]`. Le canal D rejette donc avant que T ne rejette, envoyant mécaniquement P3 dans la case « T ne rejette pas / D rejette $\to$ gel du seuil et escalade » sur une simple dérive bénigne.
  3. *Falsification par manque de puissance dans D1 et D2* : B affirme que rester sous le seuil de rejet (borne basse de Clopper-Pearson dans la bande en D1 ; absence de strate significative après correction de Holm en D2) « falsifie $H_B$ » `[RAPPORTÉ]`. À petit effectif par strate, un test non significatif ne falsifie pas la dérive conditionnelle : il reflète le défaut de puissance `[VÉRIFIÉ]`.

* **Fuite de l'aléa d'étalonnage dans l'e-processus P3 :**
  B applique l'inégalité de Ville à $K_t = \prod_{s=1}^t (1 + \lambda_s(\mathbb{I}[S_s > \hat{\tau}] - \alpha))$ `[RAPPORTÉ]` sans imposer $\lambda_s \in [0, 1/\alpha]$ (requis pour $K_t \ge 0$ `[VÉRIFIÉ]`) et en traitant le taux de dépassement sous $H_0$ comme $\le \alpha$. Conditionnellement au seuil estimé $\hat{\tau}$, cela échoue sur l'événement $\{\mathbb{P}(S > \hat{\tau} \mid \hat{\tau}) > \alpha\}$ `[VÉRIFIÉ]`, qui survient avec probabilité non nulle (jusqu'à $\delta$ sous P1, et autour de $1/2$ (illustratif) sous étalonnage conforme marginal).

### (b) Conditions probabilistes de perte de puissance ou de non-jugeabilité

* **Règle P1 telle qu'écrite ($j_* = \min\{j \in \{0,\dots,n\} : F_{\text{Bin}(n,\alpha)}(j) \le \delta\}$, $\hat{\tau}_{\text{P1}} = S_{(n-j_*)}$) `[VÉRIFIÉ]` :**
  * Pour tout $n \ge \frac{\ln \delta}{\ln(1-\alpha)}$, $j_* = 0$ et $\hat{\tau}_{\text{P1}} = S_{(n)} = \hat{\tau}_{\text{M1}}$ presque sûrement : l'écart de puissance $\mathbb{P}_{F_1}(S > \hat{\tau}_{\text{P1}}) - \mathbb{P}_{F_1}(S > \hat{\tau}_{\text{M1}}) \equiv 0$ pour toutes lois $(F_0, F_1)$.
* **Frontière par préfixes P2 ($\hat{\tau}(\ell)$ calibré ponctuellement à $\alpha$ sur $\max_{s \le \ell} S_s$) `[VÉRIFIÉ]` :**
  * Pour une suite $(S_t)_{t=1}^L$ découpée en $R$ blocs indépendants où $\hat{\tau}$ croît strictement entre blocs avec probabilités marginales de franchissement local $q_r \in (0, \alpha]$, le taux d'alerte séquentiel vaut $1 - \prod_{r=1}^R (1 - q_r) > \alpha$ dès que $\sum_{r=1}^R q_r > -\ln(1-\alpha)$.
* **Garde bicanale P3 ($K_t^T, K_t^D$ avec ratio d'intensité d'observation $\eta = m_T / m_D \in (0,1)$ et seuil de Ville $B > 1$) `[VÉRIFIÉ]` :**
  * *Explosion sous régime stationnaire* : Conditionnellement à un seuil réalisé $\hat{\tau}$ tel que $p(\hat{\tau}) = \mathbb{P}_{F_0}(S > \hat{\tau} \mid \hat{\tau}) > \alpha$, pour $\lambda \in (0, \frac{p(\hat{\tau})-\alpha}{\alpha(1-\alpha)})$ assez petit, $\mathbb{E}_{F_0}[\ln(1 + \lambda(\mathbb{I}[S > \hat{\tau}] - \alpha)) \mid \hat{\tau}] > 0$, d'où $\mathbb{P}_{F_0}(\exists t : K_t^D \ge B \mid p(\hat{\tau}) > \alpha) = 1$.
  * *Erreur de branchement sous dérive commune* : Sous $p_T = p_D = p_1 > \alpha$ avec dérive logarithmique par observation $g(p_1) > 0$, les indices de lot d'arrêt vérifient $\tau_D / \ln B \xrightarrow{\text{p.s.}} g(p_1)^{-1}$ et $\tau_T / \ln B \xrightarrow{\text{p.s.}} (\eta g(p_1))^{-1}$, donc $\mathbb{P}_{p_1}(\tau_D < \tau_T) \to 1$ lorsque $B \to \infty$ ou $\eta \to 0$.
* **Duel D2 (tests exacts de deux proportions corrigés par Holm sur $G$ strates d'effectifs $(n_g, m_g)$) `[VÉRIFIÉ]` :**
  * Sous $X_g \sim \text{Bin}(n_g, \alpha)$ et $Y_g \sim \text{Bin}(m_g, 3\alpha)$ au niveau par test $\gamma / G$, lorsque $\max_g (n_g\alpha, m_g\alpha) = O(1)$, la probabilité de non-rejet global $\mathbb{P}(\min_{1 \le g \le G} \hat{p}_{\text{Holm}, g} > \gamma)$ reste proche de $1$, entraînant la fausse falsification de $H_B$.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Contrôle de franchissements répétés de P2 sous bruit blanc** : Générer des trajectoires i.i.d. $S_{i,t} \sim \mathcal{N}(0,1)$ de longueurs hétérogènes $L_i$ sans aucune dérive ni effet de fin d'épisode. Oppose $H_A$ (le taux d'alerte séquentiel $\{\exists t \le L_i : S_{i,t} > \hat{\tau}(t)\}$ reste $\le \alpha$ avec probabilité $\ge 1-\delta$) à $H_B$ (le taux dépasse $\alpha$ par union des paliers de $\hat{\tau}(t)$). Sans ce contrôle, D5 de B (qui ne teste que l'effet de fin d'épisode `[RAPPORTÉ]`) manque le défaut mathématique de la règle d'alerte séquentielle.
2. **Contrôle de dérive commune à ratio réaliste $m_T \ll m_D$ dans P3** : Injecter une dérive honnête pure ($p_T = p_D = 3\alpha$, zéro sabotage) avec la proportion réelle de témoins par lot. Oppose $H_A$ (T et D rejettent conjointement avant gel abusif dans au moins $1-\beta$ des essais) à $H_B$ (D rejette seul en premier et fige le système).
3. **Contrôle stationnaire longue durée sur le couple P1+P3** : Tirer $\hat{\tau}$ répétitivement sur $n$ points de $F_0$ puis faire tourner $K_t^D$ sur un long flux stationnaire issu de $F_0$. Oppose $H_A$ ($\mathbb{P}(\sup_t K_t^D \ge B) \le 1/B$) à $H_B$ (dépassement de $1/B$ induit par la probabilité $\mathbb{P}(p(\hat{\tau}) > \alpha) > 0$).

---

## Sur la proposition C

### (a) Défauts de méthode : variables confondantes, vérités par construction et fuites

* **Glissement des statuts d'intégrité :**
  C étiquette `[VÉRIFIÉ]` des assertions issues du bloc `FAITS` qui n'ont pas été auditées hors énoncé (donc `[RAPPORTÉ]`), et étiquette `[OBSERVÉ-NON-AUDITÉ]` son point §1(a)4 sur la loi de Gumbel/Fréchet `[RAPPORTÉ]` alors qu'aucune trace empirique n'est observée (il s'agit d'une `[HYPOTHÈSE]`).

* **Fuite entre ajustement du modèle et conformisation dans P1 :**
  Dans P1, C ajuste les paramètres de $m(L) = a_0 + a_1 \ln L$ et $\sigma(L) = \exp(b_0 + b_1 \ln L)$ sur les $N_{\text{cal}}$ épisodes d'étalonnage, puis calcule le quantile conforme $q_{1-\alpha}$ sur les résidus $R_i = (S_i - m(L_i))/\sigma(L_i)$ de **ce même échantillon** sans découpage d'apprentissage/calibration `[RAPPORTÉ]` (contrairement à *Conformalized Quantile Regression* de Yaniv Romano, Evan Patterson et Emmanuel Candès, 2019 `[VÉRIFIÉ]`). Comme le point futur $(L_{\text{new}}, S_{\text{new}})$ n'a pas participé à l'ajustement de $(m, \sigma)$, le vecteur $(R_1, \dots, R_{N_{\text{cal}}}, R_{\text{new}})$ n'est pas échangeable : la « validité marginale conforme exacte à échantillon fini » affirmée par C est fausse `[VÉRIFIÉ]`.

* **Variables confondantes et empoisonnement dans P2 (TARR) et l'Expérience 2 :**
  1. *Ancres contaminées par l'intention interne ou la troncature* : Pour construire ses $K = 15$ (illustratif) ancres par lot, C propose d'exécuter un sous-échantillon des invites du lot avec un « masque syntaxique/bac à sable empêchant toute charge utile de sabotage » ou sur les premiers pas coïncidant avec le jumeau `[RAPPORTÉ]`. Un masque syntaxique en sortie modifie la trajectoire auto-régressive (variable confondante de bridage) mais **n'efface pas l'activation interne d'intention** $h_{i,t}$ avant l'action bloquée `[HYPOTHÈSE]` : si une salve massive d'invites du lot induit une tentative de sabotage (> $50\,\%$, illustratif), la médiane $\hat{\mu}_{\text{reg}}$ des ancres monte, réfutant l'« immunité totale à l'empoisonnement » revendiquée par C `[VÉRIFIÉ]`. Quant aux préfixes coïncidents, ils tronquent $L$ aux premiers pas, rendant $R^{\text{ancre}}$ incomparable aux résidus d'épisodes complets.
  2. *Duel confondu et non exhaustif (Expérience 2)* : C oppose P2 (alimenté par $15\,\%$ (illustratif) d'ancres certifiées) à ACI privé de toute étiquette `[RAPPORTÉ]`, confondant l'accès aux ancres avec la règle statistique. De plus, l'intervalle $\text{FPR}_{\text{P2}} \in (1{,}3\,\%, 1{,}8\,\%]$ (illustratif) n'active ni l'Issue 1 ni l'Issue 2 `[RAPPORTÉ]`.

* **Erreur algébrique et cécité par construction dans P3 (SCEM) :**
  1. *Impossibilité d'ajuster $\lambda$ pour restaurer la supermartingale* : C pose $M_t = (1-\lambda)M_{t-1} + \lambda M_{t-1} e_t$ avec $e_t = \kappa p_t^{\kappa-1}$, où $\lambda \in (0,1)$ est « ajustée sur l'étalonnage pour que $\mathbb{E}_{\text{honnête}}[e_t \mid \mathcal{F}_{t-1}] \le 1$ » `[RAPPORTÉ]`. Or $e_t$ est indépendant de $\lambda$, et pour tout $\lambda > 0$, $\mathbb{E}[1 - \lambda + \lambda e_t \mid \mathcal{F}_{t-1}] = 1 + \lambda(\mathbb{E}[e_t \mid \mathcal{F}_{t-1}] - 1) \le 1 \iff \mathbb{E}[e_t \mid \mathcal{F}_{t-1}] \le 1$ `[VÉRIFIÉ]` : aucune valeur de $\lambda \in (0,1)$ ne corrige un excès $\mathbb{E}[e_t \mid \mathcal{F}_{t-1}] > 1$.
  2. *Zéro détection par construction sur les épisodes courts* : Comme $p_t \ge \frac{1}{N_{\text{cal}}+1}$ `[RAPPORTÉ]`, chaque pas d'innovation multiplie $M_{t-1}$ au plus par $g_{\max} = 1 - \lambda + \lambda\kappa(N_{\text{cal}}+1)^{1-\kappa}$ `[VÉRIFIÉ]`. Pour tout épisode comportant moins de $\frac{\ln(1/\alpha)}{\ln g_{\max}}$ pas espacés de $\Delta$, on a $M_t < 1/\alpha$ par construction algébrique ($\text{TPR} \equiv 0$).

### (b) Conditions probabilistes de perte de puissance ou de non-jugeabilité

* **Estimateur P1 ($\hat{\Theta}(L) = \hat{m}(L) + \hat{q}_{1-\alpha}\hat{\sigma}(L)$ avec $\hat{\sigma}(L) = \exp(\hat{b}_0 + \hat{b}_1 \ln L)$ ajusté in-sample sur $N_{\text{cal}}$) `[VÉRIFIÉ]` :**
  * *Défaut d'échangeabilité hors-échantillon* : À fort levier $|\ln L_{\text{new}} - \overline{\ln L}|$, la variance prédictive de $R_{\text{new}} = (S_{\text{new}} - \hat{m}(L_{\text{new}}))/\hat{\sigma}(L_{\text{new}})$ excède celle des résidus ajustés $R_i$, donnant $\mathbb{P}(S_{\text{new}} > \hat{\Theta}(L_{\text{new}})) > \alpha$.
  * *Mauvaise spécification d'échelle Gumbel* : Pour $S_L = \max_{1 \le t \le L} Z_t$ avec $Z_t \stackrel{\text{i.i.d.}}{\sim} \mathcal{N}(0,1)$, $\text{SD}(S_L) \asymp (2\ln L)^{-1/2}$ alors que $e^{b_0} L^{b_1}$ est polynomial en $L$ : l'erreur relative de quantile diverge quand $L \to \infty$ dès que $b_1 \neq 0$.
* **Estimateur P2 ($\hat{\mu}_{\text{reg}} = \text{Médiane}(R_{1:K}^{\text{ancre}})$, $\hat{s}_{\text{reg}} = 1{,}4826\,\text{MAD}(R_{1:K}^{\text{ancre}})$) `[VÉRIFIÉ]` :**
  * *Non-bornitude du quantile sur la classe semi-paramétrique* : Sur $\mathcal{P} = \{F : F^{-1}(1/2) = 0, \text{MAD}(F) = 1\}$, $\sup_{F \in \mathcal{P}} F^{-1}(1-\alpha) = +\infty$ pour tout $\alpha < 1/4$ (illustratif) ; aucune constante finie $c_\alpha$ ne garantit $\sup_{F \in \mathcal{P}} \mathbb{P}_{F}(R > \hat{\mu}_{\text{reg}} + \hat{s}_{\text{reg}}(q_{1-\alpha} + c_\alpha K^{-1/2})) \le \alpha$.
  * *Perte de puissance sous stationnarité* : À $K$ petit, le décalage positif $c_\alpha K^{-1/2}\sigma(L)$ combiné à la variance asymptotique de la MAD réduit $\mathbb{P}_{F_{\text{sab}}}(S > \hat{\Theta}_{\text{TARR}})$.
* **Processus séquentiel P3 ($M_t = \prod_{j=1}^{\lfloor t/\Delta \rfloor} (1 - \lambda + \lambda\kappa \hat{p}_{j\Delta}^{\kappa-1})$) `[VÉRIFIÉ]` :**
  * *Puissance identiquement nulle* : $\mathbb{P}_{F_{\text{sab}}}(\sup_{t \le L} M_t \ge 1/\alpha) = 0$ pour toute loi $F_{\text{sab}}$ dès que $\lfloor L/\Delta \rfloor < \frac{\ln(1/\alpha)}{\ln(1 - \lambda + \lambda\kappa(N_{\text{cal}}+1)^{1-\kappa})}$.
  * *Explosion par partage d'ancres* : Conditionnellement à un tirage de $(\hat{\mu}_{\text{reg}}, \hat{s}_{\text{reg}})$ tel que $\mathbb{E}_{F_0}[\kappa \hat{p}_{j\Delta}^{\kappa-1} \mid \hat{\mu}_{\text{reg}}, \hat{s}_{\text{reg}}] > 1$, on a $\mathbb{P}_{F_0}(\sup_{t \le L} M_t \ge 1/\alpha \mid \hat{\mu}_{\text{reg}}, \hat{s}_{\text{reg}}) \to 1$ quand $L \to \infty$ pour tout $\lambda \in (0,1]$.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Contrôle de fuite in-sample sur P1** : Comparer sur données i.i.d. à longueurs étalées le taux hors-échantillon de P1 (ajusté et conformisé sur les mêmes $N_{\text{cal}}$ points) à celui d'une version *split conformal* ($N_{\text{cal}}/2$ ajustement, $N_{\text{cal}}/2$ calibration, illustratif). Oppose $H_A$ (absence d'excès de fausses alertes en queue de longueur pour P1 in-sample) à $H_B$ (dépassement de $\alpha$ aux grandes longueurs par sur-ajustement).
2. **Contrôle de fuite d'intention sous masque syntaxique dans P2** : Exécuter le protocole de masquage syntaxique de C sur un lot contenant une majorité d'invites qui déclenchent une intention de sabotage chez l'agent avant l'action finale. Oppose $H_A$ ($\hat{\mu}_{\text{reg}}$ des ancres masquées est indiscernable en loi de celui d'épisodes honnêtes purs) à $H_B$ (inflation de $\hat{\mu}_{\text{reg}}$ et chute du rappel).
3. **Contrôle de cécité en épisode court sur P3** : Injecter des sabotages saturant les sondes ($p_t = \frac{1}{N_{\text{cal}}+1}$) sur des épisodes de longueur $L < \Delta \frac{\ln(1/\alpha)}{\ln g_{\max}}$. Oppose $H_A$ ($\text{TPR} > 0$) à $H_B$ ($\text{TPR} = 0$ par plafonnement arithmétique des sauts de $M_t$).

---

## Sur la proposition D

### (a) Défauts de méthode : variables confondantes, vérités par construction et fuites

* **Variables confondantes :**
  1. *Longueur réalisée non contrôlée à budget prévu constant* : D stratifie à raison sur une covariable connue avant décision (« budget prévu » $L_{\max}$) plutôt que sur la longueur finale `[RAPPORTÉ]`. Toutefois, sous un plafond système $L_{\max}$ fixe, une nouvelle version d'agent ou une nouvelle source bénigne déplace la longueur effective d'arrêt $L \le L_{\max}$, qui agit comme variable confondante non contrôlée sur $S = \max_{t \le L} s_t$ `[HYPOTHÈSE]`.
  2. *Pénalisation de la suspension face aux contrôles déterministes (§4)* : D inclut les épisodes suspendus au dénominateur du taux de détection tout en exigeant un gain strict sur le meilleur contrôle mécanique admissible (lequel ne suspend jamais) `[RAPPORTÉ]`. Ce critère confond l'honnêteté épistémique du retrait de certificat avec l'infériorité intrinsèque du score.
  3. *Séparation par familles de tâches entre calibration et audit (§2)* : Découper par familles de tâches disjointes les partitions de calibration et d'audit `[RAPPORTÉ]` injecte une dérive inter-tâches artificielle dans l'estimation du taux de référence avant tout changement de régime.

* **Incompatibilités par construction avec le défaut et les contraintes de `FAITS` :**
  1. *Vacuité mathématique de `D-enveloppe` sous triplement global* : `D-enveloppe` n'autorise un seuil que si $U + \varepsilon \le 0{,}01$, où $\varepsilon$ borne l'excès de probabilité de queue cible par rapport à la référence `[RAPPORTÉ]`. Or, sur toute famille où le seuil initial passe de $1\,\%$ au triple ($3\,\%$), une enveloppe uniforme sur les seuils vérifie nécessairement $\varepsilon = \sup_q (Q_{\text{cible}}(S > q) - P_{\text{réf}}(S > q)) \ge 0{,}02 > 0{,}01$ `[VÉRIFIÉ]`. Comme $U > 0$, l'inégalité $U + \varepsilon \le 0{,}01$ est **impossible par construction** : `D-enveloppe` révoque systématiquement son certificat. Même avec une enveloppe locale hypothétique $\varepsilon(q) = 0{,}005$ (illustratif) et un risque $\delta = 0{,}05$ (illustratif), $U(0; n_{\text{cert}}, \delta) = 1 - \delta^{1/n_{\text{cert}}} \le 0{,}005$ (illustratif) exige $n_{\text{cert}} \ge 598$ (illustratif) épisodes honnêtes **par strate dans la seule partition de certification** `[VÉRIFIÉ]`, incompatible avec « quelques centaines » d'épisodes au total `[RAPPORTÉ]`.
  2. *Surcoût de `D-ancre` par cellule* : Exiger $m \ge 99$ ($\frac{1}{0{,}01} - 1$) témoins injectés par strate et par lot `[VÉRIFIÉ]` contredit la contrainte de « budget de calcul modeste » `[RAPPORTÉ]` dès que les lots sont stratifiés ou fréquents.

* **Fuite ou circularité sur l'enveloppe $\varepsilon$ :**
  Justifier quantitativement $\varepsilon < 0{,}01$ « indépendamment du lot testé » `[RAPPORTÉ]` pour une nouvelle version d'agent est impossible sans observer ce nouveau régime (fuite vers la certification) ; à l'inverse, construire le test de mort en « plantant le triplement au vieux seuil tout en respectant l'enveloppe » `[RAPPORTÉ]` adapte la loi de test au paramètre $\varepsilon$ postulé par le défenseur, rendant la survie du certificat circulaire.

### (b) Conditions probabilistes de perte de puissance ou de non-jugeabilité

* **Duel conjonctif simultané du §4 sur $G$ strates d'effectifs $(m_1, \dots, m_G)$ au niveau global $\delta$ ($\sum_{g=1}^G \delta_g \le \delta$) `[VÉRIFIÉ]` :**
  * *Non-jugeabilité certaine* : Valider $H_A$ requiert $\max_{1 \le g \le G} U_{\text{CP}}(X_g; m_g, \delta_g) \le \alpha$ avec $X_g \sim \text{Bin}(m_g, p_g)$ (C. J. Clopper et E. S. Pearson, 1934 `[VÉRIFIÉ]`). Comme $\min_{x \ge 0} U_{\text{CP}}(x; m_g, \delta_g) = 1 - \delta_g^{1/m_g}$, dès qu'il existe $g$ tel que $m_g < \frac{\ln \delta_g}{\ln(1-\alpha)}$, on a $\mathbb{P}(\text{valider } H_A) = 0$ pour tout vecteur $(p_1, \dots, p_G) \in [0,1]^G$, laissant le duel non jugeable avec probabilité $\ge 1 - \delta$ lorsque $p_g \le \alpha$.
* **Règle `D-ancre` ($\hat{p}(S_{\text{cible}}) = \frac{1 + \sum_{i=1}^m \mathbb{I}(S_i^{\text{témoin}} \ge S_{\text{cible}})}{m+1}$) `[VÉRIFIÉ]` :**
  * *Puissance nulle* : Si $m < \frac{1}{\alpha} - 1$, $\inf_s \hat{p}(s) = \frac{1}{m+1} > \alpha$, donc $\mathbb{P}_{F_{\text{sab}}}(\hat{p} \le \alpha) = 0$.
  * *Variance irréductible inter-lots* : Lorsque $B_{\text{lots}}$ lots indépendants partagent chacun $m$ témoins avec $k = \lfloor(m+1)\alpha\rfloor \ge 1$, le taux conditionnel du lot $\ell$ suit $W_\ell \stackrel{\text{i.i.d.}}{\sim} \text{Beta}(k, m+1-k)$ ; la variance de l'estimateur empirique global est minorée par $\frac{k(m+1-k)}{B_{\text{lots}}(m+1)^2(m+2)}$ même quand l'effectif cible par lot tend vers $+\infty$, empêchant la borne supérieure simultanée de descendre sous $\alpha$ si $B_{\text{lots}}$ est petit.
  * *Perte de validité sous biais d'ancre* : Si $S^{\text{témoin}} \sim F_T$ et $S^{\text{cible}} \sim F_0$, $\lim_{m \to \infty} \mathbb{P}(\hat{p}(S_{\text{cible}}) \le \alpha) = 1 - F_0(F_T^{-1}(1-\alpha))$, qui excède $\alpha$ dès que $F_0$ domine stochastiquement $F_T$ en queue droite.
* **Certificat `D-enveloppe` ($\mathbb{I}(U(X_{\text{cert}}; n_{\text{cert}}, \delta) + \varepsilon(\hat{q}) \le \alpha)$, $X_{\text{cert}} \sim \text{Bin}(n_{\text{cert}}, 1 - F_{\text{réf}}(\hat{q}))$) `[VÉRIFIÉ]` :**
  * *Suspension certaine (puissance nulle)* : $\mathbb{P}(\text{certificat actif}) = 0$ dès que $\varepsilon(\hat{q}) \ge \alpha - (1 - \delta^{1/n_{\text{cert}}})$, ce qui est toujours réalisé pour $\varepsilon = \sup_t (F_{\text{réf}}(t) - F_{\text{cible}}(t))$ lorsque $\exists q_0 : 1 - F_{\text{réf}}(q_0) = \alpha$ et $1 - F_{\text{cible}}(q_0) = 3\alpha$ ($\varepsilon \ge 2\alpha > \alpha$).
  * *Domination par le contrôle mécanique* : Même si $\varepsilon(\hat{q}) < \alpha - (1 - \delta^{1/n_{\text{cert}}})$, la perte de puissance par abaissement de $\alpha$ à $\alpha - \varepsilon(\hat{q})$ et par suspension $\pi_{\text{susp}}$ fait échouer $H_A$ dès que $(1 - \pi_{\text{susp}})(1 - F_{\text{sab}}(\hat{q})) \le p_{\text{méc}}$.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Contrôle de non-vacuité du banc §4 et de `D-enveloppe` sous régime stationnaire** : Exécuter tout le pipeline de partitionnement et de bornes simultanées sur un monde sans dérive ($\varepsilon = 0$, $F_{\text{cible}} = F_{\text{réf}}$) aux effectifs exacts disponibles par régime dans `FAITS` (« quelques centaines » `[RAPPORTÉ]`). Oppose $H_A$ (le banc tranche en faveur de la validité dans au moins $1-\beta$ des essais) à $H_B$ (le banc reste « indécis » ou suspend par insuffisance arithmétique d'effectif).
2. **Contrôle de dérive de la longueur d'arrêt à budget prévu constant** : Deux flux honnêtes partageant le même budget prévu $L_{\max}$ et la même loi de score par jeton, mais des distributions d'arrêt $L^{(1)} \ll L^{(2)} \le L_{\max}$. Oppose $H_A$ (la stratification ex ante sur $L_{\max}$ maintient le taux $\le \alpha$) à $H_B$ (l'allongement effectif intra-strate fait tripler les fausses alertes).
3. **Contrôle de source bénigne hors-générateur sur `D-ancre`** : Évaluer `D-ancre` lorsque les témoins viennent du générateur courant mais que les cibles honnêtes proviennent d'une source bénigne tierce non incluse dans ce générateur. Oppose $H_A$ (maintien de $\mathbb{P}(\hat{p} \le \alpha) \le \alpha$) à $H_B$ (rupture d'échangeabilité témoin–cible en queue).

FIN-DE-CELLULE