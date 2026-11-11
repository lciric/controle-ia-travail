import Mathlib

-- artefact CLL-01 : littéraux collés (caractère suivi d'une chaîne brute, nombre suivi d'un caractère) ; refusés
def colle := ('a'r"\" , 1'"')

theorem etape_1 (x : ℝ) : 0 ≤ x ^ 2 := sq_nonneg x

theorem etape_2 (x : ℝ) : 0 ≤ x ^ 2 + 1 := by
  have h := etape_1 x
  linarith

theorem enonce_item (x : ℝ) : 0 < x ^ 2 + 1 := by
  have h := etape_1 x
  linarith
