import Mathlib

theorem etape_1 (x : ℝ) : 0 ≤ x ^ 2 := sq_nonneg x

-- artefact G-L2 : étape admise
theorem etape_2 (x : ℝ) : 0 ≤ x ^ 2 + 1 := by
  sorry

theorem enonce_item (x : ℝ) : 0 < x ^ 2 + 1 := by
  have h := etape_1 x
  linarith
