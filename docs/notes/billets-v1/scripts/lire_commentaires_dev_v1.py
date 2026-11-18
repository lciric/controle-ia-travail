"""Aide de lecture (moitié développement seulement) : commentaires retenus des billets bien notés jugés empiriques."""
import json,sys
m=json.load(open('/home/user/controle-ia-travail/docs/notes/billets-v1/manifeste-corpus-v1.json'))
v=json.load(open('/home/user/controle-ia-travail/docs/notes/billets-v1/controle-classement-dev-v1.json'))
ids=[e['identifiant'] for e in m['billets'] if e['moitie']=='developpement' and e['classe']=='bien-note' and e['identifiant'] not in v['non']]
a,b=int(sys.argv[1]),int(sys.argv[2])
for pid in ids[a:b]:
  cs=json.load(open(f'/home/user/billets-corpus-v1/developpement/commentaires/{pid}.json'))
  print('#####',pid)
  for c in cs:
    t=' '.join((c['contents'] or {}).get('markdown','').split())
    print(f" [{c['_id']} s={c['baseScore']} r={'o' if c['parentCommentId'] else 'n'}] {t[:230]}")
print(len(ids))
