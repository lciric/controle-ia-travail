"""Fusionne les six fichiers de moisson (parts 1, 1b, 1c, 2, 2b, 2c) selon la répartition gelée ; garde, pour une fiche moissonnée
deux fois, l'entrée de la part qui l'avait en charge et range l'autre comme doublon (accord entre moissonneurs rapporté)."""
import hashlib, json, sys
d = '/home/claude/scratch/ideation-rapport'
rep = json.load(open(f'{d}/melange-v1/' + (sys.argv[2] if len(sys.argv) > 2 else 'repartition-six-moissonneurs-v1.json')))
charge = {i: k for k, ids in rep.items() for i in ids}
retenues, doublons, manquantes = {}, [], []
for k in rep:
    try: entrees = json.load(open(f'{d}/moisson-C/moisson-part-{k}-v1.json'))
    except FileNotFoundError: entrees = []
    if isinstance(entrees, dict):  # format enveloppé (part 4a) : la liste des entrées est sous une clé
        entrees = next(v for v in entrees.values() if isinstance(v, list) and v and isinstance(v[0], dict) and 'id' in v[0])
    for e in entrees:
        if charge.get(e['id']) == k: retenues[e['id']] = dict(e, part=k)
        else: doublons.append(dict(e, part=k))
for i in charge:
    if i not in retenues: manquantes.append(i)
accord = [(x['id'], x['classe'], retenues[x['id']]['classe']) for x in doublons if x['id'] in retenues]
sortie = sys.argv[1]
json.dump([retenues[i] for i in sorted(retenues)], open(sortie, 'w'), ensure_ascii=False, indent=1)
print(json.dumps({'retenues': len(retenues), 'manquantes': manquantes, 'doublons': len(doublons), 'accord_doublons': accord,
                  'sha256': hashlib.sha256(open(sortie, 'rb').read()).hexdigest()}, ensure_ascii=False))
