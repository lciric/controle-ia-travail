"""Essai à blanc de l'amorce entière de la formation du barreau 5 (`scripts/amorce_b5f_formation_v1.sh`), hors ligne
(constat M-9, point 10, de la contre-lecture du code de formation ; écrit le 19 novembre 2026).

L'amorce est jouée de bout en bout (étapes 0 à 8) sous `AMORCE_ESSAI_BLANC=1`, avec ses vraies gardes et de faux outils :
- `git` vrai, sur un dépôt distant local (nu) que l'URL officielle désigne par `url.<chemin>.insteadOf` ;
- faux `curl` (journal des demandes, réponse 200), faux `nvidia-smi` (A100, CUDA 13.0) ;
- faux `python3` (crée un faux environnement virtuel) et faux python de cet environnement (carte vue, essais du paquet
  au compte choisi, descente du modèle, et la marche, remplacée par une fausse marche qui écrit des sorties scellées) ;
- faux `timeout`, qui consigne ses arguments puis appelle le vrai, la durée de la marche raccourcie sur demande.
Ce qui est éprouvé : la minuterie lancée à l'échéance plus le quart d'heure, la porte des essais, la marche sous `timeout`,
le versement périodique et final, la liste blanche à la sortie, la preuve du versement et son témoin, la fin « stopped »,
l'extraction partielle, aucune suppression, aucune valeur de clé écrite. La minuterie, lancée en arrière-plan par l'amorce,
est arrêtée à la fin de chaque essai par son PID, lu au journal (R10)."""
from __future__ import annotations

import hashlib
import os
import re
import shutil
import signal
import subprocess
import time
from pathlib import Path

import pytest

from controle_ia.barreau5_familles import formation_v1 as fv

RACINE_DEPOT = Path(__file__).resolve().parents[1]
AMORCE = RACINE_DEPOT / "scripts" / "amorce_b5f_formation_v1.sh"
TEXTE = AMORCE.read_text(encoding="utf-8")
MIN_ESSAIS = int(re.search(r"^MIN_ESSAIS=(\d+)$", TEXTE, re.M).group(1))
URL = "https://github.com/lciric/controle-ia-travail.git"
RUN = "20261123-080000-b5f-formation-3"
PREREG = "prereg/barreau5-texte-v1.md"
GO = "GO-2026-11-20-01"

FAUX = {
    "curl": '#!/usr/bin/env bash\nprintf "%s\\n" "$*" >> "$JOURNAL_CURL"\nprintf 200\n',
    "nvidia-smi": ('#!/usr/bin/env bash\ncase "$*" in *--query-gpu*) echo "NVIDIA A100-SXM4-80GB, 81920 MiB";;\n'
                   '*) echo "| NVIDIA-SMI 580.00   Driver Version: 580.00   CUDA Version: 13.0 |";; esac\n'),
    "python3": ('#!/usr/bin/env bash\nif [ "${1:-} ${2:-}" = "-m venv" ]; then\n'
                '    mkdir -p "$3/bin" && printf "#!/usr/bin/env bash\\nexit 0\\n" > "$3/bin/pip" \\\n'
                '        && cp "$FAUX_PYTHON_VENV" "$3/bin/python" && chmod +x "$3/bin/pip" "$3/bin/python"; exit $?\n'
                'fi\nexec "$VRAI_PYTHON3" "$@"\n'),
    "timeout": ('#!/usr/bin/env bash\nprintf "%s\\n" "$*" >> "$JOURNAL_TIMEOUT"\na=("$@")\n'
                'case " $* " in *" -m controle_ia.barreau5_familles.formation_v1 "*)\n'
                '    if [ -n "${FAUX_TIMEOUT_S:-}" ]; then for i in "${!a[@]}"; do\n'
                '        case "${a[$i]}" in -*) ;; *) a[$i]="$FAUX_TIMEOUT_S"; break;; esac; done; fi;;\nesac\n'
                'exec "$VRAI_TIMEOUT" "${a[@]}"\n'),
}
PYTHON_VENV = """#!/usr/bin/env bash
case "${1:-}" in
    -c) case "${2:-}" in *cuda*) exit 0;; *precharger_modele*) echo "/cache/modele/revision"; exit 0;; esac; exit 9;;
    -m) case "${2:-}" in
            pytest) echo "$FAUX_PYTEST_LIGNE"; exit "${FAUX_PYTEST_CODE:-0}";;
            controle_ia.barreau5_familles.formation_v1) shift 2; exec bash "$FAUSSE_MARCHE" "$@";;
        esac;;
esac
exit 9
"""
FAUSSE_MARCHE = """#!/usr/bin/env bash
printf '%s\\n' "$*" >> "$JOURNAL_MARCHE"
R=""
while [ $# -gt 0 ]; do case "$1" in --run-id) R="$2"; shift 2;; *) shift;; esac; done
ecrire() { mkdir -p "$(dirname "$1")"; printf '%s' "$2" > "$1"
           (cd "$(dirname "$1")" && sha256sum "$(basename "$1")" > "$(basename "$1").sha256"); }
ecrire "runs/$R/manifeste.json" '{"run_id": "essai"}'
ecrire "diag/$R/mise-en-place.json" '{}'
ecrire "donnees/$R/T05/tirage.jsonl" '{"episode": 1}'
ecrire "donnees/$R/T05/textes-distillation.jsonl" '{"edition": 1}'
[ "${FAUSSE_MARCHE_INTERDIT:-0}" = 1 ] && printf 'x' > "donnees/$R/T05/activations.npy"
sleep "${FAUSSE_MARCHE_S:-0}"
ecrire "donnees/$R/T05/adaptateur-jumeau.pt" 'poids'
ecrire "donnees/$R/T05/evaluation-jumeau.jsonl" '{"cout": 1}'
ecrire "diag/$R/resume.json" '{}'
[ -z "${FAUSSE_MARCHE_EXEC_S:-}" ] || exec sleep "$FAUSSE_MARCHE_EXEC_S"
exit "${FAUSSE_MARCHE_CODE:-0}"
"""


def _git(r, *a):
    return subprocess.run(["git", "-C", str(r), *a], check=True, capture_output=True, text=True).stdout.strip()


@pytest.fixture
def monde(tmp_path):
    """Dépôt distant local (nu) qui porte, sur la branche du code, un arbre de dépôt fabriqué : fichiers que l'amorce
    extrait (textes et tâches fabriqués, l'amorce et le lanceur tels qu'ils sont), et d'autres qu'elle ne doit jamais
    extraire ; faux outils ; configuration de git qui fait désigner ce dépôt par l'URL officielle."""
    nu, graine = tmp_path / "distant.git", tmp_path / "graine"
    subprocess.run(["git", "init", "-q", "--bare", "-b", "main", str(nu)], check=True)
    graine.mkdir()
    for a in (["init", "-q", "-b", "lot/b5f-v1"], ["config", "user.email", "e@invalid"], ["config", "user.name", "e"]):
        _git(graine, *a)
    fichiers = {"requirements-gpu.txt": "-r requirements-cpu.txt\n-r requirements-donnees.txt\n",
                "requirements-cpu.txt": "numpy\n", "requirements-donnees.txt": "\n", "pyproject.toml": "[project]\n",
                "src/controle_ia/__init__.py": "", "tests/conftest.py": "", "tests/test_barreau5_familles_x_v1.py": "",
                fv.CONFIG_SCELLEE["chemin"]: "{}\n", "prereg/P3-consignes-v1.md": "> fabriqué\n", PREREG: "# texte\n",
                PREREG + ".sha256": f"{hashlib.sha256(b'# texte' + bytes([10])).hexdigest()}  barreau5-texte-v1.md\n",
                "prereg/gabarit-preregistrement-v1.md": "# gabarit\n", "registres/barreau5-familles-jumelles-v1.md": "\n",
                "donnees/20261007-082440-t05-extraction/taches-entrainement.json": "{}\n",
                "donnees/20261007-082440-t05-extraction/taches-evaluation.json": "{}\n",
                "docs/sources/invites-2606.08892-v1/index.json": "{}\n",
                "docs/notes/secret.md": "jamais extrait\n", "diag/autre/resultat.json": "{}\n",
                "runs/autre/manifeste.json": "{}\n", "brouillons/note.md": "jamais extrait\n", "README.md": "racine\n",
                "CLAUDE.md": "racine\n"}
    for chemin, contenu in fichiers.items():
        p = graine / chemin
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(contenu, encoding="utf-8")
    for f in (".gitignore", ".gitattributes", "scripts/amorce_b5f_formation_v1.sh", "scripts/lancer_b5f_formation_v1.sh"):
        (graine / f).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(RACINE_DEPOT / f, graine / f)
    _git(graine, "add", "-A")
    _git(graine, "add", "-f", "donnees")
    _git(graine, "commit", "-q", "-m", "code")
    _git(graine, "push", "-q", str(nu), "lot/b5f-v1")
    commit = _git(graine, "rev-parse", "HEAD")
    outils = tmp_path / "outils"
    outils.mkdir()
    for nom, contenu in {**FAUX, "python-venv": PYTHON_VENV, "fausse-marche": FAUSSE_MARCHE}.items():
        (outils / nom).write_text(contenu, encoding="utf-8")
        (outils / nom).chmod(0o755)
    (tmp_path / "gitconfig").write_text(f'[url "{nu}"]\n\tinsteadOf = {URL}\n', encoding="utf-8")
    j = tmp_path / "journaux"
    j.mkdir()
    env = {k: v for k, v in os.environ.items() if not k.startswith(("GIT_", "CONTAINER_", "B5F_", "AMORCE_"))}
    env.update({"PATH": f"{outils}:{os.environ['PATH']}", "HOME": str(tmp_path), "GIT_CONFIG_GLOBAL": str(tmp_path / "gitconfig"),
                "GIT_CONFIG_NOSYSTEM": "1", "AMORCE_ESSAI_BLANC": "1", "RACINE_AMORCE": str(tmp_path / "racine"),
                "B5F_SANS_ATTENTE": "1", "B5F_PAS_MINUTERIE": "1", "B5F_PERIODE_VERSEMENT_S": "2",
                "INSTANCE_B5F": "3", "RELANCE_B5F": "0", "COMMIT": commit, "BRANCHE_CODE": "lot/b5f-v1", "PREREG": PREREG,
                "RUN_B5F": RUN, "PRIX_USD_H": "1.2", "GO_ID": GO, "DEPOT_URL": URL,
                "GH_TOKEN": "valeur-factice-gh", "HF_TOKEN": "valeur-factice-hf", "CONTAINER_ID": "4242",
                "CONTAINER_API_KEY": "cle-factice-api", "JOURNAL_CURL": str(j / "curl.txt"),
                "JOURNAL_TIMEOUT": str(j / "timeout.txt"), "JOURNAL_MARCHE": str(j / "marche.txt"),
                "FAUX_PYTHON_VENV": str(outils / "python-venv"), "FAUSSE_MARCHE": str(outils / "fausse-marche"),
                "VRAI_PYTHON3": shutil.which("python3"), "VRAI_TIMEOUT": shutil.which("timeout"),
                "FAUX_PYTEST_LIGNE": f"{MIN_ESSAIS} passed in 1.00s", "FAUX_PYTEST_CODE": "0", "FAUSSE_MARCHE_S": "7"})
    return {"env": env, "nu": nu, "commit": commit, "journaux": j, "T": tmp_path / "racine" / "b5f-formation-v1"}


def _jouer_l_amorce(monde, **sup) -> dict:
    """Joue l'amorce entière ; arrête ensuite la minuterie par son PID, lu au journal (R10). Rend code, sorties, journal."""
    env = dict(monde["env"])
    env["ECHEANCE_ARRET_UTC_S"] = str(int(time.time()) + 600)
    env.update({k: v for k, v in sup.items() if v is not None})
    t = monde["T"]
    sortie, erreurs = monde["journaux"] / "amorce.out", monde["journaux"] / "amorce.err"
    with open(sortie, "w") as fo, open(erreurs, "w") as fe:
        p = subprocess.Popen(["bash", str(AMORCE)], env=env, stdout=fo, stderr=fe, stdin=subprocess.DEVNULL)
        try:
            code = p.wait(timeout=240)
        finally:
            journal = (t / "traces" / "journal-b5f.txt").read_text() if (t / "traces" / "journal-b5f.txt").exists() else ""
            for pid in re.findall(r"minuterie lancée \(PID (\d+)", journal):
                try:
                    os.kill(int(pid), signal.SIGTERM)
                except ProcessLookupError:
                    pass
            if p.poll() is None:
                os.kill(p.pid, signal.SIGTERM)
    lire = lambda n: (monde["journaux"] / n).read_text() if (monde["journaux"] / n).exists() else ""  # noqa: E731
    return {"code": code, "journal": journal, "echeance": int(env["ECHEANCE_ARRET_UTC_S"]), "sortie": sortie.read_text(),
            "erreurs": erreurs.read_text(), "curl": lire("curl.txt"), "timeout": lire("timeout.txt"),
            "marche": lire("marche.txt"), "D": t / "depot", "T": t}


def _branche(monde, nom="donnees/barreau5-familles-jumelles-v1-formation-instance-3"):
    tete = subprocess.run(["git", "-C", str(monde["nu"]), "rev-parse", "--verify", "-q", nom], capture_output=True,
                          text=True).stdout.strip()
    fichiers = _git(monde["nu"], "ls-tree", "-r", "--name-only", tete).split() if tete else []
    messages = _git(monde["nu"], "log", "--format=%s", tete).splitlines() if tete else []
    return tete, fichiers, messages


def _prouve_et_ancetre(monde, r, tete):
    """Le témoin porte le commit prouvé : un commit de la branche de sortie, ancêtre de sa tête (le journal de fin est
    poussé après la preuve), dont l'inventaire final liste chaque fichier à sa taille et à son empreinte."""
    prouve = (r["T"] / "versement-final-prouve").read_text().strip()
    assert subprocess.run(["git", "-C", str(monde["nu"]), "merge-base", "--is-ancestor", prouve, tete]).returncode == 0
    inventaire = _git(monde["nu"], "show", f"{prouve}:traces-b5f/inventaire-final.json")
    for chemin, octets, empreinte in re.findall(r'"chemin": "([^"]+)", "octets": (\d+), "sha256": "([0-9a-f]{64})"',
                                                inventaire):
        contenu = subprocess.run(["git", "-C", str(monde["nu"]), "show", f"{prouve}:{chemin}"], capture_output=True).stdout
        assert len(contenu) == int(octets) and hashlib.sha256(contenu).hexdigest() == empreinte, chemin


def test_amorce_entiere_nominale_porte_marche_sous_timeout_versement_preuve_et_fin_sans_destruction(monde):
    r = _jouer_l_amorce(monde)
    assert r["code"] == 0, r["journal"] + r["erreurs"]
    # minuterie à l'échéance plus le quart d'heure du versement (mutation M14)
    assert f"minuterie : échéance {r['echeance'] + 900} " in r["journal"]
    # porte des essais passée, marche lancée sous timeout jusqu'à l'échéance d'arrêt (mutation M21)
    assert f"essais du paquet : code 0, ligne de compte : {MIN_ESSAIS} passed" in r["journal"]
    ligne = next(x for x in r["timeout"].splitlines() if "-m controle_ia.barreau5_familles.formation_v1" in x)
    duree = int(re.search(r"--signal=TERM --kill-after=120 (\d+) ", ligne).group(1))
    assert 60 <= duree <= 600
    assert f"--instance 3 --relance 0 --prix-usd-h 1.2 --go-id {GO} --run-id {RUN} --prereg {PREREG}" in r["marche"]
    # extraction partielle : ni docs/notes, ni diag, runs, brouillons d'autres courses, ni fichiers de la racine non nommés
    d = r["D"]
    for absent in ("docs/notes", "diag/autre", "runs/autre", "brouillons", "README.md", "CLAUDE.md"):
        assert not (d / absent).exists(), absent
    assert (d / "requirements-gpu.txt").is_file() and (d / PREREG).is_file()
    # versement périodique pendant la marche, puis final ; preuve et témoin ; rien de supprimé (mutation M07)
    tete, fichiers, messages = _branche(monde)
    assert any("sorties scellées" in m for m in messages) and any("inventaire final" in m for m in messages)
    for f in ("tirage.jsonl", "textes-distillation.jsonl", "adaptateur-jumeau.pt", "evaluation-jumeau.jsonl"):
        assert f"donnees/{RUN}/T05/{f}" in fichiers and f"donnees/{RUN}/T05/{f}.sha256" in fichiers
        assert (d / "donnees" / RUN / "T05" / f).is_file(), f
    assert {f"runs/{RUN}/manifeste.json", f"diag/{RUN}/resume.json", "traces-b5f/journal/journal-b5f.txt",
            "traces-b5f/inventaire-final.json"} <= set(fichiers)
    _prouve_et_ancetre(monde, r, tete)
    assert any("journal de fin" in m for m in messages)
    # fin : « stopped » demandé par l'identifiant ; aucune destruction par l'amorce ; aucune valeur de clé écrite
    assert "-X PUT" in r["curl"] and '"state": "stopped"' in r["curl"] and "/instances/4242/" in r["curl"]
    assert "DELETE" not in r["curl"]
    for valeur in ("valeur-factice-gh", "valeur-factice-hf", "cle-factice-api"):
        assert valeur not in r["journal"] + r["sortie"] + r["erreurs"]


@pytest.mark.parametrize("ligne, code", [("3 failed, {n} passed in 1.00s", "1"), ("{m} passed in 1.00s", "0")])
def test_amorce_entiere_porte_des_essais_fermee_aucune_marche(monde, ligne, code):
    """Mutation M15 : essais du paquet en échec, ou moins de MIN_ESSAIS passés : arrêt (code 2) avant toute marche ;
    les traces sont versées."""
    r = _jouer_l_amorce(monde, FAUX_PYTEST_LIGNE=ligne.format(n=MIN_ESSAIS, m=MIN_ESSAIS - 1), FAUX_PYTEST_CODE=code)
    assert r["code"] == 2 and "essais du paquet en échec ou moins de" in r["journal"], r["journal"]
    assert r["marche"] == "" and "formation_v1" not in r["timeout"]
    _, fichiers, _ = _branche(monde)
    assert "traces-b5f/journal/journal-b5f.txt" in fichiers


def test_amorce_entiere_echeance_atteinte_marche_coupee_par_timeout_sorties_versees(monde):
    """La marche qui dépasse son échéance est coupée par `timeout` (code 124) : arrêt écrit (code 3), sorties déjà
    écrites versées, versement prouvé."""
    r = _jouer_l_amorce(monde, FAUX_TIMEOUT_S="3", FAUSSE_MARCHE_S="0", FAUSSE_MARCHE_EXEC_S="60")
    assert r["code"] == 3 and "échéance d'arrêt atteinte" in r["journal"], r["journal"]
    tete, fichiers, _ = _branche(monde)
    assert f"donnees/{RUN}/T05/adaptateur-jumeau.pt" in fichiers
    _prouve_et_ancetre(monde, r, tete)


def test_amorce_entiere_sortie_hors_liste_blanche_gardee_sur_le_disque_versement_non_prouve(monde):
    """Liste d'arrêt, point 5, et règle « récupérer ce qui est récupérable » : un fichier hors de la liste blanche ne sort
    pas de l'instance, reste sur le disque, noté ; le versement n'est pas prouvé (code 5), aucun témoin : la minuterie
    arrêterait l'instance sans la détruire."""
    r = _jouer_l_amorce(monde, FAUSSE_MARCHE_INTERDIT="1")
    assert r["code"] == 5 and "hors de la liste blanche" in r["journal"] and "NON PROUVÉ" in r["journal"], r["journal"]
    _, fichiers, _ = _branche(monde)
    assert f"donnees/{RUN}/T05/activations.npy" not in fichiers
    assert f"donnees/{RUN}/T05/adaptateur-jumeau.pt" in fichiers
    assert (r["D"] / "donnees" / RUN / "T05" / "activations.npy").is_file()
    assert not (r["T"] / "versement-final-prouve").exists()


def test_amorce_entiere_cle_recue_comme_nom_refusee_avant_tout_clonage(monde):
    """Constat M-1, côté instance : si le loueur reçoit le texte « $HF_TOKEN » au lieu de la valeur, l'amorce s'arrête à la
    vérification de la machine (code 2), avant tout clonage, sans écrire la valeur reçue."""
    r = _jouer_l_amorce(monde, HF_TOKEN="$HF_TOKEN")
    assert r["code"] == 2 and "un nom de variable reçu à la place d'une valeur" in r["journal"], r["journal"]
    assert not (r["D"] / ".git").exists() and r["marche"] == ""


def test_amorce_entiere_relance_branche_et_marche_suffixees(monde):
    """Constat M-5 : la relance pousse sur la branche …-instance-3-x1 et passe « --relance 1 » à la marche."""
    r = _jouer_l_amorce(monde, RELANCE_B5F="1", RUN_B5F=RUN + "-x1", FAUSSE_MARCHE_S="0")
    assert r["code"] == 0, r["journal"]
    assert "--relance 1" in r["marche"] and f"--run-id {RUN}-x1" in r["marche"]
    tete, fichiers, _ = _branche(monde, fv.branche_sortie(3, True))
    assert tete and f"donnees/{RUN}-x1/T05/tirage.jsonl" in fichiers
    assert _branche(monde)[0] == ""
