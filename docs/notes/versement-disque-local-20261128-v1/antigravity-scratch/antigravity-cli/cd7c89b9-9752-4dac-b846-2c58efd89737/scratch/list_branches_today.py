import json
import subprocess

cursor = None
rows = []
while True:
    after = f', after: "{cursor}"' if cursor else ''
    q = (
        'query { repository(owner: "lciric", name: "controle-ia-travail") { '
        f'refs(refPrefix: "refs/heads/", first: 100{after}) {{ '
        'pageInfo { hasNextPage endCursor } '
        'nodes { name target { ... on Commit { oid committedDate messageHeadline } } } '
        '} } }'
    )
    p = subprocess.run(
        ['gh', 'api', 'graphql', '--input', '-'],
        input=json.dumps({'query': q}),
        text=True,
        capture_output=True,
        check=True,
    )
    data = json.loads(p.stdout)['data']['repository']['refs']
    for n in data['nodes']:
        t = n['target']
        if t.get('committedDate', '') >= '2026-11-24T00:00:00Z':
            rows.append((t['committedDate'], n['name'], t['oid'][:8], t['messageHeadline']))
    if not data['pageInfo']['hasNextPage']:
        break
    cursor = data['pageInfo']['endCursor']

rows.sort(reverse=True)
print(f'Total branches updated on 2026-11-24: {len(rows)}')
for d, b, s, m in rows:
    print(f'{d}  {s}  {b}  |  {m}')
