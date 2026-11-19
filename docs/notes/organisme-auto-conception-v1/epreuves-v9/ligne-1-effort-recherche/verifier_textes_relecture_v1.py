#!/usr/bin/env python3
"""Vérifie que les textes des deux corrections du JSON sont tirés à l'octet de la relecture (agent de recopie, modèle L′).

Usage : python3 -B -I verifier_textes_relecture_v1.py RELECTURE ERRATUM_V1 JSON
Code 0 si tout concorde ; 1 sinon (motif imprimé).
"""
import json
import sys

relecture_p, erratum_p, json_p = sys.argv[1:4]
rel = open(relecture_p, encoding="utf-8").read().split("\n")
err = open(erratum_p, encoding="utf-8").read()
remp = json.load(open(json_p, encoding="utf-8"))
fautes = []

# Correction 1 : ligne « 1. ... Remplacer « X » par : » puis ligne «    « Y » »
i1 = next(i for i, l in enumerate(rel) if l.startswith("1. **§ 2, premier paragraphe.**"))
l1 = rel[i1]
debut, fin = "Remplacer « ", " » par :"
x1 = l1[l1.index(debut) + len(debut): l1.rindex(fin)]
y1l = rel[i1 + 1]
assert y1l.startswith("   « ") and y1l.endswith(" »"), y1l
y1 = y1l[len("   « "):-len(" »")]
renvoi = " (rectification R-3985)"
point = "ce sont ces quatre cellules"
y1_avec_renvoi = y1.replace(point, point + renvoi, 1)
if y1.count(point) != 1:
    fautes.append("correction 1 : point d'insertion du renvoi non unique")

# Correction 2 : ligne « 2. **Fin du § 3, ...** Ajouter le paragraphe : » puis ligne «    « Z » »
i2 = next(i for i, l in enumerate(rel) if l.startswith("2. **Fin du § 3, après la phrase citée.**"))
z2l = rel[i2 + 1]
assert z2l.startswith("   « ") and z2l.endswith(" »"), z2l
z2 = z2l[len("   « "):-len(" »")]

r_c1 = [r for r in remp if r["ancien"] == x1]
if len(r_c1) != 1:
    fautes.append(f"correction 1 : texte ancien de la relecture trouvé {len(r_c1)} fois dans le JSON")
elif r_c1[0]["neuf"] != y1_avec_renvoi:
    fautes.append("correction 1 : texte neuf différent du texte de la relecture (renvoi R-3985 inséré)")
if err.count(x1) != 1:
    fautes.append(f"correction 1 : texte ancien trouvé {err.count(x1)} fois dans l'erratum v1")

r_c2 = [r for r in remp if z2 in r["neuf"]]
if len(r_c2) != 1:
    fautes.append(f"correction 2 : paragraphe de la relecture trouvé dans {len(r_c2)} textes neufs")
else:
    r = r_c2[0]
    if r["neuf"] != r["ancien"] + "\n" + z2 + "\n":
        fautes.append("correction 2 : texte neuf ≠ phrase citée + ligne vide + paragraphe de la relecture")
    if not err.endswith(r["ancien"]):
        fautes.append("correction 2 : la phrase citée n'est pas la fin du § 3 (fin du fichier)")

print("x1 =", repr(x1))
print("y1 =", repr(y1))
print("z2 =", repr(z2))
for f in fautes:
    print("FAUTE :", f)
print("CONCORDE" if not fautes else "NE CONCORDE PAS")
sys.exit(1 if fautes else 0)
