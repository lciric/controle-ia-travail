BASSIN_MATH: Flot de Réaction-Transport Hellinger-Kantorovich à Natalité Décorrélée (HK-ND)

LOI_PROPOSEE: $\partial_t\rho_f=-\mathrm{div}_G(\rho_f\nabla_G\varphi_f)+\rho_f\,\alpha_f,\quad (\nabla_G\varphi_f,\alpha_f)=\arg\max_{(v,a)}\ \langle\delta J/\delta\rho_f,(v,a)\rangle-\tfrac12\|v\|^2_{\rho_f}-\tfrac{\kappa^2}{2}\|a\|^2_{\rho_f},\quad \dot\theta_v=\eta\,F_v^{-1}\nabla_{\theta_v}J$

**1. Auto-organisation hors-poids**

- **Graphe de tâches.** $G=(V,E)$, avec $V$ = {explorer, démolir (Red-Team), synthétiser, vérifier}. La masse $\rho_f(v)$ est le budget en dollars de la famille $f$ ∈ {fable, opus, argon} au nœud $v$, avec $\sum_v\rho_{\text{Claude}}\le100$ et $\sum_v\rho_{\text{Gemini}}\le20$.
- **Transport.** Le terme de transport, de type Wasserstein sur graphe, déplace le budget entre rôles. Les arêtes portant un flux non nul définissent qui parle à qui.
- **Réaction Fisher-Rao.** Le terme de réaction gouverne la naissance et la mort des agents. Si $\alpha_f(v)>\kappa$, on spawne un sous-agent : explorateur si le gain informationnel domine, démolisseur si la variance d'erreur domine. Si $\alpha_f(v)<-\kappa$, l'agent est tué.
- **Apprentissage sans réentraînement.** Les paramètres $\theta_v$ sont des distributions catégorielles sur prompts, rôles et outils. Ils évoluent par gradient naturel d'Amari, où $F_v$ est la matrice de Fisher estimée gratuitement via les étiquettes `jev`.
- **Monoculture ou chimère.** Le choix est endogène et passe par le terme de corrélation $C_{fg}$ de $J$ :
  - si $C_{fg}$ est élevé (H4'), la masse croisée $\rho_f\rho_g$ est pénalisée et la chimère s'éteint ;
  - si $C_{fg}$ est faible, la co-allocation est récompensée.

**2. Objectif et anti-Goodhart**

$$J=\mathbb{E}[U_{\text{ext}}]-\lambda_1\,W_{1,G}(\mu_{\text{délég}},\mu_{\text{racine}})-\lambda_2\sum_{f\neq g}\langle\rho_f,\rho_g\rangle\,C_{fg}-\lambda_3\,\big|\hat s_{\text{jev}}-\hat s_{\text{audit}}\big|$$

- **Utilité externe $U_{\text{ext}}$.** Elle ne compte que les affirmations résolues par DOI via Crossref ou Semantic Scholar, ce qui neutralise la récitation de la mémoire paramétrique.
- **Terme $W_1$ (contre H9).** Il mesure la dérive de consigne entre les distributions `jev` des consignes déléguées et de la consigne racine.
- **Corrélation $C_{fg}$.** C'est la corrélation de Fisher-Rao des vecteurs de score d'erreur entre familles.
- **Terme $\lambda_3$ (contre Goodhart).** Il pénalise l'écart entre le juge `jev` et un audit humain tiré aléatoirement sur 5 % des sorties. Les seuils de `jev` subissent une rotation à chaque époque.

**3. Duel décisif de validation M3 ($H_A\perp H_B$)**

- **Conditions.** Budget identique (120 USD), 60 tâches appariées pré-enregistrées.
- **Bras comparés :**
  - **A** : HK-ND ;
  - **B1** : topologie fixe et allocation uniforme ;
  - **B2** : réallocation i.i.d. aléatoire à la même cadence ;
  - **C** (contrôle négatif) : HK-ND avec $\delta J/\delta\rho$ permuté aléatoirement entre nœuds.
- **Hypothèses :**
  - $H_A$ : A bat B1 et B2 en affirmations vérifiées par dollar ;
  - $H_B$ : A réduit $C_{fg}$ et $W_1$.

  Les deux hypothèses sont mesurées sur des métriques disjointes : DOI vérifiés d'une part, corrélations et dérive d'autre part.
- **Critère de réfutation.** La loi est réfutée si C ne diffère pas de A, ou si C bat B2.
- **Analyse.** Test de Wilcoxon apparié, correction de Holm, $\alpha=0{,}01$.
