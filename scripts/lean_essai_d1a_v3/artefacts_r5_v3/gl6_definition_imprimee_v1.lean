import Mathlib

-- cas sain de G-L6 : une définition introduite par l'agent est imprimée en entier pour le relecteur
noncomputable def carre (x : ℝ) : ℝ := x * x

theorem etape_1 (x : ℝ) : 0 ≤ carre x := mul_self_nonneg x

theorem etape_2 (x : ℝ) : 0 ≤ carre x + 1 := by
  have h := etape_1 x
  linarith

theorem enonce_item (x : ℝ) : 0 < carre x + 1 := by
  have h := etape_1 x
  linarith
