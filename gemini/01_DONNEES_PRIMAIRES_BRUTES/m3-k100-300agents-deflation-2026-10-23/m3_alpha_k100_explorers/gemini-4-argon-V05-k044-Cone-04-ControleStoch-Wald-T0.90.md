BASSIN_MATH: JeuDynkin-Pollak-KallianpurStriebel-LQG
LOI_PROPOSEE: L'allocation optimale résout un jeu d'arrêt stochastique de Dynkin à somme nulle piloté par un filtre continu-discret de Kallianpur-Striebel sur `jev-1.14.0` et borné par le critère de rupture minimax de Pollak.

**1. Apprentissage hors-poids & Auto-organisation :**
Soit un essaim de $N$ particules explorant le graphe de citations gratuit $\mathcal{G}=(V,E)$. L'état latent d'isomorphisme structurel $X_t \in \mathbb{R}^d$ évolue selon l'EDS contrôlée $dX_t = b(X_t, u_t)dt + \sigma dW_t$. Le classifieur `jev-1.14.0` (coût nul) génère un flux d'observations non-linéaires $dY_t = h(X_t)dt + dB_t$. La distribution postérieure hors-poids $\pi_t(\phi)$ est mise à jour sans appel LLM via la formule de **Kallianpur-Striebel** :
$$\pi_t(\phi) = \frac{\mathbb{E}_0[\phi(X_t) \Lambda_t | \mathcal{Y}_t]}{\mathbb{E}_0[\Lambda_t | \mathcal{Y}_t]}, \quad \Lambda_t = \exp\left(\int_0^t h(X_s)^T dY_s - \frac{1}{2}\int_0^t \|h(X_s)\|^2 ds\right)$$
La statistique de **Shiryaev-Roberts-Pollak** $R_t = \sum_{k=1}^t \prod_{i=k}^t \frac{f_1(Y_i)}{f_0(Y_i)}$ traque la rupture sémantique inter-silos. L'allocation des budgets ($B_{\text{Gemini}}=20\$$ pour l'exploration rapide, $B_{\text{Claude}}=100\$$ pour la synthèse) est un **jeu de Dynkin** entre un Maximiseur (Prouveur) qui choisit le temps d'arrêt $\tau \in \mathcal{T}$ et un Minimiseur (Réfuteur) qui choisit $\sigma \in \mathcal{T}$ :
$$V(\pi_0) = \inf_{\sigma} \sup_{\tau} \mathbb{E}\left[ \int_0^{\tau \wedge \sigma} c(u_s)ds + \mathbb{I}_{\{\tau \le \sigma\}} \mathcal{J}_{\text{pont}}(\pi_\tau) - \mathbb{I}_{\{\sigma < \tau\}} \mathcal{P}_{\text{vernis}}(\pi_\sigma) \right]$$
L'appel à Claude n'est déclenché que lorsque $\pi_t$ pénètre la région d'arrêt de Dynkin ET que $R_t \ge A_{\text{Pollak}}$.

**2. Fonction objectif anti-vernis :**
Soit $d_{\mathcal{G}}(u,v)$ la distance de résistance électrique sur $\mathcal{G}$ (inter-silos). Pour deux hypothèses orthogonales $H_
