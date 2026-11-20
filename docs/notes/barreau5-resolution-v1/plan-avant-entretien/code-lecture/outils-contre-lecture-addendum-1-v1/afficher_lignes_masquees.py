"""Affiche les lignes [debut, fin] d'un fichier, avec leur numero.

Toute ligne qui porte l'un des motifs de masque est remplacee par
« [ligne masquee] » sans etre affichee. Outil du contre-lecteur de
l'addendum 1 (barreau 5) ; aucune lecture de donnee.

Usage : afficher_lignes_masquees.py FICHIER DEBUT FIN
"""
import sys

MASQUES = ("B bis", "b bis", "phrase de la consigne", "consigne-privee",
           "conception-ii-b")


def main() -> int:
    chemin, debut, fin = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    with open(chemin, encoding="utf-8") as f:
        for n, ligne in enumerate(f, start=1):
            if n < debut:
                continue
            if n > fin:
                break
            if any(m in ligne for m in MASQUES):
                print(f"{n:5d}\t[ligne masquee]")
            else:
                print(f"{n:5d}\t{ligne.rstrip()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
