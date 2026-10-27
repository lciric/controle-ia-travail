"""Rejouable : vérifie le lien mesures.json <-> engagement gelé et range les issues telles quelles."""
import hashlib
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
EMPREINTE_FICHE = "b1032d8e3700b1427e7de429c8d2e8074634dd868b08da6fdb602f214052ec6e"
EMPREINTE_ENGAGEMENT = "8aca67b3d6e9431b083b28addae560755c0ccc1c72f6e9a67592426cef13d274"


def sha256_fichier(nom):
    with open(os.path.join(ICI, nom), "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def main():
    if sha256_fichier("fiche.json") != EMPREINTE_FICHE:
        sys.exit("fiche.json altérée")
    if sha256_fichier("engagement.json") != EMPREINTE_ENGAGEMENT:
        sys.exit("engagement.json altéré")
    with open(os.path.join(ICI, "mesures.json"), encoding="utf-8") as f:
        mesures = json.load(f)
    if mesures.get("empreinte_engagement") != EMPREINTE_ENGAGEMENT:
        sys.exit("mesures.json non lié à l'engagement gelé")
    with open(os.path.join(ICI, "ordre-execution.json"), encoding="utf-8") as f:
        ordre = json.load(f)
    if ordre.get("empreinte_engagement") != EMPREINTE_ENGAGEMENT:
        sys.exit("ordre-execution.json non lié à l'engagement gelé")
    if len(mesures["issues"]) != len(ordre["ordre"]):
        sys.exit("nombre d'issues différent de la longueur de l'ordre")
    tirages = {
        "empreinte_engagement": mesures["empreinte_engagement"],
        "issues": mesures["issues"],
        "plan_execution": mesures["plan_execution"],
        "empreinte_ordre": mesures["empreinte_ordre"],
    }
    with open(os.path.join(ICI, "tirages.json"), "w", encoding="utf-8") as f:
        json.dump(tirages, f, ensure_ascii=False, indent=1)
    print("tirages.json écrit :", len(tirages["issues"]), "issues")


if __name__ == "__main__":
    main()
