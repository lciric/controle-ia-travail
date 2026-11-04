"""Script d'instance et amorce du pilote de l'exposant p, v2 (`scripts/pilote_exposant_p_instance_v2.sh`,
`scripts/amorce_instance_pilote_exposant_p_v2.sh`) : exécutés tels quels contre un dépôt distant local, avec un `python`
et un `nvidia-smi` factices (aucune installation, aucune carte). Déclinés de `tests/test_script_p3.py` (contre-lecture
R2, B6 : aucun essai ne couvrait le script du pilote). Chaque garde sur un cas sain et sur un artefact (R5) : lecture
précoce des citations, marqueurs restants en mode reel, branche présente, dernière ligne des essais, run arrêté,
révisions transmises au lanceur, amorce (vérification du GO avant toute création et sur l'instance avant toute
installation, dossiers présents, plafond atteint)."""
from __future__ import annotations

import os
import shutil
import subprocess
from datetime import date, timedelta
from pathlib import Path

import pytest

from controle_ia.scellement import sceller

RACINE = Path(__file__).resolve().parents[1]
SCRIPT = RACINE / "scripts" / "pilote_exposant_p_instance_v2.sh"
AMORCE = RACINE / "scripts" / "amorce_instance_pilote_exposant_p_v2.sh"
MODULES = ("__init__.py", "gardes.py", "scellement.py")
MODULES_V2 = ("__init__.py", "go.py")
ENV_DE_BASE = ("PATH", "LANG", "LC_ALL", "LC_CTYPE", "TMPDIR")
PREREG = "prereg/pilote-exposant-p-v1.md"
CONFIG = "brouillons/pilote-exposant-p-v1/config.json"
STIMULI = "brouillons/pilote-exposant-p-v1/stimuli.json"
BRANCHE = "calcul/pilote-exposant-p-jouet-v2"
PROGRES = "PROGRES 2026-11-04T10:00:00Z etape=lu_:_plan_(E,_R) famille=ER plan=E×R s=0 p=2.100 duree_s=14.9"

PYTHON_FACTICE = """#!/usr/bin/env bash
if [ "$1" = "-m" ] && [ "$2" = "pytest" ]; then printf '%s\\n' "${FAUX_PYTEST_LIGNE:-9 passed in 1.00s}"; exit 0; fi
if [ "$1" = "-m" ] && [ "$2" = "pip" ]; then echo "paquet-factice==1.0"; exit 0; fi
if [ "$1" = "-" ]; then cat >/dev/null; echo '{"modele": "m", "revision": "abc", "acces": true}'; exit 0; fi
if [ "$1" = "-c" ]; then
    case "$2" in *"is_available() else 1"*) exit "${FAUX_CARTE_CODE:-0}" ;; esac
    echo "torch factice"; exit 0
fi
if [ "$1" = "-m" ] && [ "$2" = "controle_ia.pilote_exposant_p_v2.run" ]; then
    run=""; prec=""
    for a in "$@"; do [ "$prec" = "--run-id" ] && run="$a"; prec="$a"; done
    echo "$*" > "$TRAVAIL/arguments-run.txt"
    mkdir -p "diag/$run" "runs/$run"
    echo '{"factice": true}' > "runs/$run/manifeste.json"
    echo "__PROGRES__" >&2
    echo "PROGRES 2026-11-04T10:00:01Z texte libre interdit" >&2
    if [ "${FAUX_RUN:-complet}" = complet ]; then
        echo '{"factice": true}' > "diag/$run/resume.json"; echo '{"run": "factice"}'; exit 0
    fi
    if [ "${FAUX_RUN}" = instrument ]; then
        echo '{"issue": "instrument non validé"}' > "diag/$run/resume.json"; exit 3
    fi
    echo '{"factice": true}' > "diag/$run/arret.json"; echo "ARRÊT : plafond simulé" >&2; exit 1
fi
echo "appel inattendu : $*" >&2; exit 3
""".replace("__PROGRES__", PROGRES)


def _git(d: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(d), *args], capture_output=True, text=True, check=True).stdout.strip()


def _prereg(doublon: str | None = None, marqueur: bool = False) -> str:
    lignes = ["# préenregistrement factice du pilote v2", "- Tests attendus : `9`",
              f"- Chemin de la configuration du pilote : `{CONFIG}`", f"- Chemin des stimuli du pilote : `{STIMULI}`"]
    if doublon:
        lignes.append(f"- {doublon} : `autre/chemin.json`")
    if marqueur:
        lignes.append("- Addendum R9-bis : <<DOI_R9_BIS>>")
    return "\n".join(lignes) + "\n"


def _resceller(chemin: Path, texte: str) -> None:
    """Fichier d'essai réécrit dans le dépôt jetable : son ancien sceau est retiré avant le nouveau (R12 vaut pour les
    fichiers du programme, pas pour ce bac à sable)."""
    Path(str(chemin) + ".sha256").unlink()
    chemin.write_text(texte, encoding="utf-8")
    sceller(chemin)


def _registre(go_id: str = "GO-2026-11-04-03", typ: str = "calcul", plafond: str = "30 USD",
              debut: date | None = None, fin: date | None = None, revoque: bool = False) -> str:
    j = date.today()
    debut, fin = debut or j - timedelta(days=1), fin or j + timedelta(days=10)
    t = ["# Registre des GO", "", "| id | accordé le | type | périmètre | plafond | échéance | accordé par | référence |",
         "|---|---|---|---|---|---|---|---|",
         f"| {go_id} | {debut} | {typ} | **Pilote de l'exposant p** (essai) | {plafond} | {fin} | Lazar | essai |"]
    if revoque:
        t.append(f"| GO-2000-01-01-01 | {debut} | révocation | {go_id} révoqué (essai) | — | {fin} | Lazar | essai |")
    return "\n".join(t) + "\n"


@pytest.fixture
def bac(tmp_path):
    src = tmp_path / "source"
    (src / "prereg").mkdir(parents=True)
    _git(tmp_path, "init", "-q", "-b", "main", str(src))
    _git(src, "config", "user.email", "t@example.invalid")
    _git(src, "config", "user.name", "t")
    for d in ("runs", "diag", "registres"):
        (src / d).mkdir(exist_ok=True)
        (src / d / ".gitkeep").write_text("", encoding="utf-8")
    (src / "registres" / "go.md").write_text(_registre(), encoding="utf-8")
    (src / PREREG).write_text(_prereg(), encoding="utf-8")
    for chemin in (CONFIG, STIMULI):
        f = src / chemin
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text('{"modeles": {"lu": "m"}}', encoding="utf-8")
        sceller(f)
    sceller(src / PREREG)
    (src / "src" / "controle_ia" / "pilote_exposant_p_v2").mkdir(parents=True)
    for nom in MODULES:
        shutil.copy(RACINE / "src" / "controle_ia" / nom, src / "src" / "controle_ia" / nom)
    for nom in MODULES_V2:
        shutil.copy(RACINE / "src" / "controle_ia" / "pilote_exposant_p_v2" / nom,
                    src / "src" / "controle_ia" / "pilote_exposant_p_v2" / nom)
    (src / "scripts").mkdir()
    for s in (SCRIPT, AMORCE):
        shutil.copy(s, src / "scripts" / s.name)
    _git(src, "add", "-A")
    _git(src, "commit", "-qm", "init")
    venv = tmp_path / "venv"
    (venv / "bin").mkdir(parents=True)
    (venv / "bin" / "activate").write_text(f'export PATH="{venv}/bin:$PATH"\n', encoding="utf-8")
    for nom, texte in (("python", PYTHON_FACTICE), ("nvidia-smi", "#!/usr/bin/env bash\necho 'A100, 580, 81920 MiB'\n"),
                       ("pip", "#!/usr/bin/env bash\nexit 0\n")):
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
    assert f"stimuli {STIMULI} : présents et scellés" in journal and f"BRANCHE={BRANCHE}" in journal
    assert "run terminé" in journal and "(v2)" in journal
    assert [x for x in journal.splitlines() if x.startswith("PROGRES ")] == [PROGRES]   # texte libre filtré
    args = (bac["racine"] / "t" / "arguments-run.txt").read_text(encoding="utf-8")
    assert "--prereg" in args and "--jouet" in args and "--revisions" not in args       # révisions : mode reel seul
    assert "run" in _git(distant, "log", "-2", "--format=%s", BRANCHE)


@pytest.mark.parametrize("artefact, motif", [
    ("doublon", "introuvable ou cité plusieurs fois"),
    ("sceau-absent", "ou son sceau absent"),
    ("sceau-faux", "sceau non conforme"),
    ("prereg-absent", "absent au commit"),
])
def test_lecture_precoce_artefacts(bac, artefact, motif):
    src = bac["source"]
    if artefact == "doublon":
        _resceller(src / PREREG, _prereg(doublon="Chemin des stimuli du pilote"))
    elif artefact == "sceau-absent":
        (src / (STIMULI + ".sha256")).unlink()
    elif artefact == "sceau-faux":
        (src / CONFIG).write_text('{"altere": 1}', encoding="utf-8")
    else:
        (src / PREREG).unlink()
    _commit_source(bac, artefact)
    code, journal, sortie = _lancer(bac, _distant(bac))
    assert code == 2 and motif in journal and "arrêt avant l'installation" in journal, sortie[-2000:]
    assert "essais :" not in journal


def test_marqueurs_restants_en_mode_reel_sain_et_artefact(bac):
    """Mode reel : un marqueur <<…>> (dont <<DOI_R9_BIS>>) dans un fichier cité arrête avant l'installation ; sans
    marqueur, le script passe et transmet les révisions relevées au lanceur (M6)."""
    smi = f"{bac['venv'] / 'bin'}:{os.environ['PATH']}"
    reel = {"MODE": "reel", "HF_TOKEN": "factice", "PATH": smi}
    code, journal, sortie = _lancer(bac, _distant(bac), env_sup=reel)
    assert code == 0, sortie[-3000:]
    assert "--revisions" in (bac["racine"] / "t" / "arguments-run.txt").read_text(encoding="utf-8")
    _resceller(bac["source"] / PREREG, _prereg(marqueur=True))
    _commit_source(bac, "marqueur")
    code, journal, sortie = _lancer(bac, _distant(bac), travail="t2", env_sup=dict(reel, BRANCHE="calcul/x-v3"))
    assert code == 2 and "marqueurs restants" in journal and "arrêt avant l'installation" in journal, sortie[-2000:]
    assert "essais :" not in journal


def test_run_arrete_consigne_et_pousse(bac):
    distant = _distant(bac)
    code, journal, _ = _lancer(bac, distant, env_sup={"FAUX_RUN": "arret"})
    assert code == 1 and "ARRÊT pendant run" in journal and f"branche {BRANCHE} poussée" in journal
    assert "ARRÊT : plafond simulé" in journal


def test_instrument_non_valide_code_3_run_complet(bac):
    distant = _distant(bac)
    code, journal, _ = _lancer(bac, distant, env_sup={"FAUX_RUN": "instrument"})
    assert code == 0 and "3 = instrument non validé" in journal and "run terminé" in journal


def test_branche_presente_arrete(bac):
    distant = _distant(bac)
    subprocess.run(["git", "-C", str(distant), "branch", "-f", BRANCHE, "main"], check=True)
    code, journal, _ = _lancer(bac, distant)
    assert code == 2 and "déjà présente" in journal


@pytest.mark.parametrize("ligne, attendu", [("9 passed in 1.00s", 0), ("8 passed in 1.00s", 1),
                                            ("9 passed, 1 skipped in 1.00s", 1)])
def test_derniere_ligne_des_essais(bac, ligne, attendu):
    code, journal, sortie = _lancer(bac, _distant(bac), env_sup={"FAUX_PYTEST_LIGNE": ligne})
    assert code == attendu, sortie[-2000:]
    if attendu:
        assert "≠ « 9 passed »" in journal and "run :" not in journal


# --- amorce ---------------------------------------------------------------------------------------------------

def _amorce(bac, env_sup: dict, racine_nom: str = "amorce"):
    racine = bac["racine"] / racine_nom
    racine.mkdir(exist_ok=True)
    env = _env(bac, _distant(bac), "inutile", {"RACINE_AMORCE": str(racine), "GH_TOKEN": "x", "HF_TOKEN": "y",
                                               "GO_ID": "GO-2026-11-04-03", "REF_GO": "main"})
    env.pop("TRAVAIL")
    env.update(env_sup)
    r = subprocess.run(["bash", str(AMORCE)], env=env, capture_output=True, text=True, timeout=300)
    return r, racine


@pytest.mark.parametrize("registre, attendu, motif", [
    (_registre(), 0, "vérifié"),
    (_registre(go_id="GO-2026-11-04-04"), 1, "absent du registre"),
    (_registre(typ="décision"), 1, "pas « calcul »"),
    (_registre(plafond="10 USD"), 1, "pire cas du devis"),
    (_registre(fin=date.today() - timedelta(days=1)), 1, "hors de sa période"),
    (_registre(revoque=True), 1, "révoqué"),
])
def test_amorce_verifier_go_avant_creation(bac, tmp_path, registre, attendu, motif):
    """Étape « verifier » (machine de la session, avant toute création d'instance) : cas sain et artefacts."""
    reg = tmp_path / "go.md"
    reg.write_text(registre, encoding="utf-8")
    r, _ = _amorce(bac, {"AMORCE_ETAPE": "verifier", "REGISTRE_GO": str(reg)})
    assert r.returncode == attendu and motif in r.stdout, r.stdout + r.stderr


def test_amorce_instance_cas_sain_et_dossiers_presents(bac):
    r, racine = _amorce(bac, {})
    assert r.returncode == 0 and "fin, code 0" in r.stdout, (r.stdout + r.stderr)[-3000:]
    assert PROGRES in r.stdout
    r, _ = _amorce(bac, {})
    assert r.returncode == 1 and "dossiers d'un essai précédent présents (R12)" in r.stdout


def test_amorce_instance_go_invalide_arrete_avant_installation(bac):
    (bac["source"] / "registres" / "go.md").write_text(_registre(plafond="5 USD"), encoding="utf-8")
    _commit_source(bac, "plafond trop bas")
    r, racine = _amorce(bac, {})
    assert r.returncode == 1 and "arrêt avant toute installation" in r.stdout, r.stdout + r.stderr
    assert not (racine / "pilote-exposant-p").exists()                 # le script d'instance n'a pas tourné


TIMEOUT_FACTICE = """#!/usr/bin/env bash
# plafond de l'amorce (630m) : la commande tourne, puis le plafond rend 124 sans rien tuer d'autre ; autres délais : vrai
for a in "$@"; do [ "$a" = "630m" ] && plafond=1; done
[ -n "${plafond:-}" ] || exec __VRAI__ "$@"
while [ "${1#-}" != "$1" ]; do shift; done
shift
"$@"
exit 124
"""


def test_amorce_plafond_atteint_pousse_resultats_partiels(bac):
    faux = bac["racine"] / "faux-bin"
    faux.mkdir()
    vrai = shutil.which("timeout")
    assert vrai
    (faux / "timeout").write_text(TIMEOUT_FACTICE.replace("__VRAI__", vrai), encoding="utf-8")
    (faux / "timeout").chmod(0o755)
    r, _ = _amorce(bac, {"PATH": f"{faux}:{os.environ['PATH']}"}, racine_nom="amorce-plafond")
    assert r.returncode == 124 and "fin, code 124" in r.stdout, (r.stdout + r.stderr)[-3000:]
    distant = sorted(bac["racine"].glob("distant-*.git"))[-1]
    assert "plafond de l'amorce atteint" in _git(distant, "log", "-1", "--format=%s", BRANCHE)
    dernier = _git(distant, "show", "--name-only", "--format=", BRANCHE).splitlines()
    assert any(f.startswith("traces/pilote-exposant-p-plafond-") and f.endswith("/journal.txt") for f in dernier)
