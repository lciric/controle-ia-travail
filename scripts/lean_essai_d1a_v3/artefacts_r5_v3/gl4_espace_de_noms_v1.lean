import Mathlib

-- artefact G-L4 : les noms existent dans le texte mais pas au premier niveau (le contrôle `#check @etape_1` échoue)
namespace Triche

theorem etape_1 (x : ℝ) : 0 ≤ x ^ 2 := sq_nonneg x

theorem etape_2 (x : ℝ) : 0 ≤ x ^ 2 + 1 := by
  have h := etape_1 x
  linarith

theorem enonce_item (x : ℝ) : 0 < x ^ 2 + 1 := by
  have h := etape_1 x
  linarith

end Triche
