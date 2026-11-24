# Note to the orchestrator — dynamics section v1

Companion to `dynamics-section-v1.tex` (same directory). The fragment compiles
with a minimal wrapper (`checks/wrap.tex`: amsmath, amssymb, amsthm, `\E` as a
symbol; 15 pages, no errors, three overfull boxes under 5pt). Nothing in the
repository was read or opened.

Labels: `thm:dynamics-tabular`, `thm:dynamics-two-channel`, plus
`lem:npg-softmax`, `def:gibbs-family`, `cor:hitting-times`, `prop:equal-time`,
`prop:discard-kl`, `cor:penalty-window`, `prop:bistability`, `prop:nonreach`,
`prop:two-channel-A`, and remarks `rem:mirror`, `rem:reentrance`,
`rem:taxonomy`, `rem:dilemma`, `rem:A-vs-B`, `rem:saddle-node`,
`rem:mean-field`, `rem:noise`, `rem:known-vs-new`.

Macro choices: `\E` is used as a bare symbol (`\E_\pi[...]`). I did not use
`\DKL`, `\Prob`, `\Var`, `\Cov` because I do not know their signatures; KL is
written `\mathrm{KL}(\cdot\,\|\,\cdot)` and Bernoulli KL `\mathrm{kl}`. The map
you called F (two-channel fixed-point map) is named `\Phi` because `F` is the
Fisher matrix in the tabular part. Citation keys to map to your .bib:
`cen2022fast`, `mei2020global`, `agarwal2021theory`, `smith1995monotone`,
`hirsch2006monotone`, `lasalle1976stability`.

## 1. Claims of yours that I found false or had to weaken

1. **(3c) "advantage-based: stealth wins for any beta_f > 0" is false once the
   KL anchor is added.** It is true without the anchor (Theorem 3(c2)). With
   the anchor (Proposition `prop:discard-kl`) the flow is the natural gradient
   flow of `b(pi) - eta^{-1} KL`, where `b` is the accepted-sample mean reward,
   and:
   - dominance from the pretrained policy is guaranteed only if
     `eta * (beta_f/beta_h) * DeltaR > L`;
   - it is provably excluded if `eta*rho*DeltaR*(1 + c e^{ybar})^2 <= ybar` for
     some `ybar <= L`, with `rho = beta_f/beta_h`, `c = (p_v+p_f)/p_h`;
   - explicit instance: `p = (1-2e-4, 1e-4, 1e-4)`, `beta_h = 1`,
     `beta_f = 0.1`, `beta_v in (0, 0.1)`, `eta*DeltaR = 20`. Static A and the
     unmonitored static policy both have stealth dominating
     (`20 > L + log 10 = 11.51`), yet the regularised discard flow keeps
     `log(pi_f/pi_h) <= 3 - L < -6.2` forever, while the global maximiser of the
     objective is another, stealth-heavy equilibrium. Simulation: gain in
     log-odds peaks at 2.003 (bound 3).
   So the message "advantage-based = filter only rescales time" must be
   restricted to the unanchored rule. With the anchor the filter rescales the
   *pressure* (multiplicatively, like operator B with C = 0), which is a
   stronger protection than the additive `log(beta_h/beta_f)` of static A when
   beta_f is small, and the system can be bistable.

2. **(3c) "stealth dominates" needs a qualifier even without the anchor.**
   Stealth beats honesty, but it does not eliminate visible cheating: the f:v
   log-odds rate is `(beta_f-beta_v) beta_h pi_h DeltaR / Zbar^2`, proportional
   to the remaining honest mass, so the total f:v gain is finite. There is a
   conserved quantity `pi_v = p_v (pi_f/p_f)^{beta_v/beta_f}` and the limit is
   `(0, 1-x*, x*)` with `x* + p_v (x*/p_f)^{beta_v/beta_f} = 1`. Contrast with
   rule (3b), where f:v grows by `log(beta_f/beta_v)` per round without bound.

3. **(3c) lower bound.** Your bound `>= beta_f DeltaR` is correct; I prove the
   slightly stronger `>= beta_f DeltaR / beta_h` (since `Zbar <= beta_h`), hence
   dominance time `<= L beta_h / (beta_f DeltaR)`.

4. **(3c) expected gradient.** With the *empirical* accepted-sample mean as
   baseline the expectation carries an exact factor `(N-1)/N` (so `N >= 2`);
   your formula is the population-baseline version. The Fisher step is right
   provided the Fisher matrix is that of the sampling policy pi (not of the
   accepted law); I state this explicitly.

5. **(3a) absolute amplification under A at equal time: no exact hitting
   time.** The criterion is
   `p_v (beta_f^lam - beta_v^lam) e^{eta lam DeltaR} > p_h (beta_h^lam - beta_f^lam)`,
   a transcendental equation in `lam = lambda(t)`. What I prove
   (`prop:equal-time`): the exact criterion; amplification holds whenever
   `eta_eff(t) DeltaR >= T_amp` (the static threshold), so the amplification
   time is never later than the naive time-slice time; the short-time
   criterion `p_v log(beta_f/beta_v)` vs `p_h log(beta_h/beta_f)`;
   convexity/concavity of the log-ratio in `lam`. **The amplification set need
   not be a half-line**: numerical re-entrance example in `rem:reentrance`
   (amplified, then not, then amplified again). I assumed the static
   definition of absolute amplification is `pi_A(f) > pi_no(f)` and derived the
   static threshold `T_amp = log[p_h(beta_h-beta_f)/(p_v(beta_f-beta_v))]`
   myself — **check that this matches the static section**.

6. **(3a) operator A is not "the static family at effective pressure".** As you
   noted, the filter enters as `beta^{lambda(t)}`; I state this as (a2) and it
   means the time slice of A is *not* static A at `eta_eff`. Consequence worth
   knowing: as `eta -> infinity`, `tau_A -> L/DeltaR`, the unmonitored value —
   the filter does not delay dominance at all in that limit under rule (a).

7. **(3b) best-of-N is not of the form `w(R)` with a fixed w.** The weight
   ratio depends on the current accepted share of cheating `chi_k`:
   `sum_{i<N} (1-chi_k)^{-i} >= N`. I give only the sufficient condition
   `N > beta_h/beta_f` (remark); the case `N <= beta_h/beta_f` is
   initial-condition dependent and not characterised.

8. **(4c) "raising C beyond C_high destroys the certificate" — true, but it
   does not imply a stealth takeover, and in your intended regime it visibly
   does not.** What is proved (`cor:penalty-window`): `q(t) <= q0` and
   `s(t) <= s0` for all t **iff** `C_low <= C <= C_high` (necessary and
   sufficient). Beyond `C_high`, s does exceed s0 at small times, but in the
   explicit instance (`C_high = 9`) integration with `C = 100` gives
   `sup s = 0.01007` for `s0 = 0.01`: the penalty also crushes q, and the
   obfuscation drive `D q` dies with it. I added a second certificate
   (`wbar = w0 + eta (D q0 - kappa)^+`, valid if `A0 + D sigma(wbar) <= 0`)
   that bounds the excursion for a range of C above `C_high`. The regime
   where larger penalties *provably* produce more obfuscation is the
   **reverse window** `C_high <= C <= C_low` (nonempty iff
   `kappa <= kappa_dagger = q0 (beta_f-beta_v) beta_h DeltaR / (beta_h - beta0bar)`):
   there q and s are monotone nondecreasing and the limit obfuscation logit is
   `>= w0 + eta (q0 (beta_f-beta_v)(DeltaR + C) - kappa)`, increasing in C. A
   parameter scan confirms the picture: final s increases with C while hacking
   stays profitable, then collapses once C deters hacking. I found **no**
   instance (3000 random draws) where raising C moves the pretrained model
   from the honest basin to the stealth basin. The "dynamic dilemma" should
   therefore be phrased as in `rem:dilemma`, not as "raising C beyond C_high
   causes obfuscation growth".

9. **(4b) "at most three" — confirmed and proved** (Phi' is strictly unimodal;
   exactly one inflection point; Rolle). Stability alternation proved for the
   three-equilibrium case. "Bistability arises through saddle-node
   bifurcations in (eta, C)" is **weakened to a remark**: I prove that the
   count can change only at tangencies `Phi' = 1` and that a bistable region
   exists (explicit sufficient conditions, and all large eta when
   `A0 < 0 < A0 + D`, `0 < kappa < D`), but I do not verify the transversality
   conditions of the saddle-node theorem along paths in (eta, C).

10. **(4a) convergence** is proved by LaSalle plus finiteness of equilibria
    (from 4b), not by planar cooperative theory; no non-isolated equilibria
    can occur.

11. **(4d) no Kramers formula**, as instructed; local rates are
    `(1 - sqrt(Phi'(w*)))/eta`, and a global contraction rate `1/eta - D/4`
    is proved when `eta D < 4`.

12. **Structural caveat I added (`rem:mean-field`)**: the bistability of
    Theorem 4 is a consequence of the *factorised* parametrisation. A tabular
    policy over the four joint outcomes falls under Theorem 3(a) and has a
    unique Gibbs path. A referee will see this; better to say it ourselves.

13. **Operator A in the two-channel model**: `eta D^A = log(beta_f/beta_v)` is
    independent of eta and C, so for `beta_f/beta_v < e^4` there is a unique,
    globally exponentially attracting equilibrium for every eta (no
    bistability, no hysteresis); obfuscation odds are capped at
    `beta_f/beta_v` times pretrained odds, but `q* -> 1` as eta grows. The
    case `beta_f/beta_v >= e^4` is not analysed.

## 2. Assumptions I added

- R and beta are constant on strata (needed for stratum-level statements);
  the time-slice identity itself holds for arbitrary r on a finite set.
- All dynamics are population-level: expected gradients, exact fits in (3b).
- Dominance is defined strictly (`pi(f) > pi(h)`); hitting-time corollary
  assumes `p_h > p_f` (L > 0).
- `beta_v = 0` under A: objects defined on the reduced space `{h, f}`, justified
  as the pointwise limit `beta_v -> 0` for each fixed t > 0.
- (3b) anchored variant: geometric anchoring,
  `argmin (1-alpha) KL(pi||kept) + alpha KL(pi||pi_0)`; gives exponent
  `c_k = ((1-alpha)/alpha)(1 - (1-alpha)^k)`. This is one clean choice among
  several possible anchorings.
- (3c): `N >= 2`; score and Fisher of the sampling policy; accepted samples
  i.i.d. from `pi*beta/Zbar`.
- `prop:discard-kl`(v) needs `beta_v > 0` (to place the global maximiser in
  the interior without boundary pathologies).
- Theorem 4 is written for general `beta_h` with
  `A0 := beta_v DeltaR - (beta_h - beta_v) C` (reduces to yours at
  `beta_h = 1`); honest trajectories survive with `beta_h` whatever the
  chain of thought; `C_low = beta0bar DeltaR / (beta_h - beta0bar)`.
- Bistability proposition needs `kappa > 0` (my test points use kappa).
- Operator A in the two-channel model needs `beta_v > 0`.

## 3. Where a numerical check would be valuable

Scripts already run are in `checks/` (`c1.py` … `c6.py`); all passed. They
are sanity checks, not part of any proof except where the text says "numerical".

- Done: time-slice identity vs ODE integration (error 3e-12); REINFORCE
  expectation by exhaustive enumeration, N = 2, 3 (exact match with the
  (N-1)/N factor); closed forms of `a` and the bound `a_f - a_h >= rho DeltaR`
  (1e5 random draws); conserved quantity and limit `x*` of unregularised
  discard flow (5 draws, error < 1e-9); trapped example of `prop:discard-kl`;
  sufficient amplification condition (2e4 draws, 0 violations) and sign of
  `g''` (2e4 draws); re-entrance example; at most three fixed points and
  single inflection (4000 random parameter draws); the explicit non-reachability
  instance (three equilibria, J values, certificate); eigenvalue formula;
  certificates (i)–(iv) of `cor:penalty-window` on 1500 random draws;
  best-of-N weight ratio; operator A uniqueness for `log(beta_f/beta_v) < 4`.
- Still worth doing for the paper:
  1. A phase portrait of the instance in `prop:nonreach`(iii) with the three
     equilibria, the saddle's stable manifold and the pretrained point.
  2. The bifurcation diagram in (eta, C) (fold curves, cusp) to back
     `rem:saddle-node`; nothing there is proved beyond the remark.
  3. Final s as a function of C from the pretrained model across the reverse
     window and beyond, to illustrate `rem:dilemma`.
  4. For `prop:discard-kl`: the actual dominance threshold in `eta rho DeltaR`
     versus the two proven bounds (how tight they are), and a count of
     equilibria of the self-consistency equation.
  5. Finite-batch simulations of rule (3c) and of Theorem 4 (noise-activated
     escape); nothing is claimed about these.
  6. Whether a KL-anchored best-of-N rule behaves like (3b) or (3c).
  7. The three numerical statements in the text that are *not* proved:
     the re-entrance example (`rem:reentrance`), `sup s = 0.01007` at C = 100
     (`rem:dilemma`), and the three equilibria with their J values quoted after
     `prop:nonreach`. They should be regenerated by a logged script before
     submission.

## 4. References cited, and how sure I am

All from memory; none verified against a PDF in this session.

- `cen2022fast`: S. Cen, C. Cheng, Y. Chen, Y. Wei, Y. Chi, "Fast Global
  Convergence of Natural Policy Gradient Methods with Entropy
  Regularization", Operations Research 70(4), 2022; arXiv:2007.06558.
  Title, authors, arXiv id: confident. Volume/issue: fairly confident; page
  range not given because I am not sure of it.
- `mei2020global`: J. Mei, C. Xiao, C. Szepesvári, D. Schuurmans, "On the
  Global Convergence Rates of Softmax Policy Gradient Methods", ICML 2020
  (PMLR 119); arXiv:2005.06392. Confident.
- `agarwal2021theory` (I added it): A. Agarwal, S. M. Kakade, J. D. Lee,
  G. Mahajan, "On the Theory of Policy Gradient Methods: Optimality,
  Approximation, and Distribution Shift", JMLR 22, 2021; arXiv:1908.00261.
  Confident on title, authors, arXiv id; JMLR paper number not given.
  Can be dropped without loss.
- `smith1995monotone`: **correction to your brief** — the 1995 monograph
  "Monotone Dynamical Systems: An Introduction to the Theory of Competitive
  and Cooperative Systems" (AMS Mathematical Surveys and Monographs 41) is by
  Hal L. Smith alone, not Hirsch and Smith. Confident.
- `hirsch2006monotone`: M. W. Hirsch and H. L. Smith, "Monotone dynamical
  systems", chapter in Handbook of Differential Equations: Ordinary
  Differential Equations, vol. 2, Elsevier. Existence and authors: confident.
  Year (2005 vs 2006) and page range: not sure. Can be dropped; the
  order-theoretic steps are proved directly in the text.
- `lasalle1976stability`: J. P. LaSalle, "The Stability of Dynamical
  Systems", SIAM (CBMS-NSF Regional Conference Series in Applied
  Mathematics), 1976. Confident on author, title, publisher, year; series
  number (25) fairly confident.
- Used without citation: the comparison lemma for scalar differential
  inequalities and the linearisation estimate at a hyperbolic sink (any ODE
  textbook); Grönwall's lemma.

The attribution in `rem:mirror` / `rem:known-vs-new` ("multiplicative form and
linear convergence of entropy-regularised NPG are due to Cen et al.") reflects
my recollection of that paper's content; their setting is discounted MDPs with
entropy (not KL-to-prior) regularisation, which covers the bandit case after
absorbing `log p` into the reward. Please have it checked against the PDF.
`rem:known-vs-new` deliberately makes no priority claim and says that no
systematic literature search was done.
