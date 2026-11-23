import json, os, sys, glob
rej, V2 = sys.argv[1], sys.argv[2]
ok = 0
for p in sorted(glob.glob(os.path.join(rej, "*.json"))):
    b = os.path.basename(p)
    src = [os.path.join(V2, "sorties", d, b) for d in ("reprises-v1", "neuves-v2") if os.path.exists(os.path.join(V2, "sorties", d, b))]
    a, o = json.load(open(p)), json.load(open(src[0]))
    da, do = a.pop("duree_s"), o.pop("duree_s")
    ident = a == o
    ok += ident
    cle = ("conj3_a", "conj3_b") if b.startswith("ab") else ("insertion_kP3_lie|conj3", "contenu_kP3_lie|conj3")
    print(("IDENTIQUE " if ident else "DIFFERENT ") + b, "origine", os.path.basename(os.path.dirname(src[0])), "| taux", [a["taux"][c] for c in cle], "| durees", da, do)
    if not ident:
        print("   cles differentes :", [k for k in o if a.get(k) != o[k]])
print(ok, "identiques sur", len(glob.glob(os.path.join(rej, "*.json"))))
