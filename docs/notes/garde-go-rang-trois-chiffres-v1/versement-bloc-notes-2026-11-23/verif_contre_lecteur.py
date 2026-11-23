import importlib.util, re, sys
from pathlib import Path
R=Path("/home/user/controle-ia-travail")
def charge(p,n):
    s=importlib.util.spec_from_file_location(n,p); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
g=charge(R/".claude/hooks/garde_calcul.py","neuf")
o=charge(sys.argv[1],"ancien")
cas={"GO-2026-11-22-7":[], "GO-2026-11-22-75":["GO-2026-11-22-75"], "GO-2026-11-22-117":["GO-2026-11-22-117"],
"GO-2026-11-22-1170":[], "GO-2026-11-22-10000":[], "x GO-2026-11-22-117-x":["GO-2026-11-22-117"],
"GO-2026-11-22-117.":["GO-2026-11-22-117"], "GO-2026-11-22-117/a":["GO-2026-11-22-117"],
"GO-2026-11-22-117_a":[], "GO-2026-11-22-1171":[], "aGO-2026-11-22-117":[], "_GO-2026-11-22-117":[],
"GO_ID=GO-2026-11-22-117,GO-2026-11-22-05":["GO-2026-11-22-117","GO-2026-11-22-05"],
"GO-2026-11-22-117é":[], "GO-2026-11-22-11 7":["GO-2026-11-22-11"]}
bad=0
for c,att in cas.items():
    r=g.GO_ID.findall(c)
    if r!=att: bad+=1; print("GO_ID KO",c,r,att)
lig={"| GO-2026-11-22-117 | a":"GO-2026-11-22-117","|GO-2026-11-22-117|":"GO-2026-11-22-117","| GO-2026-11-22-1170 | a":None,
"| GO-2026-11-22-7 | a":None,"| GO-2026-11-22-75 | a":"GO-2026-11-22-75","| GO-2026-11-22-117x | a":None,"| GO-2026-11-22-117-1 | a":None}
for c,att in lig.items():
    m=g.LIGNE_GO.match(c); r=m.group(1) if m else None
    if r!=att: bad+=1; print("LIGNE KO",c,r,att)
print("cas limites KO:",bad)
# registre reel
txt=(R/"registres/go.md").read_text(encoding="utf-8").splitlines()
neuf=g.lire_go(R/"registres/go.md"); anc=o.lire_go(R/"registres/go.md")
print("ids neuf",len(neuf),"ancien",len(anc))
nouveaux=sorted(set(neuf)-set(anc)); print("nouveaux",len(nouveaux),nouveaux[:3],nouveaux[-3:])
assert set(anc)<=set(neuf)
for k in anc: assert anc[k]==neuf[k], k
# lignes | GO- non lues
nonlues=[l[:60] for l in txt if l.startswith("| GO-") and not g.LIGNE_GO.match(l)]
print("lignes '| GO-' non lues par le neuf:",nonlues)
# rangs
rangs=[k.rsplit("-",1)[1] for k in neuf]; print("longueurs rang",sorted(set(map(len,rangs))))
# nouveaux: types, echeances, extensions
from collections import Counter
print(Counter(neuf[k]["type"] for k in nouveaux))
print("sans echeance hors calcul:",[k for k in nouveaux if neuf[k]["echeance"] is None])
print("extensions:",[k for k in nouveaux if neuf[k]["extensions"]])
# revocations nouvelles visant des GO anciens
for k in nouveaux:
    r=neuf[k]
    if r["type"]=="révocation":
        cible=[i for i in neuf if i!=k and (i in r["perimetre"] or i in r["ref"])]
        print("revocation",k,"cible",cible)
# faux positifs de sous-chaine : un id rang2 sous-chaine d'un texte de revocation qui cite un rang3
for k,r in neuf.items():
    if r["type"]=="révocation":
        for i in neuf:
            if i!=k and (i in r["perimetre"] or i in r["ref"]):
                cites=set(re.findall(r"GO-\d{4}-\d{2}-\d{2}-\d+",r["perimetre"]+" "+r["ref"]))
                if i not in cites: print("FAUX POSITIF de sous-chaine",k,"->",i)
print("types revocation total:",[k for k,r in neuf.items() if r["type"]=="révocation"])
# GO de calcul neufs
print("calcul neufs:",[(k,str(neuf[k]["accorde"]),str(neuf[k]["echeance"]),neuf[k]["par"]) for k in nouveaux if neuf[k]["type"]=="calcul"])
