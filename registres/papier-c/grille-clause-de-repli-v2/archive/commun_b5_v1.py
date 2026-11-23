"""Outils communs de la contre-lecture « methode » du brouillon 5 du papier C (lentille 1). Aucune donnee lue.

Ecrit par le contre-lecteur neuf, independamment de `commun_v1.py` de la contre-lecture du brouillon 4 (non importe).

Loi jointe (brouillon 5, Metrique, points 8 et 8 bis) : minimiser sum_m sum_i (Y_im - g_m (c - X_i))^2 en c commun et
g_m par rang. Pour c fixe, g_m(c) = (c A_m - B_m) / (n c^2 - 2 c S1 + S2), avec A_m = sum_i Y_im, B_m = sum_i Y_im X_i,
S1 = sum_i X_i, S2 = sum_i X_i^2. La somme residuelle profilee vaut const - Q(c), Q(c) = (a c^2 - 2 b c + d) /
(n c^2 - 2 S1 c + S2), a = sum_m A_m^2, b = sum_m A_m B_m, d = sum_m B_m^2. Les points stationnaires de Q annulent
(b n - a S1) c^2 + (a S2 - d n) c + (d S1 - b S2) (derivation du contre-lecteur). On garde le meilleur point parmi les
racines interieures a [-30 ; 40] et les deux bords ; un maximum au bord est « degenere ».

Loi nette du temoin (point 8 bis) : Y = v_m - v_tau(m) ; X = v0bar + rho (v0 - v0bar), rho = cov(v0, wbar) / var(v0)
borne a [0,05 ; 1], wbar = moyenne des lectures du contenu sous tous les temoins retenus ; tout recalcule par tirage.
Les sommes sont additives par tache : le reechantillonnage par grappes de taches se fait par comptes multinomiaux.
"""
from statistics import NormalDist

import numpy as np

BORNES = (-30.0, 40.0)
ND = NormalDist()


def sommes_taches(Y, v0, wbar, tache, T):
    """Y : (n, k) ; v0, wbar : (n,) ; tache : (n,) entiers 0..T-1. Sommes suffisantes par tache."""
    k = Y.shape[1]
    bc = lambda w: np.bincount(tache, weights=w, minlength=T)
    return dict(
        n=np.bincount(tache, minlength=T).astype(float),
        s0=bc(v0), s00=bc(v0 * v0), sw=bc(wbar), s0w=bc(v0 * wbar),
        A=np.stack([bc(Y[:, m]) for m in range(k)], 1),
        B0=np.stack([bc(Y[:, m] * v0) for m in range(k)], 1),
    )


def agrege(s, W=None):
    """W None : somme des taches ; W (Bt, T) : comptes de reechantillonnage."""
    return {c: (v.sum(0) if W is None else W @ v) for c, v in s.items()}


def regresseur(s, calibre=True, rho_fixe=None):
    """Renvoie n, S1, S2, A, B (sommes en X) et rho, a partir des sommes agregees."""
    n = s["n"]
    vb = s["s0"] / n
    var = s["s00"] / n - vb ** 2
    if rho_fixe is not None:
        rho = np.full_like(vb, rho_fixe)
    elif calibre:
        cov = s["s0w"] / n - vb * (s["sw"] / n)
        rho = np.clip(cov / var, 0.05, 1.0)
    else:
        rho = np.ones_like(vb)
    S1 = n * vb
    S2 = n * vb ** 2 + rho ** 2 * (s["s00"] - n * vb ** 2)
    A = s["A"]
    B = vb[..., None] * A + rho[..., None] * (s["B0"] - vb[..., None] * A)
    return n, S1, S2, A, B, rho, vb


def loi_jointe(n, S1, S2, A, B):
    """Forme fermee. Renvoie c (borne), g (..., k), G (...), degenere (bool)."""
    a = (A * A).sum(-1)
    b = (A * B).sum(-1)
    d = (B * B).sum(-1)
    q2 = b * n - a * S1
    q1 = a * S2 - d * n
    q0 = d * S1 - b * S2
    Q = lambda c: (a * c * c - 2 * b * c + d) / (n * c * c - 2 * S1 * c + S2)
    disc = q1 * q1 - 4 * q2 * q0
    sq = np.sqrt(np.maximum(disc, 0.0))
    with np.errstate(divide="ignore", invalid="ignore"):
        r1 = (-q1 + sq) / (2 * q2)
        r2 = (-q1 - sq) / (2 * q2)
    cands = [np.full_like(a, BORNES[0]), np.full_like(a, BORNES[1]), r1, r2]
    vals = []
    for c in cands:
        ok = np.isfinite(c) & (c >= BORNES[0]) & (c <= BORNES[1]) & (disc >= 0)
        if c is cands[0] or c is cands[1]:
            ok = np.ones_like(a, dtype=bool)
        v = np.where(ok, Q(np.where(ok, c, 0.0)), -np.inf)
        vals.append(v)
    vals = np.stack(vals, 0)
    idx = vals.argmax(0)
    C = np.stack([np.where(np.isfinite(c), c, 0.0) for c in cands], 0)
    c = np.take_along_axis(C, idx[None, ...], 0)[0]
    deg = idx <= 1
    den = n * c * c - 2 * S1 * c + S2
    g = (c[..., None] * A - B) / den[..., None]
    return c, g, g.mean(-1), deg


def loi_grille(Y, X, pas=0.01):
    """Verification par grille, comme le texte (test de la forme fermee)."""
    best = None
    for c in np.arange(BORNES[0], BORNES[1] + pas / 2, pas):
        z = c - X
        g = (Y * z[:, None]).sum(0) / (z * z).sum()
        r = ((Y - z[:, None] * g[None, :]) ** 2).sum()
        if best is None or r < best[0]:
            best = (r, c, g)
    return best[1], best[2]


def comptes(rng, T, B):
    return rng.multinomial(T, np.full(T, 1.0 / T), size=B).astype(float)


def p_sup(ts, t0):
    """p(theta > t0) = (1 + #{theta* <= t0}) / (B + 1) (point 12)."""
    return (1 + (ts <= t0).sum(-1)) / (ts.shape[-1] + 1)


def p_inf(ts, t0):
    return (1 + (ts >= t0).sum(-1)) / (ts.shape[-1] + 1)


def holm(p):
    """p : (..., m) -> valeurs p ajustees de Holm."""
    p = np.asarray(p, float)
    o = np.argsort(p, -1)
    ps = np.take_along_axis(p, o, -1)
    m = p.shape[-1]
    adj = np.maximum.accumulate(ps * (m - np.arange(m)), axis=-1)
    adj = np.minimum(adj, 1.0)
    out = np.empty_like(adj)
    np.put_along_axis(out, o, adj, -1)
    return out


def phi(x):
    return np.vectorize(ND.cdf)(x)


def phiinv(p):
    p = np.clip(p, 1e-12, 1 - 1e-12)
    return np.vectorize(ND.inv_cdf)(p)


def p_bca_sup(ts, t_hat, t_jack, t0):
    """Valeur p BCa de theta > t0 (nul theta <= t0) : alpha tel que la borne basse BCa vaut t0."""
    B = ts.shape[-1]
    z0 = phiinv((ts < t_hat).sum(-1) / B + 0.5 * (ts == t_hat).sum(-1) / B)
    jm = t_jack.mean(-1, keepdims=True)
    num = ((jm - t_jack) ** 3).sum(-1)
    den = 6 * (((jm - t_jack) ** 2).sum(-1)) ** 1.5
    acc = np.where(den > 0, num / np.where(den > 0, den, 1.0), 0.0)
    G = (1 + (ts <= t0).sum(-1)) / (B + 1)
    w = phiinv(G) - z0
    za = w / (1 + acc * w) - z0
    return phi(za)


if __name__ == "__main__":
    rng = np.random.default_rng(np.random.SeedSequence(20261020).spawn(1)[0])
    for essai in range(6):
        n, k = 50, 3
        X = rng.normal(3, 1.4, n)
        c0 = rng.uniform(-3, 8)
        g0 = rng.uniform(0.1, 0.6, k)
        Y = (c0 - X)[:, None] * g0[None, :] + rng.normal(0, 0.4, (n, k))
        v0 = X
        s = agrege(sommes_taches(Y, v0, v0, np.arange(n), n))
        c, g, G, deg = loi_jointe(*regresseur(s, calibre=False)[:5])
        cg, gg = loi_grille(Y, X)
        print(f"essai {essai} : c forme fermee {float(c):.4f} ; grille {cg:.2f} ; g {np.round(g, 4)} ; grille {np.round(gg, 4)}")
        assert abs(float(c) - cg) < 0.011
    X = rng.normal(3, 1.4, 60)
    Y = 0.3 * (1.0 - X) + rng.normal(0, 0.3, 60)
    p, o = np.polyfit(X, Y, 1)
    s = agrege(sommes_taches(Y[:, None], X, X, np.arange(60), 60))
    c, g, G, deg = loi_jointe(*regresseur(s, calibre=False)[:5])
    print("k = 1 : forme fermee", float(c), "; -ordonnee/pente", -o / p)
    assert abs(float(c) + o / p) < 1e-8
    print("holm", holm(np.array([0.01, 0.04, 0.03, 0.2, 0.001])))
    print("TESTS OK")
