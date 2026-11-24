"""Neuron-disjoint probe, exactly invariant score function, yet the audit catch rate among filter
survivors FALLS under in-loop training: two cheating sub-types, filter sees type A, probe sees type B."""
import sys
sys.path.insert(0, sys.argv[1])
import numpy as np
import experience_jouet_decouplage_sonde_v1 as m
rng = np.random.default_rng(np.random.SeedSequence(2026, spawn_key=(1,)))
n, p, d = 4000, 16, 32
xa = rng.normal(size=(n//2, p)); xa[:, 0] += 2.0     # cheats of type A: visible to the filter
xb = rng.normal(size=(n//2, p)); xb[:, 1] += 2.0     # cheats of type B: visible to the probe
xc = np.vstack([xa, xb]); xh = rng.normal(size=(n, p))
for kind in ("linear", "relu"):
    M0 = rng.normal(size=(d, p))/np.sqrt(p)
    if kind == "relu":   # make probe neurons read +x1 and filter neurons read +x0, positively
        M0[:12] = np.abs(M0[:12]); M0[:12, 0] += 1.0
        M0[12:24, 1] += 1.0
    W = np.zeros((2, d)); W[:, :12] = rng.normal(size=(2, 12))
    U = np.zeros((d, 8)); U[24 + np.arange(8), np.arange(8)] = 1.0
    hc0, hh0 = m.act(xc @ M0.T, kind), m.act(xh @ M0.T, kind)
    # filter direction a: best readout of x0 by the text head; probe w on neurons 12..23 reading x1
    a = W @ (hc0[: n//2].mean(0) - hh0.mean(0)); a /= np.linalg.norm(a)
    b = float(np.median(np.concatenate([(hc0 @ W.T) @ a, (hh0 @ W.T) @ a])))
    w = np.zeros(d); w[12:24] = hc0[n//2:, 12:24].mean(0) - hh0[:, 12:24].mean(0); w /= np.linalg.norm(w)
    thr = np.quantile(hh0 @ w, 0.95)
    def stats_(M):
        hc = m.act(xc @ M.T, kind); surv = 1 - m.sigmoid((hc @ W.T) @ a - b); flag = hc @ w > thr
        return (surv*flag).sum()/surv.sum(), surv.mean(), np.mean(surv*(~flag)), np.cov(surv, (~flag).astype(float))[0, 1]
    M = M0.copy()
    for t in range(1500):
        zc = xc @ M.T; hc = m.act(zc, kind); zh = xh @ M.T; hh = m.act(zh, kind)
        u = (hc @ W.T) @ a - b; sp = m.sigmoid(u)*(1-m.sigmoid(u))
        gc = 2.0*sp[:, None]*(W.T @ a)[None, :] + 2*(hc-hc0) @ U @ U.T
        G = ((gc*m.dact(zc, kind)).T @ xc)/n + ((2*(hh-hh0)*m.dact(zh, kind)).T @ xh)/n
        M = M - 0.5*G
    b0, b1 = stats_(M0), stats_(M)
    hc1, hh1 = m.act(xc @ M.T, kind), m.act(xh @ M.T, kind)
    print(f"[{kind}] probe rows unchanged: {np.array_equal(M[12:24], M0[12:24])}; probe AUC {m.auc(hc0@w, hh0@w):.4f} -> {m.auc(hc1@w, hh1@w):.4f}")
    print("   audit catch among filter survivors %.4f -> %.4f ; filter survival %.4f -> %.4f ; joint evasion %.4f -> %.4f ; Cov(loop surv, audit surv) %+.4f -> %+.4f" % (b0[0], b1[0], b0[1], b1[1], b0[2], b1[2], b0[3], b1[3]))
