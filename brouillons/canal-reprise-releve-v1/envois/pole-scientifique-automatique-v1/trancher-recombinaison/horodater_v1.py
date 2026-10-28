"""Remplace le repère @@HEURE@@ d'un fichier par l'heure passée en argument, lue sur `date -u` dans la même commande.
Usage : python3 -I -B horodater_v1.py FICHIER "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
"""
import sys
from pathlib import Path

chemin, heure = Path(sys.argv[1]), sys.argv[2]
texte = chemin.read_text(encoding="utf-8")
if texte.count("@@HEURE@@") != 1:
    raise SystemExit(f"repère @@HEURE@@ absent ou multiple dans {chemin}")
chemin.write_text(texte.replace("@@HEURE@@", heure), encoding="utf-8")
print(chemin.name, heure)
