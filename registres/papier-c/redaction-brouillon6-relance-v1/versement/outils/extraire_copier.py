import sys,os,tarfile,hashlib,shutil
W,depot=sys.argv[1],sys.argv[2]
ARCH={'A20':depot+'/registres/passations/bloc-notes-session16-2026-10-20.tar.gz','A21':depot+'/registres/passations/bloc-notes-session16-complement-2026-10-21.tar.gz'}
plan=[l.rstrip('\n').split('\t') for l in open(W+'/outils/plan.tsv',encoding='utf-8')]
idx={(l.split('\t')[0],l.rstrip('\n').split('\t')[3]) for l in open(W+'/outils/index-archives.tsv',encoding='utf-8')}
def sha(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for b in iter(lambda:f.read(1<<20),b''): h.update(b)
    return h.hexdigest()
want={'A20':set(),'A21':set()}
for lot,d,tag,n,h,s,tags in plan:
    want[tag].add(n)
    if (tag,n+'.sha256') in idx: want[tag].add(n+'.sha256')
# compagnons des PDF (noms et empreintes seulement)
for tag,n in idx:
    if n.endswith('.pdf.sha256'): want[tag].add(n)
for tag in want:
    out=W+'/extraction/'+tag; os.makedirs(out,exist_ok=True)
    with tarfile.open(ARCH[tag],'r:gz') as t:
        for m in t:
            if m.name in want[tag]:
                assert m.isfile() and '..' not in m.name and m.name.startswith('./papier-C/')
                p=os.path.join(out,m.name[2:]); os.makedirs(os.path.dirname(p),exist_ok=True)
                with t.extractfile(m) as src, open(p,'wb') as dst: shutil.copyfileobj(src,dst)
                want[tag].discard(m.name)
    if want[tag]: print('NON EXTRAITS',tag,want[tag])
ok=0
for lot,d,tag,n,h,s,tags in plan:
    src=W+'/extraction/'+tag+'/'+n[2:]; dst=W+'/arbre/'+d
    assert not os.path.exists(depot+'/'+d), 'EXISTE AU DEPOT '+d
    assert not os.path.exists(depot+'/'+d+'.sha256'), 'COMPAGNON EXISTE AU DEPOT '+d
    assert not os.path.exists(dst), 'DOUBLON '+d
    os.makedirs(os.path.dirname(dst),exist_ok=True); shutil.copyfile(src,dst)
    h2=sha(dst); assert h2==h and os.path.getsize(dst)==int(s),('EMPREINTE',d)
    with open(dst+'.sha256','w',encoding='utf-8',newline='\n') as f: f.write(h2+'  '+os.path.basename(dst)+'\n')
    # compagnon de l'archive : même empreinte déclarée ?
    c=src+'.sha256'
    if os.path.exists(c):
        dec=open(c,encoding='utf-8').read().split()[0]
        if dec!=h2: print('COMPAGNON ARCHIVE DIVERGENT',n,dec)
    else: print('sans compagnon dans l\'archive:',n)
    ok+=1
print('copiees',ok)
