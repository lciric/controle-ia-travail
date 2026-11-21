"""Liste de référence refaite par une voie à moi : git ls-tree -r -z puis git cat-file --batch (lecture seule), sha256 en Python,
tri par octets des chemins « ./… » (équivalent de LC_ALL=C sort -z), sortie au format de sha256sum.
Usage : ma-reference.py DEPOT COMMIT SORTIE
Rend aussi : décompte des modes, entrées non régulières (liens, sous-modules), noms à caractères spéciaux, fichiers .gitattributes."""
import hashlib
import subprocess
import sys

depot, commit, sortie = sys.argv[1:4]
brut = subprocess.run(["git", "-C", depot, "ls-tree", "-r", "-z", "--full-tree", commit], check=True,
                      capture_output=True).stdout
entrees = []
for e in brut.split(b"\0"):
    if not e:
        continue
    meta, chemin = e.split(b"\t", 1)
    mode, typ, sha = meta.split(b" ")
    entrees.append((mode.decode(), typ.decode(), sha.decode(), chemin))
modes = {}
for m, t, s, c in entrees:
    modes[(m, t)] = modes.get((m, t), 0) + 1
print("modes (mode, type) : nombre :", modes)
reguliers = [(m, s, c) for m, t, s, c in entrees if t == "blob" and m in ("100644", "100755")]
speciaux = [(m, t, c) for m, t, s, c in entrees if not (t == "blob" and m in ("100644", "100755"))]
print("entrées non régulières :", len(speciaux), speciaux[:5])
print("fichiers réguliers :", len(reguliers))
rep = subprocess.Popen(["git", "-C", depot, "cat-file", "--batch"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
lignes = []
speciaux_noms = 0
attrs = []
for m, s, c in reguliers:
    rep.stdin.write(s.encode() + b"\n")
    rep.stdin.flush()
    entete = rep.stdout.readline().split()
    taille = int(entete[2])
    donnees = rep.stdout.read(taille)
    rep.stdout.read(1)
    h = hashlib.sha256(donnees).hexdigest()
    nom = b"./" + c
    if c.endswith(b".gitattributes") or c == b".gitattributes":
        attrs.append((c, donnees))
    if nom in (b"./COMMIT-DE-LA-COPIE.txt", b"./EMPREINTES-DE-LA-COPIE.txt"):
        print("ATTENTION : l'arbre contient un des deux fichiers exclus :", nom)
        continue
    echap = (b"\\" in nom) or (b"\n" in nom)
    if echap:
        speciaux_noms += 1
        nom_aff = nom.replace(b"\\", b"\\\\").replace(b"\n", b"\\n")
        ligne = b"\\" + h.encode() + b"  " + nom_aff + b"\n"
    else:
        ligne = h.encode() + b"  " + nom + b"\n"
    lignes.append((nom, ligne))
rep.stdin.close()
lignes.sort(key=lambda x: x[0])
with open(sortie, "wb") as fh:
    for _, l in lignes:
        fh.write(l)
print("lignes écrites :", len(lignes), "; noms avec barre oblique inverse ou saut de ligne :", speciaux_noms)
print("fichiers .gitattributes :", [(c.decode(errors="replace"), d.decode(errors="replace")[:200]) for c, d in attrs])
