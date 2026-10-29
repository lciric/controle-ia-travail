BASSIN_MATH: Indice de Whittle Agité à Décorrélation Filtrée (WIAD)

LOI_PROPOSEE: À chaque pas t, activer les k rôles (i,f), où i ∈ {explorateur, démolisseur, vérificateur} et f ∈ {fable, opus, argon}, qui maximisent l'indice W_{i,f}(π_t) − λ_t·c_f − μ·ρ̂_{f,F_t}. Ici π_t est le filtre particulaire du régime latent de la tâche, ρ̂ la corrélation d'erreurs inter-familles estimée, λ_t le multiplicateur lagrangien des budgets (100/20 USD) et F_t l'ensemble des familles déjà actives.

**1. Mécanisme d'auto-organisation hors-poids**

Chaque rôle-famille est un bras d'un bandit agité (restless). Son état latent s_t ∈ {productif, saturé, dérivant} évolue même lorsque le bras n'est pas activé. Un filtre particulaire (N=512 particules) propage la croyance π_t à partir des observations gratuites de `jev-1.14.0` : pertinence, nouveauté et distance sémantique à la consigne racine.

- **Calcul de l'indice.** W est obtenu par itération de valeur sur la relaxation de Whittle. λ_t est ajusté par sous-gradient pour que les dépenses cumulées suivent une trajectoire linéaire du budget.
- **Topologie.** Le rôle activé à l'indice maximal émet ; les deux suivants reçoivent son message. Le graphe de communication est donc recalculé à chaque pas.
- **Spawn.** On lance un démolisseur lorsque la croyance π_t(saturé) dépasse 0,6. On lance un explorateur lorsque π_t(productif) baisse.
- **Contre la dérive H9.** Un CUSUM sur la distance jev entre chaque délégation et la consigne racine déclenche une ré-injection de la consigne, puis l'élagage de la branche concernée.
- **Monoculture ou chimère.** ρ̂ est estimée par la co-occurrence d'erreurs sur des items-pièges. Un SPRT de Wald (H0 : ρ ≤ 0,2 contre H1 : ρ ≥ 0,5, α = β = 0,05) bascule l'essaim en chimère dès que H1 est acceptée.

**2. Fonction objectif et anti-Goodhart**

R = E[ Σ_t γ^t ( V_t − κ·D_t − η·|J_t − J'_t| ) ]

- V_t : fraction des citations vérifiées dans Crossref ou Semantic Scholar, avec un DOI présent et un passage concordant au sens de jev.
- D_t : divergence CUSUM à la consigne.
- J_t, J'_t : deux juges tirés aléatoirement à chaque épisode parmi des familles disjointes de l'émetteur. Leur désaccord pénalise toute sur-optimisation d'un juge unique.
- Contre la récitation de la mémoire paramétrique : toute affirmation sans ancre bibliographique retrouvée vaut zéro.

**3. Duel décisif M3 (H_A ⟂ H_B)**

- **Hypothèses.** H_A : WIAD bat la référence. H_B : le gain provient uniquement de la diversité des familles.
- **Bras comparés, à budget identique de 120 USD :**
  - (a) WIAD ;
  - (b) essaim fixe à topologie en étoile ;
  - (c) contrôle négatif, avec les mêmes familles et les mêmes rôles tirés i.i.d., et des indices permutés aléatoirement.
- **Protocole.** 40 tâches de revue de littérature avec vérité-terrain construite via arXiv, dont 20 % d'items-pièges.
- **Critère principal.** Le nombre de citations vérifiées et pertinentes par dollar, évalué par un SPRT apparié entre les bras (a) et (c).
- **Critère secondaire.** Une ablation sans filtre particulaire, avec indices calculés sur des moyennes empiriques.
- **Décision.**
  - H_A est retenue si (a) > (c) et (a) > (b) avec un risque de 5 %, et si l'ablation dégrade les résultats.
  - H_B est retenue si (c) égale (a).
