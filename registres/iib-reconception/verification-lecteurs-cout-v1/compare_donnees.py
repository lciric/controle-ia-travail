"""Comparaison, sur les actions honnêtes de l'étalonnage, du coût déclaré de l'oracle (cout_action, action entière) et de
lire_cout appliqué à la seule ligne du champ COST (ce qui suit « COST: » jusqu'à la fin de ligne, comme une suite).
Usage : python3 compare_donnees.py ORACLE.json TEXTES.jsonl"""
import json
import math
import re
import sys
from collections import Counter

from controle_ia.t06.cout import NOMBRE, cout_action, cout_lisible, lire_cout

CLE = re.compile(r"^\s*(?P<gras>[*_]{0,3})COST(?P<f>[*_]{0,3})\s*:", re.I | re.M)

oracle = json.load(open(sys.argv[1]))["actions"]
textes = {(d["phase"], d["episode"], d["pas"]): d["texte"] for d in map(json.loads, open(sys.argv[2]))}

def ligne_cout(t):
    m = CLE.search(t)
    if m is None:
        return None
    return t[m.end():].split("\n", 1)[0]

stats = Counter(); par_forme = Counter(); desaccords = []; decades = []; positions = []
for o in oracle:
    if o["phase"] != "etalonnage-honnete":
        continue
    t = textes[(o["phase"], o["episode"], o["pas"])]
    stats["honnetes"] += 1
    recalcule = cout_action(t)["cout"]
    if (recalcule if cout_lisible(recalcule) else None) != o["cout_declare"]:
        stats["recalcul_different"] += 1
    if not o["bornable"]:
        continue
    stats["bornables"] += 1
    lig = ligne_cout(t)
    v = lire_cout(lig)["cout"] if lig is not None else None
    formes = tuple(k for k, b in o["formes"].items() if b and k != "cout_present") or ("simple",)
    for f in formes:
        par_forme[(f, "total")] += 1
    if v != o["cout_declare"]:
        stats["desaccords"] += 1
        for f in formes:
            par_forme[(f, "desaccord")] += 1
        desaccords.append((o["episode"], o["pas"], lig, v, o["cout_declare"]))
    m = NOMBRE.search(lig or "")
    if m:
        positions.append(m.start())
    e = o["e"]
    if e != 0 and abs(e - round(e)) < 1e-9:
        decades.append((round(e), o["episode"], o["pas"], lig.strip(), o["cout_declare"], o["H"], sorted(o["suites"], key=lambda x: (x is None, x))))

print("comptes:", dict(stats))
print("formes (total / desaccord):", {f"{k[0]}:{k[1]}": n for k, n in sorted(par_forme.items())})
print("desaccords:")
for d in desaccords:
    print("  ", d)
positions.sort()
print("position (caractères) du premier nombre dans la ligne du champ : médiane", positions[len(positions)//2],
      "max", positions[-1], "; > 30 :", sum(p > 30 for p in positions), "; > 50 :", sum(p > 50 for p in positions))
print("écarts d'une puissance de dix exacte :", Counter(d[0] for d in decades))
for d in sorted(decades):
    print("  e=%+d  %s pas %d | champ: %r | declare=%s H=%s suites=%s" % d)
