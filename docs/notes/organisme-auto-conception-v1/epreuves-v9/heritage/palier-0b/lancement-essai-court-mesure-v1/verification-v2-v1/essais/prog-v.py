"""Programme factice du vérificateur.
Usage : prog-v.py SORTIES PAS_S OCTETS DUREE_S MODE MARQUEUR
MODE : simple | orphelin (un enfant A en session à part lance un petit-enfant B en session à part, puis A meurt aussitôt ;
B écrit des dossiers de source sous etape-4/couche-mecanique/bras-1-a-3/p9/0.0/ toutes les 0,2 s pendant 40 s)
"""
import os
import subprocess
import sys
import time

sorties, pas, octets, duree, mode, marqueur = sys.argv[1:7]
pas, octets, duree = float(pas), int(octets), float(duree)
os.makedirs(sorties)
d3 = os.path.join(sorties, "etape-3")
os.makedirs(d3)
with open(os.path.join(d3, "manifeste.json"), "w") as fh:
    fh.write("{}\n")
with open(os.path.join(d3, "manifeste.json.sha256"), "w") as fh:
    fh.write("0  manifeste.json\n")
os.makedirs(os.path.join(sorties, "etape-4"))
if mode == "orphelin":
    here = os.path.dirname(os.path.abspath(__file__))
    subprocess.Popen([sys.executable, os.path.join(here, "enfant-a.py"), sorties, marqueur], start_new_session=True,
                     stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
if mode in ("sourd-groupe", "sourd-hors", "docile-hors"):
    here = os.path.dirname(os.path.abspath(__file__))
    script = "enfant-docile.py" if mode == "docile-hors" else "enfant-sourd.py"
    subprocess.Popen([sys.executable, os.path.join(here, script), marqueur], start_new_session=(mode != "sourd-groupe"),
                     stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
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
