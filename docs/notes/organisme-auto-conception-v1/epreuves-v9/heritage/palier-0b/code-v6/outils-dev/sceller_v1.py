"""Outil : écrit, pour chaque fichier donné, son compagnon `F.sha256` au format de `sha256sum` lancé dans le dossier du fichier
(« empreinte␣␣nom »). Jamais d'écrasement : un compagnon déjà présent et identique est laissé ; différent, arrêt. Imprime
« empreinte  chemin relatif au premier argument » pour chaque fichier. Arguments : racine, puis les fichiers."""
import hashlib
import os
import sys

racine = sys.argv[1]
for chemin in sys.argv[2:]:
    with open(chemin, "rb") as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    ligne = f"{sha}  {os.path.basename(chemin)}\n"
    compagnon = chemin + ".sha256"
    if os.path.exists(compagnon):
        with open(compagnon, encoding="ascii") as f:
            if f.read() != ligne:
                raise SystemExit(f"compagnon déjà présent et différent : {compagnon}")
    else:
        with open(compagnon, "x", encoding="ascii") as f:
            f.write(ligne)
    print(f"{sha}  {os.path.relpath(chemin, racine)}")
