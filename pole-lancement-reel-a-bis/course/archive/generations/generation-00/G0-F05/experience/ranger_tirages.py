#!/usr/bin/env python3
"""Range telles quelles les issues deposees par le noyau (mesures.json) dans tirages.json.
Verifie : empreintes fiche/engagement, liaison de mesures.json et de l'ordre a l'engagement,
empreinte de l'ordre, permutation complete du plan. Ne mesure ni ne modifie aucune issue."""
import hashlib, json, sys

EMP_FICHE = "83ec5b83b2a4c178b6e5f515a2dd000560c92929c5c35eaa275dd433cd2e45c6"
EMP_ENG = "aff8d07a128f287b3ee72c7ead255f01042e34dbaf696b4bb6eb496ae5909f52"

def sha_fichier(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

def main():
    assert sha_fichier("fiche.json") == EMP_FICHE, "fiche.json altere"
    assert sha_fichier("engagement.json") == EMP_ENG, "engagement.json altere"
    eng = json.load(open("engagement.json"))
    mes = json.load(open("mesures.json"))
    ordre = json.load(open("ordre-execution.json"))
    n = len(eng["instances"])
    k = int(eng["nombre_issues"])

    assert mes["empreinte_engagement"] == EMP_ENG, "mesures.json non lie a l'engagement"
    assert ordre["empreinte_engagement"] == EMP_ENG, "ordre non lie a l'engagement"
    emp_ordre = hashlib.sha256(json.dumps(ordre["ordre"], separators=(",", ":")).encode()).hexdigest()
    assert mes["empreinte_ordre"] == emp_ordre, "empreinte d'ordre incoherente"
    assert sorted(ordre["ordre"]) == list(range(n)), "ordre n'est pas une permutation du plan"
    assert mes["plan_execution"] == eng["plan_execution"] == "ordre_secret"
    issues = mes["issues"]
    assert len(issues) == n and all(isinstance(y, int) and 0 <= y < k for y in issues)

    # Les issues sont deja rangees par indice d'instance (ordre[s] traite au temps s) : copie telle quelle.
    tirages = {
        "empreinte_engagement": mes["empreinte_engagement"],
        "issues": issues,
        "plan_execution": mes["plan_execution"],
        "empreinte_ordre": mes["empreinte_ordre"],
    }
    with open("tirages.json", "w") as f:
        json.dump(tirages, f, ensure_ascii=False, indent=1)
    print("tirages.json ecrit :", n, "issues ; empreinte_ordre", emp_ordre)

if __name__ == "__main__":
    sys.exit(main())
