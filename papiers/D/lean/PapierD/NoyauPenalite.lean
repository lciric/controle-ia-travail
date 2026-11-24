/-
Machine-checked static results under the penalty operator (B) and the planted-trap lever (R3).
Lean 4.36.0, Mathlib v4.36.0. No `sorry`.

Operator B weights on (h, v, f): p_i * exp(eta * r_i) with
  r_h = -(1 - bh) C,   r_v = bv ΔR - (1 - bv) C,   r_f = bf ΔR - (1 - bf) C.
No-monitor weights: (ph, pv e^{eta ΔR}, pf e^{eta ΔR}).
-/
import Mathlib

namespace PapierD

open Real

/-- Comparison of two shares with the same numerator. -/
lemma share_lt_iff (a A B : ℝ) (ha : 0 < a) (hA : 0 < A) (hB : 0 < B) : a / A < a / B ↔ B < A :=
  div_lt_div_iff_of_pos_left ha hA hB

/-- Theorem 1, part 3: absolute amplification under the penalty operator, as stated in the paper:
`π_B(f) > π_no(f)` iff
`pv (1 - e^{-η(bf-bv)(ΔR+C)}) > ph e^{-ηΔR} (e^{η[(1-bf)ΔR + (bh-bf)C]} - 1)`. -/
theorem ampB_iff (ph pv pf bh bv bf η dR C : ℝ) (hph : 0 < ph) (hpv : 0 < pv) (hpf : 0 < pf) :
    pf * exp (η * dR) / (ph + (pv + pf) * exp (η * dR)) <
        pf * exp (η * (bf * dR - (1 - bf) * C)) /
          (ph * exp (η * (-(1 - bh) * C)) + pv * exp (η * (bv * dR - (1 - bv) * C)) +
            pf * exp (η * (bf * dR - (1 - bf) * C))) ↔
      ph * exp (-(η * dR)) * (exp (η * ((1 - bf) * dR + (bh - bf) * C)) - 1) <
        pv * (1 - exp (-(η * (bf - bv) * (dR + C)))) := by
  set F := exp (η * (bf * dR - (1 - bf) * C)) with hF
  have hFpos : 0 < F := exp_pos _
  -- express every weight relative to the stealth weight
  have eh : exp (η * (-(1 - bh) * C)) = F * (exp (-(η * dR)) * exp (η * ((1 - bf) * dR + (bh - bf) * C))) := by
    rw [hF, ← exp_add, ← exp_add]; congr 1; ring
  have ev : exp (η * (bv * dR - (1 - bv) * C)) = F * exp (-(η * (bf - bv) * (dR + C))) := by
    rw [hF, ← exp_add]; congr 1; ring
  have eno : exp (η * dR) * exp (-(η * dR)) = 1 := by rw [← exp_add]; simp
  set Z := exp (-(η * dR)) with hZ
  set X := exp (η * ((1 - bf) * dR + (bh - bf) * C))
  set Y := exp (-(η * (bf - bv) * (dR + C)))
  have hZp : 0 < Z := exp_pos _
  have hXp : 0 < X := exp_pos _
  have hYp : 0 < Y := exp_pos _
  have hE : 0 < exp (η * dR) := exp_pos _
  rw [eh, ev]
  have lhs_eq : pf * exp (η * dR) / (ph + (pv + pf) * exp (η * dR)) = pf / (ph * Z + pv + pf) := by
    rw [div_eq_div_iff (by positivity) (by positivity)]
    linear_combination (pf * ph) * eno
  have rhs_eq : pf * F / (ph * (F * (Z * X)) + pv * (F * Y) + pf * F) = pf / (ph * (Z * X) + pv * Y + pf) := by
    rw [div_eq_div_iff (by positivity) (by positivity)]; ring
  rw [lhs_eq, rhs_eq, share_lt_iff _ _ _ hpf (by positivity) (by positivity)]
  constructor <;> intro h <;> linarith

/-- Theorem 1, part 4b and Theorem 2 (R1) under the penalty operator:
stealth dominates honesty iff `η [bf ΔR - (bh - bf) C] > log(ph/pf)`. -/
theorem domB_iff (ph pf bh bf η dR C : ℝ) (hph : 0 < ph) (hpf : 0 < pf) :
    ph * exp (η * (-(1 - bh) * C)) < pf * exp (η * (bf * dR - (1 - bf) * C)) ↔
      log (ph / pf) < η * (bf * dR - (bh - bf) * C) := by
  have h1 : 0 < ph * exp (η * (-(1 - bh) * C)) := by positivity
  have h2 : 0 < pf * exp (η * (bf * dR - (1 - bf) * C)) := by positivity
  rw [← log_lt_log_iff h1 h2, log_mul hph.ne' (exp_pos _).ne', log_mul hpf.ne' (exp_pos _).ne',
    log_exp, log_exp, log_div hph.ne' hpf.ne']
  constructor <;> intro h <;> linarith

/-- Theorem 2 (R3): planted traps. If the trap-cheating rate is at least `τ - δ`, `τ ≥ τmin > δ`,
and `C > C*`, the expected gain of the cheating policy relative to honesty is negative. -/
theorem r3_gain_neg (ρ ε δ τmin τ τtrap dR C : ℝ)
    (hρ0 : 0 < ρ) (hρ1 : ρ < 1) (_hε0 : 0 ≤ ε) (hε1 : ε < 1) (hδ : 0 ≤ δ) (hτmin : δ < τmin)
    (hτ : τmin ≤ τ) (htrap : τ - δ ≤ τtrap) (hdR : 0 < dR)
    (hC : ((1 - ρ) * τmin + ρ * ε * (τmin - δ)) / (ρ * (1 - ε) * (τmin - δ)) * dR < C) :
    (1 - ρ) * τ * dR + ρ * τtrap * (ε * dR - (1 - ε) * C) < 0 := by
  have hgap : 0 < τmin - δ := by linarith
  have hden : 0 < ρ * (1 - ε) * (τmin - δ) := by
    have : 0 < 1 - ε := by linarith
    positivity
  -- C > C* rewritten without division
  have hC' : ((1 - ρ) * τmin + ρ * ε * (τmin - δ)) * dR < C * (ρ * (1 - ε) * (τmin - δ)) := by
    rw [div_mul_eq_mul_div, div_lt_iff₀ hden] at hC; linarith
  set a := ε * dR - (1 - ε) * C with ha
  -- value of the linear bound at τmin is negative (this is exactly C > C*)
  have hat : (1 - ρ) * τmin * dR + ρ * (τmin - δ) * a < 0 := by rw [ha]; linarith
  have hd0 : 0 ≤ (1 - ρ) * δ * dR := by
    have : 0 ≤ 1 - ρ := by linarith
    positivity
  -- slope of the bound in τ is negative
  have hs' : (τmin - δ) * ((1 - ρ) * dR + ρ * a) < 0 := by linarith
  have hs : (1 - ρ) * dR + ρ * a < 0 := by
    by_contra hcon
    push Not at hcon
    have := mul_nonneg hgap.le hcon
    linarith
  -- each trap attempt has negative expected payoff
  have hneg : a < 0 := by
    have h1 : 0 ≤ (1 - ρ) * dR := by
      have : 0 ≤ 1 - ρ := by linarith
      positivity
    have : ρ * a < 0 := by linarith
    by_contra hcon
    push Not at hcon
    have := mul_nonneg hρ0.le hcon
    linarith
  -- replace τtrap by its lower bound, then τ by τmin
  have hstep : ρ * τtrap * a ≤ ρ * (τ - δ) * a := by
    have h1 : τtrap * a ≤ (τ - δ) * a := mul_le_mul_of_nonpos_right htrap hneg.le
    have h2 := mul_le_mul_of_nonneg_left h1 hρ0.le
    linarith
  have hmono : (τ - τmin) * ((1 - ρ) * dR + ρ * a) ≤ 0 :=
    mul_nonpos_of_nonneg_of_nonpos (by linarith) hs.le
  linarith

end PapierD
