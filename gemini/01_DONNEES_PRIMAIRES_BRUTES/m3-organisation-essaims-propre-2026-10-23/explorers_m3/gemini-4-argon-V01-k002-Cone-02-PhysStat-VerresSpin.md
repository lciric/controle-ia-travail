BASSIN_MATH: Recuit Chimérique à Brisure de Symétrie des Répliques (RC-BSR)
LOI_PROPOSEE: L'essaim minimise l'énergie libre d'un hamiltonien de Sherrington-Kirkpatrick épistémique $H(\sigma) = -\sum_{i<j} J_{ij} \sigma_i \sigma_j - \sum_i h_i \sigma_i$ en poussant la distribution de recouvrement des répliques $P(q)$ vers un régime ultramétrique de Parisi ($k$-RSB) pour piéger les états fondamentaux d'hypothèses frustrées.

1. **Loi d'apprentissage & d'auto-organisation hors-poids** :
Chaque nœud documentaire (arXiv, GitHub, Alignment Forum) est un spin $\sigma_i \in \{-1, +1\}^d$ (vecteur d'assertions mécanistes). L'essaim instancie $R$ répliques chimériques évoluant sous dynamique de Glauber. Le couplage $J_{ij} = \text{jev}(i,j) \cdot \exp(-d_{\text{cit}}(i,j)/\xi) - \lambda \mathbb{I}(\text{co-citation})$ est pré-calculé gratuitement à l'infini par `jev-1.14.0` et les API bibliographiques : il crée une **frustration géométrique** ($J_{ij}J_{jk}J_{ki} < 0$) dès que deux papiers sont sémantiquement isomorphes ($\text{jev} \to 1$) mais topologiquement disjoints dans le graphe de citations ($d_{\text{cit}} \to \infty$).
Allocation des 120 USD :
- Phase paramagnétique ($T > T_c$, Gemini 20 USD) : échantillonnage thermique rapide des plaquettes frustrées.
- Transition vitreuse ($T \to T_c^-$, Claude 100 USD) : activé uniquement lorsque le paramètre d'ordre de Parisi $q_{\alpha\beta} = \frac{1}{N}\sum_i \sigma_i^\alpha \sigma_i^\beta$ bifurque ($dP(q)/dq$ devient bimodal). Claude synthétise alors le pont hors-équilibre qui résout la frustration locale.

2. **Fonction objectif anti-vernis** :
$$\mathcal{L}_{\text{anti-vernis}}(i,j) = \underbrace{\left(1 - \frac{|\Gamma(i) \cap \Gamma(j)|}{|\Gamma(i) \cup \Gamma(j)|}\right)}_{\text{Distance inter-silos}} \times \underbrace{\det\left(\Sigma_{\text{jev}}(H_A, H_B)\right) \cdot \mathcal{D}_{JS}\left(\mathbb{P}(\text{Act}_{\text{Llama}} | do(H_A)) \parallel \mathbb{P}(\text{Act}_{\text{Llama}} | do(H_B))\right)}_{\text{Falsifiabilité causale } (H_A \perp H_B)}$$
où $\Gamma$ est le voisinage de citations et $\Sigma_{\text{jev}}$ la matrice de covariance d'entailment évaluée par `jev-1.14.0` sur les interventions d'activation de Llama-3.1-8
