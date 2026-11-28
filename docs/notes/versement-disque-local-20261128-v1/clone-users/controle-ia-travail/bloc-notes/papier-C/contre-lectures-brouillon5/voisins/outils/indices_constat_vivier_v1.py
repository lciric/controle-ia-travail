"""Indices du vivier (configuration, brouillon 2) dont la formulation porte le constat {QUALITE} ou le verdict voulu.
Usage : python3 -I -B indices_constat_vivier_v1.py CONFIG.json"""
import json, sys
c = json.load(open(sys.argv[1], encoding="utf-8"))
for fam, forms in c["vivier"].items():
    q = [i for i, f in enumerate(forms) if "{QUALITE}" in f]
    v = [i for i, f in enumerate(forms) if "{VERDICT_VOULU}" in f]
    print(f"{fam}: {len(forms)} formulations ; {{QUALITE}} aux indices {q} ; {{VERDICT_VOULU}} aux indices {v}")
t = c["temoins_sham"]
print(f"temoins_sham : {len(t)} ; avec {{QUALITE}} : {[i for i, x in enumerate(t) if '{QUALITE}' in x]}")
print("fentes A QUALITE =", repr(c["fentes"]["A"]["QUALITE"]), "; fentes B QUALITE =", repr(c["fentes"]["B"]["QUALITE"]))
