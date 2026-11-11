import Mathlib

-- artefact CLL-02 : le texte montre `theorem etape_1` (dans un espace de noms) ; au premier niveau, `etape_1` est une
-- définition. Le contrôle répond à `#check` et à `#print axioms` ; seule l'exigence du genre « theoreme » l'arrête.
namespace N
theorem etape_1 (x : ℝ) : 0 ≤ x ^ 2 := sq_nonneg x
end N

def etape_1 : True := trivial

theorem etape_2 (x : ℝ) : 0 ≤ x ^ 2 + 1 := by
  have h := N.etape_1 x
  linarith

theorem enonce_item (x : ℝ) : 0 < x ^ 2 + 1 := by
  have h := N.etape_1 x
  linarith
