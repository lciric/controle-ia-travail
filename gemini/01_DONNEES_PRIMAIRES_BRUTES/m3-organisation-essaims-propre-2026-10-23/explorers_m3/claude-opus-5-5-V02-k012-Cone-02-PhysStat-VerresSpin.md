BASSIN_MATH: Loi FDR-Gardner de Vieillissement d'Essaim (VIEIL-FDR)

LOI_PROPOSEE: $X_t=\dfrac{T\,\partial_{t'}C(t,t')}{\partial_{t'}R(t,t')}\ \Rightarrow\ \begin{cases}X_t<X^*\ (\text{vieillissement, verre}) & \text{spawn démolisseur, chauffer } \beta\downarrow\\ \mathrm{Var}_{P(q)}<\epsilon\ (\text{symétrie des répliques, erreurs corrélées}) & \text{greffer une chimère}\\ \text{sinon} & \text{élaguer, } \beta\uparrow\end{cases}$

1. **Mécanisme d'auto-organisation hors-poids**
Chaque agent $i$ émet une croyance $m_i\in[-1,1]$ sur une assertion, notée par `jev-1.14.0`. Les couplages $J_{ij}$ sont estimés par l'accord historique entre agents. La mise à jour TAP avec réaction d'Onsager s'écrit :
$m_i=\tanh\!\big(\beta[h_i+\sum_j J_{ij}m_j-\beta m_i\sum_j J_{ij}^2(1-m_j^2)]\big)$.
Le terme d'Onsager soustrait l'écho de sa propre consigne renvoyée par les délégués, ce qui combat la dérive H9 et l'auto-confirmation mémorielle. Le champ $h_i$ provient uniquement de sources vérifiées par Crossref et Semantic Scholar, contre la récitation de la mémoire paramétrique.
La topologie mute selon un critère hors-équilibre de Cugliandolo-Kurchan. On mesure la corrélation $C$ (stabilité des réponses) et la réponse $R$ (sensibilité à une perturbation injectée).
- Si $X_t<X^*$, l'essaim vieillit dans un état métastable : on spawne un Red-Team.
- Si la distribution des recouvrements $P(q)$ inter-répliques est piquée (absence de brisure de symétrie des répliques, situation H4′), on remplace l'agent le plus redondant par une autre famille de poids (Claude ↔ Gemini).
- Si $P(q)$ présente une structure ultramétrique multi-vallées, la monoculture suffit.
Le budget est alloué selon un poids de Gibbs $p_k\propto e^{-\beta c_k}\,\mathrm{Var}_k(q)$ sous les contraintes 100 USD Claude et 20 USD Gemini.

2. **Fonction objectif et anti-Goodhart**
$\mathcal{R}=\underbrace{\mathrm{Acc}_{\text{held-out}}}_{\text{vérité plantée}}-\lambda\,|X_t-X^*|-\mu\,\overline{q_{iJ}}-\nu\,\frac{\text{coût}}{\text{budget}}$
Ici, $q_{iJ}$ est le recouvrement entre les sorties des agents et les biais connus du juge. Le juge `jev` est évalué sur une réplique gelée, invisible pendant l'évolution, et ses seuils sont rééchantillonnés à chaque époque. Optimiser le juge sans gagner en exactitude augmente $q_{iJ}$, ce qui pénalise la manœuvre.

3. **Duel décisif ($H_A\perp H_B$)**
- **Tâches** : instances à vérité plantée (citations réelles et falsifiées, vérifiables par les API), à difficulté $\alpha$ croissante.
- **Bras à budget égal** : (a) VIEIL-FDR ; (b) topologie fixe ; (c) ensemble i.i.d. ; (d) contrôle négatif : VIEIL-FDR avec $X_t$ et $P(q)$ permutés aléatoirement.
- **$H_A$** : (a) surpasse (b), (c) et (d) en exactitude held-out, avec une transition de phase décalée $\alpha_c^{(a)}>\alpha_c^{(b,c,d)}$.
- **$H_B$** : (d) égale (a), donc le gain provient de la simple stochasticité.
- **Test** : bootstrap apparié sur 30 graines, avec $p<0{,}01$ et correction de Holm.
