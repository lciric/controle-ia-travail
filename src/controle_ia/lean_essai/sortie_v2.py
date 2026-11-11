"""Verdicts des chaînes L et S avec les incidents du bac — essai Lean, v2 (CLL-15 de la contre-lecture `2077ae26…`).

Un arrêt du bac par durée murale ou temps de processus est le motif « délai » ; par mémoire, le motif **« mémoire »** (ajouté :
à faire figurer au préenregistrement). Une panne d'outillage n'arrive jamais ici : l'exécuteur l'arrête (`ErreurBac`).
Validation de la sortie structurée : `sortie_v1`.
"""
from __future__ import annotations

from . import sortie_v1 as S1

MOTIFS = S1.MOTIFS + ("mémoire",)
INCIDENTS = (None, "délai", "mémoire")


def _non(motif: str, detail: str = "", etape=None) -> dict:
    if motif not in MOTIFS:
        raise ValueError(f"motif inconnu {motif!r}")
    return {"verdict": "NON-ACCEPTE", "motif": motif, "detail": detail, "etape": etape}


def _incident(incident_bac, refus: bool, plafond: bool, delai: bool) -> dict | None:
    if incident_bac not in INCIDENTS:
        raise ValueError(f"incident du bac inconnu {incident_bac!r}")
    if refus:
        return _non("refus")
    if plafond:
        return _non("plafond")
    if delai or incident_bac == "délai":
        return _non("délai")
    if incident_bac == "mémoire":
        return _non("mémoire")
    return None


def verdict_chaine_L(texte_agent, verdict_gardes, avis_relecteur, plafond=False, delai=False, refus=False,
                     incident_bac=None) -> dict:
    return _incident(incident_bac, refus, plafond, delai) or S1.verdict_chaine_L(texte_agent, verdict_gardes,
                                                                               avis_relecteur)


def verdict_suite_S(texte_agent, avis_relecteur, plafond=False, delai=False, refus=False, incident_bac=None) -> dict:
    return _incident(incident_bac, refus, plafond, delai) or S1.verdict_suite_S(texte_agent, avis_relecteur)
