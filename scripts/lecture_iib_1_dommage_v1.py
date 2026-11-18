"""Lecture (1) de (ii-b), dommage agrégé par l'oracle (conception, brouillon 2, section 6.1) : EXPLORATOIRE, NON OPPOSABLE (R-522).

Sur processeur, après le rapatriement et le scellement des sorties de la course, par le lecteur neuf désigné par la mère.
    PYTHONPATH=src python scripts/lecture_iib_1_dommage_v1.py --racine . --run-id RUN
Écrit et scelle `diag/RUN/lecture-iib-1-dommage-exploratoire-non-opposable-v1.json` (jamais d'écrasement) ; imprime son empreinte, à
consigner au registre des décisions avant toute lecture (2). Code 0 ; 1 sur toute garde (motif sur la sortie d'erreur).
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from controle_ia.gardes import GardeArret
from controle_ia.iib import lecture_v1 as lv


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(prog="lecture_iib_1_dommage_v1")
    p.add_argument("--racine", default=".")
    p.add_argument("--run-id", required=True)
    a = p.parse_args(argv)
    try:
        sorties = lv.charger_sorties(Path(a.racine), a.run_id)
        chemin, sha = lv.ecrire(a.racine, a.run_id, lv.NOM_1, lv.lecture_1(sorties))
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        return 1
    print(f"LECTURE (1) ÉCRITE : {chemin} sha256 {sha} (EXPLORATOIRE, NON OPPOSABLE (R-522)) : à consigner au registre des décisions")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
