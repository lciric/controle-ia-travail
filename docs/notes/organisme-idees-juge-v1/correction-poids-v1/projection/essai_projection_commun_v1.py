"""Banc commun des essais « projection d'information inverse » (numéraire) — v1.

Mise au point exploratoire, aucune revendication. Processeur seul. Aucun code du juge n'est exécuté : la logique utile
est recopiée et simplifiée ici (dit dans methodes-projection-v1.md, section 2) :
- plan de n = 200 instances x_s = (z_s, g_s), z ~ N(0, 1) sur 2 traits, g uniforme sur {0, 1} ; K = 3 issues ;
- instants de lecture T = {25, 50, ..., 200} (comme `cycle.instants_reguliers(200, 8)`), alpha = 0,05, promotion si
  log W_t >= log(1/alpha) pour un t de T (règle de `nul_filles_v2.evaluer_v2`, carte seule, pari plein) ;
- archive A2 du préenregistrement de l'idée 1.1 : S1, S2 softmax aléatoires ; S3 = si_sinon(z_jA > s_A, U1, U2) ;
  S4 = si_sinon(z_(1-jA) > s_B, U3, U4) ; lois connues L_1..L_4 = S1..S4 ;
- familles du nul, linéaires en leurs poids (θ) :
  * « bruit commun » (forme du membre linéaire du v8 et des membres par morceaux du v9) : pour une partition en cellules,
    P_θ(y | x) = Σ_j π_{c(x), j} L_j(y | x) + ρ_y, avec Σ_j π_{c,j} + Σ_k ρ_k = 1 pour chaque cellule c ;
    paramétrage employé : ρ = τ·u, π_c = (1 − τ)·v_c (même famille) ;
  * « bruit par cellule » (forme des fiches argon-p1-01 et argon-p2-01) : P_θ(y | x) = Σ_v θ_{c(x), v} G_v(y | x) sur
    les J lois connues et les K lois certaines δ_k, un simplexe par cellule.
Les membres ordinaires du v8 autres que le membre linéaire (moyennes glissantes, log-linéaire, marginale d'entraînement)
ne sont pas au banc : ils entreraient à l'identique dans tous les bras (minimum), sans rien changer à la comparaison.
"""
import math
import time

import numpy as np

K, D, N, ALPHA = 3, 2, 200, 0.05
J = 4
T = np.arange(25, N + 1, 25)
BLOCS = [(a - 25, a) for a in T]          # blocs alignés sur les instants de lecture
SEUIL = math.log(1 / ALPHA)
PLANCHER = 1e-300


# --------------------------------------------------------------------------------------------------------------------
# lois du banc
def softmax_param(rng):
    return rng.normal(0, 1.5, (K, D)), rng.normal(0, 0.3, K)


def p_softmax(par, z):
    W, b = par
    s = z @ W.T + b
    s = s - s.max(1, keepdims=True)
    e = np.exp(s)
    return e / e.sum(1, keepdims=True)


def si_sinon(masque, p_vrai, p_faux):
    return np.where(masque[:, None], p_vrai, p_faux)


def tirer_plan(rng, n=N):
    return np.round(rng.normal(size=(n, D)), 6), rng.integers(0, 2, n)


def seuil_archive(rng):
    while True:
        s = round(float(rng.uniform(-1, 1)), 2)
        if abs(s) >= 0.05:
            return s


def tirer_archive(rng):
    """Paramètres de l'archive A2 (fonctions du plan)."""
    a = dict(S1=softmax_param(rng), S2=softmax_param(rng), U=[softmax_param(rng) for _ in range(4)],
             jA=int(rng.integers(0, 2)), sA=seuil_archive(rng), sB=seuil_archive(rng))
    return a


def lois_connues(a, z):
    """(n, J, K) : S1, S2, S3, S4 aux instances du plan."""
    S1, S2 = p_softmax(a["S1"], z), p_softmax(a["S2"], z)
    U = [p_softmax(u, z) for u in a["U"]]
    jA, jB = a["jA"], 1 - a["jA"]
    S3 = si_sinon(z[:, jA] > a["sA"], U[0], U[1])
    S4 = si_sinon(z[:, jB] > a["sB"], U[2], U[3])
    return np.stack([S1, S2, S3, S4], 1)


def cellules_archive(a, z):
    """Coupures de l'archive : A (z_jA > s_A), B (z_jB > s_B), et leur partition commune à 4 cellules."""
    cA = (z[:, a["jA"]] > a["sA"]).astype(int)
    cB = (z[:, 1 - a["jA"]] > a["sB"]).astype(int)
    return cA, cB, 2 * cA + cB


def tirer_issues(rng, P):
    u = rng.random(P.shape[0])
    return np.minimum((u[:, None] > np.cumsum(P, 1)).sum(1), K - 1)


# --------------------------------------------------------------------------------------------------------------------
# EM pondéré, famille « bruit commun », vectorisé sur F familles (même ensemble d'instances, cellules différentes)
def em_commun(G, Ind, Wt, cells, C, iterations=300, depart=None, accelere=True):
    """Maximise Σ_{s,y} Wt[s,y]·log P_θ(y | s) sur la famille « bruit commun », pour F familles à la fois.
    G (S, Y, J) ou (F, S, Y, J) : lois connues aux couples (s, y) ; Ind (S, Y, K) ou (F, S, Y, K) : indicatrice de
    l'issue ; Wt (S, Y) ou (F, S, Y) : poids (issue observée : Y = 1, poids 1 ; projection : Y = K, poids q_s(y)) ;
    cells (F, S) ; rend (tau, v, u, valeur). Pas d'EM du modèle à variables cachées « loi connue j de la cellule » ou
    « loi certaine k », avec ρ = τ·u et π_c = (1 − τ)·v_c ; accélération SQUAREM (Varadhan et Roland) avec garde : un
    pas accéléré n'est gardé que s'il ne fait pas baisser la valeur. `iterations` compte les pas d'EM."""
    F, S = cells.shape
    G = np.broadcast_to(G, (F,) + G.shape[-3:])
    yk = np.broadcast_to(np.asarray(Ind).argmax(-1), (F,) + np.asarray(Ind).shape[-3:-1])     # (F, S, Y)
    Wt = np.broadcast_to(Wt, (F,) + Wt.shape[-2:])
    ohT = np.zeros((F, C, S))
    ohT[np.arange(F)[:, None], cells, np.arange(S)[None, :]] = 1.0
    if depart is None:
        x = (np.full(F, 0.1), np.full((F, C, J), 1.0 / J), np.full((F, K), 1.0 / K))
    else:
        x = tuple(np.array(t, dtype=float) for t in depart)
    tot = Wt.sum((1, 2))
    fi = np.arange(F)[:, None]
    fi3 = np.arange(F)[:, None, None]
    masques = [(yk == k) for k in range(K)]

    def probas(x):
        tau, v, u = x
        vs = v[fi, cells]                                     # (F, S, J)
        Pk = (1 - tau)[:, None, None] * (G @ vs[..., None])[..., 0]      # (F, S, Y)
        B = tau[:, None, None] * u[fi3, yk]
        return vs, Pk, B

    def valeur(x):
        _, Pk, B = probas(x)
        return (Wt * np.log(np.maximum(Pk + B, PLANCHER))).sum((1, 2))

    def pas(x):
        tau, v, u = x
        vs, Pk, B = probas(x)
        wr = Wt / np.maximum(Pk + B, PLANCHER)
        RA = (1 - tau)[:, None, None] * vs * (wr[:, :, None, :] @ G)[:, :, 0, :]    # (F, S, J)
        RB = B * wr
        vn = ohT @ RA
        sv = vn.sum(-1, keepdims=True)
        v = np.where(sv > 0, vn / np.maximum(sv, PLANCHER), v)
        un = np.stack([(RB * mk).sum((1, 2)) for mk in masques], -1)
        bt = un.sum(-1)
        u = np.where(bt[:, None] > 0, un / np.maximum(bt[:, None], PLANCHER), u)
        tau = np.clip(bt / tot, 1e-12, 1 - 1e-12)
        return tau, v, u

    def admissible(x):
        tau, v, u = x
        tau = np.clip(tau, 1e-12, 1 - 1e-12)
        v = np.maximum(v, 1e-300); v = v / v.sum(-1, keepdims=True)
        u = np.maximum(u, 1e-300); u = u / u.sum(-1, keepdims=True)
        return tau, v, u

    def choisir(m, a, b):
        return tuple(np.where(m.reshape((F,) + (1,) * (t.ndim - 1)), t, w) for t, w in zip(a, b))

    faits = 0
    if not accelere:
        while faits < iterations:
            x = pas(x); faits += 1
    while accelere and faits + 3 <= iterations:
        x1 = pas(x); x2 = pas(x1)
        r = [b - a for a, b in zip(x, x1)]
        w = [c - 2 * b + a for a, b, c in zip(x, x1, x2)]
        nr = np.sqrt(sum((t.reshape(F, -1) ** 2).sum(1) for t in r))
        nw = np.sqrt(sum((t.reshape(F, -1) ** 2).sum(1) for t in w))
        al = np.minimum(-nr / np.maximum(nw, 1e-300), -1.0)
        def comb(a, rr, ww):
            sh = (F,) + (1,) * (a.ndim - 1)
            return a - 2 * al.reshape(sh) * rr + (al ** 2).reshape(sh) * ww
        with np.errstate(over="ignore", invalid="ignore"):
            brut = tuple(comb(a, rr, ww) for a, rr, ww in zip(x, r, w))
        interieur = np.isfinite(al) & (brut[0] > 0) & (brut[0] < 1)
        for t in brut[1:]:
            interieur &= np.all(np.isfinite(t.reshape(F, -1)) & (t.reshape(F, -1) > 0), 1)
        xa = admissible(choisir(interieur, brut, x2))
        x3 = pas(xa)
        ok = interieur & (valeur(x3) >= valeur(x2))
        x = choisir(ok, x3, x2)
        faits += 3
    tau, v, u = x
    P = probas_commun(G, Ind, cells, C, x)
    val = (Wt * np.log(np.maximum(P, PLANCHER))).sum((1, 2))
    return tau, v, u, val


def probas_commun(G, Ind, cells, C, par):
    tau, v, u = par
    F, S = cells.shape
    G = np.broadcast_to(G, (F,) + G.shape[-3:])
    yk = np.broadcast_to(np.asarray(Ind).argmax(-1), (F,) + np.asarray(Ind).shape[-3:-1])
    vs = v[np.arange(F)[:, None], cells]                      # (F, S, J)
    A = (1 - tau)[:, None, None] * (G @ vs[..., None])[..., 0]
    B = tau[:, None, None] * u[np.arange(F)[:, None, None], yk]
    return A + B


def certificat_commun(Gk, Q, P, cells, C):
    """c = max_θ (1/b) Σ_s E_{P_θ}[q_s / P_φ] sur la famille « bruit commun », calculé exactement aux sommets du polytope
    (une loi connue par cellule, ou une loi certaine δ_k). Gk (S, K, J) ou (F, S, K, J) ; Q (S, K) ou (F, S, K) loi de la
    carte ; P (F, S, K) loi φ ; rend (F,)."""
    F, S = cells.shape
    Gk = np.broadcast_to(Gk, (F,) + Gk.shape[-3:])
    Q = np.broadcast_to(Q, (F,) + Q.shape[-2:])
    r = Q / np.maximum(P, PLANCHER)                           # (F, S, K)
    M = (r[:, :, None, :] @ Gk)[:, :, 0, :]                   # (F, S, J) : Σ_y Gk[s, y, j]·r[s, y]
    ohT = np.zeros((F, C, S))
    ohT[np.arange(F)[:, None], cells, np.arange(S)[None, :]] = 1.0
    connues = (ohT @ M).max(-1).sum(-1)
    aveugles = r.sum(1).max(-1)
    return np.maximum(connues, aveugles) / S


# famille « bruit par cellule » (fiches)
def em_cellule(Gf, Wt, cells, C, iterations=300, depart=None):
    """Gf (S, Y, V) composantes (J lois connues puis K lois certaines) ; cells (F, S) ; rend (theta (F, C, V), valeur)."""
    F, S = cells.shape
    V = Gf.shape[-1]
    oh = np.zeros((F, S, C))
    oh[np.arange(F)[:, None], np.arange(S)[None, :], cells] = 1.0
    th = np.full((F, C, V), 1.0 / V) if depart is None else np.array(depart, dtype=float)
    for _ in range(iterations):
        ts = np.einsum("fsc,fcv->fsv", oh, th)
        A = ts[:, :, None, :] * Gf[None]
        P = A.sum(-1)
        R = (A * (Wt[None] / np.maximum(P, PLANCHER))[..., None]).sum(2)
        tn = np.einsum("fsc,fsv->fcv", oh, R)
        st = tn.sum(-1, keepdims=True)
        th = np.where(st > 0, tn / np.maximum(st, PLANCHER), th)
    P = probas_cellule(Gf, cells, th)
    val = (Wt[None] * np.log(np.maximum(P, PLANCHER))).sum((1, 2))
    return th, val


def probas_cellule(Gf, cells, th):
    F, S = cells.shape
    ts = th[np.arange(F)[:, None], cells]
    return np.einsum("fsv,syv->fsy", ts, Gf)


def certificat_cellule(Gfk, Q, P, cells, C):
    F, S = cells.shape
    r = Q[None] / np.maximum(P, PLANCHER)
    M = np.einsum("syv,fsy->fsv", Gfk, r)
    oh = np.zeros((F, S, C))
    oh[np.arange(F)[:, None], np.arange(S)[None, :], cells] = 1.0
    return np.einsum("fsc,fsv->fcv", oh, M).max(-1).sum(-1) / S


# --------------------------------------------------------------------------------------------------------------------
# outils de données
def tenseurs(L, y=None):
    """Formes pour les EM : projection (toutes issues) ou maximum de vraisemblance (issue observée)."""
    S = L.shape[0]
    eyeK = np.eye(K)
    if y is None:
        G = np.transpose(L, (0, 2, 1))                        # (S, K, J) : G[s, y, j] = L_j(y | s)
        Ind = np.broadcast_to(eyeK[None], (S, K, K)).copy()
        return G, Ind
    G = L[np.arange(S), :, y][:, None, :]                     # (S, 1, J)
    Ind = eyeK[y][:, None, :]                                 # (S, 1, K)
    return G, Ind


def composantes(L):
    """(S, K, J + K) : lois connues puis lois certaines, à toutes les issues."""
    S = L.shape[0]
    G = np.transpose(L, (0, 2, 1))
    return np.concatenate([G, np.broadcast_to(np.eye(K)[None], (S, K, K))], -1)


def log_q_issues(Q, y):
    return np.log(np.maximum(Q[np.arange(len(y)), y], PLANCHER))


def promue(logw_aux_instants, seuil=SEUIL):
    return bool(np.max(logw_aux_instants) >= seuil)


class Chrono:
    def __init__(self):
        self.t = {}

    def ajoute(self, nom, dt):
        self.t[nom] = self.t.get(nom, 0.0) + dt


def clopper_pearson(k, n, niveau=0.95):
    from scipy.stats import beta
    a = (1 - niveau) / 2
    bas = 0.0 if k == 0 else float(beta.ppf(a, k, n - k + 1))
    haut = 1.0 if k == n else float(beta.ppf(1 - a, k + 1, n - k))
    return [round(bas, 4), round(haut, 4)]
