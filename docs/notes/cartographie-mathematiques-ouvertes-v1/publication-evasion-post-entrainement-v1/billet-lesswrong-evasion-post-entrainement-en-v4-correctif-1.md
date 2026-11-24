# When Does In-Loop Misalignment Filtering Select for Stealth? Exact Thresholds in a Static Gibbs Model of Post-Training

## 1. TL;DR and What This Does (and Does Not) Answer

In [*Post training is fundamentally dangerous*](https://www.lesswrong.com/posts/CoRJ9saddvsXti4m2) (Nov. 22, 2026), Yair Halberstadt argues that misalignment detectors that work well at deployment—chain-of-thought monitors, elicitation checks, linear activation probes—become counterproductive once placed inside the post-training loop, *even if caught runs receive no negative penalty and are merely discarded and resampled*. He asks whether it is a mathematical law that any attempt to prevent misalignment during post-training inevitably encourages evasion.

In the comments, `testingthewaters` pushes back that an in-loop filter acts as a *selective sieve* rather than a directional gradient toward evasion, highlighting three obstacles: non-existence of stealthy strategies, unreachability under optimization constraints, and non-maintainability against competing post-training objectives.

**Scope first.** What follows is a *static* model: the KL-regularized (Gibbs) equilibrium of post-training over three *fixed* strata (honest, visible cheating, stealthy cheating), with fixed prior masses and fixed detection rates. Halberstadt's worry that training "generalises" toward masking—how training reshapes the stealthy stratum and its detectability—is **outside** this model. Within it, much of the disagreement dissolves once we separate **four distinct quantities**:
1. the **conditional share** of stealthy cheating among all cheating runs, $\pi_{\mathrm{post}}(\Pi_{\mathrm{f}} \mid \Pi_{\mathrm{tr}})$;
2. the **absolute probability** of stealthy cheating relative to unmonitored post-training, $\pi_{\mathrm{post}}(\Pi_{\mathrm{f}}) - \pi_{\mathrm{no}}(\Pi_{\mathrm{f}})$;
3. the **dominance** of stealth over honesty, $\pi_{\mathrm{post}}(\Pi_{\mathrm{f}}) / \pi_{\mathrm{post}}(\Pi_{\mathrm{h}})$, as optimization pressure $\eta$ grows;
4. the **evasion rate against a separate audit monitor** $M_{\mathrm{audit}} \neq M_{\mathrm{loop}}$.

In this model, each has an exact answer:

- **Pure rejection, as modelled here, cannot keep honesty dominant.** Under pure rejection (*discard and try again*) modelled as conditioning the base law by the survival probability, conditional stealth enrichment follows from a variance identity (a special case of the Price–Robertson covariance identity, the variance form being Fisher's fundamental theorem), and for any $\beta_{\mathrm{f}} > 0$ stealth eventually outweighs honesty as $\eta \to \infty$. Honesty collapses; the mass goes to cheating, but **not necessarily to stealth**: the stealthy share among cheaters tends to $\beta_{\mathrm{f}}p_{\mathrm{f}}/(\beta_{\mathrm{v}}p_{\mathrm{v}} + \beta_{\mathrm{f}}p_{\mathrm{f}})$, which can be small.
- **This depends on a modelling choice.** The rejection operator acts as a reward bonus $\eta^{-1}\log\beta$ that vanishes as $\eta$ grows. If instead rejection is repeated at every round of training, the barrier does **not** vanish. "Pure rejection is fatal, penalties are not" is a property of the model of rejection, not a law.
- **A penalty is not a backfire.** A negative penalty $-C < 0$ creates a non-vanishing barrier against *partially* detected stealth ($\beta_{\mathrm{f}} < \beta_{\mathrm{h}}$). If a *perfectly stealthy* niche exists ($\beta_{\mathrm{f}} = \beta_{\mathrm{h}} = 1$), the penalty yields more absolute stealth than pure rejection past an explicit threshold—but **exactly then it also yields more honesty and less total cheating**: the stealth-to-honesty odds are identical under both operators.
- **It is not an unconditional law,** and we exhibit three escape mechanisms (we do not claim they are the only ones): **(R1)** an exact criterion for honesty to dominate stealth (prior KL barrier and maintenance cost, formalizing `testingthewaters`); **(R2)** an exact identity for the audit monitor: under pure rejection, audit evasion rises by $\operatorname{Cov}(\beta_{\mathrm{loop}}, \beta_{\mathrm{audit}})/\mathbb{E}[\beta_{\mathrm{loop}}]$ under the base law, **whatever the placement** of the audit—keeping it off-loop is neither sufficient nor necessary; under the penalty, non-positive covariance is necessary but not sufficient, and independence or negative association suffices; **(R3)** planted honeypots at bounded total variation distance, which make every *frequent* cheating policy strictly worse than honesty, but leave rare attacks untouched.

Full proofs and a script that recomputes every number below are at [LINK_GITHUB_PAGE]. The proofs carry the results; the script only checks the tables and the counterexamples.

---

## 2. The Minimal Three-Stratum Model and the Two Post-Training Operators

Let $(\Pi, \mathcal{A}, \pi_0)$ be the probability space of trajectories induced by the pretrained base model $\pi_0$, partitioned into three disjoint measurable strata with strictly positive prior masses $p_{\mathrm{h}} + p_{\mathrm{v}} + p_{\mathrm{f}} = 1$:
- $\Pi_{\mathrm{h}}$: **honest** behavior (normalized to task reward $R(\pi) = 0$);
- $\Pi_{\mathrm{v}}$: **visible** misalignment / reward hacking (advantage $\Delta R_{\mathrm{v}} > 0$);
- $\Pi_{\mathrm{f}}$: **stealthy** misalignment (advantage $\Delta R_{\mathrm{f}} = \Delta R_{\mathrm{v}} - \delta_{\mathrm{maint}}$, where $\delta_{\mathrm{maint}} \ge 0$ is any capability or multi-objective maintenance cost).

Write $\Pi_{\mathrm{tr}} := \Pi_{\mathrm{v}} \sqcup \Pi_{\mathrm{f}}$. In the canonical baseline without obfuscation cost, $\Delta R_{\mathrm{v}} = \Delta R_{\mathrm{f}} = \Delta R > 0$. An in-loop monitor $M_{\mathrm{loop}} \in \{0, 1\}$ ($1 =$ caught) is characterized by its **survival probability** $\beta(\pi) := \mathbb{P}(M_{\mathrm{loop}} = 0 \mid \pi)$, with $0 \le \beta_{\mathrm{v}} < \beta_{\mathrm{f}} \le \beta_{\mathrm{h}} \le 1$ and $\beta_{\mathrm{f}} > 0$. (False alarms on honest behaviour beyond those on stealth, $\beta_{\mathrm{f}} > \beta_{\mathrm{h}}$, are excluded by assumption, although realistic.)

At KL inverse temperature $\eta > 0$, unmonitored post-training yields $\pi_{\mathrm{no}}^{(\eta)}(d\pi) \propto e^{\eta R(\pi)}\pi_0(d\pi)$ (with $\pi_{\mathrm{no}}^{(0)} := \pi_0$ by continuity), the standard Gibbs form of KL-regularized RL (Korbak, Perez and Buckley, 2022). We compare Halberstadt's two interventions:
1. **Operator A — Pure rejection with resampling (*discard and try again*), as a modelling choice:** caught runs are discarded before reinforcement, conditioning $\pi_0$ by $\beta(\pi)$ before KL-regularized reward selection:
   $$\pi_{\mathrm{A}}^{(\eta)}(d\pi) = \frac{\beta(\pi)\,e^{\eta R(\pi)}\,\pi_0(d\pi)}{Z_{\mathrm{A}}(\eta)}.$$
2. **Operator B — KL-regularized policy update with interception penalty $-C \le 0$:** caught runs are halted and scored $-C$ ($C \ge 0$), giving expected reward $\bar{R}_C(\pi) = \beta(\pi)R(\pi) - (1 - \beta(\pi))C$:
   $$\pi_{\mathrm{B}}^{(\eta, C)}(d\pi) = \frac{\exp\!\big(\eta[\beta(\pi)R(\pi) - (1 - \beta(\pi))C]\big)\,\pi_0(d\pi)}{Z_{\mathrm{B}}(\eta, C)}.$$

The structural difference is that in Operator A, $\beta(\pi)$ sits **outside** the exponential as a prior factor, whereas in Operator B it sits **inside** the exponential and scales with $\eta$.

**Why Operator A is a choice, not a law.** $\pi_{\mathrm{A}}^{(\eta)}$ maximizes $\mathbb{E}_\pi[R + \eta^{-1}\log\beta] - \eta^{-1}D_{\mathrm{KL}}(\pi\|\pi_0)$: the filter is a bonus of $\eta^{-1}\log\beta$ reward units, which fades as $\eta$ grows. Equivalently, Operator A is unmonitored training followed by a single rejection at inference time ($\pi_{\mathrm{A}} \propto \beta\,\pi_{\mathrm{no}}$). If rejection is instead applied at each of $T$ rounds, each followed by a KL step of size $\eta_1$, then $\pi_T \propto \beta^T e^{T\eta_1 R}\pi_0$, and as $T \to \infty$ stealth beats honesty iff $\eta_1\Delta R > \log(\beta_{\mathrm{h}}/\beta_{\mathrm{f}})$: a barrier that does not vanish (though it depends on the arbitrary step $\eta_1$). With the parameters of the table below, $\Delta R = 1$, $\eta_1 = 0.2$, $T = 1000$ (total pressure 200), the stealth-to-honesty log-odds are $+195.3$ under Operator A and $-92.1$ under repeated rejection. Also, at $\eta = 0$ Operator A is just the filtered output law of the base model: nothing has been learned. Everything below about pure rejection is about Operator A as defined.

---

## 3. Exact Thresholds and a Rejection–Penalty Contrast

### Theorem 1 (Summary)

1. **Conditional enrichment under Operator A (variance identity).** For any non-constant $\beta$ on $\Pi_{\mathrm{tr}}$, pure rejection strictly increases the conditional false-negative rate among cheaters by
   $$\mathbb{E}_{\pi_{\mathrm{A}}^{(\eta)}}[\beta \mid \Pi_{\mathrm{tr}}] - \mathbb{E}_{\pi_{\mathrm{no}}^{(\eta)}}[\beta \mid \Pi_{\mathrm{tr}}] = \frac{\operatorname{Var}_{\mu_{\mathrm{tr}}^{(\eta)}}(\beta)}{\mathbb{E}_{\mu_{\mathrm{tr}}^{(\eta)}}[\beta]} > 0,$$
   even when rewards differ among cheaters. This is the Price (1970) / Robertson (1966) covariance identity applied to the trait "survival", i.e. Fisher's (1930) fundamental theorem in this setting. With two cheating strata of **equal reward**, both Operator A ($\forall \eta \ge 0$) and Operator B ($\forall \eta > 0, C \ge 0$) strictly increase $\pi_{\mathrm{post}}(\Pi_{\mathrm{f}} \mid \Pi_{\mathrm{tr}})$. With heterogeneous rewards, Operator B can *decrease* the mean survival of cheaters (e.g. $0.8810 \to 0.8748$ in the paper's example).
2. **Exact absolute-amplification threshold under pure rejection.** $\pi_{\mathrm{A}}^{(\eta)}(\Pi_{\mathrm{f}}) > \pi_{\mathrm{no}}^{(\eta)}(\Pi_{\mathrm{f}})$ holds unconditionally if $\beta_{\mathrm{f}} = \beta_{\mathrm{h}}$, and for $\beta_{\mathrm{f}} < \beta_{\mathrm{h}}$ iff
   $$\Delta R > \Delta R_{\mathrm{A}}^*(\eta) := \frac{1}{\eta}\left[\log\frac{p_{\mathrm{h}}}{p_{\mathrm{v}}} + \log\frac{\beta_{\mathrm{h}} - \beta_{\mathrm{f}}}{\beta_{\mathrm{f}} - \beta_{\mathrm{v}}}\right].$$
   (Under Operator B the corresponding criterion is exact but implicit in $\Delta R$, not closed-form.)
3. **Dominance as $\eta \to \infty$.** Stealth dominates honesty ($\pi_{\mathrm{post}}(\Pi_{\mathrm{f}}) > \pi_{\mathrm{post}}(\Pi_{\mathrm{h}})$) iff:
   - under Operator A: $\Delta R > \Delta R_{\mathrm{dom, A}}^*(\eta) = \frac{1}{\eta}(\log(p_{\mathrm{h}}/p_{\mathrm{f}}) + \log(\beta_{\mathrm{h}}/\beta_{\mathrm{f}})) \to 0$; honesty collapses; with equal rewards the stealthy share among cheaters equals, for every $\eta$, $\beta_{\mathrm{f}}p_{\mathrm{f}}/(\beta_{\mathrm{v}}p_{\mathrm{v}} + \beta_{\mathrm{f}}p_{\mathrm{f}})$, which equals one only if $\beta_{\mathrm{v}} = 0$ and can be small (e.g. $3/128$ for $p = (0.49, 0.5, 0.01)$, $\beta = (1, 1/2, 3/5)$: the mass goes almost entirely to *visible* cheating);
   - under Operator B: $\Delta R > \Delta R_{\mathrm{dom, B}}^*(\eta, C) = \frac{\beta_{\mathrm{h}} - \beta_{\mathrm{f}}}{\beta_{\mathrm{f}}} C + \frac{1}{\eta \beta_{\mathrm{f}}}\log\frac{p_{\mathrm{h}}}{p_{\mathrm{f}}} \to \frac{\beta_{\mathrm{h}} - \beta_{\mathrm{f}}}{\beta_{\mathrm{f}}} C > 0$ ($C > 0, \beta_{\mathrm{f}} < \beta_{\mathrm{h}}$). With $C = 0$ and no resampling, $\pi_{\mathrm{B}}(\Pi_{\mathrm{f}}) \to 1$: pure rejection is not the only "fatal" case.
4. **The perfect-stealth niche: two sides.** If a *perfectly stealthy* niche exists ($\beta_{\mathrm{f}} = \beta_{\mathrm{h}} = 1 > \beta_{\mathrm{v}} > 0$), Operator B loses its asymptotic barrier, and $\pi_{\mathrm{B}}^{(\eta, C)}(\Pi_{\mathrm{f}}) > \pi_{\mathrm{A}}^{(\eta)}(\Pi_{\mathrm{f}}) > \pi_{\mathrm{no}}^{(\eta)}(\Pi_{\mathrm{f}})$ iff
   $$\eta(\Delta R + C) > \frac{\log(1/\beta_{\mathrm{v}})}{1 - \beta_{\mathrm{v}}}.$$
   But in the niche the stealth-to-honesty odds are the same under A and B ($p_{\mathrm{f}}e^{\eta\Delta R}/p_{\mathrm{h}}$); B only removes more visible cheating, and that mass is shared between honesty and stealth in the same proportion. So **under the same condition, B also gives more honesty and less total cheating than A.** "B is worse than A" holds for stealth only.

### Numerical Table

Take $p_{\mathrm{h}} = 0.85$, $p_{\mathrm{v}} = 0.14$, $p_{\mathrm{f}} = 0.01$, $\beta_{\mathrm{h}} = 1.0$, $\beta_{\mathrm{v}} = 0.05$ (95% detection on visible hacks), $\beta_{\mathrm{f}} = 0.75$ (25% detection on stealth), $\eta = 3.0$, and $C = 2.5$. Theorem 1 gives $\Delta R_{\mathrm{A}}^* = 0.257992$, $\Delta R_{\mathrm{dom, A}}^* = 1.576778$, and $\Delta R_{\mathrm{dom, B}}^* = 2.807845$ (asymptotic floor $0.833333$):

| $\Delta R$ | $\pi_{\mathrm{no}}(\Pi_{\mathrm{f}})$ | Cond. no mon. | $\pi_{\mathrm{A}}(\Pi_{\mathrm{f}})$ | Cond. A | $\pi_{\mathrm{A}}(\Pi_{\mathrm{h}})$ | $\pi_{\mathrm{B}}(\Pi_{\mathrm{f}})$ | $\pi_{\mathrm{B}}(\Pi_{\mathrm{h}})$ |
|---:|---:|---:|---:|---:|---:|---:|---:|
| $0.2000$ | $0.016221$ | $0.066667$ | $0.015593$ | $0.517241$ | $0.969854$ | $0.002821$ | $0.997043$ |
| **$0.2580$** | **$0.018451$** | $0.066667$ | **$0.018451$** | $0.517241$ | $0.964329$ | $0.003213$ | $0.996650$ |
| $0.8000$ | $0.044031$ | $0.066667$ | $0.081869$ | $0.517241$ | $0.841721$ | $0.010795$ | $0.989057$ |
| $1.2000$ | $0.057728$ | $0.066667$ | $0.198806$ | $0.517241$ | $0.615641$ | $0.026140$ | $0.973706$ |
| **$1.5768$** | $0.063492$ | $0.066667$ | **$0.340917$** | $0.517241$ | **$0.340894$** | $0.058966$ | $0.940876$ |
| $3.0000$ | $0.066620$ | $0.066667$ | $0.513526$ | $0.517241$ | $0.007182$ | **$0.606385$** | $0.393533$ |

*(The bold crossover rows `0.2580` and `1.5768` are evaluated at the 4-decimal rounded values of $\Delta R_{\mathrm{A}}^* = 0.257992$ and $\Delta R_{\mathrm{dom, A}}^* = 1.576778$, which explains the $2.3 \times 10^{-5}$ difference between $\pi_{\mathrm{A}}(\Pi_{\mathrm{f}}) = 0.340917$ and $\pi_{\mathrm{A}}(\Pi_{\mathrm{h}}) = 0.340894$.)*

Three regimes:
- **Below $\Delta R_{\mathrm{A}}^*$ ($0.20$):** conditional stealth among cheaters jumps nearly 8× under pure rejection ($6.7\% \to 51.7\%$), yet *absolute* stealth drops slightly ($1.62\% \to 1.56\%$).
- **Intermediate $\Delta R$ ($0.80$–$1.58$):** pure rejection amplifies absolute stealth and collapses honesty by $\Delta R = 1.5768$, while the penalty ($C=2.5$) keeps honesty above $94\%$.
- **High $\Delta R$ ($3.00$):** once Operator B crosses its threshold, $\pi_{\mathrm{B}}(\Pi_{\mathrm{f}}) = 60.6\%$ exceeds pure rejection's $51.4\%$, because Operator B nearly eliminates visible cheating; at the same time $\pi_{\mathrm{B}}(\Pi_{\mathrm{h}}) = 39.4\%$ against $0.7\%$ under A.

At fixed $\Delta R = 0.60$ (below Operator B's asymptotic floor $0.833333$), increasing $\eta$ from $0.5$ to $16.0$ drives pure-rejection honesty from $97.7\%$ down to **$0.40\%$** ($\pi_{\mathrm{A}}(\Pi_{\mathrm{f}}) = 51.5\%$), while the penalty ($C=2.5$) drives honesty up to **$99.93\%$** ($\pi_{\mathrm{B}}(\Pi_{\mathrm{f}}) = 0.07\%$). This contrast is the one that depends on the modelling of Operator A (Section 2).

In a *perfectly stealthy* niche ($\beta_{\mathrm{f}} = \beta_{\mathrm{h}} = 1.0$, $\beta_{\mathrm{v}} = 0.10$, $\eta = 2.0$, $\Delta R = 1.0$), the crossover is $C = 0.279214$: at $C = 0$, $\pi_{\mathrm{B}}(\Pi_{\mathrm{f}}) = 0.067487 < \pi_{\mathrm{A}}(\Pi_{\mathrm{f}}) = 0.071924$; at $C = 2.5$, $\pi_{\mathrm{B}}(\Pi_{\mathrm{f}}) = 0.079814 > 0.071924$ (unmonitored baseline $0.037731$). Over the same range, honesty under B rises from $0.776$ to $0.918$, crossing A's $0.827382$ exactly at $C = 0.279214$.

---

## 4. Three Escape Mechanisms—and What They Imply in Practice

**Theorem 2** gives three mechanisms against stealth selection. They are not an exhaustive classification: we claim neither that avoiding deployment-effective evasion requires one of them, nor that their failure produces evasion (under the penalty, a positive covariance between loop and audit survival need not make audit survival rise at high pressure: with $\beta_{\mathrm{loop}} \in \{0.1, 0.5, 0.9\}$ and $\beta_{\mathrm{audit}} \in \{0.1, 0.95, 0.45\}$ on three equiprobable atoms, the covariance is $+7/150$, yet audit survival goes $0.5 \to 0.543$ at $\eta(\Delta R + C) = 2$, then down to $0.459$ at $10$ and toward $0.45$).

1. **(R1) Prior KL barrier & multi-objective maintenance cost *(exact criterion for $\pi_{\mathrm{post}}(\Pi_{\mathrm{f}}) < \pi_{\mathrm{post}}(\Pi_{\mathrm{h}})$ in the three-stratum model)*:** honesty dominates stealth iff
   $$\log\frac{p_{\mathrm{h}}}{p_{\mathrm{f}}} > \begin{cases} \eta\,\Delta R_{\mathrm{net}} - \log(\beta_{\mathrm{h}}/\beta_{\mathrm{f}}) & \text{(Operator A)}, \\[4pt] \eta\big[\beta_{\mathrm{f}}\Delta R_{\mathrm{net}} - (\beta_{\mathrm{h}} - \beta_{\mathrm{f}})C\big] & \text{(Operator B)}, \end{cases}$$
   where $\Delta R_{\mathrm{net}} = \Delta R - \delta_{\mathrm{maint}}$. Formalizing `testingthewaters`, if obfuscation degrades auxiliary objectives enough that $\beta_{\mathrm{f}}\Delta R_{\mathrm{net}} < (\beta_{\mathrm{h}} - \beta_{\mathrm{f}})C$ (equivalently $\beta_{\mathrm{f}} < \frac{\beta_{\mathrm{h}} C}{\Delta R_{\mathrm{net}} + C}$ when $\Delta R_{\mathrm{net}} + C > 0$), stealth vanishes exponentially as $\eta \to \infty$ under Operator B (e.g., for $p_{\mathrm{h}}=0.90, p_{\mathrm{v}}=0.09, p_{\mathrm{f}}=0.01, \beta_{\mathrm{v}}=0.10, \beta_{\mathrm{f}}=0.90, \Delta R_{\mathrm{v}}=1.0, \delta_{\mathrm{maint}}=1.25, \eta=20, C=2.0$, honesty reaches $99.9998\%$). ("Unreachable" stealth, $p_{\mathrm{f}} = 0$, is outside the model's domain and only an informal limit.) *Takeaway:* keep KL regularization tight and co-train on auxiliary objectives that penalize obfuscated reasoning.

2. **(R2) Covariance between loop and audit survival—not placement:** on iso-reward cheaters $\mathcal{S} = \{R = \Delta R\}$ (assuming $\pi_0(\mathcal{S}) > 0$), pure rejection shifts audit evasion by exactly
   $$\mathbb{E}_{\pi_{\mathrm{A}}^{(\eta)}}[\beta_{\mathrm{audit}} \mid \mathcal{S}] - \mathbb{E}_{\pi_0}[\beta_{\mathrm{audit}} \mid \mathcal{S}] = \frac{\operatorname{Cov}_{\pi_0(\cdot\mid\mathcal{S})}(\beta_{\mathrm{loop}}, \beta_{\mathrm{audit}})}{\mathbb{E}_{\pi_0}[\beta_{\mathrm{loop}} \mid \mathcal{S}]},$$
   so audit evasion does not increase **iff** this base-law covariance is $\le 0$. Keeping the audit off-loop does **not** make it so: two detectors reading neighbouring features are positively correlated. Example: $\beta_{\mathrm{loop}} \in \{0.1, 0.9\}$, $\beta_{\mathrm{audit}} \in \{0.2, 0.8\}$ on two equiprobable atoms—audit survival rises from $1/2$ to $37/50$ although the audit never enters the loop. Nor is off-loop placement necessary in the model: an audit used inside the loop jointly with another detector can see its survival *fall* ($3/4 \to 7/12$ in the paper's example). Under Operator B, non-positive covariance is necessary but **not sufficient** (a zero-covariance example raises audit survival from $19/30$ to $0.770$, because $e^{ku}$ is convex); independence or negative association of $(\beta_{\mathrm{loop}}, \beta_{\mathrm{audit}})$ suffices. *Takeaway:* not plugging your highest-leverage audit monitors into the RL reward or rejection loop is already the published recommendation (Baker et al., 2025; Korbak et al., 2025, "Chain of Thought Monitorability"); the identity adds that it is not enough—what you need is an audit whose survival does not covary positively with the loop monitor's.

3. **(R3) Indistinguishable planted honeypots *(extended contextual model; excludes frequent cheaters only)*:** mix ordinary episodes $P_{\mathrm{ord}}$ (where the monitor may be 100% blind) with a fraction $\rho \in (0, 1)$ of verifiable trap episodes $P_{\mathrm{trap}}$ catching cheating with probability $\ge 1 - \varepsilon_{\mathrm{trap}}$, the honest policy being caught on neither. If $d_{\mathrm{TV}}(P_{\mathrm{ord}}, P_{\mathrm{trap}}) \le \delta_{\mathrm{ind}}$, any policy with ordinary cheating rate $\tau_{\mathrm{ord}} \ge \tau_{\min} > \delta_{\mathrm{ind}}$ triggers traps at rate $\ge \tau_{\mathrm{ord}} - \delta_{\mathrm{ind}}$ and is strictly worse than honesty under Operator B once
   $$C > C_{\mathrm{R3}}^* := \frac{(1 - \rho)\tau_{\min} + \rho\,\varepsilon_{\mathrm{trap}}(\tau_{\min} - \delta_{\mathrm{ind}})}{\rho(1 - \varepsilon_{\mathrm{trap}})(\tau_{\min} - \delta_{\mathrm{ind}})}\,\Delta R.$$
   For $\rho = 0.20, \varepsilon_{\mathrm{trap}} = 0.02, \delta_{\mathrm{ind}} = 0.05, \tau_{\min} = 0.20, \Delta R = 1.0$, any $C > 5.462585$ makes frequent cheating strictly worse than honesty—even with zero detection on ordinary episodes. This does **not** make honesty optimal: a policy cheating rarely ($\tau_{\mathrm{ord}} < \tau_{\min}$), concentrated on contexts where $P_{\mathrm{ord}} > P_{\mathrm{trap}}$, can still gain, and the attainable $\tau_{\min}$ only tends to $\delta_{\mathrm{ind}}$ as $C \to \infty$. (The link with R1's critical ratio holds for $\beta_{\mathrm{h}} = 1$.) *Takeaway:* distribution-matched honeypots deter frequent cheating; they do not close the rare-attack floor.

---

## 5. Limitations and Open Questions

This analysis uses a **static, non-parametric Gibbs equilibrium** with fixed strata. In particular:
1. **Generalization is outside the model.** Whether training against a detector teaches honesty or masking—how $p_{\mathrm{f}}$ and $\beta_{\mathrm{f}}$ move during training—is the heart of Halberstadt's question, and the model takes both as given.
2. **Modelling of rejection.** The contrast "pure rejection collapses, penalties hold" depends on Operator A; repeated rejection keeps a barrier (Section 2).
3. **Finite-time SGD/RL dynamics:** real post-training (PPO, GRPO, DPO) moves on a non-convex parameter manifold in finite steps, where implicit gradient bias and exploration noise modify reachability and $\delta_{\mathrm{maint}}(\theta_t)$ before any Gibbs equilibrium.
4. **Cross-monitor correlation:** detectors that share latent features have positive covariance, and optimizing against one erodes the other even if it stays off-loop; worst-case degradation under constrained coupling is open.
5. **Honeypot generation and rare-attack floor:** R3 converts detection into generative indistinguishability—harder as models become more situationally aware—and leaves rare attacks untouched.

**Prior work.** The two identities are classical (Price 1970; Robertson 1966; Fisher 1930). The Gibbs form of KL-regularized RL is Korbak, Perez and Buckley (2022). The recommendation to keep audit monitors out of training is already published (Baker et al. 2025; Korbak et al. 2025), and optimization against latent-space monitors is known to produce obfuscated activations (Bailey et al. 2024). What is offered here is the separation of the four quantities, the exact thresholds, and the counterexamples that delimit each claim.

Proofs, and a standard-library script that recomputes every number above and checks the counterexamples (partly in exact rational arithmetic; it is not a substitute for the proofs): [LINK_GITHUB_PAGE].
