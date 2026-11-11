"""Lancement de la conduite du témoin de Bailey (addendum 2, condition 6 ; procédure de la passation
`registres/passations/2026-11-11-1624-attaquant-informe-passation-autre-compte.md`, étape 5).

Usage, détaché (`setsid nohup`), depuis la racine du dépôt, sous `GO_ID=GO-2026-11-10-10`,
`DEPOT_URL=https://github.com/lciric/controle-ia-travail.git`, `PYTHONPATH=<dépôt>/src`, venv Python 3.11 actif :

    python runs/temoin-bailey-v1-20261111/lancer-conduite-v1.py --offre <id> --image <image>

Ce script ne fait que construire `lanceur_v13.Conduite` avec les valeurs de la procédure et appeler `.conduire()` ;
toutes les gardes sont celles du code au commit 4988f3f4. Le bilan rendu est écrit dans `bilan-lancement-v1.json`
à côté de la sortie (jamais dans la sortie, que la conduite exige neuve). Il ne lit aucune note.
"""
import argparse
import json
import os
import sys
import time
from pathlib import Path

from controle_ia.temoin_bailey import lanceur_v13 as L

DEPOT = Path("/home/user/controle-ia-travail")
BASE = DEPOT / "runs" / "temoin-bailey-v1-20261111"
GO_ID = "GO-2026-11-10-10"


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--offre", required=True)
    p.add_argument("--image", required=True)
    a = p.parse_args()
    if os.environ.get("GO_ID") != GO_ID or os.environ.get("DEPOT_URL") != L.DEPOT_URL:
        print("GO_ID ou DEPOT_URL absent ou différent : rien ne tourne", file=sys.stderr)
        return 2
    sortie = BASE / "sortie-conduite-v1"  # chemin absolu, le même pour `reprendre` (A-1)
    trace = BASE / "bilan-lancement-v1.json"
    if trace.exists():
        print("bilan de lancement déjà présent (R12) : rien ne tourne", file=sys.stderr)
        return 2
    conduite = L.Conduite(fournisseur=L.FournisseurVast(), manifeste_local=BASE / "manifeste-local-v3.json",
                          sortie=sortie, go_id=GO_ID, texte_go=L.texte_go_main(DEPOT), offre=str(a.offre),
                          image=a.image, depot_local=DEPOT, instances_anterieures=[])
    debut = time.time()
    try:
        bilan = conduite.conduire()
        issue = {"bilan": bilan}
    except Exception as err:  # la conduite a déjà fait `_finir` ; on consigne l'erreur sans valeur de note
        issue = {"erreur": f"{type(err).__name__}: {err}"[:500]}
    issue.update({"offre": a.offre, "image": a.image, "debut": debut, "fin": time.time(), "pid": os.getpid()})
    trace.write_text(json.dumps(issue, ensure_ascii=False, indent=2, sort_keys=True, default=str) + "\n",
                     encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
