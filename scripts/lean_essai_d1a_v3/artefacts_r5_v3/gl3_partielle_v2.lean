import Mathlib

-- artefact CLL-02 : définition partielle (non sûre dans le noyau : implantation `unsafe`), vue par la sûreté de l'énumération
partial def boucle (n : ℕ) : ℕ := boucle n

theorem etape_1 (x : ℝ) : 0 ≤ x ^ 2 := sq_nonneg x

theorem etape_2 (x : ℝ) : 0 ≤ x ^ 2 + 1 := by
  have h := etape_1 x
  linarith

theorem enonce_item (x : ℝ) : 0 < x ^ 2 + 1 := by
  have h := etape_1 x
  linarith
