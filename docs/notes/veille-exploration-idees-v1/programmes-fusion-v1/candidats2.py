import difflib, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from cles import cles, norm_titre, regroupe
E = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
K = [cles(e) for e in E]
G, _ = regroupe(E, K)
info = []
for g in G:
    ax = any(k.startswith("arxiv:") for i in g for k in K[i])
    info.append((norm_titre(E[g[0]]["titre"]), ax, g))
for a in range(len(info)):
    ta, axa, ga = info[a]
    for b in range(a + 1, len(info)):
        tb, axb, gb = info[b]
        if axa and axb:
            continue
        if len(set(ta.split()) & set(tb.split())) < 3:
            continue
        r = difflib.SequenceMatcher(None, ta, tb).ratio()
        if 0.55 <= r < 0.80:
            print(f"[{r:.2f}]")
            for g in (ga, gb):
                i = g[0]
                print("   ", "+".join(sorted({E[j]['voie'][:4] for j in g})), "|", E[i]["titre"][:120], "|", E[i]["adresse"][:50], "|", E[i]["date"][:12])
