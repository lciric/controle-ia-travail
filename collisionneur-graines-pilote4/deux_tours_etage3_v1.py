"""Deux tours (III.1 et III.2) de l'étage III du collisionneur v2.6, sans le III.3 : ordre de Lazar du 26 octobre 2026
(« étage III, deux tours (III.1 et III.2) », R-491). Écrit par l'instance de reprise de « session-depot ».

L'outil (`collisionneur_v2.py`, non modifié) enchaîne III.1, III.2 et III.3 dans `lancer_etage`, qui lit `ORDRE_ETAGE`
au moment de l'appel. Ce pilote charge l'outil, remplace pour l'étage III l'ordre des tours par (E3-T1, E3-T2), puis
appelle la commande `etage3` de l'outil lui-même : mêmes entrées versées une fois, même préambule, même plafond vérifié
avant chaque cellule, mêmes relances bornées, refus définitif ; l'ordre d'origine est rétabli à la sortie.
Usage : python -I -B deux_tours_etage3_v1.py OUTIL etage3 --sortie DOSSIER --faits FAITS --question QUESTION --plafond-usd 8
"""
import importlib.util
import sys

TOURS_GARDES = ("E3-T1", "E3-T2")


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
    if tuple(cv.ORDRE_ETAGE[3][:2]) != TOURS_GARDES:
        print(f"ordre de l'étage III inattendu : {cv.ORDRE_ETAGE[3]}", file=sys.stderr)
        return 1
    ancien = cv.ORDRE_ETAGE
    cv.ORDRE_ETAGE = {**ancien, 3: TOURS_GARDES}
    try:
        return cv.principal(argv[1:], appelants)
    finally:
        cv.ORDRE_ETAGE = ancien


if __name__ == "__main__":
    sys.exit(principal(sys.argv[1:]))
