"""Écrit le manifeste du paquet v1 du lot 10 a du véhicule NA-1 (manière de la v68 et des lots 2 à 5).

`python -B ecrire_manifeste_paquet_na_lot10a_v1.py COPIE` : `COPIE` est la copie de l'orchestrateur où les lots 2 v5, 3 v3,
4 v1 et 5 v1 sont posés par leurs programmes, **sans** le paquet du lot 10 a. Le manifeste voisin ne doit pas exister (R12).
Il porte les empreintes des fichiers du paquet, celles des dépendances des lots 2 à 5 et celles des fichiers existants de
l'orchestrateur que lisent les essais, toutes recalculées ici.
"""

import hashlib
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
SORTIE = os.path.join(ICI, "manifeste-paquet-vehicule-na-lot-10-a-v1.json")
PAQUET = ("orchestrator/pole/matiere_premiere_na_v1.py", "orchestrator/essais/aides_na_lot10a_v1.py",
          "orchestrator/essais/test_na_lot10a_v1_matiere_premiere.py", "orchestrator/essais/mutations_na_lot10a_v1.py")
DEPENDANCES = (
    ("orchestrator/pole/identifiants_na_v1.py", "1, inchangé dans le lot 2 v5"),
    ("orchestrator/pole/tirage_na_v4.py", "2 v5"), ("orchestrator/pole/garde_motifs_na_v4.py", "2 v5"),
    ("orchestrator/pole/ignorables-unicode-15.1.0-na-v1.json", "2 v5"), ("orchestrator/essais/aides_na_v4.py", "2 v5"),
    ("orchestrator/essais/liste-motifs-essai-na-v1.json", "2 v5"),
    ("orchestrator/pole/requete_na_v3.py", "3 v3"), ("orchestrator/pole/journal_na_v3.py", "3 v3"),
    ("orchestrator/essais/aides_na_lot3_v3.py", "3 v3"),
    ("orchestrator/pole/routage_na_v1.py", "4 v1"), ("orchestrator/pole/appel_garde_na_v1.py", "4 v1"),
    ("orchestrator/essais/aides_na_lot4_v1.py", "4 v1"),
    ("orchestrator/pole/lecteur_fiches_na_v1.py", "5 v1"), ("orchestrator/pole/contrat_fiche_na_v1.py", "5 v1"),
    ("orchestrator/pole/portier_na_v1.py", "5 v1"), ("orchestrator/pole/registre_na_v1.py", "5 v1"),
    ("orchestrator/pole/verifier_registre_servi_na_v1.py", "5 v1"),
)
EXISTANTS = ("orchestrator/pole/__init__.py", "orchestrator/pole/noyau_v56.py", "orchestrator/pole/relais.py",
             "orchestrator/pole/adaptateurs.py", "orchestrator/pole/suivi_roles_v54.py")


def sha(chemin):
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def main(copie):
    for rel in PAQUET:
        if os.path.exists(os.path.join(copie, rel)):
            print("la copie porte déjà le paquet du lot 10 a : refus", file=sys.stderr)
            return 2
    m = {"version": "manifeste-paquet-vehicule-na-lot-10-a-v1",
         "objet": "véhicule NA-1, lot 10 a : colonne « matière première », chargement et garde ; essais et mutations",
         "base": {"commit_orchestrateur": "a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb", "dossier": "orchestrator",
                  "lots_poses_avant": ["lot 2 v5", "lot 3 v3", "lot 4 v1", "lot 5 v1"]},
         "donnees_d_essai": "registre d'essai aux lignes inertes, pièce de relevés d'essai, libellé d'essai de la sixième "
                            "ligne, conditions d'allumage et manifeste de lecture de fin d'essai : déclarés comme tels",
         "fichiers_du_paquet": [{"chemin": r, "chemin_paquet": "paquet/" + r, "sha256": sha(os.path.join(ICI, "paquet", r))}
                                for r in PAQUET],
         "dependances_lots_2_a_5": [{"chemin": r, "sha256": sha(os.path.join(copie, r)), "lot": l} for r, l in DEPENDANCES],
         "fichiers_existants_lus": [{"chemin": r, "sha256": sha(os.path.join(copie, r))} for r in EXISTANTS]}
    with open(SORTIE, "x", encoding="utf-8") as f:
        f.write(json.dumps(m, ensure_ascii=False, indent=1) + "\n")
    print(json.dumps({"ecrit": os.path.basename(SORTIE)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
