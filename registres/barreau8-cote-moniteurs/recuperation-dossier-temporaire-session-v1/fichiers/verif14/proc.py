import sys,subprocess,hashlib
sys.path.insert(0,'src')
from controle_ia import prereg
S=sys.argv[1]
src='brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon14.md'
raw=open(src,'rb').read(); assert hashlib.sha256(raw).hexdigest()=='5b503e28e6b81285a792575f878642bbd529888cc886e7cd4ddcf80257e39891'
t=raw.decode('utf-8')
gab=open(S+'/gabarit.txt',encoding='utf-8').read().rstrip('\n')
ENT='123456789012345678901234567890123456789'
M3='À REMPLIR — À FIXER : tirée par la session mère au scellement'
DEB='- **Contre-lecture 4 (finale, texte rempli)** — À REMPLIR :'; FIN="versée avec l'empreinte du texte scellé."
def remplir(t,entropie=True,emp_rapport='2'*64):
    if entropie:
        assert t.count(M3)==1; t=t.replace(M3,ENT)
    L=t.split('\n'); idx=[i for i,l in enumerate(L) if l.startswith(DEB) and l.endswith(FIN)]
    assert len(idx)==1 and idx[0]==441, idx
    g=gab if emp_rapport is None else gab.replace('<EMPREINTE DU RAPPORT>',emp_rapport)
    if emp_rapport is None: g=g.replace(' Rapport : `brouillons/barreau8-lecture-sondes-v1/contre-lecture-brouillon14-v1.md`, empreinte `<EMPREINTE DU RAPPORT>`.','')
    L[441]=g; return '\n'.join(L)
cas={'sain':remplir(t),'artefact-entropie-ouverte':remplir(t,entropie=False),'artefact-sans-empreinte-rapport':remplir(t,emp_rapport=None)}
for k,v in cas.items():
    p=f'{S}/copie-{k}.md'; open(p,'w',encoding='utf-8').write(v)
    print(k,':',prereg.problemes(p))
    if k=='sain':
        d=subprocess.run(['diff',src,p],capture_output=True,text=True).stdout
        print('  diff :',[l for l in d.split('\n') if l[:1].isdigit()])
        print('  ligne 76 :',v.split('\n')[75])
        print('  deux empreintes distinctes ligne 442 :',len(set(prereg.EMPREINTE.findall(v.split('\n')[441]))))
        print('  À REMPLIR restant :',v.count('À REMPLIR'), '; <<>> restant:', prereg.GABARIT.findall(v))
