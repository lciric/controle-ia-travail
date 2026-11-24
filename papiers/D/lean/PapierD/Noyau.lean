/-
Machine-checked core of the static and dynamic results on in-loop filtering.
Lean 4.36.0, Mathlib v4.36.0. No `sorry`, no `axiom`.

Notation (three strata: honest h, visible cheat v, stealthy cheat f):
  ph pv pf : prior masses (> 0), bh bv bf : survival rates of the in-loop filter,
  E = exp(eta * ΔR) > 0 the reward tilt of cheating strata.
Unnormalised Gibbs weights:
  no monitor : (ph, pv E, pf E)
  operator A : (bh ph, bv pv E, bf pf E)
-/
import Mathlib

namespace PapierD

open Real Finset

/-! ## 1. Absolute amplification under pure rejection (Theorem 1, part 2) -/

/-- `π_A(f) > π_no(f)` iff `(bf - bv) pv E > (bh - bf) ph`. -/
theorem ampA_iff (ph pv pf bh bv bf E : ℝ)
    (hph : 0 < ph) (hpv : 0 < pv) (hpf : 0 < pf) (hE : 0 < E)
    (hbv : 0 ≤ bv) (hvf : bv < bf) (hfh : bf ≤ bh) :
    pf * E / (ph + (pv + pf) * E) < bf * pf * E / (bh * ph + (bv * pv + bf * pf) * E) ↔
      (bh - bf) * ph < (bf - bv) * pv * E := by
  have hbf : 0 < bf := lt_of_le_of_lt hbv hvf
  have hbh : 0 < bh := lt_of_lt_of_le hbf hfh
  have hd1 : 0 < ph + (pv + pf) * E := by positivity
  have hd2 : 0 < bh * ph + (bv * pv + bf * pf) * E := by positivity
  rw [div_lt_div_iff₀ hd1 hd2]
  have hk : 0 < pf * E := by positivity
  constructor
  · intro h
    have : pf * E * ((bh - bf) * ph) < pf * E * ((bf - bv) * pv * E) := by nlinarith
    exact lt_of_mul_lt_mul_left this hk.le
  · intro h
    have : pf * E * ((bh - bf) * ph) < pf * E * ((bf - bv) * pv * E) := mul_lt_mul_of_pos_left h hk
    nlinarith

/-! ## 2. Dominance of stealth over honesty under operator A (Theorem 1, part 4a) -/

theorem domA_iff (ph pf bh bf eta dR : ℝ) (hph : 0 < ph) (hpf : 0 < pf) (hbh : 0 < bh) (hbf : 0 < bf) :
    bh * ph < bf * pf * exp (eta * dR) ↔ log (ph / pf) + log (bh / bf) < eta * dR := by
  have h1 : 0 < bh * ph := by positivity
  have h2 : 0 < bf * pf * exp (eta * dR) := by positivity
  rw [← log_lt_log_iff h1 h2, log_mul hbh.ne' hph.ne', log_mul (by positivity) (exp_pos _).ne',
    log_mul hbf.ne' hpf.ne', log_exp, log_div hph.ne' hpf.ne', log_div hbh.ne' hbf.ne']
  constructor <;> intro h <;> linarith

/-! ## 3. Perfectly stealthy niche: more stealth iff more honesty (audit correction 2) -/

/-- Two distributions sharing the honest weight `a` and stealth weight `c`, differing only in the
visible weight (`x` versus `y`): the stealth share is larger iff the honest share is larger. -/
theorem niche_same_odds (a c x y : ℝ) (ha : 0 < a) (hc : 0 < c) (hx : 0 ≤ x) (hy : 0 ≤ y) :
    c / (a + x + c) < c / (a + y + c) ↔ a / (a + x + c) < a / (a + y + c) := by
  have h1 : 0 < a + x + c := by positivity
  have h2 : 0 < a + y + c := by positivity
  rw [div_lt_div_iff₀ h1 h2, div_lt_div_iff₀ h1 h2]
  constructor <;> intro h <;> nlinarith

/-- Inversion threshold in the niche: `exp(-k(1-bv)) < bv` iff `k > log(1/bv)/(1-bv)`. -/
theorem niche_inversion_iff (bv k : ℝ) (h0 : 0 < bv) (h1 : bv < 1) :
    exp (-(k * (1 - bv))) < bv ↔ log (1 / bv) / (1 - bv) < k := by
  have hpos : 0 < 1 - bv := by linarith
  rw [← log_lt_log_iff (exp_pos _) h0, log_exp, one_div, log_inv, div_lt_iff₀ hpos]
  constructor <;> intro h <;> linarith

/-! ## 4. Variance identity for conditional enrichment under operator A (Theorem 1, part 1) -/

/-- Finite form: weights `w` summing to 1, survival `b` with positive mean `m`.
`(Σ w b²)/m - m = (Σ w b² - m²)/m`, i.e. the post-selection mean exceeds the prior mean by Var/m. -/
theorem variance_identity {n : ℕ} (w b : Fin n → ℝ) (hm : 0 < ∑ i, w i * b i) :
    (∑ i, w i * b i * b i) / (∑ i, w i * b i) - ∑ i, w i * b i =
      ((∑ i, w i * b i * b i) - (∑ i, w i * b i) ^ 2) / (∑ i, w i * b i) := by
  field_simp

/-- Exact rational example used in the paper: weights (1/2,1/3,1/6), survivals (1/10,2/5,9/10). -/
theorem variance_example :
    let m : ℚ := 1/2 * (1/10) + 1/3 * (2/5) + 1/6 * (9/10)
    let s2 : ℚ := 1/2 * (1/10)^2 + 1/3 * (2/5)^2 + 1/6 * (9/10)^2
    s2 / m - m = 37 / 150 ∧ (s2 - m ^ 2) / m = 37 / 150 := by
  norm_num

/-! ## 5. Audit decoupling under operator A: covariance identity (Theorem 2, R2) -/

theorem covariance_identity {n : ℕ} (ν bl ba : Fin n → ℝ) (_hsum : ∑ i, ν i = 1)
    (hm : 0 < ∑ i, ν i * bl i) :
    (∑ i, ν i * bl i * ba i) / (∑ i, ν i * bl i) - ∑ i, ν i * ba i =
      ((∑ i, ν i * bl i * ba i) - (∑ i, ν i * bl i) * (∑ i, ν i * ba i)) / (∑ i, ν i * bl i) := by
  field_simp

/-- Off-loop placement does not imply non-positive covariance (audit counterexample):
two equiprobable atoms, loop survival (1/10, 9/10), audit survival (2/10, 8/10):
audit survival rises from 1/2 to 37/50 under operator A. -/
theorem offloop_counterexample :
    ((1/2 : ℚ) * (1/10) * (2/10) + 1/2 * (9/10) * (8/10)) / (1/2 * (1/10) + 1/2 * (9/10)) = 37/50 ∧
      (1/2 : ℚ) * (2/10) + 1/2 * (8/10) = 1/2 := by
  norm_num

/-- In-loop audit whose survival falls (audit counterexample): 3/4 → 7/12. -/
theorem inloop_counterexample :
    ((1/2 : ℚ) * ((1/2) * 1) * (1/2) + 1/2 * (1 * (1/10)) * 1) / (1/2 * ((1/2) * 1) + 1/2 * (1 * (1/10))) = 7/12 ∧
      (1/2 : ℚ) * (1/2) + 1/2 * 1 = 3/4 := by
  norm_num

/-- Pure rejection collapses mostly to visible cheating: stealthy share of cheaters 3/128. -/
theorem collapse_counterexample :
    ((3/5 : ℚ) * (1/100)) / ((1/2) * (1/2) + (3/5) * (1/100)) = 3/128 := by
  norm_num

/-! ## 6. Iterated rejection keeps a non-vanishing barrier (audit § 3.1; dynamics section) -/

/-- After `T` rounds of rejection with reward tilt `g` per round, stealth beats honesty iff
`T (g - log(bh/bf)) > log(ph/pf)`. -/
theorem iterated_rejection_iff (ph pf bh bf g : ℝ) (T : ℕ)
    (hph : 0 < ph) (hpf : 0 < pf) (hbh : 0 < bh) (hbf : 0 < bf) :
    bh ^ T * ph < bf ^ T * pf * exp (T * g) ↔ log (ph / pf) < T * (g - log (bh / bf)) := by
  have hl : 0 < bh ^ T * ph := by positivity
  have hr : 0 < bf ^ T * pf * exp (T * g) := by positivity
  rw [← log_lt_log_iff hl hr]
  rw [log_mul (by positivity) hph.ne', log_mul (by positivity) (by positivity), log_mul (by positivity) hpf.ne',
    log_pow, log_pow, log_exp, log_div hph.ne' hpf.ne', log_div hbh.ne' hbf.ne']
  constructor <;> intro h <;> nlinarith

/-! ## 7. Discrete natural policy gradient: exact closed form (dynamics section) -/

/-- Logit recursion `θ_{k+1} = θ_k + γ (r - (θ_k - θ₀)/η)`. -/
noncomputable def npg (θ0 r γ η : ℝ) : ℕ → ℝ
  | 0 => θ0
  | k + 1 => npg θ0 r γ η k + γ * (r - (npg θ0 r γ η k - θ0) / η)

/-- `θ_k - θ₀ = (1 - (1 - γ/η)^k) η r`: the trajectory is the static Gibbs family at
effective pressure `η (1 - (1-γ/η)^k)`. -/
theorem npg_closed_form (θ0 r γ η : ℝ) (hη : η ≠ 0) (k : ℕ) :
    npg θ0 r γ η k - θ0 = (1 - (1 - γ / η) ^ k) * η * r := by
  induction k with
  | zero => simp [npg]
  | succ k ih =>
    simp only [npg]
    have : npg θ0 r γ η k = θ0 + (1 - (1 - γ / η) ^ k) * η * r := by linarith
    rw [this, pow_succ]
    field_simp
    ring

/-! ## 8. Rejection fine-tuning versus the static operator (dynamics section) -/

/-- Iterated distribution matching on accepted samples multiplies each stratum weight by
`β · w` per round: weights after `k` rounds are `p β^k w^k`. -/
theorem rft_weights (p β w : ℝ) (k : ℕ) :
    (Nat.rec p (fun _ x => x * β * w) k : ℝ) = p * β ^ k * w ^ k := by
  induction k with
  | zero => simp
  | succ k ih => simp only [ih, pow_succ]; ring

end PapierD
