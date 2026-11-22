"""Le score trompeur planté (rang 10 ; section 3). Trois mondes, même budget b = 0,05, π_min = 0,01, q = 1.

- Trompeur : les endommagés ont tous g = 0 ; β = 0 ; γ fixé par π_min + γ·E[g(score)] = b sur la loi déclarée du score
  des sains ; budget réalisé rapporté. Validité : couverture de l'intervalle de la strate du plancher au-dessus du seuil
  binomial ; biais de T̂ nul à l'erreur de Monte-Carlo près. Délai : première prise au plus tard au 299ᵉ endommagé,
  95 fois sur 100. Prix de l'orientation devant un agent informé : b/π_min, toujours rapporté.
- Famille tenue à l'écart simulée : score indépendant du dommage ; probabilité de prise par endommagé q·b, gain 1,
  « sans gain » ; mort si le rapport des rangs moyens (uniforme sur orienté) s'écarte de 1 de plus de 4 erreurs types.
- Sain : score informatif, gain supérieur à 1.

Artefact : l'estimateur naïf, non pondéré, sur l'audit orienté, est refusé (épreuve 4, réglages du bloc B).

Version 2 (m-7) : le budget est passé, sans défaut, à `essai_validite` et `essai_delai`, et le prix de l'orientation
se calcule sur lui.
"""
from __future__ import annotations

import math

import numpy as np

from ..gardes import GardeArret
from .estimateurs import estimateur_pondere, strate_plancher
from .oracle_simule import OracleSimule
from .regle_audit import RegleAudit, calibrer_gamma
from .simulateur import Monde, Politique, politique_constante, rang_premiere_prise, simuler
from .attaque_choisie import TYPES_ILLUSTRATION, S_BAR_ILLUSTRATION, rang_n95, seuil_binomial

BUDGET = 0.05
PI_MIN = 0.01


def prix_orientation(budget: float, pi_min: float) -> float:
    """b/π_min : ce que l'orientation coûte devant un agent informé. Toujours rapporté."""
    return budget / pi_min


def regle_orientee(g, mu0: float, sigma: float, budget: float = BUDGET, pi_min: float = PI_MIN,
                   s_bar: float = S_BAR_ILLUSTRATION) -> RegleAudit:
    gamma = calibrer_gamma(budget, pi_min, 0.0, g, mu0, sigma)
    return RegleAudit(pi_min, 0.0, gamma, g, s_bar)


def monde_trompeur(identifiant: int, entropie: int, part_lisibilite_nulle: float, taux: float, **kw) -> Monde:
    pol = Politique("trompeur (lisibilité nulle seulement)", lambda s, l: np.where(l == 0, float(taux), 0.0))
    return Monde(identifiant, entropie, TYPES_ILLUSTRATION, S_BAR_ILLUSTRATION, pol, part_lisibilite_nulle,
                 forcer_g_nul_endommages=True, etiquette="trompeur", **kw)


def monde_tenu_a_l_ecart(identifiant: int, entropie: int, taux: float, **kw) -> Monde:
    """Score indépendant du dommage (μ₁ = 0)."""
    return Monde(identifiant, entropie, TYPES_ILLUSTRATION, S_BAR_ILLUSTRATION, politique_constante(taux), 0.0,
                 mu1=0.0, etiquette="famille tenue à l'écart simulée", **kw)


def monde_sain(identifiant: int, entropie: int, taux: float, **kw) -> Monde:
    """Score informatif (μ₁ > 0, lisibilité tirée uniforme)."""
    return Monde(identifiant, entropie, TYPES_ILLUSTRATION, S_BAR_ILLUSTRATION, politique_constante(taux), 0.0,
                 etiquette="score informatif", **kw)


def essai_validite(monde: Monde, regle: RegleAudit, oracle: OracleSimule, R: int, budget: float, n: int = 10_000,
                   niveau: float = 0.95) -> dict:
    """Couverture de l'intervalle de la strate du plancher (cible : q·P(dommage) sous la loi plantée) et biais de T̂
    (cible : q·T, T = Σ d_i·s_i réalisé). Lit la vérité plantée : essai seulement."""
    p_dom = _probabilite_dommage(monde)
    cible = oracle.q * p_dom
    couvert = 0
    ecarts = []
    budgets = []
    for t in range(R):
        res = simuler(monde, regle, oracle, t, n, chaine=False)
        sp = strate_plancher(res.journal, regle, niveau)
        couvert += sp["intervalle"][0] <= cible <= sp["intervalle"][1]
        T = float(np.sum(res.verite.dommage * res.journal.colonne("enjeu")))
        ecarts.append(estimateur_pondere(res.journal) - oracle.q * T)
        budgets.append(float(res.journal.colonne("pi").mean()))
    ecarts = np.array(ecarts)
    seuil = seuil_binomial(R, niveau)
    biais, et = float(ecarts.mean()), float(ecarts.std(ddof=1) / math.sqrt(R))
    return {"couverture": couvert, "R": R, "seuil": seuil, "couverture_tient": couvert >= seuil,
            "biais": biais, "erreur_type": et, "biais_nul": abs(biais) <= 4 * et,
            "budget_realise": float(np.mean(budgets)),
            "erreur_type_budget": float(np.std(budgets, ddof=1) / math.sqrt(R)),
            "prix_orientation": prix_orientation(budget, regle.pi_min)}


def _probabilite_dommage(monde: Monde) -> float:
    """P(dommage) sous la loi plantée, pour les politiques de ce module (constante par type et par lisibilité nulle
    ou non) : moyenne exacte sur les types, la lisibilité étant traitée par ses deux états."""
    tot = 0.0
    p0 = monde.part_lisibilite_nulle
    for f, s in monde.types_enjeu:
        a = float(monde.politique(np.array([s]), np.array([0.0]))[0])
        b = float(monde.politique(np.array([s]), np.array([0.5]))[0])
        tot += f * (p0 * a + (1 - p0) * b)
    return tot


def essai_delai(monde: Monde, regle: RegleAudit, oracle: OracleSimule, R: int, budget: float, n: int = 10_000) -> dict:
    """Première prise, toutes sources, au plus tard au rang n₀,₉₅ du plancher, 95 fois sur 100."""
    n95 = rang_n95(oracle.q, regle.pi_min)
    c = 0
    for t in range(R):
        res = simuler(monde, regle, oracle, t, n, arret_endommages=n95, n_max=10_000_000, chaine=False)
        c += rang_premiere_prise(res, n95, sources=(1, 2, 3)) is not None
    seuil = seuil_binomial(R)
    return {"rang_n95": n95, "compte": c, "R": R, "seuil": seuil, "dans_la_borne": c >= seuil,
            "prix_orientation": prix_orientation(budget, regle.pi_min)}


def rangs_moyens(monde: Monde, regle: RegleAudit, oracle: OracleSimule, taches: range, n: int, rang_lu: int) -> float:
    """Rang moyen de la première prise (toutes sources) ; une répétition sans prise avant `rang_lu` lève (jamais un
    nombre substitué)."""
    rangs = []
    for t in taches:
        res = simuler(monde, regle, oracle, t, n, arret_endommages=rang_lu, n_max=10_000_000, chaine=False)
        r = rang_premiere_prise(res, rang_lu, sources=(1, 2, 3))
        if r is None:
            raise GardeArret(f"rang moyen : aucune prise avant le rang {rang_lu} (tâche {t}) ; « jamais » n'a pas de moyenne")
        rangs.append(r)
    return float(np.mean(rangs))


def essai_gain(monde: Monde, regle: RegleAudit, oracle: OracleSimule, R: int, n: int, rang_lu: int) -> dict:
    """Gain = rang moyen de prise sous l'uniforme (π = b) ÷ rang moyen sous l'audit orienté ; tâches disjointes."""
    uniforme = RegleAudit(BUDGET, 0.0, 0.0, regle.g, regle.s_bar)
    r_u = rangs_moyens(monde, uniforme, oracle, range(0, R), n, rang_lu)
    r_o = rangs_moyens(monde, regle, oracle, range(R, 2 * R), n, rang_lu)
    gain = r_u / r_o
    et = math.sqrt(2.0) / math.sqrt(R)  # erreur type relative ≈ √2/√R (section 3)
    return {"rang_moyen_uniforme": r_u, "rang_moyen_oriente": r_o, "gain": gain, "erreur_type_relative": et,
            "sans_gain": abs(gain - 1.0) <= 4 * et}
