"""Contrôle de l'auteur pour l'erratum 1 du correctif 1 : condition close en détection partielle. Hors dépôt."""
import numpy as np
rng = np.random.default_rng(np.random.SeedSequence(2026112417))
N = 100000
for nom in ("beta_f uniforme sur [beta_v, 1]", "beta_f uniforme sur [0, 1]"):
    pos = 0; ecart = 0.0; fh_pos = 0
    for _ in range(N):
        pi = rng.dirichlet([1, 1, 1]); bv = rng.uniform(0.01, 0.99); dR = rng.uniform(0.1, 3); C = rng.uniform(0, 4); h = 1e-6
        bf = rng.uniform(bv, 1.0) if "beta_v" in nom else rng.uniform(0.0, 1.0)
        def taux(C):
            r = np.array([0.0, bv*dR-(1-bv)*C, bf*dR-(1-bf)*C]); return r[2]-pi@r, r[2]-r[0]
        (a1, b1), (a0, b0) = taux(C+h), taux(C-h)
        d = (a1-a0)/(2*h); close = pi[1]*(1-bv)-(1-bf)*(1-pi[2])
        ecart = max(ecart, abs(d-close)); pos += close > 0; fh_pos += (b1-b0) > 0
    print(nom, ": derivee positive dans", pos, "sur", N, "| ecart max a la forme close", ecart, "| furtif contre honnete en hausse :", fh_pos)
