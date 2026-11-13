"""Vérifie que chaque citation figure, espaces normalisés, sur la page indiquée du texte extrait par pdftotext (mode brut).

Usage : python3 -I verifier_citations_o4_v1.py <racine lecture-o4-v1> <citations.json> <sortie.json>
"""
import json, re, subprocess, sys, unicodedata, hashlib
from pathlib import Path

def norm(s):
    s = unicodedata.normalize("NFKC", s)
    return re.sub(r"\s+", " ", s).strip()

racine, cits, sortie = Path(sys.argv[1]), json.load(open(sys.argv[2], encoding="utf-8")), sys.argv[3]
cache, res = {}, []
for c in cits:
    pdf = racine / c["pdf"]
    if pdf not in cache:
        txt = subprocess.run(["pdftotext", str(pdf), "-"], capture_output=True, text=True).stdout
        cache[pdf] = (txt.split("\f"), hashlib.sha256(pdf.read_bytes()).hexdigest())
    pages, h = cache[pdf]
    p = c["page"]
    sur_page = 1 <= p <= len(pages) and norm(c["texte"]) in norm(pages[p - 1])
    ailleurs = [i + 1 for i, t in enumerate(pages) if norm(c["texte"]) in norm(t)]
    res.append({**c, "sha256_pdf": h, "trouvee_sur_la_page": sur_page, "pages_ou_trouvee": ailleurs})
json.dump(res, open(sortie, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
ok = sum(r["trouvee_sur_la_page"] for r in res)
print(f"{ok}/{len(res)} citations trouvées sur la page indiquée")
for r in res:
    if not r["trouvee_sur_la_page"]:
        print("ÉCHEC", r["cle"], r["page"], r["pages_ou_trouvee"], r["texte"][:80])
