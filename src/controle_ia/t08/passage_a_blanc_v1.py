"""Entrée en ligne de commande du passage à blanc de la lecture de T0.8 sur le registre réel (consigne de la chaîne de
lancement, `722ceb5e…`, tenue en v3 `6f52c4db…` ; texte au brouillon 15 `8d68b7a0…`, § 3.3). v1.

    python -m controle_ia.t08.passage_a_blanc_v1 --config <configuration scellée (course ou lecture)> \
        --registre registres/scellements-v1.md --prereg <texte scellé> [--racine-piece .]

Ne fait qu'appeler `lecture_v1.passage_a_blanc_reel(config["marqueurs"], registre, prereg, racine_piece=…)` après
`scellement.verifier(config)` : aucune règle n'est écrite ici. Le registre est lu, jamais écrit ; aucune sortie de course
n'est ouverte. Sortie standard : le compte rendu du passage (une ligne JSON : lignes du registre, bornes, antériorité ; aucun
résultat). Codes : 0 ; 1 sur un arrêt de garde (`ARRÊT : <motif>`) ; 2 usage.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from ..gardes import GardeArret

COMMANDE = "python -m controle_ia.t08.passage_a_blanc_v1"


def _main(argv: list[str]) -> int:
    import argparse

    from ..scellement import verifier
    from .lecture_v1 import passage_a_blanc_reel

    ap = argparse.ArgumentParser(prog=COMMANDE)
    ap.add_argument("--config", required=True)
    ap.add_argument("--registre", required=True)
    ap.add_argument("--prereg", required=True)
    ap.add_argument("--racine-piece", default=None)
    a = ap.parse_args(argv)
    verifier(a.config)
    config = json.loads(Path(a.config).read_text(encoding="utf-8"))
    r = passage_a_blanc_reel(config.get("marqueurs"), a.registre, a.prereg,
                             racine_piece=Path(a.racine_piece) if a.racine_piece else None)
    print(json.dumps(r, ensure_ascii=False, sort_keys=True, default=str))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(_main(sys.argv[1:]))
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
