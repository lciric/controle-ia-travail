"""Rejoue chaque citation sur la page indiquée du texte extrait par pdftotext (mode brut).
Normalisation : NFKC (ligatures, formes pleine chasse), guillemets et tirets unifiés, césures de fin de ligne
et espaces supprimés, casse ignorée ; la comparaison porte sur les seuls caractères alphanumériques.
Usage : python3 -I verifier_citations_priorite_haute_o4_v1.py <racine du dépôt> <citations.json> <sortie.json>
"""
import hashlib, json, re, subprocess, sys, unicodedata
from pathlib import Path

def norm(s):
    s = unicodedata.normalize("NFKC", s).replace("­", "").lower()
    return re.sub(r"[^0-9a-zà-ÿ]+", "", s)

racine, cits, sortie = Path(sys.argv[1]), json.load(open(sys.argv[2], encoding="utf-8")), sys.argv[3]
cache, res = {}, []
for c in cits:
    pdf = racine / c["pdf"]
    if pdf not in cache:
        txt = subprocess.run(["pdftotext", str(pdf), "-"], capture_output=True, text=True).stdout
        cache[pdf] = ([norm(p) for p in txt.split("\f")], hashlib.sha256(pdf.read_bytes()).hexdigest())
    pages, h = cache[pdf]
    q, p = norm(c["citation"]), c["page"]
    sur = 1 <= p <= len(pages) and q in pages[p - 1]
    res.append({**c, "sha256_pdf_recalcule": h, "empreinte_conforme": h == c["empreinte"],
                "trouvee_sur_la_page": sur, "pages_ou_trouvee": [i + 1 for i, t in enumerate(pages) if q in t]})
json.dump(res, open(sortie, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
ok = sum(r["trouvee_sur_la_page"] and r["empreinte_conforme"] for r in res)
print(f"{ok} sur {len(res)} citations trouvées sur la page indiquée, empreinte du PDF conforme")
for r in res:
    if not (r["trouvee_sur_la_page"] and r["empreinte_conforme"]):
        print("ÉCHEC", r["piece"], r["page"], r["pages_ou_trouvee"], r["citation"][:80])
