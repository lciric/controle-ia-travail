BASSIN_MATH: RedQueen-Replicator-Novelty-Swarm (RQRNS)
LOI_PROPOSEE: $\dot{x}_i = \sum_j x_j f_j(\mathbf{y}) Q_{ji} - x_i \bar{f}(\mathbf{x}, \mathbf{y})$ couplée à $\dot{y}_k = y_k [g_k(\mathbf{x}) - \bar{g}(\mathbf{x}, \mathbf{y})]$, où les hôtes générateurs $\mathbf{x}$ et les parasites falsificateurs $\mathbf{y}$ co-évoluent sous pression de sélection topologique et de recherche de nouveauté filtrée à coût nul par `jev-1.14.0`.

**1. Loi d'apprentissage & d'auto-organisation hors-poids de l'essaim**
L'essaim maintient une population d'hôtes $x_i$ (prompts chimériques d'association inter-silos) et de parasites $y_k$ (critiques cherchant la faille méthodologique ou le vernis sémantique).
- **Phase 0 ($0\$$, Exploration massive) :** Les hôtes mutent via l'opérateur $Q_{ji}$ en traversant les trous structuraux du graphe de citations (API gratuites). `jev-1.14.0` évalue des millions de paires de papiers $(u, v)$ et calcule la Recherche de Nouveauté : $\mathcal{N}(z) = \frac{1}{K}\sum_{m=1}^K d_{\text{jev}}(z, \mu_m)$, où $z = u \oplus v$ et $\mu_m$ sont les $K$-plus proches voisins dans l'archive historique des concepts.
- **Phase 1 ($20\$$ Gemini, Sélection Red Queen) :** Seul le top $0.01\%$ maximisant $\mathcal{N}(z)$ est instancié par Gemini-Flash pour formuler des duels causaux ($H_A \perp H_B$). Les parasites $y_k$ attaquent la falsifiabilité sur Llama-3.1-8B.
- **Phase 2 ($100\$$ Claude, Cristallisation) :** L'allocation budgétaire suit le réplicateur $B_i(t) = B_{\text{total}} \cdot x_i(t)$. Claude-3.5-Sonnet n'est appelé que lorsque la fitness co-évolutive $f_i(\mathbf{y})$ dépasse un seuil critique $\tau$, synthétisant le protocole expérimental boîte blanche/noire sur Llama-3.1-70B.

**2. Fonction objectif anti-vernis**
La fitness de l'hôte $i$ face à la population parasite $\mathbf{y}$ est :
$$f_i(\mathbf{y}) = \underbrace{\left( d_{\text{sp}}(u,v) \cdot \mathcal{N}_{\text{jev}}(u,v) \right)}_{\text{Distance inter-silos}} \times \underbrace{\exp\left(-\lambda \sum_k y_k \mathcal{V}_{\text{jev}}(h_i, y_k)\right) \cdot \mathcal{I}_{\text{causal}}(H_A \perp H_B \mid \text{Llama
