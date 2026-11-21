"""Donne, sans afficher aucun nom, les numéros de ligne où un nom de la liste réelle paraît comme mot entier (sans égard à
la casse) dans les fichiers du dossier v5, pour les rangs donnés en arguments. Le fichier de la source Unicode est exclu.

Usage : `python -B localiser_rangs_lot_2_v5.py RANG [RANG…]`
"""

import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ICI, "paquet", "orchestrator", "essais"))

import liste_reelle_na_v5 as LR  # noqa: E402

noms = [l[2:-2] for l in LR.lire_liste_reelle()]
rendu = {}
for rang in (int(a) for a in sys.argv[1:]):
    mot = re.compile(r"\b" + re.escape(noms[rang - 1]) + r"\b", re.IGNORECASE)
    for racine, _d, fs in os.walk(ICI):
        for f in fs:
            chemin = os.path.join(racine, f)
            rel = os.path.relpath(chemin, ICI)
            if "source-unicode" in rel:
                continue
            with open(chemin, "rb") as h:
                lignes = h.read().decode("utf-8", errors="replace").split("\n")
            n = [i for i, l in enumerate(lignes, start=1) if mot.search(l)]
            if n:
                rendu.setdefault(str(rang), {})[rel] = n[:40]
print(json.dumps(rendu, ensure_ascii=False, sort_keys=True, indent=1))
