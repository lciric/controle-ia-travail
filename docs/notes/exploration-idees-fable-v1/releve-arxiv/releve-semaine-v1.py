#!/usr/bin/env python3
"""Relevé brut des dépôts arXiv d'une fenêtre de dates, par requêtes de mots clés.
Sortie : un fichier XML par requête (brut), et une table fusionnée (TSV + JSON)."""
import sys, time, json, urllib.parse, urllib.request, xml.etree.ElementTree as ET, pathlib, hashlib

OUT = pathlib.Path(sys.argv[1])
D1, D2 = sys.argv[2], sys.argv[3]  # ex. 202611140000 202611222359
OUT.mkdir(parents=True, exist_ok=True)
NS = {"a": "http://www.w3.org/2005/Atom", "x": "http://arxiv.org/schemas/atom"}

REQUETES = [
 'abs:"AI scientist"', 'abs:"AI scientists"', 'abs:"AI co-scientist"', 'abs:"artificial scientist"',
 'abs:"scientific discovery" AND (abs:LLM OR abs:"language model" OR abs:agent OR abs:agents)',
 'abs:"automated scientific discovery"', 'abs:"autonomous scientific discovery"', 'abs:"autonomous research"',
 'abs:"automated research"', 'abs:"research agent"', 'abs:"research agents"', 'abs:"hypothesis generation"',
 'abs:"idea generation"', 'abs:"research ideas"', 'abs:"research ideation"', 'abs:ideation',
 'abs:"open-ended" AND (abs:discovery OR abs:evolution OR abs:exploration)', 'abs:"open-endedness"',
 'abs:"quality-diversity"', 'abs:"quality diversity"', 'abs:"novelty search"', 'abs:"MAP-Elites"',
 'abs:AlphaEvolve', 'abs:FunSearch', 'abs:"evolutionary" AND (abs:LLM OR abs:"language model")',
 'abs:"program search"', 'abs:"algorithm discovery"', 'abs:"mathematical discovery"',
 'abs:"multi-agent" AND (abs:science OR abs:scientific OR abs:research)', 'abs:"society of" AND abs:agents',
 'abs:"self-improving"', 'abs:"recursive self-improvement"', 'abs:"mode collapse" AND abs:diversity',
 'abs:creativity AND (abs:LLM OR abs:"language model")', 'abs:homogeneity AND (abs:LLM OR abs:"language model")',
 'abs:"Good-Turing"', 'abs:"missing mass"', 'abs:"unseen species"', 'abs:"species richness" AND abs:LLM',
 'abs:"exploration" AND abs:"scientific" AND abs:"discovery"', 'abs:"science of science"',
 'abs:"scientific novelty"', 'abs:"novelty" AND abs:"research" AND (abs:LLM OR abs:"language model")',
 'abs:"tree search" AND (abs:hypothes OR abs:idea OR abs:research OR abs:discovery)',
 'abs:"Bayesian surprise"', 'abs:serendipity', 'abs:"literature-based discovery"',
 'abs:"automated discovery"', 'abs:"AI for science" AND abs:agent', 'abs:"discovery" AND abs:"agentic"',
 'abs:"stochastic resetting"', 'abs:"adjacent possible"', 'abs:"combinatorial innovation"',
 'abs:"interdisciplinary" AND abs:"novelty"', 'abs:"disruption" AND abs:"science" AND abs:"papers"',
 'abs:"peer review" AND abs:"AI-generated"', 'abs:"autoresearch"', 'abs:"auto-research"',
 'abs:"scientific agent"', 'abs:"scientific agents"', 'abs:"AI researcher"', 'abs:"AI researchers" AND abs:autonomous',
 'abs:"diversity" AND abs:"idea" AND (abs:LLM OR abs:"language model")', 'abs:"verbalized sampling"',
 'abs:"hypothesis" AND abs:"falsification" AND abs:agent', 'abs:"equation discovery"', 'abs:"symbolic regression" AND abs:LLM',
 'abs:"theorem" AND abs:"discovery" AND abs:"agent"', 'abs:"conjecture" AND (abs:LLM OR abs:"language model")',
 'abs:"knowledge graph" AND abs:"hypothes"', 'abs:"exploration" AND abs:"exploitation" AND abs:"research"',
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
