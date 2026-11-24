"""Contrôle de l'auteur (v2, après le constat V1-01 de la vérification 1) : taux de fausse « gradation par effet partiel »
sous une réponse des intensités en deux paliers, avec des intervalles par rééchantillonnage des tâches (percentiles), comme
dans la lecture, et non par approximation normale. Règle : il existe m parmi 1,5 ; 2 ; 3 ; 5 tel que (m moins intensité 1,25)
et (intensité 10 moins m) aient une borne basse > 0 au niveau 1 − 0,05/4.
Colonnes simulées : les six intensités (1,25 ; 1,5 ; 2 ; 3 ; 5 ; 10). Un gonflement commun à toute demande ne change aucune
différence entre intensités : il n'est pas simulé. Position k : la marche tombe entre la k-ième et la (k+1)-ième intensité.
Écart type de la différence appariée : 0,796 (deux répliques, tout le bruit d'épisode), ou 0,974 (moitié d'interaction)."""
import numpy as np

rng = np.random.default_rng(np.random.SeedSequence(2026112402))
N, B, SIMS = 64, 2000, 3000
niveau = 1 - 0.05 / 4
q_bas = (1 - niveau) / 2 * 100
for position, hauteur, sd_diff in ((1, 1.52, 0.796), (3, 1.52, 0.796), (5, 1.52, 0.796), (3, 0.5, 0.796), (3, 1.52, 0.974), (5, 0.5, 0.974)):
    sd_cond = sd_diff / np.sqrt(2)
    moy = np.array([hauteur if i >= position else 0.0 for i in range(6)])
    faux = 0
    for s in range(SIMS):
        x = moy[None, :] + rng.normal(0, sd_cond, size=(N, 6)) + rng.normal(0, 0.5, size=(N, 1))
        idx = rng.integers(0, N, size=(B, N))
        ok = False
        for m in range(1, 5):
            d1 = x[:, m] - x[:, 0]; d2 = x[:, 5] - x[:, m]
            if np.percentile(d1[idx].mean(axis=1), q_bas) > 0 and np.percentile(d2[idx].mean(axis=1), q_bas) > 0:
                ok = True; break
        faux += ok
    print(f"marche à la position {position}, hauteur {hauteur}, écart type de la différence {sd_diff} : gradation établie à tort dans "
          f"{faux / SIMS:.4f} des courses ({SIMS} simulations, {B} tirages)", flush=True)
