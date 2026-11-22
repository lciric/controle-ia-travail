"""Entrée en ligne de commande de la lecture de T0.8 (consigne de la chaîne de lancement, `722ceb5e…`, § 3.3). v1.

    python -m controle_ia.t08.lire_v1 --config <configuration de la lecture> --run-id <AAAAMMJJ-HHMMSS-nom> --prereg <texte>

Ne fait qu'appeler `lecture_v1.executer_lecture(config, Path("."), run_id, prereg)`, depuis la racine du dépôt, après
`scellement.verifier(config)` (configuration scellée, comme l'entrée de la course) ; **aucune règle de lecture n'est écrite
ici** : elles sont toutes dans `lecture_v1.py`, contre-lu. Sortie standard : une ligne JSON qui ne porte que les chemins
(manifeste, `lecture-t08.json`, tables D et F) et la durée — ni la ligne de la table D ni les qualifications, que rend
`executer_lecture` : elles se lisent dans `lecture-t08.json`, par le lecteur, sous sa consigne (rien ne s'affiche à qui lance).
Codes : 0 ; 1 sur un arrêt de garde (`ARRÊT : <motif>` sur la sortie d'erreur) ; 2 usage.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from ..gardes import GardeArret

COMMANDE = "python -m controle_ia.t08.lire_v1"
CLES_AFFICHEES = ("manifeste", "lecture", "tables_d_f", "duree_s")


def _main(argv: list[str]) -> int:
    import argparse

    from ..scellement import verifier
    from .lecture_v1 import executer_lecture

    ap = argparse.ArgumentParser(prog=COMMANDE)
    ap.add_argument("--config", required=True)
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--prereg", default=None)
    a = ap.parse_args(argv)
    verifier(a.config)
    config = json.loads(Path(a.config).read_text(encoding="utf-8"))
    r = executer_lecture(config, Path("."), a.run_id, a.prereg)
    print(json.dumps({k: r[k] for k in CLES_AFFICHEES if k in r}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(_main(sys.argv[1:]))
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
