"""Recherche d'une phrase sur une page exacte d'un PDF (texte extrait par pdftotext, modes d, r, p).
Usage : pg.py RACINE_PAGES CLE PAGE "phrase" [largeur]   (PAGE = 0 : toutes les pages)
Sortie : modes ou la phrase est trouvee, et contexte normalise."""
import sys, os, re, unicodedata
def norm(s):
    s = unicodedata.normalize('NFKC', s)
    for a, b in [('’', "'"), ('‘', "'"), ('“', '"'), ('”', '"'), ('−', '-'),
                 ('–', '-'), ('—', '-'), ('ﬁ', 'fi'), ('ﬂ', 'fl'), (' ', ' ')]:
        s = s.replace(a, b)
    s = re.sub(r'-\s*\n\s*', '', s)
    s = re.sub(r'\s+', ' ', s)
    return s.lower()
racine, cle, page, phrase = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4]
larg = int(sys.argv[5]) if len(sys.argv) > 5 else 200
d = os.path.join(racine, cle)
pages = sorted({int(f[1:4]) for f in os.listdir(d)})
cibles = pages if page == 0 else [page]
q = norm(phrase)
trouve = False
for p in cibles:
    modes = []
    ctx = None
    for m in 'drp':
        f = os.path.join(d, '%s%03d.txt' % (m, p))
        if not os.path.exists(f):
            continue
        t = norm(open(f, errors='ignore').read())
        i = t.find(q)
        if i >= 0:
            modes.append(m)
            if ctx is None:
                ctx = t[max(0, i - larg): i + len(q) + larg]
    if modes:
        trouve = True
        print('%s p.%d modes=%s :: ...%s...' % (cle, p, ''.join(modes), ctx))
if not trouve:
    print('%s p.%s ABSENT :: %r' % (cle, page if page else 'toutes', phrase[:80]))
