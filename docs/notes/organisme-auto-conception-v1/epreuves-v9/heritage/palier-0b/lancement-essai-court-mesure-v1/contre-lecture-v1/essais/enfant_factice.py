"""Enfant factice : écrit une ligne par seconde dans le marqueur pendant 40 s (nouvelle session, lancé par le programme factice)."""
import sys
import time

with open(sys.argv[1], "a") as fh:
    for i in range(40):
        fh.write(f"{i} {time.time():.3f}\n")
        fh.flush()
        time.sleep(1)
