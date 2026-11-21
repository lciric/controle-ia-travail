"""Détaille, sans afficher aucun nom, les occurrences des noms de la liste réelle dans le dossier v5 : pour chaque rang de
motif qui a au moins une occurrence, la longueur du nom, s'il est fait de lettres seules, le nombre d'occurrences exactes et
mot entier, et les fichiers touchés. Sert à corriger le dossier sans lire les noms.

Usage : `python -B detailler_occurrences_par_rang_lot_2_v5.py`
"""

import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ICI, "paquet", "orchestrator", "essais"))

import liste_reelle_na_v5 as LR  # noqa: E402

noms = [l[2:-2] for l in LR.lire_liste_reelle()]
textes = {}
for racine, _d, fs in os.walk(ICI):
    for f in fs:
        chemin = os.path.join(racine, f)
        with open(chemin, "rb") as h:
            textes[os.path.relpath(chemin, ICI)] = h.read().decode("utf-8", errors="replace")

rendu = []
for rang, nom in enumerate(noms, start=1):
    mot = re.compile(r"\b" + re.escape(nom) + r"\b", re.IGNORECASE)
    par_fichier = {}
    for rel, t in textes.items():
        e, m = t.count(nom), len(mot.findall(t))
        if e or m:
            par_fichier[rel] = [e, m]
    if par_fichier:
        rendu.append({"rang": rang, "longueur": len(nom), "lettres_seules": nom.isalpha(),
                      "fichiers": par_fichier})
print(json.dumps(rendu, ensure_ascii=False, sort_keys=True, indent=1))
