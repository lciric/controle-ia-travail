"""Extraction des énoncés, classifications et cibles semées (T0.5) : contrôle des sorties et assemblage des tâches.

Les sorties viennent de sous-agents neufs (option (a) de P-006) qui appliquent mot pour mot les invites H.9 (énoncé)
et H.10 (classification) de 2606.08892, et l'invite des cibles semées de la procédure d'extraction. Ce module ne
fait aucun appel à un modèle : il contrôle chaque sortie (schéma, interdits de H.9, ancrage des cibles dans le texte
du papier) et rend la liste de ses anomalies. Une sortie avec anomalie n'entre jamais dans les tâches : elle est
refaite ou le papier est remplacé, selon la procédure scellée (aucun repli silencieux).
"""
from __future__ import annotations

import re
import unicodedata

from ..gardes import GardeArret
from .propositions import TYPES_DONNEES, TYPES_PAPIER

_FIGURE = re.compile(r"\[FIGURE\s*\d*\]|\bFig(?:ure|\.)\s*\d+|\bTable\s*\d+", re.I)


def normaliser(texte: str) -> str:
    """Texte comparable : formes Unicode composées, guillemets et tirets simplifiés, blancs réduits, minuscules."""
    t = unicodedata.normalize("NFKC", texte)
    t = t.translate({ord(a): b for a, b in zip("‘’“”–— ", "''\"\"-- ")})
    return re.sub(r"\s+", " ", t).strip().lower()


def anomalies_h9(sortie: dict) -> list[str]:
    """Contrôle d'une sortie de H.9 (énoncé, affiliations, coûts)."""
    a = []
    if not isinstance(sortie, dict):
        return ["sortie H.9 : objet JSON attendu"]
    rq = sortie.get("research_questions")
    if not isinstance(rq, str) or len(rq.strip()) < 200:
        a.append("research_questions absent ou trop court (moins de 200 caractères)")
    elif _FIGURE.search(rq):
        a.append(f"research_questions cite une figure ou un tableau : {_FIGURE.search(rq).group(0)!r}")
    if not isinstance(sortie.get("affiliations"), list):
        a.append("affiliations : liste attendue")
    couts = sortie.get("costs")
    if not isinstance(couts, dict) or "total" not in couts or not isinstance(couts.get("splits", []), list):
        a.append("costs : objet {total, splits} attendu")
    return a


def _cle(v) -> str:
    return str(v).replace("\\_", "_").strip()


def anomalies_h10(sortie: dict) -> list[str]:
    """Contrôle d'une sortie de H.10 (classification)."""
    if not isinstance(sortie, dict):
        return ["sortie H.10 : objet JSON attendu"]
    a = []
    if _cle(sortie.get("theory_experiment", "")) not in TYPES_PAPIER:
        a.append(f"theory_experiment illisible : {sortie.get('theory_experiment')!r}")
    if _cle(sortie.get("data_type", "")) not in TYPES_DONNEES:
        a.append(f"data_type illisible : {sortie.get('data_type')!r}")
    if not isinstance(sortie.get("domains", None), list):
        a.append("domains : liste attendue")
    return a


BORNES_CIBLES = {"controls": (3, 6), "fruitful_directions": (1, 3), "sterile_directions": (0, 3)}


def anomalies_cibles(sortie: dict, texte_papier: str) -> list[str]:
    """Contrôle des cibles semées : schéma, bornes, identifiants uniques, et chaque citation retrouvée dans le texte
    converti du papier (à la normalisation près)."""
    if not isinstance(sortie, dict):
        return ["cibles : objet JSON attendu"]
    a, ids = [], set()
    corps = normaliser(texte_papier)
    for famille, (lo, hi) in BORNES_CIBLES.items():
        items = sortie.get(famille)
        if not isinstance(items, list) or not lo <= len(items) <= hi:
            a.append(f"{famille} : entre {lo} et {hi} éléments attendus")
            continue
        for it in items:
            if not isinstance(it, dict):
                a.append(f"{famille} : élément non conforme")
                continue
            ident = it.get("id")
            if not ident or ident in ids:
                a.append(f"{famille} : identifiant absent ou en double ({ident!r})")
            ids.add(ident)
            if len(str(it.get("description", "")).strip()) < 10:
                a.append(f"{ident} : description absente ou trop courte")
            preuve = str(it.get("evidence", "")).strip()
            if len(preuve) < 20:
                a.append(f"{ident} : citation absente ou trop courte")
            elif normaliser(preuve) not in corps:
                a.append(f"{ident} : citation introuvable dans le texte du papier")
    calcul = sortie.get("compute")
    if not isinstance(calcul, dict) or calcul.get("basis") not in ("reported", "estimated"):
        a.append("compute : objet {reference_gpu_hours, basis, evidence} attendu")
    else:
        h = calcul.get("reference_gpu_hours")
        if h is not None and not (isinstance(h, (int, float)) and h > 0):
            a.append(f"compute.reference_gpu_hours : nombre positif ou null attendu ({h!r})")
    return a


def assembler_tache(identifiant: str, sortie_h9: dict, sortie_h10: dict, cibles: dict, texte_papier: str) -> dict:
    """Tâche prête pour le pilote, seulement si les trois sorties sont sans anomalie (sinon arrêt)."""
    anomalies = anomalies_h9(sortie_h9) + anomalies_h10(sortie_h10) + anomalies_cibles(cibles, texte_papier)
    if anomalies:
        raise GardeArret(f"{identifiant} : {len(anomalies)} anomalie(s) : {anomalies[:5]}")
    classification = {k: _cle(sortie_h10[k]) for k in ("theory_experiment", "data_type")}
    classification["domains"] = [str(d) for d in sortie_h10["domains"]]
    return {"identifiant": identifiant, "questions": sortie_h9["research_questions"].strip(),
            "classification": classification, "cibles": cibles, "couts_rapportes": sortie_h9["costs"]}


def exclue_par_classification(sortie_h10: dict) -> bool:
    """Règle d'exclusion de la procédure : un papier « theory_only » sort du pilote (remplacé par la réserve)."""
    return _cle(sortie_h10.get("theory_experiment", "")) == "theory_only"
