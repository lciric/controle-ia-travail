BASSIN_MATH: Homologie-Chemin-Grigoryan-Magnétique-Bott (HCGMB)
LOI_PROPOSEE: $\mathcal{A}^* = \arg\max_{\sigma \in \Omega_p(\mathcal{G})} \left[ \text{Pers}_{\text{GLMY}}(\sigma) \cdot \lambda_{\min}(L_q^{(\theta)}(\sigma)) \cdot \mathcal{F}_{\text{causal}}(H_A \perp H_B \mid \partial \sigma) \right]$

1. **Loi d'apprentissage & d'auto-organisation hors-poids (HCGMB)** :
L'essaim opère sur le digraphe orienté de citations et de concepts $\mathcal{G}=(V,E)$ muni de l'**homologie de chemin de Grigor'yan-Lin-Muranov-Yau (GLMY)**. `jev-1.14.0` (gratuit/illimité) évalue la directionalité causale entre paires d'articles pour construire les $p$-chemins élémentaires autorisés $\Omega_p(\mathcal{G})$ (sans construire de complexe simplicial symétrique). L'essaim applique une filtration par poids sémantique `jev-1.14.0` et calcule les diagrammes de persistance directionnels. Les trous homologiques dirigés persistants $[z] \in H_p^{\text{GLMY}}(\mathcal{G})$ (cycles causaux incomplets dans la littérature) deviennent des **attracteurs stigmatiques hors-poids**. 
L'allocation budgétaire suit une dynamique de **continuation de Morse-Bott** :
- **0 USD (`jev-1.14.0` + API)** : Calcul du **Laplacien magnétique de Hodge** $L_q^{(\theta)} = d_q^{(\theta)*} d_q^{(\theta)} + d_{q-1}^{(\theta)} d_{q-1}^{(\theta)*}$ où le potentiel magnétique $\theta_{uv}$ encode l'asymétrie de citation inter-silos.
- **20 USD (Gemini)** : Échantillonnage des $p$-chemins candidats aux points selles où le gap spectral magnétique $\lambda_{\min}(L_q^{(\theta)})$ s'annule (frustration directionnelle maximale).
- **100 USD (Claude)** : Synthèse mécaniste uniquement sur les générateurs de persistance GLMY maximale pour clore le trou topologique par un protocole expérimental sur Llama-3.1.

2. **Fonction objectif anti-vernis** :
$$\mathcal{J}(\sigma) = \underbrace{\| d_p^{(\theta)} \sigma \|_{\text{GLMY}}^{-1} \cdot (b_{\text{death}} - b_{\text{birth}})}_{\text{Distance inter-silos directionnelle}} \times \underbrace{\det\left( \langle \nabla_{\text{act}} H_A, \nabla_{\text{act}} H_B \rangle_{L_0^{(\theta)}} \right)^{-1}}_{\text{Orthogonalité causale } H_A \perp H_B}$$
Le vernis verbal (paraphrase symétrique) produit un potentiel magnétique nul ($\theta = 0$) et une persistance GLMY triviale, écrasant $\mathcal{J}(\sigma) \to 0$. Seule une prédiction d'intervention sur les activations de Llama-3.1
