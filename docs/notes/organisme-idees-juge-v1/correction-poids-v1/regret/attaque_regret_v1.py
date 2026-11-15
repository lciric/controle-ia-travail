"""Attaque indépendante des méthodes « poids appris en ligne corrigés par une borne de regret » — v1.

Statut : mise au point exploratoire, aucune revendication. Toutes les issues se rapportent à l'identique ; aucun essai ne
vise un signe. Programme du réfutateur, écrit sans recopier ceux de l'auteur (`essai_regret_*_v1.py`) : banc, optimiseur,
calcul du mélange et lecture sont les miens. Processeur seul, numpy et scipy. Aucun fichier des dossiers de copie du juge
n'est exécuté ni importé ; la logique du juge (lue dans `selection_pari.py`, `nul_filles_v2.py`, `a_blanc_v59.py`,
`nul_v9.py`) est réécrite ici en réduit :
- K = 3 issues, 2 traits gaussiens arrondis à six décimales, plan de n = 200 instances, instants de lecture
  T = {25, 50, …, 200}, α = 0,05, promotion si log W_t ≥ log(1/α) à l'un des instants (arrêt optionnel), plancher 1e-12 ;
- membres ordinaires du juge gardés : uniforme, marginale ajustée sur les issues mêmes (maximum de vraisemblance),
  marginale d'entraînement (100 instances à part, lissage 0,5 comme `_frequences`), chaque loi connue seule ; omis : moyennes
  glissantes, mélanges à l'uniforme sur une grille, membres tempérés et inclinés ;
- membres ajustés : membre linéaire (Σ_j μ_j L_j + Σ_k ρ_k δ_k) et membre par morceaux à un niveau, deux morceaux, poids
  des lois connues propres au morceau, bruit aveugle commun (famille de `nul_v9.py`).

Ce qui diffère du banc de l'auteur (voulu) :
1. le mélange uniforme sur le polytope du membre est calculé **exactement** quand il y a deux lois connues : la part
   (bruit aveugle, masse des lois connues) s'intègre en forme close (moments de Dirichlet, polynômes symétriques
   élémentaires par issue), et la part « proportions entre lois connues » par une quadrature de Gauss-Legendre exacte pour
   le degré du polynôme (membre linéaire : 101 nœuds ; membre par morceaux : produit de deux grilles, environ 2 500
   nœuds) ; avec six lois connues, cette dernière part est estimée par échantillonnage d'importance (le reste intégré
   exactement) ;
2. le maximum de vraisemblance est cherché sur les **sommets** du polytope (poids sur K lois certaines et J^C lois
   « une loi connue par morceau »), par l'algorithme EM multiplicatif ; valeur atteinte (borne basse du maximum) et
   certificat (valeur + écart de Frank-Wolfe, borné par 0 : borne haute) sont rendus tous les deux ;
3. deux régimes de lecture : « membre seul » (le dénominateur ne contient que le membre ajusté qui contient le monde : le
   plus sévère pour la méthode, rien ne masque) et « avec ordinaires » (comme le juge : maximum avec les membres
   ordinaires) ;
4. membres défavorables ajoutés : loi certaine δ_k (sommet du polytope), poids tirés d'une loi de Dirichlet très creuse,
   six lois connues, 40 tirages lus tous les 5, copie par morceaux intérieure au polytope ; et une carte qui n'est pas une
   copie (loi du monde rendue surconfiante) dans un monde de la classe ;
5. la constante calibrée par simulation (R5 de l'auteur, écartée sans essai) est lue ici : plus petite constante dont le
   taux simulé reste sous α, par cas, puis puissance à cette constante.

La partie « estimateur » est la seule qui touche au code de l'auteur : elle importe son banc
(`essai_regret_banc_v1.py`, empreinte vérifiée avant l'import, fichier non modifié) pour mesurer l'erreur de son estimateur
du mélange contre le mélange exact, en dimension 4 et 5, sur les mondes du réfutateur.

Parties (une par appel, chacune en dix minutes au plus ; `python -I -B attaque_regret_v1.py PARTIE [MONDES]`) :
  bornes | estimateur | taille:<cas> | puissance:<dose> | fusion
Sorties : `attaque-sorties/attaque_regret_v1--<partie>.json` (jamais écrasées) ; `fusion` écrit `attaque_regret_v1.json`.
Graines : numpy.random.SeedSequence(ENTROPIE, spawn_key=(partie, cas, monde[, 1 pour l'échantillonnage d'importance])).
"""
import hashlib
import itertools
import json
import math
import os
import platform
import sys
import time
from multiprocessing import Pool

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):   # un fil par processus (machine partagée)
    os.environ[_v] = "1"

import numpy as np  # noqa: E402
import scipy  # noqa: E402
from scipy.optimize import minimize_scalar
from scipy.special import gammaln, logsumexp
from scipy.stats import beta as _loi_beta

ICI = os.path.dirname(os.path.abspath(__file__))
SORTIES = os.path.join(ICI, "attaque-sorties")
LD = np.longdouble
K, DIM = 3, 2
ALPHA = 0.05
SEUIL = math.log(1.0 / ALPHA)
PLANCHER = 1e-12
N_ENT = 100
ENTROPIE = 2026111577
PROCESSUS = 3
FACT = np.concatenate([[LD(1)], np.cumprod(np.arange(1, 420, dtype=LD))])  # FACT[i] = i! (précision étendue)
ETAS_ARTEFACT = (0.05, 0.2)
PARTIES = ("bornes", "estimateur", "taille", "puissance")
CAS_TAILLE = ("lin_interieur", "lin_poids_extremes", "lin_bord", "lin_sommet_delta", "lin_sommet_loi", "lin_six_lois",
              "lin_peu_tirages", "mor_sommet", "mor_interieur", "mor_poids_extremes", "mor_hors_archive",
              "lin_carte_surconfiante")
# cas de même structure que les mondes de puissance (deux lois connues, 200 tirages, carte = copie) : calibration de R5
CAS_CALIBRATION = ("lin_interieur", "lin_poids_extremes", "lin_bord", "lin_sommet_delta", "lin_sommet_loi", "mor_sommet",
                   "mor_interieur", "mor_poids_extremes", "mor_hors_archive")
EXPOSANT_SURCONFIANCE = 1.3
DOSES = (0.1, 0.2, 0.35)
GRILLE_C = np.round(np.arange(0.0, 30.0001, 0.25), 2)
GRILLE_KAPPA = np.round(np.arange(0.0, 1.0001, 0.01), 2)
REFERENCE_SIX_LOIS = 15
NOEUDS_SIX_LOIS = 1200
CONTROLES_PRECISION = 3
MONDES_STRUCTURE_ARCHIVE = 500
EMPREINTE_BANC_AUTEUR = "8d1c44db471067333a3b267d95e393ff85eadc06ffa50faf689b7176b1e8ae65"


# --- lois, plan, tirages ------------------------------------------------------------------------------------------------
def normaliser(P):
    P = np.maximum(P, PLANCHER)
    return P / P.sum(axis=1, keepdims=True)


def loi_softmax(rng):
    return {"t": "softmax", "W": np.round(rng.normal(0.0, 1.5, (K, DIM)), 6), "b": np.round(rng.normal(0.0, 0.3, K), 6)}


def loi_si_sinon(rng, trait, seuil):
    return {"t": "si_sinon", "trait": int(trait), "seuil": float(seuil), "si": loi_softmax(rng), "sinon": loi_softmax(rng)}


def table(loi, z):
    """(n, K) : loi(· | x_s) pour chaque instance du plan."""
    if loi["t"] == "softmax":
        s = z @ loi["W"].T + loi["b"]
        s = s - s.max(axis=1, keepdims=True)
        return normaliser(np.exp(s))
    cond = z[:, loi["trait"]] > loi["seuil"]
    return np.where(cond[:, None], table(loi["si"], z), table(loi["sinon"], z))


def tirer_plan(rng, n):
    return np.round(rng.normal(0.0, 1.0, (n, DIM)), 6)


def tirer_issues(rng, P):
    u = rng.random(P.shape[0])
    return np.minimum((u[:, None] > np.cumsum(P, axis=1)).sum(axis=1), K - 1)


def rng_de(*cle):
    return np.random.default_rng(np.random.SeedSequence(ENTROPIE, spawn_key=tuple(int(c) for c in cle)))


# --- membres ordinaires -------------------------------------------------------------------------------------------------
def ordinaires(y, Lobs, q_ent, inst, debut=0):
    """Maximum, aux instants, des membres ordinaires cumulés depuis `debut` : uniforme, marginale ajustée sur ces issues
    mêmes, marginale d'entraînement, chaque loi connue seule."""
    yy = y[debut:]
    n = len(yy)
    t = np.arange(1, n + 1, dtype=float)
    H = np.cumsum(np.eye(K)[yy], axis=0)
    with np.errstate(divide="ignore", invalid="ignore"):
        mv = np.where(H > 0, H * np.log(H / t[:, None]), 0.0).sum(axis=1)
    traj = [-t * math.log(K), mv, np.cumsum(np.log(q_ent[yy]))]
    traj += [np.cumsum(np.log(Lobs[debut:, j])) for j in range(Lobs.shape[1])]
    return np.max(np.stack(traj), axis=0)[np.asarray(inst) - 1 - debut]


# --- maximum de vraisemblance sur les sommets, valeur atteinte et certificat ------------------------------------------
def matrice_sommets(Lobs, y, cell, C):
    """A (n, V) : vraisemblance de chaque issue observée sous chaque sommet du polytope ; K lois certaines δ_k, puis les
    J^C lois « loi connue j_c sur le morceau c »."""
    n, J = Lobs.shape
    r = np.arange(n)
    cols = [(y == k).astype(float) for k in range(K)]
    combos = list(itertools.product(range(J), repeat=C))
    for cb in combos:
        cols.append(Lobs[r, np.asarray(cb)[cell]])
    return np.stack(cols, axis=1), combos


def max_certifie(A, inst, iterations=1500, tol=1e-4):
    """EM multiplicatif sur les poids des sommets, tous les instants à la fois. Rend (valeur atteinte, certificat, poids).
    Certificat = min(0, f(λ) + max(0, max_v ∇f·e_v − t)) : borne haute du maximum à tout point admissible (concavité)."""
    n, V = A.shape
    tt = np.asarray(inst, dtype=float)
    M = (np.arange(n)[None, :] < tt[:, None]).astype(float)
    lam = np.full((len(tt), V), 1.0 / V)
    cert = np.full(len(tt), np.inf)
    att = np.full(len(tt), -np.inf)
    garde = lam.copy()
    for it in range(iterations):
        p = np.where(M > 0, lam @ A.T, 1.0)                     # hors de l'instant lu : aucune contribution
        f = (M * np.log(p)).sum(axis=1)
        g = (M / p) @ A
        ecart = np.maximum(g.max(axis=1) - tt, 0.0)
        cert = np.minimum(cert, np.minimum(0.0, f + ecart))
        mieux = f > att
        att = np.where(mieux, f, att)
        garde[mieux] = lam[mieux]
        if float((cert - att).max()) <= tol:
            break
        lam = lam * g / tt[:, None]
        if it % 20 == 19:  # élagage : poids négligeable et gradient sous t (le sommet sort du support) ; reste admissible
            petit = (lam < 1e-9) & (g < tt[:, None])
            lam = np.where(petit, 0.0, lam)
            lam = lam / lam.sum(axis=1, keepdims=True)
    return att, cert, garde


def comptes_lois(A, lam, cell, C, combos, J):
    """Comptes attendus (C, J) des lois connues par morceau au point λ (pour la proposition d'importance)."""
    p = A @ lam
    resp = A * lam[None, :] / p[:, None]
    out = np.zeros((C, J))
    for v, cb in enumerate(combos):
        for c in range(C):
            out[c, cb[c]] += resp[cell == c, K + v].sum()
    return out


# --- mélange uniforme sur le polytope du membre ----------------------------------------------------------------------
def _conv(X, Y, dtype=float):
    if X.shape[1] < Y.shape[1]:
        X, Y = Y, X
    out = np.zeros((X.shape[0], X.shape[1] + Y.shape[1] - 1), dtype=dtype)
    for i in range(Y.shape[1]):
        out[:, i:i + X.shape[1]] += X * Y[:, i:i + 1]
    return out


def melange_noeuds(Cn, lw, y, a_sigma, inst, diag=False):
    """log ∫ p_θ(y_1..t) dπ(θ) aux instants, π uniforme sur le polytope {ρ ≥ 0, μ_c ≥ 0, Σ_j μ_cj + Σ_k ρ_k = 1}.

    Paramétrage : σ = 1 − Σ_k ρ_k ; μ_c = σ·m_c, m_c dans le simplexe. Sous π : (ρ_1..ρ_K, σ) ~ Dirichlet(1, …, 1, a_sigma)
    avec a_sigma = C·(J − 1) + 1, et les m_c uniformes, indépendants (jacobien σ^{C(J−1)}). `Cn[q, s]` =
    Σ_j m_{c(s),j}(q)·L_j(y_s | x_s) au nœud q (une valeur des m_c), `lw[q]` le logarithme du poids du nœud (quadrature ou
    importance). À m fixé : Π_s (σ·Cn_s + ρ_{y_s}) = Π_k Σ_i e_i^{(k)} σ^i ρ_k^{n_k − i}, où e^{(k)} sont les polynômes
    symétriques élémentaires des Cn_s de l'issue k, et
    E[σ^I Π_k ρ_k^{r_k}] = Γ(K + a)/Γ(K + a + t) · Γ(a + I)/Γ(a) · Π_k r_k!.
    Tous les termes sont positifs. Double précision avec mise à l'échelle commune λ = t/K (coefficient d'indice i
    multiplié par λ^i·(n_k − i)!/n_k!, poids final divisé par λ^I) : les termes qui passeraient sous le plus petit
    flottant sont négligeables devant le terme I = 0, toujours présent (contrôle : `melange_noeuds_etendu`)."""
    Q, n = Cn.shape
    nk = np.bincount(y, minlength=K)
    E = [np.zeros((Q, int(nk[k]) + 1)) for k in range(K)]
    for k in range(K):
        E[k][:, 0] = 1.0
    cnt = [0] * K
    inst = [int(t) for t in inst]
    out = np.empty(len(inst))
    j = 0
    ess = None
    for s in range(n):
        k = int(y[s])
        c = cnt[k]
        E[k][:, 1:c + 2] += Cn[:, s:s + 1] * E[k][:, 0:c + 1]
        cnt[k] = c + 1
        if j < len(inst) and s + 1 == inst[j]:
            t = s + 1
            ll = math.log(t / K)
            ordre = sorted(range(K), key=lambda kk: cnt[kk])          # la plus grande issue en dernier
            B = None
            for kk in ordre:
                m = cnt[kk]
                i = np.arange(m + 1)
                Ak = E[kk][:, :m + 1] * np.exp(i * ll + gammaln(m - i + 1) - gammaln(m + 1))
                if kk != ordre[-1]:
                    B = Ak if B is None else _conv(B, Ak)
            I = np.arange(t + 1)
            W = np.exp(gammaln(I + a_sigma) + sum(gammaln(cnt[kk] + 1) for kk in range(K)) - gammaln(t + a_sigma) - I * ll)
            # Σ_I (B * Ak)[I]·W[I] = Σ_j B[j]·Σ_i Ak[i]·W[i + j] : dernière convolution contractée avec les poids
            F = W[np.arange(Ak.shape[1])[:, None] + np.arange(B.shape[1])[None, :]]
            lt = lw + np.log((B * (Ak @ F)).sum(axis=1))
            out[j] = (logsumexp(lt) + gammaln(t + a_sigma) + gammaln(K + a_sigma) - gammaln(K + a_sigma + t)
                      - gammaln(a_sigma))
            if diag and j == len(inst) - 1:
                ess = float(math.exp(2 * logsumexp(lt) - logsumexp(2 * lt)))
            j += 1
    return (out, ess) if diag else out


def melange_noeuds_etendu(Cn, lw, y, a_sigma, inst):
    """Le même calcul en précision étendue (80 bits), sans mise à l'échelle : contrôle de `melange_noeuds`."""
    Q, n = Cn.shape
    Cl = Cn.astype(LD)
    nk = np.bincount(y, minlength=K)
    E = [np.zeros((Q, int(nk[k]) + 1), dtype=LD) for k in range(K)]
    for k in range(K):
        E[k][:, 0] = 1
    cnt = [0] * K
    inst = [int(t) for t in inst]
    out = np.empty(len(inst))
    j = 0
    for s in range(n):
        k = int(y[s])
        c = cnt[k]
        E[k][:, 1:c + 2] += Cl[:, s:s + 1] * E[k][:, 0:c + 1]
        cnt[k] = c + 1
        if j < len(inst) and s + 1 == inst[j]:
            t = s + 1
            B = None
            for kk in range(K):
                m = cnt[kk]
                Ak = E[kk][:, :m + 1] * FACT[m - np.arange(m + 1)]
                B = Ak if B is None else _conv(B, Ak, LD)
            S = (B * FACT[a_sigma - 1 + np.arange(t + 1)]).sum(axis=1)
            out[j] = (logsumexp(lw + np.log(S).astype(float)) + gammaln(K + a_sigma) - gammaln(K + a_sigma + t)
                      - gammaln(a_sigma))
            j += 1
    return out


def _gauss_legendre(m):
    x, w = np.polynomial.legendre.leggauss(int(m))
    return (x + 1.0) / 2.0, w / 2.0


def noeuds_exacts(Lobs, cell, C):
    """Deux lois connues : m_c = (u_c, 1 − u_c), u_c uniforme sur [0, 1]. La vraisemblance est un polynôme de degré au plus
    t_c en u_c (t_c = nombre d'instances du morceau c) : la quadrature de Gauss-Legendre à ⌈(t_c + 1)/2⌉ nœuds est exacte."""
    assert Lobs.shape[1] == 2
    a, b = Lobs[:, 0], Lobs[:, 1]
    n = len(a)
    if C == 1:
        u, w = _gauss_legendre((n + 2) // 2)
        return u[:, None] * a[None, :] + (1 - u)[:, None] * b[None, :], np.log(w)
    n0, n1 = int((cell == 0).sum()), int((cell == 1).sum())
    u0, w0 = _gauss_legendre((n0 + 2) // 2)
    u1, w1 = _gauss_legendre((n1 + 2) // 2)
    U0, U1 = np.meshgrid(u0, u1, indexing="ij")
    U = np.where(cell[None, :] == 0, U0.reshape(-1, 1), U1.reshape(-1, 1))
    return U * a[None, :] + (1 - U) * b[None, :], (np.log(w0)[:, None] + np.log(w1)[None, :]).reshape(-1)


def _log_dirichlet(X, alpha):
    return ((alpha - 1.0) * np.log(X)).sum(axis=1) + gammaln(alpha.sum()) - gammaln(alpha).sum()


def noeuds_importance(Lobs, cell, C, comptes, rng, nb):
    """Nœuds tirés pour les proportions m_c seulement (le reste s'intègre exactement dans `melange_noeuds`). Proposition :
    mélange, à effectifs fixés, de Dirichlet(f·comptes + 1) pour f = 1 ; 0,35 ; 0,1, et de l'a priori uniforme. Poids =
    densité a priori / densité du mélange de propositions : estimation sans biais du mélange."""
    J = Lobs.shape[1]
    comps = [(0.40, 1.0), (0.30, 0.35), (0.15, 0.10), (0.15, None)]
    eff = [int(round(pw * nb)) for pw, _ in comps]
    eff[0] += nb - sum(eff)
    alphas = [np.ones((C, J)) if f is None else f * comptes + 1.0 for _, f in comps]
    Mm = np.empty((nb, C, J))
    pos = 0
    for al, k_ in zip(alphas, eff):
        for c in range(C):
            Mm[pos:pos + k_, c] = rng.dirichlet(al[c], size=k_)
        pos += k_
    Mm = np.maximum(Mm, 1e-300)
    Mm = Mm / Mm.sum(axis=2, keepdims=True)
    ld = [sum(_log_dirichlet(Mm[:, c], al[c]) for c in range(C)) for al in alphas]
    lprop = logsumexp(np.stack([math.log(e / nb) + l for e, l in zip(eff, ld)]), axis=0)
    lw = C * gammaln(J) - lprop - math.log(nb)
    return np.einsum("qnj,nj->qn", Mm[:, cell, :], Lobs), lw


# --- bornes de regret -----------------------------------------------------------------------------------------------
def borne_epsilon(t, d):
    """R(t, d) = d·log((t + d)/d) + t·log((t + d)/t) (énoncé de l'auteur, méthode R1)."""
    t = np.asarray(t, dtype=float)
    return d * np.log((t + d) / d) + t * np.log((t + d) / t)


def borne_hedge(t, m, C, eta, gamma):
    G = (1 - gamma) * m / gamma
    t = np.asarray(t, dtype=float)
    return C * math.log(m) / eta + eta * t * G * G / 8.0 + t * math.log(1.0 / (1.0 - gamma))


def reglage_hedge(n, m, C):
    """η et γ qui minimisent la borne à t = n (η optimal à γ fixé, puis minimisation sur γ)."""
    def b(gamma):
        G = (1 - gamma) * m / gamma
        return G * math.sqrt(C * n * math.log(m) / 2.0) + n * math.log(1.0 / (1.0 - gamma))
    r = minimize_scalar(b, bounds=(1e-4, 0.95), method="bounded", options={"xatol": 1e-10})
    gamma = float(r.x)
    G = (1 - gamma) * m / gamma
    eta = math.sqrt(8.0 * C * math.log(m) / (n * G * G))
    return eta, gamma, float(borne_hedge(n, m, C, eta, gamma))


# --- apprentissages en ligne ---------------------------------------------------------------------------------------
def gradient_exponentie(X, cell, C, eta, gamma):
    """Poids par morceau indépendant sur les m = J + K composantes ; prédiction (1 − γ)·w + γ/m ; mise à jour
    w ∝ w·exp(η(1 − γ)x/p), en logarithmes (aucun écrêtage de l'exposant ; la prédiction est bornée en bas par 1e-300).
    Rend le cumul des log-probabilités prédictives."""
    n, m = X.shape
    Xl, cl = X.tolist(), [int(c) for c in cell]
    lw = [[-math.log(m)] * m for _ in range(C)]
    out = [0.0] * n
    acc, g1, g0 = 0.0, 1.0 - gamma, gamma / m
    for s in range(n):
        l, x = lw[cl[s]], Xl[s]
        p = 0.0
        for j in range(m):
            p += (g1 * math.exp(l[j]) + g0) * x[j]
        if p < 1e-300:
            p = 1e-300
        acc += math.log(p)
        out[s] = acc
        k = eta * g1 / p
        nl = [l[j] + k * x[j] for j in range(m)]
        mx = max(nl)
        z = mx + math.log(sum(math.exp(v - mx) for v in nl))
        lw[cl[s]] = [v - z for v in nl]
    return np.array(out)


def poids_moitie(X, cell, C, h, iterations=400):
    """Maximum de vraisemblance par morceau indépendant sur les tirages 1..h ; rend le cumul, depuis h, des
    log-probabilités sous ces poids figés (façon argon-p1-01)."""
    m = X.shape[1]
    W = np.full((C, m), 1.0 / m)
    for c in range(C):
        Xc = X[:h][cell[:h] == c]
        if len(Xc):
            w = np.full(m, 1.0 / m)
            for _ in range(iterations):
                w = w * (Xc.T @ (1.0 / (Xc @ w))) / len(Xc)
            W[c] = w / w.sum()
    return np.cumsum(np.log(np.maximum((W[cell[h:]] * X[h:]).sum(axis=1), PLANCHER)))


# --- un membre ajusté, toutes méthodes -----------------------------------------------------------------------------
REGLAGES_HEDGE = {}


def reglage(n, m, C):
    cle = (n, m, C)
    if cle not in REGLAGES_HEDGE:
        REGLAGES_HEDGE[cle] = reglage_hedge(n, m, C)
    return REGLAGES_HEDGE[cle]


def evaluer_membre(Lobs, y, cell, C, inst, rng_is, melange="exact", nb_is=400):
    """Toutes les valeurs d'un membre ajusté aux instants : maximum (atteint, certifié), mélange uniforme, bornes,
    gradient exponentié lissé (R2) et non lissé (artefact), poids ajustés sur la première moitié (artefact)."""
    n, J = Lobs.shape
    inst = np.asarray(inst)
    A, combos = matrice_sommets(Lobs, y, cell, C)
    att, cert, lam = max_certifie(A, inst)
    d = C * (J - 1) + K
    a_sigma = C * (J - 1) + 1
    if melange == "exact":
        Cn, lw = noeuds_exacts(Lobs, cell, C)
    else:
        Cn, lw = noeuds_importance(Lobs, cell, C, comptes_lois(A, lam[-1], cell, C, combos, J), rng_is, nb_is)
    mix, ess = melange_noeuds(Cn, lw, y, a_sigma, inst, diag=True)
    if melange == "exact":
        ess = None
    X = np.concatenate([Lobs, np.eye(K)[y]], axis=1)
    eta, gamma, _ = reglage(n, J + K, C)
    r2 = gradient_exponentie(X, cell, C, eta, gamma)[inst - 1] + borne_hedge(inst, J + K, C, eta, gamma)
    a1 = [gradient_exponentie(X, cell, C, e, 0.0)[inst - 1] for e in ETAS_ARTEFACT]
    h = n // 2
    inst2 = inst[inst > h]
    a2 = poids_moitie(X, cell, C, h)[inst2 - 1 - h]
    return {"att": att, "cert": cert, "mix": mix, "R": borne_epsilon(inst, d), "r2": r2, "a1": a1, "a2": a2, "d": d,
            "ess": ess, "noeuds": int(Cn.shape[0])}


def melange_importance(Lobs, y, cell, C, inst, rng_is, nb_is):
    """Le mélange par importance seul (mesure de son erreur contre l'exact ou contre une référence plus fine)."""
    A, combos = matrice_sommets(Lobs, y, cell, C)
    _, _, lam = max_certifie(A, np.asarray(inst))
    J = Lobs.shape[1]
    Cn, lw = noeuds_importance(Lobs, cell, C, comptes_lois(A, lam[-1], cell, C, combos, J), rng_is, nb_is)
    return melange_noeuds(Cn, lw, y, C * (J - 1) + 1, inst)


# --- mondes -----------------------------------------------------------------------------------------------------------
def archive(rng, J):
    """J lois connues : J − 1 lois softmax, puis une loi si_sinon dont la coupure (trait, seuil) est la coupure de l'archive."""
    lois = [loi_softmax(rng) for _ in range(J - 1)]
    trait = int(rng.integers(0, DIM))
    seuil = round(float(rng.uniform(-0.8, 0.8)), 2)
    lois.append(loi_si_sinon(rng, trait, seuil))
    return lois, trait, seuil


def construire_monde(cas, rng, dose=None):
    """Tout ce qui est fixé avant les tirages frais : archive, loi du monde (fonction du plan), plans, coupures."""
    J = 6 if cas == "lin_six_lois" else 2
    n = 40 if cas == "lin_peu_tirages" else 200
    inst = np.arange(5, 41, 5) if cas == "lin_peu_tirages" else np.arange(25, 201, 25)
    lois, trait, seuil = archive(rng, J)
    prm = {"w": rng.dirichlet(np.ones(J + K)), "wx": rng.dirichlet(np.full(J + K, 0.15)), "k": int(rng.integers(0, K)),
           "j": int(rng.integers(0, J)), "v": float(rng.uniform(0.5, 0.9)),
           "poly": (rng.dirichlet(np.array([1.0] * K + [3.0])), rng.dirichlet(np.ones(2), size=2)),
           "seuil_hors": round(float(rng.choice([-1, 1]) * rng.uniform(0.3, 0.8)), 2),
           "neuve": loi_softmax(rng)}

    def loi_monde(z):
        L = np.stack([table(l, z) for l in lois], axis=1)                 # (n, J, K)
        D = np.eye(K)
        k = prm["k"]
        arch = (z[:, trait] > seuil)
        hors = (z[:, 1 - trait] > prm["seuil_hors"])
        if cas in ("lin_interieur", "lin_six_lois", "lin_peu_tirages", "lin_carte_surconfiante"):
            w = prm["w"]
            P = np.einsum("j,njk->nk", w[:J], L) + w[J:][None, :]
        elif cas == "lin_poids_extremes":
            w = prm["wx"]
            P = np.einsum("j,njk->nk", w[:J], L) + w[J:][None, :]
        elif cas == "lin_bord":
            P = prm["v"] * L[:, prm["j"]] + (1 - prm["v"]) * D[k][None, :]
        elif cas == "lin_sommet_delta":
            P = np.tile(D[k], (len(z), 1))
        elif cas == "lin_sommet_loi":
            P = L[:, prm["j"]].copy()
        elif cas == "mor_sommet":
            P = np.where(arch[:, None], L[:, 0], L[:, 1])
        elif cas == "mor_interieur":
            rs, mm = prm["poly"]
            mc = mm[arch.astype(int)]                                     # (n, 2)
            P = rs[K] * (mc[:, :1] * L[:, 0] + mc[:, 1:] * L[:, 1]) + rs[:K][None, :]
        elif cas == "mor_poids_extremes":
            haut = 0.96 * L[:, 0] + 0.02 * L[:, 1] + 0.02 * D[k][None, :]
            bas = 0.02 * L[:, 0] + 0.96 * L[:, 1] + 0.02 * D[k][None, :]
            P = np.where(arch[:, None], haut, bas)
        elif cas == "mor_hors_archive":
            P = np.where(hors[:, None], L[:, 0], L[:, 1])
        elif cas == "decouverte":
            P = (1 - dose) * (0.5 * L[:, 0] + 0.5 * L[:, 1]) + dose * table(prm["neuve"], z)
        else:
            raise ValueError(cas)
        return normaliser(P), L, arch.astype(int), hors.astype(int)

    z_ent = tirer_plan(rng, N_ENT)
    z = tirer_plan(rng, n)
    return {"J": J, "n": n, "inst": inst, "loi_monde": loi_monde, "z_ent": z_ent, "z": z}


def tirer_monde(cas, cle, dose=None):
    """Monde complet : gel (archive, carte = loi du monde, plan), puis issues d'entraînement et tirages frais."""
    rng = rng_de(*cle)
    m = construire_monde(cas, rng, dose)
    P_ent, _, _, _ = m["loi_monde"](m["z_ent"])
    P, L, c_arch, c_hors = m["loi_monde"](m["z"])
    y_ent = tirer_issues(rng, P_ent)
    q_ent = (np.bincount(y_ent, minlength=K) + 0.5) / (N_ENT + 0.5 * K)
    # carte gelée avant les tirages : la loi du monde (copie exacte), sauf le cas « carte surconfiante » (hors classe)
    Q = normaliser(P ** EXPOSANT_SURCONFIANCE) if cas == "lin_carte_surconfiante" else P
    y = tirer_issues(rng, P)                                               # tirages frais, après le gel
    r = np.arange(m["n"])
    return {"y": y, "Lobs": L[r, :, y], "num": np.cumsum(np.log(Q[r, y])), "q_ent": q_ent, "c_arch": c_arch,
            "c_hors": c_hors, "inst": m["inst"], "n": m["n"], "J": m["J"]}


# --- lecture d'un monde ------------------------------------------------------------------------------------------------
def _richesses(num_i, membres, inst, do, num2=None, do2=None):
    """Trajectoires log W aux instants, par méthode, régime « membres ajustés seuls » ; `do` = log q − ordinaires."""
    mx = lambda cle: np.max(np.stack([mb[cle] for mb in membres]), axis=0)
    out = {
        "MAX-certifie": num_i - mx("cert"),
        "MAX-atteint": num_i - mx("att"),
        "R1-melange+borne": num_i - np.max(np.stack([mb["mix"] + mb["R"] for mb in membres]), axis=0),
        "R2-gradient+Hedge": num_i - mx("r2"),
        "A1-melange-sans-correction": num_i - mx("mix"),
    }
    for i, e in enumerate(ETAS_ARTEFACT):
        out[f"A1-gradient-{e}-sans-correction"] = num_i - np.max(np.stack([mb["a1"][i] for mb in membres]), axis=0)
    out["A2-moitie"] = num2 - np.max(np.stack([mb["a2"] for mb in membres]), axis=0)
    return out


def _lire(traj, do, do2):
    """(max log W membre(s) seul(s), max log W avec ordinaires) par méthode."""
    res = {}
    for nom, lw in traj.items():
        d = do2 if nom == "A2-moitie" else do
        res[nom] = (float(lw.max()), float(np.minimum(lw, d).max()))
    res["A2-moitie-lecture-finale"] = (float(traj["A2-moitie"][-1]), float(min(traj["A2-moitie"][-1], do2[-1])))
    return res


def _seuils_r5(num_i, membres, do):
    """Pour la constante calibrée (R5) : plus grand c (resp. κ) pour lequel ce monde est promu avec le dénominateur
    max(membres : log mélange + c) (resp. + κ·R(t, d)), seul puis avec ordinaires."""
    dm = num_i - np.max(np.stack([mb["mix"] for mb in membres]), axis=0)
    kap = np.min(np.stack([(num_i - mb["mix"] - SEUIL) / mb["R"] for mb in membres]), axis=0)
    ok = do >= SEUIL
    return {"c_seul": float(dm.max() - SEUIL), "c_ord": float(dm[ok].max() - SEUIL) if ok.any() else -1e9,
            "k_seul": float(kap.max()), "k_ord": float(kap[ok].max()) if ok.any() else -1e9}


def juger_taille(arg):
    cas, i = arg
    ic = CAS_TAILLE.index(cas)
    t0 = time.perf_counter()
    w = tirer_monde(cas, (PARTIES.index("taille"), ic, i))
    rng_is = rng_de(PARTIES.index("taille"), ic, i, 1)
    inst, y, Lobs, n = w["inst"], w["y"], w["Lobs"], w["n"]
    num_i = w["num"][inst - 1]
    h = n // 2
    inst2 = inst[inst > h]
    num2 = w["num"][inst2 - 1] - w["num"][h - 1]
    do = num_i - ordinaires(y, Lobs, w["q_ent"], inst)
    do2 = num2 - ordinaires(y, Lobs, w["q_ent"], inst2, debut=h)
    zero = np.zeros(n, dtype=int)
    exact = w["J"] == 2
    if cas.startswith("lin_"):
        C, cell = 1, zero
    else:
        C, cell = 2, (w["c_hors"] if cas == "mor_hors_archive" else w["c_arch"])
    principal = evaluer_membre(Lobs, y, cell, C, inst, rng_is, "exact" if exact else "importance", nb_is=NOEUDS_SIX_LOIS)
    traj = _richesses(num_i, [principal], inst, do, num2, do2)
    out = {"lw": _lire(traj, do, do2), "r5": _seuils_r5(num_i, [principal], do),
           "regret": [float(x) for x in (principal["att"] - principal["mix"])],
           "marge_R1": float((principal["mix"] + principal["R"] - principal["att"]).min()),
           "marge_R2": float((principal["r2"] - principal["att"]).min()),
           "ecart_certificat": float((principal["cert"] - principal["att"]).max()),
           "ess": principal["ess"], "exact": bool(exact)}
    if exact and i < CONTROLES_PRECISION:           # double précision avec mise à l'échelle contre précision étendue
        Cn, lw = noeuds_exacts(Lobs, cell, C)
        out["ecart_precision"] = float(np.abs(melange_noeuds_etendu(Cn, lw, y, C + 1, inst) - principal["mix"]).max())
    if not exact and i < REFERENCE_SIX_LOIS:        # importance à NOEUDS_SIX_LOIS nœuds contre une référence à 12 000 nœuds
        out["erreur_importance"] = [float(x) for x in principal["mix"] - melange_importance(Lobs, y, cell, C, inst, rng_is, 12000)]
    if cas == "mor_hors_archive" and i < MONDES_STRUCTURE_ARCHIVE:   # hors de la classe : structure limitée à la coupure de l'archive (descriptif)
        lin = evaluer_membre(Lobs, y, zero, 1, inst, rng_is, "exact")
        arc = evaluer_membre(Lobs, y, w["c_arch"], 2, inst, rng_is, "exact")
        out["lw_structure_archive"] = _lire(_richesses(num_i, [lin, arc], inst, do, num2, do2), do, do2)
    out["duree"] = time.perf_counter() - t0
    return out


def juger_puissance(arg):
    dose, i = arg
    idd = DOSES.index(dose)
    t0 = time.perf_counter()
    w = tirer_monde("decouverte", (PARTIES.index("puissance"), idd, i), dose=dose)
    rng_is = rng_de(PARTIES.index("puissance"), idd, i, 1)
    inst, y, Lobs, n = w["inst"], w["y"], w["Lobs"], w["n"]
    num_i = w["num"][inst - 1]
    h = n // 2
    inst2 = inst[inst > h]
    num2 = w["num"][inst2 - 1] - w["num"][h - 1]
    do = num_i - ordinaires(y, Lobs, w["q_ent"], inst)
    do2 = num2 - ordinaires(y, Lobs, w["q_ent"], inst2, debut=h)
    lin = evaluer_membre(Lobs, y, np.zeros(n, dtype=int), 1, inst, rng_is, "exact")
    arc = evaluer_membre(Lobs, y, w["c_arch"], 2, inst, rng_is, "exact")
    traj = _richesses(num_i, [lin, arc], inst, do, num2, do2)
    return {"lw": _lire(traj, do, do2), "r5": _seuils_r5(num_i, [lin, arc], do),
            "ecart_certificat": float(max((lin["cert"] - lin["att"]).max(), (arc["cert"] - arc["att"]).max())),
            "marge_R1": float(min((lin["mix"] + lin["R"] - lin["att"]).min(), (arc["mix"] + arc["R"] - arc["att"]).min())),
            "surcout_R1": float((np.maximum(lin["mix"] + lin["R"], arc["mix"] + arc["R"]) - np.maximum(lin["cert"], arc["cert"]))[-1]),
            "duree": time.perf_counter() - t0}


# --- agrégats ----------------------------------------------------------------------------------------------------------
def clopper_pearson(k, n, niveau=0.95):
    a = (1 - niveau) / 2
    bas = 0.0 if k == 0 else float(_loi_beta.ppf(a, k, n - k + 1))
    haut = 1.0 if k == n else float(_loi_beta.ppf(1 - a, k + 1, n - k))
    return [round(bas, 5), round(haut, 5)]


def _ligne(vals, nb):
    v = np.asarray(vals)
    k = int((v >= SEUIL).sum())
    ic = clopper_pearson(k, nb)
    return {"promues": k, "mondes": nb, "taux": round(k / nb, 5), "intervalle_95": ic,
            "borne_haute_sous_alpha": bool(ic[1] <= ALPHA), "borne_basse_au_dessus_de_alpha": bool(ic[0] > ALPHA),
            "log_W_max_mediane": round(float(np.median(v)), 3), "log_W_max_q95": round(float(np.quantile(v, 0.95)), 3),
            "log_W_max_max": round(float(v.max()), 3)}


def _tableau(sorties, cle="lw"):
    nb = len(sorties)
    methodes = list(sorties[0][cle])
    return {m: {"membre_seul": _ligne([s[cle][m][0] for s in sorties], nb),
                "avec_ordinaires": _ligne([s[cle][m][1] for s in sorties], nb)} for m in methodes}


def _grilles_r5(sorties):
    out = {}
    for cle, grille in (("c_seul", GRILLE_C), ("c_ord", GRILLE_C), ("k_seul", GRILLE_KAPPA), ("k_ord", GRILLE_KAPPA)):
        v = np.array([s["r5"][cle] for s in sorties])
        out[cle] = {"promues_par_valeur_de_grille": [int((v >= g - 1e-12).sum()) for g in grille],
                    "quantile_95": round(float(np.quantile(v, 0.95)), 3), "max": round(float(v.max()), 3)}
    return out


def _entete(partie, extra=None):
    d = {"programme": "attaque_regret_v1.py", "partie": partie, "statut": "mise au point exploratoire, aucune revendication",
         "graines": {"entropie": ENTROPIE, "regle": "SeedSequence(entropie, spawn_key=(indice de partie, indice de cas ou de dose, "
                     "indice du monde[, 1 pour l'échantillonnage d'importance]))", "parties": list(PARTIES),
                     "cas_taille": list(CAS_TAILLE), "doses": list(DOSES)},
         "versions": {"python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__},
         "juge": {"alpha": ALPHA, "seuil_log": round(SEUIL, 6), "issues": K, "traits": DIM, "entrainement": N_ENT}}
    d.update(extra or {})
    return d


def _ecrire(nom, sortie):
    os.makedirs(SORTIES, exist_ok=True)
    chemin = os.path.join(SORTIES, nom)
    if os.path.exists(chemin):
        raise SystemExit(f"refus d'écraser {chemin}")
    with open(chemin, "w", encoding="utf-8") as f:
        json.dump(sortie, f, ensure_ascii=False, indent=1)
    print("écrit", chemin)


# --- parties -----------------------------------------------------------------------------------------------------------
def partie_taille(cas, nb):
    t0 = time.time()
    with Pool(PROCESSUS) as pool:
        sorties = pool.map(juger_taille, [(cas, i) for i in range(nb)], chunksize=8)
    reg = np.array([s["regret"] for s in sorties])
    w0 = tirer_monde(cas, (PARTIES.index("taille"), CAS_TAILLE.index(cas), 0))
    inst = [int(t) for t in w0["inst"]]
    d = (2 if cas.startswith("mor_") else 1) * (w0["J"] - 1) + K
    exact = bool(sorties[0]["exact"])
    melange = {"calcul": "exact (polynômes symétriques élémentaires, moments de Dirichlet, quadrature de Gauss-Legendre)" if exact
               else f"importance sur les proportions entre lois connues ({NOEUDS_SIX_LOIS} nœuds), le reste intégré exactement"}
    if exact:
        melange["ecart_max_double_precision_contre_precision_etendue"] = float(max(s["ecart_precision"] for s in sorties if "ecart_precision" in s))
        melange["mondes_controles_en_precision_etendue"] = int(sum("ecart_precision" in s for s in sorties))
    else:
        err = np.array([s["erreur_importance"] for s in sorties if "erreur_importance" in s])
        melange["taille_effective_mediane_t_final"] = round(float(np.median([s["ess"] for s in sorties])), 1)
        melange["taille_effective_min_t_final"] = round(float(np.min([s["ess"] for s in sorties])), 1)
        melange["erreur_contre_reference_12000_noeuds_nats"] = {
            "mondes": int(len(err)), "min": round(float(err.min()), 3), "mediane": round(float(np.median(err)), 4),
            "max": round(float(err.max()), 3)}
    sortie = _entete(f"taille:{cas}", {
        "cas": cas, "mondes": nb, "tirages": int(w0["n"]), "instants": inst, "lois_connues": int(w0["J"]), "dimension": d,
        "carte": (f"loi du monde élevée à la puissance {EXPOSANT_SURCONFIANCE} puis normalisée (hors classe, monde dans la classe)"
                  if cas == "lin_carte_surconfiante" else "copie exacte de la loi du monde"), "borne_epsilon": [round(float(x), 3) for x in borne_epsilon(inst, d)],
        "melange": melange,
        "lignes": _tableau(sorties),
        "regret_effectif_nats(maximum atteint - log melange)": {str(t): {
            "mediane": round(float(np.median(reg[:, j])), 3), "q95": round(float(np.quantile(reg[:, j], 0.95)), 3),
            "max": round(float(reg[:, j].max()), 3)} for j, t in enumerate(inst)},
        "marge_R1(log melange + borne - maximum atteint, minimum sur les instants)": {
            "min": round(float(min(s["marge_R1"] for s in sorties)), 4),
            "mediane": round(float(np.median([s["marge_R1"] for s in sorties])), 3),
            "negatives": int(sum(s["marge_R1"] < -1e-6 for s in sorties))},
        "marge_R2(prediction + borne de Hedge - maximum atteint, minimum sur les instants)": {
            "min": round(float(min(s["marge_R2"] for s in sorties)), 3),
            "negatives": int(sum(s["marge_R2"] < -1e-6 for s in sorties))},
        "ecart_certificat_max": round(float(max(s["ecart_certificat"] for s in sorties)), 5),
        "ecart_certificat_mediane": round(float(np.median([s["ecart_certificat"] for s in sorties])), 6),
        "constante_calibree_R5": _grilles_r5(sorties),
        "duree_par_monde_s_moyenne": round(float(np.mean([s["duree"] for s in sorties])), 4),
        "duree_totale_s": round(time.time() - t0, 1)})
    if cas == "mor_hors_archive":
        sortie["lignes_structure_limitee_a_la_coupure_de_l_archive(hors classe, descriptif)"] = _tableau(
            [s for s in sorties if "lw_structure_archive" in s], "lw_structure_archive")
    return sortie


def partie_puissance(dose, nb):
    t0 = time.time()
    with Pool(PROCESSUS) as pool:
        sorties = pool.map(juger_puissance, [(dose, i) for i in range(nb)], chunksize=8)
    lignes = _tableau(sorties)
    ref = np.array([s["lw"]["MAX-certifie"][1] >= SEUIL for s in sorties])
    for m in lignes:
        v = np.array([s["lw"][m][1] >= SEUIL for s in sorties])
        lignes[m]["avec_ordinaires"]["promues_par_elle_seule_contre_MAX-certifie"] = int((v & ~ref).sum())
        lignes[m]["avec_ordinaires"]["promues_par_MAX-certifie_seul"] = int((~v & ref).sum())
    return _entete(f"puissance:{dose}", {
        "dose": dose, "mondes": nb, "monde": "(1 - dose)·(½ L1 + ½ L2) + dose·N, N loi softmax neuve ; carte = loi du monde",
        "structure": "ordinaires + membre linéaire + membre par morceaux sur la coupure de l'archive ; mêmes tirages, mêmes "
                     "instants, même seuil pour toutes les méthodes",
        "lignes": lignes, "constante_calibree_R5": _grilles_r5(sorties),
        "marge_R1_min": round(float(min(s["marge_R1"] for s in sorties)), 4),
        "surcout_R1_sur_le_maximum_certifie_t200_nats": {
            "mediane": round(float(np.median([s["surcout_R1"] for s in sorties])), 3),
            "min": round(float(np.min([s["surcout_R1"] for s in sorties])), 3)},
        "ecart_certificat_max": round(float(max(s["ecart_certificat"] for s in sorties)), 5),
        "duree_par_monde_s_moyenne": round(float(np.mean([s["duree"] for s in sorties])), 4),
        "duree_totale_s": round(time.time() - t0, 1)})


def partie_bornes():
    """Contrôles sans tirage de monde : la borne ε contre le pire regret exact du mélange uniforme ; réglage de Hedge ;
    suites défavorables construites à la main (mélange exact)."""
    t0 = time.time()
    inst = np.arange(25, 201, 25)
    table_b = []
    for d in (4, 5, 8, 13):
        # sommet δ_k seul explicatif : mélange = E[ρ_k^t] = 1 / C(t + d, d) pour le polytope de dimension d (Dirichlet(1,…,1,a))
        pire = [float(gammaln(t + d + 1) - gammaln(t + 1) - gammaln(d + 1)) for t in inst]
        b = borne_epsilon(inst, d)
        table_b.append({"dimension": d, "borne_epsilon": [round(float(x), 3) for x in b],
                        "regret_exact_au_sommet_log_C(t+d,d)": [round(x, 3) for x in pire],
                        "ecart_min": round(float(np.min(b - np.array(pire))), 4),
                        "borne_respectee": bool(np.all(b >= np.array(pire)))})
    hedge = []
    for C in (1, 2):
        eta, gamma, b200 = reglage_hedge(200, 5, C)
        hedge.append({"cellules": C, "composantes": 5, "eta": round(eta, 5), "gamma": round(gamma, 5),
                      "borne_nats": {str(int(t)): round(float(borne_hedge(t, 5, C, eta, gamma)), 2) for t in inst}})
    # suites défavorables, membre linéaire à deux lois connues, mélange exact (aucun aléa dans le calcul)
    rng = rng_de(PARTIES.index("bornes"), 0)
    n = 200
    pires = []
    violations, controles, viol_hedge = 0, 0, 0
    eta, gamma, _ = reglage_hedge(n, 5, 1)

    def controle(nom, y, Lobs):
        nonlocal violations, controles, viol_hedge
        zero = np.zeros(n, dtype=int)
        A, _ = matrice_sommets(Lobs, y, zero, 1)
        att, cert, _ = max_certifie(A, inst, iterations=3000, tol=1e-7)
        Cn, lw = noeuds_exacts(Lobs, zero, 1)
        mix = melange_noeuds(Cn, lw, y, 2, inst)
        reg = att - mix
        b = borne_epsilon(inst, 4)
        violations += int((reg > b + 1e-9).sum())
        controles += len(inst)
        X = np.concatenate([Lobs, np.eye(K)[y]], axis=1)
        r2 = gradient_exponentie(X, zero, 1, eta, gamma)[inst - 1] + borne_hedge(inst, 5, 1, eta, gamma)
        viol_hedge += int((r2 < att - 1e-9).sum())
        return {"suite": nom, "regret_exact_t200": round(float(reg[-1]), 4), "borne_t200": round(float(b[-1]), 4),
                "part_de_la_borne_max_sur_les_instants": round(float((reg / b).max()), 4),
                "regret_gradient_lisse_t200": round(float(att[-1] - (r2[-1] - borne_hedge(200, 5, 1, eta, gamma))), 3)}

    y0 = np.zeros(n, dtype=int)
    bas = np.full((n, 2), PLANCHER)
    pires.append(controle("issue constante, lois connues au plancher (sommet δ_k seul explicatif)", y0, bas))
    pires.append(controle("issue constante, loi 1 certaine, loi 2 au plancher", y0, np.stack([np.ones(n), np.full(n, PLANCHER)], 1)))
    ycyc = np.arange(n) % K
    pires.append(controle("issues en cycle, loi 1 certaine de l'issue observée, loi 2 au plancher", ycyc,
                          np.stack([np.ones(n), np.full(n, PLANCHER)], 1)))
    half = np.stack([np.where(np.arange(n) < n // 2, 1.0, PLANCHER), np.where(np.arange(n) < n // 2, PLANCHER, 1.0)], 1)
    pires.append(controle("issues en cycle, loi 1 certaine sur la première moitié, loi 2 sur la seconde", ycyc, half))
    alea = {"suites": 400, "part_de_la_borne_max": 0.0}
    for _ in range(400):
        y = rng.integers(0, K, size=n) if rng.random() < 0.7 else np.full(n, int(rng.integers(0, K)))
        niveaux = np.array([PLANCHER, 1e-3, 0.3, 1.0])
        Lobs = niveaux[rng.integers(0, 4, size=(n, 2))]
        if rng.random() < 0.5:                                  # une loi explicative par tirage
            qui = rng.integers(0, 3, size=n)
            Lobs = np.where(np.stack([qui == 0, qui == 1], 1), 1.0, PLANCHER)
        r = controle("aleatoire", y, Lobs)
        alea["part_de_la_borne_max"] = max(alea["part_de_la_borne_max"], r["part_de_la_borne_max_sur_les_instants"])
    return _entete("bornes", {
        "table_borne_epsilon_contre_pire_regret_exact": table_b, "reglage_hedge": hedge,
        "suites_defavorables_membre_lineaire_dimension_4": pires, "suites_aleatoires_extremes": alea,
        "controles_borne_epsilon": controles, "depassements_borne_epsilon": violations,
        "depassements_borne_hedge": viol_hedge, "duree_s": round(time.time() - t0, 1)})


def _un_estimateur(arg):
    """Estimateur d'importance de l'auteur (ses fonctions, appelées comme dans son programme de jugement) contre le
    mélange exact du réfutateur, sur les mondes du réfutateur."""
    cas, i = arg
    sys.path.insert(0, ICI)
    import essai_regret_banc_v1 as bc
    ic = CAS_TAILLE.index(cas)
    w = tirer_monde(cas, (PARTIES.index("estimateur"), ic, i))
    inst, y, Lobs, n = w["inst"], w["y"], w["Lobs"], w["n"]
    C = 2 if cas.startswith("mor_") else 1
    cell = w["c_arch"] if C == 2 else np.zeros(n, dtype=int)
    A, _ = matrice_sommets(Lobs, y, cell, C)
    att, cert, _ = max_certifie(A, inst)
    Cn, lw = noeuds_exacts(Lobs, cell, C)
    exact = melange_noeuds(Cn, lw, y, C + 1, inst)
    T = len(inst)
    cel = np.tile(cell, (T, 1))
    act = np.arange(n)[None, :] < inst[:, None]
    _, att_a, _, (s_, r_, m_) = bc.em_certifie(Lobs, y, cel, np.full(T, C), act, rendre_parametres=True)
    rng = np.random.default_rng([int(rng_de(PARTIES.index("estimateur"), ic, i, 1).integers(0, 2**31)), 7])
    est = np.empty(T)
    for it, t in enumerate(inst):
        prm = (s_[it], r_[it], m_[it][:C])
        cpt = bc.comptes_em(Lobs[:t], y[:t], cell[:t], C, prm)
        est[it] = bc.log_melange_uniforme(Lobs[:t], y[:t], cell[:t], C, rng, nb=1000, comptes=cpt)
    R = borne_epsilon(inst, C + K)
    sup_bas = np.maximum(att, att_a)
    return {"erreur": [float(x) for x in est - exact], "marge_estimee": float((est + R - sup_bas).min()),
            "marge_exacte": float((exact + R - sup_bas).min()),
            "ecart_des_maximums_atteints": float(np.abs(att - att_a).max())}


def partie_estimateur(nb):
    """Deux cents mondes par cas par défaut (limite de dix minutes sur machine partagée)."""
    t0 = time.time()
    h = hashlib.sha256(open(os.path.join(ICI, "essai_regret_banc_v1.py"), "rb").read()).hexdigest()
    if h != EMPREINTE_BANC_AUTEUR:
        raise SystemExit("le banc de l'auteur n'a pas l'empreinte attendue")
    cas_liste = ("lin_interieur", "lin_poids_extremes", "lin_bord", "lin_sommet_delta", "lin_sommet_loi",
                 "mor_sommet", "mor_interieur", "mor_poids_extremes")
    res = {}
    with Pool(PROCESSUS) as pool:
        for cas in cas_liste:
            s = pool.map(_un_estimateur, [(cas, i) for i in range(nb)], chunksize=4)
            e = np.array([x["erreur"] for x in s])
            res[cas] = {"mondes": nb, "dimension": (2 if cas.startswith("mor_") else 1) + K,
                        "erreur_estimation_moins_exact_nats": {
                            "tous_instants": {"min": round(float(e.min()), 3), "q05": round(float(np.quantile(e, 0.05)), 3),
                                              "mediane": round(float(np.median(e)), 4),
                                              "q95": round(float(np.quantile(e, 0.95)), 3), "max": round(float(e.max()), 3)},
                            "t200": {"min": round(float(e[:, -1].min()), 3), "mediane": round(float(np.median(e[:, -1])), 4),
                                     "max": round(float(e[:, -1].max()), 3)}},
                        "marge_min(melange estime + borne - maximum atteint)": round(float(min(x["marge_estimee"] for x in s)), 3),
                        "marge_min(melange exact + borne - maximum atteint)": round(float(min(x["marge_exacte"] for x in s)), 3),
                        "calculs_ou_le_melange_estime_plus_la_borne_passe_sous_le_maximum": int(sum(x["marge_estimee"] < -1e-9 for x in s)),
                        "ecart_max_entre_les_deux_maximums_atteints": round(float(max(x["ecart_des_maximums_atteints"] for x in s)), 4)}
    return _entete("estimateur", {
        "objet": "estimateur d'importance de l'auteur (essai_regret_banc_v1.log_melange_uniforme, 1 000 échantillons, comptes de "
                 "son EM) contre le mélange exact du réfutateur, en dimension 4 (membre linéaire) et 5 (membre par morceaux)",
        "empreinte_banc_auteur": h, "cas": res, "duree_totale_s": round(time.time() - t0, 1)})


def partie_fusion():
    """Rassemble les sorties partielles (avec leurs empreintes), résume la taille, et lit la constante calibrée (R5)."""
    parties = {}
    for nom in sorted(os.listdir(SORTIES)):
        if nom.startswith("attaque_regret_v1--") and nom.endswith(".json"):
            brut = open(os.path.join(SORTIES, nom), "rb").read()
            d = json.loads(brut)
            parties[d["partie"]] = {"fichier": f"attaque-sorties/{nom}", "empreinte": hashlib.sha256(brut).hexdigest(), "contenu": d}
    tailles = {p.split(":", 1)[1]: v["contenu"] for p, v in parties.items() if p.startswith("taille:")}
    puiss = {p.split(":", 1)[1]: v["contenu"] for p, v in parties.items() if p.startswith("puissance:")}
    resume = {}
    for cas, d in tailles.items():
        for m, l in d["lignes"].items():
            for regime in ("membre_seul", "avec_ordinaires"):
                x = l[regime]
                resume.setdefault(m, {}).setdefault(regime, {})[cas] = [x["promues"], x["mondes"], x["intervalle_95"][0], x["intervalle_95"][1]]
    pires = {m: {regime: max(v[3] for v in r.values()) for regime, r in rr.items()} for m, rr in resume.items()}
    calib = [c for c in CAS_CALIBRATION if c in tailles]

    def taux(d, cle, grille, valeur):
        i = int(np.argmin(np.abs(grille - valeur)))
        return d["constante_calibree_R5"][cle]["promues_par_valeur_de_grille"][i] / d["mondes"]

    def plus_petit(cas_liste, cle, grille):
        for g in grille:
            if all(taux(tailles[c], cle, grille, g) <= ALPHA for c in cas_liste):
                return float(g)
        return None

    r5 = {}
    for regime in ("seul", "ord"):
        for sorte, grille in (("c", GRILLE_C), ("k", GRILLE_KAPPA)):
            cle = f"{sorte}_{regime}"
            par_cas = {c: plus_petit([c], cle, grille) for c in tailles}
            v_int = par_cas.get("lin_interieur")
            v_pire = plus_petit(calib, cle, grille) if calib else None
            bloc = {"plus_petite_valeur_de_grille_a_taux_simule_au_plus_alpha_par_cas": par_cas,
                    "calibree_sur_les_copies_interieures_seulement": v_int,
                    "calibree_sur_le_pire_cas_simule(cas de calibration)": v_pire}
            if v_int is not None:
                bloc["taux_de_chaque_cas_a_la_valeur_calibree_sur_l_interieur"] = {
                    c: round(taux(tailles[c], cle, grille, v_int), 4) for c in tailles}
            if v_pire is not None:
                bloc["taux_de_chaque_cas_a_la_valeur_calibree_sur_le_pire_cas"] = {
                    c: round(taux(tailles[c], cle, grille, v_pire), 4) for c in tailles}
            if regime == "ord" and puiss:
                bloc["puissance_avec_ordinaires"] = {
                    dose: {"R5_calibree_sur_le_pire_cas": None if v_pire is None else round(taux(d, cle, grille, v_pire), 4),
                           "R5_calibree_sur_l_interieur(taille non tenue ailleurs)": None if v_int is None else round(taux(d, cle, grille, v_int), 4),
                           "MAX-certifie": d["lignes"]["MAX-certifie"]["avec_ordinaires"]["taux"],
                           "R1-melange+borne": d["lignes"]["R1-melange+borne"]["avec_ordinaires"]["taux"]}
                    for dose, d in sorted(puiss.items())}
            r5[cle] = bloc
    return _entete("fusion", {
        "resume_taille(promues, mondes, borne basse, borne haute de l'intervalle à 95 %)": resume,
        "plus_grande_borne_haute_par_methode(tous cas de taille)": pires,
        "lecture_constante_calibree_R5": {
            "sens": "c : dénominateur = log mélange + c (constante) ; k : dénominateur = log mélange + k·R(t, d) ; « seul » : "
                    "membre ajusté seul ; « ord » : avec les membres ordinaires du juge. Calibration = plus petite valeur de "
                    "grille dont le taux simulé de promotion est au plus α. La calibration par simulation n'est pas une "
                    "garantie : elle ne voit que les cas simulés.",
            "cas_de_calibration": calib, "resultats": r5},
        "parties": parties})


def main():
    partie = sys.argv[1]
    if partie == "bornes":
        _ecrire("attaque_regret_v1--bornes.json", partie_bornes())
    elif partie == "estimateur":
        _ecrire("attaque_regret_v1--estimateur.json", partie_estimateur(int(sys.argv[2]) if len(sys.argv) > 2 else 200))
    elif partie.startswith("taille:"):
        cas = partie.split(":", 1)[1]
        _ecrire(f"attaque_regret_v1--taille--{cas}.json", partie_taille(cas, int(sys.argv[2]) if len(sys.argv) > 2 else 2000))
    elif partie.startswith("puissance:"):
        dose = float(partie.split(":", 1)[1])
        _ecrire(f"attaque_regret_v1--puissance--d{dose}.json", partie_puissance(dose, int(sys.argv[2]) if len(sys.argv) > 2 else 1000))
    elif partie == "fusion":
        chemin = os.path.join(ICI, "attaque_regret_v1.json")
        if os.path.exists(chemin):
            raise SystemExit(f"refus d'écraser {chemin}")
        with open(chemin, "w", encoding="utf-8") as f:
            json.dump(partie_fusion(), f, ensure_ascii=False, indent=1)
        print("écrit", chemin)
    else:
        raise SystemExit(__doc__)


if __name__ == "__main__":
    main()
