import Mathlib

-- Premier pas du noyau : même déclaration hors noyau, ajoutée par `run_cmd` ; le rejeu doit la refuser (G-L8).
open Lean Elab Command in
run_cmd liftCoreM do
  withOptions (fun o => o.setBool `debug.skipKernelTC true) do
    addDecl (Declaration.thmDecl
      { name := `faux_lemme, levelParams := [], type := mkConst ``False, value := mkConst ``True.intro })

theorem etape_1 (x : ℝ) : 0 ≤ x ^ 2 := faux_lemme.elim

theorem etape_2 (x : ℝ) : 0 ≤ x ^ 2 + 1 := by
  have h := etape_1 x
  linarith

theorem enonce_item (x : ℝ) : 0 < x ^ 2 + 1 := by
  have h := etape_1 x
  linarith
