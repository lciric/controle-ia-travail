"""Range telles quelles les issues du monde (mesures.json) dans tirages.json.
Rejouable : python3 -I ranger_mesures.py <dossier>
Vérifie les empreintes de la fiche, de l'engagement et de l'ordre ; ne calcule aucune richesse."""
import hashlib, json, os, sys

D = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
FICHE = "e0c69ba8c37794aa249908ffdbbccf53d8ec0edbbc5e4398d776f4be1fe42c2e"
ENG = "1365e4a2666d15623987d3f0ba555e06f5379e827b59c8612a0adf3c9407de9f"

def sha_file(n):
    with open(os.path.join(D, n), "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def load(n):
    with open(os.path.join(D, n), encoding="utf-8") as f:
        return json.load(f)

assert sha_file("fiche.json") == FICHE, "fiche.json altérée"
assert sha_file("engagement.json") == ENG, "engagement.json altéré"
eng = load("engagement.json")
ordre = load("ordre-execution.json")
mes = load("mesures.json")

assert ordre["empreinte_engagement"] == ENG, "ordre non lié à l'engagement"
assert mes["empreinte_engagement"] == ENG, "mesures non liées à l'engagement"
n = len(eng["instances"])
o = ordre["ordre"]
assert sorted(o) == list(range(n)), "ordre n'est pas une permutation du plan"
emp_ordre = hashlib.sha256(json.dumps(o, separators=(",", ":")).encode()).hexdigest()
assert mes["empreinte_ordre"] == emp_ordre, "empreinte de l'ordre incohérente"
assert mes["plan_execution"] == eng["plan_execution"] == "ordre_secret"
issues = mes["issues"]
assert len(issues) == n
k = eng["nombre_issues"]
assert all(isinstance(y, int) and 0 <= y < k for y in issues)

tirages = {
    "empreinte_engagement": mes["empreinte_engagement"],
    "issues": issues,  # telles quelles, rangées à l'indice de leur instance
    "plan_execution": mes["plan_execution"],
    "empreinte_ordre": mes["empreinte_ordre"],
}
with open(os.path.join(D, "tirages.json"), "w", encoding="utf-8") as f:
    json.dump(tirages, f, ensure_ascii=False, indent=1)
print("ok", n, "issues ; ordre", emp_ordre)
