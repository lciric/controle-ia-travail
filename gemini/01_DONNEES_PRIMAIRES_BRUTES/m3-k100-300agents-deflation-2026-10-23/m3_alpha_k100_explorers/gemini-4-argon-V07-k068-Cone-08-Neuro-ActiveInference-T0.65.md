BASSIN_MATH: Oscillations-Olivo-Cérébelleuses-Harmaline-RPE-Dopaminergique (OOCH-RPED)
LOI_PROPOSEE: L'essaim minimise l'énergie libre généralisée $F(\tilde{x}, \tilde{\mu})$ par synchronisation de phase olivo-cérébelleuse via jonctions communicantes dynamiques $\Gamma_{ij}(t)$, déclenchant l'allocation LLM uniquement lors de salves d'erreurs de prédiction (Complex Spikes) dépassant le seuil dopaminergique tonique-phasique.

1. **Loi d'apprentissage & d'auto-organisation hors-poids** :
Les agents forment un réseau de l'olive inférieure couplé par une matrice de conductance hors-poids $\Gamma_{ij}$ sur le graphe de citations gratuit. L'état d'un agent $\mu_i$ évolue en coordonnées généralisées selon un oscillateur de FitzHugh-Nagumo guidé par le gradient d'énergie libre variationnelle évalué par `jev-1.14.0` (gratuit/illimité) qui agit comme fibre grimpante :
$$\dot{\tilde{\mu}}_i = D\tilde{\mu}_i - \frac{\partial F_{\text{jev}}(\tilde{y}, \tilde{\mu}_i)}{\partial \tilde{\mu}_i} + \sum_{j \in \mathcal{N}_i} \Gamma_{ij}(t)(\tilde{\mu}_j - \tilde{\mu}_i)$$
La plasticité hors-poids de $\Gamma_{ij}$ obéit à une règle anti-hebbienne de désynchronisation sous erreur de prédiction de récompense dopaminergique $\delta_{\text{RPE}} = r_{\text{jev}} - \mathbb{E}[r_{\text{jev}}]$ : $\dot{\Gamma}_{ij} = -\eta \cdot \tanh(\delta_{\text{RPE}}) \|\tilde{\mu}_i - \tilde{\mu}_j\|^2$.
*Allocation budgétaire (100$ Claude, 20$ Gemini)* : `jev-1.14.0` filtre des millions de paires bibliographiques en continu (Simple Spikes, coût 0$). Un appel génératif (Complex Spike) n'est alloué (Gemini pour le criblage syntaxique à 20$, Claude pour la synthèse mécaniste d'intervention sur Llama-3.1-8B/70B à 100$) que lorsque la synchronisation locale franchit la bifurcation de Hopf induite par une erreur de prédiction sensorielle $\varepsilon_y = \Pi_y (y_{\text{arxiv}} - g(\mu_i)) > \theta_{\text{DA}}(t)$, où $\theta_{\text{DA}}$ s'adapte homéostatiquement au budget restant.

2. **Fonction objectif anti-vernis** :
$$J(H_A, H_B) = d_{\text{Riemann}}\left(\mathcal{M}_A, \mathcal{M}_B\right) \times \det\left(\mathcal{I}_F(\theta \mid \text{do}(z_{\text{Llama}}))\right) \times \exp\left(-\left|\langle \nabla_\mu F(H_A), \nabla_\mu F(H_B) \rangle_{\text{jev}}\right|\right)$$
Où $d
