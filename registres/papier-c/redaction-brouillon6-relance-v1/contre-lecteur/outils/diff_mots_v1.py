# Contre-lecteur : différence par mots entre deux corps (à partir de « ## Hypothèse »), blocs supprimés [-…-] / ajoutés {+…+}.
import sys,difflib,re
a=open(sys.argv[1],encoding='utf-8').read(); b=open(sys.argv[2],encoding='utf-8').read()
a=a[a.index('\n## Hypothèse'):]; b=b[b.index('\n## Hypothèse'):]
ta=re.findall(r'\S+|\n',a); tb=re.findall(r'\S+|\n',b)
sm=difflib.SequenceMatcher(None,ta,tb,autojunk=False)
k=0
for op,i1,i2,j1,j2 in sm.get_opcodes():
    if op=='equal': continue
    k+=1
    ctx=' '.join(t for t in ta[max(0,i1-8):i1] if t!='\n')
    rem=' '.join(t for t in ta[i1:i2] if t!='\n'); add=' '.join(t for t in tb[j1:j2] if t!='\n')
    print(f'### {k} …{ctx}')
    if rem: print('  [-',rem,'-]')
    if add: print('  {+',add,'+}')
