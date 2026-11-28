"""Greffon pytest (hors livrable) : lignes exécutées de tout fichier nommé `complements_p3_v1.py` (module et ses copies
dans les dépôts jetables), écrites à la fin dans `lignes-executees-b4.json` ; même méthode que la contre-lecture CB1."""
import json
import sys
import threading
from pathlib import Path

NOM = "complements_p3_v1.py"
LIGNES: set[int] = set()
SORTIE = Path(__file__).resolve().parent.parent / "essais" / "lignes-executees-cible.json"


def _local(frame, evenement, arg):
    if evenement == "line":
        LIGNES.add(frame.f_lineno)
    return _local


def _global(frame, evenement, arg):
    if frame.f_code.co_filename.rsplit("/", 1)[-1] == NOM:
        LIGNES.add(frame.f_lineno)
        return _local
    return None


def pytest_configure(config):
    sys.settrace(_global)
    threading.settrace(_global)


def pytest_unconfigure(config):
    sys.settrace(None)
    SORTIE.write_text(json.dumps(sorted(LIGNES)), encoding="utf-8")
