import re,sys
# usage: chercher_v1.py fichier motif [largeur] [contexte autour de la correspondance]
f,m=sys.argv[1],sys.argv[2]
w=int(sys.argv[3]) if len(sys.argv)>3 else 600
r=re.compile(m)
for i,l in enumerate(open(f,encoding='utf-8'),1):
    if 'R-2059' in l: continue
    k=r.search(l)
    if k:
        a=max(0,k.start()-w//3)
        print(f"{i}: [{len(l)}] {l[a:a+w].rstrip()}")
