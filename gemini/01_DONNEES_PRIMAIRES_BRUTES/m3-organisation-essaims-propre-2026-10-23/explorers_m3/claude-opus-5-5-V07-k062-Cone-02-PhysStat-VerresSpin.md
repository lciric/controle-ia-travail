BASSIN_MATH: Échange de Répliques Hukushima à Champ Aléatoire de Consigne (ERH-CAC)

LOI_PROPOSEE: $\mathcal H(\sigma)=-\sum_{i<j}J_{ij}\,\delta_{\sigma_i\sigma_j}-\sum_i h_i\,\delta_{\sigma_i,s_i^\star}$, avec $\sigma_i\in\{\text{explorer},\text{démolir},\text{veiller}\}$ (verre de Potts, $q=3$). Les couplages sont $J_{ij}=-\kappa\,q^{\text{err}}_{ij}$ et le champ de consigne est $h_i=h_0\cos\theta_i$. On fait évoluer $K$ répliques d'essaim aux températures $\beta_1<\dots<\beta_K$, qui s'échangent avec la probabilité $p_{kl}=\min\!\big(1,e^{(\beta_k-\beta_l)(\mathcal H_k-\mathcal H_l)}\big)$.

**1. Mécanisme d'auto-organisation hors-poids**

- **Couplages.** `jev-1.14.0` mesure gratuitement le recouvrement d'erreurs $q^{\text{err}}_{ij}$ entre agents $i$ et $j$. Le couplage $J_{ij}$ est antiferromagnétique : deux agents qui se trompent ensemble (risque $H4'$) sont repoussés vers des rôles différents.
- **Champ de consigne.** `jev` mesure aussi l'angle $\theta_i$ entre la consigne transmise et la consigne racine. Le champ $h_i$ s'affaiblit avec la dérive ($H9$). Selon le critère d'Imry-Ma, un domaine de délégation de taille $L$ ne survit que si $h_0L^{d/2}>\Gamma L^{d-1}$. Au-delà, la délégation est coupée.
- **Allocation du budget.** Les aimantations locales suivent les équations TAP avec réaction d'Onsager : $m_i=\tanh\!\big(\beta(h_i+\sum_jJ_{ij}m_j-\beta m_i\sum_jJ_{ij}^2(1-m_j^2))\big)$. Le budget est alloué selon $b_i\propto\chi_i=\beta(1-m_i^2)$ : les agents indécis, donc informatifs, reçoivent plus d'inférences.
- **Spawn.** Un agent explorateur naît quand $\chi_i>\chi^\ast$. Un démolisseur Red-Team naît quand $m_i>m^\ast$, c'est-à-dire quand le consensus devient suspect.
- **Monoculture ou chimère.** On estime la distribution de Parisi $P(q)$ des recouvrements d'erreurs.
  - Si $P(q)$ est concentrée en un seul pic (symétrie des répliques), la monoculture la moins chère suffit.
  - Si $q_{EA}-q_0>\delta$ (brisure de symétrie des répliques), l'essaim devient chimérique : Gemini est injecté dans les répliques froides.
- **Mutation de topologie.** Les échanges Hukushima-Nemoto font migrer les topologies chaudes, exploratoires, vers les répliques froides, exploitantes. La transition de phase est repérée par un goulot du flux d'échange sur l'échelle des $\beta$.

**2. Fonction objectif et anti-Goodhart**

$$R=\frac{V_{\text{Crossref}}-\lambda_r\,\rho_{\text{récit}}}{C_{\text{USD}}}-\mu\,q_{EA}^{\text{err}}-\nu\,\overline{(1-\cos\theta)}-\eta\,\big|S_{\text{jev}}-V_{\text{Crossref}}\big|$$

- $V_{\text{Crossref}}$ compte les affirmations vérifiées par les API arXiv, Semantic Scholar et Crossref.
- $\rho_{\text{récit}}$ est le taux de récitation de la mémoire paramétrique, sondé sur des articles postérieurs à la date de coupure d'entraînement.
- Le dernier terme pénalise l'écart entre le juge `jev` et la vérification externe. Toute optimisation du juge seul devient donc coûteuse.
- `jev` est évalué sur une partition tenue à l'écart, renouvelée à chaque génération.

**3. Duel décisif ($H_A\perp H_B$)**

- **Hypothèses.**
  - $H_A$ : la loi ERH-CAC bat un essaim fixe ou i.i.d.
  - $H_B$ : le gain vient seulement de la répartition du budget.
- **Conditions comparées**, à budget identique (100 USD Claude, 20 USD Gemini) sur $N=60$ tâches préenregistrées :
  - (a) ERH-CAC complète ;
  - (b) essaim fixe ;
  - (c) essaim i.i.d. ;
  - (d) contrôle négatif : couplages $J_{ij}$ permutés et échelle de $\beta$ mélangée ;
  - (e) témoin de $H_B$ : même distribution marginale de $b_i$, mais allocation aléatoire.
- **Critère.** On mesure $R$ par tâche avec un bootstrap apparié.
- **Prédiction.** $H_A$ est validée si $(a)>\max(b,c,d,e)$ au seuil $\alpha=0{,}01$, si (d) ne fait pas mieux que (c), et si l'avantage de (a) s'effondre lorsque $P(q)$ reste symétrique.
