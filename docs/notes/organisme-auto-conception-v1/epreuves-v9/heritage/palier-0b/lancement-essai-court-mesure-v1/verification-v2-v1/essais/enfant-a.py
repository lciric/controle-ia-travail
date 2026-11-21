"""Enfant A : lance B en session à part puis meurt aussitôt."""
import os
import subprocess
import sys

sorties, marqueur = sys.argv[1:3]
here = os.path.dirname(os.path.abspath(__file__))
subprocess.Popen([sys.executable, os.path.join(here, "enfant-b.py"), sorties, marqueur], start_new_session=True,
                 stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
