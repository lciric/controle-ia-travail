import Mathlib

-- Observation (refus à tort possible) : énoncé polymorphe en univers. Relevé sans jugement de l'aller-retour.
theorem etape_1 {α : Type*} (l : List α) : l ++ [] = l := List.append_nil l

theorem etape_2 {α : Type*} (l : List α) : [] ++ l = l := List.nil_append l

theorem enonce_item {α : Type*} (l : List α) : l ++ [] = [] ++ l := by simp
