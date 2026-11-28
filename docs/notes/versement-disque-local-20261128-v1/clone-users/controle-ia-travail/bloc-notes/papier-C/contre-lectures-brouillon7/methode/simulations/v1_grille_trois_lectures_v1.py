"""V1 : bloc P-021 du brouillon 7 tel qu'ecrit (option (A) ; replis (B) et (C)), sur la grille de la clause de repli.

Pour chaque essai : corpus A (T taches, deux contenus H et S par tache) et corpus B (30 items), trois juges, cinq
familles, k rangs (indices 1, 8, 16 ou 1, 4, 8, 12, 16), temoins par la regle de la configuration brouillon 4 ; vrai
reechantillonnage par grappes (memes comptes pour les trois juges et les cinq familles d'un corpus) ; trois lectures de la
loi nette (cal ; brut, rho = 1 ; rr, rho/r recalcule dans chaque tirage).
Regles (« etablie ») : C-P3a p exact <= 0,05 et p centre <= 0,05 ; C-P3b p centre des deux corpus <= 0,05 ; C-P3c p
exact <= 0,05 a quatre evaluateurs (sous P-020) ou a trois (W = 1, sans P-020). Lecture jointe du texte : les trois
lectures (conj3) ; pour comparaison, les deux premieres (conj2).
C-P3c sous deux modeles des gains d'ecart (commun_cb7_v1) : « bruit » (U1) et « paragraphe » (compression du juge
etendue au paragraphe de l'agent).
Usage : python3 -B v1_grille_trois_lectures_v1.py SCENARIO k T R B graine
"""
import sys
import time

import numpy as np

from commun_cb7_v1 import (C_P3a, C_P3b, C_P3c, PROFIL, appariement, corpus_A, corpus_B, gains_ecart_paragraphe, mc,
                           seuil_clause, trois_lectures)

S = lambda s: (s, s, 0.0)  # noqa: E731
D = lambda k: (0.0, 0.4, k)  # noqa: E731
X = lambda s, k: (s, s, k)  # noqa: E731
SCEN = {
    # nuls : meme gain vrai chez les trois juges
    "Z0": dict(juges=[S(0.4)] * 3, g=[0.0] * 3, doc="aucune attaque, S 0,4 homogene"),
    "Z4": dict(juges=[S(0.6), X(0.4, 0.08), D(0.16)], g=[0.0] * 3, doc="aucune attaque, modeles de N4"),
    "N1": dict(juges=[S(0.4)] * 3, g=[0.10] * 3, doc="g 0,10, S 0,4 homogene"),
    "N2": dict(juges=[S(0.3), S(0.45), S(0.6)], g=[0.10] * 3, doc="g 0,10, S heterogene 0,3/0,45/0,6"),
    "N2f": dict(juges=[S(0.3), S(0.45), S(0.6)], g=[0.20] * 3, doc="g 0,20, S heterogene"),
    "N3": dict(juges=[D(0.04), D(0.10), D(0.16)], g=[0.10] * 3, doc="g 0,10, D heterogene 0,04/0,10/0,16"),
    "N3f": dict(juges=[D(0.04), D(0.10), D(0.16)], g=[0.20] * 3, doc="g 0,20, D heterogene"),
    "N4": dict(juges=[S(0.6), X(0.4, 0.08), D(0.16)], g=[0.10] * 3, doc="g 0,10, S 0,6 / melange 0,4-0,08 / D 0,16"),
    "N5": dict(juges=[S(0.6), X(0.4, 0.08), D(0.16)], g=[0.20] * 3, doc="g 0,20, comme N4"),
    "M6": dict(juges=[X(0.6, 0.16)] * 3, g=[0.20] * 3, doc="g 0,20, melange 0,6-0,16 homogene"),
    "N7": dict(juges=[S(0.6), X(0.3, 0.08), X(0.3, 0.16)], g=[0.20] * 3, doc="g 0,20, S 0,6 / melange 0,3-0,08 / melange 0,3-0,16"),
    # puissance
    "P3": dict(juges=[S(0.4)] * 3, g=[0.07, 0.10, 0.13], doc="puissance, S 0,4, gains 0,07/0,10/0,13"),
    "P6": dict(juges=[S(0.4)] * 3, g=[0.04, 0.10, 0.16], doc="puissance, S 0,4, gains 0,04/0,10/0,16"),
}
LECT = ("cal", "brut", "rr", "conj2", "conj3")
STATS = ("a", "b", "c4_bruit", "c3_bruit", "c4_par", "c3_par")


def main():
    scen, k, T, R, B, graine = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])
    ss = np.random.SeedSequence([graine, k, T, 8, sum(map(ord, scen)) * 131 + len(scen)])
    rng = np.random.default_rng(ss)
    pairs = appariement([1, 8, 16] if k == 3 else [1, 4, 8, 12, 16])
    sc = SCEN[scen]
    gains = np.array([gj * PROFIL[:, None] * np.linspace(0.5, 1.5, k)[None, :] for gj in sc["g"]])
    gp = np.array(sc["g"])
    acc = {(r, s): [] for r in LECT for s in STATS}
    t0 = time.time()
    for _ in range(R):
        cA = corpus_A(rng, T)
        oA, v0s = trois_lectures(rng, cA, sc["juges"], gains, 1.0, pairs, B)
        oB, _ = trois_lectures(rng, corpus_B(rng), sc["juges"], gains, 1.0, pairs, B)
        e_bruit = rng.normal(0, 1, (2, 3))
        e_par = gains_ecart_paragraphe(rng, cA, sc["juges"], v0s, gp)
        v = {}
        for r in ("cal", "brut", "rr"):
            G = oA[r]["G"]
            c4b, c3b = C_P3c(G, e_bruit)
            c4p, c3p = C_P3c(G, e_par)
            v[r] = dict(a=C_P3a(G, oA[r]["Gb"]), b=C_P3b(G, oA[r]["Gb"], oB[r]["G"], oB[r]["Gb"]),
                        c4_bruit=c4b, c3_bruit=c3b, c4_par=c4p, c3_par=c3p)
        v["conj2"] = {s: v["cal"][s] and v["brut"][s] for s in STATS}
        v["conj3"] = {s: v["conj2"][s] and v["rr"][s] for s in STATS}
        for r in LECT:
            for s in STATS:
                acc[(r, s)].append(v[r][s])
    print(f"# V1 scenario {scen} ({sc['doc']}) ; juges {sc['juges']} ; k = {k} ; T = {T} taches ; corpus B 30 items ;"
          f" R = {R} ; B = {B} ; graine {graine} ; {time.time() - t0:.0f} s")
    print(f"# seuil de la clause de repli a R = {R} : {seuil_clause(R):.4f}")
    print("lecture | C-P3a | C-P3b | C-P3c 4 ev. (bruit) | C-P3c 3 ev. (bruit) | C-P3c 4 ev. (paragraphe) | C-P3c 3 ev. (paragraphe)")
    for r in LECT:
        cells = []
        for s in STATS:
            p = float(np.mean(acc[(r, s)]))
            cells.append(f"{p:.3f} ± {mc(p, R):.3f}")
        print(f"{r:5s}   | " + " | ".join(cells))
    return 0


if __name__ == "__main__":
    sys.exit(main())
