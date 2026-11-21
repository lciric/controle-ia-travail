"""Cherche chaque nom de la liste réelle des noms refusés dans tous les fichiers du dossier v5 du lot 2, et rend des comptes
seulement : aucun nom n'est écrit ni affiché. La liste est lue par `liste_reelle_na_v5` (branche principale, empreinte
scellée). Deux recherches : la chaîne exacte (casse respectée), puis le mot entier sans égard à la casse (bornes `\\b`).

Usage : `python -B chercher_noms_dans_le_dossier_lot_2_v5.py`
"""

import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ICI, "paquet", "orchestrator", "essais"))

import liste_reelle_na_v5 as LR  # noqa: E402

noms = [l[2:-2] for l in LR.lire_liste_reelle()]
mots = [re.compile(r"\b" + re.escape(n) + r"\b", re.IGNORECASE) for n in noms]

fichiers, exacts, mots_entiers = 0, {}, {}
for racine, _dossiers, noms_fichiers in os.walk(ICI):
    for nom_fichier in sorted(noms_fichiers):
        chemin = os.path.join(racine, nom_fichier)
        rel = os.path.relpath(chemin, ICI)
        with open(chemin, "rb") as f:
            texte = f.read().decode("utf-8", errors="replace")
        fichiers += 1
        e = sum(texte.count(n) for n in noms)
        m = sum(len(r.findall(texte)) for r in mots)
        if e:
            exacts[rel] = e
        if m:
            mots_entiers[rel] = m

print(json.dumps({
    "noms_de_la_liste": len(noms),
    "fichiers_parcourus": fichiers,
    "fichiers_avec_un_nom_exact": len(exacts),
    "occurrences_exactes": sum(exacts.values()),
    "fichiers_avec_un_nom_mot_entier_sans_casse": len(mots_entiers),
    "occurrences_mot_entier_sans_casse": sum(mots_entiers.values()),
    "fichiers_touches_exacts": sorted(exacts),
    "fichiers_touches_mot_entier_sans_casse": sorted(mots_entiers),
}, ensure_ascii=False, sort_keys=True, indent=1))
