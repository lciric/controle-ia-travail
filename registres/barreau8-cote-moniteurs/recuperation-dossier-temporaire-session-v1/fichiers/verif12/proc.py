import subprocess, re, hashlib, pathlib
from controle_ia import prereg
D='/home/user/controle-ia-travail/brouillons/barreau8-lecture-sondes-v1/'
T='/tmp/claude-0/-home-user-controle-ia-travail/ccd98af0-e97a-5c3c-8902-30e463468b85/scratchpad/verif12/'
src=D+'prereg-lecture-sondes-barreau8-v1-brouillon12.md'
b=open(src,encoding='utf-8').read()
print('validateur brouillon 12 :', prereg.problemes(src))
L=b.split('\n')
print('marqueurs :', [i+1 for i,l in enumerate(L) if 'À REMPLIR' in l])
cl=b[b.index('## Contre-lecture'):]
print('entrées :', [m.group(1) for m in prereg.ENTREE.finditer(cl)])
e37=[l for l in L if l.startswith('- **Contre-lecture 3 septies**')][0]
print('3 septies empreintes :', sorted(set(re.findall(r'[0-9a-f]{64}',e37))))
A='À REMPLIR — À FIXER : tirée par la session mère au scellement'
P='- **Contre-lecture 4 (finale, texte rempli)** — À REMPLIR :'
F="versée avec l'empreinte du texte scellé."
for s in (A,P,F): print('unique', b.count(s), repr(s[:50]))
ENT='123456789012345678901234567890123456789'
RAP='2'*64
GAB=("- **Contre-lecture 4 (finale, texte rempli)** — sous-agent neuf, modèle Claude Opus 5.5, qui n'a écrit ni ce texte, ni aucune contre-lecture antérieure de ce texte, ni la note d'interface, ni aucune notice, ni aucun code ; contre-lecture de la différence du brouillon 11 au brouillon 12 (dont la forme (A) de l'essai de la chaîne, contrôlée par simulation propre). Brouillon relu : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon12.md`, empreinte `467c2e8ba627554e454bba09dd640c3d10c5f25ed73cd7d25fcf7e491013bd5a`. Rapport : `brouillons/barreau8-lecture-sondes-v1/contre-lecture-brouillon12-v1.md`, empreinte `<EMPREINTE DU RAPPORT>`. Conclusion : « PRÊT : le brouillon 12 peut être scellé une fois l'entropie des graines versée et cette entrée de contre-lecture portée au texte, sans autre changement ». **Règle** : le texte scellé ne diffère du texte relu par cette contre-lecture que par cette entrée et par la cellule « état et raison » de F-3, où seule l'entropie tirée remplace le marqueur ; la session mère le vérifie par une comparaison faite par programme, versée avec l'empreinte du texte scellé.")
def remplir(ent=True, entree=True, rap=RAP):
    LL=list(L)
    if ent:
        assert LL[75].count(A)==1; LL[75]=LL[75].replace(A,ENT)
    if entree:
        assert LL[439].startswith(P) and LL[439].endswith(F)
        LL[439]=GAB.replace('<EMPREINTE DU RAPPORT>',rap)
    return '\n'.join(LL)
for nom,txt in [('sain',remplir()),('artefact_entropie_ouverte',remplir(ent=False)),
                ('artefact_entree4_sans_empreinte_rapport',remplir(rap='`(manquante)`'.strip('`'))),]:
    p=T+nom+'.md'; open(p,'w',encoding='utf-8').write(txt)
    print(nom, prereg.problemes(p))
    if nom=='sain':
        out=subprocess.run(['diff',src,p],capture_output=True,text=True).stdout
        print('diff :', [l for l in out.split('\n') if re.match(r'^\d',l)])
        print('ligne 76 :', txt.split('\n')[75])
