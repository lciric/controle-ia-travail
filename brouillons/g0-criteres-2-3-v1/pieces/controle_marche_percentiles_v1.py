"""Contrôle de l'auteur : taux de fausse « gradation par effet partiel » sous une réponse en une seule marche,
avec des intervalles par rééchantillonnage des tâches (percentiles), comme dans la lecture, et non par approximation normale."""
import numpy as np, sys, time
ss = np.random.SeedSequence(2026112401)
rng = np.random.default_rng(ss)
N, B, SIMS = 64, 2000, 3000
sd_cond = 0.796 / np.sqrt(2)          # écart type de la différence appariée à deux répliques : 0,796
niveau = 1 - 0.05 / 5
q_bas = (1 - niveau) / 2 * 100
t0 = time.time()
for position, hauteur in ((0, 1.52), (3, 1.52), (5, 1.52), (3, 0.5)):
    moy = np.array([0.0] + [hauteur if i >= position else 0.0 for i in range(6)])   # neutre, puis six intensités
    faux = 0
    for s in range(SIMS):
        x = moy[None, :] + rng.normal(0, sd_cond, size=(N, 7)) + rng.normal(0, 0.5, size=(N, 1))
        idx = rng.integers(0, N, size=(B, N))
        ok = False
        for m in range(1, 6):
            d1 = x[:, m] - x[:, 0]; d2 = x[:, 6] - x[:, m]
            b1 = np.percentile(d1[idx].mean(axis=1), q_bas); b2 = np.percentile(d2[idx].mean(axis=1), q_bas)
            if b1 > 0 and b2 > 0:
                ok = True; break
        faux += ok
    print(f"marche à la position {position}, hauteur {hauteur} : gradation établie à tort dans {faux / SIMS:.4f} des courses ({SIMS} simulations, {B} tirages)", flush=True)
print("durée", round(time.time() - t0), "s")
