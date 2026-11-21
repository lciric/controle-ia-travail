"""Écrit, pour le livrable du lot 3 du véhicule NA-1, un compagnon `.sha256` par fichier (« empreinte  nom ») et la table
d'empreintes du dossier (« empreinte  chemin relatif »), avec son compagnon. Rien n'est écrit par-dessus (R12).

`python -B ecrire_compagnons_na_lot3_v3.py DOSSIER`

v3 : la liste des fichiers du livrable v3 (noms v3, plus le différentiel v2 → v3).
"""

import hashlib
import os
import sys

FICHIERS = (
    "paquet/orchestrator/pole/requete_na_v3.py",
    "paquet/orchestrator/pole/journal_na_v3.py",
    "paquet/orchestrator/essais/aides_na_lot3_v3.py",
    "paquet/orchestrator/essais/test_na_v3_requete.py",
    "paquet/orchestrator/essais/test_na_v3_journal.py",
    "paquet/orchestrator/essais/mutations_na_lot3_v3.py",
    "manifeste-paquet-vehicule-na-lot-3-v3.json",
    "appliquer_paquet_vehicule_na_lot_3_v3.py",
    "journal-essais-na-lot-3-v3.txt",
    "journal-mutations-na-lot-3-v3.json",
    "sonde_gabarit_servi_na_lot3_v3.py",
    "journal-sonde-gabarit-servi-na-lot-3-v3.json",
    "differentiel-lot-3-v2-v3.diff",
    "ecrire_compagnons_na_lot3_v3.py",
    "rapport-developpeur-lot-3-na-v3.md",
)
TABLE = "table-empreintes-dossier-na-lot-3-v3.txt"


def sha(chemin):
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def compagnon(chemin):
    h = sha(chemin)
    with open(chemin + ".sha256", "x", encoding="utf-8") as f:
        f.write(f"{h}  {os.path.basename(chemin)}\n")
    return h


def main(dossier):
    lignes = [f"{compagnon(os.path.join(dossier, rel))}  {rel}\n" for rel in FICHIERS]
    table = os.path.join(dossier, TABLE)
    with open(table, "x", encoding="utf-8") as f:
        f.write("".join(lignes))
    print(compagnon(table), TABLE)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
