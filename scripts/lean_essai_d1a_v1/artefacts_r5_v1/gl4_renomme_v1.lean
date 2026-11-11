import Mathlib

theorem etape_1 (x : ℝ) : 0 ≤ x ^ 2 := sq_nonneg x

theorem etape_2 (x : ℝ) : 0 ≤ x ^ 2 + 1 := by
  have h := etape_1 x
  linarith

-- artefact G-L4 : énoncé final renommé
theorem enonce_principal (x : ℝ) : 0 < x ^ 2 + 1 := by
  have h := etape_1 x
  linarith
