"""Écrit le compagnon `.sha256` de chaque fichier livré du lot 5 du véhicule NA-1, puis la table d'empreintes du dossier et
son compagnon. Rien n'est écrasé (R12) : un compagnon ou une table déjà présents font refuser.

`python -B ecrire_compagnons_lot_5_v1.py DOSSIER`
"""

import hashlib
import os
import sys

LIVRES = (
    "rapport-developpeur-lot-5-na-v1.md",
    "manifeste-paquet-vehicule-na-lot-5-v1.json",
    "appliquer_paquet_vehicule_na_lot_5_v1.py",
    "jouer_essais_lot_5_v1.py",
    "ecrire_compagnons_lot_5_v1.py",
    "journal-essais-na-lot-5-v1.txt",
    "journal-mutations-na-lot-5-v1.json",
    "paquet/orchestrator/pole/lecteur_fiches_na_v1.py",
    "paquet/orchestrator/pole/contrat_fiche_na_v1.py",
    "paquet/orchestrator/pole/portier_na_v1.py",
    "paquet/orchestrator/pole/registre_na_v1.py",
    "paquet/orchestrator/pole/verifier_registre_servi_na_v1.py",
    "paquet/orchestrator/essais/aides_na_lot5_v1.py",
    "paquet/orchestrator/essais/test_na_lot5_v1_lecteur.py",
    "paquet/orchestrator/essais/test_na_lot5_v1_contrat.py",
    "paquet/orchestrator/essais/test_na_lot5_v1_portier.py",
    "paquet/orchestrator/essais/test_na_lot5_v1_registre.py",
    "paquet/orchestrator/essais/test_na_lot5_v1_identifiants.py",
    "paquet/orchestrator/essais/mutations_na_lot5_v1.py",
)
TABLE = "table-empreintes-dossier-na-lot-5-v1.txt"


def sha(chemin):
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def ecrire(chemin, texte):
    with open(chemin, "x", encoding="utf-8") as f:
        f.write(texte)


def main(argv):
    if len(argv) != 1:
        print("usage : ecrire_compagnons_lot_5_v1.py DOSSIER", file=sys.stderr)
        return 2
    d = argv[0]
    cibles = [os.path.join(d, r + ".sha256") for r in LIVRES] + [os.path.join(d, TABLE), os.path.join(d, TABLE + ".sha256")]
    if any(os.path.exists(c) for c in cibles):
        print("compagnon ou table déjà présents : on n'écrase jamais (R12)", file=sys.stderr)
        return 2
    lignes = []
    for r in LIVRES:
        e = sha(os.path.join(d, r))
        ecrire(os.path.join(d, r + ".sha256"), f"{e}  {os.path.basename(r)}\n")
        lignes.append(f"{e}  {r}\n")
    ecrire(os.path.join(d, TABLE), "".join(lignes))
    ecrire(os.path.join(d, TABLE + ".sha256"), f"{sha(os.path.join(d, TABLE))}  {TABLE}\n")
    print(f"{len(LIVRES)} compagnons ; table {sha(os.path.join(d, TABLE))}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
