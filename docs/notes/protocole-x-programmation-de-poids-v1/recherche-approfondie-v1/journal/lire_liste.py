#!/usr/bin/env python3
"""Met en table les entrées d'une liste publique (README en Markdown) : section, date, titre, lien, identifiant arXiv, description.
Usage : lire_liste.py README.md SORTIE.tsv"""
import sys, re
src, dst = sys.argv[1], sys.argv[2]
L = open(src, encoding="utf-8").read().split("\n")
sec = ""; sub = ""; rows = []
i = 0
while i < len(L):
    l = L[i]
    m = re.match(r"^## (.*)", l)
    if m: sec = re.sub(r"[^\w ,:\-]", "", m.group(1)).strip(); sub = ""
    m = re.match(r"^<summary><b>(.*?)</b></summary>", l)
    if m: sub = m.group(1)
    m = re.match(r"^- \*\*\[(.*?)\]\((.*?)\)\*\*", l)
    if m and sec not in ("Recently Added", ):
        title, url = m.group(1), m.group(2)
        meta = L[i+1].strip() if i+1 < len(L) else ""
        d = re.search(r"·\s*(\d{4}(?:-\d{2})?(?:-\d{2})?)\s*·", meta + " ·")
        date = d.group(1) if d else ""
        blob = " ".join(L[i:i+5])
        ax = re.search(r"arxiv\.org/abs/(\d{4}\.\d{4,5})", blob)
        desc = ""
        for k in range(i+2, min(i+6, len(L))):
            s = L[k].strip()
            if s and not s.startswith("[[") and not s.startswith("- **"):
                desc = s; break
        rows.append((sec, sub, date, title, url, ax.group(1) if ax else "", desc))
    i += 1
with open(dst, "w", encoding="utf-8") as f:
    f.write("section\tsous_section\tdate\ttitre\tlien\tarxiv\tdescription\n")
    for r in rows:
        f.write("\t".join(x.replace("\t", " ") for x in r) + "\n")
print(len(rows), "entrées")
