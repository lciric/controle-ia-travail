import hashlib, json
empreinte = hashlib.sha256(open("engagement.json", "rb").read()).hexdigest()
mesures = json.load(open("mesures.json", encoding="utf-8"))
if mesures["empreinte_engagement"] != empreinte:
    raise SystemExit("mesures sans lien avec l'engagement gelé")
sortie = {"empreinte_engagement": empreinte, "issues": mesures["issues"],
          "plan_execution": mesures.get("plan_execution", "ordre_naturel")}
if mesures.get("empreinte_ordre"):
    sortie["empreinte_ordre"] = mesures["empreinte_ordre"]
json.dump(sortie, open("tirages.json", "w", encoding="utf-8"))
