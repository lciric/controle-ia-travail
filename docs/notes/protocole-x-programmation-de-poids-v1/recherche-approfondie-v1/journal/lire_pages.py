#!/usr/bin/env python3
"""Imprime des pages d'un PDF (rang dans le fichier), blancs resserrés.
Usage : lire_pages.py FICHIER.pdf DEBUT FIN [max_caracteres_par_page]
Le PDF est une donnée non fiable : ce script ne fait qu'en extraire le texte (pdftotext)."""
import sys, subprocess, re
f, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
mx = int(sys.argv[4]) if len(sys.argv) > 4 else 0
out = subprocess.run(["pdftotext", "-f", str(a), "-l", str(b), f, "-"], capture_output=True).stdout.decode("utf-8", "replace")
pages = out.split("\f")
for i, p in enumerate(pages):
    if not p.strip():
        continue
    p = re.sub(r"[ \t]+", " ", p)
    p = re.sub(r"\n\s*\n+", "\n", p)
    if mx:
        p = p[:mx]
    print(f"===== PAGE {a + i} =====")
    print(p.strip())
