"""Range telles quelles les issues déposées par le noyau (mesures.json) dans tirages.json.

Vérifie : empreinte de fiche.json, empreinte de engagement.json, liaison de
mesures.json et ordre-execution.json à l'engagement, et empreinte de l'ordre.
Aucune issue n'est produite ni modifiée ici. Usage : python3 -I ranger_tirages.py
"""
import hashlib
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
EMPREINTE_FICHE = "e0c69ba8c37794aa249908ffdbbccf53d8ec0edbbc5e4398d776f4be1fe42c2e"
EMPREINTE_ENGAGEMENT = "1365e4a2666d15623987d3f0ba555e06f5379e827b59c8612a0adf3c9407de9f"


def sha_fichier(nom):
    with open(os.path.join(ICI, nom), "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def charger(nom):
    with open(os.path.join(ICI, nom), encoding="utf-8") as f:
        return json.load(f)


def main():
    assert sha_fichier("fiche.json") == EMPREINTE_FICHE, "fiche.json altérée"
    assert sha_fichier("engagement.json") == EMPREINTE_ENGAGEMENT, "engagement.json altéré"
    engagement = charger("engagement.json")
    mesures = charger("mesures.json")
    ordre = charger("ordre-execution.json")

    assert mesures["empreinte_engagement"] == EMPREINTE_ENGAGEMENT, "mesures non liées à l'engagement"
    assert ordre["empreinte_engagement"] == EMPREINTE_ENGAGEMENT, "ordre non lié à l'engagement"

    empreinte_ordre = hashlib.sha256(
        json.dumps(ordre["ordre"], separators=(",", ":")).encode()
    ).hexdigest()
    assert mesures["empreinte_ordre"] == empreinte_ordre, "empreinte d'ordre incohérente"

    n = len(engagement["instances"])
    issues = mesures["issues"]
    assert len(issues) == n == len(ordre["ordre"]), "tailles incohérentes"
    assert sorted(ordre["ordre"]) == list(range(n)), "ordre non permutation"
    k = engagement.get("nombre_issues", 3)
    assert all(isinstance(y, int) and 0 <= y < k for y in issues), "issue hors support"

    tirages = {
        "empreinte_engagement": mesures["empreinte_engagement"],
        "issues": issues,
        "plan_execution": mesures["plan_execution"],
        "empreinte_ordre": mesures["empreinte_ordre"],
    }
    with open(os.path.join(ICI, "tirages.json"), "w", encoding="utf-8") as f:
        json.dump(tirages, f, indent=2, ensure_ascii=False)
    print("tirages.json écrit :", n, "issues ; empreinte_ordre", empreinte_ordre)


if __name__ == "__main__":
    sys.exit(main())
