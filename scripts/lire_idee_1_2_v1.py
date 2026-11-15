#!/usr/bin/env python3
"""Lecture gelée de l'idée 1.2 sur une sortie **scellée** du jeu (étape 6 du texte scellé) ; écrit et scelle
`lecture-gelee-v1.json` dans le dossier de la sortie ; n'affiche que son chemin et son empreinte.

    python -I -B scripts/lire_idee_1_2_v1.py --manifeste runs/<run>/manifeste.json

Refuse : manifeste non scellé ou altéré, sortie non scellée (lecture avant scellement : run invalide), oracle non
scellé au rejeu, lecture déjà écrite (R12). La racine des rééchantillonnages `(99, b)` est lue au manifeste.
"""
from __future__ import annotations

import os
import sys

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_v] = "1"
sys.dont_write_bytecode = True

import argparse  # noqa: E402
from pathlib import Path  # noqa: E402

RACINE_DEPOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RACINE_DEPOT / "src"))

from controle_ia.gardes import GardeArret  # noqa: E402
from controle_ia.manifeste import lire_manifeste  # noqa: E402
from controle_ia.scellement import empreinte  # noqa: E402
from controle_ia.organisme_idees_juge import banc_tirages_repartis_v1 as B  # noqa: E402
from controle_ia.organisme_idees_juge import execution_v1 as X  # noqa: E402
from controle_ia.organisme_idees_juge import lire_banc_tirages_repartis_v1 as LB  # noqa: E402


def main(argv=None) -> int:
    a = argparse.ArgumentParser()
    a.add_argument("--manifeste", required=True)
    args = a.parse_args(argv)
    chemin_m = (RACINE_DEPOT / args.manifeste).resolve()
    m, _ = lire_manifeste(chemin_m)
    if (m.get("preenregistrement") or {}).get("sha256") != B.EMPREINTE_PREREG or not m.get("decisif"):
        raise GardeArret("manifeste d'un autre jeu, ou non décisif")
    racine = int(m["config"]["racine_graines"])
    if racine != B.racine_de(B.EMPREINTE_PREREG):
        raise GardeArret("racine du manifeste ≠ racine du texte scellé")
    dossier = RACINE_DEPOT / X.DOSSIER_DIAG / m["run_id"]
    chemin = LB.ecrire_lecture(dossier, racine, n_attendus={"N": B.GENERATIONS["N"], "T": B.GENERATIONS["T"]})
    print(f"{empreinte(chemin)}  {chemin.relative_to(RACINE_DEPOT)}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
