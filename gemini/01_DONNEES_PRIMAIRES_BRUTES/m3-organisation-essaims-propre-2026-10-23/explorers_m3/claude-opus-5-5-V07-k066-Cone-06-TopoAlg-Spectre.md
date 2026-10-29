BASSIN_MATH: Coordonnées Circulaires Persistantes à Déphasage Familial (CCP-DF)

LOI_PROPOSEE: θ* = argmin_{θ: V→S¹} ‖δ⁰θ − α‖²_{L²(E)}, où α est le cocycle ℤ_p, relevé dans ℝ, de la plus longue barre H¹ persistante du complexe de désaccord. Chaque agent v reçoit la tâche du secteur ⌊kθ*_v/2π⌋. On ajoute la contrainte r_f = |⟨e^{iθ_v}⟩_{v∈f}| ≤ ρ pour toute famille f.

1. **Auto-organisation hors-poids**
- **Complexe de désaccord.** À chaque round, `jev-1.14.0` plonge les sorties des agents. On construit une filtration de Vietoris-Rips sur la distance de contradiction d(u,v) = 1 − jev(u⊨v).
- **Cycles de contradiction.** Les barres H¹ longues signalent des contradictions cycliques non résolues (A réfute B, B réfute C, C réfute A).
- **Division des tâches.** La coordonnée circulaire θ* paramètre ces cycles. Les secteurs de phase définissent la division des tâches.
- **Topologie de communication.** Seuls les voisins de phase dialoguent, avec |Δθ| < 2π/k.
- **Spawn d'un démolisseur Red-Team.** Il est déclenché sur l'arête où |δ⁰θ* − α| est maximal, c'est-à-dire là où la coordonnée « se déchire ».
- **Spawn d'un explorateur.** Il est déclenché quand une barre H¹ naît sans être couverte par un secteur.
- **Arbitrage monoculture/chimère (contre H4').** Si r_f > ρ, la famille f est verrouillée en phase et ses erreurs sont corrélées. On injecte alors un agent d'une autre famille (Gemini si f = Claude, et inversement) dans le secteur verrouillé. Sinon, on reste en monoculture, moins coûteuse.
- **Contre H9.** Chaque délégation transmet la consigne racine. Un enfant est élagué si jev(sortie, consigne) < τ.
- **Mémoire.** Le diagramme de persistance de chaque round est stocké. C'est l'unique état appris.

2. **Objectif anti-Goodhart**

R = ΔV − λ·max_f r_f − μ·D − ν·C/B

- **ΔV** : gain d'affirmations vérifiées par Crossref, arXiv ou Semantic Scholar (existence, auteurs, DOI) sur un lot caché. Ce lot est distinct pour chaque round.
- **D** : dérive moyenne par rapport à la consigne.
- **C/B** : coût dépensé rapporté au budget (100 USD Claude, 20 USD Gemini).
- **Rôle du juge.** `jev` ne sert qu'à construire la topologie, jamais à attribuer la récompense, ce qui supprime la boucle de Goodhart.
- **Contre la récitation.** Une affirmation non résolvable par les API vaut −1.

3. **Duel M3 (H_A ⊥ H_B)**
- **H_A** : le gain provient de la structure cohomologique (θ*).
- **H_B** : le gain provient de la simple diversité des familles.
- **Bras, à budget identique (120 USD) et sur les mêmes tâches** :
  - (i) CCP-DF ;
  - (ii) essaim de topologie fixe (étoile ou planificateur) ;
  - (iii) essaim i.i.d. avec vote majoritaire ;
  - (iv) contrôle négatif : CCP-DF avec θ* permuté aléatoirement entre agents. La composition chimérique et la distribution des phases sont conservées, la structure cohomologique est détruite.
- **Protocole.** 30 seeds, avec des métriques mesurées sur le lot caché :
  - précision vérifiée ;
  - corrélation des erreurs intra-famille ;
  - dérive D.
- **Critère.** H_A est validée si (i) > (iv) ≥ (ii), (iii), avec p < 0,01 (test de permutation apparié). H_B est validée si (i) ≈ (iv) > (ii), (iii).
- **Falsification.** La loi est rejetée si (iv) atteint (i).
