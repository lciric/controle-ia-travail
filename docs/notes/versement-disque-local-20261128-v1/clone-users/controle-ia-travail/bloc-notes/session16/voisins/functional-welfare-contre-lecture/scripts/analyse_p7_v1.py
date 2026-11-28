"""Contre-lecture : analyse indépendante des caractères de la p. 7 du PDF 2610.22460v1 — v1.
Usage : python3 -B -I analyse_p7_v1.py PDF"""
import sys, collections
import pdfplumber
pdf = sys.argv[1]
with pdfplumber.open(pdf) as doc:
    for num in (6, 7, 8):
        p = doc.pages[num - 1]
        c = collections.Counter()
        boites = {}
        for ch in p.chars:
            cle = (ch["fontname"], round(ch["size"], 1))
            c[cle] += 1
            b = boites.setdefault(cle, [9e9, 9e9, -9e9, -9e9])
            b[0] = min(b[0], ch["x0"]); b[1] = min(b[1], ch["top"]); b[2] = max(b[2], ch["x1"]); b[3] = max(b[3], ch["bottom"])
        print(f"== p. {num} : {len(p.chars)} caractères ; boîte page {p.width}x{p.height}")
        for cle, n in sorted(c.items(), key=lambda kv: -kv[1]):
            b = boites[cle]
            print(f"  {n:6d}  {cle[0]:40s} {cle[1]:5.1f}  x[{b[0]:.0f},{b[2]:.0f}] y[{b[1]:.0f},{b[3]:.0f}]")
