"""Contre-lecture 2 : la « référence 1/T » du descriptif des maxima (R3) est-elle la valeur sous une loi échangeable
en temps ? Monte-Carlo jetable sous la loi de référence iid N(0, 1) (c = 0 : loi hors grille), graine jetable
SeedSequence(77001), sans aucun module du dépôt. Même définition que `blocs_hors_echantillon_v2.maxima` : argmax de
chaque agent ; premier argmax de C_t = #{i : X_it >= u} ; part des agents dont le maximum tombe à ce pas."""
import numpy as np
from scipy import stats
u = stats.norm.ppf(0.9)
g = np.random.default_rng(np.random.SeedSequence(77001))
for K, T in ((10, 10), (10, 20), (1, 10)):
    R = 200000 if K > 1 else 400000
    Y = g.standard_normal((R, K, T))
    am = Y.argmax(axis=2)
    C = (Y >= u).sum(axis=1)
    pas_c = C.argmax(axis=1)
    part = float((am == pas_c[:, None]).mean())
    se = (part * (1 - part) / (R * K)) ** 0.5
    hist = np.bincount(pas_c, minlength=T) / R
    print(f"K = {K}, T = {T} : part au pas de co-élévation maximale = {part:.4f} (± {se:.4f}) ; 1/T = {1 / T:.4f} ; "
          f"P(premier argmax de C_t = pas 0) = {hist[0]:.3f}, pas T−1 = {hist[-1]:.3f}")
