# Effectifs et notables par regroupement du § 4 de la lecture descriptive ; carte à passeport rangée nulle part.
import json,re,sys
G=sys.argv[1]+"/archives-reponses-modeles/auto-conception-course-v9-2026-11-19-v1/course-v9-sortie/sortie/generation-1"
f=json.load(open(G+"/fiches.json")); cl={l["ident"]:l["notable"] for l in json.load(open(G+"/classement.json"))["lignes"]}
note=open(sys.argv[2],encoding="utf-8").read()
s4=note.split("## 4.")[1].split("Aucune carte ne porte")[0]
tot=set()
print("cartes citees | notables | effectif ecrit | regroupement")
for bloc in re.split(r"\n(?=\d+\. \*\*)",s4)[1:]:
    ids=re.findall(r"`(f[0-9a-f]{12})`",bloc); tot|=set(ids)
    print(len(ids), sum(cl[i] for i in ids), "|", re.findall(r"\(≈? ?\d+[^)]*\)|\(\d+\)",bloc[:260]), "|", bloc[:70].replace("\n"," "))
for i in sorted(set(f)-tot): print("non rangee:",i,f[i]["meta"]["proposeur"],re.match(r"Lot (\d+)",f[i]["meta"]["case"][0]).group(0),"notable",cl[i])
