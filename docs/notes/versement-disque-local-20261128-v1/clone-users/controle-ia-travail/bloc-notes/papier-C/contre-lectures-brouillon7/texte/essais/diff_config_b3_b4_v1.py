"""Compare la configuration brouillon 3 et brouillon 4 du papier C, par chemins, types, longueurs et empreintes ;
n'affiche aucune valeur textuelle — v1. Usage : python3 -B -I diff_config_b3_b4_v1.py B3 B4"""
import sys, json, hashlib
def plat(o, p="$"):
    if isinstance(o, dict):
        for k, v in o.items():
            yield from plat(v, f"{p}.{k}")
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from plat(v, f"{p}[{i}]")
    else:
        yield p, o
def h(v):
    return hashlib.sha256(json.dumps(v, ensure_ascii=False, sort_keys=True).encode()).hexdigest()[:12]
a = json.load(open(sys.argv[1], encoding="utf-8")); b = json.load(open(sys.argv[2], encoding="utf-8"))
A = dict(plat(a)); B = dict(plat(b))
print("clés de tête b3 :", list(a)); print("clés de tête b4 :", list(b))
for k in a:
    if k in b:
        print(f"{k:28s} égal : {h(a[k]) == h(b[k])}")
print("--- chemins retirés :", [p for p in A if p not in B])
print("--- chemins ajoutés :", [p for p in B if p not in A])
print("--- chemins changés (longueur b3 -> b4) :")
for p in A:
    if p in B and A[p] != B[p]:
        la = len(str(A[p])); lb = len(str(B[p]))
        print(f"  {p} : {la} -> {lb}")
