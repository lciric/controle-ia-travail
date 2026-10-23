BASSIN_MATH: Recuit Chimérique TAP-Parisi (RCTP)
LOI_PROPOSEE: $m_i^{(t+1)} = \tanh\left(\beta_t \left[ h_i^{\text{ancrage}} + \sum_{j \neq i}^{k_t} J_{ij}^{(t)} m_j^{(t)} - m_i^{(t)} \sum_{j \neq i}^{k_t} (J_{ij}^{(t)})^2 (1 - (m_j^{(t)})^2) \right]\right)$

1. **Mécanisme d'Auto-Organisation (Essaim + Collisionneur Adaptatif)** :
L'essaim est un verre de spin de Sherrington-Kirkpatrick hors-équilibre (référence à vérifier) où chaque agent $i \in \{1, \dots, k_t\}$ d'espèce $s_i \in \{\text{fable}, \text{opus}, \text{argon}\}$ possède un état de croyance $m_i^{(t)} \in [-1, 1]$. Pour vaincre la dérive `H9`, le prompt initial agit comme un champ magnétique externe fixe $h_i^{\text{ancrage}}$ réinjecté à chaque tour $t$. Le terme de réaction d'Onsager $-m_i^{(t)} \sum (J_{ij}^{(t)})^2 (1 - (m_j^{(t)})^2)$ des équations TAP (référence à vérifier) soustrait l'auto-excitation, annulant la corrélation des erreurs par poids partagés (`H4'`). L'apprentissage sans réentraînement opère par plasticité des couplages $J_{ij}^{(t)}$ : si $s_i = s_j$ (monoculture), un chevauchement élevé $q_{ij} = m_i^{(t)} m_j^{(t)} > 0.7$ (`illustratif`) déclenche une transition vers un couplage anti-ferromagnétique ($J_{ij}^{(t+1)} < 0$, routage prédateur) en injectant un critique inter-espèces (`argon` contre `claude`). La taille $k_t$ croît par nucléation si la susceptibilité $\chi_t = \beta_t \sum_{i,j} (1 - q_{ij}^2)$ diverge. L'allocation (100 USD Claude / 20 USD Gemini) est régie par un potentiel chimique par espèce $\mu_s$ ajustant la température inverse $\beta_t$. L'arrêt adaptatif $T$ survient à la transition de phase de gel d'Almeida-Thouless (référence à vérifier), lorsque la variance de la distribution d'ordre de Parisi $P(q)$ (référence à vérifier) chute sous $\epsilon = 0.05$ (`illustratif`).

2. **Fonction Objectif & Anti-Goodhart** :
L'énergie libre de Helmholtz généralisée à minimiser couple `jev-1.14.0` ($S_{\text{jev}}$), la densité d'ancrage bibliographique vérifiée par API ($G_{\text{bib}}$) et l'entropie de compression ($H_{\text{zlib}}$) pour bloquer les textes vides, le gabarit lexical et la récitation paramétrique :
$$\mathcal{R}_t = S_{\text{jev}}(x_t) \cdot \tanh(\gamma G_{\text{bib}}(x_t)) \cdot \Theta(H_{\text{zlib}}(x_t) - H_{\min}) - \frac{1}{\beta_t} D_{\text{KL}}(P_{\text{emp}}(q) \parallel P_{\text{Parisi}}^*(q))$$
où $\Theta$ est la fonction de Heaviside, $H_{\min} = 4.2$ bits/car (`illustratif`), $\gamma = 1.5$ (`illustratif`), et $P_{\text{Parisi}}^*(q)$ impose une brisure de symétrie des répliques garantissant la diversité topologique.

3. **Duel Décisif de Validation M3 ($H_A \perp H_B$)** :
Sur un budget fixe de 5 USD Claude et 1 USD Gemini (`illustratif`) :
- $H_A$ (Dynamique RCTP) : Couplages TAP avec soustraction d'Onsager et routage prédateur anti-ferromagnétique inter-espèces.
- $H_B$ (Contrôle négatif) : Champ moyen naïf ferromagnétique ($J_{ij} > 0$ fixe, sans terme d'Onsager ni chimérisme adaptatif) à même budget.
- Observable unique $O$ : Ratio du score $\mathcal{R}_T$ final sur la covariance inter-espèces des erreurs factuelles détectées via Crossref/arXiv, avec $I_A = [2.5, +\infty[$ (`illustratif`) et $I_B = [0, 1.2]$ (`illustratif`), garantissant $I_A \cap I_B = \emptyset$.
Ce protocole valide l'auto-organisation par brisure de symétrie sans mise à jour des poids. FIN-EXPLORATEUR-M3
