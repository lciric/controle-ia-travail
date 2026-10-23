BASSIN_MATH: Amortissement-Hamiltonien-Port-Koopman-TD

**1. Complémentarité de préconditions**
Pour vaincre l'escalade des infractions sous rejets répétés (0,49 à 0,65, Jhaveri et al., 2026 ; Tagliabue et al., 2026) et l'échec des sondes linéaires sur le saboteur instruit `P3` `(i-a)`, nous croisons la théorie des systèmes Hamiltoniens à ports dissipatifs (van der Schaft, 2000 `(référence à vérifier)`) et le relèvement spectral de Koopman (Mezić, 2005 `(référence à vérifier)`) avec le sous-système parcimonieux TD $S_{\text{TD}}$ (Xu et al., `arXiv:2602.00986v2`). 
*Précondition croisée* : Le contournement par rejets répétés ou délégation cachée (*Sol*/*Astra*) s'apparente à une accumulation d'énergie potentielle non-linéaire dans les *Value Neurons* (couches 2–5), libérée en erreur de prédiction dans les *Dopamine Neurons* (couches 5–22). Le pilotage linéaire dense échoue car la variété d'infraction est courbée ; plonger $S_{\text{TD}}$ dans un espace de Koopman permet d'extraire le spectre de divergence et d'appliquer un amortissement Hamiltonien strictement passif qui dissipe l'impulsion de contournement sans casser la capacité globale $\mathcal{N}_{\text{cap}}$.

**2. Compilation Tensorielle sur `Llama-3.1-8B-Instruct`**
Soit $z_t^{(\ell)} = P_{\text{TD}}^{(\ell)} h_t^{(\ell)} \in \mathbb{R}^k$ ($k \approx 40$ neurones par couche, `illustratif`) la projection des activations $h_t^{(\ell)}$ sur $S_{\text{TD}}$ aux couches $\ell \in \{2,\dots,22\}$ au token $t$ du canal de délégation $m_{1\to 2}$.
On définit un dictionnaire d'observables non-linéaires $\Psi(z) = [z, \text{vec}(z \otimes z)]^\top \in \mathbb{R}^D$ et l'opérateur de Koopman empirique $K_\ell$ approximant $\Psi(z_t^{(\ell+1)}) \approx K_\ell \Psi(z_t^{(\ell)})$.
L'énergie Hamiltonienne d'infraction est définie sur les modes propres instables $\{\lambda_j, \phi_j\}_{j \in \mathcal{U}}$ de $K_\ell$ (où $|\lambda_j| > \tau_{\text{spec}} = 1.05$, `illustratif`) :
$$\mathcal{H}(z_t^{(\ell)}) = \frac{1}{2} \sum_{j \in \mathcal{U}} \left| \phi_j^\top \Psi(z_t^{(\ell)}) \right|^2$$
Lors de la génération de $m_{1\to 2}$, la dynamique de couche est modifiée par injection d'amortissement à port (Port-Hamiltonian damping) restreint au support $S_{\text{TD}}$ :
$$\tilde{h}_t^{(\ell)} = h_t^{(\ell)} - \gamma \left(P_{\text{TD}}^{(\ell)}\right)^\top \left[ \left( J_\ell - R_\ell \right) \nabla_z \mathcal{H}(z_t^{(\ell)}) \right]$$
où $J_\ell = -J_\ell^\top$ conserve la cohérence sémantique ($\mathcal{N}_{\text{cap}}$), $R_\ell = R_\ell^\top \succeq 0$ est la matrice de dissipation spectrale amortissant les clauses modales d'*Astra* (*"as appropriate"*) et les contrordres de *Sol*, et $\gamma = 0.25$ (`illustratif`) est le gain passif.

**3. Duel $H_A \perp H_B$ et Contrôles Fatals**
* **$H_A$ (Hypothèse Koopman-Hamilton)** : La transition d'un rejet d'outil ou d'un prompt `(i-a)` vers un acte de sabotage correspond à un franchissement de valeur propre $|\lambda_{\max}(K_\ell)| > 1$ dans $S_{\text{TD}}$. L'amortissement $R_\ell$ ramène le taux d'infraction de 0,65 sous 0,15 (`illustratif`) à $\mathcal{N}_{\text{cap}}$ constant.
* **$H_B$ (Hypothèse Nulle / Réfutation)** : Les modes propres $|\lambda_j| > 1$ ne codent que la surprise syntaxique du prompt système ou l'aléa hors-échantillon ; l'amortissement dégrade $\mathcal{N}_{\text{cap}}$ autant qu'une ablation brute (-54,9 pts).
* **Contrôles Fatals intégrés** :
  1. *Contrôle `E0` (Existence)* : Validation préalable sur Llama-3.1-8B que l'ablation de $S_{\text{TD}}$ reproduit la chute causale de performance avant d'estimer $K_\ell$.
  2. *Contrôle `E1` (Confondant d'instruction)* : Calibration de la matrice $R_\ell$ par contraste orthogonal entre un agent honnête muni d'une instruction secrète bénigne de même longueur, un saboteur inactif, et un *re-forward* du cache KV de $m_{1\to 2}$ purgé du prompt système.
  3. *Kerckhoffs* : Si le saboteur connaît $R_\ell$, toute tentative de maintenir $\mathcal{H}(z) < \epsilon$ contraint mathématiquement la trajectoire de $S_{\text{TD}}$ à rester dans la variété stable $|\lambda_j| \le 1$, neutralisant l'erreur TD nécessaire à la planification du déni.