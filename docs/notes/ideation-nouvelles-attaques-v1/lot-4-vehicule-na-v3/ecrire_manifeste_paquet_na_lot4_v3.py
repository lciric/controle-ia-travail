"""Écrit le manifeste du paquet v3 du lot 4 du véhicule NA-1 (`manifeste-paquet-vehicule-na-lot-4-v3.json`, neuf : R12).

`python -B ecrire_manifeste_paquet_na_lot4_v3.py COPIE` : `COPIE` est la copie de l'orchestrateur (commit de base, lots 2 v5,
3 v3 et 4 v1 posés par leurs programmes) qui fournit les empreintes des dépendances. Aucun réseau, aucune clé.
"""

import hashlib
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
PAQUET = ("orchestrator/pole/appel_garde_na_v3.py", "orchestrator/pole/adaptateur_claude_direct_na_v2.py",
          "orchestrator/essais/aides_na_lot4_v3.py", "orchestrator/essais/test_na_v3_appel_garde.py",
          "orchestrator/essais/test_na_v2_adaptateur_claude_direct.py", "orchestrator/essais/mutations_na_lot4_v3.py")
DEPENDANCES = ("orchestrator/pole/routage_na_v1.py", "orchestrator/pole/appel_garde_na_v1.py",
               "orchestrator/essais/aides_na_lot4_v1.py", "orchestrator/pole/garde_motifs_na_v4.py",
               "orchestrator/pole/journal_na_v3.py", "orchestrator/pole/requete_na_v3.py",
               "orchestrator/essais/aides_na_lot3_v3.py", "orchestrator/essais/aides_na_v4.py",
               "orchestrator/essais/liste-motifs-essai-na-v1.json")
EXISTANTS = ("orchestrator/pole/__init__.py", "orchestrator/pole/adaptateurs.py", "orchestrator/pole/caviardage.py",
             "orchestrator/pole/outils.py", "orchestrator/pole/relais.py", "orchestrator/pole/noyau_v56.py",
             "orchestrator/pole/suivi_roles_v54.py", "orchestrator/essais/__init__.py", "orchestrator/essais/conftest.py",
             "orchestrator/essais/aides.py", "orchestrator/essais/aides_v53.py", "orchestrator/essais/aides_v54.py",
             "orchestrator/essais/aides_v55.py", "orchestrator/essais/aides_v56.py")


def sha(chemin):
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def main(copie):
    sortie = os.path.join(ICI, "manifeste-paquet-vehicule-na-lot-4-v3.json")
    m = {"version": "manifeste-paquet-vehicule-na-lot-4-v3", "commit_base_orchestrateur": "a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb",
         "fichiers_du_paquet": [{"chemin": c, "chemin_paquet": "paquet/" + c, "sha256": sha(os.path.join(ICI, "paquet", c))}
                                for c in PAQUET],
         "dependances_lots_2_v5_3_v3_4_v1": [{"chemin": c, "sha256": sha(os.path.join(copie, c))} for c in DEPENDANCES],
         "fichiers_existants_lus": [{"chemin": c, "sha256": sha(os.path.join(copie, c))} for c in EXISTANTS]}
    with open(sortie, "x", encoding="utf-8") as f:
        f.write(json.dumps(m, ensure_ascii=False, sort_keys=True, indent=1) + "\n")
    print(sortie)


if __name__ == "__main__":
    main(sys.argv[1])
