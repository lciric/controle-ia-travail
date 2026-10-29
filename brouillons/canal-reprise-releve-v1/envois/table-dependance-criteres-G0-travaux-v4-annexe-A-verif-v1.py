#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Annexe A de la table de dépendance « critères de G0 -> travaux », v4.

Usage (toujours `python3 -I`) ; D = la table, V1 = la table v1, DEC = fichiers de décisions séparés par des virgules :
  verifier   D V1 DEC               structure + recalcul de chaque ligne dérivée, comparée une à une
  artefact   D V1 DEC               R5 : une copie altérée doit faire échouer `verifier`
  feuille    D V1 DEC "A=..;G=..;V=..;C=..;abs=..;val=..[;pres=..][;gel=..]"   (appelle `verifier` d'abord)
  tester     D V1 DEC DEPOT [P-X=chemin+chemin,...]   T1, T2, T4 sur chaque produit ; imprime abs=
  constat    D V1 DEC FICHIER "A=2,3"       contrôle le format fermé du constat du 31 décembre ; imprime pres=
  calculer   D V1 DEC               imprime les cellules dérivées (pour les recoller dans la table)
  essais     D V1 DEC [DEPOT]       R5 : altérations, refus de la feuille, constat, tester ; code non nul si une garde manque
  aveugle    D                      imprime les lignes sans classe ni produit, pour une classification à l'aveugle
  concordance D FICHIER             compare des réponses « Wxx classe produits sert » à la table
Aucun repli silencieux : toute anomalie lève une erreur et un code de sortie non nul.
"""
import glob, hashlib, os, re, subprocess, sys, tempfile


class Echec(Exception):
    pass


def exige(c, m):
    if not c:
        raise Echec(str(m))


cells = lambda l: [c.strip() for c in l.strip().strip('|').split('|')]
ks = lambda t: set(map(int, re.findall(r'\d', t)))
fmt = lambda s: ', '.join(sorted(s)) or 'aucune'
NOM = r'P-[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*'
CV = ('établi', 'négatif', 'autre')
TYPES = ('verdict', 'lecture', 'prereg', 'autre')
CLES = {'abs', 'A', 'G', 'V', 'C', 'pres', 'gel', 'val'}
EMPREINTE_SCRIPT = lambda: hashlib.sha256(open(__file__, 'rb').read()).hexdigest()


# ---------------------------------------------------------------- lecture de la table
def prods(cell):
    if cell.strip() == '—':
        return []
    r = []
    for x in cell.split(','):
        x = x.strip(); n = x.rstrip('†‡'); m = x[len(n):]
        exige(re.fullmatch(NOM, n), ('produit mal formé', x))
        exige(set(m) <= set('†‡'), ('marque inconnue', x))
        r.append((n, '†' in m, '‡' in m))
    return r


pr = lambda w: [n for n, _, _ in prods(w['prod'])]
ets = lambda w: {n for n, _, e in prods(w['prod']) if e}


def fourn(w):
    return [] if w['four'] == '—' else [x.strip() for x in w['four'].split(',')]


def tab(texte, pre, n):
    r = [cells(l) for l in texte.splitlines() if l.startswith(pre)]
    exige(r, 'table absente ' + pre)
    for c in r:
        exige(len(c) == n, ('colonnes', c[0], len(c), n))
    return r


def charge(texte):
    W = [dict(zip(('ref', 'trav', 'prod', 'four', 'sert', 'cl', 'src'), c)) for c in tab(texte, '| W', 7)]
    P = {}
    for c in tab(texte, '| P-', 8):
        exige(c[0] not in P, ('produit en double', c[0]))
        P[c[0]] = dict(k=int(c[1]) if c[1].isdigit() else 0, typ=c[2], pro=c[3], cls=c[4], chem=c[5])
    return W, P


def classe(w):
    s = w['src']
    if re.search(r'\bd1\b|\bd2\b|préalable', s):
        return 'F'
    if '[H]' in s:
        return 'H'
    if w['prod'] != '—':
        return 'K'
    return 'R' if '[REJEU]' in s else 'I'


def kprod(P):
    return {v['k']: p for p, v in P.items() if v['k']}


def cvk(P):
    return sorted(v['k'] for v in P.values() if v['k'] and v['cls'] == 'oui')


# ---------------------------------------------------------------- règles de lecture
def heritiers(W, P, X0, ab):
    """L9 : producteurs, sans « sert », des produits auxiliaires absents requis (de proche en proche) par les lignes visées."""
    by = {w['ref']: w for w in W}
    need = set(); todo = [by[r] for r in X0 if r in by]
    while todo:
        x = todo.pop()
        for p in pr(x):
            if p in ab and P[p]['k'] == 0 and P[p]['pro'] != '—' and P[p]['pro'] in by and P[p]['pro'] not in need:
                need.add(P[p]['pro']); todo.append(by[P[p]['pro']])
    return {r for r in need if by[r]['sert'] == '—' and by[r]['cl'] in 'KI'}


def analyser(W, P, ab, val, G1, A, pres, gel):
    """Retourne {réf: (état, motif, droit de devis)}, G', A'."""
    G = set(G1) | set(gel) | {k for k, v in val.items() if v == 'négatif'}
    Ap = (set(A) - set(pres)) - G
    X0 = {w['ref'] for w in W if w['cl'] in 'KIR' and ks(w['sert']) & Ap and not ks(w['sert']) & G}
    heirs = heritiers(W, P, X0, ab)
    st = {}
    for w in W:
        s = ks(w['sert']); c = w['cl']; a = sorted(set(pr(w)) & ab)
        ne = sorted(n for n in ets(w) if n not in ab and val.get(P[n]['k']) != 'établi')
        if c == 'F': e, m = 'fermée', 'L1'
        elif c == 'H': e, m = 'Lazar', 'L6'
        elif s & G: e, m = 'fermée', 'L2 gel %s' % sorted(s & G)
        elif c == 'K' and a: e, m = 'fermée', 'L3 absent %s' % a
        elif c == 'K' and ne: e, m = 'fermée', 'L3 non établi %s' % ne
        elif c == 'R' and not s & Ap: e, m = 'fermée', 'L4 hors A'
        else: e, m = 'ouverte', 'L3' if c == 'K' else 'L4'
        st[w['ref']] = (e, m, e == 'ouverte' and (bool(s & Ap) or w['ref'] in heirs))
    return st, G, Ap


# ---------------------------------------------------------------- arguments
def lire_spec(s):
    d = {}
    for x in filter(None, s.split(';')):
        exige('=' in x, ('argument sans =', x))
        k, v = x.split('=', 1)
        exige(k not in d, ('clé en double', k))
        d[k] = v
    exige(set(d) <= CLES, ('clé inconnue', sorted(set(d) - CLES)))
    return d


def ensemble(t, nom):
    if not t.strip():
        return set()
    L = [x.strip() for x in t.split(',')]
    exige(all(re.fullmatch(r'[1-8]', x) for x in L), (nom, 'critère hors 1..8', t))
    exige(len(set(L)) == len(L), (nom, 'doublon', t))
    return set(map(int, L))


def produits(t, P):
    if not t.strip():
        return set()
    L = [x.strip() for x in t.split(',')]
    exige(len(set(L)) == len(L), ('abs : doublon', t))
    for x in L:
        exige(x in P, ('produit inexistant', x))
    return set(L)


def evaluer(W, P, s, strict):
    """Valide une spécification de scénario ou de feuille ; retourne (ab, val, G1, A, V, C, pres, gel)."""
    d = lire_spec(s)
    if strict:
        manque = {'A', 'G', 'V', 'C', 'abs', 'val'} - set(d)
        exige(not manque, ('arguments manquants', sorted(manque)))
    A, G1, V, C = (ensemble(d.get(x, ''), x) for x in 'AGVC')
    for x, y in (('A', 'G'), ('A', 'V'), ('A', 'C'), ('G', 'V'), ('G', 'C'), ('V', 'C')):
        exige(not ({'A': A, 'G': G1, 'V': V, 'C': C}[x] & {'A': A, 'G': G1, 'V': V, 'C': C}[y]), ('états de V1 non disjoints', x, y))
    pres = ensemble(d.get('pres', ''), 'pres'); exige(pres <= A, ('pres hors de A', sorted(pres - A)))
    gel = ensemble(d.get('gel', ''), 'gel')
    ab = produits(d.get('abs', ''), P)
    kp = kprod(P); K = cvk(P); val = {}
    for x in filter(None, d.get('val', '').split(',')):
        exige(re.fullmatch(r'[1-8]:(établi|négatif|autre)', x.strip()), ('val mal formée', x))
        k = int(x.strip()[0]); exige(k not in val, ('val : doublon', k))
        exige(k in K, ('val : critère sans classe lue', k))
        exige(kp[k] not in ab, ('val : produit absent, aucune classe à lire', kp[k]))
        val[k] = x.strip().split(':')[1]
    for k in K:
        if kp[k] not in ab and k not in val:
            exige(not strict, ('val manquante : produit présent, classe à copier', k, kp[k]))
            val[k] = 'négatif' if k in G1 else 'établi'
    return ab, val, G1, A, V, C, pres, gel


SC = ['abs=P-V6,P-L7;G=;A=2,3',
      'abs=P-7,P-8;G=;A=2',
      'abs=P-PIL;G=;A=6',
      'abs=P-PIL;G=3;A=6',
      'abs=P-L7,P-B4;G=2;A=3,4',
      'abs=P-L7,P-B4;G=;A=2,3,4;val=2:négatif',
      'abs=;G=;A=4;val=3:négatif',
      'abs=;G=;A=3;val=2:autre']


def scenario(W, P, s):
    ab, val, G1, A, V, C, pres, gel = evaluer(W, P, s, False)
    st, G, Ap = analyser(W, P, ab, val, G1, A, pres, gel)
    by = {w['ref']: w for w in W}
    f23 = {r for r, (e, m, d) in st.items() if m.startswith(('L2', 'L3 ')) and e == 'fermée'}
    ro = {r for r, (e, m, d) in st.items() if by[r]['cl'] == 'R' and e == 'ouverte'}
    dv = {r for r, (e, m, d) in st.items() if d}
    return [fmt(f23), fmt(ro), fmt(dv)]


# ---------------------------------------------------------------- audit R4
ANC = {'W1': 'W01', 'W2': 'W04 W05 W06 W07', 'W3': 'W02', 'W4': 'W03', 'W5': 'W36', 'W6': 'W08 W09', 'W7': 'W10', 'W8': 'W11',
       'W9': 'W13 W14 W41 W50', 'W10': 'W15 W16 W17 W40', 'W11': 'W17', 'W12': 'W18 W19', 'W13': 'W32 W33', 'W14': 'W20 W21',
       'W15': 'W22', 'W16': 'W34', 'W17': 'W25', 'W18': 'W26', 'W19': 'W28', 'W20': 'W29', 'W21': 'W35', 'W22': 'W30', 'W23': 'W30',
       'W24': 'W27', 'W25': 'W31'}
JETONS29 = r'\b(?:DP|PG|PC|MO|TC|DV|P40|MSG216|SY)\b'


def audit(W, P, V1t, dates):
    by = {w['ref']: w for w in W}
    v1 = [dict(ref=c[0], dep=c[2], sert=c[3], cl=c[4]) for c in tab(V1t, '| W', 5) if c[0] in ANC]
    used = set(); rs = ra = bo = sr = sa = 0
    for x in v1:
        D = [by[r] for r in ANC[x['ref']].split()]; used |= {d['ref'] for d in D}
        s1 = set() if x['sert'].startswith('—') else ks(x['sert'])
        s3 = set().union(*[ks(d['sert']) for d in D]); sr += len(s1 - s3); sa += len(s3 - s1)
        cond = x['cl'].startswith('cond'); d1 = ks(x['dep']) if cond else set()
        d3 = {P[p]['k'] for d in D for p in pr(d)} - {0}
        aux = any(P[p]['k'] == 0 for d in D for p in pr(d))  # un produit auxiliaire est un produit ajouté
        t = bool(s1 - s3 or d3 - d1 or aux) or (x['cl'].startswith('cont') and any(d['cl'] in 'KRF' for d in D)) or (cond and any(d['cl'] == 'F' for d in D))
        l = bool(s3 - s1 or (d1 - d3 and any(d['cl'] != 'F' for d in D))) or ('ferm' in x['cl'] and any(d['cl'] != 'F' for d in D))
        rs += t; ra += l; bo += t and l
    neuves = [w for w in W if w['ref'] not in used]

    def du29(w):
        ids = re.findall(r'R-\d+', w['src']); jt = re.findall(JETONS29, w['src'])
        return bool(ids or jt) and all(dates.get(i) == '2026-10-29' for i in ids) and not re.search(r'(?<![A-Za-z])[BGE] l\.|T7|N-\d|CLAUDE', w['src'])

    L = [w['ref'] for w in W if du29(w)]; keep = [w for w in W if w['ref'] not in L]
    drop = {p for p, v in P.items() if v['pro'] in L}

    def reduit(w):
        pp = [(n, d, e) for n, d, e in prods(w['prod']) if n not in drop]
        w2 = dict(w, prod=', '.join(n + ('†' if d else '') + ('‡' if e else '') for n, d, e in pp) or '—')
        w2['cl'] = classe(w2)
        return w2

    red = [reduit(w) for w in keep]
    cdiff = sum(a['cl'] != b['cl'] for a, b in zip(keep, red))
    kp = kprod(P); K = cvk(P)
    S = ['abs=' + p for p in P] + ['G=%d' % k for k in range(1, 9)] + ['A=%d' % k for k in range(1, 9)] + ['val=%d:négatif' % k for k in K] + SC
    nd = 0; dl = set(); r0 = {w['ref'] for w in keep}
    for s in S:
        ab, val, G1, A, V, C, pres, gel = evaluer(W, P, s, False)
        a, _, _ = analyser(keep, P, ab, val, G1, A, pres, gel)
        b, _, _ = analyser(red, P, ab, val, G1, A, pres, gel)
        dif = {r for r in r0 if (a[r][0], a[r][2]) != (b[r][0], b[r][2])}
        if dif:
            nd += 1; dl |= dif
    I = [w for w in W if w['cl'] == 'I']; Id = [w for w in I if '[IND]' not in w['src']]
    h = hashlib.sha256('\n'.join(w['src'] for w in W).encode('utf-8')).hexdigest()[:16]
    v = lambda k, x: ('aud:' + k, [str(x)])
    return dict([v('v1', len(v1)), v('resserrees', rs), v('assouplies', ra), v('deux', bo), v('neutres', len(v1) - rs - ra + bo),
                 v('sert-retires', sr), v('sert-ajoutes', sa), v('deductions', sum(w['prod'].count('†') for w in W)),
                 v('lignes-deduites', sum('†' in w['prod'] for w in W)), v('neuves', len(neuves)),
                 v('neuves-sert', sum(w['sert'] != '—' for w in neuves)), v('neuves-ouvertes', sum(w['cl'] in 'IR' for w in neuves)),
                 v('L29', len(L)), v('retrait-sc', len(S)), v('retrait-diff', nd), v('retrait-lignes', len(dl)), v('retrait-classes', cdiff),
                 v('I-total', len(I)), v('I-IND', len(I) - len(Id)), v('I-defaut', len(Id)),
                 v('I-defaut-L29', sum(w['ref'] in L for w in Id)), v('chemins-a-nommer', sum(p['chem'].startswith('à nommer') for p in P.values())),
                 v('sources', h)])


def calc(W, P, V1t, dates):
    aux = {p for p, v in P.items() if v['k'] == 0}
    o = {}
    for p in P:
        o[p] = [fmt({w['ref'] for w in W if w['cl'] == 'K' and p in pr(w)}), fmt({w['ref'] for w in W if w['cl'] == 'K' and p in ets(w)})]
    for k in range(1, 9):
        L = [w for w in W if w['cl'] in 'KIR' and k in ks(w['sert'])]
        o['k:%d' % k] = [fmt({w['ref'] for w in L}), fmt({w['ref'] for w in L if w['cl'] == 'R'}), fmt(heritiers(W, P, {w['ref'] for w in L}, aux))]
    for s in SC:
        o['sc:' + s] = scenario(W, P, s)
    o.update(audit(W, P, V1t, dates))
    return o


def verifier_texte(texte, V1t, dates):
    W, P = charge(texte)
    exige(len({w['ref'] for w in W}) == len(W), 'refs en double')
    exige(sorted(p['k'] for p in P.values() if p['k']) == list(range(1, 9)), 'un produit par critère')
    four = {}
    for w in W:
        exige(re.fullmatch(r'W\d\d', w['ref']), ('réf mal formée', w['ref']))
        for x in pr(w):
            exige(x in P, (w['ref'], 'produit inconnu', x))
        for x in fourn(w):
            exige(x in P, (w['ref'], 'produit fourni inconnu', x))
            exige(x not in four, ('produit fourni par deux lignes', x)); four[x] = w['ref']
        exige(classe(w) == w['cl'], (w['ref'], 'classe recalculée sans date'))
        exige(w['cl'] not in 'FH' or w['sert'] == '—', (w['ref'], 'F ou H avec sert'))
        exige(w['cl'] != 'R' or w['sert'] != '—', (w['ref'], 'R sans sert'))
        exige(w['sert'] == '—' or re.fullmatch(r'[1-8](, [1-8])*', w['sert']), (w['ref'], 'sert mal formé'))
        exige(not set(fourn(w)) & set(pr(w)), (w['ref'], 'cite son propre produit'))
        exige('[IND]' not in w['src'] or w['cl'] == 'I', (w['ref'], '[IND] hors classe I'))
        for n in ets(w):
            exige(P[n]['cls'] == 'oui', (w['ref'], '‡ sur un produit sans classe lue', n))
    for p, v in P.items():
        exige(v['pro'] == four.get(p, '—'), (p, 'producteur différent de la ligne qui le fournit', v['pro'], four.get(p, '—')))
        exige(v['typ'] in TYPES, (p, 'type inconnu'))
        exige(v['cls'] in ('oui', 'non'), (p, 'classe oui/non'))
        exige(v['cls'] == 'non' or v['typ'] in ('verdict', 'lecture'), (p, 'classe lue sur un produit sans verdict'))
        exige(v['chem'] != '—', (p, 'chemin absent'))
    g = {w['ref']: {P[x]['pro'] for x in pr(w)} - {'—'} for w in W}

    def vis(r, pile):
        exige(r not in pile, ('cycle', pile, r))
        for s in g[r]:
            vis(s, pile + [r])
    for r in g:
        vis(r, [])
    o = calc(W, P, V1t, dates)
    rows = {}
    for l in texte.splitlines():
        if l.startswith('|'):
            c = cells(l)
            if c and re.fullmatch(r'P-[A-Za-z0-9-]+|k:\d+|sc:.+|aud:[A-Za-z0-9-]+', c[0]):
                rows.setdefault(c[0], []).append(c)
    exige(set(rows) == set(o), ('lignes dérivées en trop ou manquantes', sorted(set(rows) ^ set(o))))
    for key, v in o.items():
        exige(len(rows[key]) == 1, ('ligne dérivée dupliquée', key))
        exige(rows[key][0][-len(v):] == v, ('ligne dérivée fausse', key, v, rows[key][0]))
    return W, P, o


def charger_dec(dec):
    dates = {}
    for f in dec.split(','):
        for l in open(f, encoding='utf-8'):
            m = re.match(r'\| (R-\d+) \| (\S+) \|', l)
            if m:
                dates[m.group(1)] = m.group(2)
    return dates


def lire(p):
    return open(p, encoding='utf-8').read()


# ---------------------------------------------------------------- feuille
def feuille(D, V1, DEC, spec):
    texte = lire(D); W, P, o = verifier_texte(texte, lire(V1), charger_dec(DEC))
    ab, val, G1, A, V, C, pres, gel = evaluer(W, P, spec, True)
    st, G, Ap = analyser(W, P, ab, val, G1, A, pres, gel)
    T = set(range(1, 9)) - A - G1 - V - C
    ls = lambda s: ','.join(map(str, sorted(s))) or '—'
    print('FEUILLE DE REPLI | table sha256 %s | script sha256 %s' % (hashlib.sha256(texte.encode('utf-8')).hexdigest(), EMPREINTE_SCRIPT()))
    print('V1 : A=%s G=%s V=%s C=%s tenus=%s | constat : pres=%s | gel antérieur=%s' % (ls(A), ls(G1), ls(V), ls(C), ls(T), ls(pres), ls(gel)))
    print('lu à l\'étape : abs=%s | val=%s' % (','.join(sorted(ab)) or '—', ','.join('%d:%s' % kv for kv in sorted(val.items())) or '—'))
    print('G\' (gel effectif)=%s | A\'=%s' % (ls(G), ls(Ap)))
    for k in sorted(G & {k for k, v in val.items() if v == 'établi'}):
        print('ALERTE : critère %d gelé dont la classe lue est établi : le gel demeure (L2bis)' % k)
    for r in sorted(st):
        e, m, d = st[r]
        print(r, e, m, 'devis' if d else '—')
    n = lambda x: sum(1 for v in st.values() if v[0] == x)
    print('bilan : %d ouvertes, %d fermées, %d à Lazar, %d avec droit de devis' % (n('ouverte'), n('fermée'), n('Lazar'), sum(v[2] for v in st.values())))


# ---------------------------------------------------------------- tests de produit (T1, T2, T4)
def sha(f):
    h = hashlib.sha256()
    with open(f, 'rb') as fh:
        for b in iter(lambda: fh.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def t2(f):
    c = f + '.sha256'
    if not os.path.isfile(c):
        return 'T2 compagnon absent'
    l = [x for x in lire(c).splitlines() if x.strip()]
    if len(l) != 1:
        return 'T2 compagnon : une ligne attendue'
    m = re.fullmatch(r'([0-9a-f]{64})  (\S.*)', l[0])
    if not m:
        return 'T2 compagnon illisible'
    if m.group(2) != os.path.basename(f):
        return 'T2 nom du compagnon'
    return None if m.group(1) == sha(f) else 'T2 empreinte différente'


def t4(depot, f):
    sys.path.insert(0, os.path.join(depot, 'src'))
    try:
        from controle_ia.prereg import exiger_prereg_scelle
    except Exception as e:
        raise Echec('T4 impossible : import de controle_ia.prereg échoué (%s) ; aucun repli' % e)
    try:
        exiger_prereg_scelle(os.path.abspath(f))
    except Exception as e:
        return 'T4 ' + str(e)[:90]
    return None


version = lambda f: int((re.search(r'-v(\d+)(?:\.[^/]*)?$', f) or [0, 0])[1])


def tester(P, depot, nommes, avec_t4=True):
    abs_ = []; lignes = []
    for p, v in P.items():
        pats = nommes[p].split('+') if p in nommes else ([] if v['chem'].startswith(('nommé par', 'à nommer')) else v['chem'].split())
        if not pats:
            abs_.append(p); lignes.append('%s absent (chemin non nommé : %s)' % (p, v['chem'])); continue
        motif = ''; ref = []
        for pat in pats:
            valides = []; raisons = []
            for f in sorted(glob.glob(os.path.join(depot, pat))):
                if f.endswith('.sha256') or not os.path.isfile(f):
                    continue
                r = t2(f) or (t4(depot, f) if (v['typ'] == 'prereg' and avec_t4) else None)
                (raisons if r else valides).append(r or f)
            if not valides:
                motif = 'T1 aucun fichier pour %s' % pat if not raisons else raisons[-1] + ' (%s)' % pat; break
            ref.append(max(valides, key=lambda f: (version(f), f)))
        if motif:
            abs_.append(p); lignes.append('%s absent (%s)' % (p, motif))
        else:
            lignes.append('%s présent : %s' % (p, ' ; '.join(os.path.relpath(f, depot) for f in ref)))
    return abs_, lignes


# ---------------------------------------------------------------- constat du 31 décembre
def constat(A, fichier):
    pres = set(); vus = set(); entetes = {'commit C_31': False, 'grille': False}
    for l in lire(fichier).splitlines():
        if not l.strip() or l.startswith('#'):
            continue
        m = re.fullmatch(r'critère ([1-8]) : (présents|absents(?: — T[1-4])?)', l)
        if m:
            k = int(m.group(1)); exige(k in A, ('critère hors de A', k)); exige(k not in vus, ('critère en double', k)); vus.add(k)
            if m.group(2) == 'présents':
                pres.add(k)
            continue
        m = re.fullmatch(r'(commit C_31|grille) : ([0-9a-f]{40}|[0-9a-f]{64})', l)
        exige(m, ('ligne hors format fermé', l)); exige(not entetes[m.group(1)], ('en-tête en double', m.group(1))); entetes[m.group(1)] = True
    exige(vus == A, ('critères de A non couverts', sorted(A - vus)))
    exige(all(entetes.values()), ('en-tête manquant', [k for k, v in entetes.items() if not v]))
    return pres


# ---------------------------------------------------------------- classification à l'aveugle
def aveugle(W):
    for w in W:
        s = re.sub(r'\[(?:H|REJEU|IND)\]|\b(?:d1|d2|préalable)\b', '', w['src'])
        print('%s | %s | %s' % (w['ref'], w['trav'], re.sub(r'\s*;\s*;', ' ;', s).strip(' ;')))


def concordance(W, fichier):
    rep = {}
    for l in lire(fichier).splitlines():
        if not l.strip():
            continue
        m = re.fullmatch(r'(W\d\d) ([FKRIH]) (—|P-\S+) (—|[1-8](?:,[1-8])*)', l.strip())
        exige(m, ('réponse mal formée', l)); exige(m.group(1) not in rep, ('réponse en double', m.group(1)))
        rep[m.group(1)] = (m.group(2), set() if m.group(3) == '—' else set(m.group(3).split(',')), set() if m.group(4) == '—' else set(map(int, m.group(4).split(','))))
    ecarts = 0
    for w in W:
        if w['ref'] not in rep:
            continue
        c, p, s = rep[w['ref']]
        mot = [x for x, ok in (('classe', c == w['cl']), ('produits', p == set(pr(w))), ('sert', s == ks(w['sert']))) if not ok]
        if mot:
            ecarts += 1; print('ÉCART', w['ref'], ','.join(mot), '| table :', w['cl'], fmt(set(pr(w))), w['sert'])
    exige(set(rep) <= {w['ref'] for w in W}, ('réponse sur une réf inconnue', sorted(set(rep) - {w['ref'] for w in W})))
    print('concordance : %d réponses, %d écarts' % (len(rep), ecarts))


# ---------------------------------------------------------------- essais (R5)
def altérations(base):
    def sub(old, new, n=1):
        exige(old in base, ('essai : texte introuvable', old[:60]))
        return base.replace(old, new, n)
    L = {}
    L['E01 cellule k:3 inversée'] = sub('| k:3 | W12, W15, W16, W40 |', '| k:3 | W12, W15, W16 |')
    L['E02 produit ajouté à W15'] = sub('témoin lexical | P-T04† |', 'témoin lexical | P-T04†, P-NM |')
    L['E03 sert de W16 : 3 -> 2, 3'] = sub('| P-T04†, P-V6‡, P-7, P-P4, P-EP | P-L7, P-LST | 3 |', '| P-T04†, P-V6‡, P-7, P-P4, P-EP | P-L7, P-LST | 2, 3 |')
    L['E04 aud:neutres modifié'] = re.sub(r'(\| aud:neutres \| [^|]*\| )(\d+)( \|)', lambda m: m.group(1) + str(int(m.group(2)) + 1) + m.group(3), base, count=1)
    L['E05 producteur de P-L7 changé (colonne producteur)'] = sub('| P-L7 | 3 | verdict | W16 |', '| P-L7 | 3 | verdict | W19 |')
    L['E06 classe de W20 K -> I'] = sub('| P-T03† | — | 6 | K |', '| P-T03† | — | 6 | I |')
    L['E07 ligne W42 supprimée'] = ''.join(l for l in base.splitlines(True) if not l.startswith('| W42 |'))
    L['E08 jeton [REJEU] retiré de W09'] = sub('D R-025 ; [REJEU]', 'D R-025')
    L['E09 scénario 1 : une cellule changée'] = sub('| sc:abs=P-V6,P-L7;G=;A=2,3 | W16, W19, W21 |', '| sc:abs=P-V6,P-L7;G=;A=2,3 | W16, W19 |')
    L['E10 † retiré de W11'] = sub('rubrique | P-T04† |', 'rubrique | P-T04 |')
    L['E11 W24 (F) reçoit un sert'] = sub('sentinelle GO-03 | — | — | — | F |', 'sentinelle GO-03 | — | — | 5 | F |')
    L['E12 ligne k:2 dupliquée, fausse en tête'] = sub('| k:2 |', '| k:2 | W99 | aucune | aucune |\n| k:2 |')
    L['E13 ligne k:9 parasite'] = sub('| k:8 |', '| k:9 | W01 | aucune | aucune |\n| k:8 |')
    L['E27 cycle réel : W41 cite P-L7 (W16 attend P-V6 de W41)'] = sub('| P-T04†, P-6, P-7, P-8 | P-V6, P-EP |', '| P-T04†, P-6, P-7, P-8, P-L7 | P-V6, P-EP |')
    L['E14 cycle : W16 cite P-L7'] = sub('| P-T04†, P-V6‡, P-7, P-P4, P-EP | P-L7, P-LST | 3 |', '| P-T04†, P-V6‡, P-7, P-P4, P-EP, P-L7 | P-L7, P-LST | 3 |')
    L['E15 ligne P-T04 : W48 retirée'] = sub(', W47, W48, W51 |', ', W47, W51 |')
    L['E16 W19 : P-L7 ajouté (resserrement)'] = sub('| P-T04†, P-V6‡, P-LST, P-8, P-EP |', '| P-T04†, P-V6‡, P-LST, P-8, P-EP, P-L7 |')
    L['E17 citation de source changée'] = sub('B l.126-135 ; G l.356-362', 'B l.999-1000 ; G l.356-362')
    L['E18 W38 : [H] remplacé'] = sub('R-485 ; [H] |', 'R-485 ; [X] |')
    L['E19 W34 reçoit sert 2, sans mise à jour des tables'] = sub('essais hors ligne (v44 à v47) ; course réelle = dépense facturée sur GO | — | — | — | I |', 'essais hors ligne (v44 à v47) ; course réelle = dépense facturée sur GO | — | — | 2 | I |')
    L['E20 W34 sert 2 et k:2 mis à jour (cohérent)'] = L['E19 W34 reçoit sert 2, sans mise à jour des tables'].replace('| k:2 | W13, W14, W41, W50 |', '| k:2 | W13, W14, W34, W41, W50 |')
    L['E21 ‡ retiré de W16'] = sub('| P-T04†, P-V6‡, P-7, P-P4, P-EP | P-L7, P-LST | 3 |', '| P-T04†, P-V6, P-7, P-P4, P-EP | P-L7, P-LST | 3 |')
    L['E22 W23 : sert 6 ajouté (droit direct)'] = sub('| P-T04†, P-ARR | P-PIL | — | K |', '| P-T04†, P-ARR | P-PIL | 6 | K |')
    L['E23 W16 cite un produit inexistant'] = sub('| P-T04†, P-V6‡, P-7, P-P4, P-EP | P-L7, P-LST | 3 |', '| P-T04†, P-V6‡, P-7, P-P4, P-EP, P-V66 | P-L7, P-LST | 3 |')
    L['E24 produit fourni deux fois'] = sub('| P-L7, P-LST | 3 |', '| P-L7, P-LST, P-B4 | 3 |')
    L['E25 P-V6 : classe lue retirée'] = sub('| P-V6 | 2 | verdict | W41 | oui |', '| P-V6 | 2 | verdict | W41 | non |')
    L['E26 [IND] sur une ligne K'] = sub('B l.154-158 ; E l.44', 'B l.154-158 ; E l.44 ; [IND]')
    return L


def essais(D, V1, DEC, depot):
    base = lire(D); V1t = lire(V1); dates = charger_dec(DEC); manque = []; ok = 0
    W, P, o = verifier_texte(base, V1t, dates)
    print('sain : verifier OK (%d lignes de travaux, %d lignes dérivées)' % (len(W), len(o)))
    for nom, txt in altérations(base).items():
        try:
            verifier_texte(txt, V1t, dates)
        except Echec as e:
            ok += 1; print('détectée    ', nom, '|', str(e)[:90])
        else:
            manque.append(nom); print('NON DÉTECTÉE', nom)
    spec = 'A=2,3;G=;V=;C=;abs=P-V6,P-L7;val=1:établi,5:établi'
    sains = [spec, 'A=3,4;G=;V=;C=;abs=P-L7,P-B4;val=1:établi,2:négatif,5:établi;gel=2',
             'A=6;G=;V=;C=;abs=P-PIL;val=1:établi,2:établi,3:établi,5:établi']
    for s in sains:
        feuille_ok(D, V1, DEC, s)
    print('feuilles saines : %d produites sans erreur' % len(sains))
    refus = {'produit inexistant (P-V66)': 'A=2,3;G=;V=;C=;abs=P-V66;val=1:établi,2:établi,3:établi,5:établi',
             'critère hors 1..8 (A=9)': 'A=9;G=;V=;C=;abs=;val=1:établi,2:établi,3:établi,5:établi',
             'A et G non disjoints': 'A=2;G=2;V=;C=;abs=;val=1:établi,2:établi,3:établi,5:établi',
             'val manquante': 'A=2;G=;V=;C=;abs=;val=1:établi',
             'val sur un produit absent': 'A=2;G=;V=;C=;abs=P-V6;val=1:établi,2:établi,3:établi,5:établi',
             'val sur un critère sans classe (4)': 'A=2;G=;V=;C=;abs=;val=1:établi,2:établi,3:établi,4:établi,5:établi',
             'valeur inconnue': 'A=2;G=;V=;C=;abs=;val=1:établi,2:vrai,3:établi,5:établi',
             'clé inconnue': 'A=2;G=;V=;C=;abs=;val=1:établi,2:établi,3:établi,5:établi;zzz=1',
             'clé en double': 'A=2;A=3;G=;V=;C=;abs=;val=1:établi,2:établi,3:établi,5:établi',
             'pres hors de A': 'A=2;G=;V=;C=;abs=;pres=3;val=1:établi,2:établi,3:établi,5:établi',
             'argument manquant (V)': 'A=2;G=;C=;abs=;val=1:établi,2:établi,3:établi,5:établi'}
    for nom, s in refus.items():
        try:
            feuille_ok(D, V1, DEC, s)
        except Echec as e:
            ok += 1; print('refusée     ', nom, '|', str(e)[:80])
        else:
            manque.append('feuille ' + nom); print('NON REFUSÉE ', nom)
    # feuille sur une table altérée : doit s'arrêter avant d'imprimer
    with tempfile.TemporaryDirectory() as t:
        bad = os.path.join(t, 'bad.md'); open(bad, 'w', encoding='utf-8').write(altérations(base)['E01 cellule k:3 inversée'])
        try:
            feuille_ok(bad, V1, DEC, sains[0])
        except Echec as e:
            ok += 1; print('refusée      feuille sur table altérée | verifier a arrêté :', str(e)[:60])
        else:
            manque.append('feuille sur table altérée'); print('NON REFUSÉE  feuille sur table altérée')
        # constat
        f = os.path.join(t, 'constat.txt'); h = 'a' * 40
        open(f, 'w', encoding='utf-8').write('# constat\ncommit C_31 : %s\ngrille : %s\ncritère 2 : présents\ncritère 3 : absents — T2\n' % (h, 'b' * 64))
        assert constat({2, 3}, f) == {2}
        print('constat sain : pres={2}')
        for nom, txt in {'chaîne « franchie »': 'commit C_31 : %s\ngrille : %s\ncritère 2 : présents\ncritère 3 : absents — T2\nla porte est franchie\n' % (h, 'b' * 64),
                         'critère manquant': 'commit C_31 : %s\ngrille : %s\ncritère 2 : présents\n' % (h, 'b' * 64),
                         'critère hors de A': 'commit C_31 : %s\ngrille : %s\ncritère 2 : présents\ncritère 3 : absents — T2\ncritère 4 : présents\n' % (h, 'b' * 64),
                         'état « tenu » prononcé': 'commit C_31 : %s\ngrille : %s\ncritère 2 : tenu\ncritère 3 : absents — T2\n' % (h, 'b' * 64),
                         'en-tête absent': 'critère 2 : présents\ncritère 3 : absents — T2\n'}.items():
            open(f, 'w', encoding='utf-8').write(txt)
            try:
                constat({2, 3}, f)
            except Echec as e:
                ok += 1; print('constat refusé', nom, '|', str(e)[:70])
            else:
                manque.append('constat ' + nom); print('constat NON REFUSÉ', nom)
        # tester : dépôt jouet, cas sain et cas altéré (T1, T2)
        j = os.path.join(t, 'depot'); os.makedirs(os.path.join(j, 'docs/verdicts'))
        v = os.path.join(j, 'docs/verdicts/verdict-T0.4-critere-1-G0-v3.md')
        open(v, 'w', encoding='utf-8').write('verdict jouet\n'); open(v + '.sha256', 'w', encoding='utf-8').write('%s  %s\n' % (sha(v), os.path.basename(v)))
        a, lg = tester(P, j, {}, avec_t4=False)
        assert 'P-T04' not in a and 'P-V6' in a, lg
        print('tester sain  : P-T04 présent, P-V6 absent (dépôt jouet)')
        open(v, 'a', encoding='utf-8').write('altéré\n')
        a, lg = tester(P, j, {}, avec_t4=False)
        if 'P-T04' in a:
            ok += 1; print('tester artefact : P-T04 absent après altération |', [x for x in lg if x.startswith('P-T04')][0][:90])
        else:
            manque.append('tester artefact'); print('tester NON DÉTECTÉ')
        os.remove(v + '.sha256')
        a, lg = tester(P, j, {}, avec_t4=False)
        if 'P-T04' in a:
            ok += 1; print('tester artefact : compagnon absent |', [x for x in lg if x.startswith('P-T04')][0][:90])
        else:
            manque.append('tester compagnon absent')
    if depot:
        try:
            r = t4(depot, os.path.join(depot, 'prereg/T0.4-validation-modele-reel-v3.md'))
            print('T4 sain (préenregistrement scellé du dépôt) :', 'OK' if r is None else 'ÉCHEC ' + r)
            if r is not None:
                manque.append('T4 sain')
            with tempfile.TemporaryDirectory() as t:
                g = os.path.join(t, 'faux-v1.md'); open(g, 'w', encoding='utf-8').write('pas un préenregistrement\n')
                r2 = t4(depot, g)
                if r2:
                    ok += 1; print('T4 artefact refusé |', r2[:80])
                else:
                    manque.append('T4 artefact'); print('T4 artefact NON refusé')
            a, lg = tester(P, depot, {'P-7': 'prereg/T0.4-validation-modele-reel-v3.md'})
            if 'P-7' in a:
                manque.append('tester sain avec T4'); print('tester avec T4 : sain NON reconnu', [x for x in lg if x.startswith('P-7')])
            else:
                print('tester avec T4 sain : P-7 présent (préenregistrement scellé du dépôt nommé)')
            with tempfile.TemporaryDirectory() as t:
                os.symlink(os.path.join(depot, 'src'), os.path.join(t, 'src')); os.makedirs(os.path.join(t, 'prereg'))
                f7 = os.path.join(t, 'prereg/T0.7-faux-v1.md'); open(f7, 'w', encoding='utf-8').write('pas un préenregistrement\n')
                open(f7 + '.sha256', 'w', encoding='utf-8').write('%s  %s\n' % (sha(f7), os.path.basename(f7)))
                a, lg = tester(P, t, {})
                if 'P-7' in a:
                    ok += 1; print('tester avec T4 artefact : P-7 absent |', [x for x in lg if x.startswith('P-7')][0][:100])
                else:
                    manque.append('tester T4 artefact'); print('tester avec T4 artefact NON détecté')
        except Echec as e:
            manque.append('T4 import'); print('T4 impossible :', e)
    print('bilan des essais : %d gardes exercées avec succès, %d manquantes %s' % (ok, len(manque), manque))
    if manque:
        raise Echec('essais : %d garde(s) manquante(s)' % len(manque))


def feuille_ok(D, V1, DEC, s):
    """Comme `feuille`, mais sans impression, pour les essais."""
    import io, contextlib
    with contextlib.redirect_stdout(io.StringIO()):
        feuille(D, V1, DEC, s)


# ---------------------------------------------------------------- principal
def main(a):
    exige(a, __doc__)
    m = a[0]
    if m in ('verifier', 'artefact', 'feuille', 'tester', 'constat', 'calculer', 'essais'):
        exige(len(a) >= 4, 'arguments : D V1 DEC ...')
        D, V1, DEC = a[1:4]
    if m == 'verifier':
        W, P, o = verifier_texte(lire(D), lire(V1), charger_dec(DEC))
        print('OK', len(o), 'lignes dérivées vérifiées une à une,', len(W), 'lignes de travaux contrôlées,', len(P), 'produits')
    elif m == 'artefact':
        base = lire(D); W, P = charge(base)
        w = next(x for x in W if x['cl'] == 'K')
        bad = base.replace('| %s |' % w['prod'], '| — |', 1)
        exige(bad != base, 'artefact : altération sans effet')
        try:
            verifier_texte(bad, lire(V1), charger_dec(DEC))
        except Echec as e:
            print('artefact détecté (%s)' % str(e)[:70])
        else:
            raise Echec('artefact NON détecté')
    elif m == 'feuille':
        exige(len(a) == 5, 'feuille D V1 DEC "spec"'); feuille(D, V1, DEC, a[4])
    elif m == 'tester':
        exige(len(a) in (5, 6), 'tester D V1 DEC DEPOT [P-X=chemin,...]')
        W, P, o = verifier_texte(lire(D), lire(V1), charger_dec(DEC))
        nom = dict(x.split('=', 1) for x in a[5].split(',')) if len(a) == 6 else {}
        for p in nom:
            exige(p in P, ('produit inexistant', p))
        ab, lg = tester(P, a[4], nom)
        print('\n'.join(lg)); print('abs=' + ','.join(ab))
        print('À copier à la main (le script ne lit pas le contenu) : T3 (valeur copiée) et T5 (classe lue) -> val=')
    elif m == 'constat':
        exige(len(a) == 6, 'constat D V1 DEC FICHIER "A=2,3"')
        verifier_texte(lire(D), lire(V1), charger_dec(DEC))
        pres = constat(ensemble(lire_spec(a[5]).get('A', ''), 'A'), a[4])
        print('pres=' + ','.join(map(str, sorted(pres))))
    elif m == 'calculer':
        W, P = charge(lire(D))
        for k, v in calc(W, P, lire(V1), charger_dec(DEC)).items():
            print(k + '\t' + ' | '.join(v))
    elif m == 'essais':
        essais(D, V1, DEC, a[4] if len(a) > 4 else None)
    elif m == 'aveugle':
        aveugle(charge(lire(a[1]))[0])
    elif m == 'concordance':
        concordance(charge(lire(a[1]))[0], a[2])
    else:
        raise Echec('mode inconnu : ' + m)


if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except Echec as e:
        sys.stderr.write('ERREUR : %s\n' % e)
        sys.exit(2)
