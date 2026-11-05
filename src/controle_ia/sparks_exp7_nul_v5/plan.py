"""Plan de SPARKS-EXP7-NUL, v5 : celui de la v4, branches renommées en v5 (ordres hors de `calcul/`, sorties sous un préfixe
réglable) et étiquette du tir réel."""
from __future__ import annotations

from ..sparks_exp7_nul_v4.plan import *  # noqa: F401,F403
from ..sparks_exp7_nul_v4.plan import PREFIXES, _court


def branche_ordres(commit: str) -> str:
    return f"ordres/sparks-exp7-nul-v5-{_court(commit)}"


def branche_fabrication(commit: str, prefixe: str = "calcul/") -> str:
    if prefixe not in PREFIXES:
        raise ValueError(f"préfixe {prefixe!r}")
    return f"{prefixe}sparks-exp7-nul-v5-{_court(commit)}"


def branche_causal(commit: str, numero: int, prefixe: str = "calcul/") -> str:
    if prefixe not in PREFIXES:
        raise ValueError(f"préfixe {prefixe!r}")
    return f"{prefixe}sparks-exp7-nul-causal-v5-{_court(commit)}-{int(numero):03d}"


def etiquette_tir(commit: str) -> str:
    return f"sparks-exp7-nul-tir-{_court(commit)}"
