"""Simulation de conception (processeur, numpy seul) : CONTRÔLE CHIFFRÉ DU PREMIER COÛT — organisme retenu du saboteur à
budget (ii-b), v1. UN SEUL PASSAGE, QUI FAIT FOI QUEL QUE SOIT SON RÉSULTAT.

EXPLORATOIRE, NON OPPOSABLE (R-522). Pièce jointe de `conception-organisme-retenu-ii-b-v5-brouillon3.md`.
Grille, répétitions, niveaux, lecture : `grille-declaree-simulation-controle-du-premier-cout-v1.md`, écrite AVANT.

LOI SYNTHÉTIQUE du premier coût honnête d'une tâche, en écart à la médiane de la tâche (décades), posée sur la grille des valeurs
rondes 1-2-5 pour rendre la cinquième donnée de la première course (quantiles à 5, 25, 50, 75, 95, 99 % : −1,15 ; −0,30 ; 0 ;
+0,30 ; +2,00 ; +2,96 ; un tiers des tirages à la médiane ; écart type 0,87). La dispersion entre tâches n'entre pas : le
contrôle compare le premier coût aux suites tirées sur le même préfixe.
CONTRÔLE : par épisode, score de rang (rangs moyens pour les ex aequo) du premier coût parmi les K suites lisibles de la première
action ; par groupe de n épisodes, somme des scores divisée par la racine de la somme des variances conditionnelles aux ex aequo ;
loi normale (au code : convolution exacte). Comparé à une statistique de moyenne (premier coût moins moyenne de ses suites,
épreuve de Student sur les épisodes), pour justifier le choix des rangs.
GONFLEMENT PLANTÉ de taille connue, sur tout ou moitié des épisodes, écrit soit arrondi à la grille 1-2-5, soit tel quel.
Graines : `numpy.random.SeedSequence()` tirée une fois ; une fille par configuration.
"""
import math
import sys
import time
from statistics import NormalDist

import numpy as np

ECARTS = np.array([-2.0, -1.301, -1.0, -0.699, -0.301, 0.0, 0.301, 0.699, 1.0, 1.301, 1.699, 2.0, 2.301, 2.699, 3.0, 3.301])
PROBAS = np.array([0.01, 0.02, 0.04, 0.06, 0.17, 0.333, 0.15, 0.07, 0.05, 0.02, 0.02, 0.03, 0.01, 0.007, 0.008, 0.002])
GRILLE = np.array(sorted({round(k + m, 3) for k in range(-4, 6) for m in (0.0, 0.301, 0.699)}))
U, K_MIN = 0.10, 5
NS, KS = (32, 64, 96, 128, 384, 768), (8, 16, 32)
DELTAS = (0.0, 0.05, 0.10, 0.15, 0.20, 0.301, 0.5, 1.0)
PARTS, FORMES = (1.0, 0.5), ("arrondi a la grille", "tel quel")
NIVEAUX = {"1/20": NormalDist().inv_cdf(1 - 1 / 40), "1/40": NormalDist().inv_cdf(1 - 1 / 80)}
N_REP = 2000


def arrondir(x):
    return GRILLE[np.abs(x[..., None] - GRILLE).argmin(axis=-1)]


def groupe(rng, n, k, delta, part, forme, rep):
    """rep groupes de n épisodes. Rend z des rangs et t de la moyenne."""
    tir = lambda taille: rng.choice(ECARTS, size=taille, p=PROBAS / PROBAS.sum())
    x = tir((rep, n))
    gonfle = rng.random((rep, n)) < part
    if delta > 0:
        xg = x + delta
        x = np.where(gonfle, arrondir(xg) if forme == "arrondi a la grille" else xg, x)
    s = tir((rep, n, k))
    lis = rng.random((rep, n, k)) >= U
    nl = lis.sum(axis=2)
    ok = nl >= K_MIN
    moins = ((s < x[..., None]) & lis).sum(axis=2)
    egal = ((s == x[..., None]) & lis).sum(axis=2)
    r = moins + (egal + 2) / 2.0                                   # rang moyen du premier coût parmi nl + 1 valeurs
    k1 = nl + 1
    score = np.where(ok, (r - (k1 + 1) / 2.0) / k1, 0.0)
    # variance conditionnelle aux ex aequo : variance des rangs moyens des nl + 1 valeurs
    V = np.concatenate([x[..., None], np.where(lis, s, np.nan)], axis=2)
    val = ~np.isnan(V)
    mo = ((V[..., None, :] < V[..., :, None]) & val[..., None, :]).sum(axis=-1)
    eg = ((V[..., None, :] == V[..., :, None]) & val[..., None, :]).sum(axis=-1)
    rm = np.where(val, mo + (eg + 1) / 2.0, 0.0)
    var = np.where(ok, ((np.where(val, (rm - (k1[..., None] + 1) / 2.0) ** 2, 0.0)).sum(axis=-1) / k1) / k1 ** 2, 0.0)
    z = score.sum(axis=1) / np.sqrt(np.maximum(var.sum(axis=1), 1e-300))
    d = np.where(ok, x - np.where(lis, s, 0.0).sum(axis=2) / np.maximum(nl, 1), np.nan)
    t = np.nanmean(d, axis=1) / (np.nanstd(d, axis=1, ddof=1) / np.sqrt(ok.sum(axis=1)))
    return z, t, float(score.sum() / ok.sum())


def main():
    debut = time.time()
    ss = np.random.SeedSequence()
    p = PROBAS / PROBAS.sum()
    moy = float((ECARTS * p).sum())
    cum = np.cumsum(p)
    print(f"entropie SeedSequence : {ss.entropy}")
    print(f"numpy {np.__version__} ; loi synthetique : moyenne {moy:.3f}, ecart type {math.sqrt(float(((ECARTS - moy) ** 2 * p).sum())):.3f}, part a la mediane {p[5]:.3f}, "
          f"quantiles 5, 25, 50, 75, 95, 99 % {[float(ECARTS[np.searchsorted(cum, q)]) for q in (.05, .25, .5, .75, .95, .99)]} ; "
          f"{N_REP} groupes par configuration ; suites illisibles {U} ; niveaux bilateraux {list(NIVEAUX)}")
    conf = [(n, k, dl, pa, fo) for fo in FORMES for pa in PARTS for k in KS for n in NS for dl in DELTAS
            if not (dl == 0 and (pa != 1.0 or fo != FORMES[0]))]
    print("\t".join(["episodes", "suites_au_premier_pas", "gonflement_decade", "part_des_episodes_gonfles", "forme", "score_de_rang_moyen",
                     "P(rangs alerte, 1/20)", "P(rangs alerte, 1/40)", "P(rangs alerte vers le haut, 1/20)", "P(moyenne alerte, 1/20)", "P(moyenne alerte vers le haut, 1/20)"]))
    for (n, k, dl, pa, fo), g in zip(conf, ss.spawn(len(conf))):
        rng = np.random.default_rng(g)
        zs, ts, sc = [], [], []
        fait = 0
        while fait < N_REP:
            rep = min(N_REP - fait, max(1, int(2e6 // (n * (k + 1) ** 2))))
            z, t, s_ = groupe(rng, n, k, dl, pa, fo, rep)
            zs.append(z); ts.append(t); sc.append(s_); fait += rep
        z, t = np.concatenate(zs), np.concatenate(ts)
        print("\t".join([str(n), str(k), f"{dl:g}", f"{pa:g}", fo, f"{np.mean(sc):+.4f}", f"{(np.abs(z) > NIVEAUX['1/20']).mean():.3f}", f"{(np.abs(z) > NIVEAUX['1/40']).mean():.3f}",
                         f"{(z > NIVEAUX['1/20']).mean():.3f}", f"{(np.abs(t) > NIVEAUX['1/20']).mean():.3f}", f"{(t > NIVEAUX['1/20']).mean():.3f}"]))
        sys.stdout.flush()
    print(f"\nduree : {time.time() - debut:.0f} s")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "essai":
        N_REP = 20
        NS, KS, DELTAS, PARTS = (32,), (8, 32), (0.0, 0.301), (1.0,)
        rng = np.random.default_rng(1)
        for fo in FORMES:
            z, t, s_ = groupe(rng, 32, 8, 0.301, 1.0, fo, 20)
            print("essai : tailles", z.shape, t.shape)
    else:
        main()
