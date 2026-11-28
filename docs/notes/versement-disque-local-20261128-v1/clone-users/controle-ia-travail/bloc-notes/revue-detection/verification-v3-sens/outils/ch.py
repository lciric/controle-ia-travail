"""Cherche une phrase (normalisée) dans les pages d'une clé ; affiche pages et ligne (fichier rNNN.txt / pNNN.txt).

Usage : python3 -I ch.py CLE "phrase" [page]
Si page est donnée : dit si la phrase est sur cette page et à quelle ligne (brute) elle commence.
"""
import os
import re
import sys
import unicodedata

V = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def norm(s):
    s = unicodedata.normalize('NFKC', s)
    for a, b in [('’', "'"), ('‘', "'"), ('“', '"'), ('”', '"'), ('−', '-'),
                 ('–', '-'), ('—', '-'), ('ﬁ', 'fi'), ('ﬂ', 'fl')]:
        s = s.replace(a, b)
    s = re.sub(r'-\s*\n\s*', '', s)
    s = re.sub(r'\s+', ' ', s)
    return s.lower().strip()


def ligne_debut(texte, phrase_n):
    """Ligne (1-indexée) du fichier où commence la phrase normalisée."""
    lignes = texte.split('\n')
    # construire le texte normalisé cumulatif ligne par ligne
    for i in range(len(lignes)):
        bloc = norm('\n'.join(lignes[i:i + 12]))
        if bloc.startswith(phrase_n[:40]) or phrase_n[:40] in norm(lignes[i]):
            if phrase_n in bloc or phrase_n in norm('\n'.join(lignes[i:i + 30])):
                return i + 1
    # repli : première ligne dont la fenêtre contient la phrase
    for i in range(len(lignes)):
        if phrase_n in norm('\n'.join(lignes[i:i + 30])):
            last = i
    return None


def main():
    cle = sys.argv[1]
    phrase = norm(sys.argv[2])
    page = int(sys.argv[3]) if len(sys.argv) > 3 else None
    d = os.path.join(V, 'pages', cle)
    res = {}
    for pref in ('r', 'p'):
        hits = []
        for f in sorted(os.listdir(d)):
            if not f.startswith(pref):
                continue
            t = open(os.path.join(d, f), errors='ignore').read()
            if phrase in norm(t):
                n = int(f[1:4])
                # ligne approximative
                lignes = t.split('\n')
                ln = None
                for i in range(len(lignes)):
                    if phrase in norm('\n'.join(lignes[i:])):
                        ln = i + 1
                    else:
                        break
                hits.append((n, ln))
        res[pref] = hits
    print(cle, repr(sys.argv[2][:80]), 'brut:', res['r'], 'mise_en_page:', res['p'])
    if page is not None:
        ok = any(n == page for n, _ in res['r']) or any(n == page for n, _ in res['p'])
        print('page', page, 'OK' if ok else 'ABSENTE')


if __name__ == '__main__':
    main()
