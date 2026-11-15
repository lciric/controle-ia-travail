#!/usr/bin/env python3
"""Lecture gelée v2 de l'idée 1.2 sur une sortie **scellée et complète** du jeu (étape 6 du texte scellé) ; écrit et scelle
`lecture-gelee-v2.json` dans le dossier de la sortie ; n'affiche que son chemin et son empreinte.

    python -I -B scripts/lire_idee_1_2_v2.py --manifeste runs/<run>/manifeste.json

Refuse : manifeste non scellé ou altéré, non décisif ou d'un autre texte ; racine différente de celle du texte ; états de
contrôle des clés différents de ceux du manifeste (numpy ou manifeste altéré) ; sortie non scellée ; `arret.json`
présent ; `journal.json` absent ; empreinte du manifeste différente de celle que portent les sorties (mineur 2) ; oracle
non scellé au rejeu ; niveau de l'intervalle différent du texte ; run incomplet ; lecture déjà écrite (R12).
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
from controle_ia.organisme_idees_juge import execution_v2 as X  # noqa: E402
from controle_ia.organisme_idees_juge import lire_banc_tirages_repartis_v2 as LB  # noqa: E402


def exiger_etats_de_controle(config: dict, racine: int) -> None:
    etats = config.get("etats_de_controle")
    if not etats:
        raise GardeArret("manifeste sans états de contrôle des clés : lecture refusée")
    for cle, etat in etats.items():
        t = tuple(int(x) for x in cle.strip("()").split(",") if x.strip())
        if B.etat_graine(racine, *t) != etat:
            raise GardeArret(f"état de contrôle de la clé {cle} ≠ manifeste : numpy ou manifeste altéré")


def main(argv=None) -> int:
    a = argparse.ArgumentParser()
    a.add_argument("--manifeste", required=True)
    args = a.parse_args(argv)
    chemin_m = (RACINE_DEPOT / args.manifeste).resolve()
    m, sha_m = lire_manifeste(chemin_m)
    if (m.get("preenregistrement") or {}).get("sha256") != B.EMPREINTE_PREREG or not m.get("decisif"):
        raise GardeArret("manifeste d'un autre jeu, ou non décisif")
    racine = int(m["config"]["racine_graines"])
    if racine != B.racine_de(B.EMPREINTE_PREREG):
        raise GardeArret("racine du manifeste ≠ racine du texte scellé")
    exiger_etats_de_controle(m["config"], racine)
    dossier = RACINE_DEPOT / X.DOSSIER_DIAG / m["run_id"]
    chemin = LB.ecrire_lecture(dossier, racine, n_attendus={"N": B.GENERATIONS["N"], "T": B.GENERATIONS["T"]},
                               manifeste_sha=sha_m)
    print(f"{empreinte(chemin)}  {chemin.relative_to(RACINE_DEPOT)}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
