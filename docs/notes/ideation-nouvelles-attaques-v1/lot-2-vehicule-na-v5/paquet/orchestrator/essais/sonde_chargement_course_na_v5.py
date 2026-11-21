"""Sonde de chargement sous l'interpréteur de la course (`/usr/local/bin/python3 -I`) : la garde v4 et ses données se
chargent sans le module `regex`, et la normalisation tient, celle des motifs comprise. Données factices seules, plus la
liste réelle des noms refusés, lue par `liste_reelle_na_v5` sur la branche principale à son empreinte (v5 : aucune copie
dans le paquet), dont rien n'est affiché que des comptes. Rend un objet JSON.

Usage : `/usr/local/bin/python3 -I sonde_chargement_course_na_v5.py`
"""

import json
import os
import re
import sys
import unicodedata

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(ICI))  # -I n'ajoute pas le dossier du programme
sys.path.insert(0, ICI)

import liste_reelle_na_v5 as LR  # noqa: E402
from pole import garde_motifs_na_v4 as gm  # noqa: E402

donnees = gm.charger_donnees_ignorables(os.path.join(os.path.dirname(ICI), "pole", "ignorables-unicode-15.1.0-na-v1.json"),
                                        "8e15ad688fbb298ade214fe19986e103e4302f0e67d169b7201f730e416699f7")
n = gm.Normaliseur(donnees)
garde = gm.GardeMotifs(gm.charger_liste_motifs(os.path.join(ICI, "liste-motifs-essai-na-v1.json"),
                                               "41a50329f67c41d073115a75ae64981fd59a46b4663c269f42a32b4055c0508b", n))
formes = ["graine-factice", "graine_factice", "graine factice", "graine  factice",
          "grai️ne factice", "grai͏ne factice", "graiㅤne factice", "graine⠀factice"]

lignes = LR.lire_liste_reelle()  # empreinte vérifiée ; lève si la liste manque
mordus = 0
for ligne in lignes:
    motif = re.compile(n.normaliser_expression(ligne))
    nom = ligne[2:-2]
    mordus += all(motif.search(n.normaliser("x " + forme + " y")) is not None
                  for forme in (nom.upper(), nom.title(), "_" + nom + "_", "-" + nom.upper() + "-"))

print(json.dumps({
    "executable": sys.executable,
    "unicodedata": unicodedata.unidata_version,
    "regex_charge": "regex" in sys.modules,
    "points_ignorables": len(donnees.points),
    "refusees": [garde.examiner(f) is not None for f in formes],
    "saine_passe": garde.examiner("texte sain, avec trait-d'union et soulignement_") is None,
    "liste_reelle_motifs": len(lignes),
    "liste_reelle_motifs_mordus_dans_quatre_formes": mordus,
}, ensure_ascii=False, sort_keys=True))
