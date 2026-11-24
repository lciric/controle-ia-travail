#!/usr/bin/env python3
"""Construit audit-budget-section-v1-correctif-5.tex à partir du correctif 4.

Chaque remplacement manuel est exact et compté (une occurrence attendue) ;
les renommages de notation sont des expressions régulières bornées, contrôlées
ensuite par relecture du diff et par recherche des restes.
Usage : build_c5.py CORRECTIF4 SORTIE
"""
import re
import sys

src, out = sys.argv[1], sys.argv[2]
t = open(src, encoding="utf-8").read()

BLOCKS = {}


def rep(old, new, count=1):
    """Remplacement exact, compté."""
    global t
    n = t.count(old)
    if n != count:
        raise SystemExit(f"attendu {count}, trouvé {n} : {old[:70]!r}")
    t = t.replace(old, new)


def block(name, start, end, new):
    """Remplace le texte de `start` (inclus) à `end` (exclu) par un bloc protégé."""
    global t
    if t.count(start) != 1 or t.count(end) != 1:
        raise SystemExit(f"bornes non uniques pour {name}: {t.count(start)}, {t.count(end)}")
    i, j = t.index(start), t.index(end)
    assert i < j, name
    key = f"@@{name}@@"
    BLOCKS[key] = new
    t = t[:i] + key + t[j:]


# ---------------------------------------------------------------- B0 en-tête
B0_NEW = (r"""% ---------------------------------------------------------------------------
% Section: audit budgets in the sequential game (fragment, no preamble).
% Requires amsmath and amsthm; the macros \E, \Prob, \Var and \DKL and the
% environments theorem, proposition and remark of the manuscript; and three
% environments that the manuscript does not define yet, to be added to its
% preamble on the common counter:
%   \newtheorem{lemma}[theorem]{Lemma}
%   \newtheorem{corollary}[theorem]{Corollary}
%   \theoremstyle{definition}\newtheorem{definition}[theorem]{Definition}
% All labels are prefixed by "audit". The manuscript is referred to through
% \ref{thm:escape}, \ref{sec:reward} and \eqref{eq:R3} only.
% Citation keys that are not yet in the bibliography of the manuscript are
% provided, as \bibitem entries, in a companion file.
% ---------------------------------------------------------------------------
""")
_i = t.index(r"\section{How many audits?")
BLOCKS["@@B0@@"] = B0_NEW
t = "@@B0@@" + t[_i:]

# ---------------------------------------------------------------- B1 chapeau
block("B1", "The static analysis charges every episode", r"\subsection{Setting}", r"""In Regime~R3 of Theorem~\ref{thm:escape} every episode is a trap with the
same probability $\rho$, whatever the length of training. An auditor,
however, has a total budget: over the $N$ training episodes it can inspect at
most $B\ll N$ of them. This section asks how large $B$ must be, in three
complementary senses: so that the \emph{training signal} never favours the
stealthy stratum (Theorem~\ref{thm:audit-deterrence}); so that a cheating
policy is \emph{caught} at least once (Theorem~\ref{thm:audit-detection}); and
so that a \emph{randomised} implementation of the first schedule works with
high probability (Theorem~\ref{thm:audit-random}). The analysis is no longer
static: it follows the policy along a finite-time training dynamics, defined
below, whose fixed point is the Gibbs law of the previous sections. Throughout
this section the audit is the only oversight (there is no in-loop monitor, or
a blind one), and we follow the two strata $\Pi_{\mathrm h}$ (honest) and
$\Pi_{\mathrm f}$ (stealthy cheating). We write
\[
  L:=\log\frac{p_{\mathrm h}}{p_{\mathrm f}}
\]
for the prior barrier
$\Delta\DKL(\Pi_{\mathrm f}\,\|\,\Pi_{\mathrm h};\pi_0)$ of Regime~R1, so that
the prior log-odds of stealth against honesty are $-L$; the case of interest
is $p_{\mathrm f}<p_{\mathrm h}$, that is $L>0$, although no statement below
needs it. The reward advantage of the stealthy stratum is
$\Delta R_{\mathrm f}>0$ (Section~\ref{sec:reward}).

""")

# ------------------------------------------------- B2 dynamique et lemme (D1)
block("B2", r"\paragraph{Dynamics.} We use the logit recursion", r"\paragraph{Audit schedules and budget.}", r"""\paragraph{Dynamics.} The previous sections describe an equilibrium. Here
training proceeds in steps $k=0,1,2,\dots$, and the reward may change with the
step. Let $\eta\in(0,\infty]$ be the optimization pressure, let
$\gamma\in(0,\eta]$ be a finite step size, and put
$a:=1-\gamma/\eta\in[0,1]$ ($a=1$ iff $\eta=\infty$, the case without KL
anchoring). At step $k$ the policy is trained on a bounded measurable reward
$r_k:\Pi\to\mathbb R$, the expected effective reward of each trajectory at
that step, and its law $\pi_k$ is the exponential tilt of the base law given
by
\begin{equation}\label{eq:audit-dyn}
  \pi_k(d\pi)\;\propto\;e^{\phi_k(\pi)}\,\pi_0(d\pi),\qquad
  \phi_0\equiv0,\qquad \phi_{k+1}=a\,\phi_k+\gamma\,r_k .
\end{equation}
Equivalently, $d\pi_{k+1}/d\pi_0\propto(d\pi_k/d\pi_0)^{a}\,e^{\gamma r_k}$,
and $\pi_{k+1}$ is the unique maximizer of
$\gamma\,\E_{\pi}[r_k]-(1-a)\,\DKL(\pi\,\|\,\pi_0)-a\,\DKL(\pi\,\|\,\pi_k)$:
since $1-a=\gamma/\eta$, this is one step of size $\gamma$, proximal relative
to the current policy, on the KL-regularized objective
$\E_{\pi}[r_k]-\eta^{-1}\DKL(\pi\,\|\,\pi_0)$ that defines the Gibbs laws of
the previous sections. In a tabular softmax parametrization
($\pi_\theta(x)\propto e^{\theta_x}$ on a finite set of trajectories, with
$\theta_0=\log\pi_0$), \eqref{eq:audit-dyn} is natural-gradient ascent with
step $\gamma$ on $V_k(\pi):=\E_{\pi}[r_k]-\eta^{-1}\DKL(\pi\,\|\,\pi_0)$: the
Fisher matrix is
$F=\operatorname{diag}(\pi_\theta)-\pi_\theta\pi_\theta^{\top}$, the gradient
of $V_k\circ\pi_\theta$ is $F\,\nabla_\pi V_k$, and $F^{\dagger}F$ is the
projector orthogonal to the constant vectors, which do not move $\pi_\theta$;
since $\nabla_\pi V_k=r_k-\eta^{-1}(\theta-\theta_0)$ up to a constant vector,
the update is
$\theta_{k+1}=\theta_k+\gamma\bigl(r_k-(\theta_k-\theta_0)/\eta\bigr)$, which
is \eqref{eq:audit-dyn} with $\phi_k=\theta_k-\theta_0$.

If the reward does not change, $r_k\equiv r$, and $\eta<\infty$, then
$\phi_k=\eta(1-a^k)\,r$: the iterate $\pi_k\propto e^{\eta(1-a^k)r}\pi_0$ is
the Gibbs law at the effective pressure $\eta(1-a^k)$, and it converges to the
fixed point $\pi\propto e^{\eta r}\pi_0$ (reached in one step if
$\gamma=\eta$). For $r=\bar R_C$ this fixed point is Operator~B; when the
in-loop monitor is blind ($\beta\equiv1$, hence $\bar R_C=R$) it is the
unmonitored baseline $\pi_{\mathrm{no}}^{(\eta)}$. The statics of this
dynamics are thus those of the previous sections; only the path is new.

\begin{lemma}[Log-odds under a time-varying reward]\label{lem:audit-logodds}
Let $\pi_k$ follow \eqref{eq:audit-dyn} with rewards $r_k$ that are constant
on $\Pi_{\mathrm h}$ and on $\Pi_{\mathrm f}$, with values $r_k^{\mathrm h}$
and $r_k^{\mathrm f}$. Write
$\ell_k:=\log\bigl(\pi_k(\Pi_{\mathrm f})/\pi_k(\Pi_{\mathrm h})\bigr)$ and
$d_j:=r_j^{\mathrm f}-r_j^{\mathrm h}$. Then $\ell_0=-L$ and, with the
convention $0^0=1$,
\begin{equation}\label{eq:audit-logodds}
  \ell_k \;=\; -L+\gamma\sum_{j=0}^{k-1}a^{\,k-1-j}\,d_j ,\qquad k\ge 0 ,
\end{equation}
whatever the rewards on the visible stratum $\Pi_{\mathrm v}$.
\end{lemma}
\begin{proof}
By induction on \eqref{eq:audit-dyn}, $\phi_k$ is constant on
$\Pi_{\mathrm h}$ and on $\Pi_{\mathrm f}$, with values $\phi_k^{\mathrm h}$
and $\phi_k^{\mathrm f}$. Hence
$\pi_k(\Pi_s)=p_s\,e^{\phi_k^{s}}/Z_k$ for $s\in\{\mathrm h,\mathrm f\}$,
where $Z_k:=\int_\Pi e^{\phi_k}\,d\pi_0$, and
$\ell_k=-L+\phi_k^{\mathrm f}-\phi_k^{\mathrm h}$. Subtracting the two values
of the recursion gives $\ell_{k+1}+L=a(\ell_k+L)+\gamma d_k$; unroll from
$\ell_0+L=0$. The visible stratum enters only through $Z_k$, which cancels in
the ratio.
\end{proof}

Dropping the visible stratum is therefore exact for the log-odds, not an
approximation: $\Pi_{\mathrm v}$ changes the masses $\pi_k(\Pi_{\mathrm h})$
and $\pi_k(\Pi_{\mathrm f})$ but not their ratio. All the statements of this
section are about $\ell_k$.

""")

# ------------------------------------------ B3 plans d'audit et budget (D3)
block("B3", r"\paragraph{Audit schedules and budget.}", r"We write $G_k:=\gamma\sum_{i<k}a^i$", r"""\paragraph{Audit schedules and budget.} Training runs for $K$ steps with
$n\ge1$ episodes per step, $N:=nK$ episodes in all. A (deterministic,
fractional) \emph{audit schedule} is a vector
$\rho=(\rho_0,\dots,\rho_{K-1})\in[0,1]^K$: at step $j$ a fraction $\rho_j$ of
the $n$ episodes is audited. Its budget is $B(\rho):=n\sum_{j<K}\rho_j$. We
assume that audits are infallible; that the policy cannot tell audited from
non-audited episodes ($\delta_{\mathrm{ind}}=0$ in the notation of Regime~R3;
Proposition~\ref{prop:audit-indist} relaxes this); that there is no in-loop
monitor, or one that is blind on the two strata
($\beta_{\mathrm f}=\beta_{\mathrm h}=1$); and that an audited honest episode
is never penalised (no false positive). A stealthy trajectory earns the
advantage $\Delta R_{\mathrm f}>0$ if it is not audited; if it is, it forfeits
$\Delta R_{\mathrm f}$ and receives the score $-C_{\mathrm{aud}}\le0$. We
write $C_{\mathrm{aud}}$ for this audit penalty, to keep it apart from the
interception penalty $C$ of Operator~B; it plays the role of $C$ in Regime~R3
and, like $C$ in Section~\ref{sec:reward}, it is a gap to the honest reward,
normalized to $0$. Taking for $r_j$ the expectation over the audit draw, the
mean-field dynamics has
\begin{equation}\label{eq:audit-adv}
  d_j=(1-\rho_j)\Delta R_{\mathrm f}-\rho_j C_{\mathrm{aud}}
     =\Delta R_{\mathrm f}-W\rho_j,\qquad W:=\Delta R_{\mathrm f}+C_{\mathrm{aud}} .
\end{equation}
Two extensions follow by substitution, under conditions that we state without
developing them. An audit that misses a stealthy episode with probability
$\varepsilon_{\mathrm{aud}}$ (the analogue of $\varepsilon_{\mathrm{trap}}$ in
Regime~R3) replaces $W$ by $(1-\varepsilon_{\mathrm{aud}})W$ and
$C_{\mathrm{aud}}$ by
$C_{\mathrm{aud}}':=(1-\varepsilon_{\mathrm{aud}})C_{\mathrm{aud}}-\varepsilon_{\mathrm{aud}}\Delta R_{\mathrm f}$,
provided $C_{\mathrm{aud}}'\ge0$; otherwise full auditing does not make
stealth unprofitable and the uniform program can be infeasible. An in-loop
monitor under Operator~B with $\beta_{\mathrm h}=1$ and penalty $C$ replaces
$\Delta R_{\mathrm f}$ by
$\beta_{\mathrm f}\Delta R_{\mathrm f}-(1-\beta_{\mathrm f})C$, when this is
positive.

""")

# limite statique : lien avec R1 et R3 (D1)
rep(r"""Without audits $x_k=x^{u}_k:=\Delta R\,G_k$, which is nondecreasing in $k$ and
bounded by $\eta\Delta R$.
""", r"""Without audits $x_k=x^{u}_k:=\Delta R\,G_k$, which is nondecreasing in $k$ and
bounded by $\eta\Delta R$. @@B3bis@@
""")
BLOCKS["@@B3bis@@"] = r"""With a constant rate $\rho_j\equiv\rho$ and
$\eta<\infty$, $x_k=(\Delta R_{\mathrm f}-W\rho)\,G_k\to\eta\,(\Delta R_{\mathrm f}-W\rho)$:
the limit is the Operator~B log-odds of Regime~R1 with $\beta_{\mathrm h}=1$,
$\beta_{\mathrm f}=1-\rho$ and $C=C_{\mathrm{aud}}$, and stealth is unprofitable
there ($\Delta R_{\mathrm f}<W\rho$) iff
$C_{\mathrm{aud}}>(1-\rho)\Delta R_{\mathrm f}/\rho$, which is the threshold
$C^*_{\mathrm{R3}}$ of~\eqref{eq:R3} at
$\varepsilon_{\mathrm{trap}}=\delta_{\mathrm{ind}}=0$."""

rep(r"so that $G_k=\eta(1-a^k)$ if $\eta<\infty$",
    r"so that $G_k=\eta(1-a^k)$ if $\eta<\infty$ (the effective pressure after $k$ steps)")

# ------------------------------------------------ D12.1 remarque des critères
rep(r"and, for the uniform criterion, from an upper bound on $\gamma$. The final-criterion budget is not monotone in $\gamma$.",
    "and, for the uniform criterion, from an upper bound on $\\gamma$. @@B4@@")
BLOCKS["@@B4@@"] = r"""For the final criterion there is no such safe direction in $\gamma$: computed from an upper bound on $\gamma$, the back-loaded schedule can be infeasible when $\eta<\infty$ (for $\hat\gamma=\eta>\gamma$ it leaves $x_K-c=a\,(\Delta R_{\mathrm f}\,G_{K-1}-c)$, which is positive as soon as the niche would emerge by step $K-1$), and computed from a lower bound $\hat\gamma<\gamma$ it is infeasible at $\eta=\infty$ whenever $c>0$ and audits are needed."""

# --------------------------------- D3 : théorème de détection, partie (c)
i = t.index(r"\item[\textup{(c)}] \textbf{Certifying a rate.}")
j = t.index(r"\end{enumerate}", i)
seg = t[i:j]
print("(c) énoncé :", seg.count(r"\varepsilon'"), seg.count(r"\varepsilon"), seg.count(r"\alpha"), seg.count(r"\beta"))
seg = seg.replace(r"\varepsilon'", r"\vartheta").replace(r"\varepsilon", r"\vartheta_1")
seg = seg.replace(r"\alpha", r"\mathrm{err}_{\mathrm I}").replace(r"\beta", r"\mathrm{err}_{\mathrm{II}}")
t = t[:i] + seg + t[j:]

i = t.index(r"(c) Let $q_0\in[0,1]$ be the probability")
j = t.index(r"\end{proof}", i)
seg = t[i:j]
print("(c) preuve :", seg.count(r"\varepsilon'"), seg.count(r"\varepsilon"), seg.count(r"\alpha"), seg.count(r"\beta"))
seg = seg.replace(r"\varepsilon'", r"\vartheta").replace(r"\varepsilon", r"\vartheta_1")
seg = seg.replace(r"\alpha", r"\mathrm{err}_{\mathrm I}").replace(r"\beta", r"\mathrm{err}_{\mathrm{II}}")
t = t[:i] + seg + t[j:]

# ------------------------------------ B5 remarque détection / dissuasion
rep(r"only on the about $n\,\pi_k(f)$ sampled stealthy episodes of a step, of which about $n\rho\,\pi_k(f)$ are audited",
    r"only on the about $n\,\pi_j(\Pi_{\mathrm f})$ sampled stealthy episodes of step $j$, of which about $n\rho_j\,\pi_j(\Pi_{\mathrm f})$ are audited")
rep(r"its variance is of order $1/(n\,\pi_k(f))$", r"its variance is of order $1/(n\,\pi_j(\Pi_{\mathrm f}))$")
rep(r"""Under sampling without replacement from $T$ episodes of which
$\varepsilon T$ are cheats, $q\le(1-\varepsilon)^B$, so the finite population""",
    r"""Under sampling without replacement from $T$ episodes of which
$\vartheta_1 T$ are cheats, $q\le(1-\vartheta_1)^B$, so the finite population""")

# ------------------------------------ B6 théorème aléatoire : (b) et preuve
rep(r"The number of audits $N:=\sum_{j,i}A_{j,i}$ satisfies", r"The number of audits $\hat B:=\sum_{j,i}A_{j,i}$ satisfies")
rep(r"$\Prob\bigl(N>B(\rho)+", r"$\Prob\bigl(\hat B>B(\rho)+")
rep(r"""\le v:=(\gamma W)^2\bar\rho\,\Gamma_K/n$. Bernstein's
inequality~\cite[Theorem~2.10 and Corollary~2.11, to be checked]{boucheron2013concentration} gives
$\Prob(\pm\sum X_{j,i}\ge t)\le\exp\bigl(-t^2/(2v+2bt/3)\bigr)$, which is at most
$e^{-\Lambda}$ for $t=\sqrt{2v\Lambda}+2b\Lambda/3=""",
    r"""\le\sigma^2:=(\gamma W)^2\bar\rho\,\Gamma_K/n$. Bernstein's
inequality~\cite{boucheron2013concentration} gives
$\Prob(\pm\sum X_{j,i}\ge t)\le\exp\bigl(-t^2/(2\sigma^2+2bt/3)\bigr)$, which is at most
$e^{-\Lambda}$ for $t=\sqrt{2\sigma^2\Lambda}+2b\Lambda/3=""")
rep(r"\operatorname{Var}", r"\Var")

# ------------------------------------ B7 remarque sur le théorème aléatoire
rep(r"For $\eta=\infty$ it is $O(\sqrt{T\log(K/\delta)})$, negligible",
    r"For $\eta=\infty$ it is $O(\sqrt{T\log(K/\delta)})$, asymptotically negligible")
rep(r"""Theorem~\ref{thm:audit-random} is an upper bound only; we do not claim that the
margin is necessary.""",
    r"""Theorem~\ref{thm:audit-random} is an upper bound only; we do not claim that a
margin of the order of $\varepsilon$ is necessary
(Remark~\ref{rem:audit-random-sim}).""")
rep(r"inequality~\cite{freedman1975tail} gives the analogue of (a) with $2bt/3$ replaced by $2bt$, provided",
    r"inequality~\cite{freedman1975tail} gives an analogue of (a), with another constant in the linear term, provided")

# ------------------------------------ B8 remarque de simulation (D4-D6, D11, D12.5)
block("B8", "% Provenance of the figures of the next remark (R6)", r"\subsection{Imperfect indistinguishability}", r"""% Provenance of the figures of the next remark: preregistered simulation run by the
%   script experience_seuil_chantier3_v3.py
%   (SHA-256 535808bc8b5a79404db5257e3ab5770ad00820ec06bfbb492167ffb43b9602a2);
%   sealed outputs sorties-brutes.json
%   (SHA-256 f739c1df19b015b57c0ec817b13feba10e36ffd2dbde63bb315649f4445954c6);
%   reading verdict verdict-lecture-seuil-chantier3-2026-11-24-v1.md
%   (SHA-256 6967654e12881835fc950c0c20b96dee1224cfe904601f7eaeca01c1814af288).
\begin{remark}[A preregistered simulation of the margin]\label{rem:audit-random-sim}
We simulated the open-loop schedule of Theorem~\ref{thm:audit-random}(c) on a grid of $144$ configurations ($K\in\{50,200,500\}$, $n\in\{100,1000\}$, $\gamma\in\{0.05,0.2\}$, $\eta\in\{1,10,\infty\}$, $C_{\mathrm{aud}}\in\{4,19\}$, $\delta\in\{0.05,0.1\}$, $\Delta R_{\mathrm f}=1$, headroom $c=\tfrac12\Delta R_{\mathrm f}\,G_K$), with the predictions and reading criteria fixed before any draw. In $6$ of the $144$ configurations ($n=100$, $\gamma=0.2$, $\eta=1$, $C_{\mathrm{aud}}=19$) the margin exceeds the headroom, $\varepsilon>c$: the hypothesis of part~(c) fails, and the theorem guarantees nothing there. The remaining $138$ were simulated, with $10^5$ independent replications per configuration and margin. With the margin $\varepsilon$ of the theorem, the threshold was never crossed by the uncapped process, and the frequency of crossing by the capped process stayed below $\delta$, in all $138$ configurations. The reading criteria also require the crossing to be seen once the margin is removed; on this basis the guarantee is confirmed in $137$ configurations, and the remaining one is inconclusive (its reading without margin is sensitive to the numerical tolerance), not contradicted. Without margin the mean-field path of the just-in-time schedule sits on the threshold (Theorem~\ref{thm:audit-deterrence}(i)), and the threshold is crossed with frequency at least $0.86$ (median $0.97$): some positive margin is needed; the order of $\varepsilon$ is not claimed. On this grid the margin of the theorem is conservative. An oracle estimate of the smallest margin that keeps the crossing frequency of the uncapped process at most $\delta/2$, the level of the proof of part~(c), was located by bisection on the simulated frequency in the $137$ configurations where the crossing is seen without margin; it is smaller than $\varepsilon$ by a factor between $1.75$ and $3.56$ (median $2.49$). This oracle margin is calibrated by simulation with all parameters known, and nothing here shows that it could be used in practice. The margin is not the budget, and the saving is measured on the expected number of audits $B_\varepsilon$ of the schedule, not on the reserved number $B_{\mathrm{rand}}$: planning with the oracle margin in place of $\varepsilon$ would lower $B_\varepsilon$ by between $2\%$ and $57\%$ of the reference budget $B^\star_{\mathrm{unif}}(\ell_{\mathrm{crit}})$ (median $10.5\%$). A sharper bound is left open; two routes are a maximal martingale inequality in place of the union bound over steps, and exact binomial tails in place of Bernstein's inequality. The first applies as it stands only at $\eta=\infty$, where the deviation $\hat\ell_k-\ell_k$ is a martingale in $k$; for $\eta<\infty$ the weights $a^{\,k-1-j}$ depend on $k$, and a further argument is needed. The simulation does not prove the theorem and says nothing outside its grid, nor about closed-loop schedules or sampled actions.
\end{remark}

""")

# ------------------------------------ B9 proposition : notation et D12.2
rep(r"non-audited episodes and $\tau_A$ on audited ones", r"non-audited episodes and $\tau_{\mathrm{aud}}$ on audited ones")
rep(r"$\tau_A\ge(\tau-\delta_{\mathrm{ind}})_+$ (the planted-trap bound).",
    r"$\tau_{\mathrm{aud}}\ge(\tau-\delta_{\mathrm{ind}})_+$ (the planted-trap bound of Regime~R3, where $\tau$ and $\tau_{\mathrm{aud}}$ are the rates $\tau_{\mathrm{ord}}$ and $\tau_{\mathrm{trap}}$).")
rep(r"(traps; $\rho$ is then the fraction of planted episodes and $B$ counts them)",
    r"(traps, as in Regime~R3; $\rho$ is then the fraction of planted episodes and $B$ counts them)")
rep(r"At $\eta=\infty$ a stratum with $\tau\le\delta_{\mathrm{ind}}$ has $d_j=(1-\rho_j)\tau\Delta R>0$ whenever $\rho_j<1$, so",
    r"At $\eta=\infty$ the worst stratum with $\tau\le\delta_{\mathrm{ind}}$ allowed by the trap bound ($\tau_{\mathrm{aud}}=0$) has $d_j=(1-\rho_j)\tau\Delta R>0$ whenever $\rho_j<1$, so")
t = t.replace(r"\tau_A", r"\tau_{\mathrm{aud}}")
rep(r"with $C_\delta:=C\,(1-\delta_{\mathrm{ind}}/\tau)_+$", r"with $C_{\mathrm{aud}}^{\delta}:=C\,(1-\delta_{\mathrm{ind}}/\tau)_+$")
rep(r"$(\tau\Delta R,\tau C_\delta)$", r"$(\tau\Delta R,\tau C_{\mathrm{aud}}^{\delta})$")
rep(r"\rho_j(\Delta R+C_\delta)\bigr]$", r"\rho_j(\Delta R+C_{\mathrm{aud}}^{\delta})\bigr]$")
assert r"C_\delta" not in t

# ------------------------------------ B10 remarque « connu et nouveau » (D7-D9)
_b = t.index("% Bibliography entries")
_b = t.rindex("\n", 0, t.rindex("\n", 0, _b)) + 1
assert t[_b:].startswith("% ----"), t[_b:_b+20]
t = t[:_b] + "@@FIN@@"
block("B10", r"\begin{remark}[What is new and what is known]", "@@FIN@@", r"""\begin{remark}[What is new and what is known]\label{rem:audit-related}
The ingredients are classical, and we claim none of them. The allocation of a
limited number of inspections over time is the subject of inspection
games~\cite{avenhaus2002inspection}, going back to Dresher's sequential
game~\cite{dresher1962sampling}, and of security and audit
games~\cite{tambe2011security,blocki2013audit}; in those models the inspectee is
a strategic player who chooses when to violate, whereas in
Theorem~\ref{thm:audit-deterrence} the inspectee is a learning dynamics and the
audit acts on its gradient. The trade-off of
Corollary~\ref{cor:audit-tradeoff}(c) between the probability of inspection and
the size of the penalty is the one of the economics of
enforcement~\cite{becker1968crime}. The linear programs of
Theorem~\ref{thm:audit-deterrence} are a fractional knapsack and a greedy
schedule; Theorem~\ref{thm:audit-detection}(a) is the hypergeometric value of a
hide-and-seek game, which we prove for completeness and do not claim as new;
the question answered by (b), how many of $N$ items to sample without
replacement so as to hit at least one of $k$ corrupted ones with a given
confidence, is that of the size of a statistical audit in post-election
auditing~\cite{rivest2006,aslam2007};
and (c) is the textbook two-point method~\cite{lecam1973convergence,yu1997assouad};
Theorem~\ref{thm:audit-random} is Bernstein's inequality, and finer bounds for
sampling without replacement~\cite{hoeffding1963probability,serfling1974probability}
would apply to a without-replacement implementation. In AI control, audit
budgets covering a small fraction of episodes are central to the protocols
of~\cite{greenblatt2023} and to their game-theoretic
formalisation~\cite{griffin2024}; those works mostly consider deployment, where a
single caught attempt ends the game, which is the regime of
Theorem~\ref{thm:audit-detection}. The closest neighbours of the present setting are low-stakes alignment~\cite{christiano2021lowstakes} and distributed threats, where no single action is catastrophic and the deployment protocol adapts over many episodes~\cite{wen2024}; environment poisoning at training time, which modifies a learner's reward under a budget constraint and is the mirror problem of this one, seen from the attacker~\cite{rakhsha2020poisoning}; and the steering of no-regret learners by a committed leader~\cite{deng2019strategizing}. Two recent preprints are closer still: an audit requirement of the form $p\ge(\text{gain}-\text{cost})/(\text{fine}\times\text{detection})$ and, when the draw can be learned before acting, a floor on the audit probability that does not depend on the sanction~\cite{gans2026randomized}, which we read as the static form of our holding rate and of the floor below $\delta_{\mathrm{ind}}$; and, for audit-based certification of a violation rate, a worst-case bias proportional to the distinguishability of audited episodes that raising the audit rate cannot remove~\cite{zhu2026blindfold}, the closest analogue we know of Proposition~\ref{prop:audit-indist} and of the condition $\delta_{\mathrm{ind}}>0$. We have not searched systematically for inspection games in which the inspectee learns, nor for the steering of learners by payments under a budget, and the next sentence is to be read with that limit. What this section adds, to our knowledge, is
the coupling of the audit schedule with the closed-form log-odds recursion of
KL-regularised natural policy gradient: the exact budgets
\eqref{eq:audit-unif} and \eqref{eq:audit-fin}, the resulting contrast between
a bounded final-criterion budget and a linear uniform-criterion budget, the
double role of the KL anchor (Remark~\ref{rem:audit-criteria}), and the expression in this dynamics of the rare-attack floor already noted for Regime~R3: below $\delta_{\mathrm{ind}}$ the holding rate is $1-c/(\eta\tau\Delta R_{\mathrm f})$ whatever the penalty (Proposition~\ref{prop:audit-indist}); we do not claim the floor itself. All of it is
confined to the two-strata mean-field model.
\end{remark}
""")

# ------------------------------------ B11 bloc bibliographique en commentaire : retiré
t = t.replace("@@FIN@@", "")

# ============================ renommages de notation hors blocs protégés (D3)
# ΔR -> ΔR_f
t = t.replace(r"\Delta R'", "@@DRP@@")
t = re.sub(r"\\Delta R(?![_'A-Za-z])", lambda m: r"\Delta R_{\mathrm f}", t)
t = t.replace("@@DRP@@", r"\Delta R_{\mathrm f}'")
# C (pénalité d'audit) -> C_aud ; C' n'existe plus hors blocs
assert "C'" not in t and r"C_{\mathrm{loop}}" not in t
t, nC = re.subn(r"(?<![A-Za-z\\@])C(?![A-Za-z_'@])", lambda m: r"C_{\mathrm{aud}}", t)
# T (nombre total d'épisodes) -> N
for old, new in [(r"\binom Tk", r"\binom Nk"), (r"\binom TB", r"\binom NB"), (r"\frac Tk", r"\frac Nk"),
                 (r"\tfrac BT", r"\tfrac BN")]:
    assert old in t, old
    t = t.replace(old, new)
t, nT = re.subn(r"(?<![A-Za-z\\@])T(?![A-Za-z@])", "N", t)
print("renommages : C ->", nC, "; T ->", nT)

for k, v in BLOCKS.items():
    assert t.count(k) == 1, k
    t = t.replace(k, v)
assert "@@" not in t
open(out, "w", encoding="utf-8").write(t)
print("écrit", out, len(t.splitlines()), "lignes")
