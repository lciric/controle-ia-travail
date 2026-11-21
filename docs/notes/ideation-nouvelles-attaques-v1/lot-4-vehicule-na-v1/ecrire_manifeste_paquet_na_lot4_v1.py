"""Écrit le manifeste du paquet v1 du lot 4 du véhicule NA-1 (fichier neuf, jamais par-dessus : R12).

`python -B ecrire_manifeste_paquet_na_lot4_v1.py COPIE_DE_BASE` : COPIE_DE_BASE est la copie de l'orchestrateur (le dossier qui
contient `orchestrator/`) sur laquelle le lot 2 v5 et le lot 3 v3 sont posés ; les empreintes des dépendances et des fichiers
existants lus y sont prises ; celles du paquet, dans le paquet voisin.
"""

import hashlib
import json
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
FICHIERS = (
    "orchestrator/pole/routage_na_v1.py", "orchestrator/pole/appel_garde_na_v1.py",
    "orchestrator/pole/adaptateur_claude_na_v1.py", "orchestrator/pole/faux_fournisseur_na_v1.py",
    "orchestrator/pole/releve_sans_systeme_na_v1.py", "orchestrator/essais/aides_na_lot4_v1.py",
    "orchestrator/essais/test_na_v1_appel_garde.py", "orchestrator/essais/test_na_v1_adaptateur_claude.py",
    "orchestrator/essais/mutations_na_lot4_v1.py",
)
DEPENDANCES = (  # lot 2 v5 et lot 3 v3, posés par leurs programmes
    "orchestrator/pole/garde_motifs_na_v4.py", "orchestrator/pole/garde_motifs_na_v3.py", "orchestrator/pole/tirage_na_v4.py",
    "orchestrator/pole/identifiants_na_v1.py", "orchestrator/pole/ignorables-unicode-15.1.0-na-v1.json",
    "orchestrator/pole/requete_na_v3.py", "orchestrator/pole/journal_na_v3.py", "orchestrator/essais/aides_na_v4.py",
    "orchestrator/essais/liste-motifs-essai-na-v1.json", "orchestrator/essais/aides_na_lot3_v3.py",
)
EXISTANTS = (  # orchestrateur du commit de base, lus seulement
    "orchestrator/pole/__init__.py", "orchestrator/pole/noyau_v56.py", "orchestrator/pole/adaptateurs.py",
    "orchestrator/pole/adaptateurs_v56.py", "orchestrator/pole/suivi_roles_v54.py", "orchestrator/pole/relais.py",
    "orchestrator/pole/relais_reel.py", "orchestrator/pole/caviardage.py", "orchestrator/pole/outils.py",
    "orchestrator/pole/course2_v56.py", "orchestrator/pole/configuration_v56.py", "orchestrator/essais/aides_v56.py",
    "orchestrator/essais/conftest.py",
)


def sha(chemin):
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def main(argv):
    if len(argv) != 1:
        print("usage : ecrire_manifeste_paquet_na_lot4_v1.py COPIE_DE_BASE", file=sys.stderr)
        return 2
    base = argv[0]
    m = {"version": "manifeste-paquet-vehicule-na-lot-4-v1", "commit_base_orchestrateur": "a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb",
         "fichiers_du_paquet": [{"chemin": f, "chemin_paquet": "paquet/" + f, "sha256": sha(os.path.join(ICI, "paquet", f))}
                                for f in FICHIERS],
         "dependances_lot_2_v5_et_lot_3_v3": [{"chemin": f, "sha256": sha(os.path.join(base, f))} for f in DEPENDANCES],
         "fichiers_existants_lus": [{"chemin": f, "sha256": sha(os.path.join(base, f))} for f in EXISTANTS]}
    with open(os.path.join(ICI, "manifeste-paquet-vehicule-na-lot-4-v1.json"), "x", encoding="utf-8") as f:
        f.write(json.dumps(m, ensure_ascii=False, indent=1) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
