# When Does In-Loop Misalignment Filtering Select for Stealth?

Companion repository for the theoretical note **"When Does In-Loop Misalignment Filtering Select for Stealth? Exact Phase Transitions and Escape Regimes in Post-Training"**, analyzing the KL-regularized (Gibbs) equilibrium of in-loop misalignment detectors during post-training.

## Summary of Main Results

In a minimal 3-regime policy space $\Pi = \Pi_{\mathrm{h}} \sqcup \Pi_{\mathrm{v}} \sqcup \Pi_{\mathrm{f}}$ (honest, visibly misaligned, stealthily misaligned) comparing **Operator A** (pure rejection with resampling / *discard and try again*) against **Operator B** (KL-regularized policy update with interception penalty $-C \le 0$):

1. **Theorem 1 — Universal Conditional Enrichment & Rejection–Penalty Dilemma**
   - Conditional stealth enrichment among misaligned trajectories is universal under pure rejection, governed by the exact variance identity $\mathbb{E}_{\pi_{\mathrm{A}}}[\beta \mid \Pi_{\mathrm{tr}}] - \mathbb{E}_{\pi_{\mathrm{no}}}[\beta \mid \Pi_{\mathrm{tr}}] = \operatorname{Var}(\beta)/\mathbb{E}[\beta] > 0$.
   - Pure rejection has a fatal asymptotic vulnerability: for any $\Delta R > 0$ and any imperfect stealth detection ($\beta_{\mathrm{f}} > 0$), honesty collapses as optimization pressure $\eta \to \infty$ ($\Delta R_{\mathrm{dom, A}}^*(\eta) \to 0$).
   - Negative penalty ($C > 0$) establishes a non-vanishing asymptotic barrier $\Delta R_{\mathrm{dom, B}}^* \to \frac{\beta_{\mathrm{h}} - \beta_{\mathrm{f}}}{\beta_{\mathrm{f}}} C > 0$ when stealth is partially detected ($\beta_{\mathrm{f}} < \beta_{\mathrm{h}}$), **but** amplifies absolute stealth *strictly more than pure rejection* whenever a perfectly stealthy niche ($\beta_{\mathrm{f}} = \beta_{\mathrm{h}} = 1 > \beta_{\mathrm{v}} > 0$) exists and $\eta(\Delta R + C) > \frac{\log(1/\beta_{\mathrm{v}})}{1-\beta_{\mathrm{v}}}$.

2. **Theorem 2 — Three Escape Regimes (Necessary, Sufficient, and Constructive)**
   - **(R1) Prior KL barrier & multi-objective maintenance cost *(exact necessary and sufficient condition in the 3-regime model)*:** honesty dominates stealth ($\pi_{\mathrm{post}}(\Pi_{\mathrm{f}}) < \pi_{\mathrm{post}}(\Pi_{\mathrm{h}})$) iff $\log(p_{\mathrm{h}}/p_{\mathrm{f}})$ exceeds the net exponent after subtracting capability/auxiliary-objective costs $\delta_{\mathrm{maint}}$; under Operator B, stealth decays exponentially as $\eta \to \infty$ whenever $\beta_{\mathrm{f}} < \frac{\beta_{\mathrm{h}} C}{\Delta R_{\mathrm{net}} + C}$.
   - **(R2) Strict off-loop informational decoupling *(sufficient condition to preserve deployment audit power)*:** for an off-loop deployment monitor $M_{\mathrm{audit}}$, audit evasion shifts by $\operatorname{Cov}_{\pi_0}(\beta_{\mathrm{loop}}, \beta_{\mathrm{audit}})/\mathbb{E}_{\pi_0}[\beta_{\mathrm{loop}}]$ on iso-reward cheaters under Operator A, and is non-increasing under Operator B whenever $\beta_{\mathrm{loop}}$ and $\beta_{\mathrm{audit}}$ are independent or negatively associated.
   - **(R3) Indistinguishable planted honeypots *(sufficient constructive mechanism in the extended contextual model)*:** mixing verifiable trap episodes at total variation distance $d_{\mathrm{TV}}(P_{\mathrm{ord}}, P_{\mathrm{trap}}) \le \delta_{\mathrm{ind}}$ forces any persistent cheating policy ($\tau_{\mathrm{ord}} \ge \tau_{\min} > \delta_{\mathrm{ind}}$) below the critical false-negative ratio $\frac{\beta_{\mathrm{h}} C}{\Delta R_{\mathrm{net}} + C}$ and makes it strictly suboptimal once $C > C_{\mathrm{R3}}^*$.

## One-Command Reproduction

Requires only Python 3.10+ (standard library only, zero external dependencies):

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -W error verifier_exemples_papier_v2.py
```

This verifies:
- the exact rational variance identity (`fractions.Fraction`: $\Delta = 37/150$),
- **14,000** deterministic Monte Carlo instances (**0 counterexamples**) across Theorem 1 (10,000), the perfect-stealth niche inversion (2,000), Regime R2 (1,000), and Regime R3 (1,000),
- all numerical tables and escape-regime examples reported in the manuscript.

## Files

- **Manuscript (LaTeX / PDF):** `manuscrit-arxiv/main-v2.tex` *(compile with `pdflatex main-v2.tex` or `latexmk -pdf main-v2.tex`; PDF link: `[LINK_PDF]`)*
- **Verification script & outputs:** `verifier_exemples_papier_v2.py` and `exemples-verifies-papier-v2.json`
- **LessWrong exposition:** `[LINK_LESSWRONG_POST]`

## License

To be selected upon public release (e.g., MIT for code, CC-BY-4.0 for text).
