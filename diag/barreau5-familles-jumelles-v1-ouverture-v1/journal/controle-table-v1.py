"""Contrôle de la table déposée par Lazar, sans rien afficher d'elle : cohérence (engagement_v1), empreinte canonique
égale à ENGAGEMENT-B5F, sel du fichier égal au sel de chaque ligne, graphies des familles (comptes seulement).
Usage : PYTHONPATH=<racine>/src python controle-table-v1.py TABLE SEL"""
import json, re, sys
from controle_ia.barreau5_familles import engagement_v1 as en

ENGAGEMENT = "553cb3950d5996213185760b6bf109b30b885af89060b1d1758e4b6d349fbddf"
table = json.loads(open(sys.argv[1], encoding="utf-8").read())
sel = open(sys.argv[2], encoding="utf-8").read().rstrip("\n")
en.exiger_table_coherente(table)
print("cohérence : ok")
print("empreinte canonique égale à l'engagement :", en.empreinte_table(table) == ENGAGEMENT)
print("sel du fichier égal au sel de chaque ligne :", all(x.get("sel") == sel for x in table))
print("lignes :", len(table))
fam = sorted({x["famille"] for x in table})
nues = [f for f in fam if re.fullmatch(r"T(0[1-9]|10)", f)]
print("familles :", len(fam), "; nues :", len(nues), "; suffixées :", len(fam) - len(nues))
print("membres par famille :", sorted({sum(1 for x in table if x["famille"] == f) for f in fam}))
