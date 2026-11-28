#!/usr/bin/env python3
"""Affiche la page n (1-indexee) d'un texte pdftotext -layout."""
import sys
chemin = sys.argv[1]
pages = open(chemin, encoding="utf-8", errors="replace").read().split("\f")
for n in sys.argv[2:]:
    print(f"======== page {n} / {len(pages)-1}")
    print(pages[int(n)-1])
