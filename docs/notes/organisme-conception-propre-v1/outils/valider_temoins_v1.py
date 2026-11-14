"""Valide, sans appel, les témoins de la course « conception propre » avec le code réel de l'orchestrateur (clone en lecture) :
`charger_temoins` sur les 4 témoins de l'orchestrateur, `valider_fiche_ideation` et `signaux_niveau_methode` sur les 20
fiches de témoins. Usage : /usr/local/bin/python3 -I -B -X pycache_prefix=<dossier hors du clone> valider_temoins_v1.py ORCH DOSSIER
"""
import hashlib, json, os, sys
orch = sys.argv[1]; dossier = sys.argv[2]
sys.path.insert(0, orch)
from pole import ideation_v2 as idn
p = os.path.realpath(os.path.join(dossier, "temoins-organisme-conception-propre-v1.json"))
liste = {p: hashlib.sha256(open(p, "rb").read()).hexdigest()}
t = idn.charger_temoins(p, liste)
print("orchestrateur : charger_temoins OK,", len(t), "témoins, classes", sorted(x["temoin"]["classe"] for x in t))
for nom in ("temoins-lecteur-v1.json", "temoins-hasard-v1.json"):
    d = json.load(open(os.path.join(dossier, nom), encoding="utf-8"))
    for i, x in enumerate(d["temoins"], 1):
        f = idn.valider_fiche_ideation(x["fiche"], "temoin", i, passe=0)
        s = idn.signaux_niveau_methode(idn.vue_servie(f))
        print(nom, x["code"], "valide", "signaux:", s)
