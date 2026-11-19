"""Contre-lecture 9, constat B-1 : sous l'hypothèse nulle (aucune différence entre honnête et dose), une aire calculée à
l'unité de l'action, avec un plancher qui permute les étiquettes action par action dans chaque tâche, rejette-t-elle plus
souvent que son niveau quand les scores d'un même épisode sont corrélés ? Comparé à la permutation des étiquettes par
épisode. Loi simulée (effet d'épisode gaussien, part de variance 0,5), aucune donnée ; graines par SeedSequence (R9)."""
import numpy as np
T, E, A, NREP, NPERM, ALPHA = 16, 8, 10, 400, 400, 0.05
ss = np.random.SeedSequence(20261119)
def aire(scores, lab):
    r = scores.argsort().argsort().astype(float) + 1
    n1 = lab.sum(); n0 = lab.size - n1
    return (r[lab].sum() - n1 * (n1 + 1) / 2) / (n1 * n0)
res = {}
for rho in (0.0, 0.5):
    rej = {"action": 0, "épisode": 0}
    for rep, s in enumerate(ss.spawn(NREP)):
        g = np.random.default_rng(s)
        ep = g.normal(size=(T, 2 * E, 1)) * np.sqrt(rho)
        sc = (ep + g.normal(size=(T, 2 * E, A)) * np.sqrt(1 - rho)).ravel()
        lab_ep = np.zeros((T, 2 * E), bool); lab_ep[:, E:] = True
        lab = np.repeat(lab_ep[:, :, None], A, axis=2).ravel()
        obs = aire(sc, lab)
        cnt = {"action": 0, "épisode": 0}
        for _ in range(NPERM):
            pa = np.stack([g.permutation(lab.reshape(T, -1)[t]) for t in range(T)]).ravel()
            pe = np.repeat(np.stack([g.permutation(lab_ep[t]) for t in range(T)])[:, :, None], A, axis=2).ravel()
            cnt["action"] += aire(sc, pa) >= obs; cnt["épisode"] += aire(sc, pe) >= obs
        for k in rej: rej[k] += (1 + cnt[k]) / (1 + NPERM) <= ALPHA
    res[rho] = {k: v / NREP for k, v in rej.items()}
    print(f"part de variance d'épisode {rho} : rejet à {ALPHA} sous le nul — permutation par action {res[rho]['action']:.3f} ; par épisode {res[rho]['épisode']:.3f} ({NREP} répétitions, {NPERM} permutations)")
