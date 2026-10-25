"""Contre-lecture de la v5 — c2b : famille conscience d'évaluation, plus proche voisin du train (indice de Jaccard sur
les mots) ; exactitude équilibrée par part et par tranche de ressemblance ; mêmes chiffres pour la v3 (même famille).
Aucun texte ni identifiant imprimé. Usage : python3 -I -B c2b_conscience_voisins_v1.py DOSSIER SORTIE"""
import json, pathlib, re, sys
import numpy as np
D = pathlib.Path(sys.argv[1]); SORTIE = pathlib.Path(sys.argv[2])
FAM = "conscience-evaluation"; mots = lambda t: set(re.findall(r"[a-zà-ÿ0-9_]{2,}", t.lower()))
jac = lambda a, b: len(a & b) / max(1, len(a | b))
def ee(pred, vrai):
    pred, vrai = np.array(pred), np.array(vrai); pos = vrai == "evaluation"
    return round(float(((pred == vrai)[pos].mean() + (pred == vrai)[~pos].mean()) / 2), 4) if pos.any() and (~pos).any() else None
r = {}
for nom in ("banque-confrontation-v5.json", "banque-confrontation-v3.json"):
    b = json.loads((D / nom).read_text(encoding="utf-8")); tr = [t for t in b["train"] if t["famille"] == FAM]; Mtr = [mots(t["texte"]) for t in tr]
    out = {}
    for p in ("test", "test_final"):
        te = [t for t in b[p] if t["famille"] == FAM]; best, pred = [], []
        for t in te:
            js = [jac(mots(t["texte"]), m) for m in Mtr]; j = int(np.argmax(js)); best.append(js[j]); pred.append(tr[j]["verite"])
        vrai = [t["verite"] for t in te]; best = np.array(best)
        out[p] = {"n": len(te), "ee_plus_proche_voisin": ee(pred, vrai),
                  "ressemblance_max_quantiles": [round(float(x), 3) for x in np.quantile(best, [0, .25, .5, .75, 1])],
                  "n_ressemblance_ge_0_5": int((best >= .5).sum()),
                  "exactitude_si_ge_0_5": round(float(np.mean([pred[i] == vrai[i] for i in range(len(te)) if best[i] >= .5])), 4) if (best >= .5).any() else None,
                  "exactitude_si_lt_0_5": round(float(np.mean([pred[i] == vrai[i] for i in range(len(te)) if best[i] < .5])), 4),
                  "n_ge_0_5_par_classe": {c: int(sum(1 for i in range(len(te)) if best[i] >= .5 and vrai[i] == c)) for c in ("evaluation", "usage-reel")}}
    r[nom] = out
SORTIE.write_text(json.dumps(r, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps(r, ensure_ascii=False, indent=1))
