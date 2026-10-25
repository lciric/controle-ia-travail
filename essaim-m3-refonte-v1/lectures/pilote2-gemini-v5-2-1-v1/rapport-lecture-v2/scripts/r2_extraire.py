"""r2 — extraction d'une archive fermée dans un dossier neuf (filtre « data »), sans exécution.

Usage : python3 -I r2_extraire.py ARCHIVE EMPREINTE_ATTENDUE DOSSIER_NEUF
Refuse si l'empreinte diffère ou si le dossier existe déjà ; compte les fichiers extraits
contre les membres de l'archive.
"""
import hashlib
import os
import sys
import tarfile


def sha256(chemin):
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def main():
    archive, attendu, dossier = sys.argv[1], sys.argv[2], sys.argv[3]
    e = sha256(archive)
    if e != attendu:
        sys.exit(f"refus : empreinte {e} != {attendu}")
    if os.path.exists(dossier):
        sys.exit(f"refus : {dossier} existe déjà (dossier neuf exigé)")
    os.makedirs(dossier, mode=0o700)
    with tarfile.open(archive, "r:gz") as t:
        membres = t.getmembers()
        t.extractall(dossier, filter="data")
    n_fic = sum(1 for m in membres if m.isfile())
    n_disque = sum(len(fs) for _, _, fs in os.walk(dossier))
    print(f"archive {archive} sha256 {e} conforme ; fichiers dans l'archive {n_fic} ; sur disque {n_disque} ; égal {n_fic == n_disque}")


if __name__ == "__main__":
    main()
