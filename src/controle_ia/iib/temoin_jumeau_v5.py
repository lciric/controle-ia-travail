"""Le témoin-jumeau, redéfini pour chaque oracle, v5 (texte scellé, section 11 ; section 13, `temoin_jumeau_v5.py`).

Mêmes épisodes acceptés du maître ; premier coût gardé ; coût de chaque action 2 à 10 à coupe conforme remplacé, écrit comme en
3.3 c et d (`reecriture_v5.remplacer_valeur`). Aucun appel du modèle.

- **Oracle à contexte réécrit (N)** : remplacé par la suite retenue par la réécriture couplée (celle qui est entrée dans le
  contexte du jumeau), ou par une valeur vide si le couplage avait rendu le repli vide.
- **Oracle au contexte de l'agent (P)** : remplacé par une des huit suites du jumeau de cette action, tirée au hasard par graine
  `iib/temoin/<episode>/pas<t>` (une suite illisible si le coût déclaré l'était ; valeur vide à défaut) — jamais la médiane.
Une action à coupe non conforme reste telle quelle. Le témoin n'est pas un contrôle du texte des propositions.
"""
from __future__ import annotations

from ..gardes import GardeArret
from . import reecriture_v5 as rw
from .configuration_v5 import ORACLES
from .lecture_cout_v5 import lire_action_v5


def cle_du_temoin(episode: str, pas: int) -> str:
    return f"iib/temoin/{episode}/pas{pas}"


def choisir_suite_P(lectures_suites: list[dict], cout_lisible: bool, rng) -> int | None:
    """Indice de la suite du témoin sous P ; None : valeur vide."""
    if cout_lisible:
        return int(rng.integers(0, len(lectures_suites))) if lectures_suites else None
    illisibles = [i for i, s in enumerate(lectures_suites) if not s["lisible"]]
    return int(illisibles[int(rng.integers(0, len(illisibles)))]) if illisibles else None


def episode_temoin(oracle: str, tok, actions: list[dict], graines, episode: str, config: dict, fins=frozenset(), retenues: list | None = None,
                   suites: list | None = None, lectures_suites: list | None = None) -> dict:
    """Actions du témoin. Sous N : `retenues[t]` (jetons de la suite retenue, None pour le repli vide ou l'action non réécrite) ;
    sous P : `suites[t]` (les huit suites en jetons) et `lectures_suites[t]` (leurs lectures)."""
    if oracle not in ORACLES:
        raise GardeArret(f"témoin-jumeau : oracle {oracle!r} ni N ni P")
    if (oracle == "N" and retenues is None) or (oracle == "P" and (suites is None or lectures_suites is None)):
        raise GardeArret("témoin-jumeau : sous N les suites retenues, sous P les huit suites et leurs lectures sont exigées")
    fen = int(config["oracle"]["fenetre"])
    sortie, notes = [], []
    for t, a in enumerate(actions):
        ids = list(a["ids"])
        lu = lire_action_v5(tok, ids, fins, fen)
        if t == 0 or not lu["coupe"]["conforme"]:
            sortie.append({"ids": ids})
            notes.append({"remplacee": False, "indice": None, "vide": False})
            continue
        if oracle == "N":
            suite, indice = retenues[t], None
        else:
            indice = choisir_suite_P(lectures_suites[t], lu["cout_lisible"], graines.generateur(cle_du_temoin(episode, t)))
            suite = None if indice is None else suites[t][indice]
        r = rw.remplacer_valeur(tok, ids, lu["coupe"]["rang"], suite or [], fins, fen)
        sortie.append({"ids": r["ids"]})
        notes.append({"remplacee": True, "indice": indice, "vide": suite is None})
    return {"actions": sortie, "consignes": notes}
