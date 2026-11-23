import sys; sys.path.insert(0, sys.argv[1]); import recalcul_ecarts_1_2_v1 as m, numpy as np
B = {r: m.construire(r, "relation", 1.0) for r in range(1000, 1030)}
for sq in ["g1","g3"]:
    xs=[x for r in B for x in B[r][0] if x["sq"]==sq]
    L=[m.litt(x["texte"]) for x in xs]
    # écriture g1: A,C,R ; g3: R,A,C
    if sq=="g1": c,rr=[l[1] for l in L],[l[2] for l in L]
    else: rr,c=[l[0] for l in L],[l[2] for l in L]
    rat=np.array([min(a,b)/max(a,b) for a,b in zip(c,rr)]); y=np.array([x["y"] for x in xs])
    print(sq, "ratio moyen V", rat[~y].mean(), "F", rat[y].mean(), "part V ratio>0.95", (rat[~y]>0.95).mean(), "F", (rat[y]>0.95).mean())
