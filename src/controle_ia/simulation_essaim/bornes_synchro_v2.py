"""Puissance exacte de la co-élévation sous synchronisation, loi de référence — v2 (recommandation R6 de la
contre-lecture 1 du préenregistrement hors échantillon). Module neuf (R12) ; `bornes_synchro_v1` est inchangé et
fournit la loi jointe des indicateurs d'un agent sur r pas (`_pmf_agent`).

Inclusion-exclusion complète sur les T pas : avec A_t = {C_t ≥ j}, s le pas commun et n = T − 1,
    P(max_t C_t ≥ j) = Σ_{r ≥ 1} (−1)^{r+1} S_r,   S_r = C(n, r) P(r autres pas ≥ j) + C(n, r − 1) P(s et r − 1 autres ≥ j),
par échangeabilité des pas autres que s. Chaque probabilité jointe est exacte : convolution sur les agents des lois
jointes de leurs indicateurs, comptes plafonnés à j (seul « ≥ j » compte). La somme est arrêtée à l'ordre R dès que
S_{R+1} ≤ `TOL` ; les inégalités de Bonferroni bornent alors l'erreur par S_{R+1} (certifiée, renvoyée).
"""
from __future__ import annotations

import math

import numpy as np
from scipy.special import comb

from ..gardes import GardeArret
from .bornes_synchro_v1 import _pmf_agent, _verifier

TOL = 1e-9


def _decaler(A: np.ndarray, axe: int) -> np.ndarray:
    """Ajoute 1 au compte de l'axe donné, plafonné au dernier indice."""
    B = np.zeros_like(A)
    src = [slice(None)] * A.ndim
    dst = [slice(None)] * A.ndim
    src[axe], dst[axe] = slice(0, -1), slice(1, None)
    B[tuple(dst)] = A[tuple(src)]
    der = [slice(None)] * A.ndim
    der[axe] = -1
    B[tuple(der)] += A[tuple(der)]
    return B


def _ajouter_agent(A: np.ndarray, P: np.ndarray) -> np.ndarray:
    """Convolution d'un agent de loi jointe P (2 × … × 2) sur l'état A (comptes plafonnés)."""
    r = A.ndim
    sortie = np.zeros_like(A)

    def descendre(etat, axe, indices):
        if axe == r:
            p = P[tuple(indices)]
            if p:
                sortie.__iadd__(p * etat)
            return
        descendre(etat, axe + 1, indices + [0])
        descendre(_decaler(etat, axe), axe + 1, indices + [1])

    descendre(A, 0, [])
    return sortie


def queue_jointe(K: int, T: int, m: int, q: float, avec_s: bool, r: int, j: int) -> float:
    """P(tous les r pas ≥ j) (le premier est s si avec_s), exacte."""
    if r == 0:
        return 1.0
    A = np.zeros((j + 1,) * r)
    A[(0,) * r] = 1.0
    for synchro, n in ((True, m), (False, K - m)):
        P = _pmf_agent(T, q, synchro, avec_s, r)
        for _ in range(n):
            A = _ajouter_agent(A, P)
    return float(A[(j,) * r])


def proba_max_au_moins(K: int, T: int, m: int, q: float, j: int, tol: float = TOL) -> tuple[float, float]:
    """(P(max_t C_t ≥ j), erreur certifiée) sous synchronisation de m agents (r = 1), loi de référence."""
    _verifier(K, T, m, q)
    if j <= 0:
        return 1.0, 0.0
    if j > K:
        return 0.0, 0.0
    n = T - 1
    total, signe, R = 0.0, 1.0, 1
    while True:
        S = comb(n, R) * queue_jointe(K, T, m, q, False, R, j) if R <= n else 0.0
        S += comb(n, R - 1) * queue_jointe(K, T, m, q, True, R, j)
        total += signe * S
        signe = -signe
        if R == n + 1:
            return total, 0.0
        S_suivant = (comb(n, R + 1) * queue_jointe(K, T, m, q, False, R + 1, j) if R + 1 <= n else 0.0) + \
            comb(n, R) * queue_jointe(K, T, m, q, True, R + 1, j)
        if S_suivant <= tol:
            return total, float(S_suivant)
        R += 1


def puissance_exacte(K: int, T: int, m: int, q: float, seuil) -> tuple[float, float]:
    """(puissance exacte de `coelev_comptage` au seuil aléatoirisé (c, γ), erreur certifiée)."""
    c, g = seuil
    if c != math.floor(c):
        raise GardeArret(f"seuil {c} non entier pour la co-élévation")
    p1, e1 = proba_max_au_moins(K, T, m, q, int(c) + 1)
    p0, e0 = proba_max_au_moins(K, T, m, q, int(c))
    return (1 - g) * p1 + g * p0, (1 - g) * e1 + g * e0
