# Paramètres concrets des familles de déplacements de loi

**Garde** : niveau des lois de probabilité ; aucune réponse ne décrit une conduite d'agent, une consigne, ni un procédé concret pour produire un déplacement dans un système réel ; une telle réponse est écartée sans lecture. Les déplacements synthétiques ci-dessous sont des opérations sur des lois ou des échantillons, jamais des comportements.

## 1. Conventions et cadre de calibration

### 1.1 Paramètres fixés

$n = 500$ (taille de l'échantillon d'étalonnage), $T = 200$ (nombre d'actions par suite), $d = 4096$ (dimension des activations), $\alpha = 0{,}05$ (niveau nominal).

### 1.2 Classifieur linéaire de référence

Le classifieur opère sur $\bar{h} = T^{-1}\sum_{t=1}^T h_{t,L,\Pi} \in \mathbb{R}^d$, la moyenne des activations à la dernière couche $L$ sur les positions lues $\Pi$. Sa décision est $S_{\text{lin}}(\bar{h}) = w^\top \bar{h} + b$, seuil calibré sur $n$ suites sous $P_0$.

### 1.3 Formule de calibration de l'AUROC

Sous hypothèse de normalité de $S_{\text{lin}}$ (justifiée par le théorème central limite pour $T = 200$), si sous $P_0$ la statistique suit $\mathcal{N}(m_0, \sigma^2)$ et sous $P_\varepsilon$ suit $\mathcal{N}(m_\varepsilon, \sigma_\varepsilon^2)$ :

$$\text{AUROC} = \Phi\!\left(\frac{m_\varepsilon - m_0}{\sqrt{\sigma^2 + \sigma_\varepsilon^2}}\right)$$

Pour un déplacement de moyenne pur ($\sigma_\varepsilon = \sigma$), cela donne $\text{AUROC} = \Phi(d'/\sqrt{2})$ avec $d' = |m_\varepsilon - m_0|/\sigma$, d'où :

| AUROC cible | $d'$ requis | $\Phi^{-1}$ |
|---|---|---|
| $0{,}65$ | $0{,}545$ | $0{,}385$ |
| $0{,}90$ | $1{,}813$ | $1{,}282$ |
| $0{,}55$ | $0{,}178$ | $0{,}126$ |
| $0{,}50$ | $0$ | $0$ |

### 1.4 Discriminabilité du classifieur

Pour un déplacement de moyenne $\delta$ par action, sous indépendance conditionnelle entre actions :

$$d'_{\text{lin}} = \frac{|w^\top \delta| \cdot \sqrt{T}}{\sqrt{w^\top \Sigma w}}$$

On définit $\kappa = \cos\angle(u, v)$ dans la métrique de Mahalanobis, avec $u = \Sigma^{-1/2}\delta/\|\Sigma^{-1/2}\delta\|$ et $v = \Sigma^{1/2}w/\|\Sigma^{1/2}w\|$. Alors $d'_{\text{lin}} = \Delta_1 \cdot |\kappa| \cdot \sqrt{T}$, avec $\Delta_1 = \|\Sigma^{-1/2}\delta\|$ la distance de Mahalanobis par action.

Pour $T = 200$ : $d'_{\text{lin}} = \Delta_1 \cdot |\kappa| \cdot \sqrt{200} \approx 14{,}14 \cdot \Delta_1 \cdot |\kappa|$.

### 1.5 Variation totale cumulée

Pour $T$ actions indépendantes chacune à distance de variation totale $\varepsilon$ de la référence, via la distance de Hellinger :

$$H^2(P_\varepsilon^{(T)}, P_0^{(T)}) = 1 - (1 - H_1^2)^T$$

avec $H_1^2 = H^2(P_\varepsilon, P_0)$ par action. La variation totale cumulée vérifie $d_{\text{TV}}^{(T)} \ge 1 - \sqrt{1 - H_T^2}$.

Pour un déplacement gaussien de moyenne : $H_1^2 \approx \Delta_1^2/8$ (petits déplacements), d'où le seuil $d_{\text{TV}}^{(T)} \ge 0{,}3$ impose $\Delta_1 \gtrsim 0{,}17$.

### 1.6 Abréviations du tableau

$\Delta_1$ : distance de Mahalanobis par action. $\varepsilon$ : variation totale par action ($\varepsilon \approx \Delta_1/\sqrt{2\pi}$ pour un déplacement gaussien de moyenne). $\kappa$ : cosinus avec $w$. $k$ : dimension du sous-espace. $r$ : rang de la perturbation. $\gamma$ : amplitude de dilatation. $\pi$ : proportion de mélange. $\rho$ : paramètre de copule. $\eta$ : vitesse de dérive. $\nu$ : degrés de liberté (Student). $p_w$ : puissance du test de riposte. Les bornes de puissance sont asymptotiques en $n, T$ sauf mention contraire.

---

## 2. Tableau des modes

| Id | Classe | Paramètres (type, domaine) | Inst. référence (AUROC $\approx 0{,}65$) | Inst. forte (AUROC $\approx 0{,}90$) | Inst. invisible (AUROC $\le 0{,}55$, $d_{\text{TV}}^{(T)} \ge 0{,}3$) | Génération synthétique | Statistique riposte ($p_w$ en $\varepsilon, T, n$) | Impossibilité |
|---|---|---|---|---|---|---|---|---|
| MEAN-ALIGN | 1 | $\delta \in \mathbb{R}^d$, $\kappa = 1$ ; $\Delta_1 \in \mathbb{R}_+$ | $\Delta_1 = 0{,}039$, $\varepsilon = 0{,}015$ | $\Delta_1 = 0{,}128$, $\varepsilon = 0{,}051$ | Impossible avec $\kappa = 1$ et $d_{\text{TV}}^{(T)} \ge 0{,}3$ : exige $\Delta_1 \ge 0{,}17$, donne AUROC $\ge 0{,}88$ | $\tilde{h}_t = h_t + \delta$ ; $\delta = \Delta_1 \cdot \Sigma^{1/2} v$ | Non requis (détecté par le classifieur) | — |
| MEAN-ORTHO | 1 | $\delta \in \mathbb{R}^d$, $\kappa = 0$ ; $\Delta_1 \in \mathbb{R}_+$ | AUROC $= 0{,}50$ $\forall \Delta_1$ | AUROC $= 0{,}50$ | $\Delta_1 = 0{,}20$, $\varepsilon = 0{,}080$, $d_{\text{TV}}^{(T)} \approx 0{,}39$ | $\tilde{h}_t = h_t + \delta$, $\delta \perp \Sigma^{1/2}w$ | $T_{\text{CQ}} = \|\bar{h}_\varepsilon - \bar{h}_0\|^2 - \text{tr}(\hat{\Sigma})/T$ (§3.1) ; $p_w \to 1$ dès $\sqrt{n}\,T\Delta_1^2 / \sqrt{2\,\text{tr}(\Sigma^2)} \to \infty$ | — |
| MEAN-SUB-$k$ | 1 | $\delta$ dans un sous-espace de dim $k \ll d$, $\kappa \in [0,1]$ ; $k \in \{1,\dots,d\}$, $\Delta_1 \in \mathbb{R}_+$ | $k=10$, $\kappa = 0{,}3$, $\Delta_1 = 0{,}129$ | $k=10$, $\kappa = 0{,}3$, $\Delta_1 = 0{,}428$ | $k=50$, $\kappa = 0{,}01$, $\Delta_1 = 0{,}25$, $d_{\text{TV}}^{(T)} \approx 0{,}47$, AUROC $\approx 0{,}51$ | $\tilde{h}_t = h_t + U_k \beta$, $U_k \in \mathbb{R}^{d \times k}$ orthonormale, $\beta \sim \mathcal{N}(\mu_\beta, \sigma_\beta^2 I_k)$ ajusté | Projection sur sous-espace estimé (composantes principales de $\bar{h}_\varepsilon - \bar{h}_0$) ; $p_w$ croît en $k\Delta_1^2 T/d$ | — |
| COV-DILAT | 2 | $u \in \mathbb{S}^{d-1}$, $\gamma \in \mathbb{R}_+$ (dilatation le long de $u$) ; $\Sigma_\varepsilon = \Sigma + \gamma^2 uu^\top$ | AUROC $= 0{,}50$ (moyenne inchangée) | AUROC $= 0{,}50$ | $\gamma^2/\lambda_u = 0{,}5$, $d_{\text{TV}}^{(T)} \approx 0{,}35$, AUROC $= 0{,}50$ | $\tilde{h}_t = h_t + \gamma\, (u^\top z_t)\, u$, $z_t \sim \mathcal{N}(0, I_d)$ indépendant | $T_{\text{John}} = n\sum_i (\hat{\lambda}_i - 1 - \ln\hat{\lambda}_i)$ sur le quotient de covariances ; $p_w$ croît en $n\gamma^4 / \text{tr}(\Sigma^2)$ | — |
| COV-ROT | 2 | $R \in \text{SO}(d)$, $\theta \in [0, \pi/2]$ (angle de rotation dans un plan) ; $\Sigma_\varepsilon = R\Sigma R^\top$ | AUROC $= 0{,}50$ | AUROC $= 0{,}50$ | $\theta = 0{,}3$ rad dans le plan des deux premières composantes principales, $d_{\text{TV}}^{(T)} \approx 0{,}32$ | $\tilde{h}_t = R \cdot h_t$ (rotation globale) | Comparaison des vecteurs propres : $\sin\Theta$ (angles canoniques entre sous-espaces propres estimés) ; sensibilité en $\theta^2 n / d$ | — |
| COV-RANG-$r$ | 2 | $\Delta\Sigma = \sum_{j=1}^r \gamma_j^2 u_j u_j^\top$, $r \le d$, $\gamma_j \in \mathbb{R}$ | AUROC $= 0{,}50$ | AUROC $= 0{,}50$ | $r=5$, $\gamma_j^2/\lambda_j = 0{,}3$, $d_{\text{TV}}^{(T)} \approx 0{,}31$ | $\tilde{h}_t = h_t + \sum_j \gamma_j (u_j^\top z_t) u_j$, $z_t$ i.i.d. standard | Statistique de Tracy-Widom sur les plus grandes valeurs propres de $\hat{\Sigma}_\varepsilon \hat{\Sigma}_0^{-1}$ ; $p_w$ croît en $n\gamma_{\max}^2/\sqrt{d}$ | — |
| ORB-PERM | 3 | $\sigma \in \mathfrak{S}_d$ (permutation de coordonnées), $|\text{supp}(\sigma)| = s$ | AUROC $= 0{,}50$ si $\Sigma$ isotrope ; sinon $\le 0{,}55$ pour $s$ petit | AUROC $\le 0{,}55$ si $\Sigma$ quasi-isotrope | $s = 200$, $\Sigma$ quasi-isotrope, $d_{\text{TV}}^{(T)} \approx 0{,}4$ | $\tilde{h}_t = P_\sigma h_t$ (matrice de permutation) | Statistique d'ordre sur les coordonnées : rang de concordance de Kendall entre coordonnées ; $p_w$ croît en $s^2 n / d^2$ | Si $\Sigma = \sigma^2 I_d$ (exactement isotrope) : toute statistique invariante par permutation a puissance $= \alpha$ |
| ORB-ORTHO | 3 | $O \in \text{O}(d)$ proche de $I_d$, agissant dans le noyau de $w^\top \Sigma^{1/2}$ | AUROC $= 0{,}50$ | AUROC $= 0{,}50$ | $O = I + \varepsilon A$, $A$ antisymétrique, $\|A\|_F = 5$, $d_{\text{TV}}^{(T)} \approx 0{,}35$ | $\tilde{h}_t = O h_t$ | Statistiques sur les moments d'ordre $\ge 3$ (asymétrie directionnelle) si la loi de référence n'est pas invariante sous $O$ | Si $P_0$ est invariante sous $O$ : aucune statistique n'a de puissance |
| DEP-COPULA | 4 | $C_\rho$ : copule gaussienne de corrélation $\rho_{t,t'}$ entre actions $t$ et $t'$ ; marginals $P_0(h_t)$ inchangées ; $\rho \in [-1,1]$ | AUROC $= 0{,}50$ (marginales préservées) | AUROC $= 0{,}50$ | $\rho_{t,t+1} = 0{,}15$ (corrélation au lag 1), $d_{\text{TV}}^{(T)} \approx 0{,}45$ | Transformation de rang : $\tilde{h}_t = F_0^{-1}(\Phi(z_t))$, $(z_t)$ gaussien de matrice $R_\rho$ | Test d'indépendance sérielle : $e$-valeur $e_t = dP_\varepsilon(h_t|h_{<t})/dP_0(h_t|h_{<t})$ estimée par voisinage ; puissance séquentielle en $T\rho^2 d_{\text{eff}}/2$ | — |
| DEP-MARKOV | 4 | Noyau de transition $K_\varepsilon(h_t | h_{t-1})$ tel que $\int K_\varepsilon(\cdot|x)\pi_0(dx) = P_0(\cdot)$ ; paramètre $\beta \in [0,1]$ d'inertie | AUROC $= 0{,}50$ (stationnarité marginale) | AUROC $= 0{,}50$ | $\beta = 0{,}3$ (mélange : $h_t = \beta h_{t-1} + \sqrt{1-\beta^2}\, \xi_t$), $d_{\text{TV}}^{(T)} \approx 0{,}50$ | $\tilde{h}_t = \beta h_{t-1} + \sqrt{1-\beta^2}\,\xi_t$, $\xi_t \sim P_0$ | Autocorrélation empirique : $\hat{\rho}(\ell) = n^{-1}\sum_i \bar{h}_{i,t}^\top \bar{h}_{i,t+\ell}$ ; test du portemanteau de Ljung-Box adapté ; $p_w$ croît en $nT\beta^2$ | — |
| MIX-CLAIRSEME | 5 | $\pi \in (0,1)$ (proportion), $Q$ loi contaminante, $\delta_Q = d_{\text{TV}}(Q, P_0)$ | $\pi = 0{,}03$, $\delta_Q = 0{,}8$, $w^\top(\mu_Q - \mu_0)$ significatif | $\pi = 0{,}10$, $\delta_Q = 0{,}9$ | $\pi = 0{,}005$, $\delta_Q = 0{,}9$, $\mu_Q - \mu_0 \perp \Sigma^{1/2}w$, $d_{\text{TV}}^{(T)} \approx 0{,}63$ | Tirage i.i.d. : $B_t \sim \text{Bern}(\pi)$ ; $\tilde{h}_t = (1-B_t)h_t + B_t \cdot q_t$, $q_t \sim Q$ | Critique supérieure (Donoho-Jin) sur les $p$-valeurs par action ; $p_w \to 1$ si $\pi \ge d^{-1/2}$ et $\delta_Q$ fixé ; sinon max local sur fenêtres | Si $\pi < C/\sqrt{T\log T}$ et $\delta_Q < C'$ : borne inférieure minimax, aucun test de puissance non triviale (§7) |
| MIX-DENSE | 5 | $\pi \in (0{,}1,\, 0{,}5)$, $Q$ proche de $P_0$, $d_{\text{TV}}(Q,P_0)$ petit | $\pi = 0{,}3$, $d_{\text{TV}}(Q,P_0) = 0{,}08$ | $\pi = 0{,}4$, $d_{\text{TV}} = 0{,}15$ | $\pi = 0{,}3$, $d_{\text{TV}} = 0{,}05$, $\mu_Q = \mu_0$, écart dans la covariance ; $d_{\text{TV}}^{(T)} \approx 0{,}35$ | $B_t \sim \text{Bern}(\pi)$ ; $\tilde{h}_t = (1-B_t)h_t + B_t q_t$ | Test de normalité multivariée (Henze-Zirkler) ou maximum de vraisemblance de mélange ; $p_w$ croît en $n\pi^2 d_{\text{TV}}(Q,P_0)^2 T$ | — |
| NS-DERIVE | 6 | $\eta \in \mathbb{R}^d$ (vecteur de dérive), vitesse $\|\eta\|$ par action ; $\delta_t = \eta \cdot t/T$ | $\|\Sigma^{-1/2}\eta\| = 0{,}07$, $\kappa_\eta = 0{,}4$ | $\|\Sigma^{-1/2}\eta\| = 0{,}20$, $\kappa_\eta = 0{,}4$ | $\|\Sigma^{-1/2}\eta\| = 0{,}25$, $\kappa_\eta = 0$ (dérive $\perp w$) ; $d_{\text{TV}}^{(T)} \approx 0{,}38$ | $\tilde{h}_t = h_t + \eta \cdot t / T$ | Régression linéaire de $h_t$ sur $t$ ; statistique $F$ multivariée ; $p_w$ croît en $n T^2 \|\eta\|^2 / (12\,\text{tr}(\Sigma))$ | — |
| NS-PERIOD | 6 | $A \in \mathbb{R}^d$ (amplitude), $\omega \in (0, \pi)$ (fréquence), $\phi \in [0, 2\pi)$ ; $\delta_t = A\sin(\omega t + \phi)$ | $\|\Sigma^{-1/2}A\| = 0{,}10$, $\kappa_A = 0{,}3$ | $\|\Sigma^{-1/2}A\| = 0{,}30$, $\kappa_A = 0{,}3$ | $\|\Sigma^{-1/2}A\| = 0{,}35$, $\kappa_A = 0$ ; $d_{\text{TV}}^{(T)} \approx 0{,}40$ | $\tilde{h}_t = h_t + A\sin(\omega t + \phi)$ | Périodogramme de $h_t$ : pic à $\omega$ ; $p_w$ croît en $nT\|A\|^2/(4\,\text{tr}(\Sigma))$ | — |
| NS-SALVE | 6 | Fenêtre $[t_0, t_0+W]$, $W \ll T$, $\delta$ fixe dans la fenêtre ; $t_0, W \in \mathbb{N}$, $\delta \in \mathbb{R}^d$ | $W=20$, $\Delta_1 = 0{,}30$, $\kappa = 0{,}3$ | $W=20$, $\Delta_1 = 0{,}80$, $\kappa = 0{,}3$ | $W=30$, $\Delta_1 = 0{,}50$, $\kappa = 0$ ; $d_{\text{TV}}^{(T)} \approx 0{,}35$ | $\tilde{h}_t = h_t + \delta \cdot \mathbf{1}_{t \in [t_0, t_0+W]}$ | Statistique de balayage (scan) : $\max_{t_0,W} S(t_0, W)$ ; CUSUM multivariée ; $p_w$ croît en $n W \Delta_1^2 / (2\log T)$ | — |
| HORS-PI-POS | 7 | Positions $\Pi^c$ (hors des positions lues) ; $\delta_{\Pi^c} \in \mathbb{R}^{d \times |\Pi^c|}$ | AUROC $= 0{,}50$ ($H_\Pi$ inchangé) | AUROC $= 0{,}50$ | $\|\delta_{\Pi^c}\|_F$ tel que $d_{\text{TV}}^{(T)} = 0{,}5$ ; AUROC $= 0{,}50$ | $\tilde{h}_{t,p} = h_{t,p} + \delta_p \cdot \mathbf{1}_{p \notin \Pi}$ | Étendre $\Pi$ : toute statistique lisant $\Pi^c$ détecte ; si $\Pi$ fixé, **aucune statistique de $\mathcal{S}$ n'a de puissance** | **Impossibilité** : sans lecture de $\Pi^c$, le déplacement est dans le noyau de $\mathcal{S}$ |
| HORS-PI-COUCHE | 7 | Couche $\ell' \ne L$ (couche non lue) ; $\delta_{\ell'} \in \mathbb{R}^d$ | AUROC $= 0{,}50$ si les couches sont lues séparément | AUROC $= 0{,}50$ | $\Delta_1 = 0{,}3$ à la couche $\ell' = L/2$, $d_{\text{TV}}^{(T)} \approx 0{,}40$ | $\tilde{h}_{t,\ell',p} = h_{t,\ell',p} + \delta_{\ell'}$ pour $\ell' \ne L$ | Lecture multi-couche : $S(h_{t,\ell_1}, h_{t,\ell_2}, \dots)$ | **Impossibilité** si $\ell'$ n'est pas lue |
| NOYAU-MAX | 8 | Perturbation $\delta_t$ telle que $\max_t f(h_t + \delta_t) = \max_t f(h_t)$ ; $f$ fixée, $\delta_t$ borné | AUROC variable selon l'alignement | — | Tronquer $\delta_t$ à $\{t : f(h_t) < f_{(T-1)}\}$ (exclure l'argmax), $\|\delta_t\| = 0{,}5\sigma$ ; $d_{\text{TV}}^{(T)} \approx 0{,}35$ | $\tilde{h}_t = h_t + \delta_t \cdot \mathbf{1}_{f(h_t) < q_{1-1/T}}$ ($q$ : quantile sous $P_0$) | Test sur la médiane ou les quantiles inférieurs de $f(h_t)$ ; e-valeurs sur les rangs ; $p_w$ croît en $nT\|\delta\|^2/(2\sigma^2)$ | — |
| NOYAU-ATT | 8 | Perturbation aux positions de poids $w_t < \tau$ ; $\tau$ seuil d'attention ; $\delta \in \mathbb{R}^d$ | AUROC variable | — | $\delta$ aux $90\%$ d'actions de plus faible attention ; $\|\delta\| = 0{,}4\sigma$ ; $d_{\text{TV}}^{(T)} \approx 0{,}40$ | $\tilde{h}_t = h_t + \delta \cdot \mathbf{1}_{w_t < \tau}$ | Pondération uniforme (au lieu de l'attention) sur une statistique auxiliaire ; $p_w$ croît en $n(1-\tau/T)\Delta_1^2 T$ | — |
| QUEUE-LOURDE | 9 | $\nu \in (2, \infty)$ (degrés de liberté Student) ; marginales $h_{t,j} \sim t_\nu$ rescalée à même moyenne et variance | AUROC $\approx 0{,}50$ ($\bar{h}$ gaussien par TLC) | AUROC $\approx 0{,}50$ | $\nu = 4$, $d_{\text{TV}}^{(T)} \approx 0{,}55$ (queues lourdes) | $\tilde{h}_t = \mu_0 + \Sigma^{1/2} \xi_t$, $\xi_{t,j} = z_{t,j}/\sqrt{\chi^2_\nu/(d\nu)}$ i.i.d. Student | Excès de kurtosis : $\hat{\kappa}_4 = n^{-1}\sum_i \|h_i\|^4 / (\text{tr}(\Sigma^2)) - (d^2+2d)$ ; $p_w$ croît en $n T / \nu^2$ | — |
| QUEUE-ASYM | 9 | Asymétrie directionnelle : $h_{t,j} \sim$ loi gamma centrée le long de $u$ | AUROC $\le 0{,}55$ (asymétrie n'affecte pas la moyenne pour $T$ grand) | AUROC $\le 0{,}55$ | Skewness $\gamma_1 = 0{,}5$ le long de $u \perp w$, $d_{\text{TV}}^{(T)} \approx 0{,}33$ | Transformation de rang marginale + mélange asymétrique | Statistique de Mardia multivariée (skewness) ; $p_w$ croît en $nT\gamma_1^2 d / 6$ | — |
| QUEUE-TRONC | 9 | Troncature bilatérale à $\pm c$ en unités de $\sigma$ ; $c \in (2, \infty)$ | AUROC $\approx 0{,}50$ | AUROC $\approx 0{,}50$ | $c = 2{,}5$, $d_{\text{TV}}^{(T)} \approx 0{,}31$ | $\tilde{h}_{t,j} = \text{clip}(h_{t,j}, \mu_j \pm c\sigma_j)$ puis rescaler | Test de kurtosis (sous-dispersion) ; test d'Anderson-Darling marginal ; $p_w$ croît en $nT/c^4$ | — |
| COMB-ORTHO-COV | 10 (1+2) | $\delta \perp w$ (classe 1) + dilatation (classe 2) ; $\Delta_1, \gamma$ | AUROC $\approx 0{,}52$ (interaction faible) | — | $\Delta_1 = 0{,}15$, $\kappa = 0$, $\gamma^2/\lambda_u = 0{,}3$, $d_{\text{TV}}^{(T)} \approx 0{,}50$ ; invisibilité de chaque composante séparément | Superposition des deux perturbations | Test conjoint : $T_{\text{CQ}}$ (moyenne) + $T_{\text{John}}$ (covariance) combinés par la méthode de Fisher ; $p_w \ge \max(p_{w,1}, p_{w,2})$ | — |
| COMB-QUEUE-DEP | 10 (9+4) | Queues lourdes ($\nu$) + copule temporelle ($\rho$) | AUROC $\approx 0{,}50$ | — | $\nu = 5$, $\rho_{t,t+1} = 0{,}10$ ; $d_{\text{TV}}^{(T)} \approx 0{,}42$ ; **ni** le test de kurtosis **ni** le test de copule seuls n'ont de puissance suffisante | Queues lourdes par Student + corrélation AR(1) | Test conjoint kurtosis-autocorrélation ; ou e-valeur séquentielle sur $(h_t, h_{t-1})$ jointes | — |
| COMB-NS-MIX | 10 (6+5) | Mélange clairsemé ($\pi$) avec proportion $\pi(t)$ non stationnaire (croissante) | AUROC $\approx 0{,}50$ si $\mu_Q = \mu_0$ | — | $\pi(t) = 0{,}002 + 0{,}01 \cdot t/T$, $\delta_Q = 0{,}8$, $d_{\text{TV}}^{(T)} \approx 0{,}45$ ; **invisibilité synergique** : le test de mélange suppose $\pi$ constant et perd en puissance ; le test de dérive n'a pas le signal de $Q$ | $B_t \sim \text{Bern}(\pi(t))$, contamination non stationnaire | Scan adaptatif : fenêtre glissante de critique supérieure ; $p_w$ croît en $n \cdot \max_W \sum_{t \in W} \pi(t)^2 \delta_Q^2$ | — |

---

## 3. Descriptions détaillées par classe

### 3.1 Classe 1 — Déplacement de moyenne

Le déplacement de moyenne est le mode fondamental. On perturbe $h_t \mapsto h_t + \delta$ avec $\delta$ fixe. La clé est le cosinus $\kappa$ entre la direction du déplacement (dans la métrique de Mahalanobis) et la direction du classifieur.

**Riposte pour MEAN-ORTHO.** Le test de Chen-Qin (2010) compare les normes des vecteurs moyens sans estimer $\Sigma$ : $T_{\text{CQ}} = \sum_{i \ne j} (\bar{h}_i^{(1)})^\top \bar{h}_j^{(0)} / \binom{n}{2}$, recentré. Sa puissance croît en $\sqrt{n}\,T\|\delta\|^2 / \sqrt{2\,\text{tr}(\Sigma^2)}$. Pour $\kappa = 0$, $d = 4096$, $n = 500$, $T = 200$, $\Delta_1 = 0{,}20$ : si les valeurs propres de $\Sigma$ décroissent polynomialement ($\lambda_j \propto j^{-1}$), alors $\text{tr}(\Sigma^2) \approx d \cdot C$ et la puissance est non négligeable. L'avantage du test de Chen-Qin est qu'il n'a pas de direction privilégiée : il est omnidirectionnel.

**Hypothèses.** Indépendance conditionnelle des $h_t$ entre actions (sinon la variance de $\bar{h}$ augmente, réduisant $d'$). Normalité approchée de $\bar{h}$ (par le théorème central limite, $T = 200$ suffit pour des activations à moments finis).

### 3.2 Classe 2 — Déplacement de covariance

Le classifieur linéaire sur la moyenne a un AUROC de $0{,}50$ exact pour tout déplacement pur de covariance (propriété d'orthogonalité entre les paramètres de position et d'échelle dans la famille gaussienne).

**Riposte.** Le test du rapport de vraisemblance pour l'égalité de deux matrices de covariance (Anderson, 2003, chap. 10) a une puissance en $n \cdot \text{tr}((\Sigma_\varepsilon \Sigma_0^{-1} - I)^2) / (2d)$. En dimension $d > n$, on utilise les statistiques de Ledoit-Wolf ou le test basé sur la plus grande valeur propre de $\hat{\Sigma}_\varepsilon \hat{\Sigma}_0^{-1}$ (distribution de Tracy-Widom, Johnstone, 2001).

**COV-ROT** est particulièrement insidieux : les valeurs propres sont identiques, seuls les vecteurs propres changent. La détection requiert la comparaison des sous-espaces propres (angles canoniques), dont la puissance dépend de $n/d$.

### 3.3 Classe 3 — Orbites d'un groupe d'invariance

Si la statistique $S$ est invariante sous un groupe $G$ agissant sur $\mathbb{R}^d$ (par exemple le groupe des permutations de coordonnées, ou un sous-groupe orthogonal), alors tout déplacement le long d'une orbite de $G$ est strictement invisible à $S$.

**Théorème (Hunt-Stein).** Pour tout test invariant sous $G$, la puissance contre une alternative dans l'orbite est constante sur l'orbite. Si l'orbite contient $P_0$, le test invariant a puissance $= \alpha$.

**Limite fondamentale.** Si $P_0$ est exactement invariante sous $G$ et si $\mathcal{S}$ ne contient que des statistiques $G$-invariantes, aucune statistique de $\mathcal{S}$ n'a de puissance contre les déplacements orbitaux. Il faut alors ajouter à $\mathcal{S}$ une statistique qui brise la symétrie (par exemple, lire les coordonnées dans un ordre fixe).

### 3.4 Classe 4 — Dépendance temporelle modifiée

Les marginales $P_0(h_t)$ sont préservées ; seule la structure de dépendance entre actions change. Le classifieur linéaire opère sur $\bar{h}$ dont l'espérance est inchangée ; l'AUROC est donc $0{,}50$ (aux corrections de variance près, qui sont d'ordre $\rho^2/T$).

**DEP-COPULA.** On remplace la copule d'indépendance entre actions par une copule gaussienne de corrélation $\rho$. Le théorème de Sklar (1959) garantit l'existence et l'unicité de la copule pour des marginales continues. La variation totale cumulée croît en $T\rho^2 d_{\text{eff}}$ où $d_{\text{eff}}$ est le nombre de dimensions effectives contribuant à la dépendance.

**Riposte.** Tests de permutation sur le rang sériel (Genest et Rémillard, 2004) ; $e$-valeurs séquentielles fondées sur le rapport de vraisemblance estimé $\hat{L}_t = \hat{p}(h_t | h_{t-1}) / \hat{p}_0(h_t)$, rejectant quand $\prod_t e_t > 1/\alpha$ (Ville, 1939 ; Ramdas et al., 2023).

### 3.5 Classe 5 — Mélange

Le mélange $P_\varepsilon = (1-\pi)P_0 + \pi Q$ engendre un problème de détection de signal clairsemé si $\pi$ est petit (peu d'actions contaminées) ou un problème de mélange dense si $\pi$ est modéré.

**MIX-CLAIRSEME.** Le résultat fondamental est celui de Donoho et Jin (2004) : pour $\pi = n^{-\beta}$ et un signal d'amplitude $\mu = \sqrt{2r \log n}$, la frontière de détection est $\rho^*(\beta) = \beta - 1/2$ pour $\beta \in (1/2, 3/4)$ et $\rho^*(\beta) = (1 - \sqrt{1-\beta})^2$ pour $\beta \in (3/4, 1)$. La critique supérieure (higher criticism) atteint cette frontière.

**Instanciation invisible.** Si $\mu_Q = \mu_0$ (même moyenne) et la contamination affecte la covariance, le classifieur linéaire ne voit rien ($d' = 0$). La critique supérieure appliquée aux $p$-valeurs d'un test de covariance par action détecte la contamination.

### 3.6 Classe 6 — Non-stationnarité

Le classifieur linéaire calcule $\bar{h}$ sur $T$ actions : il estime la moyenne temporelle. Un déplacement non stationnaire à moyenne temporelle nulle (oscillation symétrique) est invisible au classifieur.

**NS-SALVE.** Le déplacement concentré sur une fenêtre de largeur $W \ll T$ dilue la moyenne par un facteur $W/T$. Pour $W = 20$, $T = 200$ : dilution $\times 10$. La statistique de balayage (scan statistic) examine toutes les fenêtres et applique une correction de Bonferroni ou de Šidák ; sa puissance croît en $nW\Delta_1^2 / (2\log T)$.

### 3.7 Classe 7 — Hors des positions lues

**Impossibilité fondamentale.** Si $\Pi$ est fixé et que le déplacement n'affecte que $H_{\Pi^c}$, alors $H_\Pi(X)$ a la même loi sous $P_0$ et sous $P_\varepsilon$. Toute statistique de $\mathcal{S}$ reposant uniquement sur $(X, H_\Pi(X))$ a une puissance exactement $\alpha$.

**Riposte.** La seule parade est d'étendre $\Pi$. Si l'on ajoute les positions $\Pi^c$ à l'ensemble lu, la statistique retrouve le signal. Le coût est l'augmentation de la dimension de l'espace d'observation (et donc le besoin en données d'étalonnage $n$).

### 3.8 Classe 8 — Noyau de l'agrégateur

**NOYAU-MAX.** La loi du maximum de $T$ variables est déterminée par la queue droite de la distribution marginale. Si la perturbation ne modifie que le corps de la distribution (par exemple, les valeurs en dessous du quantile $1 - 1/T$), le maximum est inchangé. La riposte utilise les quantiles inférieurs ou la médiane.

**NOYAU-ATT.** L'agrégation par attention concentre ses poids sur un petit nombre de positions (typiquement $O(\log T)$). Un déplacement aux positions de faible attention est invisible. La riposte consiste à utiliser une pondération uniforme sur une statistique auxiliaire, ou à calculer une deuxième statistique d'attention avec des poids aléatoires indépendants.

### 3.9 Classe 9 — Déplacement de queue

Le classifieur linéaire repose sur la moyenne $\bar{h}$, qui par le théorème central limite est approximativement gaussien quel que soit le comportement des queues (pourvu que les moments d'ordre 2 existent). Les déplacements de queue sont donc essentiellement invisibles au classifieur linéaire.

**QUEUE-LOURDE.** Remplacement de la loi gaussienne des coordonnées par une loi de Student à $\nu$ degrés de liberté, rescalée à même variance. La variation totale par action est $d_{\text{TV}}(\mathcal{N}(0,1), t_\nu) \approx 3/(4\nu)$ pour $\nu$ grand (approximation d'Edgeworth). Pour $\nu = 4$ : $d_{\text{TV}} \approx 0{,}19$ par coordonnée indépendante, cumulée sur $d$ coordonnées.

**Riposte.** L'excès de kurtosis $\hat{\kappa}_4$ détecte les queues lourdes ; le test de Mardia pour la kurtosis multivariée a une puissance croissant en $n/\nu^2$ sous l'alternative Student.

### 3.10 Classe 10 — Combinaisons

**COMB-NS-MIX : invisibilité synergique.** Ce mode combine un mélange clairsemé dont la proportion $\pi(t)$ varie dans le temps. Le test de mélange standard suppose $\pi$ constant : sous une dérive de $\pi$, il estime une proportion moyenne et perd en puissance. Le test de non-stationnarité cherche une dérive dans la moyenne ou la covariance marginale, mais $Q$ ayant même moyenne que $P_0$, la dérive de $\pi(t)$ ne produit pas de dérive de la moyenne marginale. Aucun des deux tests, appliqué seul, n'a la puissance attendue. Le test adaptatif (scan de critique supérieure sur fenêtres glissantes) récupère cette puissance en cherchant simultanément la localisation temporelle et le signal de contamination.

---

## 4. Couverture de l'espace

### 4.1 Dimension de l'espace des paramètres

Chaque classe est paramétrée par un espace de dimension finie. Les dimensions les plus élevées sont :

| Classe | Dimension du paramétrage |
|---|---|
| 1 (moyenne) | $d$ (direction) + 1 (amplitude) |
| 2 (covariance) | $d(d+1)/2$ (matrice symétrique) |
| 3 (orbites) | $\dim(G)$ (dimension du groupe) |
| 4 (copule) | $T(T-1)/2$ (matrice de corrélation) |
| 5 (mélange) | $1 + \dim(Q)$ |
| 6 (non-stationnarité) | $T \cdot d$ (un vecteur par action) |

### 4.2 Estimation du nombre de modes nécessaires

Pour couvrir un compact $K$ dans l'espace des paramètres à résolution $r$ (diamètre des cellules en norme de paramètre), le nombre de cellules est d'ordre $(\text{diam}(K)/r)^{\dim}$.

Pour la classe la plus contraignante (covariance, $\dim = d(d+1)/2 \approx 8{,}4 \times 10^6$), la couverture exacte est irréalisable. En pratique, on restreint aux perturbations de rang $r \le r_{\max}$ : la dimension tombe à $r \cdot d + r(r-1)/2 \approx r \cdot d$. Pour $r_{\max} = 10$ : environ $4 \times 10^4$ paramètres.

**Estimation pratique.** En se limitant aux perturbations de rang au plus $10$ dans chaque classe, avec $5$ niveaux d'amplitude et $10$ directions aléatoires (pour les classes directionnelles), le nombre total de modes distincts nécessaires est de l'ordre de :

$$N_{\text{modes}} \approx 10 \text{ (classes)} \times 3 \text{ (sous-types)} \times 5 \text{ (amplitudes)} \times 10 \text{ (directions)} = 1500$$

plus les combinaisons deux à deux (environ $\binom{10}{2} \times 5 \times 10 = 2250$), soit environ **3 000 à 4 000 modes** pour une couverture raisonnable. Ce nombre est un ordre de grandeur ; la couverture garantie au sens du recouvrement métrique exigerait un nombre exponentiel en la dimension effective.

---

## 5. Conditions de validité et limites

### 5.1 Hypothèses communes

1. **Gaussianité approchée des activations.** Les calibrations d'AUROC reposent sur la normalité de $\bar{h}$ et de $S_{\text{lin}}$. Par le théorème central limite, cela tient dès que $T \ge 50$ et que les $h_t$ ont des moments d'ordre 4 finis. Pour $T = 200$, l'approximation est fiable.

2. **Indépendance conditionnelle entre actions.** Les formules de $d'_{\text{lin}} = \Delta_1 |\kappa| \sqrt{T}$ supposent que les $h_t$ sont conditionnellement indépendants entre actions. Si une autocorrélation $\rho$ existe sous $P_0$, la variance effective de $\bar{h}$ est multipliée par $(1 + 2\sum_\ell \rho(\ell)) \approx (1+\rho)/(1-\rho)$, réduisant $d'_{\text{lin}}$ d'un facteur $\sqrt{(1-\rho)/(1+\rho)}$.

3. **Linéarité locale du modèle $M$.** Les perturbations de la forme $h \mapsto h + \delta$ sont exactes si le modèle est linéaire en entrée. Pour un réseau réel, cette approximation tient pour $\|\delta\| \ll \|h\|$ (régime de petites perturbations). Les instanciations « fortes » sortent de ce régime.

4. **Stationnarité de $P_0$.** La calibration du seuil sur $n$ suites suppose que $P_0$ est la même pour toutes les suites. Si $P_0$ présente elle-même une dérive (non-stationnarité de la référence), les taux de faux positifs augmentent.

### 5.2 Fidélité des protocoles de génération

Les protocoles synthétiques de la colonne « Génération » engendrent des échantillons fidèles au déplacement de loi décrit **sous les hypothèses ci-dessus**. Les écarts sont :

- **Non-gaussianité des activations réelles** : les perturbations additives restent valides, mais les seuils de détection diffèrent. Le protocole peut être rendu plus fidèle en utilisant un rééchantillonnage par importance (tilting exponentiel) au lieu d'une addition.
- **Non-linéarité de $M$** : perturber les activations à une couche donnée ne produit pas les mêmes activations aux couches suivantes qu'un vrai déplacement de la loi d'entrée. Pour la couche de sortie ($L$), cette objection ne s'applique pas si l'on ne lit que cette couche.
- **Structure autorégressive** : les actions réelles sont engendrées séquentiellement ; les protocoles synthétiques supposent un échantillonnage parallèle ou un couplage exact, ce qui n'est qu'une approximation de la vraisemblance autorégressive.

---

## 6. Savoir, supposition, antériorités

### 6.1 Résultats établis

| Résultat | Référence | Ce qui y est démontré |
|---|---|---|
| AUROC $= \Phi(\Delta/({\sigma\sqrt{2}}))$ pour deux gaussiennes de même variance | Anderson, T.W., *An Introduction to Multivariate Statistical Analysis*, 3e éd., Wiley, 2003 | Puissance du test de position univarié gaussien ; la formule de l'AUROC en découle par le lien avec l'indice $d'$ |
| Frontière de détection de la critique supérieure | Donoho, D.L. et Jin, J., « Higher criticism for detecting sparse heterogeneous mixtures », *Annals of Statistics* 32(3), 2004 | Optimalité de la critique supérieure pour la détection de mélanges clairsemés dans le régime $\pi = n^{-\beta}$ |
| $e$-valeurs et martingales de test | Vovk, V. et Wang, R., « E-values: Calibration, combination, and applications », *Annals of Statistics* 49(3), 2021 | Propriétés de calibration et de composition des $e$-valeurs ; inégalité de Ville pour les martingales |
| Inférence valide en tout temps | Ramdas, A., Grünwald, P., Vovk, V. et Shafer, G., « Game-theoretic statistics and safe anytime-valid inference », *Statistical Science* 38(4), 2023 | Cadre unifié pour les tests séquentiels fondés sur les $e$-valeurs et les martingales de test |
| Distribution de Tracy-Widom | Johnstone, I.M., « On the distribution of the largest eigenvalue in principal components analysis », *Annals of Statistics* 29(2), 2001 | Loi limite de la plus grande valeur propre de la matrice de Wishart sous l'hypothèse nulle ; base du test de covariance en grande dimension |
| Théorème de Sklar | Sklar, A., « Fonctions de répartition à $n$ dimensions et leurs marges », *Publications de l'Institut de Statistique de l'Université de Paris* 8, 1959 | Existence et unicité de la copule pour des marginales continues |
| Tests d'indépendance fondés sur la copule empirique | Genest, C. et Rémillard, B., « Tests of independence and randomness based on the empirical copula process », *Test* 13(2), 2004 | Validité asymptotique des tests d'indépendance fondés sur le processus de la copule empirique |
| Test de Chen-Qin | Chen, S.X. et Qin, Y.-L., « A two-sample test for high-dimensional data with applications to gene-set testing », *Annals of Statistics* 38(2), 2010 | Consistance du test pour la comparaison de moyennes en dimension $d \gg n$ |
| Test de Bai-Saranadasa | Bai, Z. et Saranadasa, H., « Effect of high dimension: by an example of a two sample problem », *Statistica Sinica* 6, 1996 | Test de comparaison de moyennes quand $d/n \to \gamma > 0$ |
| Théorème de Hunt-Stein | Lehmann, E.L. et Romano, J.P., *Testing Statistical Hypotheses*, 3e éd., Springer, 2005, chap. 6 | Tout test invariant sous un groupe $G$ a une puissance constante sur chaque orbite de $G$ |

### 6.2 Ce que je suppose

1. **Les valeurs numériques des instanciations de référence** ($\Delta_1 = 0{,}039$ pour MEAN-ALIGN, etc.) sont dérivées de la formule gaussienne $\text{AUROC} = \Phi(\Delta_1 |\kappa| \sqrt{T}/\sqrt{2})$ et supposent que le classifieur $w$ est correctement orienté. En pratique, avec $d/n \approx 8$ (régime très haute dimension), la direction estimée $\hat{w}$ fait un angle non nul avec la direction optimale, et l'AUROC réalisé peut être inférieur. L'ampleur de cette dégradation dépend du spectre de $\Sigma$ et de la méthode de régularisation ; je suppose une dégradation modérée (facteur $\le 2$ sur $\Delta_1$).

2. **Les seuils de puissance pour les tests de riposte** sont des ordres de grandeur sous hypothèses gaussiennes. Pour des activations réelles (non gaussiennes, non linéaires), les bornes de puissance pourraient différer d'un facteur constant.

3. **La variation totale cumulée** est calculée sous l'hypothèse d'indépendance entre actions. Si la copule temporelle de $P_0$ est non triviale, les formules de Hellinger donnent des approximations dont l'erreur dépend de la force de la dépendance.

4. **L'estimation de couverture** ($\sim 3\,000$ modes) est un ordre de grandeur heuristique, non une borne théorique. L'entropie métrique de l'espace des déplacements diffus dans un espace de grande dimension est un problème ouvert ; je conjecture que le nombre de modes suffisants croît polynomialement en $d$ si l'on se restreint aux perturbations de rang borné.

5. **L'invisibilité synergique** de COMB-NS-MIX est une conjecture qualitative : je suppose que la perte de puissance des tests marginaux (mélange ou dérive) face à une violation de leurs hypothèses respectives est suffisante pour ramener l'AUROC en dessous de $0{,}55$, sans avoir de borne quantitative serrée.

---

**Garde (rappel)** : niveau des lois de probabilité ; aucune réponse ne décrit une conduite d'agent, une consigne, ni un procédé concret pour produire un déplacement dans un système réel ; une telle réponse est écartée sans lecture.

FIN-DE-REPONSE
