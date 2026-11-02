"""(Copie de verif-graine-3/scripts/inspecter_repetition.py, plus `declarations_coeur`.) Inspection des sorties de la répétition jouet (P3 jouet, aucune donnée de P3) : lit la branche de résultats du dépôt
nu jouet ; rapporte la chaîne, la classe, les déclarations du cœur, la lecture du lot et ce que la table v3 porte pour
les cibles du lot (déclarations, entrées)."""
import json
import subprocess
import sys

DEPOT, BRANCHE = sys.argv[1], sys.argv[2]


def git(*a):
    return subprocess.run(["git", "--git-dir", DEPOT, *a], check=True, capture_output=True, text=True).stdout


fichiers = git("ls-tree", "-r", "--name-only", BRANCHE).splitlines()
print("commits de la branche :")
print(git("log", "--format=  %s", f"{BRANCHE}", "-n", "12"))


def lire(chemin):
    return json.loads(git("show", f"{BRANCHE}:{chemin}"))


res = {}
for f in fichiers:
    for etape in ("validation", "resolution", "resolution-lot"):
        if f.endswith(f"/resolution-graine-{etape}.json") and f.startswith("diag/"):
            res[etape] = (f, lire(f)["resultat"])
v = res["validation"][1]
print("validation : classe", v["lecture_validation"]["classe"], "; retrouvées", v["empreintes_retrouvees"], "/",
      v["episodes_etape"])
r = res["resolution"][1]
print("résolution : lecture", r["lecture"], "; contrôle croisé", r["controle_croise_lecture"], "; classe recopiée",
      r["lecture_validation"]["classe"])
print("  non résolus :", [(x["episode"], x["cause"][:60]) for x in r["non_resolus"]])
print("  déclarations :", r["declarations"])
if "resolution-lot" in res:
    lot = res["resolution-lot"][1]
    print("lot : lecture", lot["lecture"], "; lecture du lot", lot["lecture_lot"], "; classe", lot["classe_validation"])
    for x in lot["episodes"]:
        print("  cible", x["episode"], ": statut", x["statut"], "; voie", x["voie"], "; lecture", x["lecture_lot"],
              "; forme", x.get("forme"), "; clé declaration présente :", "declaration" in x)
t = lire("prereg/R1-table-tokenisation-v3.json")
print("table v3 : version", t["version"], "; comptes identifiants / non_resolu :", t["comptes"].get("identifiants"),
      "/", t["comptes"].get("non_resolu"))
print("  lecture_validation (clés) :", sorted(t["lecture_validation"]))
print("  declarations :", t.get("declarations"))
print("  declarations_coeur :", t.get("declarations_coeur"))
for e in t["episodes"]:
    if e["methode"] == "identifiants":
        rgx = e.get("resolution_graine", {})
        print("  entrée", e["episode"], ": méthode identifiants ; voie", rgx.get("voie"), "; déclaration dans l'entrée :",
              rgx.get("declaration"), "; déclaration dans `declarations` :", t.get("declarations", {}).get(e["episode"]))
