"""v5 (R12 ; v1 à v4 restent telles quelles) : conduite tournée sur un poste Hetzner (la session ne peut pas ouvrir de
`ssh`) ; sortie, bilan et PID neufs (`sortie-conduite-v5`, `bilan-lancement-v5.json`, `lancement-v5.pid`) ; instance
60330510 (lancement v4, détruite par la conduite) ajoutée aux instances antérieures du poste.

v4 (R12 ; v1 à v3 restent telles quelles) : sortie, bilan et PID neufs (`sortie-conduite-v4`, `bilan-lancement-v4.json`,
`lancement-v4.pid`) ; instance 60326443 (lancement v3, détruite à 08:08:49Z après l'extinction de la machine de la
session) ajoutée aux instances antérieures du poste.

v3 (R12 ; v1 et v2 restent telles quelles) : sortie et bilan neufs (`sortie-conduite-v3`, `bilan-lancement-v3.json`) ;
PID écrit par le script lui-même au démarrage (`lancement-v3.pid` ; en v2, le PID relevé était celui du parent de
`setsid`, sorti aussitôt) ; instance 60280913 (lancement v2, détruite) comptée dans les instances antérieures du poste
(B = 75, fixé à sa création ; D la compte).

v2 (R12 ; la v1 reste telle quelle) : sortie et bilan neufs (`sortie-conduite-v2`, `bilan-lancement-v2.json`) ;
refus avant toute conduite si `vastai`, `ssh` ou `scp` est introuvable dans le PATH (la v1 a échoué à la création,
`FileNotFoundError: vastai`, aucune instance créée, inventaire R10 vide pour son étiquette).

Lancement de la conduite du témoin de Bailey (addendum 2, condition 6 ; procédure de la passation
`registres/passations/2026-11-11-1624-attaquant-informe-passation-autre-compte.md`, étape 5).

Usage, détaché (`setsid nohup`), depuis la racine du dépôt, sous `GO_ID=GO-2026-11-10-10`,
`DEPOT_URL=https://github.com/lciric/controle-ia-travail.git`, `PYTHONPATH=<dépôt>/src`, venv Python 3.11 actif :

    python runs/temoin-bailey-v1-20261111/lancer-conduite-v5.py --offre <id> --image <image>

Ce script ne fait que construire `lanceur_v13.Conduite` avec les valeurs de la procédure et appeler `.conduire()` ;
toutes les gardes sont celles du code au commit 4988f3f4. Le bilan rendu est écrit dans `bilan-lancement-v2.json`
à côté de la sortie (jamais dans la sortie, que la conduite exige neuve). Il ne lit aucune note.
"""
import argparse
import json
import os
import shutil
import sys
import time
from pathlib import Path

from controle_ia.temoin_bailey import lanceur_v13 as L

DEPOT = Path("/home/user/controle-ia-travail")
BASE = DEPOT / "runs" / "temoin-bailey-v1-20261111"
GO_ID = "GO-2026-11-10-10"
# Lancement v2 : création relevée par la conduite (`conduite-v5.jsonl` de la sortie v2), destruction par l'identifiant
# à 2026-11-12T00:14:43Z (`registres/arrets.md`), c relevé par la conduite.
ANTERIEURES = [{"id": "60280913", "c": 1.6404444444444444, "creation": 1794441800.044329,
                "destruction": 1794442483.0, "B": 75.0},
               # Lancement v3 : création relevée par la conduite (sortie v3), destruction par l'identifiant à 08:08:49Z.
               {"id": "60326443", "c": 1.2392592592592593, "creation": 1794469718.6305506,
                "destruction": 1794470929.0, "B": 75.0},
               # Lancement v4 : création et destruction relevées par la conduite v4 (`sortie-conduite-v4/poste-v5.json`).
               {"id": "60330510", "c": 1.6071111111111112, "creation": 1794472034.7656338,
                "destruction": 1794473847.2796314, "B": 75.0}]


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--offre", required=True)
    p.add_argument("--image", required=True)
    a = p.parse_args()
    if os.environ.get("GO_ID") != GO_ID or os.environ.get("DEPOT_URL") != L.DEPOT_URL:
        print("GO_ID ou DEPOT_URL absent ou différent : rien ne tourne", file=sys.stderr)
        return 2
    manquants = [o for o in ("vastai", "ssh", "scp") if shutil.which(o) is None]
    if manquants:
        print(f"outils introuvables dans le PATH : {manquants} : rien ne tourne", file=sys.stderr)
        return 2
    pidf = BASE / "lancement-v5.pid"
    if pidf.exists():
        print("PID de lancement déjà présent (R12) : rien ne tourne", file=sys.stderr)
        return 2
    pidf.write_text(f"{os.getpid()}\n", encoding="utf-8")
    sortie = BASE / "sortie-conduite-v5"  # chemin absolu, le même pour `reprendre` (A-1)
    trace = BASE / "bilan-lancement-v5.json"
    if trace.exists():
        print("bilan de lancement déjà présent (R12) : rien ne tourne", file=sys.stderr)
        return 2
    conduite = L.Conduite(fournisseur=L.FournisseurVast(), manifeste_local=BASE / "manifeste-local-v3.json",
                          sortie=sortie, go_id=GO_ID, texte_go=L.texte_go_main(DEPOT), offre=str(a.offre),
                          image=a.image, depot_local=DEPOT, instances_anterieures=ANTERIEURES)
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
