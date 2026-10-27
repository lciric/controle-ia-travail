#!/usr/bin/env python3
"""Rejouable : vérifie que mesures.json est lié à l'engagement gelé et range
les issues déposées par le noyau, telles quelles, dans tirages.json.
Aucune mesure, aucun calcul de richesse. À lancer dans le dossier de l'expérience."""
import hashlib
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
EMPREINTE_FICHE = "6fae74c926f04a79d579c6665b01d37963229dc5a7077f5c5bb0691bbe07a512"
EMPREINTE_ENGAGEMENT = "4a8de271de43a6418f4f993358dcfb01a6bc425495d0824071e4004f7a95a8bc"


def sha256(nom):
    with open(os.path.join(ICI, nom), "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def charger(nom):
    with open(os.path.join(ICI, nom), encoding="utf-8") as f:
        return json.load(f)


def main():
    if sha256("fiche.json") != EMPREINTE_FICHE:
        sys.exit("fiche.json altérée")
    if sha256("engagement.json") != EMPREINTE_ENGAGEMENT:
        sys.exit("engagement.json altéré")
    mesures = charger("mesures.json")
    if mesures.get("empreinte_engagement") != EMPREINTE_ENGAGEMENT:
        sys.exit("mesures.json non lié à l'engagement gelé")
    ordre = charger("ordre-execution.json")
    if ordre.get("empreinte_engagement") != EMPREINTE_ENGAGEMENT:
        sys.exit("ordre-execution.json non lié à l'engagement gelé")
    issues = mesures["issues"]
    n = len(ordre["ordre"])
    if len(issues) != n or sorted(ordre["ordre"]) != list(range(n)):
        sys.exit("taille des issues / ordre incohérente")
    tirages = {
        "empreinte_engagement": mesures["empreinte_engagement"],
        "issues": issues,  # rangées à l'indice de leur instance, telles quelles
        "plan_execution": mesures["plan_execution"],
        "empreinte_ordre": mesures["empreinte_ordre"],
    }
    with open(os.path.join(ICI, "tirages.json"), "w", encoding="utf-8") as f:
        json.dump(tirages, f, ensure_ascii=False, indent=1)
    print("tirages.json écrit :", len(issues), "issues")


if __name__ == "__main__":
    main()
