BASSIN_MATH: Décimation-SurveyPropagation-Mézard-Zecchina-Jarzynski (DSPMZJ)
LOI_PROPOSEE: L'essaim résout la K-SAT-sémantique de la littérature via la Propagation d'Enquêtes (Survey Propagation) sur graphe de facteurs à 0 USD (`jev-1.14.0`), n'allouant le budget génératif qu'aux variables gelées à haute polarisation lors des avalanches hors-équilibre de Jarzynski.

**1. Auto-organisation hors-poids & Allocation budgétaire**
Le graphe de citations (arXiv/S2) est modélisé comme un graphe de facteurs bipartite : les nœuds-variables $i \in V$ sont les concepts/mécanismes, les nœuds-facteurs $a \in F$ sont les contraintes d'incompatibilité ou de synergie entre articles, évaluées gratuitement par `jev-1.14.0`. Au lieu d'échantillonner des états (coûteux), l'essaim propage des *enquêtes* (surveys) $\eta_{a \to i} \in [0,1]$ (probabilité d'avertissement de frustration d'un cluster de Mèzard-Zecchina) à coût $0\$$ :
$$\eta_{a \to i} = \prod_{j \in \partial a \setminus i} \left[ \frac{\Pi_{j \to a}^u}{\Pi_{j \to a}^u + \Pi_{j \to a}^s + \Pi_{j \to a}^0} \right]$$
où $\Pi^{u,s,0}$ sont les produits de messages non-satisfaits, satisfaits et jokers.
*Décimation et Jarzynski :* Les agents génératifs ne sont réveillés que lorsque la complexité configurationnelle $\Sigma(\eta)$ s'annule (transition de condensation). L'allocation des 120 USD suit l'égalité de Jarzynski hors-équilibre $\langle e^{-\beta W} \rangle = e^{-\beta \Delta F}$ : Gemini (20 USD) effectue des perturbations rapides (travail $W_{Gem}$) sur les variables à biais maximal $B_i = |\Pi^+_i - \Pi^-_i|$; Claude (100 USD) est réservé à la décimation irréversible des *backbones* (squelettes rigides où $\eta_{a \to i} \to 1$), synthétisant le pont scientifique et réduisant le graphe.

**2. Fonction objectif anti-vernis**
$$\mathcal{L}_{DSPMZJ}(i, j) = d_{\text{ultramétrique}}(i, j) \cdot \Delta \Sigma_{i \wedge j} \cdot \mathbb{I}\left( \text{JEV}(H_A \cap H_B) < \epsilon \right)$$
où $d_{\text{ultramétrique}}$ est la distance de saut entre clusters de l'arbre généalogique des états purs (silos), $\Delta \Sigma_{i \wedge j}$ est la chute d'entropie de complexité mesurée par `jev-1.14.0` lors de la fusion forcée des concepts, et le terme $\mathbb{I}$ garantit l'orthogonalité expérimentale stricte ($H_A \perp H_B
