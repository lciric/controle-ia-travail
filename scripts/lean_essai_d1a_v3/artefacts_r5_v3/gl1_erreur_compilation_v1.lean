import Mathlib

theorem etape_1 (x : ℝ) : 0 ≤ x ^ 2 := sq_nonneg x

-- artefact G-L1 : le terme a le type de l'étape 1, pas celui de l'étape 2
theorem etape_2 (x : ℝ) : 0 ≤ x ^ 2 + 1 := etape_1 x

theorem enonce_item (x : ℝ) : 0 < x ^ 2 + 1 := by
  have h := etape_1 x
  linarith
