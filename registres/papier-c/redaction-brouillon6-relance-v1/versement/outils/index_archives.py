import tarfile,hashlib,sys
# empreintes des membres des dossiers papier-C et voisins-C, sans extraction
for tag,path in (("A20",sys.argv[1]),("A21",sys.argv[2])):
    with tarfile.open(path,'r:gz') as t:
        for m in t:
            n=m.name
            if not m.isfile(): 
                if (n.startswith('./papier-C/') or n.startswith('./voisins-C/')) and not m.isdir(): print("NONFICHIER",tag,n,m.type,file=sys.stderr)
                continue
            if not (n.startswith('./papier-C/') or n.startswith('./voisins-C/')): continue
            if 'consigne-privee' in n or 'conception-ii-b' in n: print("EXCLU",tag,n,file=sys.stderr); continue
            h=hashlib.sha256(); f=t.extractfile(m)
            while True:
                b=f.read(1<<20)
                if not b: break
                h.update(b)
            print(f"{tag}\t{h.hexdigest()}\t{m.size}\t{n}")
