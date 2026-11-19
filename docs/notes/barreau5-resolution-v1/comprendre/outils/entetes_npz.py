"""Lit les noms, formes et types des tableaux d'un .npz sans lire aucune valeur."""
import sys, zipfile
import numpy.lib.format as fmt

def entetes(chemin, max_lignes=400):
    with zipfile.ZipFile(chemin) as z:
        infos = z.infolist()
        print(f"# {chemin.split('/')[-1]} : {len(infos)} tableaux")
        groupes = {}
        for i in infos:
            with z.open(i) as f:
                v = fmt.read_magic(f)
                if v == (1, 0):
                    shape, fortran, dtype = fmt.read_array_header_1_0(f)
                else:
                    shape, fortran, dtype = fmt.read_array_header_2_0(f)
            nom = i.filename[:-4] if i.filename.endswith('.npy') else i.filename
            groupes[nom] = (shape, str(dtype), i.file_size, i.compress_type)
        return groupes

if __name__ == '__main__':
    import re
    g = entetes(sys.argv[1])
    limite = int(sys.argv[2]) if len(sys.argv) > 2 else 60
    # regrouper les noms qui ne diffèrent que par des chiffres
    motifs = {}
    for nom, (shape, dt, taille, comp) in g.items():
        m = re.sub(r'\d+', '<n>', nom)
        motifs.setdefault(m, []).append((nom, shape, dt, taille))
    for m, l in motifs.items():
        formes = sorted({(s, d) for _, s, d, _ in l}, key=str)
        tot = sum(t for *_, t in l)
        ex = l[0][0]
        print(f"{m}\t n={len(l)}\t ex={ex}\t formes={formes[:6]}{' …' if len(formes)>6 else ''}\t octets={tot}")
