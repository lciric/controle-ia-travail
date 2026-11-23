import re,sys,hashlib
rep=open(sys.argv[1],encoding='utf-8').read(); out=sys.argv[2]
D='docs/notes/demandes-fable-api-2026-11-22-v1/'
cibles={'Réponse 4':D+'reponse-4/relecture-fable-api.md','Réponse 8':D+'reponse-8/relecture-fable-api.md',
 'Note des problématiques (version 1)':'docs/notes/note-problematiques-programme-v1/note-problematiques-programme-v1.md','PROG':'docs/programme-controle-ia-v2.md'}
p1,rest=rep.split('# Pièce 2'); p2=rest.split('## Décisions qui reviennent')[0]
blocs=[]
for sec in re.split(r'\n## ',p1)[1:]:
    t=sec.split('\n')[0].strip()
    for m in re.finditer(r'\*\*([A-Z0-9-]+)\.\*\* ANCIEN : « (.*?) »\s*\nNOUVEAU : « (.*?) »\s*\n',sec,re.S): blocs.append((t,)+m.groups())
for m in re.finditer(r'\*\*(D\d+)\.\*\* ANCIEN : « (.*?) »\s*\nNOUVEAU : « (.*?) »\s*\n(?=\n|\*\*D|Raison|$)',p2,re.S): blocs.append(('PROG',)+m.groups())
textes={k:open(v,encoding='utf-8').read() for k,v in cibles.items()}
for t,i,a,n in blocs:
    c=textes[t].count(a)
    print(i,'trouvé',c,'avant application', '' if c==1 else '<== ÉCHEC')
    if c==1: textes[t]=textes[t].replace(a,n)
print('blocs',len(blocs))
noms={'PROG':'programme-controle-ia-v3-application-a-blanc.md','Note des problématiques (version 1)':'note-problematiques-programme-v2-application-a-blanc.md','Réponse 4':'reponse-4-corrigee-application-a-blanc.md','Réponse 8':'reponse-8-corrigee-application-a-blanc.md'}
for k,v in noms.items():
    open(out+'/'+v,'w',encoding='utf-8').write(textes[k]); print(v,hashlib.sha256(textes[k].encode()).hexdigest())
