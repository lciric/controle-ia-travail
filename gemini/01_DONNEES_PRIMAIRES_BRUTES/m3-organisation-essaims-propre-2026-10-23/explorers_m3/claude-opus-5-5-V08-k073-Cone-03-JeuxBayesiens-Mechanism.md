BASSIN_MATH: Marché de Décision Chen-Kash à Persuasion Concurrente et Délégation Bornée (MDCK-PCDB)

LOI_PROPOSEE: $a_t\sim\pi_t,\ \pi_t(a)\ge\varepsilon$ ; $R_i=\dfrac{S_{Brier}\big(p_i(\cdot\mid a_t),y\big)-\bar S_{-f(i)}}{\pi_t(a_t)}$ ; $c_i\leftarrow c_i\,e^{\eta R_i}$ ; on lance un démolisseur si $\operatorname{cav}V(\mu_t)-V(\mu_t)>\kappa$ ; toute délégation $d$ doit vérifier $d\in D_\delta=\{d:\ \mathrm{jev}(d,\text{consigne}_0)\ge 1-\delta\}$.

**1. Mécanisme d'auto-organisation hors-poids**

- **Choix de topologie.** L'espace d'actions $A$ couvre les topologies possibles : monoculture Fable, monoculture Opus, monoculture Argon, chimère, graphe de parole, profondeur de délégation.
- **Marché de décision.** Chaque agent $i$ parie sur l'issue $y$ conditionnellement à chaque topologie, via une distribution $p_i(y\mid a)$. Le principal tire $a_t$ selon une règle stochastique $\pi_t\propto\exp(\beta\,\hat{\mathbb E}[y\mid a])$ à support plein. Ce support plein est la condition de Chen-Kash pour que le score conditionnel pondéré soit strictement propre : dire la vérité est alors optimal pour chaque agent.
- **Budget.** Les crédits $c_i$ déterminent l'allocation du budget, plafonné à 100 USD pour Claude et 20 USD pour Gemini.
- **Arbitrage monoculture/chimère.** La ligne de base $\bar S_{-f(i)}$ est calculée sur les autres familles de poids. Un agent qui ne fait que répéter sa famille obtient donc une récompense nulle, ce qui pénalise la corrélation d'erreurs (H4').
- **Explorateur ou Red-Team.** On applique la persuasion concurrente de Gentzkow-Kamenica. On lance un explorateur si l'entropie de $\mu_t$ est haute. On lance un démolisseur, issu obligatoirement d'une autre famille, si l'écart de concavification $\operatorname{cav}V-V$ dépasse le coût $\kappa$. Avec deux émetteurs de familles opposées, l'équilibre tend vers une révélation plus complète.
- **Dérive de consigne.** L'ensemble de délégation de Holmström $D_\delta$, vérifié par jev-1.14.0 sans coût, borne la dérive (H9).

**2. Fonction objectif et protection anti-Goodhart**

$$J=\sum_t\Big[\mathbb E_{\pi_t}R\Big]-\lambda\,\rho_{\text{err}}^{\text{intra-famille}}-\gamma\,\$_t$$

- **Vérité terrain hors juge.** L'issue $y$ n'est jamais produite par le juge. Elle provient d'énoncés vérifiables sur arXiv, Semantic Scholar ou Crossref : existence de références, chiffres et liens de citation.
- **Contre la récitation.** Les tâches ne portent que sur des articles postérieurs à la date de coupure des modèles.
- **Rôle limité du juge.** jev sert uniquement de contrainte (appartenance à $D_\delta$), jamais de récompense. Ce découplage empêche l'optimisation du juge.

**3. Duel décisif $H_A\perp H_B$**

- **Conditions communes.** Budget identique (120 USD) et 200 tâches post-coupure, avec des graines appariées.
- **Bras comparés :**
  - $H_A$ : MDCK-PCDB ;
  - $H_B$ : topologie chimérique fixe, réglée au préalable ;
  - $H_C$ : topologies tirées i.i.d. uniformément ;
  - contrôle négatif : MDCK avec $y$ permuté, ce qui conserve le coût mais détruit le signal.
- **Critère préenregistré.** $H_A$ doit avoir un Brier inférieur à celui de $H_B$ et de $H_C$ (bootstrap apparié, $p<0{,}01$), avec un $\rho_{\text{err}}$ plus faible. Le contrôle négatif ne doit pas faire mieux que $H_C$.
- **Réfutation.** La loi est réfutée si $H_A\le H_C$, ou si le contrôle négatif égale $H_A$.
