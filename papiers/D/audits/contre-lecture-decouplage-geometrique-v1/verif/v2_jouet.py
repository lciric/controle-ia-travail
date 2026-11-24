"""Audit-relevant checks on the toy network (copy of the companion module, imported read-only)."""
import sys
sys.path.insert(0, sys.argv[1])
import numpy as np
from scipy import stats
import experience_jouet_decouplage_sonde_v1 as m

rng = m.child_rng("toy_network"); n = 4000; steps = 1500
xc, xh, M0 = m.make_task(rng, n)
print("Bayes AUC of LDA on inputs, Phi(1.5/sqrt2) =", stats.norm.cdf(1.5/np.sqrt(2)))

def train_M(W, U, w, a, b, kind, steps, lr=0.5, opt="gd", adam_eps=1e-8, m_init=0.0, wd=0.0, train_head=False, head_lr=0.0):
    """Same objective as m.train; returns final M (and W)."""
    M = M0.copy(); Wt = W.copy()
    hc0, hh0 = m.act(xc @ M0.T, kind), m.act(xh @ M0.T, kind)
    mom = np.full_like(M, m_init); v = np.full_like(M, abs(m_init)**2 * 0 + (1e-6 if m_init else 0.0))
    for t in range(steps):
        zc = xc @ M.T; hc = m.act(zc, kind); zh = xh @ M.T; hh = m.act(zh, kind)
        u = (hc @ Wt.T) @ a - b; sp = m.sigmoid(u)*(1-m.sigmoid(u))
        gc = 2.0*sp[:, None]*(Wt.T @ a)[None, :] + 2*(hc-hc0) @ U @ U.T
        gh = 2*(hh-hh0)
        G = ((gc*m.dact(zc, kind)).T @ xc)/n + ((gh*m.dact(zh, kind)).T @ xh)/n
        if train_head:
            Wt = Wt - head_lr*2.0*np.outer(a, (sp[:, None]*hc).mean(0))
        if opt == "gd":
            M = M - lr*G - lr*wd*M
        else:  # Adam
            b1, b2 = 0.9, 0.999
            mom = b1*mom + (1-b1)*G; v = b2*v + (1-b2)*G*G
            mh = mom/(1-b1**(t+1)); vh = v/(1-b2**(t+1))
            with np.errstate(invalid="ignore", divide="ignore"):
                M = M - lr*mh/(np.sqrt(vh)+adam_eps)
    return M, Wt

def survivors_stats(M, W, w, a, b, kind, thr):
    hc = m.act(xc @ M.T, kind); hh = m.act(xh @ M.T, kind)
    surv = 1 - m.sigmoid((hc @ W.T) @ a - b)
    sc = hc @ w
    flag = (sc > thr).astype(float)
    return dict(audit_catch_all=flag.mean(), audit_catch_survivors=float((surv*flag).sum()/surv.sum()),
                mean_s_survivors=float((surv*sc).sum()/surv.sum()), mean_s_all=float(sc.mean()),
                filter_survival=float(surv.mean()), joint_evasion=float(np.mean(surv*(1-flag))),
                cov_surv_auditsurv=float(np.cov(surv, 1-flag)[0, 1]))

# (A) neuron-disjoint ReLU probe: score function invariant, but audit among filter survivors changes
for kind in ("relu", "linear"):
    W, U, w, a, b = m.heads(m.child_rng(f"heads_{kind}_disjoint"), M0, xc, xh, kind, "disjoint")
    hh0 = m.act(xh @ M0.T, kind); thr = np.quantile(hh0 @ w, 0.95)
    before = survivors_stats(M0, W, w, a, b, kind, thr)
    M1, _ = train_M(W, U, w, a, b, kind, steps)
    after = survivors_stats(M1, W, w, a, b, kind, thr)
    print(f"[{kind} disjoint] probe rows unchanged:", np.array_equal(M1[12:24], M0[12:24]))
    for k in before: print(f"   {k:24s} {before[k]: .4f} -> {after[k]: .4f}")

# (B) Ww stays ~0 while the head recruits probe neurons: choose w on S=12..23 orthogonal to E_c[sp * h_S]
kind = "relu"
W, U, w0, a, b = m.heads(m.child_rng("heads_relu_disjoint"), M0, xc, xh, kind, "disjoint")
hc0 = m.act(xc @ M0.T, kind); hh0 = m.act(xh @ M0.T, kind)
u0 = (hc0 @ W.T) @ a - b; sp0 = m.sigmoid(u0)*(1-m.sigmoid(u0))
c = (sp0[:, None]*hc0).mean(0)  # dW/dt = -2 a c^T  =>  d(Ww)/dt = -2 a (c.w)
S = np.arange(12, 24)
wS = w0[S] - c[S]*(c[S] @ w0[S])/(c[S] @ c[S]); w = np.zeros(32); w[S] = wS; w /= np.linalg.norm(w)
if (hc0 @ w).mean() < (hh0 @ w).mean(): w = -w
print("[recruitment] initial AUC of constructed probe:", m.auc(hc0 @ w, hh0 @ w), " c.w =", c @ w)
log, _, _ = m.train(xc, xh, M0, W, U, w, a, b, kind, steps, lr=0.5, train_head=True, head_lr=0.5)
M1, W1 = train_M(W, U, w, a, b, kind, steps, train_head=True, head_lr=0.5)
print("   ||W w|| end=%.4f  ||W_{:,S}|| end=%.4f  max probe change=%.4e  AUC %.4f->%.4f" % (
    np.linalg.norm(W1 @ w), np.linalg.norm(W1[:, S]), log[-1]["max_abs_probe_change"], log[0]["probe_auc"], log[-1]["probe_auc"]))
print("   trace ||Ww||:", [round(x["coupling_norm_Ww"], 4) for x in log[::5]])
# same for the companion's own probe
M1b, W1b = train_M(W, U, w0, a, b, kind, steps, train_head=True, head_lr=0.5)
print("   companion probe: ||W w||=%.4f ||W_{:,S}||=%.4f" % (np.linalg.norm(W1b @ w0), np.linalg.norm(W1b[:, S])))

# (C) optimizer edge cases on the neuron-disjoint probe
kind = "relu"
W, U, w, a, b = m.heads(m.child_rng("heads_relu_disjoint"), M0, xc, xh, kind, "disjoint")
for label, kw in (("Adam eps=1e-8, zero moments", dict(opt="adam", lr=1e-3)),
                  ("Adam eps=0, zero moments", dict(opt="adam", lr=1e-3, adam_eps=0.0)),
                  ("Adam, nonzero initial first moment (resumed state)", dict(opt="adam", lr=1e-3, m_init=1e-3)),
                  ("GD + plain weight decay 1e-3", dict(wd=1e-3))):
    M1, _ = train_M(W, U, w, a, b, kind, 200, **kw)
    hc = m.act(xc @ M1.T, kind); hh = m.act(xh @ M1.T, kind)
    s0c = hc0 @ w; s1c = hc @ w
    print(f"[{label}] probe rows moved: {not np.array_equal(M1[S], M0[S])}, NaN: {np.isnan(M1).any()}, "
          f"max|ds|={np.nanmax(np.abs(np.concatenate([s1c-s0c, hh@w-hh0@w]))):.3e}, AUC {m.auc(s0c, hh0@w):.6f}->{(m.auc(s1c, hh@w) if not np.isnan(M1).any() else float('nan')):.6f}")

# (D) linear network, Adam breaks Part 2 (Euclidean orthogonality) -- shows the 'plain GD' restriction matters
kind = "linear"
W, U, w, a, b = m.heads(m.child_rng("heads_linear_orthogonal_shared"), M0, xc, xh, kind, "orthogonal_shared")
M1, _ = train_M(W, U, w, a, b, kind, 200, opt="adam", lr=1e-3)
print("[linear orth-shared, Adam] max|w^T(M-M0)| =", np.abs(w @ (M1 - M0)).max())
M1, _ = train_M(W, U, w, a, b, kind, 200)
print("[linear orth-shared, GD]   max|w^T(M-M0)| =", np.abs(w @ (M1 - M0)).max())

# (E) first-order drift formula eq:ntk-drift, ReLU orthogonal-shared, at M0, finite step
kind = "relu"
W, U, w, a, b = m.heads(m.child_rng("heads_relu_orthogonal_shared"), M0, xc, xh, kind, "orthogonal_shared")
zc = xc @ M0.T; hc = m.act(zc, kind); u = (hc @ W.T) @ a - b; sp = m.sigmoid(u)*(1-m.sigmoid(u))
# filter loss l_x = 2*sigma(a^T W h - b) on cheats only (D = mixture, cheats weight 1/n each in the code)
gfilt = ((2*sp[:, None]*(W.T @ a)[None, :]*m.dact(zc, kind)).T @ xc)/n
for gam in (1e-2, 1e-3, 1e-4):
    M1 = M0 - gam*gfilt
    xs = np.vstack([xc[:200], xh[:200]])
    ds_true = m.act(xs @ M1.T, kind) @ w - m.act(xs @ M0.T, kind) @ w
    # formula: -gam * sum_i w_i * E_x[ W_:,i^T grad_z l  phi'(m_i x) ] phi'(m_i x') x^T x'
    ds_form = -gam * ((m.dact(xs @ M0.T, kind) * w[None, :]) * (xs @ gfilt.T)).sum(1)
    print("[ntk-drift] gamma=%.0e  max|true-formula|/max|true| = %.2e ; max|true|=%.2e" % (gam, np.abs(ds_true-ds_form).max()/np.abs(ds_true).max(), np.abs(ds_true).max()))
