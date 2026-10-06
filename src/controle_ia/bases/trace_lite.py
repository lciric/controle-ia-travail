"""TRACE-lite (T0.8 ; P-003 ; réimplémenté d'après arXiv 2606.07054, annexe B) — partie déterministe : lecture du
triage, validation des fenêtres, calendrier d'inspection borné. Les appels au moniteur et la lecture du verdict par
espérance (`scores_jetons`) se branchent dessus ; les invites dérivées pour l'environnement (a) sont à sceller
(brouillon `brouillons/T0.8-TRACE-lite-conception-v1-brouillon1.md`).

Règles (gabarit B1) : au plus 4 fenêtres ; fenêtre **locale** = 1 à 3 pas adjacents ; fenêtre **motif** = 3 à 8 pas non
adjacents. Les pas sont numérotés de 1 à T dans les invites. Aucune réparation silencieuse : un JSON illisible donne zéro
fenêtre, une fenêtre hors règles est écartée, et chaque cas devient une anomalie consignée (P-003 : journal des JSON
invalides). Calendrier fixe (le contrôleur B2 est retiré) : fenêtre locale → un InspectStep (B3-1) par pas ; fenêtre
motif → un AnalyzeDecisions (B3-4) sur ses pas puis un CompareSteps (B3-2) entre son premier et son dernier pas.
"""
from __future__ import annotations

import json
import re

from ..gardes import GardeArret

MAX_FENETRES = 4
LOCALE = (1, 3)
MOTIF = (3, 8)


def _dernier_objet_json(texte: str):
    """Dernier objet JSON de premier niveau bien formé du texte (le moniteur peut écrire avant), ou None. Balayage de
    gauche à droite : un objet lu saute ses objets internes, qui ne sont jamais pris pour lui."""
    dernier, i, decodeur = None, 0, json.JSONDecoder()
    while True:
        m = re.compile(r"\{").search(texte, i)
        if m is None:
            return dernier
        try:
            obj, fin = decodeur.raw_decode(texte, m.start())
        except json.JSONDecodeError:
            i = m.start() + 1
            continue
        if isinstance(obj, dict):
            dernier = obj
        i = fin


def _nature(pas: list[int]) -> str | None:
    """« locale » (1 à 3 pas adjacents), « motif » (3 à 8 pas non tous adjacents), sinon None."""
    n = len(pas)
    adjacents = all(b - a == 1 for a, b in zip(pas, pas[1:]))
    if LOCALE[0] <= n <= LOCALE[1] and adjacents:
        return "locale"
    if MOTIF[0] <= n <= MOTIF[1] and not adjacents:
        return "motif"
    return None


def lire_triage(reponse: str, T: int) -> tuple[list[dict], list[str]]:
    """Fenêtres valides (pas triés, uniques, dans 1..T) et anomalies. Au-delà de 4 fenêtres valides, les suivantes sont
    écartées (anomalie)."""
    if T < 1:
        raise GardeArret("épisode sans action")
    obj = _dernier_objet_json(reponse)
    if obj is None:
        return [], ["triage : aucun objet JSON lisible"]
    fenetres, anomalies = [], []
    brutes = obj.get("suspect_windows")
    if not isinstance(brutes, list):
        return [], ["triage : « suspect_windows » absent ou non liste"]
    for k, f in enumerate(brutes):
        if not isinstance(f, dict) or not isinstance(f.get("steps"), list):
            anomalies.append(f"fenêtre {k} : forme invalide")
            continue
        try:
            pas = [int(x) for x in f["steps"]]
        except (TypeError, ValueError):
            anomalies.append(f"fenêtre {k} : pas non entiers")
            continue
        if any(x < 1 or x > T for x in pas):
            anomalies.append(f"fenêtre {k} : pas hors de 1..{T} ({pas})")
            continue
        pas_u = sorted(set(pas))
        if len(pas_u) != len(pas):
            anomalies.append(f"fenêtre {k} : pas en double ({pas})")
            continue
        nature = _nature(pas_u)
        if nature is None:
            anomalies.append(f"fenêtre {k} : ni locale (1 à 3 pas adjacents) ni motif (3 à 8 pas non adjacents) ({pas_u})")
            continue
        if len(fenetres) == MAX_FENETRES:
            anomalies.append(f"fenêtre {k} : au-delà de {MAX_FENETRES} fenêtres, écartée")
            continue
        fenetres.append({"pas": pas_u, "nature": nature, "raison": str(f.get("reason", ""))})
    return fenetres, anomalies


def calendrier(fenetres: list[dict]) -> list[dict]:
    """Appels d'inspection, dans l'ordre : locale → InspectStep par pas ; motif → AnalyzeDecisions puis CompareSteps."""
    appels = []
    for i, f in enumerate(fenetres):
        if f["nature"] == "locale":
            appels += [{"fenetre": i, "action": "InspectStep", "pas": [k]} for k in f["pas"]]
        elif f["nature"] == "motif":
            appels.append({"fenetre": i, "action": "AnalyzeDecisions", "pas": list(f["pas"])})
            appels.append({"fenetre": i, "action": "CompareSteps", "pas": [f["pas"][0], f["pas"][-1]]})
        else:
            raise GardeArret(f"fenêtre {i} : nature {f['nature']!r} inconnue")
    return appels


def budget_max() -> int:
    """Appels au plus par épisode : triage + 4 fenêtres × 3 appels + verdict."""
    return 1 + MAX_FENETRES * max(LOCALE[1], 2) + 1
