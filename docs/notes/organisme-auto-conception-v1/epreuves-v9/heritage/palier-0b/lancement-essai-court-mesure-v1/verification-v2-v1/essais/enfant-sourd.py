"""Enfant sourd : ignore le signal de fin ; écrit son identifiant dans MARQUEUR.pid, puis une ligne par seconde pendant 40 s."""
import os
import signal
import sys
import time

signal.signal(signal.SIGTERM, signal.SIG_IGN)
with open(sys.argv[1] + ".pid", "w") as fh:
    fh.write(str(os.getpid()) + "\n")
with open(sys.argv[1], "a") as fh:
    for i in range(40):
        fh.write(f"{i} {time.time():.3f}\n")
        fh.flush()
        time.sleep(1)
