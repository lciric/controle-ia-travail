import numpy as np, math
from scipy import stats
from statistics import NormalDist
z = NormalDist().inv_cdf
def k0(alpha, Jtot, pi): return math.ceil(math.log(alpha / Jtot) / math.log(1 - pi))
rng = np.random.default_rng(np.random.SeedSequence(20261123))
alpha=0.0125; n=4000
crit = {0.5:(3.313,3.562), 0.05:(3.368,3.622)}
def puissance(pi, f0, c, reps=2000, continu=False):
    # fenêtre : P(signe|A=0)=f0 ; taux d'audit dans la fenêtre = c*pi
    f1 = f0 * c * (1 - pi) / (1 - c * pi)
    kk = [m * k0(alpha, 120, pi) for m in (1, 2, 4)]
    tables = [stats.norm.isf(np.clip(stats.binom.cdf(np.arange(k + 1), k, pi), 1e-300, 1 - 1e-16)) for k in kk]
    cz, call = crit[pi]
    rz = rq = rall = 0; rk=[0,0,0]
    for _ in range(reps):
        A = rng.random(n) < pi
        x = rng.random(n) < np.where(A, f1, f0)
        s = -x.astype(float)
        if continu:
            s = s * 10 + rng.normal(size=n)
        else:
            s = s + 1e-9 * rng.random(n)   # départage au hasard pour l'ordre
        r = stats.rankdata(-x.astype(float) if not continu else s); r = r - r.mean()
        Z = ((A - pi) * r).sum() / math.sqrt(pi * (1 - pi) * (r ** 2).sum())
        order = np.argsort(s)
        cs = np.cumsum(A[order[:kk[-1]]])
        Q = [tab[cs[k - 1]] for k, tab in zip(kk, tables)]
        rz += Z >= cz
        for i in range(3): rk[i] += Q[i] >= call
        rall += max(Z, max(Q)) >= call
    return rz / reps, [a / reps for a in rk], rall / reps
for pi, grid in ((0.05, (0.03, 0.04, 0.045, 0.05, 0.055, 0.06, 0.08, 0.10, 0.15, 0.2)), (0.5, (0.004, 0.006, 0.008, 0.009, 0.01, 0.012, 0.02, 0.04, 0.07))):
    for c in (0.0, 0.25, 0.5):
        for cont in (False, True):
            print(f"pi={pi} c={c} continu={cont}")
            for f0 in grid:
                pz, pk, pall = puissance(pi, f0, c, 1000, cont)
                print(f"   f0={f0:<6} Z seul(famille sans queues)={pz:.3f}  queues k0,2k0,4k0={pk}  tout={pall:.3f}")
