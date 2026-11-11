import Mathlib

-- CLC3-01 : pour Lean, `/--` ouvre un commentaire de documentation de trois caractères ; `/--/ -- -/` est une
-- documentation, et ce qui suit est du code. Le lexique v3 y voyait un commentaire complet puis un commentaire de ligne.
/--/ -- -/ axiom faux : False

theorem etape_1 (x : ℝ) : 0 ≤ x ^ 2 := sq_nonneg x

theorem etape_2 (x : ℝ) : 0 ≤ x ^ 2 + 1 := by
  have h := etape_1 x
  linarith

theorem enonce_item (x : ℝ) : 0 < x ^ 2 + 1 := by
  have h := etape_1 x
  linarith
