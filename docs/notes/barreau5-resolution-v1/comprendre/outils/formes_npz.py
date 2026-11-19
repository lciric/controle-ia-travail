"""Noms et formes des tableaux d'un fichier .npz lu sur l'entrée standard, par les en-têtes seulement (aucune valeur lue).
Usage : git cat-file blob <objet> | python3 -I formes_npz.py"""
import io, sys, zipfile, struct, ast
donnees = sys.stdin.buffer.read()
z = zipfile.ZipFile(io.BytesIO(donnees))
for info in z.infolist():
    with z.open(info) as f:
        magie = f.read(6)
        if magie != b"\x93NUMPY":
            print(info.filename, "(pas un tableau numpy)", info.file_size)
            continue
        maj, mineur = f.read(2)
        if maj == 1:
            (n,) = struct.unpack("<H", f.read(2))
        else:
            (n,) = struct.unpack("<I", f.read(4))
        entete = ast.literal_eval(f.read(n).decode("latin1"))
    print(f"{info.filename}\t{entete['descr']}\t{entete['shape']}")
