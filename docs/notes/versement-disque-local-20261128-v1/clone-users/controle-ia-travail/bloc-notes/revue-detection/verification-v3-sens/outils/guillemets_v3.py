"""Cherche chaque passage entre « » de la synthèse v3 dans toutes les pages de toutes les clés.

Usage : python3 -I guillemets_v3.py SYNTHESE.md > sortie.txt
Sortie : numéro de ligne de la v3, passage (tronqué), clés et pages où il se trouve (brut ou mise en page).
Les passages sans lettre latine de mot anglais courant sont signalés « non cherché (français ou code) » seulement
s'ils ne se trouvent nulle part.
"""
import os
import re
import sys
import unicodedata

V = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def norm(s):
    s = unicodedata.normalize('NFKC', s)
    for a, b in [('’', "'"), ('‘', "'"), ('“', '"'), ('”', '"'), ('−', '-'),
                 ('–', '-'), ('—', '-'), ('ﬁ', 'fi'), ('ﬂ', 'fl'), ('…', '...')]:
        s = s.replace(a, b)
    s = re.sub(r'-\s*\n\s*', '', s)
    s = re.sub(r'\s+', ' ', s)
    return s.lower().strip()


def charger():
    pages = {}
    base = os.path.join(V, 'pages')
    for cle in sorted(os.listdir(base)):
        for f in sorted(os.listdir(os.path.join(base, cle))):
            n = int(f[1:4])
            t = norm(open(os.path.join(base, cle, f), errors='ignore').read())
            pages.setdefault((cle, n), []).append(t)
    return pages


def main():
    texte = open(sys.argv[1], encoding='utf-8').read().split('\n')
    pages = charger()
    for i, ligne in enumerate(texte, 1):
        for m in re.finditer(r'«\s*(.+?)\s*»', ligne):
            p = m.group(1)
            # passages coupés par « … » : chercher chaque morceau
            morceaux = [x.strip() for x in re.split(r'…|\.\.\.', p) if len(x.strip()) >= 4]
            res = []
            for mo in morceaux:
                q = norm(mo)
                ou = sorted({f'{c}:{n}' for (c, n), ts in pages.items() if any(q in t for t in ts)})
                res.append((mo[:60], ou[:12]))
            print(f'l.{i}\t' + ' || '.join(f'{a!r} -> {b if b else "INTROUVABLE"}' for a, b in res))


if __name__ == '__main__':
    main()
