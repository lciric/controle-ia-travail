import difflib,sys,re
a=open(sys.argv[1],encoding='utf-8').read().split('\n'); b=open(sys.argv[2],encoding='utf-8').read().split('\n')
sm=difflib.SequenceMatcher(None,a,b,autojunk=False)
for op,i1,i2,j1,j2 in sm.get_opcodes():
    if op=='equal': continue
    print(f'=== {op} a{i1+1}-{i2} b{j1+1}-{j2}')
    A=' '.join(a[i1:i2]); B=' '.join(b[j1:j2])
    ta=re.split(r'(\s+)',A); tb=re.split(r'(\s+)',B)
    s2=difflib.SequenceMatcher(None,ta,tb,autojunk=False)
    for o,x1,x2,y1,y2 in s2.get_opcodes():
        if o=='equal': continue
        print(f'  [{o}] -«{"".join(ta[x1:x2])}»\n         +«{"".join(tb[y1:y2])}»')
