import sys, subprocess
sys.path.insert(0,'/home/user/controle-ia-travail/src')
from controle_ia import prereg
D='/home/user/controle-ia-travail/brouillons/barreau8-lecture-sondes-v1/'
B10=D+'prereg-lecture-sondes-barreau8-v1-brouillon10.md'
t=open(B10,encoding='utf-8').read()
C1='À REMPLIR — À FIXER : tirée par la session mère au scellement'
C2='- **Contre-lecture 4 (finale, texte rempli)** — À REMPLIR :'
C3="versée avec l'empreinte du texte scellé."
ENTREE4=open('gabarit-entree4.txt',encoding='utf-8').read().rstrip('\n')
def ligne4(rap):
    return ENTREE4.replace('<EMPREINTE DU RAPPORT>',rap)
def remplir(texte, entropie=None, l4=None):
    L=texte.split('\n')
    if entropie is not None:
        assert texte.count(C1)==1; L=[l.replace(C1,entropie) for l in L]
    if l4 is not None:
        idx=[i for i,l in enumerate(L) if l.startswith(C2) and l.endswith(C3)]
        assert len(idx)==1; L[idx[0]]=l4
    return '\n'.join(L)
ENT='123456789012345678901234567890123456789'
cas={'sain':remplir(t,ENT,ligne4('2'*64)),
     'artefact_sans_empreinte_rapport':remplir(t,ENT,ENTREE4.replace(' empreinte `<EMPREINTE DU RAPPORT>`','')),
     'artefact_entropie_ouverte':remplir(t,None,ligne4('2'*64))}
for k,v in cas.items():
    p=f'copie-{k}.md'; open(p,'w',encoding='utf-8').write(v)
    print(k,'problemes =',prereg.problemes(p))
    if k=='sain':
        d=subprocess.run(['diff',B10,p],capture_output=True,text=True).stdout
        print('diff =',[l for l in d.split('\n') if l[:1].isdigit()])
        print('ligne 76 =',v.split('\n')[75])
        print('empreintes ligne 429 =',__import__('re').findall(r'\b[0-9a-f]{64}\b',v.split('\n')[428]))
