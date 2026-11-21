"""Idée 1.1 (préenregistrement scellé `3ffe1739…`) : extraits **recopiés octet pour octet** (corps des fonctions et
constantes, par analyse syntaxique) de `docs/notes/organisme-idees-juge-v1/correction-poids-v1/projection/essai_projection_methodes_v1.py`
(`29704896…`) : `IT_PROJ`, `IT_MV`, `IT_CHAUD` (nombres de pas gelés), `_blocs_projection` (optimiseur et certificat du bras
J9-P, forme d'origine, employée par l'essai d'égalité EP et par l'essai qui la compare à la forme scindée du module
`projection_bras_v1`), `m3_toutes_coupures` (référence de EP), `_mv_cellule`, `a1_en_ligne` et `a2_moitie` (témoins A1 et
A2, « fiches n° 14 et n° 0 sans correction »). Seul changement : la ligne d'import de `cm`, qui désigne la copie octet pour
octet `projection_commun_v1` (`1f4ada97…`). L'égalité de chaque corps avec l'original est éprouvée par un essai."""
import math

import numpy as np

from . import projection_commun_v1 as cm


IT_PROJ = 300


IT_MV = 300


IT_CHAUD = 150


def _blocs_projection(L, Q, y, cells_blocs, C, it=IT_PROJ, diag=None, Qb=None, chaud=False):
    """Projection de la carte sur une famille « bruit commun », pour une liste de questions (bloc, partition) traitées
    en un seul lot. cells_blocs : liste de (indice de bloc, cellules (S,)) ; rend log e de chaque question (certificat
    exact appliqué : division par max(1, c)^S). Qb : lois de numérateur par bloc (défaut : la carte)."""
    nb = len(cells_blocs)
    S = 25
    Gb = np.stack([np.transpose(L[a:e], (0, 2, 1)) for (a, e) in cm.BLOCS])          # (8, S, K, J)
    Qbl = np.stack([Q[a:e] for (a, e) in cm.BLOCS]) if Qb is None else Qb           # (8, S, K)
    yb = np.stack([y[a:e] for (a, e) in cm.BLOCS])
    ib = np.array([i for i, _ in cells_blocs])
    cells = np.stack([c for _, c in cells_blocs])
    G = Gb[ib]
    Ind = np.broadcast_to(np.eye(cm.K)[None, None], (nb, S, cm.K, cm.K))
    Wt = Qbl[ib]
    depart = None
    if chaud:
        # départ chaud : la projection sans coupure du même bloc (lot de 8), mêlée à 10 % de centre (reste intérieur)
        t0, v0, u0, _ = cm.em_commun(Gb, np.broadcast_to(np.eye(cm.K)[None, None], (8, S, cm.K, cm.K)), Qbl,
                                     np.zeros((8, S), int), 1, it)
        depart = (0.9 * t0[ib] + 0.01, 0.9 * np.repeat(v0[ib], C, 1) + 0.1 / cm.J, 0.9 * u0[ib] + 0.1 / cm.K)
        it = IT_CHAUD
    tau, v, u, _ = cm.em_commun(G, Ind, Wt, cells, C, it, depart=depart)
    P = cm.probas_commun(G, Ind, cells, C, (tau, v, u))
    c = cm.certificat_commun(G, Wt, P, cells, C)
    yy = yb[ib]
    lp = np.log(np.maximum(np.take_along_axis(P, yy[..., None], 2)[..., 0], cm.PLANCHER))
    lq = np.log(np.maximum(np.take_along_axis(Wt, yy[..., None], 2)[..., 0], cm.PLANCHER))
    if diag is not None:
        diag.setdefault("certificat_moins_1", []).extend((c - 1).tolist())
    return (lq - lp).sum(1) - S * np.log(np.maximum(1.0, c))


def m3_toutes_coupures(m, diag=None):
    """Projection par blocs sur : linéaire, sous-population, et chaque coupure z_j > c pour toute valeur c du plan
    (toutes les partitions à un niveau que le v9 parcourt sur le plan gelé) ; minimum des processus. Dans un bloc de 25,
    une coupure n'induit que 26 partitions (selon le nombre de points du bloc sous le seuil) : chacune est projetée une
    fois, puis chaque coupure globale additionne ses 8 blocs."""
    L, Q, y, z, g = m["L"], m["Q"], m["y"], m["z"], m["g"]
    nb = len(cm.BLOCS)
    q = []
    for b, (a, e) in enumerate(cm.BLOCS):
        q.append((b, np.zeros(e - a, int)))
        q.append((b, g[a:e]))
    for j in range(cm.D):
        for b, (a, e) in enumerate(cm.BLOCS):
            rang = np.argsort(np.argsort(z[a:e, j]))
            for i in range(1, 25):
                q.append((b, (rang >= i).astype(int)))
    loge = _blocs_projection(L, Q, y, q, 2, IT_PROJ, diag, chaud=True)
    lin = loge[0:2 * nb:2]
    sp_ = loge[1:2 * nb:2]
    proc = [np.cumsum(lin), np.cumsum(sp_)]
    k = 2 * nb
    for j in range(cm.D):
        tab = np.zeros((nb, 26))
        tab[:, 0] = lin
        tab[:, 25] = lin
        tab[:, 1:25] = loge[k:k + nb * 24].reshape(nb, 24)
        k += nb * 24
        coupes = np.sort(np.unique(z[:, j]))
        idx = np.stack([np.searchsorted(np.sort(z[a:e, j]), coupes, side="right") for (a, e) in cm.BLOCS], 1)
        proc.append(np.cumsum(tab[np.arange(nb)[None, :], idx], axis=1))
    return np.vstack([np.atleast_2d(p) for p in proc]).min(0)


def _mv_cellule(m, fin, it=IT_MV):
    Gf = cm.composantes(m["L"])[:fin]
    y = m["y"][:fin]
    G_obs = Gf[np.arange(fin), y][:, None, :]
    th, _ = cm.em_cellule(G_obs, np.ones((fin, 1)), m["c4"][None, :fin], 4, it)
    return th


def a1_en_ligne(m, eta):
    """argon-p2-01 : poids par cellule (4 cellules de l'archive), mis à jour par descente exponentielle après chaque
    épisode ; dénominateur = loi prédictive courante ; aucune correction."""
    Gf = cm.composantes(m["L"])
    Q, y, c4 = m["Q"], m["y"], m["c4"]
    V = Gf.shape[-1]
    w = np.full((4, V), 1.0 / V)
    s, lw = 0.0, np.empty(cm.N)
    for t in range(cm.N):
        c = c4[t]
        comp = Gf[t, y[t]]
        p = max(1e-12, float(w[c] @ comp))
        s += math.log(max(Q[t, y[t]], cm.PLANCHER)) - math.log(p)
        lw[t] = s
        w[c] *= np.exp(np.minimum(eta * comp / p, 50.0))
        w[c] /= w[c].sum()
    return lw[cm.T - 1]


def a2_moitie(m):
    """argon-p1-01 : poids par cellule ajustés par maximum de vraisemblance sur la première moitié ; valeur e sur la
    seconde, sans correction ; rend log W aux instants 125..200 (0 avant)."""
    Gf = cm.composantes(m["L"])
    Q, y, c4 = m["Q"], m["y"], m["c4"]
    th = _mv_cellule(m, cm.N // 2)
    h = cm.N // 2
    P = cm.probas_cellule(Gf[h:], c4[None, h:], th)[0]
    lw = np.cumsum(cm.log_q_issues(Q[h:], y[h:]) - np.log(np.maximum(P[np.arange(cm.N - h), y[h:]], 1e-12)))
    return np.concatenate([np.zeros(4), lw[cm.T[4:] - h - 1]])
