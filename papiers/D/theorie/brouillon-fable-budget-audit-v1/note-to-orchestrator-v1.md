# Note to the orchestrator — audit-budget section, v1

Fragment: `audit-budget-section-v1.tex` (same directory). It compiles under a minimal
amsthm wrapper (7 pages at 11pt with 1in margins; no LaTeX error, no overfull box;
citations are `\cite{key}` with the full entries in a comment block at the end of the
fragment). Labels: `thm:audit-deterrence`, `thm:audit-detection`, `thm:audit-random`;
also `lem:audit-logodds`, `def:audit-budgets`, `cor:audit-tradeoff`,
`prop:audit-indist`, `rem:audit-criteria`, `rem:audit-detect-deter`,
`rem:audit-random`, `rem:audit-related`, `sec:audit-budget`.

Notation introduced: `W := ΔR + C`; `a := 1 − γ/η`; `G_k := γ Σ_{i<k} a^i`
(= η(1 − a^k), or γk when η = ∞); headroom `c := ℓ_crit + L ≥ 0`; `x_k := ℓ_k + L`;
cheating set `F`; `Γ_K := Σ_{i<K} a^{2i}`.

## 1. Claims of the brief found false, or weakened, or sharpened

1. **Detection lower bound `B* ≥ ((T−k+1)/k)·log(1/δ)` is false.**
   Counterexample: T = 100, k = 1, δ = 0.01. The miss probability is 1 − B/T, so
   B* = 99, while the claimed bound is 100·log 100 ≈ 460.5 > T. Correct two-sided
   statement (proved, and checked exhaustively for T ∈ {5, 17, 60, 200}, all k, four
   values of δ):
   `(T−k+1)·log(1/δ)/(k+log(1/δ)) ≤ (T−k+1)(1−δ^{1/k}) ≤ B* ≤ ⌈T(1−δ^{1/k})⌉ ≤ ⌈(T/k)·log(1/δ)⌉`.
   The `(T/k) log(1/δ)` form is only an upper bound; the matching lower bound carries the
   factor `1/(1 + log(1/δ)/k)`.

2. **Le Cam two-point bound: correct but not tight.** `B ≥ log(1/(2δ))/log(1/(1−ε))` is a
   valid necessary condition for both errors ≤ δ. The exact threshold (randomised tests
   allowed) is `B ≥ log((1−δ)/δ)/log(1/(1−ε))`, because the minimax error is
   μ/(1+μ) with μ = (1−ε)^B. The section states the exact form and names the sum-of-errors
   bound `α + β ≥ (1−ε)^B` as the Le Cam bound. One-sided (no false alarm) form
   `log(1/δ)/log(1/(1−ε))` is exact, as the brief expected.

3. **Final criterion: back-loading confirmed, but the consequence is the opposite of
   "budget linear in T".** For finite η the final-criterion budget is bounded uniformly in
   the horizon: `B*_fin ≤ n[1 + (η/γ)·log(η(ΔR+C)/(ηC+L+ℓ_crit))]`. Only the uniform
   criterion (or η = ∞) gives a budget linear in T. The limits K → ∞ and η → ∞ do not
   commute for the final criterion. The section says so and recommends the uniform
   criterion as the meaningful one (the final one lets stealth dominate during training,
   needs a known horizon, and decays after the last audit).

4. **Uniform criterion: threshold policy confirmed, with one extra transition step.**
   Hold rate `ρ_hold = (ΔR − (L+ℓ_crit)/η)/(ΔR+C)`, so the brief's ΔR' is
   `ΔR − (L+ℓ_crit)/η`. Between "no audit" and "hold" there is exactly one step with a
   partial rate `ρ_κ ∈ (0, ρ_hold]`. Exact value: `B*_unif = n[ρ_κ + (K−1−κ)ρ_hold]`.
   The lower bound is not obtained through a generic duality theorem but through a
   telescoping identity (sum of the recursion) plus the envelope `x_k ≤ min(c, ΔR·G_k)`;
   this is weak duality with explicit multipliers, and gives uniqueness of the optimum for
   η < ∞.

5. **Limit η → ∞: `B*/T → ΔR/(ΔR+C)` holds only as K → ∞ as well.** At η = ∞ the exact
   value, for both criteria, is `B* = (T·ΔR − n(L+ℓ_crit)/γ)_+ /(ΔR+C)`; the prior
   log-odds buys a grace period of about (L+ℓ_crit)/(γΔR) steps.

6. **Trade-off C versus B.** The brief's "B ≪ T requires C ≫ ΔR·T/B" is right in order of
   magnitude; the proved statement is two-sided and uses ΔR' rather than ΔR:
   sufficient `C ≥ ΔR'(T − nκ)/B − ΔR`, necessary `C ≥ ΔR'(T − n(κ+1))/B − ΔR`;
   bounded penalties give `B*_unif ≥ ΔR'(T − n(κ+1))/(ΔR+C_max) = Θ(T)`.

7. **Randomised implementation: the deviation term is linear in T when η < ∞.** For an
   open-loop schedule the margin must be paid at every step, so
   `B_ε − B*_unif ≤ (1 + η/(γK))·[T·sqrt(2γρ̄Λ/(ηn)) + (2γK/(3η))Λ]`, Λ = log(2K/δ),
   ρ̄ = ΔR/(ΔR+C). Only for η = ∞ is it `sqrt(2ρ̄TΛ) + 2Λ/3`. The inflation depends on
   ΔR + C only through ρ̄ (noise and leverage both scale with W), not as "(ΔR+C)·…" as the
   brief's wording suggested. No matching lower bound is claimed. Closed-loop schedules
   are not analysed (one sentence on Freedman only says what the inequality would give).

8. **Indistinguishability: `ρ_eff ≥ ρ(1 − δ_ind/τ)` is true as "fraction of cheats that
   are audited", but substituting ρ_eff for ρ in the dynamics is not the exact
   correction.** The exact worst-case advantage is `τ[ΔR − ρ(ΔR + C(1−δ_ind/τ)_+)]`: the
   audit still withholds ΔR on every audited episode where the policy abstains, so only
   the penalty is discounted. The ρ → ρ_eff substitution is a valid but looser sufficient
   condition (it overstates the advantage by ρ·δ_ind·ΔR). New consequence stated: for
   τ ≤ δ_ind the penalty is useless and the hold rate is `1 − c/(ητΔR)` whatever C.

## 2. Added assumptions (all stated in the text)

- Two strata only (v dropped); `ℓ_crit ≥ −L`; `C ≥ 0`; `γ ∈ (0, η]`, η = ∞ allowed (a = 1).
- An audited stealthy episode forfeits ΔR and pays C (advantage `ΔR − Wρ_j`), as in the
  static result.
- Schedules are deterministic and fractional (nρ_j need not be an integer); rounding up
  costs at most one audit per step with ρ_j > 0 (monotonicity argument given).
- Budget is the expected count `n Σ ρ_j`; T = nK.
- The schedule is open-loop and uses (L, ΔR, η, γ); upper bound on ΔR and lower bound on
  L are safe (monotonicity, Remark `rem:audit-criteria`).
- Final criterion, case γ = η treated apart (only the last step matters). The general
  formula would fail in the doubly degenerate case a = 0, C = 0, c = 0.
- Detection: the only F-dependent information is the outcome of audits; B ≤ T; the
  cheating set is fixed in advance (the policy cannot see audits). Rate test: i.i.d. audit
  outcomes.
- Randomised theorem: audit indicators independent of actions and of each other; the
  expectation over the policy's own actions is exact (only audits are random); action
  sampling noise is NOT covered; needs `ε ≤ L + ℓ_crit`; hard cap at `B_rand`.
- Indistinguishability proposition: τ and τ_A constant during training; trap bound taken
  as a hypothesis `τ_A ≥ (τ − δ_ind)_+`; L is the prior log-odds of that stratum.

## 3. Numerical checks

Already run (script `check_audit_v1.py`, same directory; seeds through
`numpy.random.SeedSequence(20261124)`):
- 3000 random instances (K ≤ 24; γ = η, η finite, η = ∞; C = 0 and c = 0 included):
  closed forms of `B*_fin` and `B*_unif` against `scipy.optimize.linprog` (HiGHS);
  largest gap 2.4e-8. Both expressions of `B*_unif` agree to 1e-9.
- Floor formulas for m and κ, and the horizon-free bound on `B*_fin`: 3000 instances, no
  violation.
- Hypergeometric identities and all bounds of `thm:audit-detection`(b): exhaustive for
  T ∈ {5, 17, 60, 200}, no violation.
- Monte Carlo (4000 runs each, four configurations) of the capped Bernoulli schedule:
  empirical failure 0.3–0.4 % against δ = 5–10 %; no threshold violation observed, all
  failures are budget overruns. The bound is conservative.

Worth adding for the paper (exact quantities):
1. Tightness of the Bernstein margin: for (K, n, γ, η, ΔR, C, c, δ) on a grid, the
   smallest margin ε_emp such that the open-loop schedule for threshold ℓ_crit − ε_emp has
   `P(max_k ℓ̂_k > ℓ_crit) ≤ δ`, against `ε(log(2K/δ), ΔR/W)`; report ε_emp/ε and
   `(B_rand − B*_unif)/B*_unif`. One of my runs (K = 100, n = 1000, γ = 0.2, η = 1,
   ΔR = 1, C = 4, c = 0.5, δ = 0.1) gives a 20 % inflation from the bound; the true
   requirement is probably much smaller.
2. Full stochastic policy gradient (actions sampled, n episodes per step): does
   `max_k ℓ̂_k ≤ ℓ_crit` still hold at the stated budget? Quantity: failure frequency
   against n. This is outside the theorem.
3. Figure: `B*_unif/T` and `B*_fin/T` against K for η ∈ {1, 10, 100, ∞} at fixed γ, to
   show the non-commuting limits; crossover expected near K ≈ η/γ.
4. Closed-loop greedy (rate recomputed from realised audit counts) against open-loop:
   budget needed for the same δ. Not proved; a simulation would say whether a theorem is
   worth writing.
5. Indistinguishability: `ρ_hold^δ` against τ for δ_ind ∈ {0, 0.01, 0.1}; the maximum over
   τ of the hold rate is the planning quantity if the stratum is adversarial.

## 4. Things I did not prove and did not claim

- No lower bound for randomised or adaptive deterrence schedules (only deterministic
  fractional schedules are exactly solved).
- No statement on the stochastic-gradient dynamics beyond audit randomness.
- No continuity claim of `B*_fin` in η (only the two regimes are stated).
- The novelty paragraph is hedged ("to our knowledge"); I did no literature search in
  this session. The hypergeometric minimax value is presented as folklore, not as new.

## 5. References, with my confidence that each exists exactly as cited

| Key | Reference | Confidence |
|---|---|---|
| avenhaus2002inspection | Avenhaus, von Stengel, Zamir, "Inspection games", Handbook of Game Theory with Economic Applications vol. 3, ch. 51, pp. 1947–1987, Elsevier 2002 | high (95 %); page range 90 % |
| dresher1962sampling | Dresher, "A sampling inspection problem in arms control agreements: a game-theoretic analysis", RAND Memorandum RM-2972-ARPA, 1962 | medium-high (85 %); check the memorandum number |
| tambe2011security | Tambe, "Security and Game Theory: Algorithms, Deployed Systems, Lessons Learned", Cambridge University Press 2011 | high (95 %) |
| blocki2013audit | Blocki, Christin, Datta, Procaccia, Sinha, "Audit games", IJCAI 2013 | high (90 %); author order to check |
| becker1968crime | Becker, "Crime and punishment: an economic approach", JPE 76(2):169–217, 1968 | high (97 %) |
| yao1977probabilistic | Yao, "Probabilistic computations: toward a unified measure of complexity", FOCS 1977, pp. 222–227 | high (95 %) |
| lecam1973convergence | Le Cam, "Convergence of estimates under dimensionality restrictions", Ann. Statist. 1(1):38–53, 1973 | high (95 %) |
| yu1997assouad | Yu, "Assouad, Fano, and Le Cam", Festschrift for Lucien Le Cam, Springer 1997, pp. 423–435 | high (95 %) |
| boucheron2013concentration | Boucheron, Lugosi, Massart, "Concentration Inequalities: A Nonasymptotic Theory of Independence", OUP 2013 | high (98 %) |
| freedman1975tail | Freedman, "On tail probabilities for martingales", Ann. Probab. 3(1):100–118, 1975 | high (97 %) |
| hoeffding1963probability | Hoeffding, "Probability inequalities for sums of bounded random variables", JASA 58(301):13–30, 1963 | high (98 %) |
| serfling1974probability | Serfling, "Probability inequalities for the sum in sampling without replacement", Ann. Statist. 2(1):39–48, 1974 | high (97 %) |
| greenblatt2023control | Greenblatt, Shlegeris, Sachan, Roger, "AI Control: Improving Safety Despite Intentional Subversion", arXiv:2312.06942 | high (97 %) |
| griffin2024games | Griffin, Thomson, Shlegeris, Abate, "Games for AI Control: Models of Safety Evaluations of AI Control Protocols", arXiv:2409.07985 | high for title and number (95 %); author list 85 % |

Characterisations to verify on the source before submission: that Greenblatt et al. and
Griffin et al. treat deployment with a single caught attempt ending the game (I am
confident for the first, fairly confident for the second); that Dresher's game has a
strategic violator choosing when to violate (confident). No number from any of these
papers is quoted in the section.
