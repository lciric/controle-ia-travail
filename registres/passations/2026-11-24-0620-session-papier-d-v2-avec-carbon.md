# Passation dédiée (v2 consolidée avec Carbon) — Session parallèle « Papier D » (`papier-d/evasion-post-entrainement-v1`)

- **Programme** : Plan Turing (`GO-2026-11-24-01`, `GO-2026-11-24-04`, `GO-2026-11-24-05`, `R-5240`, `R-5241`)
- **Horodatage** : `2026-11-24T06:21:00Z` (`date -u`)
- **Branche de travail EXCLUSIVE de cette session parallèle** : **`papier-d/evasion-post-entrainement-v1`**
  - **Règle absolue anti-conflit** : ne **jamais** modifier `registres/*` ni pousser sur `main` depuis la session parallèle « Papier D ». Tout le travail (preuves LaTeX, scripts Python, diagrammes de phase 2D, simulations RL tabulaires/bandits, brouillons d'atelier ICLR / NeurIPS) se commite et se pousse uniquement sur `origin/papier-d/evasion-post-entrainement-v1`.

---

## 1. Nouveautés majeures depuis la passation v1 de `05:55Z`

1. **Les deux évaluations en effort élevé de Carbon sont TERMINÉES et versées** dans `docs/notes/cartographie-mathematiques-ouvertes-v1/cible-publication-collisionneur-v1/carbon-effort-eleve/` :
   - `reponse-carbon-indep-cible-pub-v1.md` (lecture froide 100 % indépendante comme président de comité à ICML / NeurIPS / COLT / SaTML) ;
   - `reponse-carbon-critique-reponse-mere-v1.md` (contre-lecture critique sans complaisance de la feuille de route v1).
2. **Feuille de route v2 consolidée (`.md` + `.pdf` vectoriel sans débordement)** versée dans :
   - `docs/notes/cartographie-mathematiques-ouvertes-v1/publication-evasion-post-entrainement-v1/strategie-cibles-et-feuille-de-route-publication-papier-d-v2.md`
   - `docs/notes/cartographie-mathematiques-ouvertes-v1/publication-evasion-post-entrainement-v1/strategie-cibles-et-feuille-de-route-publication-papier-d-v2.pdf`
3. **Mandat `GO-2026-11-24-05` (dépôt GitHub public compagnon de la note statique courte via Neon)** :
   - Prompt complet versé dans `demande-neon-preparation-depot-public-v1.md` (incluant les 6 corrections d'`Overfull \hbox` relevées par `pdflatex` et le toilettage recommandé par Carbon).

---

## 2. Feuille de route scientifique exacte à exécuter sur `papier-d/evasion-post-entrainement-v1` (`0 USD` CPU d'abord)

Suivre strictement les **4 briques théoriques + l'échelle empirique CPU** issues de la revue Carbon (`strategie-…-v2.md`) en visant **Atelier ICLR 2027 (février, non archival) $\to$ Piste principale NeurIPS 2027 (mai)** (ou **ICML 2027 *Position Paper Track*** fin janvier) :

1. **Théorème 1 étendu — Des mesures de Gibbs abstraites aux vrais algorithmes de post-entraînement** :
   - Comparer formellement :
     (a) `RS-SFT + RL` ($\pi_{\mathrm{A}}^{(\eta)} \propto \beta e^{\eta R}\pi_0$),
     (b) filtrage itéré sur $K$ époques ($\beta(\pi)^K$),
     (c) `KL-RL` en ligne ancré sur le modèle initial gelé $\pi_0$, dont le point fixe auto-cohérent non linéaire est :
         $$\pi^*(d\pi) \propto \pi_0(d\pi)\exp\!\left(\eta\,\frac{\beta(\pi)}{\mathbb{E}_{\pi^*}[\beta]}\big(R(\pi) - \bar{R}_{\mathrm{acc}}(\pi^*)\big)\right),$$
     (d) **`GRPO` / `RLOO` avec pénalité $-C$** sur groupes de $G$ trajectoires par prompt $x \sim \mathcal{D}$ (prouver comment la pénalité $-C$ sur $\Pi_{\mathrm{v}}$ abaisse la baseline de groupe et accélère le gradient relatif vers $\Pi_{\mathrm{f}}$),
     en formulant le *Dilemme Rejet–Pénalité* en termes de **risque résiduel en déploiement** (neutralisant l'objection de taille d'effet de la Table 3).
2. **Théorème 2 nouveau — Transition de phase continue par méthode de Laplace et barrière d'échantillons finis** :
   - Sous une densité continue $\pi_0(1-\beta \in du) \asymp u^{\gamma-1}du$ ($\gamma > 0$, sans atome en $\beta = 1$), démontrer par intégration de Laplace que le poids furtif sous l'Opérateur B vaut $\Gamma(\gamma)[\eta(\Delta R + C)]^{-\gamma}e^{\eta \Delta R}$ : **la barrière asymptotique s'effondre dès que le support de $\beta$ approche $1$ continûment**, ne survivant que sous un **trou spectral strict** $\operatorname{ess\,sup}_{\Pi_{\mathrm{tr}}}\beta < \beta_{\mathrm{h}}$, avec ralentissement polynomial en $\eta^{-\gamma}$.
   - Ajouter la transition d'accessibilité en batch fini $B$ sur $T$ pas lorsque $p_{\mathrm{f}} \ll (BT)^{-1}$ avec couplage de caractéristiques $\langle \phi_{\mathrm{v}}, \phi_{\mathrm{f}} \rangle$.
3. **Théorème 3 étendu — Robustesse du découplage hors boucle (R2) sous couplage positif borné** :
   - Borner explicitement la dégradation du moniteur d'audit $M_{\mathrm{audit}}$ en fonction de $\operatorname{Cov}_{\nu_0}(\beta_{\mathrm{loop}}, \beta_{\mathrm{audit}}) \le \varepsilon > 0$ ou de l'information mutuelle $I(M_{\mathrm{loop}}; M_{\mathrm{audit}})$.
4. **Théorème 4 nouveau — Élimination intégrale du plancher d'attaques rares (R3) par divergence de Rényi $D_\infty$ et hockey-stick** :
   - Sous $e^{D_\infty(P_{\mathrm{ord}} \| P_{\mathrm{trap}})} = \operatorname{ess\,sup}_x \frac{dP_{\mathrm{ord}}}{dP_{\mathrm{trap}}}(x) \le M < \infty$, démontrer $\tau_{\mathrm{trap}}(\pi) \ge M^{-1}\tau_{\mathrm{ord}}(\pi)$ et la suppression de **toute** triche ($\forall \tau_{\mathrm{ord}} > 0$) dès que $C > \frac{(1-\rho)M + \rho\varepsilon_{\mathrm{trap}}}{\rho(1-\varepsilon_{\mathrm{trap}})}\Delta R$.
5. **Diagrammes de phase 2D vectoriels & Simulation RL tabulaire / bandit neuronal (`0 USD`, CPU)** :
   - Remplacer les tableaux numériques par des figures vectorielles 2D en couleur dans les plans $(\Delta R, \eta)$ et $(C, \beta_{\mathrm{f}})$, et simuler `PPO` en ligne, `GRPO`, `Filtered-SFT` et l'équilibre de Gibbs théorique en régime $p_{\mathrm{v}} e^{\eta\Delta R} \gg p_{\mathrm{h}}$ ;
   - Préparer un devis GPU chiffré et contre-lu R2 (sur `Qwen-2.5-3B/7B`, *School of Reward Hacks* / tests unitaires cachés $M_{\mathrm{audit}}$) à soumettre à la mère et à Lazar avant tout lancement payant.
