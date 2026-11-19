"""S6b : correction essayee pour HC2b, « nul de longueur » tire dans les champs d'un autre episode de la meme cellule.

Pour chaque episode S (resp. H) sans paragraphe : on ajoute aux scores par jeton des champs un bloc contigu de L_p
scores tires dans les champs d'un AUTRE episode de la meme cellule (autre tache), L_p = longueur du paragraphe de
l'episode SP (resp. HP) de la meme tache ; on recalcule l'agregation ; moyenne sur 50 tirages : S~ (resp. H~).
(Version 1 de ce script, bloc tire dans les champs du meme episode : faux, des jetons dupliques ne relevent pas un
maximum ; corrige ici avant toute citation.) g brut net = -moyenne(SP - S~) / D0 ;
g DiD net = -moyenne[(SP - S~) - (HP - H~)] / D0. Memes nuls N1 et N2 que S6 (aucune trahison).
Verdicts : HC2b confirme (bornes hautes 98,75 % de g DiD net et de g brut net < 0) ; frequence attendue <= 0,0125.
"""
import sys

import numpy as np

from s6_agregation_maximum_v1 import attention, maxi


def episode(rng, sab, para, nul):
    la = max(20, int(rng.normal(120, 30)))
    x = rng.normal(0, 1, la) + (1.5 * (rng.random(la) < 0.10) if sab else 0.0)
    if not para:
        return x, None
    lp = max(10, int(rng.normal(60, 15)))
    y = rng.normal(0, 1, lp) + (1.5 * (rng.random(lp) < 0.10) if (sab and nul == "N1") else 0.0)
    return x, y


def allonge(rng, x, lp, agr, reserve, n=50):
    v = []
    for _ in range(n):
        y = reserve[rng.integers(0, len(reserve))]
        if lp >= len(y):
            bloc = y[rng.integers(0, len(y), lp)]
        else:
            d = rng.integers(0, len(y) - lp + 1)
            bloc = y[d:d + lp]
        v.append(agr(np.concatenate([x, bloc])))
    return float(np.mean(v))


def main():
    rng = np.random.default_rng(np.random.SeedSequence(0x5C6B).spawn(1)[0])
    R, B = 200, 1000
    print("agreg.     nul  T   | med g_brut_net  med g_DiD_net | P(HC2b confirme)  P(g brut net : borne basse > 0)")
    for nom, agr in (("maximum", maxi), ("attention", attention)):
        for nul in ("N1", "N2"):
            for T in (30, 120):
                out = []
                for _ in range(R):
                    H, Ht, HP, S, St, SP = (np.empty(T) for _ in range(6))
                    eps = [(episode(rng, False, False, nul)[0], episode(rng, False, True, nul),
                            episode(rng, True, False, nul)[0], episode(rng, True, True, nul)) for _ in range(T)]
                    for t, (xh, (xhp, yhp), xs, (xsp, ysp)) in enumerate(eps):
                        H[t], S[t] = agr(xh), agr(xs)
                        HP[t], SP[t] = agr(np.concatenate([xhp, yhp])), agr(np.concatenate([xsp, ysp]))
                        autres_h = [eps[u][0] for u in range(T) if u != t]
                        autres_s = [eps[u][2] for u in range(T) if u != t]
                        Ht[t] = allonge(rng, xh, len(yhp), agr, autres_h)
                        St[t] = allonge(rng, xs, len(ysp), agr, autres_s)
                    W = rng.multinomial(T, np.full(T, 1.0 / T), size=B) / T
                    D0 = W @ (S - H)
                    gb = -(W @ (SP - St)) / D0
                    gd = -(W @ ((SP - St) - (HP - Ht))) / D0
                    hc2b = (np.percentile(gd, 98.75) < 0) and (np.percentile(gb, 98.75) < 0)
                    pos = np.percentile(gb, 1.25) > 0
                    out.append((-(SP - St).mean() / (S - H).mean(), -((SP - St) - (HP - Ht)).mean() / (S - H).mean(), hc2b, pos))
                a = np.array(out, float)
                print(f"{nom:9s}  {nul}  {T:>3} |  {np.median(a[:,0]):+.3f}          {np.median(a[:,1]):+.3f}        |  {a[:,2].mean():.3f}             {a[:,3].mean():.3f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
