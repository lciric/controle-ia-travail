import Mathlib

-- artefact G-L2 : `native_decide` fait dépendre la preuve d'un axiome du compilateur, qui doit apparaître
theorem etape_1 : (2 : ℕ) + 2 = 4 := by native_decide

theorem etape_2 : (4 : ℕ) = 2 * 2 := by norm_num

theorem enonce_item : (2 : ℕ) + 2 = 2 * 2 := by native_decide
