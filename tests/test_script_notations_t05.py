"""Scripts de l'instance des notations refaites du pilote de T0.5 (`scripts/notations_t05_instance.sh`,
`scripts/amorce_instance_t05_notations.sh` ; N-021) : exécutés tels quels contre un dépôt distant local, avec un
`python` et un `nvidia-smi` factices (aucune installation, aucun processeur graphique). Lecture précoce des pièces du
pilote noté, relais des seules lignes de progression au journal, run complet ou arrêté, branche présente, amorce
(cas sain et artefact, R5)."""
from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path

import pytest

from controle_ia.scellement import sceller

RACINE = Path(__file__).resolve().parents[1]
SCRIPT = RACINE / "scripts" / "notations_t05_instance.sh"
AMORCE = RACINE / "scripts" / "amorce_instance_t05_notations.sh"
MODULES_AVANT_INSTALLATION = ("__init__.py", "gardes.py", "scellement.py")
ENV_DE_BASE = ("PATH", "LANG", "LC_ALL", "LC_CTYPE", "TMPDIR")
PREREG = "prereg/notations.md"
CONFIG = "prereg/config-notations.json"
PILOTE = "20261012-105125-t05-pilote-reel"
CITES = {"Chemin des tâches du pilote noté": "donnees/t05-pilote-v1/taches.json",
         "Chemin du manifeste du pilote noté": f"runs/{PILOTE}/manifeste.json",
         "Chemin des épisodes du pilote noté": f"diag/{PILOTE}/episodes.json",
         "Chemin de l'arrêt du pilote noté": f"diag/{PILOTE}/arret.json"}

PYTHON_FACTICE = """#!/usr/bin/env bash
if [ "$1" = "-m" ] && [ "$2" = "pytest" ]; then printf '%s\\n' "${FAUX_PYTEST_LIGNE:-7 passed in 1.00s}"; exit 0; fi
if [ "$1" = "-m" ] && [ "$2" = "pip" ]; then echo "paquet-factice==1.0"; exit 0; fi
if [ "$1" = "-c" ]; then
    case "$2" in *"is_available() else 1"*) exit 0 ;; esac
    echo "torch factice"; exit 0
fi
if [ "$1" = "-m" ] && [ "$2" = "controle_ia.environnements.noter_pilote_a" ]; then
    run=""; prec=""
    for a in "$@"; do [ "$prec" = "--run-id" ] && run="$a"; prec="$a"; done
    mkdir -p "diag/$run" "runs/$run"
    echo '{"factice": true}' > "runs/$run/manifeste.json"
    echo "PROGRES 2026-10-12T10:00:00Z juge=8B lot=1/23 duree_s=344.1 jetons=24576 tronquees=8 completes=0" >&2
    echo "PROGRES 2026-10-12T10:05:00Z texte libre PROPOSAL 1: ne doit pas passer" >&2
    echo "PROPOSAL 1: texte d'un ensemble, jamais au journal" >&2
    echo "PROGRES 2026-10-12T10:06:00Z juge=8B fin=écrit lots_faits=23/23 duree_s=7900.0" >&2
    if [ "${FAUX_RUN:-complet}" = complet ]; then
        echo '{"factice": true}' > "diag/$run/resume.json"; echo '{"run": "factice"}'; exit 0
    fi
    echo '{"factice": true}' > "diag/$run/arret.json"; echo "ARRÊT : échéance globale simulée" >&2; exit 1
fi
echo "appel inattendu : $*" >&2; exit 3
"""


def _git(d: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(d), *args], capture_output=True, text=True, check=True).stdout.strip()


def _prereg(doublon: str | None = None) -> str:
    lignes = ["# préenregistrement factice des notations", "- Tests attendus : `7`",
              f"- Chemin de la configuration des notations : `{CONFIG}`",
              *(f"- {k} : `{v}`" for k, v in CITES.items())]
    if doublon:
        lignes.append(f"- {doublon} : `autre/chemin.json`")
    return "\n".join(lignes) + "\n"


@pytest.fixture
def bac(tmp_path):
    src = tmp_path / "source"
    (src / "prereg").mkdir(parents=True)
    _git(tmp_path, "init", "-q", "-b", "main", str(src))
    _git(src, "config", "user.email", "t@example.invalid")
    _git(src, "config", "user.name", "t")
    for d in ("runs", "diag"):
        (src / d).mkdir(exist_ok=True)
        (src / d / ".gitkeep").write_text("", encoding="utf-8")
    (src / PREREG).write_text(_prereg(), encoding="utf-8")
    for chemin in [CONFIG, *CITES.values()]:
        f = src / chemin
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text("{}", encoding="utf-8")
        sceller(f)
    (src / "src" / "controle_ia").mkdir(parents=True)
    for nom in MODULES_AVANT_INSTALLATION:
        shutil.copy(RACINE / "src" / "controle_ia" / nom, src / "src" / "controle_ia" / nom)
    (src / "scripts").mkdir()
    shutil.copy(SCRIPT, src / "scripts" / SCRIPT.name)
    _git(src, "add", "-A")
    _git(src, "commit", "-qm", "init")
    venv = tmp_path / "venv"
    (venv / "bin").mkdir(parents=True)
    (venv / "bin" / "activate").write_text(f'export PATH="{venv}/bin:$PATH"\n', encoding="utf-8")
    for nom, texte in (("python", PYTHON_FACTICE), ("nvidia-smi", "#!/usr/bin/env bash\necho 'A100, 580, 81920 MiB'\n")):
        (venv / "bin" / nom).write_text(texte, encoding="utf-8")
        (venv / "bin" / nom).chmod(0o755)
    return {"racine": tmp_path, "source": src, "venv": venv}


def _distant(bac) -> Path:
    d = bac["racine"] / f"distant-{len(list(bac['racine'].glob('distant-*')))}.git"
    subprocess.run(["git", "clone", "-q", "--bare", str(bac["source"]), str(d)], check=True)
    return d


def _env(bac, distant: Path, travail: str, env_sup: dict | None) -> dict:
    env = {k: os.environ[k] for k in ENV_DE_BASE if k in os.environ}
    env.update(COMMIT=_git(bac["source"], "rev-parse", "HEAD"), MODE="jouet", DEPOT_URL=str(distant),
               TRAVAIL=str(bac["racine"] / travail), PREREG=PREREG, VENV_EXISTANT=str(bac["venv"]),
               HOME=str(bac["racine"]))
    env.update(env_sup or {})
    return env


def _lancer(bac, distant: Path, travail: str = "t", env_sup: dict | None = None):
    r = subprocess.run(["bash", str(SCRIPT)], env=_env(bac, distant, travail, env_sup), capture_output=True,
                       text=True, timeout=300)
    j = bac["racine"] / travail / "journal.txt"
    return r.returncode, (j.read_text(encoding="utf-8") if j.exists() else ""), r.stdout + r.stderr


def _commit_source(bac, message: str) -> None:
    _git(bac["source"], "add", "-A")
    _git(bac["source"], "commit", "-qm", message)


def test_cas_sain_lecture_precoce_relais_et_run_complet(bac):
    distant = _distant(bac)
    code, journal, sortie = _lancer(bac, distant)
    assert code == 0, sortie[-3000:]
    assert "pilote noté : manifeste, épisodes et arrêt présents et scellés" in journal
    assert "BRANCHE=calcul/t05-notations-jouet-v1" in journal and "run terminé" in journal
    progres = [x for x in journal.splitlines() if x.startswith("PROGRES ")]
    assert progres == ["PROGRES 2026-10-12T10:00:00Z juge=8B lot=1/23 duree_s=344.1 jetons=24576 tronquees=8 completes=0",
                       "PROGRES 2026-10-12T10:06:00Z juge=8B fin=écrit lots_faits=23/23 duree_s=7900.0"]
    assert "PROPOSAL" not in journal and "texte libre" not in journal                   # aucun texte au journal
    assert "PROGRES" in sortie and "PROPOSAL" not in sortie                              # ni sur la sortie (vastai logs)
    assert "run" in _git(distant, "log", "-2", "--format=%s", "calcul/t05-notations-jouet-v1")


@pytest.mark.parametrize("artefact, motif", [
    ("doublon", "introuvable ou cité plusieurs fois"),
    ("sceau-absent", "ou son sceau absent"),
    ("sceau-faux", "sceau non conforme"),
    ("prereg-absent", "absent au commit"),
])
def test_lecture_precoce_artefacts(bac, artefact, motif):
    src = bac["source"]
    if artefact == "doublon":
        (src / PREREG).write_text(_prereg(doublon="Chemin des épisodes du pilote noté"), encoding="utf-8")
    elif artefact == "sceau-absent":
        (src / (CITES["Chemin de l'arrêt du pilote noté"] + ".sha256")).unlink()
    elif artefact == "sceau-faux":
        (src / CITES["Chemin des épisodes du pilote noté"]).write_text('{"altere": 1}', encoding="utf-8")
    else:
        (src / PREREG).unlink()
    _commit_source(bac, artefact)
    code, journal, sortie = _lancer(bac, _distant(bac))
    assert code == 2 and motif in journal and "arrêt avant l'installation" in journal, sortie[-2000:]
    assert "tests :" not in journal


def test_run_arrete_consigne_et_pousse(bac):
    distant = _distant(bac)
    code, journal, _ = _lancer(bac, distant, env_sup={"FAUX_RUN": "arret"})
    assert code == 1 and "ARRÊT pendant run" in journal and "branche calcul/t05-notations-jouet-v1 poussée" in journal
    assert "arrêt" in _git(distant, "log", "-1", "--format=%s", "calcul/t05-notations-jouet-v1")
    # diagnostic de fin, comme au pilote : dernières lignes de la sortie d'erreur du run, cause comprise ; le relais
    # pendant le run, lui, n'a laissé passer que les lignes de progression conformes
    assert "ARRÊT : échéance globale simulée" in journal
    progres = [x for x in journal.splitlines() if x.startswith("PROGRES ")]
    assert progres == ["PROGRES 2026-10-12T10:00:00Z juge=8B lot=1/23 duree_s=344.1 jetons=24576 tronquees=8 completes=0",
                       "PROGRES 2026-10-12T10:06:00Z juge=8B fin=écrit lots_faits=23/23 duree_s=7900.0"]


def test_branche_presente_arrete_puis_relancement_sous_v2(bac):
    distant = _distant(bac)
    subprocess.run(["git", "-C", str(distant), "branch", "-f", "calcul/t05-notations-jouet-v1", "main"], check=True)
    code, journal, _ = _lancer(bac, distant)
    assert code == 2 and "déjà présente" in journal
    code, journal, _ = _lancer(bac, distant, travail="t2", env_sup={"BRANCHE": "calcul/t05-notations-jouet-v2"})
    assert code == 0 and "BRANCHE=calcul/t05-notations-jouet-v2" in journal


def test_amorce_cas_sain_et_dossiers_presents(bac):
    distant = _distant(bac)
    racine = bac["racine"] / "amorce"
    racine.mkdir()
    env = _env(bac, distant, "inutile", {"RACINE_AMORCE": str(racine), "GH_TOKEN": "x", "HF_TOKEN": "y"})
    env.pop("TRAVAIL")
    r = subprocess.run(["bash", str(AMORCE)], env=env, capture_output=True, text=True, timeout=300)
    assert r.returncode == 0 and "fin, code 0" in r.stdout, (r.stdout + r.stderr)[-3000:]
    assert "PROGRES 2026-10-12T10:00:00Z juge=8B" in r.stdout                # relais vu par `vastai logs`
    journal = (racine / "t05" / "journal.txt").read_text(encoding="utf-8")
    assert "PROPOSAL" not in journal and "texte libre" not in journal
    r = subprocess.run(["bash", str(AMORCE)], env=env, capture_output=True, text=True, timeout=300)
    assert r.returncode == 1 and "dossiers d'un essai précédent présents (R12)" in r.stdout
