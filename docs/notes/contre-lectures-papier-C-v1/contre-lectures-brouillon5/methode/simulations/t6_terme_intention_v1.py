"""T6 : reserve « loi portee par le contraste d'intention » (Metrique, point 8 bis ; Combinaisons) : elle sort si le
terme d'intention (Delta-a = g_m (c - X) + beta_m 1[saboteur]) deplace c-chapeau de plus de la demi-largeur de son
intervalle. Ici AUCUN effet propre a l'intention (beta vrai = 0) ; on mesure la frequence de la reserve.
Modele de S2 (bruit d'insertion sigma = 0,4 ; temoins apparies) ; attaque lambda = 1, g = 0,10 (rangs 0,5 ; 1 ; 1,5) ;
deux ecarts honnete / saboteur : 2,0 (S2) et 3,5 (separation forte : v0 surtout porte par l'intention).
Loi avec terme d'intention : profil en c sur une grille de pas 0,02 dans [-30 ; 40], g_m et beta_m par moindres carres.
Intervalle de c-chapeau : percentiles, tirages par taches (B = 1 000) ; demi-largeur = (haut - bas) / 2.
"""
import sys

import numpy as np

from commun_b5_v1 import agrege, comptes, loi_jointe, regresseur, sommes_taches

GRILLE = np.arange(-30.0, 40.0001, 0.02)


def c_intention(Y, X, s):
    """Y (n, k), X (n,), s (n,) indicatrice saboteur. Profil en c (grille)."""
    z = GRILLE[:, None] - X[None, :]  # (G, n)
    Szz = (z * z).sum(1)
    Szs = (z * s[None, :]).sum(1)
    Sss = (s * s).sum()
    det = Szz * Sss - Szs ** 2
    rss = np.zeros(len(GRILLE))
    for m in range(Y.shape[1]):
        y = Y[:, m]
        Szy = z @ y
        Ssy = (s * y).sum()
        gm = (Sss * Szy - Szs * Ssy) / det
        bm = (Szz * Ssy - Szs * Szy) / det
        rss += (y * y).sum() - gm * Szy - bm * Ssy
    return GRILLE[np.argmin(rss)]


def essai(rng, T, ecart, B):
    u = rng.normal(0, 0.5, T)
    tache = np.repeat(np.arange(T), 2)
    sab = np.tile([0.0, 1.0], T)
    vrai = 3.0 - ecart / 2 + ecart * sab + u[tache] + rng.normal(0, 0.8, 2 * T)
    n = 2 * T
    c = 0.0
    gm = 0.10 * np.array([0.5, 1.0, 1.5])
    v0 = vrai + rng.normal(0, 0.4, n)
    vt = vrai[:, None] + rng.normal(0, 0.4, (n, 16))
    vm = vrai[:, None] + (c - vrai)[:, None] * gm[None, :] + rng.normal(0, 0.4, (n, 3))
    Y = vm - vt[:, :3]
    wbar = vt.mean(1)
    s = sommes_taches(Y, v0, wbar, tache, T)
    n_, S1, S2, A, Bm, rho, vb = regresseur(agrege(s))
    ce = float(loi_jointe(n_, S1, S2, A, Bm)[0])
    cb = loi_jointe(*regresseur(agrege(s, comptes(rng, T, B)))[:5])[0]
    lo, hi = np.percentile(cb, [2.5, 97.5])
    X = vb + rho * (v0 - vb)
    ci = c_intention(Y, X, sab)
    return dict(ce=ce, ci=ci, dl=(hi - lo) / 2, res=abs(ci - ce) > (hi - lo) / 2)


def main():
    rng = np.random.default_rng(np.random.SeedSequence(0xB5C6).spawn(1)[0])
    B, R = 1000, 300
    print("T   ecart H/S | c-chapeau med | c avec intention med | demi-largeur med | P(reserve, beta vrai = 0)")
    for T in (45, 60):
        for ecart in (2.0, 3.5):
            L = [essai(rng, T, ecart, B) for _ in range(R)]
            m = lambda x: np.median([o[x] for o in L])
            print(f"{T:3d}  {ecart:.1f}       |  {m('ce'):+.3f}       |  {m('ci'):+.3f}              |  {m('dl'):.3f}          |"
                  f"  {np.mean([o['res'] for o in L]):.3f}")
            sys.stdout.flush()
    return 0


if __name__ == "__main__":
    sys.exit(main())
