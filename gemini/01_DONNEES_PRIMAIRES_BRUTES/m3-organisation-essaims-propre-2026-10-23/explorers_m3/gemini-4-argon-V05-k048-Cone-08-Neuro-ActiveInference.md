BASSIN_MATH: Filtrage-Hippocampique-CA3-Bethe-Allostasie-Norepinephrique (FHC3-BAN)
LOI_PROPOSEE: Minimisation de l'énergie libre de Bethe $F_B$ par transition de phase allostatique entre complétion (CA3) et séparation de motifs (gyrus denté) pilotée par un gain noradrénergique sur les erreurs de prédiction de `jev-1.14.0`.

1. **Loi d'apprentissage & d'auto-organisation hors-poids** :
Le graphe de citations/code est un graphe factoriel $(V, C)$ où les cliques $c \in C$ sont évaluées sans coût par `jev-1.14.0` pour estimer les marginales $b_i(x_i)$ et $b_c(x_c)$. L'essaim minimise l'énergie libre de Bethe :
$$F_B(\{b\}) = \sum_{c \in C} \sum_{x_c} b_c(x_c) \ln \frac{b_c(x_c)}{\psi_c(x_c)} - \sum_{i \in V} (d_i - 1) \sum_{x_i} b_i(x_i) \ln b_i(x_i)$$
Deux sous-populations opèrent : **Gyrus Denté (GD, Gemini, 20$)** projette les embeddings `jev-1.14.0` dans un espace sparse orthogonal ($\ell_0$-contrainte) pour forcer la *séparation de motifs* inter-silos. **CA3 (Claude, 100$)** opère comme réseau auto-associatif de Hopfield moderne effectuant la *complétion de motifs* (ponts mécanistes). La neuromodulation tonique/phasique (Locus Coeruleus) ajuste la température inverse $\beta_{LC}(t) \propto D_{KL}(b_c^{(t)} \parallel b_c^{(t-1)})$ : un pic de surprise de Bethe déclenche un "reset réseau" allouant dynamiquement les tokens Claude aux arêtes factorielles frustrées ($\psi_c$ dissonants).

2. **Fonction objectif anti-vernis** :
$$\mathcal{J}(H_A, H_B) = \underbrace{\left(1 - \frac{|\langle \Phi_{GD}(s_A), \Phi_{GD}(s_B) \rangle|}{\|\Phi_{GD}(s_A)\|\|\Phi_{GD}(s_B)\|}\right)}_{\text{Séparation GD inter-silos}} \times \underbrace{\min_{m \in \mathcal{M}(\text{Llama})} \left| D_{KL}(P(Y|do(m), H_A) \parallel P(Y|do(m), H_B)) \right|}_{\text{Divergence interventionnelle causale } (H_A \perp H_B)} \times \exp(-H_{\text{Bethe}}(\text{vernis}))$$
où $H_{\text{Bethe}}(\text{vernis})$ pénalise la redondance sémantique mesurée par `jev-1.14.0` entre les nœuds de citation intermédiaires.

3. **Pont inédit & Duel ($
