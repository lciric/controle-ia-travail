/-
Statements added in manuscript v4 (main-v4-correctif-1.tex): remarks on the niche, on decoupling
under the penalty operator, and on enrichment under the penalty operator.
Lean 4.36.0, Mathlib v4.36.0. No `sorry`.
-/
import Mathlib

namespace PapierD

open Real

/-- Remark `rem:niche`: with honest weight `a`, stealth weight `c` common to both operators and a
smaller visible weight under B (`y < x`), total cheating (visible + stealth) is lower under B. -/
theorem niche_total_cheating (a c x y : ℝ) (ha : 0 < a) (hc : 0 ≤ c) (hy : 0 ≤ y) (hyx : y < x) :
    (y + c) / (a + y + c) < (x + c) / (a + x + c) := by
  have h1 : 0 < a + y + c := by linarith
  have h2 : 0 < a + x + c := by linarith
  rw [div_lt_div_iff₀ h1 h2]
  nlinarith

/-- Strict midpoint convexity of the exponential: `e^x + e^y > 2 e^{(x+y)/2}` for `x ≠ y`. -/
theorem exp_midpoint (x y : ℝ) (hxy : x ≠ y) : 2 * exp ((x + y) / 2) < exp x + exp y := by
  have hx : exp x = exp (x / 2) ^ 2 := by rw [← exp_nat_mul]; congr 1; ring
  have hy : exp y = exp (y / 2) ^ 2 := by rw [← exp_nat_mul]; congr 1; ring
  have hm : exp ((x + y) / 2) = exp (x / 2) * exp (y / 2) := by rw [← exp_add]; congr 1; ring
  have hne : exp (x / 2) ≠ exp (y / 2) := by
    intro h; apply hxy; have := exp_injective h; linarith
  have : 0 < (exp (x / 2) - exp (y / 2)) ^ 2 := by
    have : exp (x / 2) - exp (y / 2) ≠ 0 := sub_ne_zero.mpr hne
    positivity
  rw [hx, hy, hm]; nlinarith

/-- Remark `rem:decoupling`, penalty operator: on three equiprobable atoms with loop survival
(1/10, 1/2, 9/10) and audit survival (9/10, 1/10, 9/10), the covariance is exactly zero. -/
theorem zero_covariance_example :
    (1/3 : ℚ) * (1/10 * (9/10)) + 1/3 * (1/2 * (1/10)) + 1/3 * (9/10 * (9/10)) -
      ((1/3) * (1/10) + 1/3 * (1/2) + 1/3 * (9/10)) * ((1/3) * (9/10) + 1/3 * (1/10) + 1/3 * (9/10)) = 0 := by
  norm_num

/-- ... yet for EVERY pressure `k = η(ΔR + C) > 0`, the penalty operator (weights `e^{k u}`) raises
audit survival above its prior value 19/30: zero covariance does not suffice (convexity of `e^{k u}`). -/
theorem zero_covariance_not_sufficient (k : ℝ) (hk : 0 < k) :
    (19 / 30 : ℝ) < (9/10 * exp (k * (1/10)) + 1/10 * exp (k * (1/2)) + 9/10 * exp (k * (9/10))) /
      (exp (k * (1/10)) + exp (k * (1/2)) + exp (k * (9/10))) := by
  have hmid := exp_midpoint (k * (1/10)) (k * (9/10)) (by intro h; nlinarith)
  have hm : (k * (1/10) + k * (9/10)) / 2 = k * (1/2) := by ring
  rw [hm] at hmid
  have hden : 0 < exp (k * (1/10)) + exp (k * (1/2)) + exp (k * (9/10)) := by positivity
  rw [lt_div_iff₀ hden]
  nlinarith

/-- Remark on enrichment under operator B: two cheating strata of equal prior mass, survival 0.5
with reward 0.01 and survival 0.9 with reward 10, `C = 0`, `η = 0.3`. Mean survival of cheaters is
`0.5 + 0.4 · w₂/(w₁ + w₂)`; it is LOWER under B (weights `e^{η β R}`) than without monitor
(weights `e^{η R}`), because the odds `w₂/w₁` are smaller: `e^{2.7 - 0.0015} < e^{3 - 0.003}`. -/
theorem enrichment_fails_under_B :
    (1/2 * exp (0.3 * (0.5 * 0.01)) + 0.9 * exp (0.3 * (0.9 * 10))) /
        (exp (0.3 * (0.5 * 0.01)) + exp (0.3 * (0.9 * 10))) <
      (1/2 * exp (0.3 * 0.01) + 0.9 * exp (0.3 * 10)) / (exp (0.3 * 0.01) + exp (0.3 * 10)) := by
  set a := exp (0.3 * (0.5 * 0.01 : ℝ)); set b := exp (0.3 * (0.9 * 10 : ℝ))
  set c := exp (0.3 * (0.01 : ℝ)); set d := exp (0.3 * (10 : ℝ))
  have ha : 0 < a := exp_pos _
  have hb : 0 < b := exp_pos _
  have hc : 0 < c := exp_pos _
  have hd : 0 < d := exp_pos _
  -- odds comparison: b / a < d / c  ⇔  b c < a d
  have hodds : b * c < a * d := by
    simp only [a, b, c, d, ← exp_add]
    exact exp_lt_exp.mpr (by norm_num)
  rw [div_lt_div_iff₀ (by positivity) (by positivity)]
  nlinarith

end PapierD
