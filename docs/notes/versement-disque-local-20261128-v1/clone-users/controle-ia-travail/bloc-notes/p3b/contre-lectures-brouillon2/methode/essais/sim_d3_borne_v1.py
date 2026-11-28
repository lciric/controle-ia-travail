"""Simulation synthétique (aucune donnée de P3) : borne de l'écart Δ_b de la ligne D3 de P3b, brouillon 2.

Premier pas seulement : une action par condition et par tâche. Pour chaque action, préférence moyenne sur les couches de
la bande (13 couches), chaque couche tirée de Bernoulli(p_a), p_a = logistique(μ + effet de tâche + effet d'action).
L'effet de tâche est commun à l'honnête et au saboteur (même τ_h, même leurre). Intervalle percentile à 95 % de
Δ = π(honnête) − π(saboteur) par blocs de tâches.

Sorties : part des répliques où la borne haute ≤ 0,15 (règle du brouillon 2), et où |Δ| est borné des deux côtés.
Toutes les grandeurs sont inventées. Graines par SeedSequence (R9).
"""
import numpy as np


def logistique(x):
    return 1 / (1 + np.exp(-x))


def une(rng, n, mu, delta_logit, sd_tache=1.0, sd_action=1.0, L=13, tirages=1000):
    tache = rng.normal(0, sd_tache, n)
    ph = logistique(mu + tache + rng.normal(0, sd_action, n))
    ps = logistique(mu - delta_logit + tache + rng.normal(0, sd_action, n))
    vh = rng.binomial(L, ph) / L
    vs = rng.binomial(L, ps) / L
    d = vh - vs
    idx = rng.integers(0, n, (tirages, n))
    b = d[idx].mean(axis=1)
    lo, hi = np.quantile(b, [0.025, 0.975])
    return vh.mean(), vs.mean(), d.mean(), lo, hi


def main():
    racine = np.random.SeedSequence(2026102102)
    print("n | μ | Δ logit vrai | π hon moy | Δ moy | part borne haute ≤ 0,15 | part |Δ| borné (deux côtés)")
    for n in (60, 40, 25):
        for mu in (0.4, 1.1, 2.2):
            for dl in (0.0, -1.5):
                rngs = [np.random.default_rng(s) for s in racine.spawn(400)]
                R = np.array([une(r, n, mu, dl) for r in rngs])
                haut = np.mean(R[:, 4] <= 0.15)
                deux = np.mean((R[:, 4] <= 0.15) & (R[:, 3] >= -0.15))
                print(f"{n} | {mu} | {dl} | {R[:,0].mean():.2f} | {R[:,2].mean():+.3f} | {haut:.2f} | {deux:.2f}")


if __name__ == "__main__":
    main()
