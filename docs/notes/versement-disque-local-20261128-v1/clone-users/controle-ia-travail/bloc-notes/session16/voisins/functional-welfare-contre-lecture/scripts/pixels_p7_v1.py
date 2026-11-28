"""Contre-lecture : contrôle par pixels que la couche à échelle < 1 de la p. 7 n'est pas rendue — v1.
Pour chaque caractère caché (échelle de matrice 0,687 ou 0,426, hors DejaVu) dont la boîte ne touche aucune boîte
de caractère visible (échelle 1, ou DejaVu dans le cadre de la figure 2) ni aucun trait (lignes, rectangles, courbes),
on mesure l'encre de l'image rendue à 144 points par pouce dans sa boîte.
Usage : python3 -B -I pixels_p7_v1.py PDF IMAGE_PNG"""
import sys
import numpy as np
import pdfplumber
from PIL import Image
pdf, png = sys.argv[1], sys.argv[2]
img = np.asarray(Image.open(png).convert("L"), dtype=float)
k = 144 / 72
def encre(b):
    x0, t, x1, bo = [int(round(v * k)) for v in b]
    z = img[max(t, 0):max(bo, t + 1), max(x0, 0):max(x1, x0 + 1)]
    return 0.0 if z.size == 0 else float((z < 128).mean())
with pdfplumber.open(pdf) as doc:
    p = doc.pages[6]
    cache = lambda c: round(c["matrix"][0], 3) in (0.687, 0.426) and "DejaVu" not in c["fontname"]
    vis = [c for c in p.chars if round(c["matrix"][0], 3) == 1.0 or ("DejaVu" in c["fontname"] and 190 <= c["top"] <= 300)]
    traits = [o for o in p.lines + p.rects + p.curves if 190 <= o["top"] <= 300 or o.get("height", 0) < 2]
    boites = [(c["x0"] - 2, c["top"] - 2, c["x1"] + 2, c["bottom"] + 2) for c in vis] + [(o["x0"] - 2, o["top"] - 2, o["x1"] + 2, o["bottom"] + 2) for o in traits]
    def touche(c):
        return any(not (c["x1"] < b[0] or c["x0"] > b[2] or c["bottom"] < b[1] or c["top"] > b[3]) for b in boites)
    caches = [c for c in p.chars if cache(c)]
    isoles = [c for c in caches if c["text"].strip() and not touche(c)]
    e_caches = [encre((c["x0"], c["top"], c["x1"], c["bottom"])) for c in isoles]
    e_vis = [encre((c["x0"], c["top"], c["x1"], c["bottom"])) for c in vis if c["text"].strip() and round(c["matrix"][0], 3) == 1.0]
    print(f"caractères cachés : {len(caches)} ; isolés (sans voisin visible ni trait) : {len(isoles)}")
    print(f"encre moyenne dans les boîtes des cachés isolés : {np.mean(e_caches):.4f} ; max : {np.max(e_caches):.4f} ; part > 0,05 : {np.mean(np.array(e_caches) > 0.05):.4f}")
    print(f"témoin, caractères visibles (échelle 1) : encre moyenne {np.mean(e_vis):.4f} ; part > 0,05 : {np.mean(np.array(e_vis) > 0.05):.4f}")
