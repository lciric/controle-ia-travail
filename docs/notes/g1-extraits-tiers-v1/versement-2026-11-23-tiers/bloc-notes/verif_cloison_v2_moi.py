import sys, json, hashlib, importlib.util
sys.dont_write_bytecode = True
D="/home/user/controle-ia-travail/"
print("outil", hashlib.sha256(open(D+"docs/notes/g1-extraits-tiers-v1/outils/extraire_v4.py","rb").read()).hexdigest()[:16])
spec = importlib.util.spec_from_file_location("ex", D+"docs/notes/g1-extraits-tiers-v1/outils/extraire_v4.py")
ex = importlib.util.module_from_spec(spec); spec.loader.exec_module(ex)
for nom in ["fiche-T07-sondes-v2.json","fiche-T07-etape-B-bis-v2.json"]:
    chemin=f"docs/notes/g1-extraits-tiers-v1/fiches/{nom}"
    fi=json.load(open(D+chemin,encoding="utf-8"))
    print("==",nom,"clés:",sorted(fi), "passages clés:", {tuple(sorted(p)) for p in fi["passages"]})
    texte=ex.fabriquer(fi,chemin)
    disque=open(D+fi["sortie"],"rb").read()
    print(" régénération identique:", texte.encode()==disque)
    raw=open(D+fi["source"],"rb").read(); src=raw.decode().split("\n")
    if src[-1]=="": src=src[:-1]
    ext=disque.decode().split("\n"); i=ext.index("---")+2; body=ext[i:]
    if body[-1]=="": body=body[:-1]
    P={}
    for p in fi["passages"]: P.setdefault(p["ligne"],[]).append((p["debut"],p["fin"]))
    exp=[];prev=0
    for a,b in sorted(map(tuple,fi["plages"])):
        if a>prev+1: exp.append(f"[lignes {prev+1} à {a-1} non reprises]")
        exp.append(f"<!-- lignes {a} à {b} de la source -->")
        for k in range(a,b+1):
            l=src[k-1]
            for d,f in sorted(P.get(k,[]),reverse=True): l=l[:d]+"[passage non repris]"+l[f:]
            exp.append(l)
        prev=b
    if prev<len(src): exp.append(f"[lignes {prev+1} à {len(src)} non reprises]")
    print(" corps identique (reconstruction indépendante):", exp==body, "lignes gardées:", sum(b-a+1 for a,b in fi["plages"]))
    print(" marques:", sum(l.count("[passage non repris]") for l in body), "passages:", len(fi["passages"]))
    for k in sorted(P):
        for d,f in sorted(P[k]):
            l=src[k-1]
            print(f"  l.{k} [{d}:{f}] avant={l[max(0,d-50):d]!r}")
            print(f"      OMIS={l[d:f]!r}")
            print(f"      après={l[f:f+50]!r}")
