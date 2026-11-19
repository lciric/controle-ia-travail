import sys,re
sys.path.insert(0,'src')
from controle_ia import prereg
D='brouillons/barreau8-lecture-sondes-v1/'
p13=D+'prereg-lecture-sondes-barreau8-v1-brouillon13.md'; p14=D+'prereg-lecture-sondes-barreau8-v1-brouillon14.md'
b13=open(p13,encoding='utf-8').read(); b14=open(p14,encoding='utf-8').read()
L13=b13.split('\n'); L14=b14.split('\n')
print('problemes(b14) =',prereg.problemes(p14))
print('marqueurs :',[i for i,l in enumerate(L14,1) if 'À REMPLIR' in l], 'occurrences', b14.count('À REMPLIR'))
print('ligne 76 identique octet pour octet :', L14[75].encode()==L13[75].encode()); print('  ',L14[75])
for c in ["À REMPLIR — À FIXER : tirée par la session mère au scellement","- **Contre-lecture 4 (finale, texte rempli)** — À REMPLIR :","versée avec l'empreinte du texte scellé."]:
    print('unique ?',b14.count(c),repr(c[:50]))
print('ligne 442 commence/finit :',L14[441].startswith("- **Contre-lecture 4 (finale, texte rempli)** — À REMPLIR :"),L14[441].endswith("versée avec l'empreinte du texte scellé."), 'nb lignes', len(L14), 'fin par saut de ligne', b14.endswith('\n'))
def bloc(t):
    i=t.index('**Noms et champs, liste fermée**'); j=t.index('**Fichiers non lus avant**'); return t[i:j]
print('bloc Noms et champs identique :',bloc(b13)==bloc(b14),len(bloc(b14)))
ph="**Pour les neuf sondes, les scores par jeton sont livrés aussi : la garde de réception r7 recalcule leur maximum et leur moyenne sur toutes les actions.**"
print('O-6 phrase : occurrences',b14.count(ph),'lignes',[i for i,l in enumerate(L14,1) if ph in l])
print('  à sa place ligne 130 :', ph in L14[129], '; citée ligne 224 entre guillemets :', ('« '+ph+' »') in L14[223])
# b-5 citations
for q in ["l'essai n'échoue que par l'égalité des deux chemins non tenue, (a) ou (b)","Après une inégalité des deux chemins, ni (i), ni (ii), ni (iii) ne sont joués.","L'égalité des deux chemins n'éprouve pas le champ `rang` lui-même : la garde de réception r5 exige qu'il soit le rang de l'action dans l'ordre du fichier.","l'égalité des deux chemins n'est pas tenue, ou si","Les actions sans jeton noté n'y entrent pas."]:
    print('b-5 cité :',[i for i,l in enumerate(L14,1) if q in l],q[:45])
# entrées de contre-lecture
s=prereg.sections(b14)['Contre-lecture']
ent=list(prereg.ENTREE.finditer(s))
print('entrées ENTREE :',[e.group(1) for e in ent])
l441=L14[440]
print('3 nonies empreintes :',prereg.EMPREINTE.findall(l441))
print('égales attendues :',set(prereg.EMPREINTE.findall(l441))=={'7628ebfd8534bd44287e0a233a80339e6dde57db88fd0ada3df3c6a1b2305cd4','a723e7d91b8d4cf2c485598e24e49123359725f932b7b81b27e4e935a137575d'})
