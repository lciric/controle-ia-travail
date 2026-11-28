"""Comme guillemets_v3.py, mais les passages entre « » peuvent courir sur plusieurs lignes.

Usage : python3 -I guillemets_multi.py FICHIER.md > sortie.txt
Pour chaque passage : ligne de début, passage (tronqué), clés:pages où il se trouve, ou INTROUVABLE.
Les passages imbriqués (« … « … » … ») sont découpés au premier « » fermant ; les morceaux de moins de
quatre caractères sont ignorés.
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
    brut = open(sys.argv[1], encoding='utf-8').read()
    pages = charger()
    # position -> numéro de ligne
    debuts = [0]
    for m in re.finditer('\n', brut):
        debuts.append(m.end())

    def ligne(pos):
        lo, hi = 0, len(debuts) - 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if debuts[mid] <= pos:
                lo = mid
            else:
                hi = mid - 1
        return lo + 1

    for m in re.finditer(r'«\s*(.+?)\s*»', brut, flags=re.S):
        p = re.sub(r'\s+', ' ', m.group(1))
        if not re.search(r'[A-Za-z]{3,}', p):
            continue
        morceaux = [x.strip() for x in re.split(r'…|\.\.\.|«', p) if len(x.strip()) >= 4]
        res = []
        for mo in morceaux:
            q = norm(mo)
            ou = sorted({f'{c}:{n}' for (c, n), ts in pages.items() if any(q in t for t in ts)})
            res.append((mo[:70], ou[:10]))
        print(f'l.{ligne(m.start())}\t' + ' || '.join(f'{a!r} -> {b if b else "INTROUVABLE"}' for a, b in res))


if __name__ == '__main__':
    main()
