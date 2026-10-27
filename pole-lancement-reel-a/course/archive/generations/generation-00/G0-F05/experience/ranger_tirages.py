#!/usr/bin/env python3
"""Range telles quelles les issues deposees par le noyau (mesures.json) dans tirages.json.

Aucune mesure, aucun calcul de richesse. Verifie seulement les liaisons :
fiche gelee, engagement gele, ordre d'execution, mesures.
Usage : python3 -I ranger_tirages.py [dossier]
"""
import hashlib
import json
import os
import sys

EMPREINTE_FICHE = "83ec5b83b2a4c178b6e5f515a2dd000560c92929c5c35eaa275dd433cd2e45c6"
EMPREINTE_ENGAGEMENT = "aff8d07a128f287b3ee72c7ead255f01042e34dbaf696b4bb6eb496ae5909f52"


def sha_fichier(p):
    with open(p, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def main():
    d = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
    P = lambda n: os.path.join(d, n)

    assert sha_fichier(P("fiche.json")) == EMPREINTE_FICHE, "fiche.json modifiee"
    assert sha_fichier(P("engagement.json")) == EMPREINTE_ENGAGEMENT, "engagement.json modifie"

    eng = json.load(open(P("engagement.json")))
    ordre_doc = json.load(open(P("ordre-execution.json")))
    mes = json.load(open(P("mesures.json")))

    n = len(eng["instances"])
    k = int(eng["nombre_issues"])
    ordre = ordre_doc["ordre"]
    empreinte_ordre = hashlib.sha256(
        json.dumps(ordre, separators=(",", ":")).encode()).hexdigest()

    assert eng["empreinte_fiche"] == EMPREINTE_FICHE
    assert ordre_doc["empreinte_engagement"] == EMPREINTE_ENGAGEMENT
    assert sorted(ordre) == list(range(n)), "ordre n'est pas une permutation du plan"
    assert mes["empreinte_engagement"] == EMPREINTE_ENGAGEMENT, "mesures non liees a l'engagement"
    assert mes["plan_execution"] == eng["plan_execution"] == "ordre_secret"
    assert mes["empreinte_ordre"] == empreinte_ordre, "mesures non liees a l'ordre"
    issues = mes["issues"]
    assert len(issues) == n and all(isinstance(x, int) and 0 <= x < k for x in issues)

    # Execution dans l'ordre impose : au temps s, instance ordre[s] ; l'issue
    # (deja produite par le noyau et rangee a l'indice de l'instance) est recopiee telle quelle.
    rangees = [None] * n
    for s in range(n):
        i = ordre[s]
        rangees[i] = issues[i]
    assert rangees == issues

    sortie = {
        "empreinte_engagement": EMPREINTE_ENGAGEMENT,
        "issues": rangees,
        "plan_execution": mes["plan_execution"],
        "empreinte_ordre": mes["empreinte_ordre"],
    }
    with open(P("tirages.json"), "w") as f:
        json.dump(sortie, f, ensure_ascii=False)
    print("tirages.json ecrit :", n, "issues ; sha256 =", sha_fichier(P("tirages.json")))


if __name__ == "__main__":
    main()
