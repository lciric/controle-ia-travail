"""Contre-lecture : mesure vectorielle du panneau R1 de la figure 2 (p. 7) — v1.
Étalonnage sur les graduations « 0.00 » et « −0.06 » (étiquettes DejaVu du cadre rendu) ; hauts et bas des barres.
Usage : python3 -B -I mesure_figure2_R1_v1.py PDF"""
import sys, re
import pdfplumber
with pdfplumber.open(sys.argv[1]) as doc:
    p = doc.pages[6]
    zone = lambda o: 190 <= o["top"] <= 300 and 190 <= o["bottom"] <= 300
    mots = [w for w in p.extract_words(extra_attrs=["fontname"]) if "DejaVu" in w["fontname"] and zone(w)]
    grads = sorted({(float(w["text"].replace("−", "-")), round((w["top"] + w["bottom"]) / 2, 2), round(w["x1"], 1))
                    for w in mots if re.fullmatch(r"[−-]?0\.0\d", w["text"])})
    print("graduations :", grads)
    xs = sorted({g[2] for g in grads})
    x_axe = xs[0]
    g = [t for t in grads if t[2] == x_axe]
    (v0, y0), (v1, y1) = (g[0][0], g[0][1]), (g[-1][0], g[-1][1])
    val = lambda y: v0 + (y - y0) * (v1 - v0) / (y1 - y0)
    rects = sorted([r for r in p.rects if zone(r) and r.get("fill") and x_axe + 3 <= r["x0"] <= x_axe + 120 and r["width"] < 15], key=lambda r: r["x0"])
    for r in rects:
        print(f"  barre x={r['x0']:.1f} : haut {val(r['top']):+.4f} bas {val(r['bottom']):+.4f}")
