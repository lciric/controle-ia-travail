import re,sys,hashlib
rep=open(sys.argv[1],encoding='utf-8').read(); out=sys.argv[2]
D='docs/notes/demandes-fable-api-2026-11-22-v1/'
cibles={'E4':D+'reponse-4/relecture-fable-api.md','E8':D+'reponse-8/relecture-fable-api.md',
 'EN':'docs/notes/note-problematiques-programme-v1/note-problematiques-programme-v1.md','D':'docs/programme-controle-ia-v2.md'}
corps=rep.split('# Pièce 1 — Erratum interne')[1].split('## Décisions qui reviennent')[0]
morceaux=re.split(r'\n\*\*((?:E4|E8|EN)-\d+|D\d+)\.\*\* ANCIEN : ',corps)
blocs=[]
for i in range(1,len(morceaux),2):
    ident=morceaux[i]; b=morceaux[i+1]
    b=re.split(r'\n\n(?:\*\*Notes|## |# |---)',b)[0]
    a,n=b.split('\nNOUVEAU : ',1)
    n=n.split('\nRaison :')[0].rstrip()
    a=a.rstrip()
    assert a.startswith('« ') and a.endswith(' »'),ident
    a=a[2:-2]
    litteral=n.startswith('« ') and n.endswith(' »')
    if litteral: n=n[2:-2]
    blocs.append((ident,a,n,litteral))
print('blocs',len(blocs))
D3=[n for i,a,n,l in blocs if i=='D3'][0]
textes={k:open(v,encoding='utf-8').read() for k,v in cibles.items()}
rapport=[]
for ident,a,n,lit in blocs:
    k=re.match(r'(E4|E8|EN|D)',ident).group(1)
    if not lit:
        rapport.append(f'{ident} : NOUVEAU non littéral (« {n[:80]} ») ; appliqué avec le NOUVEAU de D3'); n=D3 if not a.startswith('« ') else '« '+D3+' »'
    c0=open(cibles[k],encoding='utf-8').read().count(a); c=textes[k].count(a)
    rapport.append(f'{ident} : ANCIEN trouvé {c0} fois dans la pièce d\'origine, {c} fois au moment de l\'application' + ('' if c==1 and c0==1 else '  <== ÉCHEC'))
    if c==1: textes[k]=textes[k].replace(a,n)
noms={'D':'programme-controle-ia-v3-application-a-blanc.md','EN':'note-problematiques-programme-v2-application-a-blanc.md','E4':'reponse-4-corrigee-application-a-blanc.md','E8':'reponse-8-corrigee-application-a-blanc.md'}
for k,v in noms.items():
    open(out+'/'+v,'w',encoding='utf-8').write(textes[k]); rapport.append(f'{v} sha256 {hashlib.sha256(textes[k].encode()).hexdigest()}')
print('\n'.join(rapport))
