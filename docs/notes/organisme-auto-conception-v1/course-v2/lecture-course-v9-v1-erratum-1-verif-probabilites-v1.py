import json, re, collections, sys
from math import comb
import numpy as np
R=sys.argv[1]
G=R+"/archives-reponses-modeles/auto-conception-course-v9-2026-11-19-v1/course-v9-sortie/sortie/generation-1"
f=json.load(open(G+"/fiches.json")); cl=json.load(open(G+"/classement.json"))
nb={l["ident"]:bool(l["notable"]) for l in cl["lignes"]}
def lot(x):
    m=re.match(r"Lot (\d+) sur 11",x["meta"]["case"][0]); return int(m.group(1))
ids=sorted(f); esp=[f[i]["meta"]["proposeur"] for i in ids]; cas=[lot(f[i]) for i in ids]; no=np.array([nb[i] for i in ids])
print("p case 6:",comb(67,6)/comb(94,6))
tailles=collections.Counter(cas); print(sorted(tailles.items()))
print("esperance:",sum(comb(67,k)/comb(94,k) for k in tailles.values()))
# par espece
ce=collections.Counter(esp); ne=collections.Counter(e for e,n in zip(esp,no) if n)
for e in sorted(ce): print(e,ce[e],ne[e],"p tout notable=%.2e"%(comb(67,ce[e])/comb(94,ce[e])))
print("conditionnel espece, case originalite:", comb(12,2)/comb(21,2)*comb(11,2)/comb(22,2))
ss=np.random.SeedSequence(2026111954); rng=np.random.default_rng(ss)
cas=np.array(cas); espa=np.array(esp); N=200000
def stat(perm_no):
    return any(perm_no[cas==c].all() for c in tailles)
a=b=0
idx_e={e:np.where(espa==e)[0] for e in ce}
for _ in range(N):
    p=rng.permutation(no); a+=stat(p)
    q=no.copy()
    for e,ix in idx_e.items(): q[ix]=rng.permutation(no[ix])
    b+=stat(q)
print("P(au moins une case toute notable) echange libre: %.4f ; dans l'espece: %.4f"%(a/N,b/N))
# juge par juge, par espece
v={}
import glob
for p in glob.glob(G+"/coffre/verdicts-passe1-*.json"):
    x=json.load(open(p)); v[x["ident"]]=x
for jg in ("juge-opus","juge-argon"):
    c=collections.Counter(f[i]["meta"]["proposeur"] for i in ids if v[i]["verdicts"][jg]["notable"]); print(jg,dict(sorted(c.items())))
print("cles d'un verdict:",sorted(v[ids[0]].keys()), sorted(v[ids[0]]["verdicts"]["juge-opus"].keys()))
print("cles meta:",sorted(f[ids[0]]["meta"].keys()))
# longueurs par espece (cartes, notes)
for e in sorted(ce):
    L=[len(json.dumps(f[i]["contenu"],ensure_ascii=False)) for i in ids if f[i]["meta"]["proposeur"]==e]
    Lo=[len(v[i]["verdicts"]["juge-opus"]["note"]) for i in ids if f[i]["meta"]["proposeur"]==e]
    La=[len(v[i]["verdicts"]["juge-argon"]["note"]) for i in ids if f[i]["meta"]["proposeur"]==e]
    print(e,"cartes",min(L),int(np.median(L)),max(L),"notes opus",min(Lo),int(np.median(Lo)),max(Lo),"notes argon",min(La),int(np.median(La)),max(La))
