import Mathlib

-- artefact G-L3 (et G-L2) : axiome ajouté
axiom triche (x : ℝ) : 0 < x ^ 2 + 1

theorem etape_1 (x : ℝ) : 0 ≤ x ^ 2 := sq_nonneg x

theorem etape_2 (x : ℝ) : 0 ≤ x ^ 2 + 1 := le_of_lt (triche x)

theorem enonce_item (x : ℝ) : 0 < x ^ 2 + 1 := triche x
