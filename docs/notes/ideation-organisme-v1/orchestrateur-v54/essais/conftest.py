"""Configuration de pytest pour la v54 (CL18-15) : les essais n'écrivent plus dans l'arbre qu'ils contrôlent.

- Les dossiers temporaires des essais (`aides.BASE`, `essais/_tmp` jusqu'à la v53) sont redirigés vers un dossier neuf du
  système (`tempfile.mkdtemp`), supprimé en fin de session ; aucun fichier d'essai existant n'est modifié (R12) : la
  redirection se fait ici, avant l'import des modules d'essai, et sur l'attribut de classe `DOSSIER` de
  `test_v7_plomberie.GardeCodeEtShell` après la collecte.
- Aucun cache d'octets (`__pycache__`) n'est écrit : `sys.dont_write_bytecode` et `PYTHONDONTWRITEBYTECODE=1` pour les
  sous-processus.
"""

import atexit
import os
import shutil
import sys
import tempfile

sys.dont_write_bytecode = True
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

ICI = os.path.dirname(os.path.abspath(__file__))
ANCIEN = os.path.join(ICI, "_tmp")
NOUVEAU = tempfile.mkdtemp(prefix="pole-essais-v54-")
atexit.register(shutil.rmtree, NOUVEAU, True)

if ICI not in sys.path:
    sys.path.insert(0, ICI)
import aides as _aides  # noqa: E402

_aides.BASE = NOUVEAU
try:
    import essais.aides as _aides_paquet  # noqa: E402
    _aides_paquet.BASE = NOUVEAU
except ImportError:  # dossier joué hors paquet : seul `aides` existe
    pass


def pytest_collection_modifyitems(session, config, items):
    for item in items:
        cls = getattr(item, "cls", None)
        if cls is not None and getattr(cls, "DOSSIER", None) == ANCIEN:
            cls.DOSSIER = NOUVEAU
        mod = getattr(item, "module", None)
        if mod is not None and getattr(mod, "BASE", None) == ANCIEN:
            mod.BASE = NOUVEAU
