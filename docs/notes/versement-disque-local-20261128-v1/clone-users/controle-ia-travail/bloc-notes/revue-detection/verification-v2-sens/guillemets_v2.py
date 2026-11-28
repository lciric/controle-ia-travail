"""Extrait les passages entre guillemets français de la synthèse v2 et cherche chacun dans toutes les pages de
toutes les clés (texte extrait par le vérificateur v2-sens). Imprime : ligne de la v2, passage, clés et pages trouvées.
Usage : python3 -I guillemets_v2.py CHEMIN_V2"""
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


pages = {}
for cle in sorted(os.listdir(os.path.join(V, 'pages'))):
    d = os.path.join(V, 'pages', cle)
    for f in sorted(os.listdir(d)):
        if f.startswith('r'):
            pages[(cle, int(f[1:4]))] = norm(open(os.path.join(d, f), errors='ignore').read())

texte = open(sys.argv[1], encoding='utf-8').read()
lignes = texte.split('\n')
# position -> numéro de ligne
debuts = []
p = 0
for i, l in enumerate(lignes):
    debuts.append(p)
    p += len(l) + 1


def ligne_de(pos):
    lo = 0
    for i, d in enumerate(debuts):
        if d > pos:
            break
        lo = i
    return lo + 1


for m in re.finditer(r'«\s*(.+?)\s*»', texte, flags=re.S):
    brut = m.group(1)
    q = norm(brut.replace('…', ' '))
    morceaux = [x.strip() for x in re.split(r'\.\.\.|…', norm(brut)) if len(x.strip()) >= 12]
    if not morceaux:
        continue
    trouves = []
    for (cle, pg), t in pages.items():
        if all(x in t for x in morceaux):
            trouves.append(f'{cle} p.{pg}')
    print(f'l.{ligne_de(m.start())}\t{brut[:90]!r}\t-> {", ".join(trouves[:8]) if trouves else "INTROUVABLE"}')
