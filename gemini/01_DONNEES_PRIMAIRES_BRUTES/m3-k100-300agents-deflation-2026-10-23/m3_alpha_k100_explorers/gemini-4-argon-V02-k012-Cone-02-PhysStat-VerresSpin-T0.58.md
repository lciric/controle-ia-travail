BASSIN_MATH: Vieillissement-RFOT-Kovacs-Franz-Parisi (VRKFP)
LOI_PROPOSEE: L'essaim évolue dans un régime vitreux hors-équilibre où des avalanches de réarrangements coopératifs (RFOT) sont déclenchées au seuil du potentiel de Franz-Parisi $V_{FP}(q)$ par injection de chocs thermiques de Kovacs asymétriques sur les sous-graphes d'idées frustrées.

1. **Loi d'apprentissage & d'auto-organisation hors-poids de l'essaim** :
Les concepts extraits forment un liquide surfondu de spins $s_i$ (embeddings `jev-1.14.0`). Sans appel LLM, `jev-1.14.0` évalue les couplages $J_{ij}$ sur le graphe de citations et mesure le potentiel de Franz-Parisi $V_{FP}(q) = -\lim_{n\to 0} \frac{1}{\beta n} \ln \int \mathcal{D}\sigma \exp(-\beta \sum_{a=1}^n \mathcal{H}[\sigma^a]) \delta(q(\sigma^a, s_0) - q)$, qui quantifie la barrière libre entre une étude source $s_0$ et un état métastable cible à recouvrement $q$.
- **Budget gratuit (`jev-1.14.0` + API)** : vieillissement physique ($t_w \to \infty$) du graphe par dynamique de Glauber hors-équilibre jusqu'au blocage dans un état amorphe (silo).
- **Effet mémoire de Kovacs (20 USD Gemini)** : dès que $\nabla_q V_{FP}(q) = 0$ (inflexion spinodale à $q = q_{EA}$), Gemini applique un saut thermique brutal $T_1 \to T_2 > T_g \to T_0$ (injection de littérature orthogonale), induisant un rebond non-monotone d'enthalpie qui brise la cage locale sans recuit global.
- **Instanton RFOT (100 USD Claude)** : alloué uniquement lorsque le rayon de la région de réarrangement coopératif atteint la longueur mosaïque critique $\xi^* = (\Upsilon / (T s_c(T)))^{1/(d-\theta)}$, où l'entropie configurationnelle $s_c(T)$ s'annule (transition de Kauzmann). Claude synthétise alors le pont.

2. **Fonction objectif anti-vernis** :
$$\mathcal{R}(H_A, H_B) = \underbrace{(1 - q_{\text{jev}}(A,B)) \cdot d_{\text{cit}}(A,B)}_{\text{Distance inter-silos}} \times \underbrace{\Delta V_{FP}(q^*) \cdot \left\| \text{do}(\mathbf{h}_l \leftarrow \mathbf{h}_l + \delta_A) - \text{do}(\mathbf{h}_l \leftarrow \mathbf{h}_l + \delta_B) \right\|_{\text{KL}}}_{\text{Falsifiabilité causale } H_A \perp H_B \text{ sur Llama-3.1}}$$
Tout vernis sémantique ($q > q_{EA}$ ou divergence KL d'intervention nulle sur
