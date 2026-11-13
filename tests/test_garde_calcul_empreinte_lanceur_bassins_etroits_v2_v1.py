"""Garde d'empreinte du lanceur « bassins étroits » v2 au crochet `garde_calcul.py` (R-2530, R-2540) : cas sains et
artefacts (R5). Le crochet est appelé comme Claude Code l'appelle (entrée JSON de `PreToolUse`, code 0 ou 2). Les cas qui
modifient un fichier travaillent sur une copie du crochet dans un dossier jetable où seule `DEPOT_COURSE` est remplacée.
Le lanceur n'est jamais exécuté : le crochet ne fait que lire et hacher."""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

RACINE = Path(__file__).resolve().parents[1]
HOOK = RACINE / ".claude" / "hooks" / "garde_calcul.py"
NOM = "lancer_course_ideation_bassins_etroits_v2"
FICHIER = NOM + ".py"
LANCEUR = RACINE / "scripts" / FICHIER
BASE = "/usr/local/bin/python3 -I -B scripts/" + FICHIER
DEPOT_REEL = "/home/user/controle-ia-travail"
LIGNE_CONSTANTE = 'DEPOT_COURSE = Path("/home/user/controle-ia-travail")'


def appeler(hook: Path, commande: str, cwd: str | None):
    entree = {"session_id": "essai", "hook_event_name": "PreToolUse", "tool_name": "Bash",
              "tool_input": {"command": commande, "description": "essai"}}
    if cwd is not None:
        entree["cwd"] = cwd
    r = subprocess.run([sys.executable, str(hook)], input=json.dumps(entree), capture_output=True, text=True, timeout=60)
    return r.returncode, r.stderr


@pytest.fixture
def jetable(tmp_path):
    (tmp_path / ".claude" / "hooks").mkdir(parents=True)
    (tmp_path / "scripts").mkdir()
    (tmp_path / "registres").mkdir()
    (tmp_path / "registres" / "go.md").write_text("# GO\n", encoding="utf-8")
    texte = HOOK.read_text(encoding="utf-8")
    assert texte.count(LIGNE_CONSTANTE) == 1
    hook = tmp_path / ".claude" / "hooks" / "garde_calcul.py"
    hook.write_text(texte.replace(LIGNE_CONSTANTE, f"DEPOT_COURSE = Path({str(tmp_path)!r})"), encoding="utf-8")
    shutil.copy(LANCEUR, tmp_path / "scripts" / FICHIER)
    shutil.copy(str(LANCEUR) + ".sha256", tmp_path / "scripts" / (FICHIER + ".sha256"))
    return {"racine": tmp_path, "hook": hook, "lanceur": tmp_path / "scripts" / FICHIER,
            "compagnon": tmp_path / "scripts" / (FICHIER + ".sha256")}


def test_sain_jetable_generation_1(jetable):
    code, err = appeler(jetable["hook"], BASE + " 1", str(jetable["racine"]))
    assert code == 0, err


@pytest.mark.skipif(str(RACINE) != DEPOT_REEL, reason="dépôt réel exigé")
def test_sain_crochet_reel_generation_1():
    code, err = appeler(HOOK, BASE + " 1", DEPOT_REEL)
    assert code == 0, err


@pytest.mark.parametrize("commande", [BASE, BASE + " 2", BASE + " 3", BASE + " 1 --x", BASE + "  1", "cd . && " + BASE + " 1",
                                      "cat scripts/" + FICHIER, "python3 scripts/" + FICHIER + " 1"])
def test_artefact_commande_non_exacte(jetable, commande):
    code, err = appeler(jetable["hook"], commande, str(jetable["racine"]))
    assert code == 2 and "bassins étroits" in err


def test_artefact_autre_dossier(jetable, tmp_path_factory):
    code, err = appeler(jetable["hook"], BASE + " 1", str(tmp_path_factory.mktemp("ailleurs")))
    assert code == 2 and "exigé" in err


def test_artefact_dossier_absent(jetable):
    code, err = appeler(jetable["hook"], BASE + " 1", None)
    assert code == 2 and "dossier courant absent" in err


def test_artefact_fichier_modifie(jetable):
    jetable["lanceur"].write_text(jetable["lanceur"].read_text(encoding="utf-8") + "\n# modifié\n", encoding="utf-8")
    code, err = appeler(jetable["hook"], BASE + " 1", str(jetable["racine"]))
    assert code == 2 and "empreinte épinglée" in err


def test_artefact_compagnon_faux(jetable):
    jetable["compagnon"].write_text("0" * 64 + "  " + FICHIER + "\n", encoding="utf-8")
    code, err = appeler(jetable["hook"], BASE + " 1", str(jetable["racine"]))
    assert code == 2 and "compagnon" in err


def test_artefact_compagnon_absent(jetable):
    jetable["compagnon"].unlink()
    code, err = appeler(jetable["hook"], BASE + " 1", str(jetable["racine"]))
    assert code == 2 and "illisible" in err


def test_artefact_lien_symbolique(jetable):
    vrai = jetable["racine"] / "scripts" / "copie.py"
    jetable["lanceur"].rename(vrai)
    jetable["lanceur"].symlink_to(vrai)
    code, err = appeler(jetable["hook"], BASE + " 1", str(jetable["racine"]))
    assert code == 2 and "lien symbolique" in err


def test_essais_du_lanceur_non_cites(jetable):
    code, err = appeler(jetable["hook"], "python -m pytest -q tests/test_" + FICHIER, str(jetable["racine"]))
    assert code == 0, err
