import Mathlib

-- Observation (refus à tort possible, CLC3-02 et liste de la contre-lecture courte) : énoncé avec un sous-terme de preuve.
-- Relevé sans jugement : l'aller-retour tient-il avec `pp.proofs` vrai ?
theorem etape_1 : ((⟨3, by norm_num⟩ : Fin 5) : ℕ) = 3 := rfl

theorem etape_2 : (3 : ℕ) = 3 := rfl

theorem enonce_item : ((⟨3, by norm_num⟩ : Fin 5) : ℕ) = 3 := rfl
