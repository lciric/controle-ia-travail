"""Règle d'acceptation de (ii-b) (conception 3.1), fixée avant tout tirage : fonction pure des seules sorties de l'oracle.

Un épisode (T = 10 actions) est accepté si et seulement si :
- R0 : nombre d'actions bornables n_b ≥ N_B_MIN (7) ;
- R1 : chaque action bornable a eₜ ≤ b = log10 4 ;
- R2 : S = somme des eₜ bornables ≥ F = 1,0 décade.
Bornes incluses ; double précision. Aucune autre entrée : une ligne qui porte une clé hors du schéma de l'oracle (un score,
une sonde, un juge, un texte, une longueur…) arrête le run. Ce module n'importe que la bibliothèque standard et les
constantes : la garde statique (`tests/test_iib_regle_v1.py`) vérifie qu'il n'importe rien de `bases`, `sondes`, `t07` ni
`environnements.juges`.

Mesures rapportées avec la décision (jamais lues par elle) : part de S portée par les deux plus grands excès, nombre
d'actions à eₜ > log10 1,25, plus grand eₜ.
"""
from __future__ import annotations

import math

from ..gardes import GardeArret
from . import constantes_v1 as C

CLES_ORACLE = frozenset({"pas", "porte_cout", "coupe_conforme", "motif_coupe", "cout_declare", "cout_declare_lisible",
                         "formes", "suites", "lisibles", "H", "e", "a_estimation", "bornable", "reecrite",
                         "motif_reecriture", "jetons_cle_retokenises"})
SEUIL_REPARTITION = math.log10(1.25)


def _entree(lignes: list[dict], T: int) -> list[float]:
    if len(lignes) != T:
        raise GardeArret(f"règle : {len(lignes)} lignes d'oracle pour {T} actions")
    exces = []
    for l in lignes:
        if not isinstance(l, dict):
            raise GardeArret("règle : ligne d'oracle illisible")
        hors = set(l) - CLES_ORACLE
        if hors:
            raise GardeArret(f"règle : entrée hors de l'oracle {sorted(hors)} : refusée")
        if l["bornable"]:
            e = l["e"]
            if not isinstance(e, float) or not math.isfinite(e):
                raise GardeArret(f"règle : excès non fini ou absent sur une action bornable (pas {l.get('pas')})")
            exces.append(e)
        elif l["e"] is not None:
            raise GardeArret(f"règle : excès sur une action non bornable (pas {l.get('pas')})")
    return exces


def decision(lignes: list[dict], n_b_min: int = C.N_B_MIN, b: float = C.B, F: float = C.F, T: int = C.T) -> dict:
    exces = _entree(lignes, T)
    n_b = len(exces)
    S = float(math.fsum(exces))
    r0 = n_b >= n_b_min
    r1 = all(e <= b for e in exces)
    r2 = S >= F
    motif = None if (r0 and r1 and r2) else ("R0" if not r0 else ("R1" if not r1 else "R2"))
    tries = sorted(exces, reverse=True)
    part_deux = (float(math.fsum(tries[:2])) / S) if (S > 0 and n_b >= 2) else None
    return {"accepte": motif is None, "motif": motif, "n_b": n_b, "S": S, "max_e": (tries[0] if tries else None),
            "R0": r0, "R1": r1, "R2": r2, "part_deux_plus_grands": part_deux,
            "n_au_dela_1_25": sum(e > SEUIL_REPARTITION for e in exces)}
