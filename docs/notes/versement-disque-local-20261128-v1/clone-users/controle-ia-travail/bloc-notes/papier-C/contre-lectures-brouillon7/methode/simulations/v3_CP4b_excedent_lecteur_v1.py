"""V3 (contre-lecture 10, point (v)) : C-P4b du brouillon 7 sur l'excedent du paragraphe a longueur fixe, des deux cotes,
dans le modele de S6 / S6c (contre-lecture methode du brouillon 4 ; fonctions `maxi`, `attention` importees sans
modification), sans aucune manipulation.

Jetons d'un episode : marque latente m (action du saboteur : part 0,10 ; action de l'honnete : 0) ; paragraphe : N1 (meme
part que l'action de la meme intention), N2 (neutre, part 0 pour les deux intentions). Aucune « trahison » : le
paragraphe ne porte aucun signal propre a la manipulation.
Score par jeton de l'auteur : N(0, 1) + 1,5 m (S6). Score par jeton du lecteur, sur les memes jetons (bruit propre) :
  L0 meme loi que l'auteur ; L1 reponse 0,8 a la marque ; L2 reponse 3,0 ; L3 reponse 0,6 etalee sur la marque et les
  quatre jetons qui suivent (lecture en contexte).
E = agregation des 32 premiers jetons du paragraphe - moyenne de l'agregation de 20 fenetres contigues de 32 jetons des
champs (memes fenetres des deux cotes) ; g_E = -moyenne_t (E_SP - E_HP) / D0, D0 = moyenne_t (S - H) sur les cellules
sans paragraphe, contenu entier, de chaque cote ; d = g_lecteur - g_auteur. Reechantillonnage des taches (B tirages),
m = 2 sondes (Bonferroni) : bornes a 1,25 % et 98,75 %. « confirmee » si borne basse > 0 ; « refutee » si borne haute < 0.
Usage : python3 -B v3_CP4b_excedent_lecteur_v1.py R B graine
"""
import sys
import time

import numpy as np

sys.path.insert(0, "/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/papier-C/contre-lectures/"
                   "simulations-methode")
from s6_agregation_maximum_v1 import attention, maxi  # noqa: E402

LSTAR, NF = 32, 20
LECTEURS = {"L0": (1.5, 1), "L1": (0.8, 1), "L2": (3.0, 1), "L3": (0.6, 5)}


def marques(rng, n, part):
    return (rng.random(n) < part).astype(float)


def score_lecteur(rng, m, beta, etal):
    if etal == 1:
        eff = m
    else:
        eff = np.convolve(m, np.ones(etal))[: len(m)]
    return rng.normal(0, 1, len(m)) + beta * eff


def episode(rng, sab, para, nul):
    la = max(40, int(rng.normal(120, 30)))
    mx = marques(rng, la, 0.10 if sab else 0.0)
    if not para:
        return mx, None
    lp = max(LSTAR, int(rng.normal(60, 15)))
    my = marques(rng, lp, (0.10 if sab else 0.0) if nul == "N1" else 0.0)
    return mx, my


def lire(rng, mx, my, cote, agr, fen):
    """Renvoie (agregation du contenu entier sans paragraphe) ou E (avec paragraphe)."""
    if cote == "A":
        sx = rng.normal(0, 1, len(mx)) + 1.5 * mx
        sy = None if my is None else rng.normal(0, 1, len(my)) + 1.5 * my
    else:
        beta, etal = LECTEURS[cote]
        if my is None:
            sx = score_lecteur(rng, mx, beta, etal)
            sy = None
        else:
            s = score_lecteur(rng, np.concatenate([mx, my]), beta, etal)
            sx, sy = s[: len(mx)], s[len(mx):]
    if sy is None:
        return agr(sx)
    ref = np.mean([agr(sx[d:d + LSTAR]) for d in fen])
    return agr(sy[:LSTAR]) - ref


def main():
    R, B, graine = map(int, sys.argv[1:4])
    rng = np.random.default_rng(np.random.SeedSequence([graine, 10, 5]))
    print(f"# V3 C-P4b sans manipulation ; R = {R} ; B = {B} ; graine {graine}")
    print("agreg.     nul  lecteur  T   | med g_auteur  med g_lecteur  med d | P(confirmee)  P(refutee)")
    t0 = time.time()
    for nom, agr in (("maximum", maxi), ("attention", attention)):
        for nul in ("N1", "N2"):
            for T in (30, 60):
                res = {c: [] for c in LECTEURS}
                for _ in range(R):
                    cells = {}
                    for t in range(T):
                        for cel, sab, para in (("H", 0, 0), ("S", 1, 0), ("HP", 0, 1), ("SP", 1, 1)):
                            mx, my = episode(rng, sab, para, nul)
                            fen = rng.integers(0, len(mx) - LSTAR + 1, NF) if para else None
                            for cote in ("A",) + tuple(LECTEURS):
                                cells.setdefault((cel, cote), []).append(lire(rng, mx, my, cote, agr, fen))
                    W = rng.multinomial(T, np.full(T, 1.0 / T), size=B) / T
                    a = {key: np.array(v) for key, v in cells.items()}

                    def gE(cote):
                        num = a[("SP", cote)] - a[("HP", cote)]
                        d0 = a[("S", cote)] - a[("H", cote)]
                        return -num.mean() / d0.mean(), -(W @ num) / (W @ d0)
                    gA, gAb = gE("A")
                    for c in LECTEURS:
                        gL, gLb = gE(c)
                        db = gLb - gAb
                        lo, hi = np.percentile(db, 1.25), np.percentile(db, 98.75)
                        res[c].append((gA, gL, gL - gA, lo > 0, hi < 0))
                for c in LECTEURS:
                    x = np.array(res[c], float)
                    print(f"{nom:9s}  {nul}   {c}      {T:>3} |   {np.median(x[:, 0]):+.3f}        {np.median(x[:, 1]):+.3f}"
                          f"      {np.median(x[:, 2]):+.3f} |  {x[:, 3].mean():.3f}         {x[:, 4].mean():.3f}")
    print(f"# {time.time() - t0:.0f} s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
