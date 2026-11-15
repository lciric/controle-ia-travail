"""Méthodes (bras) des essais « projection d'information inverse » — v1. Chaque fonction rend log W aux 8 instants de T
(tableau de 8 valeurs) ; la promotion est lue par `commun.promue` (seuil log 20), sauf mention (Bonferroni : seuil log 160).
Notations : L (n, J, K) lois connues ; Q (n, K) loi de la carte (pari plein) ; y (n,) issues fraîches ; cA, cB, c4 cellules
des coupures de l'archive ; z (n, 2) traits ; g (n,) sous-population."""
import math

import numpy as np

import essai_projection_commun_v1 as cm

IT_PROJ = 300      # pas d'EM des projections (le certificat rend toute valeur valide ; le nombre de pas coûte en puissance)
IT_MV = 300        # pas d'EM des maximums de vraisemblance
IT_CHAUD = 150     # M3 : pas d'EM des projections par morceaux après le départ chaud (projection sans coupure du bloc)


def _cumul_blocs(loge_blocs):
    return np.cumsum(loge_blocs, axis=-1)


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


def proj_blocs_commun(L, Q, y, cells, C, it=IT_PROJ, diag=None):
    """Projection par blocs alignés sur T, famille « bruit commun », pour F familles (cells (F, n)) ; rend (F, 8)."""
    F = cells.shape[0]
    q = [(b, cells[f, a:e]) for f in range(F) for b, (a, e) in enumerate(cm.BLOCS)]
    loge = _blocs_projection(L, Q, y, q, C, it, diag).reshape(F, len(cm.BLOCS))
    return np.cumsum(loge, 1)


def m1_lin(m, diag=None):
    return proj_blocs_commun(m["L"], m["Q"], m["y"], np.zeros((1, cm.N), int), 1, diag=diag)[0]


def m2_f4(m, diag=None):
    return proj_blocs_commun(m["L"], m["Q"], m["y"], m["c4"][None], 4, diag=diag)[0]


def m2b_min_lin_A_B(m, diag=None):
    cells = np.stack([np.zeros(cm.N, int), m["cA"], m["cB"]])
    return proj_blocs_commun(m["L"], m["Q"], m["y"], cells, 2, diag=diag).min(0)


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


def m4_f4_horizon_fixe(m):
    """Projection à horizon fixe à chaque instant t (première partie du plan), famille F4 « bruit commun » ;
    lue au seuil de Bonferroni log(8/alpha)."""
    L, Q, y, c4 = m["L"], m["Q"], m["y"], m["c4"]
    lq = cm.log_q_issues(Q, y)
    out = []
    depart, it = None, IT_PROJ
    for t in cm.T:
        G, Ind = cm.tenseurs(L[:t])
        tau, v, u, _ = cm.em_commun(G, Ind, Q[:t], c4[None, :t], 4, it, depart=depart)
        depart, it = (0.9 * tau + 0.01, 0.9 * v + 0.1 / cm.J, 0.9 * u + 0.1 / cm.K), 150   # départ chaud à l'instant suivant
        P = cm.probas_commun(G, Ind, c4[None, :t], 4, (tau, v, u))
        c = cm.certificat_commun(G, Q[:t], P, c4[None, :t], 4)[0]
        lp = np.log(np.maximum(P[0, np.arange(t), y[:t]], cm.PLANCHER))
        out.append(float((lq[:t] - lp).sum() - t * math.log(max(1.0, c))))
    return np.array(out)


SEUIL_BONFERRONI = math.log(len(cm.T) / cm.ALPHA)


def _pas_a_pas(Gs, Q, y, it=400):
    """Projection de q_s sur l'enveloppe des composantes Gs[s] (S, K, V), instance par instance ; certificat par pas."""
    S, _, V = Gs.shape
    th = np.full((S, V), 1.0 / V)
    for _ in range(it):
        A = th[:, None, :] * Gs
        P = A.sum(-1)
        R = (A * (Q / np.maximum(P, cm.PLANCHER))[..., None]).sum(1)
        th = R / R.sum(-1, keepdims=True)
    P = np.einsum("sv,syv->sy", th, Gs)
    c = np.einsum("syv,sy->sv", Gs, Q / np.maximum(P, cm.PLANCHER)).max(-1)
    lp = np.log(np.maximum(P[np.arange(S), y], cm.PLANCHER))
    loge = cm.log_q_issues(Q, y) - lp - np.log(np.maximum(1.0, c))
    return np.cumsum(loge)[cm.T - 1], c


def m5_pas_a_pas_avec_bruit(m):
    return _pas_a_pas(cm.composantes(m["L"]), m["Q"], m["y"])[0]


def m6_pas_a_pas_enveloppe(m, diag=None):
    """Projection pas à pas sur l'enveloppe {L_1..L_4, uniforme} (poids libres à chaque pas), en minimum avec M1."""
    L = m["L"]
    Gs = np.concatenate([np.transpose(L, (0, 2, 1)), np.full((cm.N, cm.K, 1), 1.0 / cm.K)], -1)
    w, c = _pas_a_pas(Gs, m["Q"], m["y"])
    if diag is not None:
        diag.setdefault("certificat_pas_moins_1", []).extend((c - 1).tolist())
    return np.minimum(w, m1_lin(m))


def _mv_cellule(m, fin, it=IT_MV):
    Gf = cm.composantes(m["L"])[:fin]
    y = m["y"][:fin]
    G_obs = Gf[np.arange(fin), y][:, None, :]
    th, _ = cm.em_cellule(G_obs, np.ones((fin, 1)), m["c4"][None, :fin], 4, it)
    return th


def m7_en_ligne_certifie(m, diag=None):
    """Poids « bruit par cellule » appris sur le passé (maximum de vraisemblance sur les blocs précédents ; uniformes au
    premier bloc), gelés pour le bloc, divisés par le certificat exact du bloc."""
    Gf = cm.composantes(m["L"])
    Q, y, c4 = m["Q"], m["y"], m["c4"]
    lq = cm.log_q_issues(Q, y)
    out = []
    for b, (a, e) in enumerate(cm.BLOCS):
        th = np.full((1, 4, Gf.shape[-1]), 1.0 / Gf.shape[-1]) if a == 0 else _mv_cellule(m, a)
        P = cm.probas_cellule(Gf[a:e], c4[None, a:e], th)
        c = cm.certificat_cellule(Gf[a:e], Q[a:e], P, c4[None, a:e], 4)[0]
        S = e - a
        lp = np.log(np.maximum(P[0, np.arange(S), y[a:e]], cm.PLANCHER))
        out.append((lq[a:e] - lp).sum() - S * math.log(max(1.0, c)))
        if diag is not None:
            diag.setdefault("certificat_m7", []).append(c)
    return np.cumsum(out)


def m7b_en_ligne_lisse_certifie(m, beta=0.5, diag=None):
    """Comme M7, mais la loi gelée du bloc est le mélange (1 − β)·(poids appris sur le passé) + β·(projection de la
    carte sur la même famille, calculée sur le bloc) : un point de la famille (convexité) ; certificat exact du bloc."""
    Gf = cm.composantes(m["L"])
    Q, y, c4 = m["Q"], m["y"], m["c4"]
    lq = cm.log_q_issues(Q, y)
    out = []
    V = Gf.shape[-1]
    for b, (a, e) in enumerate(cm.BLOCS):
        th = np.full((1, 4, V), 1.0 / V) if a == 0 else _mv_cellule(m, a)
        thp, _ = cm.em_cellule(Gf[a:e], Q[a:e], c4[None, a:e], 4, IT_PROJ)
        th = (1 - beta) * th + beta * thp
        P = cm.probas_cellule(Gf[a:e], c4[None, a:e], th)
        c = cm.certificat_cellule(Gf[a:e], Q[a:e], P, c4[None, a:e], 4)[0]
        S = e - a
        lp = np.log(np.maximum(P[0, np.arange(S), y[a:e]], cm.PLANCHER))
        out.append((lq[a:e] - lp).sum() - S * math.log(max(1.0, c)))
        if diag is not None:
            diag.setdefault("certificat_m7b", []).append(c)
    return np.cumsum(out)


def m2c_f4_cellule(m, diag=None):
    """Projection par blocs sur F4 « bruit par cellule » (la famille des fiches), certificat exact par bloc."""
    Gf = cm.composantes(m["L"])
    Q, y, c4 = m["Q"], m["y"], m["c4"]
    lq = cm.log_q_issues(Q, y)
    out = []
    for (a, e) in cm.BLOCS:
        th, _ = cm.em_cellule(Gf[a:e], Q[a:e], c4[None, a:e], 4, IT_PROJ)
        P = cm.probas_cellule(Gf[a:e], c4[None, a:e], th)
        c = cm.certificat_cellule(Gf[a:e], Q[a:e], P, c4[None, a:e], 4)[0]
        S = e - a
        lp = np.log(np.maximum(P[0, np.arange(S), y[a:e]], cm.PLANCHER))
        out.append((lq[a:e] - lp).sum() - S * math.log(max(1.0, c)))
        if diag is not None:
            diag.setdefault("certificat_m2c_moins_1", []).append(c - 1)
    return np.cumsum(out)


def m8_moitie_certifiee(m, diag=None):
    """Poids « bruit par cellule » ajustés sur la première moitié, valeur e sur les blocs 5 à 8, chacun divisé par son
    certificat exact ; lus aux instants 125 à 200 (log W = 0 aux quatre premiers instants)."""
    Gf = cm.composantes(m["L"])
    Q, y, c4 = m["Q"], m["y"], m["c4"]
    lq = cm.log_q_issues(Q, y)
    th = _mv_cellule(m, cm.N // 2)
    out = [0.0] * 4
    for (a, e) in cm.BLOCS[4:]:
        P = cm.probas_cellule(Gf[a:e], c4[None, a:e], th)
        c = cm.certificat_cellule(Gf[a:e], Q[a:e], P, c4[None, a:e], 4)[0]
        S = e - a
        lp = np.log(np.maximum(P[0, np.arange(S), y[a:e]], cm.PLANCHER))
        out.append((lq[a:e] - lp).sum() - S * math.log(max(1.0, c)))
        if diag is not None:
            diag.setdefault("certificat_m8", []).append(c)
    return np.cumsum(out)


FRACTIONS = (0.25, 0.5, 0.75, 1.0)


def m9_fraction_prevue(m):
    """Alternative prévisible par bloc : q^λ = λ·q + (1 − λ)·m̂ (m̂ : marginale de Laplace des issues des blocs passés,
    gelée au début du bloc) ; projection de q^λ par bloc sur F4 « bruit commun » ; richesse = moyenne sur λ des processus."""
    L, Q, y, c4 = m["L"], m["Q"], m["y"], m["c4"]
    nb = len(cm.BLOCS)
    cum = []
    for lam in FRACTIONS:
        Qb = []
        for (a, e) in cm.BLOCS:
            cnt = np.bincount(y[:a], minlength=cm.K) + 0.5
            Qb.append(lam * Q[a:e] + (1 - lam) * (cnt / cnt.sum())[None])
        q = [(b, c4[a:e]) for b, (a, e) in enumerate(cm.BLOCS)]
        cum.append(np.cumsum(_blocs_projection(L, Q, y, q, 4, IT_PROJ, None, Qb=np.stack(Qb))))
    cum = np.array(cum)
    mx = cum.max(0)
    return mx + np.log(np.exp(cum - mx).mean(0))


# --- artefacts : les deux façons des fiches, sans correction ---------------------------------------------------------
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


# --- références : maximum de vraisemblance sur les tirages mêmes (valeur atteinte ; plus favorable que le certificat) ---
def _mv_commun_valeurs(L, y, cells, C, t, it=IT_MV):
    G, Ind = cm.tenseurs(L[:t], y[:t])
    return cm.em_commun(G, Ind, np.ones((t, 1)), cells[:, :t], C, it)[3]


def references(m, avec_v9=True):
    """R8 (membre linéaire), RLa (linéaire, A, B), RF4 (partition à 4 cellules de l'archive), R9 (linéaire,
    sous-population, toutes les coupures des deux traits sur les t premières instances : élagage par 25 pas puis 300 pas
    sur les 8 meilleures, valeur atteinte)."""
    L, Q, y, z, g = m["L"], m["Q"], m["y"], m["z"], m["g"]
    num = np.cumsum(cm.log_q_issues(Q, y))[cm.T - 1]
    lin = np.zeros((1, cm.N), int)
    d8, dLa, dF4, d9 = [], [], [], []
    for t in cm.T:
        v_lin = _mv_commun_valeurs(L, y, lin, 1, t)[0]
        vAB = _mv_commun_valeurs(L, y, np.stack([m["cA"], m["cB"]]), 2, t)
        v4 = _mv_commun_valeurs(L, y, m["c4"][None], 4, t)[0]
        d8.append(v_lin)
        dLa.append(max(v_lin, vAB.max()))
        dF4.append(v4)
        if avec_v9:
            cells = [g[None, :t]]
            for j in range(cm.D):
                zt = z[:t, j]
                coupes = np.sort(zt)[:-1]
                cells.append((zt[None, :] > coupes[:, None]).astype(int))
            cells = np.concatenate(cells, 0)
            full = np.zeros((cells.shape[0], cm.N), int)
            full[:, :t] = cells
            G, Ind = cm.tenseurs(L[:t], y[:t])
            tau, v, u, val = cm.em_commun(G, Ind, np.ones((t, 1)), cells, 2, 25, accelere=False)
            top = np.argsort(val)[-8:]
            *_, val2 = cm.em_commun(G, Ind, np.ones((t, 1)), cells[top], 2, IT_MV, depart=(tau[top], v[top], u[top]))
            d9.append(max(v_lin, float(val.max()), float(val2.max())))
    r = {"R8": num - np.array(d8), "RLa": num - np.array(dLa), "RF4": num - np.array(dF4)}
    if avec_v9:
        r["R9"] = num - np.array(d9)
    return r
