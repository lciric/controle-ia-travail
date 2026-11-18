"""Essais R5 de `scripts/lancer_relais_local_v1.py` : cas sain (environnement réduit, session neuve, console écrite) et
artefacts (nom refusé, console déjà là, commande absente, usage faux). Aucun réseau."""
import importlib.util
import json
import os
import subprocess
import sys
import time
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "lancer_relais_local_v1.py"
_spec = importlib.util.spec_from_file_location("lancer_relais_local_v1", SCRIPT)
lr = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(lr)


def test_environnement_reduit_sain():
    env, absents = lr.environnement_reduit(["PATH", "FAUX_CLE_X", "ABSENT_Y"], {"PATH": "/bin", "FAUX_CLE_X": "v", "AUTRE": "z"})
    assert env == {"PATH": "/bin", "FAUX_CLE_X": "v"} and absents == ["ABSENT_Y"]


@pytest.mark.parametrize("nom", ["ANTHROPIC_BASE_URL", "CLAUDE_CODE_REMOTE", "CLAUDE_X", "CCR_Y", ""])
def test_environnement_reduit_artefact_nom_refuse(nom):
    with pytest.raises(lr.Refus):
        lr.environnement_reduit(["PATH", nom], {"PATH": "/bin"})


def test_lancer_sain_session_neuve_et_console(tmp_path):
    console = tmp_path / "console.txt"
    prog = "import os, sys; print(os.getsid(0) != os.getsid(os.getppid()), sorted(k for k in os.environ if k not in ('PATH', 'LC_CTYPE'))); sys.stdout.flush()"
    r = lr.lancer(str(console), ["PATH", "FAUX_A"], [sys.executable, "-I", "-c", prog],
                  source={"PATH": os.environ["PATH"], "FAUX_A": "1", "FAUX_B": "2"})
    for _ in range(100):
        if console.exists() and console.read_text().strip():
            break
        time.sleep(0.05)
    assert r["noms_transmis"] == ["FAUX_A", "PATH"] and r["noms_absents"] == []
    assert console.read_text().strip() == "True ['FAUX_A']"


def test_lancer_artefact_console_presente(tmp_path):
    (tmp_path / "c.txt").write_text("x")
    with pytest.raises(lr.Refus):
        lr.lancer(str(tmp_path / "c.txt"), ["PATH"], ["true"], source={"PATH": "/bin"})


def test_lancer_artefact_sans_commande(tmp_path):
    with pytest.raises(lr.Refus):
        lr.lancer(str(tmp_path / "c.txt"), ["PATH"], [], source={"PATH": "/bin"})


def test_principal_usage_faux():
    assert lr.principal(["console"]) == 2


def test_fichier_reel_refuse_sans_rien_ecrire(tmp_path):
    p = subprocess.run([sys.executable, "-I", "-B", str(SCRIPT), str(tmp_path / "c.txt"), "PATH,ANTHROPIC_BASE_URL", "--", "true"],
                       capture_output=True, text=True)
    assert p.returncode == 2 and "refus" in json.loads(p.stderr)
    assert not (tmp_path / "c.txt").exists()
