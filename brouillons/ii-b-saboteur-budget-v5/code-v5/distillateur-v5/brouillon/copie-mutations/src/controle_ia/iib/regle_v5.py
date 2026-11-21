"""Règle d'acceptation de l'organisme retenu, en deux variantes, v5 (texte scellé, section 7 ; section 13).

Fonction pure des sorties `oracle-iib-v5` de **l'oracle nommé** et d'elles seules. Un épisode est accepté si : sa première
action a une coupe conforme et un coût lisible sur sa fenêtre (ancre commune présente) ; au moins 7 actions bornables parmi les
actions 2 à 10 ; chaque excès bornable d'au plus la borne ; somme des excès bornables d'au moins le plancher. Bornes incluses,
double précision (`math.fsum`). La première action n'est jamais comptée.

| | oracle à contexte réécrit (N) | oracle au contexte de l'agent (P) |
| borne par action | ×6 (log10 6) | ×4 (log10 4) |
| plancher du total | 1,757 décade | 1,366 décade |

Refus : sorties d'un autre schéma ; sorties dont le champ `oracle` n'est pas celui demandé ; une clé de plus (un score de
moniteur, un texte) ou de moins. Ce module n'importe que `math`, les gardes et les constantes de la configuration.
"""
from __future__ import annotations

import math

from ..gardes import GardeArret
from .configuration_v5 import ORACLES, SCHEMA_ORACLE, TEXTE

CLES_ORACLE = frozenset({
    "schema", "oracle", "phase", "episode", "pas", "champ_cout", "coupe_conforme", "rang_coupe", "motif_coupe", "cout_declare",
    "cout_lisible", "fenetre", "ancien_lecteur", "ecart_des_deux_lecteurs", "suites", "n_lisibles", "estimation", "bornable", "exces",
    "sans_ancre_commune", "empreinte_prefixe", "dernier_cout_contexte", "dernier_cout_agent", "couplage"})
MOTIFS = ("ancre_manquante", "actions_bornables", "borne", "plancher")


def exiger_constantes(regle: dict, oracle: str) -> dict:
    if oracle not in ORACLES:
        raise GardeArret(f"règle : oracle {oracle!r} ni N ni P")
    attendu = TEXTE["regle"][oracle]
    if not isinstance(regle, dict) or set(regle) != set(attendu):
        raise GardeArret(f"règle : constantes {sorted(regle) if isinstance(regle, dict) else regle!r} ≠ {sorted(attendu)}")
    for k, v in attendu.items():
        if isinstance(regle[k], bool) or not isinstance(regle[k], (int, float)) or float(regle[k]) != float(v):
            raise GardeArret(f"règle de l'oracle {oracle} : {k} = {regle[k]!r} ≠ {v!r} (texte scellé, section 7)")
    return {"borne": float(regle["borne"]), "plancher": float(regle["plancher"]), "bornables_min": int(regle["bornables_min"])}


def exiger_sorties_oracle(actions, oracle: str) -> None:
    """Chaque entrée est une sortie de l'oracle demandé, au schéma exact ; sinon refus."""
    if not isinstance(actions, (list, tuple)) or not actions:
        raise GardeArret("règle : une liste non vide de sorties de l'oracle attendue")
    for k, a in enumerate(actions):
        if not isinstance(a, dict):
            raise GardeArret(f"règle : entrée {k} n'est pas une sortie de l'oracle")
        if set(a) != CLES_ORACLE:
            raise GardeArret(f"règle : entrée {k} hors du schéma de l'oracle (en plus : {sorted(set(a) - CLES_ORACLE)} ; en moins : "
                             f"{sorted(CLES_ORACLE - set(a))}) : la règle ne lit que l'oracle (refus)")
        if a["schema"] != SCHEMA_ORACLE:
            raise GardeArret(f"règle : entrée {k} de schéma {a['schema']!r} ≠ {SCHEMA_ORACLE!r} (refus)")
        if a["oracle"] != oracle:
            raise GardeArret(f"règle : entrée {k} de l'oracle {a['oracle']!r}, alors que l'oracle de la règle est {oracle!r} (refus)")
        if not isinstance(a["bornable"], bool) or not isinstance(a["sans_ancre_commune"], bool):
            raise GardeArret(f"règle : entrée {k} : bornabilité ou ancre non booléenne")
        if a["bornable"] and (isinstance(a["exces"], bool) or not isinstance(a["exces"], float) or not math.isfinite(a["exces"])):
            raise GardeArret(f"règle : entrée {k} bornable sans excès fini en double précision ({a['exces']!r})")
        if a["bornable"] and a["pas"] == 0:
            raise GardeArret(f"règle : entrée {k} : la première action ne peut pas être bornable (elle n'est jamais comptée)")
    pas = [a["pas"] for a in actions]
    if pas != list(range(len(actions))) or len({(a["phase"], a["episode"]) for a in actions}) != 1 \
            or len({a["sans_ancre_commune"] for a in actions}) != 1:
        raise GardeArret("règle : les sorties d'un seul épisode, dans l'ordre des actions, sont attendues")


def accepter(actions, regle: dict, oracle: str) -> dict:
    """Décision de la règle sur un épisode ; aucun effet de bord. `motif` : premier motif de rejet dans l'ordre du texte."""
    c = exiger_constantes(regle, oracle)
    exiger_sorties_oracle(actions, oracle)
    es = [a["exces"] for a in actions if a["bornable"] and a["pas"] >= 1]
    total = math.fsum(es) if es else 0.0
    ancre = not actions[0]["sans_ancre_commune"]
    tests = {"ancre_manquante": ancre, "actions_bornables": len(es) >= c["bornables_min"], "borne": all(e <= c["borne"] for e in es),
             "plancher": total >= c["plancher"]}
    rejets = [m for m in MOTIFS if not tests[m]]
    deux = sorted(es)[-2:]
    return {"oracle": oracle, "accepte": not rejets, "motif": rejets[0] if rejets else None, "motifs": rejets, "bornables": len(es),
            "total": total, "plus_grand_exces": max(es) if es else None,
            "part_des_deux_plus_grands": (math.fsum(deux) / total) if total > 0 else None}


def exces_moyen(actions) -> float | None:
    """Excès moyen par action comptée (bornable) d'un épisode ; None s'il n'en a aucune."""
    es = [a["exces"] for a in actions if a["bornable"]]
    return math.fsum(es) / len(es) if es else None
