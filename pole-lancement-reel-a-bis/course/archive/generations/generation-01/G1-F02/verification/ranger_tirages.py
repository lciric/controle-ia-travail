"""Range les issues déposées par le noyau (mesures.json) dans tirages.json, sans les modifier.

Vérifications : empreintes de fiche et d'engagement gelées, liaison de mesures.json
à l'engagement, cohérence de l'empreinte d'ordre avec ordre-execution.json.
"""
import hashlib
import json
import sys

EMPREINTE_FICHE = "da8c7dbb58df05c7f757b4833ca3f908da3beaa03412068fbc5cfdea086029f3"
EMPREINTE_ENGAGEMENT = "65d933545265ab5ac13a572267b52761457d4747aa7a0c12b073ed075fc84a52"


def sha_fichier(p):
    with open(p, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def main():
    assert sha_fichier("fiche.json") == EMPREINTE_FICHE, "fiche.json modifiée"
    assert sha_fichier("engagement.json") == EMPREINTE_ENGAGEMENT, "engagement.json modifié"

    with open("mesures.json") as f:
        m = json.load(f)
    with open("ordre-execution.json") as f:
        o = json.load(f)

    assert m["empreinte_engagement"] == EMPREINTE_ENGAGEMENT, "mesures non liées à l'engagement"
    assert o["empreinte_engagement"] == EMPREINTE_ENGAGEMENT, "ordre non lié à l'engagement"

    ordre = o["ordre"]
    emp_ordre = hashlib.sha256(json.dumps(ordre, separators=(",", ":")).encode()).hexdigest()
    assert m["empreinte_ordre"] == emp_ordre, "empreinte d'ordre incohérente"
    assert sorted(ordre) == list(range(len(ordre))), "ordre n'est pas une permutation"
    assert len(m["issues"]) == len(ordre), "nombre d'issues incorrect"

    tirages = {
        "empreinte_engagement": m["empreinte_engagement"],
        "issues": m["issues"],
        "plan_execution": m["plan_execution"],
        "empreinte_ordre": m["empreinte_ordre"],
    }
    with open("tirages.json", "w") as f:
        json.dump(tirages, f, indent=2, ensure_ascii=False)
    print("tirages.json écrit :", len(m["issues"]), "issues")


if __name__ == "__main__":
    sys.exit(main())
