"""Contre-lecture cl1 (oracle couplé, v3) : la composante « rangs au contexte réécrit » tient-elle son niveau sous couplage
par le préfixe (nœud 6, non joué par le rédacteur) ? Code du contre-lecteur, importe seulement `coupler`, `Contexte`,
`moyenne` de `rejeu-oracle-couple-cl1.py` (même dossier). Ancre du jumeau = (1 − kappa) ancre réécrite + kappa ancre de
l'agent. Agent honnête ; 500 étalonnages de 64 épisodes ; rangs signés (approximation normale, rangs moyens) au niveau
bilatéral 1/60. Entropie tirée une fois et écrite."""
import importlib.util, math, sys
import numpy as np
sp = importlib.util.spec_from_file_location("r", sys.argv[1]); r = importlib.util.module_from_spec(sp); sp.loader.exec_module(r)
T, K, U, Z = 10, 8, 0.10, 2.3940

def niveau(rng, sigma, rho, kappa, m, reps=500, n_ep=64):
    n = reps * n_ep
    ca, cw = r.Contexte(n, "dernier"), r.Contexte(n, "dernier")
    sc = np.full((n, T), np.nan)
    for t in range(T):
        x = r.moyenne(t, rho, ca.a) + sigma * rng.standard_normal(n)
        d = np.where(rng.random(n) >= U, x, np.nan)
        aw = np.where(np.isnan(ca.a), cw.a, np.where(np.isnan(cw.a), ca.a, (1 - kappa) * cw.a + kappa * ca.a))
        s = r.moyenne(t, rho, aw)[:, None] + sigma * rng.standard_normal((n, K))
        s = np.where(rng.random((n, K)) < U, np.nan, s)
        k = (~np.isnan(s)).sum(axis=1)
        rang = (s < d[:, None]).sum(axis=1) + 1 + (s == d[:, None]).sum(axis=1) / 2
        sc[:, t] = np.where(~np.isnan(d) & (k >= 5), (rang - (k + 2) / 2) / (k + 1), np.nan)
        cw.ajouter(r.coupler(rng, s, d, m)); ca.ajouter(d)
    nb = (~np.isnan(sc)).sum(axis=1)
    ep = (np.nansum(sc, axis=1) / np.maximum(nb, 1)).reshape(reps, n_ep)
    arr = 0
    for xs in ep:
        xs = xs[xs != 0]; a = np.abs(xs); o = a.argsort().argsort() + 1.0
        for v in np.unique(a):
            mm = a == v
            if mm.sum() > 1: o[mm] = o[mm].mean()
        arr += abs((np.sign(xs) * o).sum()) / math.sqrt((o ** 2).sum()) > Z
    return arr / reps

ss = np.random.SeedSequence(); print(f"entropie SeedSequence : {ss.entropy}")
for (sig, rho, kap, m), g in zip([(s, rho, k, m) for s in (0.05, 0.10, 0.30) for rho in (0.9,) for k in (0.0, 0.5) for m in (4, 8)], ss.spawn(12)):
    print(f"dispersion {sig} ancrage {rho} couplage par le prefixe {kap} bloc {m} : arret de la composante = {niveau(np.random.default_rng(g), sig, rho, kap, m):.3f}")
