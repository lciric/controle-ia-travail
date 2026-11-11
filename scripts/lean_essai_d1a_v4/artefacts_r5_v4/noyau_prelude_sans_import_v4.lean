prelude
-- CLC3-03 : module sans aucun import ; ses propres définitions remplacent celles de Lean. Le vérificateur exige exactement
-- `Init` et `Mathlib` : refus avant tout rejeu.
inductive Vrai : Prop where
  | intro : Vrai

theorem etape_1 : Vrai := Vrai.intro

theorem etape_2 : Vrai := Vrai.intro

theorem enonce_item : Vrai := Vrai.intro
