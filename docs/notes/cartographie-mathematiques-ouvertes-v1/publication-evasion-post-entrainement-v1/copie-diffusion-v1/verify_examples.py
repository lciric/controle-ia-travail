#!/usr/bin/env python3
"""
Standalone verifier for the examples and tables of the publication package on
in-loop misalignment filtering and stealth (v4, corrective 1, after the independent audit and two fidelity reviews).

What this script does, and does not, establish (read before citing it):
  - The theorems are carried by the written proofs. This script only
    (a) recomputes every table and numerical example of the manuscript, the post
    and the comment, (b) runs regression checks of the stated criteria, and
    (c) checks the counterexamples and corrected statements added in v3.
  - Exact rational arithmetic (`fractions.Fraction`) is used for: the variance
    identity example; the Operator A criteria with E := exp(eta * Delta R)
    treated as a free positive rational; the decoupling counterexamples; the
    perfect-stealth niche identities; the collapse limit of the stealth share.
    Everything else uses double-precision floats.
  - The floating-point regression families are described honestly in the
    output ("what_is_tested"): the R2 family covers only an exactly
    counter-monotone pairing (a special case of negative association), and the
    R3 family evaluates the extremal policy, for which the bound is tight by
    construction (it recomputes the inequality that defines C*). A count of
    "zero violations" in these families is not evidence beyond the proofs.

Usage:
  python3 -I verify_examples.py            # print JSON to stdout only
  python3 -I verify_examples.py --out PATH # also write PATH (refuses
                                                        # to overwrite an existing file)
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
        "status": "regression checks only; the proofs carry the results",
        "families": [
            {
                "name": "theorem_1_float",
                "draws": 10_000,
                "violations": violations_t1,
                "what_is_tested": (
                    "direction of conditional enrichment under A and B (two strata, equal reward); "
                    "amplification criterion under A and under B; dominance criterion under B; "
                    "each compared with direct Gibbs computation in floats. "
                    "Not tested here: dominance threshold under A, the barrier under A, the "
                    "limiting-case proposition (see exact_checks). Narrow domain: beta_f >= 0.20, "
                    "beta_h >= 0.55, eta <= 8, no draw with beta_f == beta_h."
                ),
            },
            {
                "name": "perfect_niche_float",
                "draws": 2_000,
                "violations": violations_niche,
                "what_is_tested": "pi_A(f) > pi_no(f) and the inversion criterion; priors fixed at (0.70, 0.25, 0.05).",
            },
            {
                "name": "regime_r2_float",
                "draws": 1_000,
                "violations": violations_r2,
                "what_is_tested": (
                    "SPECIAL CASE ONLY: audit survival is the exactly counter-monotone rearrangement of "
                    "loop survival (a case of negative association), four equiprobable atoms; the sign "
                    "then follows from Chebyshev's sum inequality. Neither the covariance identity, nor "
                    "independence, nor 'non-positive covariance without negative association' is tested."
                ),
            },
            {
                "name": "regime_r3_float",
                "draws": 1_000,
                "violations": violations_r3,
                "what_is_tested": (
                    "TAUTOLOGICAL: one extremal policy 1{P_ord >= P_trap} per draw, for which the gap equals "
                    "the total variation exactly; the threshold uses tau_min = tau_ord of that same policy, so "
                    "the check recomputes the inequality defining C*. Ordinary-episode monitor always blind."
                ),
            },
        ],
    }


def _a_weights(p, beta, e):
    """Unnormalized Operator A weights with E = exp(eta * Delta R) as a free value."""
    return (beta[0] * p[0], beta[1] * p[1] * e, beta[2] * p[2] * e)


def exact_checks() -> dict[str, Any]:
    """Exact (Fraction) checks of the statements corrected or added in v3."""
    F = fractions.Fraction
    out: dict[str, Any] = {}

    # (1) Off-loop placement is not sufficient: positively correlated audit, under A.
    loop, audit = [F(1, 10), F(9, 10)], [F(2, 10), F(8, 10)]
    before = sum(audit) / 2
    after = sum(l * a for l, a in zip(loop, audit)) / sum(loop)
    cov = sum(l * a for l, a in zip(loop, audit)) / 2 - (sum(loop) / 2) * before
    assert after - before == cov / (sum(loop) / 2) and after > before
    out["decoupling_off_loop_counterexample_A"] = {
        "beta_loop": ["1/10", "9/10"], "beta_audit": ["2/10", "8/10"],
        "audit_survival_before": str(before), "audit_survival_after": str(after),
        "shift": str(after - before), "cov_over_mean": str(cov / (sum(loop) / 2)),
    }

    # (2) Off-loop placement is not necessary: audit inside the loop, combined with another detector.
    b_audit, b_other = [F(1, 2), F(1)], [F(1), F(1, 10)]
    b_loop = [x * y for x, y in zip(b_audit, b_other)]
    before2 = sum(b_audit) / 2
    after2 = sum(l * a for l, a in zip(b_loop, b_audit)) / sum(b_loop)
    assert after2 < before2
    out["decoupling_in_loop_counterexample_A"] = {
        "audit_survival_before": str(before2), "audit_survival_after": str(after2),
    }

    # (3) Under B, zero covariance is not sufficient (convexity of exp(k u)).
    l3, a3 = [F(1, 10), F(1, 2), F(9, 10)], [F(9, 10), F(1, 10), F(9, 10)]
    m_l, m_a = sum(l3) / 3, sum(a3) / 3
    cov3 = sum(x * y for x, y in zip(l3, a3)) / 3 - m_l * m_a
    assert cov3 == 0
    k = 4.0
    w = [math.exp(k * float(x)) for x in l3]
    after3 = sum(wi * float(ai) for wi, ai in zip(w, a3)) / sum(w)
    assert after3 > float(m_a) + 0.1
    out["decoupling_zero_cov_counterexample_B"] = {
        "cov_exact": str(cov3), "k": k, "audit_survival_before": str(m_a),
        "audit_survival_after_float": round(after3, 6),
    }

    # (3b) Under B, a positive covariance need not make audit survival rise at high pressure.
    l3b, a3b = [F(1, 10), F(1, 2), F(9, 10)], [F(1, 10), F(19, 20), F(9, 20)]
    cov3b = sum(x * y for x, y in zip(l3b, a3b)) / 3 - (sum(l3b) / 3) * (sum(a3b) / 3)
    assert cov3b == F(7, 150) and sum(a3b) / 3 == F(1, 2)
    surv3b = {}
    for kk in (2.0, 10.0, 50.0):
        w = [math.exp(kk * float(x)) for x in l3b]
        surv3b[kk] = sum(wi * float(ai) for wi, ai in zip(w, a3b)) / sum(w)
    assert surv3b[2.0] > 0.5 and surv3b[10.0] < 0.5 and abs(surv3b[50.0] - 0.45) < 1e-6
    out["positive_cov_not_sufficient_B"] = {
        "beta_loop": ["1/10", "1/2", "9/10"], "beta_audit": ["1/10", "19/20", "9/20"],
        "cov_exact": str(cov3b), "audit_survival_before": "1/2",
        "audit_survival_after_float": {str(k): round(v, 6) for k, v in surv3b.items()},
        "limit": "9/20",
    }

    # (4) Perfect-stealth niche: equal f:h odds under A and B; B > A on stealth iff B > A on honesty.
    rng = random.Random(20261124)
    n_niche = 0
    for _ in range(2_000):
        p = [F(rng.randint(1, 50)) for _ in range(3)]
        s = sum(p)
        p = [x / s for x in p]
        bv = F(rng.randint(1, 99), 100)
        e = F(rng.randint(101, 5000), 100)          # E = exp(eta * Delta R) > 1
        q = F(rng.randint(1, 999), 1000)            # q = exp(-eta (1 - bv)(Delta R + C)) in (0, 1)
        wa = (p[0], bv * p[1] * e, p[2] * e)
        wb = (p[0], p[1] * e * q, p[2] * e)
        za, zb = sum(wa), sum(wb)
        assert (wa[2] / wa[0]) == (wb[2] / wb[0])
        b_f_more = wb[2] / zb > wa[2] / za
        b_h_more = wb[0] / zb > wa[0] / za
        assert b_f_more == b_h_more == (q < bv)
        if b_f_more:
            assert (wb[1] + wb[2]) / zb < (wa[1] + wa[2]) / za
        n_niche += 1
    out["niche_equal_odds_exact"] = {
        "draws": n_niche,
        "claim": "f:h odds identical under A and B; pi_B(f) > pi_A(f) iff pi_B(h) > pi_A(h) iff q < beta_v; "
                 "total cheating then lower under B",
    }

    # (5) Collapse of pure rejection is to cheating, not necessarily to stealth.
    p5, b5 = (F(49, 100), F(1, 2), F(1, 100)), (F(1), F(1, 2), F(3, 5))
    share_lim = b5[2] * p5[2] / (b5[1] * p5[1] + b5[2] * p5[2])
    assert share_lim == F(3, 128)
    big = F(10) ** 12
    wa = _a_weights(p5, b5, big)
    assert abs(wa[2] / (wa[1] + wa[2]) - share_lim) == 0  # exact: share does not depend on E
    # Operator A = unmonitored Gibbs law reweighted by beta; equal-reward share constant in E.
    for e in (F(1, 3), F(1), F(7), F(10) ** 6):
        wa = _a_weights(p5, b5, e)
        wn = (p5[0], p5[1] * e, p5[2] * e)
        zn = sum(wn)
        reweighted = [b * w / zn for b, w in zip(b5, wn)]
        zr = sum(reweighted)
        assert all(x / sum(wa) == y / zr for x, y in zip(wa, reweighted))
        assert wa[2] / (wa[1] + wa[2]) == share_lim
    out["operator_A_equals_reweighted_unmonitored"] = {
        "E_values": ["1/3", "1", "7", "10^6"],
        "claim": "pi_A is proportional to beta * pi_no (single rejection at inference); with equal rewards the "
                 "stealth share among cheaters equals beta_f p_f / (beta_v p_v + beta_f p_f) for every E",
        "checked_exactly": True,
    }
    out["collapse_limit_stealth_share_A"] = {
        "priors": ["49/100", "1/2", "1/100"], "betas": ["1", "1/2", "3/5"],
        "limit_stealth_share_among_cheaters": str(share_lim),
        "limit_visible_share_among_cheaters": str(1 - share_lim),
    }

    # (6) Operator A criteria in exact arithmetic (E free positive rational), incl. beta_f == beta_h.
    rng6 = random.Random(271828)
    n_amp = n_dom = 0
    for i in range(5_000):
        p = [F(rng6.randint(1, 200)) for _ in range(3)]
        s = sum(p)
        p = [x / s for x in p]
        bh = F(rng6.randint(1, 100), 100)
        bf = bh if i % 5 == 0 else F(rng6.randint(1, int(bh * 100)), 100)
        if bf == 0:
            bf = F(1, 100)
        bv = F(rng6.randint(0, max(0, int(bf * 100) - 1)), 100)
        if bv >= bf:
            continue
        e = F(rng6.randint(1, 10_000), 100)
        wa = _a_weights(p, (bh, bv, bf), e)
        wn = (p[0], p[1] * e, p[2] * e)
        amp = wa[2] / sum(wa) > wn[2] / sum(wn)
        crit_amp = (bf - bv) * p[1] * e > (bh - bf) * p[0]
        assert amp == crit_amp
        dom = wa[2] > wa[0]
        crit_dom = e * bf * p[2] > bh * p[0]          # exponentiated form of the A dominance threshold
        assert dom == crit_dom
        n_amp += 1
        n_dom += 1
    out["operator_A_exact"] = {"amplification_draws": n_amp, "dominance_draws": n_dom,
                               "note": "E := exp(eta*DeltaR) treated as a free positive rational; 20% of draws have beta_f == beta_h"}

    # (7) Repeated rejection (T rounds of filter + KL step eta_1): barrier does not vanish.
    p_h, p_f, b_h, b_f = 0.85, 0.01, 1.0, 0.75
    eta1, dr, T = 0.2, 1.0, 1000
    logodds_paper = math.log(b_f * p_f / (b_h * p_h)) + (T * eta1) * dr
    logodds_rep = math.log(p_f / p_h) + T * (eta1 * dr - math.log(b_h / b_f))
    # direct iteration check on log weights
    lw_h, lw_f = math.log(p_h), math.log(p_f)
    for _ in range(T):
        lw_h += math.log(b_h)
        lw_f += math.log(b_f) + eta1 * dr
    assert abs((lw_f - lw_h) - logodds_rep) < 1e-8
    out["repeated_rejection_sensitivity"] = {
        "params": {"p_h": p_h, "p_f": p_f, "beta_h": b_h, "beta_f": b_f, "eta_1": eta1, "delta_r": dr, "T": T},
        "total_eta": T * eta1,
        "logodds_f_over_h_paper_operator_A": round(logodds_paper, 3),
        "logodds_f_over_h_repeated_rejection": round(logodds_rep, 3),
        "limit_criterion": "as T -> inf, stealth beats honesty iff eta_1 * DeltaR > log(beta_h / beta_f)",
    }

    # (8) Under B with heterogeneous rewards among cheaters, mean cheater survival can drop.
    betas, rewards, c, eta = (0.5, 0.9), (0.01, 10.0), 0.0, 0.3
    before8 = sum(math.exp(eta * r) * b for r, b in zip(rewards, betas)) / sum(math.exp(eta * r) for r in rewards)
    wts = [math.exp(eta * (b * r - (1 - b) * c)) for r, b in zip(rewards, betas)]
    after8 = sum(wi * b for wi, b in zip(wts, betas)) / sum(wts)
    assert after8 < before8
    out["heterogeneous_reward_B_counterexample"] = {
        "mean_cheater_survival_unmonitored": round(before8, 4), "under_B": round(after8, 4),
    }
    return out


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
    args = sys.argv[1:]
    out_path = None
    if args:
        if len(args) != 2 or args[0] != "--out":
            raise SystemExit("usage: verify_examples.py [--out PATH]")
        out_path = pathlib.Path(args[1]).resolve()
        if out_path.exists():
            raise SystemExit(f"refusing to overwrite existing file: {out_path}")
    rational = verify_exact_rational_identity()
    mc = run_monte_carlo_suite()
    exact = exact_checks()
    tables = compute_paper_tables()
    out = {
        "script": "verify_examples.py",
        "exact_rational_variance_identity": rational,
        "exact_checks": exact,
        "float_regression_checks": mc,
        "verified_examples": tables,
    }
    text = json.dumps(out, indent=2) + "\n"
    if out_path is not None:
        out_path.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
