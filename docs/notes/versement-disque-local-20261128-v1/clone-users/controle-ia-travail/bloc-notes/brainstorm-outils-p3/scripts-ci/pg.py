import sys, re
# usage: pg.py fichier.txt motif [contexte]
path, pat = sys.argv[1], sys.argv[2]
ctx = int(sys.argv[3]) if len(sys.argv) > 3 else 2
txt = open(path, encoding='utf-8', errors='replace').read()
pages = txt.split('\f')
rx = re.compile(pat, re.I)
for i, p in enumerate(pages, 1):
    lines = p.split('\n')
    for j, l in enumerate(lines):
        if rx.search(l):
            lo, hi = max(0, j-ctx), min(len(lines), j+ctx+1)
            print(f'--- p.{i} l.{j+1}')
            print('\n'.join(x.rstrip() for x in lines[lo:hi]))
