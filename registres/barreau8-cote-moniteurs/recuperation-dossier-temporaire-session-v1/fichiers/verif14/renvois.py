import re,sys,collections
L=open(sys.argv[1],encoding='utf-8').read().split('\n')
T='\n'.join(L)
# définitions
defs=collections.defaultdict(list)
for i,l in enumerate(L,1):
    m=re.match(r'\| (D-\d+|F-\d+|I-\d+|P\d+|S\d|L\d|AU-[ab]|B8-P\d)(?: \(| \|)',l)
    if m: defs[m.group(1)].append(i)
    m=re.match(r'- \((r\d)\)',l)
    if m: defs[m.group(1)].append(i)
    m=re.match(r'  - \((b-\d+)\)',l)
    if m: defs[m.group(1)].append(i)
    m=re.match(r'\| (\d+) \| ',l)
    if m and 404<i<426: defs['arrêt '+m.group(1)].append(i)
    m=re.match(r'(\d+)\. \*\*',l)
    if m and 162<i<185: defs['plan '+m.group(1)].append(i)
# d1..d4
for d in ('d1','d2','d3','d4'):
    defs[d]=[i for i,l in enumerate(L,1) if re.search(r'\('+d+r'\) ',l) and i==160]
print('définitions multiples ou nulles :')
for k,v in sorted(defs.items()):
    if len(v)!=1: print(' ',k,v)
# usages
uses=collections.Counter()
pat=[(r'\b(D-\d+)\b',None),(r'\b(F-\d+)\b',None),(r'\b(I-\d+)\b',None),(r'\b(B8-P\d)\b',None),
     (r'\b(P\d+)\b',None),(r'\b(r\d)\b',None),(r'\b(AU-[ab])\b',None),(r'\b(b-\d+)\b',None),(r'\bligne (S\d|L\d)\b',None),(r'\b(d[1-4])\b',None)]
miss=set()
for i,l in enumerate(L,1):
    for p,_ in pat:
        for m in re.finditer(p,l):
            k=m.group(1); uses[k]+=1
            if k not in defs or not defs[k]: miss.add((k,i))
    for m in re.finditer(r"liste d'arrêt, lignes? (\d+)(?: (?:à|et) (\d+))?",l):
        for g in m.groups():
            if g and 'arrêt '+g not in defs: miss.add(('arrêt '+g,i))
            if g: uses['arrêt '+g]+=1
    for m in re.finditer(r'plan, points? (\d+)',l):
        k='plan '+m.group(1); uses[k]+=1
        if k not in defs: miss.add((k,i))
    for m in re.finditer(r'lignes (\d+) à (\d+) de la liste',l):
        for g in m.groups(): uses['arrêt '+g]+=1
# F-n hors F-3 sont des champs fermés listés ligne 78 : définis par la ligne 78
print('renvois non définis :',sorted(miss,key=lambda x:x[1]))
print('identifiants cités :',len(uses))
print({k:uses[k] for k in sorted(uses)})
