"""Preuve de la garde des variables git (`conftest.py` de la racine ; R-2919, point 7) : lancé sous `GIT_DIR` (et `GIT_WORK_TREE`,
`GIT_INDEX_FILE`, `GIT_COMMON_DIR`, `GIT_CONFIG_*`) pointés vers un dépôt jouet **témoin**, l'essai même de l'incident
(`tests/test_t07bbis_lien_mots_et_cout_v1.py`, essai qui fabrique sept dépôts jouets par `git -C`) ne touche pas le témoin : tête,
références, index et réglages égaux au bit près. Artefact : les commandes de l'incident jouées hors de `pytest`, sans la garde,
sous les mêmes variables, déplacent le témoin (la menace est réelle et l'essai la voit). Aucun dépôt réel n'est jamais visé."""
from __future__ import annotations

import hashlib
import os
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
VARIABLES = ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE", "GIT_COMMON_DIR", "GIT_OBJECT_DIRECTORY",
             "GIT_ALTERNATE_OBJECT_DIRECTORIES")


def _git(d, *args, env=None):
    return subprocess.run(["git", "-C", str(d), *args], check=True, capture_output=True, text=True, env=env)


def _temoin(d: Path) -> Path:
    d.mkdir(parents=True)
    _git(d, "init", "-q", "-b", "main")
    _git(d, "config", "user.email", "temoin@example.invalid")
    _git(d, "config", "user.name", "temoin")
    (d / "temoin.txt").write_text("témoin\n", encoding="utf-8")
    _git(d, "add", "-A")
    _git(d, "commit", "-q", "-m", "temoin")
    return d


def _etat(d: Path) -> tuple:
    g = d / ".git"
    return (_git(d, "rev-parse", "HEAD").stdout, _git(d, "for-each-ref").stdout,
            hashlib.sha256((g / "index").read_bytes()).hexdigest(), (g / "config").read_text(encoding="utf-8"),
            sorted(p.name for p in d.iterdir()))


def _env_vers(t: Path) -> dict:
    g = t / ".git"
    return {**os.environ, "GIT_DIR": str(g), "GIT_WORK_TREE": str(t), "GIT_INDEX_FILE": str(g / "index"),
            "GIT_COMMON_DIR": str(g), "GIT_CONFIG_COUNT": "1", "GIT_CONFIG_KEY_0": "user.name", "GIT_CONFIG_VALUE_0": "intrus"}


def test_la_session_d_essais_n_a_aucune_variable_git_dangereuse():
    assert not [k for k in os.environ if k in VARIABLES or k.startswith("GIT_CONFIG")]


def test_sous_git_dir_vers_un_temoin_l_essai_de_l_incident_ne_le_touche_pas(tmp_path):
    t = _temoin(tmp_path / "temoin")
    avant = _etat(t)
    r = subprocess.run([sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", "--color=no",
                        "tests/test_t07bbis_lien_mots_et_cout_v1.py", "-k", "artefacts_module_ligne_fichier_commit",
                        "--basetemp", str(tmp_path / "bt")],
                       cwd=RACINE, env=_env_vers(t), capture_output=True, text=True, timeout=1200)
    assert r.returncode in (0, 5) and ("passed" in r.stdout or "skipped" in r.stdout), r.stdout[-2000:] + r.stderr[-2000:]
    assert _etat(t) == avant


def test_artefact_sans_garde_les_commandes_de_l_incident_deplacent_le_temoin(tmp_path):
    t = _temoin(tmp_path / "temoin")
    avant = _etat(t)
    d = tmp_path / "jouet"
    d.mkdir()
    (d / "piece.txt").write_text("pièce\n", encoding="utf-8")
    env = _env_vers(t)
    for args in (("init", "-q", "-b", "main"), ("config", "user.email", "essai@example.invalid"), ("config", "user.name", "essai"),
                 ("add", "-A"), ("commit", "-q", "-m", "piece")):
        subprocess.run(["git", "-C", str(d), *args], capture_output=True, text=True, env=env)
    assert _etat(t) != avant                                     # sans la garde, le témoin a bougé (tête, index ou réglages)
    assert not (d / ".git").exists()                             # et le dépôt jouet voulu n'existe pas
