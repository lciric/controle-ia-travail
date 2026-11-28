# Vérification indépendante, en lecture seule : relit les deux errata sur disque.
import re, hashlib
def blocs(chemin):
    L = open(chemin, encoding='utf-8').read().split('\n')
    out = []
    for i, l in enumerate(L):
        m = re.match(r'^\*\*([A-Z]+-[0-9A-Za-z]+)\.\*\* ANCIEN : « (.*) »$', l)
        if m:
            n = re.match(r'^NOUVEAU : « (.*) »$', L[i+1]); assert n, (chemin, m.group(1))
            assert L[i+2].startswith('Raison : '), m.group(1)
            assert L[i+3] == '', m.group(1)
            assert L[i-1] == '', m.group(1)
            out.append((m.group(1), m.group(2), n.group(1)))
    # aucune ligne ANCIEN/NOUVEAU orpheline
    assert sum(1 for l in L if ' ANCIEN : « ' in l) == len(out)
    assert sum(1 for l in L if l.startswith('NOUVEAU : « ')) == len(out)
    return out
def controle(err, cible, autres=()):
    t = open(cible, encoding='utf-8').read()
    B = blocs(err)
    ids = [b[0] for b in B]; assert len(set(ids)) == len(ids)
    spans = []
    for ident, a, n in B:
        assert '«' not in a and '»' not in a and '«' not in n and '»' not in n, ident
        assert t.count(a) == 1, (ident, t.count(a))
        assert a != n, ident
        i = t.find(a); spans.append((i, i+len(a), ident))
    spans.sort()
    for x, y in zip(spans, spans[1:]): assert x[1] <= y[0], (x, y)
    u = t
    for ident, a, n in B:
        assert u.count(a) == 1, ('seq', ident); u = u.replace(a, n)
    for o in autres:
        v = open(o, encoding='utf-8').read()
        for ident, a, n in B: assert v.count(a) == 1, ('autre', o, ident)
    return B, hashlib.sha256(u.encode()).hexdigest(), spans
T = 'docs/notes/revendications-en-vigueur-v2/table-revendications-en-vigueur-v2-corrigee-v1.md'
P = 'docs/programme-controle-ia-v3.md'
PB = 'docs/notes/dossier-entretien-2026-12-01-v1/application-demande-27-defaut-2026-11-24/programme-controle-ia-v3-lecture-avec-erratum-1-variante-B.md'
E1 = 'docs/notes/dossier-entretien-2026-12-01-v1/erratum-1-programme-v3-lemme-application-v3.md'
ET = 'docs/notes/revendications-en-vigueur-v2/table-revendications-en-vigueur-v2-corrigee-v1-erratum-1.md'
E2 = 'docs/notes/dossier-entretien-2026-12-01-v1/erratum-2-programme-v3-epreuves-avant-g0-v1.md'
B, h, _ = controle(ET, T)
print('table :', len(B), 'entrées ; après application', h)
assert h in open(ET, encoding='utf-8').read()
B2, h2, s2 = controle(E2, P, autres=[PB])
print('programme :', len(B2), 'entrées ; après application', h2)
assert h2 in open(E2, encoding='utf-8').read()
# recouvrement avec l'erratum 1, variante B
e1 = open(E1, encoding='utf-8').read().split('<!-- variante B : début -->')[1].split('<!-- variante B : fin -->')[0]
A1 = re.findall(r'^\*\*L-\d\.\*\* ANCIEN : « (.*) »$', e1, flags=re.M); assert len(A1) == 8
p = open(P, encoding='utf-8').read()
for a1 in A1:
    assert p.count(a1) == 1
    i = p.find(a1)
    for (x, y, ident) in s2:
        assert y <= i or i + len(a1) <= x, ident
    for ident, a, n in B2: assert a not in a1 and a1 not in a
print('aucun recouvrement avec les 8 ANCIEN de l erratum 1 (variante B)')
# énoncé de la variante B présent à l'octet dans l'entrée T-L2
enonce = [l for l in open(E1, encoding='utf-8').read().split('\n') if l.startswith('> Chez des agents')][1][2:]
assert [n for i, a, n in B if i == 'T-L2'][0].count(enonce) == 1
print('énoncé variante B copié à l octet dans T-L2')
for f in (ET, E2):
    s = open(f, encoding='utf-8').read()
    print(f, hashlib.sha256(s.encode()).hexdigest(), len(s.split('\n')), 'lignes', '\xa0' in s)
