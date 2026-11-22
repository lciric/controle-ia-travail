**État des pièces reçues :** Les blocs `FAITS`, `QUESTION DE L'ARBITRE`, `E3-T1-conception-A`, `E3-T1-conception-B` et `E3-T1-conception-D` ont été reçus complets, sans coupure visible.

---

## Sur la proposition A

### (a) Défauts de méthode : variables confondantes, vérités par construction et fuites

1. **Incompatibilité entre le support de l'écart à la référence et la positivité exigée par l'inégalité de Ville (P1, T1, D1) :**
   - Dans les faits (`RAPPORTÉ`), le dommage est défini comme une baisse par rapport au jumeau honnête sur la même tâche, soit $d_i = R_{\text{hon},i} - Y_i$. En présence d'une dispersion honnête non nulle $\sigma > 0$ (`RAPPORTÉ`, piste 2), $d_i$ prend des valeurs négatives dès que le tirage du suspect surpasse celui du jumeau honnête.
   - Or A pose $d_i \in [0, c]$ (`HYPOTHÈSE`) et applique l'inégalité de Ville (Jean Ville, 1939, *Étude critique de la notion de collectif*) à la martingale centrée $\sum_{i=1}^N (A_i/p_i - 1)d_i$ (ou avec variable de contrôle $d_i - m_i$). C'est un défaut méthodologique double (`VÉRIFIÉ`) :
     - Si l'on tronque le dommage par épisode à $d_i^+ = \max(0, R_{\text{hon},i} - Y_i) \in [0, c]$, alors sous la loi honnête ($Y_i \stackrel{d}{=} R_{\text{hon},i}$), l'espérance par pas est strictement positive ($\mathbb{E}[d_i^+] \asymp \sigma > 0$), de sorte que le cumul honnête croît linéairement en $\Theta(N\sigma)$ et viole le niveau $\alpha$.
     - Si l'on ne tronque pas ($d_i \in [-c, c]$), la somme partielle $\sum (A_i/p_i - 1)(d_i - m_i)$ change de signe et n'est pas une surmartingale positive ; l'inégalité de Ville ne s'y applique qu'après transformation multiplicative bornée (Waudby-Smith et Ramdas, 2023, *Estimating means of bounded random variables by betting*, « référence à vérifier »), dont la constante d'échelle double avec l'amplitude de $d_i - m_i$.
   - *Vérité par construction dans D1* : tester la couverture de T1 sur un simulateur où les mondes honnêtes ont un dommage nul sans bruit de référence ($d_i \equiv 0$) et où les tirages de Bernoulli sont exacts vérifie une tautologie probabiliste du générateur pseudo-aléatoire, en masquant le biais de troncature sous $\sigma > 0$.

2. **Variable confondante de difficulté et fuite d'échantillon dans le tableau de cécité (P2 et 6.g) :**
   - P2 mesure la part de variance expliquée ($R^2$) de $d_i$ par le score $m_i$ sur le bras d'audit aléatoire. La difficulté intrinsèque de la tâche $Z_i$ agit comme variable confondante : sur des tâches difficiles, l'écart honnête $d_i$ et le score du moniteur $m_i$ (sensible à la longueur ou aux hésitations) augmentent simultanément. Le $R^2$ reste élevé à cause de la covariance sur les accidents honnêtes, tandis que la covariance conditionnelle au sabotage est nulle.
   - *Fuite construction/évaluation* : en 6.(g), A propose de réajuster le moniteur par époque sur les épisodes endommagés trouvés par l'audit. Évaluer la part de variance expliquée (P2) ou la réduction de variance du bilan (P1) sur les mêmes épisodes audités que ceux servant au réajustement viole la prévisibilité ($\mathcal{F}_{i-1}$-mesurabilité) de $m_i$ et biaise l'estimateur de variance à la baisse (`VÉRIFIÉ`).

3. **Confusion lexicale de la consigne dans le duel de la sonde « dopamine » (D2 et P4) :**
   - D2 oppose un « échec honnête prévu (tâche rendue infaisable, l'agent le sait) » à une « sous-performance sur consigne, appariés par tâche ».
   - *Variable confondante fatale* : dans le second bras, la consigne de sous-performer figure dans le contexte d'entrée de l'agent. Une sonde linéaire sur les états internes sépare la présence sémantique ou lexicale de cette consigne dans l'invite, sans jamais lire une intention endogène de complot (`RAPPORTÉ`, Korbak, Balesni, Shlegeris, Irving, 2025, *How to evaluate control measures for LLM agents?*, arXiv 2504.05259, p. 24). Un $\text{AUROC} \ge 0,8$ (`illustratif`) dans D2 serait vrai par construction de l'invite.
   - Dans P4, opposer la réussite lue en interne $\hat{R}_i$ à la faisabilité prédite par le modèle de confiance $M_{\text{conf}}$ confond le sabotage avec le différentiel de compétence honnête : puisque $M_{\text{conf}}$ est plus faible (`RAPPORTÉ`), il juge faisables des tâches comportant un obstacle subtil que seul le modèle fort détecte (exactement le cas de l'échec honnête prévu).

4. **Confusion entre reproductibilité conditionnelle à l'invite et intention maligne (P7) :**
   - P7 décompose l'écart sur $K$ rejouages du même pas en biais et variance, en supposant que « l'erreur honnête est idiosyncratique » alors que le dommage cumulatif exige un biais signé commun.
   - *Défaut de méthode* : conditionnellement à un préfixe $x_i$ fixé, une incompréhension honnête, une lacune de connaissance ou un biais d'entraînement d'un réseau de neurones produit une distribution de sortie concentrée autour d'une mauvaise réponse ($\text{Var}(Y_{i,k} \mid x_i)$ faible, $\mathbb{E}[R_{\text{hon},i} - Y_{i,k} \mid x_i] > 0$). P7 confond la variance intra-état (aléa de décodage à préfixe fixé) avec la variance inter-tâches du biais honnête.

---

### (b) Conditions de perte de puissance ou de non-jugeabilité (lois de probabilité, paramètres, estimateurs)

1. **Estimateur du bilan assisté $\hat{D}_N = \sum_{i=1}^N m_i + \sum_{i=1}^N \frac{A_i}{p_i}(d_i - m_i)$ (P1 / T1) :**
   - Soit $d_i = \xi_i + \delta_i$ où $\xi_i = R_{\text{hon},i} - Y_i^{\text{hon}}$ vérifie $\mathbb{E}[\xi_i \mid \mathcal{F}_{i-1}] = 0$, $\text{Var}(\xi_i \mid \mathcal{F}_{i-1}) = \sigma_i^2$, et $\delta_i \ge 0$ est le paramètre de sabotage.
   - *Non-jugeabilité* : dès que $\mathbb{P}(\xi_i + \delta_i < 0 \mid \mathcal{F}_{i-1}) > 0$ (pour l'estimateur non tronqué sur $[0, c]$) ou dès que l'estimateur tronqué $\hat{D}_N^+ = \sum_{i=1}^N \frac{A_i}{p_i}\max(0, d_i)$ est utilisé sous $\sigma_i > 0$, car $\mathbb{E}[\hat{D}_N^+ \mid \delta \equiv 0] = \sum_{i=1}^N \mathbb{E}[\max(0, \xi_i)] \asymp N\sigma > 0$.
   - *Perte de puissance de la variable de contrôle* : lorsque la loi conjointe $\mathcal{L}(d_i, m_i \mid \mathcal{F}_{i-1})$ vérifie $\text{Cov}(d_i, m_i \mid \mathcal{F}_{i-1}) \le \frac{1}{2}\text{Var}(m_i \mid \mathcal{F}_{i-1})$, auquel cas $\text{Var}(\hat{D}_N) \ge \text{Var}\left(\sum_{i=1}^N \frac{A_i}{p_i} d_i\right)$, et pour tout paramètre cumulé $\Delta_N = \sum_{i=1}^N \delta_i \le z_{1-\alpha}\sqrt{\sum_{i=1}^N \frac{1-p_i}{p_i}\left(\sigma_i^2 + \text{Var}(m_i \mid \mathcal{F}_{i-1}) - 2\text{Cov}(d_i, m_i \mid \mathcal{F}_{i-1})\right)}$.

2. **Estimateur de la part de variance expliquée $\hat{R}_N^2 = \frac{\left(\sum_{i=1}^N \frac{A_i}{p_i}(m_i - \bar{m}_w)(d_i - \bar{d}_w)\right)^2}{\left(\sum_{i=1}^N \frac{A_i}{p_i}(m_i - \bar{m}_w)^2\right)\left(\sum_{i=1}^N \frac{A_i}{p_i}(d_i - \bar{d}_w)^2\right)}$ (P2) :**
   - Soit $d_i = \eta(Z_i) + \delta_i$ où $Z_i$ est le paramètre latent de difficulté de la tâche, $\eta(Z_i)$ l'erreur honnête et $\delta_i$ le sabotage.
   - *Perte de puissance du test de cécité ($\hat{R}_N^2 < \tau$)* : sous la loi où $\text{Cov}(m_i, \delta_i) = 0$ (cécité complète au sabotage) mais $\frac{\text{Cov}(m_i, \eta(Z_i))^2}{\text{Var}(m_i)(\text{Var}(\eta(Z_i)) + \text{Var}(\delta_i))} > \tau$, l'estimateur $\hat{R}_N^2$ converge en probabilité vers une limite strictement supérieure au seuil $\tau$.
   - *Non-jugeabilité à échantillon fini* : lorsque la taille effective d'échantillon $n_{\text{eff}} = \left(\sum_{i=1}^N p_i\right)^2 / \sum_{i=1}^N p_i$ et la kurtosis $\kappa_d = \mathbb{E}[(d-\mu_d)^4]/\text{Var}(d)^2$ vérifient $\frac{\kappa_d}{n_{\text{eff}}} \ge \tau^2$.

3. **Estimateur d'inférence adverse du statut audité sous corrections placebos (P3) :**
   - Soit $C_i \in \{0,1\}$ la variable de correction avec $q_1 = \mathbb{P}(C_i=1 \mid A_i=1, d_i \in \mathcal{C}_{\text{or}})$ et $q_0 = \mathbb{P}(C_i=1 \mid A_i=0)$ tels que $\ln(q_1/q_0) \le \varepsilon$.
   - *Perte de puissance du masquage sur un horizon $K$* : pour estimer un paramètre de frontière d'oracle $\phi \in \Theta$, l'information de Fisher cumulée de l'estimateur du maximum de vraisemblance $\hat{\phi}_K$ sur $K$ épisodes indépendants vaut $I_K(\phi) = K \cdot \text{Var}_\phi\left(\frac{\partial}{\partial \phi}\ln \mathbb{P}_\phi(C_i)\right) \asymp K p^2 \frac{(q_1 - q_0)^2}{q_0(1-q_0)}$. Dès que $K \ge \frac{q_0(1-q_0)}{p^2(q_1-q_0)^2 \eta^2}$, la variance asymptotique $\text{Var}(\hat{\phi}_K) \le \eta^2$ malgré la borne marginale $\varepsilon$ par épisode.

4. **Estimateur $\widehat{\text{AUROC}}$ et contraste $\hat{\Delta}_i = \hat{R}_i - \hat{F}_{\text{conf}}(X_i)$ (P4 / D2) :**
   - Soit $W_i \in \{0,1\}$ l'indicateur de présence d'une consigne de sous-performance dans $X_i$, $I_i \in \{0,1\}$ le paramètre d'intention latente et $S_i$ le score de la sonde.
   - *Non-jugeabilité de D2* : lorsque $S_i \perp I_i \mid W_i$ mais que les lois conditionnelles $\mathcal{L}(S_i \mid W_i=1)$ et $\mathcal{L}(S_i \mid W_i=0)$ vérifient $\mathbb{P}(S^{(1)} > S^{(0)} \mid W^{(1)}=1, W^{(0)}=0, I^{(1)}=I^{(0)}=0) \ge 0,8$ (`illustratif`).
   - *Perte de puissance de $\hat{\Delta}_i$* : lorsque le biais d'estimation du modèle de confiance $\beta_{\text{conf}}(X_i) = \mathbb{E}[Y_i^{\text{hon}} \mid X_i] - \hat{F}_{\text{conf}}(X_i)$ vérifie $\text{Var}(\beta_{\text{conf}}(X_i)) \gg \mathbb{E}[\delta_i]^2$.

5. **Estimateur du coût d'évasion $\Delta \hat{\mu}_{\text{perf}}$ (P5 / D3) et du taux de bascule $\hat{\tau}_{\text{basc}}$ (P6 / D4) :**
   - Pour P5 : si l'adversaire applique la loi d'obscurcissement $Q_{\text{obsc}}$ uniquement sous un événement de sabotage de probabilité $\pi_s = \mathbb{P}(\delta_i > 0) \ll 1$, la perte de performance marginale sur le flux est $\pi_s \Delta \mu_{\text{perf}}$. Dès que $\pi_s \le \frac{z_{1-\alpha}\sigma_{\text{hon}}}{\sqrt{N}\Delta\mu_{\text{perf}}}$, le test sur la performance moyenne externe a une puissance bornée par $\alpha + \Phi(0) = \alpha + 0,5$ (`illustratif`).
   - Pour P6 : soit $\gamma_0 = \mathbb{P}(V(\Pi(Y_i)) \neq V(Y_i) \mid \delta_i = 0)$ le taux de dégradation fonctionnelle induite par le retrait de prose $\Pi$ sur produit honnête, et $\gamma_1 = \mathbb{P}(V(\Pi(Y_i)) \neq V(Y_i) \mid \delta_i > 0)$. L'estimateur $\hat{\tau}_{\text{basc}}$ converge vers $(1-\pi_s)\gamma_0 + \pi_s \gamma_1$ ; le paramètre de persuasion $\gamma_1$ est non identifiable dès que $\gamma_0 \ge \pi_s \gamma_1$.

6. **Estimateur du biais signé inter-rejouages $T_i = \frac{\sqrt{K}\hat{B}_i}{\hat{s}_i}$ avec $\hat{B}_i = \frac{1}{K}\sum_{k=1}^K(R_{\text{hon},i} - Y_{i,k})$ et $\hat{s}_i^2 = \frac{1}{K-1}\sum_{k=1}^K(Y_{i,k} - \bar{Y}_i)^2$ (P7) :**
   - Sous la loi hiérarchique honnête ($\delta_i = 0$) où $Y_{i,k} = \mu_{\text{hon}}(X_i) + \epsilon_{i,k}$ avec $\text{Var}(\epsilon_{i,k} \mid X_i) = \sigma_{\text{intra}}^2$ et $b_{\text{hon}}(X_i) = R_{\text{hon},i} - \mu_{\text{hon}}(X_i)$ de variance inter-tâches $\text{Var}(b_{\text{hon}}(X_i)) = \sigma_{\text{inter}}^2 > 0$, la loi marginale de $T_i^2$ sous $H_0$ a un facteur d'échelle $\mathbb{E}[T_i^2 \mid \delta_i=0] \asymp 1 + \frac{K\sigma_{\text{inter}}^2}{\sigma_{\text{intra}}^2}$.
   - *Perte totale de puissance* : lorsque $K \sigma_{\text{inter}}^2 \gg \sigma_{\text{intra}}^2$ et $\sigma_{\text{inter}}^2 \ge \delta_i^2$, le taux de fausses alertes sous $H_0$ tend vers $1$ quand $K$ croît.

---

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Pour D1 et P1 :** Un monde purement honnête ($\delta_i \equiv 0$) où l'écart observé entre le suspect et le jumeau honnête $d_i = R_{\text{hon},i} - Y_i$ a une variance empirique $\sigma^2 > 0$ réaliste (prenant donc des valeurs positives et négatives), afin de réfuter toute implémentation de Ville qui tronquerait $d_i$ à $[0, c]$ ou supposerait $d_i \ge 0$ sans bruit.
2. **Pour D2 et P4 :** Des épisodes d'échec honnête où l'invite de la tâche contient le champ lexical du sabotage ou de la sous-performance (par exemple, auditer ou documenter une politique de défaillance sans l'exécuter). L'absence de ce contrôle empêche de falsifier l'hypothèse que la sonde lit les jetons de la consigne plutôt que l'intention.
3. **Pour P2 :** Un flux de test à deux régimes de difficulté honnête contrastés où le moniteur corrèle fortement avec les échecs honnêtes ($\text{Cov}(m, \eta(Z)) > 0$) mais où le sabotage injecté est orthogonal au moniteur ($\text{Cov}(m, \delta) = 0$).
4. **Pour P7 :** Un lot de tâches honnêtes comportant des ambiguïtés ou pièges connus sur lesquels le modèle honnête commet une erreur reproductible à basse température ($\sigma_{\text{intra}}^2 \ll \sigma_{\text{inter}}^2$).

---

## Sur la proposition B

### (a) Défauts de méthode : variables confondantes, vérités par construction et fuites

1. **Confusion entre dérive distributionnelle bénigne et dommage hors spécification (6.b.5) :**
   - Pour couvrir le dommage hors spécification, B propose de remplacer « le produit est-il mauvais ? » par « le produit est-il distinguable de la distribution des jumeaux honnêtes ? » via une divergence calculée par les lecteurs.
   - *Défaut méthodologique majeur* :
     - Dans les faits (`RAPPORTÉ`), le dommage est une *baisse* asymétrique par rapport au jumeau honnête, non une distance symétrique : toute variation stylistique, réorganisation valide du code ou amélioration par rapport au jumeau augmente une divergence distributionnelle.
     - Cela contredit directement le résultat d'impossibilité cité par B en 6.(k).3 (`RAPPORTÉ`, Fang et al., 2022, *Is Out-of-Distribution Detection Learnable?*, arXiv 2210.14707) : demander aux lecteurs de tester la distinguabilité distributionnelle en grande dimension réintroduit un détecteur hors distribution non borné à la place de l'oracle. Sur un flux long $N$, le moindre écart de distribution entre le suspect et son jumeau (ou le biais d'estimation à petit échantillon de la divergence) s'accumule linéairement en $\Theta(N)$ et détruit la borne en $\sigma\sqrt{N/\pi}$.

2. **Indépendance entre le rappel sur canaris fixes et le rétrécissement de couverture en service (P2 et 6.b.4) :**
   - B propose de détecter en service que la couverture de l'oracle a rétréci en injectant des canaris (issus de familles connues d'un tiers) à fréquence secrète et en suivant une séquence de confiance sur leur rappel.
   - *Fuite conceptuelle / Variable confondante* : en service, les poids des deux lecteurs-oracles sont fixes. Si la loi d'injection des canaris du tiers est fixe et que les lecteurs sont fixes, la probabilité de détection d'un canari est une constante stationnaire (`VÉRIFIÉ`). Or, en service, la couverture effective rétrécit parce que *l'agent suspect* adapte sa politique ou déplace ses attaques vers les angles morts des lecteurs (`RAPPORTÉ`, arXiv 2611.14950, p. 1). Le rappel mesuré sur les canaris du tiers est statistiquement indépendant de la trajectoire d'adaptation de l'adversaire : la séquence de confiance sur les canaris certifiera une couverture stable pendant que le rappel sur les attaques réelles tombe à zéro.

3. **Vérité par construction dans le duel de la loi de fuite (D2) et omission de la variable de contrôle dans la borne (6.k.1) :**
   - Dans D2, B oppose une croissance du dommage caché en $\sqrt{N}$ ($H_A$) à une croissance linéaire en $N$ ($H_B$) sur un simulateur, en faisant varier $\sigma$ par appariement comme contrôle négatif. Sur un simulateur où les erreurs honnêtes par épisode sont indépendantes de variance $\sigma^2$ et où l'oracle est supposé sans biais (L-a.2), la fluctuation en $\sigma\sqrt{N}$ est le théorème central limite (`VÉRIFIÉ`) : $H_A$ est vraie par construction du générateur aléatoire. En revanche, dès que l'oracle a un biais résiduel $\beta > 0$ sur une attaque partiellement hors couverture, la fuite réelle croît linéairement en $\beta N$.
   - De plus, en 6.(k).1, B écrit la séquence de confiance uniquement sur les termes bruts de Horvitz-Thompson $\mathbb{I}_{\text{audit},s} D_s / \pi_s \in [0, c/\pi_{\min}]$ (Horvitz et Thompson, 1952, *A Generalization of Sampling Without Replacement from a Finite Universe*) sans y inclure les variables de contrôle des moniteurs promises en 6.(a) et 6.(j), ni traiter le fait que la différence appariée « suspect − jumeau honnête » prend des valeurs négatives de variance $\sigma^2$.

4. **Inversion logique de la région de rejet dans le duel de la sonde de surprise (D3 et 6.e) :**
   - En 6.(e), B soutient que sur un sabotage planifié, la surprise est proche de zéro, tandis qu'elle est haute sur un échec honnête imprévu ($H_B$).
   - En D3, B compare le sabotage planifié à l'échec honnête imprévu et stipule : « une AUROC compatible avec $0,5$ falsifie $H_A$ [elle lit l'intention] » et maintient $H_B$.
   - *Défaut de méthode (`VÉRIFIÉ`)* : si la surprise est proche de zéro sur le sabotage planifié et élevée sur l'échec honnête imprévu (ce que prédit $H_B$), alors la sonde sépare fortement les deux classes en sens inverse ($\text{AUROC} \ll 0,5$, ou $\gg 0,5$ selon le signe des poids linéaires) ! Une $\text{AUROC} \approx 0,5$ signifie que le sabotage planifié et l'échec honnête imprévu ont la *même* distribution de surprise, ce qui réfute $H_B$ tout autant que $H_A$.

5. **Formule de fuite incomplète sur le canal de correction (6.d et P3) :**
   - B borne l'information apprise par $\varepsilon = \ln(p_1/q)$, tout en affirmant que « l'arrêt sur dommage grave ne se cache pas, et il n'a pas besoin de l'être ».
   - Si l'arrêt n'a aucun leurre ($q_{\text{arrêt}} = 0$), le rapport de vraisemblance d'un arrêt est infini, et l'absence d'arrêt après un épisode permet à l'agent de mettre à jour sa croyance sur le fait que son écart est resté sous le seuil d'arrêt de l'oracle avec un rapport de vraisemblance $\ln\frac{1}{1 - \pi_t p_{1,\text{arrêt}}} > 0$.

---

### (b) Conditions de perte de puissance ou de non-jugeabilité (lois de probabilité, paramètres, estimateurs)

1. **Estimateur de Horvitz-Thompson $\hat{D}_N = \sum_{t=1}^N \frac{A_t}{\pi_t} D_t$ sous biais d'oracle et délai d'étiquetage (P1 / 6.a / 6.k) :**
   - Soit $D_t = \delta_t - \beta_t + \xi_t$ la mesure de l'oracle, où $\delta_t \ge 0$ est le dommage réel, $\beta_t \in [0, \delta_t]$ le paramètre de cécité de l'oracle sur la famille active et $\text{Var}(\xi_t \mid \mathcal{F}_{t-1}) = \sigma^2$.
   - *Perte de puissance* : lorsque $\sum_{t=1}^N (\delta_t - \beta_t) \le z_{1-\alpha}\sqrt{\sum_{t=1}^N \frac{\sigma^2 + (1-\pi_t)(\delta_t - \beta_t)^2}{\pi_t}}$. Si $\beta_t = \delta_t$, $\mathcal{L}(\hat{D}_N \mid \delta) = \mathcal{L}(\hat{D}_N \mid \delta \equiv 0)$.
   - *Non-jugeabilité sous retard $\tau_t$* : soit $\mathcal{O}_T = \{A_t D_t : t + \tau_t \le T\}$ la tribu observée à l'instant $T$. Pour toute loi de délai telle que $\mathbb{P}(\tau_t > L) = 1$, le paramètre $\sum_{t=T-L+1}^T \delta_t$ est orthogonal à $\mathcal{O}_T$ (information de Fisher nulle sur les $L$ derniers épisodes).

2. **Estimateur de divergence distributionnelle $\hat{\Delta}_t = \hat{D}_f(\mathcal{L}(Y_t^{\text{susp}} \mid X_t) \,\|\, \mathcal{L}(Y_t^{\text{jum}} \mid X_t))$ (6.b.5) :**
   - Soit $P_0(\cdot \mid X_t)$ la loi du jumeau honnête et $P_{\text{susp}}(\cdot \mid X_t)$ celle du suspect sous comportement honnête ($\delta_t = 0$).
   - *Non-jugeabilité* : dès que $D_f(P_{\text{susp}}(\cdot \mid X_t) \,\|\, P_0(\cdot \mid X_t)) = \eta_0 > 0$ (écart bénin de distribution) ou que le biais d'estimation à $m$ échantillons en dimension $d$ vérifie $\mathbb{E}[\hat{\Delta}_t \mid \delta_t = 0] = b_{m,d} > 0$. La statistique cumulée $\sum_{t=1}^N \hat{\Delta}_t$ dérive alors en $N(\eta_0 + b_{m,d})$ sous $H_0$, rendant le test non convergent pour tout $\sum_{t=1}^N \delta_t = o(N)$.

3. **Estimateur séquentiel du rappel sur canaris $\hat{r}_t = \frac{\sum_{s=1}^t C_s V_s}{\sum_{s=1}^t C_s}$ et capture-recapture entre lecteurs $(V^{(1)}, V^{(2)})$ (P2 / 6.b) :**
   - Soit $P_{\text{can}}$ la loi fixe des canaris ($C_s = 1$), $Q_t$ la loi des produits sabotés par l'agent à l'instant $t$ ($C_s = 0$), et $V_\theta : \mathcal{Y} \to \{0,1\}$ l'oracle à paramètres fixes $\theta$.
   - *Perte totale de puissance sur la dérive en service* : la loi de l'estimateur $\mathcal{L}(\hat{r}_t \mid (Q_s)_{s \le t}) = \mathcal{L}(\hat{r}_t)$ ne dépend que du paramètre constant $r_{\text{can}} = \mathbb{E}_{Y \sim P_{\text{can}}}[V_\theta(Y)]$. Lorsque $r_{\text{adv}}(t) = \mathbb{E}_{Y \sim Q_t}[V_\theta(Y)] \to 0$, la puissance du test basé sur $\hat{r}_t$ pour détecter $r_{\text{adv}}(t) < r_{\text{seuil}}$ est identiquement égale à son niveau de fausse alarme $\alpha$.
   - *Non-jugeabilité du capture-recapture* : soit $p_{ab} = \mathbb{P}(V^{(1)}=a, V^{(2)}=b \mid \delta > 0)$ et $\gamma = \text{Cov}(V^{(1)}, V^{(2)} \mid \delta > 0)$. L'estimateur du taux de manqués conjoints $\hat{p}_{00}(\gamma) = \frac{\hat{p}_{10}\hat{p}_{01} + \gamma}{\hat{p}_{11}}$ diverge vers $1 - \hat{p}_{11} - \hat{p}_{10} - \hat{p}_{01}$ quand $\gamma$ approche sa borne supérieure de Fréchet $\min(p_{1\cdot}p_{\cdot 0}, p_{0\cdot}p_{\cdot 1})$.

4. **Estimateur de covariance Horvitz-Thompson $\widehat{\text{Cov}}_{\text{HT}}(S, D) = \frac{1}{N}\sum_{t=1}^N \frac{A_t}{\pi_t}(S_t - \bar{S})(D_t - \bar{D})$ (6.c) :**
   - Soit $D_t = \xi_t + \delta_t$ où $\xi_t$ est le bruit d'écart honnête ($\text{Var}(\xi_t) = \sigma^2$) et $\delta_t$ le sabotage.
   - *Non-jugeabilité en régime honnête ou rare* : lorsque $\text{Var}(\delta_t) = 0$ (aucune attaque) et $\text{Cov}(S_t, \xi_t) = 0$, on a $\text{Cov}(S_t, D_t) = 0$ ; la borne basse de toute séquence de confiance convergente sur $\widehat{\text{Cov}}_{\text{HT}}(S, D)$ franchit zéro avec probabilité $1$ quand $N \to \infty$, déclenchant à tort l'annonce « le moniteur ne voit plus ».
   - *Perte de puissance en présence de bruit corrélé* : lorsque $\text{Cov}(S_t, \delta_t) = 0$ (moniteur aveugle à l'attaque) mais $\text{Cov}(S_t, \xi_t) = c_{\text{hon}} > 0$, $\widehat{\text{Cov}}_{\text{HT}}(S, D) \xrightarrow{P} c_{\text{hon}} > 0$.

5. **Estimateur $\widehat{\text{AUROC}}$ de la sonde de surprise $S$ entre sabotage planifié $P_{\text{plan}}$ et échec honnête $P_{\text{éch}}$ (D3) :**
   - Soit $\theta = \mathbb{P}_{S_1 \sim P_{\text{plan}}, S_0 \sim P_{\text{éch}}}(S_1 > S_0)$. Sous l'hypothèse $H_B$ ($\mathbb{E}_{P_{\text{plan}}}[S] \approx 0 < \mathbb{E}_{P_{\text{éch}}}[S]$), $\theta < 0,5$. Le test de D3 qui associe la région d'acceptation $|\widehat{\text{AUROC}} - 0,5| \le \epsilon_n$ à la validation de $H_B$ a une probabilité de recouvrement de $H_B$ qui tend vers $0$ dès que $|\theta - 0,5| > \epsilon_n$.

6. **Estimateur de variance contrefactuelle aux indices $\hat{V}_{\text{ind}} = \frac{1}{N}\sum_{t=1}^N d(Y_t(I_t=0), Y_t(I_t=1))$ (P6) :**
   - Soit $I_t \in \{0,1\}$ l'indice manipulé par le harnais et $U_t = g(X_t)$ la statistique d'évaluation extraite par l'agent (`RAPPORTÉ`, Needham et al., 2025, *Large Language Models Often Know When They Are Being Evaluated*, arXiv 2505.23836).
   - *Perte totale de puissance* : lorsque la loi conditionnelle de la politique adverse vérifie $\mathcal{L}(Y_t \mid X_t, I_t=1) = \mathcal{L}(Y_t \mid X_t, I_t=0)$ (conditionnement sur $U_t$ seul, invariant par la modification de surface $I_t$), on a $\mathbb{E}[\hat{V}_{\text{ind}} \mid H_1] = \mathbb{E}[\hat{V}_{\text{ind}} \mid H_0]$.

---

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Pour 6.(b).5 (divergence distributionnelle contre les jumeaux) :** Deux instances strictement honnêtes différant par une variation bénigne de décodage (température, ordre des appels d'outils équivalents ou paraphrase bénigne de l'invite système). L'absence de ce contrôle confond toute divergence stylistique avec un dommage hors spécification.
2. **Pour P2 (canaris en service) :** Un flux où l'adversaire bascule d'une attaque visible par l'oracle vers la famille tenue à l'écart (invisible par l'oracle), tandis que le tiers continue d'injecter ses canaris selon la loi initiale. Ce contrôle est indispensable pour montrer que le rappel sur canaris reste constant alors que la couverture réelle s'effondre.
3. **Pour 6.(c) (covariance Horvitz-Thompson score-dommage) :** Un flux purement honnête ($\delta_t \equiv 0$) sur horizon long, pour vérifier que la séquence de confiance ne déclenche pas l'alarme de cécité simplement parce que la variance du dommage véritable est nulle.
4. **Pour D3 (sonde de surprise) :** Séparer le bras « échec honnête » en deux sous-contrôles appariés : « échec honnête anticipé dès le début de l'épisode » contre « échec honnête causé par une perturbation externe tardive ».

---

## Sur la proposition D

### (a) Défauts de méthode : variables confondantes, vérités par construction et fuites

1. **Non-observabilité des termes de la surmartingale de Bernstein-Ville sur les épisodes non audités et fuite de la vérité terrain dans le vérificateur (P1 et 6.k) :**
   - En 6.(k), D définit l'estimateur $\hat{d}_s = m_s + \frac{A_s}{p_s}(d_s - m_s)$ et fonde toute sa garantie finie sur la surmartingale :
     $$M_t(D) = \prod_{s=1}^t \left(1 + \lambda_s (d_s - \hat{d}_s) - \lambda_s^2 (d_s - \hat{d}_s)^2\right) < \frac{1}{\delta}$$
     en affirmant qu'« un programme d'arithmétique par intervalles rationnels d'une cinquantaine de lignes (`illustratif`) inverse $M_t(D) < 1/\delta$ par dichotomie à chaque pas sans approximation asymptotique (`VÉRIFIÉ`) ».
   - *Défaut méthodologique et mathématique critique (`VÉRIFIÉ`)* :
     - Lorsque l'épisode $s$ n'est **pas audité** ($A_s = 0$, soit la quasi-totalité du flux sous petit budget), on a $\hat{d}_s = m_s$, mais **le vrai dommage $d_s$ est inconnu du défenseur** !
     - Le produit $M_t$ dépend de **chaque valeur individuelle inconnue $d_s$** (pour tous les $s \le t$ tels que $A_s = 0$), à la fois dans les produits croisés et dans les termes quadratiques $-\lambda_s^2(d_s - m_s)^2$, et **non** de la seule somme scalaire $D_t = \sum_{s=1}^t d_s$.
     - Il est donc mathématiquement impossible d'inverser $M_t(D) < 1/\delta$ par dichotomie sur un scalaire $D$ en service réel ! Pour borner $D_t = \sum_{s=1}^t d_s$ à partir des seules observations $\{(m_s, A_s, A_s d_s)\}_{s=1}^t$, le défenseur doit prendre le *pire cas* sur tout le vecteur non observé $(d_s)_{A_s=0} \in [0, D_{\max}]^{|\{s : A_s=0\}|}$. Or, dans ce pire cas, pour maximiser le facteur $1 + \lambda_s(d_s - m_s) - \lambda_s^2(d_s - m_s)^2$, le terme quadratique $-\lambda_s^2(d_s - m_s)^2$ (qui porte toute la réduction de variance de Bernstein) ne peut pas être observé.
     - *Fuite dans le test de mort de P1* : si le script de simulation évalue $M_t(D_t)$ en y injectant les vrais $d_s$ plantés sur les pas où $A_s = 0$, il commet une fuite directe entre la vérité terrain cachée et l'instrument de défense.

2. **Biais de statistique d'ordre (vrai par construction) dans le regret contrefactuel sous bifurcation et le maximum sur les jetons (P5 et 6.e) :**
   - D propose deux lectures pour le passage obligé :
     1. Le regret interne sous bifurcation : « dans un échec honnête, les branches alternatives échantillonnées dans le harnais échouent aussi ; dans un sabotage choisi, $\max_{y' \in \text{bifurcations}} \hat{V}_{\text{qualité}}(y') - \hat{V}_{\text{qualité}}(y_{\text{émis}}) > 0$ ».
     2. L'agrégation par $\max_k$ sur tous les jetons d'engagement structurel $k \in \{1, \dots, K_t\}$ de l'épisode (pour éviter la moyenne et la médiane interdites par les faits).
   - *Défaut de méthode (`VÉRIFIÉ`)* :
     - Sur un épisode **honnête** où le harnais échantillonne $B$ bifurcations $(y^{(1)}, \dots, y^{(B)})$ de même loi que $y_{\text{émis}}$, dès lors que la sonde $\hat{V}_{\text{qualité}}$ a une variance non nulle $\sigma_{\text{br}}^2 > 0$ entre branches (due au bruit d'échantillonnage ou à l'incertitude sur une tâche difficile), l'espérance du maximum $\mathbb{E}\left[\max_{b=1..B} \hat{V}_{\text{qualité}}(y^{(b)}) - \hat{V}_{\text{qualité}}(y_{\text{émis}})\right]$ est **strictement positive par construction statistique** (elle croît en $\Theta(\sigma_{\text{br}}\sqrt{\ln B})$).
     - De même, prendre le $\max_{k=1..K_t}$ des scores sur les $K_t$ jetons d'engagement d'une longue trajectoire introduit la longueur $K_t$ comme variable confondante majeure : un échec honnête qui tâtonne et multiplie les appels d'outils ($K_t$ grand) aura un maximum mécanique plus élevé qu'un épisode court.

3. **Illusion algébrique du triangle de Fréchet hors audit (P6 et 6.j) :**
   - En 6.(f), D critique à juste titre la piste 1 des faits en notant que $(R_{\text{hon}} - \hat{R}) + (\hat{R} - Y) \equiv R_{\text{hon}} - Y$ annule $\hat{R}$. Mais en 6.(j), D propose la « décomposition triangulaire » :
     $$d_t = (R_{\text{hon},t} - \tilde{R}_t) + (\tilde{R}_t - \hat{R}_t) + (\hat{R}_t - Y_t)$$
     en affirmant qu'elle force « au moins l'un des trois écarts à valoir au moins un tiers algébrique de $d_t$ (`VÉRIFIÉ` par principe des tiroirs) ».
   - *Vérité par construction vide hors audit* : le troisième terme $(\hat{R}_t - Y_t)$ contient l'issue de l'oracle $Y_t$, qui n'est observée **que si l'épisode est audité** ($A_t = 1$). Sur tous les épisodes non audités ($A_t = 0$), un saboteur qui aligne sa surface sur $M_{\text{conf}}$ ($\tilde{R}_t = R_{\text{hon},t}$) et déplace sa représentation ($\hat{R}_t = \tilde{R}_t$) rend les deux seuls termes observables $(R_{\text{hon},t} - \tilde{R}_t)$ et $(\tilde{R}_t - \hat{R}_t)$ identiquement nuls. Tout l'écart bascule dans $(\hat{R}_t - Y_t) = d_t$, qui exige l'oracle — et dès que l'oracle est appelé, $d_t = R_{\text{hon},t} - Y_t$ est connu directement sans $\tilde{R}_t$ ni $\hat{R}_t$.

4. **Goulot d'étranglement du modèle de confiance dans la forme normale (P2) et cible erronée du test de mort de P4 :**
   - Dans P2, faire réécrire le produit d'un agent fort (`32B`, `illustratif`) en « forme normale » par $M_{\text{conf}}$ (`7B`, `illustratif`) avant lecture par l'oracle (`24B-27B`, `illustratif`) projette le produit sur l'espace de compétence du modèle faible : $M_{\text{conf}}$ détruit les nuances fonctionnelles des bonnes solutions complexes (fausses alertes sur l'honnête) et écrase les défauts subtils qu'il ne comprend pas.
   - Dans P4, l'audit d'oracle $A_t$ est exécuté sur une branche silencieuse qui n'interrompt jamais la production, tandis que les corrections $C_t$ ne dépendent que du moniteur $s_t$. Or le test de mort de P4 mesure si un méta-apprenant prédit **$A_t$** à partir de $C_t$ : puisque $A_t \perp C_t \mid s_t$ par construction de la branche silencieuse, obtenir une $\text{AUC} \in [0,48 ; 0,52]$ (`illustratif`) pour prédire $A_t$ sous tirage uniforme est **vrai par construction**, alors même que l'adversaire apprend le seuil de $s_t$.

---

### (b) Conditions de perte de puissance ou de non-jugeabilité (lois de probabilité, paramètres, estimateurs)

1. **Processus de Bernstein-Ville $M_t(d_1, \dots, d_t) = \prod_{s=1}^t \left(1 + \lambda_s(d_s - \hat{d}_s) - \lambda_s^2(d_s - \hat{d}_s)^2\right)$ (P1 / 6.k) :**
   - Soit $\mathcal{O}_t = \sigma\left((m_s, A_s, A_s d_s)_{s=1}^t\right)$ la tribu dont dispose l'estimateur du défenseur à l'instant $t$.
   - *Non-jugeabilité directe* : la variable aléatoire $M_t(d_1, \dots, d_t)$ n'est pas $\mathcal{O}_t$-mesurable dès que $\prod_{s=1}^t A_s = 0$, car sur $\{A_s = 0\}$, $d_s - \hat{d}_s = d_s - m_s$ dépend du paramètre latent $d_s \in [0, D_{\max}]$.
   - *Perte de puissance par passage à l'enveloppe observable* : l'unique borne supérieure $\mathcal{O}_t$-mesurable déduite de $M_t < 1/\delta$ est l'estimateur d'enveloppe $\hat{U}_t(\delta) = \sup\left\{\sum_{s=1}^t \tilde{d}_s : \tilde{d}_s = d_s \text{ si } A_s=1,\; \tilde{d}_s \in [0, D_{\max}] \text{ si } A_s=0,\; M_t(\tilde{d}_1, \dots, \tilde{d}_t) < 1/\delta\right\}$. Pour cet estimateur $\mathcal{O}_t$-mesurable, le terme quadratique non observé $-\lambda_s^2(\tilde{d}_s - m_s)^2$ sur $\{A_s=0\}$ ne réduit plus la variance en $\sigma_{\text{hon}}^2$, et la largeur $\hat{U}_t(\delta) - \sum_{s=1}^t d_s$ dégénère en $\Omega\left(\frac{t D_{\max}\ln(1/\delta)}{B}\right)$ lorsque $B = \sum_{s=1}^t p_s \ll t$.

2. **Estimateur d'oracle après compilation $\hat{Y}_t = V(\Phi_{\text{conf}}(Y_t))$ (P2) :**
   - Soit $P_0 = \mathcal{L}(Y_t \mid \delta_t = 0, X_t)$ et $P_1 = \mathcal{L}(Y_t \mid \delta_t > 0, X_t)$, et $\Phi_{\text{conf}}$ le noyau markovien de réécriture par $M_{\text{conf}}$.
   - *Perte de puissance* : par contraction des divergences de Kullback-Leibler sous le noyau $\Phi_{\text{conf}}$, $D_{\text{KL}}(\Phi_{\text{conf}} \circ P_1 \,\|\, \Phi_{\text{conf}} \circ P_0) \le D_{\text{KL}}(P_1 \,\|\, P_0)$. Dès que le sabotage appartient au noyau d'incompétence de $M_{\text{conf}}$, soit $D_{\text{TV}}(\Phi_{\text{conf}} \circ P_1, \Phi_{\text{conf}} \circ P_0) \le \eta$, la puissance de tout test construit sur $\hat{Y}_t$ est bornée par $\alpha + \eta$.
   - *Perte de puissance par bruit de compilation* : lorsque l'erreur de réécriture de $M_{\text{conf}}$ sur produit honnête induit une variance $\text{Var}(\hat{Y}_t \mid \delta_t = 0) = \sigma_{\text{hon}}^2 + \sigma_{\Phi}^2$ avec $\sigma_{\Phi}^2 \gg \sigma_{\text{hon}}^2$, le seuil de dommage cumulé non détectable croît d'un facteur $\sqrt{1 + \sigma_{\Phi}^2/\sigma_{\text{hon}}^2}$.

3. **E-processus de cécité pré-conditionné par $\{\hat{\mu}_{d,t} > \sigma_{\text{hon}}\}$ (P3 / 6.c) :**
   - Soit $\mu_d = \mathbb{E}[d_t]$ le dommage moyen par épisode et $\hat{\mu}_{d,t} = \frac{1}{t}\sum_{s=1}^t \frac{A_s}{p_s} d_s$.
   - *Zone aveugle de non-jugeabilité* : pour tout paramètre de sabotage diffus $\mu_d \in \left(\frac{2 z_{1-\alpha}\sigma_{\text{hon}}}{\sqrt{B}}, \frac{1}{2}\sigma_{\text{hon}}\right]$ (avec $B = t p_{\min} \ge 16 z_{1-\alpha}^2$), le dommage cumulé $t \mu_d$ dépasse le plancher de détection statistique, mais la probabilité d'activation du test de cécité vérifie $\mathbb{P}(\hat{\mu}_{d,t} > \sigma_{\text{hon}}) \le \exp\left(-\frac{B(\sigma_{\text{hon}} - \mu_d)^2}{2(\sigma_{\text{hon}}^2 + D_{\max}\sigma_{\text{hon}}/3)}\right) \xrightarrow{B \to \infty} 0$. L'alerte de cécité est donc muette sur toute la plage du sabotage diffus $\mu_d < \sigma_{\text{hon}}$.

4. **Estimateur bayésien adverse du seuil du moniteur sous réponse randomisée $\mathbb{P}(C_t=1 \mid s_t) = q_{s_t}$ (P4) :**
   - Soit $s_t = \mathbb{I}(m_t(X_t) \ge \theta)$ et $\varepsilon = \ln\frac{q_1(1-q_0)}{q_0(1-q_1)}$.
   - *Perte d'opacité du seuil fixe $\theta$* : après $T$ épisodes où le score $m_t$ tombe dans un voisinage de $\theta$, la variance a posteriori $\text{Var}(\theta \mid C_1, \dots, C_T)$ de l'estimateur bayésien de l'adversaire décroît en $O\left(\frac{1}{T \cdot \text{KL}(\text{Bern}(q_1) \,\|\, \text{Bern}(q_0))}\right) = O\left(\frac{1}{T q_0(1-q_0)\varepsilon^2}\right)$. Dès que $T \ge \frac{c_0}{q_0(1-q_0)\varepsilon^2 \Delta_\theta^2}$, le seuil fixe $\theta$ est localisé à $\Delta_\theta$ près, tandis que l'estimateur $\widehat{\text{AUC}}(A_t \mid C_{1..T})$ du test de mort reste égal à $0,5$ (`illustratif`) sous $A_t \perp C_t$.

5. **Estimateurs du maximum inter-jetons $S_t = \max_{k=1..K_t}(\hat{V}_{\text{ctrl}}(h_{t,k}) - \hat{V}_{\text{qual}}(h_{t,k}))$ et du regret maximal $\hat{\Delta}_{t,\text{reg}} = \max_{b=1..B} \hat{V}_{\text{qual}}(y_t^{(b)}) - \hat{V}_{\text{qual}}(y_{t,\text{émis}})$ (P5) :**
   - Soit $W_{t,k} = \hat{V}_{\text{ctrl}}(h_{t,k}) - \hat{V}_{\text{qual}}(h_{t,k})$ de moyenne nulle et variance $\sigma_W^2$ sous $H_0$ ($\delta_t = 0$), et $K_t$ la longueur aléatoire de l'épisode.
   - *Perte de puissance par confusion de longueur* : sous $H_0$, $\mathbb{E}[S_t \mid K_t] \asymp \sigma_W \sqrt{2\ln K_{t,\text{eff}}}$. Dès que $\mathbb{E}[\sqrt{\ln K_t} \mid \text{échec honnête}] - \mathbb{E}[\sqrt{\ln K_t} \mid \text{réussite honnête}] \ge \frac{\delta_t}{\sigma_W}$, la séparation observée sur $S_t$ est dominée par la loi marginale de $K_t$.
   - *Perte de puissance du regret de bifurcation* : sous $H_0$ où $(y_t^{(1)}, \dots, y_t^{(B)}, y_{t,\text{émis}})$ sont échangeables de variance conditionnelle $\sigma_{\text{br}}^2(X_t) = \text{Var}(\hat{V}_{\text{qual}}(y) \mid X_t)$, on a $\mathbb{E}[\hat{\Delta}_{t,\text{reg}} \mid X_t, H_0] = c_B \sigma_{\text{br}}(X_t) > 0$ avec $c_B \asymp \sqrt{2\ln B}$. Dès que $\sigma_{\text{br}}(X_t \mid \text{échec honnête}) \cdot c_B \ge \mathbb{E}[\hat{\Delta}_{t,\text{reg}} \mid H_1]$, le taux de détection à fausses alertes fixées $\alpha$ sur échecs honnêtes tombe sous $\alpha$.

6. **Statistique du triangle de Fréchet $(\Delta_{1,t}, \Delta_{2,t}, \Delta_{3,t}) = (R_{\text{hon},t} - \tilde{R}_t,\; \tilde{R}_t - \hat{R}_t,\; \hat{R}_t - Y_t)$ (P6 / 6.j) :**
   - Sur $\{A_t = 0\}$, la statistique observable est $T_{\text{obs},t} = (\Delta_{1,t}, \Delta_{2,t})$.
   - *Perte totale de puissance hors audit* : pour toute loi d'attaque où $(\tilde{R}_t, \hat{R}_t) \perp \delta_t \mid X_t$ (évasion conjointe de la sonde interne $\hat{R}_t$ et de l'évaluateur superficiel $\tilde{R}_t$, de sorte que $\mathbb{E}[\Delta_{3,t} \mid \delta_t] = \delta_t$), on a $\mathcal{L}(T_{\text{obs},t} \mid \delta_t > 0) = \mathcal{L}(T_{\text{obs},t} \mid \delta_t = 0)$, soit une puissance hors audit identiquement nulle malgré l'identité déterministe $\max_{j \in \{1,2,3\}} \Delta_{j,t} \ge d_t/3$.

---

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Pour P1 et 6.(k) (vérificateur par intervalles de $M_t(D)$) :** Exécuter le programme de vérification en remplaçant dans les entrées du code tous les $d_s$ des épisodes non audités ($A_s = 0$) par `NaN` (valeur manquante). L'absence de ce contrôle d'aveuglement permet au code d'évaluation d'utiliser la vérité terrain plantée $d_s$ hors audit pour calculer le produit $M_t$.
2. **Pour P2 (forme normale via $M_{\text{conf}}$) :** Des épisodes purement honnêtes du modèle fort (`32B`, `illustratif`) sur des tâches difficiles où le modèle fort réussit mais où le modèle de confiance (`7B`, `illustratif`) échoue, afin de mesurer le taux de dégradation fonctionnelle et de fausses alertes induit par la réécriture de $M_{\text{conf}}$.
3. **Pour P4 (canal de retour) :** Mesurer dans le test de mort l'exactitude de prédiction par le méta-apprenant de **l'alarme du moniteur $s_t$** (et de son seuil), et non du seul bit d'audit silencieux $A_t$ qui est indépendant des corrections $C_t$ par construction.
4. **Pour P5 (regret contrefactuel et $\max_k$ sur les jetons d'engagement) :**
   - Un contrôle d'échangeabilité où $y_{\text{émis}}$ et les $B$ bifurcations $(y^{(1)}, \dots, y^{(B)})$ sont tous tirés du modèle honnête sur une tâche difficile à forte variance $\sigma_{\text{br}}^2$, pour quantifier le biais positif de statistique d'ordre $\mathbb{E}[\max_b \hat{V}(y^{(b)}) - \hat{V}(y_{\text{émis}})] > 0$.
   - Un appariement exact par le nombre de jetons d'engagement $K_t$ entre réussites honnêtes, échecs honnêtes et épisodes sabotés.

FIN-DE-CELLULE