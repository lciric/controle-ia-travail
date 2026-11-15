"""Attaque des méthodes « ensemble de confiance pour les poids du nul, puis maximum sur cet ensemble » — v1.

Programme du réfutateur. Mise au point exploratoire, aucune revendication. Processeur seul, aucun appel réseau.
Écrit sans recopier le code de l'auteur des méthodes : les méthodes sont reprogrammées d'après leur énoncé
(note `methodes-confiance-v1.md`, sections 3 et 4) ; aucun module de l'auteur ni des dossiers de copie n'est importé.
Ce qui est repris de l'énoncé (et non du code) : la famille du nul (mélange par morceau des lois connues, bruit aveugle
commun), les constructions des ensembles de confiance, le lissage du prédicteur (0,2 % vers l'uniforme), son réajustement
tous les 25 tirages, les deux parts beta (0,01 et 0,025), le pari lu au seuil log(1/(alpha - beta)), les huit instants.

Modes (un lot par appel, sortie JSON neuve, jamais d'écrasement) :
  taille CAS DEBUT FIN SORTIE      monde = membre du nul du banc ; cartes : copie exacte, hors classe, deux cartes
                                   « pari » (tout misé sur des issues rares, puis copie) ; méthodes BB_A, BB_T_seq,
                                   BB_T_coupe, BB_S_moitie, BB_Q_blocs, artefacts F1 et F2, référence v9 ;
  hors_nul CAS DEBUT FIN SORTIE    monde hors du nul du banc ; calcul complet à chaque monde ; cartes : le monde
                                   lui-même et des cartes MEMBRES du nul (copie d'une loi connue, recollage sur une
                                   coupure, meilleur membre ajusté) ; références v8, v9, limité ;
  exact PARTIE SORTIE              calcul exact (programmation dynamique, aucune simulation) de la taille et de la
                                   puissance sur un nul jouet à une issue binaire, aux tailles du juge (A1, A2, BC) ;
  certificat SORTIE                mon majorant contraint comparé à un solveur convexe indépendant (scipy, SLSQP).

Raccourci du mode « taille » (dit dans la note de réfutation) : un majorant certifié D du maximum sur l'ensemble C vérifie
D_t >= l_t(theta*) dès que theta* est dans C. Une carte ne peut donc être promue que si theta* est hors de C, ou si son
rapport de vraisemblance contre le monde, Lambda_t = q(y_1..t) / p_theta*(y_1..t), atteint le seuil à un instant lu. Le
calcul lourd (maximum contraint aux huit instants) n'est fait que dans ces mondes-là, et dans un monde sur vingt fixé
d'avance (audit : on y vérifie D_t >= l_t(theta*) et on y mesure la marge). Dans les autres mondes la promotion est
impossible ; la couverture et Lambda y sont calculés exactement.

Graines : numpy.random.SeedSequence(entropy=RACINE, spawn_key=(mode, indice du cas, monde)), un générateur par monde.
"""

import hashlib
import json
import math
import os
import platform
import sys
import time

import numpy as np

RACINE = 2026111577
ALPHA = 0.05
BETAS = (0.01, 0.025)
D = 2
N = 200
INSTANTS = tuple(range(25, N + 1, 25))
INSTANTS_2 = tuple(t for t in INSTANTS if t > N // 2)
PLANCHER = 1e-12
EPS_LISSAGE = 0.002
BLOC = 25
GAMMAS = (0.0, 0.15, 0.4, 1.0, 2.5, 6.0)      # multiplicateurs de Lagrange, en unités de n_e / n_c
TOL_EM = 2e-3
SEUIL_V9 = math.log(1.0 / ALPHA)
SEUILS = {b: math.log(1.0 / (ALPHA - b)) for b in BETAS}
LB = {b: math.log(1.0 / b) for b in BETAS}
AUDIT_MODULO = 20


def deciles():
    from scipy.stats import norm
    return [round(float(norm.ppf(i / 10)), 4) for i in range(1, 10)]


GRILLE9 = deciles()


# ---------------------------------------------------------------------------------------------------------------------
# Lois, archive, partitions
# ---------------------------------------------------------------------------------------------------------------------
def tirer_softmax(rng, K):
    return rng.normal(0.0, 1.5, size=(K, D)), rng.normal(0.0, 0.3, size=K)


def p_softmax(par, z):
    s = z @ par[0].T + par[1]
    s = s - s.max(axis=1, keepdims=True)
    e = np.exp(s)
    return e / e.sum(axis=1, keepdims=True)


def seuil_libre(rng, interdits, ecart=0.05):
    while True:
        s = round(float(rng.uniform(-1.0, 1.0)), 2)
        if all(abs(s - c) >= ecart for c in interdits):
            return s


def tirer_archive(rng, J, K):
    """J lois connues : J - n_ss lois softmax et n_ss lois « si_sinon » sur un seuil de l'archive (1 si J < 6, 2 sinon)."""
    n_ss = 1 if J < 6 else 2
    lois = [("softmax", tirer_softmax(rng, K)) for _ in range(J - n_ss)]
    jA = int(rng.integers(0, D))
    coupes = []
    for i in range(n_ss):
        j = jA if i == 0 else 1 - jA
        s = seuil_libre(rng, GRILLE9)
        lois.append(("si_sinon", j, s, tirer_softmax(rng, K), tirer_softmax(rng, K)))
        coupes.append((j, s))
    return {"J": J, "K": K, "lois": lois, "coupes": coupes}


def p_loi(loi, z):
    if loi[0] == "softmax":
        return p_softmax(loi[1], z)
    _, j, s, pa, pb = loi
    return np.where((z[:, j] > s)[:, None], p_softmax(pa, z), p_softmax(pb, z))


def lois_connues(arch, z):
    return np.stack([p_loi(l, z) for l in arch["lois"]], axis=1)          # (n, J, K)


def partitions(arch, coupes_en_plus=()):
    """Classe du banc : aucune, sous-population, coupures de l'archive, neuf déciles par trait, plus des coupures données."""
    P = [{"sorte": "aucune", "limite": True}, {"sorte": "sp", "limite": False}]
    for j, s in arch["coupes"]:
        P.append({"sorte": "seuil", "j": j, "s": s, "limite": True})
    for j in range(D):
        for s in GRILLE9:
            P.append({"sorte": "seuil", "j": j, "s": s, "limite": False})
    for j, s in coupes_en_plus:
        P.append({"sorte": "seuil", "j": j, "s": s, "limite": False})
    return P


def masque_un(p, z, g):
    if p["sorte"] == "sp":
        return g == 1
    if p["sorte"] == "seuil":
        return z[:, p["j"]] > p["s"]
    if p["sorte"] == "oblique":
        return z[:, 0] + z[:, 1] > 0.0
    return np.zeros(z.shape[0], dtype=bool)


def masques(parts, z, g):
    return np.stack([masque_un(p, z, g) for p in parts], axis=0)


def tirer_plan(rng, n):
    return np.round(rng.normal(size=(n, D)), 6), rng.integers(0, 2, size=n)


def tirer_issues(rng, P):
    u = rng.random(P.shape[0])
    c = np.cumsum(P, axis=1)
    return np.minimum((u[:, None] > c).sum(axis=1), P.shape[1] - 1)


def p_membre(Lz, m, rho, rt, b):
    connu = np.where(m[:, None], np.einsum("j,njk->nk", b[1], Lz), np.einsum("j,njk->nk", b[0], Lz))
    return (1.0 - rho) * connu + rho * rt[None, :]


# ---------------------------------------------------------------------------------------------------------------------
# Maximum de vraisemblance pondéré d'une famille, par lots, avec majorant certifié (écart de Frank-Wolfe)
# ---------------------------------------------------------------------------------------------------------------------
def em(A, y, M, w, K, depart=None, pas_max=160, tol=TOL_EM):
    """A (n, J) : L_j(y_s | x_s) ; y (n,) ; M (P, n) booléen (morceau 1) ; w (L, 1 ou P, n) poids >= 0.

    Paramètres : rho (L, P), rt (L, P, K), b0 et b1 (L, P, J). Rend le majorant certifié U (L, P) de
    sup_theta sum_s w_s log p_theta(y_s | x_s), la valeur atteinte f, les log-probabilités par tirage lp (L, P, n) au point
    atteint, et l'état. Majorant : pour tout point u, log p_v <= log p_u + p_v / p_u - 1 (tangente du logarithme), donc
    sup_v f(v) <= f(u) + max_sommets sum_s w_s p_v(s) / p_u(s) - sum_s w_s ; borné par 0."""
    n, J = A.shape
    P = M.shape[0]
    L = w.shape[0]
    Mf = M[None, :, :]
    Y = np.zeros((n, K))
    Y[np.arange(n), y] = 1.0
    At, Yt = np.ascontiguousarray(A.T), np.ascontiguousarray(Y.T)
    if depart is None:
        rho = np.full((L, P), 0.2)
        rt = np.full((L, P, K), 1.0 / K)
        b0 = np.full((L, P, J), 1.0 / J)
        b1 = np.full((L, P, J), 1.0 / J)
    else:
        rho, rt, b0, b1 = (x.copy() for x in depart)
    W = np.broadcast_to(w.sum(axis=2), (L, P)) if w.shape[1] == P else np.repeat(w.sum(axis=2), P, axis=1)
    W = np.asarray(W, dtype=float)
    Wp = np.maximum(W, 1e-300)
    it = 0
    while True:
        connu = np.where(Mf, b1 @ At, b0 @ At)
        p = np.maximum((1.0 - rho)[..., None] * connu + rho[..., None] * (rt @ Yt), PLANCHER)
        gq = w / p
        S1 = (gq * Mf) @ A
        S0 = gq @ A - S1
        R = gq @ Y
        fini = it >= pas_max
        if not fini and it % 10 == 0 and it > 0:
            ecart = np.maximum(R.max(axis=-1), S0.max(axis=-1) + S1.max(axis=-1)) - W
            fini = float(ecart.max()) < tol
        if fini:
            break
        rho = np.clip(rho * (rt * R).sum(axis=-1) / Wp, 0.0, 1.0)
        rt = rt * R
        rt = rt / np.maximum(rt.sum(axis=-1, keepdims=True), 1e-300)
        for b, S in ((b0, S0), (b1, S1)):
            nb = b * S
            s = nb.sum(axis=-1, keepdims=True)
            np.copyto(b, np.where(s > 0, nb / np.maximum(s, 1e-300), b))
        it += 1
    lp = np.log(p)
    f = (w * lp).sum(axis=-1)
    ecart = np.maximum(R.max(axis=-1), S0.max(axis=-1) + S1.max(axis=-1)) - W
    U = np.minimum(0.0, f + np.maximum(ecart, 0.0))
    return {"U": U, "f": f, "lp": lp, "etat": (rho, rt, b0, b1), "pas": it, "ecart": np.maximum(ecart, 0.0)}


PALIERS = (0.2, 5e-3, 2e-4)      # paliers de la barrière logarithmique (valeurs absolues, en nat)


def newton(A, y, M, w, K, pas_palier=8, pas_final=60, tol=1e-6):
    """Même problème que `em`, résolu par points intérieurs (Newton, barrière logarithmique, deux contraintes d'égalité).

    Paramètres u = (a0 (J), a1 (J), r (K)) >= 0, somme(a0) + somme(r) = 1 et somme(a1) + somme(r) = 1 ;
    p_s = G_s . u est linéaire en u. La valeur rendue est le même majorant certifié que dans `em` (tangente du logarithme
    au point atteint, maximum sur les sommets, grad.u = somme des poids), valable quel que soit l'état de l'optimiseur.
    Sert aux dénominateurs ; `em` reste employé pour les prédicteurs."""
    n, J = A.shape
    P = M.shape[0]
    L = w.shape[0]
    d = 2 * J + K
    G = np.zeros((P, n, d))
    G[:, :, :J] = A[None] * (~M)[:, :, None]
    G[:, :, J:2 * J] = A[None] * M[:, :, None]
    G[:, np.arange(n), 2 * J + y] = 1.0
    Gt = np.ascontiguousarray(G.transpose(0, 2, 1))
    C = np.zeros((2, d))
    C[0, :J] = 1.0
    C[0, 2 * J:] = 1.0
    C[1, J:2 * J] = 1.0
    C[1, 2 * J:] = 1.0
    wl = np.broadcast_to(w, (L, P, n))
    rw = np.sqrt(wl)
    W = wl.sum(axis=-1)
    u = np.empty((L, P, d))
    u[..., :2 * J] = 0.8 / J
    u[..., 2 * J:] = 0.2 / K
    KKT = np.zeros((L, P, d + 2, d + 2))
    KKT[..., :d, d:] = C.T
    KKT[..., d:, :d] = C
    rhs = np.zeros((L, P, d + 2))
    idx = np.arange(d)

    def val(v, mu):
        q = (G @ v[..., None])[..., 0]
        return q, (wl * np.log(q)).sum(axis=-1) + mu * np.log(v).sum(axis=-1)
    tot = 0
    for ip, mu in enumerate(PALIERS):
        dernier = ip == len(PALIERS) - 1
        p, phi = val(u, mu)
        for _ in range(pas_final if dernier else pas_palier):
            g = (Gt @ (wl / p)[..., None])[..., 0] + mu / u
            X = G[None] * (rw / p)[..., None]
            H = X.transpose(0, 1, 3, 2) @ X
            H[..., idx, idx] += mu / u ** 2
            KKT[..., :d, :d] = H
            rhs[..., :d] = g
            dlt = np.linalg.solve(KKT, rhs[..., None])[..., :d, 0]
            dec = (g * dlt).sum(axis=-1)
            tot += 1
            if float(dec.max()) < (tol if dernier else 1e-2):
                break
            neg = dlt < 0
            t = np.minimum(1.0, 0.99 * np.where(neg, u / np.where(neg, -dlt, 1.0), np.inf).min(axis=-1))
            for _ in range(12):
                un = u + t[..., None] * dlt
                pn, phin = val(un, mu)
                ok = phin >= phi + 0.2 * t * dec - 1e-12
                if ok.all():
                    break
                t = np.where(ok, t, 0.5 * t)
            u, p, phi = un, pn, phin
    grad = (Gt @ (wl / p)[..., None])[..., 0]
    lp = np.log(p)
    f = (wl * lp).sum(axis=-1)
    ecart = np.maximum(grad[..., 2 * J:].max(axis=-1), grad[..., :J].max(axis=-1) + grad[..., J:2 * J].max(axis=-1)) - W
    U = np.minimum(0.0, f + np.maximum(ecart, 0.0))
    return {"U": U, "f": f, "lp": lp, "u": u, "pas": tot, "ecart": np.maximum(ecart, 0.0)}


def borne_contrainte(Ae, ye, Me, Ac, yc, Mc, kappas, K, Vc=None, gammas=GAMMAS):
    """Majorant certifié de sup { l_e(theta) : theta dans F_P, l_c(theta) >= kappa }, par partition P et par kappa.

    Dualité faible : pour lambda >= 0, sup_{F_P inter C} l_e <= sup_{F_P} [l_e + lambda l_c] - lambda kappa ; chaque sup est
    majoré par le certificat de `newton` sur les tirages pondérés ; minimum sur la grille de lambda (lambda = 0 : valeur sans
    contrainte). Famille vide si le majorant certifié de sup l_c est sous kappa : -inf.
    Rend aussi un minorant : la meilleure valeur l_e atteinte par un point trouvé qui vérifie l_c >= kappa."""
    ne, nc = Ae.shape[0], Ac.shape[0]
    lam = np.array(gammas) * ne / max(nc, 1)
    L = len(lam)
    A = np.vstack([Ae, Ac])
    y = np.concatenate([ye, yc])
    M = np.hstack([Me, Mc])
    w = np.concatenate([np.ones((L, 1, ne)), lam[:, None, None] * np.ones((L, 1, nc))], axis=2)
    r = newton(A, y, M, w, K)
    fe = r["lp"][:, :, :ne].sum(axis=-1)
    fc = r["lp"][:, :, ne:].sum(axis=-1)
    if Vc is None:
        Vc = newton(Ac, yc, Mc, np.ones((1, 1, nc)), K)["U"][0]
    kap = np.asarray(kappas, dtype=float)
    B = (r["U"][None, :, :] - lam[None, :, None] * kap[:, None, None]).min(axis=1)       # (nk, P)
    B = np.where(Vc[None, :] < kap[:, None], -np.inf, B)
    faisable = fc[None, :, :] >= kap[:, None, None]
    bas = np.where(faisable, fe[None, :, :], -np.inf).max(axis=1)                         # (nk, P)
    return {"B": B, "U0": r["U"][0], "Vc": Vc, "bas": bas, "ecart_max": float(r["ecart"].max()), "pas": r["pas"]}


# ---------------------------------------------------------------------------------------------------------------------
# Prédicteurs (pour les ensembles de confiance)
# ---------------------------------------------------------------------------------------------------------------------
def ajuster(A, y, M, K, pas_max=60):
    """Meilleur membre ajusté (par valeur atteinte) : rend (indice de partition, rho, rt, b0, b1)."""
    r = em(A, y, M, np.ones((1, 1, A.shape[0])), K, pas_max=pas_max)
    i = int(np.argmax(r["f"][0]))
    rho, rt, b0, b1 = r["etat"]
    return i, float(rho[0, i]), rt[0, i].copy(), b0[0, i].copy(), b1[0, i].copy()


def predicteur_defaut(J, K):
    return 0, 0.1, np.full(K, 1.0 / K), np.full(J, 1.0 / J), np.full(J, 1.0 / J)


def log_pred(A, y, M, pred, K):
    """Log-probabilité lissée des issues observées par le membre `pred` : log((1 - eps) p + eps / K)."""
    i, rho, rt, b0, b1 = pred
    connu = np.where(M[i], A @ b1, A @ b0)
    p = (1.0 - rho) * connu + rho * rt[y]
    return np.log((1.0 - EPS_LISSAGE) * p + EPS_LISSAGE / K)


def log_sequentiel(A, y, M, bornes, K):
    """Prédicteur séquentiel prévisible : le bloc [s0, s1) est prédit par le meilleur membre ajusté sur [0, s0)."""
    out = np.empty(A.shape[0])
    for s0, s1 in zip(bornes[:-1], bornes[1:]):
        pred = predicteur_defaut(A.shape[1], K) if s0 == 0 else ajuster(A[:s0], y[:s0], M[:, :s0], K, pas_max=40)
        out[s0:s1] = log_pred(A[s0:s1], y[s0:s1], M[:, s0:s1], pred, K)
    return out


def bornes_blocs(n_tr):
    bloc_tr = BLOC if n_tr <= 250 else n_tr // 10
    return list(range(0, n_tr, bloc_tr)) + list(range(n_tr, n_tr + N, BLOC)) + [n_tr + N]


# ---------------------------------------------------------------------------------------------------------------------
# Un monde préparé et les ensembles de confiance des cinq méthodes
# ---------------------------------------------------------------------------------------------------------------------
class Monde:
    pass


def preparer(rng, arch, parts, p_monde, n_tr):
    m = Monde()
    m.K, m.J, m.parts, m.n_tr = arch["K"], arch["J"], parts, n_tr
    zf, gf = tirer_plan(rng, N)
    m.Pf = p_monde(zf, gf)
    m.yf = tirer_issues(rng, m.Pf)
    zt, gt = tirer_plan(rng, n_tr)
    m.Pt = p_monde(zt, gt)
    m.yt = tirer_issues(rng, m.Pt)
    m.zf, m.gf, m.zt, m.gt = zf, gf, zt, gt
    Lf, Lt = lois_connues(arch, zf), lois_connues(arch, zt)
    m.Lf = Lf
    m.Af = Lf[np.arange(N), :, m.yf]
    m.At = Lt[np.arange(n_tr), :, m.yt]
    m.Mf, m.Mt = masques(parts, zf, gf), masques(parts, zt, gt)
    m.lsf = np.log(np.maximum(m.Pf[np.arange(N), m.yf], PLANCHER))        # log p_monde aux issues fraîches
    m.lst = np.log(np.maximum(m.Pt[np.arange(n_tr), m.yt], PLANCHER))
    return m


def ensembles(m, methodes):
    """Seuils kappa de chaque ensemble de confiance (par beta) ; aucun calcul de maximum contraint ici."""
    K, n_tr = m.K, m.n_tr
    e = {}
    if "BB_T_seq" in methodes or "BB_Q_blocs" in methodes:
        Aseq, yseq, Mseq = np.vstack([m.At, m.Af]), np.concatenate([m.yt, m.yf]), np.hstack([m.Mt, m.Mf])
        lm = log_sequentiel(Aseq, yseq, Mseq, bornes_blocs(n_tr), K)
        cm = np.concatenate([[0.0], np.cumsum(lm)])
        e["seq"] = {"cm": cm, "Aseq": Aseq, "yseq": yseq, "Mseq": Mseq}
        e["BB_T_seq"] = {b: cm[n_tr] - LB[b] for b in BETAS}
        e["BB_Q_blocs"] = {b: [cm[n_tr + t - BLOC] - LB[b] for t in INSTANTS] for b in BETAS}
    if "BB_T_coupe" in methodes:
        h = n_tr // 2
        pred = ajuster(m.At[:h], m.yt[:h], m.Mt[:, :h], K)
        l2 = float(log_pred(m.At[h:], m.yt[h:], m.Mt[:, h:], pred, K).sum())
        e["BB_T_coupe"] = {b: l2 - LB[b] for b in BETAS}
    if "BB_S_moitie" in methodes:
        hf = N // 2
        pred = ajuster(m.At, m.yt, m.Mt, K)
        l2 = float(log_pred(m.Af[:hf], m.yf[:hf], m.Mf[:, :hf], pred, K).sum())
        e["BB_S_moitie"] = {b: l2 - LB[b] for b in BETAS}
    if "BB_A" in methodes:
        lmf = log_sequentiel(m.Af, m.yf, m.Mf, list(range(0, N, BLOC)) + [N], K)
        cmf = np.concatenate([[0.0], np.cumsum(lmf)])
        e["BB_A"] = {b: [cmf[t] - LB[b] for t in INSTANTS] for b in BETAS}
    return e


def couvertures(m, e):
    """theta* (le monde, membre du nul) est-il dans chaque ensemble ? (à tous les blocs ou instants pour Q et A)."""
    n_tr = m.n_tr
    cf = np.concatenate([[0.0], np.cumsum(m.lsf)])
    tot_t = float(m.lst.sum())
    c = {}
    for b in BETAS:
        if "BB_T_seq" in e:
            c[("BB_T_seq", b)] = bool(tot_t >= e["BB_T_seq"][b])
            c[("BB_Q_blocs", b)] = all(tot_t + cf[t - BLOC] >= k for t, k in zip(INSTANTS, e["BB_Q_blocs"][b]))
        if "BB_T_coupe" in e:
            c[("BB_T_coupe", b)] = bool(float(m.lst[n_tr // 2:].sum()) >= e["BB_T_coupe"][b])
        if "BB_S_moitie" in e:
            c[("BB_S_moitie", b)] = bool(cf[N // 2] >= e["BB_S_moitie"][b])
        if "BB_A" in e:
            c[("BB_A", b)] = all(cf[t] >= k for t, k in zip(INSTANTS, e["BB_A"][b]))
    return c


def denominateurs(m, e, methodes, refs=True):
    """Calcul lourd : dénominateurs certifiés D[(méthode, beta)][t] et références ; minorants pour BB_T."""
    K, n_tr = m.K, m.n_tr
    Af, yf, Mf, At, yt, Mt = m.Af, m.yf, m.Mf, m.At, m.yt, m.Mt
    lim = np.array([p["limite"] for p in m.parts])
    Dn, bas, diag = {}, {}, {"ecart_max": 0.0}
    kb = list(BETAS)

    def v9_seul():
        for t in INSTANTS:
            r = newton(Af[:t], yf[:t], Mf[:, :t], np.ones((1, 1, t)), K)
            U0 = r["U"][0]
            Dn.setdefault("v9", {})[t] = float(U0.max())
            Dn.setdefault("limite", {})[t] = float(U0[lim].max())
            Dn.setdefault("v8", {})[t] = float(U0[0])
            diag["ecart_max"] = max(diag["ecart_max"], float(r["ecart"].max()))

    def bb_t(nom, Ac, yc, Mc, kap, avec_refs):
        Vc = None
        for t in INSTANTS:
            r = borne_contrainte(Af[:t], yf[:t], Mf[:, :t], Ac, yc, Mc, kap, K, Vc)
            Vc = r["Vc"]
            diag["ecart_max"] = max(diag["ecart_max"], r["ecart_max"])
            for i, b in enumerate(kb):
                Dn.setdefault((nom, b), {})[t] = float(r["B"][i].max())
                bas.setdefault((nom, b), {})[t] = float(r["bas"][i].max())
            if avec_refs:
                Dn.setdefault("v9", {})[t] = float(r["U0"].max())
                Dn.setdefault("limite", {})[t] = float(r["U0"][lim].max())
                Dn.setdefault("v8", {})[t] = float(r["U0"][0])

    fait_refs = False
    if "BB_T_seq" in methodes:
        bb_t("BB_T_seq", At, yt, Mt, [e["BB_T_seq"][b] for b in kb], True)
        fait_refs = True
    if "BB_T_coupe" in methodes:
        h = n_tr // 2
        bb_t("BB_T_coupe", At[h:], yt[h:], Mt[:, h:], [e["BB_T_coupe"][b] for b in kb], not fait_refs)
        fait_refs = True
    if (refs or "BB_A" in methodes) and not fait_refs:
        v9_seul()
    if "BB_S_moitie" in methodes:
        hf = N // 2
        Vc = None
        kap = [e["BB_S_moitie"][b] for b in kb]
        for t in INSTANTS_2:
            r = borne_contrainte(Af[hf:t], yf[hf:t], Mf[:, hf:t], Af[:hf], yf[:hf], Mf[:, :hf], kap, K, Vc)
            Vc = r["Vc"]
            diag["ecart_max"] = max(diag["ecart_max"], r["ecart_max"])
            for i, b in enumerate(kb):
                Dn.setdefault(("BB_S_moitie", b), {})[t] = float(r["B"][i].max())
    if "BB_Q_blocs" in methodes:
        s = e["seq"]
        acc = {b: 0.0 for b in kb}
        for it, t in enumerate(INSTANTS):
            s0 = t - BLOC
            nc = n_tr + s0
            kap = [e["BB_Q_blocs"][b][it] for b in kb]
            r = borne_contrainte(Af[s0:t], yf[s0:t], Mf[:, s0:t], s["Aseq"][:nc], s["yseq"][:nc], s["Mseq"][:, :nc], kap, K)
            diag["ecart_max"] = max(diag["ecart_max"], r["ecart_max"])
            for i, b in enumerate(kb):
                acc[b] += float(r["B"][i].max())
                Dn.setdefault(("BB_Q_blocs", b), {})[t] = acc[b]
    if "BB_A" in methodes:
        for b in kb:
            Dn[("BB_A", b)] = {t: (-np.inf if Dn["v9"][t] < k else Dn["v9"][t]) for t, k in zip(INSTANTS, e["BB_A"][b])}
    return Dn, bas, diag


def richesse_max(cle, Dt, cq):
    """max sur les instants lus de log q - D ; BB_S_moitie : pari sur la seconde moitié seulement."""
    if isinstance(cle, tuple) and cle[0] == "BB_S_moitie":
        return max(cq[t] - cq[N // 2] - Dt[t] for t in Dt)
    return max(cq[t] - Dt[t] for t in Dt)


def seuil_de(cle):
    return SEUILS[cle[1]] if isinstance(cle, tuple) else SEUIL_V9


def nom_cle(cle):
    return f"{cle[0]}|beta={cle[1]}" if isinstance(cle, tuple) else cle


# ---------------------------------------------------------------------------------------------------------------------
# Artefacts : les deux façons des fiches, sur la partition du monde lui-même
# ---------------------------------------------------------------------------------------------------------------------
def f1_en_ligne(m, masque, eta=0.05):
    """Poids par morceau sur les J lois connues et les K lois certaines, descente exponentielle ; rend log p_w(y_s)."""
    K, J = m.K, m.J
    w = np.full((2, J + K), 1.0 / (J + K))
    lp = np.empty(N)
    for s in range(N):
        c = int(masque[s])
        comp = np.concatenate([m.Af[s], (np.arange(K) == m.yf[s]).astype(float)])
        p = max(PLANCHER, float(w[c] @ comp))
        lp[s] = math.log(p)
        w[c] = w[c] * np.exp(np.minimum(eta * comp / p, 50.0))
        w[c] = w[c] / w[c].sum()
    return lp


def f2_moitie(m, masque):
    """Maximum de vraisemblance de la famille du monde sur y_1..100 ; rend log p_ajusté(y_s) sur y_101..200."""
    h = N // 2
    r = em(m.Af[:h], m.yf[:h], masque[None, :h], np.ones((1, 1, h)), m.K, pas_max=400, tol=1e-5)
    rho, rt, b0, b1 = (x[0, 0] for x in r["etat"])
    connu = np.where(masque[h:], m.Af[h:] @ b1, m.Af[h:] @ b0)
    return np.log(np.maximum((1.0 - rho) * connu + rho * rt[m.yf[h:]], PLANCHER))


# ---------------------------------------------------------------------------------------------------------------------
# Lecture
# ---------------------------------------------------------------------------------------------------------------------
def clopper_pearson(k, n, niveau=0.95):
    from scipy.stats import beta
    a = (1.0 - niveau) / 2.0
    lo = 0.0 if k == 0 else float(beta.ppf(a, k, n - k + 1))
    hi = 1.0 if k == n else float(beta.ppf(1.0 - a, k + 1, n - k))
    return [round(lo, 5), round(hi, 5)]


def taux(k, n):
    return {"k": int(k), "n": int(n), "taux": (round(k / n, 5) if n else None), "ic95": clopper_pearson(int(k), int(n))}


def ecrire(sortie, doc):
    if os.path.exists(sortie):
        raise SystemExit(f"refus : {sortie} existe (jamais d'écrasement)")
    with open(sortie, "w") as fh:
        json.dump(doc, fh, ensure_ascii=False)
    print(f"écrit : {sortie}")


def entete(mode, **k):
    return dict({"essai": "attaque_confiance_v1", "mode": mode, "racine_seedsequence": RACINE,
                 "derivation": "SeedSequence(entropy=RACINE, spawn_key=(mode, indice du cas, monde))",
                 "alpha": ALPHA, "betas": list(BETAS), "instants": list(INSTANTS), "grille9": GRILLE9,
                 "gammas": list(GAMMAS), "eps_lissage": EPS_LISSAGE, "tol_em": TOL_EM,
                 "versions": {"python": platform.python_version(), "numpy": np.__version__}}, **k)


# ---------------------------------------------------------------------------------------------------------------------
# Mode « taille » : monde = membre du nul
# ---------------------------------------------------------------------------------------------------------------------
METHODES = ("BB_A", "BB_T_seq", "BB_T_coupe", "BB_S_moitie", "BB_Q_blocs")
# cas : (J, K, n_tr, forme du monde)
CAS_TAILLE = {
    "copie_interieure": (3, 3, 100, "interieur"),
    "poids_extremes": (3, 3, 100, "sommet"),
    "bord_simplexe": (3, 3, 100, "bord"),
    "morceaux_archive": (3, 3, 100, "morceaux_archive"),
    "morceaux_hors_archive": (3, 3, 100, "morceaux_grille"),
    "sous_population": (3, 3, 100, "sous_population"),
    "beaucoup_de_composantes": (8, 3, 100, "interieur"),
    "peu_de_tirages": (3, 3, 20, "interieur"),
    "peu_de_tirages_morceaux": (3, 3, 20, "morceaux_grille"),
    "bruit_presque_total": (3, 3, 100, "bruit"),
    "quatre_issues_bord": (4, 4, 100, "bord"),
    "seuil_reel_classe_elargie": (3, 3, 100, "morceaux_reel"),
}
NOMS_TAILLE = tuple(CAS_TAILLE)


def tirer_monde_nul(rng, arch, parts, forme):
    """Rend (indice de partition, rho, rt, b (2, J)) d'un membre du nul du banc."""
    J, K = arch["J"], arch["K"]
    e = np.eye(J)
    unif = np.full(K, 1.0 / K)
    grille = [i for i, p in enumerate(parts) if p["sorte"] == "seuil" and not p["limite"]]
    if forme == "interieur":
        bb = rng.dirichlet(np.ones(J))
        return 0, float(rng.uniform(0.05, 0.4)), rng.dirichlet(np.ones(K)), np.stack([bb, bb])
    if forme == "sommet":
        j = int(rng.integers(0, J))
        return 0, 0.0, unif, np.stack([e[j], e[j]])
    if forme == "bord":
        i = int(rng.choice(grille))
        j1, j2 = rng.choice(J, size=2, replace=False)
        a = float(rng.uniform(0.02, 0.98))
        return i, 0.0, unif, np.stack([a * e[j1] + (1 - a) * e[j2], e[int(rng.integers(0, J))]])
    if forme == "morceaux_archive":
        return 2, 0.0, unif, np.stack([e[1], e[0]])
    if forme in ("morceaux_grille", "morceaux_reel"):
        i = len(parts) - 1 if forme == "morceaux_reel" else int(rng.choice(grille))
        return i, 0.0, unif, np.stack([e[1], e[0]])
    if forme == "sous_population":
        return 1, 0.0, unif, np.stack([e[0], e[1]])
    if forme == "bruit":
        bb = rng.dirichlet(np.ones(J))
        return 0, 0.97, np.eye(K)[int(rng.integers(0, K))], np.stack([bb, bb])
    raise ValueError(forme)


def carte_pari(Pf, yf, debut, G):
    """Carte « pari » : à partir de l'instance `debut`, elle mise tout sur l'issue de rang médian de chaque instance, jusqu'à
    ce que le produit des probabilités du monde passe sous 1/G ; ensuite elle copie le monde. Rend log q(y_s) et ce
    produit (= probabilité que la carte gagne tous ses paris ; son rapport de vraisemblance vaut alors 1/produit)."""
    lq = np.log(np.maximum(Pf[np.arange(N), yf], PLANCHER))
    prod, s = 1.0, debut
    while prod > 1.0 / G and s < debut + BLOC - 1:
        k = int(np.argsort(Pf[s])[Pf.shape[1] // 2])
        prod *= float(Pf[s, k])
        lq[s] = 0.0 if yf[s] == k else math.log(PLANCHER)
        s += 1
    return lq, prod


def un_monde_taille(cas, r):
    J, K, n_tr, forme = CAS_TAILLE[cas]
    ss = np.random.SeedSequence(entropy=RACINE, spawn_key=(1, NOMS_TAILLE.index(cas), r))
    rng = np.random.default_rng(ss)
    arch = tirer_archive(rng, J, K)
    en_plus = ()
    if forme == "morceaux_reel":
        # coupure réelle quelconque, hors de la grille et de l'archive ; la classe du banc est élargie à cette coupure
        # (toute coupure réelle est dans le vrai nul v9 ; le calcul sur toutes les coupures n'est pas fait ici)
        en_plus = ((int(rng.integers(0, D)), seuil_libre(rng, GRILLE9 + [s for _, s in arch["coupes"]])),)
    parts = partitions(arch, en_plus)
    i, rho, rt, b = tirer_monde_nul(rng, arch, parts, forme)
    autre = tirer_softmax(rng, K)

    def p_monde(z, g):
        return p_membre(lois_connues(arch, z), masque_un(parts[i], z, g), rho, rt, b)
    m = preparer(rng, arch, parts, p_monde, n_tr)
    pari_d, prod_d = carte_pari(m.Pf, m.yf, 0, 30.0)
    pari_m, prod_m = carte_pari(m.Pf, m.yf, N // 2, 30.0)
    pari_f, prod_f = carte_pari(m.Pf, m.yf, 0, 150.0)
    hc = 0.7 * m.Pf + 0.3 * p_softmax(autre, m.zf)
    logq = {"copie": m.lsf.copy(), "hors_classe": np.log(np.maximum(hc[np.arange(N), m.yf], PLANCHER)),
            "pari_debut": pari_d, "pari_milieu": pari_m, "pari_fort": pari_f}
    cq = {c: np.concatenate([[0.0], np.cumsum(v)]) for c, v in logq.items()}
    cf = np.concatenate([[0.0], np.cumsum(m.lsf)])
    hf = N // 2
    lam = {c: max(cq[c][t] - cf[t] for t in INSTANTS) for c in logq}                       # max log Lambda, 8 instants
    lam2 = {c: max((cq[c][t] - cq[c][hf]) - (cf[t] - cf[hf]) for t in INSTANTS_2) for c in logq}  # seconde moitié
    e = ensembles(m, METHODES)
    couv = couvertures(m, e)
    audit = (r % AUDIT_MODULO == 0)
    smin = min(SEUILS.values())
    besoin = set()
    for meth in METHODES:
        lmax = max((lam2 if meth == "BB_S_moitie" else lam).values())
        if audit or lmax >= smin or not all(couv[(meth, b)] for b in BETAS):
            besoin.add(meth)
    besoin_v9 = audit or max(lam.values()) >= SEUIL_V9
    ligne = {"monde": r, "audit": audit, "non_couvert": [nom_cle(k) for k, v in couv.items() if not v],
             "calcule": sorted(besoin) + (["v9"] if besoin_v9 else []), "promues": [], "marge_min": {},
             "log_lambda_max": {c: round(float(v), 4) for c, v in lam.items()},
             "produit_pari": [round(prod_d, 6), round(prod_m, 6), round(prod_f, 6)]}
    if besoin or besoin_v9:
        Dn, bas, diag = denominateurs(m, e, besoin, refs=besoin_v9)
        ligne["ecart_certificat_max"] = round(diag["ecart_max"], 6)
        for cle, Dt in Dn.items():
            if cle in ("limite", "v8"):
                continue
            nom = nom_cle(cle)
            for c in logq:
                v = richesse_max(cle, Dt, cq[c])
                if v >= seuil_de(cle):
                    ligne["promues"].append([nom, c, round(float(min(v, 1e6)), 4)])
            # audit du certificat : dans un monde couvert, D_t >= l_t(theta*) à chaque instant
            if isinstance(cle, tuple) and cle[0] == "BB_S_moitie":
                marge = min(Dt[t] - (cf[t] - cf[hf]) for t in Dt)
            else:
                marge = min(Dt[t] - cf[t] for t in Dt)
            if cle == "v9" or couv[cle]:
                ligne["marge_min"][nom] = round(float(marge), 5)
        for cle, bt in bas.items():
            ligne.setdefault("jeu_dual_max", {})[nom_cle(cle)] = round(float(max(Dn[cle][t] - bt[t] for t in bt
                                                                             if np.isfinite(bt[t]) and np.isfinite(Dn[cle][t])) if any(np.isfinite(bt[t]) and np.isfinite(Dn[cle][t]) for t in bt) else -1.0), 4)
    # artefacts (peu coûteux) : dans tous les mondes
    masque = m.Mf[i]
    lp1 = f1_en_ligne(m, masque)
    lp2 = f2_moitie(m, masque)
    for c in ("copie", "hors_classe"):
        lw1 = np.cumsum(logq[c] - lp1)
        v1 = max(lw1[t - 1] for t in INSTANTS)
        lw2 = np.cumsum(logq[c][hf:] - lp2)
        v2 = max(lw2[t - hf - 1] for t in INSTANTS_2)
        if v1 >= SEUIL_V9:
            ligne["promues"].append(["F1_en_ligne", c, round(float(v1), 4)])
        if v2 >= SEUIL_V9:
            ligne["promues"].append(["F2_moitie", c, round(float(v2), 4)])
    return ligne, list(ss.spawn_key)


def mode_taille(cas, debut, fin, sortie):
    if os.path.exists(sortie):
        raise SystemExit(f"refus : {sortie} existe")
    t0 = time.time()
    lignes = []
    for r in range(debut, fin):
        ligne, _ = un_monde_taille(cas, r)
        lignes.append(ligne)
    J, K, n_tr, forme = CAS_TAILLE[cas]
    ecrire(sortie, entete("taille", cas=cas, indice_du_cas=NOMS_TAILLE.index(cas), J=J, K=K, n_tr=n_tr, forme=forme,
                          cle_de_graine=[1, NOMS_TAILLE.index(cas), "monde"],
                          mondes=[debut, fin], audit_modulo=AUDIT_MODULO, duree_s=round(time.time() - t0, 1),
                          cartes=["copie", "hors_classe", "pari_debut", "pari_milieu", "pari_fort"], lignes=lignes))


# ---------------------------------------------------------------------------------------------------------------------
# Mode « hors_nul » : monde hors du nul du banc, calcul complet ; cartes membres du nul comprises
# ---------------------------------------------------------------------------------------------------------------------
# cas : (forme, paramètre, n_tr, méthodes)
T2 = ("BB_T_seq", "BB_T_coupe")
CAS_HORS = {
    "V1_0.25_ntr100": ("V1", 0.25, 100, METHODES), "V1_0.50_ntr100": ("V1", 0.50, 100, METHODES),
    "V1_0.75_ntr100": ("V1", 0.75, 100, METHODES),
    "V1_0.25_ntr1000": ("V1", 0.25, 1000, T2), "V1_0.50_ntr1000": ("V1", 0.50, 1000, T2),
    "V1_0.75_ntr1000": ("V1", 0.75, 1000, T2),
    "oblique_ntr100": ("oblique", None, 100, T2), "oblique_ntr1000": ("oblique", None, 1000, T2),
    "seuil_hors_grille_ntr100": ("seuil_hors_grille", None, 100, T2),
}
NOMS_HORS = tuple(CAS_HORS)


def un_monde_hors(cas, r):
    forme, par, n_tr, methodes = CAS_HORS[cas]
    # même graine pour un même monde aux deux tailles d'entraînement : la clé ne dépend pas de n_tr
    cle_cas = {"V1": 10 + int(round((par or 0) * 100)), "oblique": 50, "seuil_hors_grille": 60}[forme]
    ss = np.random.SeedSequence(entropy=RACINE, spawn_key=(2, cle_cas, r))
    rng = np.random.default_rng(ss)
    J, K = 3, 3
    arch = tirer_archive(rng, J, K)
    parts = partitions(arch)
    S1, S2 = arch["lois"][0], arch["lois"][1]
    cartes = {}
    if forme == "V1":
        W1, b1 = S1[1]
        Dl = rng.normal(size=W1.shape)
        Dl = Dl - Dl.mean(axis=0, keepdims=True)
        loi = (W1 + par * Dl, b1)

        def p_monde(z, g):
            return p_softmax(loi, z)
        cartes["membre_copie_S1"] = lambda z, g: p_loi(S1, z)
    elif forme == "oblique":
        def p_monde(z, g):
            return np.where((z[:, 0] + z[:, 1] > 0.0)[:, None], p_loi(S1, z), p_loi(S2, z))
        cartes["membre_coupe_z0"] = lambda z, g: np.where((z[:, 0] > 0.0)[:, None], p_loi(S1, z), p_loi(S2, z))
        cartes["membre_coupe_z1"] = lambda z, g: np.where((z[:, 1] > 0.0)[:, None], p_loi(S1, z), p_loi(S2, z))
        cartes["membre_copie_S1"] = lambda z, g: p_loi(S1, z)
    else:
        j = int(rng.integers(0, D))
        s = seuil_libre(rng, GRILLE9 + [c for _, c in arch["coupes"]])

        def p_monde(z, g):
            return np.where((z[:, j] > s)[:, None], p_loi(S1, z), p_loi(S2, z))
    cartes["monde"] = p_monde
    # carte membre « ajustée » : le meilleur membre du nul du banc, ajusté sur 1 000 tirages du monde tirés à part
    za, ga = tirer_plan(rng, 1000)
    ya = tirer_issues(rng, p_monde(za, ga))
    La = lois_connues(arch, za)
    ia, rho_a, rt_a, b0_a, b1_a = ajuster(La[np.arange(1000), :, ya], ya, masques(parts, za, ga), K, pas_max=200)
    cartes["membre_ajuste"] = lambda z, g: p_membre(lois_connues(arch, z), masque_un(parts[ia], z, g), rho_a, rt_a,
                                                    np.stack([b0_a, b1_a]))
    m = preparer(rng, arch, parts, p_monde, n_tr)
    logq = {c: np.log(np.maximum(f(m.zf, m.gf)[np.arange(N), m.yf], PLANCHER)) for c, f in cartes.items()}
    cq = {c: np.concatenate([[0.0], np.cumsum(v)]) for c, v in logq.items()}
    e = ensembles(m, methodes)
    Dn, bas, diag = denominateurs(m, e, methodes, refs=True)
    ligne = {"monde": r, "ecart_certificat_max": round(diag["ecart_max"], 6), "w": {}}
    for cle, Dt in Dn.items():
        nom = nom_cle(cle)
        ligne["w"][nom] = {c: round(float(max(min(richesse_max(cle, Dt, cq[c]), 1e6), -1e6)), 4) for c in logq}
    ligne["jeu_dual_max"] = {nom_cle(cle): round(float(max([Dn[cle][t] - bt[t] for t in bt
                                                             if np.isfinite(bt[t]) and np.isfinite(Dn[cle][t])] or [-1.0])), 4)
                             for cle, bt in bas.items()}
    return ligne, list(ss.spawn_key)


def mode_hors(cas, debut, fin, sortie):
    if os.path.exists(sortie):
        raise SystemExit(f"refus : {sortie} existe")
    t0 = time.time()
    lignes = [un_monde_hors(cas, r)[0] for r in range(debut, fin)]
    forme, par, n_tr, methodes = CAS_HORS[cas]
    seuils = {"v9": SEUIL_V9, "v8": SEUIL_V9, "limite": SEUIL_V9}
    seuils.update({f"{mth}|beta={b}": SEUILS[b] for mth in methodes for b in BETAS})
    cle_cas = {"V1": 10 + int(round((par or 0) * 100)), "oblique": 50, "seuil_hors_grille": 60}[forme]
    ecrire(sortie, entete("hors_nul", cas=cas, indice_du_cas=NOMS_HORS.index(cas), forme=forme, parametre=par, n_tr=n_tr,
                          cle_de_graine=[2, cle_cas, "monde"],
                          J=3, K=3, methodes=list(methodes), mondes=[debut, fin], seuils_log=seuils,
                          duree_s=round(time.time() - t0, 1), lignes=lignes))


# ---------------------------------------------------------------------------------------------------------------------
# Mode « certificat » : mon majorant contraint contre un solveur convexe indépendant
# ---------------------------------------------------------------------------------------------------------------------
def mode_certificat(sortie, problemes=150):
    from scipy.optimize import minimize
    lignes, viol, marges, jeux = [], 0, [], []
    for r in range(problemes):
        rng = np.random.default_rng(np.random.SeedSequence(entropy=RACINE, spawn_key=(3, 0, r)))
        K, J = 3, 3
        lois = [tirer_softmax(rng, K) for _ in range(J)]
        ne, nc = int(rng.choice([25, 60])), int(rng.choice([20, 50]))

        def tirer(n, th):
            z, g = tirer_plan(rng, n)
            Lz = np.stack([p_softmax(l, z) for l in lois], axis=1)
            m = z[:, 0] > 0.2
            y = tirer_issues(rng, p_membre(Lz, m, *th))
            return Lz[np.arange(n), :, y], y, m
        def th():
            return (float(rng.uniform(0, 0.3)), rng.dirichlet(np.ones(K)), np.stack([rng.dirichlet(np.ones(J) * 0.5) for _ in range(2)]))
        Ae, ye, me = tirer(ne, th())
        Ac, yc, mc = tirer(nc, th())
        supc = float(em(Ac, yc, mc[None, :], np.ones((1, 1, nc)), K, pas_max=3000, tol=1e-7)["f"][0, 0])

        def logv(x, A, y, m):
            rho, rt, b0, b1 = x[0], x[1:1 + K], x[1 + K:1 + K + J], x[1 + K + J:]
            p = (1 - rho) * np.where(m, A @ b1, A @ b0) + rho * rt[y]
            return float(np.log(np.maximum(p, 1e-300)).sum())
        for rayon in (0.3, 1.5, 4.0):
            kappa = supc - rayon
            rb = borne_contrainte(Ae, ye, me[None, :], Ac, yc, mc[None, :], [kappa], K)
            borne, bas = float(rb["B"][0, 0]), float(rb["bas"][0, 0])
            cons = [{"type": "eq", "fun": lambda x: x[1:1 + K].sum() - 1}, {"type": "eq", "fun": lambda x: x[1 + K:1 + K + J].sum() - 1},
                    {"type": "eq", "fun": lambda x: x[1 + K + J:].sum() - 1},
                    {"type": "ineq", "fun": lambda x: logv(x, Ac, yc, mc) - kappa}]
            ref = -np.inf
            for _ in range(6):
                x0 = np.concatenate([[rng.uniform(0, 0.5)], rng.dirichlet(np.ones(K)), rng.dirichlet(np.ones(J)), rng.dirichlet(np.ones(J))])
                s = minimize(lambda x: -logv(x, Ae, ye, me), x0, method="SLSQP", bounds=[(0, 1)] * (1 + K + 2 * J),
                             constraints=cons, options={"maxiter": 400, "ftol": 1e-12})
                x = np.clip(s.x, 0, 1)
                if (abs(x[1:1 + K].sum() - 1) < 1e-6 and abs(x[1 + K:1 + K + J].sum() - 1) < 1e-6
                        and abs(x[1 + K + J:].sum() - 1) < 1e-6 and logv(x, Ac, yc, mc) >= kappa - 1e-7):
                    ref = max(ref, logv(x, Ae, ye, me))
            if np.isfinite(ref) and np.isfinite(borne):
                marges.append(borne - ref)
                viol += int(borne - ref < -1e-6)
                if np.isfinite(bas):
                    jeux.append(borne - max(bas, ref))
            lignes.append({"probleme": r, "ne": ne, "nc": nc, "rayon": rayon, "borne": borne, "minorant": bas, "reference": ref})
    ecrire(sortie, entete("certificat", problemes=problemes, cas_compares=len(marges), violations=viol,
                          marge_min=float(np.min(marges)), marge_mediane=float(np.median(marges)),
                          marge_max=float(np.max(marges)), jeu_median_borne_moins_meilleur_point=float(np.median(jeux)),
                          lignes=lignes))


# ---------------------------------------------------------------------------------------------------------------------
# Mode « exact » : nul jouet à issue binaire, tailles du juge, programmation dynamique (aucune simulation)
# ---------------------------------------------------------------------------------------------------------------------
def _binom_pmf(n, p):
    from scipy.stats import binom
    return binom.pmf(np.arange(n + 1), n, p)


def _ll(k, n, p):
    return k * np.log(p) + (n - k) * np.log1p(-p)


def exact_promotion(p_monde, carte, nul, n1, n2, betas, mode="coupe", masse_min=1e-12):
    """Probabilité exacte de promotion, sous une loi de Bernoulli(p_monde) sans traits.

    nul : liste d'intervalles [a, b] de probabilités (un intervalle = une famille convexe ; un point = [a, a]).
    carte : probabilité constante c de l'issue 1. mode « v9 » : dénominateur = maximum sur tout le nul, seuil 1/alpha ;
    mode « coupe » : m~ = maximum de vraisemblance du nul sur Z1 (n1 tirages), lissé ; C = {p du nul : l_Z2(p) >=
    log m~(Z2) - log(1/beta)} ; dénominateur = maximum sur C (exact : la log-vraisemblance est concave sur chaque
    intervalle) ; seuil 1/(alpha - beta). mode « moitie » (artefact F2) : p^ = maximum de vraisemblance du nul sur les
    100 premiers tirages frais, valeur e sur les suivants, lue aux instants 125 à 200, seuil 1/alpha.
    Rend {beta: (probabilité de promotion, probabilité de non-couverture du monde s'il est dans le nul)}."""
    res = {}
    grille_k = {t: np.arange(t + 1) for t in INSTANTS}

    def mv(k, n):
        """Maximum de vraisemblance du nul sur (k, n) : meilleur point parmi les intervalles (k tableau)."""
        best_p, best_l = None, None
        for a, b in nul:
            ph = np.clip(k / max(n, 1), a, b) if n > 0 else np.full(np.shape(k), (a + b) / 2)
            l = _ll(k, n, ph)
            if best_l is None:
                best_p, best_l = ph, l
            else:
                mieux = l > best_l
                best_p, best_l = np.where(mieux, ph, best_p), np.where(mieux, l, best_l)
        return best_p, best_l

    def sup_sur(k, t, intervalles):
        """max sur une liste d'intervalles [lo, hi] (tableaux, vides si lo > hi) de la log-vraisemblance de (k, t)."""
        out = np.full(k.shape, -np.inf)
        for lo, hi in intervalles:
            ok = lo <= hi
            ph = np.clip(k / t, np.where(ok, lo, 0.5), np.where(ok, hi, 0.5))
            out = np.maximum(out, np.where(ok, _ll(k, t, ph), -np.inf))
        return out

    def dp(promo_t):
        """promo_t[t] : tableau booléen (t + 1,) « promue à l'instant t si le compte vaut k » ; rend P(promotion)."""
        etat = np.array([1.0])
        prev = 0
        pm = _binom_pmf(BLOC, p_monde)
        promue = 0.0
        for t in INSTANTS:
            nouv = np.convolve(etat, pm)
            hit = promo_t[t]
            promue += float(nouv[hit].sum())
            nouv = np.where(hit, 0.0, nouv)
            etat, prev = nouv, t
        return promue

    dans_nul = any(a - 1e-12 <= p_monde <= b + 1e-12 for a, b in nul)
    if mode == "v9":
        promo = {}
        for t in INSTANTS:
            k = grille_k[t]
            promo[t] = _ll(k, t, carte) - mv(k, t)[1] >= SEUIL_V9
        return {"v9": (dp(promo), 0.0)}
    if mode == "moitie":
        h = N // 2
        tot = 0.0
        pm1 = _binom_pmf(h, p_monde)
        for k1 in range(h + 1):
            if pm1[k1] < masse_min:
                continue
            ph = float(mv(np.array([float(k1)]), h)[0][0])
            # valeur e sur la seconde moitié, lue aux instants 125..200 : comptes de la seconde moitié
            etat = np.array([1.0])
            pm = _binom_pmf(BLOC, p_monde)
            promue = 0.0
            for t in INSTANTS_2:
                nouv = np.convolve(etat, pm)
                k = np.arange(t - h + 1)
                hit = _ll(k, t - h, carte) - _ll(k, t - h, ph) >= SEUIL_V9
                promue += float(nouv[hit].sum())
                etat = np.where(hit, 0.0, nouv)
            tot += pm1[k1] * promue
        return {"moitie": (tot, 0.0)}
    pm1, pm2 = _binom_pmf(n1, p_monde), _binom_pmf(n2, p_monde)
    for beta in betas:
        seuil = math.log(1.0 / (ALPHA - beta))
        tot, non_couv = 0.0, 0.0
        for k1 in range(n1 + 1):
            if pm1[k1] < masse_min:
                continue
            ph1 = float(mv(np.array([float(k1)]), n1)[0][0])
            mt = (1.0 - EPS_LISSAGE) * ph1 + EPS_LISSAGE / 2.0
            k2 = np.arange(n2 + 1)
            kappa = _ll(k2, n2, mt) - math.log(1.0 / beta)                 # (n2 + 1,)
            # C par intervalle du nul : {p dans [a, b] : l_Z2(p) >= kappa} = [lo, hi] (concavité) ; résolu par bissection
            inter = []
            for a, b in nul:
                ph2 = np.clip(k2 / n2, a, b)
                ok = _ll(k2, n2, ph2) >= kappa
                lo, hi = np.where(ok, ph2, 1.0), np.where(ok, ph2, 0.0)
                # borne basse : plus petit p de [a, ph2] avec l >= kappa
                x0, x1 = np.full(n2 + 1, a), ph2.copy()
                for _ in range(60):
                    xm = 0.5 * (x0 + x1)
                    bon = _ll(k2, n2, xm) >= kappa
                    x1 = np.where(bon, xm, x1)
                    x0 = np.where(bon, x0, xm)
                lo = np.where(ok, np.where(_ll(k2, n2, np.full(n2 + 1, a)) >= kappa, a, x1), 1.0)
                x0, x1 = ph2.copy(), np.full(n2 + 1, b)
                for _ in range(60):
                    xm = 0.5 * (x0 + x1)
                    bon = _ll(k2, n2, xm) >= kappa
                    x0 = np.where(bon, xm, x0)
                    x1 = np.where(bon, x1, xm)
                hi = np.where(ok, np.where(_ll(k2, n2, np.full(n2 + 1, b)) >= kappa, b, x0), 0.0)
                inter.append((lo, hi))
            couvert = _ll(k2, n2, p_monde) >= kappa if dans_nul else np.ones(n2 + 1, dtype=bool)
            for kk in range(n2 + 1):
                poids = pm1[k1] * pm2[kk]
                if poids < masse_min:
                    continue
                if dans_nul and not couvert[kk]:
                    non_couv += poids
                promo = {}
                for t in INSTANTS:
                    k = grille_k[t].astype(float)
                    d = sup_sur(k, t, [(np.full(t + 1, lo[kk]), np.full(t + 1, hi[kk])) for lo, hi in inter])
                    promo[t] = _ll(k, t, carte) - d >= seuil
                tot += poids * dp(promo)
        res[beta] = (tot, non_couv)
    return res


def mode_exact(partie, sortie):
    """partie « A1 » : taille, 100 tirages de confiance, et artefact F2 ; « A2 » : taille, 1 000 tirages de confiance ;
    « BC » : puissance (B), carte membre du nul dans un monde hors du nul (C), taille sur un nul non convexe (C')."""
    t0 = time.time()
    doc = entete("exact", partie=partie)
    doc["note"] = ("Lois de Bernoulli sans traits ; 200 tirages frais, instants 25 à 200 ; ensemble « coupé » sur n1 + n2 "
                   "tirages de confiance ; probabilités exactes (convolutions de lois binomiales, masse négligée < 1e-12 "
                   "par couple de comptes).")
    blocs = []
    nulA = [(0.3, 0.8)]
    nulC = [(0.3, 0.3), (0.7, 0.7)]
    if partie in ("A1", "A2"):
        # (A) nul convexe [0,3 ; 0,8] : taille exacte de la méthode coupée, cartes constantes, plusieurs mondes du nul
        n1, n2 = (50, 50) if partie == "A1" else (500, 500)
        pire = {b: (0.0, None) for b in BETAS}
        pire_nc = {b: 0.0 for b in BETAS}
        pire_v9 = (0.0, None)
        pire_f2 = (0.0, None)
        mondes = (0.3, 0.35, 0.5, 0.65, 0.8) if n1 == 50 else (0.3, 0.8)
        cartes = ((0.05, 0.15, 0.2, 0.25, 0.3, 0.4, 0.45, 0.5, 0.55, 0.6, 0.7, 0.8, 0.85, 0.9, 0.95) if n1 == 50
                  else (0.15, 0.3, 0.4, 0.5, 0.6, 0.7, 0.85, 0.95))
        for pm in mondes:
            for c in cartes:
                r = exact_promotion(pm, c, nulA, n1, n2, BETAS)
                for b in BETAS:
                    if r[b][0] > pire[b][0]:
                        pire[b] = (r[b][0], [pm, c])
                    pire_nc[b] = max(pire_nc[b], r[b][1])
                if n1 == 50:
                    v = exact_promotion(pm, c, nulA, 0, 0, BETAS, mode="v9")["v9"][0]
                    if v > pire_v9[0]:
                        pire_v9 = (v, [pm, c])
                    f2 = exact_promotion(pm, c, nulA, 0, 0, BETAS, mode="moitie")["moitie"][0]
                    if f2 > pire_f2[0]:
                        pire_f2 = (f2, [pm, c])
        blocs.append({"bloc": "A_taille_nul_convexe", "nul": nulA, "n1": n1, "n2": n2, "mondes": list(mondes),
                      "cartes": list(cartes),
                      "pire_promotion_methode_coupee": {str(b): {"probabilite": pire[b][0], "monde_carte": pire[b][1]} for b in BETAS},
                      "pire_non_couverture": {str(b): pire_nc[b] for b in BETAS},
                      "pire_promotion_v9": {"probabilite": pire_v9[0], "monde_carte": pire_v9[1]} if n1 == 50 else None,
                      "pire_promotion_F2_moitie": {"probabilite": pire_f2[0], "monde_carte": pire_f2[1]} if n1 == 50 else None})
    if partie == "A1":
        # (A') artefact F2 : copie exacte d'un membre du nul
        blocs.append({"bloc": "A_artefact_F2_copie_exacte", "nul": nulA,
                      "promotion_copie": {str(pm): exact_promotion(pm, pm, nulA, 0, 0, BETAS, mode="moitie")["moitie"][0]
                                          for pm in (0.3, 0.4, 0.5, 0.6, 0.7, 0.8)},
                      "promotion_copie_v9": {str(pm): exact_promotion(pm, pm, nulA, 0, 0, BETAS, mode="v9")["v9"][0]
                                             for pm in (0.3, 0.5, 0.8)},
                      "promotion_copie_methode_coupee_n50": {str(pm): {str(b): v[0] for b, v in exact_promotion(pm, pm, nulA, 50, 50, BETAS).items()}
                                                             for pm in (0.3, 0.5, 0.8)}})
    if partie == "BC":
        # (B) puissance : monde hors du nul convexe, carte = monde
        for pm in (0.86, 0.9):
            ligne = {"bloc": "B_puissance_nul_convexe", "nul": nulA, "monde": pm, "carte": pm,
                     "v9": exact_promotion(pm, pm, nulA, 0, 0, BETAS, mode="v9")["v9"][0]}
            for n1, n2 in ((50, 50), (500, 500)):
                r = exact_promotion(pm, pm, nulA, n1, n2, BETAS)
                ligne[f"coupee_n{n1 + n2}"] = {str(b): r[b][0] for b in BETAS}
            blocs.append(ligne)
        # (C) carte MEMBRE du nul dans un monde hors du nul : nul non convexe (deux lois connues sans leurs mélanges)
        for pm, c in ((0.5, 0.7), (0.5, 0.3), (0.45, 0.7), (0.45, 0.3)):
            ligne = {"bloc": "C_carte_membre_monde_hors_nul", "nul": nulC, "monde": pm, "carte": c,
                     "v9": exact_promotion(pm, c, nulC, 0, 0, BETAS, mode="v9")["v9"][0]}
            for n1, n2 in ((50, 50), (500, 500)):
                r = exact_promotion(pm, c, nulC, n1, n2, BETAS)
                ligne[f"coupee_n{n1 + n2}"] = {str(b): r[b][0] for b in BETAS}
            blocs.append(ligne)
        # (C') même nul non convexe, monde DANS le nul : la taille tient (théorème)
        for pm, c in ((0.3, 0.7), (0.3, 0.5), (0.7, 0.3), (0.7, 0.5)):
            ligne = {"bloc": "C_taille_nul_non_convexe", "nul": nulC, "monde": pm, "carte": c}
            for n1, n2 in ((50, 50), (500, 500)):
                r = exact_promotion(pm, c, nulC, n1, n2, BETAS)
                ligne[f"coupee_n{n1 + n2}"] = {str(b): {"promotion": r[b][0], "non_couverture": r[b][1]} for b in BETAS}
            blocs.append(ligne)
    doc["blocs"] = blocs
    doc["duree_s"] = round(time.time() - t0, 1)
    ecrire(sortie, doc)


def main():
    mode = sys.argv[1]
    if mode == "taille":
        mode_taille(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), sys.argv[5])
    elif mode == "hors_nul":
        mode_hors(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), sys.argv[5])
    elif mode == "certificat":
        mode_certificat(sys.argv[2])
    elif mode == "exact":
        mode_exact(sys.argv[2], sys.argv[3])
    else:
        raise SystemExit("modes : taille, hors_nul, certificat, exact")


if __name__ == "__main__":
    main()
