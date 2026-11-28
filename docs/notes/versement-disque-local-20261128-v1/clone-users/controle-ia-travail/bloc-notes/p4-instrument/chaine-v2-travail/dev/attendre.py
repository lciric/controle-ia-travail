# Outil de travail (non versé) : attend qu'un motif apparaisse dans chacun des fichiers nommés, ou un délai.
# Usage : python -B attendre.py DELAI_S MOTIF FICHIER...   (code 0 : motif vu partout ; 1 : délai écoulé)
import re
import sys
import time
from pathlib import Path

delai, motif, fichiers = float(sys.argv[1]), re.compile(sys.argv[2], re.M), [Path(x) for x in sys.argv[3:]]
fin = time.monotonic() + delai
while True:
    vus = [f for f in fichiers if f.exists() and motif.search(f.read_text(encoding="utf-8", errors="replace"))]
    if len(vus) == len(fichiers):
        print("motif vu dans", len(vus), "fichier(s)")
        sys.exit(0)
    if time.monotonic() > fin:
        print("délai écoulé ; motif vu dans", [f.name for f in vus])
        sys.exit(1)
    time.sleep(10)
