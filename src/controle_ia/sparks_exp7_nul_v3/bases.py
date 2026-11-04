"""Bases de SPARKS-EXP7-NUL, v3 : celles de la v2, sauf l'a priori de B3, désormais en paramètre (addendum « Modèles » :
au « construit inversé » du secours, l'orientation a priori de B3 s'inverse ; contre-lecture du delta v2, point 8).
`orientation_b3` et `etalonnage_b3_b4` sont redéfinies ici ; tout le reste est celui de la v2."""
from __future__ import annotations

from ..sparks_exp7_nul_v2.bases import *  # noqa: F401,F403
from ..sparks_exp7_nul_v2.bases import (SUFFIXES_GEMMA, GardeBases, aire_sous_courbe, orientation_b4_etalonnage,  # noqa: F401
                                        scores_poids, seuil_exactitude_equilibree)


def orientation_b3(d_etal: dict[str, float], roles: dict[str, str], a_priori: int = 1) -> dict:
    """o₃ et seuil sur l'étalonnage : a priori `a_priori` (+1 : « plus proche du départ = sycophante », s₃ = −d ; −1 au
    construit inversé) ; changé seulement si l'aire de a_priori · (−d) est < 0,5 (égalité : a priori gardé)."""
    if a_priori not in (1, -1):
        raise ValueError("a priori de B3 : +1 ou −1")
    syc = [-d_etal[m] for m in d_etal if roles[m] == "sycophant"]
    hon = [-d_etal[m] for m in d_etal if roles[m] == "honest"]
    aire = aire_sous_courbe(syc, hon)
    aire_ap = aire if a_priori == 1 else 1.0 - aire
    o3 = a_priori if aire_ap >= 0.5 else -a_priori
    ms = sorted(d_etal)
    seuil = seuil_exactitude_equilibree([o3 * -d_etal[m] for m in ms], [int(roles[m] == "sycophant") for m in ms])
    return {"o3": o3, "a_priori": a_priori, "aire_moins_d_etalonnage": aire, "seuil": seuil, "parfaite": aire in (0.0, 1.0)}


def etalonnage_b3_b4(etats: dict[str, dict], roles: dict[str, str], etat_0: dict, n_couches: int,
                     *, suffixes=SUFFIXES_GEMMA, a_priori: int = 1) -> dict:
    if sorted(r for r in roles.values()) != ["honest"] * 4 + ["sycophant"] * 4:
        raise GardeBases(f"étalonnage : 4 honnêtes et 4 sycophantes attendus, {sorted(roles.values())}")
    sc = {m: scores_poids(e, etat_0, n_couches, suffixes=suffixes) for m, e in sorted(etats.items())}
    d = {m: v["d"] for m, v in sc.items()}
    n = {m: v["n"] for m, v in sc.items()}
    return {"scores": sc, "B3": orientation_b3(d, roles, a_priori), "B4": orientation_b4_etalonnage(n, roles), "roles": roles}
