"""Compare deux JSON en retirant toute clé « chemin » ou « fichier » (à toute profondeur). Rend aussi l'égalité octet.
Usage : comparer_json_hors_chemins_v1.py A.json B.json"""
import json, sys

def net(o):
    if isinstance(o, dict):
        return {k: net(v) for k, v in o.items() if k not in ("chemin", "fichier")}
    if isinstance(o, list):
        return [net(v) for v in o]
    return o

a, b = open(sys.argv[1], "rb").read(), open(sys.argv[2], "rb").read()
ja, jb = json.loads(a), json.loads(b)
print("octet :", a == b, "| hors chemins :", net(ja) == net(jb))
if net(ja) != net(jb) and isinstance(ja, dict):
    print("cles divergentes :", [k for k in set(ja) | set(jb) if net(ja.get(k)) != net(jb.get(k))])
