import json, subprocess, sys, re
D="/home/user/controle-ia-travail"
M="[passage non repris]"
def src(f):
    if f.get("ref"):
        b=subprocess.run(["git","show",f"{f['ref']}:{f['source']}"],capture_output=True,cwd=D,check=True).stdout
    else: b=open(D+"/"+f["source"],"rb").read()
    L=b.decode().split("\n")
    if L[-1]=="": L=L[:-1]
    return L
for nom in sys.argv[1:]:
    f=json.load(open(D+"/docs/notes/g1-extraits-tiers-v1/fiches/"+nom))
    S=src(f)
    E=open(D+"/"+f["sortie"],encoding="utf-8").read().split("\n")
    # locate body
    i=E.index("---")+2
    bad=0; kept=[]; gaps=[]
    cur=None
    while i<len(E):
        e=E[i]
        m=re.fullmatch(r"<!-- lignes (\d+) à (\d+) de la source -->",e)
        g=re.fullmatch(r"\[lignes (\d+) à (\d+) non reprises\]",e)
        if m:
            a,b=int(m[1]),int(m[2])
            for k in range(a,b+1):
                i+=1; e=E[i]; s=S[k-1]
                if M not in e:
                    if e!=s: bad+=1; print("DIFF",k)
                else:
                    parts=e.split(M); pos=0; found=[]
                    if not s.startswith(parts[0]): bad+=1; print("DEBUT",k)
                    pos=len(parts[0])
                    for p in parts[1:]:
                        # next part: find occurrence after pos (gap>0)
                        if p=="" : j=len(s)
                        else:
                            j=s.find(p,pos+1)
                            # choose occurrence such that remaining works: take last valid if final
                            if p is parts[-1]: j=len(s)-len(p) if s.endswith(p) else -1
                        if j<0: bad+=1; print("PART",k); break
                        found.append((pos,j)); pos=j+len(p)
                    if pos!=len(s): bad+=1; print("FIN",k)
                    gaps+= [(k,a_,b_) for a_,b_ in found]
                kept.append(k)
            i+=1; continue
        if g:
            i+=1; continue
        break
    exp=sorted((p["ligne"],p["debut"],p["fin"]) for p in f["passages"])
    print(nom, "lignes gardées", len(kept), "écarts", bad, "passages trouvés=fiche:", sorted(gaps)==exp)
    if sorted(gaps)!=exp: print(sorted(gaps)); print(exp)
    print("  reste après corps:", repr(E[i][:80]) if i<len(E) else None)
