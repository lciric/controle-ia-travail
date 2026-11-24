### 1. Repository Slug & GitHub Description

- **Repository slug:** `github.com/lciric/in-loop-stealth-equilibrium`
- **GitHub description:** Concise analytical note and reproducible verification code characterizing the static three-state KL-regularized (Gibbs) equilibrium of in-loop misalignment filtering during post-training.

---

### 2. Mathematical & Typographical Audit

1. **Theorem numbering mismatch caught and fixed:** In `main-v2.tex`, `\newtheorem{proposition}[theorem]{Proposition}` and `\newtheorem{remark}[theorem]{Remark}` shared the `theorem` counter, causing `thm:escape` to compile as **Theorem 3** and the duality remark as **Remark 4**, contradicting the hardcoded **Theorem 2** in the Abstract and `README-v2.md`. Giving `proposition` and `remark` independent counters restores exact consistency (`Theorem 1`, `Proposition 1`, `Theorem 2`, `Remark 1`).
2. **Rényi $D_\infty$ remark verification (0 errors):** Suppose $e^{D_\infty(P_{\mathrm{ord}} \,\|\, P_{\mathrm{trap}})} = \operatorname{ess\,sup}_x \frac{dP_{\mathrm{ord}}}{dP_{\mathrm{trap}}}(x) \le M < \infty$ (hence $P_{\mathrm{ord}} \ll P_{\mathrm{trap}}$ and $M \ge 1$). For any measurable cheating probability $\tau_\pi : \mathcal{X} \to [0,1]$,
   $$\tau_{\mathrm{ord}}(\pi) = \int \tau_\pi \frac{dP_{\mathrm{ord}}}{dP_{\mathrm{trap}}}\,dP_{\mathrm{trap}} \le M\tau_{\mathrm{trap}}(\pi) \implies \tau_{\mathrm{trap}}(\pi) \ge M^{-1}\tau_{\mathrm{ord}}(\pi).$$
   Whenever $C > \frac{(1-\rho)M + \rho\varepsilon_{\mathrm{trap}}}{\rho(1-\varepsilon_{\mathrm{trap}})}\Delta R$, we automatically have $C > \frac{\varepsilon_{\mathrm{trap}}}{1-\varepsilon_{\mathrm{trap}}}\Delta R$ (since $(1-\rho)M > 0$), so $\varepsilon_{\mathrm{trap}}\Delta R - (1-\varepsilon_{\mathrm{trap}})C < 0$. Hence, for every policy with $\tau_{\mathrm{ord}}(\pi) > 0$,
   $$\E_{P_{\mathrm{mix}}}[\bar{R}_C(\pi)] \le \tau_{\mathrm{ord}}(\pi)M^{-1}\Big[\big((1-\rho)M + \rho\varepsilon_{\mathrm{trap}}\big)\Delta R - \rho(1-\varepsilon_{\mathrm{trap}})C\Big] < 0,$$
   and any policy with $\tau_{\mathrm{ord}}(\pi) = 0 < \tau_{\mathrm{trap}}(\pi)$ also has strictly negative payoff. The rare-attack floor is eliminated completely, and at $M = 1$ the threshold coincides with~\eqref{eq:R3} at $\delta_{\mathrm{ind}} = 0$.
3. **Perfect-stealth niche honesty-vs-stealth tension verified:** When $\beta_{\mathrm{f}} = \beta_{\mathrm{h}} = 1 > \beta_{\mathrm{v}} > 0$, unnormalized weights satisfy $w_{\mathrm{h}}^{\mathrm{B}} = w_{\mathrm{h}}^{\mathrm{A}} = p_{\mathrm{h}}$ and $w_{\mathrm{f}}^{\mathrm{B}} = w_{\mathrm{f}}^{\mathrm{A}} = p_{\mathrm{f}} e^{\eta \Delta R}$, while only $w_{\mathrm{v}}^{\mathrm{B}} = p_{\mathrm{v}} e^{\eta\Delta R} e^{-\eta(1-\beta_{\mathrm{v}})(\Delta R+C)}$ differs from $w_{\mathrm{v}}^{\mathrm{A}} = \beta_{\mathrm{v}} p_{\mathrm{v}} e^{\eta\Delta R}$. Thus $Z_{\mathrm{B}} < Z_{\mathrm{A}} \iff \eqref{eq:inversion}$, strictly raising **both** $\pi_{\mathrm{B}}(\Pi_{\mathrm{h}})$ (from $0.827382$ to $0.918135$ at $C=2.5$ in Table 3) **and** $\pi_{\mathrm{B}}(\Pi_{\mathrm{f}})$ (from $0.071924$ to $0.079814$) by $Z_{\mathrm{A}}/Z_{\mathrm{B}} > 1$.
4. **Minor mathematical edge cases tightened:**
   - Added `(for $p_{\mathrm{h}} > p_{\mathrm{f}}$)` in Proposition 1(1) so the denominator $\log(p_{\mathrm{h}}/p_{\mathrm{f}}) + \log(\beta_{\mathrm{h}}/\beta_{\mathrm{f}})$ cannot vanish.
   - Clarified the quantifier order in the proof of Theorem 2(3): the upper bound is strictly decreasing in $\tau_{\mathrm{ord}}(\pi)$ *whenever $C > C_{\mathrm{R3}}^*$* (since $C_{\mathrm{R3}}^* \ge \frac{1-\rho+\rho\varepsilon_{\mathrm{trap}}}{\rho(1-\varepsilon_{\mathrm{trap}})}\Delta R$ makes the slope strictly negative).
   - Aligned the critical-ratio reference in Theorem 2(3) to $\frac{C}{\Delta R + C}$ (the $\beta_{\mathrm{h}} = 1, \delta_{\mathrm{maint}} = 0$ case of R1).
   - Verified every threshold and numerical table entry (exact rational variance identity $37/150$, Tables 1–3, R1 and R3 worked examples): **0 mathematical errors**.
5. **All 6 `pdflatex` Overfull/Underfull `\hbox` warnings diagnosed and fixed** (plus `\usepackage{microtype}`):
   - *Line 35 (`\maketitle`/`\thanks`)*: unbreakable `\texttt{verifier\_exemples\_papier\_v2.py}` -> concise author/footnote using `\texttt{verify\_examples.py}`.
   - *Line 174 (`9.91pt`)*: side-by-side fractions in Proof of Theorem 1(3) -> stacked `align*`.
   - *Lines 189–190 (`33.90pt`)*: inline formula in Proof of Proposition 1 -> display equation.
   - *Lines 205–206 (`28.03pt`)*: unbreakable `\Delta \DKL(\Pi_{\mathrm{f}} \,\|\, \Pi_{\mathrm{h}}; \pi_0)` after long bold header in Theorem 2(1) -> reorder definitions so `\Delta R_{\mathrm{net}}` precedes `\Delta \DKL`.
   - *Lines 237–238 (`1.89pt`)*: wide inline quotients in Proof of Theorem 2(2) -> concise prose without wide inline fractions.
   - *Lines 252–253 (`98.52pt`)*: long unbreakable filename in Section 5 -> `\texttt{verify\_examples.py}` in a concise paragraph.
   - *Lines 330–331 (`63.13pt`)*: unbreakable `\Cov_{\nu_0}(\beta_{\mathrm{loop}}, \beta_{\mathrm{audit}})` at end of line in Section 6 -> rephrased so covariance lands cleanly mid-line.

---

### 3. Complete `README.md`

```markdown
# When Does In-Loop Misalignment Filtering Select for Stealth?

Companion repository for the concise analytical note **"When Does In-Loop Misalignment Filtering Select for Stealth? Exact Phase Transitions and Escape Regimes in Post-Training"** by **Lazar Ciric**, responding to Yair Halberstadt's November 22, 2026 LessWrong question (*"Post training is fundamentally dangerous"*, post `CoRJ9saddvsXti4m2`).

This note characterizes the **static three-state KL-regularized (Gibbs) equilibrium** of placing an imperfect misalignment detector inside the post-training loop, separating four selection quantities often conflated in informal discussion: conditional stealth share among misaligned policies, absolute stealth probability relative to unmonitored post-training, asymptotic dominance over honesty, and evasion against an off-loop deployment monitor.

## Summary of Main Results

In a three-regime policy space $\Pi = \Pi_{\mathrm{h}} \sqcup \Pi_{\mathrm{v}} \sqcup \Pi_{\mathrm{f}}$ (honest, visibly misaligned, stealthily misaligned), we compare **Operator A** (rejection-conditioned post-training relative to the accepted prior $\pi_0^{\mathrm{acc}}$, or equivalently post-hoc rejection) against **Operator B** (KL-regularized optimization with interception penalty $-C \le 0$):

1. **Theorem 1 — Universal Conditional Enrichment & Rejection–Penalty Dilemma**
   - Conditional stealth enrichment among misaligned policies is universal under pure rejection, governed by the exact variance identity $\mathbb{E}_{\pi_{\mathrm{A}}}[\beta \mid \Pi_{\mathrm{tr}}] - \mathbb{E}_{\pi_{\mathrm{no}}}[\beta \mid \Pi_{\mathrm{tr}}] = \operatorname{Var}(\beta)/\mathbb{E}[\beta] > 0$.
   - Pure rejection collapses to stealth as optimization pressure $\eta \to \infty$ for any $\Delta R > 0$ and any imperfect stealth detection ($\beta_{\mathrm{f}} > 0$), since $\Delta R_{\mathrm{dom, A}}^*(\eta) \to 0$.
   - A negative penalty ($C > 0$) establishes a non-vanishing asymptotic barrier $\Delta R_{\mathrm{dom, B}}^* \to \frac{\beta_{\mathrm{h}} - \beta_{\mathrm{f}}}{\beta_{\mathrm{f}}} C > 0$ when stealth is partially detected ($\beta_{\mathrm{f}} < \beta_{\mathrm{h}}$). However, when a perfectly stealthy niche exists ($\beta_{\mathrm{f}} = \beta_{\mathrm{h}} = 1 > \beta_{\mathrm{v}} > 0$) and $\eta(\Delta R + C) > \frac{\log(1/\beta_{\mathrm{v}})}{1-\beta_{\mathrm{v}}}$, Operator B suppresses $\Pi_{\mathrm{v}}$ and raises honesty ($\pi_{\mathrm{B}}(\Pi_{\mathrm{h}}) > \pi_{\mathrm{A}}(\Pi_{\mathrm{h}})$), **yet** strictly increases the absolute probability of undetected stealthy misalignment ($\pi_{\mathrm{B}}(\Pi_{\mathrm{f}}) > \pi_{\mathrm{A}}(\Pi_{\mathrm{f}})$)—increasing expected deployment harm whenever visible misalignment would be caught prior to deployment whereas $\Pi_{\mathrm{f}}$ causes unmitigated harm.

2. **Theorem 2 — Three Escape Regimes**
   - **(R1) Prior KL barrier & maintenance cost *(necessary and sufficient in the three-regime model)*:** honesty dominates stealth iff $\log(p_{\mathrm{h}}/p_{\mathrm{f}})$ exceeds the net exponent after subtracting capability/maintenance costs $\delta_{\mathrm{maint}}$; under Operator B, stealth decays exponentially as $\eta \to \infty$ whenever $\beta_{\mathrm{f}} < \frac{\beta_{\mathrm{h}} C}{\Delta R_{\mathrm{net}} + C}$.
   - **(R2) Off-loop informational decoupling *(sufficient to preserve deployment audit power)*:** for an off-loop audit monitor $M_{\mathrm{audit}}$, audit evasion shifts by $\operatorname{Cov}_{\nu_0}(\beta_{\mathrm{loop}}, \beta_{\mathrm{audit}})/\mathbb{E}_{\nu_0}[\beta_{\mathrm{loop}}]$ on iso-reward cheaters under Operator A, and is non-increasing under Operator B whenever $(\beta_{\mathrm{loop}}, \beta_{\mathrm{audit}})$ are independent or negatively associated.
   - **(R3) Indistinguishable planted honeypots *(constructive mechanism in an extended contextual model)*:** mixing verifiable trap episodes at total variation distance $d_{\mathrm{TV}}(P_{\mathrm{ord}}, P_{\mathrm{trap}}) \le \delta_{\mathrm{ind}}$ forces any policy with ordinary cheating rate $\tau_{\mathrm{ord}} \ge \tau_{\min} > \delta_{\mathrm{ind}}$ to have negative expected reward once $C > C_{\mathrm{R3}}^*$; strengthening indistinguishability to bounded one-sided Rényi max-divergence $e^{D_\infty(P_{\mathrm{ord}} \| P_{\mathrm{trap}})} \le M < \infty$ eliminates the rare-attack floor altogether once $C > \frac{(1-\rho)M + \rho\varepsilon_{\mathrm{trap}}}{\rho(1-\varepsilon_{\mathrm{trap}})}\Delta R$.

## Reproduction

Requires Python 3.10+ (standard library only, zero external dependencies):

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -W error verify_examples.py
```

The script regenerates [verified_examples.json](./verified_examples.json), reproducing all phase-transition tables and worked examples in the note alongside exact rational and numerical sanity checks.

## Repository Contents

- **Manuscript (PDF):** [main.pdf](./main.pdf)
- **Manuscript (LaTeX source):** [main.tex](./main.tex) *(compile with `pdflatex main.tex`)*
- **Verification script:** [verify_examples.py](./verify_examples.py)
- **Generated numerical outputs:** [verified_examples.json](./verified_examples.json)
- **License:** [LICENSE](./LICENSE)

## License

Dual-licensed under **MIT** (for code) and **CC-BY-4.0** (for text and manuscript); see [LICENSE](./LICENSE).
```

---

### 4. Exact Surgical Edits for `main.tex` (from `main-v2.tex`)

#### Edit 1 — Add `microtype`, fix theorem/proposition/remark counters, set author `Lazar Ciric`
```latex
<<< OLD
\usepackage{hyperref}
\usepackage{xcolor}
===
\usepackage{hyperref}
\usepackage{xcolor}
\usepackage{microtype}
>>> NEW
```

```latex
<<< OLD
\newtheorem{theorem}{Theorem}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{remark}[theorem]{Remark}
===
\newtheorem{theorem}{Theorem}
\newtheorem{proposition}{Proposition}
\newtheorem{remark}{Remark}
>>> NEW
```

```latex
<<< OLD
\author{[Author Name]\thanks{Preprint draft prepared for review. Standalone companion verification code: \texttt{verifier\_exemples\_papier\_v2.py}.}}
===
\author{Lazar Ciric\thanks{Companion verification code: \texttt{verify\_examples.py}.}}
>>> NEW
```

#### Edit 2 — Abstract (scope framing, niche harm nuance, remove Monte Carlo boasting)
```latex
<<< OLD
\begin{abstract}
When a misalignment detector---such as a chain-of-thought monitor or activation probe---is placed inside the post-training loop, does it inevitably select for stealthy evasion, even when intercepted runs are merely discarded and resampled without negative reward? We analyze this question at the Kullback--Leibler (KL)-regularized Gibbs equilibrium over a three-regime policy space partitioning honest behavior, visible misalignment, and stealthy misalignment. Separating four quantities often conflated in informal debate---conditional stealth enrichment, absolute stealth amplification relative to unmonitored post-training, asymptotic dominance over honesty, and evasion against a separate deployment monitor---we establish two exact results. \textbf{Theorem~1} proves that conditional stealth enrichment is universal via an exact variance identity, derives sharp closed-form phase-transition thresholds for both pure rejection with resampling (Operator~A) and KL-regularized negative penalties (Operator~B), and exposes a \emph{Rejection--Penalty Dilemma}: pure rejection always collapses to stealth as optimization pressure $\eta \to \infty$ whenever any stealthy false-negative rate $\beta_{\mathrm{f}} > 0$ exists, whereas a negative penalty $-C < 0$ creates a non-vanishing asymptotic barrier against partially detected stealth ($\beta_{\mathrm{f}} < \beta_{\mathrm{h}}$) yet amplifies absolute stealth \emph{strictly more than pure rejection} whenever a perfectly stealthy niche ($\beta_{\mathrm{f}} = \beta_{\mathrm{h}} = 1$) exists and $\eta(\Delta R + C) > \log(1/\beta_{\mathrm{v}})/(1-\beta_{\mathrm{v}})$. \textbf{Theorem~2} establishes three escape regimes within this framework: (R1)~the exact necessary and sufficient condition for suppressing stealth dominance via prior KL accessibility barriers and multi-objective maintenance costs, (R2)~a sufficient condition for preserving deployment audit power through strict off-loop informational decoupling (non-positive covariance / negative association), and (R3)~a sufficient constructive mechanism using indistinguishable planted honeypots bounded in total variation distance to force the effective false-negative rate below the critical R1 threshold. Every theorem and numerical table is verified in exact rational arithmetic and across $14{,}000$ randomized finite-world test instances with zero counterexamples.
\end{abstract}
===
\begin{abstract}
When a misalignment detector---such as a chain-of-thought monitor or activation probe---is placed inside the post-training loop, does it inevitably select for stealthy evasion, even when intercepted runs are merely discarded and resampled without negative reward? This concise analytical note characterizes the static Kullback--Leibler (KL)-regularized Gibbs equilibrium over a three-regime policy space partitioning honest behavior, visible misalignment, and stealthy misalignment. Separating four quantities often conflated in informal debate---conditional stealth enrichment, absolute stealth amplification relative to unmonitored post-training, asymptotic dominance over honesty, and evasion against an off-loop deployment monitor---we establish two closed-form results. \textbf{Theorem~1} proves that conditional stealth enrichment is universal via an exact variance identity, derives sharp phase-transition thresholds for rejection-conditioned post-training (Operator~A) and KL-regularized negative penalties (Operator~B), and exposes a \emph{Rejection--Penalty Dilemma}: pure rejection collapses to stealth as optimization pressure $\eta \to \infty$ whenever any stealthy false-negative rate $\beta_{\mathrm{f}} > 0$ exists, whereas a negative penalty $-C < 0$ creates a non-vanishing asymptotic barrier against partially detected stealth ($\beta_{\mathrm{f}} < \beta_{\mathrm{h}}$), yet---when a perfectly stealthy niche ($\beta_{\mathrm{f}} = \beta_{\mathrm{h}} = 1 > \beta_{\mathrm{v}} > 0$) exists and $\eta(\Delta R + C) > \log(1/\beta_{\mathrm{v}})/(1-\beta_{\mathrm{v}})$---increases honesty while strictly amplifying absolute undetected stealth relative to pure rejection. \textbf{Theorem~2} characterizes three escape regimes: (R1)~the exact necessary and sufficient condition for honesty to dominate stealth via prior KL accessibility barriers and maintenance costs, (R2)~a sufficient condition for preserving deployment audit power via off-loop informational decoupling, and (R3)~a constructive mechanism using indistinguishable planted honeypots to drive the effective false-negative rate below the critical R1 threshold.
\end{abstract}
>>> NEW
```

#### Edit 3 — Introduction (concise analytical scope, remove Contribution #4)
```latex
<<< OLD
This note resolves the question exactly at the standard KL-regularized (Gibbs) post-training equilibrium, connecting it to strategic classification~\cite{hardt2016}, partial monitoring~\cite{bartok2014}, and AI control~\cite{greenblatt2023,griffin2024,terekhov2025,ukaisi2025}. Our main contributions are:
\begin{enumerate}
  \item \textbf{Disambiguation of four selection metrics:} conditional stealth share among cheaters, absolute stealth probability relative to unmonitored post-training, asymptotic dominance of stealth over honesty as $\eta \to \infty$, and evasion against an off-loop deployment monitor $M_{\mathrm{audit}}$.
  \item \textbf{Exact phase transitions and the Rejection--Penalty Dilemma (Theorem~\ref{thm:selection}):} we prove a universal variance identity for conditional enrichment, derive exact thresholds for absolute amplification and dominance under both pure rejection (Operator~A) and KL-regularized penalties (Operator~B), and show that while pure rejection is asymptotically fatal whenever $\beta_{\mathrm{f}} > 0$, negative penalties backfire harder than pure rejection when a perfectly stealthy niche exists.
  \item \textbf{Three escape regimes (Theorem~\ref{thm:escape}):} we establish (R1)~the exact necessary and sufficient condition for honesty to dominate stealth via prior KL barriers and multi-objective maintenance costs, (R2)~a sufficient condition for preserving deployment audit power via off-loop informational decoupling (exact covariance identity under Operator~A; independence or negative association under Operator~B), and (R3)~a sufficient constructive mechanism via planted honeypots at bounded total variation distance $\dTV(P_{\mathrm{ord}}, P_{\mathrm{trap}}) \le \delta_{\mathrm{ind}}$ that forces the effective false-negative rate below the critical R1 threshold.
  \item \textbf{Reproducible verification:} all identities and phase-transition tables are verified by a standalone script in exact rational arithmetic (\texttt{fractions.Fraction}) and across $14{,}000$ randomized finite-world instances with zero counterexamples.
\end{enumerate}
===
This concise analytical note resolves the question in the static three-state KL-regularized (Gibbs) equilibrium, connecting it to strategic classification~\cite{hardt2016}, partial monitoring~\cite{bartok2014}, and AI control~\cite{greenblatt2023,griffin2024,terekhov2025,ukaisi2025}. Our main contributions are:
\begin{enumerate}
  \item \textbf{Disambiguation of four selection metrics:} conditional stealth share among cheaters, absolute stealth probability relative to unmonitored post-training, asymptotic dominance of stealth over honesty as $\eta \to \infty$, and evasion against an off-loop deployment monitor $M_{\mathrm{audit}}$.
  \item \textbf{Exact phase transitions and the Rejection--Penalty Dilemma (Theorem~\ref{thm:selection}):} we prove a universal variance identity for conditional enrichment, derive exact thresholds for absolute amplification and dominance under both rejection-conditioned post-training (Operator~A) and KL-regularized penalties (Operator~B), and show that while pure rejection collapses asymptotically whenever $\beta_{\mathrm{f}} > 0$, negative penalties raise absolute undetected stealth strictly above pure rejection when a perfectly stealthy niche exists.
  \item \textbf{Three escape regimes (Theorem~\ref{thm:escape}):} we establish (R1)~the exact necessary and sufficient condition for honesty to dominate stealth via prior KL barriers and multi-objective maintenance costs, (R2)~a sufficient condition for preserving deployment audit power via off-loop informational decoupling (exact covariance identity under Operator~A; independence or negative association under Operator~B), and (R3)~a constructive mechanism via planted honeypots at bounded total variation distance $\dTV(P_{\mathrm{ord}}, P_{\mathrm{trap}}) \le \delta_{\mathrm{ind}}$ (with a R\'enyi max-divergence strengthening in Remark~\ref{rem:r3-duality}) that drives the effective false-negative rate below the critical R1 threshold.
\end{enumerate}
>>> NEW
```

#### Edit 4 — Section 2.2 (Clarify Operator A precisely)
```latex
<<< OLD
  \item \textbf{Operator~(A) --- Pure rejection with resampling (discard and try again).} Intercepted trajectories ($M_{\mathrm{loop}} = 1$) are discarded prior to reinforcement, conditioning the base law to $\pi_0^{\mathrm{acc}}(d\pi) = \beta(\pi)\pi_0(d\pi)/\E_{\pi_0}[\beta]$ and then applying KL-regularized reward maximization relative to $\pi_0^{\mathrm{acc}}$:
  \begin{equation}
    \pi_{\mathrm{A}}^{(\eta)}(d\pi) = \frac{\beta(\pi)\,e^{\eta R(\pi)}\,\pi_0(d\pi)}{Z_{\mathrm{A}}(\eta)},
    \qquad Z_{\mathrm{A}}(\eta) = \int_{\Pi} \beta(\pi')\,e^{\eta R(\pi')}\,\pi_0(d\pi').
  \end{equation}
  At $\eta = 0$, $\pi_{\mathrm{A}}^{(0)}$ reduces to pure Bayesian rejection conditioning without reward optimization.
===
  \item \textbf{Operator~(A) --- Rejection-conditioned post-training (discard and try again).} Intercepted trajectories ($M_{\mathrm{loop}} = 1$) are discarded, conditioning the base law to $\pi_0^{\mathrm{acc}}(d\pi) = \beta(\pi)\pi_0(d\pi)/\E_{\pi_0}[\beta]$ and then maximizing $\E_{\pi}[R] - \eta^{-1}\DKL(\pi \,\|\, \pi_0^{\mathrm{acc}})$ relative to the accepted base distribution $\pi_0^{\mathrm{acc}}$:
  \begin{equation}
    \pi_{\mathrm{A}}^{(\eta)}(d\pi) = \frac{\beta(\pi)\,e^{\eta R(\pi)}\,\pi_0(d\pi)}{Z_{\mathrm{A}}(\eta)},
    \qquad Z_{\mathrm{A}}(\eta) = \int_{\Pi} \beta(\pi')\,e^{\eta R(\pi')}\,\pi_0(d\pi').
  \end{equation}
  This operator models rejection-sampled supervised fine-tuning followed by KL-regularized optimization anchored to $\pi_0^{\mathrm{acc}}$, or equivalently post-hoc rejection applied to $\pi_{\mathrm{no}}^{(\eta)}$. At $\eta = 0$, $\pi_{\mathrm{A}}^{(0)}$ reduces to pure Bayesian rejection conditioning without reward optimization. (Online RL with in-loop rejection anchored to the unconditioned prior $\DKL(\pi \,\|\, \pi_0)$ induces a distinct self-consistent fixed point; see Section~6.)
>>> NEW
```

#### Edit 5 — Theorem 1(4c) (Clarify perfect-stealth niche honesty-vs-stealth tension and deployment harm)
```latex
<<< OLD
    \item \emph{Inversion under a perfectly stealthy niche ($\beta_{\mathrm{f}} = \beta_{\mathrm{h}} = 1 > \beta_{\mathrm{v}} > 0$):} If a stealthy strategy completely evades the in-loop monitor, Operator~B loses its asymptotic barrier ($\Delta R_{\mathrm{dom, B}}^* \to 0$) and amplifies absolute stealth \emph{strictly more strongly than pure rejection}---that is, $\pi_{\mathrm{B}}^{(\eta, C)}(\Pi_{\mathrm{f}}) > \pi_{\mathrm{A}}^{(\eta)}(\Pi_{\mathrm{f}}) > \pi_{\mathrm{no}}^{(\eta)}(\Pi_{\mathrm{f}})$---if and only if
    \begin{equation}\label{eq:inversion}
      \eta(\Delta R + C) > \frac{\log(1/\beta_{\mathrm{v}})}{1 - \beta_{\mathrm{v}}}.
    \end{equation}
===
    \item \emph{Inversion under a perfectly stealthy niche ($\beta_{\mathrm{f}} = \beta_{\mathrm{h}} = 1 > \beta_{\mathrm{v}} > 0$):} If a stealthy strategy completely evades the in-loop monitor, Operator~B loses its asymptotic barrier ($\Delta R_{\mathrm{dom, B}}^* \to 0$). Moreover, Operator~B suppresses $\Pi_{\mathrm{v}}$ and increases overall honesty ($\pi_{\mathrm{B}}^{(\eta, C)}(\Pi_{\mathrm{h}}) > \pi_{\mathrm{A}}^{(\eta)}(\Pi_{\mathrm{h}})$), \emph{yet} strictly increases the absolute probability of undetected stealthy misalignment above pure rejection---that is, $\pi_{\mathrm{B}}^{(\eta, C)}(\Pi_{\mathrm{f}}) > \pi_{\mathrm{A}}^{(\eta)}(\Pi_{\mathrm{f}}) > \pi_{\mathrm{no}}^{(\eta)}(\Pi_{\mathrm{f}})$---if and only if
    \begin{equation}\label{eq:inversion}
      \eta(\Delta R + C) > \frac{\log(1/\beta_{\mathrm{v}})}{1 - \beta_{\mathrm{v}}}.
    \end{equation}
    Consequently, whenever visible misalignment $\Pi_{\mathrm{v}}$ would be caught prior to deployment whereas $\Pi_{\mathrm{f}}$ causes unmitigated harm, Operator~B strictly increases expected deployment harm relative to Operator~A above~\eqref{eq:inversion}.
>>> NEW
```

#### Edit 6 — Proof of Theorem 1, Parts 3 & 4 (Fix Line 174 `9.91pt` Overfull `\hbox` & clarify honesty increase)
```latex
<<< OLD
\emph{Part~3.} Dividing numerator and denominator of $\pi_{\mathrm{B}}^{(\eta, C)}(\Pi_{\mathrm{f}})$ by $\exp(\eta[\beta_{\mathrm{f}}\Delta R - (1-\beta_{\mathrm{f}})C])$ gives
\[
  \pi_{\mathrm{B}}^{(\eta, C)}(\Pi_{\mathrm{f}})
  = \frac{p_{\mathrm{f}}}{p_{\mathrm{h}} e^{-\eta[\beta_{\mathrm{f}}\Delta R - (\beta_{\mathrm{h}}-\beta_{\mathrm{f}})C]} + p_{\mathrm{v}} e^{-\eta(\beta_{\mathrm{f}}-\beta_{\mathrm{v}})(\Delta R + C)} + p_{\mathrm{f}}},
  \qquad
  \pi_{\mathrm{no}}^{(\eta)}(\Pi_{\mathrm{f}})
  = \frac{p_{\mathrm{f}}}{p_{\mathrm{h}} e^{-\eta \Delta R} + p_{\mathrm{v}} + p_{\mathrm{f}}}.
\]
Comparing the two denominators directly yields~\eqref{eq:ampB}.

\emph{Part~4.} The log-odds $\log\frac{\pi_{\mathrm{A}}^{(\eta)}(\Pi_{\mathrm{f}})}{\pi_{\mathrm{A}}^{(\eta)}(\Pi_{\mathrm{h}})} = \log\frac{\beta_{\mathrm{f}} p_{\mathrm{f}}}{\beta_{\mathrm{h}} p_{\mathrm{h}}} + \eta\Delta R$ and $\log\frac{\pi_{\mathrm{B}}^{(\eta, C)}(\Pi_{\mathrm{f}})}{\pi_{\mathrm{B}}^{(\eta, C)}(\Pi_{\mathrm{h}})} = \log\frac{p_{\mathrm{f}}}{p_{\mathrm{h}}} + \eta[\beta_{\mathrm{f}}\Delta R - (\beta_{\mathrm{h}} - \beta_{\mathrm{f}})C]$ immediately give~\eqref{eq:domA} and~\eqref{eq:domB}. Finally, when $\beta_{\mathrm{f}} = \beta_{\mathrm{h}} = 1$ and $0 < \beta_{\mathrm{v}} < 1$, both $\pi_{\mathrm{A}}^{(\eta)}(\Pi_{\mathrm{f}})$ and $\pi_{\mathrm{B}}^{(\eta, C)}(\Pi_{\mathrm{f}})$ share the numerator $p_{\mathrm{f}} e^{\eta \Delta R}$ and the denominator terms $p_{\mathrm{h}} + p_{\mathrm{f}} e^{\eta \Delta R}$; only the weight of $\Pi_{\mathrm{v}}$ differs, being $\beta_{\mathrm{v}} p_{\mathrm{v}} e^{\eta \Delta R}$ under Operator~A versus $p_{\mathrm{v}} e^{\eta[\beta_{\mathrm{v}}\Delta R - (1-\beta_{\mathrm{v}})C]} = p_{\mathrm{v}} e^{\eta \Delta R} e^{-\eta(1-\beta_{\mathrm{v}})(\Delta R + C)}$ under Operator~B. Thus $\pi_{\mathrm{B}}^{(\eta, C)}(\Pi_{\mathrm{f}}) > \pi_{\mathrm{A}}^{(\eta)}(\Pi_{\mathrm{f}})$ iff $e^{-\eta(1-\beta_{\mathrm{v}})(\Delta R + C)} < \beta_{\mathrm{v}}$, which is~\eqref{eq:inversion}.
===
\emph{Part~3.} Dividing numerator and denominator of $\pi_{\mathrm{B}}^{(\eta, C)}(\Pi_{\mathrm{f}})$ by $\exp(\eta[\beta_{\mathrm{f}}\Delta R - (1-\beta_{\mathrm{f}})C])$ gives
\begin{align*}
  \pi_{\mathrm{B}}^{(\eta, C)}(\Pi_{\mathrm{f}})
  &= \frac{p_{\mathrm{f}}}{p_{\mathrm{h}} e^{-\eta[\beta_{\mathrm{f}}\Delta R - (\beta_{\mathrm{h}}-\beta_{\mathrm{f}})C]} + p_{\mathrm{v}} e^{-\eta(\beta_{\mathrm{f}}-\beta_{\mathrm{v}})(\Delta R + C)} + p_{\mathrm{f}}}, \\
  \pi_{\mathrm{no}}^{(\eta)}(\Pi_{\mathrm{f}})
  &= \frac{p_{\mathrm{f}}}{p_{\mathrm{h}} e^{-\eta \Delta R} + p_{\mathrm{v}} + p_{\mathrm{f}}}.
\end{align*}
Comparing the two denominators directly yields~\eqref{eq:ampB}.

\emph{Part~4.} The log-odds identities
\begin{align*}
  \log\frac{\pi_{\mathrm{A}}^{(\eta)}(\Pi_{\mathrm{f}})}{\pi_{\mathrm{A}}^{(\eta)}(\Pi_{\mathrm{h}})}
  &= \log\frac{\beta_{\mathrm{f}} p_{\mathrm{f}}}{\beta_{\mathrm{h}} p_{\mathrm{h}}} + \eta\Delta R, \\
  \log\frac{\pi_{\mathrm{B}}^{(\eta, C)}(\Pi_{\mathrm{f}})}{\pi_{\mathrm{B}}^{(\eta, C)}(\Pi_{\mathrm{h}})}
  &= \log\frac{p_{\mathrm{f}}}{p_{\mathrm{h}}} + \eta\big[\beta_{\mathrm{f}}\Delta R - (\beta_{\mathrm{h}} - \beta_{\mathrm{f}})C\big]
\end{align*}
immediately give~\eqref{eq:domA} and~\eqref{eq:domB}. Finally, when $\beta_{\mathrm{f}} = \beta_{\mathrm{h}} = 1$ and $0 < \beta_{\mathrm{v}} < 1$, both operators assign identical unnormalized weights $p_{\mathrm{h}}$ to $\Pi_{\mathrm{h}}$ and $p_{\mathrm{f}} e^{\eta \Delta R}$ to $\Pi_{\mathrm{f}}$; only the unnormalized weight of $\Pi_{\mathrm{v}}$ differs, being $\beta_{\mathrm{v}} p_{\mathrm{v}} e^{\eta \Delta R}$ under Operator~A versus
\[
  p_{\mathrm{v}} e^{\eta[\beta_{\mathrm{v}}\Delta R - (1-\beta_{\mathrm{v}})C]}
  = p_{\mathrm{v}} e^{\eta \Delta R} e^{-\eta(1-\beta_{\mathrm{v}})(\Delta R + C)}
\]
under Operator~B. Thus $Z_{\mathrm{B}}(\eta, C) < Z_{\mathrm{A}}(\eta)$ iff $e^{-\eta(1-\beta_{\mathrm{v}})(\Delta R + C)} < \beta_{\mathrm{v}}$, which is~\eqref{eq:inversion}; whenever this holds, both $\pi_{\mathrm{B}}^{(\eta, C)}(\Pi_{\mathrm{h}})$ and $\pi_{\mathrm{B}}^{(\eta, C)}(\Pi_{\mathrm{f}})$ strictly exceed their Operator~A values by the common factor $Z_{\mathrm{A}}(\eta)/Z_{\mathrm{B}}(\eta, C) > 1$.
>>> NEW
```

#### Edit 7 — Proposition 1 & Proof (Edge-case guard + Fix Lines 189–190 `33.90pt` Overfull `\hbox`)
```latex
<<< OLD
  \item \emph{Zero-penalty halting without resampling ($C = 0$ in Operator~B):} Setting $C = 0$ in Operator~B reduces the stealth reward exponent from $\eta\Delta R$ to $\eta\beta_{\mathrm{f}}\Delta R$, which still converges to $\pi_{\mathrm{B}}^{(\eta, 0)}(\Pi_{\mathrm{f}}) \to 1$ as $\eta \to +\infty$ for any $\beta_{\mathrm{f}} > 0$. Thus, halting without resampling and without negative penalty slows the asymptotic exponential rate of stealth dominance by a factor $\beta_{\mathrm{f}}$ (scaling the asymptotic $\eta$-scale by $1/\beta_{\mathrm{f}}$) compared to pure rejection, while the exact finite-$\eta$ threshold ratio $\Delta R_{\mathrm{dom, B}}^*(\eta, 0)/\Delta R_{\mathrm{dom, A}}^*(\eta) = \frac{1}{\beta_{\mathrm{f}}}\frac{\log(p_{\mathrm{h}}/p_{\mathrm{f}})}{\log(p_{\mathrm{h}}/p_{\mathrm{f}}) + \log(\beta_{\mathrm{h}}/\beta_{\mathrm{f}})}$ differs from $1/\beta_{\mathrm{f}}$ whenever $\beta_{\mathrm{f}} < \beta_{\mathrm{h}}$; in either case, it does not prevent asymptotic collapse.
  \item \emph{Perfect detection of visible cheating ($\beta_{\mathrm{v}} = 0$):} Under Operator~A, $\pi_{\mathrm{A}}^{(\eta)}(\Pi_{\mathrm{v}}) = 0$ for all $\eta \ge 0$, so $\pi_{\mathrm{A}}^{(\eta)}(\Pi_{\mathrm{f}} \mid \Pi_{\mathrm{tr}}) = 1$; under Operator~B with $\beta_{\mathrm{f}} = \beta_{\mathrm{h}} = 1$, $\pi_{\mathrm{A}}^{(\eta)}(\Pi_{\mathrm{f}}) > \pi_{\mathrm{B}}^{(\eta, C)}(\Pi_{\mathrm{f}})$ for all finite $\eta, C$ because Operator~A eliminates $\Pi_{\mathrm{v}}$ completely while Operator~B retains exponentially small mass $p_{\mathrm{v}} e^{-\eta C}$.
\end{enumerate}
\end{proposition}

\begin{proof}
Part~1 follows directly from~\eqref{eq:domA} and~\eqref{eq:domB} at $C = 0$, giving $\Delta R_{\mathrm{dom, B}}^*(\eta, 0) = (\eta\beta_{\mathrm{f}})^{-1}\log(p_{\mathrm{h}}/p_{\mathrm{f}}) \to 0$. Part~2 follows by substituting $\beta_{\mathrm{v}} = 0$ into the unnormalized weights of $\Pi_{\mathrm{v}}$ ($0$ under Operator~A versus $p_{\mathrm{v}} e^{-\eta C} > 0$ under Operator~B).
\end{proof}
===
  \item \emph{Zero-penalty halting without resampling ($C = 0$ in Operator~B):} Setting $C = 0$ in Operator~B reduces the stealth reward exponent from $\eta\Delta R$ to $\eta\beta_{\mathrm{f}}\Delta R$, which still converges to $\pi_{\mathrm{B}}^{(\eta, 0)}(\Pi_{\mathrm{f}}) \to 1$ as $\eta \to +\infty$ for any $\beta_{\mathrm{f}} > 0$. Halting without resampling or negative penalty thus slows the asymptotic exponential rate of stealth dominance by a factor $\beta_{\mathrm{f}}$ compared to pure rejection; for $p_{\mathrm{h}} > p_{\mathrm{f}}$, the finite-$\eta$ threshold ratio
  \[
    \frac{\Delta R_{\mathrm{dom, B}}^*(\eta, 0)}{\Delta R_{\mathrm{dom, A}}^*(\eta)}
    = \frac{1}{\beta_{\mathrm{f}}}\,\frac{\log(p_{\mathrm{h}}/p_{\mathrm{f}})}{\log(p_{\mathrm{h}}/p_{\mathrm{f}}) + \log(\beta_{\mathrm{h}}/\beta_{\mathrm{f}})}
  \]
  differs from $1/\beta_{\mathrm{f}}$ whenever $\beta_{\mathrm{f}} < \beta_{\mathrm{h}}$, and in either case does not prevent asymptotic collapse.
  \item \emph{Perfect detection of visible cheating ($\beta_{\mathrm{v}} = 0$):} Under Operator~A, $\pi_{\mathrm{A}}^{(\eta)}(\Pi_{\mathrm{v}}) = 0$ for all $\eta \ge 0$, so $\pi_{\mathrm{A}}^{(\eta)}(\Pi_{\mathrm{f}} \mid \Pi_{\mathrm{tr}}) = 1$; under Operator~B with $\beta_{\mathrm{f}} = \beta_{\mathrm{h}} = 1$, $\pi_{\mathrm{A}}^{(\eta)}(\Pi_{\mathrm{f}}) > \pi_{\mathrm{B}}^{(\eta, C)}(\Pi_{\mathrm{f}})$ for all finite $\eta, C$ because Operator~A eliminates $\Pi_{\mathrm{v}}$ completely while Operator~B retains exponentially small mass $p_{\mathrm{v}} e^{-\eta C}$.
\end{enumerate}
\end{proposition}

\begin{proof}
Part~1 follows directly from~\eqref{eq:domA} and~\eqref{eq:domB} at $C = 0$, which yields
\[
  \Delta R_{\mathrm{dom, B}}^*(\eta, 0) = \frac{1}{\eta\beta_{\mathrm{f}}}\log\frac{p_{\mathrm{h}}}{p_{\mathrm{f}}} \xrightarrow[\eta \to +\infty]{} 0.
\]
Part~2 follows by substituting $\beta_{\mathrm{v}} = 0$ into the unnormalized weights of $\Pi_{\mathrm{v}}$ ($0$ under Operator~A versus $p_{\mathrm{v}} e^{-\eta C} > 0$ under Operator~B).
\end{proof}
>>> NEW
```

#### Edit 8 — Theorem 2 (Fix Lines 205–206 `28.03pt` Overfull `\hbox` & align R3 critical ratio)
```latex
<<< OLD
  \item \textbf{Regime (R1) --- Prior KL barrier and multi-objective maintenance cost (exact necessary and sufficient condition in the 3-regime model).} Define $\Delta \DKL(\Pi_{\mathrm{f}} \,\|\, \Pi_{\mathrm{h}}; \pi_0) := \log(p_{\mathrm{h}}/p_{\mathrm{f}})$ and $\Delta R_{\mathrm{net}} := \Delta R - \delta_{\mathrm{maint}}$. Honesty strictly dominates stealth ($\pi_{\mathrm{post}}(\Pi_{\mathrm{f}}) < \pi_{\mathrm{post}}(\Pi_{\mathrm{h}})$) if and only if
===
  \item \textbf{Regime (R1) --- Prior KL barrier and multi-objective maintenance cost} \emph{(exact necessary and sufficient condition in the three-regime model).} Set $\Delta R_{\mathrm{net}} := \Delta R - \delta_{\mathrm{maint}}$ and $\Delta \DKL(\Pi_{\mathrm{f}} \,\|\, \Pi_{\mathrm{h}}; \pi_0) := \log(p_{\mathrm{h}}/p_{\mathrm{f}})$. Honesty strictly dominates stealth ($\pi_{\mathrm{post}}(\Pi_{\mathrm{f}}) < \pi_{\mathrm{post}}(\Pi_{\mathrm{h}})$) if and only if
>>> NEW
```

```latex
<<< OLD
has strictly negative expected reward relative to pure honesty ($\tau \equiv 0$, $\beta_{\mathrm{h}} = 1$) under Operator~B---driving its effective false-negative rate below the critical ratio $\frac{\beta_{\mathrm{h}} C}{\Delta R_{\mathrm{net}} + C}$---whenever
===
has strictly negative expected reward relative to pure honesty ($\tau \equiv 0$, $\beta_{\mathrm{h}} = 1$) under Operator~B---driving its effective false-negative rate below the critical ratio $\frac{C}{\Delta R + C}$---whenever
>>> NEW
```

#### Edit 9 — Proof of Theorem 2 (Fix Lines 237–238 `1.89pt` Overfull `\hbox` & tighten R3 proof quantifier)
```latex
<<< OLD
\emph{Part~1 (R1).} Substituting $\Delta R_{\mathrm{f}} = \Delta R_{\mathrm{net}}$ into the log-odds ratios $\pi_{\mathrm{A}}^{(\eta)}(\Pi_{\mathrm{f}})/\pi_{\mathrm{A}}^{(\eta)}(\Pi_{\mathrm{h}}) = \frac{\beta_{\mathrm{f}} p_{\mathrm{f}}}{\beta_{\mathrm{h}} p_{\mathrm{h}}} e^{\eta \Delta R_{\mathrm{net}}}$ and $\pi_{\mathrm{B}}^{(\eta, C)}(\Pi_{\mathrm{f}})/\pi_{\mathrm{B}}^{(\eta, C)}(\Pi_{\mathrm{h}}) = \frac{p_{\mathrm{f}}}{p_{\mathrm{h}}} e^{\eta[\beta_{\mathrm{f}}\Delta R_{\mathrm{net}} - (\beta_{\mathrm{h}}-\beta_{\mathrm{f}})C]}$ shows that each ratio is strictly less than $1$ iff~\eqref{eq:R1} holds. Whenever the coefficient of $\eta$ is strictly negative, the ratio decays exponentially to $0$ as $\eta \to +\infty$.

\emph{Part~2 (R2).} On $\mathcal{S}$, $e^{\eta R(\pi)} = e^{\eta \Delta R}$ cancels in $\pi_{\mathrm{A}}^{(\eta)}(\cdot \mid \mathcal{S})$, so $d\pi_{\mathrm{A}}^{(\eta)}(\cdot \mid \mathcal{S})/d\nu_0 = \beta_{\mathrm{loop}} / \E_{\nu_0}[\beta_{\mathrm{loop}}]$. Expanding $\E_{\nu_0}[\beta_{\mathrm{loop}}\beta_{\mathrm{audit}}]/\E_{\nu_0}[\beta_{\mathrm{loop}}] - \E_{\nu_0}[\beta_{\mathrm{audit}}]$ gives~\eqref{eq:R2}. Under Operator~B, the conditional density is proportional to $g(\beta_{\mathrm{loop}})$ where $g(u) = e^{\eta u (\Delta R + C)}$ is non-decreasing; by negative association~\cite{joagdev1983} (or independence), $\Cov_{\nu_0}(g(\beta_{\mathrm{loop}}), \beta_{\mathrm{audit}}) \le 0$, giving the stated inequality.

\emph{Part~3 (R3).} By the dual representation of total variation distance, $|\E_{P_{\mathrm{ord}}}[\tau_\pi] - \E_{P_{\mathrm{trap}}}[\tau_\pi]| \le \dTV(P_{\mathrm{ord}}, P_{\mathrm{trap}}) \le \delta_{\mathrm{ind}}$ for all measurable $\tau_\pi : \mathcal{X} \to [0, 1]$, hence $\tau_{\mathrm{trap}}(\pi) \ge \tau_{\mathrm{ord}}(\pi) - \delta_{\mathrm{ind}}$. On $P_{\mathrm{ord}}$, expected gain is at most $\tau_{\mathrm{ord}}(\pi)\Delta R$. On $P_{\mathrm{trap}}$, whenever $C > \frac{\varepsilon_{\mathrm{trap}}}{1-\varepsilon_{\mathrm{trap}}}\Delta R$, each cheating attempt yields expected payoff $\varepsilon_{\mathrm{trap}}\Delta R - (1-\varepsilon_{\mathrm{trap}})C < 0$, so expected gain on $P_{\mathrm{trap}}$ is at most $(\tau_{\mathrm{ord}}(\pi) - \delta_{\mathrm{ind}})[\varepsilon_{\mathrm{trap}}\Delta R - (1-\varepsilon_{\mathrm{trap}})C]$. Combining with mixture weights $(1-\rho)$ and $\rho$, the total expected reward $\E_{P_{\mathrm{mix}}}[\bar{R}_C(\pi)]$ is upper-bounded by
\[
  \tau_{\mathrm{ord}}(\pi)\left[(1-\rho)\Delta R + \rho\big(\varepsilon_{\mathrm{trap}}\Delta R - (1-\varepsilon_{\mathrm{trap}})C\big)\left(1 - \frac{\delta_{\mathrm{ind}}}{\tau_{\mathrm{ord}}(\pi)}\right)\right],
\]
which is strictly decreasing in $\tau_{\mathrm{ord}}(\pi)$ and strictly negative for all $\tau_{\mathrm{ord}}(\pi) \ge \tau_{\min}$ whenever $C > C_{\mathrm{R3}}^*$.
===
\emph{Part~1 (R1).} Substituting $\Delta R_{\mathrm{f}} = \Delta R_{\mathrm{net}}$ into the odds ratios
\[
  \frac{\pi_{\mathrm{A}}^{(\eta)}(\Pi_{\mathrm{f}})}{\pi_{\mathrm{A}}^{(\eta)}(\Pi_{\mathrm{h}})}
  = \frac{\beta_{\mathrm{f}} p_{\mathrm{f}}}{\beta_{\mathrm{h}} p_{\mathrm{h}}}\,e^{\eta \Delta R_{\mathrm{net}}},
  \qquad
  \frac{\pi_{\mathrm{B}}^{(\eta, C)}(\Pi_{\mathrm{f}})}{\pi_{\mathrm{B}}^{(\eta, C)}(\Pi_{\mathrm{h}})}
  = \frac{p_{\mathrm{f}}}{p_{\mathrm{h}}}\,e^{\eta[\beta_{\mathrm{f}}\Delta R_{\mathrm{net}} - (\beta_{\mathrm{h}}-\beta_{\mathrm{f}})C]}
\]
shows that each ratio is strictly less than $1$ iff~\eqref{eq:R1} holds. Whenever the coefficient of $\eta$ is strictly negative, the odds ratio---and hence $\pi_{\mathrm{B}}^{(\eta, C)}(\Pi_{\mathrm{f}})$---decays exponentially to $0$ as $\eta \to +\infty$.

\emph{Part~2 (R2).} On $\mathcal{S}$, $e^{\eta R(\pi)} = e^{\eta \Delta R}$ cancels in $\pi_{\mathrm{A}}^{(\eta)}(\cdot \mid \mathcal{S})$, so its density relative to $\nu_0$ is $\beta_{\mathrm{loop}} / \E_{\nu_0}[\beta_{\mathrm{loop}}]$; subtracting $\E_{\nu_0}[\beta_{\mathrm{audit}}]$ yields~\eqref{eq:R2}. Under Operator~B, the conditional density relative to $\nu_0$ is proportional to $g(\beta_{\mathrm{loop}})$ with $g(u) = e^{\eta u (\Delta R + C)}$ non-decreasing; by negative association~\cite{joagdev1983} (or independence), $\Cov_{\nu_0}(g(\beta_{\mathrm{loop}}), \beta_{\mathrm{audit}}) \le 0$, giving the stated inequality.

\emph{Part~3 (R3).} By the dual representation of total variation distance, $|\E_{P_{\mathrm{ord}}}[\tau_\pi] - \E_{P_{\mathrm{trap}}}[\tau_\pi]| \le \dTV(P_{\mathrm{ord}}, P_{\mathrm{trap}}) \le \delta_{\mathrm{ind}}$ for all measurable $\tau_\pi : \mathcal{X} \to [0, 1]$, hence $\tau_{\mathrm{trap}}(\pi) \ge \tau_{\mathrm{ord}}(\pi) - \delta_{\mathrm{ind}}$. On $P_{\mathrm{ord}}$, expected gain is at most $\tau_{\mathrm{ord}}(\pi)\Delta R$. Whenever $C > C_{\mathrm{R3}}^*$, we have $C > \frac{\varepsilon_{\mathrm{trap}}}{1-\varepsilon_{\mathrm{trap}}}\Delta R$, so each cheating attempt on $P_{\mathrm{trap}}$ yields expected payoff $\varepsilon_{\mathrm{trap}}\Delta R - (1-\varepsilon_{\mathrm{trap}})C < 0$, and expected gain on $P_{\mathrm{trap}}$ is at most $(\tau_{\mathrm{ord}}(\pi) - \delta_{\mathrm{ind}})[\varepsilon_{\mathrm{trap}}\Delta R - (1-\varepsilon_{\mathrm{trap}})C]$. Combining with mixture weights $(1-\rho)$ and $\rho$, $\E_{P_{\mathrm{mix}}}[\bar{R}_C(\pi)]$ is upper-bounded by
\[
  \tau_{\mathrm{ord}}(\pi)\left[(1-\rho)\Delta R + \rho\big(\varepsilon_{\mathrm{trap}}\Delta R - (1-\varepsilon_{\mathrm{trap}})C\big)\left(1 - \frac{\delta_{\mathrm{ind}}}{\tau_{\mathrm{ord}}(\pi)}\right)\right].
\]
For $C > C_{\mathrm{R3}}^*$, this affine upper bound has strictly negative slope in $\tau_{\mathrm{ord}}(\pi)$ and is strictly negative at $\tau_{\mathrm{ord}}(\pi) = \tau_{\min}$, hence strictly negative for all $\tau_{\mathrm{ord}}(\pi) \ge \tau_{\min}$.
>>> NEW
```

#### Edit 10 — Remark 1 on Regime R3 (Add verified Rényi $D_\infty$ sentence)
```latex
<<< OLD
\begin{remark}[Information-Theoretic Duality and Rare-Attack Floor of Regime~R3]
Total variation bounds are classically used to establish impossibility limits for \emph{monitors} trying to distinguish covert attacks from honest behavior (Neyman--Pearson power ceiling $\alpha + \dTV$). Theorem~\ref{thm:escape}(3) turns the exact same total variation inequality in favor of the \emph{defender}: if planted honeypots are close to ordinary episodes in total variation, no policy can selectively cheat on ordinary episodes while avoiding the traps. However, this guarantee requires $\tau_{\min} > \delta_{\mathrm{ind}}$ and does not block a policy that cheats at a very rare rate $\tau_{\mathrm{ord}} \le \delta_{\mathrm{ind}}$ concentrated exclusively on contexts where $P_{\mathrm{ord}} > P_{\mathrm{trap}}$.
\end{remark}
===
\begin{remark}[Information-Theoretic Duality and Rare-Attack Floor of Regime~R3]\label{rem:r3-duality}
Total variation bounds are classically used to establish impossibility limits for \emph{monitors} trying to distinguish covert attacks from honest behavior (Neyman--Pearson power ceiling $\alpha + \dTV$). Theorem~\ref{thm:escape}(3) turns the exact same inequality in favor of the \emph{defender}: if planted honeypots are close to ordinary episodes in total variation, no policy can selectively cheat on ordinary episodes while avoiding the traps. However, while $\dTV(P_{\mathrm{ord}}, P_{\mathrm{trap}}) \le \delta_{\mathrm{ind}}$ leaves a rare-attack floor $\tau_{\mathrm{ord}} \le \delta_{\mathrm{ind}}$ on high likelihood-ratio contexts where $P_{\mathrm{ord}} > P_{\mathrm{trap}}$, strengthening indistinguishability to one-sided R\'enyi max-divergence,
\[
  e^{D_\infty(P_{\mathrm{ord}} \,\|\, P_{\mathrm{trap}})}
  = \operatorname{ess\,sup}_x \frac{dP_{\mathrm{ord}}}{dP_{\mathrm{trap}}}(x)
  \le M < \infty,
\]
yields the multiplicative bound $\tau_{\mathrm{trap}} \ge M^{-1}\tau_{\mathrm{ord}}$ and eliminates the rare-attack floor altogether once
\[
  C > \frac{(1-\rho)M + \rho\,\varepsilon_{\mathrm{trap}}}{\rho(1-\varepsilon_{\mathrm{trap}})}\,\Delta R.
\]
\end{remark}
>>> NEW
```

#### Edit 11 — Section 5 (Sober verification framing, Fix Lines 252–253 `98.52pt` Overfull `\hbox`, Table 3 harm nuance)
```latex
<<< OLD
\section{Numerical Phase Transitions and Exact Verification}

All numerical examples below are generated and checked by the standalone script \texttt{verifier\_exemples\_papier\_v2.py}. The verification suite establishes:
\begin{itemize}
  \item \textbf{Exact rational arithmetic (\texttt{fractions.Fraction}):} for cheating sub-species weights $(1/2, 1/3, 1/6)$ and survival rates $(1/10, 2/5, 9/10)$, $\E_0[\beta] = 1/3$, $\Var_0(\beta) = 37/450$, $\E_{\mathrm{post}}[\beta] = 29/50$, and $\E_{\mathrm{post}}[\beta] - \E_0[\beta] = 37/150 = \Var_0(\beta)/\E_0[\beta]$ holds identically.
  \item \textbf{Deterministic Monte Carlo stress test ($14{,}000$ instances, $0$ violations):} $10{,}000$ random parameter draws for Theorem~\ref{thm:selection}, $2{,}000$ draws for the perfect-stealth inversion~\eqref{eq:inversion}, $1{,}000$ draws for Regime~R2, and $1{,}000$ draws for Regime~R3.
\end{itemize}
===
\section{Numerical Phase Transitions}

All phase-transition tables and worked examples below are reproduced by the standalone companion script \texttt{verify\_examples.py} (writing \texttt{verified\_examples.json}), which also runs an exact rational sanity check of the variance identity~\eqref{eq:variance}---for cheating weights $(1/2, 1/3, 1/6)$ and survival rates $(1/10, 2/5, 9/10)$, $\E_0[\beta] = 1/3$, $\Var_0(\beta) = 37/450$, and $\E_{\mathrm{post}}[\beta] - \E_0[\beta] = 37/150$---alongside deterministic numerical consistency checks across randomized parameter draws for Theorems~\ref{thm:selection}--\ref{thm:escape} and the R\'enyi max-divergence bound in Remark~\ref{rem:r3-duality}.
>>> NEW
```

```latex
<<< OLD
When a perfectly stealthy niche exists ($\beta_{\mathrm{f}} = \beta_{\mathrm{h}} = 1.0$, $\beta_{\mathrm{v}} = 0.10$, $p_{\mathrm{h}}=0.85, p_{\mathrm{v}}=0.14, p_{\mathrm{f}}=0.01$, $\eta = 2.0$, $\Delta R = 1.0$),~\eqref{eq:inversion} predicts the exact crossover $\eta(\Delta R + C) = \log(10)/0.9 = 2.558428$, i.e., $C = 0.279214$. Table~\ref{tab:niche} shows that for $C > 0.279214$, Operator~B drives absolute stealth strictly above Operator~A.
===
When a perfectly stealthy niche exists ($\beta_{\mathrm{f}} = \beta_{\mathrm{h}} = 1.0$, $\beta_{\mathrm{v}} = 0.10$, $p_{\mathrm{h}} = 0.85$, $p_{\mathrm{v}} = 0.14$, $p_{\mathrm{f}} = 0.01$, $\eta = 2.0$, $\Delta R = 1.0$),~\eqref{eq:inversion} predicts the exact crossover $\eta(\Delta R + C) = \log(10)/0.9 = 2.558428$, i.e., $C = 0.279214$. Table~\ref{tab:niche} shows that for $C > 0.279214$, Operator~B suppresses $\Pi_{\mathrm{v}}$ and raises overall honesty above pure rejection ($\pi_{\mathrm{B}}(\Pi_{\mathrm{h}})$ climbs from $\pi_{\mathrm{A}}(\Pi_{\mathrm{h}}) = 0.827382$ to $0.918135$ at $C = 2.5$), \emph{yet} simultaneously increases the absolute probability of undetected stealthy misalignment strictly above Operator~A ($\pi_{\mathrm{B}}(\Pi_{\mathrm{f}}) = 0.079814 > 0.071924 = \pi_{\mathrm{A}}(\Pi_{\mathrm{f}})$), increasing expected deployment harm whenever visible misalignment would be caught prior to deployment whereas $\Pi_{\mathrm{f}}$ causes unmitigated harm.
>>> NEW
```

```latex
<<< OLD
For Regime~R1, with $p_{\mathrm{h}} = 0.90, p_{\mathrm{v}} = 0.09, p_{\mathrm{f}} = 0.01, \beta_{\mathrm{h}} = 1.0, \beta_{\mathrm{v}} = 0.10, \beta_{\mathrm{f}} = 0.90$, a maintenance cost $\delta_{\mathrm{maint}} = 1.25$ against $\Delta R_{\mathrm{v}} = 1.0$ yields $\Delta R_{\mathrm{net}} = -0.25$, driving honesty to $\pi_{\mathrm{B}}(\Pi_{\mathrm{h}}) = 0.999998$ at $\eta = 20, C = 2.0$.
===
For Regime~R1, with $p_{\mathrm{h}} = 0.90$, $p_{\mathrm{v}} = 0.09$, $p_{\mathrm{f}} = 0.01$, $\beta_{\mathrm{h}} = 1.0$, $\beta_{\mathrm{v}} = 0.10$, and $\beta_{\mathrm{f}} = 0.90$, a maintenance cost $\delta_{\mathrm{maint}} = 1.25$ against $\Delta R_{\mathrm{v}} = 1.0$ yields $\Delta R_{\mathrm{net}} = -0.25$, driving honesty to $\pi_{\mathrm{B}}(\Pi_{\mathrm{h}}) = 0.999998$ at $\eta = 20$, $C = 2.0$.
>>> NEW
```

#### Edit 12 — Section 6 (Add Online RL unconditioned-prior fixed-point problem & Fix Lines 330–331 `63.13pt` Overfull `\hbox`)
```latex
<<< OLD
Our results are intentionally derived in a static, non-parametric Gibbs equilibrium model. Three open problems remain for bridging this exact characterization to practical frontier post-training:
\begin{enumerate}
  \item \textbf{Finite-time stochastic gradient dynamics on neural manifolds:} In parametric policy optimization ($\theta_{t+1} = \theta_t + \gamma_t \hat{g}_t$), implicit gradient bias and finite exploration simultaneously shape effective reachability and multi-objective maintenance costs $\delta_{\mathrm{maint}}(\theta_t)$ well before reaching any Gibbs equilibrium.
  \item \textbf{Multi-monitor coupling and cross-channel covariance:} Regime~R2 requires $\Cov_{\nu_0}(\beta_{\mathrm{loop}}, \beta_{\mathrm{audit}}) \le 0$. When an in-loop monitor and an off-loop audit channel share latent features, characterizing worst-case degradation under constrained coupling remains open.
  \item \textbf{Dynamic monitor-versus-policy allocation and rare-attack floor:} As highlighted in AI control research~\cite{ukaisi2025}, rare interceptions create a non-stationary partial-monitoring trade-off~\cite{bartok2014} between updating the monitor and updating the policy, since policy updates can reduce future observability; moreover, Regime~R3 leaves an irreducible floor for rare attacks with $\tau_{\mathrm{ord}} \le \delta_{\mathrm{ind}}$.
\end{enumerate}
===
Our results are intentionally derived in a static, non-parametric Gibbs equilibrium model. Four open problems remain for bridging this exact characterization to practical frontier post-training:
\begin{enumerate}
  \item \textbf{Online RL anchored to the unconditioned prior:} Operator~A models rejection-conditioned post-training relative to $\pi_0^{\mathrm{acc}}$ (or post-hoc rejection). By contrast, online reinforcement learning with in-loop rejection anchored directly to the unconditioned prior $\DKL(\pi \,\|\, \pi_0)$ couples the rejection normalizer to the evolving policy, inducing a distinct self-consistent fixed point whose phase transitions merit separate analysis.
  \item \textbf{Finite-time stochastic gradient dynamics on neural manifolds:} In parametric policy optimization ($\theta_{t+1} = \theta_t + \gamma_t \hat{g}_t$), implicit gradient bias and finite exploration simultaneously shape effective reachability and multi-objective maintenance costs $\delta_{\mathrm{maint}}(\theta_t)$ well before reaching any Gibbs equilibrium.
  \item \textbf{Multi-monitor coupling and cross-channel covariance:} Regime~R2 relies on non-positive cross-channel covariance, $\Cov_{\nu_0}(\beta_{\mathrm{loop}}, \beta_{\mathrm{audit}}) \le 0$ (or negative association under Operator~B). When an in-loop monitor and an off-loop audit channel share latent features, characterizing worst-case degradation under constrained coupling remains open.
  \item \textbf{Dynamic monitor-versus-policy allocation and honeypot likelihood ratios:} As highlighted in AI control research~\cite{ukaisi2025}, rare interceptions create a non-stationary partial-monitoring trade-off~\cite{bartok2014} between updating the monitor and updating the policy, since policy updates can reduce future observability; moreover, eliminating the total-variation rare-attack floor of Regime~R3 via Remark~\ref{rem:r3-duality} requires constructing trap distributions with controlled worst-case likelihood ratio $M$.
\end{enumerate}
>>> NEW
```

---

### 5. Exact Surgical Edits for `verify_examples.py` (from `verifier_exemples_papier_v2.py`)

#### Edit 1 — Clean English docstring
```python
<<< OLD
"""
Standalone reproducible numerical and exact-rational verifier for all examples
and tables cited in the Halberstadt post-training evasion publication package (v2).

Checks performed:
  - Exact rational check (`fractions.Fraction`) of the conditional-enrichment
    variance identity (Theorem 1.1).
  - 14,000 deterministic Monte Carlo checks (0 counterexamples) across
    Theorem 1 (10,000), the perfect-stealth niche inversion (2,000),
    Regime R2 off-loop decoupling (1,000), and Regime R3 planted honeypots (1,000).
  - Exact computation of every table and concrete numerical example used in
    the LessWrong comment, the LessWrong post, and the arXiv manuscript.
"""
===
"""
Standalone companion script reproducing all phase-transition tables, worked
examples, and analytical sanity checks for "When Does In-Loop Misalignment
Filtering Select for Stealth? Exact Phase Transitions and Escape Regimes in
Post-Training" (Lazar Ciric).

Outputs `verified_examples.json` in the repository root.
"""
>>> NEW
```

#### Edit 2 — Add Rényi $D_\infty$ multiplicative & rare-attack check to R3 verification loop
```python
<<< OLD
    # 4. 1,000 instances for R3
    rng4 = random.Random(161803)
    violations_r3 = 0
    for _ in range(1_000):
        m_obs = 6
        base = [rng4.uniform(0.1, 1.0) for _ in range(m_obs)]
        sb = sum(base)
        p_ord = [x / sb for x in base]
        pert = [max(1e-4, x + rng4.uniform(-0.03, 0.03)) for x in p_ord]
        sp = sum(pert)
        p_trap = [x / sp for x in pert]
        d_tv = 0.5 * sum(abs(a - b) for a, b in zip(p_ord, p_trap))
        pol = [1.0 if p_ord[x] >= p_trap[x] else 0.0 for x in range(m_obs)]
        tau_ord = sum(p_ord[x] * pol[x] for x in range(m_obs))
        tau_trap = sum(p_trap[x] * pol[x] for x in range(m_obs))
        if tau_trap + TOL < tau_ord - d_tv:
            violations_r3 += 1
        if tau_ord > d_tv + 0.05:
            rho, eps_trap, dr = 0.20, 0.02, 1.0
            c_star = ((1.0 - rho) * tau_ord + rho * eps_trap * (tau_ord - d_tv)) / (
                rho * (1.0 - eps_trap) * (tau_ord - d_tv)
            ) * dr
            c_chosen = c_star + 0.5
            gain = (1.0 - rho) * tau_ord * dr + rho * tau_trap * (eps_trap * dr - (1.0 - eps_trap) * c_chosen)
            if gain >= 0.0:
                violations_r3 += 1
===
    # 4. 1,000 instances for R3 (TV bound and one-sided Renyi D_inf bound)
    rng4 = random.Random(161803)
    violations_r3 = 0
    for _ in range(1_000):
        m_obs = 6
        base = [rng4.uniform(0.1, 1.0) for _ in range(m_obs)]
        sb = sum(base)
        p_ord = [x / sb for x in base]
        pert = [max(1e-4, x + rng4.uniform(-0.03, 0.03)) for x in p_ord]
        sp = sum(pert)
        p_trap = [x / sp for x in pert]
        d_tv = 0.5 * sum(abs(a - b) for a, b in zip(p_ord, p_trap))
        m_renyi = max(po / pt for po, pt in zip(p_ord, p_trap))
        pol = [1.0 if p_ord[x] >= p_trap[x] else 0.0 for x in range(m_obs)]
        tau_ord = sum(p_ord[x] * pol[x] for x in range(m_obs))
        tau_trap = sum(p_trap[x] * pol[x] for x in range(m_obs))
        if tau_trap + TOL < tau_ord - d_tv:
            violations_r3 += 1
        if tau_trap + TOL < tau_ord / m_renyi:
            violations_r3 += 1
        rho, eps_trap, dr = 0.20, 0.02, 1.0
        if tau_ord > d_tv + 0.05:
            c_star = ((1.0 - rho) * tau_ord + rho * eps_trap * (tau_ord - d_tv)) / (
                rho * (1.0 - eps_trap) * (tau_ord - d_tv)
            ) * dr
            c_chosen = c_star + 0.5
            gain = (1.0 - rho) * tau_ord * dr + rho * tau_trap * (eps_trap * dr - (1.0 - eps_trap) * c_chosen)
            if gain >= 0.0:
                violations_r3 += 1
        # Worst-case rare attack concentrated on the argmax likelihood-ratio context
        x_star = max(range(m_obs), key=lambda x: p_ord[x] / p_trap[x])
        tau_ord_rare = 1e-4 * p_ord[x_star]
        tau_trap_rare = 1e-4 * p_trap[x_star]
        if tau_trap_rare + TOL < tau_ord_rare / m_renyi:
            violations_r3 += 1
        c_star_dinf = ((1.0 - rho) * m_renyi + rho * eps_trap) / (rho * (1.0 - eps_trap)) * dr
        c_dinf = c_star_dinf + 0.5
