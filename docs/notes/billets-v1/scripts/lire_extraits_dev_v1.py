"""Aide de lecture (moitié développement seulement) : extraits autour d'un motif dans les billets jugés empiriques."""
import json,re,sys
m=json.load(open('/home/user/controle-ia-travail/docs/notes/billets-v1/manifeste-corpus-v1.json'))
v=json.load(open('/home/user/controle-ia-travail/docs/notes/billets-v1/controle-classement-dev-v1.json'))
pat=re.compile(sys.argv[1],re.I)
n=int(sys.argv[2]) if len(sys.argv)>2 else 3
for e in m['billets']:
  if e['moitie']!='developpement' or e['identifiant'] in v['non']: continue
  t=' '.join(open(f"/home/user/billets-corpus-v1/developpement/billets/{e['identifiant']}.md").read().split())
  hits=[mm.start() for mm in pat.finditer(t)][:n]
  for h in hits:
    print(e['identifiant'],e['classe'][:4],'|',t[max(0,h-120):h+220].replace('\n',' '))
