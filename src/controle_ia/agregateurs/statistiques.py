"""Statistiques d'agrégation sur un épisode (N, T). Plus grand = plus suspect.

Les scores sont standardisés par (μ₀, σ) honnêtes, connus ou estimés sur épisodes honnêtes.
Statistiques symétriques (invariantes par toute permutation des cases) : somme terminale,
max par action. Statistiques d'ordre locales : balayage, somme cumulée de Page,
co-élévation. Statistiques d'ordre globales : autocorrélation, test des suites,
corrélation entre agents (sans garantie face à un attaquant adaptatif, note v2, T3).
"""
from __future__ import annotations

import math

import numpy as np

from ..gardes import GardeArret
from .indexation import verifier_episode


def _z(X, mu0: float, sigma: float) -> np.ndarray:
    if not (sigma > 0 and np.isfinite(sigma)):
        raise GardeArret(f"σ = {sigma} : réel strictement positif attendu")
    return (verifier_episode(X) - mu0) / sigma


def somme_terminale(X, mu0: float = 0.0, sigma: float = 1.0) -> float:
    """Σ (X − μ₀)/σ, sommation exacte (math.fsum) : invariante par permutation au bit près."""
    return math.fsum(_z(X, mu0, sigma).ravel().tolist())


def max_par_action(X, mu0: float = 0.0, sigma: float = 1.0) -> float:
    return float(np.max(_z(X, mu0, sigma)))


def balayage(X, w: int, mu0: float = 0.0, sigma: float = 1.0) -> float:
    """Maximum, sur les agents et les fenêtres de w pas consécutifs, de la somme glissante (T3)."""
    Z = _z(X, mu0, sigma)
    if not (1 <= w <= Z.shape[1]):
        raise GardeArret(f"fenêtre w = {w} hors de [1, T = {Z.shape[1]}]")
    c = np.concatenate([np.zeros((Z.shape[0], 1)), np.cumsum(Z, axis=1)], axis=1)
    return float(np.max(c[:, w:] - c[:, :-w]))


def page_cusum(X, k: float = 0.5, mu0: float = 0.0, sigma: float = 1.0, poolee: bool = False) -> float:
    """Somme cumulée de Page, C_t = max(0, C_{t−1} + z_t − k) ; max sur agents et pas.
    poolee=True : sur la somme des agents par pas, divisée par √N."""
    Z = _z(X, mu0, sigma)
    if poolee:
        Z = Z.sum(axis=0, keepdims=True) / math.sqrt(Z.shape[0])
    meilleur = 0.0
    for ligne in Z:
        c = 0.0
        for z in ligne:
            c = max(0.0, c + z - k)
            meilleur = max(meilleur, c)
    return float(meilleur)


def co_elevation(X, m: int, mu0: float = 0.0, sigma: float = 1.0) -> float:
    """Maximum sur les pas de la somme des m plus hauts scores standardisés du pas (T3, axe agents)."""
    Z = _z(X, mu0, sigma)
    if not (1 <= m <= Z.shape[0]):
        raise GardeArret(f"m = {m} hors de [1, N = {Z.shape[0]}]")
    hauts = np.sort(Z, axis=0)[-m:, :]
    return float(np.max(hauts.sum(axis=0)))


def autocorrelation_lag1(X, absolue: bool = False) -> float:
    """Moyenne sur les agents de l'autocorrélation empirique de pas 1 (T ≥ 3)."""
    X = verifier_episode(X)
    if X.shape[1] < 3:
        raise GardeArret("autocorrélation : T ≥ 3 requis")
    vals = []
    for x in X:
        x = x - x.mean()
        v = float(np.dot(x, x))
        vals.append(0.0 if v == 0.0 else float(np.dot(x[:-1], x[1:])) / v)
    r = float(np.mean(vals))
    return abs(r) if absolue else r


def suites_wald_wolfowitz(X, seuil: float | None = None) -> float:
    """Wald-Wolfowitz : suites au-dessus / au-dessous du seuil (médiane de l'agent par défaut).
    Renvoie −z moyen sur les agents : peu de suites (regroupement) = suspect."""
    X = verifier_episode(X)
    zs = []
    for x in X:
        s = np.median(x) if seuil is None else seuil
        b = x > s
        n1, n2 = int(b.sum()), int((~b).sum())
        if n1 == 0 or n2 == 0:
            zs.append(0.0)
            continue
        runs = 1 + int(np.count_nonzero(b[1:] != b[:-1]))
        mu = 2.0 * n1 * n2 / (n1 + n2) + 1.0
        var = 2.0 * n1 * n2 * (2.0 * n1 * n2 - n1 - n2) / ((n1 + n2) ** 2 * (n1 + n2 - 1))
        zs.append(0.0 if var <= 0 else (runs - mu) / math.sqrt(var))
    return float(-np.mean(zs))


def correlation_inter_agents(X) -> float:
    """Moyenne des corrélations de Pearson entre séries d'agents (N ≥ 2, T ≥ 3)."""
    X = verifier_episode(X)
    if X.shape[0] < 2 or X.shape[1] < 3:
        raise GardeArret("corrélation entre agents : N ≥ 2 et T ≥ 3 requis")
    Xc = X - X.mean(axis=1, keepdims=True)
    normes = np.sqrt((Xc ** 2).sum(axis=1))
    if np.any(normes == 0):
        raise GardeArret("corrélation entre agents : série constante")
    C = (Xc @ Xc.T) / np.outer(normes, normes)
    iu = np.triu_indices(X.shape[0], k=1)
    return float(C[iu].mean())


STATISTIQUES = {
    "somme_terminale": somme_terminale,
    "max_par_action": max_par_action,
    "balayage": balayage,
    "page_cusum": page_cusum,
    "co_elevation": co_elevation,
    "autocorrelation_lag1": autocorrelation_lag1,
    "suites_wald_wolfowitz": suites_wald_wolfowitz,
    "correlation_inter_agents": correlation_inter_agents,
}
