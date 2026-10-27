#!/usr/bin/env python3
"""Range telles quelles les issues deposees par le noyau (mesures.json) dans tirages.json,
apres verification du lien avec l'engagement gele et la fiche."""
import hashlib, json, sys

def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

FICHE = "b1032d8e3700b1427e7de429c8d2e8074634dd868b08da6fdb602f214052ec6e"
ENG = "8aca67b3d6e9431b083b28addae560755c0ccc1c72f6e9a67592426cef13d274"

assert sha("fiche.json") == FICHE, "fiche.json alteree"
assert sha("engagement.json") == ENG, "engagement.json altere"
eng = json.load(open("engagement.json"))
m = json.load(open("mesures.json"))
assert m["empreinte_engagement"] == ENG, "mesures.json non lie a l'engagement"
ordre = json.load(open("ordre-execution.json"))
assert ordre["empreinte_engagement"] == ENG, "ordre non lie a l'engagement"
n = len(eng["instances"])
assert len(m["issues"]) == n == len(ordre["ordre"]), "tailles incoherentes"
assert sorted(ordre["ordre"]) == list(range(n)), "ordre non permutation"
assert hashlib.sha256(json.dumps(ordre["ordre"], separators=(",", ":")).encode()).hexdigest() == m["empreinte_ordre"], "empreinte de l'ordre incoherente"
k = eng.get("nombre_issues", 3)
assert all(isinstance(x, int) and 0 <= x < k for x in m["issues"]), "issue hors domaine"

tirages = {
    "empreinte_engagement": m["empreinte_engagement"],
    "issues": m["issues"],
    "plan_execution": m["plan_execution"],
    "empreinte_ordre": m["empreinte_ordre"],
}
with open("tirages.json", "w") as f:
    json.dump(tirages, f, indent=2, ensure_ascii=False)
print("ok", n, "issues rangees")
