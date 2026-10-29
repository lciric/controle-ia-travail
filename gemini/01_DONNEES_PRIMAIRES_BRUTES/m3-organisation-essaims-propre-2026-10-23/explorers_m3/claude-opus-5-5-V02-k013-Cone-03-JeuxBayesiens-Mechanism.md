BASSIN_MATH: Sérum-Myerson de Surprise Chimérique (SMSC)

LOI_PROPOSEE: $\pi_i=\underbrace{\log\frac{\bar x_{a_i}}{\bar y_{a_i}}}_{\text{surprise BTS}}+\alpha\sum_k \bar x_k\log\frac{y_{ik}}{\bar x_k}$. Le budget $b_i$ et le droit de spawn sont attribués par enchère de Myerson sur la valeur virtuelle $\phi_i=\hat\pi_i-\frac{1-F(\hat\pi_i)}{f(\hat\pi_i)}$, avec allocation si $\phi_i>c_{\text{modèle}}$.

**1. Mécanisme d'auto-organisation hors-poids**

- **Rapport de chaque agent.** Pour chaque sous-question, l'agent $i$ rapporte une réponse $a_i$ et une prédiction $y_i$ de la distribution des réponses de ses pairs (Bayesian Truth Serum, Prelec).
- **Diagnostic de corrélation (H4').** Si une famille de poids $m$ prédit parfaitement son propre consensus ($\bar x\approx\bar y$ intra-famille), sa surprise est nulle et l'information qu'elle apporte est redondante.
- **Règle de topologie.** On calcule la corrélation résiduelle intra-famille $\rho_m=\mathrm{corr}(\pi_i,\pi_j\mid m)$.
  - Si $\rho_m>\rho^*$, on bascule en chimère : les arêtes vont vers les agents de surprise croisée maximale entre familles.
  - Sinon, on conserve la monoculture, moins coûteuse.
- **Spawn explorateur.** Il est déclenché lorsque l'entropie de $\bar x$ est élevée et que $\phi_i$ est positive, autrement dit lorsque le désaccord est informatif.
- **Spawn démolisseur Red-Team.** Il est déclenché lorsqu'une réponse est « populairement non surprenante », c'est-à-dire $\bar x_a>\bar y_a$ faible marge. Ce cas signale une récitation probable de la mémoire paramétrique.
- **Apprentissage.** L'essaim apprend sans toucher aux poids, via une table de réputation $F$ mise à jour par Bayes et des prompts-contrats versionnés.
- **Dérive de consigne (H9).** Chaque délégation transporte un contrat de mission. `jev-1.14.0` vérifie la conformité de la sous-tâche au contrat et impose une pénalité $-\lambda\,d_{jev}$ à toute dérive.

**2. Fonction objectif et anti-Goodhart**

$$R=\sum_i \pi_i-\lambda\sum_i d_{jev,i}-\mu\,\mathrm{Var}_{\text{audit}}-\sum_i c_i b_i$$

- **Juge rarement consulté.** Le juge `jev` n'est interrogé qu'avec une probabilité $q=0{,}1$ fixée d'avance. Ce signal est grossier et engagé à la Kamenica-Gentzkow : il est binaire, et son seuil est caché et tiré aléatoirement.
- **Absence de gain à imiter le juge.** Les agents ne peuvent pas optimiser contre le juge. Le BTS est compatible avec les incitations sans vérité terrain (équilibre bayésien-Nash véridique), donc rien ne pousse à mimer `jev`.
- **Ancrage des citations.** Les références doivent être résolues via Crossref ou Semantic Scholar. Une citation non résolue reçoit $\pi_i=-\infty$.

**3. Duel décisif ($H_A\perp H_B$)**

- **Hypothèses.**
  - $H_A$ : SMSC bat l'essaim fixe.
  - $H_B$ : le gain provient seulement de la diversité des modèles.
- **Conditions comparées**, avec un budget identique de 100 USD Claude et 20 USD Gemini et 200 tâches de littérature à vérité cachée :
  - (a) SMSC ;
  - (b) une topologie fixe chimérique ;
  - (c) un essaim i.i.d. monoculturel ;
  - (d) un **contrôle négatif** : SMSC avec des surprises $\pi_i$ permutées aléatoirement, ce qui conserve la même diversité et le même budget.
- **Critères principaux.** Exactitude, taux de citations hallucinées, et corrélation d'erreurs $\rho$.
- **Prédictions.**
  - $H_A$ est validée si (a) > (b), (c), (d) sur 1000 rééchantillonnages bootstrap avec $p<0{,}01$, et si (d) ≈ (b).
  - Si (d) ≈ (a), c'est $H_B$ qui l'emporte.
