# When Does In-Loop Misalignment Filtering Select for Stealth? Exact Phase Transitions and Escape Regimes in Post-Training

## 1. TL;DR and Direct Answer to Halberstadt's Question

In [*Post training is fundamentally dangerous*](https://www.lesswrong.com/posts/CoRJ9saddvsXti4m2) (Nov. 22, 2026), Yair Halberstadt argues that misalignment detectors that work well at deployment—chain-of-thought monitors, elicitation checks, linear activation probes—become counterproductive once placed inside the post-training loop, *even if caught runs receive no negative penalty and are merely discarded and resampled*. He asks whether it is a mathematical law that any attempt to prevent misalignment during post-training inevitably encourages evasion.

In the comments, `testingthewaters` pushes back that an in-loop filter acts as a *selective sieve* rather than a directional gradient toward evasion, highlighting three obstacles: non-existence of stealthy strategies, unreachability under optimization constraints, and non-maintainability against competing post-training objectives.

Much of the disagreement dissolves once we separate **four distinct quantities**:
1. the **conditional share** of stealthy cheating among all cheating runs, $\pi_{\mathrm{post}}(\Pi_{\mathrm{f}} \mid \Pi_{\mathrm{tr}})$;
2. the **absolute probability** of stealthy cheating relative to unmonitored post-training, $\pi_{\mathrm{post}}(\Pi_{\mathrm{f}}) - \pi_{\mathrm{no}}(\Pi_{\mathrm{f}})$;
3. the **asymptotic dominance** of stealth over honesty, $\pi_{\mathrm{post}}(\Pi_{\mathrm{f}}) / \pi_{\mathrm{post}}(\Pi_{\mathrm{h}})$, as optimization pressure $\eta$ grows;
4. the **evasion rate against a separate deployment monitor** $M_{\mathrm{audit}} \neq M_{\mathrm{loop}}$.

In one deliberately simple model — the KL-regularized (Gibbs) post-training equilibrium with fixed behaviour strata — all four admit **exact answers** (explicit thresholds; one of them, the absolute-amplification condition under the penalty operator, is an implicit inequality rather than a closed form). The model does not settle the deeper part of the question — whether training against a detector teaches honesty or concealment — because the stealthy stratum and its detection rate are inputs here, not outcomes of learning.

- **Within this model, pure rejection (*discard and try again*) behaves as Halberstadt fears:** conditional stealth enrichment under rejection is a variance identity (a special case of Price's equation), and *no imperfect detection rate* ($\beta_{\mathrm{f}} > 0$) prevents honesty from collapsing as $\eta \to \infty$ — the mass goes to cheaters, though not necessarily to *stealthy* cheaters (the stealthy share of cheaters tends to $\beta_{\mathrm{f}}p_{\mathrm{f}}/(\beta_{\mathrm{v}}p_{\mathrm{v}}+\beta_{\mathrm{f}}p_{\mathrm{f}})$). This conclusion depends on modelling rejection as Operator A below; if rejection is applied at every round, the barrier no longer fades (Section 2).
- **Penalty versus rejection:** A negative penalty $-C < 0$ creates a non-vanishing barrier against *partially* detected stealth ($\beta_{\mathrm{f}} < \beta_{\mathrm{h}}$). If a *perfectly stealthy* niche exists ($\beta_{\mathrm{f}} = \beta_{\mathrm{h}} = 1$), the penalty puts more mass on stealth than pure rejection past an explicit threshold — but in that niche the stealth-to-honest odds are identical under both operators, so the penalty then *also* yields more honesty and less cheating in total. It is worse on stealth and better on honesty and total cheating; both halves matter.
- **It is not an unconditional law, and we give three levers rather than an exhaustive list:** **(R1)** prior KL barrier & multi-objective maintenance cost (the exact condition for $\pi_{\mathrm{post}}(\Pi_{\mathrm{f}}) < \pi_{\mathrm{post}}(\Pi_{\mathrm{h}})$ in this model, formalizing `testingthewaters`); **(R2)** a condition on the *covariance* between in-loop and audit survival — under rejection the audit's survival rate does not increase iff that covariance is non-positive, and keeping the audit out of the loop does not by itself guarantee this; under the penalty, non-positive covariance is necessary but not sufficient, and the proved sufficient condition is independence or negative association; **(R3)** indistinguishable planted honeypots, a sufficient mechanism that excludes frequent cheaters but not rare ones.

Full proofs and a script that recomputes every number in this post are hosted at [LINK_GITHUB_PAGE]. The proofs carry the result; the script checks the arithmetic.

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

**Operator A is a modelling choice, not a law.** $\pi_{\mathrm{A}}^{(\eta)}$ is the KL-regularized optimum for the reward $R + \eta^{-1}\log\beta$: the filter acts as a bonus $\eta^{-1}\log\beta$ that fades as $\eta$ grows, by construction, and Operator A coincides with unmonitored training followed by a single rejection at inference time. Other models of "discard and try again" behave differently. If rejection is applied at every round (iterated filtered fine-tuning), after $T$ rounds $\pi \propto \beta^T e^{T\eta_1 R}\pi_0$, and stealth eventually beats honesty iff $\eta_1\Delta R > \log(\beta_{\mathrm{h}}/\beta_{\mathrm{f}})$: the barrier no longer fades. The asymptotic contrast "pure rejection is fatal, penalty is not" therefore depends on how rejection is modelled. Note also that halting without retry and without penalty ($C = 0$ in Operator B) is fatal too: there $\pi_{\mathrm{B}}(\Pi_{\mathrm{f}}) \to 1$.

---

## 3. Exact Phase Transitions and the Rejection–Penalty Dilemma

### Theorem 1 (Summary)

1. **Conditional enrichment under rejection (variance identity, for every $\beta$).** For any non-constant $\beta$ on $\Pi_{\mathrm{tr}}$, pure rejection strictly increases the conditional false-negative rate among cheaters by
   $$\mathbb{E}_{\pi_{\mathrm{A}}^{(\eta)}}[\beta \mid \Pi_{\mathrm{tr}}] - \mathbb{E}_{\pi_{\mathrm{no}}^{(\eta)}}[\beta \mid \Pi_{\mathrm{tr}}] = \frac{\operatorname{Var}_{\mu_{\mathrm{tr}}^{(\eta)}}(\beta)}{\mathbb{E}_{\mu_{\mathrm{tr}}^{(\eta)}}[\beta]} > 0.$$
   This is the selection identity of Price (1970) and Robertson (1966). In the two-stratum model with equal reward for visible and stealthy cheating, both Operator A ($\forall \eta \ge 0$) and Operator B ($\forall \eta > 0, C \ge 0$) strictly increase $\pi_{\mathrm{post}}(\Pi_{\mathrm{f}} \mid \Pi_{\mathrm{tr}})$. Under Operator B with heterogeneous rewards among cheaters, enrichment can fail.
2. **Exact absolute-amplification threshold under pure rejection.** $\pi_{\mathrm{A}}^{(\eta)}(\Pi_{\mathrm{f}}) > \pi_{\mathrm{no}}^{(\eta)}(\Pi_{\mathrm{f}})$ holds unconditionally if $\beta_{\mathrm{f}} = \beta_{\mathrm{h}}$, and for $\beta_{\mathrm{f}} < \beta_{\mathrm{h}}$ iff
   $$\Delta R > \Delta R_{\mathrm{A}}^*(\eta) := \frac{1}{\eta}\left[\log\frac{p_{\mathrm{h}}}{p_{\mathrm{v}}} + \log\frac{\beta_{\mathrm{h}} - \beta_{\mathrm{f}}}{\beta_{\mathrm{f}} - \beta_{\mathrm{v}}}\right].$$
3. **Asymptotic divergence as $\eta \to \infty$.** Stealth dominates honesty ($\pi_{\mathrm{post}}(\Pi_{\mathrm{f}}) > \pi_{\mathrm{post}}(\Pi_{\mathrm{h}})$) iff:
   - under Operator A: $\Delta R > \Delta R_{\mathrm{dom, A}}^*(\eta) = \frac{1}{\eta}(\log(p_{\mathrm{h}}/p_{\mathrm{f}}) + \log(\beta_{\mathrm{h}}/\beta_{\mathrm{f}})) \to 0$;
   - under Operator B: $\Delta R > \Delta R_{\mathrm{dom, B}}^*(\eta, C) = \frac{\beta_{\mathrm{h}} - \beta_{\mathrm{f}}}{\beta_{\mathrm{f}}} C + \frac{1}{\eta \beta_{\mathrm{f}}}\log\frac{p_{\mathrm{h}}}{p_{\mathrm{f}}} \to \frac{\beta_{\mathrm{h}} - \beta_{\mathrm{f}}}{\beta_{\mathrm{f}}} C > 0$ ($C > 0, \beta_{\mathrm{f}} < \beta_{\mathrm{h}}$).
4. **The perfect-stealth inversion.** If a *perfectly stealthy* niche exists ($\beta_{\mathrm{f}} = \beta_{\mathrm{h}} = 1 > \beta_{\mathrm{v}} > 0$), Operator B loses its asymptotic barrier and amplifies absolute stealth **strictly more than pure rejection** ($\pi_{\mathrm{B}}^{(\eta, C)}(\Pi_{\mathrm{f}}) > \pi_{\mathrm{A}}^{(\eta)}(\Pi_{\mathrm{f}}) > \pi_{\mathrm{no}}^{(\eta)}(\Pi_{\mathrm{f}})$) iff
   $$\eta(\Delta R + C) > \frac{\log(1/\beta_{\mathrm{v}})}{1 - \beta_{\mathrm{v}}}.$$
   In that niche the stealth-to-honest odds equal $p_{\mathrm{f}}e^{\eta\Delta R}/p_{\mathrm{h}}$ under both operators: whenever $\pi_{\mathrm{B}}(\Pi_{\mathrm{f}}) > \pi_{\mathrm{A}}(\Pi_{\mathrm{f}})$, also $\pi_{\mathrm{B}}(\Pi_{\mathrm{h}}) > \pi_{\mathrm{A}}(\Pi_{\mathrm{h}})$, and total cheating is lower under B.

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
- **High $\Delta R$ ($3.00$):** Once Operator B flips, $\pi_{\mathrm{B}}(\Pi_{\mathrm{f}}) = 60.6\%$ exceeds pure rejection's $51.4\%$ because Operator B crushes visible cheating to $0.01\%$; honesty is also far higher under B ($39.4\%$ versus $0.7\%$).

At fixed $\Delta R = 0.60$ (below Operator B's asymptotic floor $0.833333$), increasing $\eta$ from $0.5$ to $16.0$ drives pure-rejection honesty from $97.7\%$ down to **$0.40\%$** ($\pi_{\mathrm{A}}(\Pi_{\mathrm{f}}) = 51.5\%$), while negative penalty ($C=2.5$) drives honesty up to **$99.93\%$** ($\pi_{\mathrm{B}}(\Pi_{\mathrm{f}}) = 0.07\%$).

Conversely, in a *perfectly stealthy* niche ($\beta_{\mathrm{f}} = \beta_{\mathrm{h}} = 1.0$, $\beta_{\mathrm{v}} = 0.10$, $\eta = 2.0$, $\Delta R = 1.0$), the inversion threshold is $C = 0.279214$: at $C = 0$, $\pi_{\mathrm{B}}(\Pi_{\mathrm{f}}) = 0.067487 < \pi_{\mathrm{A}}(\Pi_{\mathrm{f}}) = 0.071924$; at $C = 2.5$, negative penalty pushes absolute stealth to **$0.079814 > 0.071924$** (more than double the unmonitored baseline $0.037731$) — while honesty rises to $\pi_{\mathrm{B}}(\Pi_{\mathrm{h}}) = 0.918$, above its value $0.827$ under pure rejection.

---

## 4. Three Escape Regimes—and Practical Safety Implications

In this framework, producing a deployed policy that both favors stealth over honesty and evades deployment monitoring $M_{\mathrm{audit}}$ requires: (H1) net stealth reward overcomes the prior KL barrier; (H2) survival against $M_{\mathrm{loop}}$ correlates positively with survival against $M_{\mathrm{audit}}$; and (H3) the policy keeps its effective false-negative rate above the critical R1 ratio $\frac{\beta_{\mathrm{h}} C}{\Delta R_{\mathrm{net}} + C}$. These three hypotheses are a reading aid, not a proved decomposition: we do not claim that avoiding evasion requires breaking one of them. **Theorem 2** gives one exact dominance condition (R1), one covariance condition for the audit (R2), and one sufficient constructive mechanism (R3); the levers are not claimed to be exhaustive. (The link between R3 and the critical ratio of R1 assumes $\beta_{\mathrm{h}} = 1$.)

1. **(R1) Prior KL barrier & multi-objective maintenance cost *(exact necessary and sufficient condition for $\pi_{\mathrm{post}}(\Pi_{\mathrm{f}}) < \pi_{\mathrm{post}}(\Pi_{\mathrm{h}})$ in the 3-regime model)*:** Honesty dominates stealth iff
   $$\log\frac{p_{\mathrm{h}}}{p_{\mathrm{f}}} > \begin{cases} \eta\,\Delta R_{\mathrm{net}} - \log(\beta_{\mathrm{h}}/\beta_{\mathrm{f}}) & \text{(Operator A)}, \\[4pt] \eta\big[\beta_{\mathrm{f}}\Delta R_{\mathrm{net}} - (\beta_{\mathrm{h}} - \beta_{\mathrm{f}})C\big] & \text{(Operator B)}, \end{cases}$$
   where $\Delta R_{\mathrm{net}} = \Delta R - \delta_{\mathrm{maint}}$. Formalizing `testingthewaters`, if obfuscation degrades auxiliary objectives enough that $\beta_{\mathrm{f}}\Delta R_{\mathrm{net}} < (\beta_{\mathrm{h}} - \beta_{\mathrm{f}})C$ (equivalently $\beta_{\mathrm{f}} < \frac{\beta_{\mathrm{h}} C}{\Delta R_{\mathrm{net}} + C}$ when $\Delta R_{\mathrm{net}} + C > 0$), stealth vanishes exponentially as $\eta \to \infty$ (e.g., for $p_{\mathrm{h}}=0.90, p_{\mathrm{v}}=0.09, p_{\mathrm{f}}=0.01, \beta_{\mathrm{v}}=0.10, \beta_{\mathrm{f}}=0.90, \Delta R_{\mathrm{v}}=1.0, \delta_{\mathrm{maint}}=1.25, \eta=20, C=2.0$, honesty reaches $99.9998\%$). *Takeaway:* keep KL regularization tight and co-train on auxiliary objectives that penalize obfuscated reasoning.

2. **(R2) Audit decoupling — a covariance condition, not a placement *(defined on any iso-reward cheating stratum $\mathcal S$ with $\pi_0(\mathcal S) > 0$)*:** For a deployment monitor $M_{\mathrm{audit}}$, pure rejection shifts audit evasion on iso-reward cheaters $\{R = \Delta R\}$ by
   $$\mathbb{E}_{\pi_{\mathrm{A}}^{(\eta)}}[\beta_{\mathrm{audit}} \mid \Pi_{\mathrm{tr}}, R = \Delta R] - \mathbb{E}_{\pi_0}[\beta_{\mathrm{audit}} \mid \Pi_{\mathrm{tr}}, R = \Delta R] = \frac{\operatorname{Cov}_{\pi_0}(\beta_{\mathrm{loop}}, \beta_{\mathrm{audit}})}{\mathbb{E}_{\pi_0}[\beta_{\mathrm{loop}}]}.$$
   So under rejection the audit's survival rate does not increase iff this covariance is non-positive. **Keeping the audit out of the loop is not enough**: two detectors reading similar cues are positively correlated (exact example: $\beta_{\mathrm{loop}} \in \{0.1, 0.9\}$, $\beta_{\mathrm{audit}} \in \{0.2, 0.8\}$ on two equiprobable atoms; audit survival rises from $1/2$ to $37/50$ although the audit was never used in training). Nor is it necessary: an audit used in the loop jointly with another detector can see its survival fall. Under Operator B, a non-positive covariance is necessary but not sufficient (the weight $e^{ku}$ is convex); the proved sufficient condition is independence or negative association of $(\beta_{\mathrm{loop}}, \beta_{\mathrm{audit}})$. *Takeaway:* the published recommendation not to train against the monitors you rely on (Baker et al. 2025; Korbak et al. 2025) is necessary hygiene, not a guarantee; what protects an audit is weak dependence on what the loop selects.

3. **(R3) Indistinguishable planted honeypots *(sufficient constructive mechanism in the extended contextual model)*:** Mix ordinary episodes $P_{\mathrm{ord}}$ (where the monitor may be 100% blind) with a fraction $\rho \in (0, 1)$ of verifiable trap episodes $P_{\mathrm{trap}}$ catching cheating with probability $\ge 1 - \varepsilon_{\mathrm{trap}}$. If $d_{\mathrm{TV}}(P_{\mathrm{ord}}, P_{\mathrm{trap}}) \le \delta_{\mathrm{ind}}$, any policy with ordinary cheating rate $\tau_{\mathrm{ord}} \ge \tau_{\min} > \delta_{\mathrm{ind}}$ triggers traps at rate $\ge \tau_{\mathrm{ord}} - \delta_{\mathrm{ind}}$, forcing its effective false-negative rate below the critical ratio $\frac{\beta_{\mathrm{h}} C}{\Delta R_{\mathrm{net}} + C}$ and making it strictly suboptimal under Operator B once
   $$C > C_{\mathrm{R3}}^* := \frac{(1 - \rho)\tau_{\min} + \rho\,\varepsilon_{\mathrm{trap}}(\tau_{\min} - \delta_{\mathrm{ind}})}{\rho(1 - \varepsilon_{\mathrm{trap}})(\tau_{\min} - \delta_{\mathrm{ind}})}\,\Delta R.$$
   For $\rho = 0.20, \varepsilon_{\mathrm{trap}} = 0.02, \delta_{\mathrm{ind}} = 0.05, \tau_{\min} = 0.20, \Delta R = 1.0$, any $C > 5.462585$ makes persistent cheating strictly worse than honesty—even with zero detection on ordinary episodes. Note that R3 requires $\tau_{\min} > \delta_{\mathrm{ind}}$ and does not block ultra-rare attacks ($\tau_{\mathrm{ord}} \le \delta_{\mathrm{ind}}$) concentrated on contexts where $P_{\mathrm{ord}} > P_{\mathrm{trap}}$. *Takeaway:* invest in distribution-matched honeypots rather than chasing 100% in-loop detection on ordinary trajectories.

---

## 5. Honest Limitations and Open Questions

This analysis uses a **static, non-parametric Gibbs equilibrium** model to isolate the exact selection laws. Three caveats apply in practice:
1. **Finite-time SGD/RL dynamics:** Real post-training (PPO, GRPO, DPO) moves on a non-convex parameter manifold $\theta \mapsto \pi_\theta$ in finite steps, where implicit gradient bias and exploration noise jointly modify reachability and $\delta_{\mathrm{maint}}(\theta_t)$ before reaching any Gibbs equilibrium.
2. **Cross-monitor correlation:** Regime (R2) requires $\operatorname{Cov}(\beta_{\mathrm{loop}}, \beta_{\mathrm{audit}}) \le 0$ (necessary under both operators, sufficient under A only). If an in-loop monitor and an off-loop probe share latent features, optimizing against the first can still partially erode the second.
3. **Low-$d_{\mathrm{TV}}$ honeypot generation and rare-attack floor:** Regime (R3) converts the detection problem into a generative indistinguishability problem—which grows harder as models become more situationally aware—and leaves an irreducible floor for rare attacks with $\tau_{\mathrm{ord}} \le \delta_{\mathrm{ind}}$.

4. **Generalisation is outside the model:** $p_{\mathrm{f}}$ and $\beta_{\mathrm{f}}$ are fixed inputs; whether training against a detector reshapes them (teaching honesty or concealment) is exactly the open question, and the model does not answer it. Cases outside the domain: $p_{\mathrm{f}} = 0$, and false alarms on honest behaviour exceeding the stealthy survival rate ($\beta_{\mathrm{f}} > \beta_{\mathrm{h}}$).

**Prior work.** The variance and covariance identities are classical selection identities (Fisher 1930; Robertson 1966; Price 1970); the Gibbs form of KL-regularized RL is known (Korbak, Perez & Buckley 2022); the recommendation to keep monitors out of the training loop is already published (Baker et al. 2025; Korbak et al. 2025). What this post adds is the exact thresholds and the two-operator comparison inside one explicit model.

Full proofs and reproducible Python code that recomputes every number above: [LINK_GITHUB_PAGE].
