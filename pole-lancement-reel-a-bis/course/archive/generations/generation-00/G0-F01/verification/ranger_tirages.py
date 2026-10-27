#!/usr/bin/env python3
"""Range les issues déposées par le noyau (mesures.json) dans tirages.json.
Aucune mesure propre : vérifie seulement le lien à l'engagement gelé et à l'ordre imposé."""
import hashlib, json, sys

EMP_FICHE = "6e468f9a63b776f77baa85d626c44070d34a2f94b725a6fe81f06bc3412f313f"
EMP_ENG = "9894b6d8b596730f93f7b52ff4bdfe37c5d4dc1c9a815bbc57a4c72cd44b7dbd"

def sha_file(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

def main():
    assert sha_file("fiche.json") == EMP_FICHE, "fiche.json altérée"
    assert sha_file("engagement.json") == EMP_ENG, "engagement.json altéré"
    eng = json.load(open("engagement.json"))
    mes = json.load(open("mesures.json"))
    ordre = json.load(open("ordre-execution.json"))
    assert mes["empreinte_engagement"] == EMP_ENG, "mesures.json non lié à l'engagement"
    assert ordre["empreinte_engagement"] == EMP_ENG, "ordre non lié à l'engagement"
    emp_ordre = hashlib.sha256(json.dumps(ordre["ordre"], separators=(",", ":")).encode()).hexdigest()
    assert mes["empreinte_ordre"] == emp_ordre, "empreinte d'ordre incohérente"
    n = len(eng["instances"])
    assert sorted(ordre["ordre"]) == list(range(n)), "ordre n'est pas une permutation du plan"
    issues = mes["issues"]
    assert len(issues) == n and all(isinstance(i, int) and 0 <= i < eng["nombre_issues"] for i in issues)
    tirages = {
        "empreinte_engagement": mes["empreinte_engagement"],
        "issues": issues,  # telles quelles, indexées par instance du plan
        "plan_execution": mes["plan_execution"],
        "empreinte_ordre": mes["empreinte_ordre"],
    }
    with open("tirages.json", "w") as f:
        json.dump(tirages, f, indent=2, ensure_ascii=False)
    print("tirages.json écrit,", n, "issues")

if __name__ == "__main__":
    sys.exit(main())
