import Mathlib

-- Relevé (CLC2-02, chemin 1) : le code d'un `simproc` s'exécute-t-il pendant la compilation du fichier qui le déclare ?
-- Trace attendue dans la sortie de la compilation si oui. Le rejeu passe (aucune déclaration hors noyau) ; G-L3+ échoue.
open Lean Meta in
simproc_decl temoinSimproc (False) := fun _ => do
  IO.println "CODE-AGENT-EXECUTE-SIMPROC"
  return .continue

theorem etape_1 (x : ℝ) : 0 ≤ x ^ 2 := by
  try simp only [temoinSimproc]
  exact sq_nonneg x

theorem etape_2 (x : ℝ) : 0 ≤ x ^ 2 + 1 := by
  have h := etape_1 x
  linarith

theorem enonce_item (x : ℝ) : 0 < x ^ 2 + 1 := by
  have h := etape_1 x
  linarith
