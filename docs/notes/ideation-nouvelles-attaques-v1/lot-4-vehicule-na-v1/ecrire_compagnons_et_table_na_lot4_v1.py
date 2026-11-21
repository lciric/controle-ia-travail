"""Compagnons `.sha256` et table d'empreintes du dossier du lot 4 du véhicule NA-1 (v1).

`python -B ecrire_compagnons_et_table_na_lot4_v1.py` : pour chaque fichier livré, écrit son compagnon s'il n'existe pas (un
compagnon existant doit porter la même empreinte, sinon refus) ; puis écrit la table (fichier neuf) et son compagnon.
Chemins relatifs au dossier ; aucun chemin complet n'est écrit.
"""

import hashlib
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
LIVRES = (
    "paquet/orchestrator/pole/routage_na_v1.py",
    "paquet/orchestrator/pole/appel_garde_na_v1.py",
    "paquet/orchestrator/pole/adaptateur_claude_na_v1.py",
    "paquet/orchestrator/pole/faux_fournisseur_na_v1.py",
    "paquet/orchestrator/pole/releve_sans_systeme_na_v1.py",
    "paquet/orchestrator/essais/aides_na_lot4_v1.py",
    "paquet/orchestrator/essais/test_na_v1_appel_garde.py",
    "paquet/orchestrator/essais/test_na_v1_adaptateur_claude.py",
    "paquet/orchestrator/essais/mutations_na_lot4_v1.py",
    "manifeste-paquet-vehicule-na-lot-4-v1.json",
    "appliquer_paquet_vehicule_na_lot_4_v1.py",
    "ecrire_manifeste_paquet_na_lot4_v1.py",
    "ecrire_compagnons_et_table_na_lot4_v1.py",
    "journal-essais-na-lot-4-v1.txt",
    "journal-mutations-na-lot-4-v1.json",
    "releve-faux-fournisseur-na-lot-4-v1/releve-sans-systeme-na-v1.json",
    "rapport-developpeur-lot-4-na-v1.md",
)
TABLE = "table-empreintes-dossier-na-lot-4-v1.txt"


def sha(chemin):
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def main():
    lignes = []
    for rel in LIVRES:
        chemin = os.path.join(ICI, rel)
        s = sha(chemin)
        compagnon = chemin + ".sha256"
        if os.path.exists(compagnon):
            with open(compagnon, encoding="utf-8") as f:
                if f.read().split()[0] != s:
                    print(f"refus : compagnon différent pour {rel}", file=sys.stderr)
                    return 2
        else:
            with open(compagnon, "x", encoding="utf-8") as f:
                f.write(f"{s}  {os.path.basename(rel)}\n")
        lignes.append(f"{s}  {rel}\n")
    table = os.path.join(ICI, TABLE)
    with open(table, "x", encoding="utf-8") as f:
        f.writelines(lignes)
    with open(table + ".sha256", "x", encoding="utf-8") as f:
        f.write(f"{sha(table)}  {TABLE}\n")
    print(sha(table))
    return 0


if __name__ == "__main__":
    sys.exit(main())
