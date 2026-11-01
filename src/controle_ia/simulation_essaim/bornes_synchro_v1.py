"""Bornes exactes, sans tirage, de la puissance de la co-élévation (`coelev_comptage`) sous synchronisation — v1.

Module neuf (R12) du préenregistrement hors échantillon (`essaim-hors-echantillon-v1`) ; n'importe que
`calibrage` de la version 1, inchangé.

Synchronisation (`menaces.synchro`, r = 1) : m agents tirés uniformément placent leur plus haut score au pas
commun s ; leurs autres scores gardent leur ordre dans les T − 1 autres pas.

**Loi de référence (cases iid, P(X ≥ u) = q).** Pour un agent synchronisé, N = #{t : X_t ≥ u} ~ Bin(T, q) ;
son indicateur au pas s vaut 1{N ≥ 1} ; sur les T − 1 autres pas, ses indicateurs forment un sous-ensemble
uniforme de taille M = max(N − 1, 0) (l'argmax est uniforme parmi les cases au-dessus de u, et retirer un
élément uniforme d'un sous-ensemble uniforme laisse un sous-ensemble uniforme). Un agent non synchronisé a des
indicateurs iid Bernoulli(q). Les agents sont indépendants. Les lois jointes des comptes C_t sur 1, 2 ou 3 pas
sont donc exactes (convolution sur les agents), d'où les bornes de Bonferroni de P(max_t C_t ≥ j) :
    max(P(C_s ≥ j), S1 − S2) ≤ P(max_t C_t ≥ j) ≤ min(S1, S1 − S2 + S3),
et, pour le seuil aléatoirisé (c, γ), P(alarme) = (1 − γ) P(V ≥ c + 1) + γ P(V ≥ c).

**Équicorrélation c entre agents d'un même pas** (`lois`, type `equicorrelation` : X_{i,t} = √c W_t +
√(1 − c) ε_{i,t}) : borne inférieure exacte P(C_s ≥ j) seulement, par quadrature sur W_s ; les agents
synchronisés y sont dépendants par les W_t des autres pas.
"""
from __future__ import annotations

import math
from itertools import product

import numpy as np
from scipy import stats
from scipy.special import comb

from ..gardes import GardeArret
from . import calibrage as cal


def _verifier(K: int, T: int, m: int, q: float) -> None:
    if not (K >= 2 and T >= 3 and 1 <= m <= K and 0.0 < q < 1.0):
        raise GardeArret(f"bornes de synchronisation : K = {K}, T = {T}, m = {m}, q = {q} hors domaine")


def _loi_M(T: int, q: float) -> tuple[np.ndarray, float]:
    """P(M = k), k = 0…T − 1, M = max(N − 1, 0), N ~ Bin(T, q) ; et P(N = 0)."""
    pN = stats.binom.pmf(np.arange(T + 1), T, q)
    pM = np.zeros(T)
    pM[0] = pN[0] + pN[1]
    pM[1:] = pN[2:]
    return pM, float(pN[0])


def _motif_autres(pM: np.ndarray, T: int, a: int, b: int) -> float:
    """P(a uns et b zéros à a + b pas donnés parmi les T − 1 autres pas), agent synchronisé."""
    n, r = T - 1, a + b
    k = np.arange(pM.size)
    num = comb(n - r, k - a)                        # nul hors du domaine (k − a < 0 ou > n − r)
    num = np.where((k >= a) & (k - a <= n - r), num, 0.0)
    return float(np.sum(pM * num / comb(n, k)))


def _pmf_agent(T: int, q: float, synchronise: bool, avec_s: bool, r: int) -> np.ndarray:
    """Loi jointe des indicateurs d'un agent sur r pas (le premier est s si avec_s) : tableau 2 × … × 2."""
    P = np.zeros((2,) * r)
    if not synchronise:
        for motif in product((0, 1), repeat=r):
            P[motif] = np.prod([q if x else 1 - q for x in motif])
        return P
    pM, pN0 = _loi_M(T, q)
    for motif in product((0, 1), repeat=r):
        autres = motif[1:] if avec_s else motif
        a, b = sum(autres), len(autres) - sum(autres)
        if not avec_s:
            P[motif] = _motif_autres(pM, T, a, b)
            continue
        # indicateur en s : 1{N ≥ 1}. N = 0 ⇔ M = 0 et N ≠ 1 : tous les autres à zéro.
        p0 = pN0 if a == 0 else 0.0
        P[motif] = (_motif_autres(pM, T, a, b) - p0) if motif[0] == 1 else p0
    if not np.isclose(P.sum(), 1.0, atol=1e-12):
        raise GardeArret("loi jointe d'un agent synchronisé : masse ≠ 1")
    return P


def _loi_comptes(K: int, T: int, m: int, q: float, avec_s: bool, r: int) -> np.ndarray:
    """Loi jointe des comptes (C_t) sur r pas (le premier est s si avec_s) : tableau (K + 1)^r."""
    sortie = np.zeros((1,) * r)
    sortie[(0,) * r] = 1.0
    for synchro, n in ((True, m), (False, K - m)):
        P = _pmf_agent(T, q, synchro, avec_s, r)
        for _ in range(n):
            nouveau = np.zeros(tuple(d + 1 for d in sortie.shape))
            for motif in product((0, 1), repeat=r):
                if P[motif] == 0.0:
                    continue
                tranche = tuple(slice(x, x + d) for x, d in zip(motif, sortie.shape))
                nouveau[tranche] += P[motif] * sortie
            sortie = nouveau
    return sortie


def _queue_jointe(L: np.ndarray, j: int) -> float:
    return float(L[(slice(j, None),) * L.ndim].sum())


def bornes_union(K: int, T: int, m: int, q: float, j: int) -> tuple[float, float]:
    """(borne basse, borne haute) exactes de P(max_t C_t ≥ j) sous synchronisation, loi de référence."""
    _verifier(K, T, m, q)
    if j <= 0:
        return 1.0, 1.0
    if j > K:
        return 0.0, 0.0
    n = T - 1
    ps = _queue_jointe(_loi_comptes(K, T, m, q, True, 1), j)
    po = _queue_jointe(_loi_comptes(K, T, m, q, False, 1), j)
    pso = _queue_jointe(_loi_comptes(K, T, m, q, True, 2), j)
    poo = _queue_jointe(_loi_comptes(K, T, m, q, False, 2), j)
    psoo = _queue_jointe(_loi_comptes(K, T, m, q, True, 3), j)
    pooo = _queue_jointe(_loi_comptes(K, T, m, q, False, 3), j)
    S1 = ps + n * po
    S2 = n * pso + comb(n, 2) * poo
    S3 = comb(n, 2) * psoo + comb(n, 3) * pooo
    bas = max(ps, S1 - S2, 0.0)
    haut = min(S1, S1 - S2 + S3, 1.0)
    if not (bas <= haut + 1e-12):
        raise GardeArret(f"bornes de Bonferroni incohérentes : {bas} > {haut}")
    return bas, haut


def bornes_puissance(K: int, T: int, m: int, q: float, seuil) -> tuple[float, float]:
    """Bornes exactes de la puissance de `coelev_comptage` au seuil aléatoirisé (c, γ), loi de référence."""
    c, g = seuil
    if c != math.floor(c):
        raise GardeArret(f"seuil {c} non entier pour la co-élévation")
    b1, h1 = bornes_union(K, T, m, q, int(c) + 1)
    b0, h0 = bornes_union(K, T, m, q, int(c))
    return (1 - g) * b1 + g * b0, (1 - g) * h1 + g * h0


def seuil_coelev_exact(K: int, T: int, q: float, alpha: float) -> tuple[float, float]:
    return cal.seuils_exacts(K, T, q, alpha)["coelev_comptage"]


# --- équicorrélation : borne basse exacte au pas commun ---
def borne_synchro_correlee(K: int, T: int, m: int, c: float, q: float, seuil) -> float:
    """P(alarme de C_s) ≤ puissance, sous équicorrélation c : au pas commun, les m agents synchronisés portent leur
    maximum ; conditionnellement à W_s = w, un ensemble donné de a agents synchronisés a tous son maximum sous u
    avec la probabilité Φ_w^a · (E_W[Φ_W^a])^{T−1}, Φ_w = Φ((u − √c w)/√(1 − c)) ; les K − m autres sont
    Bin(K − m, 1 − Φ_w). Inclusion-exclusion sur les ensembles (agents échangeables), quadrature sur w."""
    _verifier(K, T, m, q)
    if not (0.0 <= c < 1.0):
        raise GardeArret(f"c = {c} hors de [0, 1[")
    u = cal.seuil_par_case(q)
    x, w = np.polynomial.hermite_e.hermegauss(cal.NOEUDS_GH)
    w = w / math.sqrt(2.0 * math.pi)
    s = math.sqrt(1.0 - c)
    Phi = stats.norm.cdf((u - math.sqrt(c) * x) / s)                    # Φ_w aux nœuds
    G = np.array([np.sum(w * Phi ** a) for a in range(m + 1)])          # E_W[Φ_W^a]
    pmf = np.zeros(K + 1)
    for xk, wk, ph in zip(x, w, Phi):
        g = np.array([ph ** a * G[a] ** (T - 1) for a in range(m + 1)])  # P(a agents donnés tous < u | w)
        # P(exactement j au-dessus parmi m) = C(m, j) Σ_i (−1)^i C(j, i) g(m − j + i)
        pj = np.array([comb(m, j) * sum((-1) ** i * comb(j, i) * g[m - j + i] for i in range(j + 1))
                       for j in range(m + 1)])
        pj = np.clip(pj, 0.0, None)
        autres = stats.binom.pmf(np.arange(K - m + 1), K - m, 1.0 - ph)
        pmf += wk * np.convolve(pj, autres)
    pmf = np.clip(pmf, 0.0, None)
    pmf /= pmf.sum()
    return cal.taux_discret(np.minimum(np.cumsum(pmf), 1.0), seuil)


def seuil_coelev_correle_exact(K: int, T: int, c: float, q: float, alpha: float) -> tuple[float, float]:
    """Seuil exact de taille α de max_t C_t sous équicorrélation (pas indépendants, C_t de loi mélange)."""
    u = cal.seuil_par_case(q)
    x, w = np.polynomial.hermite_e.hermegauss(cal.NOEUDS_GH)
    w = w / math.sqrt(2.0 * math.pi)
    p = stats.norm.sf((u - math.sqrt(c) * x) / math.sqrt(1.0 - c))
    pmf = sum(wk * stats.binom.pmf(np.arange(K + 1), K, pk) for pk, wk in zip(p, w))
    pmf = pmf / pmf.sum()
    return cal.seuil_max_discret(np.minimum(np.cumsum(pmf), 1.0), T, alpha)
