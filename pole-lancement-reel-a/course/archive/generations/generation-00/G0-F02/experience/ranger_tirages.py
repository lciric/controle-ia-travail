#!/usr/bin/env python3
"""Range telles quelles les issues deposees par le noyau (mesures.json) dans tirages.json.
Verifie fiche, engagement, ordre et liaison de mesures.json. Aucune mesure, aucune richesse."""
import hashlib, json, os, sys

D = os.path.dirname(os.path.abspath(__file__))
EMP_FICHE = "b1032d8e3700b1427e7de429c8d2e8074634dd868b08da6fdb602f214052ec6e"
EMP_ENG = "8aca67b3d6e9431b083b28addae560755c0ccc1c72f6e9a67592426cef13d274"

def sha_file(n):
    with open(os.path.join(D, n), "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def load(n):
    with open(os.path.join(D, n), encoding="utf-8") as f:
        return json.load(f)

def fail(msg):
    sys.exit("ECHEC: " + msg)

if sha_file("fiche.json") != EMP_FICHE: fail("empreinte fiche")
if sha_file("engagement.json") != EMP_ENG: fail("empreinte engagement")
eng = load("engagement.json")
if eng.get("empreinte_fiche") not in (None, EMP_FICHE): fail("engagement non lie a la fiche")
n = len(eng["instances"])
k = int(eng["nombre_issues"])

ordre_doc = load("ordre-execution.json")
if ordre_doc.get("empreinte_engagement") != EMP_ENG: fail("ordre non lie a l'engagement")
ordre = ordre_doc["ordre"]
if sorted(ordre) != list(range(n)): fail("ordre n'est pas une permutation du plan")
emp_ordre = hashlib.sha256(json.dumps(ordre, separators=(",", ":")).encode()).hexdigest()

m = load("mesures.json")
if m.get("empreinte_engagement") != EMP_ENG: fail("mesures non liees a l'engagement")
if m.get("empreinte_ordre") != emp_ordre: fail("empreinte d'ordre incoherente")
if m.get("plan_execution") != eng.get("plan_execution"): fail("plan d'execution incoherent")
issues = m["issues"]
if len(issues) != n: fail("nombre d'issues")
if not all(isinstance(x, int) and 0 <= x < k for x in issues): fail("issue hors domaine")

tirages = {
    "empreinte_engagement": m["empreinte_engagement"],
    "issues": issues,  # telles quelles, indexees par instance du plan
    "plan_execution": m["plan_execution"],
    "empreinte_ordre": m["empreinte_ordre"],
}
with open(os.path.join(D, "tirages.json"), "w", encoding="utf-8") as f:
    json.dump(tirages, f, ensure_ascii=False, indent=1)
print("OK", n, "issues rangees ; empreinte_ordre", emp_ordre)
