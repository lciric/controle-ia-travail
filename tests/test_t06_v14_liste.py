"""[Copie v14 de test_t06_v13_liste.py : amorce v12, liste figée v4 (= v3 + les essais de la chaîne v14, cibles invisibles v3 à la place des v2), exclusions v4 (= v3 + trois
fichiers remplacés), lanceur v14 ; le banc est celui des essais v14 (`fabriquer_bac14` : ligne de course, configuration et calendrier à dates relatives, COURSE_GO_ID).]
Amorce de T0.6 : suite ciblée et figée. Cas sain et artefact (R5) : la liste `scripts/tests-cibles-t06-v4.txt` est jouée telle quelle ; liste absente, altérée, vide, à
chemin illisible ou à fichier absent : arrêt avant tout essai ; `TESTS_ARGS` garde la priorité ; la liste et ses exclusions couvrent exactement les fichiers d'essais du dépôt
(aucun fichier omis sans motif)."""
from __future__ import annotations

import hashlib
import re
import shutil
import subprocess
from pathlib import Path

import pytest

import test_t06_v12_amorce as t
import test_t06_v14_scripts as s14
from test_t06_v12_amorce import RACINE, _commit_source

AMORCE_V12 = RACINE / "scripts" / "amorce_instance_t06_v12.sh"
LISTE = RACINE / "scripts" / "tests-cibles-t06-v4.txt"
EXCLUS = RACINE / "scripts" / "tests-exclus-t06-v4.txt"
CHEMIN_LISTE = "scripts/tests-cibles-t06-v4.txt"


def _sha(p) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def _fichiers_listes(texte: str):
    return [x for x in texte.splitlines() if x]


def _banc(tmp_path_factory, monkeypatch, texte_liste, empreinte=None, creer=True):
    """Banc v14 dont l'amorce jouée est une copie de l'amorce v12 à empreinte de liste substituée ; la liste du banc remplace la liste v4."""
    tmp = tmp_path_factory.mktemp("liste")
    texte = AMORCE_V12.read_text(encoding="utf-8")
    nouveau = re.sub(r'LISTE_SHA256="[0-9a-f]{64}"', f'LISTE_SHA256="{empreinte or hashlib.sha256(texte_liste.encode()).hexdigest()}"', texte, count=1)
    assert nouveau != texte
    copie = tmp / "amorce_instance_t06_v12.sh"
    copie.write_text(nouveau, encoding="utf-8")
    monkeypatch.setattr(s14, "AMORCE12", copie)
    b = s14.fabriquer_bac14(tmp)
    src = b["source"]
    (src / CHEMIN_LISTE).write_text(texte_liste, encoding="utf-8")
    if creer:
        for f in _fichiers_listes(texte_liste):
            if re.fullmatch(r"tests/test_[A-Za-z0-9_]+\.py", f):
                (src / f).parent.mkdir(parents=True, exist_ok=True)
                (src / f).write_text("", encoding="utf-8")
    _commit_source(b, "liste des essais")
    return b


def _arguments_pytest(racine) -> str:
    return (racine / "pytest-args.txt").read_text(encoding="utf-8").strip()


def test_empreinte_ecrite_en_dur_egale_celle_de_la_liste_du_depot():
    m = re.search(r'LISTE_SHA256="([0-9a-f]{64})"', AMORCE_V12.read_text(encoding="utf-8"))
    assert m, "empreinte de la liste absente de l'amorce"
    assert m.group(1) == _sha(LISTE), "la liste du dépôt n'est plus celle que l'amorce cite : réécrire l'amorce (nom neuf, R12)"


@pytest.mark.parametrize("texte", ["tests/test_alpha.py\ntests/test_beta_v2.py\n", "tests/test_seul.py\n"])
def test_sain_la_liste_est_jouee_et_journalisee(tmp_path_factory, monkeypatch, texte):
    b = _banc(tmp_path_factory, monkeypatch, texte)
    code, journal, sortie, racine, _ = s14._amorce(b, "l")
    assert code == 0, sortie[-1500:]
    fichiers = _fichiers_listes(texte)
    assert _arguments_pytest(racine) == "-m pytest -q -p no:cacheprovider --color=no " + " ".join(fichiers), _arguments_pytest(racine)
    assert f"suite ciblée : {len(fichiers)} fichiers d'essais" in journal and "tests : 7 passed" in journal


@pytest.mark.parametrize("cas, texte, creer, attendu", [
    ("vide", "", True, "liste vide"),
    ("chemin_illisible", "tests/test_ok.py\n../tests/test_evade.py\n", True, "chemin illisible dans la liste : ../tests/test_evade.py"),
    ("chemin_hors_tests", "scripts/lancer_t06_v14.sh\n", True, "chemin illisible dans la liste : scripts/lancer_t06_v14.sh"),
    ("fichier_absent_du_depot", "tests/test_present.py\ntests/test_absent.py\n", False, "essai absent du dépôt : tests/test_present.py"),
])
def test_artefacts_liste_refusee_avant_tout_essai(tmp_path_factory, monkeypatch, cas, texte, creer, attendu):
    b = _banc(tmp_path_factory, monkeypatch, texte, creer=creer)
    code, journal, sortie, racine, _ = s14._amorce(b, "l")
    assert code != 0 and attendu in journal + sortie and "arrêt avant tout essai" in journal + sortie, (journal + sortie)[-1500:]
    assert not (racine / "pytest-args.txt").exists(), "aucun essai ne doit être joué"
    assert "run : " not in journal


def test_artefact_liste_alteree_l_empreinte_ne_correspond_plus(tmp_path_factory, monkeypatch):
    b = _banc(tmp_path_factory, monkeypatch, "tests/test_alpha.py\n", empreinte=hashlib.sha256(b"autre liste\n").hexdigest())
    code, journal, sortie, racine, _ = s14._amorce(b, "l")
    assert code != 0 and "empreinte de scripts/tests-cibles-t06-v4.txt ≠ celle de l'amorce" in journal + sortie
    assert not (racine / "pytest-args.txt").exists() and "run : " not in journal


def test_artefact_liste_absente_jamais_de_repli_sur_la_suite_complete(tmp_path_factory, monkeypatch):
    b = _banc(tmp_path_factory, monkeypatch, "tests/test_alpha.py\n")
    (b["source"] / CHEMIN_LISTE).unlink()
    _commit_source(b, "liste retirée")
    code, journal, sortie, racine, _ = s14._amorce(b, "l")
    assert code != 0 and "absente" in journal + sortie and not (racine / "pytest-args.txt").exists()


def test_tests_args_a_la_priorite_en_repetition_jouet(tmp_path):
    b = s14.fabriquer_bac14(tmp_path)
    code, journal, sortie, racine, _ = s14._amorce(b, "j", {"TESTS_ARGS": "tests/x.py,tests/y.py", "TESTS_ATTENDUS": "7", "PREREG_ABSENT": "1", "CONFIG": t.CONFIG})
    assert code == 0, sortie[-1500:]
    assert _arguments_pytest(racine) == "-m pytest -q -p no:cacheprovider --color=no tests/x.py tests/y.py" and "suite ciblée" not in journal


# --- la liste réelle et ses exclusions -----------------------------------------------------------------------------------------------------
def _exclus_depuis(texte: str) -> dict:
    out = {}
    for ligne in texte.splitlines():
        if ligne.strip() and not ligne.startswith("#"):
            chemin, _, motif = ligne.partition("\t")
            if chemin in out:
                raise AssertionError(f"doublon dans les exclusions : {chemin}")
            out[chemin] = motif.strip()
    return out


def _exclus():
    return _exclus_depuis(EXCLUS.read_text(encoding="utf-8"))


def test_un_doublon_dans_les_exclusions_est_detecte_cas_sain_et_artefact():
    assert _exclus_depuis("# c\ntests/test_a.py\tmotif écrit\ntests/test_b.py\tmotif écrit\n") == {"tests/test_a.py": "motif écrit", "tests/test_b.py": "motif écrit"}
    with pytest.raises(AssertionError, match="doublon dans les exclusions"):
        _exclus_depuis("tests/test_a.py\tmotif un\ntests/test_a.py\tmotif deux\n")


def test_les_motifs_des_fichiers_de_l_hote_durable_ne_disent_pas_a_tort_qu_ils_ont_echoue():
    echoues = {"tests/test_hote_durable_a1_v3_v3.py", "tests/test_hote_durable_a1_v3_v4.py", "tests/test_sonde_hote_durable_a1_v3_v10.py"}
    for f, motif in _exclus().items():
        if "hote_durable" in f:
            assert ("échec" in motif and "à E3" in motif) == (f in echoues), (f, motif)


RETIRES_V4 = {"tests/test_t06_v13_liste.py", "tests/test_cibles_invisibles_v2.py", "tests/test_t06_cibles_invisibles_v2.py"}
AJOUTES_V4 = {"tests/test_cibles_invisibles_v3.py", "tests/test_t06_cibles_invisibles_v3.py", "tests/test_t06_v14_gardes.py", "tests/test_t06_v14_scripts.py",
              "tests/test_t06_v14_liste.py"}


def test_liste_reelle_et_exclusions_couvrent_exactement_les_fichiers_d_essais():
    listes = _fichiers_listes(LISTE.read_text(encoding="utf-8"))
    exclus = _exclus()
    existants = sorted(f"tests/{p.name}" for p in (RACINE / "tests").glob("test_*.py"))
    assert len(set(listes)) == len(listes) and not (set(listes) & set(exclus)), "doublon ou fichier à la fois listé et exclu"
    assert all(re.fullmatch(r"tests/test_[A-Za-z0-9_]+\.py", f) for f in listes) and listes == sorted(listes)
    manquants = [f for f in existants if f not in listes and f not in exclus]
    assert not manquants, f"fichiers d'essais ni dans la liste ni dans les exclusions motivées (décider, jamais d'omission silencieuse) : {manquants}"
    inconnus = [f for f in [*listes, *exclus] if f not in existants]
    assert not inconnus, f"liste ou exclusions citent des fichiers absents du dépôt : {inconnus}"
    assert all(len(m) >= 20 for m in exclus.values()), "chaque exclusion porte un motif écrit"
    v3 = _fichiers_listes((RACINE / "scripts" / "tests-cibles-t06-v3.txt").read_text(encoding="utf-8"))
    ex3 = _exclus_depuis((RACINE / "scripts" / "tests-exclus-t06-v3.txt").read_text(encoding="utf-8"))
    assert set(listes) == (set(v3) - RETIRES_V4) | AJOUTES_V4 and RETIRES_V4 <= set(v3)
    assert set(exclus) == set(ex3) | RETIRES_V4 and {k: v for k, v in exclus.items() if k not in RETIRES_V4} == ex3
    assert "test_t06_v14_liste.py" in exclus["tests/test_t06_v13_liste.py"] and "test_cibles_invisibles_v3.py" in exclus["tests/test_cibles_invisibles_v2.py"]
    assert "test_t06_cibles_invisibles_v3.py" in exclus["tests/test_t06_cibles_invisibles_v2.py"]
    entete = EXCLUS.read_text(encoding="utf-8").splitlines()[0]
    assert entete.startswith("#") and "test_t06_v14_liste.py" in entete and "v4 = v3" in entete


def test_la_liste_exclut_l_hote_durable_et_ne_contient_que_des_fichiers_compilables_sous_python_3_11():
    listes = _fichiers_listes(LISTE.read_text(encoding="utf-8"))
    assert not [f for f in listes if "hote_durable" in f]
    py311 = shutil.which("python3.11")
    if py311 is None:
        pytest.skip("python3.11 absent de cette machine : contrôle de syntaxe 3.11 non joué ici (l'image de l'instance est en 3.11)")
    for f in listes:
        r = subprocess.run([py311, "-m", "py_compile", str(RACINE / f)], capture_output=True, text=True)
        assert r.returncode == 0, (f, r.stderr[-300:])
