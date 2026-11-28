"""Contre-lecture : texte de la couche non rendue de la p. 7 dans l'ordre du flux de contenu (chaque copie reste contiguë) — v1.
Usage : python3 -B -I couche_ordre_flux_v1.py PDF SORTIE"""
import sys
import pdfplumber
CACHEES = {"ZPXDWK+TeXGyreTermesX-Regular", "NUSUND+TeXGyreTermesX-Bold"}
with pdfplumber.open(sys.argv[1]) as doc:
    p = doc.pages[6]
    morceaux, prec = [], None
    for c in p.chars:
        n = c["fontname"]
        cache = ("DejaVu" not in n) and (n in CACHEES or c["size"] < 8.9)
        if not cache:
            continue
        if prec is not None and (abs(c["top"] - prec["top"]) > 2 or c["x0"] - prec["x1"] > 1.0):
            morceaux.append(" " if abs(c["top"] - prec["top"]) <= 2 else "\n")
        morceaux.append(c["text"])
        prec = c
    open(sys.argv[2], "w").write("".join(morceaux))
