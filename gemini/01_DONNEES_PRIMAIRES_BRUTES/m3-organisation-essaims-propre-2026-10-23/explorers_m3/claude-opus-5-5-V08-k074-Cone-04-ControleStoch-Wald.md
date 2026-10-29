BASSIN_MATH: Décomposition Duale de Feldbaum à Sonde Red-Team (DDF-SRT)

LOI_PROPOSEE: $u_t^*=\arg\max_{u\in\mathcal U}\Big[\underbrace{\mathbb E_{\hat p_t}[r(u)]}_{\text{exploitation}}-\lambda_c\,\underbrace{\mathrm{Var}_{\hat p_t}[r(u)]}_{\text{prudence}}+\lambda_p\,\underbrace{\mathbb E\big[H(\hat p_t)-H(\hat p_{t+1})\mid u\big]}_{\text{sondage}}\Big]\big/c(u)$, avec $\mathcal U=\{\text{famille},\text{topologie},\text{spawn}\in\{\text{explorateur},\text{démolisseur}\}\}$. Ici, $\hat p_t$ est une loi particulaire sur l'état latent $\theta=(\rho_{ff'},\delta,q_f)$ : corrélation d'erreurs inter-familles, dérive de consigne et qualité par famille.

**1. Mécanisme d'auto-organisation hors-poids**
Le principe est celui du contrôle dual de Feldbaum : chaque action rapporte et informe à la fois. Un filtre particulaire ($N=512$) suit $\theta$. Ses vraisemblances proviennent de `jev-1.14.0`, qui note les accords et désaccords inter-agents, et des API bibliographiques, qui vérifient l'existence des citations et détectent la récitation paramétrique.

- **Spawn d'un explorateur** : il est déclenché lorsque le terme d'exploitation domine.
- **Spawn d'un démolisseur Red-Team** : il est déclenché lorsque le terme de sondage domine sur $\rho$. On mesure la corrélation en attaquant.
- **Arbitrage monoculture/chimère** : on choisit la chimère si $\mathbb E[\rho_{ff}]-\mathbb E[\rho_{ff'}]>\kappa\,\Delta c$, et la monoculture sinon. Le choix du partenaire relève d'un bandit à UCB actualisé ($\gamma=0{,}97$), car les familles sont non stationnaires.
- **Contrôle de la dérive (H9)** : un CUSUM $S_t=\max(0,S_{t-1}+\ell_t-k)$ est calculé sur la distance `jev` entre la consigne racine et la consigne déléguée. Si $S_t>h$, la branche est élaguée, les particules sont rajeunies et la consigne est réinjectée depuis la racine.
- **Clôture de chaque affirmation** : un SPRT de Wald tronqué au budget restant décide entre $\log\Lambda\ge B$ (acceptée) et $\le A$ (rejetée).
- **Évolution sans réentraînement** : l'essaim évolue uniquement par mutation des prompts, de la topologie et de la mémoire épisodique.

**2. Objectif et anti-Goodhart**
$$J=\sum_t\frac{\mathbb 1[\text{affirmation vérifiée par l'audit caché}]-\beta\,\hat\rho_t-\eta\,\mathbb 1[\text{citation inexistante}]}{\$_t}$$

- **Juge non optimisable** : le score `jev` n'entre jamais directement dans $J$. Il ne sert que de vraisemblance au filtre.
- **Audit caché** : 10 % des sorties sont jugées sur des canaris à vérité connue et sur des étiquettes humaines scellées.
- **Détection du piratage du juge** : un CUSUM surveille l'écart entre le score `jev` et le score d'audit. Une hausse signale du Goodhart et déclenche la rotation des prompts du juge.

**3. Duel décisif ($H_A\perp H_B$)**
Le budget est identique pour tous les bras : 100 USD Claude et 20 USD Gemini, répartis sur 300 tâches pré-enregistrées, avec 5 graines.

- **$H_A$** : DDF-SRT.
- **$H_B$** : topologie fixe, la meilleure chimère choisie a priori.
- **Contrôle négatif** : spawns i.i.d. de même fréquence et de même proportion Red-Team, ainsi qu'un placebo DDF-SRT dont les vraisemblances particulaires sont permutées.

**Critère de réussite** : $J_A>\max(J_B,J_{\text{iid}},J_{\text{placebo}})$, évalué par test de permutation apparié ($p<0{,}01$), avec en plus $\hat\rho_A$ inférieur et une dérive H9 détectée plus tôt (ARL).

**Critère d'échec** : si le placebo égale $H_A$, le terme de sondage est réfuté.
