"""Devis au pire cas de la confrontation (brouillon v7 ; CR3-01, CR3-08), calculé par le code, sur la banque scellée.

Règle : pire cas d'un poste = ce que le noyau peut réserver au plus ; le pire cas d'une génération, d'une ronde ou d'une
défense est son `usd_max` (le noyau refuse au-delà : `PLAFOND`) ; celui d'un amorçage = `cout_pire_cas(prix, longueur
réelle de la consigne avec les six exemples de la banque, sortie maximale du modèle)`. Tout est rendu avec son calcul.
Usage : python -m essaim_m3.outils.devis_confrontation BANQUE.json MISSION.md [--json SORTIE]
"""
from __future__ import annotations

import argparse
import json
import pathlib
import sys

from .. import banque as _banque  # noqa: F401  (import vérifié : la banque est celle du paquet)
from ..noyau import contrat
from ..noyau import taches as _taches

PRIX = {"CLAUDE_FABLE_5_1": ((10.0, 50.0), 64000), "CLAUDE_OPUS_5_5": ((4.0, 20.0), 64000), "GEMINI_ARGON": ((10.0, 50.0), 32000)}


def cout_pire_cas(prix, caracteres: int, max_tokens: int) -> float:
    """Même formule que le collisionneur et `appels.py` : caractères / 3 jetons d'entrée, `max_tokens` jetons de sortie."""
    return caracteres / 3 / 1e6 * prix[0] + max_tokens / 1e6 * prix[1]


def devis(banque: dict, mission: str, bornes: dict) -> dict:
    exemples = banque["train"][:6]
    consigne = contrat.prompt_amorcage(mission, _taches.ETIQUETTES, {"appels_max": bornes["appels_max"], "usd_max": bornes["usd_max"], "temps_max_s": bornes["temps_max_s"]}, exemples)
    amorcage = {e: round(cout_pire_cas(p, len(consigne), mx), 3) for e, (p, mx) in PRIX.items()}
    texte_max = max(len(t["texte"]) for n in ("train", "test", "test_final") for t in banque[n])
    pire_appel = {e: round(cout_pire_cas(p, texte_max + bornes["preambule_caracteres"], bornes["max_tokens_appel"]), 4) for e, (p, _) in PRIX.items()}
    L, R, G, P = bornes["lignees"], bornes["rondes_conception_max"], bornes["generations"], bornes["paires_applicables"]
    conception = L * R * bornes["usd_max_conception"]
    generations = L * G * bornes["usd_max"]
    adaptative = round(sum(amorcage.values()) + conception + generations, 2)
    gelee = round(L * G * bornes["usd_max"], 2)
    confrontation = round(P * bornes["usd_max_defense"], 2)
    une_graine = round(adaptative + gelee + confrontation, 2)
    rep = bornes["repetition"]
    repetition = round(sum(amorcage[e] for e in rep["especes"]) + rep["lignees"] * rep["rondes"] * rep["usd_max_conception"] + rep["lignees"] * rep["generations"] * rep["usd_max"], 2)
    total = round(bornes["graines"] * une_graine + repetition, 2)
    appels_max_total = bornes["graines"] * (L * (R + G) * bornes["appels_max"] + L * G * bornes["appels_max"] + P * bornes["appels_max_defense"])
    return {"bornes": bornes, "consigne_amorcage_caracteres": len(consigne), "texte_max_caracteres": texte_max,
            "amorcage_par_espece": amorcage, "amorcage_total": round(sum(amorcage.values()), 3),
            "pire_cas_appel_par_espece": pire_appel,
            "appels_couverts_par_usd_max": {e: int(bornes["usd_max"] // c) for e, c in pire_appel.items()},
            "course_adaptative": adaptative, "course_gelee": gelee, "confrontation": confrontation, "une_graine": une_graine,
            "repetition": repetition, "total": total, "plafond_demande": bornes["plafond_demande"],
            "somme_des_plafonds_sous_le_go": total <= bornes["plafond_demande"], "appels_max_total": appels_max_total,
            "recherches_max_total": bornes["graines"] * (L * (R + G) * bornes["recherches_max"]) + rep["lignees"] * (rep["rondes"] + rep["generations"]) * bornes["recherches_max"]}


BORNES_V7 = {"lignees": 5, "rondes_conception_max": 8, "generations": 3, "paires_applicables": 12, "graines": 2,
             "appels_max": 160, "usd_max": 46.0, "temps_max_s": 2400, "usd_max_conception": 10.0, "recherches_max": 30,
             "appels_max_defense": 80, "usd_max_defense": 23.0, "max_tokens_appel": 4096, "preambule_caracteres": 3000,
             "repetition": {"especes": ["CLAUDE_OPUS_5_5", "CLAUDE_FABLE_5_1"], "lignees": 2, "rondes": 2, "usd_max_conception": 10.0, "generations": 1, "usd_max": 46.0},
             "plafond_demande": 4270.0}


def principal(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("banque")
    ap.add_argument("mission")
    ap.add_argument("--json", default=None)
    a = ap.parse_args(argv)
    banque = json.loads(pathlib.Path(a.banque).read_text(encoding="utf-8"))
    mission = pathlib.Path(a.mission).read_text(encoding="utf-8")
    d = devis(banque, mission, dict(BORNES_V7))
    texte = json.dumps(d, ensure_ascii=False, indent=1)
    if a.json:
        pathlib.Path(a.json).write_text(texte + "\n", encoding="utf-8")
    print(texte)
    return 0


if __name__ == "__main__":
    sys.exit(principal())
