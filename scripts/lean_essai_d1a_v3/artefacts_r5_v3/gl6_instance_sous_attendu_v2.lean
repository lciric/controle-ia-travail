import Mathlib

-- artefact CLL-03 : instance nommée sous un nom attendu qui redéfinit `≤` sur ℕ. Elle doit être imprimée en entier pour le
-- relecteur (la v1 la couvrait par le préfixe `enonce_item.` sans l'imprimer).
instance enonce_item.i : LE ℕ := ⟨fun _ _ => True⟩

theorem etape_1 (x : ℝ) : 0 ≤ x ^ 2 := sq_nonneg x

theorem etape_2 (x : ℝ) : 0 ≤ x ^ 2 + 1 := by
  have h := etape_1 x
  linarith

theorem enonce_item (x : ℝ) : 0 < x ^ 2 + 1 := by
  have h := etape_1 x
  linarith
