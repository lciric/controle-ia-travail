# Empreinte d'arbre, transcription de boucle.empreinte_arbre (noyau 8e5e2f7b, l. 98-106), lecture seule.
import hashlib, pathlib, sys
def empreinte_arbre(dossier):
    dossier = pathlib.Path(dossier)
    h = hashlib.sha256(); n = 0
    for f in sorted(p for p in dossier.rglob("*")
                    if p.is_file() and p.suffix != ".pyc" and "__pycache__" not in p.relative_to(dossier).parts):
        h.update(str(f.relative_to(dossier)).encode("utf-8") + b"\0")
        h.update(hashlib.sha256(f.read_bytes()).hexdigest().encode("ascii") + b"\n"); n += 1
    return h.hexdigest(), n
for d in sys.argv[1:]:
    e, n = empreinte_arbre(d)
    print(e, n, d)
