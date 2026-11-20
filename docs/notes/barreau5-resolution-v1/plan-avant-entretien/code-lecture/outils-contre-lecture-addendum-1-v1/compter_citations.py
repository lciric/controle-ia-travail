"""Compte, sans rien afficher du contexte, les occurrences de citations dans un fichier.

Usage : compter_citations.py FICHIER CITATIONS
  CITATIONS : un fichier texte, une citation par ligne (lignes vides ignorees).
Pour chaque citation : son numero, le compte exact, et le compte apres
normalisation (espaces insecables ramenes a l'espace, marques de gras « ** »
et d'italique « * » retirees, casse ignoree). Rien du fichier lu n'est affiche.
Outil du contre-lecteur de l'addendum 1 (barreau 5).
"""
import sys

ESPACES = {" ": " ", " ": " ", " ": " ", " ": " "}


def normaliser(s: str) -> str:
    for a, b in ESPACES.items():
        s = s.replace(a, b)
    s = s.replace("**", "").replace("*", "")
    s = s.replace("’", "'")
    return " ".join(s.split()).casefold()


def main() -> int:
    chemin, chemin_citations = sys.argv[1], sys.argv[2]
    with open(chemin, encoding="utf-8") as f:
        texte = f.read()
    texte_n = normaliser(texte)
    with open(chemin_citations, encoding="utf-8") as f:
        citations = [ligne.rstrip("\n") for ligne in f if ligne.strip()]
    for i, c in enumerate(citations, 1):
        print(f"citation {i:2d} : exact {texte.count(c)} ; normalise {texte_n.count(normaliser(c))} ; "
              f"longueur {len(c)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
