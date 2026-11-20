"""Contre-lecteur, modèle S : longueurs des onze témoins v2 selon deux mesures (forme JSON indentée ; somme des champs)."""
import hashlib
import json

CH = "/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/course-v2/temoins-juge-auto-conception-v2.json"
octets = open(CH, "rb").read()
assert hashlib.sha256(octets).hexdigest() == "84a1e0ea870ecb54c2de8ec5071e689e2ba409b3c97aecb57ab16ef3388439e0"
temoins = json.loads(octets.decode("utf-8"))["temoins"]
a = sorted(len(json.dumps(t["contenu"], ensure_ascii=False, indent=1)) for t in temoins)
b = sorted(sum(len(v) for v in t["contenu"].values()) for t in temoins)
print(json.dumps({"n": len(temoins), "json_indente": a, "somme_des_champs": b, "max_champ": max(len(v) for t in temoins for v in t["contenu"].values())}))
