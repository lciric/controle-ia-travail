#!/usr/bin/env python3
"""Trace des écritures d'un script Python (crochets d'audit, PEP 578) — relecture du script de lecture du pilote 4, v1.

Usage : PYTHON -I -B trace_ecritures_v1.py JOURNAL DOSSIER_PERMIS SCRIPT [ARGUMENTS…]

Installe un crochet d'audit, puis exécute SCRIPT comme programme principal (`runpy.run_path`, nom `__main__`). Toute
ouverture en écriture (mode « w », « a », « x », « + », ou drapeaux d'écriture et de création), création de dossier,
renommage, suppression, lien, changement de droits ou de dates, fichier ou dossier temporaire, copie ou déplacement par
`shutil` est consignée dans JOURNAL, une ligne par chemin : « permis » s'il est dans DOSSIER_PERMIS, sinon « HORS ».
Un événement HORS est aussi bloqué (PermissionError), pour que l'essai ne puisse rien écrire ailleurs. Le journal est
ouvert avant l'installation du crochet ; aucune autre écriture n'est faite par cette trace.
"""
import os
import sys

journal, permis, script = sys.argv[1], os.path.realpath(sys.argv[2]), sys.argv[3]
FD = os.open(journal, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
ECRITURE = os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND
EVENEMENTS = {"os.mkdir", "os.rename", "os.remove", "os.rmdir", "os.symlink", "os.link", "os.chmod", "os.chown",
              "os.truncate", "os.utime", "os.mkfifo", "os.mknod", "os.setxattr", "os.removexattr", "os.chflags",
              "shutil.copyfile", "shutil.copymode", "shutil.copystat", "shutil.copytree", "shutil.move",
              "shutil.rmtree", "shutil.make_archive", "shutil.unpack_archive", "tempfile.mkstemp", "tempfile.mkdtemp"}


def _chemin(x):
    if isinstance(x, int):
        return None
    try:
        return os.path.realpath(os.fsdecode(x))
    except Exception:  # noqa
        return None


def crochet(evenement, args):
    if evenement == "open":
        chemin, mode, drapeaux = (list(args) + [None, None, None])[:3]
        ecrit = (isinstance(mode, str) and any(c in mode for c in "wax+")) or \
                (isinstance(drapeaux, int) and bool(drapeaux & ECRITURE))
        if not ecrit or isinstance(chemin, int):
            return
        chemins = [chemin]
    elif evenement in EVENEMENTS:
        chemins = [a for a in args if isinstance(a, (str, bytes, os.PathLike))][:2]
    else:
        return
    for c in chemins:
        r = _chemin(c)
        dedans = r is not None and (r == permis or r.startswith(permis + os.sep))
        ligne = f"{'permis' if dedans else 'HORS'}\t{evenement}\t{r if r is not None else repr(c)}\n"
        os.write(FD, ligne.encode("utf-8", "backslashreplace"))
        if not dedans:
            raise PermissionError(f"trace : écriture hors du dossier permis bloquée ({evenement})")


sys.addaudithook(crochet)
sys.argv = [script] + sys.argv[4:]
import runpy  # noqa: E402

runpy.run_path(script, run_name="__main__")
