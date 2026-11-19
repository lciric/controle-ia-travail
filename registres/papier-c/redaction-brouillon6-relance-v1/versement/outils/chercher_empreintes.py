import tarfile,hashlib,sys
cibles={l.split('\t')[2] for l in open(sys.argv[1]) if l.startswith('H')}
for tag,path in (("A20",sys.argv[2]),("A21",sys.argv[3])):
    with tarfile.open(path,'r:gz') as t:
        for m in t:
            if not m.isfile(): continue
            n=m.name
            if 'consigne-privee' in n or 'conception-ii-b' in n: continue
            if n.startswith('./papier-C/') or n.startswith('./voisins-C/'): continue
            h=hashlib.sha256(); f=t.extractfile(m)
            while True:
                b=f.read(1<<20)
                if not b: break
                h.update(b)
            if h.hexdigest() in cibles: print(tag,h.hexdigest(),m.size,n,sep='\t')
