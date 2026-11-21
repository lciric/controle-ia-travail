"""Programme factice v3 (essais de l'erratum 2, correction 1) : écrit son identifiant dans MARQUEUR.pid, crée etape-3/manifeste.json
et son compagnon, puis un dossier de source toutes les PAS secondes pendant DUREE secondes ; peut, après GROS_APRES secondes,
écrire un gros fichier par blocs de 20 Mo (pour passer sous un seuil de place factice proche de la place libre réelle, sans
remplir le disque) ; peut ignorer le signal de fin.
Usage : prog-v3.py SORTIES MARQUEUR [--pas S] [--duree S] [--gros-apres S] [--gros-octets B] [--sourd]
"""
import argparse
import os
import signal
import sys
import time


def main(argv):
    p = argparse.ArgumentParser()
    p.add_argument("sorties")
    p.add_argument("marqueur")
    p.add_argument("--pas", type=float, default=0.5)
    p.add_argument("--duree", type=float, default=60)
    p.add_argument("--gros-apres", type=float, default=-1)
    p.add_argument("--gros-octets", type=int, default=0)
    p.add_argument("--sourd", action="store_true")
    a = p.parse_args(argv)
    if a.sourd:
        signal.signal(signal.SIGTERM, signal.SIG_IGN)
    with open(a.marqueur + ".pid", "x") as fh:
        fh.write(f"{os.getpid()}\n")
    os.makedirs(os.path.join(a.sorties, "etape-3"))
    with open(os.path.join(a.sorties, "etape-3", "manifeste.json"), "x") as fh:
        fh.write("{}\n")
    with open(os.path.join(a.sorties, "etape-3", "manifeste.json.sha256"), "x") as fh:
        fh.write("0  manifeste.json\n")
    base = os.path.join(a.sorties, "etape-4", "couche-mecanique", "bras-1-a-3", "p1", "0.0")
    os.makedirs(base)
    debut = time.monotonic()
    s = 0
    gros_fait = False
    while time.monotonic() - debut < a.duree:
        d = os.path.join(base, str(s))
        os.makedirs(d)
        with open(os.path.join(d, "f.bin"), "xb") as fh:
            fh.write(b"x" * 1000)
        with open(a.marqueur, "a") as fh:
            fh.write(f"{s} {time.time():.3f}\n")
        s += 1
        if a.gros_apres >= 0 and not gros_fait and time.monotonic() - debut >= a.gros_apres:
            gros_fait = True
            bloc = b"\0" * (20 * 1000 * 1000)
            with open(os.path.join(a.sorties, "etape-4", "gros.bin"), "xb") as fh:
                ecrits = 0
                while ecrits < a.gros_octets:
                    fh.write(bloc)
                    fh.flush()
                    os.fsync(fh.fileno())
                    ecrits += len(bloc)
        time.sleep(a.pas)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
