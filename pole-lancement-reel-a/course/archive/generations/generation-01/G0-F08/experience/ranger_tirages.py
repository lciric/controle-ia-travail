"""Rejouable : vérifie le lien mesures.json <-> engagement gelé et range les issues telles quelles.
Usage : python3 -I ranger_tirages.py  (depuis le dossier de l'expérience)
"""
import hashlib
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
EMPREINTE_FICHE = "463c425fe6b6a7a8beeef533914068a13886b1ecd0d647173bdd293a14c625e5"
EMPREINTE_ENGAGEMENT = "796cab83d9068b33a36804a1842c25f76da684415b435aef86e2b217f1ec5aa2"


def sha(nom):
    with open(os.path.join(ICI, nom), "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def charger(nom):
    with open(os.path.join(ICI, nom), encoding="utf-8") as f:
        return json.load(f)


def main():
    if sha("fiche.json") != EMPREINTE_FICHE:
        sys.exit("fiche.json altérée")
    if sha("engagement.json") != EMPREINTE_ENGAGEMENT:
        sys.exit("engagement.json altéré")
    m = charger("mesures.json")
    if m.get("empreinte_engagement") != EMPREINTE_ENGAGEMENT:
        sys.exit("mesures.json non lié à l'engagement gelé")
    issues = m["issues"]
    ordre = charger("ordre-execution.json")
    if ordre.get("empreinte_engagement") not in (None, EMPREINTE_ENGAGEMENT):
        sys.exit("ordre-execution.json non lié à l'engagement gelé")
    o = ordre.get("ordre")
    if o is not None and sorted(o) != list(range(len(issues))):
        sys.exit("ordre incohérent avec le nombre d'issues")
    sortie = {
        "empreinte_engagement": m["empreinte_engagement"],
        "issues": issues,  # déjà rangées à l'indice de leur instance, inchangées
        "plan_execution": m["plan_execution"],
        "empreinte_ordre": m["empreinte_ordre"],
    }
    with open(os.path.join(ICI, "tirages.json"), "w", encoding="utf-8") as f:
        json.dump(sortie, f, ensure_ascii=False, indent=1)
    print("tirages.json écrit :", len(issues), "issues ;", "sha256", sha("tirages.json"))


if __name__ == "__main__":
    main()
