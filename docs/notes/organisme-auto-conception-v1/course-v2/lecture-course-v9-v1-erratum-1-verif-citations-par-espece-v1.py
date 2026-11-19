# Complément d'audit par espèce, par programme, sans lecture : définitions fixées avant l'exécution.
# marque de citation : "et al." | "arXiv" | une année 1900-2099 en mot entier ; marque de réserve : "non vérifi" (insensible à la casse)
import json,re,sys,collections,statistics as st
G=sys.argv[1]+"/archives-reponses-modeles/auto-conception-course-v9-2026-11-19-v1/course-v9-sortie/sortie/generation-1"
f=json.load(open(G+"/fiches.json")); cl={l["ident"]:l["notable"] for l in json.load(open(G+"/classement.json"))["lignes"]}
cit=re.compile(r"et al\.|arxiv|\b(?:19|20)\d{2}\b",re.I); res=re.compile(r"non v[ée]rifi",re.I)
T=collections.defaultdict(list)
for i,x in f.items():
    t=" ".join(str(v) for v in x["contenu"].values())
    T[x["meta"]["proposeur"]].append((len(cit.findall(t)),len(res.findall(t)),cl[i]))
print("espece | cartes | avec citation | mediane citations | avec reserve | mediane reserves | notables")
for e,L in sorted(T.items()):
    print(e,len(L),sum(c>0 for c,_,_ in L),st.median(c for c,_,_ in L),sum(r>0 for _,r,_ in L),st.median(r for _,r,_ in L),sum(n for *_,n in L))
tout=[x for L in T.values() for x in L]
for nom,cond in (("citation>0 et reserve=0",lambda c,r:c>0 and r==0),("citation>0 et reserve>0",lambda c,r:c>0 and r>0),("citation=0",lambda c,r:c==0)):
    S=[n for c,r,n in tout if cond(c,r)]; print(nom,len(S),"notables",sum(S))
