import difflib,sys
a=open('prereg/T0.7-organismes-discrets-v-a-v2-brouillon55.md',encoding='utf-8').read().split('\n')
b=open('prereg/T0.7-organismes-discrets-v-a-v2-brouillon56.md',encoding='utf-8').read().split('\n')
assert len(a)==len(b)
for i,(x,y) in enumerate(zip(a,b),1):
    if x!=y:
        print('LIGNE',i)
        sm=difflib.SequenceMatcher(None,x.split(' '),y.split(' '),autojunk=False)
        for op,i1,i2,j1,j2 in sm.get_opcodes():
            if op!='equal': print(' ',op,'-[',' '.join(x.split(' ')[i1:i2]),']\n    +[',' '.join(y.split(' ')[j1:j2]),']')
