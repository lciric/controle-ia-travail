"""Cherche une phrase (normalisée) dans les pages d'une clé ; imprime pages et contexte.
Usage : python3 -I cherche2.py CLE "phrase" [largeur_contexte]
Pages extraites par le vérificateur v2-sens (pdftotext, brut r*.txt et mise en page p*.txt)."""
import os
import re
import sys
import unicodedata

V = os.path.dirname(os.path.abspath(__file__))


def norm(s):
    s = unicodedata.normalize('NFKC', s)
    for a, b in [('’', "'"), ('‘', "'"), ('“', '"'), ('”', '"'), ('−', '-'),
                 ('–', '-'), ('—', '-'), ('ﬁ', 'fi'), ('ﬂ', 'fl')]:
        s = s.replace(a, b)
    s = re.sub(r'-\s*\n\s*', '', s)
    s = re.sub(r'\s+', ' ', s)
    return s.lower()


cle, phrase = sys.argv[1], norm(sys.argv[2])
larg = int(sys.argv[3]) if len(sys.argv) > 3 else 0
d = os.path.join(V, 'pages', cle)
res = {}
for pref in ('r', 'p'):
    for f in sorted(os.listdir(d)):
        if not f.startswith(pref):
            continue
        t = norm(open(os.path.join(d, f), errors='ignore').read())
        i = t.find(phrase)
        if i >= 0:
            res.setdefault(pref, []).append(int(f[1:4]))
            if larg and pref == 'r':
                print(f'--- {cle} p.{int(f[1:4])} : ...{t[max(0, i - larg):i + len(phrase) + larg]}...')
print(cle, repr(sys.argv[2][:80]), 'brut:', res.get('r', []), 'mise en page:', res.get('p', []))
