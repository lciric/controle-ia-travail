"""Plan de SPARKS-EXP7-NUL, v4 : celui de la v3, avec les noms de branches liés au commit lancé (contre-lecture du delta v3,
points 10 et 15) : ordres écrits par la session hors de `calcul/`, sorties écrites par l'instance sous un préfixe réglable
(`calcul/` par défaut, `essai/` pour la répétition)."""
from __future__ import annotations

import re

from ..sparks_exp7_nul_v3.plan import *  # noqa: F401,F403
from ..sparks_exp7_nul_v3.plan import FIN_ECHEANCE_UTC_S  # noqa: F401

PREFIXES = ("calcul/", "essai/")


def _court(commit: str) -> str:
    if not re.fullmatch(r"[0-9a-f]{40}", commit):
        raise ValueError("commit : 40 chiffres hexadécimaux")
    return commit[:12]


def branche_ordres(commit: str) -> str:
    return f"ordres/sparks-exp7-nul-v4-{_court(commit)}"


def branche_fabrication(commit: str, prefixe: str = "calcul/") -> str:
    if prefixe not in PREFIXES:
        raise ValueError(f"préfixe {prefixe!r}")
    return f"{prefixe}sparks-exp7-nul-v4-{_court(commit)}"


def branche_causal(commit: str, numero: int, prefixe: str = "calcul/") -> str:
    if prefixe not in PREFIXES:
        raise ValueError(f"préfixe {prefixe!r}")
    return f"{prefixe}sparks-exp7-nul-causal-v4-{_court(commit)}-{int(numero):03d}"
