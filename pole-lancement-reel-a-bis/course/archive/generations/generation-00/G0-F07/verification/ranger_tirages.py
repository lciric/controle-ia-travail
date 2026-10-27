"""Range les issues déposées par le noyau (mesures.json) dans tirages.json.
Rejouable : python3 -I ranger_tirages.py
Vérifie les liaisons (fiche, engagement, ordre) ; ne mesure ni ne modifie aucune issue."""
import hashlib, json, sys

EMP_FICHE = "315c5a81f4b550c714fd9b79572ed942ef16506280a13a719fb3e45063680434"
EMP_ENG = "277448c25ec54bbb06722b0cefa819400a4b6653d980ac4a4c6e2907f68ee9c7"

def sha_file(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

def main():
    assert sha_file("fiche.json") == EMP_FICHE, "fiche altérée"
    assert sha_file("engagement.json") == EMP_ENG, "engagement altéré"
    eng = json.load(open("engagement.json"))
    assert eng["empreinte_fiche"] == EMP_FICHE
    n, k = len(eng["instances"]), eng["nombre_issues"]

    ordre = json.load(open("ordre-execution.json"))
    assert ordre["empreinte_engagement"] == EMP_ENG, "ordre non lié à l'engagement"
    perm = ordre["ordre"]
    assert sorted(perm) == list(range(n)), "ordre n'est pas une permutation du plan"
    emp_ordre = hashlib.sha256(json.dumps(perm, separators=(",", ":")).encode()).hexdigest()

    mes = json.load(open("mesures.json"))
    assert mes["empreinte_engagement"] == EMP_ENG, "mesures non liées à l'engagement gelé"
    assert mes["empreinte_ordre"] == emp_ordre, "empreinte d'ordre incohérente"
    assert mes["plan_execution"] == eng["plan_execution"] == "ordre_secret"
    issues = mes["issues"]
    assert len(issues) == n and all(isinstance(x, int) and 0 <= x < k for x in issues)

    # Issues déjà rangées par indice d'instance par le noyau : recopiées telles quelles.
    tirages = {
        "empreinte_engagement": mes["empreinte_engagement"],
        "issues": list(issues),
        "plan_execution": mes["plan_execution"],
        "empreinte_ordre": mes["empreinte_ordre"],
    }
    with open("tirages.json", "w") as f:
        json.dump(tirages, f, indent=2, sort_keys=True)
    print("ok", n, "issues ; empreinte_ordre", emp_ordre)

if __name__ == "__main__":
    sys.exit(main())
