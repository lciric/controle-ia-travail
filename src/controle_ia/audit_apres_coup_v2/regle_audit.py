"""La règle d'audit en trois parts (rang 3 ; section 1, « Règle d'audit »).

π_i = min(1, π_min + β·s_i/s̄ + γ·g(score_i)) ; un uniforme U_i est tiré après la fin de l'épisode ; l'épisode est
audité si U_i < π_i ; source « plancher » si U_i < π_min, « enjeu » si U_i < π_min + β·s_i/s̄, sinon « soupçon ».

Refus : π_min ≤ 0 hors de la configuration de comparaison `sans_plancher` (π_min = 0 et β = 0, γ > 0), dans laquelle
tout appel à la borne ou à la table rend le refus nommé « pas de borne » ; g non croissante ou hors de [0, 1] ;
paramètre manquant (aucune valeur par défaut pour β, γ, g, s̄).

Le plancher est une base, jamais une revendication : cette pièce ne rend aucune phrase de garantie.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable

import numpy as np
from scipy import special, stats

from ..gardes import GardeArret

CONFIG_STANDARD = "standard"
CONFIG_SANS_PLANCHER = "sans_plancher"
REFUS_PAS_DE_BORNE = "pas de borne"
ETIQUETTE_SANS_PLANCHER = "sans plancher : aucune borne"


def verifier_g(g: Callable[[np.ndarray], np.ndarray], nom: str = "g") -> None:
    x = np.linspace(0.0, 1.0, 1001)
    y = np.asarray(g(x), dtype=float)
    if y.shape != x.shape or np.any(~np.isfinite(y)):
        raise GardeArret(f"{nom} : doit rendre un réel fini par point de [0, 1]")
    if np.any(y < 0) or np.any(y > 1):
        raise GardeArret(f"{nom} : doit aller de [0, 1] dans [0, 1]")
    if np.any(np.diff(y) < -1e-15):
        raise GardeArret(f"{nom} : doit être croissante")


def g_identite(x):
    return np.clip(np.asarray(x, dtype=float), 0.0, 1.0)


def g_nulle(x):
    return np.zeros_like(np.asarray(x, dtype=float))


@dataclass(frozen=True)
class RegleAudit:
    pi_min: float
    beta: float
    gamma: float
    g: Callable[[np.ndarray], np.ndarray]
    s_bar: float
    configuration: str = field(default=CONFIG_STANDARD)

    def __post_init__(self):
        for nom in ("pi_min", "beta", "gamma", "s_bar"):
            v = getattr(self, nom)
            if v is None or not np.isfinite(v):
                raise GardeArret(f"règle d'audit : {nom} absent ou non fini (aucune valeur par défaut)")
        if self.beta < 0 or self.gamma < 0:
            raise GardeArret("règle d'audit : β et γ doivent être positifs ou nuls")
        if self.s_bar <= 0:
            raise GardeArret("règle d'audit : s̄ doit être strictement positif")
        if self.configuration == CONFIG_STANDARD:
            if not (self.pi_min > 0):
                raise GardeArret("règle d'audit : π_min = 0 refusé hors de la configuration `sans_plancher`")
        elif self.configuration == CONFIG_SANS_PLANCHER:
            if self.pi_min != 0 or self.beta != 0 or not (self.gamma > 0):
                raise GardeArret("configuration `sans_plancher` : π_min = 0, β = 0 et γ > 0 exigés")
        else:
            raise GardeArret(f"règle d'audit : configuration inconnue {self.configuration!r}")
        if self.pi_min > 1:
            raise GardeArret("règle d'audit : π_min > 1")
        if self.g is None:
            raise GardeArret("règle d'audit : g absente")
        verifier_g(self.g)

    @property
    def sans_plancher(self) -> bool:
        return self.configuration == CONFIG_SANS_PLANCHER

    def exiger_borne(self) -> None:
        """Toute borne ou table appelée sur `sans_plancher` rend le refus nommé « pas de borne »."""
        if self.sans_plancher:
            raise GardeArret(REFUS_PAS_DE_BORNE)

    def parts(self, enjeu: np.ndarray, score: np.ndarray, g_force: np.ndarray | None = None) -> dict[str, np.ndarray]:
        """Les trois parts, π_i et l'écrêtage. `g_force` (booléen par épisode) force g(score) = 0, consigné."""
        s = np.asarray(enjeu, dtype=float)
        x = np.asarray(score, dtype=float)
        if s.shape != x.shape:
            raise GardeArret("règle d'audit : enjeu et score de formes différentes")
        if np.any(~np.isfinite(s)) or np.any(~np.isfinite(x)):
            raise GardeArret("règle d'audit : enjeu ou score absent")
        gx = np.asarray(self.g(x), dtype=float)
        if g_force is not None:
            gx = np.where(np.asarray(g_force, dtype=bool), 0.0, gx)
        p_pl = np.full_like(s, self.pi_min)
        p_en = self.beta * s / self.s_bar
        p_so = self.gamma * gx
        brut = p_pl + p_en + p_so
        pi = np.minimum(1.0, brut)
        return {"part_plancher": p_pl, "part_enjeu": p_en, "part_soupcon": p_so, "pi": pi, "ecrete": brut > 1.0}

    def tirer(self, parts: dict[str, np.ndarray], u: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        """(audité, source) à partir de l'uniforme U_i tiré après la fin de l'épisode."""
        u = np.asarray(u, dtype=float)
        audite = u < parts["pi"]
        source = np.zeros(u.shape, dtype=np.int8)
        s1 = u < parts["part_plancher"]
        s2 = (~s1) & (u < parts["part_plancher"] + parts["part_enjeu"])
        source[audite] = 3
        source[audite & s2] = 2
        source[audite & s1] = 1
        return audite, source


def esperance_g_gaussienne_tronquee(g, mu: float, sigma: float, points: int = 20001) -> float:
    """E[g(X)], X gaussienne de moyenne mu et d'écart type sigma tronquée à [0, 1] (intégration de Simpson)."""
    a, b = (0.0 - mu) / sigma, (1.0 - mu) / sigma
    z = special.ndtr(b) - special.ndtr(a)
    if z <= 0:
        raise GardeArret("loi du score dégénérée sur [0, 1]")
    x = np.linspace(0.0, 1.0, points)
    dens = stats.norm.pdf((x - mu) / sigma) / (sigma * z)
    y = np.asarray(g(x), dtype=float) * dens
    h = x[1] - x[0]
    coef = np.ones(points)
    coef[1:-1:2] = 4
    coef[2:-1:2] = 2
    return float(np.sum(coef * y) * h / 3.0)


def calibrer_gamma(budget: float, pi_min: float, beta: float, g, mu0: float, sigma: float) -> float:
    """γ fixé par π_min + β + γ·E[g(score)] = b, l'espérance prise sur la loi du score des épisodes sains
    (moyenne μ₀, écart type σ, tronquée à [0, 1]). L'écrêtage à 1 n'est pas compté ici : le budget réalisé est
    rapporté à part (`estimateurs.budget_realise`)."""
    eg = esperance_g_gaussienne_tronquee(g, mu0, sigma)
    reste = budget - pi_min - beta
    if reste < 0:
        raise GardeArret("budget inférieur à π_min + β : γ négatif refusé")
    if reste == 0:
        return 0.0
    if eg <= 0:
        raise GardeArret("E[g(score)] nulle sur les sains : γ indéfini")
    return reste / eg
