BASSIN_MATH: Région de Slepian-Wolf à Commutation de Willems (RSW-CW)

LOI_PROPOSEE: Un agent i reste actif tant que son taux conditionnel par dollar dépasse le prix courant μ : ρᵢ = L(Xᵢ | X₋ᵢ, S) / cᵢ ≥ μ. L est une longueur de code calculée par un compresseur PPM sur les preuves vérifiées Xᵢ, avec S l'information latérale (graphes bibliographiques, scores `jev`). μ est ajusté pour que la dépense cumulée Σcᵢ suive la trajectoire budgétaire (100 USD Claude, 20 USD Gemini). La topologie suit un mélange à commutation de Willems (fixed-share) sur les configurations τ : w_{t+1}(τ) ∝ (1−α)·w_t(τ)·2^{−ℓ_t(τ)} + (α/|T|)·Σ_{τ'} w_t(τ')·2^{−ℓ_t(τ')}.

1. **Auto-organisation hors-poids**
- **Coin de la région de Slepian-Wolf.** Chaque agent ne doit transmettre que son « bin », c'est-à-dire l'information non déductible des autres. On impose Rᵢ ≥ H(Xᵢ|X₋ᵢ) et ΣRᵢ ≥ H(X).
- **Qui parle à qui.** Une arête i→j est créée si L(Xⱼ) − L(Xⱼ|Xᵢ) > κ, autrement dit si i comprime réellement j.
- **Explorateur ou démolisseur.** Si L(X|S) croît, la frontière est encore inexplorée et l'on spawne un explorateur. Si une affirmation reste compressible sans preuve externe, soit L(claim|S) ≈ L(claim|∅), il s'agit d'une suspicion de récitation paramétrique et l'on spawne un démolisseur Red-Team.
- **Monoculture ou chimère (H4').** Deux agents de même famille dont la redondance algorithmique estimée dépasse le seuil, I(Xᵢ:Xⱼ) > θ, ont des erreurs corrélées. L'agent le moins rentable est alors basculé vers une autre famille.
- **Dérive de consigne (H9).** Toute sous-consigne vérifie L(c_k|c₀) ≤ δ. Sinon, elle est re-dérivée depuis c₀.
- **Mémoire et apprentissage.** L'apprentissage tient entièrement dans les poids de mélange w et les bins mémorisés.

2. **Objectif et anti-Goodhart**

J = Σ_claims 𝟙[vérifié par l'API] · (L(X₋|S) − L(X₋|S, claim)) − λ·Σcᵢ − β·Σ_{i<j} I(Xᵢ:Xⱼ), où X₋ désigne les preuves déjà acquises.

- **Garde-fou 1.** `jev` ne sert que d'information latérale au décodeur, jamais de récompense directe.
- **Garde-fou 2.** Ses invites sont tournées aléatoirement et un lot réservé est noté a posteriori.
- **Garde-fou 3.** Seul un gain de compression adossé à une source externe vérifiable compte.

3. **Duel décisif H_A ⟂ H_B**

Le protocole est préenregistré, à budget identique de 120 USD par bras, sur N = 40 questions et 5 graines.
- **Bras A :** RSW-CW complet.
- **Bras B :** topologie fixe (planificateur, deux travailleurs, critique).
- **Bras C :** agents i.i.d. avec vote majoritaire.
- **Contrôle négatif D :** RSW-CW avec des longueurs L permutées aléatoirement entre agents. La structure et la dépense sont identiques, mais le signal informationnel est détruit.

Les hypothèses sont formulées ainsi :
- **H_A :** l'adaptation informationnelle cause le gain, ce qui prédit A > D.
- **H_B :** la seule diversité des familles suffit, ce qui prédit A ≈ D > B, C.

Les critères de jugement sont :
- les affirmations vérifiées et nouvelles par dollar ;
- la corrélation des erreurs ρ entre agents ;
- le taux de dérive L(c_k|c₀).

L'analyse repose sur un test de permutation stratifié par question, avec correction de Holm. H_A est validée seulement si A > D et A > B, C avec p < 0,01, sans baisse du score sur le lot `jev` réservé.
