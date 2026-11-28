import sys,re
# usage: pg.py fichier.txt motif [contexte]
t=open(sys.argv[1],encoding='utf-8',errors='replace').read().split('\f')
pat=re.compile(sys.argv[2],re.I)
ctx=int(sys.argv[3]) if len(sys.argv)>3 else 0
for i,p in enumerate(t):
    L=p.split('\n')
    for j,l in enumerate(L):
        if pat.search(l):
            lo=max(0,j-ctx);hi=min(len(L),j+ctx+1)
            print(f"--- p.{i+1} l.{j+1}")
            print('\n'.join(L[lo:hi]))
