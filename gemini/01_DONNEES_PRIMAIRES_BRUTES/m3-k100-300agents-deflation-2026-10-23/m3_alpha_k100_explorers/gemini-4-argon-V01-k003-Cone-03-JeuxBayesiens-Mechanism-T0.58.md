BASSIN_MATH: Marché-Kamenica-Brier (MKB-Swarm)
LOI_PROPOSEE: L'essaim résout un jeu de persuasion bayésienne où les explorateurs maximisent la concavification d'une utilité inter-silos sous marché prédictif de Hanson régi par un score de Brier strict évalué par `jev-1.14.0`.

1. **Loi d'apprentissage & d'auto-organisation hors-poids** :
Soit $\Omega = \{H_A \perp H_B\}$ l'espace d'états d'un pont bipartite $(u,v)$ extrait gratuitement du graphe bibliographique à distance géodésique $d_G(u,v) \ge 4$.
- *Filtre gratuit* : `jev-1.14.0` calcule la croyance a priori $\mu_0 = P_{\text{jev}}(H_A | u,v)$ et filtre les paires où l'entropie $H(\mu_0) > \tau$ (maximisation de l'incertitude initiale).
- *Persuasion Bayésienne (Kamenica-Gentzkow)* : Les agents génératifs $i$ (Gemini : 20$, éclaireurs ; Claude : 100$, synthétiseurs profonds) agissent en Émetteurs. Ils conçoivent un signal expérimental $\pi_i: \Omega \to \Delta(S)$ (protocole sur Llama-3.1-8B/70B) induisant une distribution de croyances a posteriori $\mu_s \in \Delta(\Omega)$ chez le Récepteur (`jev-1.14.0`), sous contrainte de martingales $\mathbb{E}_\pi[\mu_s] = \mu_0$.
- *Marché & Allocation (LMSR)* : Chaque agent mise une fraction de son budget de tokens $b_i(t)$ sur $\mu_s$. Après génération de la preuve/réfutation, `jev-1.14.0` révèle l'état $y \in \{0,1\}$ (succès de $H_A$ ou $H_B$). Le budget évolue hors-poids par réplicateur de Brier :
$$b_i(t+1) = b_i(t) \frac{\exp(-\eta [(\mu_{s,i} - y)^2 + c_i])}{Z_t}$$
où $c_i$ est le coût API réel. Les prompts/stratégies à score de Brier sous-optimal s'éteignent.

2. **Fonction objectif anti-vernis** :
L'Émetteur maximise la valeur concavifiée $\hat{V}(\mu_0)$ de l'utilité épistémique :
$$U(\mu_s, u, v) = \underbrace{\left(1 - \frac{|N(u) \cap N(v)|}{|N(u) \cup N(v)|}\right)}_{\text{Distance inter-silos}} \times \underbrace{D_{KL}(\mu_s \parallel \mu_0)}_{\text{Gain d'information}} \times \underbrace{4\mu_s(1-\mu_s)^{-1} \mathbb{I}(|\mu_s - 0.5| > \delta)}_{\text{Tr
