import re, hashlib
D='/home/user/controle-ia-travail/brouillons/barreau8-lecture-sondes-v1/'
a=open(D+'prereg-lecture-sondes-barreau8-v1-brouillon11.md',encoding='utf-8').read()
b=open(D+'prereg-lecture-sondes-barreau8-v1-brouillon12.md',encoding='utf-8').read()
r=open(D+'contre-lecture-brouillon11-v1.md',encoding='utf-8').read()
rl=r.split('\n')
def bt(s):  # extract backticked replacement pairs on a line: "Remplacer `X` par `Y`"
    return s
# N-1 : lines 109-111 of report
def paires(line):
    m=re.search(r"[Rr]emplacer (`+) ?(.*?) ?\1 par (`+) ?(.*?) ?\3\.?$", line.strip().rstrip('.').rstrip())
    return m
rep=[]
L109=rl[108]; L110=rl[109]; L111=rl[110]; L113=rl[112]; L114=rl[113]
def extract(line, n_expected):
    # split on " par " between backtick spans: find spans delimited by '` ' boundaries is ambiguous; do manual
    return None
# Manual extraction using known anchors
def between(s, start, end):
    i=s.index(start)+len(start); j=s.index(end,i); return s[i:j]
x1=between(L109,"Remplacer `","` par `"); y1=L109.split("` par `",1)[1].rsplit("`.",1)[0]
x2=between(L110,"Remplacer `","` par `"); y2=L110.split("` par `",1)[1].rsplit("`.",1)[0]
x3=between(L111,"Remplacer `` ","`` par `` "); y3=L111.split("`` par `` ",1)[1].rsplit(" ``",1)[0]
x4=between(L113,"remplacer `","` par `"); y4=L113.split("` par `",1)[1].split("`.",1)[0]
segs=L114.split(" ; (")
pairs=[(x1,y1),(x2,y2),(x3,y3),(x4,y4)]
for sg in segs:
    if "remplacer `" in sg:
        xx=between(sg,"remplacer `","` par `"); yy=sg.split("` par `",1)[1]; yy=yy[:yy.rindex("`")]
        pairs.append((xx,yy))
print(len(pairs))
c=a
for i,(x,y) in enumerate(pairs):
    n=c.count(x); print(i,'occurrences',n, repr(x[:60]))
    c=c.replace(x,y)
# forme (A) : lines 167-176
cl=c.split('\n')
L167=rl[166]; x=between(L167,"remplacer `","` par `"); y=L167.split("` par `",1)[1].rsplit("`.",1)[0]
print('382 occ',c.count(x)); c=c.replace(x,y); cl=c.split('\n')
def lignebt(k):  # line k (1-based in report) is "  `...`"
    s=rl[k-1].strip(); assert s[0]=='`' and s[-1]=='`'; return s[1:-1]
# find line indices in c for (i), (iii), limite by prefix
def remplace_ligne(prefix, new):
    global cl
    idx=[i for i,l in enumerate(cl) if l.startswith(prefix)]; assert len(idx)==1,(prefix,idx); cl[idx[0]]=new
remplace_ligne("- (i) **Cas sain.**", lignebt(169))
remplace_ligne("- (iii) **Artefact d'alignement.**", lignebt(172))
remplace_ligne("- **Limite déclarée de l'artefact positif (ii)", lignebt(176))
c='\n'.join(cl)
open('/tmp/claude-0/-home-user-controle-ia-travail/ccd98af0-e97a-5c3c-8902-30e463468b85/scratchpad/verif12/rebati.md','w',encoding='utf-8').write(c)
import difflib
A=c.split('\n'); B=b.split('\n')
sm=difflib.SequenceMatcher(None,A,B,autojunk=False)
for op,i1,i2,j1,j2 in sm.get_opcodes():
    if op!='equal': print('RESTE',op,f"rebati {i1+1}-{i2}",f"b12 {j1+1}-{j2}")
# noms et champs
def bloc(t): i=t.index("**Noms et champs, liste fermée**"); j=t.index("**Fichiers non lus avant**"); return t[i:j]
print('Noms et champs identiques:', bloc(a)==bloc(b), len(bloc(a)))
la=a.split('\n'); lb=b.split('\n')
print('ligne 76 identique:', la[75].encode()==lb[75].encode())
print(lb[75])
