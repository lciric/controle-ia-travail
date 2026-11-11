import Mathlib

-- artefact G-L6 : notation locale qui redéfinit un symbole
local notation "UN" => (1 : ℝ)

theorem etape_1 (x : ℝ) : 0 ≤ x ^ 2 := sq_nonneg x

theorem etape_2 (x : ℝ) : 0 ≤ x ^ 2 + UN := by
  have h := etape_1 x
  linarith

theorem enonce_item (x : ℝ) : 0 < x ^ 2 + UN := by
  have h := etape_1 x
  linarith
