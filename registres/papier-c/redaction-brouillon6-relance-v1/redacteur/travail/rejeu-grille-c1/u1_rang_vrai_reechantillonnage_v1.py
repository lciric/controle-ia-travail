"""U1 : statistiques de rang de l'option (A) de P-021, telles qu'ecrites au brouillon 6 (bloc P-021 ; configuration
brouillon 3, `stabilite_rang`), avec un vrai reechantillonnage par grappes (taches du corpus A, items du corpus B),
temoins partages par la regle, trois juges, cinq familles, k rangs.

Regles evaluees (« etablie ») :
  C-P3a : p exact <= 0,05 ET p par reechantillonnage centre <= 0,05 (W* sur les rangs de G* - G) ;
  C-P3b : p unilateral par reechantillonnage centre des deux corpus <= 0,05 (tau entre ecarts intra-famille) ;
  C-P3c : p exact <= 0,05 a quatre evaluateurs (deux gains d'ecart, bruit pur sous le nul ; G net des familles 1 et 4) ;
          a trois evaluateurs (sans P-020) : W = 1 ;
  chacune sur la loi nette calibree (cal), sans calibrage (brut, rho = 1), et aux deux lectures (conjointe).

Scenarios (nul = meme gain vrai chez les trois juges ; profil de famille commun (0,6 ; 0,8 ; 1 ; 1,2 ; 1,4)) :
  N0 aucune attaque, modele S homogene (s0 = sig = 0,4) ;
  N1 meme attaque (g 0,10 ; lambda 1), S homogene ;
  N2 meme attaque, S heterogene (sig = s0 = 0,3 / 0,45 / 0,6) : la lecture sans calibrage ordonne les juges ;
  N3 meme attaque, D heterogene (s0 = 0 ; kap = 0,04 / 0,10 / 0,16) : la lecture calibree ordonne les juges ;
  N4 meme attaque, mecanismes differents d'un juge a l'autre : juge 1 S (0,6), juge 2 mixte (s0 0,4 ; kap 0,08),
     juge 3 D (kap 0,16) : les deux lectures ordonnent les juges dans le meme sens ;
  N5 comme N4 avec g = 0,20 ;
  P3, P6 : puissance, S homogene, gains vrais 0,10 + delta (j - 1), delta = 0,03 et 0,06 (comme T2c).
Usage : python3 -B u1_rang_vrai_reechantillonnage_v1.py SCENARIO k T R B graine
"""
import sys
import time

import numpy as np

from commun_cb6_v1 import C_P3a, C_P3b, C_P3c, G_corpus, appariement, corpus_A, corpus_B, mc

PROFIL = np.array([0.6, 0.8, 1.0, 1.2, 1.4])
S04 = (0.4, 0.4, 0.0)
SCEN = {
    "N0": dict(juges=[S04] * 3, g=[0.0] * 3),
    "N1": dict(juges=[S04] * 3, g=[0.10] * 3),
    "N2": dict(juges=[(0.3, 0.3, 0.0), (0.45, 0.45, 0.0), (0.6, 0.6, 0.0)], g=[0.10] * 3),
    "N3": dict(juges=[(0.0, 0.4, 0.04), (0.0, 0.4, 0.10), (0.0, 0.4, 0.16)], g=[0.10] * 3),
    "N4": dict(juges=[(0.6, 0.6, 0.0), (0.4, 0.4, 0.08), (0.0, 0.4, 0.16)], g=[0.10] * 3),
    "N5": dict(juges=[(0.6, 0.6, 0.0), (0.4, 0.4, 0.08), (0.0, 0.4, 0.16)], g=[0.20] * 3),
    "P3": dict(juges=[S04] * 3, g=[0.07, 0.10, 0.13]),
    "P6": dict(juges=[S04] * 3, g=[0.04, 0.10, 0.16]),
}


def main():
    scen, k, T, R, B, graine = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])
    rng = np.random.default_rng(np.random.SeedSequence([graine, k, T, sum(map(ord, scen))]))
    idx = [1, 8, 16] if k == 3 else [1, 4, 8, 12, 16]
    pairs = appariement(idx)
    sc = SCEN[scen]
    gains = np.array([gj * PROFIL[:, None] * np.linspace(0.5, 1.5, k)[None, :] for gj in sc["g"]])
    cles = ["a_exact", "a_centre", "a", "b", "c4", "c3"]
    acc = {(r, c): [] for r in ("cal", "brut", "conj") for c in cles}
    t0 = time.time()
    for _ in range(R):
        oA = G_corpus(rng, corpus_A(rng, T), sc["juges"], gains, 1.0, pairs, B)
        oB = G_corpus(rng, corpus_B(rng), sc["juges"], gains, 1.0, pairs, B)
        bruit = rng.normal(0, 1, (2, 3))
        v = {}
        for r in ("cal", "brut"):
            w, pe, pc = C_P3a(oA[r]["G"], oA[r]["Gb"])
            t, pb = C_P3b(oA[r]["G"], oA[r]["Gb"], oB[r]["G"], oB[r]["Gb"])
            p4, p3 = C_P3c(oA[r]["G"], bruit)
            v[r] = dict(a_exact=pe <= 0.05, a_centre=pc <= 0.05, a=(pe <= 0.05) and (pc <= 0.05), b=pb <= 0.05,
                        c4=p4 <= 0.05, c3=p3 <= 0.05)
        v["conj"] = {c: v["cal"][c] and v["brut"][c] for c in cles}
        for r in v:
            for c in cles:
                acc[(r, c)].append(v[r][c])
    print(f"# U1 scenario {scen} ; k = {k} ; T = {T} taches (corpus B : 30 items) ; R = {R} essais ; B = {B} tirages ;"
          f" graine {graine} ; {time.time() - t0:.0f} s")
    print("lecture | C-P3a exact seul | C-P3a centre seul | C-P3a (A) | C-P3b (A) | C-P3c 4 ev. | C-P3c 3 ev.  (taux ± erreur MC)")
    for r in ("cal", "brut", "conj"):
        cells = []
        for c in cles:
            p = float(np.mean(acc[(r, c)]))
            cells.append(f"{p:.3f} ± {mc(p, R):.3f}")
        print(f"{r:5s}   | " + " | ".join(cells))
    return 0


if __name__ == "__main__":
    sys.exit(main())
