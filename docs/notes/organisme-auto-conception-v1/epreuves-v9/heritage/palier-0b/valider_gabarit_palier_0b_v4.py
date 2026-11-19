"""Passe un préenregistrement au validateur du gabarit du dépôt (`controle_ia.prereg.problemes`). Lecture seule.

Usage : PYTHONPATH=<dépôt>/src python3 -B valider_gabarit.py CHEMIN
"""
import sys

from controle_ia.prereg import problemes

for p in problemes(sys.argv[1]):
    print("remarque :", p)
print("fin du validateur")
