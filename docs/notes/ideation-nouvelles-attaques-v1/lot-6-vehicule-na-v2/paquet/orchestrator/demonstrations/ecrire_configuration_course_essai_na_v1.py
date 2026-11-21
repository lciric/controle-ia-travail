"""Véhicule NA-1, lot 6 — écrit la configuration de course **d'essai** et ses pièces factices dans un dossier neuf.

    python -I -B demonstrations/ecrire_configuration_course_essai_na_v1.py DOSSIER_NEUF

Brouillon d'essai, déclaré comme tel dans son champ `statut` : aucune valeur n'est celle de l'additif du véhicule. Les
chemins des pièces sont relatifs au dossier de la configuration. Imprime le nom de la configuration et son empreinte.
"""

import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)
for _p in (RACINE, os.path.join(RACINE, "essais")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import configuration_essai_na_lot6_v1 as CE  # noqa: E402


def principal(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 1:
        print("usage : ecrire_configuration_course_essai_na_v1.py DOSSIER_NEUF", file=sys.stderr)
        return 2
    chemin, sha = CE.ecrire_configuration_essai(argv[0])
    print(json.dumps({"configuration": os.path.basename(chemin), "sha256": sha, "statut": CE.STATUT_ESSAI},
                     ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(principal())
