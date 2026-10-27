#!/usr/bin/env python3
"""Range rejouable des issues deposees par le noyau dans tirages.json.

Verifie : empreinte fiche, empreinte engagement, liaison de mesures.json a
l'engagement, liaison a l'ordre d'execution, taille du plan. Copie les issues
telles quelles (deja rangees a l'indice de leur instance par le noyau).
Usage : python3 -I ranger_tirages.py [dossier]
"""
import hashlib
import json
import os
import sys

EMPREINTE_FICHE = "c7a4f68787e254584e7cd921c5535b1d5f93515d1a11c71f6208452df78da849"
EMPREINTE_ENGAGEMENT = "7488bbb1ece3baf48c22f8f1db5d0f8ad36a8b1e18f79a097518743bc5d9c6bb"


def sha_fichier(p):
    with open(p, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def main(d):
    p = lambda n: os.path.join(d, n)
    assert sha_fichier(p("fiche.json")) == EMPREINTE_FICHE, "fiche modifiee"
    assert sha_fichier(p("engagement.json")) == EMPREINTE_ENGAGEMENT, "engagement modifie"

    eng = json.load(open(p("engagement.json")))
    ordre = json.load(open(p("ordre-execution.json")))
    mes = json.load(open(p("mesures.json")))

    assert ordre["empreinte_engagement"] == EMPREINTE_ENGAGEMENT, "ordre non lie"
    assert mes["empreinte_engagement"] == EMPREINTE_ENGAGEMENT, "mesures non liees"

    n = len(eng["instances"])
    o = ordre["ordre"]
    assert sorted(o) == list(range(n)), "ordre n'est pas une permutation du plan"
    empreinte_ordre = hashlib.sha256(
        json.dumps(o, separators=(",", ":")).encode()).hexdigest()
    assert mes["empreinte_ordre"] == empreinte_ordre, "empreinte d'ordre divergente"
    assert mes["plan_execution"] == eng["plan_execution"] == "ordre_secret"

    issues = mes["issues"]
    k = eng["nombre_issues"]
    assert len(issues) == n, "nombre d'issues != taille du plan"
    assert all(isinstance(i, int) and 0 <= i < k for i in issues), "issue hors domaine"

    sortie = {
        "empreinte_engagement": mes["empreinte_engagement"],
        "issues": issues,
        "plan_execution": mes["plan_execution"],
        "empreinte_ordre": mes["empreinte_ordre"],
    }
    with open(p("tirages.json"), "w") as f:
        json.dump(sortie, f, ensure_ascii=False, indent=1)
    print("tirages.json ecrit :", n, "issues ; empreinte_ordre", empreinte_ordre)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__)))
