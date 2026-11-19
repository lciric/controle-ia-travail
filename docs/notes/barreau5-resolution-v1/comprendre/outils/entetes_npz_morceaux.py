"""En-têtes d'un .npz découpé en morceaux git, lus morceau par morceau sans rien écrire sur disque
ni garder plus d'un morceau en mémoire. Aucune valeur de tableau n'est lue."""
import sys, subprocess, struct, re, io
import numpy.lib.format as fmt

depot, *specs = sys.argv[1:]
def blob(spec):
    return subprocess.run(['git', '-C', depot, 'cat-file', 'blob', spec], check=True, capture_output=True).stdout
tailles = [int(subprocess.run(['git', '-C', depot, 'cat-file', '-s', s], check=True, capture_output=True).stdout) for s in specs]
debuts = [sum(tailles[:i]) for i in range(len(tailles))]
total = sum(tailles)
fin = blob(specs[-1])
# fin du répertoire central (éventuellement zip64)
i = fin.rfind(b'PK\x05\x06')
n_ent, taille_cd, off_cd = struct.unpack('<HIi', fin[i+10:i+20])[0], *struct.unpack('<II', fin[i+12:i+20])
j = fin.rfind(b'PK\x06\x06')
if j >= 0:
    n_ent, taille_cd, off_cd = struct.unpack('<QQQ', fin[j+32:j+56])
assert off_cd >= debuts[-1], 'répertoire central hors du dernier morceau'
cd = fin[off_cd - debuts[-1]: off_cd - debuts[-1] + taille_cd]
ents = []; p = 0
while p < len(cd) and cd[p:p+4] == b'PK\x01\x02':
    comp, = struct.unpack('<H', cd[p+10:p+12])
    csize, usize, nlen, elen, clen = struct.unpack('<IIHHH', cd[p+20:p+34])
    off, = struct.unpack('<I', cd[p+42:p+46])
    nom = cd[p+46:p+46+nlen].decode()
    extra = cd[p+46+nlen:p+46+nlen+elen]
    q = 0
    while q + 4 <= len(extra):
        tag, sz = struct.unpack('<HH', extra[q:q+4])
        if tag == 1:
            champs = extra[q+4:q+4+sz]; r = 0
            if usize == 0xFFFFFFFF: usize, = struct.unpack('<Q', champs[r:r+8]); r += 8
            if csize == 0xFFFFFFFF: csize, = struct.unpack('<Q', champs[r:r+8]); r += 8
            if off == 0xFFFFFFFF: off, = struct.unpack('<Q', champs[r:r+8]); r += 8
        q += 4 + sz
    ents.append((nom, off, usize, comp))
    p += 46 + nlen + elen + clen
del fin
print(f"# {len(ents)} tableaux, {total} octets, compression {sorted({c for *_, c in ents})}")
res = {}
reste = sorted(ents, key=lambda e: e[1])
BESOIN = 1200
for k, spec in enumerate(specs):
    ici = [e for e in reste if debuts[k] <= e[1] < debuts[k] + tailles[k]]
    if not ici: continue
    b = blob(spec)
    suiv = None
    for nom, off, usize, comp in ici:
        loc = off - debuts[k]
        morceau = b[loc:loc + BESOIN]
        if len(morceau) < BESOIN and k + 1 < len(specs):
            if suiv is None: suiv = blob(specs[k+1])[:BESOIN]
            morceau += suiv[:BESOIN - len(morceau)]
        nlen, elen = struct.unpack('<HH', morceau[26:30])
        if comp != 0:
            res[nom] = ('compressé', '?', usize); continue
        f = io.BytesIO(morceau[30 + nlen + elen:])
        v = fmt.read_magic(f)
        shape, _, dt = (fmt.read_array_header_1_0 if v == (1, 0) else fmt.read_array_header_2_0)(f)
        res[nom] = (shape, str(dt), usize)
    del b
motifs = {}
for nom, (shape, dt, usize) in res.items():
    nom = nom[:-4] if nom.endswith('.npy') else nom
    motifs.setdefault(re.sub(r'\d+', '<n>', nom), []).append((nom, shape, dt, usize))
for m, l in motifs.items():
    formes = sorted({(s, d) for _, s, d, _ in l}, key=str)
    print(f"{m}\t n={len(l)}\t ex={l[0][0]}\t formes={formes[:5]}{' …' if len(formes) > 5 else ''}\t octets={sum(x[3] for x in l)}")
