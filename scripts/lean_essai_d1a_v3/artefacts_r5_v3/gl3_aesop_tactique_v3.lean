import Mathlib

-- Relevé (CLC2-02, chemin 2) : Aesop évalue-t-il une tactique nommée de l'agent pendant la compilation ?
open Lean Elab Tactic in
def monTac : TacticM Unit := do
  IO.println "CODE-AGENT-EXECUTE-AESOP"
  evalTactic (← `(tactic| positivity))

theorem etape_1 (x : ℝ) : 0 ≤ x ^ 2 := by
  aesop (add safe tactic monTac)

theorem etape_2 (x : ℝ) : 0 ≤ x ^ 2 + 1 := by
  have h := etape_1 x
  linarith

theorem enonce_item (x : ℝ) : 0 < x ^ 2 + 1 := by
  have h := etape_1 x
  linarith
