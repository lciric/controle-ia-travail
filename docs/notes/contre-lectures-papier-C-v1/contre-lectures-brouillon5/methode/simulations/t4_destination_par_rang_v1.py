"""T4 : reserve « destination heterogene dans la famille » (Metrique, point 10 ; Combinaisons). Le texte la lit sur les
c-chapeau_m de la loi SEPAREE (point 7 : Delta = v_m - v0 regresse sur v0, loi brute). Sous la regression vers la
moyenne de la loi brute (CR-methode-01), c_m brut est tire vers v0bar d'autant plus que g_m est petit : les rangs faible
et fort ont des destinations brutes differentes meme quand la destination vraie est commune.
Modele de S2 (bruit d'insertion sigma sur toutes les lectures, v0 compris) ; une famille, g_m = g (0,5 ; 1 ; 1,5) ;
destination commune c = 3 + lambda (0 - 3). Intervalles a 95 % par percentiles, tirages par taches (B = 1 000).
Lectures : P(intervalles des rangs 1 et 3 disjoints) sur la loi separee brute (texte) et sur la loi separee nette
(Delta-a_m sur X calibre, proposition).
"""
import sys

import numpy as np

from commun_b5_v1 import agrege, comptes, loi_jointe, regresseur, sommes_taches


def c_sep(s, W, cal, m):
    """c-chapeau de la loi separee du rang m (k = 1), estimation et tirages."""
    s1 = dict(s)
    s1["A"] = s["A"][:, [m]]
    s1["B0"] = s["B0"][:, [m]]
    ce = float(loi_jointe(*regresseur(agrege(s1), calibre=cal)[:5])[0])
    cb = loi_jointe(*regresseur(agrege(s1, W), calibre=cal)[:5])[0]
    return ce, np.percentile(cb, [2.5, 97.5])


def essai(rng, T, sigma, g, lam, B):
    u = rng.normal(0, 0.5, T)
    tache = np.repeat(np.arange(T), 2)
    vrai = np.tile([2.0, 4.0], T) + u[tache] + rng.normal(0, 0.8, 2 * T)
    n = 2 * T
    c = 3.0 + lam * (0.0 - 3.0)
    gm = g * np.array([0.5, 1.0, 1.5])
    v0 = vrai + rng.normal(0, sigma, n)
    vt = vrai[:, None] + rng.normal(0, sigma, (n, 16))
    vm = vrai[:, None] + (c - vrai)[:, None] * gm[None, :] + rng.normal(0, sigma, (n, 3))
    W = comptes(rng, T, B)
    wbar = vt.mean(1)
    out = {}
    s_brut = sommes_taches(vm - v0[:, None], v0, wbar, tache, T)
    s_net = sommes_taches(vm - vt[:, :3], v0, wbar, tache, T)
    for nom, s, cal in (("brut", s_brut, False), ("net", s_net, True)):
        c1, i1 = c_sep(s, W, cal, 0)
        c3, i3 = c_sep(s, W, cal, 2)
        out[nom] = dict(c1=c1, c3=c3, disj=bool(i1[1] < i3[0] or i3[1] < i1[0]))
    return out


def main():
    rng = np.random.default_rng(np.random.SeedSequence(0xB5C4).spawn(1)[0])
    B, R = 1000, 300
    print("T   sigma  g     lambda | brute (texte) : c1 med  c3 med  P(disjoints) | nette : c1 med  c3 med  P(disjoints)")
    for T in (45, 60):
        for sigma in (0.4, 0.6):
            for g in (0.10, 0.20):
                for lam in (1.0, 0.5):
                    L = [essai(rng, T, sigma, g, lam, B) for _ in range(R)]
                    m = lambda k, x: np.median([o[k][x] for o in L])
                    f = lambda k: np.mean([o[k]["disj"] for o in L])
                    print(f"{T:3d}  {sigma:.1f}  {g:.2f}  {lam:.1f}   |  {m('brut', 'c1'):+.2f}  {m('brut', 'c3'):+.2f}  {f('brut'):.3f}"
                          f"        |  {m('net', 'c1'):+.2f}  {m('net', 'c3'):+.2f}  {f('net'):.3f}")
                    sys.stdout.flush()
    return 0


if __name__ == "__main__":
    sys.exit(main())
