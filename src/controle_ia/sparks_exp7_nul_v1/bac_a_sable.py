"""Bac à sable d'analyse des lecteurs (texte scellé, section « Lecteurs », isolement et limites).

Chaque exécution est un processus Python neuf, dans un espace de noms utilisateur, réseau et montage propre
(`unshare -rnm`), enfermé (`chroot`) dans une racine qui ne monte que : `/usr` (lecture seule, interpréteur et
bibliothèque standard), numpy seul sous `/opt/site` (lecture seule), `/case` (copies servies, lecture seule),
`/work` (lecture et écriture), `/tmp` (mémoire), `/run` (le code et le prélude, lecture seule) et trois fichiers de
`/dev`. Ni torch, ni transformers, ni réseau, ni coffre, ni dépôt, ni manifeste. Python lancé en `-I -S` (aucun
`site-packages`). Limites : 600 s, 12 Go d'espace d'adresses, sortie coupée à 15 000 caractères ; `/work` au plus
3 Go (vérifié après chaque exécution). Écarts au billet écrits d'avance : 12 Go au lieu de 48, 3 Go au lieu de 20.

Aucun repli : si l'isolement n'est pas disponible, `exiger_isolement()` lève (R5).
Prélude : celui des auteurs (`runs/attention_tool/sandbox/prelude.py`, MIT, sha256 aa0c84d3…), copié sans changement
dans `donnees_auteurs/prelude_auteurs.py.txt`.
"""
from __future__ import annotations

import os
import shlex
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

DUREE_S = 600
MEMOIRE_OCTETS = 12 * 1024 ** 3
SORTIE_MAX = 15_000
WORK_MAX_OCTETS = 3 * 1024 ** 3
PRELUDE = Path(__file__).resolve().parent / "donnees_auteurs" / "prelude_auteurs.py.txt"
SHA_PRELUDE = "aa0c84d341ab9b2582b29b85a38b7b663cabc3062d9cb8297aa6414e346f2826"

LANCEUR = """import sys
sys.path.insert(0, "/opt/site")
g = {"__name__": "__main__"}
exec(compile(open("/run/prelude.py").read(), "prelude.py", "exec"), g)
exec(compile(open("/run/code.py").read(), "code.py", "exec"), g)
"""


class GardeBac(RuntimeError):
    pass


def interpreteur() -> Path:
    p = Path(os.path.realpath(sys.executable))
    if not str(p).startswith("/usr/"):
        raise GardeBac(f"interpréteur {p} hors de /usr : la racine du bac ne le contiendrait pas")
    return p


def site_numpy() -> tuple[Path, Path | None]:
    import numpy

    d = Path(numpy.__file__).resolve().parent
    libs = d.parent / "numpy.libs"
    return d, (libs if libs.is_dir() else None)


def paquets_masques() -> list[str]:
    """Dossiers de paquets sous /usr (le bac voit /usr) : masqués, pour que numpy et la bibliothèque standard soient
    seuls importables, même si le code du lecteur ajoute un chemin à `sys.path`."""
    import glob

    return sorted(d for motif in ("/usr/lib/python3*/*-packages", "/usr/local/lib/python3*/*-packages",
                                  "/usr/lib/python3/dist-packages") for d in glob.glob(motif) if os.path.isdir(d))


def exiger_isolement() -> None:
    for outil in ("unshare", "chroot", "timeout", "prlimit"):
        if shutil.which(outil) is None:
            raise GardeBac(f"{outil} absent : isolement impossible, aucun lecteur ne doit tourner")
    r = subprocess.run(["unshare", "-rnm", "true"], capture_output=True)
    if r.returncode != 0:
        raise GardeBac("espaces de noms utilisateur indisponibles : isolement impossible")


def taille(d: Path) -> int:
    return sum(p.stat().st_size for p in d.rglob("*") if p.is_file() and not p.is_symlink())


def executer(code: str, dossier_cas: Path, dossier_work: Path, *, duree_s: int = DUREE_S,
             memoire: int = MEMOIRE_OCTETS) -> dict:
    """Exécute `code` (après le prélude) ; renvoie {"sortie", "code_retour", "coupee", "work_octets", "work_depasse"}."""
    exiger_isolement()
    from .harnais import sha256_texte   # import tardif : pas de cycle

    prelude = PRELUDE.read_text(encoding="utf-8")
    if sha256_texte(PRELUDE.read_bytes()) != SHA_PRELUDE:
        raise GardeBac("prélude altéré")
    py = interpreteur()
    np_dir, np_libs = site_numpy()
    dossier_cas, dossier_work = Path(dossier_cas).resolve(), Path(dossier_work).resolve()
    with tempfile.TemporaryDirectory(prefix="bac-") as tmp:
        tmp = Path(tmp)
        racine, run = tmp / "racine", tmp / "run"
        run.mkdir()
        (run / "prelude.py").write_text(prelude, encoding="utf-8")
        (run / "code.py").write_text(code, encoding="utf-8")
        (run / "lanceur.py").write_text(LANCEUR, encoding="utf-8")
        for d in ("usr", "case", "work", "tmp", "run", "dev", "opt/site/numpy", "opt/site/numpy.libs"):
            (racine / d).mkdir(parents=True)
        for f in ("null", "zero", "urandom"):
            (racine / "dev" / f).touch()
        for lien, cible in (("bin", "usr/bin"), ("lib", "usr/lib"), ("lib64", "usr/lib64")):
            (racine / lien).symlink_to(cible)
        R = shlex.quote(str(racine))
        m = [f"mount --bind /usr {R}/usr", f"mount -o remount,bind,ro {R}/usr",
             f"mount --bind {shlex.quote(str(np_dir))} {R}/opt/site/numpy",
             f"mount -o remount,bind,ro {R}/opt/site/numpy",
             f"mount --bind {shlex.quote(str(dossier_cas))} {R}/case", f"mount -o remount,bind,ro {R}/case",
             f"mount --bind {shlex.quote(str(dossier_work))} {R}/work",
             f"mount --bind {shlex.quote(str(run))} {R}/run", f"mount -o remount,bind,ro {R}/run",
             f"mount -t tmpfs -o size=1g none {R}/tmp"]
        for d in paquets_masques():   # site-packages et dist-packages de /usr masqués par un dossier vide
            m.append(f"mount -t tmpfs -o size=4k,ro none {R}{shlex.quote(d)}")
        if np_libs is not None:
            m += [f"mount --bind {shlex.quote(str(np_libs))} {R}/opt/site/numpy.libs"]
        for f in ("null", "zero", "urandom"):
            m.append(f"mount --bind /dev/{f} {R}/dev/{f}")
        chroot = shlex.quote(shutil.which("chroot"))
        script = " && ".join(m) + f" && cd {R} && exec {chroot} {R} {shlex.quote(str(py))} -I -S -B /run/lanceur.py"
        cmd = ["timeout", "--signal=KILL", str(duree_s), "prlimit", f"--as={memoire}", "unshare", "-rnm", "--fork",
               "sh", "-c", f"cd / && {script}"]
        env = {"PATH": "/usr/sbin:/usr/bin:/sbin:/bin", "LANG": "C.UTF-8", "HOME": "/work", "OMP_NUM_THREADS": "4"}
        r = subprocess.run(cmd, capture_output=True, env=env)
    sortie = (r.stdout + r.stderr).decode("utf-8", errors="replace")
    if r.returncode in (137, -9):          # timeout --signal=KILL frappe le groupe de processus
        sortie += f"\n[arrêt : plus de {duree_s} s]"
    coupee = len(sortie) > SORTIE_MAX
    w = taille(dossier_work)
    return {"sortie": sortie[:SORTIE_MAX], "code_retour": r.returncode, "coupee": coupee, "work_octets": w,
            "work_depasse": w > WORK_MAX_OCTETS}
