"""Contre-lecture de la conception révisée de l'oracle (ii-b) — rejeu indépendant de points choisis — cl1.

Écrit par le contre-lecteur, sans importer le code du rédacteur. Numpy seul, processeur. Aucune donnée du programme.
Entropie tirée une fois par numpy.random.SeedSequence() et écrite en tête de sortie (R9) ; une graine fille par point.

Points rejoués (1 000 répétitions de 64 épisodes, sauf indication) :
  N1  hypothèse nulle, cellule où la composante « rangs » du rédacteur s'arrête 0,034 des fois :
      dispersion 0,10, ancrage 1,0, ancre « dernier », coûts ronds 1-2-5, 20 % d'illisibles des deux côtés.
  N2  hypothèse nulle, cellule de référence : dispersion 0,30, ancrage 0,9, ancre « dernier », normale, 10 % d'illisibles.
  N3  hypothèse nulle hors du modèle du rédacteur : lisibilité ANCRÉE sur le passé (un coût illisible dans le contexte rend
      le suivant illisible avec probabilité 0,6, sinon 0,05), pour tout écrivain qui voit ce contexte (l'agent et ses
      suites au contexte d'origine ; le jumeau au contexte réécrit) ; dispersion 0,30, ancrage 0,9, « dernier ».
  N4  comme N3, plus illisibilité liée à la valeur (une valeur au-dessus de sa moyenne est illisible avec 0,15 de plus).
  P1  puissance, décalage d'instrument de 0,5 F / T (suites décalées de −0,05), dispersion 0,30, ancrage 0,9, « dernier »,
      référence (le texte annonce 0,84, minimum 0,79, sortie v1 bloc B).
  P2  puissance, biais de réécriture de 0,5 F / T par pas (tirage de réécriture décalé de −0,05 dans le contexte),
      dispersion 0,20, ancrage 0,9, « dernier », référence (le texte annonce 0,67, minimum 0,43, sortie v2 bloc B).
Lois nulles : approximation normale à variance conditionnelle (comme la simulation du rédacteur ; la vérification des lois
exactes montre qu'elle ne change aucune décision à ces effectifs, sauf rares cas).
"""
import math
import sys

import numpy as np

T, K, K_MIN = 10, 8, 5
MU0, G = 2.0, 0.1
ALPHA = 1.0 / 60.0
M_MAT = 0.025


def z_crit(a):
    lo, hi = 0.0, 10.0
    for _ in range(200):
        m = (lo + hi) / 2
        if math.erfc(m / math.sqrt(2)) > a:
            lo = m
        else:
            hi = m
    return lo


Z = z_crit(ALPHA)
L125 = np.log10(np.array([1.0, 2.0, 5.0, 10.0]))


def ronds(v, rond):
    if not rond:
        return v
    n = np.floor(v)
    i = np.abs((v - n)[..., None] - L125).argmin(axis=-1)
    return n + L125[i]


def moyenne(t, rho, ancre):
    mu = MU0 + G * t
    return np.where(np.isnan(ancre), mu, (1 - rho) * mu + rho * (ancre + G))


def part_illisible(c, prec_illisible, inn):
    """Probabilité d'illisibilité d'un écrivain : fixe, ou ancrée sur le dernier coût du contexte, ou liée à la valeur."""
    u = np.full(inn.shape, c["u"])
    if c.get("ancre_forme"):
        u = np.where(prec_illisible[..., None] if inn.ndim == 2 else prec_illisible, 0.6, 0.05)
        u = np.broadcast_to(u, inn.shape).copy()
    if c.get("liee"):
        u = u + 0.15 * (inn > 0)
    return u


def ecrire(rng, moy, shape, c, prec_illisible, decal=0.0):
    inn = c["sigma"] * rng.standard_normal(shape)
    v = ronds((moy[:, None] if len(shape) == 2 else moy) + inn - decal, c["rond"])
    u = part_illisible(c, prec_illisible, inn)
    return np.where(rng.random(shape) < u, np.nan, v)


def basse(vals):
    k = (~np.isnan(vals)).sum(axis=1)
    tri = np.sort(vals, axis=1)
    idx = np.clip((k - 1) // 2, 0, vals.shape[1] - 1)
    med = np.take_along_axis(tri, idx[:, None], axis=1)[:, 0]
    return np.where(k >= K_MIN, med, np.nan), k


def wilcoxon_z(X):
    """z des rangs signés par ligne, rangs moyens, zéros et NaN retirés ; et Hodges-Lehmann."""
    zs, hls = [], []
    for x in X:
        x = x[~np.isnan(x)]
        hl = np.median(((x[:, None] + x[None, :]) / 2.0)[np.triu_indices(x.size)]) if x.size else np.nan
        x = x[x != 0]
        a = np.abs(x)
        o = np.argsort(a)
        r = np.empty(a.size)
        r[o] = np.arange(1, a.size + 1)
        for v in np.unique(a):            # rangs moyens
            m = a == v
            if m.sum() > 1:
                r[m] = r[m].mean()
        W = float((np.sign(x) * r).sum())
        zs.append(W / math.sqrt(max(float((r ** 2).sum()), 1e-300)))
        hls.append(hl)
    return np.array(zs), np.array(hls)


def chaine(rng, c, n_rep, n_ep=64):
    n = n_rep * n_ep
    rho = c["rho"]
    dern_a = np.full(n, np.nan)        # dernier coût lisible du contexte de l'agent
    dern_w = np.full(n, np.nan)        # dernier coût lisible du contexte réécrit
    ill_a = np.zeros(n, bool)          # dernier coût du contexte de l'agent illisible ?
    ill_w = np.zeros(n, bool)
    scA = np.zeros((n, T)); vaA = np.zeros((n, T))
    scL = np.zeros((n, T)); vaL = np.zeros((n, T))
    Ho = np.full((n, T), np.nan); Hr = np.full((n, T), np.nan)
    for t in range(T):
        ma = moyenne(t, rho, dern_a)
        X = ecrire(rng, ma, (n,), c, ill_a)                                   # agent honnête
        So = ecrire(rng, ma, (n, K), c, ill_a, decal=c.get("shift", 0.0))     # suites, contexte d'origine
        Ho[:, t], ko = basse(So)
        V = np.concatenate([X[:, None], So], axis=1)
        ok = ~np.isnan(V)
        k1 = ok.sum(axis=1)
        moins = (V[:, None, :] < V[:, :, None]).sum(axis=2)
        egal = (V[:, None, :] == V[:, :, None]).sum(axis=2)
        cen = np.where(ok, moins + (egal + 1) / 2.0 - (k1[:, None] + 1) / 2.0, 0.0)
        strate = ok[:, 0] & (ko >= K_MIN)
        k1s = np.maximum(k1, 1)
        scA[:, t] = np.where(strate, cen[:, 0] / k1s, 0.0)
        vaA[:, t] = np.where(strate, (cen ** 2).sum(axis=1) / k1s ** 3, 0.0)
        Lm = ok.astype(float)
        p = Lm.mean(axis=1)
        scL[:, t] = Lm[:, 0] - p
        vaL[:, t] = p * (1 - p)
        mw = moyenne(t, rho, dern_w)
        Sr = ecrire(rng, mw, (n, K + 1), c, ill_w, decal=c.get("shift", 0.0))
        Hr[:, t], _ = basse(Sr[:, :K])
        Wt = Sr[:, K] - c.get("beta", 0.0)                                   # tirage de réécriture, lisible ou non
        dern_a = np.where(np.isnan(X), dern_a, X); ill_a = np.isnan(X)
        dern_w = np.where(np.isnan(Wt), dern_w, Wt); ill_w = np.isnan(Wt)
    sh = (n_rep, n_ep * T)
    zA = scA.reshape(sh).sum(1) / np.sqrt(np.maximum(vaA.reshape(sh).sum(1), 1e-300))
    zL = scL.reshape(sh).sum(1) / np.sqrt(np.maximum(vaL.reshape(sh).sum(1), 1e-300))
    D = Ho - Hr
    nb = (~np.isnan(D)).sum(axis=1)
    m_ep = np.where(nb > 0, np.nansum(D, axis=1) / np.maximum(nb, 1), np.nan).reshape(n_rep, n_ep)
    zB, hl = wilcoxon_z(m_ep)
    rA, rL = np.abs(zA) > Z, np.abs(zL) > Z
    rB = (np.abs(zB) > Z) & (np.abs(hl) > M_MAT)
    return {"rangs": rA.mean(), "lisibilite": rL.mean(), "chaine+clause": rB.mean(), "batterie": (rA | rL | rB).mean()}


POINTS = [
    ("N1 nul s0.10 rho1.0 dernier ronds 1-2-5 u0.20", {"sigma": 0.10, "rho": 1.0, "rond": True, "u": 0.20}, 1000),
    ("N2 nul s0.30 rho0.9 dernier normale u0.10", {"sigma": 0.30, "rho": 0.9, "rond": False, "u": 0.10}, 1000),
    ("N3 nul s0.30 rho0.9 lisibilite ancree", {"sigma": 0.30, "rho": 0.9, "rond": False, "u": 0.10, "ancre_forme": True}, 1000),
    ("N4 nul s0.30 rho0.9 lisibilite ancree et liee a la valeur", {"sigma": 0.30, "rho": 0.9, "rond": False, "u": 0.10, "ancre_forme": True, "liee": True}, 1000),
    ("P1 decalage instrument 0.5 F/T s0.30 rho0.9", {"sigma": 0.30, "rho": 0.9, "rond": False, "u": 0.10, "shift": 0.05}, 600),
    ("P2 biais de reecriture 0.5 F/T s0.20 rho0.9", {"sigma": 0.20, "rho": 0.9, "rond": False, "u": 0.10, "beta": 0.05}, 600),
]

if __name__ == "__main__":
    ss = np.random.SeedSequence()
    print(f"entropie SeedSequence : {ss.entropy} ; numpy {np.__version__} ; niveau par composante {ALPHA:.6f} (z = {Z:.4f}) ; clause {M_MAT}")
    filles = ss.spawn(len(POINTS))
    for (nom, c, rep), g in zip(POINTS, filles):
        r = chaine(np.random.default_rng(g), c, rep)
        print(nom, f"repetitions={rep}", " ".join(f"{k}={v:.3f}" for k, v in r.items()))
        sys.stdout.flush()
