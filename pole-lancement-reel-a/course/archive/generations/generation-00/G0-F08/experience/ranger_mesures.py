#!/usr/bin/env python3
"""Range telles quelles les issues du monde (mesures.json) dans tirages.json.

Vérifie : fiche et engagement intacts, mesures.json lié à l'engagement gelé,
ordre d'exécution lié à l'engagement et cohérent avec empreinte_ordre.
Aucune mesure, aucun calcul de richesse.
"""
import hashlib
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
EMPREINTE_FICHE = "463c425fe6b6a7a8beeef533914068a13886b1ecd0d647173bdd293a14c625e5"
EMPREINTE_ENGAGEMENT = "796cab83d9068b33a36804a1842c25f76da684415b435aef86e2b217f1ec5aa2"


def sha_fichier(nom):
    with open(os.path.join(ICI, nom), "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def charger(nom):
    with open(os.path.join(ICI, nom), encoding="utf-8") as f:
        return json.load(f)


def echec(msg):
    sys.exit("ECHEC : " + msg)


def main():
    if sha_fichier("fiche.json") != EMPREINTE_FICHE:
        echec("fiche.json altérée")
    if sha_fichier("engagement.json") != EMPREINTE_ENGAGEMENT:
        echec("engagement.json altéré")

    engagement = charger("engagement.json")
    n = len(engagement["instances"])
    k = len(engagement.get("loi_predictive", {}).get("biais", [])) or 3

    ordre_doc = charger("ordre-execution.json")
    if ordre_doc.get("empreinte_engagement") != EMPREINTE_ENGAGEMENT:
        echec("ordre-execution.json non lié à l'engagement")
    ordre = ordre_doc["ordre"]
    if sorted(ordre) != list(range(n)):
        echec("ordre n'est pas une permutation du plan")
    empreinte_ordre = hashlib.sha256(
        json.dumps(ordre, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()

    mesures = charger("mesures.json")
    if mesures.get("empreinte_engagement") != EMPREINTE_ENGAGEMENT:
        echec("mesures.json non lié à l'engagement gelé")
    if mesures.get("empreinte_ordre") != empreinte_ordre:
        echec("empreinte_ordre de mesures.json incohérente avec ordre-execution.json")
    issues = mesures["issues"]
    if len(issues) != n:
        echec("nombre d'issues %d != %d instances" % (len(issues), n))
    if not all(isinstance(y, int) and 0 <= y < k for y in issues):
        echec("issue hors de l'espace des issues")

    tirages = {
        "empreinte_engagement": mesures["empreinte_engagement"],
        "issues": list(issues),  # telles quelles, indexées par instance
        "plan_execution": mesures["plan_execution"],
        "empreinte_ordre": mesures["empreinte_ordre"],
    }
    with open(os.path.join(ICI, "tirages.json"), "w", encoding="utf-8") as f:
        json.dump(tirages, f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write("\n")
    print("tirages.json écrit : %d issues, sha256=%s" % (n, sha_fichier("tirages.json")))


if __name__ == "__main__":
    main()
