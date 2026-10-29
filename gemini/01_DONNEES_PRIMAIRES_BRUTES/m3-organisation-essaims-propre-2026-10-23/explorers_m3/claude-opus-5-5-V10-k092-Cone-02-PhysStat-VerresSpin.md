BASSIN_MATH: Température Effective de Cugliandolo-Kurchan à Réaction d'Onsager (TECK-O)

LOI_PROPOSEE: $X_i(t,t_w)=\dfrac{T\,R_i(t,t_w)}{\partial_{t_w}C_i(t,t_w)}$ et $T^{\rm eff}_i=T/X_i$ ; on spawne un démolisseur chimérique si $T^{\rm eff}_i>T^*$, un explorateur si $X_i\to1$ avec un faible recouvrement aux sources, et l'on fusionne les agents sinon.

**1. Mécanisme d'auto-organisation hors-poids**

Chaque agent $i$ d'une famille $f$ est un spin dont l'état $s_i$ est le plongement `jev` de ses affirmations.

- **Couplages.** On pose $J_{ij}=\mathrm{corr}_{\rm jev}(s_i,s_j)$.
- **Équation TAP avec terme d'Onsager.** La magnétisation suit
$$m_i=\tanh\Big(\beta\big[h_0+h_i+\textstyle\sum_j J_{ij}m_j-\beta m_i\sum_j J_{ij}^2(1-m_j^2)\big]\Big).$$
Le terme d'Onsager retire l'écho de sa propre opinion. Pour les paires de même famille, on soustrait en plus $J_{ff}$, mesuré sur des tâches témoins : cela neutralise `H4'`.
- **Mesures de vieillissement.** $C$ est l'autocorrélation à deux temps des sorties. $R$ est la réponse à un micro-champ canari $\delta h$ injecté dans la consigne à l'instant $t_w$.
- **Diagnostic de phase.**
  - $X\approx1$ indique un équilibre trivial, c'est-à-dire une récitation paramétrique. On spawne alors un explorateur ancré dans le graphe arXiv ou Semantic Scholar.
  - $X\to0$ indique un régime vitreux bloqué dans un état métastable. On spawne alors un démolisseur Red-Team issu d'une autre famille : la chimère est justifiée.
- **Topologie.** Une arête de délégation $i\to j$ n'existe que si $q_0^{(j)}=\langle m_j\,h_0\rangle\ge q_c$, ce qui coupe la dérive `H9`.
- **Budget.** La part d'une famille vaut $b_f\propto e^{-\beta\,\Delta F^{\rm TAP}_f}$, projetée sur les plafonds de 100 USD pour Claude et 20 USD pour Gemini.

**2. Fonction objectif et anti-Goodhart**

$$\mathcal R=\frac{N_{\rm vérif}}{\rm USD}-\lambda\,|X-X^*|-\mu\sum_{i\sim j,\,f(i)=f(j)}C^{\rm conn}_{ij}-\nu\,(1-q_0).$$

- $N_{\rm vérif}$ compte les affirmations validées par les API Crossref et Semantic Scholar : DOI existant et citation exacte.
- `jev` sert uniquement d'instrument de mesure de $C$ et $R$. Il n'est jamais une récompense.
- Les canaris sont cachés et renouvelés à chaque époque, et un lot d'audit est tenu à l'écart. Optimiser contre le juge est donc impossible.

**3. Duel décisif $H_A\perp H_B$**

- **Conditions comparées**, toutes au même budget (100 USD Claude, 20 USD Gemini) et sur $N=60$ tâches appariées :
  - $H_A$ : l'essaim TECK-O ;
  - $H_B$ : une topologie fixe ;
  - un essaim i.i.d. de même taille ;
  - un **contrôle négatif** : TECK-O avec des $X_i$ permutés entre agents et instants, soit le même coût mais une information de phase détruite.
- **Métriques préenregistrées** : affirmations vérifiées par USD, corrélation intra-famille des erreurs, et taux de dérive $1-q_0$.
- **Analyse** : bootstrap apparié et test de Holm.
- **Critère de falsification** : la loi est réfutée si TECK-O ne surpasse pas le contrôle permuté avec $p<0.01$, ou si $T^{\rm eff}$ ne prédit pas la qualité des spawns ($\rho\le0$).
