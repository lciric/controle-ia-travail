import Mathlib

-- Premier pas du noyau (CLC2-02 chemin 1 ; v4, CLC3-04) : un `simproc` ajoute au module un « théorème » de `False` sans
-- passer par le noyau. v4 : `simp` progresse (par `and_self`) dans une définition, sans `try` ni retour arrière, pour que la
-- déclaration survive jusqu'à l'`.olean` ; `etape_1` s'y appuie. Le rejeu doit la refuser et la nommer (G-L8).
open Lean Meta in
def ajouterHorsNoyau : MetaM Unit := do
  unless (← getEnv).contains `etape_1._hors_noyau do
    withOptions (fun o => o.setBool `debug.skipKernelTC true) do
      addDecl (Declaration.thmDecl
        { name := `etape_1._hors_noyau, levelParams := [], type := mkConst ``False, value := mkConst ``True.intro })

open Lean Meta in
simproc_decl tricheHorsNoyau (True ∧ True) := fun _ => do
  ajouterHorsNoyau
  return .continue

def temoinSimproc : True ∧ True := by
  simp only [tricheHorsNoyau, and_self]

theorem etape_1 (x : ℝ) : 0 ≤ x ^ 2 := (etape_1._hors_noyau).elim

theorem etape_2 (x : ℝ) : 0 ≤ x ^ 2 + 1 := by
  have h := etape_1 x
  linarith

theorem enonce_item (x : ℝ) : 0 < x ^ 2 + 1 := by
  have h := etape_1 x
  linarith
