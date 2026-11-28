"""Cherche une expression dans un texte pdftotext et donne la page du PDF (pages separees par \\f).

Usage : python3 -I chercher.py FICHIER.txt "expression" [contexte]
Normalisation : minuscules, blancs fusionnes, coupures de mots par trait d'union en fin de ligne recollees.
"""
import re
import sys


def pages(chemin):
    with open(chemin, encoding="utf-8", errors="replace") as f:
        brut = f.read()
    return brut.split("\f")


def normaliser(t):
    t = re.sub(r"-\s*\n\s*", "", t)
    t = re.sub(r"\s+", " ", t)
    return t.lower()


def main():
    chemin, expr = sys.argv[1], sys.argv[2]
    ctx = int(sys.argv[3]) if len(sys.argv) > 3 else 120
    e = normaliser(expr)
    trouve = 0
    for i, p in enumerate(pages(chemin), start=1):
        n = normaliser(p)
        k = n.find(e)
        while k != -1:
            trouve += 1
            print(f"p. {i} : ...{n[max(0, k - ctx):k + len(e) + ctx]}...")
            k = n.find(e, k + 1)
    if not trouve:
        print("ABSENT")


if __name__ == "__main__":
    main()
