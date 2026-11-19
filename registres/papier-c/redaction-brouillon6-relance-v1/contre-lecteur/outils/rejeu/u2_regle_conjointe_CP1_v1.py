"""U2 : regle conjointe de C-P1 (brouillon 6, Seuil, C-P1 ; test du module du point 8 bis), avec un vrai
reechantillonnage par taches, cinq familles, temoins partages, k = 3, trois juges de meme modele.

Par couple juge x famille, sans Holm (lecture la plus severe pour le niveau), sans condition de famille positive :
« vers la cible » si p(lambda > 0,5) <= 0,025 ; « vers la moyenne » si p(lambda < 0,5) <= 0,025 ; sur la loi nette
calibree (cal), sans calibrage (brut, rho = 1), et aux deux (conj, regle du brouillon 6).
Erreur de Monte-Carlo : ecart type entre essais de la moyenne des 15 couples d'un essai, / racine(R).
Usage : python3 -B u2_regle_conjointe_CP1_v1.py MODELE s0 sig kap g lam T R B graine
"""
import sys
import time

import numpy as np

from commun_cb6_v1 import G_corpus, appariement, corpus_A, p_inf, p_sup


def main():
    nom = sys.argv[1]
    s0, sig, kap, g, lam = map(float, sys.argv[2:7])
    T, R, B, graine = map(int, sys.argv[7:11])
    rng = np.random.default_rng(np.random.SeedSequence([graine, T, R, int(1000 * s0), int(1000 * kap), int(1000 * g), int(10 * lam)]))
    pairs = appariement([1, 8, 16])
    gains = np.array([g * np.ones(5)[:, None] * np.array([0.5, 1.0, 1.5])[None, :]] * 3)
    t0 = time.time()
    res = {(r, d): [] for r in ("cal", "brut", "conj") for d in ("cible", "moy")}
    med = {"cal": [], "brut": []}
    for _ in range(R):
        o = G_corpus(rng, corpus_A(rng, T), [(s0, sig, kap)] * 3, gains, lam, pairs, B)
        v = {}
        for r in ("cal", "brut"):
            lb = o[r]["lamb"]
            v[(r, "cible")] = p_sup(np.moveaxis(lb, 0, -1), 0.5) <= 0.025
            v[(r, "moy")] = p_inf(np.moveaxis(lb, 0, -1), 0.5) <= 0.025
            med[r].append(np.median(o[r]["lam"]))
        for d in ("cible", "moy"):
            v[("conj", d)] = v[("cal", d)] & v[("brut", d)]
        for key in res:
            res[key].append(v[key].mean())
    print(f"# U2 {nom} : s0 {s0} ; sig {sig} ; kap {kap} ; g {g} ; lambda {lam} ; T {T} ; R {R} ; B {B} ; {time.time() - t0:.0f} s")
    print(f"  mediane lambda : calibree {np.median(med['cal']):+.3f} ; sans calibrage {np.median(med['brut']):+.3f}")
    for r in ("cal", "brut", "conj"):
        a = np.array(res[(r, "cible")])
        b = np.array(res[(r, "moy")])
        print(f"  {r:5s} : P(vers la cible) {a.mean():.3f} ± {a.std(ddof=1) / np.sqrt(R):.3f} ;"
              f" P(vers la moyenne) {b.mean():.3f} ± {b.std(ddof=1) / np.sqrt(R):.3f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
