"""Applique une mutation (remplacement unique) à un fichier du clone jetable. Usage : python3 -I muter.py FICHIER AVANT APRES"""
import sys
from pathlib import Path
f, avant, apres = sys.argv[1:4]
t = Path(f).read_text(encoding="utf-8")
n = t.count(avant)
if n != 1:
    raise SystemExit(f"motif trouvé {n} fois : {avant[:80]!r}")
Path(f).write_text(t.replace(avant, apres), encoding="utf-8")
print("muté :", f)
