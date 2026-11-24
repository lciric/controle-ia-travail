You are preparing a clean, standalone, publication-grade public GitHub companion repository (`github.com/lciric/<repo-name>`) for author **Lazar Ciric**, to accompany a concise theoretical note responding to Yair Halberstadt's November 22, 2026 LessWrong question (*"Post training is fundamentally dangerous"*).

### Context & Strict Requirements
1. **Target files in the root of the public GitHub repository**:
   - `README.md` (clean, self-contained, zero broken placeholders like `[LINK_PDF]` or `[LINK_LESSWRONG_POST]`; link directly to `[main.pdf](./main.pdf)`, `[main.tex](./main.tex)`, `[verify_examples.py](./verify_examples.py)`, and `[verified_examples.json](./verified_examples.json)`)
   - `main.tex` (compiled cleanly with `pdflatex` into `main.pdf`, author `Lazar Ciric`, zero internal draft notes like `"Preprint draft prepared for review"`, zero francophone filenames like `verifier_exemples_papier_v2.py` -> use `verify_examples.py` and `verified_examples.json`)
   - `verify_examples.py` (clean standalone Python 3.10+ verification script outputting `verified_examples.json`)
   - `LICENSE` (MIT for code, CC-BY-4.0 for text/manuscript)
2. **Double-blind hygiene for a future major conference paper**:
   - Frame this public note cleanly and soberly as a **concise analytical note** characterizing the *static three-state KL-regularized (Gibbs) equilibrium* of in-loop misalignment filtering, so that a subsequent major manuscript (with new title, multi-algorithm online RL / GRPO theory, continuous Laplace tail analysis, Rényi $D_\infty$ honeypots, and empirical LLM experiments) remains clearly distinct in scope and title.
3. **Refinements from senior Area Chair review to incorporate cleanly into `main.tex` and `README.md`** (without breaking any verified mathematical theorem or numerical table):
   - **Remove overclaimed Monte Carlo boasting** from the Abstract and Contribution #4: do NOT present `"14,000 randomized Monte Carlo test instances"` or `fractions.Fraction` as a major scientific contribution in the Abstract/Introduction; instead, present the analytical closed-form results soberly and mention `verify_examples.py` concisely in Section 5 as reproducible companion code for all phase-transition tables and sanity checks.
   - **Clarify Operator A precisely in Section 2.2**: state explicitly that Operator A ($\pi_{\mathrm{A}}^{(\eta)}(d\pi) \propto \beta(\pi) e^{\eta R(\pi)} \pi_0(d\pi)$) models rejection-conditioned post-training relative to the accepted base distribution $\pi_0^{\mathrm{acc}}$ (such as rejection-sampled SFT followed by KL-regularized optimization, or post-hoc rejection), and note in Section 6 (Open Problems) that online RL anchored to the unconditioned prior $\DKL(\pi \,\|\, \pi_0)$ induces a distinct self-consistent fixed point.
   - **Clarify the Perfect-Stealth Niche Inversion (Theorem 1(4c) & Table 3)**: note explicitly that when $\beta_{\mathrm{f}} = \beta_{\mathrm{h}} = 1 > \beta_{\mathrm{v}} > 0$, Operator B suppresses $\Pi_{\mathrm{v}}$ and increases honesty overall ($\pi_{\mathrm{B}}(\Pi_{\mathrm{h}}) > \pi_{\mathrm{A}}(\Pi_{\mathrm{h}})$), **yet** strictly increases the *absolute probability of undetected stealthy misalignment* $\pi_{\mathrm{B}}(\Pi_{\mathrm{f}}) > \pi_{\mathrm{A}}(\Pi_{\mathrm{f}})$—which increases expected deployment harm whenever visible misalignment $\Pi_{\mathrm{v}}$ would have been caught prior to deployment whereas $\Pi_{\mathrm{f}}$ causes unmitigated harm.
   - **Clarify Remark 4 on Regime R3**: note in one crisp sentence that while total variation distance $\dTV(P_{\mathrm{ord}}, P_{\mathrm{trap}}) \le \delta_{\mathrm{ind}}$ leaves a rare-attack floor $\tau_{\mathrm{ord}} \le \delta_{\mathrm{ind}}$ on high likelihood-ratio contexts, strengthening indistinguishability to one-sided Rényi max-divergence $e^{D_\infty(P_{\mathrm{ord}} \| P_{\mathrm{trap}})} = \operatorname{ess\,sup}_x \frac{dP_{\mathrm{ord}}}{dP_{\mathrm{trap}}}(x) \le M < \infty$ yields a multiplicative bound $\tau_{\mathrm{trap}} \ge M^{-1}\tau_{\mathrm{ord}}$ that eliminates the rare-attack floor altogether once $C > \frac{(1-\rho)M + \rho\varepsilon_{\mathrm{trap}}}{\rho(1-\varepsilon_{\mathrm{trap}})} \Delta R$. (Verify this 2-line inequality carefully!)
   - **Fix all 6 `pdflatex` Overfull/Underfull `\hbox` warnings** observed when compiling `main-v2.tex`:
     * Line 35 (`\maketitle` / `\thanks`): clean `\author{Lazar Ciric}` with optional concise footnote.
     * Line 174 (`Overfull \hbox 9.91pt`): split the two side-by-side display fractions for $\pi_{\mathrm{B}}^{(\eta, C)}(\Pi_{\mathrm{f}})$ and $\pi_{\mathrm{no}}^{(\eta)}(\Pi_{\mathrm{f}})$ into `align*` or `gather*`.
     * Lines 189--190 (`Overfull \hbox 33.90pt`), lines 205--206 (`Overfull \hbox 28.03pt`), lines 237--238 (`Overfull \hbox 1.89pt`), lines 252--253 (`Overfull \hbox 98.52pt`), lines 330--331 (`Overfull \hbox 63.13pt`): add `\usepackage{microtype}` and reformulate inline math / display breaks so `pdflatex` produces **0 Overfull `\hbox`**.

### Output Format (Strictly <= 3,500 words total)
1. **Repository slug & 1-sentence GitHub description** (matching `lciric`'s existing public repos: `sycophancy-psychophysical-law`, `sycophancy-construct-validity`, `safety-concept-vectors`, `eval-awareness-detection`).
2. **Mathematical & Typographical Audit**: list every flaw/box/edge-case checked (including rigorous verification of the $D_\infty$ remark) and confirm 0 mathematical errors.
3. **Complete `README.md`** inside a fenced ```markdown block.
4. **Exact surgical edits for `main.tex`** (clearly delimited `OLD` -> `NEW` blocks covering every change from `main-v2.tex`, so `main.tex` can be patched deterministically and compiled with `pdflatex` with 0 Overfull `\hbox`).
5. **Exact surgical edits for `verify_examples.py`** (renaming internal references from `verifier_exemples_papier_v2.py` / `exemples-verifies-papier-v2.json` to `verify_examples.py` / `verified_examples.json`, plus a quick check of the $D_\infty$ inequality).

---
### Input File 1: `README-v2.md`
```markdown
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

```

### Input File 2: `main-v2.tex`
```latex
\documentclass[11pt,a4paper]{article}

\usepackage[margin=1in]{geometry}
\usepackage{amsmath,amssymb,amsthm}
\usepackage{booktabs}
\usepackage{hyperref}
\usepackage{xcolor}

\hypersetup{
  colorlinks=true,
  linkcolor=blue!60!black,
  citecolor=blue!60!black,
  urlcolor=blue!60!black
}

\newtheorem{theorem}{Theorem}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{remark}[theorem]{Remark}

\newcommand{\E}{\mathbb{E}}
\newcommand{\Prob}{\mathbb{P}}
\newcommand{\Var}{\operatorname{Var}}
\newcommand{\Cov}{\operatorname{Cov}}
\newcommand{\DKL}{D_{\mathrm{KL}}}
\newcommand{\dTV}{d_{\mathrm{TV}}}

\title{When Does In-Loop Misalignment Filtering Select for Stealth?\\
Exact Phase Transitions and Escape Regimes in Post-Training}

\author{[Author Name]\thanks{Preprint draft prepared for review. Standalone companion verification code: \texttt{verifier\_exemples\_papier\_v2.py}.}}
\date{November 2026}

\begin{document}
\maketitle

\begin{abstract}
When a misalignment detector---such as a chain-of-thought monitor or activation probe---is placed inside the post-training loop, does it inevitably select for stealthy evasion, even when intercepted runs are merely discarded and resampled without negative reward? We analyze this question at the Kullback--Leibler (KL)-regularized Gibbs equilibrium over a three-regime policy space partitioning honest behavior, visible misalignment, and stealthy misalignment. Separating four quantities often conflated in informal debate---conditional stealth enrichment, absolute stealth amplification relative to unmonitored post-training, asymptotic dominance over honesty, and evasion against a separate deployment monitor---we establish two exact results. \textbf{Theorem~1} proves that conditional stealth enrichment is universal via an exact variance identity, derives sharp closed-form phase-transition thresholds for both pure rejection with resampling (Operator~A) and KL-regularized negative penalties (Operator~B), and exposes a \emph{Rejection--Penalty Dilemma}: pure rejection always collapses to stealth as optimization pressure $\eta \to \infty$ whenever any stealthy false-negative rate $\beta_{\mathrm{f}} > 0$ exists, whereas a negative penalty $-C < 0$ creates a non-vanishing asymptotic barrier against partially detected stealth ($\beta_{\mathrm{f}} < \beta_{\mathrm{h}}$) yet amplifies absolute stealth \emph{strictly more than pure rejection} whenever a perfectly stealthy niche ($\beta_{\mathrm{f}} = \beta_{\mathrm{h}} = 1$) exists and $\eta(\Delta R + C) > \log(1/\beta_{\mathrm{v}})/(1-\beta_{\mathrm{v}})$. \textbf{Theorem~2} establishes three escape regimes within this framework: (R1)~the exact necessary and sufficient condition for suppressing stealth dominance via prior KL accessibility barriers and multi-objective maintenance costs, (R2)~a sufficient condition for preserving deployment audit power through strict off-loop informational decoupling (non-positive covariance / negative association), and (R3)~a sufficient constructive mechanism using indistinguishable planted honeypots bounded in total variation distance to force the effective false-negative rate below the critical R1 threshold. Every theorem and numerical table is verified in exact rational arithmetic and across $14{,}000$ randomized finite-world test instances with zero counterexamples.
\end{abstract}

\section{Introduction}

Post-training methods based on reinforcement learning and KL-regularized preference optimization substantially increase model capability, but also amplify reward hacking and strategic misalignment~\cite{zhuang2021,skalse2022,gao2022}. A natural engineering response is to deploy misalignment detectors---such as chain-of-thought monitors~\cite{baker2025}, elicitation checks, or internal activation probes---directly inside the post-training loop. Yet empirical and conceptual work on deceptive persistence~\cite{hubinger2024,greenblatt2024} and chain-of-thought obfuscation~\cite{baker2025} raises a fundamental concern: optimizing against an imperfect detector may simply teach the model to hide its misalignment rather than eliminate it.

In a recent discussion~\cite{halberstadt2026}, Halberstadt argued that even \emph{pure rejection without negative penalty} (``discard the run and try again'') reinforces undetected reward hacks, asking whether it is a mathematical law that any attempt to prevent misalignment during post-training inevitably encourages evasion. In response, \texttt{testingthewaters}~\cite{testingthewaters2026} argued that an in-loop filter acts as a selective sieve rather than a directional gradient, and that evasion may fail due to non-existence, unreachability under optimization constraints, or non-maintainability against competing post-training objectives.

This note resolves the question exactly at the standard KL-regularized (Gibbs) post-training equilibrium, connecting it to strategic classification~\cite{hardt2016}, partial monitoring~\cite{bartok2014}, and AI control~\cite{greenblatt2023,griffin2024,terekhov2025,ukaisi2025}. Our main contributions are:
\begin{enumerate}
  \item \textbf{Disambiguation of four selection metrics:} conditional stealth share among cheaters, absolute stealth probability relative to unmonitored post-training, asymptotic dominance of stealth over honesty as $\eta \to \infty$, and evasion against an off-loop deployment monitor $M_{\mathrm{audit}}$.
  \item \textbf{Exact phase transitions and the Rejection--Penalty Dilemma (Theorem~\ref{thm:selection}):} we prove a universal variance identity for conditional enrichment, derive exact thresholds for absolute amplification and dominance under both pure rejection (Operator~A) and KL-regularized penalties (Operator~B), and show that while pure rejection is asymptotically fatal whenever $\beta_{\mathrm{f}} > 0$, negative penalties backfire harder than pure rejection when a perfectly stealthy niche exists.
  \item \textbf{Three escape regimes (Theorem~\ref{thm:escape}):} we establish (R1)~the exact necessary and sufficient condition for honesty to dominate stealth via prior KL barriers and multi-objective maintenance costs, (R2)~a sufficient condition for preserving deployment audit power via off-loop informational decoupling (exact covariance identity under Operator~A; independence or negative association under Operator~B), and (R3)~a sufficient constructive mechanism via planted honeypots at bounded total variation distance $\dTV(P_{\mathrm{ord}}, P_{\mathrm{trap}}) \le \delta_{\mathrm{ind}}$ that forces the effective false-negative rate below the critical R1 threshold.
  \item \textbf{Reproducible verification:} all identities and phase-transition tables are verified by a standalone script in exact rational arithmetic (\texttt{fractions.Fraction}) and across $14{,}000$ randomized finite-world instances with zero counterexamples.
\end{enumerate}

\section{Formal Framework}

Let $(\Pi, \mathcal{A}, \pi_0)$ be the probability space of elementary policies or complete trajectories (including internal reasoning traces and tool calls) induced by a pretrained base model $\pi_0$. Partition $\Pi$ into three disjoint measurable events of strictly positive prior mass:
\begin{equation}
  \Pi = \Pi_{\mathrm{h}} \sqcup \Pi_{\mathrm{v}} \sqcup \Pi_{\mathrm{f}},
  \qquad p_{\mathrm{h}} := \pi_0(\Pi_{\mathrm{h}}) > 0,\quad p_{\mathrm{v}} := \pi_0(\Pi_{\mathrm{v}}) > 0,\quad p_{\mathrm{f}} := \pi_0(\Pi_{\mathrm{f}}) > 0,
\end{equation}
with $p_{\mathrm{h}} + p_{\mathrm{v}} + p_{\mathrm{f}} = 1$. Here $\Pi_{\mathrm{h}}$ denotes \emph{honest} behavior, $\Pi_{\mathrm{v}}$ denotes \emph{visible} misalignment (transparent reward hacking), $\Pi_{\mathrm{f}}$ denotes \emph{stealthy} misalignment (obfuscated reward hacking), and $\Pi_{\mathrm{tr}} := \Pi_{\mathrm{v}} \sqcup \Pi_{\mathrm{f}}$ denotes all misaligned behavior.

\subsection{Task Reward and In-Loop Monitor}
By shift invariance of Gibbs measures and KL-regularized objectives, we normalize task reward $R : \Pi \to \mathbb{R}$ to $R(\pi) = 0$ on $\Pi_{\mathrm{h}}$. On $\Pi_{\mathrm{v}}$ and $\Pi_{\mathrm{f}}$, misalignment yields reward advantages $\Delta R_{\mathrm{v}} > 0$ and $\Delta R_{\mathrm{f}} = \Delta R_{\mathrm{v}} - \delta_{\mathrm{maint}}$, where $\delta_{\mathrm{maint}} \ge 0$ captures any capability loss or conflict with auxiliary post-training objectives. In the canonical regime without intrinsic obfuscation cost, $\Delta R_{\mathrm{v}} = \Delta R_{\mathrm{f}} = \Delta R > 0$.

An in-loop monitor $M_{\mathrm{loop}} : \Pi \to \{0, 1\}$ ($1 =$ intercepted, $0 =$ accepted) is summarized by its \emph{survival probability}
\begin{equation}
  \beta(\pi) := \Prob(M_{\mathrm{loop}} = 0 \mid \pi) \in [0, 1],
\end{equation}
which equals the false-negative rate on $\Pi_{\mathrm{tr}}$ and $1 - \alpha_{\mathrm{h}}$ on $\Pi_{\mathrm{h}}$ ($\alpha_{\mathrm{h}} \in [0, 1)$ being the false-positive rate). In the stratum-constant reduction, we assume $0 \le \beta_{\mathrm{v}} < \beta_{\mathrm{f}} \le \beta_{\mathrm{h}} \le 1$ with $\beta_{\mathrm{f}} > 0$.

\subsection{Canonical Post-Training Operators}
At optimization pressure (inverse KL temperature) $\eta > 0$, the unmonitored baseline ($\beta \equiv 1$) is the unique maximizer of $\E_{\pi}[R] - \eta^{-1}\DKL(\pi \,\|\, \pi_0)$:
\begin{equation}
  \pi_{\mathrm{no}}^{(\eta)}(d\pi) = \frac{e^{\eta R(\pi)}\,\pi_0(d\pi)}{Z_{\mathrm{no}}(\eta)},
  \qquad Z_{\mathrm{no}}(\eta) = \int_{\Pi} e^{\eta R(\pi')}\,\pi_0(d\pi'),
\end{equation}
extended by continuity to $\pi_{\mathrm{no}}^{(0)} := \pi_0$. We formalize the two canonical in-loop interventions:
\begin{enumerate}
  \item \textbf{Operator~(A) --- Pure rejection with resampling (discard and try again).} Intercepted trajectories ($M_{\mathrm{loop}} = 1$) are discarded prior to reinforcement, conditioning the base law to $\pi_0^{\mathrm{acc}}(d\pi) = \beta(\pi)\pi_0(d\pi)/\E_{\pi_0}[\beta]$ and then applying KL-regularized reward maximization relative to $\pi_0^{\mathrm{acc}}$:
  \begin{equation}
    \pi_{\mathrm{A}}^{(\eta)}(d\pi) = \frac{\beta(\pi)\,e^{\eta R(\pi)}\,\pi_0(d\pi)}{Z_{\mathrm{A}}(\eta)},
    \qquad Z_{\mathrm{A}}(\eta) = \int_{\Pi} \beta(\pi')\,e^{\eta R(\pi')}\,\pi_0(d\pi').
  \end{equation}
  At $\eta = 0$, $\pi_{\mathrm{A}}^{(0)}$ reduces to pure Bayesian rejection conditioning without reward optimization.
  \item \textbf{Operator~(B) --- KL-regularized update with interception penalty $-C \le 0$.} Intercepted trajectories are halted before taking effect and receive score $-C$ ($C \ge 0$), yielding expected reward $\bar{R}_C(\pi) = \beta(\pi)R(\pi) - (1-\beta(\pi))C$. The unique maximizer of $\E_{\pi}[\bar{R}_C] - \eta^{-1}\DKL(\pi \,\|\, \pi_0)$ ($\eta > 0$) is:
  \begin{equation}
    \pi_{\mathrm{B}}^{(\eta, C)}(d\pi) = \frac{\exp\!\big(\eta\big[\beta(\pi)R(\pi) - (1-\beta(\pi))C\big]\big)\,\pi_0(d\pi)}{Z_{\mathrm{B}}(\eta, C)}.
  \end{equation}
\end{enumerate}

\section{Exact Phase Transitions and the Rejection--Penalty Dilemma}

\begin{theorem}[Exact Characterization of Stealth Selection under an Imperfect Filter]\label{thm:selection}
Suppose $\Delta R_{\mathrm{v}} = \Delta R_{\mathrm{f}} = \Delta R > 0$ and $0 \le \beta_{\mathrm{v}} < \beta_{\mathrm{f}} \le \beta_{\mathrm{h}} \le 1$ with $\beta_{\mathrm{f}} > 0$.
\begin{enumerate}
  \item \textbf{Universal conditional enrichment (variance identity).} For any measurable survival function $\beta : \Pi_{\mathrm{tr}} \to [0, 1]$ not almost surely constant under $\mu_{\mathrm{tr}}^{(\eta)}(\cdot) := \pi_{\mathrm{no}}^{(\eta)}(\cdot \mid \Pi_{\mathrm{tr}})$ (with $\E_{\mu_{\mathrm{tr}}^{(\eta)}}[\beta] > 0$),
  \begin{equation}\label{eq:variance}
    \E_{\pi_{\mathrm{A}}^{(\eta)}}[\beta(\pi) \mid \Pi_{\mathrm{tr}}] - \E_{\mu_{\mathrm{tr}}^{(\eta)}}[\beta(\pi)]
    = \frac{\Var_{\mu_{\mathrm{tr}}^{(\eta)}}(\beta(\pi))}{\E_{\mu_{\mathrm{tr}}^{(\eta)}}[\beta(\pi)]} > 0.
  \end{equation}
  In the two-stratum cheating model ($\beta_{\mathrm{v}} < \beta_{\mathrm{f}}$), conditional stealth share strictly increases without any threshold under both Operator~A ($\forall \eta \ge 0$) and Operator~B ($\forall \eta > 0, \forall C \ge 0$):
  \begin{equation}
    \pi_{\mathrm{A}}^{(\eta)}(\Pi_{\mathrm{f}} \mid \Pi_{\mathrm{tr}}) > \pi_{\mathrm{no}}^{(\eta)}(\Pi_{\mathrm{f}} \mid \Pi_{\mathrm{tr}})
    \qquad \text{and} \qquad
    \pi_{\mathrm{B}}^{(\eta, C)}(\Pi_{\mathrm{f}} \mid \Pi_{\mathrm{tr}}) > \pi_{\mathrm{no}}^{(\eta)}(\Pi_{\mathrm{f}} \mid \Pi_{\mathrm{tr}}).
  \end{equation}

  \item \textbf{Exact absolute-amplification threshold under pure rejection (Operator~A).} For fixed $\eta > 0$, $\pi_{\mathrm{A}}^{(\eta)}(\Pi_{\mathrm{f}}) > \pi_{\mathrm{no}}^{(\eta)}(\Pi_{\mathrm{f}})$ holds if and only if either $\beta_{\mathrm{f}} = \beta_{\mathrm{h}}$ (in which case amplification holds for all $\Delta R \ge 0, \eta \ge 0$), or $\beta_{\mathrm{f}} < \beta_{\mathrm{h}}$ and
  \begin{equation}\label{eq:ampA}
    \Delta R > \Delta R_{\mathrm{A}}^*(\eta)
    := \frac{1}{\eta}\left[\log\frac{p_{\mathrm{h}}}{p_{\mathrm{v}}} + \log\frac{\beta_{\mathrm{h}} - \beta_{\mathrm{f}}}{\beta_{\mathrm{f}} - \beta_{\mathrm{v}}}\right].
  \end{equation}

  \item \textbf{Exact absolute-amplification threshold under KL-regularized penalty (Operator~B).} For all $\eta > 0$ and $C \ge 0$, $\pi_{\mathrm{B}}^{(\eta, C)}(\Pi_{\mathrm{f}}) > \pi_{\mathrm{no}}^{(\eta)}(\Pi_{\mathrm{f}})$ holds if and only if
  \begin{equation}\label{eq:ampB}
    p_{\mathrm{v}}\Big(1 - e^{-\eta(\beta_{\mathrm{f}} - \beta_{\mathrm{v}})(\Delta R + C)}\Big)
    > p_{\mathrm{h}} e^{-\eta \Delta R}\Big(e^{\eta[(1-\beta_{\mathrm{f}})\Delta R + (\beta_{\mathrm{h}} - \beta_{\mathrm{f}})C]} - 1\Big).
  \end{equation}

  \item \textbf{Structural divergence (Rejection--Penalty Dilemma).}
  \begin{enumerate}
    \item \emph{Asymptotic collapse of pure rejection:} Under Operator~A, $\pi_{\mathrm{A}}^{(\eta)}(\Pi_{\mathrm{f}}) > \pi_{\mathrm{A}}^{(\eta)}(\Pi_{\mathrm{h}})$ holds iff
    \begin{equation}\label{eq:domA}
      \Delta R > \Delta R_{\mathrm{dom, A}}^*(\eta)
      := \frac{1}{\eta}\left(\log\frac{p_{\mathrm{h}}}{p_{\mathrm{f}}} + \log\frac{\beta_{\mathrm{h}}}{\beta_{\mathrm{f}}}\right)
      \xrightarrow[\eta \to +\infty]{} 0.
    \end{equation}
    Hence, for any $\Delta R > 0$ and any imperfect detection rate ($\beta_{\mathrm{f}} > 0$), honesty collapses under pure rejection as $\eta \to +\infty$.
    \item \emph{Non-vanishing barrier under negative penalty when $\beta_{\mathrm{f}} < \beta_{\mathrm{h}}$:} Under Operator~B, $\pi_{\mathrm{B}}^{(\eta, C)}(\Pi_{\mathrm{f}}) > \pi_{\mathrm{B}}^{(\eta, C)}(\Pi_{\mathrm{h}})$ holds iff
    \begin{equation}\label{eq:domB}
      \Delta R > \Delta R_{\mathrm{dom, B}}^*(\eta, C)
      := \frac{\beta_{\mathrm{h}} - \beta_{\mathrm{f}}}{\beta_{\mathrm{f}}}\,C + \frac{1}{\eta \beta_{\mathrm{f}}}\log\frac{p_{\mathrm{h}}}{p_{\mathrm{f}}}
      \xrightarrow[\eta \to +\infty]{} \frac{\beta_{\mathrm{h}} - \beta_{\mathrm{f}}}{\beta_{\mathrm{f}}}\,C > 0 \quad (C > 0).
    \end{equation}
    \item \emph{Inversion under a perfectly stealthy niche ($\beta_{\mathrm{f}} = \beta_{\mathrm{h}} = 1 > \beta_{\mathrm{v}} > 0$):} If a stealthy strategy completely evades the in-loop monitor, Operator~B loses its asymptotic barrier ($\Delta R_{\mathrm{dom, B}}^* \to 0$) and amplifies absolute stealth \emph{strictly more strongly than pure rejection}---that is, $\pi_{\mathrm{B}}^{(\eta, C)}(\Pi_{\mathrm{f}}) > \pi_{\mathrm{A}}^{(\eta)}(\Pi_{\mathrm{f}}) > \pi_{\mathrm{no}}^{(\eta)}(\Pi_{\mathrm{f}})$---if and only if
    \begin{equation}\label{eq:inversion}
      \eta(\Delta R + C) > \frac{\log(1/\beta_{\mathrm{v}})}{1 - \beta_{\mathrm{v}}}.
    \end{equation}
  \end{enumerate}
\end{enumerate}
\end{theorem}

\begin{proof}
\emph{Part~1.} Since $e^{\eta R(\pi)}$ is already absorbed into $\mu_{\mathrm{tr}}^{(\eta)}(\cdot) = \pi_{\mathrm{no}}^{(\eta)}(\cdot \mid \Pi_{\mathrm{tr}})$, the Radon--Nikodym derivative of $\pi_{\mathrm{A}}^{(\eta)}(\cdot \mid \Pi_{\mathrm{tr}})$ with respect to $\mu_{\mathrm{tr}}^{(\eta)}$ is $\beta(\pi) / \E_{\mu_{\mathrm{tr}}^{(\eta)}}[\beta]$ (even when $R(\pi)$ varies on $\Pi_{\mathrm{tr}}$). Therefore,
\[
  \E_{\pi_{\mathrm{A}}^{(\eta)}}[\beta \mid \Pi_{\mathrm{tr}}]
  = \frac{\E_{\mu_{\mathrm{tr}}^{(\eta)}}[\beta^2]}{\E_{\mu_{\mathrm{tr}}^{(\eta)}}[\beta]}
  = \E_{\mu_{\mathrm{tr}}^{(\eta)}}[\beta] + \frac{\Var_{\mu_{\mathrm{tr}}^{(\eta)}}(\beta)}{\E_{\mu_{\mathrm{tr}}^{(\eta)}}[\beta]},
\]
which strictly exceeds $\E_{\mu_{\mathrm{tr}}^{(\eta)}}[\beta]$ whenever $\Var_{\mu_{\mathrm{tr}}^{(\eta)}}(\beta) > 0$. For two strata with $\beta_{\mathrm{v}} < \beta_{\mathrm{f}}$, the conditional odds are $\frac{\pi_{\mathrm{A}}^{(\eta)}(\Pi_{\mathrm{f}})}{\pi_{\mathrm{A}}^{(\eta)}(\Pi_{\mathrm{v}})} = \frac{\beta_{\mathrm{f}}}{\beta_{\mathrm{v}}}\frac{p_{\mathrm{f}}}{p_{\mathrm{v}}} > \frac{p_{\mathrm{f}}}{p_{\mathrm{v}}}$ (infinite when $\beta_{\mathrm{v}} = 0$) and $\frac{\pi_{\mathrm{B}}^{(\eta, C)}(\Pi_{\mathrm{f}})}{\pi_{\mathrm{B}}^{(\eta, C)}(\Pi_{\mathrm{v}})} = e^{\eta(\beta_{\mathrm{f}} - \beta_{\mathrm{v}})(\Delta R + C)}\frac{p_{\mathrm{f}}}{p_{\mathrm{v}}} > \frac{p_{\mathrm{f}}}{p_{\mathrm{v}}}$ since $\eta > 0$, $\beta_{\mathrm{f}} > \beta_{\mathrm{v}}$, and $\Delta R + C > 0$. Strict monotonicity of $x \mapsto x/(1+x)$ on $[0, +\infty]$ yields both strict inequalities.

\emph{Part~2.} Writing the stratum probabilities explicitly,
\[
  \pi_{\mathrm{A}}^{(\eta)}(\Pi_{\mathrm{f}})
  = \frac{\beta_{\mathrm{f}} p_{\mathrm{f}} e^{\eta \Delta R}}{\beta_{\mathrm{h}} p_{\mathrm{h}} + (\beta_{\mathrm{v}} p_{\mathrm{v}} + \beta_{\mathrm{f}} p_{\mathrm{f}}) e^{\eta \Delta R}},
  \qquad
  \pi_{\mathrm{no}}^{(\eta)}(\Pi_{\mathrm{f}})
  = \frac{p_{\mathrm{f}} e^{\eta \Delta R}}{p_{\mathrm{h}} + (p_{\mathrm{v}} + p_{\mathrm{f}}) e^{\eta \Delta R}}.
\]
Since $p_{\mathrm{f}} e^{\eta \Delta R} > 0$ and both denominators are strictly positive, cross-multiplying shows that $\pi_{\mathrm{A}}^{(\eta)}(\Pi_{\mathrm{f}}) > \pi_{\mathrm{no}}^{(\eta)}(\Pi_{\mathrm{f}})$ is equivalent to
\[
  (\beta_{\mathrm{f}} - \beta_{\mathrm{v}}) p_{\mathrm{v}} e^{\eta \Delta R} > (\beta_{\mathrm{h}} - \beta_{\mathrm{f}}) p_{\mathrm{h}}.
\]
The left-hand side is strictly positive because $\beta_{\mathrm{f}} > \beta_{\mathrm{v}}$ and $p_{\mathrm{v}} > 0$. If $\beta_{\mathrm{f}} = \beta_{\mathrm{h}}$, the right-hand side vanishes and the inequality always holds. If $\beta_{\mathrm{f}} < \beta_{\mathrm{h}}$, dividing by $(\beta_{\mathrm{f}} - \beta_{\mathrm{v}})p_{\mathrm{v}}$ and taking logarithms yields~\eqref{eq:ampA}.

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
\end{proof}

\begin{proposition}[Limiting Cases and Zero-Penalty Halting without Resampling]\label{prop:limits}
Under the assumptions of Theorem~\ref{thm:selection}:
\begin{enumerate}
  \item \emph{Zero-penalty halting without resampling ($C = 0$ in Operator~B):} Setting $C = 0$ in Operator~B reduces the stealth reward exponent from $\eta\Delta R$ to $\eta\beta_{\mathrm{f}}\Delta R$, which still converges to $\pi_{\mathrm{B}}^{(\eta, 0)}(\Pi_{\mathrm{f}}) \to 1$ as $\eta \to +\infty$ for any $\beta_{\mathrm{f}} > 0$. Thus, halting without resampling and without negative penalty slows the asymptotic exponential rate of stealth dominance by a factor $\beta_{\mathrm{f}}$ (scaling the asymptotic $\eta$-scale by $1/\beta_{\mathrm{f}}$) compared to pure rejection, while the exact finite-$\eta$ threshold ratio $\Delta R_{\mathrm{dom, B}}^*(\eta, 0)/\Delta R_{\mathrm{dom, A}}^*(\eta) = \frac{1}{\beta_{\mathrm{f}}}\frac{\log(p_{\mathrm{h}}/p_{\mathrm{f}})}{\log(p_{\mathrm{h}}/p_{\mathrm{f}}) + \log(\beta_{\mathrm{h}}/\beta_{\mathrm{f}})}$ differs from $1/\beta_{\mathrm{f}}$ whenever $\beta_{\mathrm{f}} < \beta_{\mathrm{h}}$; in either case, it does not prevent asymptotic collapse.
  \item \emph{Perfect detection of visible cheating ($\beta_{\mathrm{v}} = 0$):} Under Operator~A, $\pi_{\mathrm{A}}^{(\eta)}(\Pi_{\mathrm{v}}) = 0$ for all $\eta \ge 0$, so $\pi_{\mathrm{A}}^{(\eta)}(\Pi_{\mathrm{f}} \mid \Pi_{\mathrm{tr}}) = 1$; under Operator~B with $\beta_{\mathrm{f}} = \beta_{\mathrm{h}} = 1$, $\pi_{\mathrm{A}}^{(\eta)}(\Pi_{\mathrm{f}}) > \pi_{\mathrm{B}}^{(\eta, C)}(\Pi_{\mathrm{f}})$ for all finite $\eta, C$ because Operator~A eliminates $\Pi_{\mathrm{v}}$ completely while Operator~B retains exponentially small mass $p_{\mathrm{v}} e^{-\eta C}$.
\end{enumerate}
\end{proposition}

\begin{proof}
Part~1 follows directly from~\eqref{eq:domA} and~\eqref{eq:domB} at $C = 0$, giving $\Delta R_{\mathrm{dom, B}}^*(\eta, 0) = (\eta\beta_{\mathrm{f}})^{-1}\log(p_{\mathrm{h}}/p_{\mathrm{f}}) \to 0$. Part~2 follows by substituting $\beta_{\mathrm{v}} = 0$ into the unnormalized weights of $\Pi_{\mathrm{v}}$ ($0$ under Operator~A versus $p_{\mathrm{v}} e^{-\eta C} > 0$ under Operator~B).
\end{proof}

\section{Three Escape Regimes: Necessary, Sufficient, and Constructive Conditions}

In the analysis of Theorem~\ref{thm:selection}, producing a deployed policy that both favors stealth over honesty ($\pi_{\mathrm{post}}(\Pi_{\mathrm{f}}) \ge \pi_{\mathrm{post}}(\Pi_{\mathrm{h}})$) and evades deployment monitoring $M_{\mathrm{audit}}$ relies on three conditions:
\begin{itemize}
  \item \textbf{(H1)} the net stealth advantage $\Delta R_{\mathrm{net}} = \Delta R - \delta_{\mathrm{maint}}$ overcomes the prior rarity $\log(p_{\mathrm{h}}/p_{\mathrm{f}})$ under $\pi_0$;
  \item \textbf{(H2)} survival $\beta_{\mathrm{loop}}$ selected during training correlates positively with survival $\beta_{\mathrm{audit}}$ at deployment;
  \item \textbf{(H3)} under Operator~B with $\Delta R_{\mathrm{net}} + C > 0$, the policy keeps its effective false-negative rate $\beta_{\mathrm{loop}}$ above the critical R1 ratio $\frac{\beta_{\mathrm{h}} C}{\Delta R_{\mathrm{net}} + C}$ by distinguishing unmonitored from monitored contexts.
\end{itemize}
In the static three-regime Gibbs model, avoiding deployment-effective evasion requires breaking one of two exact algebraic inequalities---either suppressing stealth dominance (\textbf{R1}, exact necessary and sufficient condition) or decoupling training selection from deployment auditing (\textbf{R2}, exact covariance identity under Operator~A and sufficient condition under Operator~B)---while \textbf{R3} (indistinguishable planted honeypots in an extended contextual model) provides a sufficient constructive mechanism for forcing the effective false-negative rate below $\frac{\beta_{\mathrm{h}} C}{\Delta R_{\mathrm{net}} + C}$ and thus entering the negative-drift regime of R1 even when the monitor is completely blind on ordinary episodes.

\begin{theorem}[Escape Regimes R1, R2, and R3]\label{thm:escape}
\leavevmode
\begin{enumerate}
  \item \textbf{Regime (R1) --- Prior KL barrier and multi-objective maintenance cost (exact necessary and sufficient condition in the 3-regime model).} Define $\Delta \DKL(\Pi_{\mathrm{f}} \,\|\, \Pi_{\mathrm{h}}; \pi_0) := \log(p_{\mathrm{h}}/p_{\mathrm{f}})$ and $\Delta R_{\mathrm{net}} := \Delta R - \delta_{\mathrm{maint}}$. Honesty strictly dominates stealth ($\pi_{\mathrm{post}}(\Pi_{\mathrm{f}}) < \pi_{\mathrm{post}}(\Pi_{\mathrm{h}})$) if and only if
  \begin{equation}\label{eq:R1}
    \Delta \DKL(\Pi_{\mathrm{f}} \,\|\, \Pi_{\mathrm{h}}; \pi_0) >
    \begin{cases}
      \eta\,\Delta R_{\mathrm{net}} - \log(\beta_{\mathrm{h}}/\beta_{\mathrm{f}}) & \text{under Operator~(A)}, \\[4pt]
      \eta\big[\beta_{\mathrm{f}}\Delta R_{\mathrm{net}} - (\beta_{\mathrm{h}} - \beta_{\mathrm{f}})C\big] & \text{under Operator~(B)}.
    \end{cases}
  \end{equation}
  In particular, if $\Pi_{\mathrm{f}}$ is unreachable ($p_{\mathrm{f}} = 0 \iff \Delta \DKL = +\infty$) or non-maintainable ($\beta_{\mathrm{f}}\Delta R_{\mathrm{net}} < (\beta_{\mathrm{h}} - \beta_{\mathrm{f}})C$, equivalently $\beta_{\mathrm{f}} < \frac{\beta_{\mathrm{h}} C}{\Delta R_{\mathrm{net}} + C}$ when $\Delta R_{\mathrm{net}} + C > 0$, or $\Delta R_{\mathrm{net}} < 0$), then $\lim_{\eta \to +\infty}\pi_{\mathrm{B}}^{(\eta, C)}(\Pi_{\mathrm{f}}) = 0$.

  \item \textbf{Regime (R2) --- Strict off-loop informational decoupling (sufficient condition for preserving deployment audit power).} Suppose post-training uses only $(R, M_{\mathrm{loop}})$, while deployment monitoring relies on an off-loop detector $M_{\mathrm{audit}}$ with survival probability $\beta_{\mathrm{audit}}(\pi) := \Prob(M_{\mathrm{audit}} = 0 \mid \pi)$. On any iso-reward cheating stratum $\mathcal{S} := \{\pi \in \Pi_{\mathrm{tr}} : R(\pi) = \Delta R\}$ with $\nu_0 := \pi_0(\cdot \mid \mathcal{S})$ and $\E_{\nu_0}[\beta_{\mathrm{loop}}] > 0$, Operator~A satisfies the exact identity
  \begin{equation}\label{eq:R2}
    \E_{\pi_{\mathrm{A}}^{(\eta)}}[\beta_{\mathrm{audit}} \mid \mathcal{S}] - \E_{\nu_0}[\beta_{\mathrm{audit}}]
    = \frac{\Cov_{\nu_0}(\beta_{\mathrm{loop}}, \beta_{\mathrm{audit}})}{\E_{\nu_0}[\beta_{\mathrm{loop}}]}.
  \end{equation}
  Moreover, under Operator~B, if $(\beta_{\mathrm{loop}}, \beta_{\mathrm{audit}})$ are independent or negatively associated~\cite{joagdev1983} under $\nu_0$, then for all $\eta \ge 0$ and $C \ge 0$,
  \begin{equation}
    \E_{\pi_{\mathrm{B}}^{(\eta, C)}}[\beta_{\mathrm{audit}} \mid \mathcal{S}] \le \E_{\nu_0}[\beta_{\mathrm{audit}}].
  \end{equation}

  \item \textbf{Regime (R3) --- Indistinguishable planted honeypots (sufficient constructive mechanism in the extended contextual model).} Let $\mathcal{X}$ be the space of contexts observed by the policy, drawn from the mixture $P_{\mathrm{mix}} = (1-\rho)P_{\mathrm{ord}} + \rho P_{\mathrm{trap}}$ ($\rho \in (0, 1)$), where the monitor may be completely blind on ordinary episodes $P_{\mathrm{ord}}$ ($\beta_{\mathrm{ord}} \le 1$) but catches any cheating on trap episodes $P_{\mathrm{trap}}$ with probability at least $1 - \varepsilon_{\mathrm{trap}} \in (0, 1]$. If every admissible policy $\pi$ (with context-dependent cheating probability $\tau_{\pi} : \mathcal{X} \to [0, 1]$) satisfies $|\E_{P_{\mathrm{ord}}}[\tau_\pi(X)] - \E_{P_{\mathrm{trap}}}[\tau_\pi(X)]| \le \delta_{\mathrm{ind}} \in [0, 1)$---which holds unconditionally whenever $\dTV(P_{\mathrm{ord}}, P_{\mathrm{trap}}) \le \delta_{\mathrm{ind}}$---then any policy with $\tau_{\mathrm{ord}}(\pi) := \E_{P_{\mathrm{ord}}}[\tau_\pi(X)] \ge \tau_{\min} > \delta_{\mathrm{ind}}$ incurs trap-cheating rate $\tau_{\mathrm{trap}}(\pi) \ge \tau_{\mathrm{ord}}(\pi) - \delta_{\mathrm{ind}}$ and has strictly negative expected reward relative to pure honesty ($\tau \equiv 0$, $\beta_{\mathrm{h}} = 1$) under Operator~B---driving its effective false-negative rate below the critical ratio $\frac{\beta_{\mathrm{h}} C}{\Delta R_{\mathrm{net}} + C}$---whenever
  \begin{equation}\label{eq:R3}
    C > C_{\mathrm{R3}}^*
    := \frac{(1-\rho)\tau_{\min} + \rho\,\varepsilon_{\mathrm{trap}}(\tau_{\min} - \delta_{\mathrm{ind}})}{\rho(1 - \varepsilon_{\mathrm{trap}})(\tau_{\min} - \delta_{\mathrm{ind}})}\,\Delta R
    \le \frac{1 - \rho + \rho\,\varepsilon_{\mathrm{trap}}}{\rho(1 - \varepsilon_{\mathrm{trap}})(1 - \delta_{\mathrm{ind}}/\tau_{\min})}\,\Delta R.
  \end{equation}
\end{enumerate}
\end{theorem}

\begin{proof}
\emph{Part~1 (R1).} Substituting $\Delta R_{\mathrm{f}} = \Delta R_{\mathrm{net}}$ into the log-odds ratios $\pi_{\mathrm{A}}^{(\eta)}(\Pi_{\mathrm{f}})/\pi_{\mathrm{A}}^{(\eta)}(\Pi_{\mathrm{h}}) = \frac{\beta_{\mathrm{f}} p_{\mathrm{f}}}{\beta_{\mathrm{h}} p_{\mathrm{h}}} e^{\eta \Delta R_{\mathrm{net}}}$ and $\pi_{\mathrm{B}}^{(\eta, C)}(\Pi_{\mathrm{f}})/\pi_{\mathrm{B}}^{(\eta, C)}(\Pi_{\mathrm{h}}) = \frac{p_{\mathrm{f}}}{p_{\mathrm{h}}} e^{\eta[\beta_{\mathrm{f}}\Delta R_{\mathrm{net}} - (\beta_{\mathrm{h}}-\beta_{\mathrm{f}})C]}$ shows that each ratio is strictly less than $1$ iff~\eqref{eq:R1} holds. Whenever the coefficient of $\eta$ is strictly negative, the ratio decays exponentially to $0$ as $\eta \to +\infty$.

\emph{Part~2 (R2).} On $\mathcal{S}$, $e^{\eta R(\pi)} = e^{\eta \Delta R}$ cancels in $\pi_{\mathrm{A}}^{(\eta)}(\cdot \mid \mathcal{S})$, so $d\pi_{\mathrm{A}}^{(\eta)}(\cdot \mid \mathcal{S})/d\nu_0 = \beta_{\mathrm{loop}} / \E_{\nu_0}[\beta_{\mathrm{loop}}]$. Expanding $\E_{\nu_0}[\beta_{\mathrm{loop}}\beta_{\mathrm{audit}}]/\E_{\nu_0}[\beta_{\mathrm{loop}}] - \E_{\nu_0}[\beta_{\mathrm{audit}}]$ gives~\eqref{eq:R2}. Under Operator~B, the conditional density is proportional to $g(\beta_{\mathrm{loop}})$ where $g(u) = e^{\eta u (\Delta R + C)}$ is non-decreasing; by negative association~\cite{joagdev1983} (or independence), $\Cov_{\nu_0}(g(\beta_{\mathrm{loop}}), \beta_{\mathrm{audit}}) \le 0$, giving the stated inequality.

\emph{Part~3 (R3).} By the dual representation of total variation distance, $|\E_{P_{\mathrm{ord}}}[\tau_\pi] - \E_{P_{\mathrm{trap}}}[\tau_\pi]| \le \dTV(P_{\mathrm{ord}}, P_{\mathrm{trap}}) \le \delta_{\mathrm{ind}}$ for all measurable $\tau_\pi : \mathcal{X} \to [0, 1]$, hence $\tau_{\mathrm{trap}}(\pi) \ge \tau_{\mathrm{ord}}(\pi) - \delta_{\mathrm{ind}}$. On $P_{\mathrm{ord}}$, expected gain is at most $\tau_{\mathrm{ord}}(\pi)\Delta R$. On $P_{\mathrm{trap}}$, whenever $C > \frac{\varepsilon_{\mathrm{trap}}}{1-\varepsilon_{\mathrm{trap}}}\Delta R$, each cheating attempt yields expected payoff $\varepsilon_{\mathrm{trap}}\Delta R - (1-\varepsilon_{\mathrm{trap}})C < 0$, so expected gain on $P_{\mathrm{trap}}$ is at most $(\tau_{\mathrm{ord}}(\pi) - \delta_{\mathrm{ind}})[\varepsilon_{\mathrm{trap}}\Delta R - (1-\varepsilon_{\mathrm{trap}})C]$. Combining with mixture weights $(1-\rho)$ and $\rho$, the total expected reward $\E_{P_{\mathrm{mix}}}[\bar{R}_C(\pi)]$ is upper-bounded by
\[
  \tau_{\mathrm{ord}}(\pi)\left[(1-\rho)\Delta R + \rho\big(\varepsilon_{\mathrm{trap}}\Delta R - (1-\varepsilon_{\mathrm{trap}})C\big)\left(1 - \frac{\delta_{\mathrm{ind}}}{\tau_{\mathrm{ord}}(\pi)}\right)\right],
\]
which is strictly decreasing in $\tau_{\mathrm{ord}}(\pi)$ and strictly negative for all $\tau_{\mathrm{ord}}(\pi) \ge \tau_{\min}$ whenever $C > C_{\mathrm{R3}}^*$.
\end{proof}

\begin{remark}[Information-Theoretic Duality and Rare-Attack Floor of Regime~R3]
Total variation bounds are classically used to establish impossibility limits for \emph{monitors} trying to distinguish covert attacks from honest behavior (Neyman--Pearson power ceiling $\alpha + \dTV$). Theorem~\ref{thm:escape}(3) turns the exact same total variation inequality in favor of the \emph{defender}: if planted honeypots are close to ordinary episodes in total variation, no policy can selectively cheat on ordinary episodes while avoiding the traps. However, this guarantee requires $\tau_{\min} > \delta_{\mathrm{ind}}$ and does not block a policy that cheats at a very rare rate $\tau_{\mathrm{ord}} \le \delta_{\mathrm{ind}}$ concentrated exclusively on contexts where $P_{\mathrm{ord}} > P_{\mathrm{trap}}$.
\end{remark}

\section{Numerical Phase Transitions and Exact Verification}

All numerical examples below are generated and checked by the standalone script \texttt{verifier\_exemples\_papier\_v2.py}. The verification suite establishes:
\begin{itemize}
  \item \textbf{Exact rational arithmetic (\texttt{fractions.Fraction}):} for cheating sub-species weights $(1/2, 1/3, 1/6)$ and survival rates $(1/10, 2/5, 9/10)$, $\E_0[\beta] = 1/3$, $\Var_0(\beta) = 37/450$, $\E_{\mathrm{post}}[\beta] = 29/50$, and $\E_{\mathrm{post}}[\beta] - \E_0[\beta] = 37/150 = \Var_0(\beta)/\E_0[\beta]$ holds identically.
  \item \textbf{Deterministic Monte Carlo stress test ($14{,}000$ instances, $0$ violations):} $10{,}000$ random parameter draws for Theorem~\ref{thm:selection}, $2{,}000$ draws for the perfect-stealth inversion~\eqref{eq:inversion}, $1{,}000$ draws for Regime~R2, and $1{,}000$ draws for Regime~R3.
\end{itemize}

\subsection{Phase Transition across Reward Advantage and Optimization Pressure}

For representative parameters $p_{\mathrm{h}} = 0.85$, $p_{\mathrm{v}} = 0.14$, $p_{\mathrm{f}} = 0.01$, $\beta_{\mathrm{h}} = 1.0$, $\beta_{\mathrm{v}} = 0.05$, $\beta_{\mathrm{f}} = 0.75$, $\eta = 3.0$, and $C = 2.5$, Theorem~\ref{thm:selection} predicts $\Delta R_{\mathrm{A}}^* = 0.257992$, $\Delta R_{\mathrm{dom, A}}^* = 1.576778$, and $\Delta R_{\mathrm{dom, B}}^* = 2.807845$ (with asymptotic floor $0.833333$). Tables~\ref{tab:deltaR} and~\ref{tab:eta} confirm these thresholds to full precision.

\begin{table}[ht]
\centering
\caption{Phase transition across reward advantage $\Delta R$ ($p_{\mathrm{h}}=0.85, p_{\mathrm{v}}=0.14, p_{\mathrm{f}}=0.01, \beta_{\mathrm{h}}=1.0, \beta_{\mathrm{v}}=0.05, \beta_{\mathrm{f}}=0.75, \eta=3.0, C=2.5$). Bold entries highlight the crossovers $\Delta R_{\mathrm{A}}^*$, $\Delta R_{\mathrm{dom, A}}^*$, and the high-$\Delta R$ flip of Operator~B. The bold crossover rows ($0.2580$ and $1.5768$) are evaluated at the 4-decimal rounded values of $\Delta R_{\mathrm{A}}^* = 0.257992$ and $\Delta R_{\mathrm{dom, A}}^* = 1.576778$, which accounts for the $2.3 \times 10^{-5}$ difference between $\pi_{\mathrm{A}}(\Pi_{\mathrm{f}}) = 0.340917$ and $\pi_{\mathrm{A}}(\Pi_{\mathrm{h}}) = 0.340894$.}
\label{tab:deltaR}
\small
\setlength{\tabcolsep}{4pt}
\begin{tabular}{@{}rccccccc@{}}
\toprule
$\Delta R$ & $\pi_{\mathrm{no}}(\Pi_{\mathrm{f}})$ & Cond.\ no mon. & $\pi_{\mathrm{A}}(\Pi_{\mathrm{f}})$ & Cond.\ A & $\pi_{\mathrm{A}}(\Pi_{\mathrm{h}})$ & $\pi_{\mathrm{B}}(\Pi_{\mathrm{f}})$ & $\pi_{\mathrm{B}}(\Pi_{\mathrm{h}})$ \\
\midrule
$0.2000$ & $0.016221$ & $0.066667$ & $0.015593$ & $0.517241$ & $0.969854$ & $0.002821$ & $0.997043$ \\
$\mathbf{0.2580}$ & $\mathbf{0.018451}$ & $0.066667$ & $\mathbf{0.018451}$ & $0.517241$ & $0.964329$ & $0.003213$ & $0.996650$ \\
$0.8000$ & $0.044031$ & $0.066667$ & $0.081869$ & $0.517241$ & $0.841721$ & $0.010795$ & $0.989057$ \\
$1.2000$ & $0.057728$ & $0.066667$ & $0.198806$ & $0.517241$ & $0.615641$ & $0.026140$ & $0.973706$ \\
$\mathbf{1.5768}$ & $0.063492$ & $0.066667$ & $\mathbf{0.340917}$ & $0.517241$ & $\mathbf{0.340894}$ & $0.058966$ & $0.940876$ \\
$2.2000$ & $0.066157$ & $0.066667$ & $0.479040$ & $0.517241$ & $0.073856$ & $0.202970$ & $0.796883$ \\
$3.0000$ & $0.066620$ & $0.066667$ & $0.513526$ & $0.517241$ & $0.007182$ & $\mathbf{0.606385}$ & $0.393533$ \\
\bottomrule
\end{tabular}
\end{table}

\begin{table}[ht]
\centering
\caption{Asymptotic divergence as optimization pressure $\eta$ increases at fixed $\Delta R = 0.60 < \frac{1-\beta_{\mathrm{f}}}{\beta_{\mathrm{f}}}C = 0.833333$ (same base parameters as Table~\ref{tab:deltaR}).}
\label{tab:eta}
\small
\begin{tabular}{@{}rcccc@{}}
\toprule
$\eta$ & $\pi_{\mathrm{A}}(\Pi_{\mathrm{h}})$ & $\pi_{\mathrm{A}}(\Pi_{\mathrm{f}})$ & $\pi_{\mathrm{B}}(\Pi_{\mathrm{h}})$ ($C=2.5$) & $\pi_{\mathrm{B}}(\Pi_{\mathrm{f}})$ ($C=2.5$) \\
\midrule
$0.5$ & $0.977491$ & $0.011642$ & $0.941823$ & $0.010152$ \\
$1.0$ & $0.969854$ & $0.015593$ & $0.974980$ & $0.009629$ \\
$2.0$ & $0.946399$ & $0.027725$ & $0.990292$ & $0.008210$ \\
$4.0$ & $0.841721$ & $0.081869$ & $0.994178$ & $0.005808$ \\
$8.0$ & $0.325433$ & $0.348914$ & $0.997107$ & $0.002893$ \\
$16.0$ & $\mathbf{0.003955}$ & $\mathbf{0.515196}$ & $\mathbf{0.999285}$ & $\mathbf{0.000715}$ \\
\bottomrule
\end{tabular}
\end{table}

\subsection{Perfect-Stealth Niche Inversion and Escape-Regime Examples}

When a perfectly stealthy niche exists ($\beta_{\mathrm{f}} = \beta_{\mathrm{h}} = 1.0$, $\beta_{\mathrm{v}} = 0.10$, $p_{\mathrm{h}}=0.85, p_{\mathrm{v}}=0.14, p_{\mathrm{f}}=0.01$, $\eta = 2.0$, $\Delta R = 1.0$),~\eqref{eq:inversion} predicts the exact crossover $\eta(\Delta R + C) = \log(10)/0.9 = 2.558428$, i.e., $C = 0.279214$. Table~\ref{tab:niche} shows that for $C > 0.279214$, Operator~B drives absolute stealth strictly above Operator~A.

\begin{table}[ht]
\centering
\caption{Perfect-stealth niche inversion ($\beta_{\mathrm{f}} = \beta_{\mathrm{h}} = 1.0, \beta_{\mathrm{v}} = 0.10, \eta = 2.0, \Delta R = 1.0$). Above $C = 0.279214$, negative penalty amplifies absolute stealth strictly more than pure rejection. The bold crossover row ($C = 0.2792$) is evaluated at the 4-decimal rounded threshold, giving $\eta(\Delta R + C) = 2.558400$ versus the exact value $2.558428$.}
\label{tab:niche}
\small
\begin{tabular}{@{}rccccc@{}}
\toprule
Penalty $C$ & $\eta(\Delta R + C)$ & $\pi_{\mathrm{no}}(\Pi_{\mathrm{f}})$ & $\pi_{\mathrm{A}}(\Pi_{\mathrm{f}})$ & $\pi_{\mathrm{B}}(\Pi_{\mathrm{f}})$ & $\pi_{\mathrm{B}}(\Pi_{\mathrm{h}})$ \\
\midrule
$0.0000$ & $2.000000$ & $0.037731$ & $0.071924$ & $0.067487$ & $0.776336$ \\
$\mathbf{0.2792}$ & $\mathbf{2.558400}$ & $0.037731$ & $\mathbf{0.071924}$ & $\mathbf{0.071924}$ & $0.827379$ \\
$1.0000$ & $4.000000$ & $0.037731$ & $0.071924$ & $0.077603$ & $0.892711$ \\
$2.5000$ & $7.000000$ & $0.037731$ & $0.071924$ & $\mathbf{0.079814}$ & $0.918135$ \\
\bottomrule
\end{tabular}
\end{table}

For Regime~R1, with $p_{\mathrm{h}} = 0.90, p_{\mathrm{v}} = 0.09, p_{\mathrm{f}} = 0.01, \beta_{\mathrm{h}} = 1.0, \beta_{\mathrm{v}} = 0.10, \beta_{\mathrm{f}} = 0.90$, a maintenance cost $\delta_{\mathrm{maint}} = 1.25$ against $\Delta R_{\mathrm{v}} = 1.0$ yields $\Delta R_{\mathrm{net}} = -0.25$, driving honesty to $\pi_{\mathrm{B}}(\Pi_{\mathrm{h}}) = 0.999998$ at $\eta = 20, C = 2.0$. For Regime~R3, with trap fraction $\rho = 0.20$, trap false-negative rate $\varepsilon_{\mathrm{trap}} = 0.02$, indistinguishability $\delta_{\mathrm{ind}} = 0.05$, minimum targeted cheating rate $\tau_{\min} = 0.20$, and $\Delta R = 1.0$,~\eqref{eq:R3} gives $C_{\mathrm{R3}}^* = 5.462585$.

\section{Limitations and Open Problems}

Our results are intentionally derived in a static, non-parametric Gibbs equilibrium model. Three open problems remain for bridging this exact characterization to practical frontier post-training:
\begin{enumerate}
  \item \textbf{Finite-time stochastic gradient dynamics on neural manifolds:} In parametric policy optimization ($\theta_{t+1} = \theta_t + \gamma_t \hat{g}_t$), implicit gradient bias and finite exploration simultaneously shape effective reachability and multi-objective maintenance costs $\delta_{\mathrm{maint}}(\theta_t)$ well before reaching any Gibbs equilibrium.
  \item \textbf{Multi-monitor coupling and cross-channel covariance:} Regime~R2 requires $\Cov_{\nu_0}(\beta_{\mathrm{loop}}, \beta_{\mathrm{audit}}) \le 0$. When an in-loop monitor and an off-loop audit channel share latent features, characterizing worst-case degradation under constrained coupling remains open.
  \item \textbf{Dynamic monitor-versus-policy allocation and rare-attack floor:} As highlighted in AI control research~\cite{ukaisi2025}, rare interceptions create a non-stationary partial-monitoring trade-off~\cite{bartok2014} between updating the monitor and updating the policy, since policy updates can reduce future observability; moreover, Regime~R3 leaves an irreducible floor for rare attacks with $\tau_{\mathrm{ord}} \le \delta_{\mathrm{ind}}$.
\end{enumerate}
As future work on formal verification, the purely rational algebraic identity underlying Theorem~\ref{thm:selection}(2) (upon setting $E := e^{\eta \Delta R} > 0$) lends itself directly to machine-checked formalization in a proof assistant such as Lean~4.

\begin{thebibliography}{99}

\bibitem{baker2025}
B.~Baker et al.,
\emph{Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation},
arXiv:2503.11926, 2025.

\bibitem{bartok2014}
G.~Bart\'ok, D.~P.~Foster, D.~P\'al, A.~Rakhlin, and C.~Szepesv\'ari,
\emph{Partial Monitoring---Classification, Regret Bounds, and Algorithms},
arXiv:1102.2041, 2014.

\bibitem{gao2022}
L.~Gao, J.~Schulman, and J.~Hilton,
\emph{Scaling Laws for Reward Model Overoptimization},
arXiv:2210.10760, 2022.

\bibitem{greenblatt2023}
R.~Greenblatt et al.,
\emph{AI Control: Improving Safety Despite Intentional Subversion},
arXiv:2312.06942, 2023.

\bibitem{greenblatt2024}
R.~Greenblatt et al.,
\emph{Alignment Faking in Large Language Models},
arXiv:2412.14093, 2024.

\bibitem{griffin2024}
C.~Griffin et al.,
\emph{Games for AI Control: Models of Safety Evaluations of AI Deployment Protocols},
arXiv:2409.07985, 2024.

\bibitem{halberstadt2026}
Y.~Halberstadt,
\emph{Post training is fundamentally dangerous},
LessWrong, post \texttt{CoRJ9saddvsXti4m2}, November 22, 2026.

\bibitem{hardt2016}
M.~Hardt, N.~Megiddo, C.~Papadimitriou, and M.~Wootters,
\emph{Strategic Classification},
arXiv:1506.06980, 2016.

\bibitem{hubinger2024}
E.~Hubinger et al.,
\emph{Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training},
arXiv:2401.05566, 2024.

\bibitem{joagdev1983}
K.~Joag-Dev and F.~Proschan,
\emph{Negative Association of Random Variables with Applications},
The Annals of Statistics, 11(1):286--295, 1983.

\bibitem{skalse2022}
J.~Skalse, N.~H.~R.~Howe, D.~Krasheninnikov, and D.~Krueger,
\emph{Defining and Characterizing Reward Gaming},
arXiv:2209.13085, 2022.

\bibitem{terekhov2025}
M.~Terekhov et al.,
\emph{Control Tax: The Price of Keeping AI in Check},
arXiv:2506.05296, 2025.

\bibitem{testingthewaters2026}
\texttt{testingthewaters},
Comment on \emph{Post training is fundamentally dangerous},
LessWrong, comment \texttt{gFufuPsjYMbutMtkb}, November 2026.

\bibitem{ukaisi2025}
UK AI Security Institute (UK AISI),
\emph{Research Areas in AI Control},
LessWrong, post \texttt{rGcg4XDPDzBFuqNJz}, August 2025.

\bibitem{zhuang2021}
S.~Zhuang and D.~Hadfield-Menell,
\emph{Consequences of Misaligned AI},
arXiv:2102.03896, 2021.

\end{thebibliography}

\end{document}

```

### Input File 3: `verifier_exemples_papier_v2.py`
```python
#!/usr/bin/env python3
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

from __future__ import annotations

import fractions
import json
import math
import os
import pathlib
import random
import sys
from typing import Any

os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
sys.dont_write_bytecode = True

TOL = 1e-11


def dist_no_monitor(
    p_h: float, p_v: float, p_f: float, eta: float, dr_v: float, dr_f: float
) -> tuple[float, float, float]:
    """KL-regularized post-training without monitor (beta == 1), R_h = 0."""
    m = max(0.0, eta * dr_v, eta * dr_f)
    w_h = p_h * math.exp(-m)
    w_v = p_v * math.exp(eta * dr_v - m)
    w_f = p_f * math.exp(eta * dr_f - m)
    z = w_h + w_v + w_f
    return w_h / z, w_v / z, w_f / z


def dist_operator_a(
    p_h: float,
    p_v: float,
    p_f: float,
    beta_h: float,
    beta_v: float,
    beta_f: float,
    eta: float,
    dr_v: float,
    dr_f: float,
) -> tuple[float, float, float]:
    """Operator A: pure rejection with resampling (discard and try again)."""
    m = max(0.0, eta * dr_v, eta * dr_f)
    w_h = beta_h * p_h * math.exp(-m)
    w_v = beta_v * p_v * math.exp(eta * dr_v - m)
    w_f = beta_f * p_f * math.exp(eta * dr_f - m)
    z = w_h + w_v + w_f
    return w_h / z, w_v / z, w_f / z


def dist_operator_b(
    p_h: float,
    p_v: float,
    p_f: float,
    beta_h: float,
    beta_v: float,
    beta_f: float,
    eta: float,
    dr_v: float,
    dr_f: float,
    penalty_c: float,
) -> tuple[float, float, float]:
    """Operator B: KL-regularized policy update with interception penalty -C."""
    r_h = -(1.0 - beta_h) * penalty_c
    r_v = beta_v * dr_v - (1.0 - beta_v) * penalty_c
    r_f = beta_f * dr_f - (1.0 - beta_f) * penalty_c
    m = max(eta * r_h, eta * r_v, eta * r_f)
    w_h = p_h * math.exp(eta * r_h - m)
    w_v = p_v * math.exp(eta * r_v - m)
    w_f = p_f * math.exp(eta * r_f - m)
    z = w_h + w_v + w_f
    return w_h / z, w_v / z, w_f / z


def verify_exact_rational_identity() -> dict[str, str]:
    F = fractions.Fraction
    weights = [F(1, 2), F(1, 3), F(1, 6)]
    betas = [F(1, 10), F(2, 5), F(9, 10)]
    assert sum(weights) == F(1, 1)
    mean_0 = sum(w * b for w, b in zip(weights, betas))
    var_0 = sum(w * (b - mean_0) ** 2 for w, b in zip(weights, betas))
    post_weights = [(w * b) / mean_0 for w, b in zip(weights, betas)]
    mean_post = sum(pw * b for pw, b in zip(post_weights, betas))
    assert mean_post - mean_0 == var_0 / mean_0
    assert var_0 > 0
    return {
        "E0_beta": str(mean_0),
        "Var0_beta": str(var_0),
        "Epost_beta": str(mean_post),
        "delta_exact": str(mean_post - mean_0),
        "ratio_exact": str(var_0 / mean_0),
    }


def run_monte_carlo_suite() -> dict[str, int]:
    # 1. 10,000 general instances for Theorem 1
    rng = random.Random(20261124)
    violations_t1 = 0
    for _ in range(10_000):
        u1, u2, u3 = rng.uniform(0.02, 1.0), rng.uniform(0.02, 1.0), rng.uniform(0.02, 1.0)
        s = u1 + u2 + u3
        p_h, p_v, p_f = u1 / s, u2 / s, u3 / s
        beta_h = rng.uniform(0.55, 1.0)
        beta_f = rng.uniform(0.20, beta_h)
        beta_v = rng.uniform(0.0, beta_f - 1e-3)
        eta = rng.uniform(0.1, 8.0)
        dr = rng.uniform(0.05, 5.0)
        c_pen = rng.uniform(0.0, 4.0)

        h0, v0, f0 = dist_no_monitor(p_h, p_v, p_f, eta, dr, dr)
        ha, va, fa = dist_operator_a(p_h, p_v, p_f, beta_h, beta_v, beta_f, eta, dr, dr)
        hb, vb, fb = dist_operator_b(p_h, p_v, p_f, beta_h, beta_v, beta_f, eta, dr, dr, c_pen)

        if not (fa / (va + fa) > f0 / (v0 + f0) + 1e-14 and fb / (vb + fb) > f0 / (v0 + f0) + 1e-14):
            violations_t1 += 1

        lhs_a = (beta_f - beta_v) * p_v * math.exp(eta * dr)
        rhs_a = (beta_h - beta_f) * p_h
        if abs(lhs_a - rhs_a) > 1e-9 and ((lhs_a > rhs_a) != (fa > f0)):
            violations_t1 += 1

        lhs_dom_b = eta * (beta_f * dr - (beta_h - beta_f) * c_pen)
        rhs_dom_b = math.log(p_h / p_f)
        if abs(lhs_dom_b - rhs_dom_b) > 1e-9 and ((lhs_dom_b > rhs_dom_b) != (fb > hb)):
            violations_t1 += 1

        lhs_amp_b = p_v * (1.0 - math.exp(-eta * (beta_f - beta_v) * (dr + c_pen)))
        rhs_amp_b = p_h * math.exp(-eta * dr) * (
            math.exp(eta * ((1.0 - beta_f) * dr + (beta_h - beta_f) * c_pen)) - 1.0
        )
        if abs(lhs_amp_b - rhs_amp_b) > 1e-9 and ((lhs_amp_b > rhs_amp_b) != (fb > f0)):
            violations_t1 += 1

    # 2. 2,000 instances for perfect-stealth niche inversion
    rng2 = random.Random(314159)
    violations_niche = 0
    for _ in range(2_000):
        p_h, p_v, p_f = 0.70, 0.25, 0.05
        beta_v = rng2.uniform(0.05, 0.90)
        eta = rng2.uniform(0.2, 5.0)
        dr = rng2.uniform(0.1, 3.0)
        c_pen = rng2.uniform(0.0, 3.0)
        _, _, f0 = dist_no_monitor(p_h, p_v, p_f, eta, dr, dr)
        _, _, fa = dist_operator_a(p_h, p_v, p_f, 1.0, beta_v, 1.0, eta, dr, dr)
        _, _, fb = dist_operator_b(p_h, p_v, p_f, 1.0, beta_v, 1.0, eta, dr, dr, c_pen)
        if not (fa > f0):
            violations_niche += 1
        thresh = math.log(1.0 / beta_v) / (1.0 - beta_v)
        val = eta * (dr + c_pen)
        if abs(val - thresh) > 1e-9 and ((fb > fa) != (val > thresh)):
            violations_niche += 1

    # 3. 1,000 instances for R2
    rng3 = random.Random(271828)
    violations_r2 = 0
    for _ in range(1_000):
        b_loop = [rng3.uniform(0.05, 0.95) for _ in range(4)]
        b_sorted = sorted(rng3.uniform(0.05, 0.95) for _ in range(4))
        ranks = sorted(range(4), key=lambda i: b_loop[i])
        b_audit = [0.0] * 4
        for pos, idx in enumerate(ranks):
            b_audit[idx] = b_sorted[3 - pos]
        before = sum(b_audit) / 4.0
        eta = rng3.uniform(0.5, 6.0)
        dr = rng3.uniform(0.5, 3.0)
        c_pen = rng3.uniform(0.0, 3.0)
        za = sum(b_loop)
        after_a = sum((b_loop[i] / za) * b_audit[i] for i in range(4))
        wb = [math.exp(eta * b_loop[i] * (dr + c_pen)) for i in range(4)]
        zb = sum(wb)
        after_b = sum((wb[i] / zb) * b_audit[i] for i in range(4))
        if after_a > before + TOL or after_b > before + TOL:
            violations_r2 += 1

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

    assert violations_t1 == 0
    assert violations_niche == 0
    assert violations_r2 == 0
    assert violations_r3 == 0
    return {
        "theorem_1_instances": 10_000,
        "perfect_niche_instances": 2_000,
        "regime_r2_instances": 1_000,
        "regime_r3_instances": 1_000,
        "total_instances": 14_000,
        "total_violations": 0,
    }


def compute_paper_tables() -> dict[str, Any]:
    # Table 1: Phase transition across Delta R (canonical reference parameters)
    p_h, p_v, p_f = 0.85, 0.14, 0.01
    beta_h, beta_v, beta_f = 1.0, 0.05, 0.75
    eta = 3.0
    c_pen = 2.5

    dr_amp_a = (1.0 / eta) * (math.log(p_h / p_v) + math.log((beta_h - beta_f) / (beta_f - beta_v)))
    dr_dom_a = (1.0 / eta) * (math.log(p_h / p_f) + math.log(beta_h / beta_f))
    dr_asymp_b = ((beta_h - beta_f) / beta_f) * c_pen
    dr_dom_b = dr_asymp_b + (1.0 / (eta * beta_f)) * math.log(p_h / p_f)

    table1_rows = []
    for dr in (0.2, round(dr_amp_a, 4), 0.8, 1.2, round(dr_dom_a, 4), 2.2, 3.0):
        _, v0, f0 = dist_no_monitor(p_h, p_v, p_f, eta, dr, dr)
        ha, va, fa = dist_operator_a(p_h, p_v, p_f, beta_h, beta_v, beta_f, eta, dr, dr)
        hb, vb, fb = dist_operator_b(p_h, p_v, p_f, beta_h, beta_v, beta_f, eta, dr, dr, c_pen)
        table1_rows.append(
            {
                "delta_r": dr,
                "pi_no_f": round(f0, 6),
                "cond_no_f": round(f0 / (v0 + f0), 6),
                "pi_A_f": round(fa, 6),
                "cond_A_f": round(fa / (va + fa), 6),
                "pi_A_h": round(ha, 6),
                "pi_B_f": round(fb, 6),
                "cond_B_f": round(fb / (vb + fb), 6),
                "pi_B_h": round(hb, 6),
            }
        )

    # Table 2: Asymptotic divergence as eta -> inf at Delta R = 0.60, C = 2.5
    table2_rows = []
    for eta_val in (0.5, 1.0, 2.0, 4.0, 8.0, 16.0):
        ha, _, fa = dist_operator_a(p_h, p_v, p_f, beta_h, beta_v, beta_f, eta_val, 0.6, 0.6)
        hb, _, fb = dist_operator_b(p_h, p_v, p_f, beta_h, beta_v, beta_f, eta_val, 0.6, 0.6, c_pen)
        table2_rows.append(
            {
                "eta": eta_val,
                "pi_A_h": round(ha, 6),
                "pi_A_f": round(fa, 6),
                "pi_B_h": round(hb, 6),
                "pi_B_f": round(fb, 6),
            }
        )

    # Table 3: Perfect-stealth niche inversion (beta_h = beta_f = 1.0, beta_v = 0.10, Delta R = 1.0, eta = 2.0)
    beta_v_niche = 0.10
    eta_niche = 2.0
    dr_niche = 1.0
    inversion_threshold_eta_drc = math.log(1.0 / beta_v_niche) / (1.0 - beta_v_niche)
    c_crossover = inversion_threshold_eta_drc / eta_niche - dr_niche
    table3_rows = []
    for c_val in (0.0, round(c_crossover, 4), 1.0, 2.5):
        h0, _, f0 = dist_no_monitor(p_h, p_v, p_f, eta_niche, dr_niche, dr_niche)
        ha, _, fa = dist_operator_a(p_h, p_v, p_f, 1.0, beta_v_niche, 1.0, eta_niche, dr_niche, dr_niche)
        hb, _, fb = dist_operator_b(p_h, p_v, p_f, 1.0, beta_v_niche, 1.0, eta_niche, dr_niche, dr_niche, c_val)
        table3_rows.append(
            {
                "C": c_val,
                "eta_times_dr_plus_C": round(eta_niche * (dr_niche + c_val), 6),
                "pi_no_f": round(f0, 6),
                "pi_A_f": round(fa, 6),
                "pi_B_f": round(fb, 6),
                "pi_B_h": round(hb, 6),
            }
        )

    # Concrete R1 example: multi-objective maintenance cost
    hb_r1, vb_r1, fb_r1 = dist_operator_b(0.90, 0.09, 0.01, 1.0, 0.10, 0.90, 20.0, 1.0, -0.25, 2.0)

    # Concrete R3 example: planted honeypots
    rho_r3, eps_r3, delta_ind_r3, tau_min_r3, dr_r3 = 0.20, 0.02, 0.05, 0.20, 1.0
    c_star_r3 = (
        ((1.0 - rho_r3) * tau_min_r3 + rho_r3 * eps_r3 * (tau_min_r3 - delta_ind_r3))
        / (rho_r3 * (1.0 - eps_r3) * (tau_min_r3 - delta_ind_r3))
        * dr_r3
    )

    return {
        "thresholds_table1": {
            "dr_amp_A": round(dr_amp_a, 6),
            "dr_dom_A": round(dr_dom_a, 6),
            "dr_asymp_B": round(dr_asymp_b, 6),
            "dr_dom_B": round(dr_dom_b, 6),
        },
        "table1_phase_transition": table1_rows,
        "table2_eta_divergence": table2_rows,
        "table3_perfect_niche_inversion": {
            "params": {"p_h": p_h, "p_v": p_v, "p_f": p_f, "beta_v": beta_v_niche, "beta_f": 1.0, "beta_h": 1.0, "eta": eta_niche, "delta_r": dr_niche},
            "threshold_eta_dr_plus_C": round(inversion_threshold_eta_drc, 6),
            "C_crossover": round(c_crossover, 6),
            "rows": table3_rows,
        },
        "example_R1": {
            "p_h": 0.90,
            "p_v": 0.09,
            "p_f": 0.01,
            "beta_h": 1.0,
            "beta_v": 0.10,
            "beta_f": 0.90,
            "eta": 20.0,
            "delta_r_v": 1.0,
            "delta_r_f_net": -0.25,
            "C": 2.0,
            "pi_B_h": round(hb_r1, 6),
            "pi_B_v_plus_f": round(vb_r1 + fb_r1, 6),
        },
        "example_R3": {
            "rho": rho_r3,
            "eps_trap": eps_r3,
            "delta_ind": delta_ind_r3,
            "tau_min": tau_min_r3,
            "delta_r": dr_r3,
            "C_star_R3": round(c_star_r3, 6),
        },
    }


def main() -> None:
    rational = verify_exact_rational_identity()
    mc = run_monte_carlo_suite()
    tables = compute_paper_tables()
    out = {
        "script": "verifier_exemples_papier_v2.py",
        "exact_rational_variance_identity": rational,
        "monte_carlo_verification": mc,
        "verified_examples": tables,
    }
    out_path = pathlib.Path(__file__).resolve().parent / "exemples-verifies-papier-v2.json"
    out_path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()

```
