"""Contrôle des plages « Default_Ignorable_Code_Point » du fichier de données contre le module `regex`, là où il est
présent (mère, 08:55Z et 08:59Z). Outil d'essai : il n'est jamais lu par le code de la course.

`regex` porte sa propre version d'Unicode, postérieure à 15.1 (22 995 points assignés de plus qu'Unicode 15.1 selon
`unicodedata` : sonde de la v3). La comparaison est donc faite **sur les points communs**, c'est-à-dire les points
assignés en 15.1 selon `unicodedata` de l'interpréteur (version 15.1.0 exigée) ; les écarts y sont comptés et nommés. Les
écarts sur les points non assignés en 15.1 sont comptés et nommés à part, pour information.

Usage : `.venv/bin/python -B controle_ignorables_regex_na_v3.py DONNEES.json EMPREINTE`
"""

import json
import os
import sys
import unicodedata

ICI = os.path.dirname(os.path.abspath(__file__))
if os.path.dirname(ICI) not in sys.path:
    sys.path.insert(0, os.path.dirname(ICI))

from pole import garde_motifs_na_v3 as gm  # noqa: E402


def points_regex():
    import regex  # présent sous .venv seulement ; absent, l'appelant le dit
    tous = "".join(chr(c) for c in range(0x110000) if not 0xD800 <= c <= 0xDFFF)
    return frozenset(ord(ch) for ch in regex.findall(r"\p{Default_Ignorable_Code_Point}", tous))


def controler(points_donnees, points_de_regex=None):
    """Rend les écarts entre les données et `regex`, sur les points communs (assignés en 15.1) et ailleurs."""
    if unicodedata.unidata_version != gm.VERSION_UNICODE_ATTENDUE:
        raise RuntimeError("le contrôle exige unicodedata 15.1.0 pour dire quels points sont assignés en 15.1")
    rx = points_regex() if points_de_regex is None else points_de_regex
    ecarts = set(points_donnees) ^ set(rx)

    def assigne(c):
        return not 0xD800 <= c <= 0xDFFF and unicodedata.category(chr(c)) != "Cn"

    communs = sorted(c for c in ecarts if assigne(c))
    hors = sorted(c for c in ecarts if not assigne(c))

    def nommer(liste):
        return [{"point": f"U+{c:04X}", "donnees": c in points_donnees, "regex": c in rx} for c in liste]

    return {"points_donnees": len(points_donnees), "points_regex": len(rx),
            "ecarts_sur_points_communs": len(communs), "ecarts_communs_nommes": nommer(communs),
            "ecarts_hors_points_communs": len(hors), "ecarts_hors_nommes": nommer(hors[:50])}


def main(argv):
    donnees = gm.charger_donnees_ignorables(argv[0], argv[1])
    print(json.dumps(controler(donnees.points), ensure_ascii=False, sort_keys=True, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
