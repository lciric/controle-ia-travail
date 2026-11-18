"""Gardes de la liste d'arrêt du brouillon 4, v1 (chacune éprouvée sur un cas sain et sur un artefact : `tests/test_narcbench_v1.py`).

| garde | liste d'arrêt |
|---|---|
| `exiger_identite_lot` : sous-ensemble repassé dans un lot de même composition et même ordre, égal au bit près | 5 |
| `exiger_texte_identique` : identifiants du texte d'une cellule = identifiants générés, à la position annoncée | 5 |
| `compter_exclusions_positions` : plus de 2 % de messages exclus d'un duel → arrêt | 14 |
| `exiger_invariance_bases` : scores des bases égaux dans toutes les cellules d'un même message | 12 |
| `exiger_passe_arretee_egale` : passe arrêtée après la couche 23 = passe entière, au bit près | 12 |
| `exiger_retokenisation` : plus de 2 % de messages discordants → arrêt | 4 |
| `decider_cellules` : chronométrage, retraits `K-c0` puis `H-c0`, puis arrêt | 13 |
| `exiger_budget` : 16 h de carte depuis la création, 25 USD cumulés | 7 |
"""
from __future__ import annotations

from typing import Callable

import numpy as np

from ..gardes import GardeArret
from .contextes_v1 import HORS_SOCLE_ORDRE_DE_RETRAIT

PLAFOND_HEURES, PLAFOND_USD, PROJECTION_MAX_HEURES = 16.0, 25.0, 8.0
PROPORTION_MAX = 0.02


def exiger_identite_lot(premiere: dict, repassee: dict, quoi: str = "garde d'identité") -> None:
    """Deux passes du même lot (même composition, même ordre) : activations égales au bit près, clé par clé."""
    if set(premiere) != set(repassee):
        raise GardeArret(f"{quoi} : clés différentes")
    fautes = [k for k in premiere if not (np.shape(premiere[k]) == np.shape(repassee[k])
                                          and np.array_equal(np.asarray(premiere[k]), np.asarray(repassee[k])))]
    if fautes:
        raise GardeArret(f"{quoi} : {len(fautes)} entrée(s) différentes au bit près ({fautes[:3]}…) : arrêt, aucune lecture")


def exiger_texte_identique(ids_cellule, debut: int, texte_genere) -> None:
    t = [int(i) for i in texte_genere]
    vu = [int(i) for i in ids_cellule][int(debut):int(debut) + len(t)]
    if vu != t or int(debut) + len(t) != len(ids_cellule):
        raise GardeArret("identifiants du texte d'une cellule ≠ identifiants générés : arrêt, aucune lecture")


def compter_exclusions_positions(exclus: int, total: int, duel: str) -> dict:
    if total <= 0 or exclus < 0 or exclus > total:
        raise GardeArret(f"duel {duel} : comptes invalides ({exclus}/{total})")
    p = exclus / total
    if p > PROPORTION_MAX:
        raise GardeArret(f"duel {duel} : {exclus}/{total} messages exclus par la garde des positions (> 2 %) : arrêt, nœud")
    return {"duel": duel, "exclus": int(exclus), "total": int(total), "proportion": p}


def exiger_retokenisation(discordants: int, total: int) -> dict:
    if total <= 0 or not 0 <= discordants <= total:
        raise GardeArret("retokenisation : comptes invalides")
    if discordants / total > PROPORTION_MAX:
        raise GardeArret(f"retokenisation discordante sur {discordants}/{total} messages (> 2 %) : arrêt, nœud")
    return {"discordants": int(discordants), "total": int(total)}


def exiger_invariance_bases(scores_par_cellule: dict) -> None:
    """`scores_par_cellule` : cellule → (messages,) des scores d'une base, mêmes messages dans le même ordre."""
    cellules = list(scores_par_cellule)
    if len(cellules) < 2:
        raise GardeArret("invariance des bases : au moins deux cellules")
    ref = np.asarray(scores_par_cellule[cellules[0]])
    for c in cellules[1:]:
        if not np.array_equal(ref, np.asarray(scores_par_cellule[c])):
            raise GardeArret(f"invariance des bases rompue entre {cellules[0]} et {c} : arrêt")


def exiger_passe_arretee_egale(entiere: dict, arretee: dict, couches_lues=(7, 15, 23)) -> None:
    for c in couches_lues:
        if c not in entiere or c not in arretee or not np.array_equal(np.asarray(entiere[c]), np.asarray(arretee[c])):
            raise GardeArret(f"passe arrêtée après la couche {max(couches_lues)} ≠ passe entière à la couche {c} : arrêt")


def decider_cellules(cellules: list[str], projection: Callable[[list[str]], float]) -> dict:
    """Règle du chronométrage, avant la génération : projection nominale > 8 h → retrait de `K-c0`, puis de `H-c0` ; toujours
    > 8 h → arrêt, nœud. Rend la liste jouée et le journal (à écrire au manifeste avant la génération)."""
    jouees, journal = list(cellules), []
    h = float(projection(jouees))
    journal.append({"cellules": list(jouees), "projection_h": h})
    for retrait in HORS_SOCLE_ORDRE_DE_RETRAIT:
        if h <= PROJECTION_MAX_HEURES:
            break
        if retrait in jouees:
            jouees.remove(retrait)
            h = float(projection(jouees))
            journal.append({"retrait": retrait, "cellules": list(jouees), "projection_h": h})
    if h > PROJECTION_MAX_HEURES:
        raise GardeArret(f"chronométrage : projection {h:.2f} h > 8 h après les retraits permis : arrêt avant la génération, nœud")
    return {"cellules_jouees": jouees, "journal": journal, "retraits": [j["retrait"] for j in journal if "retrait" in j]}


def exiger_budget(heures_depuis_creation: float, usd_cumules: float) -> None:
    """Liste d'arrêt 7 : la première borne atteinte commande l'arrêt **par l'identifiant de l'instance** (R10, hors de ce module)."""
    if not (np.isfinite(heures_depuis_creation) and np.isfinite(usd_cumules)) or heures_depuis_creation < 0 or usd_cumules < 0:
        raise GardeArret("budget : relevés invalides ; aucun repli")
    if heures_depuis_creation >= PLAFOND_HEURES:
        raise GardeArret(f"{heures_depuis_creation:.2f} h de carte depuis la création ≥ 16 h : arrêt par identifiant (R10)")
    if usd_cumules >= PLAFOND_USD:
        raise GardeArret(f"{usd_cumules:.2f} USD cumulés ≥ 25 USD sur la ligne de GO : arrêt par identifiant (R10)")


__all__ = ["exiger_identite_lot", "exiger_texte_identique", "compter_exclusions_positions", "exiger_retokenisation",
           "exiger_invariance_bases", "exiger_passe_arretee_egale", "decider_cellules", "exiger_budget"]
