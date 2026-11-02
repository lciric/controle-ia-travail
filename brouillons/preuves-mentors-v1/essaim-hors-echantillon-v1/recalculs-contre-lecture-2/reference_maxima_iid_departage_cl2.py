"""Contre-lecture 2 : même mesure que `reference_maxima_iid_cl2.py`, avec départage uniforme des ex aequo de C_t
(règle proposée en M2). Loi de référence iid N(0, 1), hors grille ; graine jetable SeedSequence(77002)."""
import numpy as np
from scipy import stats
u = stats.norm.ppf(0.9)
g = np.random.default_rng(np.random.SeedSequence(77002))
for K, T in ((10, 10), (10, 20)):
    R = 200000
    Y = g.standard_normal((R, K, T))
    am = Y.argmax(axis=2)
    C = (Y >= u).sum(axis=1)
    pas_c = (C + 0.5 * g.random(C.shape)).argmax(axis=1)
    part = float((am == pas_c[:, None]).mean())
    se = (part * (1 - part) / (R * K)) ** 0.5
    hist = np.bincount(pas_c, minlength=T) / R
    print(f"K = {K}, T = {T} : part (départage uniforme) = {part:.4f} (± {se:.4f}) ; 1/T = {1 / T:.4f} ; "
          f"P(pas de co-élévation = 0) = {hist[0]:.3f}, = T−1 : {hist[-1]:.3f}")
