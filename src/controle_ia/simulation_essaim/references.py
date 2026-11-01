"""Références scalaires des statistiques d'essaim : un épisode (K, T), boucles explicites.

Écrites indépendamment des versions vectorisées de `statistiques` (sommes exactes `math.fsum`,
boucles sur les pas et les agents). La garde d'équivalence du run exige un écart relatif ≤ 1e-9
sur chaque épisode testé (liste d'arrêt).
"""
from __future__ import annotations

import math

import numpy as np

from ..agregateurs import co_elevation, max_par_action, somme_terminale
from ..agregateurs.indexation import verifier_episode
from ..agregateurs.processus_e import trajectoire_e
from ..gardes import GardeArret
from .statistiques import FRACTIONS_LAMBDA, M_COELEV


def _logmoyexp(valeurs: list[float]) -> float:
    m = max(valeurs)
    if m == -math.inf:
        return -math.inf
    return m + math.log(sum(math.exp(v - m) for v in valeurs) / len(valeurs))


def comptes(X, u: float) -> list[int]:
    X = verifier_episode(X)
    return [sum(1 for i in range(X.shape[0]) if X[i, t] >= u) for t in range(X.shape[1])]


def ref_agent_moyenne(X) -> float:
    X = verifier_episode(X)
    return max(math.fsum(X[i].tolist()) / math.sqrt(X.shape[1]) for i in range(X.shape[0]))


def ref_agent_comptage(X, u: float) -> int:
    X = verifier_episode(X)
    return max(sum(1 for t in range(X.shape[1]) if X[i, t] >= u) for i in range(X.shape[0]))


def ref_pas_moyenne(X) -> float:
    X = verifier_episode(X)
    return max(math.fsum(X[:, t].tolist()) / math.sqrt(X.shape[0]) for t in range(X.shape[1]))


def ref_e_coelev(X, u: float, q: float, fractions=FRACTIONS_LAMBDA) -> float:
    X = verifier_episode(X)
    K = X.shape[0]
    lams = [f / (K * q) for f in fractions]
    logs = [0.0] * len(lams)
    meilleur = -math.inf
    for c in comptes(X, u):
        logs = [l + math.log(1.0 + lam * (c - K * q)) for l, lam in zip(logs, lams)]
        meilleur = max(meilleur, _logmoyexp(logs))
    return meilleur


def ref_ed_coelev(X, u: float, q: float, fractions=FRACTIONS_LAMBDA) -> float:
    X = verifier_episode(X)
    K = X.shape[0]
    lams = [f / (K * q) for f in fractions]
    D = [-math.inf] * len(lams)
    meilleur = -math.inf
    for c in comptes(X, u):
        D = [max(d, 0.0) + math.log(1.0 + lam * (c - K * q)) for d, lam in zip(D, lams)]
        meilleur = max(meilleur, _logmoyexp(D))
    return meilleur


def ref_e_pas(X, rho: float) -> float:
    """Référence de `agregateurs` : trajectoire e unilatérale aux frontières de pas (L4)."""
    return float(np.max(trajectoire_e(X, 0.0, 1.0, rho, "unilateral", frontieres_de_pas=True)))


def reference(stat: str, X, params: dict) -> float:
    u, q = params.get("u"), params.get("q")
    if stat == "somme":
        return somme_terminale(X)
    if stat == "max":
        return max_par_action(X)
    if stat == "comptage":
        return float(sum(comptes(X, u)))
    if stat == "agent_moyenne":
        return ref_agent_moyenne(X)
    if stat == "agent_comptage":
        return float(ref_agent_comptage(X, u))
    if stat == "pas_moyenne":
        return ref_pas_moyenne(X)
    if stat == "coelev_comptage":
        return float(max(comptes(X, u)))
    if stat == "coelev_somme3":
        return co_elevation(X, M_COELEV)
    if stat == "e_coelev":
        return ref_e_coelev(X, u, q, params["fractions"])
    if stat == "ed_coelev":
        return ref_ed_coelev(X, u, q, params["fractions"])
    if stat == "e_pas":
        return ref_e_pas(X, params["rho"])
    raise GardeArret(f"pas de référence scalaire pour {stat!r}")
