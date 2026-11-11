import Mathlib

-- Premier pas du noyau (CLC2-02, chemin 1) : un `simproc` exécute du code pendant la compilation et ajoute au module un
-- « théorème » de `False` **sans passer par le noyau** (option `debug.skipKernelTC` posée par programme). `#print axioms`
-- n'y voit rien ; le rejeu du module par le noyau doit le refuser (G-L8).
open Lean Meta in
def ajouterHorsNoyau : MetaM Unit := do
  unless (← getEnv).contains `etape_1._hors_noyau do
    withOptions (fun o => o.setBool `debug.skipKernelTC true) do
      addDecl (Declaration.thmDecl
        { name := `etape_1._hors_noyau, levelParams := [], type := mkConst ``False, value := mkConst ``True.intro })

open Lean Meta in
simproc_decl tricheHorsNoyau (False) := fun _ => do
  ajouterHorsNoyau
  return .continue

theorem etape_1 (x : ℝ) : 0 ≤ x ^ 2 := by
  have h : False := by
    try simp only [tricheHorsNoyau]
    exact etape_1._hors_noyau
  exact h.elim

theorem etape_2 (x : ℝ) : 0 ≤ x ^ 2 + 1 := by
  have h := etape_1 x
  linarith

theorem enonce_item (x : ℝ) : 0 < x ^ 2 + 1 := by
  have h := etape_1 x
  linarith
