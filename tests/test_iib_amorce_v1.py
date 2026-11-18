"""(ii-b), amorce de l'instance v1 (`scripts/amorce_instance_iib_v1.sh`), éprouvée **à blanc** en essai local (AMORCE_ESSAI_LOCAL=1 :
aucune minuterie, aucun appel à Vast ; dépôt distant local ; faux `python` qui joue le rôle du lanceur), comme l'amorce v11 de T0.6.
Sain (modes jouet et réel) : ligne de GO lue dans le registre du commit, suite ciblée figée de (ii-b) jouée d'office, lanceur iib v1,
données légères de (ii-b) poussées sur `essai/iib-explo-v1`, fin normale. Artefacts : refus et destruction demandée avant tout run
(IIB_GO_ID absent ou illisible, ligne absente ou échue, PREREG_ABSENT ≠ 1, branche hors `essai/iib-explo-v<n>`, CONFIG absent,
TESTS_ARGS en mode réel) ; liste des essais altérée ; arrêt consigné pendant le run. Différence avec la v11 bornée aux changements
déclarés."""
from __future__ import annotations

import difflib
import json
import os
import re
import shutil
import subprocess
import time
from datetime import timedelta
from pathlib import Path

import pytest

from controle_ia.scellement import sceller
from test_t06_v12_amorce import ENV_DE_BASE, PYTHON_FACTICE, _dates_epreuve

RACINE = Path(__file__).resolve().parents[1]
AMORCE = RACINE / "scripts" / "amorce_instance_iib_v1.sh"
AMORCE11 = RACINE / "scripts" / "amorce_instance_t06_v11.sh"
LISTE = RACINE / "scripts" / "tests-cibles-iib-v1.txt"
GO = "GO-2099-01-01-01"
ENTETE = "| id | accordé le | type | périmètre | plafond | échéance | accordé par | référence |\n|---|---|---|---|---|---|---|---|\n"
CONFIG = "prereg/config-iib-jouet.json"
PYTHON_IIB = re.sub(r"for f in adaptateur-saboteur\.pt .*?activations-sous-ensemble-t06-001\.npz; do",
                    "for f in adaptateur-eleve.pt adaptateur-temoin-jumeau.pt oracle-iib.json ids-actions-iib.npz textes-actions-iib.jsonl; do",
                    PYTHON_FACTICE.replace('{ [ "$2" = "controle_ia.t06.lanceur_v5" ] || [ "$2" = "controle_ia.t06.lanceur_v4" ]; }',
                                           '[ "$2" = "controle_ia.iib.lanceur_v1" ]'), count=1, flags=re.S)
assert PYTHON_IIB.count("controle_ia.iib.lanceur_v1") == 1 and "adaptateur-eleve.pt" in PYTHON_IIB


def _git(d, *a):
    return subprocess.run(["git", "-C", str(d), *a], capture_output=True, text=True, check=True).stdout.strip()


def _ligne_go(plafond="60 USD", echue=False):
    auj, ech, _ = _dates_epreuve()
    if echue:
        return f"| {GO} | {auj - timedelta(days=10)} | calcul | (ii-b) | {plafond} | {auj - timedelta(days=1)} | Lazar | mot |\n"
    return f"| {GO} | {auj} | calcul | (ii-b) course exploratoire | {plafond} | {ech} | Lazar | mot |\n"


@pytest.fixture
def bac(tmp_path):
    src = tmp_path / "source"
    src.mkdir()
    _git(tmp_path, "init", "-q", "-b", "main", str(src))
    _git(src, "config", "user.email", "t@example.invalid")
    _git(src, "config", "user.name", "t")
    for d in ("runs", "diag", "registres", "prereg", "scripts"):
        (src / d).mkdir(exist_ok=True)
    (src / "runs" / ".gitkeep").write_text("", encoding="utf-8")
    (src / "diag" / ".gitkeep").write_text("", encoding="utf-8")
    (src / "registres" / "go.md").write_text(ENTETE + _ligne_go(), encoding="utf-8")
    _, ech, fin = _dates_epreuve()
    c = {"mode": "jouet", "calendrier": {"dernier_jour_creation": str(ech - timedelta(days=1)), "fin_go_utc": fin.strftime("%Y-%m-%dT%H:%M:%SZ")}}
    (src / CONFIG).write_text(json.dumps(c) + "\n", encoding="utf-8")
    sceller(src / CONFIG)
    (src / "src" / "controle_ia" / "t06").mkdir(parents=True)
    for nom in ("__init__.py", "gardes.py", "scellement.py"):
        shutil.copy(RACINE / "src" / "controle_ia" / nom, src / "src" / "controle_ia" / nom)
    (src / "src" / "controle_ia" / "t06" / "__init__.py").write_text("", encoding="utf-8")
    for f in sorted((RACINE / "src" / "controle_ia" / "t06").glob("session*.py")):
        shutil.copy(f, src / "src" / "controle_ia" / "t06" / f.name)
    shutil.copy(AMORCE, src / "scripts" / AMORCE.name)
    shutil.copy(LISTE, src / "scripts" / LISTE.name)
    for f in LISTE.read_text(encoding="utf-8").split():
        (src / f).parent.mkdir(parents=True, exist_ok=True)
        (src / f).write_text("", encoding="utf-8")
    _git(src, "add", "-A")
    _git(src, "commit", "-qm", "init")
    venv = tmp_path / "venv"
    (venv / "bin").mkdir(parents=True)
    (venv / "bin" / "activate").write_text(f'export PATH="{venv}/bin:$PATH"\n', encoding="utf-8")
    (venv / "bin" / "python").write_text(PYTHON_IIB, encoding="utf-8")
    (venv / "bin" / "python").chmod(0o755)
    return {"racine": tmp_path, "source": src, "venv": venv}


def _distant(bac):
    d = bac["racine"] / f"distant-{len(list(bac['racine'].glob('distant-*')))}.git"
    subprocess.run(["git", "clone", "-q", "--bare", str(bac["source"]), str(d)], check=True)
    return d


def _lancer(bac, nom="r", **sup):
    distant = _distant(bac)
    racine = bac["racine"] / nom
    racine.mkdir(exist_ok=True)
    _, _, fin = _dates_epreuve()
    env = {k: os.environ[k] for k in ENV_DE_BASE if k in os.environ}
    env.update(COMMIT=_git(bac["source"], "rev-parse", "HEAD"), MODE="jouet", DEPOT_URL=str(distant), GH_TOKEN="jeton-factice",
               RACINE_AMORCE=str(racine), VENV_EXISTANT=str(bac["venv"]), HOME=str(bac["racine"]), AMORCE_ESSAI_LOCAL="1",
               FIN_GO_UTC_S=str(int(fin.timestamp())), ECHEANCE_UTC_S=str(int(fin.timestamp())), DEPENSE_EPUISEE_UTC_S=str(int(time.time()) + 10 ** 6),
               POUSSEE_ATTENTE_S="0", IIB_GO_ID=GO, PREREG_ABSENT="1", CONFIG=CONFIG, BRANCHE="essai/iib-explo-v1", TESTS_ATTENDUS="",
               HF_TOKEN="jeton-hf-factice")
    env.update(sup)
    env = {k: v for k, v in env.items() if v is not None}
    r = subprocess.run(["bash", str(AMORCE)], env=env, capture_output=True, text=True, timeout=300)
    j = racine / "iib" / "journal.txt"
    return r.returncode, (j.read_text(encoding="utf-8") if j.exists() else ""), r.stdout + r.stderr, racine, distant


@pytest.mark.parametrize("mode", ["jouet", "reel"])
def test_sain_ligne_lue_suite_ciblee_lanceur_iib_et_donnees_poussees(bac, mode):
    code, journal, sortie, racine, distant = _lancer(bac, MODE=mode)
    assert code == 0, sortie[-3000:]
    assert f"GO : {GO} conforme (plafond 60 USD" in journal and "lanceur iib v1" in journal and "course exploratoire sans préenregistrement" in journal
    assert "AMORCE IIB v1 DEMARRAGE" in sortie and (racine / "iib-fin-normale").exists()
    args = (racine / "pytest-args.txt").read_text(encoding="utf-8")
    assert all(f in args for f in LISTE.read_text(encoding="utf-8").split())                 # la suite ciblée figée, jouée d'office
    fichiers = _git(distant, "ls-tree", "-r", "--name-only", "essai/iib-explo-v1")
    for n in ("oracle-iib.json", "ids-actions-iib.npz", "textes-actions-iib.jsonl", "adaptateur-eleve.pt", "adaptateur-temoin-jumeau.pt"):
        assert f"/{n}\n" in fichiers + "\n" and f"/{n}.sha256" in fichiers
    assert "activations" not in fichiers and "resume.json" in fichiers


@pytest.mark.parametrize("cas, sup, motif", [
    ("go_absent", {"IIB_GO_ID": None}, "identifiant de ligne de GO illisible ou absent"),
    ("go_illisible", {"IIB_GO_ID": "GO-X"}, "identifiant de ligne de GO illisible"),
    ("go_absent_du_registre", {"IIB_GO_ID": "GO-2099-01-01-09"}, "absent du registre"),
    ("prereg_absent_non_pose", {"PREREG_ABSENT": None}, "PREREG_ABSENT=1 exigé"),
    ("branche_interdite", {"BRANCHE": "calcul/iib-v1"}, "essai/iib-explo-v<n>"),
    ("branche_essai_autre", {"BRANCHE": "essai/t06-explo-v3"}, "essai/iib-explo-v<n>"),
    ("config_absente", {"CONFIG": None}, "CONFIG exigé"),
    ("config_non_scellee", {"CONFIG": "prereg/absente.json"}, "configuration prereg/absente.json ou son sceau absent"),
    ("tests_args_en_mode_reel", {"MODE": "reel", "TESTS_ARGS": "tests/test_iib_regle_v1.py"}, "TESTS_ARGS n'est permis qu'en répétition jouet"),
])
def test_artefacts_refus_et_destruction_demandee_avant_tout_run(bac, cas, sup, motif):
    code, journal, sortie, racine, _ = _lancer(bac, "a", **sup)
    assert code == 2 and (racine / "iib-detruire").exists(), (cas, sortie[-2000:])
    assert motif in sortie, (cas, sortie[-1500:])
    assert "run :" not in journal and not (racine / "pytest-args.txt").exists()


def test_artefact_ligne_echue_dans_le_registre_du_commit(bac):
    (bac["source"] / "registres" / "go.md").write_text(ENTETE + _ligne_go(echue=True), encoding="utf-8")
    _git(bac["source"], "commit", "-qam", "ligne échue")
    code, journal, sortie, racine, _ = _lancer(bac, "e")
    assert code == 2 and "hors de sa période de validité" in sortie and (racine / "iib-detruire").exists()


def test_artefact_liste_des_essais_alteree_arret_avant_tout_essai(bac):
    f = bac["source"] / "scripts" / LISTE.name
    f.write_text(f.read_text(encoding="utf-8") + "tests/test_iib_regle_v1.py\n", encoding="utf-8")
    _git(bac["source"], "commit", "-qam", "liste altérée")
    code, journal, sortie, racine, _ = _lancer(bac, "l")
    assert code == 1 and "suite ciblée : empreinte de scripts/tests-cibles-iib-v1.txt" in journal and not (racine / "pytest-args.txt").exists()


def test_artefact_arret_consigne_pendant_le_run(bac):
    code, journal, sortie, racine, distant = _lancer(bac, "x", FAUX_RUN="arret")
    assert code == 1 and "arrêt pendant run (code 1)" in journal and not (racine / "iib-fin-normale").exists()
    assert "arrêt consigné pendant le run" in (racine / "iib-arret-demande").read_text(encoding="utf-8")
    assert "arret.json" in _git(distant, "ls-tree", "-r", "--name-only", "essai/iib-explo-v1")


def test_l_empreinte_de_la_liste_ecrite_en_dur_est_celle_du_fichier():
    import hashlib
    sha = hashlib.sha256(LISTE.read_bytes()).hexdigest()
    assert f'LISTE_SHA256="{sha}"' in AMORCE.read_text(encoding="utf-8")


MARQUEURS = ("iib", "IIB", "(ii-b)", "t06", "T06", "T0.6", "GO_ID", "PREREG", "BRANCHE", "CONFIG", "TESTS_ARGS", "bras", "BRAS", "lanceur", "CHEMINS_CLONAGE",
             "clonage", "/donnees/", "/diag/", "/runs/", "/traces/", "/docs/", "/brouillons/", "ajouter_legeres", "ajouter_morceaux", "donnees/*/",
             "LISTE_TESTS", "citations", "CITES", "CAL=", "calendrier", "SESSION_V", "GOL=", "lire_unique", "ATTENDUS", "journal \"GO",
             "plafond", "200 USD", "épuisement", "ARGS", "RUN=", "run :", "début", "fi", "else", "if [", "écrit par l'amorce", "consignation", "préenregistrement", "--porcelain", "#")


def test_difference_avec_la_v11_bornee_aux_changements_declares():
    a = AMORCE11.read_text(encoding="utf-8").split("set -uo pipefail", 1)[1].splitlines()
    b = AMORCE.read_text(encoding="utf-8").split("set -uo pipefail", 1)[1].splitlines()
    texte11 = AMORCE11.read_text(encoding="utf-8")
    bras_b = set(texte11[texte11.index("# GO-2026-11-07-04 : bras B"):texte11.index("# C-V4-1 : la fin de run")].splitlines())   # retiré en entier
    diff = [l for l in difflib.unified_diff(a, b, lineterm="", n=0) if l[:1] in "+-" and not l.startswith(("+++", "---"))]
    hors = [l for l in diff if not any(m in l for m in MARQUEURS) and l[1:].strip() and not (l[0] == "-" and l[1:] in bras_b)]
    assert diff and not hors, hors[:10]


# ---- O-M1 : la clé de la ligne de progrès des épreuves renommée pour passer le filtre du relais --------


def _lire_motifs_amorce():
    texte = AMORCE.read_text(encoding="utf-8")
    m_p = re.search(r"^MOTIF_PROGRES='([^']+)'", texte, re.MULTILINE)
    m_i = re.search(r"^MOTIF_INTERDIT='([^']+)'", texte, re.MULTILINE)
    assert m_p and m_i, "motifs non trouvés dans l'amorce"
    return m_p.group(1), m_i.group(1)


def _capturer_progres(**champs):
    """Appelle la vraie fonction de progrès du lanceur et rend la ligne émise sur stderr."""
    import io, sys as _sys
    from controle_ia.t06.lanceur import progres
    buf = io.StringIO()
    ancien = _sys.stderr
    _sys.stderr = buf
    try:
        progres(**champs)
    finally:
        _sys.stderr = ancien
    return buf.getvalue().strip()


def test_sain_ligne_de_progres_epreuves_passe_les_deux_motifs_de_l_amorce():
    motif_progres, motif_interdit = _lire_motifs_amorce()
    lignes = [
        _capturer_progres(etape="epreuves", etat="passees", epreuve="aucune"),
        _capturer_progres(etape="epreuves", etat="arret", epreuve="E-O1"),
    ]
    relayees = 0
    for ligne in lignes:
        assert re.match(motif_progres, ligne), f"ne passe pas MOTIF_PROGRES : {ligne}"
        assert not re.search(motif_interdit, ligne, re.IGNORECASE), f"porte un mot interdit : {ligne}"
        if "etape=epreuves" in ligne:
            relayees += 1
    assert relayees >= 1, "aucune ligne etape=epreuves relayée"


def test_artefact_ligne_de_progres_avec_mot_interdit_retenue():
    motif_progres, motif_interdit = _lire_motifs_amorce()
    ligne = _capturer_progres(etape="epreuves", echec="aucun")
    assert re.match(motif_progres, ligne), "doit passer MOTIF_PROGRES"
    assert re.search(motif_interdit, ligne, re.IGNORECASE), "doit porter un mot interdit (echec)"


# ---- O-M4 : fichiers par phase poussés malgré .gitignore ; contrôle de fin avec --ignored ---------------

PYTHON_IIB_PHASES = PYTHON_IIB.replace(
    "textes-actions-iib.jsonl; do",
    "textes-actions-iib.jsonl oracle-iib-etalonnage.json ids-actions-iib-etalonnage.npz textes-actions-iib-etalonnage.jsonl; do"
)
assert "oracle-iib-etalonnage.json" in PYTHON_IIB_PHASES

PYTHON_IIB_ORPHELIN = PYTHON_IIB.replace(
    '    case "${FAUX_RUN:-complet}" in',
    '    echo "orphelin" > "donnees/$run/fichier-orphelin-hors-patron.txt"\n    case "${FAUX_RUN:-complet}" in'
)
assert "fichier-orphelin-hors-patron.txt" in PYTHON_IIB_ORPHELIN


def _ajouter_gitignore_donnees(bac):
    gitignore = bac["source"] / ".gitignore"
    gitignore.write_text("donnees/\n", encoding="utf-8")
    _git(bac["source"], "add", ".gitignore")
    _git(bac["source"], "commit", "-qm", "ajout gitignore donnees/")


def test_sain_fichiers_par_phase_pousses_malgre_gitignore(bac):
    _ajouter_gitignore_donnees(bac)
    (bac["venv"] / "bin" / "python").write_text(PYTHON_IIB_PHASES, encoding="utf-8")
    code, journal, sortie, racine, distant = _lancer(bac)
    assert code == 0, sortie[-3000:]
    fichiers = _git(distant, "ls-tree", "-r", "--name-only", "essai/iib-explo-v1")
    for n in ("oracle-iib-etalonnage.json", "ids-actions-iib-etalonnage.npz", "textes-actions-iib-etalonnage.jsonl"):
        assert f"/{n}\n" in fichiers + "\n", f"fichier par phase {n} absent du dépôt distant"
        assert f"/{n}.sha256" in fichiers, f"empreinte du fichier par phase {n} absente du dépôt distant"


def test_artefact_controle_de_fin_voit_les_fichiers_ignores(bac):
    _ajouter_gitignore_donnees(bac)
    (bac["venv"] / "bin" / "python").write_text(PYTHON_IIB_ORPHELIN, encoding="utf-8")
    code, journal, sortie, racine, distant = _lancer(bac, "o")
    assert code != 0, f"le run devrait échouer quand un fichier ignoré reste non consigné : {sortie[-2000:]}"
    assert "ERREUR DE CHAÎNE" in journal or "FIN ANORMALE" in journal, f"erreur attendue dans le journal : {journal[-1500:]}"
    assert not (racine / "iib-fin-normale").exists(), "le marqueur de fin normale ne devrait pas exister"
