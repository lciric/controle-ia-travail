"""Outil de travail du correcteur de la chaîne v4 (non versé) : remplacements exacts dans un fichier, chacun trouvé une
seule fois (sinon arrêt, fichier inchangé). Usage : python3 -I -B remplacer_v1.py FICHIER PAIRES.py
PAIRES.py définit P = [(ancien, nouveau), …]."""
import sys
from pathlib import Path
f, prog = sys.argv[1], sys.argv[2]
ns = {}
exec(Path(prog).read_text(encoding="utf-8"), ns)
t = Path(f).read_text(encoding="utf-8")
for i, (a, b) in enumerate(ns["P"]):
    n = t.count(a)
    if n != 1:
        raise SystemExit(f"paire {i} : trouvée {n} fois : {a[:80]!r}")
    t = t.replace(a, b)
Path(f).write_text(t, encoding="utf-8")
print(f"{f} : {len(ns['P'])} remplacement(s)")
