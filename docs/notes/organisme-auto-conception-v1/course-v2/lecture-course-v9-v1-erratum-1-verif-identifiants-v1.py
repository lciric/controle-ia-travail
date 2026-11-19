import json,re,glob,sys,collections
R=sys.argv[1]; note=open(sys.argv[2],encoding='utf-8').read()
G=R+"/archives-reponses-modeles/auto-conception-course-v9-2026-11-19-v1/course-v9-sortie/sortie/generation-1"
f=json.load(open(G+"/fiches.json")); v={}
for p in glob.glob(G+"/coffre/verdicts-passe1-*.json"):
    x=json.load(open(p)); v[x["ident"]]=x
s4=note.split("## 4.")[1].split("## 5.")[0]
nom={"Opus":"prop-opus","Fable":"prop-fable","Argon":"prop-argon","Astra":"prop-astra","Carbon":"prop-carbon"}
# dans les 13 regroupements : paires (espece, ident)
reg=s4.split("Aucune carte ne porte")[0]
faux=[];cites=collections.Counter()
for seg in re.split(r"(?=\b(?:Opus|Fable|Argon|Astra|Carbon) `)",reg):
    m=re.match(r"(Opus|Fable|Argon|Astra|Carbon) ((?:`f[0-9a-f]{12}`(?:, )?)+)",seg)
    if not m: continue
    for i in re.findall(r"`(f[0-9a-f]{12})`",m.group(2)):
        cites[i]+=1
        if i not in f: faux.append((i,"absente"))
        elif f[i]["meta"]["proposeur"]!=nom[m.group(1)]: faux.append((i,m.group(1),f[i]["meta"]["proposeur"]))
print("cartes citees dans les regroupements:",len(cites),"citations:",sum(cites.values()),"erreurs:",faux)
print("citees plusieurs fois:",[i for i,n in cites.items() if n>1])
print("non citees:",len(set(f)-set(cites)))
tous=set(re.findall(r"`(f[0-9a-f]{12})`",note)); print("ident de la note absents des 94:",sorted(tous-set(f)))
sept="f4a47f030c829 f4b85ff3c1033 f68f93bac44e8 fb9e8ae1b97b8 fdafe4598caad f20fbf8b6d797 f7cc0003c4b2c".split()
print("sept:",[(v[i]["verdicts"]["juge-opus"]["items"]["reserves_tenues"],v[i]["verdicts"]["juge-argon"]["items"]["reserves_tenues"]) for i in sept])
cinq="fed7a993d9671 f7a4918afe116 f0d21fb62aff2 f6f8c8b855234 fc37640a0181d".split()
print("cinq:",[(v[i]["verdicts"]["juge-opus"]["items"]["reserves_tenues"],v[i]["verdicts"]["juge-argon"]["items"]["reserves_tenues"]) for i in cinq])
print("non notables:",sum(not all(v[i]["verdicts"][j]["notable"] for j in v[i]["verdicts"]) for i in v))
# regroupement 7 : notables
