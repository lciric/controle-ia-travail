"""(1) ||Ww|| = 0 at the end while the head has recruited the probe neurons; (2) sign of the change of
audit catch among filter survivors for neuron-disjoint probes, over seeds and a variant task."""
import sys
sys.path.insert(0, sys.argv[1])
import numpy as np
import experience_jouet_decouplage_sonde_v1 as m

def run(xc, xh, M0, W, U, a, b, kind, steps, train_head, head_lr=0.5, lr=0.5):
    n = xc.shape[0]; M = M0.copy(); Wt = W.copy()
    hc0, hh0 = m.act(xc @ M0.T, kind), m.act(xh @ M0.T, kind)
    for t in range(steps):
        zc = xc @ M.T; hc = m.act(zc, kind); zh = xh @ M.T; hh = m.act(zh, kind)
        u = (hc @ Wt.T) @ a - b; sp = m.sigmoid(u)*(1-m.sigmoid(u))
        gc = 2.0*sp[:, None]*(Wt.T @ a)[None, :] + 2*(hc-hc0) @ U @ U.T
        G = ((gc*m.dact(zc, kind)).T @ xc)/n + ((2*(hh-hh0)*m.dact(zh, kind)).T @ xh)/n
        if train_head: Wt = Wt - head_lr*2.0*np.outer(a, (sp[:, None]*hc).mean(0))
        M = M - lr*G
    return M, Wt

# (1)
rng = m.child_rng("toy_network"); xc, xh, M0 = m.make_task(rng, 4000)
W, U, w0, a, b = m.heads(m.child_rng("heads_relu_disjoint"), M0, xc, xh, "relu", "disjoint")
M1, W1 = run(xc, xh, M0, W, U, a, b, "relu", 1500, True)   # training does not depend on w at all
S = np.arange(12, 24); WS = W1[:, S]
P = np.eye(12) - WS.T @ np.linalg.solve(WS @ WS.T, WS)
wS = P @ w0[S]; w = np.zeros(32); w[S] = wS / np.linalg.norm(wS)
hc0, hh0 = m.act(xc @ M0.T, "relu"), m.act(xh @ M0.T, "relu"); hc1, hh1 = m.act(xc @ M1.T, "relu"), m.act(xh @ M1.T, "relu")
if (hc0 @ w).mean() < (hh0 @ w).mean(): w = -w
print("[Ww monitor] ||W(T) w|| = %.2e, ||W(T)_{:,S}|| = %.3f, max probe change = %.3e, AUC %.4f -> %.4f" % (
    np.linalg.norm(W1 @ w), np.linalg.norm(WS), np.abs(np.concatenate([hc1@w-hc0@w, hh1@w-hh0@w])).max(),
    m.auc(hc0@w, hh0@w), m.auc(hc1@w, hh1@w)))

# (2) sign of the change of the audit catch rate among filter survivors, neuron-disjoint probes
def audit_surv(M, W, w, a, b, xc, xh, kind, thr):
    hc = m.act(xc @ M.T, kind); surv = 1 - m.sigmoid((hc @ W.T) @ a - b); flag = (hc @ w > thr)
    return float((surv*flag).sum()/surv.sum()), float(surv.mean())
res = []
for variant in ("companion", "two_dirs"):
    for seed in range(12):
        r = np.random.default_rng(np.random.SeedSequence(777, spawn_key=(seed, variant == "two_dirs")))
        n, p, d = 2000, 16, 32
        if variant == "companion":
            e = np.zeros(p); e[0] = 1.0; sc, sh = 0.75*e, -0.75*e
        else:  # cheats shifted along two directions, honest at the origin
            sc = np.zeros(p); sc[0] = 1.0; sc[1] = 1.0; sh = np.zeros(p)
        xc_ = r.normal(size=(n, p)) + sc; xh_ = r.normal(size=(n, p)) + sh
        M0_ = r.normal(size=(d, p))/np.sqrt(p)
        for kind in ("relu", "linear"):
            W_, U_, w_, a_, b_ = m.heads(np.random.default_rng(np.random.SeedSequence(778, spawn_key=(seed,))), M0_, xc_, xh_, kind, "disjoint")
            thr = np.quantile(m.act(xh_ @ M0_.T, kind) @ w_, 0.95)
            before = audit_surv(M0_, W_, w_, a_, b_, xc_, xh_, kind, thr)
            M1_, _ = run(xc_, xh_, M0_, W_, U_, a_, b_, kind, 600, False)
            after = audit_surv(M1_, W_, w_, a_, b_, xc_, xh_, kind, thr)
            res.append((variant, seed, kind, before[0], after[0], before[1], after[1]))
dec = [x for x in res if x[4] < x[3] - 1e-3]
print("[sign] %d runs, audit catch among survivors decreased in %d" % (len(res), len(dec)))
for x in sorted(res, key=lambda x: x[4]-x[3])[:5]:
    print("   %-9s seed=%2d %-6s audit|surv %.4f -> %.4f   filter survival %.4f -> %.4f" % x)
