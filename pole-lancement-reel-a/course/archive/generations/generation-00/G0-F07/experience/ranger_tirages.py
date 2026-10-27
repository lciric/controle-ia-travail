"""Range telles quelles les issues du monde (mesures.json) dans tirages.json.

Vérifie : empreintes de fiche et d'engagement gelées, liaison de mesures.json
et d'ordre-execution.json à l'engagement, empreinte de l'ordre, forme des issues.
Aucune issue n'est produite ni modifiée ici. Rejouable : python3 -I ranger_tirages.py
"""
import hashlib
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
EMPREINTE_FICHE = "315c5a81f4b550c714fd9b79572ed942ef16506280a13a719fb3e45063680434"
EMPREINTE_ENGAGEMENT = "277448c25ec54bbb06722b0cefa819400a4b6653d980ac4a4c6e2907f68ee9c7"


def sha_fichier(nom):
    with open(os.path.join(ICI, nom), "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def charger(nom):
    with open(os.path.join(ICI, nom), encoding="utf-8") as f:
        return json.load(f)


def echec(msg):
    sys.exit("ÉCHEC : " + msg)


def main():
    if sha_fichier("fiche.json") != EMPREINTE_FICHE:
        echec("fiche.json modifiée")
    if sha_fichier("engagement.json") != EMPREINTE_ENGAGEMENT:
        echec("engagement.json modifié")

    eng = charger("engagement.json")
    mes = charger("mesures.json")
    ordre = charger("ordre-execution.json")

    if mes.get("empreinte_engagement") != EMPREINTE_ENGAGEMENT:
        echec("mesures.json non lié à l'engagement gelé")
    if ordre.get("empreinte_engagement") != EMPREINTE_ENGAGEMENT:
        echec("ordre-execution.json non lié à l'engagement gelé")

    n = len(eng["instances"])
    k = int(eng["nombre_issues"])
    perm = ordre["ordre"]
    if sorted(perm) != list(range(n)):
        echec("l'ordre n'est pas une permutation du plan")
    emp_ordre = hashlib.sha256(
        json.dumps(perm, separators=(",", ":")).encode()).hexdigest()
    if mes.get("empreinte_ordre") != emp_ordre:
        echec("empreinte de l'ordre incohérente")
    if mes.get("plan_execution") != eng.get("plan_execution"):
        echec("plan d'exécution incohérent avec l'engagement")

    issues = mes["issues"]
    if len(issues) != n or any(
            not isinstance(y, int) or isinstance(y, bool) or not 0 <= y < k
            for y in issues):
        echec("issues mal formées")

    tirages = {
        "empreinte_engagement": mes["empreinte_engagement"],
        "issues": list(issues),
        "plan_execution": mes["plan_execution"],
        "empreinte_ordre": mes["empreinte_ordre"],
    }
    with open(os.path.join(ICI, "tirages.json"), "w", encoding="utf-8") as f:
        json.dump(tirages, f, ensure_ascii=False, indent=1)
    print("tirages.json écrit :", n, "issues rangées telles quelles")


if __name__ == "__main__":
    main()
