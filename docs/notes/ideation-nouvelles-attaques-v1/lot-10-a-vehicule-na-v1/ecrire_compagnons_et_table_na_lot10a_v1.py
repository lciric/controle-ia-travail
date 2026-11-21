"""Écrit un compagnon `.sha256` pour chaque fichier livré du lot 10 a, puis la table d'empreintes du dossier et son compagnon.
Aucun fichier existant n'est écrasé (R12). Noms relatifs au dossier.

`python -B ecrire_compagnons_et_table_na_lot10a_v1.py`
"""

import hashlib
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
TABLE = "table-empreintes-dossier-na-lot-10-a-v1.txt"
LIVRES = (
    "paquet/orchestrator/pole/matiere_premiere_na_v1.py",
    "paquet/orchestrator/essais/aides_na_lot10a_v1.py",
    "paquet/orchestrator/essais/test_na_lot10a_v1_matiere_premiere.py",
    "paquet/orchestrator/essais/mutations_na_lot10a_v1.py",
    "manifeste-paquet-vehicule-na-lot-10-a-v1.json",
    "appliquer_paquet_vehicule_na_lot_10_a_v1.py",
    "ecrire_manifeste_paquet_na_lot10a_v1.py",
    "jouer_essais_lot_10_a_v1.py",
    "journal-essais-na-lot-10-a-v1.txt",
    "journal-mutations-na-lot-10-a-v1.json",
    "mesure-faux-refus-essai-na-lot-10-a-v1.json",
    "ecrire_compagnons_et_table_na_lot10a_v1.py",
    "rapport-developpeur-lot-10-a-na-v1.md",
)


def sha(chemin):
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def ecrire(chemin, texte):
    with open(chemin, "x", encoding="utf-8") as f:
        f.write(texte)


def main():
    lignes = []
    for rel in LIVRES:
        chemin = os.path.join(ICI, rel)
        s = sha(chemin)
        ecrire(chemin + ".sha256", f"{s}  {os.path.basename(rel)}\n")
        lignes.append(f"{s}  {rel}\n")
    ecrire(os.path.join(ICI, TABLE), "".join(lignes))
    s = sha(os.path.join(ICI, TABLE))
    ecrire(os.path.join(ICI, TABLE + ".sha256"), f"{s}  {TABLE}\n")
    print(f"{s}  {TABLE}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
