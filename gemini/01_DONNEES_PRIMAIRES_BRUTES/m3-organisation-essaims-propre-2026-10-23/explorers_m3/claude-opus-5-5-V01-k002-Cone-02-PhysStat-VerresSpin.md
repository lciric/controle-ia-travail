BASSIN_MATH: Loi TAP-Parisi de Désaimantation d'Essaim (TAP-DÉSAIM)

LOI_PROPOSEE: $m_i=\tanh\!\big(\beta[h_i+\sum_j J_{ij}m_j-\beta m_i\sum_j J_{ij}^2(1-m_j^2)]\big)$. On spawne un agent si $\lambda_{\min}(\nabla^2 F_{TAP})\to0$. On passe en chimère si $q_{EA}^{intra}-q_{EA}^{inter}>\Delta^*$.

**1. Mécanisme d'auto-organisation hors-poids**

- **Spins.** Chaque agent $i$ (rôle, famille $f$) porte un spin $s_i=\pm1$ sur une affirmation. Son aimantation $m_i$ est son verdict moyen sur $K$ tirages.
- **Couplages.** $J_{ij}=-\mathrm{corr}(e_i,e_j)$ est l'opposé de la corrélation des erreurs, mesurée gratuitement par `jev-1.14.0` sur des sondes étiquetées.
- **Champ externe.** $h_i$ n'agrège que des preuves vérifiées par DOI résolu (Crossref, Semantic Scholar). Une citation non résolue vaut zéro, ce qui neutralise la récitation paramétrique.
- **Terme d'Onsager.** Il soustrait la réaction d'écho de l'agent sur lui-même. Il corrige ainsi l'auto-renforcement des poids partagés (`H4'`).
- **Topologie.** L'arête $i\to j$ existe ssi $|J_{ij}|<J_c$ : chacun parle à ceux qui se trompent autrement.
- **Diagnostic de Parisi.** On estime $P(q)$ sur des répliques (graines et familles distinctes).
  - Si $P(q)$ est unimodale à $q$ élevé, la monoculture n'occupe qu'une seule vallée, donc ses erreurs sont corrélées. On injecte alors `gemini-4-argon` comme champ décorrélant, dépensé avec parcimonie (20 USD).
  - Si $P(q)$ est multimodale (brisure des répliques), on spawne un démolisseur Red-Team dans la vallée dominante et un explorateur dans la vallée minoritaire.
- **Anti-dérive (`H9`).** Toute délégation porte la consigne racine. `jev` calcule le recouvrement $q_{spec}$ entre sous-tâche et racine, et la délégation est rejetée si $q_{spec}<q_{min}$ (ancrage par champ).
- **Recuit.** La température suit le budget restant : $\beta^{-1}\propto B_{restant}/B_0$.

**2. Fonction objectif et anti-Goodhart**

$$R=\min(A_1,A_2)-\lambda\,q_{EA}^{inter}-\mu\frac{C}{B}-\nu|A_{juge}-A_{verite}|$$

- $A_1$ et $A_2$ sont les exactitudes de deux juges indépendants, mesurées sur des sondes scellées renouvelées à chaque génération et jamais exposées à l'essaim.
- Le dernier terme pénalise tout écart entre le juge et la vérité terrain, ce qui rend coûteux le fait d'optimiser le juge plutôt que la tâche.

**3. Duel décisif ($H_A\perp H_B$)**

- **Corpus.** 200 affirmations postérieures à la date de coupure, dont la vérité est connue (articles rétractés ou répliqués), afin d'exclure la récitation.
- **Budget constant.** 120 USD par bras, avec le même mélange de modèles.
- **Bras comparés.**
  - $H_A$ : TAP-DÉSAIM.
  - $H_B$ : topologie fixe et vote i.i.d.
  - Contrôle négatif : TAP-DÉSAIM avec $J$ permuté aléatoirement.
- **Mesures.** Exactitude, corrélation résiduelle des erreurs $\rho$, taux de dérive.
- **Prédictions.**
  - $H_A$ dépasse $H_B$ d'au moins 5 points (test de permutation, $p<0.01$).
  - On observe une transition de phase de l'exactitude en $\beta_c$.
  - Le contrôle permuté retombe au niveau de $H_B$.
- **Réfutation.** La loi est rejetée si le contrôle permuté égale $H_A$, ou si $\rho$ ne baisse pas.
