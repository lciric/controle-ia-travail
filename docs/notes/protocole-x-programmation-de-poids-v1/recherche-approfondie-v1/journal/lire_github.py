#!/usr/bin/env python3
"""Lit des réponses de recherche de dépôts (GitHub) et imprime une ligne par dépôt, sans doublon."""
import sys, json
vus = set(); tot = None
for f in sys.argv[1:]:
    d = json.load(open(f, encoding="utf-8"))
    tot = d.get("total_count", tot)
    for it in d.get("items", []):
        if it["full_name"] in vus: continue
        vus.add(it["full_name"])
        desc = (it.get("description") or "").replace("\n", " ")[:170]
        print(f'{it["stargazers_count"]:>6}\t{it["created_at"][:10]}\t{it["pushed_at"][:10]}\t{it["full_name"]}\t{desc}')
print(f"# total annoncé : {tot} ; dépôts lus : {len(vus)}", file=sys.stderr)
