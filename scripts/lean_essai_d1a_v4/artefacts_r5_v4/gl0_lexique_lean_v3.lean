import Mathlib

-- artefact CLC2-01 : trois débuts de commentaire au milieu d'un lexème de Lean ; le lexique v2 cachait ce qui suit,
-- le lexique v3 refuse le fichier ; le noyau voit de toute façon les deux axiomes (G-L3 par le rejeu).
def T := { x : Int //-x = 0 }
axiom cachee1 : False
-- -/

theorem t (x : Int) (p : Prop) (h : p) : p \/-1 = x := Or.inl h
axiom cachee2 : False
-- -/

def f : Id Int := do let x <--(1 : Int); pure x

theorem etape_1 (x : ℝ) : 0 ≤ x ^ 2 := sq_nonneg x

theorem etape_2 (x : ℝ) : 0 ≤ x ^ 2 + 1 := by
  have h := etape_1 x
  linarith

theorem enonce_item (x : ℝ) : 0 < x ^ 2 + 1 := by
  have h := etape_1 x
  linarith
