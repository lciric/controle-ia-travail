import re,sys
rep=open(sys.argv[1],encoding='utf-8').read()
D='docs/notes/demandes-fable-api-2026-11-22-v1/'
cibles={'Réponse 4':D+'reponse-4/relecture-fable-api.md','Réponse 8':D+'reponse-8/relecture-fable-api.md',
 'Note des problématiques (version 1)':'docs/notes/note-problematiques-programme-v1/note-problematiques-programme-v1.md',
 'PROG':'docs/programme-controle-ia-v2.md'}
def norm(s):
    s=re.sub(r'[*_`]','',s); s=s.replace('’',"'"); return re.sub(r'\s+',' ',s).strip()
p1,p2=rep.split('# Pièce 2')[0],rep.split('# Pièce 2')[1].split('## Décisions qui reviennent')[0]
blocs=[]
for sec in re.split(r'\n## ',p1)[1:]:
    titre=sec.split('\n')[0].strip()
    for m in re.finditer(r'\*\*([A-Z0-9-]+)\.\*\* ANCIEN : « (.*?) »\s*\nNOUVEAU',sec,re.S): blocs.append((titre,m.group(1),m.group(2)))
for m in re.finditer(r'\*\*(D\d+)\.\*\* ANCIEN : « (.*?) »\s*\nNOUVEAU',p2,re.S): blocs.append(('PROG',m.group(1),m.group(2)))
for t,i,a in blocs:
    if t not in cibles: print(i,'cible inconnue',t); continue
    txt=open(cibles[t],encoding='utf-8').read()
    exact=txt.count(a); n=norm(txt).count(norm(a))
    print(f"{i:6} {t[:12]:12} exact={exact} normalisé={n}" + ("" if exact==1 else "   <== "+a[:90]))
print('blocs',len(blocs))
