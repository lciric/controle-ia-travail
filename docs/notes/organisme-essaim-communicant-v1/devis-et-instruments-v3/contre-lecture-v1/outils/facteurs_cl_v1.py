"""Recalcul indépendant des facteurs R4 (pire v3 / pire v1) et R5 (leviers), lus dans les sorties versées.
Usage : python -B facteurs_cl_v1.py RACINE"""
import json, os, sys, hashlib
R = sys.argv[1]; N = os.path.join(R, "docs/notes/organisme-essaim-communicant-v1")
def lj(p):
    b = open(p, "rb").read(); return json.loads(b), hashlib.sha256(b).hexdigest()
v1, s1 = lj(f"{N}/devis-et-instruments-v1/calcul-devis-essaim-v1.json")
v3, s3 = lj(f"{N}/devis-et-instruments-v3/calcul-devis-essaim-v3.json")
r = {}
for v in v3["resume_usd"]:
    for e in v3["resume_usd"][v]:
        r[f"{e}|{v}"] = round(v3["resume_usd"][v][e]["pire"] / v1["resume_usd"][v][e]["pire"], 3)
print("R4 sha v1", s1[:8], "v3", s3[:8], "min", min(r.values()), "max", max(r.values()),
      "kimi", sorted(x for k, x in r.items() if k.startswith("kimi")))
ecarts = {k: (x, v3["rapport_pire_v3_sur_pire_v1"]["par_cellule"][k]) for k, x in r.items() if x != v3["rapport_pire_v3_sur_pire_v1"]["par_cellule"][k]}
print("R4 écarts avec le champ du script :", ecarts)
cr, sc = lj(f"{N}/devis-et-instruments-v3/calcul-devis-cout-reduit-v2.json")
print("R5 sha", sc[:8], "clés", list(cr.keys()))
json.dump({"R4": r}, sys.stdout if False else open(os.devnull, "w"))
