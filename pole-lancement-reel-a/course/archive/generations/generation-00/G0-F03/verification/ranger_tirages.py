#!/usr/bin/env python3
"""Range les issues déposées par le noyau (mesures.json) dans tirages.json.

Aucune mesure ni calcul de richesse : vérifications de liaison puis recopie telle quelle.
Usage : python3 -I ranger_tirages.py [dossier]
"""
import hashlib
import json
import os
import sys

D = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
EMPREINTE_FICHE = "6fae74c926f04a79d579c6665b01d37963229dc5a7077f5c5bb0691bbe07a512"
EMPREINTE_ENGAGEMENT = "4a8de271de43a6418f4f993358dcfb01a6bc425495d0824071e4004f7a95a8bc"


def sha_fichier(nom):
    with open(os.path.join(D, nom), "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def charger(nom):
    with open(os.path.join(D, nom), encoding="utf-8") as f:
        return json.load(f)


assert sha_fichier("fiche.json") == EMPREINTE_FICHE, "fiche.json altérée"
assert sha_fichier("engagement.json") == EMPREINTE_ENGAGEMENT, "engagement.json altéré"

engagement = charger("engagement.json")
ordre_doc = charger("ordre-execution.json")
mesures = charger("mesures.json")

n = len(engagement["instances"])
k = int(engagement["nombre_issues"])
ordre = ordre_doc["ordre"]
empreinte_ordre = hashlib.sha256(
    json.dumps(ordre, separators=(",", ":")).encode()).hexdigest()

assert ordre_doc["empreinte_engagement"] == EMPREINTE_ENGAGEMENT, "ordre non lié à l'engagement"
assert sorted(ordre) == list(range(n)), "ordre n'est pas une permutation du plan"
assert mesures["empreinte_engagement"] == EMPREINTE_ENGAGEMENT, "mesures non liées à l'engagement"
assert mesures["empreinte_ordre"] == empreinte_ordre, "mesures non liées à l'ordre"
assert mesures["plan_execution"] == engagement["plan_execution"] == "ordre_secret"
issues = mesures["issues"]
assert len(issues) == n, "nombre d'issues != nombre d'instances"
assert all(isinstance(y, int) and 0 <= y < k for y in issues), "issue hors domaine"

# Les issues sont déjà rangées par le noyau à l'indice de leur instance
# (instance ordre[s] traitée au temps s) : recopie telle quelle.
tirages = {
    "empreinte_engagement": EMPREINTE_ENGAGEMENT,
    "issues": list(issues),
    "plan_execution": mesures["plan_execution"],
    "empreinte_ordre": empreinte_ordre,
}
with open(os.path.join(D, "tirages.json"), "w", encoding="utf-8") as f:
    json.dump(tirages, f, indent=2, ensure_ascii=False)
    f.write("\n")
print("tirages.json écrit :", n, "issues ; empreinte_ordre", empreinte_ordre)
