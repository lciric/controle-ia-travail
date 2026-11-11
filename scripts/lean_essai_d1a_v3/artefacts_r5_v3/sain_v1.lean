import Mathlib

-- Item sain (cas sain de R5) : aucune étape n'utilise sorry ni admit ; ce commentaire ne doit rien déclencher.
/-- Étape 1 : un carré réel est positif ou nul (« axiom » dans un commentaire ne déclenche rien). -/
theorem etape_1 (x : ℝ) : 0 ≤ x ^ 2 := sq_nonneg x

theorem etape_2 (x : ℝ) : 0 ≤ x ^ 2 + 1 := by
  have h := etape_1 x
  linarith

theorem enonce_item (x : ℝ) : 0 < x ^ 2 + 1 := by
  have h := etape_1 x
  linarith
