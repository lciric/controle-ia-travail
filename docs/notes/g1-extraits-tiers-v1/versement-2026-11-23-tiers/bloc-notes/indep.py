import json, hashlib, re
D="/home/user/controle-ia-travail/"
for nom in ["fiche-T07-sondes-v1.json","fiche-T07-etape-B-bis-v1.json"]:
    fi=json.load(open(D+"docs/notes/g1-extraits-tiers-v1/fiches/"+nom,encoding="utf-8"))
    print("==",nom,"clés:",sorted(fi))
    raw=open(D+fi["source"],"rb").read()
    print(" sha source", hashlib.sha256(raw).hexdigest()[:16], "attendu", fi["empreinte_attendue"])
    src=raw.decode().split("\n"); 
    if src[-1]=="": src=src[:-1]
    ext=open(D+fi["sortie"],encoding="utf-8").read().split("\n")
    # body after '---' separator line index
    i=ext.index("---")+2
    body=ext[i:]
    if body[-1]=="": body=body[:-1]
    P={}
    for p in fi["passages"]: P.setdefault(p["ligne"],[]).append((p["debut"],p["fin"]))
    # expected body
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
    print(" corps identique:", exp==body, len(body))
    # count markers in body vs passages
    n_mark=sum(l.count("[passage non repris]") for l in body)
    print(" marques:",n_mark,"passages:",len(fi["passages"]))
    # does the source itself contain the marker text anywhere?
    print(" marque présente dans la source:", any("[passage non repris]" in l for l in src), any("non reprises]" in l for l in src))
    # omitted lengths
    for p in fi["passages"]:
        print("  passage l.",p["ligne"],"longueur",p["fin"]-p["debut"])
    # fiche content: any strings beyond metadata?
    print(" titre/objet:", fi["titre"], "|", fi["objet"])
