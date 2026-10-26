"""Cherche dans un dossier les valeurs des clés nommées (lues dans l'environnement) ; n'affiche que des comptes."""
import os, sys, pathlib
noms = [n for n in os.environ if any(m in n for m in ("API_KEY", "WORKSPACE_ID"))]
vals = [os.environ[n].encode() for n in noms if len(os.environ[n]) >= 12]
formes = [b"sk-ant-", b"AIza"]
n_val = n_forme = 0
for p in pathlib.Path(sys.argv[1]).rglob("*"):
    if p.is_file():
        b = p.read_bytes()
        n_val += sum(v in b for v in vals)
        n_forme += sum(f in b for f in formes)
print(f"noms cherchés {len(vals)} ; valeurs trouvées {n_val} ; formes de clés trouvées {n_forme}")
sys.exit(1 if n_val or n_forme else 0)
