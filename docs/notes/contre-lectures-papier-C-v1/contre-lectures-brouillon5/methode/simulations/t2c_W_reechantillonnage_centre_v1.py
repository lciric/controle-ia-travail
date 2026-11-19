"""T2c : correction proposee pour C-P3a (temoins partages) : valeur p du W par reechantillonnage centre. Dans chaque
tirage par taches, W* est calcule sur les rangs de (G*_{j,f} - G_{j,f}) ; p = (1 + #{W* >= W}) / (B + 1). Le centrage
retire tout ecart vrai entre juges et garde la dependance des erreurs (temoins et contenus partages).
Niveau sous le nul (aucun ecart entre juges) avec temoins partages par la regle ; puissance quand les juges different
vraiment (ecart de gain delta entre juges successifs, toutes familles), comparee a la valeur p exacte du texte.
"""
import sys

import numpy as np

from commun_b5_v1 import agrege, comptes, loi_jointe, regresseur, sommes_taches
from t1_loi_nette_rejeu_v1 import FAMILLES, appariement, simule_juge
from t2_rang_temoins_partages_v1 import nul_exact, p_exact, rangs, w_kendall


def essai(rng, T, pairs, delta, B):
    u = rng.normal(0, 0.5, T)
    tache = np.repeat(np.arange(T), 2)
    vrai = np.tile([2.0, 4.0], T) + u[tache] + rng.normal(0, 0.8, 2 * T)
    W = comptes(rng, T, B)
    G = np.zeros((5, 3))
    Gb = np.zeros((B, 5, 3))
    for j in range(3):
        g = 0.10 + delta * (j - 1)
        v0, wbar, Ys = simule_juge(rng, vrai, 0.4, g, 1.0, len(pairs[FAMILLES[0]]), pairs, False)
        for fi, Y in enumerate(Ys):
            s = sommes_taches(Y, v0, wbar, tache, T)
            G[fi, j] = float(loi_jointe(*regresseur(agrege(s))[:5])[2])
            Gb[:, fi, j] = loi_jointe(*regresseur(agrege(s, W))[:5])[2]
    w = w_kendall(rangs(G)[None])[0]
    ws = w_kendall(rangs(Gb - G[None]))
    return w, (1 + (ws >= w - 1e-12).sum()) / (B + 1)


def main():
    rng = np.random.default_rng(np.random.SeedSequence(0xB5CA).spawn(1)[0])
    nul5 = nul_exact(5)
    B, R = 500, 400
    print("k  T   delta | texte (p exact) P(p <= 0,05) | reechantillonnage centre P(p <= 0,05)")
    for idx, k in (([1, 8, 16], 3), ([1, 4, 8, 12, 16], 5)):
        pairs, _ = appariement(idx)
        for T in (45,):
            for delta in (0.0, 0.03, 0.06):
                L = [essai(rng, T, pairs, delta, B) for _ in range(R)]
                pe = np.array([p_exact(w, nul5) for w, _ in L])
                pb = np.array([p for _, p in L])
                print(f"{k}  {T:3d}  {delta:.2f}  |  {np.mean(pe <= 0.05):.3f}                         |  {np.mean(pb <= 0.05):.3f}")
                sys.stdout.flush()
    return 0


if __name__ == "__main__":
    sys.exit(main())
