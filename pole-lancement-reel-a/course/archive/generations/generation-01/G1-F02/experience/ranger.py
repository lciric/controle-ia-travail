"""Rejouable : vérifie le lien mesures.json <-> engagement gelé et range les issues telles quelles."""
import hashlib, json, os, sys

ICI = os.path.dirname(os.path.abspath(__file__))
EMP_FICHE = "da8c7dbb58df05c7f757b4833ca3f908da3beaa03412068fbc5cfdea086029f3"
EMP_ENG = "65d933545265ab5ac13a572267b52761457d4747aa7a0c12b073ed075fc84a52"


def sha(nom):
    with open(os.path.join(ICI, nom), "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def charger(nom):
    with open(os.path.join(ICI, nom), encoding="utf-8") as f:
        return json.load(f)


def main():
    assert sha("fiche.json") == EMP_FICHE, "fiche.json altérée"
    assert sha("engagement.json") == EMP_ENG, "engagement.json altéré"
    m = charger("mesures.json")
    assert m["empreinte_engagement"] == EMP_ENG, "mesures.json non lié à l'engagement"
    o = charger("ordre-execution.json")
    assert o.get("empreinte_engagement", EMP_ENG) == EMP_ENG, "ordre non lié à l'engagement"
    issues = m["issues"]
    assert len(issues) == len(o["ordre"]) == 120, "taille inattendue"
    assert sorted(o["ordre"]) == list(range(len(issues))), "ordre non permutation"
    tirages = {
        "empreinte_engagement": m["empreinte_engagement"],
        "issues": issues,
        "plan_execution": m["plan_execution"],
        "empreinte_ordre": m["empreinte_ordre"],
    }
    with open(os.path.join(ICI, "tirages.json"), "w", encoding="utf-8") as f:
        json.dump(tirages, f, ensure_ascii=False, indent=1)
    print("tirages.json écrit :", len(issues), "issues ; sha256 =", sha("tirages.json"))


if __name__ == "__main__":
    sys.exit(main())
