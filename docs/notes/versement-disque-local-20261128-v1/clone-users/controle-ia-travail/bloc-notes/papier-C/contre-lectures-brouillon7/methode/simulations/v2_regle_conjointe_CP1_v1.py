"""V2 : regle conjointe de C-P1 (Seuil, C-P1 du brouillon 7) sur la grille : k = 3 et 5, 45 et 60 taches, modeles S
(0,3 ; 0,6), D (0,16), melanges (0,3-0,08 ; 0,6-0,16), g = 0,10 et 0,20 ; niveau a la frontiere lambda = 0,5,
puissance a lambda = 1 et lambda = 0. Par couple juge x famille, sans Holm ni condition de famille positive (lecture la
plus severe pour le niveau). « vers la cible » : p(lambda > 0,5) <= 0,025 ; « vers la moyenne » : p(lambda < 0,5) <=
0,025 ; lectures cal, brut et conjointe (regle du texte). Erreur MC : ecart type entre essais de la moyenne des 15
couples / racine(R).
Usage : python3 -B v2_regle_conjointe_CP1_v1.py s0 sig kap g lam k T R B graine
"""
import sys
import time

import numpy as np

from commun_cb7_v1 import appariement, corpus_A, p_inf, p_sup, trois_lectures


def main():
    s0, sig, kap, g, lam = map(float, sys.argv[1:6])
    k, T, R, B, graine = map(int, sys.argv[6:11])
    rng = np.random.default_rng(np.random.SeedSequence([graine, k, T, int(1000 * s0), int(1000 * kap), int(1000 * g),
                                                        int(10 * lam), 2]))
    pairs = appariement([1, 8, 16] if k == 3 else [1, 4, 8, 12, 16])
    gains = np.array([g * np.ones(5)[:, None] * np.linspace(0.5, 1.5, k)[None, :]] * 3)
    res = {(r, d): [] for r in ("cal", "brut", "conj") for d in ("cible", "moy")}
    t0 = time.time()
    for _ in range(R):
        o, _ = trois_lectures(rng, corpus_A(rng, T), [(s0, sig, kap)] * 3, gains, lam, pairs, B, lam_aussi=True)
        v = {}
        for r in ("cal", "brut"):
            lb = np.moveaxis(o[r]["lamb"], 0, -1)
            v[(r, "cible")] = p_sup(lb, 0.5) <= 0.025
            v[(r, "moy")] = p_inf(lb, 0.5) <= 0.025
        for d in ("cible", "moy"):
            v[("conj", d)] = v[("cal", d)] & v[("brut", d)]
        for key in res:
            res[key].append(v[key].mean())
    print(f"# V2 s0 {s0} ; sig {sig} ; kap {kap} ; g {g} ; lambda {lam} ; k {k} ; T {T} ; R {R} ; B {B} ; graine {graine} ;"
          f" {time.time() - t0:.0f} s")
    for r in ("cal", "brut", "conj"):
        a, b = np.array(res[(r, "cible")]), np.array(res[(r, "moy")])
        print(f"  {r:5s} : P(vers la cible) {a.mean():.3f} ± {a.std(ddof=1) / np.sqrt(R):.3f} ;"
              f" P(vers la moyenne) {b.mean():.3f} ± {b.std(ddof=1) / np.sqrt(R):.3f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
