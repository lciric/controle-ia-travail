"""S8 : point A7, partage des 60 taches entre le pilote (choix des formulations) et l'etape 2 (episodes neufs).

Modele : interaction tache x formulation eta_{t,f} ~ N(0, s_eta^2), en unites de gain vers v* :
  Delta_{i,f} = gamma_f (c - v0_i) + eta_{t(i),f} (v* - v0_i) + bruit N(0, 0,4^2).
Population : lambda vrai = 0,5 (c = 1,5 ; v* = 0 ; moyenne de v0 = 3) ; gains gamma_f de 0 a 0,20 sur 16 formulations.
Pilote : 60 contenus (un par tache, taches 0..59) ; gamma chapeau_f vers v* (destination imposee, point 18) ; regle
des cibles equidistantes, k = 3. Etape 2 : 60 taches x 2 contenus (H, S), episodes neufs, soit sur LES MEMES taches
(eta partage), soit sur des taches neuves (eta neuf). Loi jointe sur les 3 formulations retenues.
Sortie : moyenne de lambda chapeau et de Gbar, contre les valeurs vraies de population ; part des essais ou
lambda chapeau > 0,5 (sens « vers la cible »).
"""
import sys

import numpy as np

from commun_v1 import agrege, loi_jointe, sommes_par_tache
from s4_vivier_kmax_v1 import regle

NF = 16
V_ETOILE = 0.0


def contenus(rng, T, par_tache):
    u = rng.normal(0, 0.5, T)
    tache = np.repeat(np.arange(T), par_tache)
    centres = np.tile([2.0, 4.0], T) if par_tache == 2 else rng.choice([2.0, 4.0], T)
    return centres + u[tache] + rng.normal(0, 0.8, T * par_tache), tache


def deltas(rng, v0, tache, gam, eta, c):
    D = (c - v0)[:, None] * gam[None, :] + eta[tache] * (V_ETOILE - v0)[:, None]
    return D + rng.normal(0, 0.4, D.shape)


def main():
    rng = np.random.default_rng(np.random.SeedSequence(0x5C81).spawn(1)[0])
    gam = np.linspace(0.0, 0.20, NF)
    c = 1.5
    R = 2000
    print("s_eta  | memes taches : moy. lambda  moy. Gbar  P(lambda>0,5) | taches neuves : moy. lambda  moy. Gbar  P(lambda>0,5) | Gbar vrai des retenues")
    for s_eta in (0.0, 0.03, 0.06, 0.10):
        res = []
        for _ in range(R):
            eta = rng.normal(0, s_eta, (60, NF)) if s_eta > 0 else np.zeros((60, NF))
            v0p, tp = contenus(rng, 60, 1)
            Dp = deltas(rng, v0p, tp, gam, eta, c)
            z = V_ETOILE - v0p
            gh = (Dp * z[:, None]).sum(0) / (z * z).sum()
            _, k, pris, _ = regle(gh, 1.0, 120)
            pris = pris[:3] if len(pris) > 3 else pris
            ligne = []
            for meme in (True, False):
                v02, t2 = contenus(rng, 60, 2)
                eta2 = eta if meme else (rng.normal(0, s_eta, (60, NF)) if s_eta > 0 else np.zeros((60, NF)))
                D2 = deltas(rng, v02, t2, gam, eta2, c)[:, pris]
                est = loi_jointe(agrege(sommes_par_tache(D2, v02, t2, 60)))
                lam = (float(est["c"]) - float(est["v0bar"])) / (V_ETOILE - float(est["v0bar"]))
                ligne += [lam, float(est["G"])]
            ligne.append(gam[pris].mean())
            res.append(ligne)
        a = np.array(res)
        print(f"{s_eta:.2f}   |  {a[:,0].mean():+.3f}       {a[:,1].mean():.3f}      {np.mean(a[:,0] > 0.5):.3f}         |"
              f"  {a[:,2].mean():+.3f}       {a[:,3].mean():.3f}      {np.mean(a[:,2] > 0.5):.3f}          |  {a[:,4].mean():.3f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
