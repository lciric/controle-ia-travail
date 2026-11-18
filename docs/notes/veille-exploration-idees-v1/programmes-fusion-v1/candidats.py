#!/usr/bin/env python3
"""Premier regroupement par cles fortes, puis liste des paires de groupes aux titres proches, a trancher a la main.
Usage : python -I candidats.py brutes.json
"""
import difflib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cles import cles, norm_titre, regroupe  # noqa: E402

E = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
K = [cles(e) for e in E]
G, index = regroupe(E, K)
print("entrees", len(E), "groupes", len(G))

# groupes fusionnes par titre seul alors que les identifiants arXiv different : a verifier
for g in G:
    ax = {k for i in g for k in K[i] if k.startswith("arxiv:")}
    if len(ax) > 1:
        print("PLUSIEURS ARXIV DANS UN GROUPE", ax, [E[i]["titre"][:70] for i in g])

# representants
rep = []
for g in G:
    t = norm_titre(E[g[0]]["titre"])
    rep.append((t, g))
# paires proches
vus = 0
toks = [set(t.split()) for t, _ in rep]
for a in range(len(rep)):
    ta, ga = rep[a]
    if len(ta) < 8:
        continue
    pa = ta.split()[0]
    for b in range(a + 1, len(rep)):
        tb, gb = rep[b]
        if len(tb) < 8:
            continue
        inter = len(toks[a] & toks[b])
        if inter < 2 and pa != tb.split()[0]:
            continue
        r = difflib.SequenceMatcher(None, ta, tb).ratio()
        court, long_ = sorted((ta, tb), key=len)
        contient = len(court) >= 14 and court in long_
        prem = (pa == tb.split()[0] and len(pa) >= 6 and pa not in (
            "towards", "toward", "evaluating", "learning", "automated", "measuring", "scaling", "position",
            "rethinking", "training", "language", "beyond", "agentic", "autonomous", "scientific", "research",
            "benchmarking", "teaching", "diversity", "evolving", "recursive", "discovery", "selecting"))
        if r >= 0.80 or contient or prem:
            vus += 1
            print(f"\n[{r:.2f}{' contient' if contient else ''}{' prem' if prem else ''}]")
            for g in (ga, gb):
                for i in g:
                    print("   ", E[i]["voie"][:5], "|", E[i]["titre"][:110], "|", E[i]["adresse"][:60], "|", E[i]["date"][:22])
print("paires candidates", vus)
