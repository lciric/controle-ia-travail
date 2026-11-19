# Contre-lecteur : empreintes des membres d'archives tar.gz, sans extraction ; noms interdits sautés (contenu non lu).
import tarfile, hashlib, sys
for a in sys.argv[1:]:
    with tarfile.open(a) as t:
        for m in t:
            if not m.isfile(): continue
            if 'consigne-privee' in m.name or 'conception-ii-b' in m.name: continue
            e = hashlib.sha256(t.extractfile(m).read()).hexdigest()
            print(e, a.split('/')[-1], m.name)
