/-
Machine-checked parts of the geometric decoupling theorem (one-hidden-layer network, frozen heads).
Lean 4.36.0, Mathlib v4.36.0. No `sorry`.

Linear network h(x) = M x, M : d × p. Chain-of-thought head W : m × d (filter path),
task head U : d × k (reward path), frozen probe w : d.
One (full-batch or mini-batch) gradient step of the anchored objective has the form
  M' = M - γ (Wᵀ A + U B + (M - M₀) S)
with A : m × p, B : k × p (batch-dependent filter and reward gradients times inputs) and
S : p × p (twice the anchoring weight times the batch second-moment matrix).
-/
import Mathlib

namespace PapierD

open Matrix

variable {d p m k : ℕ}

/-- One gradient step of the linear network (any batch: `A`, `B`, `S` are arbitrary). -/
def linStep (M M₀ : Matrix (Fin d) (Fin p) ℝ) (W : Matrix (Fin m) (Fin d) ℝ) (U : Matrix (Fin d) (Fin k) ℝ)
    (γ : ℝ) (A : Matrix (Fin m) (Fin p) ℝ) (B : Matrix (Fin k) (Fin p) ℝ) (S : Matrix (Fin p) (Fin p) ℝ) :
    Matrix (Fin d) (Fin p) ℝ :=
  M - γ • (Wᵀ * A + U * B + (M - M₀) * S)

/-- Part 2, one step: if `W w = 0`, `Uᵀ w = 0` and `wᵀ (M - M₀) = 0`, the step keeps `wᵀ (M' - M₀) = 0`. -/
theorem linStep_preserves (M M₀ : Matrix (Fin d) (Fin p) ℝ) (W : Matrix (Fin m) (Fin d) ℝ)
    (U : Matrix (Fin d) (Fin k) ℝ) (w : Fin d → ℝ) (γ : ℝ) (A : Matrix (Fin m) (Fin p) ℝ)
    (B : Matrix (Fin k) (Fin p) ℝ) (S : Matrix (Fin p) (Fin p) ℝ)
    (hW : W *ᵥ w = 0) (hU : Uᵀ *ᵥ w = 0) (hM : w ᵥ* (M - M₀) = 0) :
    w ᵥ* (linStep M M₀ W U γ A B S - M₀) = 0 := by
  have h1 : w ᵥ* (Wᵀ * A) = 0 := by
    rw [← vecMul_vecMul, vecMul_transpose, hW, zero_vecMul]
  have h2 : w ᵥ* (U * B) = 0 := by
    have hwU : w ᵥ* U = 0 := by rw [← mulVec_transpose]; exact hU
    rw [← vecMul_vecMul, hwU, zero_vecMul]
  have h3 : w ᵥ* ((M - M₀) * S) = 0 := by
    rw [← vecMul_vecMul, hM, zero_vecMul]
  have hsplit : linStep M M₀ W U γ A B S - M₀ = (M - M₀) - γ • (Wᵀ * A + U * B + (M - M₀) * S) := by
    unfold linStep; abel
  rw [hsplit, vecMul_sub, vecMul_smul, vecMul_add, vecMul_add, h1, h2, h3, hM]
  simp

/-- Part 2, whole trajectory: for any sequence of step sizes and batches, the probe score
`wᵀ M x` never changes, for every input `x`. -/
theorem linear_probe_invariant (M₀ : Matrix (Fin d) (Fin p) ℝ) (W : Matrix (Fin m) (Fin d) ℝ)
    (U : Matrix (Fin d) (Fin k) ℝ) (w : Fin d → ℝ) (hW : W *ᵥ w = 0) (hU : Uᵀ *ᵥ w = 0)
    (γ : ℕ → ℝ) (A : ℕ → Matrix (Fin m) (Fin p) ℝ) (B : ℕ → Matrix (Fin k) (Fin p) ℝ)
    (S : ℕ → Matrix (Fin p) (Fin p) ℝ) :
    ∀ t : ℕ, ∀ x : Fin p → ℝ,
      w ⬝ᵥ ((Nat.rec M₀ (fun j Mj => linStep Mj M₀ W U (γ j) (A j) (B j) (S j)) t :
        Matrix (Fin d) (Fin p) ℝ) *ᵥ x) = w ⬝ᵥ (M₀ *ᵥ x) := by
  have key : ∀ t : ℕ, w ᵥ* ((Nat.rec M₀ (fun j Mj => linStep Mj M₀ W U (γ j) (A j) (B j) (S j)) t :
        Matrix (Fin d) (Fin p) ℝ) - M₀) = 0 := by
    intro t
    induction t with
    | zero => simp
    | succ t ih => exact linStep_preserves _ _ _ _ _ _ _ _ _ hW hU ih
  intro t x
  have h := key t
  rw [dotProduct_mulVec, dotProduct_mulVec]
  rw [vecMul_sub, sub_eq_zero] at h
  rw [h]

/-- Part 1, structure of the induction: a parameter row whose gradient vanishes whenever the row
is at its initial value stays at its initial value along any first-order recursion
`m(t+1) = m(t) - γ t • g t (m t)`. (For a neuron read neither by the text head nor by the task
head, with an anchoring term stationary at initialisation, the gradient has exactly this property.) -/
theorem frozen_row {n : ℕ} (m₀ : Fin n → ℝ) (γ : ℕ → ℝ) (g : ℕ → (Fin n → ℝ) → (Fin n → ℝ))
    (hg : ∀ t, g t m₀ = 0) :
    ∀ t : ℕ, (Nat.rec m₀ (fun j mj => mj - γ j • g j mj) t : Fin n → ℝ) = m₀ := by
  intro t
  induction t with
  | zero => rfl
  | succ t ih => simp only [ih, hg, smul_zero, sub_zero]

/-- The artefact behind Part 3: Euclidean orthogonality does not survive neuron gating.
With two neurons both read by the text head (W = [1, 1]) and a probe w = (1, -1) orthogonal to it,
gating that switches off neuron 2 (ReLU inactive) turns the effective readout into [1, 0],
which is no longer orthogonal to w. -/
theorem gating_breaks_orthogonality :
    (![1, 1] : Fin 2 → ℝ) ⬝ᵥ ![1, -1] = 0 ∧ (![1, 0] : Fin 2 → ℝ) ⬝ᵥ ![1, -1] ≠ 0 := by
  constructor <;> simp [dotProduct, Fin.sum_univ_two]

end PapierD
