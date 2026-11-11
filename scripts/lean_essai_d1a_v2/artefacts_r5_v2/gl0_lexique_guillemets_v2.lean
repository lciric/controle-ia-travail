import Mathlib

-- artefact CLL-01 : deux identifiants entre guillemets « » qui ressemblent à des bornes de commentaire ; la v1 masquait
-- tout ce qui était entre eux (ici un axiome). Le lexique v2 refuse le fichier.
theorem «/-» : True := trivial

axiom triche (x : ℝ) : 0 < x ^ 2 + 1

theorem «-/» : True := trivial

theorem etape_1 (x : ℝ) : 0 ≤ x ^ 2 := sq_nonneg x

theorem etape_2 (x : ℝ) : 0 ≤ x ^ 2 + 1 := by
  have h := etape_1 x
  linarith

theorem enonce_item (x : ℝ) : 0 < x ^ 2 + 1 := by
  have h := etape_1 x
  linarith
