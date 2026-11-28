"""Contre-lecture : regroupe les caractères de la p. 7 par échelle de matrice et police, avec leur boîte — v1."""
import sys, collections
import pdfplumber
with pdfplumber.open(sys.argv[1]) as doc:
    p = doc.pages[6]
    g = collections.defaultdict(list)
    for c in p.chars:
        g[(round(c["matrix"][0], 3), c["fontname"].split("+")[-1])].append(c)
    for k, v in sorted(g.items(), key=lambda kv: -len(kv[1])):
        print(f"{len(v):6d} échelle {k[0]:7.3f} {k[1]:28s} x[{min(c['x0'] for c in v):.0f},{max(c['x1'] for c in v):.0f}] y[{min(c['top'] for c in v):.0f},{max(c['bottom'] for c in v):.0f}]")
