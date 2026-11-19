import re, sys, subprocess, shutil, hashlib
sys.path.insert(0,'/home/user/controle-ia-travail/src')
from controle_ia import prereg
D='/home/user/controle-ia-travail/brouillons/barreau8-lecture-sondes-v1/'
B10=D+'prereg-lecture-sondes-barreau8-v1-brouillon10.md'
B9=D+'prereg-lecture-sondes-barreau8-v1-brouillon9.md'
t=open(B10,encoding='utf-8').read()
L=t.split('\n'); L9=open(B9,encoding='utf-8').read().split('\n')
print('problemes(b10) =', prereg.problemes(B10))
print('marqueurs lignes =', [i+1 for i,l in enumerate(L) for _ in range(l.count('À REMPLIR'))])
print('ligne 76 b10 == ligne 76 b9 (octets):', L[75].encode()==L9[75].encode())
C1='À REMPLIR — À FIXER : tirée par la session mère au scellement'
C2='- **Contre-lecture 4 (finale, texte rempli)** — À REMPLIR :'
C3="versée avec l'empreinte du texte scellé."
for c in (C1,C2,C3): print('compte', repr(c[:40]), t.count(c), [i+1 for i,l in enumerate(L) if c in l])
# 3 quinquies
q=[l for l in L if l.startswith('- **Contre-lecture 3 quinquies**')][0]
print('3 quinquies empreintes =', re.findall(r'\b[0-9a-f]{64}\b', q))
cl=prereg.sections(t)['Contre-lecture']
print('entrees reconnues =', [m.group(0).strip() for m in prereg.ENTREE.finditer(cl)])
