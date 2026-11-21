"""Sonde de chargement sous l'interpréteur de la course (`/usr/local/bin/python3 -I`) : la garde v3 et ses données se
chargent sans le module `regex`, et la normalisation tient. Données factices seules. Rend un objet JSON sur la sortie.

Usage : `/usr/local/bin/python3 -I sonde_chargement_course_na_v3.py`
"""

import json
import os
import sys
import unicodedata

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(ICI))  # -I n'ajoute pas le dossier du programme

from pole import garde_motifs_na_v3 as gm  # noqa: E402

donnees = gm.charger_donnees_ignorables(os.path.join(os.path.dirname(ICI), "pole", "ignorables-unicode-15.1.0-na-v1.json"),
                                        "8e15ad688fbb298ade214fe19986e103e4302f0e67d169b7201f730e416699f7")
n = gm.Normaliseur(donnees)
garde = gm.GardeMotifs(gm.charger_liste_motifs(os.path.join(ICI, "liste-motifs-essai-na-v1.json"),
                                               "41a50329f67c41d073115a75ae64981fd59a46b4663c269f42a32b4055c0508b", n))
formes = ["graine-factice", "graine_factice", "graine factice", "graine  factice",
          "grai️ne factice", "grai͏ne factice", "graiㅤne factice", "grai⠀ne factice"]
print(json.dumps({
    "executable": sys.executable,
    "unicodedata": unicodedata.unidata_version,
    "regex_charge": "regex" in sys.modules,
    "points_ignorables": len(donnees.points),
    "refusees": [garde.examiner(f) is not None for f in formes],
    "saine_passe": garde.examiner("texte sain, avec trait-d'union et soulignement_") is None,
}, ensure_ascii=False, sort_keys=True))
