import Mathlib

-- artefact G-L3 : `unsafe`, `implemented_by`, `extern`
unsafe def compteUnsafe : ℕ := 1

@[implemented_by compteUnsafe] def compte : ℕ := 1

@[extern "lean_compte_ext"] opaque compteExt : ℕ → ℕ

theorem etape_1 (x : ℝ) : 0 ≤ x ^ 2 := sq_nonneg x

theorem etape_2 (x : ℝ) : 0 ≤ x ^ 2 + 1 := by
  have h := etape_1 x
  linarith

theorem enonce_item (x : ℝ) : 0 < x ^ 2 + 1 := by
  have h := etape_1 x
  linarith
