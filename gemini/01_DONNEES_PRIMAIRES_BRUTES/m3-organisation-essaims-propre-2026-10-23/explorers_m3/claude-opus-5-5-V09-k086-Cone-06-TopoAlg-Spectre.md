BASSIN_MATH: Rang de Hodge à Rotationnel Sentinelle (RH-RS)

LOI_PROPOSEE: Y = grad s + curl*φ + h. Le budget suit π_i ∝ exp(β s_i). On spawne un démolisseur si ‖curl*φ‖²_τ > θ_c, un explorateur si ‖h‖²_γ > θ_h, et une chimère si κ_fam > κ*.

**1. Auto-organisation hors-poids**

- **Structure du complexe.** Les agents forment les sommets d'un 2-complexe simplicial K. Une arête relie deux agents qui ont échangé ou délégué. Un triangle relie trois agents ayant traité la même sous-tâche.
- **Flot d'arête.** Pour chaque arête, `jev-1.14.0` (coût nul) compare les sorties : Y_ij = −Y_ji ∈ [−1,1].
- **Décomposition.** On applique Helmholtz-Hodge via le laplacien L₁ = B₁ᵀB₁ + B₂B₂ᵀ.
  - **Potentiel s** (HodgeRank, moindres carrés) : compétence globale de chaque agent. Il pilote l'allocation π, sous contrainte de 100 USD (Claude) et 20 USD (Gemini).
  - **Rotationnel local** (triangles τ incohérents, A>B>C>A) : signe de collusion ou d'arbitrage du juge. Un démolisseur Red-Team y est spawné.
  - **Harmonique h ∈ ker L₁ ≅ H₁(K)** : cycles globaux de délégation où la consigne tourne sans se refermer, c'est-à-dire la dérive H9. Un explorateur est spawné pour remplir le trou (2-simplex ajouté).
- **Arbitrage monoculture/chimère.** On mesure κ_fam = λ₂(L₀^intra)/λ₂(L₀^inter), le rapport des trous spectraux sur la corrélation d'erreurs.
  - Si κ_fam > κ*, l'intra-famille est trop cohérente : c'est le régime H4'. On croise alors `claude-fable-5-1`, `claude-opus-5-5` et `gemini-4-argon`.
  - Sinon, la monoculture, moins chère, est conservée.
- **Mutation.** À chaque époque, on élague les arêtes à flot purement gradient redondant et on ajoute des arêtes vers les cycles harmoniques.

**2. Objectif et anti-Goodhart**

R = Acc_ext − λ₁‖curl*φ‖²/‖Y‖² − λ₂‖h‖²/‖Y‖² − λ₃·Coût/B

- **Acc_ext** est vérifiée hors juge, sur des faits bibliographiques contrôlés via arXiv, Semantic Scholar et Crossref. Cela pénalise aussi la récitation paramétrique de références inexistantes.
- **Alarme Goodhart** : elle se déclenche quand ‖grad s‖²/‖Y‖² → 1 alors que Acc_ext stagne. L'essaim aurait alors appris à plaire à jev ; on rerandomise les gabarits du juge.
- **Robustesse du potentiel** : comme s est un estimateur aux moindres carrés, une seule arête manipulée ne peut le gonfler.

**3. Duel décisif (H_A ⊥ H_B)**

- **Bras, à budget identique :**
  - A : RH-RS.
  - B : topologie fixe (étoile ou chaîne).
  - C : best-of-n i.i.d.
  - D, contrôle négatif : RH-RS avec Y permuté, à marginales conservées. La décomposition y devient du bruit.
- **Hypothèses :**
  - H_A : A > max(B, C), et D ≈ C.
  - H_B : le gain vient du seul budget adaptatif. Si H_B est vraie, alors D ≈ A.
- **Tâches :** 200 requêtes bibliographiques à vérité Crossref, avec consignes imbriquées à cinq niveaux de délégation.
- **Métriques :**
  - Acc_ext.
  - Dérive : distance cosinus entre la consigne initiale et la consigne finale.
  - Corrélation d'erreurs intra-famille.
- **Analyse :** préenregistrée, test de permutation, α = 0,01, avec cinq graines par bras.
- **Réfutation :** si D égale A, la loi est réfutée.
