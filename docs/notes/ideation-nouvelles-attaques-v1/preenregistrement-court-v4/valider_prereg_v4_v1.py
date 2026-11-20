#!/usr/bin/env python3
"""Appelle le validateur du depot (controle_ia.prereg.problemes) sur un fichier, et n'ecrit rien.

Usage, depuis la racine du depot, avec PYTHONPATH=src :
    python3 -B CE_FICHIER PREENREGISTREMENT.md
Le module controle_ia.prereg n'a pas d'entree en ligne de commande : ce script ne fait que l'appeler.
"""
import sys

from controle_ia.prereg import SECTIONS, problemes, sections


def main(argv):
    if len(argv) != 2:
        sys.stderr.write("usage : valider_prereg_v4_v1.py PREENREGISTREMENT.md\n")
        return 2
    with open(argv[1], encoding="utf-8") as f:
        s = sections(f.read())
    print("sections exigees presentes :", [n for n in SECTIONS if n in s])
    print("sections exigees absentes :", [n for n in SECTIONS if n not in s])
    p = problemes(argv[1])
    print("problemes :", p if p else "aucun")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
