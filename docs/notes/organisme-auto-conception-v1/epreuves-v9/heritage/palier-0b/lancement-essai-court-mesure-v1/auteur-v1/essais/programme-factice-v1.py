"""Programme factice de l'essai court : imite les noms du programme du palier 0b (etape-3/manifeste.json et compagnon, puis
etape-4/couche-mecanique/bras-1-a-3/<proposeur>/<dose>/<source>/), sans rien calculer.

Usage : programme-factice-v1.py SORTIES [--delai-etape-3 S] [--pas S] [--max-sources M] [--octets-par-source B]
                                 [--ignorer-terme] [--sans-fin]
Après M sources, écrit le manifeste de l'étape 4 et son compagnon, puis rend 0 (sauf --sans-fin : il attend sans fin).
"""
import argparse
import hashlib
import os
import signal
import sys
import time


def sceller(chemin, octets):
    with open(chemin, "xb") as fh:
        fh.write(octets)
    with open(chemin + ".sha256", "x", encoding="ascii") as fh:
        fh.write(f"{hashlib.sha256(octets).hexdigest()}  {os.path.basename(chemin)}\n")


def main(argv):
    p = argparse.ArgumentParser()
    p.add_argument("sorties")
    p.add_argument("--delai-etape-3", type=float, default=2)
    p.add_argument("--pas", type=float, default=1)
    p.add_argument("--max-sources", type=int, default=20)
    p.add_argument("--octets-par-source", type=int, default=4096)
    p.add_argument("--ignorer-terme", action="store_true")
    p.add_argument("--sans-fin", action="store_true")
    a = p.parse_args(argv)
    if a.ignorer_terme:
        signal.signal(signal.SIGTERM, signal.SIG_IGN)
    print(f"programme factice : processus {os.getpid()}, groupe {os.getpgid(0)}, ignore le signal de fin : "
          f"{a.ignorer_terme}", flush=True)
    if os.path.exists(a.sorties):
        print("dossier déjà présent : arrêt", flush=True)
        return 1
    os.makedirs(os.path.join(a.sorties, "etape-3"))
    time.sleep(a.delai_etape_3)
    sceller(os.path.join(a.sorties, "etape-3", "rapport-factice.json"), b'{"factice": true}\n')
    sceller(os.path.join(a.sorties, "etape-3", "manifeste.json"), b'{"etape": "3", "factice": true}\n')
    base = os.path.join(a.sorties, "etape-4", "couche-mecanique", "bras-1-a-3")
    os.makedirs(base)
    for i in range(a.max_sources):
        d = os.path.join(base, f"proposeur-{i // 216}", f"dose-{(i // 36) % 6}", f"source-{i % 36:02d}")
        os.makedirs(d)
        with open(os.path.join(d, "sortie.npy"), "xb") as fh:
            fh.write(b"\0" * a.octets_par_source)
        time.sleep(a.pas)
    if a.sans_fin:
        while True:
            time.sleep(1)
    sceller(os.path.join(a.sorties, "etape-4", "manifeste.json"), b'{"etape": "4", "factice": true}\n')
    print("programme factice : fin normale", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
