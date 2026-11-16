#!/usr/bin/env python3
"""Étape 0 de l'idée 1.1, version 3 (modules v3 ; lectures de la lecture gelée v3 dans le bloc d'addendum).
Version 2 : étape 0 de l'idée 1.1, version 2 (modules v2 ; déclarations m9, m10, m11 et comptes non écrits imprimés dans le
bloc d'addendum). Version 1 : étape 0 de l'idée 1.1 (préenregistrement scellé `3ffe1739…`) : préalables 1 et 2, essais d'égalité E0, E9, EP, ED,
banc de mutations et cas sains, critères de H7 et comptes de Hn, chronométrage (20 répétitions de chacune des 30 lignes),
règle de réduction appliquée mécaniquement. N'écrit que des comptes, des temps et des empreintes, dans un fichier d'étape 0
**scellé**, destiné à l'addendum d'empreintes. Processeur seul, sans dépense, aucun appel réseau.

    python -I -B scripts/etape0_idee_1_1_v3.py --travail DOSSIER_HORS_DU_DEPOT [--processus 3] [--sortie CHEMIN.json]
    python -I -B scripts/etape0_idee_1_1_v3.py --lister-empreintes      # lignes « <sha256>  <chemin> » de l'addendum

Graines : racine = entier de l'empreinte du texte ; (98, r) pour E0 ; (97, k, …) pour le reste (k listés dans le fichier).
"""
from __future__ import annotations

import os
import sys

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_v] = "1"
sys.dont_write_bytecode = True

import argparse  # noqa: E402
import json  # noqa: E402
from datetime import datetime, timezone  # noqa: E402
from pathlib import Path  # noqa: E402

RACINE_DEPOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RACINE_DEPOT / "src"))

from controle_ia.gardes import GardeArret, etat_git  # noqa: E402
from controle_ia.manifeste import versions  # noqa: E402
from controle_ia.prereg import exiger_prereg_scelle  # noqa: E402
from controle_ia.organisme_idees_juge import banc_idee_1_1_v2 as B  # noqa: E402
from controle_ia.organisme_idees_juge import etape0_idee_1_1_v3 as E0  # noqa: E402
from controle_ia.organisme_idees_juge import execution_idee_1_1_v3 as X  # noqa: E402

SORTIE_DEFAUT = "docs/notes/organisme-idees-juge-v1/code-idee-1-1-v3/etape0-v1/etape0-idee-1-1-v3.json"


def main(argv=None) -> int:
    a = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    a.add_argument("--travail")
    a.add_argument("--processus", type=int, default=E0.PROCESSUS_MAX)
    a.add_argument("--sortie", default=SORTIE_DEFAUT)
    a.add_argument("--lister-empreintes", action="store_true")
    args = a.parse_args(argv)
    if args.lister_empreintes:
        print(X.lister_empreintes(RACINE_DEPOT), end="")
        return 0
    if exiger_prereg_scelle(RACINE_DEPOT / B.CHEMIN_PREREG) != B.EMPREINTE_PREREG:
        raise GardeArret("préenregistrement différent du texte scellé")
    if not args.travail:
        raise GardeArret("--travail DOSSIER_HORS_DU_DEPOT exigé (vues assemblées hors du dépôt)")
    travail = Path(args.travail).resolve()
    if RACINE_DEPOT.resolve() in travail.parents or travail == RACINE_DEPOT.resolve() or travail.exists():
        raise GardeArret("--travail : dossier neuf hors du dépôt exigé")
    sortie = (RACINE_DEPOT / args.sortie).resolve()
    if sortie.exists():
        raise GardeArret(f"{sortie} existe déjà : R12 interdit d'écraser")
    for interdit in ("diag", "runs", "donnees"):
        if (RACINE_DEPOT / interdit).resolve() in sortie.parents:
            raise GardeArret(f"fichier d'étape 0 sous {interdit}/ : interdit")
    os.nice(10)
    travail.mkdir(parents=True)
    X.installer_garde_reseau()
    debut = datetime.now(timezone.utc).isoformat(timespec="seconds")
    res = E0.etape0(B.racine_de(B.EMPREINTE_PREREG), travail, p=args.processus,
                    journal=lambda m: print(f"[{datetime.now(timezone.utc).strftime('%H:%M:%S')}] {m}", flush=True))
    git = etat_git(RACINE_DEPOT)
    corps = {"debut_utc": debut, "fin_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
             "commit": git["commit"], "depot_propre": git["propre"], "versions": versions(),
             "fichiers_geles": {f: line.split()[0] for f, line in zip(X.FICHIERS_GELES, X.lister_empreintes(RACINE_DEPOT).splitlines())},
             "resultat": res}
    sha = X.ecrire_json_scelle(sortie, corps)
    prog = {"processus": res["programme"]["processus"], "reductions": res["programme"]["reductions"],
            "duree_attendue_h": round(res["programme"]["D_h"], 3),
            "etape0": {"chemin": str(sortie.relative_to(RACINE_DEPOT)), "sha256": sha},
            "declarations": res["declarations"]}
    print(json.dumps({"fichier_etape0": str(sortie.relative_to(RACINE_DEPOT)), "sha256": sha, "jeu_permis": res["jeu_permis"],
                      "bloquants": res["bloquants"]}, ensure_ascii=False, indent=1))
    print("\n--- bloc programme pour l'addendum ---")
    print(X.DEBUT_PROGRAMME + "\n```json\n" + json.dumps(prog, ensure_ascii=False, indent=1) + "\n```\n" + X.FIN_PROGRAMME)
    return 0 if res["jeu_permis"] else 2


if __name__ == "__main__":
    try:
        sys.exit(main())
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
