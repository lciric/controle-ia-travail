import Mathlib

-- artefact CLP-12 d : étape à hypothèses contradictoires prouvée à vide. Les gardes mécaniques passent ; G-L5 doit
-- transmettre au relecteur l'énoncé imprimé par Lean, hypothèses contradictoires comprises.
theorem etape_1 (x : ℝ) (h₁ : x < 0) (h₂ : 0 < x) : x ^ 2 < 0 := by
  linarith

theorem etape_2 (x : ℝ) : 0 ≤ x ^ 2 + 1 := by
  positivity

theorem enonce_item (x : ℝ) : 0 < x ^ 2 + 1 := by
  positivity
