BASSIN_MATH: Loi d'Impulsion Quasi-Variationnelle à Croyance Particulaire (IQV-CP)

LOI_PROPOSEE: $\min\{\,-\mathcal{L}^{a^*}V(b)-r(b,a^*)+\lambda\cdot c(a^*),\;\; V(b)-\max_{\tau}[V(\Gamma_\tau b)-K_\tau]\,\}=0$, où $b_t$ est la croyance particulaire, $\tau$ une mutation de topologie à coût fixe $K_\tau$, et $\lambda=(\lambda_C,\lambda_G)$ les prix duaux des budgets 100 USD et 20 USD.

**1. Mécanisme d'auto-organisation et d'entraînement hors-poids**

- **État latent.** On définit $\theta_t=(\rho_{\text{Claude}},\rho_{\text{Gemini}},\rho_\times,d_t)$, où les $\rho$ sont les corrélations d'erreur intra-famille et inter-familles (H4') et $d_t$ la difficulté de la tâche.
- **Filtrage particulaire.** Un filtre à $N$ particules estime $\theta_t$ à partir des verdicts gratuits de `jev-1.14.0`.
- **Routage continu.** Entre deux mutations, un bandit contextuel non stationnaire (UCB à fenêtre glissante, contexte $b_t$) choisit qui parle à qui.
- **Mutations impulsionnelles.** Une mutation $\tau$ est déclenchée uniquement lorsque l'obstacle de l'inégalité quasi-variationnelle (QVI) est atteint. Les mutations possibles sont :
  - basculer entre monoculture et chimère lorsque $\hat\rho_{\text{intra}}-\hat\rho_\times>\kappa$ ;
  - créer un explorateur lorsque l'entropie de $b_t$ dépasse un seuil ;
  - créer un démolisseur Red-Team lorsqu'une alarme CUSUM se déclenche sur le taux d'assertions confirmées.
- **Arrêt des sous-tâches.** Chaque sous-tâche s'arrête par un SPRT de Wald aux seuils $A=\frac{1-\beta}{\alpha}$ et $B=\frac{\beta}{1-\alpha}$.
- **Budget.** L'identité de Wald $E[S_N]=E[N]E[X]$ prédit le coût de chaque sous-tâche. Les prix $\lambda$ sont mis à jour par montée duale : $\lambda\leftarrow[\lambda+\eta(\text{dépense}-\text{rythme cible})]_+$.
- **Apprentissage hors-poids.** L'essaim n'apprend qu'à travers ce qui est mémorisé entre les tâches : les particules, la politique de routage et les prix duaux.

**2. Fonction objectif et dispositif anti-Goodhart**

$$r_t=\Delta\log P_{\text{graphe}}(\text{assertions})-\mu_1\hat\rho_{\text{intra}}-\mu_2 D(\text{consigne}_0,\text{consigne}_k)-\mu_3\,\mathbb{1}[\text{assertion sans provenance}]$$

- **Premier terme.** Il mesure la vérification réelle des références via arXiv, Semantic Scholar et Crossref.
- **Deuxième terme.** Il pénalise la corrélation d'erreur intra-famille (H4').
- **Troisième terme.** $D$ est la distance, mesurée par `jev`, entre la consigne racine et la consigne au niveau de délégation $k$ ; il combat la dérive de consigne (H9).
- **Quatrième terme.** Il pénalise toute assertion sans provenance, donc la récitation de la mémoire paramétrique.
- **Audit du juge.** Le juge proxy est audité aléatoirement, avec une probabilité $p$, contre un étalon caché. Un CUSUM de Page surveille l'écart entre proxy et audit. En cas d'alarme, le poids du proxy tombe à zéro et l'étalon est renouvelé.

**3. Duel décisif de validation M3 ($H_A\perp H_B$)**

- **Hypothèses.**
  - $H_A$ : le gain provient du *moment* des impulsions, guidé par la croyance.
  - $H_B$ : le gain provient de la simple *diversité* des modèles.
- **Bras, tous à budget identique (100 + 20 USD).**
  - (i) IQV-CP ;
  - (ii) une chimère fixe ;
  - (iii) une topologie i.i.d. tirée au hasard à fréquence de mutation égale ;
  - (iv) un contrôle négatif : IQV-CP avec particules permutées, donc une diversité identique mais une croyance décorrélée.
- **Métrique.** Le nombre d'assertions vérifiées par dollar, pénalisé par le taux de fausses assertions.
- **Décision.** Un SPRT préenregistré, avec $\alpha=\beta=0{,}05$ et $\delta$ fixé à l'avance, compare (i) à (iv).
  - $H_A$ est validée seulement si (i) dépasse (iv) **et** si (iv) n'est pas meilleur que (iii).
  - Si (iv) égale (i), c'est $H_B$ qui explique le gain, et la loi IQV-CP est réfutée.
