"""Vérifie chaque compagnon .sha256 d'un dossier (récursif) contre le fichier voisin ; signale les fichiers sans compagnon."""
import hashlib, pathlib, sys

racine = pathlib.Path(sys.argv[1])
ok = ko = sans = 0
for f in sorted(racine.rglob("*")):
    if not f.is_file():
        continue
    if f.suffix == ".sha256":
        ligne = f.read_text().split()
        attendu, nom = ligne[0], ligne[1]
        cible = f.parent / nom
        if not cible.exists():
            print("CIBLE ABSENTE", f); ko += 1; continue
        reel = hashlib.sha256(cible.read_bytes()).hexdigest()
        if reel == attendu:
            ok += 1
        else:
            print("DIVERGE", cible, attendu, reel); ko += 1
    else:
        if not (f.parent / (f.name + ".sha256")).exists():
            print("SANS COMPAGNON", f); sans += 1
print(f"ok={ok} ko={ko} sans_compagnon={sans}")
for f in sorted(racine.rglob("*")):
    if f.is_file() and f.suffix != ".sha256":
        print(hashlib.sha256(f.read_bytes()).hexdigest(), f.relative_to(racine))
