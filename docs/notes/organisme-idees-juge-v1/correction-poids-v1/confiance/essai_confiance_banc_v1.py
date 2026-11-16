"""Banc commun des essais « ensemble de confiance pour les poids, puis maximum sur cet ensemble » — v1.

Mise au point exploratoire, aucune revendication. Processeur seul. Aucun fichier des dossiers de copie n'est exécuté :
la logique utile du juge est **recopiée et simplifiée** ici, d'après la lecture de
`copie-nul-v9-a41b7b5/orchestrator/pole/nul_v9.py` (famille par morceaux à un niveau, bruit aveugle commun à tous les
morceaux, certificat de Frank-Wolfe, borne par 0) et de `code-organisme-94bfd92/orchestrator/pole/` (`selection_pari.py` :
richesse W_t = q(y_1..t) / max du nul, tirages frais après le gel ; `nul_filles_v2.py` : membre linéaire certifié, lecture
aux instants fixés ; `a_blanc_v59.py` : 100 instances d'entraînement tirées du monde, 200 tirages frais, alpha = 0,05 ;
`cycle.instants_reguliers(200, 8)` : instants 25, 50, ..., 200).

Simplifications déclarées (le banc n'est pas le juge) :
- K = 3 issues, 2 traits z ~ N(0, 1), une sous-population g dans {0, 1} ; pari plein (numérateur = loi de la carte) ;
- lois connues : S1, S2 softmax aléatoires, S3 = si_sinon(z_jA > s_A, U1, U2) ; pour J = 6 : plus S4, S5 softmax et
  S6 = si_sinon(z_(1-jA) > s_B, U3, U4) ;
- membres du nul : seulement la famille « mélange des lois connues + bruit aveugle commun » sur une partition à deux
  morceaux au plus (le membre linéaire du v8 = partition « aucune ») ; membres log-linéaires du v8 absents ;
- « v9 du banc » : partitions = aucune, sous-population, coupure(s) de l'archive, et coupures sur une **grille fixe** de
  neuf seuils par trait (déciles de N(0, 1)), non sur tout seuil réel ; le prix en puissance du vrai v9 est au moins celui
  du banc (plus de coupures, plus de surajustement) ;
- « limité » : partitions = aucune et coupure(s) de l'archive ; « v8 du banc » : partition aucune seule.

Calcul du maximum certifié (comme nul_v9) : algorithme EM multiplicatif (montée monotone), puis certificat de Frank-Wolfe
f(u) + max_sommets grad f(u).(v - u), avec grad f(u).u = somme des poids (homogénéité), borné par 0. Valide quel que
soit l'état de l'optimiseur : un arrêt précoce coûte en puissance, jamais en validité.

Maximum sur un ensemble de confiance C = {theta : l_c(theta) >= kappa} (l_c : log-vraisemblance sur des tirages de
confiance, disjoints des tirages évalués) : borne certifiée par dualité faible de Lagrange,
sup_{theta in F_P inter C} l_e(theta) <= sup_{theta in F_P} [l_e(theta) + lambda (l_c(theta) - kappa)] pour tout lambda >= 0,
chaque sup étant lui-même majoré par le certificat de Frank-Wolfe du problème pondéré ; on prend le minimum sur une grille
de lambda (lambda = 0 rend la valeur du v9 du banc : jamais pire). Famille vide (certificat de sup l_c < kappa) : -inf.
"""

import math
import time

import numpy as np

K, D, N = 3, 2, 200
ALPHA = 0.05
INSTANTS = tuple(range(25, N + 1, 25))
PLANCHER = 1e-12
GRILLE = (-1.2816, -0.8416, -0.5244, -0.2533, 0.0, 0.2533, 0.5244, 0.8416, 1.2816)  # déciles de N(0, 1)
ITER = 80             # pas d'EM par résolution (avec départ chaud d'un instant au suivant)
GAMMAS = (0.0, 0.3, 1.0, 3.0)   # grille de lambda, en unités de n_e / n_c
BETAS = (0.01, 0.025)  # part du niveau payée pour l'ensemble de confiance ; niveau du pari alpha' = alpha - beta
EPS_PREQ = 0.002       # lissage vers l uniforme du prédicteur séquentiel ; 0,02 au pilote de 3 mondes, abaissé car il coûte jusqu à 0,02 nat par tirage au seuil kappa
BLOC_PREQ = 25         # le prédicteur séquentiel est réajusté tous les 25 tirages


# --- lois ---------------------------------------------------------------------------------------------------------------
def softmax_par(rng):
    return rng.normal(0.0, 1.5, size=(K, D)), rng.normal(0.0, 0.3, size=K)


def probas_softmax(par, z):
    W, b = par
    s = z @ W.T + b
    s = s - s.max(axis=1, keepdims=True)
    e = np.exp(s)
    return e / e.sum(axis=1, keepdims=True)


def _seuil_hors_grille(rng):
    while True:
        s = round(float(rng.uniform(-1.0, 1.0)), 2)
        if abs(s) >= 0.05 and min(abs(s - c) for c in GRILLE) >= 0.05:
            return s


def tirer_archive(rng, J=3):
    a = {"J": J, "S1": softmax_par(rng), "S2": softmax_par(rng), "U1": softmax_par(rng), "U2": softmax_par(rng),
         "jA": int(rng.integers(0, D)), "sA": _seuil_hors_grille(rng)}
    if J == 6:
        a.update({"S4": softmax_par(rng), "S5": softmax_par(rng), "U3": softmax_par(rng), "U4": softmax_par(rng),
                  "sB": _seuil_hors_grille(rng)})
    elif J != 3:
        raise ValueError("J = 3 ou 6")
    return a


def lois_connues(arch, z):
    """(n, J, K) : probabilités de chaque loi connue aux instances z."""
    p1, p2 = probas_softmax(arch["S1"], z), probas_softmax(arch["S2"], z)
    h = z[:, arch["jA"]] > arch["sA"]
    p3 = np.where(h[:, None], probas_softmax(arch["U1"], z), probas_softmax(arch["U2"], z))
    lois = [p1, p2, p3]
    if arch["J"] == 6:
        hb = z[:, 1 - arch["jA"]] > arch["sB"]
        lois += [probas_softmax(arch["S4"], z), probas_softmax(arch["S5"], z),
                 np.where(hb[:, None], probas_softmax(arch["U3"], z), probas_softmax(arch["U4"], z))]
    return np.stack(lois, axis=1)


def partitions(arch):
    """Liste des partitions du v9 du banc ; champ 'groupe' : v8 (aucune), limite (aucune + coupures de l'archive), v9."""
    P = [{"nom": "aucune", "sorte": "aucune", "limite": True}]
    P.append({"nom": "sous_population", "sorte": "sp", "limite": False})
    P.append({"nom": f"archive:z{arch['jA']}>{arch['sA']}", "sorte": "seuil", "j": arch["jA"], "s": arch["sA"], "limite": True})
    if arch["J"] == 6:
        P.append({"nom": f"archive:z{1 - arch['jA']}>{arch['sB']}", "sorte": "seuil", "j": 1 - arch["jA"], "s": arch["sB"],
                  "limite": True})
    for j in range(D):
        for s in GRILLE:
            P.append({"nom": f"grille:z{j}>{s}", "sorte": "seuil", "j": j, "s": s, "limite": False})
    return P


def masques(parts, z, g):
    """(P, n) booléen : l'instance est dans le morceau 1."""
    M = np.zeros((len(parts), z.shape[0]), dtype=bool)
    for i, p in enumerate(parts):
        if p["sorte"] == "sp":
            M[i] = g == 1
        elif p["sorte"] == "seuil":
            M[i] = z[:, p["j"]] > p["s"]
    return M


def tirer_plan(rng, n):
    return np.round(rng.normal(size=(n, D)), 6), rng.integers(0, 2, size=n)


def tirer_issues(rng, P):
    u = rng.random(P.shape[0])
    return np.minimum((u[:, None] > np.cumsum(P, axis=1)).sum(axis=1), K - 1)


# --- membres du nul (loi d'un point theta de la famille d'une partition) -------------------------------------------------
def probas_membre(Lz, masque, rho, rt, b):
    """Lz (n, J, K) lois connues ; masque (n,) morceau 1 ; rho part aveugle ; rt (K,) loi aveugle ; b (2, J) poids."""
    known = np.where(masque[:, None], np.einsum("j,njk->nk", b[1], Lz), np.einsum("j,njk->nk", b[0], Lz))
    return (1.0 - rho) * known + rho * rt[None, :]


# --- maximum certifié (EM + certificat de Frank-Wolfe), par lots -----------------------------------------------------------
def em_certifie(A, y, w, M, iters=ITER, init=None):
    """A (n, J) = L_j(y_s | x_s) aux issues observées ; y (n,) ; w (L, n) poids >= 0 ; M (P, n) morceau 1.

    Rend U (L, P) : majorant certifié de sup_{theta in F_P} sum_s w_s log p_theta(y_s | x_s), atteint (L, P) (valeur au
    point courant), et les paramètres (pour un départ chaud)."""
    L, n = w.shape
    P = M.shape[0]
    J = A.shape[1]
    Mf = M.astype(float)[None, :, :]
    Y = np.zeros((n, K))
    Y[np.arange(n), y] = 1.0
    if init is None:
        rho = np.full((L, P), 0.2)
        rt = np.full((L, P, K), 1.0 / K)
        b = np.full((L, P, 2, J), 1.0 / J)
    else:
        rho, rt, b = (x.copy() for x in init)
    W = w.sum(axis=1)[:, None]
    wb = w[:, None, :]
    for it in range(iters + 1):
        k0 = b[:, :, 0, :] @ A.T
        k1 = b[:, :, 1, :] @ A.T
        known = k0 + Mf * (k1 - k0)
        blind = rt @ Y.T
        p = np.maximum((1.0 - rho)[..., None] * known + rho[..., None] * blind, PLANCHER)
        q = wb / p
        S1 = (q * Mf) @ A
        S0 = q @ A - S1
        R = q @ Y
        if it == iters:
            break
        tot_b = (rt * R).sum(axis=-1)
        rho = np.clip(rho * tot_b / np.maximum(W, 1e-300), 0.0, 1.0)
        rt = rt * R
        rt = rt / np.maximum(rt.sum(axis=-1, keepdims=True), 1e-300)
        for c, S in ((0, S0), (1, S1)):
            nb = b[:, :, c, :] * S
            s = nb.sum(axis=-1, keepdims=True)
            b[:, :, c, :] = np.where(s > 0, nb / np.maximum(s, 1e-300), b[:, :, c, :])
    f = (wb * np.log(p)).sum(axis=-1)
    gap = np.maximum(R.max(axis=-1), S0.max(axis=-1) + S1.max(axis=-1)) - W
    U = np.minimum(0.0, f + np.maximum(gap, 0.0))
    return U, f, (rho, rt, b)


def lignes(Lz, y):
    """A (n, J) = L_j(y_s | x_s)."""
    return Lz[np.arange(Lz.shape[0]), :, y]


def borne_sur_ensemble(Ae, ye, Me, Ac, yc, Mc, kappas, iters=ITER, init=None, Vc=None):
    """Majorant certifié de sup_{theta in F_P inter C} l_e(theta), C = {l_c >= kappa}, pour chaque kappa et chaque P.

    Rend B (len(kappas), P) (avec -inf pour une famille vide), U0 (P,) = sup certifié sans contrainte (v9 du banc par
    partition), les paramètres, et Vc (P,) = sup certifié de l_c (calculé une fois par jeu de confiance)."""
    ne, nc = Ae.shape[0], Ac.shape[0]
    lam = np.array(GAMMAS) * ne / max(nc, 1)
    A = np.vstack([Ae, Ac])
    y = np.concatenate([ye, yc])
    M = np.hstack([Me, Mc])
    w = np.hstack([np.ones((len(lam), ne)), lam[:, None] * np.ones((len(lam), nc))])
    U, _, par = em_certifie(A, y, w, M, iters, init)
    if Vc is None:
        Vc, _, _ = em_certifie(Ac, yc, np.ones((1, nc)), Mc, iters)
        Vc = Vc[0]
    kap = np.asarray(kappas, dtype=float)
    B = (U[None, :, :] - lam[None, :, None] * kap[:, None, None]).min(axis=1)
    B = np.where(Vc[None, :] < kap[:, None], -np.inf, B)
    return B, U[0], par, Vc


# --- prédicteurs séquentiels (pour les ensembles de confiance) --------------------------------------------------------------
def ajuster_meilleur(A, y, M, iters=ITER):
    """Ajuste chaque famille sur (A, y) et rend (indice de la meilleure partition par valeur atteinte, paramètres)."""
    _, f, (rho, rt, b) = em_certifie(A, y, np.ones((1, A.shape[0])), M, iters)
    i = int(np.argmax(f[0]))
    return i, (float(rho[0, i]), rt[0, i].copy(), b[0, i].copy())


def proba_lissee(A, y, M, i, par):
    """Probabilité lissée, par le membre (i, par), des issues observées : (1 - eps) p + eps / K."""
    rho, rt, b = par
    m = M[i]
    known = np.where(m, A @ b[1], A @ b[0])
    p = (1.0 - rho) * known + rho * rt[y]
    return (1.0 - EPS_PREQ) * p + EPS_PREQ / K


def log_prequentiel(A, y, M, bloc=BLOC_PREQ, iters=60):
    """Log-probabilité séquentielle (prévisible) de chaque issue : le prédicteur des issues du bloc [s0, s0 + bloc) est le
    meilleur membre ajusté sur les issues [0, s0), lissé ; avant toute issue : poids uniformes, rho = 0,1."""
    n, J = A.shape
    out = np.empty(n)
    defaut = (0.1, np.full(K, 1.0 / K), np.full((2, J), 1.0 / J))
    for s0 in range(0, n, bloc):
        s1 = min(n, s0 + bloc)
        if s0 == 0:
            i, par = 0, defaut
        else:
            i, par = ajuster_meilleur(A[:s0], y[:s0], M[:, :s0], iters)
        out[s0:s1] = np.log(proba_lissee(A[s0:s1], y[s0:s1], M[:, s0:s1], i, par))
    return out


# --- lecture --------------------------------------------------------------------------------------------------------------
def clopper_pearson(k, n, niveau=0.95):
    from scipy.stats import beta
    a = (1 - niveau) / 2
    lo = 0.0 if k == 0 else float(beta.ppf(a, k, n - k + 1))
    hi = 1.0 if k == n else float(beta.ppf(1 - a, k + 1, n - k))
    return [round(lo, 4), round(hi, 4)]


def taux(k, n):
    return {"promues": int(k), "mondes": int(n), "taux": round(k / n, 4) if n else None,
            "intervalle_95_clopper_pearson": clopper_pearson(int(k), int(n))}


def chrono():
    return time.perf_counter()


SEUIL = math.log(1.0 / ALPHA)
