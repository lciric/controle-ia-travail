"""Bac à sable des lecteurs pour l'addendum n° 1 : celui de la v1 (mêmes montages, mêmes limites, même isolement),
avec le prélude en paramètre (prélude des auteurs chez Gemma ; prélude porté au secours, couple 15). Les couches du
modèle de départ ne sont jamais montées : seuls `/usr`, numpy, `/case`, `/work`, `/run`, `/tmp` et trois fichiers de
`/dev` le sont (essai d'isolement : un lecteur d'essai chargé de les lire échoue).
"""
from __future__ import annotations

import hashlib
import shlex
import shutil
import subprocess
import tempfile
from pathlib import Path

from ..sparks_exp7_nul_v1.bac_a_sable import (DUREE_S, LANCEUR, MEMOIRE_OCTETS, PRELUDE, SHA_PRELUDE,  # noqa: F401
                                              SORTIE_MAX, WORK_MAX_OCTETS, GardeBac, exiger_isolement, interpreteur,
                                              paquets_masques, site_numpy, taille)


def executer(code: str, dossier_cas: Path, dossier_work: Path, *, duree_s: int = DUREE_S,
             memoire: int = MEMOIRE_OCTETS, prelude_chemin: Path = PRELUDE, sha_prelude: str = SHA_PRELUDE) -> dict:
    """Comme la v1 ; le prélude est celui des auteurs (Gemma) ou, au secours, le prélude porté et éprouvé, dont
    l'empreinte est consignée au manifeste (`sha_prelude`)."""
    exiger_isolement()
    p = Path(prelude_chemin)
    if hashlib.sha256(p.read_bytes()).hexdigest() != sha_prelude:
        raise GardeBac("prélude altéré")
    prelude = p.read_text(encoding="utf-8")
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
