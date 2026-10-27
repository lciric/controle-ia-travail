#!/usr/bin/env python3
"""Range telles quelles les issues deposees par le noyau (mesures.json) dans tirages.json,
apres verification du lien avec l'engagement gele et l'ordre d'execution. Rejouable."""
import hashlib, json, sys

EMP_FICHE = "c7a4f68787e254584e7cd921c5535b1d5f93515d1a11c71f6208452df78da849"
EMP_ENG = "7488bbb1ece3baf48c22f8f1db5d0f8ad36a8b1e18f79a097518743bc5d9c6bb"


def sha_file(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def main():
    assert sha_file("fiche.json") == EMP_FICHE, "fiche.json modifiee"
    assert sha_file("engagement.json") == EMP_ENG, "engagement.json modifie"
    m = json.load(open("mesures.json"))
    assert m["empreinte_engagement"] == EMP_ENG, "mesures.json non lie a l'engagement"
    o = json.load(open("ordre-execution.json"))
    assert o["empreinte_engagement"] == EMP_ENG, "ordre non lie a l'engagement"
    ordre = o["ordre"]
    emp_ordre = hashlib.sha256(json.dumps(ordre, separators=(",", ":")).encode()).hexdigest()
    assert m["empreinte_ordre"] == emp_ordre, "empreinte d'ordre incoherente"
    issues = m["issues"]
    assert sorted(ordre) == list(range(len(issues))), "ordre n'est pas une permutation du plan"
    assert all(i in (0, 1, 2) for i in issues), "issue hors des 3 issues"
    tirages = {
        "empreinte_engagement": m["empreinte_engagement"],
        "issues": issues,  # telles quelles, deja rangees a l'indice de leur instance
        "plan_execution": m["plan_execution"],
        "empreinte_ordre": m["empreinte_ordre"],
    }
    with open("tirages.json", "w") as f:
        json.dump(tirages, f, indent=2, ensure_ascii=False)
    print("tirages.json ecrit:", len(issues), "issues; sha256", sha_file("tirages.json"))


if __name__ == "__main__":
    sys.exit(main())
