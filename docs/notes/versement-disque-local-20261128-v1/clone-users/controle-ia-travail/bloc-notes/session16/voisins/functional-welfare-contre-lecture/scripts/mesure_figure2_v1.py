"""Contre-lecture : mesure vectorielle de la figure 2 (p. 7) — v1.
Étalonne chaque panneau sur les étiquettes de graduation (DejaVu, cadre 190-300) et lit hauts et bas des barres
(rectangles remplis) et extrémités des moustaches (segments verticaux). Usage : python3 -B -I mesure_figure2_v1.py PDF"""
import sys, re
import pdfplumber
with pdfplumber.open(sys.argv[1]) as doc:
    p = doc.pages[6]
    zone = lambda o: 190 <= o["top"] <= 300 and 190 <= o["bottom"] <= 300
    mots = [w for w in p.extract_words(extra_attrs=["fontname", "size"]) if "DejaVu" in w["fontname"] and zone(w)]
    rects = [r for r in p.rects if zone(r) and r["width"] > 2 and r.get("fill")]
    segs = [l for l in p.lines + [c for c in p.curves] if zone(l)]
    # panneaux : par x
    panneaux = {"R1": (150, 300), "sondes": (300, 430), "PANAS": (430, 560)}
    for nom, (x0, x1) in panneaux.items():
        graduations = []
        for w in mots:
            t = w["text"].replace("−", "-")
            if re.fullmatch(r"-?\d+(\.\d+)?", t) and x0 - 20 <= w["x1"] <= x0 + 25:
                graduations.append((float(t), (w["top"] + w["bottom"]) / 2))
        graduations.sort()
        if len(graduations) < 2:
            print(nom, "graduations introuvables", [w["text"] for w in mots if x0 - 20 <= w["x1"] <= x0 + 25][:10]); continue
        (v0, y0), (v1, y1) = graduations[0], graduations[-1]
        val = lambda y: v0 + (y - y0) * (v1 - v0) / (y1 - y0)
        print(f"== {nom} : graduations {graduations}")
        for r in sorted([r for r in rects if x0 + 5 <= r["x0"] <= x1], key=lambda r: r["x0"]):
            print(f"  barre x={r['x0']:.1f}-{r['x1']:.1f} : haut {val(r['top']):+.4f} bas {val(r['bottom']):+.4f}")
        vs = [l for l in segs if x0 + 5 <= l["x0"] <= x1 and abs(l["x1"] - l["x0"]) < 0.6 and (l["bottom"] - l["top"]) > 0.5]
        for l in sorted(vs, key=lambda l: l["x0"]):
            print(f"  moustache x={l['x0']:.1f} : de {val(l['bottom']):+.4f} à {val(l['top']):+.4f}")
