"""Imprime les seuls champs nommés d'un JSON (objet, ou liste d'objets) : python -I lire_champ.py FICHIER champ1 champ2 ..."""
import json, sys
d = json.load(open(sys.argv[1], encoding="utf-8"))
d = d.get("instances", d) if isinstance(d, dict) and "instances" in d else d
for x in (d if isinstance(d, list) else [d]):
    print({k: x.get(k) for k in sys.argv[2:]})
