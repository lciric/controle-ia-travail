BASSIN_MATH: Fisher-Haldanian-Trophic-Cascade-Swarm (FHTCS)
LOI_PROPOSEE: $\frac{dx_i}{dt} = x_i \left( \sum_j Q_{ji} f_j(y) - \bar{f} \right)$ couplée à une cascade trophique de Haldane-Fisher où des prédateurs-réfutateurs $y_k$ chassent les phénotypes d'hypothèses $x_i$ selon une sélection dépendante de la fréquence négative sur le graphe bibliographique.

1. **Loi d'apprentissage & d'auto-organisation hors-poids** :
L'essaim opère comme un réseau trophique à trois niveaux sans mise à jour des poids :
- **Proies (Générateurs de ponts $x_i$, Gemini - 20$)** : Prompts-génotypes explorant les trous structuraux du graphe de citations gratuit. Mutation dirigée par la matrice de transition $Q_{ji}$ qui recombine les opérateurs d'extraction syntaxique.
- **Filtre abiotique (`jev-1.14.0` illimité)** : Évalue à coût nul la viabilité topologique et la densité formelle de millions de paires d'articles. Il calcule l'indice de nouveauté $\mathcal{N}(x_i) = \frac{1}{k}\sum_{m=1}^k d_{JEV}(x_i, \mu_m)$ par rapport à l'archive des $k$-plus proches voisins sémantiques, éliminant 99.9% des ponts triviaux avant tout appel LLM.
- **Prédateurs (Falsificateurs $y_k$, Claude - 100$)** : Alloués dynamiquement selon l'équation de dynamique adaptative $\frac{dy_k}{dt} = \gamma y_k \left( \sum_i A_{ki} x_i - \bar{g} \right)$, où $A_{ki}$ est le taux de capture (réfutation logique d'un pont $x_i$). Plus un cluster d'hypothèses $x_i$ prolifère, plus il attire le budget Claude pour tenter de le détruire (sélection apostaltique de Haldane), forçant l'essaim vers des niches théoriques inexplorées.

2. **Fonction objectif anti-vernis** :
La fitness $f_i(y)$ d'un pont entre deux études $(u,v)$ maximise l'orthogonalité causale sous pression de prédation :
$$\mathcal{F}(u,v) = \underbrace{\left(1 - \frac{|N_{cit}(u) \cap N_{cit}(v)|}{|N_{cit}(u) \cup N_{cit}(v)|}\right)}_{\text{Distance inter-silos}} \times \underbrace{\mathcal{N}_{JEV}(u,v)}_{\text{Nouveauté}} \times \underbrace{\exp\left(-\lambda \text{Sim}_{JEV}(H_A, H_B)\right) \cdot \min_{y_k} \text{Survie}(H_A \perp H_B | y_k)}_{\text{Falsifiabilité causale anti-vernis}}$$
Tout pont dont le duel $(H_A \perp H_B)$ ne pré
