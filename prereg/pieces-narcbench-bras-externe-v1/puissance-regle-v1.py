"""Puissance de la règle « reproduit / non reproduit / non tranché » (rédacteur du texte court, bras externe NARCBench).

Données SIMULÉES seulement (modèle binormal), aucune donnée réelle. 20 sabots, chacun un épisode de collusion et un
épisode témoin ; intervalle percentile à 95 % par rééchantillonnage des sabots (2 000 tirages) ; marge = publié − 0,03.
"""
import sys

import numpy as np
from scipy.stats import norm, rankdata


def aires_lots(s1, s0):
    """Aires de Mann-Whitney, ex aequo pour moitié, pour des lots (B, n1) et (B, n0)."""
    n1, n0 = s1.shape[1], s0.shape[1]
    tout = np.concatenate([s1, s0], axis=1)
    r = rankdata(tout, axis=1)
    return (r[:, :n1].sum(axis=1) - n1 * (n1 + 1) / 2.0) / (n1 * n0)


def simuler(aire_vraie, publie, n_sabots=20, n_sim=2000, n_tirages=2000, rng=None):
    dprime = np.sqrt(2.0) * norm.ppf(aire_vraie)
    marge = publie - 0.03
    etats = {"reproduit": 0, "non reproduit": 0, "non tranché": 0}
    for _ in range(n_sim):
        s1 = rng.standard_normal(n_sabots) + dprime
        s0 = rng.standard_normal(n_sabots)
        choix = rng.integers(0, n_sabots, size=(n_tirages, n_sabots))
        a = aires_lots(s1[choix], s0[choix])
        bas, haut = np.quantile(a, 0.025), np.quantile(a, 0.975)
        if bas >= marge:
            etats["reproduit"] += 1
        elif haut < marge:
            etats["non reproduit"] += 1
        else:
            etats["non tranché"] += 1
    return {k: v / n_sim for k, v in etats.items()}


def main():
    racine = np.random.SeedSequence(int(sys.argv[1]))
    for publie in (1.00, 0.99):
        for k, aire in enumerate((0.9999, 0.995, 0.99, 0.98, 0.97, 0.95, 0.90, 0.80, 0.70, 0.50)):
            rng = np.random.default_rng(np.random.SeedSequence(racine.entropy, spawn_key=(int(publie * 100), k)))
            r = simuler(aire, publie, rng=rng)
            print(f"publié {publie:.2f}  aire vraie {aire:.4f}  " + "  ".join(f"{e} {p:.3f}" for e, p in r.items()))


if __name__ == "__main__":
    main()
