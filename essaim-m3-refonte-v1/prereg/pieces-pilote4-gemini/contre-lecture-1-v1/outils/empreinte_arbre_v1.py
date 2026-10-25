"""Recopie autonome de boucle.empreinte_arbre (noyau b1c7f4b6, l. 70-78) : lit les fichiers, n'exécute rien."""
import hashlib, pathlib, sys
def empreinte_arbre(dossier):
    dossier = pathlib.Path(dossier)
    h = hashlib.sha256()
    for f in sorted(p for p in dossier.rglob("*") if p.is_file() and p.suffix != ".pyc" and "__pycache__" not in p.relative_to(dossier).parts):
        h.update(str(f.relative_to(dossier)).encode("utf-8") + b"\0")
        h.update(hashlib.sha256(f.read_bytes()).hexdigest().encode("ascii") + b"\n")
    return h.hexdigest()
for d in sys.argv[1:]:
    n = sum(1 for p in pathlib.Path(d).rglob("*") if p.is_file())
    print(empreinte_arbre(d), n, d)
