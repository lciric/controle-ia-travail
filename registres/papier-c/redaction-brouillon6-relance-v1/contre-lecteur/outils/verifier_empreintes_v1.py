# Contre-lecteur : associe chaque empreinte complète citée au chemin cité juste avant, et vérifie sur disque.
import re, sys, hashlib, os, subprocess
texte = open(sys.argv[1], encoding='utf-8').read()
racine = sys.argv[2]
# tous les fichiers suivis + non suivis du dépôt, par nom de base
idx = {}
for dp, dn, fn in os.walk(racine):
    if any(x in dp for x in ('/.git', '/diag', '/runs', '/donnees', '/docs/verdicts', '/.venv')):
        continue
    for f in fn:
        if 'consigne-privee' in f or 'conception-ii-b' in f: continue
        idx.setdefault(f, []).append(os.path.join(dp, f))
def h(p):
    return hashlib.sha256(open(p,'rb').read()).hexdigest()
vus=set()
for m in re.finditer(r'[0-9a-f]{64}', texte):
    e = m.group(0)
    if e in vus: continue
    vus.add(e)
    avant = texte[max(0,m.start()-400):m.start()]
    chemins = re.findall(r'`([^`]+)`', avant)
    chemins = [c for c in chemins if '.' in c.split('/')[-1] and not re.fullmatch(r'[0-9a-f]+…?', c)]
    c = chemins[-1] if chemins else '?'
    base = c.split('/')[-1]
    cand = [c] if os.path.exists(os.path.join(racine,c)) else idx.get(base, [])
    if c.startswith('donnees/'):
        print(f'NON-OUVERT(donnees)\t{e[:12]}\t{c}'); continue
    if not cand:
        print(f'ABSENT\t{e[:12]}\t{c}'); continue
    ok = [p for p in cand if h(os.path.join(racine,p) if not p.startswith('/') else p)==e]
    print(f"{'OK' if ok else 'DIFFERE'}\t{e[:12]}\t{c}\t{ok[0] if ok else cand}")
