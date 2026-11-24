"""[v2, après la contre-lecture 1 ; nom neuf, R12 : la v1 reste telle quelle. La configuration est celle de
`dose_reponse.controles_v2.configuration` (même fonction que la garde CL-05) ; argument facultatif : le texte de désignation
pour le critère 3 (fichier JSON {chemin, sha256, lignes_registre}), sinon `null` ; dernier jour de création porté.]

Écrit et scelle la configuration réelle de la course de dose–réponse de l'organisme à consigne cachée (texte scellé
`prereg/T0.6-organisme-consigne-cachee-dose-reponse-v1.md`, 2263c5c4…). Entrées : la banque de 64 tâches (empreinte lue sur
son compagnon), le commit du code cité par la ligne CODE-DOSE-REPONSE-CONSIGNE-CACHEE, et, facultatifs, le chemin de la
pièce jointe (même empreinte exigée) et la désignation. Vérifiée par `controles_v2.exiger_config` avant écriture ; R12.

    PYTHONPATH=src python scripts/ecrire_configuration_dose_reponse_v2.py BANQUE.json COMMIT_CODE [--piece-jointe CHEMIN]
        [--designation DESIGNATION.json] [--sortie SORTIE]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from controle_ia.dose_reponse import controles_v2 as ct
from controle_ia.gardes import GardeArret
from controle_ia.scellement import sceller, verifier

SORTIE = "prereg/T0.6-dose-reponse-configuration-course-v1.json"


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("banque")
    ap.add_argument("commit")
    ap.add_argument("--piece-jointe", default=ct.PIECE_JOINTE)
    ap.add_argument("--designation", default=None)
    ap.add_argument("--sortie", default=SORTIE)
    a = ap.parse_args(argv)
    if not re.fullmatch(r"[0-9a-f]{40}", a.commit):
        print("commit du code : 40 caractères hexadécimaux", file=sys.stderr)
        return 2
    sortie = Path(a.sortie)
    if sortie.exists():
        print(f"{sortie} existe déjà (R12)", file=sys.stderr)
        return 1
    try:
        designation = None
        if a.designation:
            designation = json.loads(Path(a.designation).read_text(encoding="utf-8"))
            if set(designation) != {"chemin", "sha256", "lignes_registre"}:
                raise GardeArret("désignation : clés chemin, sha256, lignes_registre attendues")
        c = ct.configuration(a.banque, verifier(a.banque), a.commit, ct.charger_config_7b(Path(".")), a.piece_jointe, designation)
        ct.exiger_config(c, Path("."))
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        return 1
    sortie.write_text(json.dumps(c, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(f"{sortie} écrite, scellée : {sceller(sortie)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
