import re,sys
cells=lambda l:[c.strip() for c in l.strip().strip('|').split('|')]
ks=lambda t:set(map(int,re.findall(r'\d',t)))
fmt=lambda s:', '.join(sorted(s)) or 'aucune'
pr=lambda w:[] if w['prod']=='—' else [x.strip().rstrip('†') for x in w['prod'].split(',')]
def tab(p,pre,n):
    r=[cells(l) for l in open(p,encoding='utf-8') if l.startswith(pre)]
    assert r and all(len(c)==n for c in r),pre
    return r
def charge(D):
    W=[dict(zip(('ref','trav','prod','sert','cl','src'),c)) for c in tab(D,'| W',6)]
    return W,{c[0]:dict(k=int(c[1]) if c[1].isdigit() else 0,pro=c[2]) for c in tab(D,'| P-',4)}
def classe(w):
    if re.search(r'\bd1\b|\bd2\b|préalable',w['src']):return 'F'
    if '[H]' in w['src']:return 'H'
    if w['prod']!='—':return 'K'
    return 'R' if '[REJEU]' in w['src'] else 'I'
def verifier(W,P):
    assert len({w['ref'] for w in W})==len(W),'refs en double'
    assert sorted(p['k'] for p in P.values() if p['k'])==list(range(1,9)),'un produit par critère'
    for w in W:
        assert all(x in P for x in pr(w)),(w['ref'],'produit inconnu')
        assert classe(w)==w['cl'],(w['ref'],'classe recalculée sans date')
        assert w['cl'] not in 'FH' or w['sert']=='—',(w['ref'],'F ou H avec sert')
        assert w['cl']!='R' or w['sert']!='—',(w['ref'],'R sans sert')
        assert all(P[x]['pro']!=w['ref'] for x in pr(w)),(w['ref'],'cite son propre produit')
    assert all(p['pro'] in {w['ref'] for w in W}|{'—'} for p in P.values()),'producteur inconnu'
    g={w['ref']:{P[x]['pro'] for x in pr(w)}-{'—'} for w in W}
    def vis(r,pile):
        assert r not in pile,('cycle',pile,r)
        for s in g[r]:vis(s,pile+[r])
    for r in g:vis(r,[])
def sc(s):
    d=dict(x.split('=') for x in s.split(';'));n=lambda t:{int(x) for x in t.split(',') if x}
    return {x for x in d['abs'].split(',') if x},n(d['G']),n(d['A'])
def ferm(W,ab,G,A):
    f={w['ref'] for w in W if w['cl'] in 'KI' and (ks(w['sert'])&G or (w['cl']=='K' and set(pr(w))&ab))}
    return f,{w['ref'] for w in W if w['cl']=='R' and ks(w['sert'])&A and not ks(w['sert'])&G}
SC=['abs=P-V6,P-L7;G=;A=2,3','abs=P-7,P-8;G=;A=2','abs=P-PIL;G=3;A=6','abs=P-L7,P-B4;G=2;A=3,4']
ANC={'W1':'W01','W2':'W04 W05 W06 W07','W3':'W02','W4':'W03','W5':'W36','W6':'W08 W09','W7':'W10','W8':'W11','W9':'W13 W14 W41','W10':'W15 W16 W17 W40','W11':'W17','W12':'W18 W19','W13':'W32 W33','W14':'W20 W21','W15':'W22','W16':'W34','W17':'W25','W18':'W26','W19':'W28','W20':'W29','W21':'W35','W22':'W30','W23':'W30','W24':'W27','W25':'W31'}
def audit(W,P,V1,DEC):
    by={w['ref']:w for w in W};dates={}
    for l in open(DEC,encoding='utf-8'):
        m=re.match(r'\| (R-\d+) \| (\S+) \|',l)
        if m:dates[m.group(1)]=m.group(2)
    v1=[dict(ref=c[0],dep=c[2],sert=c[3],cl=c[4]) for c in tab(V1,'| W',5) if c[0] in ANC]
    used=set();rs=ra=bo=sr=sa=0
    for x in v1:
        D=[by[r] for r in ANC[x['ref']].split()];used|={d['ref'] for d in D}
        s1=set() if x['sert'].startswith('—') else ks(x['sert']);s3=set().union(*[ks(d['sert']) for d in D]);sr+=len(s1-s3);sa+=len(s3-s1)
        cond=x['cl'].startswith('cond');d1=ks(x['dep']) if cond else set();d3={P[p]['k'] for d in D for p in pr(d)}-{0}
        t=bool(s1-s3 or d3-d1) or (x['cl'].startswith('cont') and any(d['cl'] in 'KRF' for d in D)) or (cond and any(d['cl']=='F' for d in D))
        l=bool(s3-s1 or (d1-d3 and any(d['cl']!='F' for d in D))) or ('ferm' in x['cl'] and any(d['cl']!='F' for d in D))
        rs+=t;ra+=l;bo+=t and l
    neuves=[w for w in W if w['ref'] not in used]
    def du29(w):
        ids=re.findall(r'R-\d+',w['src']);ks_=re.findall(r'\b(?:DP|PG|PC|MO|TC|DV|P40|MSG216)\b',w['src'])
        return bool(ids or ks_) and all(dates.get(i)=='2026-10-29' for i in ids) and not re.search(r'(?<![A-Za-z])[BGE] l\.|T7|N-\d|CLAUDE',w['src'])
    L=[w['ref'] for w in W if du29(w)];keep=[w for w in W if w['ref'] not in L]
    drop={p for p,v in P.items() if v['pro'] in L}
    red=[dict(w,prod=', '.join(x for x in w['prod'].split(', ') if x.rstrip('†') not in drop) or '—') for w in keep]
    S=[({p},set(),set()) for p in P]+[(set(),{k},set()) for k in range(1,9)]+[(set(),set(),{k}) for k in range(1,9)]+[sc(s) for s in SC]
    nd=0;dl=set()
    for ab,G,A in S:
        a,b=ferm(keep,ab,G,A),ferm(red,ab,G,A)
        if a!=b:nd+=1;dl|=(a[0]^b[0])|(a[1]^b[1])
    v=lambda k,x:('aud:'+k,[str(x)])
    return dict([v('v1',len(v1)),v('resserrees',rs),v('assouplies',ra),v('deux',bo),v('neutres',len(v1)-rs-ra+bo),v('sert-retires',sr),
        v('sert-ajoutes',sa),v('deductions',sum(w['prod'].count('†') for w in W)),v('lignes-deduites',sum('†' in w['prod'] for w in W)),
        v('neuves',len(neuves)),v('neuves-sert',sum(w['sert']!='—' for w in neuves)),v('neuves-ouvertes',sum(w['cl'] in 'IR' for w in neuves)),v('L29',len(L)),v('retrait-sc',len(S)),v('retrait-diff',nd),v('retrait-lignes',len(dl))])
def calc(W,P,V1,DEC):
    o={p:[fmt({w['ref'] for w in W if w['cl']=='K' and p in pr(w)})] for p in P}
    for k in range(1,9):
        L=[w for w in W if w['cl'] in 'KIR' and k in ks(w['sert'])]
        o['k:%d'%k]=[fmt({w['ref'] for w in L}),fmt({w['ref'] for w in L if w['cl']=='R'}),fmt({w['ref'] for w in L if w['cl']!='R'})]
    for s in SC:o['sc:'+s]=[fmt(x) for x in ferm(W,*sc(s))]
    o.update(audit(W,P,V1,DEC));return o
def feuille(W,s):
    d=dict(x.split('=',1) for x in s.split(';'));n=lambda t:{int(x) for x in t.split(',') if x}
    S={k:n(d[k]) for k in 'AGVC'};ab={x for x in d['abs'].split(',') if x}
    for w in W:
        sert=ks(w['sert']);c=w['cl'];a=set(pr(w))&ab
        e,m={'F':('fermée','L1'),'H':('Lazar','L6')}.get(c,('ouverte','L3' if c=='K' else 'L4'))
        if c in 'KIR' and sert&S['G']:e,m='fermée','L2 gel %s'%sorted(sert&S['G'])
        elif c=='K' and a:e,m='fermée','L3 absent %s'%sorted(a)
        elif c=='R' and not sert&S['A']:e,m='fermée','L4 hors A'
        print(w['ref'],e,m,'devis' if e=='ouverte' and sert&S['A'] else '—')
if __name__=='__main__':
    mode,D,V1,DEC=sys.argv[1:5];W,P=charge(D)
    if mode=='verifier':
        verifier(W,P);o=calc(W,P,V1,DEC)
        dr={cells(l)[0]:cells(l) for l in open(D,encoding='utf-8') if re.match(r'\| (P-\S+|k:\d|sc:\S.*?|aud:\S+) \|',l)}
        for key,v in o.items():assert key in dr and dr[key][-len(v):]==v,(key,v,dr.get(key))
        print('OK',len(o),'lignes dérivées vérifiées une à une,',len(W),'lignes de travaux contrôlées')
    elif mode=='artefact':
        W2=[dict(w) for w in W];next(w for w in W2 if w['cl']=='K')['prod']='—'
        try:verifier(W2,P)
        except AssertionError:print('artefact détecté')
        else:sys.exit('artefact NON détecté')
    else:feuille(W,sys.argv[5])
