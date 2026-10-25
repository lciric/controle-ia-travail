"""Contre-lecture banque v2 — c7 : `essaim_m3.banque.verifier_banque` (code du dépôt, importé en lecture) sur la v1, la v2
et la variante triée par identifiant v2 écrite par c6 (correction proposée) ; aucune écriture.
Usage : python3 -I -B c7_verifier_banque_v1.py RACINE_CODE FICHIER…
"""
import pathlib
import sys

sys.path.insert(0, sys.argv[1])
from essaim_m3.banque import verifier_banque  # noqa: E402

for f in sys.argv[2:]:
    pb = verifier_banque(pathlib.Path(f))
    print(f"{pathlib.Path(f).name} : {'banque conforme' if not pb else pb}")
