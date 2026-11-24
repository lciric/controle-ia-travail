# When Does In-Loop Misalignment Filtering Select for Stealth?

Companion repository for the theoretical note **"When Does In-Loop Misalignment Filtering Select for Stealth? Exact Thresholds in a Gibbs Model of Post-Training"**. The note studies one deliberately simple model: the KL-regularized (Gibbs) equilibrium of post-training with fixed behaviour strata. It does not model generalisation: the stealthy stratum and its detection rate are inputs, not outcomes of learning.

## Summary of main results (within the model)

Policy space $\Pi = \Pi_{\mathrm{h}} \sqcup \Pi_{\mathrm{v}} \sqcup \Pi_{\mathrm{f}}$ (honest, visibly misaligned, stealthily misaligned). Two operators:

- **Operator A (pure rejection, a modelling choice):** $\pi_{\mathrm{A}} \propto \beta e^{\eta R}\pi_0$, i.e. the KL-regularized optimum for $R + \eta^{-1}\log\beta$. The filter is a bonus that fades as $\eta$ grows. Iterated rejection at every round ($\pi \propto \beta^T e^{T\eta_1 R}\pi_0$) behaves differently: its barrier does not fade.
- **Operator B (penalty $-C \le 0$):** $\pi_{\mathrm{B}} \propto e^{\eta[\beta R - (1-\beta)C]}\pi_0$.

1. **Theorem 1 — Selection under an imperfect filter**
   - Under A, for every survival function, the mean survival of cheaters rises by exactly $\operatorname{Var}(\beta)/\mathbb{E}[\beta]$ (a special case of the selection identities of Price and Robertson). Under B, conditional enrichment holds in the two-stratum model with equal rewards; it can fail with heterogeneous rewards.
   - Under A, honesty collapses as $\eta \to \infty$ for any $\beta_{\mathrm{f}} > 0$; the mass goes to cheaters, and the stealthy share of cheaters is $\beta_{\mathrm{f}}p_{\mathrm{f}}/(\beta_{\mathrm{v}}p_{\mathrm{v}}+\beta_{\mathrm{f}}p_{\mathrm{f}})$, possibly small.
   - Under B with $C > 0$ and $\beta_{\mathrm{f}} < \beta_{\mathrm{h}}$, a barrier $\frac{\beta_{\mathrm{h}} - \beta_{\mathrm{f}}}{\beta_{\mathrm{f}}} C$ survives as $\eta \to \infty$. In a perfectly stealthy niche ($\beta_{\mathrm{f}} = \beta_{\mathrm{h}} = 1 > \beta_{\mathrm{v}} > 0$), B puts more mass on stealth than A iff $\eta(\Delta R + C) > \frac{\log(1/\beta_{\mathrm{v}})}{1-\beta_{\mathrm{v}}}$, and then also more mass on honesty and less on cheating overall.

2. **Theorem 2 — Three levers (not an exhaustive classification)**
   - **(R1)** Exact condition, in this model, for honesty to dominate stealth: prior barrier $\log(p_{\mathrm{h}}/p_{\mathrm{f}})$ versus the net exponent after maintenance costs.
   - **(R2)** Audit decoupling is a condition on covariance, not on placement. Under A the audit survival of iso-reward cheaters changes by exactly $\operatorname{Cov}(\beta_{\mathrm{loop}}, \beta_{\mathrm{audit}})/\mathbb{E}[\beta_{\mathrm{loop}}]$; keeping the audit out of the loop does not make that covariance non-positive. Under B, non-positive covariance is necessary but not sufficient; independence or negative association suffices.
   - **(R3)** Indistinguishable planted traps exclude frequent cheaters ($\tau_{\mathrm{ord}} \ge \tau_{\min} > \delta_{\mathrm{ind}}$) once $C > C^*_{\mathrm{R3}}$; rare cheaters are not excluded.

## Reproduction

Python 3.10+, standard library only:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -W error verifier_exemples_papier_v3.py --out ./sortie-verification-v3
```

The script recomputes every table and example from the closed-form weights, checks the variance identity on one example in exact rational arithmetic, runs randomized consistency checks between the stated thresholds and the directly computed weights (these catch typos; they are not evidence beyond the proofs), and recomputes the exact counterexamples that delimit the claims. It writes its JSON to `--out`, never next to itself.

## Files

- Manuscript: `manuscrit-arxiv/main-v3.tex` (PDF link: `[LINK_PDF]`)
- Script and reference output: `verifier_exemples_papier_v3.py`, `exemples-verifies-papier-v3.json`
- LessWrong post: `[LINK_LESSWRONG_POST]`

## Prior work

The variance and covariance identities are classical (Fisher 1930; Robertson 1966; Price 1970). The Gibbs form of KL-regularized RL is known (Korbak, Perez & Buckley 2022). Keeping chain-of-thought monitors out of the training loop is an existing recommendation (Baker et al. 2025; Korbak et al. 2025).

## License

To be selected upon public release (e.g., MIT for code, CC-BY-4.0 for text).
