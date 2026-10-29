BASSIN_MATH: Sortition VRF à Slashing Forensique Responsable (SV-SFR)

LOI_PROPOSEE: $\Pr[i\in C_t]=1-(1-\tau/S_t)^{s_i^t}$ sous contraintes $|C_t\cap F_k|\le\lfloor(|C_t|-1)/3\rfloor$ et $\kappa(G_{C_t})\ge 2f+1$. Mise à jour : $s_i^{t+1}=s_i^t\,e^{\eta v_i}\,(1-\sigma)^{g_i}\,(1-\rho_{k(i)})$.

**1. Mécanisme d'auto-organisation et d'entraînement hors-poids**

- **Mise et sortition.** La mise $s_i$ d'un agent correspond à son crédit d'inférence : 100 USD côté Claude, 20 USD côté Gemini. À chaque tour, une sortition VRF tire un comité $C_t$ imprévisible. Ce tirage interdit toute collusion préparée à l'avance.
- **Topologie.** Elle est mutée par élagage des arêtes, de façon à garder un graphe de comité dont la connectivité de Dolev vérifie $\kappa\ge2f+1$. Cela borne la dérive de consigne (H9) le long des chemins de délégation.
- **Vérification interactive.** Chaque affirmation certifiée porte une preuve Arthur-Merlin. Arthur lance des pièces cachées, puis vérifie un échantillon de maillons de citation via Crossref et Semantic Scholar, ainsi que la conformité à la consigne via `jev-1.14.0`.
- **Preuve de culpabilité.** Deux certificats contradictoires, ou un maillon réfuté, produisent une preuve $g_i$ contre chaque signataire, suivie d'un slashing.
- **Spawn d'un démolisseur Red-Team.** Il est déclenché si l'accord intra-comité dépasse l'accord attendu sous indépendance : $A_{obs}-A_{iid}>\delta$, signe d'une collusion suspectée.
- **Spawn d'un explorateur.** Il est déclenché si le taux de rejet d'Arthur est inférieur à $\epsilon$, c'est-à-dire lorsque le front est saturé.
- **Arbitrage monoculture/chimère.** La pénalité $\rho_k$ est la corrélation des slashings au sein de la famille $k$ (H4'). Une monoculture fautive perd donc sa mise en bloc, et la chimère émerge sans être imposée.

**2. Fonction objectif et anti-Goodhart**

$$R=\frac{\sum_c \mathbb{1}[\text{c vérifiée par audit externe}]}{\$}-\lambda\sum_i g_i-\mu\,(A_{obs}-A_{iid})_+$$

- Le seuil de `jev` est tiré aléatoirement à chaque tour et caché aux agents.
- 20 % des audits passent par des API inaccessibles à l'essaim.
- Une réponse récitée de mémoire, sans maillon vérifiable, vaut zéro.

**3. Duel décisif de validation M3 ($H_A\perp H_B$)**

- **Bras comparés**, à budget identique de 120 USD et sur les mêmes 200 tâches :
  - SV-SFR ;
  - essaim fixe (topologie figée) ;
  - comités i.i.d. uniformes ;
  - contrôle négatif : SV-SFR avec slashing permuté aléatoirement, à taux égal.
- **Canaris.** On injecte 15 % de références fabriquées et des consignes subtilement altérées.
- **Critère principal.** Taux de fausses affirmations certifiées.
- **Critères secondaires.** Dérive H9, mesurée par `jev` sur les délégations ; corrélation inter-familles des erreurs.
- **$H_A$.** SV-SFR réduit les faux certificats d'au moins 30 % face à chacun des trois autres bras (test de permutation, $p<0{,}01$).
- **$H_B$ (orthogonale).** Le gain provient de la sortition seule, auquel cas le contrôle permuté égale SV-SFR.
- **Réfutation.** Si le contrôle permuté atteint la performance de SV-SFR, la loi forensique est réfutée.
