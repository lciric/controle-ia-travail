BASSIN_MATH: Symbiogenèse-Eigen-Quasispecies-LotkaVolterra (SEQLV)
LOI_PROPOSEE: L'essaim évolue via une dynamique de quasi-espèces d'Eigen couplée à un réseau trophique de Lotka-Volterra généralisé, opérant sous le seuil critique d'erreur de mutation où les prompts-hôtes (générateurs) et les prompts-parasites (réfutateurs) fusionnent par symbiogenèse de Margulis.

1. **Loi d'apprentissage & d'auto-organisation hors-poids** :
Soit $x_i$ la fréquence du génotype de recherche $i$ (couple d'opérateurs de requête arXiv/GitHub + heuristique d'assemblage). L'évolution hors-poids suit l'équation de quasi-espèce prédatrice :
$$\dot{x}_i = \sum_{j=1}^N x_j f_j(\mathbf{y}) Q_{ji} - x_i \left( \bar{f} + \sum_{k=1}^M \alpha_{ik} y_k \right)$$
où $Q_{ji} \propto \exp(-\beta d_{\text{jev}}(j,i))$ est la matrice de mutation guidée gratuitement par l'embedding de `jev-1.14.0`, et $y_k$ la population de parasites (prompts d'invalidation). Le taux de mutation $\mu = 1 - Q_{ii}$ est maintenu exactement au seuil de catastrophe d'erreur d'Eigen $\mu_c = \frac{\ln \sigma}{L}$ (avec $\sigma$ la supériorité sélective mesurée par `jev-1.14.0` sur le graphe de citations). Allocation budgétaire : 0 USD pour l'exploration topologique (mutations syntaxiques et filtrage de survie par `jev-1.14.0` sur 10^5 paires d'abstracts) ; 20 USD Gemini pour la recombinaison sexuée (crossover des génotypes survivants) ; 100 USD Claude déclenchés uniquement lors d'une *endosymbiose* ($\alpha_{ik} < 0$, quand un parasite échoue à réfuter un hôte mais fusionne avec lui pour former une chimère mécaniste).

2. **Fonction objectif anti-vernis** :
La fitness $f_i$ combine la recherche de nouveauté comportementale (Novelty Search) dans l'espace de `jev-1.14.0` et la survie aux parasites :
$$f_i = \left( \frac{1}{|K|} \sum_{n \in K} \| \phi_{\text{jev}}(x_i) - \phi_{\text{jev}}(n) \|_2 \cdot d_{\text{bib}}(A,B) \right) \times \det\left(\Sigma_{H_A \perp H_B}^{\text{Llama}}\right)$$
où $d_{\text{bib}}(A,B)$ est la résistance de coupure minimale dans le graphe de citations entre les études $A$ et $B$, et $\det(\Sigma_{H_A \perp H_B}^{\text{Llama}})$ mesure le volume d'orthogonalité empirique des interventions causales (patching d'activations sur Llama-3.1-8B/
