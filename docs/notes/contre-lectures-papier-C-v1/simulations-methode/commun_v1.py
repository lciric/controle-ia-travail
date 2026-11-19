"""Outils communs des simulations de la contre-lecture « methode » (brouillon 4 du papier C). Aucune donnee lue.

Loi jointe (metrique, point 8) : minimiser sum_m sum_i (D_im - g_m (c - v0_i))^2 en c commun et g_m par rang.
Forme fermee : pour w = (x, y), c = x / y, la somme residuelle profilee vaut const - (w' M w) / (w' N w), avec
M = sum_m [A_m, -B_m]' [A_m, -B_m], A_m = sum_i D_im, B_m = sum_i D_im v0_i, N = [[n, -S1], [-S1, S2]].
Le maximum du quotient de Rayleigh generalise donne c chapeau (vecteur propre du plus grand mu).
Les sommes sont additives par tache : le reechantillonnage par blocs se fait par comptes multinomiaux.
"""
import numpy as np

BORNES_C = (-30.0, 40.0)


def sommes_par_tache(D, v0, tache, T):
    """D : (n, k) ; v0 : (n,) ; tache : (n,) entiers 0..T-1. Renvoie les sommes suffisantes par tache."""
    k = D.shape[1]
    cnt = np.bincount(tache, minlength=T).astype(float)
    S1 = np.bincount(tache, weights=v0, minlength=T)
    S2 = np.bincount(tache, weights=v0 * v0, minlength=T)
    A = np.stack([np.bincount(tache, weights=D[:, m], minlength=T) for m in range(k)], axis=1)
    Bm = np.stack([np.bincount(tache, weights=D[:, m] * v0, minlength=T) for m in range(k)], axis=1)
    return dict(cnt=cnt, S1=S1, S2=S2, A=A, B=Bm)


def agrege(s, poids=None):
    """Somme des taches (poids None) ou combinaisons par comptes de reechantillonnage (poids : (Bt, T))."""
    if poids is None:
        return {k: v.sum(axis=0) for k, v in s.items()}
    return {k: poids @ v for k, v in s.items()}


def loi_jointe(s):
    """s : sommes agregees (scalaires ou lots). Renvoie c, g (..., k), Gbar, degenere (bool)."""
    cnt, S1, S2, A, Bm = s["cnt"], s["S1"], s["S2"], s["A"], s["B"]
    M11 = (A * A).sum(-1)
    M12 = -(A * Bm).sum(-1)
    M22 = (Bm * Bm).sum(-1)
    N11, N12, N22 = cnt, -S1, S2
    a = N11 * N22 - N12 ** 2
    b = -(M11 * N22 + M22 * N11 - 2 * M12 * N12)
    cc = M11 * M22 - M12 ** 2
    disc = np.maximum(b * b - 4 * a * cc, 0.0)
    mu = (-b + np.sqrt(disc)) / (2 * a)
    r1x, r1y = -(M12 - mu * N12), (M11 - mu * N11)
    r2x, r2y = (M22 - mu * N22), -(M12 - mu * N12)
    n1 = r1x ** 2 + r1y ** 2
    n2 = r2x ** 2 + r2y ** 2
    x = np.where(n1 >= n2, r1x, r2x)
    y = np.where(n1 >= n2, r1y, r2y)
    with np.errstate(divide="ignore", invalid="ignore"):
        c = x / y
    deg = ~np.isfinite(c) | (c < BORNES_C[0]) | (c > BORNES_C[1])
    cb = np.clip(np.where(np.isfinite(c), c, BORNES_C[1]), *BORNES_C)
    Q = cnt * cb ** 2 - 2 * cb * S1 + S2
    g = (cb[..., None] * A - Bm) / Q[..., None]
    return dict(c=cb, g=g, G=g.mean(-1), deg=deg, v0bar=S1 / cnt)


def loi_jointe_grille(D, v0, pas=0.01):
    """Verification par grille (comme le brouillon 4) : sert seulement de test de la forme fermee."""
    grille = np.arange(BORNES_C[0], BORNES_C[1] + pas / 2, pas)
    best = None
    for c in grille:
        z = c - v0
        g = (D * z[:, None]).sum(0) / (z * z).sum()
        r = ((D - z[:, None] * g[None, :]) ** 2).sum()
        if best is None or r < best[0]:
            best = (r, c, g)
    return best[1], best[2]


def comptes_bootstrap(rng, T, B):
    return rng.multinomial(T, np.full(T, 1.0 / T), size=B).astype(float)


def p_sup(theta_star, theta0):
    """p(theta > theta0) = (1 + #{theta* <= theta0}) / (B + 1) (metrique, point 12)."""
    B = theta_star.shape[-1]
    return (1 + (theta_star <= theta0).sum(-1)) / (B + 1)


def p_inf(theta_star, theta0):
    B = theta_star.shape[-1]
    return (1 + (theta_star >= theta0).sum(-1)) / (B + 1)


if __name__ == "__main__":
    # test de la forme fermee contre la grille
    rng = np.random.default_rng(1)
    for essai in range(5):
        n, k = 40, 3
        v0 = rng.normal(3, 1.4, n)
        c_vrai = rng.uniform(-2, 8)
        g_vrai = rng.uniform(0.1, 0.6, k)
        D = (c_vrai - v0)[:, None] * g_vrai[None, :] + rng.normal(0, 0.4, (n, k))
        s = agrege(sommes_par_tache(D, v0, np.arange(n), n))
        r = loi_jointe(s)
        cg, gg = loi_jointe_grille(D, v0)
        print(f"essai {essai} : c forme fermee {float(r['c']):.4f} ; c grille {cg:.2f} ; g {np.round(r['g'], 4)} ; g grille {np.round(gg, 4)}")
        assert abs(float(r["c"]) - cg) < 0.011
    # k = 1 : identite avec -ordonnee/pente des moindres carres
    v0 = rng.normal(3, 1.4, 50)
    D = 0.3 * (1.0 - v0) + rng.normal(0, 0.3, 50)
    p, o = np.polyfit(v0, D, 1)
    r = loi_jointe(agrege(sommes_par_tache(D[:, None], v0, np.arange(50), 50)))
    print("k=1 : forme fermee", float(r["c"]), "; -ordonnee/pente", -o / p)
    assert abs(float(r["c"]) + o / p) < 1e-8
    print("TESTS OK")
