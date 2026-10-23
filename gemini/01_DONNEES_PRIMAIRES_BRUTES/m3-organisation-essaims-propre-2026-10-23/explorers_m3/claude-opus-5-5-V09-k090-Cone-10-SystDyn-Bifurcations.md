BASSIN_MATH: Pilotage On-Off au Blowout d'Ashwin-Ott (POBAO)

LOI_PROPOSEE: $\dot\mu = \eta\,(\lambda_\perp^\ast - \hat\lambda_\perp)$, avec $\hat\lambda_\perp=\frac1T\sum_t \log\frac{\|\delta^\perp_{t+1}\|}{\|\delta^\perp_t\|}$ et $\lambda_\perp^\ast = 0^-$. On spawne un agent si $\|\delta^\perp_t\|>\theta$ (bouffée intermittente) et on valide un résultat en phase laminaire.

**1. Mécanisme d'auto-organisation hors-poids**

- **Variété de synchronisation.** Chaque agent $i$ produit une sortie $x_i$, plongée dans l'espace des traits de `jev-1.14.0`. La variété invariante $\mathcal M=\{x_i=\bar x\}$ représente le consensus. L'écart $\delta^\perp=x-\bar x$ mesure la divergence transverse.
- **Diagnostic de corrélation (H4′).** $\hat\lambda_\perp \ll 0$ signale une monoculture sur-synchronisée, donc des erreurs corrélées. $\hat\lambda_\perp>0$ signale un éclatement, donc du bruit.
- **Paramètre de contrôle.** $\mu$ est la fraction chimérique (part de `gemini-4-argon` et mélange `fable`/`opus`), plafonnée à $20/120$ du budget, couplée à la température.
- **Régime visé.** L'essaim est maintenu juste avant la bifurcation de blowout, en intermittence on-off (bassins criblés).
- **Rôle des bouffées.** Une bouffée portant sur un fait déclenche un sous-agent explorateur, qui interroge arXiv, Semantic Scholar et Crossref. Une bouffée portant sur une inférence déclenche un démolisseur Red-Team.
- **Topologie.** Les arêtes de communication relient les paires dont la covariance transverse est maximale.
- **Dérive de consigne (H9).** Chaque délégation est traitée comme une application dont l'exposant transverse $\lambda_{H9}$ est mesuré par rapport à la consigne racine. Toute délégation avec $\lambda_{H9}>0$ est refusée.

**2. Fonction objectif et anti-Goodhart**

$$R = V_{ext} - \alpha\,|\hat\lambda_\perp-\lambda_\perp^\ast| - \beta\,C_{\$} - \gamma\,\big|S_{jev}-V_{ext}\big|$$

- $V_{ext}$ compte les affirmations vérifiées par les API bibliographiques et les falsifications réussies sur des tâches tenues à l'écart. Une citation introuvable vaut $-1$, ce qui pénalise la récitation de la mémoire paramétrique.
- `jev` ne sert qu'à mesurer la géométrie de l'essaim, jamais à le récompenser directement. Ses sondes sont tirées aléatoirement à chaque époque.
- Le terme $\gamma$ punit tout écart entre le score du juge et la vérité externe, ce qui neutralise la loi de Goodhart.
- $C_{\$}$ est le coût d'inférence dépensé.

**3. Duel décisif ($H_A \perp H_B$)**

- **Hypothèses.** $H_A$ : le gain provient de la rétroaction sur $\hat\lambda_\perp$. $H_B$ : le gain provient de la seule diversité chimérique.
- **Bras expérimentaux**, tous à budget identique (100 USD Claude et 20 USD Gemini) :
  - (a) POBAO ;
  - (b) essaim à topologie fixe ;
  - (c) ensemble i.i.d. ;
  - (d) contrôle négatif : trajectoire $\mu(t)$ de POBAO permutée temporellement, même histogramme de $\mu$ mais sans boucle de rétroaction.
- **Protocole.** 40 tâches, appariement par tâche, test de permutation préenregistré.
- **Métriques.** Affirmations vérifiées par dollar ; corrélation inter-agents des erreurs $\rho$.
- **Signature de bifurcation.** On balaie $\lambda_\perp^\ast\in\{-0.5,-0.1,0^-,+0.1\}$. $H_A$ prédit un pic de performance à $0^-$. $H_B$ prédit une performance plate en $\lambda_\perp^\ast$ et l'égalité entre (a) et (d).
- **Critère de réfutation.** $H_A$ est rejetée si (a) ne dépasse pas (d) avec $p<0.01$.
