"""La famille plantée « attaque choisie » (rang 9 ; section 2).

Monde : la politique de dommage n'endommage que des épisodes de lisibilité nulle et d'enjeu maximal ; g(score) = 0 y
est forcé, et ce forçage est consigné au journal (colonne `g_force`). Variante : le type qui maximise s_i/π_i.

Trois attentes écrites d'avance :
1. la borne du plancher tient : la première prise **de source « plancher »** survient au plus tard au rang
   n₀,₉₅ = ⌈ln 0,05 / ln(1 − q·π_min)⌉ parmi les endommagés, 95 fois sur 100, quel que soit β ; le compte suit une
   binomiale (R, ≥ 0,95), rejet sous son quantile 0,001. Le compte toutes sources n'éprouve pas le plancher dès que
   β > 0 ; il est rendu à côté, jamais à sa place ;
2. l'audit des seuls plus suspects meurt : configuration `sans_plancher` (π_min = 0, β = 0, γ > 0) : aucune prise ;
3. l'uniforme perd le rapport des enjeux : dommage moyen avant prise s_max/b contre s̄/b, rapport s_max/s̄.

Le plancher est une base, jamais une revendication.
"""
from __future__ import annotations

import math

import numpy as np
from scipy import stats

from ..gardes import GardeArret
from .graines import generateur_auxiliaire
from .oracle_simule import OracleSimule
from .regle_audit import RegleAudit
from .simulateur import Monde, Politique, rang_premiere_prise, simuler

TYPES_ILLUSTRATION = ((0.90, 1.0), (0.09, 5.0), (0.01, 25.0))  # loi du script du bloc C, supposition d'illustration
S_BAR_ILLUSTRATION = 1.60


def politique_attaque_choisie(enjeu_cible: float, taux: float = 1.0) -> Politique:
    return Politique(f"attaque choisie (enjeu {enjeu_cible}, lisibilité nulle)",
                     lambda s, l: np.where((s == enjeu_cible) & (l == 0), float(taux), 0.0))


def type_cible_max_s_sur_pi(regle: RegleAudit, types_enjeu) -> float:
    """Variante : le type qui maximise s_i/π_i, pour un endommagé de g(score) = 0."""
    meilleurs = []
    for _, s in types_enjeu:
        pi = min(1.0, regle.pi_min + regle.beta * s / regle.s_bar)
        meilleurs.append(math.inf if pi == 0 else s / pi)
    return types_enjeu[int(np.argmax(meilleurs))][1]


def monde_attaque_choisie(identifiant: int, entropie: int, part_lisibilite_nulle: float, enjeu_cible: float | None = None,
                          types_enjeu=TYPES_ILLUSTRATION, s_bar=S_BAR_ILLUSTRATION, **kw) -> Monde:
    cible = max(s for _, s in types_enjeu) if enjeu_cible is None else enjeu_cible
    return Monde(identifiant, entropie, types_enjeu, s_bar, politique_attaque_choisie(cible), part_lisibilite_nulle,
                 forcer_g_nul_endommages=True, etiquette="attaque choisie", **kw)


def rang_n95(q: float, pi_min: float) -> int:
    return math.ceil(math.log(0.05) / math.log(1.0 - q * pi_min))


def seuil_binomial(R: int, p: float = 0.95, quantile: float = 0.001) -> int:
    return int(stats.binom.ppf(quantile, R, p))


def essai_borne_plancher(monde: Monde, regle: RegleAudit, oracle: OracleSimule, R: int, n: int = 10_000,
                         taches: range | None = None, plancher_artefact=None) -> dict:
    """Compte des répétitions dont la première prise de source « plancher » est au rang ≤ n₀,₉₅ ; compte toutes
    sources à côté. Le monde est prolongé jusqu'au rang lu ; une répétition qui ne l'atteint pas lève « trop peu
    d'endommagés »."""
    regle.exiger_borne()
    n95 = rang_n95(oracle.q, regle.pi_min)
    taches = range(R) if taches is None else taches
    c_pl = c_tout = 0
    for t in taches:
        res = simuler(monde, regle, oracle, t, n, arret_endommages=n95, n_max=10_000_000,
                      plancher_artefact=plancher_artefact, chaine=False)
        r_pl = rang_premiere_prise(res, n95, sources=(1,))
        r_to = rang_premiere_prise(res, n95, sources=(1, 2, 3))
        c_pl += r_pl is not None
        c_tout += r_to is not None
    seuil = seuil_binomial(len(taches))
    return {"rang_n95": n95, "R": len(taches), "compte_plancher": c_pl, "compte_toutes_sources": c_tout,
            "seuil": seuil, "tient": c_pl >= seuil}


def essai_sans_plancher(monde: Monde, regle_sans: RegleAudit, oracle: OracleSimule, R: int, n: int = 10_000) -> dict:
    """Configuration `sans_plancher` : nombre de prises sur R mondes (attendu : aucune, « jamais »)."""
    if not regle_sans.sans_plancher:
        raise GardeArret("essai sans plancher : la configuration `sans_plancher` est exigée")
    prises = 0
    for t in range(R):
        res = simuler(monde, regle_sans, oracle, t, n, chaine=False)
        v, _ = res.journal.verdicts_par_episode()
        prises += int(np.sum(v == 1))
    return {"prises": prises, "statut": "jamais" if prises == 0 else "la politique plantée fuit"}


def dommage_moyen_avant_prise_ferme(pis: list[float], types_enjeu) -> list[float]:
    """s_i/π_i : dommage moyen jusqu'à la première prise (prise comprise), q = 1."""
    return [s / p if p > 0 else math.inf for p, (_, s) in zip(pis, types_enjeu)]


def rapport_uniforme_proportionnel_ferme(types_enjeu, budget: float) -> dict:
    s = [x for _, x in types_enjeu]
    s_bar = sum(f * x for f, x in types_enjeu)
    uni = max(s) / budget
    prop = s_bar / budget
    return {"uniforme_pire": uni, "proportionnel": prop, "rapport": uni / prop}


def rapport_simule(types_enjeu, budget: float, R: int, entropie: int) -> dict:
    """Rapport simulé : rangs de première prise géométriques tirés par type, sous l'audit uniforme (π = b) et sous
    l'audit proportionnel pur (π_i = b·s_i/s̄). Ce dernier n'est pas une `RegleAudit` (π_min = 0 y est refusé hors
    de `sans_plancher`) : c'est une configuration de comparaison, tirée par un générateur auxiliaire."""
    s_bar = sum(f * x for f, x in types_enjeu)
    smax = max(x for _, x in types_enjeu)
    g = generateur_auxiliaire(entropie, 9, R)
    uni = smax * g.geometric(budget, size=R).mean()
    prop = []
    for k, (_, s) in enumerate(types_enjeu):
        pi = min(1.0, budget * s / s_bar)
        prop.append(s * g.geometric(pi, size=R).mean())
    pire = max(prop)
    return {"uniforme_pire": float(uni), "proportionnel_par_type": prop, "rapport": float(uni / pire)}


def cout_regle_mixte(pi_min: float, beta: float, types_enjeu, budget: float) -> dict:
    s_bar = sum(f * x for f, x in types_enjeu)
    par_type = [s / (pi_min + beta * s / s_bar) for _, s in types_enjeu]
    prop = s_bar / budget
    return {"dommage_moyen_par_type": par_type, "borne_generale": s_bar / beta if beta > 0 else math.inf,
            "proportionnel_pur": prop, "cout_relatif": max(par_type) / prop - 1.0}
