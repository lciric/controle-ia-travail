import difflib, sys, re
a=open(sys.argv[1],encoding='utf-8').read().split('\n')
b=open(sys.argv[2],encoding='utf-8').read().split('\n')
sm=difflib.SequenceMatcher(None,a,b,autojunk=False)
for tag,i1,i2,j1,j2 in sm.get_opcodes():
    if tag=='equal': continue
    print(f"=== {tag} a{i1+1}-{i2} b{j1+1}-{j2}")
    A='\n'.join(a[i1:i2]); B='\n'.join(b[j1:j2])
    ta=re.split(r'(\s+)',A); tb=re.split(r'(\s+)',B)
    s2=difflib.SequenceMatcher(None,ta,tb,autojunk=False)
    for t,x1,x2,y1,y2 in s2.get_opcodes():
        if t=='equal': continue
        print(f"  [{t}] -<<{''.join(ta[x1:x2])}>>\n         +<<{''.join(tb[y1:y2])}>>")
