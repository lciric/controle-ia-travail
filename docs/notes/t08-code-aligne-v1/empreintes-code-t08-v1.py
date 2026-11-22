"""Pièce des empreintes du code de T0.8 à un commit (forme de `brouillons/t08-code-compte4-v1/
empreintes-code-t08-453a71e1-v1.md`) : fichiers `src/controle_ia/t08/*.py` et `tests/test_t08_*.py`, octets lus par
`git show`, lignes et sha256. Écrit SORTIE (refus si elle existe : R12) et rien d'autre.

Usage : python empreintes-code-t08-v1.py COMMIT BRANCHE SORTIE
"""
from __future__ import annotations

import fnmatch
import hashlib
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

COMMIT, BRANCHE, SORTIE = sys.argv[1], sys.argv[2], Path(sys.argv[3])
if SORTIE.exists():
    sys.exit(f"ARRÊT : {SORTIE} existe déjà (R12)")
plein = subprocess.run(["git", "rev-parse", COMMIT], check=True, capture_output=True, text=True).stdout.strip()
noms = subprocess.run(["git", "ls-tree", "-r", "--name-only", plein, "--", "src/controle_ia/t08", "tests"], check=True,
                      capture_output=True, text=True).stdout.splitlines()
noms = sorted(n for n in noms if fnmatch.fnmatch(n, "src/controle_ia/t08/*.py") or fnmatch.fnmatch(n, "tests/test_t08_*.py"))
lignes = []
for n in noms:
    o = subprocess.run(["git", "show", f"{plein}:{n}"], check=True, capture_output=True).stdout
    lignes.append(f"| `{n}` | {o.count(b'\\n')} | `{hashlib.sha256(o).hexdigest()}` |")
quand = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
SORTIE.write_text(
    f"# Empreintes du code aligné de T0.8 au commit `{plein[:8]}` — v1\n\n"
    f"Écrite le {quand} (heure de la machine, UTC) par le développeur de l'alignement (modèle A), par "
    f"`docs/notes/t08-code-aligne-v1/empreintes-code-t08-v1.py`, sur la branche `{BRANCHE}`.\n\n"
    f"- Commit : `{plein}`.\n"
    f"- Fichiers : {len(noms)} (`src/controle_ia/t08/*.py`, `tests/test_t08_*.py`), octets lus par `git show`.\n\n"
    "| fichier | lignes | sha256 |\n|---|---|---|\n" + "\n".join(lignes) + "\n", encoding="utf-8")
print(SORTIE)
