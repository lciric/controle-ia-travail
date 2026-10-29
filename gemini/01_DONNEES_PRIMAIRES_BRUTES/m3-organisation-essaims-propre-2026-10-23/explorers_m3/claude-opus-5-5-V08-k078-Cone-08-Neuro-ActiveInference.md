BASSIN_MATH: Bascule Neuromodulatoire Yu-Dayan ACh/NE (BNYD)

LOI_PROPOSEE: $a_t=\arg\max_a \dfrac{\mathrm{IG}_a}{c_a}$ sous le régime $\mathcal{R}_t=\begin{cases}\text{EXPLOITER} & \mathrm{ACh}_t<\theta_A,\ \mathrm{NE}_t<\theta_N\\ \text{EXPLORER (spawn)} & \mathrm{ACh}_t\ge\theta_A\\ \text{RESET + RED-TEAM} & \mathrm{NE}_t\ge\theta_N\end{cases}$, avec $\mathrm{ACh}_t=\mathbb{E}_{q}[H(p(o\mid s))]$ (incertitude attendue) et $\mathrm{NE}_t=-\ln p(o_t\mid q_{t-1})-\mathrm{ACh}_t$ (incertitude inattendue).

**1. Mécanisme d'auto-organisation hors-poids**

Chaque agent $i$, de famille $f_i$, tient une croyance explicite $q_i(s)$ sur les affirmations du projet. Cette croyance est stockée en mémoire externe et non dans les poids.

- **Signal ACh.** `jev-1.14.0` fournit $p(o\mid s)$ à coût nul. Quand $\mathrm{ACh}$ est élevé, le modèle est incertain mais stable : l'essaim spawne un explorateur chargé d'interroger arXiv, Semantic Scholar ou Crossref.
- **Signal NE.** Quand $\mathrm{NE}$ est élevé, le monde contredit le modèle. L'essaim rabaisse alors la précision des agents concernés, $\gamma_i \leftarrow \gamma_i e^{-\mathrm{NE}}$, et spawne un démolisseur Red-Team.
- **Topologie.** Une arête $i\to j$ existe si $\mathrm{IG}_{j\mid i}>0$, c'est-à-dire si les prédictions de $j$ réduisent l'énergie libre de $i$.
- **Monoculture ou chimère.** Si la corrélation des erreurs de prédiction intra-famille $\rho_f$ dépasse $\rho^*$ (risque H4'), l'arête suivante est obligatoirement inter-famille. Sinon, la monoculture est conservée parce qu'elle coûte moins cher.
- **Budget.** L'essaim alloue $\arg\max \mathrm{IG}/c$ séparément dans deux pools : 100 USD pour Claude et 20 USD pour Gemini.
- **Dérive de consigne (H9).** La consigne $\pi_0$ sert d'a priori. Chaque délégation paie $\mathrm{KL}(\pi_k\Vert\pi_0)$.

**2. Fonction objectif et anti-Goodhart**

$$J=\sum_t\Big[\underbrace{\mathrm{IG}^{\text{ext}}_t}_{\text{vérifié API}}-\lambda\,\mathrm{KL}(\pi_k\Vert\pi_0)-\mu\,\bar\rho_{\text{err}}-\nu\,\mathbb{1}[\text{récitation}]\Big]\ \text{s.c.}\ \textstyle\sum c\le B$$

- **Gain d'information.** $\mathrm{IG}^{\text{ext}}$ ne compte que les prédictions prospectives, par exemple l'existence d'une citation ou d'un DOI, confirmées par les graphes bibliographiques. Il n'utilise jamais `jev` seul.
- **Rôle de `jev`.** `jev` sert uniquement de vraisemblance. Il est recalibré sur un lot témoin rotatif tenu secret.
- **Récitation.** Une affirmation est marquée comme récitée lorsque $p_{\text{param}}(\text{claim})$ est élevée alors qu'aucune source n'a été retrouvée.

**3. Duel décisif ($H_A \perp H_B$) à budget constant**

Trois bras, chacun avec 100 USD Claude, 20 USD Gemini et un ensemble de tâches identique :

- **A : BNYD.**
- **B : essaim fixe**, avec topologie et rôles figés.
- **C : contrôle négatif i.i.d.**, avec les mêmes nombre, types et familles de spawns que A, mais déclenchés aléatoirement.

Mesures, préenregistrées : précision vérifiée, calibration (ECE) et $\bar\rho_{\text{err}}$ entre agents.

- **$H_A$ :** la temporalité des déclenchements ACh/NE est causale, donc $A>C\ge B$.
- **$H_B$ :** seul le volume de diversité compte, donc $A\approx C$.

Chaque configuration est répétée sur 30 graines. Le test est une permutation stratifiée par tâche, avec $\alpha=0{,}01$ corrigé.

Le rejet de $H_B$ est la condition nécessaire et suffisante pour valider la loi.
