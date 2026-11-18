"""Niveaux des lectures : répartition du risque entre deux lectures, et deux références de comparaison.

- `repartir` : partage par borne d'union (valide quelle que soit la dépendance entre les lectures, quelle que
  soit la fraction de tâches atteinte à l'intermédiaire, pourvu que cette fraction ne dépende d'aucun score).
- `bornes_depense` : frontière à dépense de risque de type O'Brien-Fleming (Lan et DeMets), référence.
- `frontiere_melange` : frontière d'un processus e à mélange normal (test toujours valide), référence.
"""
from __future__ import annotations

import math

from scipy.optimize import brentq
from scipy.stats import multivariate_normal, norm

from ..gardes import GardeArret

# Percentiles du brouillon 3 du préenregistrement (« Seuil ») : par dose et par côté.
Q_DECISIF = 0.003125      # 0,025 / 4 doses, queue nominale divisée par deux
Q_EQUIVALENCE = 0.0125    # 0,025 unilatéral, queue nominale divisée par deux
QUEUE_MINIMALE = 25       # tirages attendus au-delà du percentile lu (résolution de l'intervalle percentile)


def _exiger_niveau(q: float) -> None:
    if not (isinstance(q, float) and 0.0 < q < 0.5):
        raise GardeArret(f"niveau {q!r} : un réel dans ]0 ; 0,5[ est attendu")


def repartir(q: float, part_intermediaire: float) -> tuple[float, float]:
    """Partage q entre la lecture intermédiaire et la lecture finale ; la somme vaut q exactement (borne d'union)."""
    _exiger_niveau(q)
    if not (isinstance(part_intermediaire, float) and 0.0 < part_intermediaire < 1.0):
        raise GardeArret(f"part de l'intermédiaire {part_intermediaire!r} : un réel dans ]0 ; 1[ est attendu")
    q_i = q * part_intermediaire
    return q_i, q - q_i


def tirages_minimaux(q: float, queue: int = QUEUE_MINIMALE) -> int:
    """Nombre de tirages de rééchantillonnage pour qu'au moins `queue` tirages soient attendus au-delà du percentile q."""
    _exiger_niveau(q)
    return int(math.ceil(queue / q))


def z_de(q: float) -> float:
    _exiger_niveau(q)
    return float(norm.isf(q))


def bornes_depense(q: float, fraction: float) -> tuple[float, float]:
    """Frontière à deux lectures, dépense de type O'Brien-Fleming : (z intermédiaire, z final), niveau unilatéral q.

    Suppose des accroissements indépendants et normaux (corrélation des deux statistiques : racine de la fraction).
    """
    _exiger_niveau(q)
    if not (0.0 < fraction < 1.0):
        raise GardeArret(f"fraction d'information {fraction!r} : un réel dans ]0 ; 1[ est attendu")
    depense = 2.0 * float(norm.sf(norm.isf(q / 2.0) / math.sqrt(fraction)))
    if not (0.0 < depense < q):
        raise GardeArret("dépense intermédiaire hors de ]0 ; q[ : frontière non calculable")
    z1 = float(norm.isf(depense))
    loi = multivariate_normal(mean=[0.0, 0.0], cov=[[1.0, -math.sqrt(fraction)], [-math.sqrt(fraction), 1.0]])

    def exces(z2: float) -> float:
        # P(Z1 < z1, Z2 >= z2) = P(Z1 < z1, -Z2 <= -z2)
        return float(loi.cdf([z1, -z2])) - (q - depense)

    z2 = float(brentq(exces, 0.0, 10.0, xtol=1e-10))
    return z1, z2


def risque_deux_lectures(z1: float, z2: float, fraction: float) -> float:
    """Probabilité, sous le nul à la frontière, de franchir z1 à l'intermédiaire ou z2 à la finale (accroissements normaux)."""
    r = math.sqrt(fraction)
    loi = multivariate_normal(mean=[0.0, 0.0], cov=[[1.0, r], [r, 1.0]])
    return 1.0 - float(loi.cdf([z1, z2]))


def frontiere_melange(n: float, q: float, rho: float) -> float:
    """Frontière, en écarts types, d'un processus e à mélange normal lu après n unités d'information.

    Processus bilatéral M_n = (1 + n rho)^(-1/2) exp(rho S_n² / (2 (1 + n rho))), seuil 1 / (2 q) : par symétrie,
    le franchissement du côté positif a une probabilité d'au plus q sous le nul, à tout instant d'arrêt.
    """
    _exiger_niveau(q)
    if not (n > 0 and rho > 0):
        raise GardeArret("n et rho strictement positifs attendus")
    return math.sqrt((1.0 + n * rho) / (n * rho) * (2.0 * math.log(1.0 / (2.0 * q)) + math.log(1.0 + n * rho)))
