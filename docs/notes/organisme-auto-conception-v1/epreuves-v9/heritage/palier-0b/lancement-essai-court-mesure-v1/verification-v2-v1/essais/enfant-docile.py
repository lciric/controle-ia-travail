"""Enfant docile : comportement par défaut au signal de fin ; écrit son identifiant dans MARQUEUR.pid, une ligne par seconde."""
import os
import sys
import time

with open(sys.argv[1] + ".pid", "w") as fh:
    fh.write(str(os.getpid()) + "\n")
with open(sys.argv[1], "a") as fh:
    for i in range(40):
        fh.write(f"{i} {time.time():.3f}\n")
        fh.flush()
        time.sleep(1)
