#!/usr/bin/env python3
"""G1-F03 : range telles quelles les issues deposees par le noyau dans tirages.json.

Verifie : empreinte de fiche.json et engagement.json, liaison de mesures.json et
ordre-execution.json a l'engagement, empreinte de l'ordre, permutation complete,
issues dans {0..nombre_issues-1}. Aucune issue n'est calculee ni modifiee.
"""
import hashlib
import json
import sys

FICHE_SHA = "5b679414b5153326eba8b351396c49d73626eaebbc30f4751debf5df72444d62"
ENGAGEMENT_SHA = "1f2439cb9510cbbe02c64826faf89504b0a9a755458cc4a937fc618ddef705d6"


def sha_file(p):
    with open(p, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def main():
    assert sha_file("fiche.json") == FICHE_SHA, "fiche.json altérée"
    assert sha_file("engagement.json") == ENGAGEMENT_SHA, "engagement.json altéré"
    eng = json.load(open("engagement.json"))
    assert eng["empreinte_fiche"] == FICHE_SHA
    n_inst = len(eng["instances"])
    k = eng["nombre_issues"]

    mes = json.load(open("mesures.json"))
    assert mes["empreinte_engagement"] == ENGAGEMENT_SHA, "mesures.json non lié à l'engagement"
    ordre_doc = json.load(open("ordre-execution.json"))
    assert ordre_doc["empreinte_engagement"] == ENGAGEMENT_SHA
    ordre = ordre_doc["ordre"]
    assert sorted(ordre) == list(range(n_inst)), "ordre non permutation du plan"
    emp_ordre = hashlib.sha256(json.dumps(ordre, separators=(",", ":")).encode()).hexdigest()
    assert mes["empreinte_ordre"] == emp_ordre, "empreinte d'ordre incohérente"
    assert mes["plan_execution"] == eng["plan_execution"] == "ordre_secret"

    issues = mes["issues"]
    assert len(issues) == n_inst
    assert all(isinstance(y, int) and 0 <= y < k for y in issues)

    sortie = {
        "empreinte_engagement": mes["empreinte_engagement"],
        "issues": issues,
        "plan_execution": mes["plan_execution"],
        "empreinte_ordre": mes["empreinte_ordre"],
    }
    with open("tirages.json", "w") as f:
        json.dump(sortie, f, ensure_ascii=False)
    print("tirages.json écrit :", len(issues), "issues ; ordre", emp_ordre)


if __name__ == "__main__":
    sys.exit(main())
