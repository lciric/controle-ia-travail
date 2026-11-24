# When Does In-Loop Misalignment Filtering Select for Stealth?

Companion repository for the theoretical note **"When Does In-Loop Misalignment Filtering Select for Stealth? Exact Phase Transitions and Escape Regimes in Post-Training"** (v4, revised after an independent audit and a fidelity review). It studies a restricted, static question: the KL-regularized (Gibbs) equilibrium of post-training with an in-loop misalignment detector, over *fixed* strata with fixed detection rates. How training reshapes the stealthy behaviours and their detectability is outside the model.

## Summary of Main Results

In a minimal three-stratum policy space $\Pi = \Pi_{\mathrm{h}} \sqcup \Pi_{\mathrm{v}} \sqcup \Pi_{\mathrm{f}}$ (honest, visibly misaligned, stealthily misaligned), comparing **Operator A** (pure rejection with resampling, *modelled* as conditioning the base law by the survival probability) with **Operator B** (KL-regularized policy update with interception penalty $-C \le 0$):

1. **Theorem 1 — Conditional enrichment and a rejection–penalty contrast**
   - Under Operator A, conditional stealth enrichment among misaligned trajectories follows from the variance identity $\mathbb{E}_{\pi_{\mathrm{A}}}[\beta \mid \Pi_{\mathrm{tr}}] - \mathbb{E}_{\pi_{\mathrm{no}}}[\beta \mid \Pi_{\mathrm{tr}}] = \operatorname{Var}(\beta)/\mathbb{E}[\beta] > 0$, a special case of the Price (1970) / Robertson (1966) covariance identity (Fisher's 1930 fundamental theorem for the trait "survival"). Under Operator B, enrichment holds for two cheating strata of equal reward, not in general.
   - Under Operator A, for any $\Delta R > 0$ and any $\beta_{\mathrm{f}} > 0$, honesty collapses as $\eta \to \infty$ ($\Delta R_{\mathrm{dom, A}}^*(\eta) \to 0$). The mass goes to cheating; the stealthy share among cheaters tends to $\beta_{\mathrm{f}}p_{\mathrm{f}}/(\beta_{\mathrm{v}}p_{\mathrm{v}}+\beta_{\mathrm{f}}p_{\mathrm{f}})$, not necessarily to one.
   - **This depends on modelling Operator A** as a reward bonus $\eta^{-1}\log\beta$ that vanishes with $\eta$ (equivalently, unmonitored training followed by a single rejection at inference); under repeated rejection at every round, the barrier does not vanish.
   - A penalty ($C > 0$) keeps a non-vanishing barrier $\Delta R_{\mathrm{dom, B}}^* \to \frac{\beta_{\mathrm{h}} - \beta_{\mathrm{f}}}{\beta_{\mathrm{f}}} C > 0$ when stealth is partially detected. In a perfectly stealthy niche ($\beta_{\mathrm{f}} = \beta_{\mathrm{h}} = 1 > \beta_{\mathrm{v}} > 0$), it yields more absolute stealth than pure rejection iff $\eta(\Delta R + C) > \frac{\log(1/\beta_{\mathrm{v}})}{1-\beta_{\mathrm{v}}}$—and exactly then also more honesty and less total cheating (the stealth-to-honesty odds are identical under A and B).

2. **Theorem 2 — Three escape mechanisms (not claimed exhaustive)**
   - **(R1) Prior KL barrier & multi-objective maintenance cost *(exact criterion for honesty to dominate stealth in the three-stratum model)*:** under Operator B, stealth decays exponentially as $\eta \to \infty$ whenever $\beta_{\mathrm{f}} < \frac{\beta_{\mathrm{h}} C}{\Delta R_{\mathrm{net}} + C}$.
   - **(R2) Covariance between loop and audit survival:** under Operator A, audit survival on iso-reward cheaters shifts by exactly $\operatorname{Cov}_{\pi_0}(\beta_{\mathrm{loop}}, \beta_{\mathrm{audit}})/\mathbb{E}_{\pi_0}[\beta_{\mathrm{loop}}]$, and does not increase iff that covariance is $\le 0$. Keeping the audit off-loop is neither sufficient nor necessary. Under Operator B, $\operatorname{Cov} \le 0$ is necessary but not sufficient; independence or negative association suffices. Not training against audit monitors is already published advice (Baker et al. 2025; Korbak et al. 2025).
   - **(R3) Indistinguishable planted honeypots *(extended contextual model)*:** traps at total variation distance $d_{\mathrm{TV}}(P_{\mathrm{ord}}, P_{\mathrm{trap}}) \le \delta_{\mathrm{ind}}$ make every *frequent* cheating policy ($\tau_{\mathrm{ord}} \ge \tau_{\min} > \delta_{\mathrm{ind}}$) strictly worse than honesty once $C > C_{\mathrm{R3}}^*$. Rare attacks are not excluded.

## Reproduction

Requires only Python 3.10+ (standard library only):

```bash
python3 -I verifier_exemples_papier_v4_correctif_1.py                 # prints JSON to stdout
python3 -I verifier_exemples_papier_v4_correctif_1.py --out out.json  # also writes out.json (never overwrites)
```

What the script does—and does not—show. **The results are carried by the written proofs; the script is not evidence for the general statements.** It:
- recomputes every table and numerical example of the manuscript, the post and the comment (floating point, six decimals);
- checks in exact rational arithmetic (`fractions.Fraction`): the variance-identity example ($\Delta = 37/150$); the Operator A amplification and dominance criteria on 5,000 rational instances with $E := e^{\eta\Delta R}$ treated as a free rational; the perfect-niche identities; the collapse limit $3/128$; and the covariance counterexamples for Regime R2 (including a positive covariance under which audit survival falls at high pressure);
- reruns floating-point regression checks from earlier versions, reported with their limits: the R2 family covers only an exactly counter-monotone pairing (a special case of negative association), and the R3 family evaluates the extremal policy, for which the bound is tight by construction.

## Files

- **Manuscript (LaTeX / PDF):** `manuscrit-arxiv/main-v4-correctif-1.tex` *(compile with `pdflatex main-v4-correctif-1.tex` twice; PDF link: `[LINK_PDF]`)*
- **Verification script & reference output:** `verifier_exemples_papier_v4_correctif_1.py` and `exemples-verifies-papier-v4-correctif-1.json`
- **LessWrong exposition:** `[LINK_LESSWRONG_POST]`

## References for prior work

Price (1970), *Selection and covariance*, Nature 227; Robertson (1966), Animal Production 8; Fisher (1930), *The Genetical Theory of Natural Selection*; Korbak, Perez & Buckley (2022), *RL with KL penalties is better viewed as Bayesian inference*, arXiv:2205.11275; Baker et al. (2025), arXiv:2503.11926; Korbak et al. (2025), *Chain of Thought Monitorability*, arXiv:2507.11473; Bailey et al. (2024), *Obfuscated Activations Bypass LLM Latent-Space Defenses*, arXiv:2412.09565.

## License

To be selected upon public release (e.g., MIT for code, CC-BY-4.0 for text).
