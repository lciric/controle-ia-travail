import sys,os,re,glob,collections
W,depot=sys.argv[1],sys.argv[2]
dep={};depn=collections.defaultdict(list)
for l in open(W+'/outils/index-depot.txt',encoding='utf-8'):
    h,p=l.rstrip('\n').split('  ',1); dep.setdefault(h,p); depn[os.path.basename(p)].append((h,p))
# compagnons de PDF des archives
comp={}
for c in glob.glob(W+'/extraction/**/*.pdf.sha256',recursive=True):
    h,n=open(c,encoding='utf-8').read().split()[:2]; comp[os.path.basename(n)]=(h,c.split('/extraction/')[1])
notes=sorted(glob.glob(W+'/arbre/docs/notes/lecture-voi*.md')+glob.glob(W+'/arbre/docs/notes/papier-C-session16-archive-v1/notes-voisins-posterieures-au-brouillon5/*/lecture-*.md'))
rows={}
for n in notes:
    t=open(n,encoding='utf-8').read()
    for m in re.finditer(r'[A-Za-z0-9][A-Za-z0-9._\-]*\.pdf',t):
        pdf=m.group(0)
        # empreinte complète la plus proche après le nom (400 signes)
        hh=re.search(r'[0-9a-f]{64}',t[m.end():m.end()+400])
        rows.setdefault(pdf,{'notes':set(),'h':set()})
        rows[pdf]['notes'].add(os.path.basename(n))
        if hh: rows[pdf]['h'].add(hh.group(0))
out=[]
for pdf in sorted(set(rows)|set(comp)):
    r=rows.get(pdf,{'notes':set(),'h':set()})
    hc=comp.get(pdf,(None,None))
    au_nom=os.path.exists(depot+'/docs/sources/pdf/'+pdf)
    ailleurs=[p for h,p in depn.get(pdf,[])]
    par_h=dep.get(hc[0]) if hc[0] else None
    etat='PRESENT' if au_nom else ('PRESENT AILLEURS: '+ailleurs[0] if ailleurs else ('PRESENT SOUS AUTRE NOM: '+par_h if par_h else 'ABSENT'))
    out.append((etat,pdf,hc[0] or '-',hc[1] or '-',';'.join(sorted(r['notes'])) or '(compagnon seul)', 'empreinte du compagnon citée dans la note' if hc[0] in r['h'] else ('empreintes voisines dans la note: '+','.join(x[:12] for x in sorted(r['h'])) if r['h'] else '-')))
for o in out: print('\t'.join(o))
