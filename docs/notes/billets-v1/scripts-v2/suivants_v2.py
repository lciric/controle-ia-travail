"""Prochains candidats à lire pour les bien notés d'une année : suivants_v2.py AN K."""
import sys, json
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from candidats_v2 import *
an, k = int(sys.argv[1]), int(sys.argv[2])
J = "/home/user/controle-ia-travail/docs/notes/billets-v1/journal-tri-v2.jsonl"
lus = {}
for l in open(J):
    l = json.loads(l)
    if l["role"] == "haut": lus[l["identifiant"]] = l["decision"]
oui = [i for i in lus if billets[i]["annee"] == an and lus[i] == "oui"]
rest = [p["_id"] for p in hauts(an) if p["_id"] not in lus]
print(len(oui), "oui ;", len(rest), "restants", file=sys.stderr)
print(" ".join(rest[:max(0, min(k, 15 - len(oui)))]))
