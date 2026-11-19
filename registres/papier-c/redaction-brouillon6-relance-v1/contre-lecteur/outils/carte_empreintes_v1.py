# Contre-lecteur : carte empreinte -> fichiers (dépôt hors zones interdites ; archive extraite), puis contrôle des empreintes citées (complètes et abrégées).
import re, sys, hashlib, os
texte = open(sys.argv[1], encoding='utf-8').read()
racines = sys.argv[2:]
INTERDIT = ('/.git/', '/diag/', '/runs/', '/donnees/', '/docs/verdicts/', '/.venv/', '/node_modules/')
carte = {}
for r in racines:
    for dp, dn, fn in os.walk(r):
        d = dp + '/'
        if any(x in d for x in INTERDIT): continue
        for f in fn:
            if 'consigne-privee' in f or 'conception-ii-b' in f: continue
            p = os.path.join(dp, f)
            try:
                if os.path.getsize(p) > 200_000_000: continue
                e = hashlib.sha256(open(p,'rb').read()).hexdigest()
            except Exception: continue
            carte.setdefault(e, []).append(p)
full = sorted(set(re.findall(r'(?<![0-9a-f])[0-9a-f]{64}(?![0-9a-f])', texte)))
abr = sorted(set(re.findall(r'(?<![0-9a-f])([0-9a-f]{8,16})…', texte)))
print('== empreintes complètes', len(full))
for e in full:
    ps = carte.get(e)
    print(('TROUVE ' if ps else 'NON-TROUVE ') + e[:16] + ' ' + (' | '.join(p.replace('/home/user/controle-ia-travail/','DEPOT:').replace(racines[-1],'ARCH:') for p in ps) if ps else ''))
print('== empreintes abrégées', len(abr))
for a in abr:
    ps = [p for e,pp in carte.items() if e.startswith(a) for p in pp]
    print(('TROUVE ' if ps else 'NON-TROUVE ') + a + ' ' + ' | '.join(p.replace('/home/user/controle-ia-travail/','DEPOT:').replace(racines[-1],'ARCH:') for p in ps[:2]))
