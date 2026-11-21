"""Contrôles de session de l'organisme retenu, v5 : ceux de `session_v1`, sauf la vérification de la configuration.

Le lanceur de session appelle `session_v1` pour le GO, le plafond de la ligne, la variante, la carte, le filtre et le choix des
offres, les instances et le préalable de création ; ces sous-commandes lisent dans la configuration des sections de la forme de
la version 1, que la configuration en version 5 porte à l'identique en mode réel (`configuration_v5.exiger_location`). Seule la
sous-commande `config` change : elle vérifie par `configuration_v5.exiger_config_v5` (prête à lancer), non par la version 1.
Usage : `python -I -B -c "… session_v5.main(sys.argv[1:])" config CONFIG.json`, ou toute sous-commande de `session_v1`.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from ..gardes import GardeArret
from . import configuration_v5 as cf


def verifier_config(chemin, racine=".") -> dict:
    config = json.loads(Path(chemin).read_text(encoding="utf-8"))
    return cf.exiger_config_v5(config, racine, pour_lancer=True)


def main(argv: list[str]) -> int:
    if len(argv) in (2, 3) and argv[0] == "config":
        try:
            r = verifier_config(argv[1], argv[2] if len(argv) == 3 else Path(__file__).resolve().parents[3])
        except (GardeArret, OSError, ValueError) as e:
            print(f"REFUS : {e}", file=sys.stderr)
            return 1
        print(f"configuration v5 conforme (mode {r['mode']}, nœuds {''.join(r['noeuds'][k] for k in sorted(r['noeuds']))})")
        return 0
    from . import session_v1

    return session_v1.main(argv)
