"""Recopie autonome de boucle.empreinte_arbre (lecture des fichiers seulement) — contre-lecture 2 du pilote 4, v1."""
import hashlib, pathlib, sys
def empreinte(d):
    d = pathlib.Path(d); h = hashlib.sha256(); n = 0
    for f in sorted(p for p in d.rglob("*") if p.is_file() and p.suffix != ".pyc" and "__pycache__" not in p.relative_to(d).parts):
        h.update(str(f.relative_to(d)).encode("utf-8") + b"\0")
        h.update(hashlib.sha256(f.read_bytes()).hexdigest().encode("ascii") + b"\n"); n += 1
    return h.hexdigest(), n
for a in sys.argv[1:]:
    e, n = empreinte(a); print(e, n, a)
