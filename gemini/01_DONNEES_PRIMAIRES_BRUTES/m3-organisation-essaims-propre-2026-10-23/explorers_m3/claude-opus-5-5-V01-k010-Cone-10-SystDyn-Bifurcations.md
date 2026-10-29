BASSIN_MATH: Loi de Bord-du-Chaos Spectral (LBCS)

LOI_PROPOSEE: $\dot w_i = w_i\big[(\mathcal{K}\Phi)_i - \bar{\Phi}\big] - \eta\,\partial_{w_i} C$, sous la contrainte $\lambda_{\mathrm{dérive}} < 0 < \lambda_{\mathrm{décor}}$. Ici $w_i$ est la part de budget du rôle ou modèle $i$, $\mathcal{K}$ l'opérateur de Koopman estimé et $C$ le coût en USD.

**1. Mécanisme d'auto-organisation hors-poids**

L'état de l'essaim est $x_t = (W_t, P_t, M_t)$ : graphe de communication, consignes et mémoire externe. Les sorties sont plongées dans l'espace des traits de `jev-1.14.0`, d'usage gratuit. On estime ensuite $\mathcal{K}$ par EDMD sur les trajectoires.

- **Explorateur.** Si la valeur propre dominante $|\mu_1| \to 1$ avec un trou spectral faible, l'essaim est piégé dans un attracteur, c'est-à-dire une récitation paramétrique. On spawne alors un explorateur, ancré sur arXiv, Semantic Scholar et Crossref.
- **Démolisseur Red-Team.** Si un mode instable apparaît ($|\mu_k| > 1$, consensus fragile), on spawne un démolisseur.
- **Monoculture ou chimère.** On mesure l'exposant de Lyapunov $\lambda_{\mathrm{décor}}$ entre répliques perturbées. Une valeur $\lambda_{\mathrm{décor}} \approx 0$ signale des erreurs corrélées (H4'). Le paramètre de bifurcation $\beta$, part chimérique (Fable, Opus, Argon), augmente alors jusqu'à franchir la bifurcation de Hopf où $\lambda_{\mathrm{décor}} > 0$.
- **Contrôle de la dérive (H9).** On impose $\lambda_{\mathrm{dérive}} = \lim \frac{1}{n}\log\lVert P_n - P_0 \rVert < 0$ le long des chaînes de délégation. Toute délégation expansive est élaguée.
- **Budget.** Une dynamique de réplicateur répartit le budget séparément sur chaque réservoir (Claude 100, Gemini 20).

**2. Fonction objectif et anti-Goodhart**

$$R = \frac{V_{\mathrm{ext}}}{C} - \alpha\,\rho_{\mathrm{err}} - \gamma\,\big|\,\overline{J}_t - \langle J\rangle_{\mathrm{ens}}\big| - \delta\,\mathrm{KL}\big(J \,\Vert\, V_{\mathrm{ext}}\big)$$

- $V_{\mathrm{ext}}$ compte les affirmations vérifiées par les graphes bibliographiques, un signal non manipulable par l'essaim.
- $\rho_{\mathrm{err}}$ est la corrélation des erreurs entre agents.
- Le terme ergodique pénalise l'écart entre la moyenne temporelle et la moyenne d'ensemble du juge $J$. Une rupture d'ergodicité indique une exploitation locale du juge.
- Le terme KL pénalise le découplage entre le juge et la vérification externe.
- Les rubriques de `jev` tournent selon un calendrier caché.

**3. Duel décisif ($H_A \perp H_B$)**

- **$H_A$** : la LBCS augmente $V_{\mathrm{ext}}/C$ et réduit $\rho_{\mathrm{err}}$.
- **$H_B$** : tout gain provient du seul surcroît de diversité ou de mutation.

Quatre bras sont comparés à budget strictement identique (120 USD) :
- (a) LBCS ;
- (b) essaim fixe ;
- (c) essaim i.i.d., avec mutations aléatoires au même taux que (a) ;
- (d) contrôle négatif : LBCS alimentée par un spectre de Koopman permuté.

Protocole :
- $N = 60$ tâches préenregistrées, avec des seeds appariées.
- Test de permutation, avec correction de Holm.

$H_A$ est validée si (a) bat à la fois (c) et (d) avec $p < 0{,}01$ et si $\lambda_{\mathrm{dérive}}(a) < 0$. Elle est réfutée si (d) égale (a).
