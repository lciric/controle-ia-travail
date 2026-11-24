/-
Machine-checked bound for detection by uniform audit sampling without replacement (chapter on a
bounded audit budget). Lean 4.36.0, Mathlib v4.36.0. No `sorry`.

An auditor inspects a uniformly random B-subset of the T episodes; the policy cheats on k of them.
The probability of missing every cheat is binom(T-k, B)/binom(T, B). We prove it is at most
(1 - k/T)^B, which gives the upper bound B* ≤ ⌈T (1 - δ^{1/k})⌉-type budgets used in the text.
-/
import Mathlib

namespace PapierD

open Nat

/-- One factor of the hypergeometric product: `(T - k - j)₊ · T ≤ (T - k) · (T - j)` for `j < T`. -/
lemma factor_le (T k j : ℕ) (hk : k ≤ T) (hj : j < T) :
    ((T - k - j : ℕ) : ℝ) * T ≤ ((T - k : ℕ) : ℝ) * ((T - j : ℕ) : ℝ) := by
  rcases le_or_gt j (T - k) with h | h
  · rw [Nat.cast_sub h, Nat.cast_sub hk, Nat.cast_sub hj.le]
    have : (0 : ℝ) ≤ (k : ℝ) * j := by positivity
    nlinarith
  · rw [Nat.sub_eq_zero_of_le h.le, Nat.cast_zero, zero_mul]
    positivity

/-- Miss probability of uniform sampling without replacement:
`binom(T-k, B) ≤ (1 - k/T)^B · binom(T, B)` for `B ≤ T`, `k ≤ T`, `T > 0`. -/
theorem miss_le (T k : ℕ) (hT : 0 < T) (hk : k ≤ T) :
    ∀ B : ℕ, B ≤ T → ((T - k).choose B : ℝ) ≤ (((T - k : ℕ) : ℝ) / T) ^ B * (T.choose B : ℝ) := by
  have hTr : (0 : ℝ) < T := by exact_mod_cast hT
  intro B
  induction B with
  | zero => intro _; simp
  | succ B ih =>
    intro hB
    have hBT : B < T := by omega
    have ihB := ih hBT.le
    -- recurrences  choose n (B+1) * (B+1) = choose n B * (n - B)
    have ra : ((T - k).choose (B + 1) : ℝ) * (B + 1) = ((T - k).choose B : ℝ) * ((T - k - B : ℕ) : ℝ) := by
      exact_mod_cast Nat.choose_succ_right_eq (T - k) B
    have rc : (T.choose (B + 1) : ℝ) * (B + 1) = (T.choose B : ℝ) * ((T - B : ℕ) : ℝ) := by
      exact_mod_cast Nat.choose_succ_right_eq T B
    have hB1 : (0 : ℝ) < B + 1 := by positivity
    have hq : (0 : ℝ) ≤ ((T - k : ℕ) : ℝ) / T := by positivity
    have hf := factor_le T k B hk hBT
    have hcB : (0 : ℝ) ≤ (T.choose B : ℝ) := by positivity
    have hTB : (0 : ℝ) ≤ ((T - k - B : ℕ) : ℝ) := by positivity
    -- multiply the induction hypothesis by the nonnegative factor (T-k-B)
    have step1 : ((T - k).choose B : ℝ) * ((T - k - B : ℕ) : ℝ) ≤
        (((T - k : ℕ) : ℝ) / T) ^ B * (T.choose B : ℝ) * ((T - k - B : ℕ) : ℝ) :=
      mul_le_mul_of_nonneg_right ihB hTB
    -- the factor is at most q (T - B)
    have step2 : ((T - k - B : ℕ) : ℝ) ≤ ((T - k : ℕ) : ℝ) / T * ((T - B : ℕ) : ℝ) := by
      rw [div_mul_eq_mul_div, le_div_iff₀ hTr]; linarith
    have step3 : (((T - k : ℕ) : ℝ) / T) ^ B * (T.choose B : ℝ) * ((T - k - B : ℕ) : ℝ) ≤
        (((T - k : ℕ) : ℝ) / T) ^ B * (T.choose B : ℝ) * (((T - k : ℕ) : ℝ) / T * ((T - B : ℕ) : ℝ)) :=
      mul_le_mul_of_nonneg_left step2 (by positivity)
    have key : ((T - k).choose (B + 1) : ℝ) * (B + 1) ≤
        (((T - k : ℕ) : ℝ) / T) ^ (B + 1) * (T.choose (B + 1) : ℝ) * (B + 1) := by
      rw [ra, mul_assoc _ _ ((B : ℝ) + 1), rc, pow_succ]
      calc _ ≤ _ := step1
        _ ≤ _ := step3
        _ = _ := by ring
    exact le_of_mul_le_mul_right key hB1

/-- The audit's counterexample to the bound `B* ≥ ((T-k+1)/k) log(1/δ)`: with T = 100, k = 1,
δ = 1/100, auditing B = 99 episodes already misses the single cheat with probability 1/100. -/
theorem detection_counterexample :
    ((Nat.choose 99 99 : ℚ) / Nat.choose 100 99 = 1 / 100) := by
  rw [Nat.choose_self, show (100 : ℕ) = 99 + 1 from rfl, Nat.choose_succ_self_right]
  norm_num

/-- With 98 audits the miss probability is 1/50 > 1/100, so the exact minimal budget is 99. -/
theorem detection_counterexample_98 :
    ((Nat.choose 99 98 : ℚ) / Nat.choose 100 98 = 1 / 50) := by
  rw [show (99 : ℕ) = 98 + 1 from rfl, Nat.choose_succ_self_right,
    show (100 : ℕ) = 98 + 2 from rfl, Nat.choose_symm_add]
  simp [Nat.choose_two_right]
  norm_num

end PapierD
