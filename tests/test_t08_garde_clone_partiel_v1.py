"""Reproduction sur processeur de l'arrêt de la course de T0.8 (tentative 1, instance 62094761, 23 novembre) pendant les
gardes de l'instance, et essai du correctif proposé (note `docs/notes/t08-chaine-de-lancement-v1/diag-gardes-tentative-1-v1.md`).

Sur l'instance, le code est cloné en clone partiel (`--filter=blob:none`) : les blobs de l'histoire ne sont pas
téléchargés. La garde `entrees_v1.exiger_instance_sans_interdits` lance `git rev-list --all --objects` ; dans un clone
partiel, git va alors chercher chaque blob manquant, un par un, chez le dépôt distant (« lazy fetch »). Sur GitHub, avec
45 444 fichiers dans l'arbre du seul commit C et toute l'histoire de la branche, le délai de 900 s de l'amorce est dépassé.
L'essai de bout en bout ne le voyait pas : son clone était bien partiel, mais l'arbre de son code ne portait que
≈ 1 800 objets, servis en local (`file://`) ; la garde y a pris 2 s. Ici, le même mécanisme est rendu mesurable : on
compte les objets que la garde télécharge.
"""
from __future__ import annotations

import subprocess
from pathlib import Path

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.t08 import entrees_v1 as en

RUN = "20261111-151701-t06-reel"
N_BLOBS = 300


def _git(*a, cwd=None):
    return subprocess.run(["git", *a], cwd=cwd, check=True, capture_output=True, text=True).stdout


def _objets(depot: Path) -> int:
    v = dict(l.split(": ") for l in _git("count-objects", "-v", cwd=depot).splitlines())
    return int(v["count"]) + int(v["in-pack"])


def _clone_partiel(tmp: Path, avec_resume_7b: bool) -> Path:
    src = tmp / "src"
    src.mkdir()
    _git("init", "-q", cwd=src)
    for d in range(10):
        (src / f"d{d}").mkdir()
        for f in range(N_BLOBS // 10):
            (src / f"d{d}" / f"f{f}.txt").write_text(f"{d}-{f}\n")
    if avec_resume_7b:                                    # présent dans un commit ancien, retiré ensuite
        (src / "diag" / RUN).mkdir(parents=True)
        (src / "diag" / RUN / "resume.json").write_text("{}\n")
    _git("add", ".", cwd=src)
    _git("-c", "user.email=e@x", "-c", "user.name=e", "commit", "-qm", "a", cwd=src)
    if avec_resume_7b:
        _git("rm", "-q", "-r", "diag", cwd=src)
        _git("-c", "user.email=e@x", "-c", "user.name=e", "commit", "-qm", "b", cwd=src)
    _git("clone", "-q", "--bare", str(src), str(tmp / "serveur.git"))
    _git("config", "uploadpack.allowFilter", "true", cwd=tmp / "serveur.git")
    _git("config", "uploadpack.allowAnySHA1InWant", "true", cwd=tmp / "serveur.git")
    client = tmp / "client"
    _git("-c", "gc.auto=0", "clone", "-q", "--filter=blob:none", "--no-checkout", "--single-branch",
         f"file://{tmp / 'serveur.git'}", str(client))
    _git("config", "gc.auto", "0", cwd=client)
    assert _git("config", "remote.origin.promisor", cwd=client).strip() == "true"
    return client


def test_garde_ne_telecharge_aucun_blob_d_un_clone_partiel(tmp_path):
    """Cas sain : la garde passe sans aller chercher un seul blob manquant (avant le correctif : 300 téléchargés un par
    un, ce qui, à l'échelle de l'instance, dépasse le délai de 900 s)."""
    c = _clone_partiel(tmp_path, avec_resume_7b=False)
    avant = _objets(c)
    r = en.exiger_instance_sans_interdits(c, RUN)
    assert r["interdits"] == 0
    assert _objets(c) == avant, f"{_objets(c) - avant} objets téléchargés par la garde (clone partiel)"


def test_garde_voit_un_resume_de_7b_dont_le_blob_manque(tmp_path):
    """Artefact : un `resume.json` de 7b dans l'histoire, blob absent du clone partiel ; la garde l'arrête (passe des
    chemins des commits, qui ne lit que les arbres), toujours sans rien télécharger."""
    c = _clone_partiel(tmp_path, avec_resume_7b=True)
    avant = _objets(c)
    with pytest.raises(GardeArret, match="resume.json"):
        en.exiger_instance_sans_interdits(c, RUN)
    assert _objets(c) == avant


def test_rev_list_par_defaut_telecharge_les_blobs_un_par_un(tmp_path):
    """Constat de la cause (indépendant du correctif) : `rev-list --all --objects` sans `--missing` va chercher chaque
    blob manquant ; avec `--missing=allow-promisor`, aucun."""
    c = _clone_partiel(tmp_path, avec_resume_7b=False)
    avant = _objets(c)
    _git("rev-list", "--all", "--objects", "--missing=allow-promisor", cwd=c)
    assert _objets(c) == avant
    _git("rev-list", "--all", "--objects", cwd=c)
    assert _objets(c) - avant >= N_BLOBS
