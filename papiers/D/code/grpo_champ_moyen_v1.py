#!/usr/bin/env python3
"""Group-normalised advantages (GRPO-style) with an in-loop filter: mean field vs finite groups.

Tabular three-stratum model (honest h, visible cheat v, stealthy cheat f).  Per sample:
honest reward 0; a cheating sample survives the in-loop monitor with probability beta_i
and then earns dR, otherwise it is intercepted and
  - 'penalty': earns -C and stays in the group statistics;
  - 'mask'   : is removed from the group (statistics over survivors only).
Advantage of a kept sample: (r - mean_group) / std_group (0 if std_group = 0).
Expected natural-gradient direction for stratum i: E[advantage | sample in stratum i] (the
tabular natural gradient of the softmax policy, up to a common additive constant).

Mean-field prediction (G -> infinity), penalty variant: (rbar_i - mu) / sigma with rbar_i the
expected per-sample reward of stratum i and mu, sigma the mean and std of per-sample reward under pi.
Checks the prediction against Monte Carlo for increasing G, and reports how the log-odds rates
f:h and f:v depend on C (standardisation rescales time; it does not change the ranking).

Usage: PYTHONDONTWRITEBYTECODE=1 python3 grpo_champ_moyen_v1.py --out DIR
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

import numpy as np

ROOT_ENTROPY = 20261124


def child_rng(task):
    key = int.from_bytes(hashlib.sha256(task.encode()).digest()[:8], "big")
    return np.random.default_rng(np.random.SeedSequence(ROOT_ENTROPY, spawn_key=(key,)))


def meanfield(pi, beta, dR, C):
    R = np.array([0.0, dR, dR])
    rbar = beta * R - (1 - beta) * C
    second = beta * R ** 2 + (1 - beta) * C ** 2
    mu = pi @ rbar
    sigma = np.sqrt(pi @ second - mu ** 2)
    return (rbar - mu) / sigma, sigma


def monte_carlo(pi, beta, dR, C, G, n_groups, rng, variant="penalty"):
    K = 3
    strata = rng.choice(K, size=(n_groups, G), p=pi)
    surv = rng.random((n_groups, G)) < beta[strata]
    R = np.where(strata == 0, 0.0, dR)
    r = np.where(surv, R, -C)
    keep = np.ones_like(surv) if variant == "penalty" else surv
    cnt = keep.sum(1, keepdims=True)
    mean = np.where(cnt > 0, (r * keep).sum(1, keepdims=True) / np.maximum(cnt, 1), 0.0)
    var = np.where(cnt > 0, ((r - mean) ** 2 * keep).sum(1, keepdims=True) / np.maximum(cnt, 1), 0.0)
    std = np.sqrt(var)
    adv = np.where((std > 0) & keep, (r - mean) / np.where(std > 0, std, 1.0), 0.0)
    out = np.zeros(K)
    for i in range(K):
        mask = strata == i
        out[i] = adv[mask].mean() if mask.any() else np.nan
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(); ap.add_argument("--out", required=True); ap.add_argument("--quick", action="store_true")
    a = ap.parse_args(argv)
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    pi = np.array([0.80, 0.15, 0.05]); dR = 1.0
    res = {"pi": pi.tolist(), "dR": dR, "convergence": [], "rates_vs_C": {}}
    ng = 20000 if a.quick else 200000
    for beta_f in (1.0, 0.75):
        beta = np.array([1.0, 0.1, beta_f])
        for C in (0.0, 1.0, 4.0):
            mf, sig = meanfield(pi, beta, dR, C)
            for G in (4, 16, 64, 256):
                mc = monte_carlo(pi, beta, dR, C, G, max(ng // G, 2000), child_rng(f"mc-{beta_f}-{C}-{G}"))
                res["convergence"].append({"beta_f": beta_f, "C": C, "G": G, "meanfield": mf.tolist(), "mc": mc.tolist(),
                                           "max_abs_err": float(np.nanmax(np.abs(mc - mf)))})
        rows = []
        for C in np.linspace(0, 10, 21):
            mf, sig = meanfield(pi, beta, dR, float(C))
            rows.append({"C": float(C), "sigma": float(sig), "rate_f_over_h": float(mf[2] - mf[0]),
                         "rate_f_over_v": float(mf[2] - mf[1]),
                         "unnormalised_rate_f_over_h": float((mf[2] - mf[0]) * sig),
                         "unnormalised_rate_f_over_v": float((mf[2] - mf[1]) * sig)})
        res["rates_vs_C"][str(beta_f)] = rows
    # mask variant (discard): mean-field over survivors
    beta = np.array([1.0, 0.1, 1.0])
    mc = monte_carlo(pi, beta, dR, 0.0, 256, max(ng // 256, 2000), child_rng("mask"), variant="mask")
    acc = pi * beta / (pi @ beta); R = np.array([0.0, dR, dR])
    mu = acc @ R; sd = np.sqrt(acc @ R ** 2 - mu ** 2)
    res["mask_variant"] = {"mc_given_stratum_including_masked_as_zero": mc.tolist(),
                           "meanfield_survivor_advantage": ((R - mu) / sd).tolist(), "note": "per-stratum mean includes masked samples (advantage 0), so mc_i ~ beta_i*(R_i-mu)/sd"}
    res["mask_variant"]["meanfield_times_beta"] = (beta * (R - mu) / sd).tolist()
    fn = out / "resultats-grpo-champ-moyen-v1.json"
    fn.write_text(json.dumps(res, indent=1) + "\n")
    Path(str(fn) + ".sha256").write_text(f"{hashlib.sha256(fn.read_bytes()).hexdigest()}  {fn.name}\n")
    for row in res["convergence"]:
        print(row["beta_f"], row["C"], row["G"], round(row["max_abs_err"], 4))
    for k, rows in res["rates_vs_C"].items():
        print("beta_f", k, [(r["C"], round(r["rate_f_over_h"], 3), round(r["rate_f_over_v"], 3), round(r["sigma"], 3)) for r in rows[::4]])
    print(res["mask_variant"])


if __name__ == "__main__":
    main()
