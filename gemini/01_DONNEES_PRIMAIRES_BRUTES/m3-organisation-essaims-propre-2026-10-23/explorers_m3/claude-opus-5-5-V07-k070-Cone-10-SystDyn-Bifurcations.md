BASSIN_MATH: Canal Hétérocline de Rabinovich à Quantité de Selle (CHR-QS)

LOI_PROPOSEE: ẋᵢ = xᵢ(σᵢ − Σⱼ ρᵢⱼxⱼ) + η, avec ρ asymétrique sur le cycle E→D→S→A→E. On définit ν = Πᵢ cᵢ/eᵢ, où eᵢ = σᵢ₊₁ − ρᵢ₊₁,ᵢσᵢ et cᵢ = ρᵢ₋₁,ᵢσᵢ − σᵢ₋₁. Le canal est stable si ν > 1. Au voisinage de ν = 1, une bifurcation de résonance se produit et déclenche la mutation topologique.

**1. Mécanisme d'auto-organisation hors-poids**

- **Rôles.** L'essaim compte quatre rôles : E (explorateur), D (démolisseur Red-Team), S (synthétiseur) et A (auditeur de consigne). xᵢ désigne la fraction du budget allouée au rôle i.
- **Compétition sans gagnant.** La dynamique de Lotka-Volterra asymétrique produit une séquence de selles. Le temps de séjour vaut Tᵢ ≈ eᵢ⁻¹ ln(1/η) : la division des tâches émerge de la dynamique, sans planificateur.
- **Apprentissage.** Les poids restent figés. Seuls σᵢ (gain marginal mesuré par jev-1.14.0) et ρᵢⱼ (inhibition, c'est-à-dire la redondance entre sorties) sont réestimés à chaque cycle.
- **Anti-H4'.** Soit κ_f la corrélation d'erreurs intra-famille estimée par jev. Elle pondère la contraction : cᵢ ← cᵢ(1 − κ_f).
- **Mutation topologique.** Si ν chute vers 1 et que κ_f > κ*, un nœud passe en famille croisée (chimère). Si ν chute sans corrélation élevée, on spawne un nœud E′ (exploration) ou D′ (démolition) sur le lien de plus faible eᵢ.
- **Anti-H9.** Le nœud A mesure la distance d(consigne₀, sortie) ; tout σᵢ est multiplié par exp(−λd).

**2. Fonction objectif et anti-Goodhart**

R = ΔQ_jev^holdout − α·|Q_jev^train − Q_jev^holdout| − β·(1 − V_DOI) − γ·κ̄ − μ·d,

sous la contrainte de budget C_Claude ≤ 100 et C_Gemini ≤ 20.

- **Sondes cachées.** Les sondes jev holdout sont tournantes et secrètes : l'écart train/holdout pénalise le sur-ajustement au juge.
- **Anti-récitation.** V_DOI est la fraction d'affirmations vérifiées via Crossref, Semantic Scholar ou arXiv. Toute citation absente des graphes est pénalisée.

**3. Duel décisif (H_A ⊥ H_B), à budget constant de 120 USD**

- **H_A :** CHR-QS adaptatif.
- **H_B₁ :** topologie fixe, avec rôles et allocations figés.
- **H_B₂ :** ensemble i.i.d. monoculturel par famille.
- **Contrôle négatif :** séquence de rôles permutée aléatoirement, avec la même distribution des temps de séjour. Si ce contrôle égale H_A, c'est l'allocation qui agit, et non l'ordre hétérocline.
- **Placebo :** ν gelé, sans bifurcation.
- **Mesures :** hypothèses vérifiées et nouvelles par dollar, κ̄ et dérive d, sur 30 tâches tirées au hasard, avec 5 graines chacune. Le test est un test de permutations apparié.
- **Prédiction falsifiable :** en faisant varier η (température d'injection), les temps de séjour Tᵢ doivent croître linéairement en ln(1/η), avec une pente 1/eᵢ. Une absence de loi logarithmique, ou H_A ≤ contrôle négatif, réfute CHR-QS.
