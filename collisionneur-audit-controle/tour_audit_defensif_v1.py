"""Étage III du collisionneur v2.6 avec un tour III.2 défensif : audit du programme de contrôle, ordre de Lazar du
26 octobre 2026 (« La partie à plusieurs modèles de l'audit (collisionneur, puis organisme) : go », R-504, R-509).
Écrit par l'instance de reprise de « session-depot ».

L'outil (`collisionneur_v2.py`, non modifié) demande au tour III.2, point (b), « les scénarios d'évasion : comment un
agent adverse tromperait chaque instrument ». Le plan de R-504 exclut tout procédé de contournement d'un moniteur. Ce
pilote charge l'outil, remplace ce seul point (b) de la consigne E3-T2 par une demande défensive (les hypothèses non
testées, avec la mesure qui les testerait), puis appelle la commande `etage3` de l'outil lui-même : mêmes tours,
mêmes entrées versées une fois, même plafond vérifié avant chaque cellule, mêmes relances bornées, refus définitif.
La consigne d'origine est rétablie à la sortie.
Usage : python -I -B tour_audit_defensif_v1.py OUTIL etage3 --sortie DOSSIER --faits FAITS --question QUESTION --plafond-usd 10
"""
import importlib.util
import sys

ANCIEN = ("(b) les scénarios d'évasion : comment un agent adverse tromperait chaque instrument, puis tous à la fois, "
          "et à quel coût ;")
NOUVEAU = ("(b) les hypothèses que la conception suppose sans les tester, chacune avec la mesure qui la testerait ; "
           "aucun procédé pour tromper un instrument n'est décrit (ni étapes, ni consignes, ni code) ;")


def charger(outil):
    cv = sys.modules.get("collisionneur_v2")  # essais : module déjà chargé
    if cv is None:
        spec = importlib.util.spec_from_file_location("collisionneur_v2", outil)
        cv = importlib.util.module_from_spec(spec)
        sys.modules["collisionneur_v2"] = cv
        spec.loader.exec_module(cv)
    return cv


def principal(argv, appelants=None):
    if len(argv) < 2 or argv[1] != "etage3":
        print(__doc__)
        return 1
    cv = charger(argv[0])
    ancienne = cv.CONSIGNES["E3-T2"]
    if ancienne.count(ANCIEN) != 1:
        print("consigne E3-T2 inattendue : point (b) introuvable", file=sys.stderr)
        return 1
    cv.CONSIGNES["E3-T2"] = ancienne.replace(ANCIEN, NOUVEAU)
    try:
        return cv.principal(argv[1:], appelants)
    finally:
        cv.CONSIGNES["E3-T2"] = ancienne


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:]))
