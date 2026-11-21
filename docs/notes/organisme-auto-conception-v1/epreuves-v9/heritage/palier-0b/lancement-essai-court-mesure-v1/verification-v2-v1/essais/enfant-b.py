"""Enfant B (orphelin, session à part) : écrit son identifiant dans le marqueur, puis crée un dossier de source toutes les 0,2 s."""
import os
import sys
import time

sorties, marqueur = sys.argv[1:3]
with open(marqueur + ".pid", "w") as fh:
    fh.write(str(os.getpid()) + "\n")
base = os.path.join(sorties, "etape-4", "couche-mecanique", "bras-1-a-3", "p9", "0.0")
os.makedirs(base, exist_ok=True)
for i in range(200):
    os.makedirs(os.path.join(base, str(i)), exist_ok=True)
    time.sleep(0.2)
