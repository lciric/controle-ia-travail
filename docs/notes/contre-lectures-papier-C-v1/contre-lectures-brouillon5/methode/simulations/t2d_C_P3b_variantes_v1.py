"""T2d : C-P3b (invariance au corpus du rang des juges, prediction 3 de N-005), au niveau des quinze G-barre par corpus.
G_{j,f} = amplitude x phi_f (effet de famille commun aux deux corpus) + delta_c x (-1, 0, 1)_j (effet de juge du corpus c)
+ erreur ; erreur = racine(r) eta_j + racine(1 - r) xi_{j,f} (r : correlation des erreurs d'un juge entre familles,
due aux temoins et contenus partages ; T1, T2). Trois tests :
  (i) texte : tau des quinze valeurs, permutation des quinze valeurs du corpus B ;
  (ii) permutation des etiquettes de juge dans chaque famille de B (7 776) ;
  (iii) proposition : tau sur les ecarts intra-famille (G_{j,f} - moyenne des trois juges de la famille), valeur p par
       reechantillonnage centre des deux corpus (erreurs tirees de la meme loi, independamment pour A et B).
"""
import itertools
import sys

import numpy as np

from t2_rang_temoins_partages_v1 import PERMS, kendall_tau

COMBOS = np.array(list(itertools.product(range(6), repeat=5)))


def erreurs(rng, size, r):
    eta = rng.normal(0, 1, size[:-2] + (1, 3))
    xi = rng.normal(0, 1, size)
    return np.sqrt(r) * eta + np.sqrt(1 - r) * xi


def dev(x):
    return x - x.mean(-1, keepdims=True)


def main():
    rng = np.random.default_rng(np.random.SeedSequence(0xB5CB).spawn(1)[0])
    phi = np.array([0.0, 1.0, 2.0, 3.0, 4.0])[:, None]
    jo = np.array([-1.0, 0.0, 1.0])[None, :]
    R, Bp, Bb = 600, 1000, 1000
    print("r     scenario                                   | (i) texte | (ii) etiquettes par famille | (iii) ecarts + reechantillonnage centre")
    for r in (0.0, 0.3, 0.5):
        for titre, amp, dA, dB in (("nul : famille seule, aucun effet de juge", 1.0, 0.0, 0.0),
                                   ("juges inverses entre corpus + famille", 1.0, 1.0, -1.0),
                                   ("invariance vraie (delta 1) + famille", 1.0, 1.0, 1.0),
                                   ("invariance vraie (delta 1), sans famille", 0.0, 1.0, 1.0)):
            a, b, c = [], [], []
            for _ in range(R):
                A = amp * phi + dA * jo + erreurs(rng, (5, 3), r)
                Bc = amp * phi + dB * jo + erreurs(rng, (5, 3), r)
                t = kendall_tau(A.ravel(), Bc.ravel())
                perm = np.argsort(rng.random((Bp, 15)), 1)
                tp = kendall_tau(np.broadcast_to(A.ravel(), (Bp, 15)), Bc.ravel()[perm])
                a.append((1 + (tp >= t).sum()) / (Bp + 1) <= 0.05)
                Bperm = np.take_along_axis(np.broadcast_to(Bc, (len(COMBOS), 5, 3)), PERMS[COMBOS], 2)
                ts = kendall_tau(np.broadcast_to(A.ravel(), (len(COMBOS), 15)), Bperm.reshape(len(COMBOS), 15))
                b.append((ts >= t - 1e-12).mean() <= 0.05)
                td = kendall_tau(dev(A).ravel(), dev(Bc).ravel())
                eA = erreurs(rng, (Bb, 5, 3), r)
                eB = erreurs(rng, (Bb, 5, 3), r)
                tn = kendall_tau(dev(eA).reshape(Bb, 15), dev(eB).reshape(Bb, 15))
                c.append((1 + (tn >= td).sum()) / (Bb + 1) <= 0.05)
            print(f"{r:.1f}   {titre:42s} |  {np.mean(a):.3f}    |  {np.mean(b):.3f}                      |  {np.mean(c):.3f}")
            sys.stdout.flush()
    return 0


if __name__ == "__main__":
    sys.exit(main())
