"""Essai de la fonction gelée `lire_une_note` (rubrique.py, l. 44-60) sur des valeurs nettoyées de la règle RS1.

Usage : PYTHONPATH=<clone>/src python essai_lire_une_note.py
Aucune réponse de juge n'est lue : les valeurs sont écrites ici, à la main.
"""
from controle_ia.environnements.rubrique import lire_une_note

CAS = ["3", "4.0", "4/5", "4/4", "4.5", "6", "-1", "−1", "2 of the proposals", "3 - 4", "3 or 4", "3 to 4",
       "3-4", "3–4", "3 (competent)", "4, solid", "<4>", ""]
for c in CAS:
    print(f"{c!r:24} -> {lire_une_note(c, 0, 5)!r}")
