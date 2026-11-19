import sys, subprocess
sys.path.insert(0,'src')
from controle_ia import prereg
V='/tmp/claude-0/-home-user-controle-ia-travail/ccd98af0-e97a-5c3c-8902-30e463468b85/scratchpad/verif13/'
src='brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon13.md'
t=open(src,encoding='utf-8').read()
M1='À REMPLIR — À FIXER : tirée par la session mère au scellement'
DEB='- **Contre-lecture 4 (finale, texte rempli)** — À REMPLIR :'
FIN="versée avec l'empreinte du texte scellé."
GAB=open(V+'gabarit.txt',encoding='utf-8').read().rstrip('\n')
assert '\n' not in GAB and 'À REMPLIR' not in GAB
def remplir(t, entropie=True, entree=True, rapport='2'*64):
    if entropie:
        assert t.count(M1)==1; t=t.replace(M1,'123456789012345678901234567890123456789')
    if entree:
        L=t.split('\n'); idx=[i for i,l in enumerate(L) if l.startswith(DEB) and l.endswith(FIN)]
        assert len(idx)==1, idx
        L[idx[0]]=GAB.replace('<EMPREINTE DU RAPPORT>',rapport) if rapport else GAB.replace(', empreinte `<EMPREINTE DU RAPPORT>`','')
        t='\n'.join(L)
    return t
cas={'sain':remplir(t),'artefact_entropie_ouverte':remplir(t,entropie=False),'artefact_entree4_sans_empreinte_rapport':remplir(t,rapport=None)}
for k,v in cas.items():
    p=V+k+'.md'; open(p,'w',encoding='utf-8').write(v)
    print(k, prereg.problemes(p))
r=subprocess.run(['diff',src,V+'sain.md'],capture_output=True,text=True).stdout
print('diff:',[l for l in r.split('\n') if l[:1].isdigit()])
print('lignes:',len(cas['sain'].split('\n')), '| l76:',cas['sain'].split('\n')[75])
import re
print('entrees:',[m.group(1) for m in prereg.ENTREE.finditer(prereg.sections(cas['sain'])['Contre-lecture'])])
