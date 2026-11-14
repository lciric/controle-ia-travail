"""Valide, sans appel, des fichiers de témoins avec le code réel de l'orchestrateur (clone en lecture, jamais modifié) :
`valider_fiche_ideation` et `signaux_niveau_methode` sur chaque fiche. v2.1 = v2 (`valider_temoins_orchestrateur_v2.py`,
`913e2a38…`) avec les fichiers donnés en arguments (témoins du lecteur v2 et hasard v2.1).
Usage : /usr/local/bin/python3 -I -B -X pycache_prefix=<hors du clone> valider_temoins_orchestrateur_v2_1.py ORCH FICHIER…
"""
import json, os, sys
orch, fichiers = sys.argv[1], sys.argv[2:]
sys.path.insert(0, orch)
from pole import ideation_v2 as idn
mauvais = 0
for chemin in fichiers:
    d = json.load(open(chemin, encoding="utf-8"))
    for i, x in enumerate(d["temoins"], 1):
        f = idn.valider_fiche_ideation(x["fiche"], "temoin", i, passe=0)
        s = idn.signaux_niveau_methode(idn.vue_servie(f))
        mauvais += bool(s)
        print(os.path.basename(chemin), x["code"], "valide", "signaux:", s)
print("fiches avec signal :", mauvais)
sys.exit(1 if mauvais else 0)
