#!/usr/bin/env python3
"""Repère, page par page, les passages d'un PDF qui portent un motif, avec leur contexte.
Usage : python3 -I pages_v1.py FICHIER.pdf LARGEUR MOTIF [MOTIF…]   (motifs : expressions régulières, casse ignorée)"""
import re, subprocess, sys

pdf, largeur, motifs = sys.argv[1], int(sys.argv[2]), sys.argv[3:]
n = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout).group(1))
for p in range(1, n + 1):
    t = subprocess.run(["pdftotext", "-f", str(p), "-l", str(p), pdf, "-"], capture_output=True, text=True).stdout
    t = re.sub(r"\s+", " ", t.replace("-\n", "").replace("‐", "-"))
    for m in motifs:
        for r in re.finditer(m, t, flags=re.I):
            a, b = max(0, r.start() - largeur), min(len(t), r.end() + largeur)
            print(f"p.{p} [{m}] …{t[a:b]}…")
