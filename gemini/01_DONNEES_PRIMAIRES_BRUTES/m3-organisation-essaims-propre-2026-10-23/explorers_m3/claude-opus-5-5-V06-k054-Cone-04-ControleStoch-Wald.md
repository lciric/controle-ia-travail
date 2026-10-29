BASSIN_MATH: Barrière de De Finetti à Sinistres Corrélés (BDF-SC)

LOI_PROPOSEE: Soit $X_t^f$ la réserve de famille $f$ (Claude ou Gemini), avec $dX_t^f=\mu_f\,dt+\sigma_f\,dW_t-dD_t^f-dJ_t^f$, où $D$ est la dépense d'exploration et $J$ le coût des échecs de vérification. L'essaim spawne un explorateur ssi $X_t^f\ge b^*(\hat\rho_t)$, avec $b^*=\arg\max_b\,\mathbb E\big[\int_0^{\tau_{ruine}}e^{-\delta t}\,dI_t\big]$. Il spawne un démolisseur ssi $S_t=\max(0,S_{t-1}+\ell_t-k)>h$.

1. **Auto-organisation hors-poids**
- **Budget et barrière.** Le budget est traité comme un surplus assurantiel, dont les « sinistres » sont les affirmations réfutées. Le problème de dividende optimal (contrôle singulier, équation HJB $\max(\mathcal L V-\delta V,\;1-V')=0$) donne une barrière $b^*$. Au-dessus de $b^*$, l'excédent finance des explorateurs. En dessous, seuls les vérificateurs agissent.
- **Filtrage de la corrélation.** Un filtre particulaire suit la corrélation latente $\rho$ des erreurs entre familles (risque $H4'$), à partir des désaccords mesurés par `jev`. Plus $\hat\rho$ est élevé, plus la barrière $b^*$ monte : les sinistres corrélés sont plus lourds.
- **Démolisseurs Red-Team.** Un CUSUM est appliqué sur $\ell_t$, l'écart entre la consigne racine et la sortie déléguée (embedding `jev`). Il détecte la dérive $H9$ et déclenche alors un démolisseur Red-Team.
- **Monoculture ou chimère.** Le choix est fait par Thompson sampling escompté (facteur $\gamma$), dans le contexte (type de tâche, $\hat\rho$). La topologie mute par réécriture des arêtes de délégation vers le bras gagnant.

2. **Objectif et anti-Goodhart**
$$R=\sum_c \mathbb 1[\Lambda_c\ge A]\,\mathbb 1[\mathrm{DOI}_c]-\lambda\,\hat\rho-\eta\,\mathrm{KL}(\pi_{jev}^{public}\,\|\,\pi_{jev}^{secret})$$
- $\Lambda_c$ est le rapport de vraisemblance d'un SPRT de Wald accumulé à travers les familles, avec $A=(1-\beta)/\alpha$.
- $\mathrm{DOI}_c$ exige une vérification de l'affirmation par Crossref ou Semantic Scholar, ce qui pénalise la récitation de la mémoire paramétrique.
- Des sondes secrètes et aléatoires de `jev` détectent la sur-optimisation du juge public (loi de Goodhart).

3. **Duel $H_A\perp H_B$**
- **Bras.** BDF-SC adaptatif, essaim à topologie fixe, et essaim i.i.d. à topologie aléatoire. Tous reçoivent un budget identique (100/20 USD) sur un corpus de tâches tenu secret.
- **Contrôle négatif.** BDF-SC avec labels `jev` permutés : l'avantage doit s'annuler.
- **Métrique.** Affirmations certifiées par dollar.
- **Décision.** Un SPRT apparié par tâche ($\alpha=\beta=0{,}05$) entre les bras s'arrête dès que $\Lambda$ franchit $A$ ou $B$.
- **Critère de validation.** $H_A$ (BDF-SC bat les deux témoins) est validée seulement si le placebo ne bat pas l'essaim fixe, si $\hat\rho$ prédit les échecs observés et si la barrière n'entraîne jamais la ruine.
