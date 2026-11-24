#!/usr/bin/env python3
"""Off-loop probe decoupling under in-loop filtering of a chain-of-thought head (companion code).

Standalone, CPU-only, deterministic.  Checks the geometric decoupling results:

  (a) Selection on the filter readout z = W h (rejection / any tilting g(Wh)):
      Gaussian representation -> exact Stein mean-shift of the frozen probe score
      s = w.h:  E_g[s] - E[s] = (W Sigma w) . E_g[grad log g(z)];  zero shift
      when W Sigma w = 0;  a non-Gaussian counterexample where W Sigma w = 0 but
      the probe still drifts (uncorrelated is not independent).
  (b) Gradient training of a one-hidden-layer network h = act(M x) against a
      logistic filter on W h, with frozen heads: three probe placements
      (neuron-disjoint from the filter head; Euclidean-orthogonal but sharing
      neurons; aligned with the filter readout), linear vs ReLU activations.
      Prediction: neuron-disjoint -> exact invariance for the whole trajectory
      (both activations); orthogonal-shared -> invariant for linear, drifts for
      ReLU; aligned -> drifts (probe evaded together with the filter).
  (c) Trainable chain-of-thought head: the head recruits probe neurons
      (coupling W w grows from zero), after which the probe score moves.

Usage: PYTHONDONTWRITEBYTECODE=1 python3 experience_jouet_decouplage_sonde_v1.py --out DIR [--quick]
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
    pass


def child_rng(task):
    key = int.from_bytes(hashlib.sha256(task.encode()).digest()[:8], "big")
    return np.random.default_rng(np.random.SeedSequence(ROOT_ENTROPY, spawn_key=(key,)))


def sigmoid(x):
    return 0.5 * (1.0 + np.tanh(0.5 * x))


def auc(pos, neg):
    """Mann-Whitney AUC, ties counted 1/2."""
    pos = np.asarray(pos); neg = np.asarray(neg)
    allv = np.concatenate([pos, neg])
    order = np.argsort(allv, kind="mergesort")
    ranks = np.empty(allv.size); ranks[order] = np.arange(1, allv.size + 1)
    # average ranks for ties
    vals, inv, cnt = np.unique(allv, return_inverse=True, return_counts=True)
    sums = np.zeros(vals.size); np.add.at(sums, inv, ranks)
    ranks = (sums / cnt)[inv]
    return float((ranks[: pos.size].sum() - pos.size * (pos.size + 1) / 2) / (pos.size * neg.size))


# ---------------------------------------------------------------------------
# (a) selection on the filter readout
# ---------------------------------------------------------------------------
def selection_gaussian(rng, n, quick):
    d, m = 6, 2
    A = rng.normal(size=(d, d)); Sigma = A @ A.T / d + 0.5 * np.eye(d)
    mu = rng.normal(size=d)
    W = rng.normal(size=(m, d))
    a = np.array([1.0, -0.5]); b = 0.3
    L = np.linalg.cholesky(Sigma)
    h = mu + rng.normal(size=(n, d)) @ L.T
    z = h @ W.T
    g = 1.0 - sigmoid(z @ a - b)               # survival probability of the filter
    glog = -(sigmoid(z @ a - b))[:, None] * a[None, :]  # grad_z log g
    out = {}
    # probe directions: aligned, Sigma-orthogonal to W rows, random
    w_al = W.T @ a
    # Sigma-orthogonal: project a random vector onto {w : W Sigma w = 0}
    r = rng.normal(size=d)
    K = W @ Sigma                                # m x d
    w_orth = r - K.T @ np.linalg.solve(K @ K.T, K @ r)
    w_rand = rng.normal(size=d)
    for name, w in (("aligned", w_al), ("sigma_orthogonal", w_orth), ("random", w_rand)):
        s = h @ w
        wt = g / g.mean()
        shift_mc = float(np.mean(wt * s) - np.mean(s))
        pred = float((W @ Sigma @ w) @ np.mean(wt[:, None] * glog, axis=0))
        # Monte Carlo standard error of the difference (delta method, crude)
        se = float(np.std(wt * s - s) / np.sqrt(n))
        out[name] = {"W_Sigma_w_norm": float(np.linalg.norm(W @ Sigma @ w)), "shift_mc": shift_mc,
                     "stein_prediction": pred, "abs_diff": abs(shift_mc - pred), "mc_se": se}
    # non-Gaussian counterexample: uncorrelated but dependent
    x = rng.normal(size=n)
    zc = x                                     # filter reads z = x
    sc = x ** 2 - 1.0                          # probe reads x^2 - 1: Cov(z, s) = 0
    gc = 1.0 - sigmoid(2.0 * zc - 0.5)
    wt = gc / gc.mean()
    out["nongaussian_counterexample"] = {"cov_z_s": float(np.cov(zc, sc)[0, 1]),
                                         "shift_mc": float(np.mean(wt * sc) - np.mean(sc)),
                                         "mc_se": float(np.std(wt * sc - sc) / np.sqrt(n))}
    return out


# ---------------------------------------------------------------------------
# (b, c) gradient training of a one-hidden-layer representation
# ---------------------------------------------------------------------------
def make_task(rng, n, p=16, d=32, sep=1.5):
    e = np.zeros(p); e[0] = 1.0
    xc = rng.normal(size=(n, p)) + sep * e / 2
    xh = rng.normal(size=(n, p)) - sep * e / 2
    M0 = rng.normal(size=(d, p)) / np.sqrt(p)
    return xc, xh, M0


def act(z, kind):
    return np.maximum(z, 0.0) if kind == "relu" else z


def dact(z, kind):
    return (z > 0).astype(float) if kind == "relu" else np.ones_like(z)


def heads(rng, M0, xc, xh, kind, placement, d=32, m=2):
    hc, hh = act(xc @ M0.T, kind), act(xh @ M0.T, kind)
    dmu = hc.mean(0) - hh.mean(0)
    W = np.zeros((m, d))
    filt = np.arange(0, 12)                    # neurons read by the chain-of-thought head
    task = np.arange(24, 32)                   # task-causal neurons (reward readout)
    W[:, filt] = rng.normal(size=(m, filt.size))
    U = np.zeros((d, task.size)); U[task, np.arange(task.size)] = 1.0
    if placement == "disjoint":
        mask = np.zeros(d); mask[12:24] = 1.0
        w = mask * dmu
    elif placement == "orthogonal_shared":
        mask = np.zeros(d); mask[0:12] = 1.0
        w = mask * dmu
        Wr = W[:, filt]
        ws = w[filt] - Wr.T @ np.linalg.solve(Wr @ Wr.T, Wr @ w[filt])  # Euclidean projection: W w = 0
        w = np.zeros(d); w[filt] = ws
    elif placement == "aligned":
        w = W.T @ (W @ dmu)
    else:
        raise GuardError(placement)
    if np.linalg.norm(w) == 0:
        raise GuardError("degenerate probe")
    w = w / np.linalg.norm(w)
    if np.mean(hc @ w) < np.mean(hh @ w):
        w = -w
    a = W @ dmu; a = a / (np.linalg.norm(a) + 1e-12)
    zc = (hc @ W.T) @ a; zh = (hh @ W.T) @ a
    b = float(np.median(np.concatenate([zc, zh])))
    return W, U, w, a, b


def refit_probe_auc(hc, hh):
    """Linear separability after training: Fisher LDA on half, AUC on the other half."""
    n = hc.shape[0] // 2
    mu_c, mu_h = hc[:n].mean(0), hh[:n].mean(0)
    S = np.cov(np.vstack([hc[:n] - mu_c, hh[:n] - mu_h]).T) + 1e-3 * np.eye(hc.shape[1])
    v = np.linalg.solve(S, mu_c - mu_h)
    return auc(hc[n:] @ v, hh[n:] @ v)


def train(xc, xh, M0, W, U, w, a, b, kind, steps, lr, lam=2.0, mu=1.0, nu=1.0, train_head=False, head_lr=0.0):
    M = M0.copy(); Wt = W.copy()
    hc0, hh0 = act(xc @ M0.T, kind), act(xh @ M0.T, kind)
    nc, nh = xc.shape[0], xh.shape[0]
    log = []
    for t in range(steps + 1):
        zc_pre = xc @ M.T; hc = act(zc_pre, kind)
        zh_pre = xh @ M.T; hh = act(zh_pre, kind)
        if t % max(1, steps // 20) == 0 or t == steps:
            filt_c = sigmoid((hc @ Wt.T) @ a - b)
            log.append({"step": t, "probe_auc": auc(hc @ w, hh @ w),
                        "probe_mean_cheat_shift": float(np.mean(hc @ w) - np.mean(hc0 @ w)),
                        "filter_catch_rate_cheat": float(np.mean(filt_c)),
                        "coupling_norm_Ww": float(np.linalg.norm(Wt @ w)),
                        "max_abs_probe_change": float(np.max(np.abs(np.concatenate([hc @ w - hc0 @ w, hh @ w - hh0 @ w]))))})
        if t == steps:
            break
        u = (hc @ Wt.T) @ a - b
        sp = sigmoid(u) * (1 - sigmoid(u))
        gc = lam * sp[:, None] * (Wt.T @ a)[None, :] + 2 * mu * (hc - hc0) @ U @ U.T
        gh = 2 * nu * (hh - hh0)
        gradM = ((gc * dact(zc_pre, kind)).T @ xc) / nc + ((gh * dact(zh_pre, kind)).T @ xh) / nh
        if train_head:
            gW = lam * np.outer(a, (sp[:, None] * hc).mean(0))
            Wt = Wt - head_lr * gW
        M = M - lr * gradM
    hc, hh = act(xc @ M.T, kind), act(xh @ M.T, kind)
    return log, refit_probe_auc(hc, hh), refit_probe_auc(hc0, hh0)


def experiment_training(quick):
    rng = child_rng("toy_network")
    n = 1500 if quick else 4000
    steps = 400 if quick else 1500
    xc, xh, M0 = make_task(rng, n)
    out = {}
    for kind in ("linear", "relu"):
        for placement in ("disjoint", "orthogonal_shared", "aligned"):
            W, U, w, a, b = heads(child_rng(f"heads_{kind}_{placement}"), M0, xc, xh, kind, placement)
            log, refit_after, refit_before = train(xc, xh, M0, W, U, w, a, b, kind, steps, lr=0.5)
            out[f"{kind}_{placement}"] = {"start": log[0], "end": log[-1], "refit_auc_before": refit_before,
                                          "refit_auc_after": refit_after, "W_w_norm_init": float(np.linalg.norm(W @ w)),
                                          "neuron_overlap": int(np.sum((np.abs(W).sum(0) > 0) & (np.abs(w) > 0))),
                                          "trace": log}
    # (c) trainable head, disjoint start, relu
    W, U, w, a, b = heads(child_rng("heads_relu_disjoint"), M0, xc, xh, "relu", "disjoint")
    log, ra, rb = train(xc, xh, M0, W, U, w, a, b, "relu", steps, lr=0.5, train_head=True, head_lr=0.5)
    out["relu_disjoint_trainable_head"] = {"start": log[0], "end": log[-1], "refit_auc_before": rb, "refit_auc_after": ra, "trace": log}
    return out


def manifest():
    try:
        commit = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, timeout=10).stdout.strip()
    except Exception:  # noqa: BLE001
        commit = "unavailable"
    return {"script": Path(__file__).name, "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "version": VERSION, "root_entropy": ROOT_ENTROPY, "python": sys.version.split()[0], "numpy": np.__version__,
            "platform": platform.platform(), "git_commit": commit}


def figure(res, outdir):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams.update({"font.size": 8, "axes.spines.top": False, "axes.spines.right": False, "svg.fonttype": "none", "pdf.fonttype": 42})
    fig, axs = plt.subplots(1, 3, figsize=(7.2, 2.4))
    cols = {"disjoint": "#2e6da4", "orthogonal_shared": "#d35400", "aligned": "#c0392b"}
    for kind, ls in (("linear", "--"), ("relu", "-")):
        for pl, c in cols.items():
            tr = res["training"][f"{kind}_{pl}"]["trace"]
            st = [x["step"] for x in tr]
            axs[0].plot(st, [x["filter_catch_rate_cheat"] for x in tr], color=c, ls=ls, lw=1)
            axs[1].plot(st, [x["probe_auc"] for x in tr], color=c, ls=ls, lw=1, label=f"{pl} ({kind})")
    tr = res["training"]["relu_disjoint_trainable_head"]["trace"]
    st = [x["step"] for x in tr]
    axs[2].plot(st, [x["coupling_norm_Ww"] for x in tr], color="#8e44ad", label="|W w| (head trainable)")
    axs[2].plot(st, [x["max_abs_probe_change"] for x in tr], color="#16a085", label="max probe-score change")
    axs[0].set_title("in-loop filter: catch rate on cheats", fontsize=7); axs[0].set_xlabel("gradient step")
    axs[1].set_title("frozen off-loop probe: AUC", fontsize=7); axs[1].set_xlabel("gradient step")
    axs[1].legend(frameon=False, fontsize=5)
    axs[2].set_title("trainable CoT head recruits probe neurons", fontsize=7); axs[2].set_xlabel("gradient step")
    axs[2].legend(frameon=False, fontsize=6)
    fig.tight_layout()
    paths = []
    for ext in ("pdf", "svg"):
        f = outdir / f"fig-decouplage-sonde-v1.{ext}"; fig.savefig(f); paths.append(f)
    plt.close(fig)
    return paths


def main(argv=None):
    ap = argparse.ArgumentParser(); ap.add_argument("--out", required=True); ap.add_argument("--quick", action="store_true")
    ap.add_argument("--no-figures", action="store_true")
    a = ap.parse_args(argv)
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    res = {"manifest": manifest(), "quick": a.quick}
    res["selection"] = selection_gaussian(child_rng("selection"), 400000 if a.quick else 4000000, a.quick)
    res["training"] = experiment_training(a.quick)
    figs = [] if a.no_figures else figure(res, out)
    # guards
    sel = res["selection"]
    for k in ("aligned", "sigma_orthogonal", "random"):
        if sel[k]["abs_diff"] > 6 * sel[k]["mc_se"] + 1e-12:
            raise GuardError(f"Stein mean-shift prediction fails for {k}")
    tr = res["training"]
    for kind in ("linear", "relu"):
        if tr[f"{kind}_disjoint"]["end"]["max_abs_probe_change"] > 1e-10:
            raise GuardError("neuron-disjoint probe moved: exact invariance claim fails")
    if tr["linear_orthogonal_shared"]["end"]["max_abs_probe_change"] > 1e-8:
        raise GuardError("orthogonal probe moved in the linear network")
    if tr["relu_orthogonal_shared"]["end"]["max_abs_probe_change"] < 1e-6:
        raise GuardError("artefact check: orthogonal-shared ReLU probe did not move (prediction says it should)")
    pub = {k: v for k, v in res.items()}
    pub["training"] = {k: {kk: vv for kk, vv in v.items() if kk != "trace"} for k, v in tr.items()}
    fn = out / f"resultats-decouplage-{VERSION}{'-rapide' if a.quick else ''}.json"
    fn.write_text(json.dumps(pub, indent=1, ensure_ascii=False) + "\n")
    for f in [fn, *figs]:
        Path(str(f) + ".sha256").write_text(f"{hashlib.sha256(f.read_bytes()).hexdigest()}  {f.name}\n")
    print(json.dumps({"selection": sel, "training": {k: {"start_auc": v["start"]["probe_auc"], "end_auc": v["end"]["probe_auc"],
                     "filter_start": v["start"]["filter_catch_rate_cheat"], "filter_end": v["end"]["filter_catch_rate_cheat"],
                     "max_probe_change": v["end"]["max_abs_probe_change"], "Ww_end": v["end"]["coupling_norm_Ww"],
                     "refit_before": v["refit_auc_before"], "refit_after": v["refit_auc_after"]} for k, v in tr.items()}}, indent=1))
    return res


if __name__ == "__main__":
    main()
