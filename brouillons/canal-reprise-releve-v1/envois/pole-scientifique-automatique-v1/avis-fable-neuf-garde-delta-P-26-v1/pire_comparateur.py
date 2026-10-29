# Forme « garde unique sur le pire comparateur » : processus de 1 + λ clip(δ − max_j g_j(t)), contre le minimum des k gardes.
# Même richesse mélangée que pari_apparie.trajectoire_log_richesse (Λ = 0,1 ; 0,3 ; 0,6 ; 0,9), sujet partagé, binomiale.
import numpy as np, math, sys
L = np.array([0.1, 0.3, 0.6, 0.9])
def logW(v):
    lw = np.cumsum(np.log1p(L[None, None, :] * v[:, :, None]), axis=1); m = lw.max(axis=2, keepdims=True)
    return (m + np.log(np.exp(lw - m).mean(axis=2, keepdims=True)))[:, :, 0]
def part(lw, s): return float((lw.max(axis=1) >= math.log(s)).mean())
rng = np.random.default_rng(np.random.SeedSequence([7312]))
reps, n, k = 1000, 160, 3
for K, tau, delta in [(10, .01, .05), (10, .10, .05), (3, .01, .05), (3, .10, .10)]:
    fa = rng.binomial(K, tau, size=(reps, 1, n)) / K
    fb = rng.binomial(K, tau, size=(reps, k, n)) / K
    g = fa - fb
    gardes = np.stack([logW(np.clip(delta - g[:, j, :], -1, 1)) for j in range(k)])
    pire = logW(np.clip(delta - g.max(axis=1), -1, 1))
    print(f"K={K} tau={tau} delta={delta} n={n} k={k} : min des {k} gardes 160/20 = {part(gardes.min(axis=0),160):.2f}/{part(gardes.min(axis=0),20):.2f} ; "
          f"pire comparateur 160/20 = {part(pire,160):.2f}/{part(pire,20):.2f} ; E[max_j g] = {g.max(axis=1).mean():+.4f}")
