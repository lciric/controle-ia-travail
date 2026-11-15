"""Banc commun des essais « poids appris en ligne corrigés par une borne de regret » — v1.

Mise au point exploratoire, aucune revendication. Processeur seul, numpy et scipy seulement ; aucun fichier des dossiers de
copie n'est exécuté ni importé : la logique utile du juge est **recopiée** ici, en réduit, à partir de la lecture de
`copie-nul-v9-a41b7b5/orchestrator/pole/nul_v9.py` et de `code-organisme-94bfd92/orchestrator/pole/` (`selection_pari.py`,
`nul_filles_v2.py`, `nul_v8.py`, `a_blanc_v59.py`).

Ce qui est recopié (au niveau du juge) : K = 3 issues, 2 traits gaussiens, 2 sous-populations, plan de n = 200 instances,
instants de lecture T = {25, 50, …, 200}, α = 0,05, promotion si log W_t ≥ log(1/α) à un instant de T, plancher 1e-12,
lois softmax tirées comme `loi_softmax_aleatoire` (force 1,5, biais 0,3), membres ajustés à valeur **certifiée** (valeur
atteinte + écart de Frank-Wolfe, bornée par 0), membres par morceaux à un niveau avec bruit aveugle **commun** aux morceaux.

Ce qui est réduit (dit, assumé) :
- membres fixes : uniforme, marginale d'entraînement (100 instances à part), chaque loi connue seule ; les membres
  log-linéaires (tempérés et inclinés) et les moyennes glissantes du v8 sont **omis** ;
- « v9 réduit » : partitions par sous-population, par la coupure d'archive, et par 7 seuils par trait (octiles du plan,
  fixés avant les tirages) au lieu de tout seuil réel : son dénominateur est plus bas que celui du vrai v9 (plus de
  puissance, moins de couverture) ;
- pari plein (numérateur = vraisemblance de la carte), sans pari à fraction ; ordre du plan = ordre des tirages.

Optimisation : algorithme EM dans la paramétrisation (s, r, m_c) du polytope du membre — ρ = s·r, μ_c = (1 − s)·m_c —,
certificat de Frank-Wolfe à chaque itération (on garde le plus petit certificat rencontré, chacun est une borne haute).
"""
import math

import numpy as np
from scipy.special import gammaln, logsumexp

K = 3
DIM = 2
SOUS_POP = 2
N = 200
ENTRAINEMENT = 100
INSTANTS = np.arange(25, N + 1, 25)
ALPHA = 0.05
SEUIL = math.log(1 / ALPHA)
PLANCHER = 1e-12
SEUIL_ARCHIVE = 0.3          # coupure portée par la loi d'archive L2 : si z0 > 0,3 alors A sinon B
OCTILES = np.arange(1, 8) / 8.0
J = 2                        # lois connues : L1 (softmax), L2 (si_sinon sur la coupure d'archive)
ITER_EM = 400
TOL_GAP = 1e-3


def softmax_alea(rng, force=1.5):
    return rng.normal(0.0, force, size=(K, DIM)), rng.normal(0.0, 0.3, size=K)


def probas_softmax(loi, z):
    W, b = loi
    s = z @ W.T + b
    s = s - s.max(axis=1, keepdims=True)
    p = np.exp(s)
    p /= p.sum(axis=1, keepdims=True)
    return np.maximum(p, PLANCHER) / np.maximum(p, PLANCHER).sum(axis=1, keepdims=True)


def archive(rng):
    """Deux lois connues : L1 softmax ; L2 si_sinon(z0 > 0,3 : A ; sinon : B)."""
    return {"L1": softmax_alea(rng), "A": softmax_alea(rng), "B": softmax_alea(rng)}


def lois_connues(arch, z):
    """(n, J, K) : L_j(· | x_s)."""
    p1 = probas_softmax(arch["L1"], z)
    pa, pb = probas_softmax(arch["A"], z), probas_softmax(arch["B"], z)
    p2 = np.where((z[:, 0] > SEUIL_ARCHIVE)[:, None], pa, pb)
    return np.stack([p1, p2], axis=1)


def plan(rng, n=N):
    z = np.round(rng.normal(0.0, 1.0, size=(n, DIM)), 6)
    g = rng.integers(0, SOUS_POP, size=n)
    return z, g


def tirer(rng, P):
    """Issues tirées de P (n, K)."""
    u = rng.random(P.shape[0])
    return np.minimum((u[:, None] > np.cumsum(P, axis=1)).sum(axis=1), K - 1)


# --- partitions (fixées avant les tirages : fonction du plan et de l'archive seulement) --------------------------------
def partitions(z, g, genre):
    """Liste (nom, cellule (n,) entière, nombre de cellules)."""
    n = z.shape[0]
    out = [("lineaire", np.zeros(n, dtype=int), 1)]
    if genre in ("La", "v9r"):
        out.append(("archive:z0>0.3", (z[:, 0] > SEUIL_ARCHIVE).astype(int), 2))
    if genre == "v9r":
        out.append(("sous_population", g.astype(int), 2))
        for j in range(DIM):
            for q in np.quantile(z[:, j], OCTILES):
                out.append((f"z{j}>{q:.4f}", (z[:, j] > q).astype(int), 2))
    return out


def dimension_famille(C, j=J, k=K):
    """Dimension affine du polytope {μ_c ≥ 0, ρ ≥ 0, Σ_j μ_cj + Σ_k ρ_k = 1 pour chaque c} : C·(J − 1) + K."""
    return C * (j - 1) + k


# --- maximum certifié par EM + écart de Frank-Wolfe, par lots (partition × instant) -----------------------------------
def em_certifie(Aobs, y, cellules, nb_cell, actifs, iterations=ITER_EM, tol=TOL_GAP, rendre_parametres=False):
    """Aobs (n, J) = L_j(y_s | x_s) ; y (n,) ; cellules (B, n) ; nb_cell (B,) ; actifs (B, n) booléens.
    Rend (certificat (B,), valeur atteinte (B,), écart final (B,)[, paramètres]). Le certificat est
    min(0, f(u) + max(0, écart(u))) pris au plus petit sur les itérations : borne haute du maximum quel que soit l'arrêt."""
    B, n = cellules.shape
    Cmax = int(nb_cell.max())
    Y = np.zeros((n, K))
    Y[np.arange(n), y] = 1.0
    act = actifs.astype(float)
    tB = act.sum(axis=1)
    s = np.full(B, K / (K + J))
    r = np.full((B, K), 1.0 / K)
    m = np.full((B, Cmax, J), 1.0 / J)
    masques = [(cellules == c).astype(float) for c in range(Cmax)]          # (B, n) par cellule
    meilleur = np.full(B, np.inf)
    atteinte = np.full(B, -np.inf)
    ecart = np.full(B, np.inf)
    actifs_lot = np.arange(B)
    for _ in range(iterations):
        if not len(actifs_lot):
            break
        a = actifs_lot
        mc = m[a[:, None], cellules[a]]                                          # m_{c(s)} (b, n, J)
        loi = (1 - s[a])[:, None] * (mc * Aobs[None, :, :]).sum(axis=2)
        dlt = s[a][:, None] * r[a][:, y]
        p = np.maximum(loi + dlt, PLANCHER)
        f = (act[a] * np.log(p)).sum(axis=1)
        inv = act[a] / p
        g_mu = np.stack([(inv * mq[a]) @ Aobs for mq in masques], axis=1)        # ∂f/∂μ_cj (b, C, J)
        g_rho = inv @ Y                                                           # ∂f/∂ρ_k
        sommet = np.maximum(g_rho.max(axis=1), g_mu.max(axis=2).sum(axis=1))
        gap = sommet - tB[a]
        cert = np.minimum(0.0, f + np.maximum(0.0, gap))
        meilleur[a] = np.minimum(meilleur[a], cert)
        atteinte[a] = np.maximum(atteinte[a], f)
        ecart[a] = np.maximum(0.0, gap)
        # pas EM
        resp_loi = (1 - s[a])[:, None, None] * mc * Aobs[None, :, :] / p[:, :, None] * act[a][:, :, None]
        resp_d = dlt / p * act[a]
        tot_d = resp_d.sum(axis=1)
        s[a] = tot_d / np.maximum(tB[a], 1.0)
        rk = resp_d @ Y + 1e-300
        r[a] = rk / rk.sum(axis=1, keepdims=True)
        mk = np.stack([(resp_loi * mq[a][:, :, None]).sum(axis=1) for mq in masques], axis=1) + 1e-300
        m[a] = mk / mk.sum(axis=2, keepdims=True)
        fini = (meilleur[a] - atteinte[a]) <= tol
        actifs_lot = a[~fini]
    if rendre_parametres:
        return meilleur, atteinte, ecart, (s, r, m)
    return meilleur, atteinte, ecart


def lot_partitions(parts, n=N, instants=INSTANTS):
    """Construit les lots (partition × instant)."""
    cel, nbc, act, cle = [], [], [], []
    for nom, c, C in parts:
        for t in instants:
            cel.append(c)
            nbc.append(C)
            a = np.zeros(n, dtype=bool)
            a[:t] = True
            act.append(a)
            cle.append((nom, int(t)))
    return np.array(cel), np.array(nbc), np.array(act), cle


def valeurs_fixes(Aobs, y, q_ent, instants=INSTANTS, debut=0):
    """Trajectoires des membres fixes (uniforme, marginale d'entraînement, chaque loi connue seule), lues aux instants,
    cumulées à partir de l'indice `debut`. Rend (nombre d'instants,) : le maximum des membres fixes."""
    logs = np.stack([np.full(len(y), -math.log(K)), np.log(np.maximum(q_ent[y], PLANCHER))]
                    + [np.log(np.maximum(Aobs[:, j], PLANCHER)) for j in range(Aobs.shape[1])], axis=0)
    cum = np.cumsum(logs[:, debut:], axis=1)
    return cum[:, np.asarray(instants) - 1 - debut].max(axis=0)


# --- bornes de regret --------------------------------------------------------------------------------------------------
def regret_cover(t, d):
    """Borne de regret du mélange uniforme sur un polytope de dimension d (argument ε, preuve dans la note) :
    min_ε d·log(1/ε) + t·log(1/(1 − ε)), atteint en ε = d/(t + d)."""
    t = np.asarray(t, dtype=float)
    eps = d / (t + d)
    return d * np.log(1 / eps) + t * np.log(1 / (1 - eps))


def regret_eg(t, m, C, eta, gamma):
    """Borne certifiée du gradient exponentié lissé, par cellule indépendante (preuve dans la note) :
    C·log m/η + η·t·G²/8 + t·log(1/(1 − γ)), G = (1 − γ)·m/γ."""
    G = (1 - gamma) * m / gamma
    return C * math.log(m) / eta + eta * np.asarray(t, dtype=float) * G * G / 8 + np.asarray(t, dtype=float) * math.log(1 / (1 - gamma))


def meilleurs_eta_gamma(n, m, C):
    """η et γ qui minimisent la borne à t = n (fixés d'avance, fonction de n, m, C seulement)."""
    best = (np.inf, None, None)
    for gamma in np.geomspace(1e-4, 0.5, 400):
        G = (1 - gamma) * m / gamma
        eta = math.sqrt(8 * C * math.log(m) / (n * G * G))
        b = float(regret_eg(n, m, C, eta, gamma))
        if b < best[0]:
            best = (b, eta, gamma)
    return best


# --- apprentissages en ligne -------------------------------------------------------------------------------------------
def eg_en_ligne(Aobs, y, cellule, C, eta, gamma=0.0, borne_exposant=50.0):
    """Gradient exponentié par cellule indépendante, composantes = J lois connues + K lois certaines δ_k ; prédiction
    w̃ = (1 − γ)·w + γ/m. Rend la trajectoire cumulée des log-probabilités prédictives (n,)."""
    n = len(y)
    m = J + K
    w = np.full((C, m), 1.0 / m)
    out = np.empty(n)
    acc = 0.0
    for t in range(n):
        c = cellule[t]
        x = np.concatenate([Aobs[t], np.eye(K)[y[t]]])
        wt = (1 - gamma) * w[c] + gamma / m
        p = max(PLANCHER, float(wt @ x))
        acc += math.log(p)
        out[t] = acc
        w[c] = w[c] * np.exp(np.minimum(eta * (1 - gamma) * x / p, borne_exposant))
        w[c] /= w[c].sum()
    return out


def _log_beta_pdf(x, a, b):
    return (a - 1) * np.log(np.maximum(x, 1e-300)) + (b - 1) * np.log(np.maximum(1 - x, 1e-300)) - (
        gammaln(a) + gammaln(b) - gammaln(a + b))


def _log_dir_pdf(x, alpha):
    alpha = np.asarray(alpha, dtype=float)
    return ((alpha - 1) * np.log(np.maximum(x, 1e-300))).sum(axis=-1) + gammaln(alpha.sum(axis=-1)) - gammaln(alpha).sum(axis=-1)


def log_melange_uniforme(Aobs, y, cellule, C, rng, nb=1000, parametres=None, comptes=None, kk=K):
    """Estimation par échantillonnage d'importance défensif de log ∫ p_θ(y^t) dπ(θ), π uniforme sur le polytope du membre
    (paramétrisation : s ~ Bêta(K, C(J−1)+1), r ~ Dir(1_K), m_c ~ Dir(1_J), indépendants — image exacte de la mesure
    uniforme, jacobien s^{K−1}(1−s)^{C(J−1)}). Proposition : 0,45 « comptes de l'EM + 1 », 0,45 « 0,3·comptes + 1 »,
    0,10 a priori. Estimation sans biais du mélange ; son logarithme est biaisé vers le bas (Jensen)."""
    t = len(y)
    jj = Aobs.shape[1]
    a_s, b_s = kk, C * (jj - 1) + 1
    if comptes is None:
        nd = np.zeros(kk)
        nl = np.zeros((C, jj))
    else:
        nd, nl = comptes
    comps = [(0.45, 1.0), (0.45, 0.3), (0.10, None)]
    choix = rng.choice(3, size=nb, p=[c[0] for c in comps])
    S = np.empty(nb)
    R = np.empty((nb, kk))
    Mm = np.empty((nb, C, jj))
    params = []
    for i, (_, f) in enumerate(comps):
        if f is None:
            pa = (a_s, b_s, np.ones(kk), np.ones((C, jj)))
        else:
            pa = (f * nd.sum() + 1, f * nl.sum() + 1, f * nd + 1, f * nl + 1)
        params.append(pa)
        sel = choix == i
        k_ = int(sel.sum())
        if k_:
            S[sel] = rng.beta(pa[0], pa[1], size=k_)
            R[sel] = rng.dirichlet(pa[2], size=k_) if kk > 1 else 1.0
            for c in range(C):
                Mm[sel, c] = rng.dirichlet(pa[3][c], size=k_)
    S = np.clip(S, 1e-12, 1 - 1e-12)

    def logdens(pa):
        v = _log_beta_pdf(S, pa[0], pa[1])
        if kk > 1:
            v = v + _log_dir_pdf(R, pa[2])
        for c in range(C):
            v = v + _log_dir_pdf(Mm[:, c], pa[3][c])
        return v
    lprior = logdens(params[2])
    lprop = logsumexp(np.stack([math.log(comps[i][0]) + logdens(params[i]) for i in range(3)]), axis=0)
    loi = (1 - S)[:, None] * np.einsum("ntj,tj->nt", Mm[:, cellule, :], Aobs)
    dl = S[:, None] * (R[:, y] if kk > 1 else (np.asarray(y) == 0)[None, :].astype(float))
    ll = np.log(np.maximum(loi + dl, PLANCHER)).sum(axis=1)
    return float(logsumexp(ll + lprior - lprop) - math.log(nb))


def comptes_em(Aobs, y, cellule, C, params):
    """Comptes attendus (δ_k, et lois par cellule) au point (s, r, m) de l'EM."""
    s, r, m = params
    mc = m[cellule]
    loi = (1 - s) * (mc * Aobs)
    dl = s * r[y]
    p = np.maximum(loi.sum(axis=1) + dl, PLANCHER)
    nd = np.zeros(K)
    np.add.at(nd, y, dl / p)
    nl = np.zeros((C, Aobs.shape[1]))
    np.add.at(nl, cellule, loi / p[:, None])
    return nd, nl


def clopper_pearson(k, n, niveau=0.95):
    from scipy.stats import beta
    a = (1 - niveau) / 2
    lo = 0.0 if k == 0 else float(beta.ppf(a, k, n - k + 1))
    hi = 1.0 if k == n else float(beta.ppf(1 - a, k + 1, n - k))
    return [round(lo, 4), round(hi, 4)]
