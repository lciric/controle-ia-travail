"""Module d'étape B **jouet**, pour la seule répétition `repetition_phase_c_jouet_v2.sh` (jamais pour une vraie étape B), v1.

Écrit le 2026-11-14 par le préparateur (modèle A). Même ligne de commande que `lecture_v4 etape-b` :
`python -m etape_b_jouet_v1 etape-b RACINE RUN_T06 RUN_T07 CONFIG_T07 --registre REGISTRE`. Il appelle la **vraie** garde
d'ouverture du code importé (`lecture_v4.ouvrir`, c'est-à-dire `lecture_v2.ouvrir` de C7 : registre, sceaux, garde adaptée, `CODE-T07`,
manifestes, table A, audit, issue de P3-bis ; elle écrit elle-même la ligne `OUVERTURE-T07` au journal), attend `JOUET_DUREE` secondes,
puis écrit une ligne d'ouverture des scores (sans rien ouvrir) et `lecture-t07.json` par la vraie fonction `lecture_v1.ecrire_resultat`.
`JOUET_CODE=2` : refus journalisé par `registre_v1.journaliser_refus` (code 2) ; `JOUET_CODE=3` : `arret-etape-b.json` (code 3).
"""
from __future__ import annotations

import os
import sys
import time
from pathlib import Path

from controle_ia.gardes import GardeArret
from controle_ia.t07 import lecture_v1 as lv1
from controle_ia.t07 import lecture_v4 as lv4
from controle_ia.t07 import registre_v1 as rg


def main(argv: list[str]) -> int:
    if not argv or argv[0] != "etape-b" or "--registre" not in argv:
        print("usage : etape-b RACINE RUN_T06 RUN_T07 CONFIG_T07 --registre REGISTRE", file=sys.stderr)
        return 1
    racine, r6, r7, config_p = Path(argv[1]), argv[2], argv[3], Path(argv[4])
    reg = Path(argv[argv.index("--registre") + 1])
    code, duree = int(os.environ.get("JOUET_CODE", "0")), float(os.environ.get("JOUET_DUREE", "0"))
    instant = int(time.time())
    if code == 2:
        rg.journaliser_refus(reg, instant, f"etape-B/{r6}/{r7}", "refus jouet de la répétition")
        print("REFUS : refus jouet de la répétition", file=sys.stderr)
        return 2
    try:
        config = lv4.charger_configuration(config_p)
        o = lv4.ouvrir(racine, reg, config, "B", r6, instant, r7, racine)
    except GardeArret as e:
        print(f"REFUS : {e}", file=sys.stderr)
        return 2
    time.sleep(duree)
    chemin_m = Path(o["manifeste_t07"]["chemin"])
    if code == 3:
        lv1.ecrire_resultat(racine, chemin_m, "arret-etape-b", {"etape": "B", "motif": "arrêt jouet de la répétition"})
        print("ARRÊT : arrêt jouet", file=sys.stderr)
        return 3
    rg.journaliser_ouverture(reg, instant, f"scores-t07/{r7} (jouet : aucun score ouvert)", o["garde"]["lignes"][rg.SCORES_T07]["sha256"])
    lv1.ecrire_resultat(racine, chemin_m, "lecture-t07", {"jouet": True, "issue_critere_3": "L-jouet"})
    print("L-jouet : phrase jouet")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
