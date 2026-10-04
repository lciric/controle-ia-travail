"""Seuils de T0.3 : exacts (gaussiens), Monte-Carlo sous P₀, de Ville (log 1/α), conformes.

Convention : alarme si statistique ≥ seuil.
- Monte-Carlo : plus petit seuil t tel que P̂₀(stat ≥ t) ≤ α sur l'échantillon de calibrage
  (conservateur pour une statistique discrète) ;
- conforme : rang ⌈(K + 1)(1 − α)⌉ parmi K épisodes honnêtes entiers ; taux exact
  1 − ⌈(K + 1)(1 − α)⌉/(K + 1) ≤ α pour une statistique continue et des épisodes échangeables ;
- ρ du mélange : minimiseur de la frontière d'alarme à l'horizon n₀ (note v2, section 2).
"""
from __future__ import annotations

import math

import numpy as np
from scipy import optimize, stats

from ..agregateurs.processus_e import log_e_bilateral, log_e_unilateral
from ..gardes import GardeArret


def _alpha(alpha: float) -> float:
    if not (0.0 < alpha < 1.0):
        raise GardeArret(f"α = {alpha} hors de ]0, 1[")
    return alpha


def seuil_ville(alpha: float) -> float:
    return math.log(1.0 / _alpha(alpha))


def seuil_somme_exact(alpha: float, n0: int, bilateral: bool = False, facteur_variance: float = 1.0) -> float:
    """Seuil de Σ z sous P₀ gaussienne de variance n₀·facteur (|Σ z| si bilatéral)."""
    q = stats.norm.isf(_alpha(alpha) / 2 if bilateral else alpha)
    return float(q * math.sqrt(n0 * facteur_variance))


def seuil_max_exact(alpha: float, n0: int) -> float:
    """c_n = Φ⁻¹((1 − α)^{1/n}), calculé par la queue pour la précision."""
    queue = -math.expm1(math.log1p(-_alpha(alpha)) / n0)
    return float(stats.norm.isf(queue))


def seuil_mc(valeurs, alpha: float) -> float:
    v = np.sort(np.asarray(valeurs, dtype=float))
    if v.ndim != 1 or v.size == 0 or not np.all(np.isfinite(v)):
        raise GardeArret("calibrage : valeurs nulles absentes ou non finies")
    R = v.size
    depassements = int(math.floor(_alpha(alpha) * R + 1e-9))
    k = R - depassements
    if k >= R:
        return math.inf
    t = float(v[k])
    while (R - np.searchsorted(v, t, side="left")) / R > alpha:   # ex aequo : valeur distincte suivante
        plus = v[v > t]
        if plus.size == 0:
            return math.inf
        t = float(plus[0])
    return t


def rang_conforme(K: int, alpha: float) -> int:
    return int(math.ceil((K + 1) * (1.0 - _alpha(alpha)) - 1e-9))


def taux_conforme(K: int, alpha: float) -> float:
    return 1.0 - rang_conforme(K, alpha) / (K + 1)


def seuil_conforme(valeurs_calibrage, alpha: float) -> float:
    v = np.sort(np.asarray(valeurs_calibrage, dtype=float))
    if v.ndim != 1 or v.size == 0 or not np.all(np.isfinite(v)):
        raise GardeArret("calibrage conforme : valeurs absentes ou non finies")
    j = rang_conforme(v.size, alpha)
    return math.inf if j > v.size else float(v[j - 1])


def frontiere(n0: int, rho: float, alpha: float, cote: str) -> float:
    """s* > 0 tel que log E_{n₀}(s*) = log(1/α) (σ = 1)."""
    f = log_e_unilateral if cote == "unilateral" else log_e_bilateral
    h = seuil_ville(alpha)
    return float(optimize.brentq(lambda s: float(f(s, float(n0), 1.0, rho)) - h, 0.0, 1e7, xtol=1e-12))


def rho_optimal(n0: int, alpha: float, cote: str) -> tuple[float, float]:
    """(ρ*, s*) : ρ minimisant la frontière d'alarme à l'horizon n₀."""
    if cote not in ("unilateral", "bilateral"):
        raise GardeArret(f"côté {cote!r} inconnu")
    res = optimize.minimize_scalar(lambda lr: frontiere(n0, math.exp(lr), alpha, cote),
                                   bounds=(math.log(1e-3), math.log(10.0)), method="bounded",
                                   options={"xatol": 1e-10})
    if not res.success:
        raise GardeArret(f"ρ optimal introuvable pour n₀ = {n0} ({cote})")
    return float(math.exp(res.x)), float(res.fun)


def puissance_somme(alpha: float, n0: int, B: float) -> float:
    """L1, test z unilatéral : Φ̄(z_α − B/√n₀)."""
    return float(stats.norm.sf(stats.norm.isf(alpha) - B / math.sqrt(n0)))


def puissance_max(alpha: float, n0: int, B: float, m: int) -> float:
    """L2 : 1 − Φ(c_n)^{n−m} Φ(c_n − B/m)^m, budget réparti également sur m actions."""
    c = seuil_max_exact(alpha, n0)
    log_reste = (n0 - m) * stats.norm.logcdf(c) + m * stats.norm.logcdf(c - B / m)
    return float(-math.expm1(log_reste))


def borne_terminale(alpha: float, n0: int, B: float, rho: float) -> float:
    """L3 (b) : P(E⁺_{n₀} ≥ 1/α) = P(N(B, n₀) ≥ s*)."""
    return float(stats.norm.sf((frontiere(n0, rho, alpha, "unilateral") - B) / math.sqrt(n0)))


def rejet_somme_sous_variance(alpha: float, rapport_variance: float) -> float:
    """Taux de rejet du test z unilatéral calibré sous une variance v₀ quand la vraie est v₁ :
    Φ̄(z_α / √(v₁/v₀)) (classe K : copule AR(1), équicorrélation)."""
    return float(stats.norm.sf(stats.norm.isf(alpha) / math.sqrt(rapport_variance)))
