BASSIN_MATH: Compression-Kolmogorov-Saut-Bipartite
LOI_PROPOSEE: L'essaim maximise le gain de compression algorithmique conditionnelle croisée $\Delta K(x,y) = K(x) + K(y) - K(x,y)$ entre sous-graphes bibliographiques disjoints sous contrainte de budget Solomonoff-Levin.

1. **Loi d'apprentissage & d'auto-organisation hors-poids de l'essaim**
L'essaim maintient un dictionnaire de préfixes $D_t$ hors-poids (prompts, schémas formels). `jev-1.14.0` (coût $0$) approxime la distance d'information normalisée $NID(x,y) = \frac{\max\{K(x|y), K(y|x)\}}{\max\{K(x), K(y)\}}$ via la compression croisée des embeddings et du graphe de citations sur des millions de paires $(x,y)$ issues de silos disjoints (plus court chemin $d_G(x,y) > 4$). L'allocation des 120 USD suit la recherche universelle de Levin : un appel génératif $p_i$ (Gemini à faible coût $c_i$ pour l'extraction de schémas de préfixes, Claude à coût élevé pour la synthèse) est déclenché si et seulement si $\frac{\hat{\Delta} K(x,y | D_t)}{c_i \cdot 2^{|p_i|}} > \tau_t$. Si le pont généré réduit la longueur de description minimale (MDL) d'un cluster de contrôle-IA, il est intégré à $D_{t+1}$, modifiant la topologie de routage de l'essaim sans toucher aux poids.

2. **Fonction objectif anti-vernis**
Pour tout pont candidat $z$ reliant $x$ et $y$ via deux hypothèses causales orthogonales $H_A \perp H_B$ testables sur Llama-3.1-8B/70B :
$$\mathcal{J}(z) = d_G(x,y) \cdot \left[ K(y | d_{<t}) - K(y | x, z, d_{<t}) - |z|_{MDL} \right] \cdot \min_{m \in \{A, B\}} I_{alg}(H_m ; \text{do}(\text{Act}_{Llama}) | H_{\neg m})$$
Le terme $-|z|_{MDL}$ pénalise impitoyablement le vernis verbal (bruit incompressible). L'information algorithmique mutuelle $I_{alg}$ sous intervention causale ($\text{do}$) exige que $H_A$ et $H_B$ prédisent des trajectoires d'activations compressibles distinctes.

3. **Exemple concret de pont in?dit et duel ($H_A \perp H_B$)**
Pont entre la dynamique des systèmes de contrôle à événements discrets par automates de supervision de Ramadge-Wonham (référence à vérifier) et la géométrie des représentations linéaires d'états de vérité dans les LLM de Marks & Tegmark 2023 (référence à vérifier).
* **Duel sur Llama-3.1-8B/70B :** Pour bloquer un comportement trompeur en boîte blanche :
