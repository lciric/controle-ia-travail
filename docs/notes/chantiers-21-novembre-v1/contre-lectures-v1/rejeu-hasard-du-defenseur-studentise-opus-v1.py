"""Complément du rejeu (Opus 5.5) : statistique studentisée stratifiée pour le
contraste apparié sous le seul nul faible (moyennes égales, lois différentes).
Même monde que la case « 4 bis » de rejeu-hasard-du-defenseur-opus-v1.py.
T = somme_t (moyenne_U - moyenne_E) / racine(somme_t (s2_U + s2_E) / K).
"""
import zlib
import numpy as np

RACINE, K, B = 20261122, 2, 999


def stud(Z):
    U, E = Z[..., 2 * K:], Z[..., :K]
    num = (U.mean(-1) - E.mean(-1)).sum(-1)
    den = np.sqrt((U.var(-1, ddof=1) / K + E.var(-1, ddof=1) / K).sum(-1))
    return num / den


def p_valeur(rng, Z):
    t = stud(Z)
    o = np.argsort(rng.random((B,) + Z.shape), axis=-1)
    Zp = np.take_along_axis(np.broadcast_to(Z, (B,) + Z.shape), o, axis=-1)
    return (1 + np.sum(stud(Zp) >= t - 1e-12)) / (B + 1)


for n_taches in (50, 10):
    ss = np.random.SeedSequence(RACINE, spawn_key=(zlib.crc32(f"stud-{n_taches}".encode()),))
    ps = []
    for e in ss.spawn(2000):
        rng = np.random.default_rng(e)
        Z = rng.normal(0, 1, (n_taches, 3 * K))
        Z[:, 2 * K:] *= 4.0
        Z[:, :K] = rng.exponential(1.0, (n_taches, K)) - 1.0
        ps.append(p_valeur(rng, Z))
    r = np.mean(np.array(ps) <= 0.05)
    print(f"taches={n_taches}: rejet studentisé {r:.4f} (erreur type {np.sqrt(r*(1-r)/2000):.4f})")
