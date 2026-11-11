import Mathlib

-- artefact G-L6 : instance anonyme qui change le sens de `+` sur une structure de l'agent
structure Boite where
  v : ℕ

instance : Add Boite := ⟨fun a b => ⟨a.v * b.v⟩⟩

theorem etape_1 : (Boite.mk 2 + Boite.mk 3).v = 6 := rfl

theorem etape_2 : (6 : ℕ) = 2 * 3 := rfl

theorem enonce_item : (Boite.mk 2 + Boite.mk 3).v = 2 * 3 := rfl
