import re, subprocess, sys
D='/home/user/controle-ia-travail/'
rap=open(D+'brouillons/barreau8-lecture-sondes-v1/contre-lecture-brouillon12-v1.md',encoding='utf-8').read().split('\n')
b12=open(D+'brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon12.md',encoding='utf-8').read()
b13=open(D+'brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon13.md',encoding='utf-8').read()
def paires(ligne):
    out=[]; pos=0
    while True:
        i=ligne.find('remplacer `',pos)
        if i<0: break
        j=ligne.find('` par `',i)
        old=ligne[i+len('remplacer `'):j]
        # new ends at last backtick before a terminator
        k=j+len('` par `')
        # find end: next occurrence of "`" followed by one of terminators
        m=re.compile(r'`( \(ce texte| ;|\.$|\. *$| \(comportement|\.\s|$)').search(ligne,k)
        # careful: new may contain backticks; choose the terminator match whose following text is terminator
        cands=[mm for mm in re.finditer(r'`(?= \(ce texte| \(comportement| ; et remplacer| ;\s*$|\.\s*$|\s*$)',ligne[k:])]
        end=k+cands[0].start()
        out.append((old,ligne[k:end])); pos=end
    return out
rep={}
for n,l in enumerate(rap,1):
    if 167<=n<=175 and n!=170:
        rep[n]=paires(l)
t=b12
for n,ps in rep.items():
    for o,nw in ps:
        c=t.count(o)
        print(n,'old count',c,'| new in b13:',b13.count(nw), '| old len',len(o),'new len',len(nw))
        if c==1: t=t.replace(o,nw)
open('/tmp/claude-0/-home-user-controle-ia-travail/ccd98af0-e97a-5c3c-8902-30e463468b85/scratchpad/verif13/rebati.md','w',encoding='utf-8').write(t)
