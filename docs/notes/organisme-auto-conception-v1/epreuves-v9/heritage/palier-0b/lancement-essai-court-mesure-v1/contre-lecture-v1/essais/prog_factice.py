"""Programme factice du contre-lecteur : crée etape-3/manifeste.json, puis des dossiers de source au fil du temps.
Usage : prog_factice.py SORTIES PAS_S OCTETS_PAR_SOURCE DUREE_S ENFANT(0|1) ENFANT_PY MARQUEUR
"""
import os
import subprocess
import sys
import time

sorties, pas, octets, duree, enfant, enfant_py, marqueur = sys.argv[1:8]
pas, octets, duree = float(pas), int(octets), float(duree)
os.makedirs(sorties)
d3 = os.path.join(sorties, "etape-3")
os.makedirs(d3)
with open(os.path.join(d3, "manifeste.json"), "w") as fh:
    fh.write("{}\n")
with open(os.path.join(d3, "manifeste.json.sha256"), "w") as fh:
    fh.write("0  manifeste.json\n")
os.makedirs(os.path.join(sorties, "etape-4"))
if enfant == "1":
    subprocess.Popen([sys.executable, enfant_py, marqueur], start_new_session=True, stdin=subprocess.DEVNULL,
                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
if enfant == "2":
    subprocess.Popen([sys.executable, enfant_py, marqueur], stdin=subprocess.DEVNULL,
                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
base = os.path.join(sorties, "etape-4", "couche-mecanique", "bras-1-a-3", "p1", "0.0")
debut = time.monotonic()
s = 0
while time.monotonic() - debut < duree:
    d = os.path.join(base, str(s))
    os.makedirs(d)
    with open(os.path.join(d, "f.bin"), "wb") as fh:
        fh.write(b"x" * octets)
    s += 1
    time.sleep(pas)
