#!/usr/bin/env python3
"""Range telles quelles les issues deposees par le noyau (mesures.json) dans tirages.json,
apres verification du lien avec l'engagement gele et l'ordre d'execution."""
import hashlib, json, sys

EMP_FICHE = "a2eea19a89c2020056116c958e548d9cb57e8067423bc7d32d98ef3c1cdd9b81"
EMP_ENG = "a4a978dc523ac874f1f80a0e40185e485c6fa728750463e0a5707942d18f8f6b"

def sha_file(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

def main():
    assert sha_file("fiche.json") == EMP_FICHE, "fiche.json alteree"
    assert sha_file("engagement.json") == EMP_ENG, "engagement.json altere"
    eng = json.load(open("engagement.json"))
    assert eng["empreinte_fiche"] == EMP_FICHE
    n = len(eng["instances"])

    m = json.load(open("mesures.json"))
    assert m["empreinte_engagement"] == EMP_ENG, "mesures.json non lie a l'engagement"
    assert m["plan_execution"] == eng["plan_execution"] == "ordre_secret"

    o = json.load(open("ordre-execution.json"))
    assert o["empreinte_engagement"] == EMP_ENG
    ordre = o["ordre"]
    assert sorted(ordre) == list(range(n)), "ordre non permutation du plan"
    emp_ordre = hashlib.sha256(json.dumps(ordre, separators=(",", ":")).encode()).hexdigest()
    assert m["empreinte_ordre"] == emp_ordre, "empreinte d'ordre incoherente"

    issues = m["issues"]
    assert len(issues) == n
    k = int(eng["nombre_issues"])
    assert all(isinstance(y, int) and 0 <= y < k for y in issues)

    out = {
        "empreinte_engagement": m["empreinte_engagement"],
        "issues": issues,  # rangees a l'indice de leur instance, telles que deposees
        "plan_execution": m["plan_execution"],
        "empreinte_ordre": m["empreinte_ordre"],
    }
    with open("tirages.json", "w") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print("tirages.json ecrit :", n, "issues ; sha256 =", sha_file("tirages.json"))

if __name__ == "__main__":
    sys.exit(main())
