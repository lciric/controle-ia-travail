import re,sys
D='brouillons/barreau8-lecture-sondes-v1/'
b13=open(D+'prereg-lecture-sondes-barreau8-v1-brouillon13.md',encoding='utf-8').read()
b14=open(D+'prereg-lecture-sondes-barreau8-v1-brouillon14.md',encoding='utf-8').read()
rap=open(D+'contre-lecture-brouillon13-v1.md',encoding='utf-8').read().split('\n')
integ=open('docs/notes/barreau8-cote-moniteurs-sorties-v1/contre-lecture-codes-passe-v5-lecture-v4-integration-v1.md',encoding='utf-8').read().split('\n')
paires={}
for n in (135,136):  # lignes 136, 137 du rapport (index 0)
    m=re.search(r'remplacer `(.*?)` par `(.*)`\.?$',rap[n])
    old,new=m.group(1),m.group(2)
    if new.endswith('`'): new=new[:-1]
    paires[rap[n][4:7]]=(old,new)
for k,(o,n) in paires.items():
    print(k,'cherché dans b13:',b13.count(o),'| remplacement dans b14:',b14.count(n))
t=b13
for k,(o,n) in paires.items():
    assert t.count(o)==1; t=t.replace(o,n)
# phrases T-1..T-4 extraites du rapport d'intégration, lignes 62-65
T={}
for n in range(61,65):
    m=re.search(r'(T-\d) : « (.*) »$',integ[n]); T[m.group(1)]=m.group(2)
for k,v in T.items():
    parts=[p.strip(' ,') for p in v.split('…') if p.strip(' ,')]
    print(k,[ (p[:50], b13.count(p), b14.count(p)) for p in parts])
open(sys.argv[1],'w',encoding='utf-8').write(t)
