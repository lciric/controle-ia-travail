"""Compte des composantes certifiées (étiquette C8) par classe dans les 12 mondes de développement de la conception v4
(famille MR-2), lu dans les sorties scellées `sorties-v4/partie-v4-monde-{0…11}.json` ; lecture seule, aucun calcul de monde.
Usage : python3 -I compte_certifiees_mr2_v1.py DOSSIER_SORTIES_V4"""
import hashlib
import json
import os
import sys
from collections import Counter

d = sys.argv[1]
total = Counter()
for w in range(12):
    p = os.path.join(d, f"partie-v4-monde-{w}.json")
    sha = hashlib.sha256(open(p, "rb").read()).hexdigest()
    attendu = open(p + ".sha256", encoding="utf-8").read().split()[0]
    assert sha == attendu, f"empreinte différente : {p}"
    r = json.load(open(p, encoding="utf-8"))["resultat"]
    c = Counter(r["c8"][k]["classe"] for k in r["certifiees"])
    tous = Counter(v["classe"] for v in r["c8"].values())
    print(f"monde {w:2d} ({sha[:8]}) : certifiées {len(r['certifiees'])} {dict(sorted(c.items()))} ; toutes {dict(sorted(tous.items()))}")
    total += c
print("total des certifiées sur 12 mondes :", dict(sorted(total.items())))
