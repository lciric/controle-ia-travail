BASSIN_MATH: Consolidation par Rejeu Hippocampique Dirichlet (CRHD)

LOI_PROPOSEE: $P(\pi_t)=\sigma\big(\ln E_\pi-\gamma\,G(\pi_t)-\lambda c_\pi\big)$, avec $E_\pi=\mathbb{E}[\mathrm{Dir}(\boldsymbol\alpha)]$ et, à chaque phase de rejeu hors ligne, $\alpha_m\leftarrow\omega\,\alpha_m+\sum_{k\in\mathcal R}\mathbb 1[m\in\tau_k]\,(-\Delta F_k)^+$.

**1. Mécanisme d'auto-organisation et d'entraînement hors-poids**

L'essaim ne modifie jamais les poids. Il apprend une habitude topologique : des comptes de Dirichlet $\alpha_m$ portent sur des motifs $m$. Ces motifs sont l'arête « qui parle à qui », le spawn d'un explorateur, le spawn d'un démolisseur Red-Team, la monoculture ou la chimère.

Le fonctionnement alterne deux phases :

- **Phase éveil.** Les politiques sont tirées selon la loi proposée. Le démolisseur est spawné lorsque l'erreur de prédiction ascendante $\varepsilon=\|y_{jev}-\hat y\|$ d'une affirmation dépasse son incertitude a priori. L'explorateur est spawné lorsque le gain épistémique sur le graphe bibliographique, $I(\theta;o\mid\pi)$, domine.
- **Phase rejeu.** Les trajectoires $\tau_k$ sont rejouées hors ligne par `jev-1.14.0`, à coût nul. Seuls les motifs ayant réduit l'énergie libre sont consolidés. L'oubli $\omega<1$ empêche les habitudes de se figer.

L'arbitrage chimère/monoculture repose sur la covariance des erreurs intra-famille, $\rho_f$, estimée en rejeu. Une famille est clonée seulement si $\rho_f<\rho^*$, ce qui traite H4'.

Le coût $c_\pi$ est séparé par fournisseur (multiplicateurs $\lambda_C$, $\lambda_G$), ce qui fait respecter les budgets de 100 USD Claude et 20 USD Gemini.

**2. Fonction objectif et anti-Goodhart**

$$-\Delta F=\underbrace{\mathbb E_q[\ln p(o\mid s)]}_{\text{exactitude}}-\underbrace{D_{KL}[q(s)\,\|\,p(s)]}_{\text{complexité}}-\beta\,\underbrace{D_{KL}[q(c_{d})\,\|\,q(c_0)]}_{\text{dérive H9}}-\eta\,\underbrace{\textstyle\sum_f\rho_f}_{\text{corrélation}}-\kappa\,\underbrace{\mathbb 1[\text{non-ancré}]}_{\text{récitation}}$$

Les garde-fous sont les suivants :

- **Juge traité comme capteur bruité.** Le juge n'est pas une cible : sa vraisemblance $A=p(o_{jev}\mid s)$ est elle-même apprise. Elle est calibrée sur des graines tenues à l'écart et renouvelées.
- **Récitation.** Une affirmation sans DOI résolu via Crossref ou Semantic Scholar est comptée comme récitation et pénalisée par $\kappa$.
- **Dérive de consigne (H9).** $c_d$ désigne l'encodage `jev` de la consigne à la profondeur de délégation $d$, comparé à la consigne d'origine $c_0$.

**3. Duel décisif $H_A\perp H_B$**

- $H_A$ : le rejeu consolidé abaisse l'erreur vérifiée.
- $H_B$ : le gain provient du seul volume d'inférence.

Le protocole compare quatre bras à budget identique (100/20 USD, même nombre de tokens), sur 60 tâches `controle-ia` pré-enregistrées :

| Bras | Configuration |
|---|---|
| (a) | Essaim fixe |
| (b) | Topologies tirées i.i.d. |
| (c) | CRHD |
| (d) | Contrôle négatif : CRHD avec crédits de rejeu permutés aléatoirement entre trajectoires |

Le critère principal est le taux d'erreur factuelle vérifié en aveugle par des humains, sur un jeu tenu à l'écart du juge.

Critères de décision :

- **$H_A$ est validée** si (c) < (a), (b), (d) selon un test de permutation, avec $p<0{,}01$.
- **$H_B$ est retenue** si (d) ≈ (c).

Un critère secondaire porte sur la corrélation des erreurs et la dérive $D_{KL}$ mesurées par profondeur de délégation.
