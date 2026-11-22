import json, sys, hashlib
from pathlib import Path
v10, v11 = Path(sys.argv[1]), Path(sys.argv[2])
def chemins(a, b, p=""):
    if type(a) != type(b):
        yield p, "type"; return
    if isinstance(a, dict):
        if list(a) != list(b): yield p, "clés"
        for k in a:
            if k in b: yield from chemins(a[k], b[k], f"{p}.{k}")
    elif isinstance(a, list):
        if len(a) != len(b): yield p, "longueur"
        for i, (x, y) in enumerate(zip(a, b)): yield from chemins(x, y, f"{p}[{i}]")
    elif a != b:
        yield p, "valeur"
f10 = sorted(x.relative_to(v10) for x in v10.rglob("*") if x.is_file() and not x.name.endswith(".sha256"))
f11 = sorted(x.relative_to(v11) for x in v11.rglob("*") if x.is_file() and not x.name.endswith(".sha256"))
print("mêmes fichiers :", f10 == f11, len(f10))
for f in f10:
    a, b = (v10 / f).read_text(), (v11 / f).read_text()
    if f.suffix == ".jsonl":
        print(f, "identique" if a == b else "DIFFÈRE", hashlib.sha256(a.encode()).hexdigest()[:12])
        continue
    d = list(chemins(json.loads(a), json.loads(b)))
    print(f, "écarts :", d)
