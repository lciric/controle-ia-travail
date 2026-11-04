"""Préparation de la répétition jouet des deux sessions de la relance v4 de R1 (amorce v2, script v2), hors réseau.

Lancé par pytest (fixtures du dépôt : P3 jouet, tables jouets) : `E` = variable REPETITION_V4 (dossier neuf). Dépôt
d'essai = arbre du commit cité (`git archive`) + fichiers neufs de l'arbre de travail (liste FICHIERS_NEUFS) + pièces
jouets (P3 jouet, table v2 et v3 jouets, configurations jouets, chemins relatifs) ; dépôt nu `depot.git`."""
import json
import os
import shutil
import subprocess
from pathlib import Path

from conftest import _signal_term_efface, depot  # noqa: F401  (fixtures)
from test_premier_test_ia_run import entropie_fixe  # noqa: F401
from test_resolution_graine_lot_v1 import _preparer
from test_resolution_graine_lot_v3 import _config_v4, _table_v3_jouet
from test_runs_nuit_v1 import source  # noqa: F401
from test_runs_nuit_v2 import _config_v2

ARBRE = Path(os.environ["ARBRE_V4"]).resolve()
COMMIT = os.environ["COMMIT_V4"]
E = Path(os.environ["REPETITION_V4"]).resolve()
FICHIERS_NEUFS = os.environ["FICHIERS_NEUFS_V4"].split()


def git(d, *a):
    return subprocess.run(["git", "-C", str(d), *a], check=True, capture_output=True, text=True).stdout.strip()


def test_preparer(source, tmp_path):
    from conftest import committer
    from controle_ia.scellement import sceller

    E.mkdir(parents=True, exist_ok=False)
    src = E / "depot-source"
    src.mkdir()
    arch = subprocess.run(["git", "-C", str(ARBRE), "archive", COMMIT, "src", "tests", "scripts", "prereg",
                           "pyproject.toml", "requirements-cpu.txt", "requirements-gpu.txt", ".gitignore",
                           "docs/sources/invites-2606.08892-v1", "donnees/T0.7-faits-repe-v1",
                           "donnees/T0.7-models-under-pressure-v1"], capture_output=True, check=True).stdout
    subprocess.run(["tar", "-x", "-C", str(src)], input=arch, check=True)
    for f in FICHIERS_NEUFS:
        (src / f).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ARBRE / f, src / f)
    # pièces jouets (dépôt jetable des essais = tmp_path)
    d0, f, c, tp, pieces0, fmt_j, cl, connus, autres = _preparer(source, tmp_path)
    t3 = _table_v3_jouet(d0, tmp_path, tmp_path / "table0.json")
    committer(d0)
    conf_r = _config_v4(d0, f, c, tp, t3)
    conf_j = _config_v2(d0, f, c, Path("prereg/R1-table-tokenisation-v4.json"),
                        table_tokenisation_sha256="construite-en-session")

    def relatif(conf):
        out = {}
        for k, v in conf.items():
            if isinstance(v, str) and v.startswith(str(d0)):
                v = str(Path(v).relative_to(d0))
            elif isinstance(v, str) and v.startswith(str(ARBRE)):
                v = str(Path(v).relative_to(ARBRE))
            out[k] = v
        return out

    for x in d0.iterdir():
        if x.name in (".git", "README"):
            continue
        cible = src / x.name
        if x.is_dir():
            shutil.copytree(x, cible, dirs_exist_ok=True)
        else:
            shutil.copy2(x, cible)
    essai = src / "essai"
    essai.mkdir(exist_ok=True)
    for nom, conf in (("reparation-v4-jouet.json", relatif(conf_r)), ("rejeu-v6-jouet.json", relatif(conf_j))):
        (essai / nom).write_text(json.dumps(conf, sort_keys=True, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        sceller(essai / nom)
    absolus = [k for conf in (relatif(conf_r), relatif(conf_j)) for k, v in conf.items()
               if isinstance(v, str) and v.startswith("/")]
    assert not absolus, absolus
    git(src, "init", "-q", "-b", "main")
    git(src, "config", "user.email", "essai@example.invalid")
    git(src, "config", "user.name", "essai")
    subprocess.run(["git", "-C", str(src), "add", "-A", "-f", "."], check=True)
    git(src, "commit", "-q", "-m", f"essai jouet v4 : arbre {COMMIT} + fichiers neufs + pièces jouets")
    subprocess.run(["git", "clone", "-q", "--bare", str(src), str(E / "depot.git")], check=True)
    (E / "preparation.json").write_text(json.dumps({
        "commit_essai": git(src, "rev-parse", "HEAD"), "cibles_jouet": len(autres), "connus_jouet": len(connus),
        "configurations": ["essai/reparation-v4-jouet.json", "essai/rejeu-v6-jouet.json"]}, indent=1), encoding="utf-8")
