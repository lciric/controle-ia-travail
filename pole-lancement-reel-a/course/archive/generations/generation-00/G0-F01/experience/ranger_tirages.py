#!/usr/bin/env python3
"""Range telles quelles les issues deposees par le noyau (mesures.json) dans tirages.json.

Rejouable : python3 -I ranger_tirages.py [dossier]
Aucune mesure, aucun hasard, aucun calcul de richesse.
"""
import hashlib
import json
import os
import sys

EMPREINTE_FICHE = "6e468f9a63b776f77baa85d626c44070d34a2f94b725a6fe81f06bc3412f313f"
EMPREINTE_ENGAGEMENT = "9894b6d8b596730f93f7b52ff4bdfe37c5d4dc1c9a815bbc57a4c72cd44b7dbd"


def sha_fichier(p):
    with open(p, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def main():
    d = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
    P = lambda n: os.path.join(d, n)

    assert sha_fichier(P("fiche.json")) == EMPREINTE_FICHE, "fiche.json altérée"
    assert sha_fichier(P("engagement.json")) == EMPREINTE_ENGAGEMENT, "engagement.json altéré"

    eng = json.load(open(P("engagement.json")))
    n = len(eng["instances"])
    k = int(eng["nombre_issues"])

    ordre_doc = json.load(open(P("ordre-execution.json")))
    assert ordre_doc["empreinte_engagement"] == EMPREINTE_ENGAGEMENT, "ordre non lié à l'engagement"
    ordre = ordre_doc["ordre"]
    assert sorted(ordre) == list(range(n)), "ordre n'est pas une permutation du plan"
    empreinte_ordre = hashlib.sha256(
        json.dumps(ordre, separators=(",", ":")).encode()).hexdigest()

    m = json.load(open(P("mesures.json")))
    assert m["empreinte_engagement"] == EMPREINTE_ENGAGEMENT, "mesures.json non lié à l'engagement gelé"
    assert m["empreinte_ordre"] == empreinte_ordre, "mesures.json non lié à l'ordre imposé"
    assert m["plan_execution"] == eng["plan_execution"] == "ordre_secret"
    issues = m["issues"]
    assert len(issues) == n and all(isinstance(x, int) and 0 <= x < k for x in issues)

    # Parcours dans l'ordre imposé : au temps s, instance ordre[s] ; issue rangée à son indice.
    rangees = [None] * n
    for s in range(n):
        i = ordre[s]
        rangees[i] = issues[i]  # issue du monde telle que déposée, sans modification
    assert rangees == issues

    out = {
        "empreinte_engagement": EMPREINTE_ENGAGEMENT,
        "issues": rangees,
        "plan_execution": m["plan_execution"],
        "empreinte_ordre": empreinte_ordre,
    }
    with open(P("tirages.json"), "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print("tirages.json écrit :", n, "issues ; empreinte_ordre", empreinte_ordre)


if __name__ == "__main__":
    main()
