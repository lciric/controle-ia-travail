"""Exact (quadrature) check of the Stein shift and the counterexample; proper SE by replication."""
import sys, json
sys.path.insert(0, sys.argv[1])
import numpy as np
from scipy import integrate, stats
import experience_jouet_decouplage_sonde_v1 as m

J = json.load(open(sys.argv[2]))["selection"]
print("SE ratios:", {k: J[k]["abs_diff"]/J[k]["mc_se"] for k in ("aligned","sigma_orthogonal","random")})

# rebuild the exact parameters by replaying the rng in the same order as selection_gaussian
def params(rng, n):
    d, mm = 6, 2
    A = rng.normal(size=(d, d)); Sigma = A @ A.T / d + 0.5*np.eye(d)
    mu = rng.normal(size=d); W = rng.normal(size=(mm, d))
    a = np.array([1.0, -0.5]); b = 0.3
    L = np.linalg.cholesky(Sigma)
    _ = rng.normal(size=(n, d))  # h draws
    r = rng.normal(size=d); K = W @ Sigma
    w_orth = r - K.T @ np.linalg.solve(K @ K.T, K @ r)
    w_rand = rng.normal(size=d)
    return Sigma, mu, W, a, b, {"aligned": W.T @ a, "sigma_orthogonal": w_orth, "random": w_rand}
Sigma, mu, W, a, b, probes = params(m.child_rng("selection"), 4000000)
# u = a^T W h ~ N(mu_u, var_u); g = 1 - sigma(u - b); E_g[s]-E[s] = Cov(s,u)/var_u * (E_g u - E u) (Gaussian regression)
v = W.T @ a; mu_u = v @ mu; var_u = v @ Sigma @ v; sd_u = np.sqrt(var_u)
g = lambda u: 1 - 1/(1+np.exp(-(u-b)))
pdf = lambda u: stats.norm.pdf(u, mu_u, sd_u)
lo, hi = mu_u - 40*sd_u, mu_u + 40*sd_u
Eg = integrate.quad(lambda u: g(u)*pdf(u), lo, hi, epsabs=1e-14, epsrel=1e-13)[0]
Egu = integrate.quad(lambda u: u*g(u)*pdf(u), lo, hi, epsabs=1e-14, epsrel=1e-13)[0]/Eg
Egsig = integrate.quad(lambda u: (1-g(u))*g(u)*pdf(u), lo, hi, epsabs=1e-14, epsrel=1e-13)[0]/Eg
for k, w in probes.items():
    exact = (w @ Sigma @ v)/var_u * (Egu - mu_u)
    stein = -Egsig * (w @ Sigma @ v)
    print(k, "exact=%.10f stein_exact=%.10f mc=%.6f pred_mc=%.6f  (mc-exact)/se=%.2f" % (exact, stein, J[k]["shift_mc"], J[k]["stein_prediction"], (J[k]["shift_mc"]-exact)/J[k]["mc_se"]))

# counterexample exact
gc = lambda x: 1 - 1/(1+np.exp(-(2*x-0.5)))
E1 = integrate.quad(lambda x: gc(x)*stats.norm.pdf(x), -40, 40, epsabs=1e-15)[0]
E2 = integrate.quad(lambda x: (x*x-1)*gc(x)*stats.norm.pdf(x), -40, 40, epsabs=1e-15)[0]
print("counterexample exact shift = %.6f ; mc = %.6f" % (E2/E1, J["nongaussian_counterexample"]["shift_mc"]))

# replication: actual sd of (shift_mc - pred) vs the crude se, at n = 4e5, 40 reps
n = 400000; R = 40
diffs = {k: [] for k in probes}; ses = {k: [] for k in probes}; dev_exact = {k: [] for k in probes}
for rep in range(R):
    rng = np.random.default_rng(np.random.SeedSequence(12345, spawn_key=(rep,)))
    h = mu + rng.normal(size=(n, 6)) @ np.linalg.cholesky(Sigma).T
    z = h @ W.T; u = z @ a
    gg = g(u); glog = -(1-gg)[:, None]*a[None, :]; wt = gg/gg.mean()
    for k, w in probes.items():
        s = h @ w
        sh = np.mean(wt*s) - np.mean(s); pr = (W @ Sigma @ w) @ np.mean(wt[:, None]*glog, axis=0)
        diffs[k].append(sh - pr); ses[k].append(np.std(wt*s - s)/np.sqrt(n))
        dev_exact[k].append(sh - (w @ Sigma @ v)/var_u*(Egu - mu_u))
for k in probes:
    print(k, "sd(shift-pred) over reps=%.3e  mean crude se=%.3e  ratio=%.2f ; sd(shift-exact)=%.3e" % (np.std(diffs[k], ddof=1), np.mean(ses[k]), np.std(diffs[k], ddof=1)/np.mean(ses[k]), np.std(dev_exact[k], ddof=1)))
