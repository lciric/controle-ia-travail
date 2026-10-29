BASSIN_MATH: Fibre-Finsler-Randers-Wasserstein-Martingale-Ay-Kantorovich (FFRW-MAK)
LOI_PROPOSEE: L'essaim évolue par gradient naturel de Finsler-Randers sur un fibré de Wasserstein asymétrique dirigé par le DAG de citations, maximisant le défaut de fermeture de la martingale d'information d'Ay sous contrainte de transport de Kantorovich-Rubinstein évalué par `jev-1.14.0`.

1. **Loi d'apprentissage & d'auto-organisation hors-poids de l'essaim**
Soit $G=(V,E)$ le DAG de citations gratuit et $\mathcal{P}(V)$ la variété statistique des croyances d'agents paramétrée par les prompts $\theta_i \in \Theta$. Le classifieur gratuit `jev-1.14.0` évalue des paires de nœuds $(u,v) \in V^2$ et induit une métrique de Finsler-Randers sur l'espace tangent $T_\theta \Theta$ :
$$F(\theta, \dot{\theta}) = \sqrt{\dot{\theta}^T I_F(\theta) \dot{\theta}} + \beta_\theta^T \dot{\theta}$$
où $I_F(\theta)$ est la matrice d'information de Fisher-Rao empirique des logits de `jev-1.14.0` et $\beta_\theta$ la 1-forme de dérive temporelle du DAG ($\|\beta_\theta\|_{I_F^{-1}} < 1$). L'auto-organisation hors-poids met à jour les contextes $\theta_i$ sans toucher aux poids LLM via le flot de gradient naturel de Randers couplé au sous-différentiel de Kantorovich-Rubinstein asymétrique $\vec{W}_1$ sur $G$ :
$$\dot{\theta}_i = -g_F^{-1}(\theta_i, \dot{\theta}_i) \left( \nabla_{\theta_i} \mathcal{J}_{\text{anti}}(\theta_i) - \gamma \sum_{j} \nabla_{\theta_i} \vec{W}_1(\mu_{\theta_i}, \mu_{\theta_j}) \right)$$
Allocation budgétaire : 0 USD pour l'exploration massive de $G$ et l'estimation de $(I_F, \beta_\theta)$ par `jev-1.14.0`. Les 20 USD Gemini servent de solveur primal-dual pour extraire les potentiels de Kantorovich $f$ ($1$-Lipschitz sur $G$). Les 100 USD Claude sont déclenchés uniquement lorsque la courbure flag de Finsler $K(\theta_i, \dot{\theta}_i)$ dépasse un seuil critique $\tau_c$, synthétisant le pont mécaniste sur Llama-3.1-8B/70B.

2. **Fonction objectif anti-vernis**
Soit $\Delta M^{(2)}(\mu_A, \mu_B) = D_{KL}(\mu_{AB} \| \pi_{\mathcal{E}_2}(\mu_{AB}))$ le défaut de martingale d'information d'Ay mesurant l'interaction synergique pure (irréductible aux facteurs marginaux $A,B$). L'objectif s'écrit :
$$\
