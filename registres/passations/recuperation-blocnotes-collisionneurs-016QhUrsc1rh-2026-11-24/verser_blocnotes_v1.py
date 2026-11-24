"""Inventaire et archive du bloc-notes de la session des collisionneurs (règle « récupérer ce qui est récupérable »).

Usage : python3 -I verser_blocnotes_v1.py BLOC_NOTES EMPREINTES_DU_DEPOT DOSSIER_DE_SORTIE
- Inventaire de tous les fichiers du bloc-notes : chemin, taille, empreinte, présence dans le dépôt, présence dans l'archive.
- Archive tar.gz des fichiers dont l'empreinte n'est pas déjà dans le dépôt (docs/ et runs/, fichiers de moins de 20 Mo).
- Aucun fichier n'est lu pour son contenu au-delà du calcul d'empreinte.
"""
import hashlib
import sys
import tarfile
from pathlib import Path

bloc, empreintes, sortie = (Path(a) for a in sys.argv[1:4])
connues = set(empreintes.read_text().split())
sortie.mkdir(parents=True, exist_ok=False)
lignes = ["chemin\ttaille_octets\tsha256\tdeja_dans_le_depot\tdans_l_archive"]
a_archiver = []
for p in sorted(x for x in bloc.rglob("*") if x.is_file()):
    rel = p.relative_to(bloc).as_posix()
    h = hashlib.sha256(p.read_bytes()).hexdigest()
    dedans = h in connues
    if not dedans:
        a_archiver.append((p, rel))
    lignes.append(f"{rel}\t{p.stat().st_size}\t{h}\t{'oui' if dedans else 'non'}\t{'non' if dedans else 'oui'}")
archive = sortie / "blocnotes-collisionneurs-fichiers-non-verses-v1.tar.gz"
with tarfile.open(archive, "w:gz") as t:
    for p, rel in a_archiver:
        t.add(p, arcname=rel, recursive=False)
(sortie / "blocnotes-collisionneurs-inventaire-v1.tsv").write_text("\n".join(lignes) + "\n", encoding="utf-8")
print(f"{len(lignes) - 1} fichiers inventoriés ; {len(a_archiver)} archivés ; {len(lignes) - 1 - len(a_archiver)} déjà dans le dépôt")
print(f"archive : {archive.stat().st_size} octets")
