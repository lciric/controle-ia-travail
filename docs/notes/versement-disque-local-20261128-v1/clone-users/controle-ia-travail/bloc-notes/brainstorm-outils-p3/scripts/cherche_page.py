#!/usr/bin/env python3
"""Cherche un motif (regex, insensible a la casse) dans un texte pdftotext -layout ; donne la page du PDF (split sur \f)."""
import re, sys
chemin, motif = sys.argv[1], sys.argv[2]
ctx = int(sys.argv[3]) if len(sys.argv) > 3 else 0
pages = open(chemin, encoding="utf-8", errors="replace").read().split("\f")
rx = re.compile(motif, re.I)
for i, p in enumerate(pages, 1):
    lignes = p.split("\n")
    for j, l in enumerate(lignes):
        if rx.search(l):
            a, b = max(0, j-ctx), min(len(lignes), j+ctx+1)
            print(f"--- p.{i} l.{j+1}")
            for k in range(a, b):
                print(lignes[k].rstrip())
