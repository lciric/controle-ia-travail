"""Sortie structurée des bras et verdicts des chaînes L et S — essai Lean, v1.

Brouillon 3, § 1.2 (`ACCEPTE` ou `NON-ACCEPTE`, tout le reste compté `NON-ACCEPTE` avec son motif), § 3.1 (verdict de la
chaîne L : l'agent accepte, les gardes passent, le relecteur ne relève aucune infidélité), § 3.2 (règle du « ou » de la suite),
§ 3.5 (sortie validée par schéma ; sortie invalide et refus comptés avec leur motif, jamais reformulés).
"""
from __future__ import annotations

import json

VERDICTS_AGENT = ("ACCEPTE", "REJET")
MOTIFS = ("rejet", "infidélité", "gardes", "plafond", "délai", "sortie invalide", "refus", "relecteur absent")
CLES = {"L": {"verdict", "etape", "raison", "fichier_lean"}, "S": {"verdict", "etape", "raison"},
        "N": {"verdict", "etape", "raison"}}
RAISON_MAX, FICHIER_MAX = 8000, 256 * 1024


def valider_sortie(obj, bras: str) -> tuple[bool, str]:
    if bras not in CLES:
        raise ValueError(f"bras inconnu {bras!r}")
    if not isinstance(obj, dict):
        return False, "objet JSON attendu"
    if set(obj) != CLES[bras]:
        return False, f"clés {sorted(obj)} ≠ {sorted(CLES[bras])}"
    if obj["verdict"] not in VERDICTS_AGENT:
        return False, f"verdict {obj['verdict']!r} hors de {VERDICTS_AGENT}"
    etape = obj["etape"]
    if obj["verdict"] == "REJET":
        if not (isinstance(etape, int) and not isinstance(etape, bool) and etape >= 0):
            return False, "un rejet porte une étape localisée (entier ≥ 0 ; 0 = énoncé annoncé)"
    elif etape is not None:
        return False, "une acceptation ne porte pas d'étape"
    if not isinstance(obj["raison"], str) or len(obj["raison"]) > RAISON_MAX:
        return False, "raison : chaîne d'au plus 8000 caractères"
    if bras == "L":
        f = obj["fichier_lean"]
        if not isinstance(f, str) or not f.strip() or len(f.encode("utf-8")) > FICHIER_MAX:
            return False, "fichier_lean : chaîne non vide d'au plus 256 Kio"
    return True, ""


def lire_sortie(texte: str, bras: str) -> tuple[dict | None, str]:
    try:
        obj = json.loads(texte)
    except (json.JSONDecodeError, TypeError) as e:
        return None, f"JSON illisible ({type(e).__name__})"
    ok, motif = valider_sortie(obj, bras)
    return (obj, "") if ok else (None, motif)


def _non(motif: str, detail: str = "", etape=None) -> dict:
    if motif not in MOTIFS:
        raise ValueError(f"motif inconnu {motif!r}")
    return {"verdict": "NON-ACCEPTE", "motif": motif, "detail": detail, "etape": etape}


def verdict_chaine_L(texte_agent: str | None, verdict_gardes: dict | None, avis_relecteur: dict | None,
                     plafond: bool = False, delai: bool = False, refus: bool = False) -> dict:
    """`avis_relecteur` : {"infidele": bool, "etapes": [entiers]} rendu par le relecteur de fidélité."""
    if refus:
        return _non("refus")
    if plafond:
        return _non("plafond")
    if delai:
        return _non("délai")
    obj, motif = lire_sortie(texte_agent, "L") if texte_agent is not None else (None, "aucune sortie")
    if obj is None:
        return _non("sortie invalide", motif)
    if obj["verdict"] == "REJET":
        return _non("rejet", obj["raison"][:500], obj["etape"])
    if not verdict_gardes or not verdict_gardes.get("accepte_gardes"):
        echecs = [g for g, v in (verdict_gardes or {}).get("gardes", {}).items() if not v["ok"]]
        return _non("gardes", ", ".join(echecs) or "verdict des gardes absent")
    if avis_relecteur is None or not isinstance(avis_relecteur.get("infidele"), bool):
        return _non("relecteur absent")
    if avis_relecteur["infidele"]:
        return _non("infidélité", "", avis_relecteur.get("etapes"))
    return {"verdict": "ACCEPTE", "motif": "", "detail": "", "etape": None}


def verdict_suite_S(texte_agent: str | None, avis_relecteur: dict | None, plafond: bool = False, delai: bool = False,
                    refus: bool = False) -> dict:
    """Règle du « ou » : `NON-ACCEPTE` si l'agent rejette **ou** si le relecteur marque une étape fausse.
    `avis_relecteur` : {"etapes_fausses": [entiers]}."""
    if refus:
        return _non("refus")
    if plafond:
        return _non("plafond")
    if delai:
        return _non("délai")
    obj, motif = lire_sortie(texte_agent, "S") if texte_agent is not None else (None, "aucune sortie")
    if obj is None:
        return _non("sortie invalide", motif)
    if obj["verdict"] == "REJET":
        return _non("rejet", obj["raison"][:500], obj["etape"])
    if avis_relecteur is None or not isinstance(avis_relecteur.get("etapes_fausses"), list):
        return _non("relecteur absent")
    if avis_relecteur["etapes_fausses"]:
        return _non("rejet", "étape marquée fausse par le relecteur", avis_relecteur["etapes_fausses"][0])
    return {"verdict": "ACCEPTE", "motif": "", "detail": "", "etape": None}
