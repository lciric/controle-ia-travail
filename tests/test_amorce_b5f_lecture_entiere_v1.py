"""Essai à blanc de l'amorce entière de l'instance de lecture du barreau 5 (`scripts/amorce_b5f_lecture_v1.sh`), hors ligne,
écrit le 20 novembre 2026 sur le modèle de `tests/test_amorce_b5f_formation_entiere_v1.py`.

L'amorce est jouée de bout en bout sous `AMORCE_ESSAI_BLANC=1`, avec ses vraies gardes et de faux outils : `git` vrai, sur
des dépôts distants locaux que l'URL officielle désigne (`url.<chemin>.insteadOf`) ; faux `curl` (journal, réponse 200) ;
faux `nvidia-smi` (A100, CUDA 13.0) ; faux `python3` (faux environnement virtuel) et faux interpréteur de cet environnement
(essais au compte choisi, descente du modèle, configuration, liste des activations gardées, et une fausse marche qui écrit
des sorties scellées) ; faux `timeout`, qui consigne ses arguments puis appelle le vrai. L'échéance d'arrêt est fixée à
65 secondes (la plus courte que l'amorce admet), le quart d'heure du versement à une seconde, et la minuterie ne fait qu'une
demande à l'échéance (essai à blanc seulement) : chaque essai attend donc une minute environ, et aucune minuterie ne reste
en vie, sans aucun signal envoyé par l'essai."""
from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import time
from pathlib import Path

import pytest

from controle_ia.barreau5_familles import relecture_v1 as rv

RACINE_DEPOT = Path(__file__).resolve().parents[1]
AMORCE = RACINE_DEPOT / "scripts" / "amorce_b5f_lecture_v1.sh"
TEXTE = AMORCE.read_text(encoding="utf-8")
MIN_ESSAIS = int(next(x for x in TEXTE.splitlines() if x.startswith("MIN_ESSAIS=")).split("=")[1].split()[0])
URL = "https://github.com/lciric/controle-ia-travail.git"
RUN = "20261124-120000-b5f-lecture"
PREREG = "prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md"
CLES = ("valeur-factice-gh", "valeur-factice-hf", "cle-factice-api")

FAUX = {
    "curl": '#!/usr/bin/env bash\nprintf "%s\\n" "$*" >> "$JOURNAL_CURL"\nprintf 200\n',
    "nvidia-smi": ('#!/usr/bin/env bash\ncase "$*" in *--query-gpu*) echo "NVIDIA A100-SXM4-80GB, 81920 MiB";;\n'
                   '*) echo "| NVIDIA-SMI 580.00   Driver Version: 580.00   CUDA Version: 13.0 |";; esac\n'),
    "python3": ('#!/usr/bin/env bash\nif [ "${1:-} ${2:-}" = "-m venv" ]; then\n'
                '    mkdir -p "$3/bin" && printf "#!/usr/bin/env bash\\nexit 0\\n" > "$3/bin/pip" \\\n'
                '        && cp "$FAUX_PYTHON_VENV" "$3/bin/python" && chmod +x "$3/bin/pip" "$3/bin/python"; exit $?\n'
                'fi\nexec "$VRAI_PYTHON3" "$@"\n'),
    "timeout": '#!/usr/bin/env bash\nprintf "%s\\n" "$*" >> "$JOURNAL_TIMEOUT"\nexec "$VRAI_TIMEOUT" "$@"\n',
}
PYTHON_VENV = """#!/usr/bin/env bash
case "${1:-} ${2:-}" in
    "-m pytest") echo "$FAUX_PYTEST_LIGNE"; exit "${FAUX_PYTEST_CODE:-0}";;
    "-m controle_ia.barreau5_familles.relecture_v1")
        case "${3:-}" in
            session) case "${4:-}" in
                    precharger) echo "/cache/modele/revision"; exit 0;;
                    config) printf '%s\\n' "$*" >> "$JOURNAL_CONFIG"; echo '{"config": "fausse"}'; exit 0;;
                    gardees) find "$5/activations" -type f -name '*.npy' | LC_ALL=C sort | head -n "${FAUX_GARDEES_N:-3}"; exit 0;;
                esac; exit 9;;
            --config) shift 2; exec bash "$FAUSSE_MARCHE" "$@";;
        esac; exit 9;;
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
for s in nu X-01 A1-sur_saboteur X-02; do
    mkdir -p "donnees/$R/activations/$s/c15"; printf 'a%.0s' $(seq 100) > "donnees/$R/activations/$s/c15/e0__p0.npy"; done
ecrire "donnees/$R/lecture/bilan-relecture.json" '{}'
ecrire "donnees/$R/lecture/scores/decisive-pli0.json" '{"statut": "notee"}'
ecrire "donnees/$R/lecture/jetons/decisive-pli0/X-01.json" '{"jetons": {}}'
ecrire "donnees/$R/lecture/inventaire.json" '{"format": "b5f-inventaire-lecture-v1"}'
ecrire "donnees/$R/poids/decisive-pli0.json" '{}'
ecrire "donnees/$R/garde-activations.json" '{}'
ecrire "donnees/$R/inventaire-activations.json" '{}'
ecrire "diag/$R/resume.json" '{}'
echo '{"inventaire_sha256": "fausse"}'
exit "${FAUSSE_MARCHE_CODE:-0}"
"""


def _git(r, *a):
    return subprocess.run(["git", "-C", str(r), *a], check=True, capture_output=True, text=True).stdout.strip()


def _graine(chemin: Path, branche: str) -> Path:
    chemin.mkdir()
    for a in (["init", "-q", "-b", branche], ["config", "user.email", "e@invalid"], ["config", "user.name", "e"]):
        _git(chemin, *a)
    return chemin


@pytest.fixture
def monde(tmp_path):
    """Dépôt distant local : branche du code (fichiers que l'amorce extrait, et d'autres qu'elle ne doit jamais extraire, dont
    une marche de la formation et les tâches de réserve) ; branche des entrées de lecture, leur dossier ajouté en un seul
    commit (ou, sur demande, en deux) ; faux outils ; configuration de git qui fait désigner ce dépôt par l'URL officielle."""
    nu = tmp_path / "distant.git"
    subprocess.run(["git", "init", "-q", "--bare", "-b", "main", str(nu)], check=True)
    g = _graine(tmp_path / "graine", "lot/b5f-lecture-v1")
    fichiers = {"requirements-gpu.txt": "-r requirements-cpu.txt\n-r requirements-donnees.txt\n",
                "requirements-cpu.txt": "numpy\n", "requirements-donnees.txt": "\n", "pyproject.toml": "[project]\n",
                "src/controle_ia/__init__.py": "", "tests/conftest.py": "",
                "tests/test_barreau5_familles_lecture_v1.py": "", "tests/test_barreau5_familles_sondes_v1.py": "",
                "tests/test_barreau5_familles_relecture_v1.py": "", "tests/test_barreau5_familles_formation_v1.py": "",
                rv.CONFIG_SCELLEE["chemin"]: "{}\n", PREREG: "# texte\n", "prereg/P3-consignes-v1.md": "> fabriqué\n",
                "registres/barreau5-familles-jumelles-v1.md": "\n",
                "donnees/20261007-082440-t05-extraction/taches-evaluation.json": "{}\n",
                "donnees/20261007-082440-t05-extraction/taches-entrainement.json": "{}\n",
                "donnees/20261122-101010-b5f-formation-1/T01/evaluation-jumeau.jsonl": "{\"cout\": 1}\n",
                "docs/sources/invites-2606.08892-v1/index.json": "{}\n", "docs/notes/secret.md": "jamais extrait\n",
                "diag/autre/resultat.json": "{}\n", "runs/autre/manifeste.json": "{}\n", "brouillons/note.md": "x\n",
                "README.md": "racine\n"}
    for chemin, contenu in fichiers.items():
        (g / chemin).parent.mkdir(parents=True, exist_ok=True)
        (g / chemin).write_text(contenu, encoding="utf-8")
    for f in (".gitignore", ".gitattributes", "scripts/amorce_b5f_lecture_v1.sh", "scripts/lancer_b5f_lecture_v1.sh"):
        (g / f).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(RACINE_DEPOT / f, g / f)
    _git(g, "add", "-A")
    _git(g, "add", "-f", "donnees")
    _git(g, "commit", "-q", "-m", "code")
    _git(g, "push", "-q", str(nu), "lot/b5f-lecture-v1")
    commit = _git(g, "rev-parse", "HEAD")

    def entrees(en_deux=False):
        e = _graine(tmp_path / f"entrees-graine-{int(en_deux)}", "x")
        (e / "LISEZ-MOI").write_text("base\n")
        _git(e, "add", "-A")
        _git(e, "commit", "-q", "-m", "base")
        d = e / rv.DOSSIER_ENTREES
        d.mkdir()
        for n in ("X-01.safetensors", "A1-saboteur.safetensors"):
            (d / n).write_bytes(n.encode())
            if en_deux:
                _git(e, "add", "-A")
                _git(e, "commit", "-q", "-m", f"versement de {n}")
        _git(e, "add", "-A")
        if not en_deux:
            _git(e, "commit", "-q", "-m", "entrées de lecture")
        _git(e, "push", "-q", "-f", str(nu), f"x:refs/heads/{rv.BRANCHE_ENTREES}")
        return _git(e, "rev-parse", "HEAD")
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
                "B5F_SANS_ATTENTE": "1", "B5F_PAS_MINUTERIE": "1", "B5F_VERSEMENT_S": "1", "B5F_MINUTERIE_UNE_FOIS": "1",
                "PLAN_B5F": "decisif", "COMMIT": commit, "BRANCHE_CODE": "lot/b5f-lecture-v1", "PREREG": PREREG,
                "RUN_LECTURE": RUN, "PRIX_USD_H": "1.2", "GO_ID": "GO-2026-11-24-01", "DEPOT_URL": URL,
                "DIVERGENCE_B5F": "1", "GARDE_B5F": "une_sur_dix", "EXISTANTS_B5F": "W10=", "EXISTANTS_CHEMINS": "-",
                "GH_TOKEN": CLES[0], "HF_TOKEN": CLES[1], "CONTAINER_ID": "4242", "CONTAINER_API_KEY": CLES[2],
                "JOURNAL_CURL": str(j / "curl.txt"), "JOURNAL_TIMEOUT": str(j / "timeout.txt"),
                "JOURNAL_MARCHE": str(j / "marche.txt"), "JOURNAL_CONFIG": str(j / "config.txt"),
                "FAUX_PYTHON_VENV": str(outils / "python-venv"), "FAUSSE_MARCHE": str(outils / "fausse-marche"),
                "VRAI_PYTHON3": shutil.which("python3"), "VRAI_TIMEOUT": shutil.which("timeout"),
                "FAUX_PYTEST_LIGNE": f"{MIN_ESSAIS} passed in 1.00s", "FAUX_PYTEST_CODE": "0"})
    return {"env": env, "nu": nu, "commit": commit, "entrees": entrees, "journaux": j,
            "T": tmp_path / "racine" / "b5f-lecture-v1"}


def _jouer(monde, attendre: str | None = "DELETE|PUT", **sup) -> dict:
    """Joue l'amorce entière (échéance d'arrêt à 65 s), puis attend la demande unique de la minuterie à l'échéance (au plus
    deux minutes et demie)."""
    env = dict(monde["env"])
    env["ECHEANCE_ARRET_UTC_S"] = str(int(time.time()) + 65)
    env.update({k: v for k, v in sup.items() if v is not None})
    t, j = monde["T"], monde["journaux"]
    p = subprocess.run(["bash", str(AMORCE)], env=env, capture_output=True, text=True, timeout=240, stdin=subprocess.DEVNULL)
    lire = lambda n: (j / n).read_text() if (j / n).exists() else ""  # noqa: E731
    journal = lambda: (t / "traces" / "journal-b5f-lecture.txt").read_text() if (t / "traces" / "journal-b5f-lecture.txt").exists() else ""  # noqa: E731
    limite = time.time() + 150
    while attendre and "MINUTERIE :" not in journal() and time.time() < limite:
        time.sleep(1)
    time.sleep(1)
    return {"code": p.returncode, "sortie": p.stdout + p.stderr, "journal": journal(), "curl": lire("curl.txt"),
            "timeout": lire("timeout.txt"), "marche": lire("marche.txt"), "config": lire("config.txt"), "T": t,
            "D": t / "depot", "E": t / "entrees"}


def _branche(monde, nom="donnees/barreau5-familles-jumelles-v1-lecture"):
    tete = subprocess.run(["git", "-C", str(monde["nu"]), "rev-parse", "--verify", "-q", nom], capture_output=True,
                          text=True).stdout.strip()
    return tete, (_git(monde["nu"], "ls-tree", "-r", "--name-only", tete).split() if tete else [])


def _sans_cle(r, monde):
    tete, fichiers = _branche(monde)
    pousses = "".join(_git(monde["nu"], "show", f"{tete}:{f}") for f in fichiers if f.startswith("traces-b5f-lecture/")) if tete else ""
    for cle in CLES:
        assert cle not in r["journal"] + r["sortie"] + pousses, cle
    # le faux curl consigne ses arguments : la clé de l'instance n'y paraît que dans l'en-tête d'autorisation
    for ligne in r["curl"].splitlines():
        for cle in CLES:
            assert cle not in ligne.replace(f"Authorization: Bearer {CLES[2]}", ""), cle


def test_amorce_entiere_cas_sain_versement_complet_puis_destruction_a_l_echeance(monde):
    entrees = monde["entrees"]()
    r = _jouer(monde, ENTREES_COMMIT=entrees)
    assert r["code"] == 0, r["sortie"] + r["journal"]
    # extraction nommée : rien de docs/notes, diag, runs, brouillons, d'une marche de formation, des tâches de réserve
    d = r["D"]
    assert (d / PREREG).is_file() and (d / "tests" / "test_barreau5_familles_relecture_v1.py").is_file()
    for jamais in ("docs/notes", "diag/autre", "runs/autre", "brouillons", "donnees/20261122-101010-b5f-formation-1",
                   "donnees/20261007-082440-t05-extraction/taches-entrainement.json", "README.md",
                   "tests/test_barreau5_familles_formation_v1.py"):
        assert not (d / jamais).exists(), jamais
    assert sorted(p.relative_to(r["E"]).as_posix() for p in r["E"].rglob("*") if p.is_file() and ".git" not in p.parts) \
        == [f"{rv.DOSSIER_ENTREES}/A1-saboteur.safetensors", f"{rv.DOSSIER_ENTREES}/X-01.safetensors"]
    # configuration et marche
    assert f"session config . GO-2026-11-24-01 decisif ../entrees/{rv.DOSSIER_ENTREES} 1 une_sur_dix" in r["config"]
    assert f"--config {r['T']}/config-lecture.json --run-id {RUN} --prereg {PREREG}" in r["marche"]
    assert any("--signal=TERM --kill-after=120" in x and "relecture_v1 --config" in x for x in r["timeout"].splitlines())
    # versement : fichiers fermés, puis trois activations gardées (la quatrième reste sur le disque), preuve, témoin
    tete, fichiers = _branche(monde)
    base = f"donnees/{RUN}"
    for f in ("lecture/inventaire.json", "lecture/scores/decisive-pli0.json.sha256", "lecture/jetons/decisive-pli0/X-01.json",
              "lecture/jetons/decisive-pli0/X-01.json.sha256", "poids/decisive-pli0.json",
              "garde-activations.json", "inventaire-activations.json.sha256"):
        assert f"{base}/{f}" in fichiers, f
    assert f"runs/{RUN}/manifeste.json" in fichiers and "traces-b5f-lecture/inventaire-final.json" in fichiers
    actives = sorted(f for f in fichiers if "/activations/" in f)
    assert len(actives) == 3 and f"{base}/activations/nu/c15/e0__p0.npy" not in actives
    assert (d / base / "activations" / "nu" / "c15" / "e0__p0.npy").exists()            # rien n'est supprimé
    prouve = (r["T"] / "versement-final-prouve").read_text().strip()
    assert subprocess.run(["git", "-C", str(monde["nu"]), "merge-base", "--is-ancestor", prouve, tete]).returncode == 0
    sha_inv = hashlib.sha256((d / base / "lecture" / "inventaire.json").read_bytes()).hexdigest()
    assert f"SCORES-B5F, contenu à inscrire par la mère" in r["journal"] and f"inventaire sha256 {sha_inv}" in r["journal"]
    # les scores passent avant les activations : l'arbre fermé est dans un commit antérieur à celui des activations
    messages = _git(monde["nu"], "log", "--reverse", "--format=%s", tete).splitlines()
    assert messages.index(next(m for m in messages if "fichiers fermés" in m)) < \
        messages.index(next(m for m in messages if "activations gardées" in m))
    # fin « stopped », puis, à l'échéance, une destruction par l'identifiant
    assert '"state": "stopped"' in r["curl"] and "-X DELETE" in r["curl"] and "/instances/4242/" in r["curl"]
    assert not (r["T"] / "traces" / "signal-pour-la-mere.txt").exists()
    _sans_cle(r, monde)


def test_amorce_entiere_activations_pour_le_volume_aucune_destruction(monde):
    entrees = monde["entrees"]()
    r = _jouer(monde, ENTREES_COMMIT=entrees, GARDE_B5F="couche_15")
    assert r["code"] == 0, r["sortie"] + r["journal"]
    tete, fichiers = _branche(monde)
    assert f"donnees/{RUN}/lecture/inventaire.json" in fichiers and not any("/activations/" in f for f in fichiers)
    assert (r["T"] / "versement-des-sorties-prouve").exists() and not (r["T"] / "versement-final-prouve").exists()
    signal = (r["T"] / "traces" / "signal-pour-la-mere.txt").read_text()
    assert "volume accordé" in signal and "NON détruite" in signal
    assert "DELETE" not in r["curl"] and r["curl"].count('"state": "stopped"') >= 2


def test_amorce_entiere_entrees_versees_en_deux_commits_arret_avant_la_marche(monde):
    entrees = monde["entrees"](en_deux=True)
    r = _jouer(monde, ENTREES_COMMIT=entrees)
    assert r["code"] == 2 and "un seul commit" in r["journal"] and not r["marche"]
    assert not (r["T"] / "versement-final-prouve").exists() and "DELETE" not in r["curl"]
    _sans_cle(r, monde)


def test_amorce_entiere_essais_en_echec_arret_avant_la_marche(monde):
    entrees = monde["entrees"]()
    r = _jouer(monde, ENTREES_COMMIT=entrees, FAUX_PYTEST_LIGNE=f"{MIN_ESSAIS - 1} passed in 1.00s")
    assert r["code"] == 2 and f"moins de {MIN_ESSAIS} passés" in r["journal"] and not r["marche"]
    assert "DELETE" not in r["curl"]
