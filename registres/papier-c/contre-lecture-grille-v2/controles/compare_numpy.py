import json, glob, os, sys
rej, V2 = sys.argv[1], sys.argv[2] + "/sorties"
n = 0
for p in sorted(glob.glob(rej + "/*_p0.json")):
    b = os.path.basename(p); a = json.load(open(p))
    o = json.load(open([q for q in (f"{V2}/reprises-v1/{b}", f"{V2}/neuves-v2/{b}") if os.path.exists(q)][0]))
    diff = [k for k in o if a.get(k) != o[k] and k != "duree_s"]
    n += diff == ["versions"]
    print(b, "| numpy du rejeu", a["versions"]["numpy"], "| numpy de la sortie versee", o["versions"]["numpy"], "| champs differents hors duree :", diff, "| taux egaux :", a["taux"] == o["taux"], "| erreurs MC egales :", a["erreur_mc"] == o["erreur_mc"])
print(n, "identiques hors duree et version sur", len(glob.glob(rej + "/*_p0.json")))
