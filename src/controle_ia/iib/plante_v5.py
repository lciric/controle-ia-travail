"""L'excès planté, v5 (texte scellé, section 10.1 ; section 13, `plante_v5.py`) : rapporté, lu par l'oracle à contexte réécrit.

Copie d'un épisode honnête où le coût de chaque action de rang 2 à 10, s'il est lisible sur sa fenêtre, est multiplié par 10^δ
(même loi et même écriture que l'épisode régénéré), **sans rien régénérer** : l'agent n'a pas réagi. Graine
`iib/plante/<episode>/pas<t>`. Tout le reste de l'épisode est égal à l'octet.
"""
from __future__ import annotations

from . import reecriture_v5 as rw
from .lecture_cout_v5 import lire_action_v5
from .regenere_v5 import tirer_delta


def cle_du_plante(episode: str, pas: int) -> str:
    return f"iib/plante/{episode}/pas{pas}"


def planter(tok, actions: list[dict], graines, episode: str, config: dict, fins=frozenset(), deltas: list | None = None) -> dict:
    """Rend la copie aux coûts multipliés à partir de l'action 2 et, par action, δ et le coût d'avant. `deltas` (essais) :
    δ imposés par action, à la place du tirage."""
    loi, fen = config["organisme"]["loi"], int(config["oracle"]["fenetre"])
    sortie, notes = [], []
    for t, a in enumerate(actions):
        ids = list(a["ids"])
        if t == 0:
            sortie.append({"ids": ids})
            notes.append({"delta": 0.0, "cout_avant": None, "multipliee": False})
            continue
        lu = lire_action_v5(tok, ids, fins, fen)
        if not (lu["coupe"]["conforme"] and lu["cout_lisible"]):
            sortie.append({"ids": ids})
            notes.append({"delta": None, "cout_avant": None, "multipliee": False})
            continue
        delta = deltas[t] if deltas is not None else tirer_delta(graines.generateur(cle_du_plante(episode, t)), loi)
        r = rw.multiplier_cout(tok, ids, lu["coupe"]["rang"], delta, fins, fen)
        sortie.append({"ids": r["ids"]})
        notes.append({"delta": float(delta), "cout_avant": lu["cout_declare"], "multipliee": bool(r["multipliee"])})
    return {"actions": sortie, "consignes": notes}
