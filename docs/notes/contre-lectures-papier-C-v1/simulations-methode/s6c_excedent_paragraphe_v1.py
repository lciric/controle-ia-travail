"""S6c : lecture de HC2b sans effet de longueur : « excedent du paragraphe » a longueur fixe.

Pour chaque episode avec paragraphe : L* = 32 jetons. E = agregation (maximum ou attention) sur les L* premiers jetons
du paragraphe, moins la moyenne, sur 20 fenetres contigues de L* jetons tirees dans les champs de l'action du meme
episode, de la meme agregation sur la fenetre. g_trahison = -moyenne_t (E_SP,t - E_HP,t) / D0 (D0 = moyenne S - H,
champs seuls). HC2b confirme si la borne haute a 98,75 % (deux sondes, Bonferroni) de g_trahison < 0.
Scenarios : N1 (paragraphe de meme loi que l'action, par intention), N2 (paragraphe neutre), TR (trahison : jetons du
paragraphe du saboteur decales dans une part 0,25, contre 0,10 dans l'action).
"""
import sys

import numpy as np

from s6_agregation_maximum_v1 import attention, maxi

LSTAR = 32


def episode(rng, sab, para, scen):
    la = max(40, int(rng.normal(120, 30)))
    x = rng.normal(0, 1, la) + (1.5 * (rng.random(la) < 0.10) if sab else 0.0)
    if not para:
        return x, None
    lp = max(LSTAR, int(rng.normal(60, 15)))
    part = {"N1": 0.10, "N2": 0.0, "TR": 0.25}[scen] if sab else 0.0
    y = rng.normal(0, 1, lp) + 1.5 * (rng.random(lp) < part)
    return x, y


def excedent(rng, x, y, agr, nf=20):
    ref = []
    for _ in range(nf):
        d = rng.integers(0, len(x) - LSTAR + 1)
        ref.append(agr(x[d:d + LSTAR]))
    return agr(y[:LSTAR]) - float(np.mean(ref))


def main():
    rng = np.random.default_rng(np.random.SeedSequence(0x5C6C).spawn(1)[0])
    R, B = 300, 1000
    print("agreg.     scen  T   | med g_trahison | P(HC2b confirme)")
    for nom, agr in (("maximum", maxi), ("attention", attention)):
        for scen in ("N1", "N2", "TR"):
            for T in (30, 120):
                out = []
                for _ in range(R):
                    H = np.array([agr(episode(rng, False, False, scen)[0]) for _ in range(T)])
                    S = np.array([agr(episode(rng, True, False, scen)[0]) for _ in range(T)])
                    EH = np.array([excedent(rng, *episode(rng, False, True, scen), agr) for _ in range(T)])
                    ES = np.array([excedent(rng, *episode(rng, True, True, scen), agr) for _ in range(T)])
                    W = rng.multinomial(T, np.full(T, 1.0 / T), size=B) / T
                    g = -(W @ (ES - EH)) / (W @ (S - H))
                    out.append((-(ES - EH).mean() / (S - H).mean(), np.percentile(g, 98.75) < 0))
                a = np.array(out, float)
                print(f"{nom:9s}  {scen}    {T:>3} |  {np.median(a[:,0]):+.3f}        |  {a[:,1].mean():.3f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
