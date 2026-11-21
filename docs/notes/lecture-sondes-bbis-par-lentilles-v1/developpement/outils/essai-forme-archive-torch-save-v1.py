"""Essai opposable de la forme de l'archive écrite par `torch.save` (texte de lecture v2, « Entrées », point 3 ; « Code neuf »,
essais « archive ») : sur la version de torch installée, un dictionnaire jouet de la forme d'un fichier d'ajustement
(`meta`, `state.n_docs`, `state.next_doc`, `state.sums[(cible, moitié)]`) est écrit par `torch.save`, puis l'archive est relue
octet par octet, sans `zipfile` pour l'ordre et les en-têtes. Constats imprimés : `data.pkl` est le premier enregistrement ;
aucun enregistrement n'est compressé ; où se lit la taille d'un enregistrement ; alignement des données ; classes que
`data.pkl` demande. Aucune donnée, aucun modèle, aucun réseau. Usage : python essai-forme-archive-torch-save-v1.py <dossier vide>."""
import io
import pickletools
import struct
import sys
import zipfile
import zlib
from pathlib import Path

import torch

dossier = Path(sys.argv[1])
dossier.mkdir(parents=True, exist_ok=True)
chemin = dossier / "ajustement-jouet.pt"
d = 8
objet = {"meta": {"lens": "R", "layers": 4, "targets": ["out", "mid"], "full_length": True, "basis": None, "rules": {"a": 1}},
         "state": {"n_docs": [3, 3], "next_doc": 6,
                   "sums": {("out", 0): torch.arange(3 * d * d, dtype=torch.float32).reshape(3, d, d), ("out", 1): torch.ones(3, d, d),
                            ("mid", 0): torch.zeros(4, d, d), ("mid", 1): torch.zeros(4, d, d)}}}
torch.save(objet, chemin)
b = chemin.read_bytes()
print(f"torch {torch.__version__} ; taille de l'archive : {len(b)} octets")
tailles = {i.filename: i.file_size for i in zipfile.ZipFile(chemin).infolist()}   # tailles du répertoire central, pour avancer
pos, noms, compresses, sans_taille, descripteurs = 0, [], 0, 0, 0
while b[pos:pos + 4] == b"PK\x03\x04":
    _, _, drapeaux, methode, _, _, _, comprime, taille, n_nom, n_extra = struct.unpack("<IHHHHHIIIHH", b[pos:pos + 30])
    nom = b[pos + 30:pos + 30 + n_nom].decode()
    donnees = pos + 30 + n_nom + n_extra
    fin = donnees + tailles[nom]
    noms.append(nom)
    compresses += int(methode != 0)
    sans_taille += int(taille == 0 and tailles[nom] != 0)
    ligne = (f"enregistrement {len(noms)} : {nom} ; méthode {methode} ; drapeaux {drapeaux:#06x} ; taille dans l'en-tête local "
             f"{taille} ; taille réelle {tailles[nom]} ; données à l'octet {donnees} (modulo 64 : {donnees % 64})")
    pos = fin
    if drapeaux & 8:
        assert b[fin:fin + 4] == b"PK\x07\x08"
        crc, c32, u32 = struct.unpack("<III", b[fin + 4:fin + 16])
        court = c32 == u32 == tailles[nom] and b[fin + 16:fin + 18] == b"PK"
        ligne += (f" ; descripteur de données de {16 if court else 24} octets, tailles égales à la taille réelle, somme de "
                  f"contrôle {'juste' if zlib.crc32(b[donnees:fin]) == crc else 'FAUSSE'}")
        descripteurs += 1
        pos = fin + (16 if court else 24)
    print(ligne)
print(f"suite : {b[pos:pos + 4]!r} (répertoire central)")
print(f"constat 1 — `data.pkl` est le premier enregistrement : {noms[0].endswith('data.pkl')}")
print(f"constat 2 — enregistrements compressés : {compresses} sur {len(noms)}")
print(f"constat 3 — enregistrements dont l'en-tête local ne porte pas la taille : {sans_taille} sur {len(noms)} ; avec "
      f"descripteur de données : {descripteurs}")
sortie = io.StringIO()
pickletools.dis(zipfile.ZipFile(chemin).read(noms[0]), out=sortie)
classes = sorted({l.split("GLOBAL", 1)[1].strip() for l in sortie.getvalue().splitlines() if "GLOBAL" in l})
print(f"constat 4 — classes que `data.pkl` demande : {classes}")
stockages = [l.split("BINUNICODE", 1)[1].strip() for l in sortie.getvalue().splitlines() if "BINUNICODE" in l]
print(f"constat 5 — chaque tenseur de `sums` a son stockage (clés {sorted(n.rsplit('/', 1)[1] for n in noms if '/data/' in n)}), "
      f"de taille = éléments × 4 octets : {[tailles[n] for n in noms if '/data/' in n]}")
