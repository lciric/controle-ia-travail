"""Contrôle indépendant de la liste de référence, sans l'arbre extrait : par une autre voie (git ls-tree et git cat-file, lus
dans le dépôt seulement), refait l'ensemble des chemins et l'empreinte sha256 du contenu de chaque fichier du commit, et
compare à la liste, ligne à ligne (chemins « ./… », triés en octets comme LC_ALL=C). Rend 0 si égal.
Usage : controler-liste-reference-l4.py DEPOT COMMIT LISTE
"""
import hashlib
import subprocess
import sys


def main(args):
    if len(args) != 3:
        print(__doc__)
        return 2
    depot, commit, liste = args
    sortie = subprocess.run(["git", "-C", depot, "ls-tree", "-r", "-z", commit], check=True, capture_output=True).stdout
    entrees = []
    for e in sortie.split(b"\0"):
        if not e:
            continue
        tete, chemin = e.split(b"\t", 1)
        mode, typ, objet = tete.split(b" ")
        if typ != b"blob" or mode not in (b"100644", b"100755"):
            print("ÉCHEC : entrée non régulière dans l'arbre :", mode, typ, chemin)
            return 1
        entrees.append((b"./" + chemin, objet))
    entrees.sort()
    lot = subprocess.Popen(["git", "-C", depot, "cat-file", "--batch"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    lignes = []
    for chemin, objet in entrees:
        lot.stdin.write(objet + b"\n")
        lot.stdin.flush()
        entete = lot.stdout.readline().split()
        taille = int(entete[2])
        contenu = lot.stdout.read(taille)
        lot.stdout.read(1)
        if b"\\" in chemin or b"\n" in chemin:
            print("ÉCHEC : chemin à échapper, non traité :", chemin)
            return 1
        lignes.append(hashlib.sha256(contenu).hexdigest().encode() + b"  " + chemin + b"\n")
    lot.stdin.close()
    lot.wait()
    refaite = b"".join(lignes)
    with open(liste, "rb") as fh:
        lue = fh.read()
    print("entrées de l'arbre :", len(entrees))
    print("liste refaite par git cat-file : sha256", hashlib.sha256(refaite).hexdigest())
    print("liste lue                      : sha256", hashlib.sha256(lue).hexdigest())
    ok = refaite == lue
    print("ÉGALES à l'octet" if ok else "DIFFÉRENTES")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
