"""Valide, sans appel, les témoins v2 (lecteur et hasard) avec le code réel de l'orchestrateur (clone en lecture, jamais
modifié) : `valider_fiche_ideation` et `signaux_niveau_methode` (garde lexicale « niveau méthode ») sur chaque fiche.
Reprise de `../../outils/valider_temoins_v1.py` (sans le chargement des 4 témoins du juge, sans objet ici).
Usage : /usr/local/bin/python3 -I -B -X pycache_prefix=<dossier hors du clone> valider_temoins_orchestrateur_v2.py ORCH DOSSIER
"""
import json, os, sys
orch, dossier = sys.argv[1], sys.argv[2]
sys.path.insert(0, orch)
from pole import ideation_v2 as idn
mauvais = 0
for nom in ("temoins-lecteur-v2.json", "temoins-hasard-v2.json"):
    d = json.load(open(os.path.join(dossier, nom), encoding="utf-8"))
    for i, x in enumerate(d["temoins"], 1):
        f = idn.valider_fiche_ideation(x["fiche"], "temoin", i, passe=0)
        s = idn.signaux_niveau_methode(idn.vue_servie(f))
        mauvais += bool(s)
        print(nom, x["code"], "valide", "signaux:", s)
print("fiches avec signal :", mauvais)
sys.exit(1 if mauvais else 0)
