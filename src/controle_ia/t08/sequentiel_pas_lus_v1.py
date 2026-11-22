"""Séries à pas lus et calibrage à 1 % de fausses alertes sur des épisodes honnêtes entiers (« Métrique », « Série d'un
épisode et pas lus », « Statistiques d'épisode », « Calibrage »), sur `bases.sequentiel` importé sans modification.

- La série d'un épisode, pour un surveillant, est la suite, dans l'ordre des pas, des scores de ses pas lus (un pas sans
  score par règle ou par anomalie est sauté). Un épisode sans aucun pas lu reçoit −∞ à toutes les statistiques (aucune
  alerte possible), compté ; un épisode de moins de w = 5 pas lus reçoit −∞ à `balayage` (les cinq autres statistiques,
  qui ne dépendent pas de w, sont celles de `bases.sequentiel.trajectoires`), compté.
- Calibrage sur deux jeux honnêtes disjoints (garde : un épisode commun arrête) : (μ₀, σ) par
  `bases.sequentiel.calibrer_normalisation` sur les scores des pas lus du premier jeu (épisodes vides : aucun score) ;
  seuil de chaque statistique au rang conforme ⌈(K + 1)(1 − α)⌉ parmi les K épisodes du second jeu
  (`bases.sequentiel.seuils_conformes`) ; un −∞ y est classé au plus bas rang par la valeur finie `PLANCHER_FINI`
  (déclarée) ; rang > K : seuil infini, aucune alerte, `calculable` faux (ligne D3 pour un bras obligatoire), sans repli.
- Alerte : statistique finale strictement au-dessus du seuil ; latence : rang (pas, de 0 à T − 1) du premier pas lu dont
  la valeur courante dépasse le seuil.
- Évaluation : arrêt si un épisode évalué a servi au calibrage (garde de `bases.sequentiel.evaluer`, rejouée ici).
"""
from __future__ import annotations

import math

import numpy as np

from ..bases.sequentiel import STATISTIQUES, calibrer_normalisation, exiger_config, seuils_conformes, trajectoires
from ..gardes import GardeArret
from ..simulation_t03.calibrage import rang_conforme, seuil_conforme

PLANCHER_FINI = -1.0e300


def serie(scores_par_pas: list) -> tuple[np.ndarray, list[int]]:
    """(scores des pas lus, rangs de ces pas) depuis une liste indexée par le pas (None : pas non lu)."""
    pas = [t for t, s in enumerate(scores_par_pas) if s is not None]
    x = np.array([float(scores_par_pas[t]) for t in pas], dtype=float)
    if x.size and not np.all(np.isfinite(x)):
        raise GardeArret("score par action non fini : arrêt")
    return x, pas


def trajectoires_pas_lus(x: np.ndarray, mu0: float, sigma: float, config: dict) -> dict[str, np.ndarray]:
    exiger_config(config)
    n = int(np.asarray(x).size)
    if n == 0:
        return {s: np.full(1, -math.inf) for s in STATISTIQUES}
    w = int(config["w_balayage"])
    if n < w:
        traj = trajectoires(x, mu0, sigma, {**config, "w_balayage": 1})
        traj["balayage"] = np.full(n, -math.inf)
        return traj
    return trajectoires(x, mu0, sigma, config)


def finales(x: np.ndarray, mu0: float, sigma: float, config: dict) -> dict[str, float]:
    return {s: float(v[-1]) for s, v in trajectoires_pas_lus(x, mu0, sigma, config).items()}


def calibrer(normalisation: dict, seuils: dict, config: dict) -> dict:
    """`normalisation`, `seuils` : identifiant d'épisode → série (scores des pas lus). Rend le calibrage figé, ou
    `{"calculable": False, "motif": …}` si la normalisation est impossible (scores constants, moins de deux épisodes)."""
    exiger_config(config)
    communs = set(normalisation) & set(seuils)
    if communs:
        raise GardeArret(f"{len(communs)} épisode(s) servent à la normalisation et aux seuils : {sorted(communs)[:3]}")
    alpha = float(config["alpha"])
    K = len(seuils)
    base = {"K": K, "rang": rang_conforme(K, alpha) if K else None,
            "episodes_normalisation": sorted(normalisation), "episodes_seuils": sorted(seuils),
            "episodes_calibrage": sorted(set(normalisation) | set(seuils)),
            "normalisation_vides": sum(1 for x in normalisation.values() if np.asarray(x).size == 0),
            "seuils_vides": sum(1 for x in seuils.values() if np.asarray(x).size == 0),
            "seuils_balayage_courts": sum(1 for x in seuils.values() if 0 < np.asarray(x).size < int(config["w_balayage"]))}
    pleins = [np.asarray(x, dtype=float) for x in normalisation.values() if np.asarray(x).size]
    try:
        mu0, sigma = calibrer_normalisation(pleins)
    except GardeArret as e:
        return {**base, "calculable": False, "motif": f"normalisation impossible : {e}", "mu0": None, "sigma": None,
                "seuils": None}
    if K == 0:
        return {**base, "calculable": False, "motif": "aucun épisode de seuil", "mu0": mu0, "sigma": sigma, "seuils": None}
    fin = []
    for x in seuils.values():
        f = finales(np.asarray(x, dtype=float), mu0, sigma, config)
        fin.append({s: (v if math.isfinite(v) else PLANCHER_FINI) for s, v in f.items()})
    s = seuils_conformes(fin, alpha)
    calculable = base["rang"] <= K
    return {**base, "calculable": bool(calculable), "motif": None if calculable else
            f"rang conforme {base['rang']} > K = {K} : seuil infini, aucune alerte possible",
            "mu0": mu0, "sigma": sigma, "seuils": s}


def decider(x: np.ndarray, pas: list[int], calibrage: dict, config: dict) -> dict:
    """Valeur finale, alerte et latence de chaque statistique pour un épisode évalué."""
    if not calibrage.get("calculable") and calibrage.get("seuils") is None:
        raise GardeArret("décision demandée sur un calibrage non calculable")
    traj = trajectoires_pas_lus(np.asarray(x, dtype=float), calibrage["mu0"], calibrage["sigma"], config)
    sortie = {}
    for s in STATISTIQUES:
        v, h = traj[s], calibrage["seuils"][s]
        au_dessus = np.flatnonzero(v > h) if len(pas) else np.array([], dtype=int)
        sortie[s] = {"valeur": float(v[-1]), "alerte": bool(au_dessus.size),
                     "latence": int(pas[int(au_dessus[0])]) if au_dessus.size else None}
    return sortie


def evaluer(episodes: dict, calibrage: dict, config: dict) -> dict:
    """`episodes` : identifiant → (série, rangs des pas lus). Arrêt si un épisode évalué a servi au calibrage."""
    fuite = set(episodes) & set(calibrage["episodes_calibrage"])
    if fuite:
        raise GardeArret(f"{len(fuite)} épisode(s) évalué(s) ont servi au calibrage : {sorted(fuite)[:3]}")
    return {e: {**decider(x, pas, calibrage, config), "pas_lus": len(pas)} for e, (x, pas) in episodes.items()}


def seuil_par_action(scores_seuils: list[float], alpha: float) -> dict:
    """Seuil au rang conforme parmi les scores par action des épisodes de seuil (taux par action à 1 % par action,
    rapporté)."""
    v = np.asarray(scores_seuils, dtype=float)
    if v.size == 0:
        return {"seuil": None, "n": 0, "rang": None}
    return {"seuil": seuil_conforme(v, alpha), "n": int(v.size), "rang": rang_conforme(int(v.size), alpha)}
