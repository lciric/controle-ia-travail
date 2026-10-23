BASSIN_MATH: Hystérésis de Sethna-TAP à Mémoire de Point de Retour (HST-MPR)

LOI_PROPOSEE: $m_{ia}=\tanh\beta\big[f_{ia}+H(t)+\sum_j J_{ij}m_{ja}-\beta\,m_{ia}\sum_j J_{ij}^2(1-m_{ja}^2)\big]$, avec $J_{ij}=-\rho_{ij}^{\text{jev}}$, et désordre $R=\mathrm{std}(f)$ maintenu à $R_c$. L'agent $i$ prend la tâche $a$ si $m_{ia}>0$.

**1. Mécanisme d'auto-organisation hors-poids**
- **Spins et champs.** Chaque couple agent–tâche est un spin $s_{ia}=\pm1$ (prendre ou céder la tâche).
  - Le champ aléatoire $f_{ia}$ est l'affinité mesurée gratuitement par `jev-1.14.0`.
  - $J_{ij}$ est l'opposé de la corrélation d'erreurs entre $i$ et $j$. Ce couplage antiferromagnétique pénalise la redondance de poids (H4').
- **Terme d'Onsager.** Il retire à chaque agent l'écho de sa propre influence revenue par délégation, ce qui coupe la récitation et la dérive de consigne (H9).
- **Champ budgétaire.** $H(t)=H_0-\kappa\,(\text{USD consommés}/\text{USD alloués})$ est balayé lentement, séparément pour le budget Claude (100 USD) et le budget Gemini (20 USD).
- **Avalanches de Barkhausen.** Chaque basculement collectif de taille $S$ déclenche une mutation de topologie :
  - si $S>S^*$, on spawne un explorateur, car un front nouveau apparaît ;
  - si l'aire de la boucle d'hystérésis dépasse $A^*$, on spawne un démolisseur Red-Team, car la consigne est métastable.
- **Monoculture ou chimère (Parisi).** On mesure $P(q)$ sur les recouvrements des verdicts `jev` entre répliques d'une même famille.
  - Un pic unique à $q_{EA}\to1$ signale un effondrement réplique-symétrique : on injecte des agents d'une autre famille.
  - Un $P(q)$ large signale une brisure de symétrie des répliques (RSB) : on conserve la monoculture.
- **Mémoire hors-poids.** Seule la *mémoire de point de retour* est stockée, c'est-à-dire les états revisités. L'apprentissage consiste à ajuster $R\to R_c$, où les avalanches suivent $P(S)\sim S^{-3/2}$ (champ moyen).

**2. Fonction objectif et anti-Goodhart**

$$\mathcal{R}=\Delta V_{\text{holdout}}-\lambda\,\bar q_{EA}^{\text{intra}}-\mu\,|\partial_t\langle m\rangle_{\text{consigne}}|-\nu\,\text{USD}+\eta\,V_{\text{Crossref}}$$

- $\Delta V_{\text{holdout}}$ est noté par un sous-ensemble secret et tournant de grilles `jev`, que l'essaim n'observe jamais.
- $V_{\text{Crossref}}$ est la fraction de citations vérifiées par les API de graphes bibliographiques.
- Le terme d'Onsager interdit en outre de compter son propre écho comme un accord.

**3. Duel décisif ($H_A\perp H_B$)**

À budget constant (100/20 USD, coûts journalisés), sur 40 tâches et 5 graines :

| Bras | Configuration |
|---|---|
| (A) | HST-MPR |
| (B) | Topologie fixe |
| (C) | Agents i.i.d. |
| (N) | Contrôle négatif : même loi, mais $J$ permuté aléatoirement et terme d'Onsager supprimé |

- **$H_A$ (criticité).** $\mathcal{R}$ est maximal à $R=R_c$ et décroît de part et d'autre.
- **$H_B$ (diversité).** $\mathcal{R}$ croît de façon monotone avec la fraction chimérique.
- **Orthogonalisation.** On fait varier $R$ à fraction chimérique fixe, puis l'inverse.
- **Critères de validation.** HST-MPR est validée si les trois conditions suivantes sont réunies :
  - A bat B, C et N selon un test de Wilcoxon avec $p<0{,}01$ ;
  - N ne fait pas mieux que C ;
  - l'exposant ajusté vérifie $\tau\approx1{,}5\pm0{,}2$.
