"""Script de l'instance des notations complémentaires de T0.5 (`scripts/complement_t05_instance.sh`) : exécuté tel quel
contre un dépôt distant local, avec un `python` et un `nvidia-smi` factices (aucune installation, aucun processeur
graphique). Deux runs successifs au plus, lecture précoce des pièces citées par chaque préenregistrement, relais des
seules lignes de progression, échec du premier run consigné sans empêcher le second, délai externe global borné, mode
jouet sans préenregistrement (cas sain et artefact, R5)."""
from __future__ import annotations

import os
import re
import shutil
import subprocess
from pathlib import Path

import pytest

from controle_ia.scellement import sceller

RACINE = Path(__file__).resolve().parents[1]
SCRIPT = RACINE / "scripts" / "complement_t05_instance.sh"
MODULES_AVANT_INSTALLATION = ("__init__.py", "gardes.py", "scellement.py")
ENV_DE_BASE = ("PATH", "LANG", "LC_ALL", "LC_CTYPE", "TMPDIR")
SOURCES = ("20261012-105125-t05-pilote-reel", "20261020-090000-t05-banque-reel")
BRANCHE = "calcul/t05-complement-jouet-v1"


def _cites(k: int) -> dict:
    source = SOURCES[k - 1]
    return {"Chemin de la configuration du complément": f"prereg/config-complement-{k}.json",
            "Chemin des tâches du run source": f"donnees/t05-taches-{k}/taches.json",
            "Chemin du manifeste du run source": f"runs/{source}/manifeste.json",
            "Chemin des épisodes du run source": f"diag/{source}/episodes.json"}


PYTHON_FACTICE = """#!/usr/bin/env bash
if [ "$1" = "-m" ] && [ "$2" = "pytest" ]; then printf '%s\\n' "${FAUX_PYTEST_LIGNE:-7 passed in 1.00s}"; exit 0; fi
if [ "$1" = "-m" ] && [ "$2" = "pip" ]; then echo "paquet-factice==1.0"; exit 0; fi
if [ "$1" = "-c" ]; then
    case "$2" in *"is_available() else 1"*) exit "${FAUX_CARTE_CODE:-0}" ;; esac
    echo "torch factice"; exit 0
fi
if [ "$1" = "-m" ] && [ "$2" = "controle_ia.environnements.noter_complement_t05" ]; then
    run=""; prec=""; config=""
    for a in "$@"; do [ "$prec" = "--run-id" ] && run="$a"; [ "$prec" = "--config" ] && config="$a"; prec="$a"; done
    echo "$run $config $*" >> "$TRAVAIL/appels.txt"
    mkdir -p "diag/$run" "runs/$run"
    echo '{"factice": true}' > "runs/$run/manifeste.json"
    echo "PROGRES 2026-10-27T10:00:00Z juge=8B lot=1/3 duree_s=344.1" >&2
    echo "PROGRES 2026-10-27T10:05:00Z texte libre PROPOSAL 1: ne doit pas passer" >&2
    echo "PROPOSAL 1: texte d'un ensemble, jamais au journal" >&2
    case "$run" in *-complement-1-*) issue="${FAUX_RUN_1:-complet}" ;; *) issue="${FAUX_RUN_2:-complet}" ;; esac
    if [ "$issue" = complet ]; then
        echo '{"factice": true}' > "diag/$run/resume.json"; echo '{"run": "factice"}'; exit 0
    fi
    echo '{"factice": true}' > "diag/$run/arret.json"; echo "ARRÊT : échéance globale simulée" >&2; exit 1
fi
echo "appel inattendu : $*" >&2; exit 3
"""


def _git(d: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(d), *args], capture_output=True, text=True, check=True).stdout.strip()


def _prereg(k: int, attendus: str = "7", doublon: str | None = None) -> str:
    lignes = [f"# préenregistrement factice du complément {k}", f"- Tests attendus : `{attendus}`",
              *(f"- {c} : `{v}`" for c, v in _cites(k).items())]
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
    for k in (1, 2):
        (src / "prereg" / f"complement-{k}.md").write_text(_prereg(k), encoding="utf-8")
        for chemin in _cites(k).values():
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


def _lancer(bac, distant: Path, travail: str = "t", env_sup: dict | None = None, deux: bool = True):
    env = {k: os.environ[k] for k in ENV_DE_BASE if k in os.environ}
    env.update(COMMIT=_git(bac["source"], "rev-parse", "HEAD"), MODE="jouet", DEPOT_URL=str(distant),
               TRAVAIL=str(bac["racine"] / travail), PREREG_1="prereg/complement-1.md",
               VENV_EXISTANT=str(bac["venv"]), HOME=str(bac["racine"]))
    if deux:
        env["PREREG_2"] = "prereg/complement-2.md"
    env.update(env_sup or {})
    r = subprocess.run(["bash", str(SCRIPT)], env=env, capture_output=True, text=True, timeout=300)
    j = bac["racine"] / travail / "journal.txt"
    return r.returncode, (j.read_text(encoding="utf-8") if j.exists() else ""), r.stdout + r.stderr


def _commit_source(bac, message: str) -> None:
    _git(bac["source"], "add", "-A")
    _git(bac["source"], "commit", "-qm", message)


def _appels(bac, travail="t") -> list[str]:
    f = bac["racine"] / travail / "appels.txt"
    return f.read_text(encoding="utf-8").splitlines() if f.exists() else []


def test_deux_runs_complets_lecture_precoce_relais(bac):
    distant = _distant(bac)
    code, journal, sortie = _lancer(bac, distant)
    assert code == 0, sortie[-3000:]
    assert journal.count("run source : manifeste et épisodes présents et scellés") == 2
    assert journal.count("run terminé") == 2 and "2 runs prévus, 0 en échec" in journal
    appels = _appels(bac)
    assert len(appels) == 2
    assert "-t05-complement-1-jouet prereg/config-complement-1.json" in appels[0]
    assert "--prereg prereg/complement-1.md" in appels[0] and "donnees/t05-taches-1/taches.json" in appels[0]
    assert "-t05-complement-2-jouet prereg/config-complement-2.json" in appels[1]
    assert "--prereg prereg/complement-2.md" in appels[1] and "donnees/t05-taches-2/taches.json" in appels[1]
    progres = [x for x in journal.splitlines() if x.startswith("PROGRES ")]
    assert progres == ["PROGRES 2026-10-27T10:00:00Z juge=8B lot=1/3 duree_s=344.1"] * 2
    assert "PROPOSAL" not in journal and "texte libre" not in journal and '{"run": "factice"}' not in journal
    # délai externe : celui du second run ne dépasse pas celui du premier, et tous deux tiennent sous 400 minutes
    delais = [int(x) for x in re.findall(r"délai externe (\d+) s", journal)]
    assert len(delais) == 2 and 0 < delais[1] <= delais[0] <= 24_000
    log = _git(distant, "log", "--format=%s", BRANCHE)
    assert "run 1" in log and "run 2" in log and "traces de l'instance (fin)" in log


def test_un_seul_run(bac):
    code, journal, sortie = _lancer(bac, _distant(bac), deux=False)
    assert code == 0 and journal.count("run terminé") == 1 and "1 runs prévus, 0 en échec" in journal, sortie[-2000:]
    assert len(_appels(bac)) == 1


def test_premier_run_en_echec_le_second_est_lance(bac):
    distant = _distant(bac)
    code, journal, sortie = _lancer(bac, distant, env_sup={"FAUX_RUN_1": "arret"})
    assert code == 1, sortie[-3000:]
    assert "ARRÊT pendant run" in journal and "run 1/2 en échec, consigné : le run suivant est lancé" in journal
    assert "ARRÊT : échéance globale simulée" in journal                       # diagnostic, hors progression
    assert journal.count("run terminé") == 1 and "2 runs prévus, 1 en échec" in journal
    assert len(_appels(bac)) == 2
    log = _git(distant, "log", "--format=%s", BRANCHE)
    assert "arrêt pendant run" in log and "run 2" in log
    # arrêt du premier run committé et poussé
    fichiers = _git(distant, "ls-tree", "-r", "--name-only", BRANCHE)
    assert re.search(r"diag/\d{8}-\d{6}-t05-complement-1-jouet/arret.json", fichiers)
    assert re.search(r"diag/\d{8}-\d{6}-t05-complement-2-jouet/resume.json", fichiers)


def test_second_run_en_echec(bac):
    code, journal, sortie = _lancer(bac, _distant(bac), env_sup={"FAUX_RUN_2": "arret"})
    assert code == 1 and journal.count("run terminé") == 1 and "2 runs prévus, 1 en échec" in journal, sortie[-2000:]


@pytest.mark.parametrize("artefact, motif", [
    ("doublon", "introuvable ou cité plusieurs fois dans prereg/complement-2.md"),
    ("sceau-absent", "ou son sceau absent"),
    ("sceau-faux", "sceau non conforme parmi les fichiers cités par prereg/complement-2.md"),
    ("prereg-absent", "préenregistrement prereg/complement-2.md absent au commit"),
    ("tests-differents", "tests attendus différents d'un préenregistrement à l'autre"),
    ("tests-doubles", "nombre de tests attendus introuvable ou cité plusieurs fois"),
])
def test_lecture_precoce_du_second_preenregistrement_artefacts(bac, artefact, motif):
    src = bac["source"]
    p2 = src / "prereg" / "complement-2.md"
    if artefact == "doublon":
        p2.write_text(_prereg(2, doublon="Chemin des épisodes du run source"), encoding="utf-8")
    elif artefact == "sceau-absent":
        (src / (_cites(2)["Chemin du manifeste du run source"] + ".sha256")).unlink()
    elif artefact == "sceau-faux":
        (src / _cites(2)["Chemin des épisodes du run source"]).write_text('{"altere": 1}', encoding="utf-8")
    elif artefact == "prereg-absent":
        p2.unlink()
    elif artefact == "tests-differents":
        p2.write_text(_prereg(2, attendus="8"), encoding="utf-8")
    else:
        p2.write_text(_prereg(2) + "- Tests attendus : `7`\n", encoding="utf-8")
    _commit_source(bac, artefact)
    code, journal, sortie = _lancer(bac, _distant(bac))
    assert code == 2 and motif in journal and "arrêt avant l'installation" in journal, sortie[-2000:]
    assert "tests :" not in journal and not _appels(bac)


@pytest.mark.parametrize("env_sup, motif", [
    ({"DELAI_GLOBAL_MIN": "401"}, "DELAI_GLOBAL_MIN=401"),
    ({"DELAI_GLOBAL_MIN": "0"}, "DELAI_GLOBAL_MIN=0"),
    ({"PREREG_1": ""}, "PREREG_1 obligatoire"),
    ({"MODE": "reel", "PREREG_ABSENT": "1"}, "n'est permis qu'en mode jouet"),
])
def test_variables_hors_bornes(bac, env_sup, motif):
    code, journal, sortie = _lancer(bac, _distant(bac), env_sup=env_sup)
    assert code == 2 and motif in sortie and not _appels(bac), sortie[-2000:]


def test_mode_jouet_sans_preenregistrement(bac):
    env = {"PREREG_ABSENT": "1", "PREREG_1": "", "CONFIG_1": "prereg/config-complement-1.json",
           "TACHES_1": "donnees/t05-taches-1/taches.json", "CONFIG_2": "prereg/config-complement-2.json",
           "TACHES_2": "donnees/t05-taches-2/taches.json"}
    code, journal, sortie = _lancer(bac, _distant(bac), env_sup=env, deux=False)
    assert code == 0 and journal.count("répétition sans préenregistrement") == 2, sortie[-2000:]
    assert journal.count("run terminé") == 2 and all("--prereg" not in a for a in _appels(bac))


@pytest.mark.parametrize("ligne, attendu", [("7 passed in 1.00s", 0), ("7 passed, 1 skipped in 1.00s", 1),
                                            ("6 passed in 1.00s", 1)])
def test_derniere_ligne_des_tests(bac, ligne, attendu):
    code, journal, sortie = _lancer(bac, _distant(bac), env_sup={"FAUX_PYTEST_LIGNE": ligne})
    assert code == attendu, sortie[-2000:]
    assert bool(_appels(bac)) == (attendu == 0)


def test_branche_presente_arrete(bac):
    distant = _distant(bac)
    subprocess.run(["git", "-C", str(distant), "branch", "-f", BRANCHE, "main"], check=True)
    code, journal, _ = _lancer(bac, distant)
    assert code == 2 and "déjà présente" in journal and not _appels(bac)
