"""Bornes de durée réglables de la relance de R1 sur la table v3 (scripts `amorce_instance_r1_relance_v3.sh` et
`r1_relance_instance_v3.sh`) et préenregistrement par défaut (addendum v3).

Les deux bornes qui coupaient en dur (plafond de l'amorce, 110 min ; délai externe de l'étape du rejeu, 60 min) se règlent
par `PLAFOND_AMORCE_MIN` et `DELAI_REJEU_MIN` (entiers de minutes de 1 à 9999 ; défauts inchangés) : l'addendum v3 les
règle à la création de l'instance (gardes très larges contre une boucle folle, non des budgets). Cas sain : valeur
transmise à `timeout` (amorce) ou écrite au journal (script), défaut inchangé. Artefacts (R5) : valeur hors domaine →
arrêt avant tout clonage, sans repli silencieux. Préenregistrement par défaut du script = l'addendum v3 : absent au
commit lancé → arrêt avant l'installation (code 2). Hors réseau : dépôts locaux seulement, jetons factices.
L'effet de chaque borne sur une étape réelle (coupure à 1 min) est éprouvé par l'essai jouet versé avec l'addendum v3."""
import os
import subprocess
from pathlib import Path

import pytest

RACINE = Path(__file__).resolve().parents[1]
AMORCE = RACINE / "scripts" / "amorce_instance_r1_relance_v3.sh"
SCRIPT = RACINE / "scripts" / "r1_relance_instance_v3.sh"
HORS_DOMAINE = ("0", "abc", "12h", "-5", "10000", "1.5", " 5", "")


def _env(**k) -> dict:
    """Environnement minimal et isolé : aucun jeton réel, aucune variable de la session (PREREG, BRANCHE…)."""
    e = {"PATH": os.environ["PATH"], "HOME": k.pop("HOME"), "LANG": "C.UTF-8", "GIT_TERMINAL_PROMPT": "0",
         "GIT_CONFIG_NOSYSTEM": "1", "GIT_AUTHOR_NAME": "essai", "GIT_AUTHOR_EMAIL": "essai@example.invalid",
         "GIT_COMMITTER_NAME": "essai", "GIT_COMMITTER_EMAIL": "essai@example.invalid"}
    e.update({c: v for c, v in k.items() if v is not None})
    return e


def _git(*a, cwd):
    subprocess.run(["git", *a], cwd=cwd, check=True, capture_output=True, text=True)


def _depot_stub(tmp_path: Path, corps_script: str) -> tuple[str, str]:
    """Dépôt local (et son dépôt nu) dont `scripts/r1_relance_instance_v3.sh` est un script témoin ; rend (url, commit)."""
    src = tmp_path / "stub-src"
    (src / "scripts").mkdir(parents=True)
    (src / "scripts" / "r1_relance_instance_v3.sh").write_text(corps_script, encoding="utf-8")
    _git("init", "-q", "-b", "main", cwd=src)
    _git("add", "-A", cwd=src)
    _git("commit", "-q", "-m", "témoin", cwd=src)
    commit = subprocess.run(["git", "rev-parse", "HEAD"], cwd=src, capture_output=True, text=True,
                            check=True).stdout.strip()
    nu = tmp_path / "stub.git"
    subprocess.run(["git", "clone", "-q", "--bare", str(src), str(nu)], check=True, capture_output=True)
    return f"file://{nu}", commit


@pytest.mark.parametrize("valeur", HORS_DOMAINE)
def test_amorce_plafond_hors_domaine_arrete_avant_le_clonage(tmp_path, valeur):
    r = subprocess.run(["bash", str(AMORCE)], capture_output=True, text=True, timeout=60,
                       env=_env(HOME=str(tmp_path), COMMIT="0" * 40, GH_TOKEN="jouet", HF_TOKEN="jouet",
                                DEPOT_URL=f"file://{tmp_path}/absent.git", RACINE_AMORCE=str(tmp_path),
                                PLAFOND_AMORCE_MIN=valeur))
    assert r.returncode == 1, r.stdout + r.stderr
    assert "PLAFOND_AMORCE_MIN" in r.stdout and "arrêt avant le clonage" in r.stdout
    assert not (tmp_path / "amorce-depot").exists() and not (tmp_path / "r1rel3").exists()


@pytest.mark.parametrize("valeur, attendu", ((None, "110m"), ("720", "720m"), ("1", "1m"), ("9999", "9999m")))
def test_amorce_plafond_transmis_a_timeout(tmp_path, valeur, attendu):
    # le script témoin lit la ligne de commande de son parent (`timeout`, qui a exécuté `env` puis `bash`)
    url, commit = _depot_stub(tmp_path, '#!/usr/bin/env bash\nprintf "PARENT %s\\n" "$(tr "\\0" " " < /proc/$PPID/cmdline)"\n'
                                        'printf "TRAVAIL %s\\n" "$TRAVAIL"\n')
    racine = tmp_path / "instance"
    racine.mkdir()
    r = subprocess.run(["bash", str(AMORCE)], capture_output=True, text=True, timeout=120,
                       env=_env(HOME=str(tmp_path), COMMIT=commit, GH_TOKEN="jouet", HF_TOKEN="jouet", DEPOT_URL=url,
                                RACINE_AMORCE=str(racine), PLAFOND_AMORCE_MIN=valeur))
    assert r.returncode == 0, r.stdout + r.stderr
    parent = [x for x in r.stdout.splitlines() if x.startswith("PARENT ")]
    assert len(parent) == 1, r.stdout
    mots = parent[0].split()
    assert mots[1] == "timeout" and attendu in mots and mots.index(attendu) < mots.index("env"), parent[0]
    assert f"plafond de l'amorce {attendu[:-1]} min" in r.stdout
    assert f"TRAVAIL {racine}/r1rel3" in r.stdout


@pytest.mark.parametrize("valeur", HORS_DOMAINE)
def test_script_delai_hors_domaine_arrete_avant_tout_clonage(tmp_path, valeur):
    travail = tmp_path / "travail"
    r = subprocess.run(["bash", str(SCRIPT)], capture_output=True, text=True, timeout=60,
                       env=_env(HOME=str(tmp_path), COMMIT="0" * 40, MODE="jouet", TESTS_CIBLES="tests/x.py",
                                DEPOT_URL=f"file://{tmp_path}/absent.git", TRAVAIL=str(travail),
                                DELAI_REJEU_MIN=valeur))
    assert r.returncode == 2, r.stdout + r.stderr
    assert "DELAI_REJEU_MIN" in r.stderr and "arrêt avant tout clonage" in r.stderr
    assert not travail.exists()


@pytest.mark.parametrize("valeur, attendu", ((None, "60"), ("600", "600")))
def test_script_delai_lu_et_journalise(tmp_path, valeur, attendu):
    # cas sain : la valeur est acceptée et écrite au journal ; le clonage échoue ensuite (dépôt absent, hors réseau)
    travail = tmp_path / "travail"
    r = subprocess.run(["bash", str(SCRIPT)], capture_output=True, text=True, timeout=60,
                       env=_env(HOME=str(tmp_path), COMMIT="0" * 40, MODE="jouet", TESTS_CIBLES="tests/x.py",
                                DEPOT_URL=f"file://{tmp_path}/absent.git", TRAVAIL=str(travail),
                                DELAI_REJEU_MIN=valeur))
    assert r.returncode != 0
    journal = (travail / "journal.txt").read_text(encoding="utf-8")
    assert f"ETAPES=rejeu DELAI_REJEU_MIN={attendu}\n" in journal, journal
    assert not (travail / "controle-ia" / "scripts").exists()


def test_script_preregistrement_par_defaut_addendum_v3(tmp_path):
    # mode réel, préenregistrement par défaut : l'addendum v3, absent au commit lancé → arrêt avant l'installation
    url, commit = _depot_stub(tmp_path, "#!/usr/bin/env bash\nexit 0\n")
    travail = tmp_path / "travail"
    r = subprocess.run(["bash", str(SCRIPT)], capture_output=True, text=True, timeout=120,
                       env=_env(HOME=str(tmp_path), COMMIT=commit, HF_TOKEN="jouet", GH_TOKEN="jouet", DEPOT_URL=url,
                                TRAVAIL=str(travail), BRANCHE="calcul/essai-prereg-defaut"))
    assert r.returncode == 2, r.stdout + r.stderr
    journal = (travail / "journal.txt").read_text(encoding="utf-8")
    assert "préenregistrement prereg/R1-addendum-relance-v3.md ou son sceau absent" in journal, journal
    branches = subprocess.run(["git", "ls-remote", "--heads", url], capture_output=True, text=True, check=True).stdout
    assert "calcul/essai-prereg-defaut" not in branches        # rien n'est poussé avant la lecture du préenregistrement
