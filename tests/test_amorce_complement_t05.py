"""Amorce de l'instance des notations complémentaires de T0.5 (`scripts/amorce_complement_t05.sh`) : exécutée telle
quelle contre un dépôt distant local, avec le `python` et le `nvidia-smi` factices des tests du script du complément.
Cas sain en mode jouet (lignes de départ et de fin, deux runs, relais des seules lignes de progression), plafond atteint
(traces versées sur la branche), artefacts : COMMIT, jeton ou PREREG_1 absent, seconde exécution refusée (R12)."""
from __future__ import annotations

import os
import re
import shutil
import subprocess
from pathlib import Path

import pytest

from test_script_complement_t05 import BRANCHE, ENV_DE_BASE, _distant, _git, bac  # noqa: F401 (fixture importée)

AMORCE = Path(__file__).resolve().parents[1] / "scripts" / "amorce_complement_t05.sh"


def _env(bac, distant: Path, env_sup: dict | None = None) -> dict:
    env = {k: os.environ[k] for k in ENV_DE_BASE if k in os.environ}
    env.update(COMMIT=_git(bac["source"], "rev-parse", "HEAD"), MODE="jouet", DEPOT_URL=str(distant),
               RACINE_AMORCE=str(bac["racine"] / "amorce"), PREREG_1="prereg/complement-1.md",
               PREREG_2="prereg/complement-2.md", VENV_EXISTANT=str(bac["venv"]), HOME=str(bac["racine"]),
               GH_TOKEN="x", HF_TOKEN="y")
    env.update(env_sup or {})
    return env


def _amorcer(bac, distant: Path, env_sup: dict | None = None, sans: tuple = ()):
    (bac["racine"] / "amorce").mkdir(exist_ok=True)
    env = {k: v for k, v in _env(bac, distant, env_sup).items() if k not in sans}
    r = subprocess.run(["bash", str(AMORCE)], env=env, capture_output=True, text=True, timeout=300)
    return r.returncode, r.stdout, r.stdout + r.stderr


def test_amorce_cas_sain_puis_seconde_execution_refusee(bac):
    distant = _distant(bac)
    code, sortie, tout = _amorcer(bac, distant)
    assert code == 0, tout[-3000:]
    lignes = sortie.splitlines()
    assert re.fullmatch(r"AMORCE \d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z : commit [0-9a-f]{40}", lignes[0])
    assert any(re.fullmatch(r"AMORCE \S+ : fin, code 0", x) for x in lignes)
    assert sortie.count("PROGRES 2026-10-27T10:00:00Z juge=8B lot=1/3 duree_s=344.1") >= 2   # relais (vastai logs)
    journal = (bac["racine"] / "amorce" / "t05" / "journal.txt").read_text(encoding="utf-8")
    assert journal.count("run terminé") == 2 and "PROPOSAL" not in journal and "texte libre" not in journal
    assert "(dernières lignes, hors progression)" in sortie
    assert "run 2" in _git(distant, "log", "--format=%s", BRANCHE)
    # seconde exécution sur la même instance : refus (R12), aucun run de plus
    code, sortie, _ = _amorcer(bac, distant)
    assert code == 1 and "dossiers d'un essai précédent présents (R12)" in sortie
    assert len((bac["racine"] / "amorce" / "t05" / "appels.txt").read_text().splitlines()) == 2


@pytest.mark.parametrize("absente", ["COMMIT", "GH_TOKEN", "HF_TOKEN", "PREREG_1"])
def test_variable_obligatoire_absente(bac, absente):
    code, sortie, tout = _amorcer(bac, _distant(bac), sans=(absente,))
    assert code != 0 and f"{absente} absent" in tout and "AMORCE" not in sortie, tout[-2000:]
    assert not (bac["racine"] / "amorce" / "amorce-depot").exists()


def test_plafond_atteint_traces_versees(bac):
    """Plafond de l'amorce ramené à 20 s (faux `timeout`, qui ne change que la durée du plafond), premier run endormi :
    TERM au script (arrêt consigné), code 124, traces de l'amorce versées sur la branche."""
    faux = bac["racine"] / "faux-timeout"
    faux.mkdir()
    (faux / "timeout").write_text(
        "#!/usr/bin/env bash\nargs=()\nfor a in \"$@\"; do [ \"$a\" = 480m ] && a=20s; args+=(\"$a\"); done\n"
        f"exec {shutil.which('timeout')} \"${{args[@]}}\"\n", encoding="utf-8")
    (faux / "timeout").chmod(0o755)
    python = bac["venv"] / "bin" / "python"
    shutil.move(python, bac["venv"] / "bin" / "python-factice")
    python.write_text("#!/usr/bin/env bash\n"
                      "if [ \"$2\" = controle_ia.environnements.noter_complement_t05 ]; then exec sleep 120; fi\n"
                      f"exec {bac['venv'] / 'bin' / 'python-factice'} \"$@\"\n", encoding="utf-8")
    python.chmod(0o755)
    distant = _distant(bac)
    code, sortie, tout = _amorcer(bac, distant, env_sup={"PATH": f"{faux}:{os.environ['PATH']}"})
    assert code == 124 and re.search(r"AMORCE \S+ : fin, code 124", sortie), tout[-3000:]
    journal = (bac["racine"] / "amorce" / "t05" / "journal.txt").read_text(encoding="utf-8")
    assert "TERM reçu pendant" in journal
    log = _git(distant, "log", "--format=%s", BRANCHE)
    assert "complément : plafond de l'amorce atteint : résultats partiels et traces" in log
    assert "traces/t05-complement-plafond-" in _git(distant, "ls-tree", "-r", "--name-only", BRANCHE)
