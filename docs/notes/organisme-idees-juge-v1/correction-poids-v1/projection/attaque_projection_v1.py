"""Attaque indépendante des méthodes « projection d'information inverse » — v1.

Mise au point exploratoire, aucune revendication. Processeur seul. Programme du réfutateur : il n'importe aucun
fichier de l'auteur pour ses propres calculs (les optimiseurs, les certificats, les mondes et les cartes sont écrits
ici). Quatre options appellent en plus le code de l'auteur, pour le comparer au mien : `taille … --auteur` et
`taille … --auteur-m3` (ses méthodes sur MES mondes), `memoire … --complet N` (ses M1, M2 et M3 sur mes mondes à
carte qui lit l'historique) et `reference` (encadrement de sa référence « façon v9 » sur SES mondes). Aucun fichier des
dossiers de copie du juge n'est exécuté ni importé ; la logique utile du juge (loi softmax, loi « sans remise », plan
de 200 instances à 2 traits gaussiens et 2 sous-populations, 8 instants de lecture, seuil 1/alpha, écart de
Frank-Wolfe du nul v9) est réécrite ici.

Sous-commandes (une simulation par appel, bornée à dix minutes par le lanceur) :
  taille CAS R0 R1 SORTIE [options]                         taux de promotion par méthode, R1 − R0 mondes ; options :
        --n N --J J (taille du plan, nombre de lois connues) ; --it N (pas d'optimiseur) ; --leger (familles « bruit
        commun » seulement : M1, M2, M2b, vraie famille) ; --sans-m4-m9 ; --seulement-m4-m9 ; --m3 (mon M3 complet) ;
        --auteur, --auteur-m3 (code de l'auteur sur les mêmes mondes)
  exact SORTIE                                              sup exact de l'espérance d'un bloc ; énumération exacte
  memoire REGLAGE SORTIE [--mondes N] [--complet N]         carte qui lit l'historique du bloc (hypothèse P4)
  amplification CAS E R SORTIE                              E engagements, R suites d'issues par engagement
  tirages R SORTIE [--m M]                                  lois connues seulement par tirages (P1, P2)
  reference CAS DOSE R0 R1 SORTIE                           encadrement de la référence « façon v9 » de l'auteur
  rejeu DOSSIER SORTIE                                      compare des sorties rejouées aux sorties scellées de l'auteur
  controle ORIGINE REJOUEE SORTIE                           compare deux sorties de taille de la même tranche
  fusion DOSSIER SORTIE                                     réunit les sorties en un seul fichier

Graines : numpy.random.SeedSequence(entropy=RACINE, spawn_key=(numéro de tâche, numéro de cas ou de réglage, r, …)) ;
écrites dans chaque sortie. Notations : L (n, J, K) lois connues aux instances ; Q (n, K) loi de la carte ; M (n, K) loi du monde ;
y (n,) issues ; blocs = intervalles entre instants de lecture.
"""
import argparse
import glob
import itertools
import json
import math
import os
import platform
import sys
import time

import numpy as np

RACINE = 2026111517
K = 3
ALPHA = 0.05
SEUIL = math.log(1.0 / ALPHA)
MINI = 1e-300
TACHES = {"taille": 1, "exact": 2, "memoire": 3, "tirages": 4, "reference": 5, "amplification": 6}


def graine(tache, *cle):
    return np.random.default_rng(np.random.SeedSequence(entropy=RACINE, spawn_key=(TACHES[tache],) + tuple(int(c) for c in cle)))


def clopper(k, n, niveau=0.95):
    from scipy.stats import beta
    a = (1 - niveau) / 2
    bas = 0.0 if k == 0 else float(beta.ppf(a, k, n - k + 1))
    haut = 1.0 if k == n else float(beta.ppf(1 - a, k + 1, n - k))
    return [round(bas, 5), round(haut, 5)]


# ----------------------------------------------------------------------------------------------------------------------
# lois, plan, archive
def loi_softmax(rng, z, force=1.5, biais=0.3, poids=None):
    W = rng.normal(0.0, force, (K, z.shape[1])) if poids is None else poids[0]
    b = rng.normal(0.0, biais, K) if poids is None else poids[1]
    s = z @ W.T + b
    e = np.exp(s - s.max(1, keepdims=True))
    return e / e.sum(1, keepdims=True), (W, b)


def aiguille(masque, a, b):
    return np.where(masque[:, None], a, b)


def engagement(rng, n=200, J=4, nb=8):
    """Plan gelé et archive : J − 2 lois softmax, puis deux lois si/sinon dont les coupures (A sur un trait, B sur
    l'autre) sont les coupures de l'archive."""
    z = rng.standard_normal((n, 2))
    g = rng.integers(0, 2, n)
    jA = int(rng.integers(0, 2))
    sA, sB = (float(v) for v in rng.uniform(-0.8, 0.8, 2))
    cA = (z[:, jA] > sA).astype(int)
    cB = (z[:, 1 - jA] > sB).astype(int)
    douces, params = [], []
    for _ in range(J - 2 + 4):
        p, par = loi_softmax(rng, z)
        douces.append(p)
        params.append(par)
    lois = douces[:J - 2] + [aiguille(cA == 1, douces[J - 2], douces[J - 1]), aiguille(cB == 1, douces[J], douces[J + 1])]
    return dict(z=z, g=g, jA=jA, sA=sA, sB=sB, cA=cA, cB=cB, c4=2 * cA + cB, L=np.stack(lois, 1), n=n, J=J, nb=nb,
                b=n // nb, params=params)


def tirer(rng, M):
    u = rng.random(M.shape[0])
    return np.minimum((u[:, None] > np.cumsum(M, 1)).sum(1), K - 1)


# ----------------------------------------------------------------------------------------------------------------------
# famille « bruit commun » : P(y | x) = (1 − τ)·Σ_j v[c(x), j]·L_j(y | x) + τ·u_y ; optimiseur général par lots
def em_commun(a, bb, w, cel, C, iters):
    """Maximise Σ_i w_i·log((1 − τ)·Σ_j v[cel_i, j]·a[i, j] + τ·Σ_k u_k·bb[i, k]) pour F problèmes à la fois.
    a (F, N, J), bb (F, N, Kb), w (F, N), cel (F, N). Espérance-maximisation ; après chaque pas, un pas allongé dans
    la même direction (x·(x'/x)^α, renormalisé) est essayé et gardé seulement s'il fait mieux que le pas simple ;
    α double après un succès, se divise par deux après un échec. Rend (tau, v, u)."""
    F, N, J = a.shape
    Kb = bb.shape[2]
    lig = np.arange(F)[:, None]
    oh = np.zeros((F, N, C))
    oh[lig, np.arange(N)[None, :], cel] = 1.0
    wt = w.sum(1)

    def lois(tau, v, u):
        cj = v[lig, cel] * a
        ck = bb * u[:, None, :]
        return cj, ck, (1.0 - tau)[:, None] * cj.sum(2) + tau[:, None] * ck.sum(2)

    def valeur(p):
        return (w * np.log(np.maximum(p, MINI))).sum(1)

    def pas(tau, v, u, cj, ck, p):
        gr = w / np.maximum(p, MINI)
        rj = (1.0 - tau)[:, None, None] * cj * gr[:, :, None]
        rk = tau[:, None] * np.einsum("fn,fnk->fk", gr, ck)
        nv = np.einsum("fnc,fnj->fcj", oh, rj)
        sv = nv.sum(2, keepdims=True)
        v1 = np.where(sv > 0, nv / np.where(sv > 0, sv, 1.0), v)
        sk = rk.sum(1)
        u1 = np.where(sk[:, None] > 0, rk / np.where(sk[:, None] > 0, sk[:, None], 1.0), u)
        return np.clip(sk / wt, 1e-12, 1.0 - 1e-12), v1, u1

    def allonge(x, x1, al):
        with np.errstate(divide="ignore", invalid="ignore", over="ignore"):
            lx = np.log(np.maximum(x, MINI)) + al * (np.log(np.maximum(x1, MINI)) - np.log(np.maximum(x, MINI)))
            lx = lx - lx.max(-1, keepdims=True)
            ex = np.exp(lx)
            return ex / ex.sum(-1, keepdims=True)

    tau = np.full(F, 0.2)
    v = np.full((F, C, J), 1.0 / J)
    u = np.full((F, Kb), 1.0 / Kb)
    al = np.full(F, 2.0)
    cj, ck, p = lois(tau, v, u)
    for _ in range(iters):
        t1, v1, u1 = pas(tau, v, u, cj, ck, p)
        c1 = lois(t1, v1, u1)
        duo = allonge(np.stack([tau, 1.0 - tau], 1), np.stack([t1, 1.0 - t1], 1), al[:, None])
        te = np.clip(duo[:, 0], 1e-12, 1.0 - 1e-12)
        ve = allonge(v, v1, al[:, None, None])
        ue = allonge(u, u1, al[:, None])
        ce = lois(te, ve, ue)
        f1, fe = valeur(c1[2]), valeur(ce[2])
        ok = np.isfinite(fe) & (fe > f1)
        tau = np.where(ok, te, t1)
        v = np.where(ok[:, None, None], ve, v1)
        u = np.where(ok[:, None], ue, u1)
        cj = np.where(ok[:, None, None], ce[0], c1[0])
        ck = np.where(ok[:, None, None], ce[1], c1[1])
        p = np.where(ok[:, None], ce[2], c1[2])
        al = np.where(ok, np.minimum(2.0 * al, 64.0), np.maximum(0.5 * al, 1.5))
    return tau, v, u


def loi_commun(Lb, cel, tau, v, u):
    """Lb (F, S, J, K) ; rend P (F, S, K)."""
    F = Lb.shape[0]
    vs = v[np.arange(F)[:, None], cel]
    return (1.0 - tau)[:, None, None] * np.einsum("fsj,fsjk->fsk", vs, Lb) + (tau[:, None] * u)[:, None, :]


def projeter_commun(Lb, Qb, cel, C, iters):
    """Projection d'information inverse de la carte sur la famille, pour F questions (bloc, partition) : maximise
    Σ_s Σ_y Qb[s, y]·log P(y | x_s). Rend P (F, S, K)."""
    F, S, J, _ = Lb.shape
    a = np.transpose(Lb, (0, 1, 3, 2)).reshape(F, S * K, J)
    bb = np.broadcast_to(np.tile(np.eye(K), (S, 1))[None], (F, S * K, K))
    tau, v, u = em_commun(a, bb, Qb.reshape(F, S * K), np.repeat(cel, K, axis=1), C, iters)
    return loi_commun(Lb, cel, tau, v, u)


def certificat_commun(Lb, Qb, P, cel, C):
    """c = max sur les sommets du polytope de (1/S)·Σ_s Σ_y P_sommet(y | x_s)·Q(y)/P(y). Sommets : une loi certaine δ_k
    (commune), ou une loi connue par cellule."""
    F, S = cel.shape
    r = Qb / np.maximum(P, MINI)
    aveugles = r.sum(1).max(1)
    m = np.einsum("fsk,fsjk->fsj", r, Lb)
    oh = np.zeros((F, S, C))
    oh[np.arange(F)[:, None], np.arange(S)[None, :], cel] = 1.0
    connues = np.einsum("fsc,fsj->fcj", oh, m).max(2).sum(1)
    return np.maximum(aveugles, connues) / S


def blocs_commun(e, Q, y, M, cel, C, iters, num=None):
    """Processus par blocs d'une famille « bruit commun » (cellules cel (n,)). Rend (log e de chaque bloc, logarithme
    de l'espérance exacte de chaque valeur e de bloc sous le monde M, certificats, P). num : numérateur par bloc."""
    nb, b, J = e["nb"], e["b"], e["J"]
    Lb = e["L"].reshape(nb, b, J, K)
    Qp = Q.reshape(nb, b, K)
    Qn = Qp if num is None else num
    cb = cel.reshape(nb, b)
    P = projeter_commun(Lb, Qn, cb, C, iters)
    return _valeurs_blocs(Qn, P, y.reshape(nb, b), M.reshape(nb, b, K), certificat_commun(Lb, Qn, P, cb, C)) + (P,)


def _valeurs_blocs(Qn, P, yb, Mb, c):
    S = Qn.shape[1]
    r = Qn / np.maximum(P, MINI)
    obs = np.take_along_axis(r, yb[:, :, None], 2)[:, :, 0]
    pen = S * np.log(np.maximum(1.0, c))
    loge = np.log(np.maximum(obs, MINI)).sum(1) - pen
    lesp = np.log(np.maximum((Mb * r).sum(2), MINI)).sum(1) - pen
    return loge, lesp, c


# ----------------------------------------------------------------------------------------------------------------------
# famille des fiches (« bruit par cellule ») et mélanges généraux : un simplexe par groupe
def em_melange(a, w, grp, G, iters, theta0=None):
    """Maximise Σ_i w_i·log(Σ_v θ[grp_i, v]·a[i, v]) ; a (N, V) ; rend θ (G, V). Même schéma que `em_commun` :
    espérance-maximisation, pas allongé gardé seulement s'il fait mieux."""
    N, V = a.shape
    H = np.zeros((G, N))
    H[grp, np.arange(N)] = 1.0
    wg = H @ w
    plein = wg[:, None] > 0
    th = np.full((G, V), 1.0 / V) if theta0 is None else np.array(theta0, dtype=float)
    al = np.full(G, 2.0)

    def valeur(t):
        return H @ (w * np.log(np.maximum((t[grp] * a).sum(1), MINI)))

    for _ in range(iters):
        t = th[grp] * a
        nt = H @ (t * (w / np.maximum(t.sum(1), MINI))[:, None])
        t1 = np.where(plein, nt / np.where(plein, wg[:, None], 1.0), th)
        with np.errstate(divide="ignore", invalid="ignore", over="ignore"):
            lx = np.log(np.maximum(th, MINI)) + al[:, None] * (np.log(np.maximum(t1, MINI)) - np.log(np.maximum(th, MINI)))
            ex = np.exp(lx - lx.max(1, keepdims=True))
            te = ex / ex.sum(1, keepdims=True)
        ok = valeur(te) > valeur(t1)
        th = np.where(ok[:, None], te, t1)
        al = np.where(ok, np.minimum(2.0 * al, 64.0), np.maximum(0.5 * al, 1.5))
    return th


def composantes(L):
    """(n, J + K, K) : les lois connues puis les lois certaines."""
    n = L.shape[0]
    return np.concatenate([L, np.broadcast_to(np.eye(K)[None], (n, K, K))], 1)


def certificat_cellules(Gb, Qn, P, cel, C):
    """Gb (S, V, K), Qn, P (S, K), cel (S,) : c = (1/S)·Σ_cellules max_v Σ_{s de la cellule} Σ_y G_v(y)·Q(y)/P(y)."""
    r = Qn / np.maximum(P, MINI)
    m = np.einsum("sk,svk->sv", r, Gb)
    tot = np.zeros((C, m.shape[1]))
    np.add.at(tot, cel, m)
    return float(tot.max(1).sum() / len(cel))


def proj_cellules(Gb, Qn, cel, C, iters):
    S, V, _ = Gb.shape
    a = np.transpose(Gb, (0, 2, 1)).reshape(S * K, V)
    return em_melange(a, Qn.reshape(S * K), np.repeat(cel, K), C, iters)


def mv_cellules(G, y, cel, C, iters):
    """Maximum de vraisemblance des poids par cellule sur des issues observées."""
    return em_melange(G[np.arange(len(y)), :, y], np.ones(len(y)), cel, C, iters)


def un_bloc_cellules(Gb, Qn, th, yb, Mb, cel, C):
    P = np.einsum("sv,svk->sk", th[cel], Gb)
    c = certificat_cellules(Gb, Qn, P, cel, C)
    loge, lesp, _ = _valeurs_blocs(Qn[None], P[None], yb[None], Mb[None], np.array([c]))
    return float(loge[0]), float(lesp[0]), c


# ----------------------------------------------------------------------------------------------------------------------
# les méthodes (mes écritures), sur un monde
FRACTIONS = (0.25, 0.5, 0.75, 1.0)


def evaluer(e, Q, y, M, avec_m3=False, it=60, it_m3=60, vraie=None, leger=False, sans_m4_m9=False):
    """Rend {méthode: (log W aux instants, seuil, plus grand log d'espérance exacte d'un bloc sous le monde)}.
    `vraie` = (genre, trait, seuil) : la famille du v9 qui contient le monde, quand il y en a une."""
    n, nb, b, J, L, z = e["n"], e["nb"], e["b"], e["J"], e["L"], e["z"]
    T = np.arange(b, n + 1, b)
    Lb, Qb, yb, Mb = L.reshape(nb, b, J, K), Q.reshape(nb, b, K), y.reshape(nb, b), M.reshape(nb, b, K)
    lq = np.log(np.maximum(Q[np.arange(n), y], MINI))
    res = {}
    # un seul lot pour les familles « bruit commun » : linéaire, 4 cellules, coupure A, coupure B, sous-population,
    # et la vraie coupure du monde s'il y en a une
    fam = {"lin": np.zeros(n, int), "f4": e["c4"], "A": e["cA"], "B": e["cB"], "g": e["g"]}
    if vraie is not None and vraie[0] == "coupure":
        fam["vraie"] = (z[:, vraie[1]] > vraie[2]).astype(int)
    noms = list(fam)
    rep = len(noms)
    cel = np.concatenate([fam[k].reshape(nb, b) for k in noms])
    Lr, Qr = np.tile(Lb, (rep, 1, 1, 1)), np.tile(Qb, (rep, 1, 1))
    P = projeter_commun(Lr, Qr, cel, 4, it)
    lo, le, _ = _valeurs_blocs(Qr, P, np.tile(yb, (rep, 1)), np.tile(Mb, (rep, 1, 1)), certificat_commun(Lr, Qr, P, cel, 4))
    bl = {k: (lo[i * nb:(i + 1) * nb], le[i * nb:(i + 1) * nb]) for i, k in enumerate(noms)}
    lin, elin = bl["lin"]
    res["M1"] = (np.cumsum(lin), SEUIL, float(elin.max()))
    res["M2"] = (np.cumsum(bl["f4"][0]), SEUIL, float(bl["f4"][1].max()))
    res["M2b"] = (np.minimum(np.minimum(np.cumsum(lin), np.cumsum(bl["A"][0])), np.cumsum(bl["B"][0])), SEUIL,
                  float(min(elin.max(), bl["A"][1].max(), bl["B"][1].max())))
    if vraie is not None:
        v = bl[{"lin": "lin", "sous_pop": "g", "coupure": "vraie"}[vraie[0]]]
        # processus de la vraie famille du monde : il majore M3 trajectoire par trajectoire
        res["M3_borne_vraie_famille"] = (np.cumsum(v[0]), SEUIL, float(v[1].max()))
    if leger:      # seulement les familles « bruit commun » du premier lot (et M3 si demandé)
        if avec_m3:
            res["M3"] = (m3(e, Q, y, M, lin, elin, bl["g"][0], it_m3), SEUIL, float("nan"))
        return res
    if not sans_m4_m9:
        res.update(_m4_m9(e, Q, y, M, it))

    # M5 : pas à pas avec les lois certaines. L'enveloppe d'une instance est tout le simplexe : la projection de la carte
    # est la carte elle-même, le certificat vaut 1, chaque facteur vaut 1 (calcul exact, sans optimiseur)
    res["M5"] = (np.zeros(nb), SEUIL, 0.0)
    # M6 : pas à pas sur l'enveloppe des lois connues et de l'uniforme, en minimum avec M1
    comp = np.concatenate([L, np.full((n, 1, K), 1.0 / K)], 1)
    th = em_melange(np.transpose(comp, (0, 2, 1)).reshape(n * K, J + 1), Q.reshape(n * K), np.repeat(np.arange(n), K), n, 150)
    P6 = np.einsum("sv,svk->sk", th, comp)
    r6 = Q / np.maximum(P6, MINI)
    cs = np.einsum("sk,svk->sv", r6, comp).max(1)
    pas = np.log(np.maximum(r6[np.arange(n), y], MINI)) - np.log(np.maximum(1.0, cs))
    esp = float((np.log(np.maximum((M * r6).sum(1), MINI)) - np.log(np.maximum(1.0, cs))).max())
    w6 = np.cumsum(pas)[T - 1]
    res["M6_pas_seul"] = (w6, SEUIL, esp)
    res["M6"] = (np.minimum(w6, np.cumsum(lin)), SEUIL, min(esp, float(elin.max())))
    # famille des fiches : M2c, M7, M7b, M8 et les deux artefacts A1, A2
    G = composantes(L)
    V = J + K
    c4 = e["c4"]
    bloc_de = np.repeat(np.arange(nb), b)
    thp = em_melange(np.transpose(G, (0, 2, 1)).reshape(n * K, V), Q.reshape(n * K), np.repeat(bloc_de * 4 + c4, K), nb * 4,
                     it).reshape(nb, 4, V)
    idx = np.concatenate([np.arange(i * b) for i in range(1, nb)])
    grp = np.concatenate([(i - 1) * 4 + c4[:i * b] for i in range(1, nb)])
    thm = em_melange(G[idx, :, y[idx]], np.ones(len(idx)), grp, (nb - 1) * 4, 2 * it).reshape(nb - 1, 4, V)
    thm = np.concatenate([np.full((1, 4, V), 1.0 / V), thm])           # premier bloc : poids uniformes
    th_moitie = thm[nb // 2]                                           # ajustés sur la première moitié
    w2c, w7, w7b, w8 = [], [], [], [0.0] * (nb // 2)
    x2c, x7, x7b, x8 = [], [], [], []
    for i in range(nb):
        sl = slice(i * b, (i + 1) * b)
        arg, fin = (G[sl], Q[sl]), (y[sl], M[sl], c4[sl], 4)
        a_, b_, _ = un_bloc_cellules(*arg, thp[i], *fin)
        w2c.append(a_); x2c.append(b_)
        a_, b_, _ = un_bloc_cellules(*arg, thm[i], *fin)
        w7.append(a_); x7.append(b_)
        a_, b_, _ = un_bloc_cellules(*arg, 0.5 * thm[i] + 0.5 * thp[i], *fin)
        w7b.append(a_); x7b.append(b_)
        if i >= nb // 2:
            a_, b_, _ = un_bloc_cellules(*arg, th_moitie, *fin)
            w8.append(a_); x8.append(b_)
    res["M2c"] = (np.cumsum(w2c), SEUIL, max(x2c))
    res["M7"] = (np.cumsum(w7), SEUIL, max(x7))
    res["M7b"] = (np.cumsum(w7b), SEUIL, max(x7b))
    res["M8"] = (np.cumsum(w8), SEUIL, max(x8))
    # A2 : poids ajustés sur la première moitié, rapport sur la seconde, sans correction
    h = n // 2
    Ph = np.einsum("sv,svk->sk", th_moitie[c4[h:]], G[h:])
    rh = Q[h:] / np.maximum(Ph, 1e-12)
    la2 = np.cumsum(np.log(np.maximum(rh[np.arange(n - h), y[h:]], MINI)))
    esp_a2 = float(np.log(np.maximum((M[h:] * rh).sum(1), MINI)).sum())    # log E[W final | première moitié], exact
    a2 = np.concatenate([np.zeros(nb // 2), la2[T[nb // 2:] - h - 1]])
    res["A2_instants"] = (a2, SEUIL, esp_a2)
    fin2 = np.full(nb, -1e300)
    fin2[-1] = a2[-1]
    res["A2_fin"] = (fin2, SEUIL, esp_a2)
    # A1 : poids par cellule mis à jour en ligne par descente exponentielle, sans correction
    for eta in (0.05, 0.2):
        wts = np.full((4, V), 1.0 / V)
        tot, lw, cumul = 0.0, np.empty(n), 0.0
        for t in range(n):
            c = c4[t]
            pred = wts[c] @ G[t]
            cumul += math.log(max(float((M[t] * Q[t] / np.maximum(pred, 1e-12)).sum()), MINI))
            py = max(float(pred[y[t]]), 1e-12)
            tot += lq[t] - math.log(py)
            lw[t] = tot
            wts[c] = wts[c] * np.exp(np.minimum(eta * G[t, :, y[t]] / py, 50.0))
            wts[c] /= wts[c].sum()
        # `cumul` : somme, le long de la trajectoire, des log d'espérance conditionnelle exacte de chaque facteur
        res[f"A1_pas{eta}"] = (lw[T - 1], SEUIL, cumul)
    if avec_m3:
        res["M3"] = (m3(e, Q, y, M, lin, elin, bl["g"][0], it_m3), SEUIL, float("nan"))
    return res


def _m4_m9(e, Q, y, M, it):
    """M4 (horizon fixe à chaque instant, seuil de Bonferroni) et M9 (fraction gelée par bloc)."""
    n, nb, b, J, L = e["n"], e["nb"], e["b"], e["J"], e["L"]
    T = np.arange(b, n + 1, b)
    Lb, Qb, yb, Mb = L.reshape(nb, b, J, K), Q.reshape(nb, b, K), y.reshape(nb, b), M.reshape(nb, b, K)
    res = {}
    # M4 : les instances au-delà de t ont un poids nul dans la projection de l'instant t
    masque = (np.arange(n)[None, :] < T[:, None]).astype(float)
    c4n = np.broadcast_to(e["c4"][None], (nb, n))
    P4 = projeter_commun(np.broadcast_to(L[None], (nb, n, J, K)), Q[None] * masque[:, :, None], c4n, 4, it)
    w4, e4h = [], []
    for i, t in enumerate(T):
        Lt, Qt, ct, Pt = L[None, :t], Q[None, :t], e["c4"][None, :t], P4[i:i + 1, :t]
        a4, b4, _ = _valeurs_blocs(Qt, Pt, y[None, :t], M[None, :t], certificat_commun(Lt, Qt, Pt, ct, 4))
        w4.append(float(a4[0]))
        e4h.append(float(b4[0]))
    res["M4"] = (np.array(w4), math.log(nb / ALPHA), float(max(e4h)))
    # M9 : fraction gelée par bloc (marginale de Laplace des blocs passés), moyenne sur quatre fractions
    num = np.empty((len(FRACTIONS), nb, b, K))
    for i in range(nb):
        cpt = np.bincount(y[:i * b], minlength=K) + 0.5
        for f, lam in enumerate(FRACTIONS):
            num[f, i] = lam * Qb[i] + (1 - lam) * (cpt / cpt.sum())[None]
    nf = len(FRACTIONS)
    numr = num.reshape(nf * nb, b, K)
    L9, c9 = np.tile(Lb, (nf, 1, 1, 1)), np.tile(e["c4"].reshape(nb, b), (nf, 1))
    P9 = projeter_commun(L9, numr, c9, 4, it)
    lo9, le9, _ = _valeurs_blocs(numr, P9, np.tile(yb, (nf, 1)), np.tile(Mb, (nf, 1, 1)), certificat_commun(L9, numr, P9, c9, 4))
    traj = np.cumsum(lo9.reshape(nf, nb), 1)
    mx = traj.max(0)
    res["M9"] = (mx + np.log(np.exp(traj - mx).mean(0)), SEUIL, float(le9.max()))
    return res


def m3(e, Q, y, M, lin, elin, sp, it):
    """Minimum des processus par blocs sur : linéaire, sous-population, chaque coupure z_j > c pour toute valeur c du
    plan. Dans un bloc, une coupure sur un trait n'induit que b + 1 partitions (nombre de points du bloc sous le seuil)."""
    nb, b, J, z, L = e["nb"], e["b"], e["J"], e["z"], e["L"]
    Lb, Qb = L.reshape(nb, b, J, K), Q.reshape(nb, b, K)
    yb, Mb = y.reshape(nb, b), M.reshape(nb, b, K)
    procs = [np.cumsum(lin), np.cumsum(sp)]
    for j in range(2):
        zb = z[:, j].reshape(nb, b)
        rang = np.argsort(np.argsort(zb, 1), 1)                       # rang de chaque point dans son bloc
        ks = np.arange(1, b)
        cel = (rang[:, None, :] >= ks[None, :, None]).astype(int)      # (nb, b − 1, b) : cellule 1 = au-dessus
        F = nb * (b - 1)
        Lr, Qr, cr = np.repeat(Lb, b - 1, axis=0), np.repeat(Qb, b - 1, axis=0), cel.reshape(F, b)
        P = projeter_commun(Lr, Qr, cr, 2, it)
        lo, _, _ = _valeurs_blocs(Qr, P, np.repeat(yb, b - 1, 0), np.repeat(Mb, b - 1, 0), certificat_commun(Lr, Qr, P, cr, 2))
        tab = np.empty((nb, b + 1))
        tab[:, 0] = lin
        tab[:, b] = lin
        tab[:, 1:b] = lo.reshape(nb, b - 1)
        seuils = np.unique(z[:, j])
        sous = (zb[None, :, :] <= seuils[:, None, None]).sum(2)        # (coupures, nb) : points du bloc sous le seuil
        procs.append(np.cumsum(tab[np.arange(nb)[None, :], sous], 1))
    return np.vstack([np.atleast_2d(p) for p in procs]).min(0)


# ----------------------------------------------------------------------------------------------------------------------
# cas : (monde, carte) ; étiquettes = familles qui contiennent le monde
def membre(L, cel, pi, rho):
    return np.einsum("sj,sjk->sk", pi[cel], L) + rho[None]


def projection_globale(e, Q, cel, C, it=600):
    """Membre de la famille le plus proche de la carte sur tout le plan (un point de la famille : le pire monde nul)."""
    L = e["L"]
    P = projeter_commun(L[None], Q[None], cel[None], C, it)[0]
    return P / P.sum(1, keepdims=True)


def carte_voisine(rng, e, dose):
    """Loi neuve : la première loi softmax de l'archive, poids déplacés de `dose` dans une direction au hasard."""
    W, b = e["params"][0]
    D = rng.standard_normal(W.shape)
    D -= D.mean(0, keepdims=True)
    return loi_softmax(rng, e["z"], poids=(W + dose * D, b))[0]


def seuil_hors(rng, e, j):
    ref = e["sA"] if j == e["jA"] else e["sB"]
    while True:
        s = float(rng.uniform(-1.0, 1.0))
        if abs(s - ref) >= 0.25:
            return s


CAS = ["copie_lin", "copie_extreme", "copie_bord_loi", "copie_aveugle", "copie_coupure_archive", "copie_coupure_hors",
       "copie_sous_pop", "copie_coupure_bruit", "copie_deux_niveaux", "pire_lin_d03", "pire_lin_d06", "pire_f4_d06",
       "pire_coupure_hors_d06", "pire_sous_pop_d06", "pire_bloc_lin_d03", "pire_bloc_lin_d06", "pire_bloc_f4_d06",
       "surconfiante", "audacieuse", "carte_autre_membre", "carte_neuve_monde_coupure", "pire_bloc_lin_d10"]


def construire(rng, e, cas):
    L, n, J, z = e["L"], e["n"], e["J"], e["z"]
    zero = np.zeros(n, int)
    a, bq = (int(v) for v in rng.choice(J - 2, 2, replace=False))
    carte, vraie, tags = None, None, set()
    if cas == "copie_lin":
        th = rng.dirichlet(np.ones(J + K))
        M = membre(L, zero, th[None, :J], th[J:]); tags = {"lin"}; vraie = ("lin", 0, 0.0)
    elif cas == "copie_extreme":
        pi = np.zeros((1, J)); rho = np.zeros(K)
        pi[0, int(rng.integers(0, J))] = 0.999; rho[int(rng.integers(0, K))] = 0.001
        M = membre(L, zero, pi, rho); tags = {"lin"}; vraie = ("lin", 0, 0.0)
    elif cas == "copie_bord_loi":
        M = L[:, int(rng.integers(0, J))].copy(); tags = {"lin", "env"}; vraie = ("lin", 0, 0.0)
    elif cas == "copie_aveugle":
        M = np.broadcast_to(rng.dirichlet(np.full(K, 0.3)) * 0.98 + 0.02 / K, (n, K)).copy(); tags = {"lin"}; vraie = ("lin", 0, 0.0)
    elif cas in ("copie_coupure_archive", "carte_autre_membre", "carte_neuve_monde_coupure"):
        M = aiguille(e["cA"] == 1, L[:, a], L[:, bq]); tags = {"A", "env"}; vraie = ("coupure", e["jA"], e["sA"])
        if cas == "carte_autre_membre":
            carte = L[:, a].copy()
        if cas == "carte_neuve_monde_coupure":
            carte = carte_voisine(rng, e, 0.5)
    elif cas == "copie_coupure_hors":
        j = int(rng.integers(0, 2)); s = seuil_hors(rng, e, j)
        M = aiguille(z[:, j] > s, L[:, a], L[:, bq]); tags = {"coupure", "env"}; vraie = ("coupure", j, s)
    elif cas == "copie_sous_pop":
        M = aiguille(e["g"] == 1, L[:, a], L[:, bq]); tags = {"sous_pop", "env"}; vraie = ("sous_pop", 0, 0.0)
    elif cas == "copie_coupure_bruit":
        rho = 0.25 * rng.dirichlet(np.ones(K))
        M = 0.75 * aiguille(e["cA"] == 1, L[:, a], L[:, bq]) + rho[None]; tags = {"A"}; vraie = ("coupure", e["jA"], e["sA"])
    elif cas == "copie_deux_niveaux":
        hA, hB = e["cA"] == 1, e["cB"] == 1
        M = aiguille(hA, aiguille(hB, L[:, a], L[:, bq]), aiguille(hB, L[:, bq], L[:, a])); tags = {"f4", "env"}
    elif cas.startswith("pire_bloc_"):
        dose = int(cas[-2:]) / 10.0
        carte = carte_voisine(rng, e, dose)
        cel, C = (zero, 1) if "_lin_" in cas else (e["c4"], 4)
        nb, b = e["nb"], e["b"]
        P = projeter_commun(L.reshape(nb, b, J, K), carte.reshape(nb, b, K), cel.reshape(nb, b), C, 600).reshape(n, K)
        M = P; tags = {"bloc_lin"} if C == 1 else {"bloc_f4"}; vraie = ("lin", 0, 0.0) if C == 1 else None
    elif cas.startswith("pire_"):
        dose = int(cas[-2:]) / 10.0
        carte = carte_voisine(rng, e, dose)
        if "_lin_" in cas:
            M = projection_globale(e, carte, zero, 1); tags = {"lin"}; vraie = ("lin", 0, 0.0)
        elif "_f4_" in cas:
            M = projection_globale(e, carte, e["c4"], 4); tags = {"f4"}
        elif "_coupure_hors_" in cas:
            j = int(rng.integers(0, 2)); s = seuil_hors(rng, e, j)
            M = projection_globale(e, carte, (z[:, j] > s).astype(int), 2); tags = {"coupure"}; vraie = ("coupure", j, s)
        else:
            M = projection_globale(e, carte, e["g"], 2); tags = {"sous_pop"}; vraie = ("sous_pop", 0, 0.0)
    elif cas in ("surconfiante", "audacieuse"):
        th = rng.dirichlet(np.ones(J + K))
        M = membre(L, zero, th[None, :J], th[J:]); tags = {"lin"}; vraie = ("lin", 0, 0.0)
        if cas == "surconfiante":
            carte = M ** 2.0
        else:   # carte très tranchée, sans lien avec le monde : gros gains rares
            carte = loi_softmax(rng, z, force=4.0)[0] * 0.98 + 0.02 / K
    else:
        raise ValueError(cas)
    M = M / M.sum(1, keepdims=True)
    Q = M.copy() if carte is None else carte / carte.sum(1, keepdims=True)
    return M, Q, tags, vraie


def dans_la_classe(methode, tags):
    lin, A, f4 = "lin" in tags, "A" in tags, "f4" in tags
    bl, bf = "bloc_lin" in tags, "bloc_f4" in tags
    v9 = lin or A or "coupure" in tags or "sous_pop" in tags
    quatre = lin or A or f4
    if methode == "M1":
        return lin or bl
    if methode in ("M2", "M9", "M2c", "M7", "M7b", "M8"):
        return quatre or bl or bf
    if methode in ("M4", "A1_pas0.05", "A1_pas0.2", "A2_fin", "A2_instants"):
        return quatre
    if methode == "M2b":
        return lin or A or bl
    if methode in ("M3", "M3_borne_vraie_famille"):
        return v9 or bl
    if methode == "M5":
        return True
    if methode == "M6":
        return "env" in tags or lin or bl
    if methode == "M6_pas_seul":
        return "env" in tags
    raise ValueError(methode)


# ----------------------------------------------------------------------------------------------------------------------
def charger_auteur():
    ici = os.path.dirname(os.path.abspath(__file__))
    if ici not in sys.path:
        sys.path.insert(0, ici)
    import essai_projection_cas_v1 as cs
    import essai_projection_commun_v1 as cm
    import essai_projection_methodes_v1 as me
    return cs, cm, me


def cmd_taille(a):
    if os.path.exists(a.sortie):
        raise SystemExit("sortie existante, aucun écrasement")
    i_cas = CAS.index(a.cas)
    auteur = charger_auteur() if a.auteur else None
    auteur_m3 = charger_auteur() if a.auteur_m3 else None
    depasse, exces = [], []
    if (auteur or auteur_m3) and (a.n != 200 or a.J != 4):
        raise SystemExit("le code de l'auteur est figé à n = 200 et J = 4")
    noms_auteur = {"M1": "m1_lin", "M2": "m2_f4", "M2b": "m2b_min_lin_A_B", "M4": "m4_f4_horizon_fixe",
                   "M5": "m5_pas_a_pas_avec_bruit", "M6": "m6_pas_a_pas_enveloppe", "M2c": "m2c_f4_cellule",
                   "M7": "m7_en_ligne_certifie", "M7b": "m7b_en_ligne_lisse_certifie", "M8": "m8_moitie_certifiee",
                   "M9": "m9_fraction_prevue"}
    t0 = time.time()
    compte, pire, lwmax, ecarts, compte_aut, viol = {}, {}, {}, {}, {}, 0
    tags0 = None
    for r in range(a.r0, a.r1):
        rng = graine("taille", i_cas, r, a.n, a.J)
        e = engagement(rng, a.n, a.J)
        M, Q, tags, vraie = construire(rng, e, a.cas)
        tags0 = tags
        y = tirer(rng, M)
        if a.seulement_m4_m9:
            res = _m4_m9(e, Q, y, M, a.it)
        else:
            res = evaluer(e, Q, y, M, avec_m3=a.m3, vraie=vraie, it=a.it, it_m3=a.it, leger=a.leger, sans_m4_m9=a.sans_m4_m9)
        if a.m3 and "M3_borne_vraie_famille" in res:
            # mon M3 doit rester sous le processus de la vraie famille (même famille, deux calculs : tolérance 0,05)
            exces.append(float(np.max(res["M3"][0] - res["M3_borne_vraie_famille"][0])))
            viol += int(exces[-1] > 0.05)
        for nom, (w, seuil, esp) in res.items():
            compte[nom] = compte.get(nom, 0) + int(np.max(w) >= seuil)
            pire.setdefault(nom, []).append(esp)
            lwmax.setdefault(nom, []).append(float(np.max(w)))
        if auteur:
            cs, cm, me = auteur
            m = dict(L=e["L"], Q=Q, M=M, y=y, z=e["z"], g=e["g"], cA=e["cA"], cB=e["cB"], c4=e["c4"])
            for nom, f in noms_auteur.items():
                if nom not in res:
                    continue
                wa = np.asarray(getattr(me, f)(m))
                seuil = me.SEUIL_BONFERRONI if nom == "M4" else cm.SEUIL
                compte_aut[nom] = compte_aut.get(nom, 0) + int(np.max(wa) >= seuil)
                ecarts.setdefault(nom, []).append(float(np.max(np.abs(wa - res[nom][0]))))
            for eta in (0.05, 0.2) if not a.leger else ():
                wa = me.a1_en_ligne(m, eta)
                nom = f"A1_pas{eta}"
                compte_aut[nom] = compte_aut.get(nom, 0) + int(np.max(wa) >= cm.SEUIL)
                ecarts.setdefault(nom, []).append(float(np.max(np.abs(wa - res[nom][0]))))
            if not a.leger:
                wa = me.a2_moitie(m)
                compte_aut["A2_instants"] = compte_aut.get("A2_instants", 0) + int(np.max(wa) >= cm.SEUIL)
                compte_aut["A2_fin"] = compte_aut.get("A2_fin", 0) + int(wa[-1] >= cm.SEUIL)
                ecarts.setdefault("A2_instants", []).append(float(np.max(np.abs(wa - res["A2_instants"][0]))))
        if auteur_m3:
            cs, cm, me = auteur_m3
            m = dict(L=e["L"], Q=Q, M=M, y=y, z=e["z"], g=e["g"], cA=e["cA"], cB=e["cB"], c4=e["c4"])
            wa = me.m3_toutes_coupures(m)
            compte_aut["M3"] = compte_aut.get("M3", 0) + int(np.max(wa) >= cm.SEUIL)
            lwmax.setdefault("M3_code_auteur", []).append(float(np.max(wa)))
            if "M3_borne_vraie_famille" in res:
                # le M3 de l'auteur doit rester sous le processus de la vraie famille (au réglage de l'optimiseur près)
                depasse.append(float(np.max(wa - res["M3_borne_vraie_famille"][0])))
            if a.m3:
                ecarts.setdefault("M3", []).append(float(np.max(np.abs(wa - res["M3"][0]))))
    R = a.r1 - a.r0
    methodes = {}
    if auteur_m3 and "M3" not in compte:
        methodes["M3_code_auteur"] = {"monde_dans_la_classe": dans_la_classe("M3", tags0), "promues": compte_aut["M3"], "mondes": R,
                                      "taux": round(compte_aut["M3"] / R, 5), "clopper_pearson_95": clopper(compte_aut["M3"], R),
                                      "log_w_max_mediane": round(float(np.median(lwmax["M3_code_auteur"])), 4),
                                      "log_w_max_maximum": round(float(np.max(lwmax["M3_code_auteur"])), 4),
                                      "log_esperance_exacte_bloc_maximum": None, "mondes_a_esperance_de_bloc_au_dessus_de_1": 0}
    for nom, k in compte.items():
        ex = np.array(pire[nom], dtype=float)
        d = {"monde_dans_la_classe": dans_la_classe(nom, tags0), "promues": k, "mondes": R, "taux": round(k / R, 5),
             "clopper_pearson_95": clopper(k, R), "log_w_max_mediane": round(float(np.median(lwmax[nom])), 4),
             "log_w_max_maximum": round(float(np.max(lwmax[nom])), 4),
             "log_esperance_exacte_bloc_maximum": None if np.all(np.isnan(ex)) else round(float(np.nanmax(ex)), 9),
             "mondes_a_esperance_de_bloc_au_dessus_de_1": int(np.nansum(ex > 1e-9))}
        if nom in compte_aut:
            d["code_auteur_sur_mes_mondes"] = {"promues": compte_aut[nom], "clopper_pearson_95": clopper(compte_aut[nom], R),
                                               "ecart_max_log_w_mediane": round(float(np.median(ecarts[nom])), 6),
                                               "ecart_max_log_w_maximum": round(float(np.max(ecarts[nom])), 6)} if nom in ecarts else \
                {"promues": compte_aut[nom], "clopper_pearson_95": clopper(compte_aut[nom], R)}
        methodes[nom] = d
    sortie = {"essai": "taille", "cas": a.cas, "etiquettes_du_monde": sorted(tags0), "n": a.n, "J": a.J, "blocs": 8,
              "mondes": R, "r0": a.r0, "r1": a.r1, "m3": bool(a.m3), "code_auteur_compare": bool(a.auteur), "m3_code_auteur": bool(a.auteur_m3),
              "graines": {"racine": RACINE, "derivation": "SeedSequence(entropy=racine, spawn_key=(1, indice du cas, r, n, J))",
                          "indice_du_cas": i_cas},
              "niveau": {"alpha": ALPHA, "seuil_log": SEUIL, "seuil_log_M4": math.log(8 / ALPHA)},
              "m3_au_dessus_de_sa_vraie_famille": viol, "m3_moins_vraie_famille_maximum": None if not exces else round(max(exces), 6),
              "pas_d_optimiseur": a.it, "leger": bool(a.leger), "sans_m4_m9": bool(a.sans_m4_m9), "seulement_m4_m9": bool(a.seulement_m4_m9),
              "m3_code_auteur_moins_vraie_famille": None if not depasse else {
                  "maximum": round(max(depasse), 6), "mondes_au_dessus_de_0,05": int(sum(d > 0.05 for d in depasse)), "mondes": len(depasse)},
              "methodes": methodes, "duree_s": round(time.time() - t0, 1),
              "versions": {"python": platform.python_version(), "numpy": np.__version__}}
    json.dump(sortie, open(a.sortie, "w"), ensure_ascii=False, indent=1)
    print(a.cas, R, "mondes", round(time.time() - t0, 1), "s")
    print({k: (v["promues"], v["monde_dans_la_classe"]) for k, v in methodes.items()})


# ----------------------------------------------------------------------------------------------------------------------
# amplification : pour un engagement gelé, les projections ne dépendent pas des issues ; on retire donc beaucoup de
# suites d'issues par engagement (la garantie du théorème est conditionnelle à l'engagement)
def cmd_amplification(a):
    if os.path.exists(a.sortie):
        raise SystemExit("sortie existante, aucun écrasement")
    t0 = time.time()
    i_cas = CAS.index(a.cas)
    noms = ["M1", "M2", "M2b", "M3", "M3_borne_vraie_famille"]
    par_eng = {k: [] for k in noms}
    tags0 = None
    for i in range(a.engagements):
        rng = graine("amplification", i_cas, i)
        e = engagement(rng)
        n, nb, b, J, L, z = e["n"], e["nb"], e["b"], e["J"], e["L"], e["z"]
        M, Q, tags, vraie = construire(rng, e, a.cas)
        tags0 = tags
        Lb, Qb = L.reshape(nb, b, J, K), Q.reshape(nb, b, K)
        Y = (rng.random((a.tirages, n))[:, :, None] > np.cumsum(M, 1)[None]).sum(2).clip(0, K - 1)      # (R, n)

        def table(cel, C):
            """log e de chaque bloc, pour chaque tirage, d'une liste de partitions de blocs cel (F, b) rangées par bloc."""
            F = cel.shape[0]
            rep = F // nb
            Lr, Qr = np.repeat(Lb, rep, axis=0), np.repeat(Qb, rep, axis=0)
            P = projeter_commun(Lr, Qr, cel, C, a.it)
            c = certificat_commun(Lr, Qr, P, cel, C)
            lr = np.log(np.maximum(Qr / np.maximum(P, MINI), MINI)).reshape(nb, rep, b, K)
            pen = (b * np.log(np.maximum(1.0, c))).reshape(nb, rep)
            Yb = Y.reshape(a.tirages, nb, b)
            # g[r, bloc, partition] = Σ_s lr[bloc, partition, s, Y[r, bloc, s]]
            g = np.zeros((a.tirages, nb, rep))
            for s_ in range(b):
                g += lr[np.arange(nb)[None, :, None], np.arange(rep)[None, None, :], s_, Yb[:, :, s_][:, :, None]]
            return g - pen[None]

        def famille(cel):
            return table(cel.reshape(nb, b), 4)[:, :, 0]                       # (R, nb)

        lin, f4, fa, fb, fg = (famille(c) for c in (np.zeros(n, int), e["c4"], e["cA"], e["cB"], e["g"]))
        w = {"M1": np.cumsum(lin, 1), "M2": np.cumsum(f4, 1)}
        w["M2b"] = np.minimum(np.minimum(w["M1"], np.cumsum(fa, 1)), np.cumsum(fb, 1))
        m3w = np.minimum(w["M1"], np.cumsum(fg, 1))
        for j in range(2):
            zb = z[:, j].reshape(nb, b)
            rang = np.argsort(np.argsort(zb, 1), 1)
            cel = (rang[:, None, :] >= np.arange(1, b)[None, :, None]).astype(int).reshape(nb * (b - 1), b)
            tab = np.empty((a.tirages, nb, b + 1))
            tab[:, :, 0] = lin
            tab[:, :, b] = lin
            tab[:, :, 1:b] = table(cel, 2)
            sous = (zb[None, :, :] <= np.unique(z[:, j])[:, None, None]).sum(2)          # (coupures, nb)
            for c0 in range(0, sous.shape[0], 50):
                bloc = tab[:, np.arange(nb)[None, :], sous[c0:c0 + 50]]                  # (R, coupures, nb)
                m3w = np.minimum(m3w, np.cumsum(bloc, 2).min(1))
            if vraie is not None and vraie[0] == "coupure" and vraie[1] == j:
                kv = (zb <= vraie[2]).sum(1)
                w["M3_borne_vraie_famille"] = np.cumsum(tab[:, np.arange(nb), kv], 1)
        w["M3"] = m3w
        if vraie is not None and vraie[0] == "lin":
            w["M3_borne_vraie_famille"] = w["M1"]
        if vraie is not None and vraie[0] == "sous_pop":
            w["M3_borne_vraie_famille"] = np.cumsum(fg, 1)
        for k in noms:
            if k in w:
                par_eng[k].append(int((w[k].max(1) >= SEUIL).sum()))
    res = {}
    for k in noms:
        if not par_eng[k]:
            continue
        x = np.array(par_eng[k]) / a.tirages
        res[k] = {"monde_dans_la_classe": dans_la_classe(k, tags0), "engagements": len(x), "tirages_par_engagement": a.tirages,
                  "promues": int(sum(par_eng[k])), "taux_moyen": round(float(x.mean()), 5),
                  "intervalle_95_par_engagements": [round(float(x.mean() - 1.96 * x.std(ddof=1) / math.sqrt(len(x))), 5),
                                                    round(float(x.mean() + 1.96 * x.std(ddof=1) / math.sqrt(len(x))), 5)],
                  "plus_grand_taux_d_un_engagement": round(float(x.max()), 5),
                  "engagements_dont_la_borne_basse_de_clopper_pearson_depasse_alpha": int(sum(clopper(v, a.tirages)[0] > ALPHA for v in par_eng[k]))}
    json.dump({"essai": "amplification", "cas": a.cas, "etiquettes_du_monde": sorted(tags0), "pas_d_optimiseur": a.it,
               "graines": {"racine": RACINE, "derivation": "SeedSequence(entropy=racine, spawn_key=(6, indice du cas, engagement))", "indice_du_cas": i_cas},
               "methodes": res, "duree_s": round(time.time() - t0, 1)}, open(a.sortie, "w"), ensure_ascii=False, indent=1)
    print(a.cas, {k: (v["taux_moyen"], v["plus_grand_taux_d_un_engagement"], v["monde_dans_la_classe"]) for k, v in res.items()}, round(time.time() - t0, 1), "s")


# ----------------------------------------------------------------------------------------------------------------------
# contrôles exacts
def sup_esperance(Lb, r, cel, C, famille, rng, it=600):
    """Plus grand logarithme d'espérance trouvé, sur le polytope des poids, de Π_s r_s(y_s) : Σ_s log m_s(θ), avec
    m_s(θ) = Σ_y P_θ(y | x_s)·r_s(y). Fonction concave ; espérance-maximisation depuis plusieurs départs, et sommets."""
    S, J, _ = Lb.shape
    aj = np.einsum("sk,sjk->sj", r, Lb)
    if famille == "commun":
        tau, v, u = em_commun(aj[None], r[None], np.ones((1, S)), cel[None], C, it)
        m = (1 - tau[0]) * (v[0][cel] * aj).sum(1) + tau[0] * (r * u[0][None]).sum(1)
        meilleur = float(np.log(np.maximum(m, MINI)).sum())
        for k in range(K):
            meilleur = max(meilleur, float(np.log(np.maximum(r[:, k], MINI)).sum()))
        for choix in itertools.islice(itertools.product(range(J), repeat=C), 1024):
            meilleur = max(meilleur, float(np.log(np.maximum(aj[np.arange(S), np.array(choix)[cel]], MINI)).sum()))
        return meilleur
    a = np.concatenate([aj, r], 1)
    th = em_melange(a, np.ones(S), cel, C, it)
    return float(np.log(np.maximum((th[cel] * a).sum(1), MINI)).sum())


def cmd_exact(a):
    if os.path.exists(a.sortie):
        raise SystemExit("sortie existante, aucun écrasement")
    t0 = time.time()
    # X1 : sup exact (sur le polytope) du logarithme de l'espérance d'une valeur e de bloc, pour des φ de toute sorte
    lignes, pire_global, essais = [], -np.inf, 0
    for i, (b, J, C, sorte) in enumerate(itertools.product((1, 2, 5, 25), (2, 4, 12), (1, 2, 4),
                                                           ("projection", "projection_courte", "hasard", "bord"))):
        pire = -np.inf
        for rep in range(8):
            rng = graine("exact", 1, i, rep)
            z = rng.standard_normal((b, 2))
            Lb = np.stack([loi_softmax(rng, z)[0] for _ in range(J)], 1)
            cel = rng.integers(0, C, b)
            q = loi_softmax(rng, z, force=float(rng.choice([1.0, 3.0, 6.0])))[0]
            if rep % 3 == 0:
                q = np.eye(K)[rng.integers(0, K, b)] * 0.999 + 0.001 / K
            for famille in ("commun", "cellules"):
                if famille == "commun":
                    if sorte.startswith("projection"):
                        P = projeter_commun(Lb[None], q[None], cel[None], C, 400 if sorte == "projection" else 3)[0]
                    else:
                        conc = 1.0 if sorte == "hasard" else 0.05
                        tau = np.array([rng.uniform(0.001, 0.999)])
                        v = rng.dirichlet(np.full(J, conc), (1, C)) + 1e-9
                        u = rng.dirichlet(np.full(K, conc), 1) + 1e-9
                        P = loi_commun(Lb[None], cel[None], tau, v / v.sum(2, keepdims=True), u / u.sum(1, keepdims=True))[0]
                    c = float(certificat_commun(Lb[None], q[None], P[None], cel[None], C)[0])
                else:
                    G = composantes(Lb)
                    if sorte.startswith("projection"):
                        th = proj_cellules(G, q, cel, C, 400 if sorte == "projection" else 3)
                    else:
                        th = rng.dirichlet(np.full(J + K, 1.0 if sorte == "hasard" else 0.05), C) + 1e-9
                        th /= th.sum(1, keepdims=True)
                    P = np.einsum("sv,svk->sk", th[cel], G)
                    c = certificat_cellules(G, q, P, cel, C)
                r = q / np.maximum(P, MINI)
                val = sup_esperance(Lb, r, cel, C, famille, rng) - b * math.log(max(1.0, c))
                pire = max(pire, val)
                essais += 1
        lignes.append({"bloc": b, "lois": J, "cellules": C, "sorte_de_phi": sorte, "log_sup_esperance_maximum": round(pire, 9)})
        pire_global = max(pire_global, pire)
    x1 = {"essais": essais, "plus_grand_log_sup_esperance": round(pire_global, 9),
          "lecture": "≤ 0 attendu par le lemme 1 ; > 0 serait un contre-exemple", "par_reglage": lignes}
    # X2 : énumération exacte, peu de tirages : K = 2 issues, 4 blocs de 3, toutes les suites ; probabilité exacte de
    # passer le seuil 1/alpha à l'un des 4 instants, sous le pire monde par bloc et sous des mondes au hasard
    x2 = []
    suites = np.array(list(itertools.product(range(2), repeat=12)))
    for alpha in (0.5, 0.25, 0.1):
        pire_p, pire_e = 0.0, -np.inf
        for rep in range(150):
            rng = graine("exact", 2, int(alpha * 100), rep)
            n, nb, b, J = 12, 4, 3, 2
            Lb = rng.dirichlet(np.ones(2), (n, J))                      # (n, J, 2)
            q = rng.dirichlet(np.full(2, 0.7), n)
            cuts = [np.zeros(n, int), rng.integers(0, 2, n), rng.integers(0, 2, n)]
            procs, lois = [], []
            for cel in cuts:
                a_ = np.transpose(Lb.reshape(nb, b, J, 2), (0, 1, 3, 2)).reshape(nb, b * 2, J)
                bb = np.broadcast_to(np.tile(np.eye(2), (b, 1))[None], (nb, b * 2, 2))
                tau, v, u = em_commun(a_, bb, q.reshape(nb, b * 2), np.repeat(cel.reshape(nb, b), 2, 1), 2, 300)
                P = loi_commun(Lb.reshape(nb, b, J, 2), cel.reshape(nb, b), tau, v, u)
                rr = q.reshape(nb, b, 2) / P
                mm = np.einsum("fsk,fsjk->fsj", rr, Lb.reshape(nb, b, J, 2))
                oh = np.zeros((nb, b, 2)); oh[np.arange(nb)[:, None], np.arange(b)[None, :], cel.reshape(nb, b)] = 1
                c = np.maximum(rr.sum(1).max(1), np.einsum("fsc,fsj->fcj", oh, mm).max(2).sum(1)) / b
                r = (rr / np.maximum(1.0, c)[:, None, None]).reshape(n, 2)
                procs.append(np.cumsum(np.log(r[np.arange(n)[None, :], suites]), 1)[:, b - 1::b])
                lois.append(P.reshape(n, 2))
            W = np.minimum(np.minimum(procs[0], procs[1]), procs[2])     # minimum sur trois familles
            passe = (W >= math.log(1 / alpha) - 1e-12).any(1)
            arret = np.where(passe, W[np.arange(len(W)), (W >= math.log(1 / alpha) - 1e-12).argmax(1)], W[:, -1])
            for monde in lois + [None, None]:
                # mondes nuls : la projection par bloc sur chacune des trois familles (pire cas, espérance 1 par
                # bloc), puis deux membres au hasard de la famille linéaire
                if monde is None:
                    wts = rng.dirichlet(np.ones(J + 2))
                    monde = np.einsum("j,sjk->sk", wts[:J], Lb) + wts[J:][None]
                pr = np.prod(monde[np.arange(n)[None, :], suites], 1)
                pire_p = max(pire_p, float(pr[passe].sum()))
                pire_e = max(pire_e, float((pr * np.exp(arret)).sum()))
        x2.append({"alpha": alpha, "engagements": 150, "plus_grande_probabilite_exacte_de_promotion": round(pire_p, 6),
                   "plus_grande_esperance_exacte_de_la_valeur_arretee": round(pire_e, 6)})
    json.dump({"essai": "exact", "graines": {"racine": RACINE, "derivation": "SeedSequence(entropy=racine, spawn_key=(2, …))"},
               "X1_sup_esperance_bloc": x1,
               "X2_enumeration": {"lecture": "K = 2, 4 blocs de 3, les 4 096 suites ; richesse = minimum de trois familles "
                                             "(linéaire et deux coupures) ; mondes : projection par bloc sur chacune des trois "
                                             "familles (pire cas) et deux membres linéaires au hasard ; probabilité ≤ alpha et "
                                             "espérance ≤ 1 attendues", "par_alpha": x2},
               "duree_s": round(time.time() - t0, 1)}, open(a.sortie, "w"), ensure_ascii=False, indent=1)
    print("X1", x1["plus_grand_log_sup_esperance"], "X2", x2, round(time.time() - t0, 1), "s")


# ----------------------------------------------------------------------------------------------------------------------
# hypothèse P4 : carte qui lit l'historique du bloc courant
REGLAGES_MEMOIRE = [  # (monde, genre de carte, paramètre, part) — tous rapportés, quel que soit le résultat
    ("uniforme", "sans_remise", 70, 1.0), ("uniforme", "sans_remise", 100, 1.0), ("uniforme", "sans_remise", 200, 1.0),
    ("melange_deux_lois", "sans_remise", 100, 0.5), ("melange_deux_lois", "sans_remise", 70, 0.5),
    ("melange_deux_lois", "sans_remise", 70, 0.25),
    ("melange_deux_lois", "contre_exces_du_bloc", 0.1, 1.0), ("melange_deux_lois", "contre_exces_du_bloc", 0.3, 1.0),
    ("melange_deux_lois", "contre_exces_du_bloc", 1.0, 1.0)]


def carte_a_memoire(genre, param, part, M, y, b, gele):
    """Loi de la carte à chaque instance, sachant les issues passées. « sans_remise » : la loi de la grammaire du juge
    (p_k ∝ c − nombre de k déjà vus, c = param pour chaque issue), mêlée à la loi du monde avec le poids `part`.
    « contre_exces_du_bloc » : la loi du monde inclinée contre l'excès de chaque issue dans le bloc en cours,
    q(y) ∝ M(y)·exp(−param·(nombre de y dans le bloc − nombre attendu)). `gele` : l'historique n'est lu qu'au début de
    chaque bloc (hypothèse P4 rétablie)."""
    n = len(y)
    Q = np.empty((n, K))
    vus, exces = np.zeros(K), np.zeros(K)
    fige_vus = vus.copy()
    for t in range(n):
        if t % b == 0:
            exces[:] = 0.0
            fige_vus = vus.copy()
        if genre == "sans_remise":
            p = np.maximum(param - (fige_vus if gele else vus), 0.0)
            p = p / p.sum() if p.sum() > 0 else np.full(K, 1.0 / K)
            q = part * p + (1.0 - part) * M[t]
        else:
            q = M[t] * np.exp(-param * (0.0 if gele else exces))
        q = np.maximum(q, 1e-12)
        Q[t] = q / q.sum()
        vus[y[t]] += 1
        exces += np.eye(K)[y[t]] - M[t]
    return Q


def cmd_memoire(a):
    if os.path.exists(a.sortie):
        raise SystemExit("sortie existante, aucun écrasement")
    t0 = time.time()
    # (i) calcul exact : K = 2, un bloc de 2, nul = toutes les lois constantes ; carte : première issue à pile ou face,
    # puis « l'autre issue, sûrement » ; projection calculée sur les lois réalisées (moyenne des deux lois de la carte)
    esp = {}
    for p in (0.5, 0.3, 0.1):
        tot = 0.0
        for y1 in (0, 1):
            for y2 in (0, 1):
                q1 = np.array([0.5, 0.5]); q2 = np.eye(2)[1 - y1]
                phi = (q1 + q2) / 2                                    # projection sur les constantes : la moyenne
                c = max((q1 / phi + q2 / phi).max() / 2, 1.0)          # sommets δ_0, δ_1
                proba = (p if y1 else 1 - p) * (p if y2 else 1 - p)
                tot += proba * q1[y1] * q2[y2] / (phi[y1] * phi[y2]) / c ** 2
        esp[str(p)] = round(tot, 6)
    # (ii) à l'échelle du juge : n = 200, 8 blocs de 25, K = 3, famille linéaire (4 lois connues, bruit aveugle) ; la
    # projection et le certificat de chaque bloc sont calculés sur les lois que la carte a réalisées
    monde, genre, param, part = REGLAGES_MEMOIRE[a.reglage]
    R = a.mondes
    k_bloc, k_vrai, k_gele, e1, wfin = 0, 0, 0, [], []
    quand = np.zeros(8, int)
    auteur = charger_auteur() if a.complet else None
    complet = {}
    for r in range(R):
        rng = graine("memoire", a.reglage, r)
        e = engagement(rng)
        n, J, nb, b = e["n"], e["J"], e["nb"], e["b"]
        M = np.full((n, K), 1.0 / K) if monde == "uniforme" else 0.5 * e["L"][:, 0] + 0.5 * e["L"][:, 1]
        y = tirer(rng, M)
        Q = carte_a_memoire(genre, param, part, M, y, b, False)
        Qg = carte_a_memoire(genre, param, part, M, y, b, True)
        Lb = np.tile(e["L"].reshape(nb, b, J, K), (2, 1, 1, 1))
        Qb = np.concatenate([Q.reshape(nb, b, K), Qg.reshape(nb, b, K)])
        cel = np.zeros((2 * nb, b), int)
        P = projeter_commun(Lb, Qb, cel, 1, 100)
        lo, _, _ = _valeurs_blocs(Qb, P, np.tile(y.reshape(nb, b), (2, 1)), np.tile(M.reshape(nb, b, K), (2, 1, 1)),
                                  certificat_commun(Lb, Qb, P, cel, 1))
        w = np.cumsum(lo[:nb])
        if w.max() >= SEUIL:
            k_bloc += 1
            quand[int(np.argmax(w >= SEUIL))] += 1
        e1.append(float(np.exp(lo[0])))
        wfin.append(float(np.exp(min(w[-1], 50.0))))
        k_gele += int(np.cumsum(lo[nb:]).max() >= SEUIL)
        # témoin : le rapport de vraisemblance vrai q/P* (martingale exacte) aux mêmes instants
        lv = np.cumsum(np.log(Q[np.arange(n), y] / M[np.arange(n), y]))[np.arange(b, n + 1, b) - 1]
        k_vrai += int(lv.max() >= SEUIL)
        if r < a.complet:
            # les autres méthodes par blocs sur les mêmes lois réalisées : mes écritures, puis le code de l'auteur
            res = evaluer(e, Q, y, M, avec_m3=True, leger=True, vraie=("lin", 0, 0.0))
            cs, cm, me = auteur
            m = dict(L=e["L"], Q=Q, M=M, y=y, z=e["z"], g=e["g"], cA=e["cA"], cB=e["cB"], c4=e["c4"])
            res["M1_code_auteur"] = (me.m1_lin(m), SEUIL, 0.0)
            res["M2_code_auteur"] = (me.m2_f4(m), SEUIL, 0.0)
            res["M3_code_auteur"] = (me.m3_toutes_coupures(m), SEUIL, 0.0)
            for nom in ("M1", "M2", "M2b", "M3", "M1_code_auteur", "M2_code_auteur", "M3_code_auteur"):
                complet[nom] = complet.get(nom, 0) + int(np.max(res[nom][0]) >= SEUIL)
    ligne = {"monde": monde, "carte": genre, "parametre": param, "part": part, "mondes": R,
             "promues_blocs_sur_lois_realisees": k_bloc, "clopper_pearson_95": clopper(k_bloc, R),
             "instant_de_premiere_promotion_par_bloc": quand.tolist(),
             "moyenne_de_la_valeur_e_du_premier_bloc": round(float(np.mean(e1)), 4),
             "erreur_type_de_cette_moyenne": round(float(np.std(e1) / math.sqrt(R)), 4),
             "temoin_rapport_de_vraisemblance_vrai_promues": k_vrai, "temoin_vrai_clopper_pearson_95": clopper(k_vrai, R),
             "temoin_historique_gele_par_bloc_promues": k_gele, "temoin_gele_clopper_pearson_95": clopper(k_gele, R)}
    if a.complet:
        nc = min(a.complet, R)
        ligne["autres_methodes_sur_les_premiers_mondes"] = {"mondes": nc, "promues": complet,
                                                            "clopper_pearson_95": {k: clopper(v, nc) for k, v in complet.items()}}
    print(ligne)
    json.dump({"essai": "memoire", "reglage": a.reglage,
               "graines": {"racine": RACINE, "derivation": "SeedSequence(entropy=racine, spawn_key=(3, réglage, r))"},
               "exact_bloc_de_2": {"esperance_de_la_valeur_e_selon_p": esp,
                                   "lecture": "monde = pile ou face de probabilité p, membre du nul ; > 1 : pas une valeur e"},
               "echelle_du_juge": ligne, "duree_s": round(time.time() - t0, 1)}, open(a.sortie, "w"), ensure_ascii=False, indent=1)


# ----------------------------------------------------------------------------------------------------------------------
# lois connues seulement par tirages (cas d'école de l'auteur, réécrit)
def cmd_tirages(a):
    if os.path.exists(a.sortie):
        raise SystemExit("sortie existante, aucun écrasement")
    t0 = time.time()
    delta, res = 0.01, {}
    for i_m, m in enumerate((50, 200, 1000, 5000)):
        if a.m is not None and m != a.m:
            continue
        eps = math.sqrt(2 * math.log((2 ** K - 2) * 2 / delta) / m)
        cpt = {"vraies_lois": 0, "comme_si_exact": 0, "robuste": 0}
        couvert, robuste_sous_vrai = 0, 0
        for r in range(a.mondes):
            rng = graine("tirages", i_m, r)
            L1, L2 = rng.dirichlet(np.ones(K)), rng.dirichlet(np.ones(K))
            t = rng.uniform()
            q = t * L1 + (1 - t) * L2                                   # copie d'un membre du vrai nul
            y = tirer(rng, np.broadcast_to(q, (200, K)))
            H1, H2 = rng.multinomial(m, L1) / m, rng.multinomial(m, L2) / m
            dedans = abs(H1 - L1).sum() <= eps and abs(H2 - L2).sum() <= eps
            couvert += int(dedans)

            def proj(A, B):
                th = em_melange(np.stack([np.maximum(A, 1e-12), np.maximum(B, 1e-12)], 1), q, np.zeros(K, int), 1, 150)[0]
                return th[0] * np.maximum(A, 1e-12) + th[1] * np.maximum(B, 1e-12)

            def promue(phi, c):
                lw = np.cumsum(np.log(q[y] / phi[y]).reshape(8, 25).sum(1) - 25 * math.log(max(1.0, c)))
                return bool(lw.max() >= SEUIL)
            phi = proj(L1, L2)
            cpt["vraies_lois"] += promue(phi, max((L1 * q / phi).sum(), (L2 * q / phi).sum()))
            ph = proj(H1, H2)
            f = q / ph
            cpt["comme_si_exact"] += promue(ph, max((H1 * f).sum(), (H2 * f).sum()))
            cr = max((H * f).sum() + eps / 2 * (f.max() - f.min()) for H in (H1, H2))
            cpt["robuste"] += promue(ph, cr)
            vrai = max((L1 * f).sum(), (L2 * f).sum())
            robuste_sous_vrai += int(dedans and cr < vrai - 1e-12)
        res[f"m={m}"] = {"rayon": round(eps, 4), "mondes": a.mondes,
                         "copies_promues": {k: {"promues": v, "clopper_pearson_95": clopper(v, a.mondes)} for k, v in cpt.items()},
                         "mondes_ou_les_deux_boules_contiennent_la_vraie_loi": couvert,
                         "certificat_robuste_sous_le_vrai_alors_que_boules_couvrantes": robuste_sous_vrai}
        print(m, res[f"m={m}"])
    json.dump({"essai": "tirages", "delta": delta, "graines": {"racine": RACINE, "derivation": "SeedSequence(entropy=racine, spawn_key=(4, indice de m, r))"},
               "resultats": res, "duree_s": round(time.time() - t0, 1)}, open(a.sortie, "w"), ensure_ascii=False, indent=1)


# ----------------------------------------------------------------------------------------------------------------------
# encadrement de la référence « façon v9 » de l'auteur sur SES mondes : maximum de vraisemblance de la classe du v9 à
# chaque instant, valeur atteinte (borne basse) et valeur certifiée par l'écart de Frank-Wolfe (borne haute, comme le v9)
def max_v9(L, y, z, g, t, it=150):
    Lt = L[:t]
    a1 = Lt[np.arange(t), :, y[:t]]                                    # (t, J)
    cels = [np.zeros(t, int), g[:t]]
    for j in range(2):
        zt = z[:t, j]
        for s in np.sort(zt)[:-1]:
            cels.append((zt > s).astype(int))
    cel = np.stack(cels)
    F = cel.shape[0]
    bb = np.broadcast_to(np.eye(K)[y[:t]][None], (F, t, K))
    tau, v, u = em_commun(np.broadcast_to(a1[None], (F, t, a1.shape[1])), bb, np.ones((F, t)), cel, 2, it)
    vs = v[np.arange(F)[:, None], cel]
    p = (1 - tau)[:, None] * (vs * a1[None]).sum(2) + tau[:, None] * u[:, y[:t]]
    f = np.log(np.maximum(p, MINI)).sum(1)
    inv = 1.0 / np.maximum(p, MINI)
    oh = np.zeros((F, t, 2)); oh[np.arange(F)[:, None], np.arange(t)[None, :], cel] = 1.0
    V1 = np.einsum("ftc,ftj->fcj", oh, inv[:, :, None] * a1[None]).max(2).sum(1)
    V2 = np.einsum("ft,tk->fk", inv, np.eye(K)[y[:t]]).max(1)
    cert = np.minimum(0.0, f + np.maximum(0.0, np.maximum(V1, V2) - t))
    return float(f.max()), float(cert.max())


def cmd_reference(a):
    if os.path.exists(a.sortie):
        raise SystemExit("sortie existante, aucun écrasement")
    cs, cm, me = charger_auteur()
    import essai_projection_puissance_v1 as pu
    t0 = time.time()
    i_cas = pu.NOMS.index(a.cas)
    dose = pu.CAS[a.cas][a.dose]
    lignes = []
    for r in range(a.r0, a.r1):
        rng = np.random.default_rng(np.random.SeedSequence(entropy=pu.RACINE, spawn_key=(i_cas, a.dose, r)))
        m = cs.construire(rng, (a.cas, dose))                       # monde de l'auteur, sa graine
        refs = me.references(m)
        w3 = me.m3_toutes_coupures(m)
        num = np.cumsum(cm.log_q_issues(m["Q"], m["y"]))[cm.T - 1]
        att, cer = zip(*(max_v9(m["L"], m["y"], m["z"], m["g"], int(t)) for t in cm.T))
        d9 = num - refs["R9"]
        e = dict(z=m["z"], g=m["g"], L=m["L"], n=200, J=4, nb=8, b=25, cA=m["cA"], cB=m["cB"], c4=m["c4"])
        lin, elin, _, _ = blocs_commun(e, m["Q"], m["y"], m["M"], np.zeros(200, int), 1, 200)
        sp, _, _, _ = blocs_commun(e, m["Q"], m["y"], m["M"], m["g"], 2, 200)
        mien = m3(e, m["Q"], m["y"], m["M"], lin, elin, sp, 150)
        lignes.append({"r": r, "R9_auteur": bool(refs["R9"].max() >= SEUIL), "M3_auteur": bool(w3.max() >= SEUIL),
                       "M3_moi": bool(mien.max() >= SEUIL),
                       "v9_valeur_atteinte_moi": bool((num - np.array(att)).max() >= SEUIL),
                       "v9_certifie_moi": bool((num - np.array(cer)).max() >= SEUIL),
                       "denominateur_auteur_moins_certifie_max": float((d9 - np.array(cer)).max()),
                       "atteinte_moi_moins_denominateur_auteur_max": float((np.array(att) - d9).max()),
                       "atteinte_moi_moins_denominateur_auteur_min": float((np.array(att) - d9).min()),
                       "ecart_m3_max": float(np.abs(mien - w3).max())})
    R = len(lignes)
    tot = {k: int(sum(l[k] for l in lignes)) for k in ("R9_auteur", "M3_auteur", "M3_moi", "v9_valeur_atteinte_moi", "v9_certifie_moi")}
    json.dump({"essai": "reference", "cas": a.cas, "dose": dose, "mondes": R, "r0": a.r0, "r1": a.r1,
               "graines": "celles de l'auteur : SeedSequence(entropy=2026111510, spawn_key=(indice du cas, indice de dose, r))",
               "promues": tot,
               "denominateur_auteur_au_dessus_du_maximum_certifie": int(sum(l["denominateur_auteur_moins_certifie_max"] > 1e-6 for l in lignes)),
               "plus_grand_depassement": max(l["denominateur_auteur_moins_certifie_max"] for l in lignes),
               "avance_de_ma_valeur_atteinte_sur_la_sienne": {"mediane_des_max": float(np.median([l["atteinte_moi_moins_denominateur_auteur_max"] for l in lignes])),
                                                             "maximum": max(l["atteinte_moi_moins_denominateur_auteur_max"] for l in lignes),
                                                             "minimum": min(l["atteinte_moi_moins_denominateur_auteur_min"] for l in lignes)},
               "ecart_m3_moi_auteur_maximum": max(l["ecart_m3_max"] for l in lignes),
               "par_monde": lignes, "duree_s": round(time.time() - t0, 1)}, open(a.sortie, "w"), ensure_ascii=False, indent=1)
    print(a.cas, dose, tot, round(time.time() - t0, 1), "s")


# ----------------------------------------------------------------------------------------------------------------------
# rejeu : comparaison, monde par monde, des sorties rejouées (programmes de l'auteur relancés tels quels, ses graines)
# aux sorties scellées de l'auteur ; et tables des cas qu'il avait programmés sans les jouer
def cmd_rejeu(a):
    if os.path.exists(a.sortie):
        raise SystemExit("sortie existante, aucun écrasement")
    ici = os.path.dirname(os.path.abspath(__file__))
    scelle = os.path.join(ici, "sorties")
    bilan = {"essai": "rejeu", "taille": {}, "puissance": {}, "tirages": None, "cas_non_joues_par_l_auteur": {}}
    for f in sorted(glob.glob(os.path.join(a.dossier, "taille-*.json"))):
        d = json.load(open(f))
        orig = {}
        for g in sorted(glob.glob(os.path.join(scelle, f"taille-{d['cas'][:3]}-r*-v1.json"))):
            o = json.load(open(g))
            for m, v in o["par_monde"].items():
                orig.setdefault(m, {}).update({o["r_debut"] + i: x for i, x in enumerate(v)})
        n = eg_p = eg_w = 0
        for m, v in d["par_monde"].items():
            for i, x in enumerate(v):
                ref = orig[m][d["r_debut"] + i]
                n += 1; eg_p += int(x[0] == ref[0]); eg_w += int(x[1] == ref[1])
        bilan["taille"][d["cas"]] = {"mondes_rejoues": d["mondes"], "couples_methode_monde": n, "promotions_egales": eg_p,
                                     "log_w_max_egaux_a_4_decimales": eg_w}
    for f in sorted(glob.glob(os.path.join(a.dossier, "puissance-*.json"))):
        d = json.load(open(f))
        o = json.load(open(os.path.join(scelle, f"puissance-{d['cas'][:2]}-d{d['indice_dose']}-r0000-0100-v1.json")))
        n = eg = 0
        for m, v in d["par_monde"].items():
            for i, x in enumerate(v):
                n += 1; eg += int(x == o["par_monde"][m][d["r_debut"] + i])
        bilan["puissance"][f"{d['cas']}|{d['dose']}"] = {"mondes_rejoues": d["mondes"], "couples_bras_monde": n, "promotions_egales": eg}
    t = os.path.join(a.dossier, "tirages-rejeu.json")
    if os.path.exists(t):
        x, y_ = json.load(open(t)), json.load(open(os.path.join(scelle, "tirages-v1.json")))
        bilan["tirages"] = {"mondes_par_cas": x["mondes_par_cas"], "resultats_identiques": x["resultats"] == y_["resultats"]}
    for nom in ("taille", "puissance"):
        f = os.path.join(a.dossier, f"fusion-{nom}.json")
        if os.path.exists(f):
            bilan[f"fusion_{nom}_identique_a_l_octet"] = open(f, "rb").read() == open(os.path.join(ici, f"sortie-{nom}-v1.json"), "rb").read()
    for f in sorted(glob.glob(os.path.join(a.dossier, "nonjoue-*.json"))):
        d = json.load(open(f))
        bilan["cas_non_joues_par_l_auteur"][d["cas"]] = {
            "mondes": d["mondes"], "graines": d["graines"],
            "methodes": {m: {k: v[k] for k in ("monde_dans_la_classe", "promues", "mondes", "clopper_pearson_95", "log_w_max_maximum")}
                         for m, v in d["methodes"].items()}}
    json.dump(bilan, open(a.sortie, "w"), ensure_ascii=False, indent=1)
    print(json.dumps({k: v for k, v in bilan.items() if k != "cas_non_joues_par_l_auteur"}, ensure_ascii=False)[:1500])


# ----------------------------------------------------------------------------------------------------------------------
# contrôle de non-régression : une tranche de taille rejouée par la version finale du programme, comparée à la tranche
# d'origine (les sous-commandes ajoutées en cours de route ne doivent rien changer aux comptes)
def cmd_controle(a):
    if os.path.exists(a.sortie):
        raise SystemExit("sortie existante, aucun écrasement")
    x, y_ = json.load(open(a.origine)), json.load(open(a.rejouee))
    cles = ("cas", "n", "J", "r0", "r1", "pas_d_optimiseur", "leger", "sans_m4_m9")
    memes_reglages = all(x.get(k) == y_.get(k) for k in cles)
    champs = ("promues", "mondes", "log_w_max_mediane", "log_w_max_maximum", "log_esperance_exacte_bloc_maximum",
              "mondes_a_esperance_de_bloc_au_dessus_de_1")
    differences = [m for m in x["methodes"] if any(x["methodes"][m].get(c) != y_["methodes"].get(m, {}).get(c) for c in champs)]
    json.dump({"essai": "controle", "tranche": os.path.basename(a.origine), "memes_reglages": memes_reglages,
               "methodes_comparees": len(x["methodes"]), "methodes_differentes": differences,
               "identique": memes_reglages and not differences}, open(a.sortie, "w"), ensure_ascii=False, indent=1)
    print("contrôle :", os.path.basename(a.origine), "identique" if memes_reglages and not differences else f"DIFFÉRENT {differences}")


# ----------------------------------------------------------------------------------------------------------------------
def cmd_fusion(a):
    if os.path.exists(a.sortie):
        raise SystemExit("sortie existante, aucun écrasement")
    pieces = {}
    for f in sorted(glob.glob(os.path.join(a.dossier, "*.json"))):
        pieces[os.path.basename(f)] = json.load(open(f))
    taille = {}
    for nom, d in pieces.items():
        if d.get("essai") != "taille":
            continue
        cle = f"{d['cas']}|n={d['n']}|J={d['J']}"
        g = taille.setdefault(cle, {"etiquettes_du_monde": d["etiquettes_du_monde"], "tranches": [], "methodes": {},
                                    "m3_au_dessus_de_sa_vraie_famille": 0})
        g["tranches"].append({"fichier": nom, "r": [d["r0"], d["r1"]], "m3": d["m3"], "code_auteur_compare": d["code_auteur_compare"]})
        g["m3_au_dessus_de_sa_vraie_famille"] += d["m3_au_dessus_de_sa_vraie_famille"]
        for cle_max in ("m3_moins_vraie_famille_maximum",):
            if d.get(cle_max) is not None:
                g[cle_max] = max(g.get(cle_max, -1e300), d[cle_max])
        if d.get("m3_code_auteur_moins_vraie_famille"):
            x = d["m3_code_auteur_moins_vraie_famille"]
            y_ = g.setdefault("m3_code_auteur_moins_vraie_famille", {"maximum": -1e300, "mondes_au_dessus_de_0,05": 0, "mondes": 0})
            y_["maximum"] = max(y_["maximum"], x["maximum"]); y_["mondes_au_dessus_de_0,05"] += x["mondes_au_dessus_de_0,05"]; y_["mondes"] += x["mondes"]
        for m, v in d["methodes"].items():
            t = g["methodes"].setdefault(m, {"monde_dans_la_classe": v["monde_dans_la_classe"], "promues": 0, "mondes": 0,
                                             "log_w_max_maximum": -1e300, "log_esperance_exacte_bloc_maximum": None,
                                             "mondes_a_esperance_de_bloc_au_dessus_de_1": 0})
            t["promues"] += v["promues"]; t["mondes"] += v["mondes"]
            t["log_w_max_maximum"] = max(t["log_w_max_maximum"], v["log_w_max_maximum"])
            if v["log_esperance_exacte_bloc_maximum"] is not None:
                t["log_esperance_exacte_bloc_maximum"] = max(v["log_esperance_exacte_bloc_maximum"],
                                                              t["log_esperance_exacte_bloc_maximum"] if t["log_esperance_exacte_bloc_maximum"] is not None else -1e300)
            t["mondes_a_esperance_de_bloc_au_dessus_de_1"] += v["mondes_a_esperance_de_bloc_au_dessus_de_1"]
            if "code_auteur_sur_mes_mondes" in v:
                ca = t.setdefault("code_auteur_sur_mes_mondes", {"promues": 0, "mondes": 0, "ecart_max_log_w_maximum": 0.0})
                ca["promues"] += v["code_auteur_sur_mes_mondes"]["promues"]; ca["mondes"] += v["mondes"]
                ca["ecart_max_log_w_maximum"] = max(ca["ecart_max_log_w_maximum"], v["code_auteur_sur_mes_mondes"].get("ecart_max_log_w_maximum", 0.0))
    for g in taille.values():
        rs = sorted({tuple(t["r"]) for t in g["tranches"]})
        g["tranches_distinctes"] = [list(r) for r in rs]
        for t in g["methodes"].values():
            t["taux"] = round(t["promues"] / t["mondes"], 5)
            t["clopper_pearson_95"] = clopper(t["promues"], t["mondes"])
            if "code_auteur_sur_mes_mondes" in t:
                ca = t["code_auteur_sur_mes_mondes"]
                ca["clopper_pearson_95"] = clopper(ca["promues"], ca["mondes"])
    json.dump({"essai": "attaque de la projection — fusion", "racine_des_graines": RACINE, "niveau": {"alpha": ALPHA, "seuil_log": SEUIL},
               "taille_par_cas": taille, "pieces": pieces}, open(a.sortie, "w"), ensure_ascii=False, indent=1)
    print("fusion :", len(pieces), "pièces,", len(taille), "cas de taille")


def main():
    p = argparse.ArgumentParser()
    s = p.add_subparsers(dest="commande", required=True)
    t = s.add_parser("taille"); t.add_argument("cas"); t.add_argument("r0", type=int); t.add_argument("r1", type=int)
    t.add_argument("sortie"); t.add_argument("--m3", action="store_true"); t.add_argument("--auteur", action="store_true")
    t.add_argument("--auteur-m3", dest="auteur_m3", action="store_true"); t.add_argument("--leger", action="store_true")
    t.add_argument("--it", type=int, default=60); t.add_argument("--sans-m4-m9", dest="sans_m4_m9", action="store_true")
    t.add_argument("--seulement-m4-m9", dest="seulement_m4_m9", action="store_true")
    t.add_argument("--n", type=int, default=200); t.add_argument("--J", type=int, default=4); t.set_defaults(f=cmd_taille)
    x = s.add_parser("exact"); x.add_argument("sortie"); x.set_defaults(f=cmd_exact)
    am = s.add_parser("amplification"); am.add_argument("cas"); am.add_argument("engagements", type=int)
    am.add_argument("tirages", type=int); am.add_argument("sortie"); am.add_argument("--it", type=int, default=60)
    am.set_defaults(f=cmd_amplification)
    m = s.add_parser("memoire"); m.add_argument("reglage", type=int); m.add_argument("sortie")
    m.add_argument("--mondes", type=int, default=2000); m.add_argument("--complet", type=int, default=0); m.set_defaults(f=cmd_memoire)
    d = s.add_parser("tirages"); d.add_argument("mondes", type=int); d.add_argument("sortie")
    d.add_argument("--m", type=int, default=None); d.set_defaults(f=cmd_tirages)
    r = s.add_parser("reference"); r.add_argument("cas"); r.add_argument("dose", type=int); r.add_argument("r0", type=int)
    r.add_argument("r1", type=int); r.add_argument("sortie"); r.set_defaults(f=cmd_reference)
    rj = s.add_parser("rejeu"); rj.add_argument("dossier"); rj.add_argument("sortie"); rj.set_defaults(f=cmd_rejeu)
    co = s.add_parser("controle"); co.add_argument("origine"); co.add_argument("rejouee"); co.add_argument("sortie")
    co.set_defaults(f=cmd_controle)
    f = s.add_parser("fusion"); f.add_argument("dossier"); f.add_argument("sortie"); f.set_defaults(f=cmd_fusion)
    a = p.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
