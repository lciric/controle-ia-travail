"""Critères d'admission du plan séquentiel, écrits avant que la simulation soit jouée, appliqués par programme.

Trois genres de critère, portés par chaque monde de la configuration scellée (clé « critere ») :
  « risque »    : la part des répliques où un état interdit est prononcé (à l'intermédiaire OU à la finale) a une
                  borne haute exacte (Clopper-Pearson, 95 %, unilatérale) au plus égale au plafond, pour le plan jugé ;
  « temoin »    : le plan « naif » (deux lectures sans correction) doit dépasser le plan jugé — sinon la simulation
                  ne sait pas voir un plan qui gonfle le risque, et aucun critère de risque ne vaut ;
  « puissance » : la part des répliques où l'état visé est prononcé ; perte du plan jugé contre le plan « unique »
                  au plus égale à la perte permise.
"""
from __future__ import annotations

from scipy.stats import beta

from ..gardes import GardeArret

GENRES = ("risque", "temoin", "puissance")
PLAN_JUGE = "reparti"


def borne_haute(evenements: int, repliques: int, confiance: float = 0.95) -> float:
    if not (0 <= evenements <= repliques and repliques > 0):
        raise GardeArret(f"compte {evenements} sur {repliques} : incohérent")
    return 1.0 if evenements == repliques else float(beta.ppf(confiance, evenements + 1, repliques - evenements))


def borne_basse(evenements: int, repliques: int, confiance: float = 0.95) -> float:
    if not (0 <= evenements <= repliques and repliques > 0):
        raise GardeArret(f"compte {evenements} sur {repliques} : incohérent")
    return 0.0 if evenements == 0 else float(beta.ppf(1.0 - confiance, evenements, repliques - evenements + 1))


def prononces(couples: dict, etats_vises: list[str]) -> int:
    """Répliques où l'un des états visés est prononcé à l'intermédiaire ou à la finale (clés « e1>e2 »)."""
    total = 0
    for cle, nombre in couples.items():
        e1, e2 = cle.split(">")
        if e1 in etats_vises or e2 in etats_vises:
            total += nombre
    return total


def juger(critere: dict, comptes: dict, repliques: int) -> dict:
    """Applique un critère aux comptes d'un monde ; rend les comptes, les bornes et « tenu » (booléen)."""
    genre = critere.get("genre")
    if genre not in GENRES:
        raise GardeArret(f"genre de critère {genre!r} inconnu")
    for plan in (PLAN_JUGE, "unique", "naif"):
        if plan not in comptes or sum(comptes[plan]["couple"].values()) != repliques:
            raise GardeArret(f"comptes du plan {plan!r} absents ou incomplets")
    k = {plan: prononces(comptes[plan]["couple"], critere["etats"]) for plan in (PLAN_JUGE, "unique", "naif")}
    sortie = {"genre": genre, "etats": critere["etats"], "prononces": k, "repliques": repliques}
    if genre == "risque":
        sortie["borne_haute"] = borne_haute(k[PLAN_JUGE], repliques)
        sortie["tenu"] = sortie["borne_haute"] <= critere["plafond"]
    elif genre == "temoin":
        sortie["borne_basse_naif"] = borne_basse(k["naif"], repliques)
        sortie["borne_haute_juge"] = borne_haute(k[PLAN_JUGE], repliques)
        sortie["tenu"] = sortie["borne_basse_naif"] > sortie["borne_haute_juge"]
    else:
        seul = sum(n for cle, n in comptes[PLAN_JUGE]["couple"].items() if cle.split(">")[0] in critere["etats"])
        sortie["part_juge"], sortie["part_unique"] = k[PLAN_JUGE] / repliques, k["unique"] / repliques
        sortie["part_des_l_intermediaire"] = seul / repliques
        sortie["tenu"] = sortie["part_unique"] - sortie["part_juge"] <= critere["perte_permise"]
    return sortie
