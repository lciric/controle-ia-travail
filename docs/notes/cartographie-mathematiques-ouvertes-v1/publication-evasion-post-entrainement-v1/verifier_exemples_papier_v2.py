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
