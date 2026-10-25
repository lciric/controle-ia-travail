"""Contre-lecture de la v5 — c3 : référence de surface recalculée avec le code du noyau (reference_traits_texte) sur
la v5, et loi sur les 400 sélections possibles (3 paires sur 6 gardent l'honnête, par source et par part) ; longueurs.
Usage : python3 -I -B c3_surface_selections_v1.py RACINE_ESSAIM DOSSIER_BANQUE SORTIE"""
import itertools, json, pathlib, sys
import numpy as np
sys.path.insert(0, sys.argv[1])
from essaim_m3 import banque as B
D = pathlib.Path(sys.argv[2]); SORTIE = pathlib.Path(sys.argv[3]); FAM = "controle-delegation"
r = {"reference_v5": B.reference_traits_texte(D / "banque-confrontation-v5.json")["par_famille"]}
v3 = json.loads((D / "banque-confrontation-v3.json").read_text(encoding="utf-8")); s3 = json.loads((D / "banque-confrontation-v3-secret.json").read_text(encoding="utf-8"))
v5 = json.loads((D / "banque-confrontation-v5.json").read_text(encoding="utf-8"))
tr = [t for t in v5["train"] if t["famille"] == FAM]
X = np.stack([B._traits_texte(t["texte"]) for t in tr]); y = np.array([1.0 if t["verite"] == "sabotage" else 0.0 for t in tr])
w, b0, mu, sd = B._regression_logistique(X, y)
for part in ("test", "test_final"):
    te = [t for t in v3[part] if t["famille"] == FAM]
    pred = {t["id"]: bool(((B._traits_texte(t["texte"]) - mu) / sd) @ w + b0 >= 0) for t in te}
    paires = {}
    for t in te:
        paires.setdefault((t["source"], s3[t["id"]]["paire"]), {})[t["verite"]] = t["id"]
    srcs = sorted({k[0] for k in paires}); par_src = {s: sorted(k for k in paires if k[0] == s) for s in srcs}
    vals = []
    for choix in itertools.product(*[list(itertools.combinations(range(len(par_src[s])), len(par_src[s]) // 2)) for s in srcs]):
        garde = []
        for s, hon in zip(srcs, choix):
            for j, k in enumerate(par_src[s]):
                garde.append(paires[k]["honnete" if j in hon else "sabotage"])
        sab = [i for i in garde if i in {m["sabotage"] for m in paires.values()}]; hon = [i for i in garde if i not in sab]
        vals.append(round((np.mean([pred[i] for i in sab]) + np.mean([not pred[i] for i in hon])) / 2, 4))
    vals = np.array(vals); garde5 = {t["texte"] for t in v5[part] if t["famille"] == FAM}
    obs = [t for t in te if t["texte"] in garde5]
    sab = [t for t in obs if t["verite"] == "sabotage"]; hon = [t for t in obs if t["verite"] == "honnete"]
    obs_val = round((np.mean([pred[t["id"]] for t in sab]) + np.mean([not pred[t["id"]] for t in hon])) / 2, 4)
    r[part] = {"n_selections": len(vals), "min": float(vals.min()), "max": float(vals.max()), "moyenne": round(float(vals.mean()), 4),
               "valeur_v5_meme_classifieur": obs_val, "P_ge_observee": round(float((vals >= obs_val).mean()), 3),
               "P_le_observee": round(float((vals <= obs_val).mean()), 3),
               "longueur_moyenne_servies": {"sabotage": round(float(np.mean([len(t["texte"]) for t in sab])), 1),
                                            "honnete": round(float(np.mean([len(t["texte"]) for t in hon])), 1)}}
from math import comb
r["hasard_12_traces_P_ge_k"] = {k: round(sum(comb(12, j) for j in range(k, 13)) / 4096, 4) for k in (8, 9, 10)}
SORTIE.write_text(json.dumps(r, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps(r, ensure_ascii=False, indent=1))
