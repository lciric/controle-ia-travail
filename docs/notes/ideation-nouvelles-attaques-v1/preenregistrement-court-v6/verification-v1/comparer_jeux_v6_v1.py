#!/usr/bin/env python3
"""Dit si chaque objet d'un jeu de corrections figure a l'identique dans un autre jeu, et si un texte
donne (fichier UTF-8, fin de ligne finale retiree) est le « neuf » d'un objet du second jeu. N'ecrit rien.
Usage : python3 -B comparer_jeux_v6_v1.py MON_JEU.json SON_JEU.json TEXTE_ATTENDU.txt
"""
import json
import sys


def main(a):
    if len(a) != 4:
        sys.stderr.write("usage : 3 chemins\n")
        return 2
    with open(a[1], encoding="utf-8") as f:
        mien = json.load(f)
    with open(a[2], encoding="utf-8") as f:
        sien = json.load(f)
    with open(a[3], encoding="utf-8") as f:
        attendu = f.read().rstrip("\n")
    for i, k in enumerate(mien, 1):
        print("C%d porte mot pour mot :" % i, k in sien)
    print("texte attendu porte comme « neuf » :", any(x["neuf"] == attendu for x in sien))
    print("objets du second jeu hors du premier :", sum(1 for x in sien if x not in mien))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
