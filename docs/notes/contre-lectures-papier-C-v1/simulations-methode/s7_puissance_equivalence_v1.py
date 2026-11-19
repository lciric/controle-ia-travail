"""S7 : puissance de l'equivalence de HC2 (marge 0,10 en unites de D0), g vrai = 0.

Scores de sonde par cellule ~ N(mu_cellule, 1) + effet de tache (correlation rho = 0,3 entre cellules d'une tache) ;
D0 = mu_S - mu_H = d (separation de la sonde en ecarts types) ; SP et S de meme loi (aucun effet du plaidoyer).
Verdict « HC2 confirme » : intervalle par reechantillonnage des taches, niveau 1 - 0,10/m, dans [-0,10 ; 0,10].
Sortie : P(confirme) selon d, T (taches) et m (1 ou 2 sondes) ; demi-largeur mediane de l'intervalle.
Plus : demi-largeur predite par la methode delta, ET(g) ~ sqrt(2 (1 - rho)) / (d sqrt(T)), pour fixer l'effectif d'avance.
"""
import sys

import numpy as np


def main():
    rng = np.random.default_rng(np.random.SeedSequence(0x5C70).spawn(1)[0])
    R, B, rho = 400, 1000, 0.3
    print("d     T    m  | P(HC2 confirme)  demi-largeur mediane | demi-largeur delta (1,96 ou 2,24 x ET)")
    for d in (1.0, 2.0, 3.0, 5.0):
        for T in (30, 60, 120):
            for m in (1, 2):
                niv = 0.10 / m
                ok, hw = [], []
                for _ in range(R):
                    u = rng.normal(0, np.sqrt(rho), (T, 1))
                    e = rng.normal(0, np.sqrt(1 - rho), (T, 3))
                    H, S, SP = u[:, 0] + e[:, 0], d + u[:, 0] + e[:, 1], d + u[:, 0] + e[:, 2]
                    W = rng.multinomial(T, np.full(T, 1.0 / T), size=B) / T
                    g = -(W @ (SP - S)) / (W @ (S - H))
                    lo, hi = np.percentile(g, [100 * niv / 2, 100 * (1 - niv / 2)])
                    ok.append(lo >= -0.10 and hi <= 0.10)
                    hw.append((hi - lo) / 2)
                z = 1.645 if m == 1 else 1.96
                et = np.sqrt(2 * (1 - rho)) / (d * np.sqrt(T))
                print(f"{d:.1f}  {T:>4}  {m}  |  {np.mean(ok):.3f}            {np.median(hw):.3f}               |  {z * et:.3f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
