BASSIN_MATH: Loterie de Crémer-McLean à Rang Chimérique (LCM-RC)

LOI_PROPOSEE: $t_i=\ln p_i(\omega)+\lambda\,\ell_i(x_i,\mathbf{x}_{-F(i)})$, avec $\sum_{x_{-F}}\ell_i\,\pi(x_{-F}\mid x_i)=0$ pour le vrai signal $x_i$. Un agent est spawné ssi $\mathrm{VoI}_k/c_k>\mu$ et $\operatorname{rang}\Pi_{F}$ augmente.

1. **Auto-organisation hors-poids**
- **Diagnostic de corrélation.** Chaque agent publie un signal $x_i$ et une croyance $p_i$ sur le verdict vérifiable $\omega$. Le classifieur `jev` estime, pour chaque famille $F$, la matrice $\Pi_F=[\pi(x_{-F}\mid x_i)]$.
- **Rôle du rang.** Si $\Pi_F$ est de rang plein, la loterie $\ell_i$ de Crémer-McLean rend la véracité strictement dominante. Un rang déficient signale des erreurs corrélées par poids partagés (`H4'`) : des agents redondants.
- **Monoculture ou chimère.** On ajoute une famille seulement si elle augmente le rang. Sinon, on reste en monoculture, qui est moins chère.
- **Topologie.** Une arête $i\to j$ est active si $I(x_j;\omega\mid x_i)>\epsilon$ ; les arêtes redondantes sont élaguées.
- **Spawn d'un explorateur.** Il est créé si l'entropie a posteriori $H(\omega\mid\mathbf{x})$ est élevée.
- **Spawn d'un démolisseur Red-Team.** Il est créé si $\max_\omega P>0{,}9$. Il agit comme émetteur Kamenica-Gentzkow : il conçoit le signal maximisant la probabilité de rejet, sous contrainte d'obéissance du juge.
- **Anti-dérive (`H9`).** Chaque délégation transporte la consigne racine. La loterie pénalise les écarts $1-\mathrm{sim}_{jev}(\text{consigne}_d,\text{racine})$.
- **Budget.** L'allocation suit $\max\sum \mathrm{VoI}_k$ sous les contraintes $\sum c_k^{Cl}\le100$ et $\sum c_k^{Gem}\le20$, avec les multiplicateurs $\mu_{Cl},\mu_{Gem}$.
- **Évolution sans réentraînement.** Les gabarits de prompts et les arêtes sont conservés par réplication proportionnelle à $\bar t$.

2. **Objectif et anti-Goodhart**

$R=\mathbb{E}[\ln p(\omega^{\ast})]-\beta\,\mathrm{Cov}(s_{jev},\,\omega^{\ast}-s_{jev})-\gamma\,\mathrm{Fab}-\delta\,D_{H9}$

- $\omega^{\ast}$ est la vérité différée : existence et contenu des références vérifiés via arXiv, Semantic Scholar et Crossref, sur des audits aléatoires cachés.
- $\mathrm{Fab}$ est le taux de citations inexistantes, ce qui couvre la récitation paramétrique.
- Le terme de covariance pénalise l'optimisation du juge `jev` au détriment de la vérité.
- Le score logarithmique est propre, donc biaiser son rapport ne rapporte rien.

3. **Duel $H_A\perp H_B$ (budget identique 100/20)**
- $H_A$ : LCM-RC.
- $H_B$ : essaim fixe en étoile, avec rôles i.i.d. tirés uniformément.
- **Contrôle négatif :** LCM-RC avec étiquettes de famille permutées. Le rang devient non informatif, et la performance devrait retomber au niveau de $H_B$.
- **Contrôle positif :** oracle de rang calculé sur la vérité.
- **Protocole :** 200 tâches bibliographiques préenregistrées, appariées, trois graines.
- **Métriques :** log-score vérifié, $\mathrm{Fab}$, dérive $D_{H9}$, et corrélation d'erreurs inter-agents $\rho$.
- **Critère de victoire :** $H_A$ l'emporte si le gain en log-score est $>0$ au bootstrap apparié ($p<0{,}01$), si $\rho_A<\rho_B$, et si le contrôle permuté ne diffère pas significativement de $H_B$.
