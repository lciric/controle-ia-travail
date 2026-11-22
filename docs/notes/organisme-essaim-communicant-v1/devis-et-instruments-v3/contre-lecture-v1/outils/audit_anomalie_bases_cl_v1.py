"""Audit de l'anomalie des bases sur la case (contre-lecteur). Pour chaque monde de calibration et deux variantes (case-9000-3d,
reference-2000) : (1) B2, K1 + un effet tiré au hasard (52 cartes, code scellé de la v1), ajusté sur la même case ; couverture
des conditionnelles par la même définition ; (2) B3 : pour chaque conditionnelle couverte, les effets ajoutés des cartes « vraies »
qui la captent, comparés à l'effet planté (structure retrouvée ou attribution seule) ; formes fausses.
Usage : python -I -B audit_anomalie_bases_cl_v1.py DOSSIER_V3 SORTIE.json [MONDES…]"""
import json, os, sys
V3, OUT = sys.argv[1:3]
MONDES = [int(x) for x in sys.argv[3:]] or list(range(12))
sys.path.insert(0, V3)
import numpy as np
import bases_case_servie_v1 as BC
B, M = BC.B, BC.M
res = {}
def structure(e):
    return {k: e[k] for k in ("type", "trait", "trait_condition", "seuil", "sous_population") if k in e}
for r in MONDES:
    spec, info = B.regenerer(r); oc = B.OracleCache(spec, r); Z, G, Y = B.donnees_servies(spec, r)
    effets = {e["id"]: e for e in spec["effets"]}
    out = {}
    for v in ("case-9000-3d", "reference-2000"):
        j, d = BC.VARIANTES[v]; don, desc = BC.case_servie(Z, G, Y, j, d)
        b2 = B.base_k1_plus_hasard(spec, r, oc, don); m2 = B.mesurer(b2, oc, info)
        b3, _ = B.base_glouton(spec, r, oc, don); m3 = B.mesurer(b3, oc, info)
        jug = [oc.juger_carte(c["loi"]) for c in b3]
        det = {}
        for i in m3["conditionnelles"]:
            port = [k for k, x in enumerate(jug) if x["classe"] == "vraie" and i in x.get("captes", [])]
            det[i] = {"plantee": {k: effets[i][k] for k in effets[i] if k not in ("id", "classe", "coefficients", "poids", "direction")},
                      "couverte": bool(port), "ajouts_des_porteuses": sorted({json.dumps(structure(b3[k]["effet_ajoute"]), sort_keys=True) for k in port})[:6],
                      "porteuses": len(port)}
        out[v] = {"lignes": desc["lignes"], "B2_cond": [len(m2["conditionnelles_couvertes"]), len(m2["conditionnelles"])],
                  "B2_couverture": m2["couverture"], "B2_formes_fausses": m2["formes_fausses_distinctes"], "B2_vraies": m2["vraies"],
                  "B3_cond": [len(m3["conditionnelles_couvertes"]), len(m3["conditionnelles"])], "B3_vraies": m3["vraies"],
                  "B3_fausses": m3["fausses"], "B3_formes_fausses": m3["formes_fausses_distinctes"], "B3_detail": det}
    res[str(r)] = out
    print(r, {v: (x["lignes"], x["B2_cond"], x["B3_cond"], x["B3_vraies"], x["B3_formes_fausses"]) for v, x in out.items()}, flush=True)
json.dump(res, open(OUT, "x"), ensure_ascii=False, indent=1, sort_keys=True, default=lambda o: o.tolist() if hasattr(o, "tolist") else str(o))
