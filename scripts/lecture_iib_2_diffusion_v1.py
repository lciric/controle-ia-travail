"""Lecture (2) de (ii-b), diffusion réalisée (conception, brouillon 2, section 6.2) : EXPLORATOIRE, NON OPPOSABLE (R-522).

Refuse de tourner sans la sortie scellée de la lecture (1) et une ligne du registre des décisions qui cite son empreinte.
    PYTHONPATH=src python scripts/lecture_iib_2_diffusion_v1.py --racine . --run-id RUN --registre-decisions registres/decisions.md
Écrit et scelle `diag/RUN/lecture-iib-2-diffusion-exploratoire-non-opposable-v1.json` et, à part,
`diag/RUN/lecture-iib-2-mots-ponderes-exploratoire-non-opposable-v1.json` (jamais montré à un concepteur de moniteur générique).
N'ouvre aucun fichier de sonde (il n'en existe pas). Code 0 ; 1 sur toute garde.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from controle_ia.gardes import GardeArret
from controle_ia.iib import lecture_v1 as lv


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(prog="lecture_iib_2_diffusion_v1")
    p.add_argument("--racine", default=".")
    p.add_argument("--run-id", required=True)
    p.add_argument("--registre-decisions", required=True)
    a = p.parse_args(argv)
    try:
        l1 = lv.exiger_lecture_1_consignee(a.racine, a.run_id, a.registre_decisions)
        sorties = lv.charger_sorties(Path(a.racine), a.run_id, avec_textes=True)
        resultat, mots = lv.lecture_2(sorties, l1["contenu"])
        resultat["lecture_1"]["sha256"] = l1["sha256"]
        chemin, sha = lv.ecrire(a.racine, a.run_id, lv.NOM_2, resultat)
        _, sha_m = lv.ecrire(a.racine, a.run_id, lv.NOM_MOTS, mots)
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        return 1
    print(f"LECTURE (2) ÉCRITE : {chemin} sha256 {sha} ; mots pondérés à part sha256 {sha_m} (EXPLORATOIRE, NON OPPOSABLE (R-522))")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
