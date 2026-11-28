import sys, re
# usage: pg.py ID regex [context_lines]
D="/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/revue-detection/extraction/txt-agents/"
pid=sys.argv[1]; rx=re.compile(sys.argv[2], re.I); ctx=int(sys.argv[3]) if len(sys.argv)>3 else 0
pages=open(D+pid+".txt",encoding="utf-8",errors="replace").read().split("\f")
for i,p in enumerate(pages,1):
    L=p.split("\n")
    for j,l in enumerate(L):
        if rx.search(l):
            lo=max(0,j-ctx); hi=min(len(L),j+ctx+1)
            print(f"--- p.{i} l.{j+1}")
            print("\n".join(L[lo:hi]))
