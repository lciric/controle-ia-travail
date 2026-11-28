# cherche.py TXT MOTIF [contexte] : imprime les pages (rang physique, 1 = premiere) ou le motif (regex, insensible a la casse) apparait
import sys, re
txt, motif = sys.argv[1], sys.argv[2]
ctx = int(sys.argv[3]) if len(sys.argv) > 3 else 1
pages = open(txt, encoding='utf-8', errors='replace').read().split('\f')
rx = re.compile(motif, re.I)
for i, p in enumerate(pages, 1):
    lignes = p.split('\n')
    for j, l in enumerate(lignes):
        if rx.search(l):
            a, b = max(0, j-ctx), min(len(lignes), j+ctx+1)
            print(f"--- p. {i}, l. {j+1}")
            print('\n'.join(x.rstrip() for x in lignes[a:b]))
