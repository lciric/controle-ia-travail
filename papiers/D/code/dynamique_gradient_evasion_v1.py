#!/usr/bin/env python3
"""Finite-time learning dynamics of in-loop misalignment filtering (companion code).

Standalone, CPU-only, deterministic.  Reproduces every number and figure of the
finite-time dynamics section:

  1. Tabular softmax, natural policy gradient (NPG) on the KL-regularised
     objective: the trajectory is exactly the static Gibbs family at effective
     pressure eta*(1 - exp(-t/eta)); closed-form hitting times are checked
     against numerical integration.
  2. "Discard and try again" is not one operator: iterated rejection
     fine-tuning (distribution matching on accepted samples; the filter
     compounds) versus discard policy gradient (advantage-based learning on
     accepted samples; the filter only rescales time).
  3. Two-channel factorised model (action channel x chain-of-thought channel):
     cooperative planar flow, equilibria, saddle, basins, order-interval
     certificate, phase diagram over (penalty C, pressure eta).
  4. Finite-batch REINFORCE on the two-channel model: noise-activated escape
     from the honest basin.

Usage:  PYTHONDONTWRITEBYTECODE=1 python3 dynamique_gradient_evasion_v1.py --out DIR [--quick]
Writes DIR/resultats-dynamique-v1.json (+ .sha256) and figures (PDF and SVG).
Seeds: numpy.random.SeedSequence, root entropy fixed below, one child per task.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
import subprocess
import sys
from pathlib import Path

import numpy as np

ROOT_ENTROPY = 20261124
VERSION = "v1"


class GuardError(RuntimeError):
    """Raised by a guard; never silently bypassed."""


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------
def sigmoid(x):
    x = np.asarray(x, dtype=float)
    return np.where(x >= 0, 1.0 / (1.0 + np.exp(-np.abs(x))), np.exp(-np.abs(x)) / (1.0 + np.exp(-np.abs(x))))


def logit(p):
    p = np.asarray(p, dtype=float)
    if np.any((p <= 0) | (p >= 1)):
        raise GuardError(f"logit outside (0,1): {p}")
    return np.log(p) - np.log1p(-p)


def softmax(theta):
    z = np.asarray(theta, dtype=float)
    z = z - z.max(axis=-1, keepdims=True)
    e = np.exp(z)
    return e / e.sum(axis=-1, keepdims=True)


def child_rng(task: str) -> np.random.Generator:
    key = int.from_bytes(hashlib.sha256(task.encode()).digest()[:8], "big")
    return np.random.default_rng(np.random.SeedSequence(ROOT_ENTROPY, spawn_key=(key,)))


def check_probability_vector(pi, name="pi"):
    pi = np.asarray(pi, dtype=float)
    if not np.all(np.isfinite(pi)) or np.any(pi < -1e-15) or abs(pi.sum(axis=-1) - 1).max() > 1e-9:
        raise GuardError(f"{name} is not a probability vector: {pi}")
    return pi


# ---------------------------------------------------------------------------
# 1. tabular NPG: exact time-slice property
# ---------------------------------------------------------------------------
STRATA = ("h", "v", "f")


def effective_rewards(op, dR, beta, C=0.0, eta=1.0):
    """Effective reward vector over strata (h, v, f) for an operator.

    op: 'none' -> R ; 'A' -> R + log(beta)/eta (static pure rejection) ;
        'B' -> beta R - (1 - beta) C.
    """
    R = np.array([0.0, dR, dR])
    b = np.asarray(beta, dtype=float)
    if op == "none":
        return R
    if op == "A":
        if np.any(b <= 0):
            raise GuardError("operator A effective reward needs beta > 0 on every stratum kept")
        return R + np.log(b) / eta
    if op == "B":
        return b * R - (1 - b) * C
    raise GuardError(f"unknown operator {op}")


def npg_closed_form(p, r, eta, t):
    lam = 1.0 - np.exp(-np.asarray(t, dtype=float) / eta)
    logits = np.log(p)[None, :] + np.outer(np.atleast_1d(lam), eta * r)
    return softmax(logits)


def npg_integrate(p, r, eta, T, dt):
    """RK4 on the logit ODE  d theta/dt = r - (theta - log p)/eta."""
    th = np.log(p).astype(float).copy()
    f = lambda x: r - (x - np.log(p)) / eta
    n = int(round(T / dt))
    for _ in range(n):
        k1 = f(th); k2 = f(th + dt / 2 * k1); k3 = f(th + dt / 2 * k2); k4 = f(th + dt * k3)
        th = th + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return softmax(th)


def npg_vanilla_pg_integrate(p, r, eta, T, dt):
    """Euclidean softmax policy gradient on the same objective (same fixed point, different path)."""
    th = np.log(p).astype(float).copy()
    n = int(round(T / dt))
    for _ in range(n):
        pi = softmax(th)
        a = r - np.log(pi / p) / eta
        g = pi * (a - pi @ a)
        th = th + dt * g
    return softmax(th)


def dominance_time(p_num, p_den, r_num, r_den, eta):
    """First t with log-odds(num:den) > 0 along the NPG path; inf if never."""
    L = np.log(p_den / p_num)
    d = r_num - r_den
    if L <= 0:
        return 0.0
    if d <= 0 or eta * d <= L:
        return float("inf")
    return float(-eta * np.log(1.0 - L / (eta * d)))


def discrete_npg_lambda(k, gamma, eta):
    return 1.0 - (1.0 - gamma / eta) ** np.asarray(k, dtype=float)


# ---------------------------------------------------------------------------
# 2. discard-and-retry: rejection fine-tuning vs discard policy gradient
# ---------------------------------------------------------------------------
def rft_rounds(p, beta, R, w, K):
    """pi_{k+1} proportional to pi_k * beta * w(R) (exact distribution matching)."""
    out = [np.asarray(p, float)]
    for _ in range(K):
        x = out[-1] * beta * w(R)
        out.append(x / x.sum())
    return np.array(out)


def rft_dominance_round(p_f, p_h, beta_f, beta_h, w_ratio):
    slope = np.log(w_ratio) - np.log(beta_h / beta_f)
    L = np.log(p_h / p_f)
    if L <= 0:
        return 0
    if slope <= 0:
        return None
    return int(np.floor(L / slope) + 1)


def discard_pg_field(theta, beta, R, p=None, eta=None):
    pi = softmax(theta)
    Z = pi @ beta
    b = (pi * beta) @ R / Z
    a = beta * (R - b) / Z
    if eta is not None:
        a = a - (theta - np.log(p)) / eta
    return a


def discard_pg_integrate(p, beta, R, T, dt, eta=None, record=None):
    th = np.log(p).astype(float).copy()
    traj = []
    n = int(round(T / dt))
    for i in range(n + 1):
        if record is not None and i % record == 0:
            traj.append((i * dt, softmax(th)))
        if i == n:
            break
        f = lambda x: discard_pg_field(x, beta, R, p, eta)
        k1 = f(th); k2 = f(th + dt / 2 * k1); k3 = f(th + dt / 2 * k2); k4 = f(th + dt * k3)
        th = th + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return softmax(th), traj


def discard_pg_stochastic(p, beta, R, n_acc, steps, lr, rng):
    """Finite-batch REINFORCE on accepted samples (natural-gradient scaling per stratum)."""
    th = np.log(p).astype(float).copy()
    K = len(p)
    hist = np.empty((steps + 1, K))
    for s in range(steps + 1):
        pi = softmax(th)
        hist[s] = pi
        if s == steps:
            break
        acc = np.zeros(K)
        need = n_acc
        while need > 0:
            draw = rng.choice(K, size=4 * need, p=pi)
            keep = draw[rng.random(draw.size) < beta[draw]][:need]
            np.add.at(acc, keep, 1)
            need -= keep.size
        freq = acc / n_acc
        bhat = freq @ R
        g = freq * (R - bhat) - pi * (freq @ (R - bhat))  # vanilla softmax REINFORCE estimate
        nat = np.where(pi > 1e-300, g / np.maximum(pi, 1e-300), 0.0)
        nat -= pi @ nat
        th = th + lr * nat
    return hist


# ---------------------------------------------------------------------------
# 3. two-channel factorised model
# ---------------------------------------------------------------------------
def two_channel_coeffs(par, op="B"):
    bv, bf, dR, C, eta = par["bv"], par["bf"], par["dR"], par["C"], par["eta"]
    if op == "B":
        A0 = bv * dR - (1 - bv) * C
        D = (bf - bv) * (dR + C)
    elif op == "A":
        if bv <= 0:
            raise GuardError("operator A in the two-channel model needs beta_v > 0")
        A0 = dR + np.log(bv) / eta
        D = np.log(bf / bv) / eta
    else:
        raise GuardError(op)
    return A0, D


def two_channel_field(u, w, par, op="B", geometry="natural"):
    A0, D = two_channel_coeffs(par, op)
    eta, k = par["eta"], par["kappa"]
    gu = A0 + D * sigmoid(w) - (u - par["u0"]) / eta
    gw = D * sigmoid(u) - k - (w - par["w0"]) / eta
    if geometry == "vanilla":
        q, s = sigmoid(u), sigmoid(w)
        return q * (1 - q) * gu, s * (1 - s) * gw
    return gu, gw


def two_channel_J(q, s, par, op="B"):
    A0, D = two_channel_coeffs(par, op)
    q0, s0 = sigmoid(par["u0"]), sigmoid(par["w0"])
    kl = lambda a, a0: a * np.log(a / a0) + (1 - a) * np.log((1 - a) / (1 - a0))
    return q * (A0 + D * s) - par["kappa"] * s - (kl(q, q0) + kl(s, s0)) / par["eta"]


def two_channel_equilibria(par, op="B", grid=400001):
    """Fixed points of F(w) = w0 + eta(D sigma(u0 + eta(A0 + D sigma(w))) - kappa)."""
    from scipy.optimize import brentq
    A0, D = two_channel_coeffs(par, op)
    eta, k, u0, w0 = par["eta"], par["kappa"], par["u0"], par["w0"]
    U = lambda w: u0 + eta * (A0 + D * sigmoid(w))
    G = lambda w: w0 + eta * (D * sigmoid(U(w)) - k) - w
    lo, hi = w0 - eta * k - 1.0, w0 + eta * (D - k) + 1.0  # all fixed points lie inside
    ws = np.linspace(lo, hi, grid)
    g = G(ws)
    roots = []
    for i in np.where(np.sign(g[:-1]) != np.sign(g[1:]))[0]:
        roots.append(brentq(G, ws[i], ws[i + 1], xtol=1e-13))
    for i in np.where(g == 0)[0]:
        roots.append(ws[i])
    roots = sorted(set(np.round(roots, 11)))
    eqs = []
    for w in roots:
        u = float(U(w))
        q, s = float(sigmoid(u)), float(sigmoid(w))
        det = 1 / eta ** 2 - D ** 2 * q * (1 - q) * s * (1 - s)
        eqs.append({"u": u, "w": float(w), "q": q, "s": s, "det": det,
                    "type": "stable" if det > 0 else ("saddle" if det < 0 else "degenerate"),
                    "J": float(two_channel_J(q, s, par, op)) if 0 < q < 1 and 0 < s < 1 else float("nan")})
    return eqs


def two_channel_flow(u, w, par, T, dt, op="B", geometry="natural", record=0):
    u = np.array(u, dtype=float); w = np.array(w, dtype=float)
    traj = []
    n = int(round(T / dt))
    for i in range(n):
        if record and i % record == 0:
            traj.append((i * dt, np.copy(u), np.copy(w)))
        f = lambda a, b: two_channel_field(a, b, par, op, geometry)
        k1 = f(u, w); k2 = f(u + dt / 2 * k1[0], w + dt / 2 * k1[1])
        k3 = f(u + dt / 2 * k2[0], w + dt / 2 * k2[1]); k4 = f(u + dt * k3[0], w + dt * k3[1])
        u = u + dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
        w = w + dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
    if record:
        traj.append((n * dt, np.copy(u), np.copy(w)))
    return u, w, traj


def order_interval_certificate(par, op="B"):
    """Corollary certificate: wbar = w0, ubar = max(u0, u0 + eta(A0 + D s0)); holds iff D sigma(ubar) <= kappa."""
    A0, D = two_channel_coeffs(par, op)
    s0 = sigmoid(par["w0"])
    ubar = max(par["u0"], par["u0"] + par["eta"] * (A0 + D * s0))
    return bool(D * sigmoid(ubar) <= par["kappa"]), float(ubar)


def penalty_window(par):
    """C_low <= C <= C_high for the base-model certificate (A0 + D s0 <= 0 and q0 D <= kappa)."""
    bv, bf, dR, k = par["bv"], par["bf"], par["dR"], par["kappa"]
    q0, s0 = sigmoid(par["u0"]), sigmoid(par["w0"])
    b0 = bv + s0 * (bf - bv)
    c_low = b0 * dR / (1 - b0) if b0 < 1 else float("inf")
    c_high = k / (q0 * (bf - bv)) - dR
    return float(c_low), float(c_high)


def two_channel_stochastic(par, n_batch, steps, lr, rng, op="B"):
    """Finite-batch REINFORCE (vanilla logit gradient) on the two-channel model.

    Per sample: a ~ Bern(q) (hack), c ~ Bern(s) (obfuscated CoT); a hack survives
    the CoT monitor w.p. beta_v (transparent) or beta_f (obfuscated); honest
    samples always survive.  Score = survive*dR*a - (1-survive)*C - kappa*c.
    Leave-one-out baseline (unbiased gradient); KL gradient is exact.  Returns final (q, s).
    """
    if op != "B":
        raise GuardError("stochastic simulation implemented for operator B only")
    u, w = float(par["u0"]), float(par["w0"])
    bv, bf, dR, C, k, eta = par["bv"], par["bf"], par["dR"], par["C"], par["kappa"], par["eta"]
    q0, s0 = sigmoid(par["u0"]), sigmoid(par["w0"])
    for _ in range(steps):
        q, s = float(sigmoid(u)), float(sigmoid(w))
        a = rng.random(n_batch) < q
        c = rng.random(n_batch) < s
        surv_p = np.where(a, np.where(c, bf, bv), 1.0)
        surv = rng.random(n_batch) < surv_p
        score = np.where(surv, dR * a, -C) - k * c
        if n_batch < 2:
            raise GuardError("leave-one-out baseline needs n_batch >= 2")
        adv = (score - score.mean()) * n_batch / (n_batch - 1)  # leave-one-out baseline: unbiased
        gu = np.mean(adv * (a - q))
        gw = np.mean(adv * (c - s))
        # exact gradient of -KL/eta wrt logits
        gu -= q * (1 - q) * (np.log(q / q0) - np.log((1 - q) / (1 - q0))) / eta
        gw -= s * (1 - s) * (np.log(s / s0) - np.log((1 - s) / (1 - s0))) / eta
        u += lr * gu
        w += lr * gw
        u = float(np.clip(u, -40, 40)); w = float(np.clip(w, -40, 40))
    return float(sigmoid(u)), float(sigmoid(w))


# ---------------------------------------------------------------------------
# experiments
# ---------------------------------------------------------------------------
BASE_TAB = dict(p=[0.85, 0.14, 0.01], beta=[1.0, 0.05, 0.75], dR=1.0, C=2.5, eta=3.0)
BASE_2CH = dict(bv=0.1, bf=1.0, dR=1.0, C=2.0, eta=8.0, kappa=0.05,
                u0=float(np.log(0.05 / 0.95)), w0=float(np.log(0.02 / 0.98)))


def experiment_tabular(quick):
    p = np.array(BASE_TAB["p"]); beta = np.array(BASE_TAB["beta"]); dR, C, eta = BASE_TAB["dR"], BASE_TAB["C"], BASE_TAB["eta"]
    out = {"params": BASE_TAB, "checks": []}
    worst = 0.0
    for op in ("none", "A", "B"):
        r = effective_rewards(op, dR, beta, C, eta)
        for T in (0.5, 2.0, 7.0, 30.0):
            exact = npg_closed_form(p, r, eta, T)[0]
            num = npg_integrate(p, r, eta, T, 1e-3)
            err = float(np.max(np.abs(exact - num)))
            worst = max(worst, err)
            out["checks"].append({"op": op, "t": T, "pi_exact": exact.tolist(), "max_abs_err_rk4": err})
        stat = softmax(np.log(p) + eta * r)
        out[f"fixed_point_{op}"] = stat.tolist()
        van = npg_vanilla_pg_integrate(p, r, eta, 400.0 if not quick else 200.0, 1e-2)
        out[f"vanilla_pg_endpoint_{op}"] = van.tolist()
        out[f"vanilla_pg_vs_gibbs_err_{op}"] = float(np.max(np.abs(van - stat)))
    out["max_abs_err_closed_form_vs_rk4"] = worst
    rA = effective_rewards("A", dR, beta, C, eta); rB = effective_rewards("B", dR, beta, C, eta)
    out["hitting_times"] = {
        "dominance_f_over_h_A": dominance_time(p[2], p[0], rA[2], rA[0], eta),
        "dominance_f_over_h_B": dominance_time(p[2], p[0], rB[2], rB[0], eta),
    }
    # hitting-time check by dense time grid
    ts = np.linspace(0, 60, 600001)
    for op, r in (("A", rA), ("B", rB)):
        pis = npg_closed_form(p, r, eta, ts)
        idx = np.where(pis[:, 2] > pis[:, 0])[0]
        out["hitting_times"][f"grid_first_dominance_{op}"] = float(ts[idx[0]]) if idx.size else float("inf")
    # same quantities at larger eta, where dominance happens in finite time under A
    eta2 = 8.0
    rA2 = effective_rewards("A", dR, beta, C, eta2); rB2 = effective_rewards("B", dR, beta, C, eta2)
    tA2 = dominance_time(p[2], p[0], rA2[2], rA2[0], eta2)
    pis = npg_closed_form(p, rA2, eta2, ts)
    idx = np.where(pis[:, 2] > pis[:, 0])[0]
    out["hitting_times_eta8"] = {"dominance_f_over_h_A": tA2,
                                 "grid_first_dominance_A": float(ts[idx[0]]) if idx.size else float("inf"),
                                 "dominance_f_over_h_B": dominance_time(p[2], p[0], rB2[2], rB2[0], eta2)}
    # discrete NPG
    gamma = 0.5
    k = np.arange(0, 41)
    th = np.log(p).copy(); errs = []
    for kk in k:
        lam = discrete_npg_lambda(kk, gamma, eta)
        exact = softmax(np.log(p) + lam * eta * rA2 * 0 + lam * eta * effective_rewards("A", dR, beta, C, eta))
        errs.append(float(np.max(np.abs(exact - softmax(th)))))
        th = th + gamma * (effective_rewards("A", dR, beta, C, eta) - (th - np.log(p)) / eta)
    out["discrete_npg_max_err"] = max(errs)
    return out


def experiment_discard(quick):
    p = np.array(BASE_TAB["p"]); R = np.array([0.0, 1.0, 1.0])
    res = {}
    # RFT with w = exp(gamma R): compounding filter
    beta = np.array([1.0, 0.05, 0.75])
    for gamma in (0.2, 0.5):
        w = lambda r, g=gamma: np.exp(g * r)
        traj = rft_rounds(p, beta, R, w, 60)
        lo = np.log(traj[:, 2] / traj[:, 0])
        pred = np.log(p[2] / p[0]) + np.arange(61) * (gamma - np.log(beta[0] / beta[2]))
        k_star = rft_dominance_round(p[2], p[0], beta[2], beta[0], np.exp(gamma))
        emp = np.where(traj[:, 2] > traj[:, 0])[0]
        res[f"rft_gamma_{gamma}"] = {"slope_pred": float(gamma - np.log(beta[0] / beta[2])),
                                     "max_err_logodds": float(np.max(np.abs(lo - pred))),
                                     "dominance_round_pred": k_star,
                                     "dominance_round_emp": int(emp[0]) if emp.size else None,
                                     "pi_f_round_60": float(traj[60, 2]), "pi_h_round_60": float(traj[60, 0])}
    # discard policy gradient (mean field, no KL): stealth always wins
    pi_end, traj = discard_pg_integrate(p, beta, R, 40.0, 1e-3, record=100)
    tt = np.array([t for t, _ in traj]); pp = np.array([x for _, x in traj])
    lo = np.log(pp[:, 2] / pp[:, 0])
    bound = np.log(p[2] / p[0]) + beta[2] * R[2] * tt
    emp = np.where(pp[:, 2] > pp[:, 0])[0]
    res["discard_pg_meanfield"] = {"min_logodds_minus_bound": float(np.min(lo - bound)),
                                   "dominance_time_bound": float(np.log(p[0] / p[2]) / (beta[2] * R[2])),
                                   "dominance_time_emp": float(tt[emp[0]]) if emp.size else None,
                                   "pi_end": pi_end.tolist()}
    # same monitor, gamma=0.2: RFT never lets stealth dominate while discard-PG does
    rng = child_rng("discard_pg_stochastic")
    hist = discard_pg_stochastic(p, beta, R, n_acc=256, steps=400 if not quick else 150, lr=0.1, rng=rng)
    res["discard_pg_stochastic_final"] = hist[-1].tolist()
    res["_traj_rft"] = {str(g): rft_rounds(p, beta, R, (lambda r, g=g: np.exp(g * r)), 60).tolist() for g in (0.2, 0.5)}
    res["_traj_pg"] = {"t": tt.tolist(), "pi": pp.tolist()}
    res["_traj_pg_stoch"] = hist.tolist()
    return res


def experiment_two_channel(quick):
    par = dict(BASE_2CH)
    res = {"params": par}
    eqs = two_channel_equilibria(par)
    res["equilibria"] = eqs
    u, w, traj = two_channel_flow(par["u0"], par["w0"], par, T=300.0, dt=0.01, record=50)
    res["flow_from_pi0"] = {"q": float(sigmoid(u)), "s": float(sigmoid(w))}
    res["certificate"] = order_interval_certificate(par)
    res["penalty_window"] = penalty_window(par)
    # lyapunov monotonicity along the trajectory
    Js = [float(two_channel_J(sigmoid(a), sigmoid(b), par)) for _, a, b in traj]
    res["lyapunov_min_increment"] = float(np.min(np.diff(Js)))
    res["_traj_pi0"] = [(t, float(a), float(b)) for t, a, b in traj]
    # vanilla geometry: same equilibria, check endpoint
    uv, wv, _ = two_channel_flow(par["u0"], par["w0"], par, T=3000.0, dt=0.05, geometry="vanilla")
    res["vanilla_flow_from_pi0"] = {"q": float(sigmoid(uv)), "s": float(sigmoid(wv))}
    res["phase"] = {}
    for kappa in (0.05, 0.25):
        res["phase"][str(kappa)] = phase_diagram(dict(par, kappa=kappa), quick)
    return res


def phase_diagram(par, quick):
    Cs = np.linspace(0.0, 6.0, 25 if quick else 61)
    etas = np.linspace(1.0, 25.0, 25 if quick else 49)
    outcome = np.zeros((etas.size, Cs.size)); neq = np.zeros_like(outcome); cert = np.zeros_like(outcome)
    stealth_global = np.zeros_like(outcome)
    for i, e in enumerate(etas):
        for j, c in enumerate(Cs):
            pp = dict(par, eta=float(e), C=float(c))
            E = two_channel_equilibria(pp, grid=40001 if quick else 200001)
            neq[i, j] = len(E)
            stab = [x for x in E if x["type"] == "stable"]
            if stab:
                best = max(stab, key=lambda x: x["J"])
                stealth_global[i, j] = float(best["q"] > 0.5 and best["s"] > 0.5)
            cert[i, j] = float(order_interval_certificate(pp)[0])
    for i, e in enumerate(etas):
        U = np.full(Cs.size, par["u0"]); W = np.full(Cs.size, par["w0"])
        A0 = par["bv"] * par["dR"] - (1 - par["bv"]) * Cs
        D = (par["bf"] - par["bv"]) * (par["dR"] + Cs)
        dt = 0.01
        for _ in range(int(40 * e / dt) if not quick else int(20 * e / dt)):
            gu = A0 + D * sigmoid(W) - (U - par["u0"]) / e
            gw = D * sigmoid(U) - par["kappa"] - (W - par["w0"]) / e
            U = U + dt * gu; W = W + dt * gw
        outcome[i, :] = (sigmoid(U) > 0.5) & (sigmoid(W) > 0.5)
    return {"kappa": par["kappa"], "C": Cs.tolist(), "eta": etas.tolist(), "stealth_reached": outcome.tolist(),
            "n_equilibria": neq.tolist(), "certificate": cert.tolist(), "stealth_global_opt": stealth_global.tolist(),
            "n_cells": int(outcome.size), "n_certified_cells": int(cert.sum()), "n_stealth_reached_cells": int(outcome.sum()),
            "n_bistable_cells": int((neq >= 3).sum()),
            "certificate_violations": int(np.sum((cert == 1) & (outcome == 1))),
            "unreachable_global_stealth_cells": int(np.sum((stealth_global == 1) & (outcome == 0))),
            "penalty_window": penalty_window(par)}


def experiment_stochastic(quick):
    """Finite-batch REINFORCE near the basin boundary (eta = 20): escape fraction vs batch size."""
    res = {}
    reps = 8 if quick else 24
    steps = 4000 if quick else 8000
    for C in (0.1, 0.15, 0.2):
        par = dict(BASE_2CH, eta=20.0, C=C)
        u, w, _ = two_channel_flow(par["u0"], par["w0"], par, T=400.0, dt=0.02)
        res[f"C{C}"] = {"meanfield_natural_endpoint": [float(sigmoid(u)), float(sigmoid(w))],
                        "equilibria": [(e["q"], e["s"], e["type"]) for e in two_channel_equilibria(par)]}
        for n_batch in (2, 4, 16, 256):
            rng = child_rng(f"two_channel_stochastic_C{C}_N{n_batch}")
            finals = [two_channel_stochastic(par, n_batch, steps, lr=0.5, rng=rng) for _ in range(reps)]
            esc = sum(1 for q, s in finals if q > 0.5 and s > 0.5)
            res[f"C{C}"][f"N{n_batch}"] = {"escape_fraction": esc / reps, "reps": reps, "steps": steps, "lr": 0.5}
    return res


def manifest():
    try:
        commit = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, timeout=10).stdout.strip()
    except Exception:  # noqa: BLE001
        commit = "unavailable"
    import scipy
    try:
        import matplotlib
        mpl = matplotlib.__version__
    except Exception:  # noqa: BLE001
        mpl = "absent"
    src = Path(__file__).read_bytes()
    return {"script": Path(__file__).name, "script_sha256": hashlib.sha256(src).hexdigest(), "version": VERSION,
            "root_entropy": ROOT_ENTROPY, "python": sys.version.split()[0], "numpy": np.__version__,
            "scipy": scipy.__version__, "matplotlib": mpl, "platform": platform.platform(), "git_commit": commit}


def figures(res, outdir: Path):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams.update({"font.size": 9, "axes.spines.top": False, "axes.spines.right": False, "svg.fonttype": "none",
                         "pdf.fonttype": 42})
    paths = []
    # Fig 1: NPG paths under none/A/B (pi_f and pi_h vs t), eta=8
    p = np.array(BASE_TAB["p"]); beta = np.array(BASE_TAB["beta"]); dR, C = BASE_TAB["dR"], BASE_TAB["C"]
    eta = 8.0
    ts = np.linspace(0, 40, 801)
    fig, ax = plt.subplots(1, 2, figsize=(7.0, 2.6))
    cols = {"none": "#555555", "A": "#c0392b", "B": "#2e6da4"}
    for op in ("none", "A", "B"):
        pis = npg_closed_form(p, effective_rewards(op, dR, beta, C, eta), eta, ts)
        ax[0].plot(ts, pis[:, 2], color=cols[op], label={"none": "no monitor", "A": "pure rejection (A)", "B": f"penalty C={C} (B)"}[op])
        ax[0].plot(ts, pis[:, 0], color=cols[op], ls="--", lw=0.9)
    tA = res["tabular"]["hitting_times_eta8"]["dominance_f_over_h_A"]
    if np.isfinite(tA):
        ax[0].axvline(tA, color=cols["A"], lw=0.6, ls=":")
    ax[0].set_xlabel("training time t"); ax[0].set_ylabel("probability"); ax[0].set_title("NPG, eta=8: solid stealth, dashed honest")
    ax[0].legend(frameon=False, fontsize=7)
    d = res["discard"]
    for g, col in (("0.2", "#8e44ad"), ("0.5", "#d35400")):
        tr = np.array(d["_traj_rft"][g])
        ax[1].plot(np.arange(tr.shape[0]), tr[:, 2], color=col, label=f"rejection fine-tuning, gamma={g}")
    tpg = np.array(d["_traj_pg"]["t"]); ppg = np.array(d["_traj_pg"]["pi"])
    ax[1].plot(tpg * 1.5, ppg[:, 2], color="#16a085", label="discard policy gradient (time x1.5)")
    ax[1].set_xlabel("round / rescaled time"); ax[1].set_ylabel("stealth probability"); ax[1].set_title("discard-and-retry: two algorithms")
    ax[1].legend(frameon=False, fontsize=7)
    fig.tight_layout()
    for ext in ("pdf", "svg"):
        f = outdir / f"fig-dynamique-tabulaire-v1.{ext}"; fig.savefig(f); paths.append(f)
    plt.close(fig)
    # Fig 2: two-channel phase portrait
    par = res["two_channel"]["params"]
    qs = np.linspace(0.002, 0.998, 300); ss = np.linspace(0.002, 0.998, 300)
    Q, S = np.meshgrid(qs, ss)
    gu, gw = two_channel_field(logit(Q), logit(S), par)
    fig, ax = plt.subplots(figsize=(3.6, 3.2))
    ax.contour(Q, S, gu, levels=[0], colors="#c0392b", linewidths=1.0)
    ax.contour(Q, S, gw, levels=[0], colors="#2e6da4", linewidths=1.0)
    st = 18
    Qs, Ss = np.meshgrid(np.linspace(0.02, 0.98, st), np.linspace(0.02, 0.98, st))
    a, b = two_channel_field(logit(Qs), logit(Ss), par)
    dq = Qs * (1 - Qs) * a; ds = Ss * (1 - Ss) * b
    nrm = np.hypot(dq, ds) + 1e-12
    ax.quiver(Qs, Ss, dq / nrm, ds / nrm, color="#999999", width=0.003, scale=30)
    for e in res["two_channel"]["equilibria"]:
        ax.plot(e["q"], e["s"], "o" if e["type"] == "stable" else "X", color="k", ms=5, mfc="k" if e["type"] == "stable" else "w")
    tr = np.array(res["two_channel"]["_traj_pi0"])
    ax.plot(sigmoid(tr[:, 1]), sigmoid(tr[:, 2]), color="#27ae60", lw=1.5, label="trajectory from base model")
    ax.set_xlabel("q = P(hack)"); ax.set_ylabel("s = P(obfuscated chain of thought)")
    ax.set_title("two-channel flow (red/blue: nullclines)", fontsize=8)
    ax.legend(frameon=False, fontsize=7, loc="center right")
    fig.tight_layout()
    for ext in ("pdf", "svg"):
        f = outdir / f"fig-portrait-deux-canaux-v1.{ext}"; fig.savefig(f); paths.append(f)
    plt.close(fig)
    # Fig 3: phase diagrams for two obfuscation costs
    fig, axs = plt.subplots(1, 2, figsize=(7.0, 3.0), sharey=True)
    for ax, kap in zip(axs, ("0.05", "0.25")):
        ph = res["two_channel"]["phase"][kap]
        Cs, etas = np.array(ph["C"]), np.array(ph["eta"])
        ax.pcolormesh(Cs, etas, (np.array(ph["n_equilibria"]) >= 3).astype(float), cmap="Greys", alpha=0.25, shading="nearest", vmin=0, vmax=1)
        if np.array(ph["stealth_reached"]).sum():
            ax.contourf(Cs, etas, np.array(ph["stealth_reached"]), levels=[0.5, 1.5], colors=["#c0392b"], alpha=0.6)
        if 0 < np.array(ph["certificate"]).sum() < np.array(ph["certificate"]).size:
            ax.contour(Cs, etas, np.array(ph["certificate"]), levels=[0.5], colors="#2e6da4", linewidths=1.2)
        if 0 < np.array(ph["stealth_global_opt"]).sum() < np.array(ph["stealth_global_opt"]).size:
            ax.contour(Cs, etas, np.array(ph["stealth_global_opt"]), levels=[0.5], colors="k", linestyles="--", linewidths=0.8)
        ax.set_xlabel("interception penalty C"); ax.set_title(f"obfuscation cost kappa = {kap}", fontsize=8)
    axs[0].set_ylabel("optimization pressure eta")
    fig.suptitle("red: stealth reached from the base model; grey: bistable; dashed: stealth node is the global optimum; blue: certificate boundary", fontsize=6.5)
    fig.tight_layout()
    for ext in ("pdf", "svg"):
        f = outdir / f"fig-diagramme-phases-deux-canaux-v1.{ext}"; fig.savefig(f); paths.append(f)
    plt.close(fig)
    return paths


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--no-figures", action="store_true")
    a = ap.parse_args(argv)
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    res = {"manifest": manifest(), "quick": a.quick}
    res["tabular"] = experiment_tabular(a.quick)
    res["discard"] = experiment_discard(a.quick)
    res["two_channel"] = experiment_two_channel(a.quick)
    res["stochastic"] = experiment_stochastic(a.quick)
    figs = [] if a.no_figures else figures(res, out)
    # guards on the scientific claims (never silent)
    t = res["tabular"]
    if t["max_abs_err_closed_form_vs_rk4"] > 1e-9:
        raise GuardError("closed-form NPG path disagrees with integration")
    if t["discrete_npg_max_err"] > 1e-12:
        raise GuardError("discrete NPG lambda_k formula fails")
    ph = res["two_channel"]["phase"]
    if any(v["certificate_violations"] for v in ph.values()):
        raise GuardError("order-interval certificate violated on the phase grid")
    if not any(v["n_certified_cells"] > 0 for v in ph.values()):
        raise GuardError("certificate soundness check is vacuous (no certified cell)")
    if res["two_channel"]["lyapunov_min_increment"] < -1e-10:
        raise GuardError("Lyapunov function decreased along the flow")
    public = {k: v for k, v in res.items()}
    public["discard"] = {k: v for k, v in res["discard"].items() if not k.startswith("_")}
    public["two_channel"] = {k: v for k, v in res["two_channel"].items() if not k.startswith("_")}
    fn = out / f"resultats-dynamique-{VERSION}{'-rapide' if a.quick else ''}.json"
    fn.write_text(json.dumps(public, indent=1, default=float, ensure_ascii=False) + "\n")
    for f in [fn, *figs]:
        h = hashlib.sha256(f.read_bytes()).hexdigest()
        Path(str(f) + ".sha256").write_text(f"{h}  {f.name}\n")
    print(json.dumps({"json": str(fn), "figures": [str(f) for f in figs],
                      "tab_err": t["max_abs_err_closed_form_vs_rk4"], "hitting": t["hitting_times"],
                      "hit8": t["hitting_times_eta8"],
                      "rft": {k: v for k, v in res["discard"].items() if k.startswith("rft")},
                      "pg": res["discard"]["discard_pg_meanfield"],
                      "2ch_eq": [(round(e["q"], 4), round(e["s"], 4), e["type"], round(e["J"], 4)) for e in res["two_channel"]["equilibria"]],
                      "2ch_flow": res["two_channel"]["flow_from_pi0"], "2ch_vanilla": res["two_channel"]["vanilla_flow_from_pi0"],
                      "cert": res["two_channel"]["certificate"], "window": res["two_channel"]["penalty_window"],
                      "phase": {k: {kk: vv for kk, vv in v.items() if kk.startswith("n_") or kk in ("certificate_violations", "unreachable_global_stealth_cells", "penalty_window")} for k, v in res["two_channel"]["phase"].items()},
                      "lyap": res["two_channel"]["lyapunov_min_increment"], "stoch": res["stochastic"]}, indent=1, default=float))
    return res


if __name__ == "__main__":
    main()
