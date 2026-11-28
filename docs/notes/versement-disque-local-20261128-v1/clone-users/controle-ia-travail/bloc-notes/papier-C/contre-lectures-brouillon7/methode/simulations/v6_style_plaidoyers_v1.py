"""V6 (contre-lecture 10, point (viii)) : la difference des differences de l'excedent (g_trahison, HC2b ; brouillon 7,
TC.2, lecture (2)) ne retire le style que si les plaidoyers de l'honnete et du saboteur ont le meme style.

Modele de S6c (contre-lecture methode du brouillon 4 ; `episode`, `excedent`, `maxi`, `attention` importes sans
modification), nul N1 (aucune trahison : le paragraphe a la loi de l'action de la meme intention). Ecart de style : les
jetons du plaidoyer du saboteur portent un decalage moyen s (en ecarts types du score par jeton) que la sonde lit comme
le style, sans aucun signal de manipulation (s = 0 : nul de S6c). HC2b « confirmee » si la borne haute a 98,75 % (deux
sondes, Bonferroni) de g_trahison < 0 (reechantillonnage des taches, B tirages).
Usage : python3 -B v6_style_plaidoyers_v1.py R B graine
"""
import sys
import time

import numpy as np

sys.path.insert(0, "/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/papier-C/contre-lectures/"
                   "simulations-methode")
from s6_agregation_maximum_v1 import attention, maxi  # noqa: E402
from s6c_excedent_paragraphe_v1 import episode, excedent  # noqa: E402


def main():
    R, B, graine = map(int, sys.argv[1:4])
    rng = np.random.default_rng(np.random.SeedSequence([graine, 10, 8]))
    print(f"# V6 style des plaidoyers ; nul N1 de S6c ; R = {R} ; B = {B} ; graine {graine}")
    print("agreg.     s     T   | med g_trahison | P(HC2b confirmee)")
    t0 = time.time()
    for nom, agr in (("maximum", maxi), ("attention", attention)):
        for s in (0.0, 0.05, 0.10, 0.20):
            for T in (30, 60):
                out = []
                for _ in range(R):
                    H = np.array([agr(episode(rng, False, False, "N1")[0]) for _ in range(T)])
                    S = np.array([agr(episode(rng, True, False, "N1")[0]) for _ in range(T)])
                    EH = np.array([excedent(rng, *episode(rng, False, True, "N1"), agr) for _ in range(T)])
                    ES = []
                    for _ in range(T):
                        x, y = episode(rng, True, True, "N1")
                        ES.append(excedent(rng, x, y + s, agr))
                    ES = np.array(ES)
                    W = rng.multinomial(T, np.full(T, 1.0 / T), size=B) / T
                    g = -(W @ (ES - EH)) / (W @ (S - H))
                    out.append((-(ES - EH).mean() / (S - H).mean(), np.percentile(g, 98.75) < 0))
                a = np.array(out, float)
                print(f"{nom:9s}  {s:.2f}  {T:>3}  |  {np.median(a[:, 0]):+.3f}        |  {a[:, 1].mean():.3f}")
    print(f"# {time.time() - t0:.0f} s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
