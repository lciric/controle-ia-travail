"""Contre-lecture : par page, caractères hors DejaVu dont la matrice n'est pas d'échelle 1 (signe d'un texte inclus dans
une figure mise à l'échelle), et accord, p. 7, entre le filtre du lecteur (police et corps) et le mien (échelle) — v1."""
import sys, collections
import pdfplumber
CACHEES = {"ZPXDWK+TeXGyreTermesX-Regular", "NUSUND+TeXGyreTermesX-Bold"}
with pdfplumber.open(sys.argv[1]) as doc:
    for i, p in enumerate(doc.pages, start=1):
        c = collections.Counter((round(ch["matrix"][0], 3), ch["fontname"].split("+")[-1]) for ch in p.chars
                                if "DejaVu" not in ch["fontname"] and round(ch["matrix"][0], 3) != 1.0)
        print(f"p. {i:2d} : {sum(c.values()):6d} caractères hors DejaVu à échelle ≠ 1 {dict(c) if c and i != 7 else ''}")
    p = doc.pages[6]
    lecteur = {id(ch) for ch in p.chars if "DejaVu" not in ch["fontname"] and ch["fontname"] not in CACHEES and ch["size"] >= 8.9}
    moi = {id(ch) for ch in p.chars if "DejaVu" not in ch["fontname"] and round(ch["matrix"][0], 3) == 1.0}
    print(f"p. 7 : filtre du lecteur {len(lecteur)} caractères, le mien {len(moi)}, communs {len(lecteur & moi)}")
