"""Cherche un motif dans le texte d'un PDF (pdftotext -layout) et donne la page de chaque occurrence.

Usage : python3 -I page_de.py FICHIER.txt MOTIF [contexte]
La page est le nombre de sauts de page (\f) avant la ligne, plus un.
"""
import re
import sys

chemin, motif = sys.argv[1], sys.argv[2]
contexte = int(sys.argv[3]) if len(sys.argv) > 3 else 0
texte = open(chemin, encoding="utf-8", errors="replace").read()
lignes = texte.split("\n")
page = 1
pages = []
for ligne in lignes:
    pages.append(page)
    page += ligne.count("\f")
rx = re.compile(motif, re.I)
for i, ligne in enumerate(lignes):
    if rx.search(ligne):
        debut, fin = max(0, i - contexte), min(len(lignes), i + contexte + 1)
        print(f"--- p. {pages[i]} (ligne {i + 1})")
        for j in range(debut, fin):
            print("   " + lignes[j].replace("\f", "").rstrip()[:200])
