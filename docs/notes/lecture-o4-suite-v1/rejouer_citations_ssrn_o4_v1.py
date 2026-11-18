"""Rejoue les citations de la lecture sur PDF de SSRN 6569258 (septembre 2026) et SSRN 6474601 contre O4 (v1).
Pour chaque citation : texte de la page par `pdftotext -f N -l N`, espaces réduits, la citation (espaces réduits) doit en être une
sous-chaîne. Empreinte de chaque PDF exigée. Aucun réseau. Usage : python3 -I rejouer_citations_ssrn_o4_v1.py CITATIONS.json DOSSIER_PDF SORTIE.json"""
import hashlib, json, os, re, subprocess, sys
cit, dossier, sortie = sys.argv[1:4]
if os.path.exists(sortie):
    sys.exit("REFUS : sortie existante")
C = json.load(open(cit, encoding="utf-8"))
norm = lambda s: re.sub(r"\s+", " ", s).strip()
res, cache = [], {}
for pdf, sha in C["pdf"].items():
    p = os.path.join(dossier, pdf)
    if hashlib.sha256(open(p, "rb").read()).hexdigest() != sha:
        sys.exit(f"REFUS : empreinte de {pdf}")
for c in C["citations"]:
    p = os.path.join(dossier, c["pdf"]); k = (p, c["page"])
    if k not in cache:
        cache[k] = norm(subprocess.run(["pdftotext", "-f", str(c["page"]), "-l", str(c["page"]), p, "-"], capture_output=True, text=True, check=True).stdout)
    res.append({"id": c["id"], "pdf": c["pdf"], "page": c["page"], "conforme": norm(c["citation"]) in cache[k]})
ok = sum(r["conforme"] for r in res)
json.dump({"citations_sha256": hashlib.sha256(open(cit, "rb").read()).hexdigest(), "total": len(res), "conformes": ok, "resultats": res},
          open(sortie, "x", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{ok} sur {len(res)} conformes")
