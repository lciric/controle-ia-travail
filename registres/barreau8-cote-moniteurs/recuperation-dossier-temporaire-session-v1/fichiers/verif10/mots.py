import difflib
D='/home/user/controle-ia-travail/brouillons/barreau8-lecture-sondes-v1/'
a=open('rebati.md',encoding='utf-8').read().split('\n')
b=open(D+'prereg-lecture-sondes-barreau8-v1-brouillon10.md',encoding='utf-8').read().split('\n')
for n in (1,3,5,7,24,261):
    s=difflib.SequenceMatcher(None,a[n-1],b[n-1],autojunk=False)
    for op,i1,i2,j1,j2 in s.get_opcodes():
        if op!='equal': print(n,op,repr(a[n-1][i1:i2]),'->',repr(b[n-1][j1:j2]))
