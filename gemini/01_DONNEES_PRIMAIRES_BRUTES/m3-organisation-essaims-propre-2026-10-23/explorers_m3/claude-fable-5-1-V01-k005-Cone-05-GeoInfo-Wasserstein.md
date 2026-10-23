BASSIN_MATH: `WFR-Swarm` (flot de Wasserstein-Fisher-Rao sur graphe d'agents)

LOI_PROPOSEE: L'essaim est une mesure $\mu_t$ sur le graphe $G=(V,E)$ des nœuds (famille, rôle, sous-tâche). Elle évolue par le flot de gradient de l'énergie libre
$$F(\mu)=-\mathbb{E}_\mu[R]+\beta\,\mathrm{KL}(\mu\|\mu_0)-\gamma\log\det \mathcal{I}(\mu)$$
sous la métrique non équilibrée WFR : $\partial_t\mu=\nabla\!\cdot(\mu\nabla\phi)+\mu\,\phi$, $\phi=-\delta F/\delta\mu$. Les paramètres $\theta$ (prompts, routage, température) suivent le gradient naturel $\dot\theta=-\mathcal{I}(\theta)^{-1}\nabla_\theta F$.

**1. Mécanisme.** Le terme transport (Wasserstein) déplace le budget le long des arêtes avec coût $c(u,v)=d_{FR}(p_u,p_v)$, distance de Fisher-Rao entre distributions de sorties ; le terme réaction (Fisher-Rao) crée/détruit de la masse : spawn d'un explorateur quand l'information de Fisher loc
