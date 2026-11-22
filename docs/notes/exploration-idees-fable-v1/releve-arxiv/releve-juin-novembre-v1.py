#!/usr/bin/env python3
"""Relevé brut des dépôts arXiv d'une fenêtre de dates, par requêtes de mots clés.
Sortie : un fichier XML par requête (brut), et une table fusionnée (TSV + JSON)."""
import sys, time, json, urllib.parse, urllib.request, xml.etree.ElementTree as ET, pathlib, hashlib

OUT = pathlib.Path(sys.argv[1])
D1, D2 = sys.argv[2], sys.argv[3]  # ex. 202611140000 202611222359
OUT.mkdir(parents=True, exist_ok=True)
NS = {"a": "http://www.w3.org/2005/Atom", "x": "http://arxiv.org/schemas/atom"}

REQUETES = [
 'abs:"idea generation" AND (abs:LLM OR abs:"language model" OR abs:"language models")',
 'abs:"research ideas"', 'abs:"research ideation"', 'abs:"research idea"',
 'abs:"AI scientist"', 'abs:"AI scientists"', 'abs:"AI co-scientist"',
 'abs:"hypothesis generation" AND (abs:LLM OR abs:"language model" OR abs:"language models")',
 'abs:novelty AND abs:ideas AND (abs:LLM OR abs:"language model" OR abs:"language models")',
 'abs:homogeneity AND (abs:LLM OR abs:"language model" OR abs:"language models")',
 'abs:"mode collapse" AND abs:diversity AND (abs:LLM OR abs:"language model" OR abs:"language models")',
 'abs:"random search" AND (abs:evolutionary OR abs:AlphaEvolve OR abs:LLM)',
 'abs:AlphaEvolve', 'abs:FunSearch', 'abs:ShinkaEvolve', 'abs:OpenEvolve',
 'abs:"quality-diversity" AND (abs:LLM OR abs:"language model" OR abs:"language models")',
 'abs:"Good-Turing"', 'abs:"unseen species"', 'abs:"missing mass"',
 'abs:"open-ended" AND abs:"scientific discovery"', 'abs:"automated scientific discovery"',
 'abs:"best-of-N" AND (abs:search OR abs:evolution)', 'abs:"repeated sampling" AND abs:LLM',
 'abs:"scientific discovery" AND abs:exploration AND (abs:LLM OR abs:agent OR abs:agents)',
 'abs:"research taste"', 'abs:"scientific novelty"', 'abs:"literature-based discovery"',
 'abs:"exploration" AND abs:"idea" AND abs:"diversity"',
 'abs:"society" AND abs:"AI scientists"', 'abs:"multi-agent" AND abs:"scientific discovery"',
 'abs:"analogical" AND (abs:LLM OR abs:"language model") AND abs:"cross-domain"',
 'abs:"stochastic resetting" AND abs:search', 'abs:"adjacent possible"',
 'abs:"ideation" AND abs:"execution" AND abs:"gap"', 'abs:"novelty" AND abs:"peer review" AND abs:LLM',
 'abs:"evolutionary search" AND (abs:LLM OR abs:"language model")',
 'abs:"tree search" AND abs:"research" AND (abs:agent OR abs:agents)',
]
table = {}
for i, q in enumerate(REQUETES):
    full = f'({q}) AND submittedDate:[{D1} TO {D2}]'
    start = 0
    while True:
        url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(
            {"search_query": full, "start": start, "max_results": 200, "sortBy": "submittedDate", "sortOrder": "descending"})
        for essai in range(4):
            try:
                with urllib.request.urlopen(url, timeout=60) as r:
                    brut = r.read()
                break
            except Exception as e:
                brut = None; time.sleep(5 * (essai + 1))
        if brut is None:
            print("ECHEC", q, file=sys.stderr); break
        (OUT / f"req-{i:02d}-{start}.xml").write_bytes(brut)
        root = ET.fromstring(brut)
        total = int(root.find("{http://a9.com/-/spec/opensearch/1.1/}totalResults").text)
        entries = root.findall("a:entry", NS)
        for e in entries:
            idv = e.find("a:id", NS).text.rsplit("/", 1)[-1]
            ident = idv.split("v")[0]
            rec = table.setdefault(ident, {
                "id": idv, "titre": " ".join(e.find("a:title", NS).text.split()),
                "publie": e.find("a:published", NS).text, "maj": e.find("a:updated", NS).text,
                "categories": [c.get("term") for c in e.findall("a:category", NS)],
                "auteurs": [a.find("a:name", NS).text for a in e.findall("a:author", NS)][:6],
                "resume": " ".join(e.find("a:summary", NS).text.split()), "requetes": []})
            rec["requetes"].append(q)
        print(f"{i:02d} total={total} recus={len(entries)} :: {q}", file=sys.stderr)
        start += len(entries)
        time.sleep(3.2)
        if start >= total or not entries: break
recs = sorted(table.values(), key=lambda r: r["publie"], reverse=True)
(OUT / "table.json").write_text(json.dumps(recs, ensure_ascii=False, indent=1))
with open(OUT / "table.tsv", "w") as f:
    for r in recs:
        f.write("\t".join([r["id"], r["publie"], ",".join(r["categories"][:3]), r["titre"], str(len(r["requetes"]))]) + "\n")
print(len(recs), "articles distincts", file=sys.stderr)
