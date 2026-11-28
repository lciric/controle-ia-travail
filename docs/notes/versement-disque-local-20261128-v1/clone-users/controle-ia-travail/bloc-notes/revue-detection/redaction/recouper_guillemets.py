"""Pour chaque phrase anglaise entre « » de la synthèse, liste les (clé, page) des PDF où elle figure.
Usage : python3 -I recouper_guillemets.py synthese.md citations.json"""
import json, re, subprocess, sys
syn = open(sys.argv[1], encoding="utf-8").read()
d = json.load(open(sys.argv[2], encoding="utf-8"))
def norm(t):
    t = re.sub(r"(?<=[A-Za-z])-\n(?=[a-z])", "", t)
    return re.sub(r"\s+", " ", t)
pages = {}
for cle, p in d["pdfs"].items():
    for mode in ("brut", "layout"):
        args = ["pdftotext"] + (["-layout"] if mode == "layout" else []) + [p["chemin"], "-"]
        out = subprocess.run(args, capture_output=True, text=True).stdout
        for i, pg in enumerate(out.split("\f"), start=1):
            pages.setdefault((cle, i), []).append(norm(pg))
quotes = re.findall(r"«\s*([^»]+?)\s*»", syn)
vus = set()
for q in quotes:
    if not re.search(r"[A-Za-z]{3}", q) or re.search(r"[éèàêç]", q):
        continue
    if q in vus: continue
    vus.add(q)
    qn = re.sub(r"\s+", " ", q)
    hits = [f"{c} p{i}" for (c, i), txts in pages.items() if any(qn in t for t in txts)]
    print(("OK   " if hits else "ABS  ") + repr(q[:90]) + " -> " + ", ".join(hits[:6]))
