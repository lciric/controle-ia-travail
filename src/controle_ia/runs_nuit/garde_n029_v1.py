"""Garde codée de l'exception à N-029 pour R2 (CLC-02) : le bras boîte noire de R2 sur les textes de P3 ne se lance que si
`registres/decisions.md`, au commit lancé, contient une ligne qui porte à la fois « N-029 » et « exception confirmée par
Lazar ». Appelée par `scripts/r1_r2_instance_v1.sh` avant toute installation, dès que `ETAPES` contient un juge.

    PYTHONPATH=src python3 -m controle_ia.runs_nuit.garde_n029_v1 registres/decisions.md
"""
from __future__ import annotations

import sys
from pathlib import Path

from ..gardes import GardeArret

MARQUES = ("N-029", "exception confirmée par Lazar")


def exiger_exception_n029(chemin) -> str:
    """Rend la première ligne qui porte les deux marques ; arrêt si le fichier manque ou si aucune ligne ne les porte."""
    p = Path(chemin)
    if not p.is_file():
        raise GardeArret(f"{p} absent : exception à N-029 non vérifiable")
    for ligne in p.read_text(encoding="utf-8").splitlines():
        if all(m in ligne for m in MARQUES):
            return ligne
    raise GardeArret(f"{p} : aucune ligne ne porte « N-029 » et « exception confirmée par Lazar » : R2 non autorisé")


if __name__ == "__main__":
    try:
        print(exiger_exception_n029(sys.argv[1])[:200])
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(2)
