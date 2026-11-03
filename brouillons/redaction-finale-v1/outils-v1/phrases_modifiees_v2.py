"""Phrases modifiées entre la version vérifiée et la version finale de chaque réponse (v2).
Usage : phrases_modifiees_v2.py correspondances.json sortie.md
correspondances.json : {"slug": ["fichier vérifié", "fichier final"], ...} (chemins relatifs au dossier redaction-finale-v1).
Corps de la réponse = lignes avant la première ligne « --- ». Découpage en phrases sur la ponctuation finale suivie d'un blanc, et sur les sauts de ligne."""
import json, re, sys, hashlib, difflib
B = '/home/claude/controle-ia-travail/brouillons/redaction-finale-v1/'
corr, sortie = sys.argv[1:3]
def corps(p):
    t = open(B + p).read().split('\n')
    out = []
    for l in t:
        if l.strip() == '---': break
        out.append(l)
    return '\n'.join(out)
def phrases(t):
    res = []
    for para in t.split('\n'):
        para = para.strip()
        if not para: continue
        res += [s.strip() for s in re.split(r'(?<=[.!?])\s+(?=[A-Z0-9"“(\[])', para) if s.strip()]
    return res
def sha(p): return hashlib.sha256(open(B + p, 'rb').read()).hexdigest()
C = json.load(open(corr))
L = ["# Phrases modifiées par le directeur entre la version vérifiée et la version finale — v2", "",
     "Pour le vérificateur final : chaque phrase ajoutée ou changée (« + ») et celle qu'elle remplace (« − »). Ces phrases n'ont pas été revues par le premier vérificateur.", ""]
total = 0
for slug, (av, ap) in C.items():
    a, b = phrases(corps(av)), phrases(corps(ap))
    sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
    bloc = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal': continue
        bloc += [f"− {s}" for s in a[i1:i2]] + [f"+ {s}" for s in b[j1:j2]]
        total += j2 - j1
    L += [f"## {slug} ({av} `{sha(av)[:8]}…` → {ap} `{sha(ap)[:8]}…`)", ""] + (bloc if bloc else ["(aucune phrase changée)"]) + [""]
L.append(f"Phrases ajoutées ou changées : {total}.")
open(sortie, 'w').write('\n'.join(L) + '\n')
print(sortie, hashlib.sha256(open(sortie, 'rb').read()).hexdigest(), total)
