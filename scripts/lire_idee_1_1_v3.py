#!/usr/bin/env python3
"""Lecture gelée du jeu de l'idée 1.1, version 3 (`lire_v3` : format vérifié, erreurs en `GardeArret`). Version 2 :
lecture gelée du jeu de l'idée 1.1, version 2 (M1 : addendum du manifeste relu, fichiers gelés revérifiés ;
lecture `lire_v2`). Version 1 : lecture gelée du jeu de l'idée 1.1 (préenregistrement scellé `3ffe1739…`). **Non lancée par le développeur.**

    python -I -B scripts/lire_idee_1_1_v3.py diag/organisme-idees-juge-v1/<RUN_ID>

Refuse : un préenregistrement autre que le texte ; un manifeste non scellé ; une sortie non scellée, une tranche non
scellée ou différente de l'index, un arrêt consigné (aucune lecture partielle) ; une lecture déjà écrite (R12). Écrit
`lecture.json` scellé dans le dossier du run (étage par étage, issue pour le nœud R-1779, audit de symétrie, prédictions).
Le lecteur neuf (R13) recalcule l'issue de façon indépendante ; l'audit de symétrie (R4) est écrit avant le prononcé.
"""
from __future__ import annotations

import os
import sys

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_v] = "1"
sys.dont_write_bytecode = True

import argparse  # noqa: E402
import json  # noqa: E402
from pathlib import Path  # noqa: E402

RACINE_DEPOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RACINE_DEPOT / "src"))

from controle_ia.gardes import GardeArret  # noqa: E402
from controle_ia.manifeste import lire_manifeste  # noqa: E402
from controle_ia.prereg import exiger_prereg_scelle  # noqa: E402
from controle_ia.organisme_idees_juge import banc_idee_1_1_v2 as B  # noqa: E402
from controle_ia.organisme_idees_juge import execution_idee_1_1_v3 as X  # noqa: E402
from controle_ia.organisme_idees_juge import lecture_idee_1_1_v3 as LE  # noqa: E402


def main(argv=None) -> int:
    a = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    a.add_argument("dossier")
    args = a.parse_args(argv)
    if exiger_prereg_scelle(RACINE_DEPOT / B.CHEMIN_PREREG) != B.EMPREINTE_PREREG:
        raise GardeArret("préenregistrement différent du texte scellé")
    dossier = (RACINE_DEPOT / args.dossier).resolve()
    run_id = dossier.name
    m, sha_m = lire_manifeste(RACINE_DEPOT / "runs" / run_id / "manifeste.json")
    if m["config"]["preenregistrement"]["sha256"] != B.EMPREINTE_PREREG or m["config"]["miniature"]:
        raise GardeArret("manifeste d'un autre texte, ou d'une répétition miniature : lecture refusée")
    X.verifier_addendum_du_manifeste(RACINE_DEPOT, m["config"])      # M1
    racine = B.racine_de(B.EMPREINTE_PREREG)
    for cle, etat in m["config"]["etats_de_controle"].items():
        c = tuple(int(x) for x in cle.strip("()").split(",") if x.strip())
        if B.etat_graine(racine, *c) != etat:
            raise GardeArret(f"état de contrôle de la clé {cle} différent : lecture refusée")
    sortie = X.charger_sortie(dossier)
    if sortie["index"]["manifeste_sha256"] != sha_m:
        raise GardeArret("sortie d'un autre manifeste : lecture refusée")
    chemin = dossier / "lecture.json"
    res = LE.lire_v3(sortie["donnees"], racine)
    sha = X.ecrire_json_scelle(chemin, {"run_id": run_id, "manifeste_sha256": sha_m, "sortie_sha256": sortie["index_sha256"],
                                        "resultat": res})
    print(json.dumps({"lecture": str(chemin.relative_to(RACINE_DEPOT)), "sha256": sha}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
