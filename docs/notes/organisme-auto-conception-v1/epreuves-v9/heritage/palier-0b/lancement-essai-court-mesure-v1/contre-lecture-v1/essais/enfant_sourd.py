"""Enfant factice du même groupe, qui ignore le signal de fin : écrit une ligne par seconde pendant 40 s."""
import signal
import sys
import time

signal.signal(signal.SIGTERM, signal.SIG_IGN)
with open(sys.argv[1], "a") as fh:
    for i in range(40):
        fh.write(f"{i} {time.time():.3f}\n")
        fh.flush()
        time.sleep(1)
