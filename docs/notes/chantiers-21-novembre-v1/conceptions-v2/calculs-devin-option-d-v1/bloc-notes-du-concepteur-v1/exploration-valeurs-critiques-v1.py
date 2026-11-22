import numpy as np, math, time
from scipy import stats
from statistics import NormalDist
z = NormalDist().inv_cdf

def k0(alpha, Jtot, pi):
    return math.ceil(math.log(alpha / Jtot) / math.log(1 - pi))

def nul(n, pi, J, K_mult, alpha, N, rng, corr=0.0, discret=False):
    # sorties fixes
    if corr > 0:
        f = rng.normal(size=n)
        X = math.sqrt(corr) * f + math.sqrt(1 - corr) * rng.normal(size=(J, n))
    else:
        X = rng.normal(size=(J, n))
    R = stats.rankdata(X, axis=1) ; R = R - R.mean(axis=1, keepdims=True)
    den = np.sqrt(pi * (1 - pi) * (R ** 2).sum(axis=1))
    order = np.argsort(X, axis=1)  # plus petites sorties d'abord : jugées les moins auditées
    Jtot = J * (1 + len(K_mult))
    kk = [m * k0(alpha, Jtot, pi) for m in K_mult]
    tables = [stats.norm.isf(np.clip(stats.binom.cdf(np.arange(k + 1), k, pi), 1e-300, 1 - 1e-16)) for k in kk]
    MZ, MQ = [], []
    bloc = 2000
    for d in range(0, N, bloc):
        A = (rng.random((bloc, n)) < pi)
        Zs = ((A - pi) @ R.T) / den
        MZ.append(Zs.max(axis=1))
        mq = np.full(bloc, -np.inf)
        for j in range(J):
            cs = np.cumsum(A[:, order[j, :kk[-1]]], axis=1)
            for k, tab in zip(kk, tables):
                mq = np.maximum(mq, tab[cs[:, k - 1]])
        MQ.append(mq)
    MZ = np.concatenate(MZ); MQ = np.concatenate(MQ)
    return MZ, MQ, kk

rng = np.random.default_rng(np.random.SeedSequence(20261122))
alpha = 0.0125
for pi in (0.5, 0.05):
    for corr in (0.0, 0.5):
        t = time.time()
        MZ, MQ, kk = nul(4000, pi, 30, (1, 2, 4), alpha, 40000, rng, corr)
        cz = np.quantile(MZ, 1 - alpha); call = np.quantile(np.maximum(MZ, MQ), 1 - alpha); cq = np.quantile(MQ, 1 - alpha)
        c05 = np.quantile(MZ, 0.95)
        print(f"pi={pi} corr={corr} k={kk} crit Z seul={cz:.3f} (Bonf30 {z(1-alpha/30):.3f}) crit tout={call:.3f} (Bonf120 {z(1-alpha/120):.3f}) crit Q seul={cq:.3f} ; crit Z a 0.05={c05:.3f} ; "
              f"facteur taille (c+0.8416): {(call+0.8416)/(cz+0.8416):.4f} ; P(MQ>MZ)={np.mean(MQ>MZ):.3f} ; {time.time()-t:.0f}s")
