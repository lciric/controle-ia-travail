"""Contre-lecture : sépare, p. 7, les caractères de la couche non rendue (polices ZPXDWK/NUSUND et corps < 9 hors DejaVu)
des caractères du texte courant, et écrit les deux textes — v1. Usage : python3 -B -I couche_p7_v1.py PDF SORTIE_DIR"""
import sys, os
import pdfplumber
pdf, sortie = sys.argv[1], sys.argv[2]
CACHEES = {"ZPXDWK+TeXGyreTermesX-Regular", "NUSUND+TeXGyreTermesX-Bold"}
with pdfplumber.open(pdf) as doc:
    p = doc.pages[6]
    def cachee(o):
        if o.get("object_type") != "char":
            return False
        n = o["fontname"]
        if "DejaVu" in n:
            return False
        return n in CACHEES or o["size"] < 8.9
    def rendue(o):
        if o.get("object_type") != "char":
            return True
        return not cachee(o)
    h = p.filter(cachee)
    r = p.filter(rendue)
    open(os.path.join(sortie, "p7-couche-non-rendue.txt"), "w").write(h.extract_text(x_tolerance=1) or "")
    open(os.path.join(sortie, "p7-rendue.txt"), "w").write(r.extract_text(x_tolerance=1) or "")
    # Les caractères cachés sont-ils dans la zone de la figure 2 ou sur le texte courant ?
    ys = sorted(c["top"] for c in p.chars if cachee(c))
    print("caractères cachés :", len(ys), "top min/max", round(ys[0]), round(ys[-1]))
    # Attributs de rendu disponibles
    c0 = next(c for c in p.chars if cachee(c))
    print({k: c0.get(k) for k in ("fontname", "size", "non_stroking_color", "stroking_color", "matrix", "upright")})
    c1 = next(c for c in p.chars if c["fontname"].startswith("PIFFUR") and c["size"] >= 9.9)
    print({k: c1.get(k) for k in ("fontname", "size", "non_stroking_color", "stroking_color", "matrix", "upright")})
