#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Écrit le compagnon `.sha256` de chaque pièce rendue, nommée une par une — v1.

Aucun parcours de dossier : la liste est écrite ici. Refus si une pièce manque ou si un
compagnon existe déjà (on n'écrase jamais). Usage : python3 -B ecrire_compagnons_v1.py
"""
import hashlib
import os
import sys

PIECES = [
    "criteres-choix-cartes-v9-v4.md",
    "note-conception-juge-selection-cartes-ecartees-v4.md",
    "assemblage_selection_v4_v1.py",
    "essais_assemblage_selection_v4_v1.py",
    "essais-assemblage-selection-v4-sortie-v1.txt",
    "masque_style_cartes_v1.py",
    "essais_masque_style_cartes_v1.py",
    "essais-masque-style-cartes-sortie-v1.txt",
    "lecteur_par_programme_cartes_v1.py",
    "essais_lecteur_par_programme_cartes_v1.py",
    "essais-lecteur-par-programme-cartes-sortie-v1.txt",
    "mesure_faux_declenchement_gardes_v1.py",
    "mesure-faux-declenchement-gardes-sortie-v1.txt",
    "construire_par_lignes_v1.py",
    "operations-criteres-v3-vers-v4-v1.txt",
    "operations-note-v3-vers-v4-v1.txt",
    "rapport-redacteur-criteres-v4-note-v4-v1.md",
    "ecrire_compagnons_v1.py",
]


def main():
    ici = os.path.dirname(os.path.abspath(__file__))
    for nom in PIECES:
        if not os.path.isfile(os.path.join(ici, nom)):
            print(f"REFUS : pièce absente : {nom}", file=sys.stderr)
            return 2
        if os.path.exists(os.path.join(ici, nom + ".sha256")):
            print(f"REFUS : compagnon déjà présent : {nom}.sha256", file=sys.stderr)
            return 2
    for nom in PIECES:
        with open(os.path.join(ici, nom), "rb") as f:
            h = hashlib.sha256(f.read()).hexdigest()
        with open(os.path.join(ici, nom + ".sha256"), "x", encoding="utf-8") as f:
            f.write(f"{h}  {nom}\n")
        print(f"{h}  {nom}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
