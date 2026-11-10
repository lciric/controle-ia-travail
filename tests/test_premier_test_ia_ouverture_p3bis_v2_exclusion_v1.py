"""Garde du fichier d'exclusion local de `premier_test_ia.ouverture_p3bis_v2.exclure_localement` (contre-lecture
différentielle de P3-bis, CD-01 ; incident R-2085 : une ligne écrite dans le fichier d'exclusion commun d'un dépôt
englobant). Essais R5 : un cas sain (racine d'un clone : motif écrit une fois, sous `<racine>/.git/`) et deux artefacts
(sous-dossier d'un dépôt ; arbre lié, `.git` fichier), plus le même refus par `fermer_run`, qui appelle la garde d'abord.
Tous dans un dossier temporaire hors de tout dépôt, git plafonné par `GIT_CEILING_DIRECTORIES` : aucun essai ne peut
remonter vers un dépôt réel."""
import subprocess
from pathlib import Path

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.premier_test_ia import ouverture_p3bis_v2 as ob


def _git(d: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(d), *args], check=True, capture_output=True, text=True).stdout.strip()


def _depot(d: Path) -> Path:
    d.mkdir(parents=True)
    _git(d, "init", "-q", "-b", "main")
    _git(d, "config", "user.email", "essai@example.invalid")
    _git(d, "config", "user.name", "essai")
    (d / "README").write_text("x\n", encoding="utf-8")
    _git(d, "add", "-A")
    _git(d, "commit", "-qm", "init")
    return d


def _exclusion(d: Path) -> bytes | None:
    p = d / ".git" / "info" / "exclude"
    return p.read_bytes() if p.exists() else None


@pytest.fixture(autouse=True)
def _plafond(tmp_path, monkeypatch):
    monkeypatch.setenv("GIT_CEILING_DIRECTORIES", str(tmp_path))


def test_racine_d_un_clone_saine(tmp_path):
    d = _depot(tmp_path / "clone")
    ob.exclure_localement(d, ["/runs/x/", "/runs/x/", "/diag/x/"])
    lignes = (d / ".git" / "info" / "exclude").read_text(encoding="utf-8").splitlines()
    assert lignes.count("/runs/x/") == 1 and lignes.count("/diag/x/") == 1


def test_sous_dossier_d_un_depot_refuse_rien_ecrit(tmp_path):
    d = _depot(tmp_path / "englobant")
    (d / "sous" / "plus-bas").mkdir(parents=True)
    avant = _exclusion(d)
    for cible in (d / "sous", d / "sous" / "plus-bas"):
        with pytest.raises(GardeArret, match="n'est pas la racine de son dépôt git"):
            ob.exclure_localement(cible, ["/x/"])
    assert _exclusion(d) == avant


def test_arbre_lie_refuse_rien_ecrit(tmp_path):
    d = _depot(tmp_path / "principal")
    _git(d, "worktree", "add", "-q", str(tmp_path / "lie"), "-b", "lie")
    lie = tmp_path / "lie"
    assert (lie / ".git").is_file()
    avant = _exclusion(d)
    with pytest.raises(GardeArret, match="arbre lié"):
        ob.exclure_localement(lie, ["/x/"])
    assert _exclusion(d) == avant
    assert not (d / ".git" / "worktrees" / "lie" / "info" / "exclude").exists()


def test_fermer_run_sur_un_sous_dossier_refuse_avant_toute_ecriture(tmp_path):
    d = _depot(tmp_path / "englobant")
    sous = d / "sous"
    sous.mkdir()
    avant = _exclusion(d)
    with pytest.raises(GardeArret, match="n'est pas la racine de son dépôt git"):
        ob.fermer_run(sous, "20261120-120000-p3bis-reel")
    assert _exclusion(d) == avant
    assert sorted(p.name for p in sous.iterdir()) == []


def test_hors_d_un_depot_refuse(tmp_path):
    (tmp_path / "pas-git").mkdir()
    with pytest.raises(GardeArret, match="n'est pas un clone git"):
        ob.exclure_localement(tmp_path / "pas-git", ["/x/"])
