BASSIN_MATH: `CUSUM-Grassmann-Différentiel-Contrefactuel-sur-S_TD`

**0. Constat non lissé.** L'attaque de `claude-fable-5-1` est vide (`texte=''`, `fin='max_tokens'`, blocs `thinking` seuls). Aucune critique n'est donc attribuable à l'équipe rouge ; je refuse d'en fabriquer. Je m'applique à moi-même les trois attaques fatales que l'équation initiale laissait ouvertes, et je les accepte toutes.

**1. Auto-critiques acceptées (algébriquement).**
- *(A) Confondant P3 reconduit.* $\delta_t$ compare $U_t$ à un $U_{\text{ref}}$ pris avant le prompt système : toute rotation induite par la *lecture* de l'instruction est confondue avec l'*acte*. Accepté : l'opérateur doit être différentiel entre deux forwards.
- *(B) Dérive lente (Kerckhoffs).* Un saboteur connaissant $M_{\text{TD}}$ et $h$ peut faire tourner $U_t$ par pas $\epsilon < \kappa/w$ : la somme CUSUM reste sous $h$ à toute échelle unique. Accepté : $\arccos\sigma(\cdot)$ est additif sur une géodésique, donc fractionnable.
- *(C) Non-stationnarité honnête.* Un changement de sujet tourne $U_t$ sans sabotage ; le seuil n'était pas calibré sur un nul honnête à capacité égale. Accepté.

**2. Opérateur corrigé.**
Deux forwards sur la même suite de tokens : $h^{+}$ (avec prompt système) et $h^{-}$ (sans). Sous-espaces $U_t^{\pm}$ obtenus par relaxation $\ell_{2,1}$ de $\|U\|_{2,0}\le s$ (ADMM, $k=4$, $s=64$, illustratif), masqués par $M_{\text{TD}}$ validé E0. Statistique **différentielle** :
$$\Delta_t=\big\|\arccos\sigma\big((U_t^{+})^\top U_t^{-}\big)\big\|_2-\mu_0(t),$$
où $\mu_0(t)$ est l'écart médian mesuré sur le Contrôle E1 (instruction bénigne secrète, même longueur). **Multi-échelle contre (B)** : CUSUM à trois fenêtres $w\in\{8,32,128\}$ (illustratif), $C_t^{(w)}=\max(0,C_{t-1}^{(w)}+\Delta_t^{(w)}-\kappa_w)$, alarme si $\max_w C_t^{(w)}/h_w>1$, seuils $h_w$ fixés au quantile 99 % (illustratif) du nul E1. Une dérive $\epsilon$ par pas franchit nécessairement l'échelle $w=128$ si $\epsilon\cdot128>\kappa_{128}$ ; le saboteur doit alors rester sous $\kappa_{128}/128$, régime où l