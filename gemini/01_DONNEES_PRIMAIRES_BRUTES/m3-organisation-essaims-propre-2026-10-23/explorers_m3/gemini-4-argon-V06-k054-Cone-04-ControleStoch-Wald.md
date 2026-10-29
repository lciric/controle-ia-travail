BASSIN_MATH: ControleErgodique-RobbinsSiegmund-Shewhart-DaumHuang
LOI_PROPOSEE: L'essaim évolue par flot de particules de Daum-Huang sans dégénérescence guidé par une inégalité de supermartingale de Robbins-Siegmund, où l'allocation budgétaire résout une équation de Hamilton-Jacobi-Bellman (HJB) ergodique déclenchée par des cartes de contrôle multivariées de Shewhart-Hotelling $T^2$ et un test séquentiel à frontière parabolique de Kiefer-Weiss.

1. **Loi d'apprentissage & d'auto-organisation hors-poids** :
L'essaim de $N$ éclaireurs non-génératifs parcourt le graphe gratuit (arXiv/GitHub/Alignment Forum) en évaluant des paires $(u,v)$ via `jev-1.14.0` illimité, générant un vecteur de scores $y_t \in \mathbb{R}^d$. La distribution empirique des pistes est transportée continûment sans rééchantillonnage par un **flot de particules exact de Daum-Huang** :
$$\frac{dx_t^{(i)}}{d\lambda} = A(\lambda)x_t^{(i)} + b(\lambda), \quad A(\lambda) = -\frac{1}{2}P_t H^T (\lambda H P_t H^T + R)^{-1} H$$
où $P_t$ est la covariance de l'essaim et $H$ l'opérateur d'observation `jev-1.14.0`. Une **carte de contrôle multivariée de Shewhart-Hotelling** $T^2_t = (y_t - \mu_t)^T \Sigma_t^{-1} (y_t - \mu_t)$ surveille les anomalies topologiques inter-silos. L'adaptation hors-poids des hyperparamètres de fouille $\theta_t$ obéit au **lemme d'arrêt de supermartingale de Robbins-Siegmund** :
$$\mathbb{E}[\mathcal{V}(\theta_{t+1}) \mid \mathcal{F}_t] \le (1 + \alpha_t)\mathcal{V}(\theta_t) - \beta_t \mathcal{J}_{anti-vernis}(u_t,v_t) + \gamma_t$$
garantissant la convergence p.s. vers les crêtes de haute densité causale. L'invocation des LLM payants (20$ Gemini pour la synthèse d'hypothèses, 100$ Claude pour la réfutation formelle) est gouvernée par un **contrôle stochastique ergodique HJB** minimisant le temps d'arrêt maximal au point d'indifférence (**problème de Kiefer-Weiss**), qui n'alloue les tokens que lorsque $T^2_t > \chi^2_{d, 1-\alpha}$ et que la frontière parabolique du log-rapport de vraisemblance est franchie.

2. **Fonction objectif anti-vernis** :
$$\mathcal{J}(u,v) = d_{\text{Riemann}}\left(\mathcal{N}_u, \mathcal{N}_v\right) \times \inf_{\mathbb{Q} \in \mathcal{P}_{
