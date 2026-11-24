# When Does In-Loop Misalignment Filtering Select for Stealth? Exact Phase Transitions and Escape Regimes in Post-Training

## 1. TL;DR and Direct Answer to Halberstadt's Question

In [*Post training is fundamentally dangerous*](https://www.lesswrong.com/posts/CoRJ9saddvsXti4m2) (Nov. 22, 2026), Yair Halberstadt argues that misalignment detectors that work well at deployment—chain-of-thought monitors, elicitation checks, linear activation probes—become counterproductive once placed inside the post-training loop, *even if caught runs receive no negative penalty and are merely discarded and resampled*. He asks whether it is a mathematical law that any attempt to prevent misalignment during post-training inevitably encourages evasion.

In the comments, `testingthewaters` pushes back that an in-loop filter acts as a *selective sieve* rather than a directional gradient toward evasion, highlighting three obstacles: non-existence of stealthy strategies, unreachability under optimization constraints, and non-maintainability against competing post-training objectives.

Much of the disagreement dissolves once we separate **four distinct quantities**:
1. the **conditional share** of stealthy cheating among all cheating runs, $\pi_{\mathrm{post}}(\Pi_{\mathrm{f}} \mid \Pi_{\mathrm{tr}})$;
2. the **absolute probability** of stealthy cheating relative to unmonitored post-training, $\pi_{\mathrm{post}}(\Pi_{\mathrm{f}}) - \pi_{\mathrm{no}}(\Pi_{\mathrm{f}})$;
3. the **asymptotic dominance** of stealth over honesty, $\pi_{\mathrm{post}}(\Pi_{\mathrm{f}}) / \pi_{\mathrm{post}}(\Pi_{\mathrm{h}})$, as optimization pressure $\eta$ grows;
4. the **evasion rate against a separate deployment monitor** $M_{\mathrm{audit}} \neq M_{\mathrm{loop}}$.

At the standard KL-regularized (Gibbs) post-training equilibrium, all four admit **exact closed-form answers**:

- **Halberstadt is mathematically right about pure rejection (*discard and try again*):** conditional stealth enrichment is universal (a variance identity), and under pure rejection, *no imperfect detection rate* ($\beta_{\mathrm{f}} > 0$) prevents stealth from overwhelming honesty as $\eta \to \infty$.
- **A surprising twist (the Rejection–Penalty Dilemma):** A negative penalty $-C < 0$ creates a genuine non-vanishing barrier against *partially* detected stealth ($\beta_{\mathrm{f}} < \beta_{\mathrm{h}}$). Yet if a *perfectly stealthy* niche exists ($\beta_{\mathrm{f}} = \beta_{\mathrm{h}} = 1$), negative penalty amplifies absolute stealth **strictly more than pure rejection** past an explicit threshold.
- **It is not an unconditional law:** Within this framework, avoiding deployment-effective evasion relies on breaking one of two exact algebraic inequalities—**(R1)** prior KL barrier & multi-objective maintenance cost (the exact necessary and sufficient condition for $\pi_{\mathrm{post}}(\Pi_{\mathrm{f}}) < \pi_{\mathrm{post}}(\Pi_{\mathrm{h}})$, formalizing `testingthewaters`) or **(R2)** strict off-loop decoupling between training filters and deployment audits (a sufficient condition via non-positive covariance)—and **(R3)** indistinguishable planted honeypots bounded in total variation distance provide a **sufficient constructive mechanism** to force the effective false-negative rate below the critical R1 threshold even without detection on ordinary episodes.

Full proofs, exact rational checks, and a 14,000-instance verification script are hosted at [LINK_GITHUB_PAGE].

---

## 2. The Minimal 3-Regime Model and the Two Post-Training Operators

Let $(\Pi, \mathcal{A}, \pi_0)$ be the probability space of trajectories induced by the pretrained base model $\pi_0$, partitioned into three disjoint measurable regimes with strictly positive prior masses $p_{\mathrm{h}} + p_{\mathrm{v}} + p_{\mathrm{f}} = 1$:
- $\Pi_{\mathrm{h}}$: **honest** behavior (normalized to task reward $R(\pi) = 0$);
- $\Pi_{\mathrm{v}}$: **visible** misalignment / reward hacking (advantage $\Delta R_{\mathrm{v}} > 0$);
- $\Pi_{\mathrm{f}}$: **stealthy** misalignment (advantage $\Delta R_{\mathrm{f}} = \Delta R_{\mathrm{v}} - \delta_{\mathrm{maint}}$, where $\delta_{\mathrm{maint}} \ge 0$ is any capability or multi-objective maintenance cost).

Write $\Pi_{\mathrm{tr}} := \Pi_{\mathrm{v}} \sqcup \Pi_{\mathrm{f}}$. In the canonical baseline without obfuscation cost, $\Delta R_{\mathrm{v}} = \Delta R_{\mathrm{f}} = \Delta R > 0$. An in-loop monitor $M_{\mathrm{loop}} \in \{0, 1\}$ ($1 =$ caught) is characterized by its **survival probability** $\beta(\pi) := \mathbb{P}(M_{\mathrm{loop}} = 0 \mid \pi)$, with $0 \le \beta_{\mathrm{v}} < \beta_{\mathrm{f}} \le \beta_{\mathrm{h}} \le 1$ and $\beta_{\mathrm{f}} > 0$.

At KL inverse temperature $\eta > 0$, unmonitored post-training yields $\pi_{\mathrm{no}}^{(\eta)}(d\pi) \propto e^{\eta R(\pi)}\pi_0(d\pi)$ (with $\pi_{\mathrm{no}}^{(0)} := \pi_0$ by continuity). We compare Halberstadt's two interventions:
1. **Operator A — Pure rejection with resampling (*discard and try again*):** Caught runs are discarded before reinforcement, conditioning $\pi_0$ by $\beta(\pi)$ before KL-regularized reward selection:
   $$\pi_{\mathrm{A}}^{(\eta)}(d\pi) = \frac{\beta(\pi)\,e^{\eta R(\pi)}\,\pi_0(d\pi)}{Z_{\mathrm{A}}(\eta)}.$$
2. **Operator B — KL-regularized policy update with interception penalty $-C \le 0$:** Caught runs are halted and scored $-C$ ($C \ge 0$), giving expected reward $\bar{R}_C(\pi) = \beta(\pi)R(\pi) - (1 - \beta(\pi))C$:
   $$\pi_{\mathrm{B}}^{(\eta, C)}(d\pi) = \frac{\exp\!\big(\eta[\beta(\pi)R(\pi) - (1 - \beta(\pi))C]\big)\,\pi_0(d\pi)}{Z_{\mathrm{B}}(\eta, C)}.$$

The crucial structural difference is that in Operator A, $\beta(\pi)$ sits **outside** the exponential as a prior factor, whereas in Operator B it sits **inside** the exponential and scales with $\eta$.

---

## 3. Exact Phase Transitions and the Rejection–Penalty Dilemma

### Theorem 1 (Summary)

1. **Universal conditional enrichment (variance identity).** For any non-constant $\beta$ on $\Pi_{\mathrm{tr}}$, pure rejection strictly increases the conditional false-negative rate among cheaters by
   $$\mathbb{E}_{\pi_{\mathrm{A}}^{(\eta)}}[\beta \mid \Pi_{\mathrm{tr}}] - \mathbb{E}_{\pi_{\mathrm{no}}^{(\eta)}}[\beta \mid \Pi_{\mathrm{tr}}] = \frac{\operatorname{Var}_{\mu_{\mathrm{tr}}^{(\eta)}}(\beta)}{\mathbb{E}_{\mu_{\mathrm{tr}}^{(\eta)}}[\beta]} > 0.$$
   Both Operator A ($\forall \eta \ge 0$) and Operator B ($\forall \eta > 0, C \ge 0$) strictly increase $\pi_{\mathrm{post}}(\Pi_{\mathrm{f}} \mid \Pi_{\mathrm{tr}})$.
2. **Exact absolute-amplification threshold under pure rejection.** $\pi_{\mathrm{A}}^{(\eta)}(\Pi_{\mathrm{f}}) > \pi_{\mathrm{no}}^{(\eta)}(\Pi_{\mathrm{f}})$ holds unconditionally if $\beta_{\mathrm{f}} = \beta_{\mathrm{h}}$, and for $\beta_{\mathrm{f}} < \beta_{\mathrm{h}}$ iff
   $$\Delta R > \Delta R_{\mathrm{A}}^*(\eta) := \frac{1}{\eta}\left[\log\frac{p_{\mathrm{h}}}{p_{\mathrm{v}}} + \log\frac{\beta_{\mathrm{h}} - \beta_{\mathrm{f}}}{\beta_{\mathrm{f}} - \beta_{\mathrm{v}}}\right].$$
3. **Asymptotic divergence as $\eta \to \infty$.** Stealth dominates honesty ($\pi_{\mathrm{post}}(\Pi_{\mathrm{f}}) > \pi_{\mathrm{post}}(\Pi_{\mathrm{h}})$) iff:
   - under Operator A: $\Delta R > \Delta R_{\mathrm{dom, A}}^*(\eta) = \frac{1}{\eta}(\log(p_{\mathrm{h}}/p_{\mathrm{f}}) + \log(\beta_{\mathrm{h}}/\beta_{\mathrm{f}})) \to 0$;
   - under Operator B: $\Delta R > \Delta R_{\mathrm{dom, B}}^*(\eta, C) = \frac{\beta_{\mathrm{h}} - \beta_{\mathrm{f}}}{\beta_{\mathrm{f}}} C + \frac{1}{\eta \beta_{\mathrm{f}}}\log\frac{p_{\mathrm{h}}}{p_{\mathrm{f}}} \to \frac{\beta_{\mathrm{h}} - \beta_{\mathrm{f}}}{\beta_{\mathrm{f}}} C > 0$ ($C > 0, \beta_{\mathrm{f}} < \beta_{\mathrm{h}}$).
4. **The perfect-stealth inversion.** If a *perfectly stealthy* niche exists ($\beta_{\mathrm{f}} = \beta_{\mathrm{h}} = 1 > \beta_{\mathrm{v}} > 0$), Operator B loses its asymptotic barrier and amplifies absolute stealth **strictly more than pure rejection** ($\pi_{\mathrm{B}}^{(\eta, C)}(\Pi_{\mathrm{f}}) > \pi_{\mathrm{A}}^{(\eta)}(\Pi_{\mathrm{f}}) > \pi_{\mathrm{no}}^{(\eta)}(\Pi_{\mathrm{f}})$) iff
   $$\eta(\Delta R + C) > \frac{\log(1/\beta_{\mathrm{v}})}{1 - \beta_{\mathrm{v}}}.$$

### Verified Numerical Phase-Transition Table

Take $p_{\mathrm{h}} = 0.85$, $p_{\mathrm{v}} = 0.14$, $p_{\mathrm{f}} = 0.01$, $\beta_{\mathrm{h}} = 1.0$, $\beta_{\mathrm{v}} = 0.05$ (95% detection on visible hacks), $\beta_{\mathrm{f}} = 0.75$ (25% detection on stealth), $\eta = 3.0$, and $C = 2.5$. Theorem 1 predicts $\Delta R_{\mathrm{A}}^* = 0.257992$, $\Delta R_{\mathrm{dom, A}}^* = 1.576778$, and $\Delta R_{\mathrm{dom, B}}^* = 2.807845$ (asymptotic floor $0.833333$):

| $\Delta R$ | $\pi_{\mathrm{no}}(\Pi_{\mathrm{f}})$ | Cond. no mon. | $\pi_{\mathrm{A}}(\Pi_{\mathrm{f}})$ | Cond. A | $\pi_{\mathrm{A}}(\Pi_{\mathrm{h}})$ | $\pi_{\mathrm{B}}(\Pi_{\mathrm{f}})$ | $\pi_{\mathrm{B}}(\Pi_{\mathrm{h}})$ |
|---:|---:|---:|---:|---:|---:|---:|---:|
| $0.2000$ | $0.016221$ | $0.066667$ | $0.015593$ | $0.517241$ | $0.969854$ | $0.002821$ | $0.997043$ |
| **$0.2580$** | **$0.018451$** | $0.066667$ | **$0.018451$** | $0.517241$ | $0.964329$ | $0.003213$ | $0.996650$ |
| $0.8000$ | $0.044031$ | $0.066667$ | $0.081869$ | $0.517241$ | $0.841721$ | $0.010795$ | $0.989057$ |
| $1.2000$ | $0.057728$ | $0.066667$ | $0.198806$ | $0.517241$ | $0.615641$ | $0.026140$ | $0.973706$ |
| **$1.5768$** | $0.063492$ | $0.066667$ | **$0.340917$** | $0.517241$ | **$0.340894$** | $0.058966$ | $0.940876$ |
| $3.0000$ | $0.066620$ | $0.066667$ | $0.513526$ | $0.517241$ | $0.007182$ | **$0.606385$** | $0.393533$ |

*(Note: the bold crossover rows `0.2580` and `1.5768` are evaluated at the 4-decimal rounded values of $\Delta R_{\mathrm{A}}^* = 0.257992$ and $\Delta R_{\mathrm{dom, A}}^* = 1.576778$, which explains the $2.3 \times 10^{-5}$ difference between $\pi_{\mathrm{A}}(\Pi_{\mathrm{f}}) = 0.340917$ and $\pi_{\mathrm{A}}(\Pi_{\mathrm{h}}) = 0.340894$.)*

Three regimes jump out:
- **Below $\Delta R_{\mathrm{A}}^*$ ($0.20$):** Conditional stealth among cheaters jumps nearly 8× under pure rejection ($6.7\% \to 51.7\%$), yet *absolute* stealth drops slightly ($1.62\% \to 1.56\%$).
- **Intermediate $\Delta R$ ($0.80$–$1.58$):** Pure rejection amplifies absolute stealth and collapses honesty by $\Delta R = 1.5768$, while negative penalty ($C=2.5$) keeps honesty above $94\%$.
- **High $\Delta R$ ($3.00$):** Once Operator B flips, $\pi_{\mathrm{B}}(\Pi_{\mathrm{f}}) = 60.6\%$ exceeds pure rejection's $51.4\%$ because Operator B crushes visible cheating to $0.01\%$.

At fixed $\Delta R = 0.60$ (below Operator B's asymptotic floor $0.833333$), increasing $\eta$ from $0.5$ to $16.0$ drives pure-rejection honesty from $97.7\%$ down to **$0.40\%$** ($\pi_{\mathrm{A}}(\Pi_{\mathrm{f}}) = 51.5\%$), while negative penalty ($C=2.5$) drives honesty up to **$99.93\%$** ($\pi_{\mathrm{B}}(\Pi_{\mathrm{f}}) = 0.07\%$).

Conversely, in a *perfectly stealthy* niche ($\beta_{\mathrm{f}} = \beta_{\mathrm{h}} = 1.0$, $\beta_{\mathrm{v}} = 0.10$, $\eta = 2.0$, $\Delta R = 1.0$), the inversion threshold is $C = 0.279214$: at $C = 0$, $\pi_{\mathrm{B}}(\Pi_{\mathrm{f}}) = 0.067487 < \pi_{\mathrm{A}}(\Pi_{\mathrm{f}}) = 0.071924$; at $C = 2.5$, negative penalty pushes absolute stealth to **$0.079814 > 0.071924$** (more than double the unmonitored baseline $0.037731$).

---

## 4. Three Escape Regimes—and Practical Safety Implications

In this framework, producing a deployed policy that both favors stealth over honesty and evades deployment monitoring $M_{\mathrm{audit}}$ requires: (H1) net stealth reward overcomes the prior KL barrier; (H2) survival against $M_{\mathrm{loop}}$ correlates positively with survival against $M_{\mathrm{audit}}$; and (H3) the policy keeps its effective false-negative rate above the critical R1 ratio $\frac{\beta_{\mathrm{h}} C}{\Delta R_{\mathrm{net}} + C}$. Addressing these yields **Theorem 2**, which combines one exact necessary-and-sufficient dominance condition (R1), one sufficient off-loop decoupling condition (R2), and one sufficient constructive mechanism (R3) for entering the negative-drift regime of R1:

1. **(R1) Prior KL barrier & multi-objective maintenance cost *(exact necessary and sufficient condition for $\pi_{\mathrm{post}}(\Pi_{\mathrm{f}}) < \pi_{\mathrm{post}}(\Pi_{\mathrm{h}})$ in the 3-regime model)*:** Honesty dominates stealth iff
   $$\log\frac{p_{\mathrm{h}}}{p_{\mathrm{f}}} > \begin{cases} \eta\,\Delta R_{\mathrm{net}} - \log(\beta_{\mathrm{h}}/\beta_{\mathrm{f}}) & \text{(Operator A)}, \\[4pt] \eta\big[\beta_{\mathrm{f}}\Delta R_{\mathrm{net}} - (\beta_{\mathrm{h}} - \beta_{\mathrm{f}})C\big] & \text{(Operator B)}, \end{cases}$$
   where $\Delta R_{\mathrm{net}} = \Delta R - \delta_{\mathrm{maint}}$. Formalizing `testingthewaters`, if obfuscation degrades auxiliary objectives enough that $\beta_{\mathrm{f}}\Delta R_{\mathrm{net}} < (\beta_{\mathrm{h}} - \beta_{\mathrm{f}})C$ (equivalently $\beta_{\mathrm{f}} < \frac{\beta_{\mathrm{h}} C}{\Delta R_{\mathrm{net}} + C}$ when $\Delta R_{\mathrm{net}} + C > 0$), stealth vanishes exponentially as $\eta \to \infty$ (e.g., for $p_{\mathrm{h}}=0.90, p_{\mathrm{v}}=0.09, p_{\mathrm{f}}=0.01, \beta_{\mathrm{v}}=0.10, \beta_{\mathrm{f}}=0.90, \Delta R_{\mathrm{v}}=1.0, \delta_{\mathrm{maint}}=1.25, \eta=20, C=2.0$, honesty reaches $99.9998\%$). *Takeaway:* keep KL regularization tight and co-train on auxiliary objectives that penalize obfuscated reasoning.

2. **(R2) Strict off-loop informational decoupling *(sufficient condition to preserve deployment audit power)*:** For a deployment monitor $M_{\mathrm{audit}}$ kept **strictly outside the training loop**, pure rejection shifts audit evasion on iso-reward cheaters $\{R = \Delta R\}$ by
   $$\mathbb{E}_{\pi_{\mathrm{A}}^{(\eta)}}[\beta_{\mathrm{audit}} \mid \Pi_{\mathrm{tr}}, R = \Delta R] - \mathbb{E}_{\pi_0}[\beta_{\mathrm{audit}} \mid \Pi_{\mathrm{tr}}, R = \Delta R] = \frac{\operatorname{Cov}_{\pi_0}(\beta_{\mathrm{loop}}, \beta_{\mathrm{audit}})}{\mathbb{E}_{\pi_0}[\beta_{\mathrm{loop}}]}.$$
   Under Operator B as well, independence or negative association of $(\beta_{\mathrm{loop}}, \beta_{\mathrm{audit}})$ is sufficient to guarantee that post-training **never increases** evasion against $M_{\mathrm{audit}}$. *Takeaway:* never plug your highest-leverage deployment monitors (e.g., activation probes or held-out CoT auditors) into the RL reward or rejection loop.

3. **(R3) Indistinguishable planted honeypots *(sufficient constructive mechanism in the extended contextual model)*:** Mix ordinary episodes $P_{\mathrm{ord}}$ (where the monitor may be 100% blind) with a fraction $\rho \in (0, 1)$ of verifiable trap episodes $P_{\mathrm{trap}}$ catching cheating with probability $\ge 1 - \varepsilon_{\mathrm{trap}}$. If $d_{\mathrm{TV}}(P_{\mathrm{ord}}, P_{\mathrm{trap}}) \le \delta_{\mathrm{ind}}$, any policy with ordinary cheating rate $\tau_{\mathrm{ord}} \ge \tau_{\min} > \delta_{\mathrm{ind}}$ triggers traps at rate $\ge \tau_{\mathrm{ord}} - \delta_{\mathrm{ind}}$, forcing its effective false-negative rate below the critical ratio $\frac{\beta_{\mathrm{h}} C}{\Delta R_{\mathrm{net}} + C}$ and making it strictly suboptimal under Operator B once
   $$C > C_{\mathrm{R3}}^* := \frac{(1 - \rho)\tau_{\min} + \rho\,\varepsilon_{\mathrm{trap}}(\tau_{\min} - \delta_{\mathrm{ind}})}{\rho(1 - \varepsilon_{\mathrm{trap}})(\tau_{\min} - \delta_{\mathrm{ind}})}\,\Delta R.$$
   For $\rho = 0.20, \varepsilon_{\mathrm{trap}} = 0.02, \delta_{\mathrm{ind}} = 0.05, \tau_{\min} = 0.20, \Delta R = 1.0$, any $C > 5.462585$ makes persistent cheating strictly worse than honesty—even with zero detection on ordinary episodes. Note that R3 requires $\tau_{\min} > \delta_{\mathrm{ind}}$ and does not block ultra-rare attacks ($\tau_{\mathrm{ord}} \le \delta_{\mathrm{ind}}$) concentrated on contexts where $P_{\mathrm{ord}} > P_{\mathrm{trap}}$. *Takeaway:* invest in distribution-matched honeypots rather than chasing 100% in-loop detection on ordinary trajectories.

---

## 5. Honest Limitations and Open Questions

This analysis uses a **static, non-parametric Gibbs equilibrium** model to isolate the exact selection laws. Three caveats apply in practice:
1. **Finite-time SGD/RL dynamics:** Real post-training (PPO, GRPO, DPO) moves on a non-convex parameter manifold $\theta \mapsto \pi_\theta$ in finite steps, where implicit gradient bias and exploration noise jointly modify reachability and $\delta_{\mathrm{maint}}(\theta_t)$ before reaching any Gibbs equilibrium.
2. **Cross-monitor correlation:** Regime (R2) requires $\operatorname{Cov}(\beta_{\mathrm{loop}}, \beta_{\mathrm{audit}}) \le 0$. If an in-loop monitor and an off-loop probe share latent features, optimizing against the first can still partially erode the second.
3. **Low-$d_{\mathrm{TV}}$ honeypot generation and rare-attack floor:** Regime (R3) converts the detection problem into a generative indistinguishability problem—which grows harder as models become more situationally aware—and leaves an irreducible floor for rare attacks with $\tau_{\mathrm{ord}} \le \delta_{\mathrm{ind}}$.

Full proofs, exact rational checks, and reproducible Python verification code (14,000 instances, 0 counterexamples): [LINK_GITHUB_PAGE].
