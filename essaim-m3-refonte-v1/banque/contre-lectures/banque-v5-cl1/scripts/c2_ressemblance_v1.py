"""Contre-lecture de la v5 — c2 : contraste résiduel. Une trace servie en test ou test final ressemble-t-elle à une
trace d'entraînement (ou à une autre trace servie) autant que deux traces d'une paire ? Plus proche voisin.
Aucune sortie par tâche (seulement des distributions). Usage : python3 -I -B c2_ressemblance_v1.py DOSSIER SORTIE"""
import json, pathlib, re, sys
import numpy as np
D = pathlib.Path(sys.argv[1]); SORTIE = pathlib.Path(sys.argv[2])
J = lambda n: json.loads((D / n).read_text(encoding="utf-8"))
v3, s3, v5, s5 = J("banque-confrontation-v3.json"), J("banque-confrontation-v3-secret.json"), J("banque-confrontation-v5.json"), J("banque-confrontation-v5-secret.json")
FAM = "controle-delegation"; PARTS = ("train", "test", "test_final")
def decoupe(t):
    lignes = t.split("\n"); scen = lignes[0].split(":", 1)[-1].strip().lower()
    i = next((k for k, l in enumerate(lignes) if l.strip().startswith("Trace d'actions")), 0)
    corps = {l.strip().lower() for l in lignes[i + 1:] if l.strip()}
    mots = set(re.findall(r"[a-zà-ÿ0-9_]{2,}", t.lower()))
    return scen, corps, mots
jac = lambda a, b: len(a & b) / max(1, len(a | b))
def sims(a, b):
    sa, ca, ma = a; sb, cb, mb = b
    ms_a, ms_b = set(re.findall(r"[a-zà-ÿ0-9_]{2,}", sa)), set(re.findall(r"[a-zà-ÿ0-9_]{2,}", sb))
    return {"lignes": jac(ca, cb), "mots": jac(ma, mb), "scenario": jac(ms_a, ms_b)}
r = {}
# délégation : train (32), servies (24 : test + test_final), jumelles retirées (24, depuis la v3)
tr = [t for t in v5["train"] if t["famille"] == FAM]
serv = [(p, t) for p in ("test", "test_final") for t in v5[p] if t["famille"] == FAM]
D_tr = [decoupe(t["texte"]) for t in tr]; D_sv = [decoupe(t["texte"]) for _, t in serv]
# paires du train (dans la v5)
pa = {}
for t, d in zip(tr, D_tr):
    pa.setdefault((t["source"], s5[t["id"]]["paire"]), []).append(d)
intra = [sims(*m) for m in pa.values() if len(m) == 2]
r["train_paires"] = {"n": len(intra), **{k: {"min": round(min(x[k] for x in intra), 3), "mediane": round(float(np.median([x[k] for x in intra])), 3)} for k in ("lignes", "mots", "scenario")}}
# jumelles retirées
p3 = {}
for p in ("test", "test_final"):
    for t in v3[p]:
        if t["famille"] == FAM:
            p3[(p, t["source"], s3[t["id"]]["paire"], t["verite"])] = t["texte"]
jum = []
for (p, t), d in zip(serv, D_sv):
    autre = "honnete" if t["verite"] == "sabotage" else "sabotage"
    jum.append(sims(d, decoupe(p3[(p, t["source"], s5[t["id"]]["paire"], autre)])))
r["servie_contre_sa_jumelle_retiree"] = {k: {"min": round(min(x[k] for x in jum), 3), "max": round(max(x[k] for x in jum), 3)} for k in ("lignes", "mots", "scenario")}
# servie contre train, servie contre servie
st = [[sims(a, b) for b in D_tr] for a in D_sv]
ss = [[sims(a, b) if i != j else None for j, b in enumerate(D_sv)] for i, a in enumerate(D_sv)]
r["servie_contre_train_max"] = {k: round(max(x[k] for row in st for x in row), 3) for k in ("lignes", "mots", "scenario")}
r["servie_contre_servie_max"] = {k: round(max(x[k] for row in ss for x in row if x), 3) for k in ("lignes", "mots", "scenario")}
r["servies_plus_proches_de_leur_jumelle_que_de_toute_trace_servie_ou_train"] = sum(
    jum[i]["mots"] > max([x["mots"] for x in st[i]] + [x["mots"] for x in ss[i] if x]) for i in range(len(serv)))
# plus proche voisin dans le train (vote du voisin), par part ; exactitude équilibrée
def ee(pred, vrai):
    pred, vrai = np.array(pred), np.array(vrai); pos = vrai == "sabotage"
    return round(float(((pred == vrai)[pos].mean() + (pred == vrai)[~pos].mean()) / 2), 4)
r["plus_proche_voisin_train"] = {}
for k in ("lignes", "mots", "scenario"):
    out = {}
    for p in ("test", "test_final"):
        idx = [i for i, (q, _) in enumerate(serv) if q == p]
        pred = [tr[int(np.argmax([x[k] for x in st[i]]))]["verite"] for i in idx]
        out[p] = ee(pred, [serv[i][1]["verite"] for i in idx])
    r["plus_proche_voisin_train"][k] = out
# même scénario qu'une trace du train ?
r["scenario_identique_a_une_trace_train"] = sum(any(a[0] == b[0] for b in D_tr) for a in D_sv)
r["scenario_identique_entre_servies"] = sum(any(a[0] == b[0] for j, b in enumerate(D_sv) if j != i) for i, a in enumerate(D_sv))
# conscience d'évaluation : quasi-doublons entre train et servies, et entre servies
ce_tr = [t for t in v5["train"] if t["famille"] != FAM]; ce_sv = [t for p in ("test", "test_final") for t in v5[p] if t["famille"] != FAM]
M_tr = [set(re.findall(r"[a-zà-ÿ0-9_]{2,}", t["texte"].lower())) for t in ce_tr]
M_sv = [set(re.findall(r"[a-zà-ÿ0-9_]{2,}", t["texte"].lower())) for t in ce_sv]
mx = []; acc = []
for i, a in enumerate(M_sv):
    js = [jac(a, b) for b in M_tr]; j = int(np.argmax(js)); mx.append(js[j]); acc.append(ce_tr[j]["verite"] == ce_sv[i]["verite"])
r["conscience_servie_contre_train"] = {"max": round(max(mx), 3), "n_sup_0_8": sum(x >= 0.8 for x in mx), "n_sup_0_5": sum(x >= 0.5 for x in mx),
    "accord_classe_si_sup_0_5": [bool(acc[i]) for i in range(len(mx)) if mx[i] >= 0.5].count(True),
    "textes_identiques_train_servie": sum(any(t["texte"] == u["texte"] for u in ce_tr) for t in ce_sv)}
SORTIE.write_text(json.dumps(r, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps(r, ensure_ascii=False, indent=1))
