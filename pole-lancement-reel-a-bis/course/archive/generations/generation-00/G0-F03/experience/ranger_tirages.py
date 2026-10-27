"""Range telles quelles les issues déposées par le noyau dans tirages.json.

Vérifie : empreintes fiche/engagement gelées, liaison de mesures.json à
l'engagement, cohérence de l'empreinte d'ordre et des tailles. Ne modifie
aucune issue et ne touche jamais fiche.json.
"""
import hashlib
import json
import sys

EMPREINTE_FICHE = "6fae74c926f04a79d579c6665b01d37963229dc5a7077f5c5bb0691bbe07a512"
EMPREINTE_ENGAGEMENT = "4a8de271de43a6418f4f993358dcfb01a6bc425495d0824071e4004f7a95a8bc"


def sha_fichier(chemin):
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def main():
    assert sha_fichier("fiche.json") == EMPREINTE_FICHE, "fiche.json altérée"
    assert sha_fichier("engagement.json") == EMPREINTE_ENGAGEMENT, "engagement altéré"

    engagement = json.load(open("engagement.json"))
    mesures = json.load(open("mesures.json"))
    ordre = json.load(open("ordre-execution.json"))

    assert mesures["empreinte_engagement"] == EMPREINTE_ENGAGEMENT, "mesures non liées à l'engagement"
    assert ordre["empreinte_engagement"] == EMPREINTE_ENGAGEMENT, "ordre non lié à l'engagement"

    emp_ordre = hashlib.sha256(
        json.dumps(ordre["ordre"], separators=(",", ":")).encode()
    ).hexdigest()
    assert emp_ordre == mesures["empreinte_ordre"], "empreinte d'ordre incohérente"

    issues = mesures["issues"]
    n = len(engagement["instances"])
    k = engagement.get("nombre_issues", 3)
    assert len(issues) == n == len(ordre["ordre"]), "tailles incohérentes"
    assert sorted(ordre["ordre"]) == list(range(n)), "ordre non permutation"
    assert all(isinstance(y, int) and 0 <= y < k for y in issues), "issue hors domaine"

    tirages = {
        "empreinte_engagement": mesures["empreinte_engagement"],
        "issues": issues,
        "plan_execution": mesures["plan_execution"],
        "empreinte_ordre": mesures["empreinte_ordre"],
    }
    with open("tirages.json", "w") as f:
        json.dump(tirages, f, ensure_ascii=False, indent=1)
    print("tirages.json écrit :", len(issues), "issues")


if __name__ == "__main__":
    sys.exit(main())
