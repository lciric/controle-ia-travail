"""Vérifie, par compte seulement, que la liste réelle se lit sur `origin/main` du dépôt de l'organisme à son empreinte
scellée. N'affiche aucun nom. Usage : `python -B verifier_liste_sur_main_lot_2_v5.py`."""

import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "paquet", "orchestrator", "essais"))

import liste_reelle_na_v5 as L  # noqa: E402

lignes = L.lire_liste_reelle()
print(json.dumps({"source": f"{L.DEPOT_PAR_DEFAUT}@{L.REF_PAR_DEFAUT}", "empreinte_verifiee": L.EMPREINTE,
                  "lignes_de_motif": len(lignes)}, ensure_ascii=False))
