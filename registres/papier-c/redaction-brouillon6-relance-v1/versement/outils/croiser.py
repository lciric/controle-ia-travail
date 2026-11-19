import sys,os,collections
W=sys.argv[1]
dep=collections.defaultdict(list)
for l in open(W+'/outils/index-depot.txt',encoding='utf-8'):
    h,p=l.rstrip('\n').split('  ',1); dep[h].append(p)
arc=collections.defaultdict(list)
for l in open(W+'/outils/index-archives.tsv',encoding='utf-8'):
    tag,h,s,n=l.rstrip('\n').split('\t'); arc[h].append((tag,n,s))
seen={}
for l in open(W+'/outils/releve-brut.tsv',encoding='utf-8'):
    c=l.rstrip('\n').split('\t')
    if c[0]!='H': continue
    ln,h,p,d=c[1:]
    if h in seen: continue
    seen[h]=1
    D=dep.get(h,[]); A=arc.get(h,[])
    print(f"L{ln}\t{h[:12]}\t{p}\tdepot={len(D)}:{D[0] if D else '-'}\tarch={';'.join(t+':'+n for t,n,s in A) if A else '-'}")
