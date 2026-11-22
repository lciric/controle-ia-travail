"""Pièce 8 — gabarit d'inventaire préalable (§ 6 de la spécification).

L'agent habilité relève par étiquettes seulement, sans lire aucun résultat. Par course déjà jouée, les onze rubriques du
§ 6 (la graine et l'engagement en deux champs). Le gabarit refuse tout champ hors liste (un champ de résultat ne peut pas y entrer).

Ce que cela décide (§ 6) : si aucune affectation passée n'a été tirée, aucune p-valeur de permutation n'est permise sur
le passé et tout est à rejouer. La règle par course (« affectation non tirée : p-valeur de permutation interdite sur
cette course ») en découle ; la spécification ne dit rien des courses tirées (point laissé ouvert : aucune permission
n'est écrite ici pour elles). Le nombre de tâches disponibles est compté ; le choix de k et de N qui en découle n'est pas
écrit (la spécification ne donne pas la règle).
"""
from __future__ import annotations

import json

from .erreurs_v2 import RefusInventaire

# Champs du § 6, dans l'ordre ; valeur None : texte libre non vide ; tuple : valeurs permises.
CHAMPS = {
    "identifiant_tache": None,
    "organisme": ("saboteur", "jumeau"),
    "regime": ("observé", "non observé"),
    "affectation_par": None,  # qui a affecté le régime
    "affectation_comment": ("tiré", "fixé à la main", "par lot"),
    # « la graine et son engagement, présents ou non » : relevés en deux champs (choix d'écriture, point laissé ouvert)
    "graine": ("présente", "absente"),
    "engagement": ("présent", "absent"),
    "unite_affectation": None,
    "episodes_par_regime_et_tache": None,  # texte ou nombre relevé, jamais un résultat
    "texte_etiquette": None,
    "ordre_et_date_passage": None,
    "juge_du_dommage": ("aveugle", "non aveugle"),
    "episodes_manquants": None,
}
INCONNU = "inconnu"


def gabarit() -> str:
    """Gabarit vide, une course, en JSON ; chaque valeur rappelle ce qui est attendu."""
    vide = {c: (" | ".join(v) if v else "<à relever, par étiquettes seulement>") for c, v in CHAMPS.items()}
    return json.dumps({"courses": [vide]}, ensure_ascii=False, indent=1) + "\n"


def verifier_course(course: dict) -> None:
    if not isinstance(course, dict):
        raise RefusInventaire("course non structurée")
    hors = set(course) - set(CHAMPS)
    if hors:
        raise RefusInventaire(f"champ(s) hors gabarit, refusé(s) (aucun résultat ne se relève) : {sorted(hors)}")
    absents = [c for c in CHAMPS if c not in course]
    if absents:
        raise RefusInventaire(f"champ(s) absent(s) : {absents} (écrire « {INCONNU} » plutôt que d'omettre)")
    for c, permis in CHAMPS.items():
        v = course[c]
        if permis is None:
            if not isinstance(v, (str, int)) or isinstance(v, bool) or (isinstance(v, str) and not v.strip()):
                raise RefusInventaire(f"{c} : valeur vide ou mal formée : {v!r}")
        elif v not in permis and v != INCONNU:
            raise RefusInventaire(f"{c} : {v!r} hors des valeurs permises {permis} (ou « {INCONNU} »)")


def ce_que_cela_decide(inventaire: dict) -> dict:
    courses = inventaire.get("courses") if isinstance(inventaire, dict) else None
    if not courses:
        raise RefusInventaire("inventaire vide")
    for c in courses:
        verifier_course(c)
    tirees = [c for c in courses if c["affectation_comment"] == "tiré"]
    interdites = [c["identifiant_tache"] for c in courses if c["affectation_comment"] != "tiré"]
    decisions = []
    if not tirees:
        decisions.append("Aucune affectation passée n'a été tirée : aucune p-valeur de permutation n'est permise sur le "
                         "passé, et tout est à rejouer.")
    return {
        "decisions": decisions,
        "p_valeur_permutation_interdite": interdites,
        "taches_disponibles": len({c["identifiant_tache"] for c in courses}),
        "textes_etiquette": sorted({str(c["texte_etiquette"]) for c in courses}),
    }
